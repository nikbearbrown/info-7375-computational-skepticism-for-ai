#!/usr/bin/env python3
"""Tests for the Workday reader (collect.fetch_workday / post_json, consulting_collect.records) and the Workday boards in targets.json. No network."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import contextlib, datetime as dt, io, json, tempfile, unittest, urllib.request

import collect
import consulting_collect as cc
import consulting_jobs as cj
import federal508_collect
import federal508_jobs as fj

with open(lp.config("keywords.json")) as _f:
    KW = json.load(_f)
with open(lp.config("targets.json")) as _f:
    DOC = json.load(_f)


def item(n, title="Analyst", place="US - TX, Austin", posted="Posted Today"):
    return {"title": title, "externalPath": f"/job/Austin/{title.replace(' ', '-')}_{n}", "locationsText": place, "postedOn": posted, "bulletFields": [str(n)]}


class FakeBoard:
    """A stand-in for post_json: a board of `n` postings that answers a page of `limit` at an offset, and gives `total` on the first page only (as Workday does)."""
    def __init__(self, n, total=None, shift=0):
        self.n, self.total, self.calls, self.shift = n, n if total is None else total, [], shift

    def __call__(self, url, body, timeout=30):
        self.calls.append((url, dict(body)))
        off = body["offset"] - (self.shift if len(self.calls) > 1 else 0)          # `shift`: a posting was added in front while the list was being read
        page = [item(i) for i in range(off, min(off + body["limit"], self.n))]
        return {"total": self.total if body["offset"] == 0 else 0, "jobPostings": page}


class Reader(unittest.TestCase):
    def setUp(self):
        self.real = (collect.post_json, collect.time.sleep)
        self.slept = []
        collect.time.sleep = self.slept.append

    def tearDown(self):
        collect.post_json, collect.time.sleep = self.real

    def test_a_board_id_is_tenant_wdN_slash_site_and_nothing_else(self):
        self.assertEqual(collect.workday_parts("guidehouse.wd1/External"), ("guidehouse.wd1.myworkdayjobs.com", "guidehouse", "External"))
        for bad in ("guidehouse", "guidehouse.wd1", "evil.example.com/External", "guidehouse.wd1/../x", "guidehouse.wd1/a b", ""):
            with self.assertRaises(collect.InputError, msg=bad):
                collect.workday_parts(bad)

    def test_it_pages_by_twenty_asks_with_the_documented_body_pauses_between_pages_and_stops_at_the_total(self):
        collect.post_json = board = FakeBoard(45)
        out = collect.fetch_workday("guidehouse.wd1/External", pause=0.7)
        self.assertEqual((out["total"], len(out["jobs"]), out["pages"], out["complete"]), (45, 45, 3, True))
        self.assertEqual([c[1]["offset"] for c in board.calls], [0, 20, 40])
        self.assertEqual({c[0] for c in board.calls}, {"https://guidehouse.wd1.myworkdayjobs.com/wday/cxs/guidehouse/External/jobs"})
        self.assertEqual(board.calls[0][1], {"appliedFacets": {}, "limit": 20, "offset": 0, "searchText": ""})      # no search text: titles are read, not ad bodies
        self.assertEqual(self.slept, [0.7, 0.7])                                                                     # a pause between pages, none before the first or after the last

    def test_an_empty_board_is_one_request_and_a_short_page_ends_the_read(self):
        collect.post_json = board = FakeBoard(0)
        self.assertEqual(collect.fetch_workday("huron.wd1/huroncareers")["jobs"], [])
        self.assertEqual(len(board.calls), 1)
        collect.post_json = board = FakeBoard(10, total=30)                  # the board says 30 and gives 10, then nothing: not complete, and it says so
        out = collect.fetch_workday("huron.wd1/huroncareers")
        self.assertEqual((len(out["jobs"]), out["complete"]), (10, False))

    def test_a_posting_that_shifts_into_the_next_page_is_counted_once(self):
        collect.post_json = FakeBoard(30, shift=1)
        out = collect.fetch_workday("huron.wd1/huroncareers")
        self.assertEqual(len({j["externalPath"] for j in out["jobs"]}), len(out["jobs"]))

    def test_a_total_of_exactly_2000_is_a_display_cap_so_the_read_is_not_complete(self):
        collect.post_json = FakeBoard(2000)
        out = collect.fetch_workday("huron.wd1/huroncareers")
        self.assertEqual(len(out["jobs"]), 2000)
        self.assertFalse(out["complete"])

    def test_a_reply_with_no_list_is_an_error_not_an_empty_board(self):
        collect.post_json = lambda url, body, timeout=30: {"errorCode": "HTTP_500"}
        with self.assertRaises(ValueError):
            collect.fetch_workday("huron.wd1/huroncareers")

    def test_a_board_that_never_ends_is_stopped(self):
        collect.post_json = lambda url, body, timeout=30: {"total": 10 ** 9, "jobPostings": [item(body["offset"] + i) for i in range(20)]}
        out = collect.fetch_workday("huron.wd1/huroncareers", pause=0)
        self.assertEqual(out["pages"], collect.WORKDAY_MAX_PAGES)
        self.assertFalse(out["complete"])


class Wire(unittest.TestCase):
    """post_json itself, with the opener replaced: the host list, no redirects, JSON only."""
    def test_a_host_outside_the_list_and_a_plain_http_url_are_refused_before_any_request(self):
        for url in ("https://bah.wd1.myworkdayjobs.com/wday/cxs/bah/BAH_Jobs/jobs", "https://caci.wd1.myworkdayjobs.com/wday/cxs/caci/External/jobs",
                    "https://example.com/x", "http://guidehouse.wd1.myworkdayjobs.com/wday/cxs/guidehouse/External/jobs"):
            with self.assertRaises(collect.InputError, msg=url):
                collect.post_json(url, {})

    def _with_opener(self, content_type, body):
        class Resp:
            headers = {"Content-Type": content_type}
            def __enter__(s): return s
            def __exit__(s, *a): return False
            def read(s): return body
        seen = {}

        class Opener:
            def open(s, req, timeout=None):
                seen["req"] = req
                return Resp()
        real = urllib.request.build_opener
        urllib.request.build_opener = lambda *h: Opener()
        try:
            return collect.post_json("https://guidehouse.wd1.myworkdayjobs.com/wday/cxs/guidehouse/External/jobs", {"limit": 20}), seen
        finally:
            urllib.request.build_opener = real

    def test_it_posts_json_says_who_it_is_and_parses_a_json_reply(self):
        out, seen = self._with_opener("application/json;charset=utf-8", b'{"total": 1, "jobPostings": []}')
        self.assertEqual(out["total"], 1)
        req = seen["req"]
        self.assertEqual(req.get_method(), "POST")
        self.assertEqual(json.loads(req.data), {"limit": 20})
        self.assertEqual(req.get_header("User-agent"), "lectern (course project)")
        self.assertEqual((req.get_header("Accept"), req.get_header("Content-type")), ("application/json", "application/json"))

    def test_an_html_reply_is_an_error_and_is_never_parsed(self):
        with self.assertRaises(ValueError):
            self._with_opener("text/html", b"<html>Sign in</html>")


class Records(unittest.TestCase):
    def test_a_workday_list_item_becomes_the_common_record(self):
        j = {"title": "Section 508 Subject Matter Expert", "externalPath": "/job/US---VA-Reston/Section-508-Subject-Matter-Expert_JR1", "locationsText": "US - VA, Reston",
             "postedOn": "Posted 3 Days Ago", "bulletFields": ["JR1"]}
        r = cc.records("workday", "Guidehouse", "guidehouse.wd1/External", {"jobs": [j]})[0]
        self.assertEqual((r["source"], r["company"], r["source_id"], r["title"], r["location_text"]), ("workday", "Guidehouse", "JR1", "Section 508 Subject Matter Expert", "US - VA, Reston"))
        self.assertEqual(r["url"], "https://guidehouse.wd1.myworkdayjobs.com/en-US/External/job/US---VA-Reston/Section-508-Subject-Matter-Expert_JR1")
        self.assertEqual(r["date_posted"], (dt.date.today() - dt.timedelta(days=3)).isoformat())
        self.assertEqual(cj.posting_view(r)["id"], "workday:JR1")

    def test_a_posted_on_phrase_is_a_date_only_when_it_gives_one(self):
        today = dt.date(2026, 11, 1)
        self.assertEqual(cc.workday_posted("Posted Today", today), "2026-11-01")
        self.assertEqual(cc.workday_posted("Posted Yesterday", today), "2026-10-31")
        self.assertEqual(cc.workday_posted("Posted 1 Day Ago", today), "2026-10-31")
        self.assertEqual(cc.workday_posted("Posted 12 Days Ago", today), "2026-10-20")
        for none in ("Posted 30+ Days Ago", "", None, "Posted Sometime"):
            self.assertIsNone(cc.workday_posted(none, today), none)

    def test_a_list_with_no_place_gets_the_city_of_the_postings_own_address_and_a_count_stays_a_count(self):
        self.assertEqual(cc.workday_place({"locationsText": None, "externalPath": "/job/Riyadh/MEA-Lead_R1"}), "Riyadh")
        self.assertEqual(cc.workday_place({"externalPath": "/job/Bogot-DC-Colombia/x_R1"}), "Bogot DC Colombia")
        self.assertEqual(cc.workday_place({"locationsText": "2 Locations", "externalPath": "/job/Chicago/x_R1"}), "2 Locations")
        self.assertEqual(cc.workday_place({}), "")

    def test_the_raw_file_name_has_no_slash(self):
        self.assertEqual(cc.raw_name("workday", "Guidehouse.wd1/External", "2026-11-01"), "workday-guidehouse.wd1_external-2026-11-01.json")
        self.assertEqual(cc.raw_name("greenhouse", "navapbc", "2026-11-01"), "greenhouse-navapbc-2026-11-01.json")


class Judged(unittest.TestCase):
    def test_a_workday_posting_goes_through_the_same_judges_as_any_other(self):
        r = cc.records("workday", "Guidehouse", "guidehouse.wd1/External",
                       {"jobs": [{"title": "Section 508 Subject Matter Expert (Remote)", "externalPath": "/job/US---Remote/x_JR2", "locationsText": "US - Remote", "bulletFields": ["JR2"]}]})[0]
        j = fj.judge_federal508(fj.posting_view(r), KW)
        self.assertEqual(j["decision"], "post")
        self.assertTrue(j["remote"])


class Places(unittest.TestCase):
    """A bare count of places ('3 Locations') hides a 'US - Remote'. Only a posting whose TITLE matches a 508 phrase is looked up, by its own record."""
    RULE = KW["federal508_rule"]

    def setUp(self):
        self.real = collect.workday_places
        self.asked = []

        def fake(slug, path):
            self.asked.append(path)
            return ["US - MD, Rockville", "US - VA, McLean", "US - Remote (Any location)"]
        collect.workday_places = fake

    def tearDown(self):
        collect.workday_places = self.real

    def recs(self, *rows):
        return cc.records("workday", "Guidehouse", "guidehouse.wd1/External",
                          {"jobs": [{"title": t, "externalPath": f"/job/X/{i}_{i}", "locationsText": p, "bulletFields": [str(i)]} for i, (t, p) in enumerate(rows)]})

    def test_only_a_matching_title_with_a_count_for_a_place_is_looked_up_and_then_it_is_remote_to_the_judge(self):
        recs = federal508_collect.name_the_places(self.recs(("Section 508 Subject Matter Expert", "3 Locations"), ("Program Manager", "3 Locations"),
                                                           ("Accessibility Tester", "US - VA, Reston"), ("Section 508 Tester", "1 Location")), "guidehouse.wd1/External", self.RULE, pause=0)
        self.assertEqual(self.asked, ["/job/X/0_0", "/job/X/3_3"])
        self.assertEqual(recs[0]["location_text"], "US - MD, Rockville · US - VA, McLean · US - Remote (Any location)")
        self.assertEqual((recs[1]["location_text"], recs[2]["location_text"]), ("3 Locations", "US - VA, Reston"))
        j = fj.judge_federal508(fj.posting_view(recs[0]), KW)
        self.assertEqual((j["decision"], bool(j["remote"])), ("post", True))
        self.assertEqual(fj.judge_federal508(fj.posting_view(self.recs(("Section 508 Subject Matter Expert", "3 Locations"))[0]), KW)["decision"], "unstated")

    def test_a_failed_lookup_keeps_the_count_and_does_not_stop_the_read(self):
        def boom(slug, path):
            raise OSError("down")
        collect.workday_places = boom
        with contextlib.redirect_stderr(io.StringIO()):
            recs = federal508_collect.name_the_places(self.recs(("Section 508 Tester", "2 Locations")), "guidehouse.wd1/External", self.RULE, pause=0)
        self.assertEqual(recs[0]["location_text"], "2 Locations")

    def test_the_lookup_takes_only_a_posting_address_and_pauses_before_each_request(self):
        collect.workday_places = self.real
        for bad in ("", None, "/job/a", "/other/a/b", "https://evil.example.com/job/a/b", "/job/a/b/c"):
            with self.assertRaises(collect.InputError, msg=bad):
                collect.workday_places("guidehouse.wd1/External", bad)
        real_get, collect.get_json = collect.get_json, lambda url, timeout=30: {"jobPostingInfo": {"location": "A", "additionalLocations": ["B", "US - Remote"]}}
        try:
            self.assertEqual(collect.workday_places("guidehouse.wd1/External", "/job/X/Y_1"), ["A", "B", "US - Remote"])
        finally:
            collect.get_json = real_get
        slept, real_sleep = [], federal508_collect.time.sleep
        federal508_collect.time.sleep = slept.append
        collect.workday_places = lambda slug, path: ["US - Remote"]
        try:
            federal508_collect.name_the_places(self.recs(("Section 508 Tester", "2 Locations")), "guidehouse.wd1/External", self.RULE, pause=0.9)
        finally:
            federal508_collect.time.sleep = real_sleep
        self.assertEqual(slept, [0.9])


class Boards(unittest.TestCase):
    ACTIVE = [(t["section"], t["name"], t["provider"], t[t["section"]]["board"]["slug"]) for t in DOC["targets"]
              if t["section"] in ("federal508", "consulting") and t["status"] == "active" and t["provider"] == "workday"]

    def test_the_workday_boards_that_are_read_are_exactly_the_hosts_on_the_list(self):
        self.assertTrue(self.ACTIVE)
        hosts = {collect.workday_parts(slug)[0] for _, _, _, slug in self.ACTIVE}
        self.assertEqual(hosts, collect.WORKDAY_HOSTS)
        self.assertTrue(hosts <= collect.ALLOWED)

    def test_a_board_whose_robots_file_or_terms_forbid_a_script_is_not_on_the_list_and_is_not_active(self):
        for host in ("bah.wd1", "icf.wd5", "leidos.wd5", "caci.wd1", "cambridgeassociates.wd5", "bakertilly.wd5", "perkins.wd503", "accenture.wd103", "vizient.wd1"):
            self.assertNotIn(f"{host}.myworkdayjobs.com", collect.ALLOWED, host)
        for t in DOC["targets"]:
            if t["id"] in ("federal508-booz-allen-hamilton", "federal508-icf", "federal508-leidos", "federal508-caci", "consulting-booz-allen", "consulting-cambridge-associates",
                           "consulting-baker-tilly", "federal508-perkins-access-perkins-school-for-the-blind", "consulting-accenture", "consulting-kaufman-hall"):
                self.assertNotEqual(t["status"], "active", t["id"])
                self.assertTrue(t["todo"], t["id"])

    def test_an_active_workday_board_carries_the_links_the_reader_calls_and_the_date_of_its_check(self):
        for section, name, provider, slug in self.ACTIVE:
            t = next(x for x in DOC["targets"] if x["section"] == section and x["name"] == name)
            host, tenant, site = collect.workday_parts(slug)
            self.assertEqual([d["label"] for d in t["data"] if d.get("call")], ["API the script calls"], name)
            self.assertIn(f"https://{host}/wday/cxs/{tenant}/{site}/jobs", [d["url"] for d in t["data"]], name)
            self.assertEqual(t[section]["workday_terms_checked"], "2026-11-01", name)
            self.assertIn("robots.txt", t["why"], name)

    def test_the_collectors_read_them_and_keep_the_response_in_a_file_with_no_slash(self):
        boards = {b[2] for b in cc.boards_from_targets(DOC)} | {b[2] for b in federal508_collect.boards_from_targets(DOC)}
        self.assertIn("guidehouse.wd1/External", boards)
        real = (federal508_collect.cc.fetch_list, federal508_collect.PAUSE)
        try:
            def fake(provider, slug):
                if provider == "workday":
                    return {"total": 2, "jobs": [item(1, "Section 508 Tester"), item(2)], "pages": 1, "complete": True}
                return {"jobs": []}
            federal508_collect.cc.fetch_list = fake
            federal508_collect.PAUSE = 0
            with tempfile.TemporaryDirectory() as d, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(federal508_collect.main(["--out", d, "--only", "guidehouse.wd1/External"]), 0)
                names = _os.listdir(_os.path.join(d, "federal508-raw"))
                self.assertEqual(len(names), 1)
                self.assertNotIn("/", names[0])
                with open(_os.path.join(d, [f for f in _os.listdir(d) if f.startswith("federal508-jobs-")][0])) as f:
                    data = json.load(f)
                self.assertEqual(data["sources"][0]["listed_total"], 2)
                self.assertTrue(data["sources"][0]["complete"])
                self.assertEqual({r["source"] for r in data["records"]}, {"workday"})
        finally:
            federal508_collect.cc.fetch_list, federal508_collect.PAUSE = real


if __name__ == "__main__":
    unittest.main()
