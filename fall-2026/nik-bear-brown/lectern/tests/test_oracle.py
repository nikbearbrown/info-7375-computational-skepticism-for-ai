#!/usr/bin/env python3
"""Tests for the Oracle Recruiting Cloud reader (collect.fetch_oracle / oracle_parts, consulting_collect.records / oracle_place) and the Oracle boards in targets.json. No network."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import json, unittest, urllib.request
from urllib.parse import parse_qs, urlparse

import collect
import consulting_collect as cc
import consulting_jobs as cj

with open(lp.config("keywords.json")) as _f:
    KW = json.load(_f)
with open(lp.config("targets.json")) as _f:
    DOC = json.load(_f)


def req(n, title="Associate Consultant", place="Atlanta, GA, United States", posted="2026-11-02", second=None):
    return {"Id": str(n), "Title": title, "PostedDate": posted, "PrimaryLocation": place, "PrimaryLocationCountry": "US", "secondaryLocations": second or []}


def reply(rows, total):
    """What the public list answers: one item holding the page and the total."""
    return {"items": [{"TotalJobsCount": total, "Offset": 0, "Limit": 25, "requisitionList": rows}], "count": 1, "hasMore": False, "limit": 200, "offset": 0}


class FakeSite:
    """A stand-in for get_json: a site of `n` postings that answers a page of the asked `limit` at the asked offset, and gives the total on every page."""
    def __init__(self, n, total=None, shift=0):
        self.n, self.total, self.calls, self.shift = n, n if total is None else total, [], shift

    def __call__(self, url, timeout=30, headers=None):
        finder = url.split("finder=", 1)[1]
        args = dict(kv.split("=", 1) for kv in finder.split(";", 1)[1].split(","))
        self.calls.append((url, args))
        off = int(args["offset"]) - (self.shift if len(self.calls) > 1 else 0)
        return reply([req(i) for i in range(off, min(off + int(args["limit"]), self.n))], self.total)


class Reader(unittest.TestCase):
    def setUp(self):
        self.real = (collect.get_json, collect.time.sleep)
        self.slept = []
        collect.time.sleep = self.slept.append

    def tearDown(self):
        collect.get_json, collect.time.sleep = self.real

    def test_a_board_id_is_pod_fa_region_slash_site_number_and_nothing_else(self):
        self.assertEqual(collect.oracle_parts("ebqb.fa.us2/CX_1001"), ("ebqb.fa.us2.oraclecloud.com", "CX_1001"))
        self.assertEqual(collect.oracle_parts("eeih.fa.us2/CX_6"), ("eeih.fa.us2.oraclecloud.com", "CX_6"))
        for bad in ("ebqb", "ebqb.fa.us2", "ebqb.fa.us2/BDOEntryLevelCareers", "evil.example.com/CX_1", "ebqb.fa.us2/CX_1/../x", "ebqb.fa.us2/CX_1;limit=1", "ebqb.fa.us2/cx_1", ""):
            with self.assertRaises(collect.InputError, msg=bad):
                collect.oracle_parts(bad)

    def test_it_pages_by_twenty_five_asks_for_the_newest_first_pauses_between_pages_and_stops_at_the_total(self):
        collect.get_json = site = FakeSite(60)
        out = collect.fetch_oracle("ebqb.fa.us2/CX_1", pause=0.7)
        self.assertEqual((out["total"], len(out["jobs"]), out["pages"], out["complete"]), (60, 60, 3, True))
        self.assertEqual([int(c[1]["offset"]) for c in site.calls], [0, 25, 50])
        self.assertEqual({urlparse(c[0]).netloc for c in site.calls}, {"ebqb.fa.us2.oraclecloud.com"})
        self.assertEqual({c[1]["siteNumber"] for c in site.calls}, {"CX_1"})
        self.assertEqual({(c[1]["limit"], c[1]["sortBy"]) for c in site.calls}, {("25", "POSTING_DATES_DESC")})
        self.assertEqual(self.slept, [0.7, 0.7])                                       # a pause between pages, none before the first or after the last
        q = parse_qs(urlparse(site.calls[0][0]).query)
        self.assertEqual(q["onlyData"], ["true"])
        self.assertEqual(q["expand"], ["requisitionList.secondaryLocations"])           # the other places come with the list: no request per posting

    def test_an_empty_site_is_one_request_and_a_short_list_ends_the_read_and_says_it_is_not_complete(self):
        collect.get_json = site = FakeSite(0)
        out = collect.fetch_oracle("egpy.fa.us2/CX_3001")
        self.assertEqual((out["jobs"], out["total"], out["complete"]), ([], 0, True))
        self.assertEqual(len(site.calls), 1)
        collect.get_json = FakeSite(10, total=30)                                      # the site says 30 and gives 10, then nothing: not complete, and it says so
        out = collect.fetch_oracle("egpy.fa.us2/CX_3001")
        self.assertEqual((len(out["jobs"]), out["complete"]), (10, False))

    def test_a_posting_that_shifts_into_the_next_page_is_counted_once(self):
        collect.get_json = FakeSite(40, shift=1)
        out = collect.fetch_oracle("eeih.fa.us2/CX_6")
        self.assertEqual(len({j["Id"] for j in out["jobs"]}), len(out["jobs"]))

    def test_a_reply_with_no_list_is_an_error_not_an_empty_board(self):
        for bad in ({"title": "Not Found"}, {"items": []}, {"items": [{"TotalJobsCount": 3}]}, {"items": ["x"]}):
            collect.get_json = lambda url, timeout=30, headers=None, bad=bad: bad
            with self.assertRaises(ValueError, msg=str(bad)):
                collect.fetch_oracle("eeih.fa.us2/CX_6")

    def test_a_site_that_never_ends_is_stopped(self):
        collect.get_json = lambda url, timeout=30, headers=None: reply([req(i) for i in range(25)], 10 ** 9)
        out = collect.fetch_oracle("eeih.fa.us2/CX_6", pause=0)
        self.assertEqual(out["pages"], collect.ORACLE_MAX_PAGES)
        self.assertFalse(out["complete"])


class Wire(unittest.TestCase):
    """The host list and the JSON-only guard that every Oracle request passes through."""
    def test_a_host_outside_the_list_and_a_plain_http_url_are_refused_before_any_request(self):
        for url in ("https://zzzz.fa.us2.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions",      # an Oracle site of nobody on the list
                    "https://fa-zzzz-saasfaprod1.fa.ocs.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions",
                    "https://example.com/x", "http://ebqb.fa.us2.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions"):
            with self.assertRaises(collect.InputError, msg=url):
                collect.get_json(url)

    def test_an_html_reply_is_an_error_and_is_never_parsed(self):
        class Resp:
            headers = {"Content-Type": "text/html"}
            def __enter__(s): return s
            def __exit__(s, *a): return False
            def read(s): return b"<html>Sign in</html>"

        class Opener:
            def open(s, req, timeout=None): return Resp()
        real = urllib.request.build_opener
        urllib.request.build_opener = lambda *h: Opener()
        try:
            with self.assertRaises(ValueError):
                collect.get_json("https://ebqb.fa.us2.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions")
        finally:
            urllib.request.build_opener = real

    def test_every_oracle_board_in_targets_is_on_the_host_list(self):
        boards = [t for t in DOC["targets"] if t["status"] == "active" and t.get("provider") == "oracle"]
        self.assertTrue(boards)
        for t in boards:
            host, _site = collect.oracle_parts(t["consulting"]["board"]["slug"])
            self.assertIn(host, collect.ORACLE_HOSTS, t["id"])
            self.assertIn(host, collect.ALLOWED, t["id"])


class Records(unittest.TestCase):
    def test_an_oracle_list_item_becomes_the_common_record(self):
        j = req(13887, "Assurance Associate - Fall 2027 (San Jose)", "San Jose, CA, United States", "2026-11-03")
        r = cc.records("oracle", "BDO (campus site)", "ebqb.fa.us2/CX_1001", {"jobs": [j]})[0]
        self.assertEqual((r["source"], r["company"], r["source_id"], r["title"], r["location_text"], r["date_posted"]),
                         ("oracle", "BDO (campus site)", "13887", "Assurance Associate - Fall 2027 (San Jose)", "San Jose, CA, United States", "2026-11-03"))
        self.assertEqual(r["url"], "https://ebqb.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/13887")
        self.assertEqual(cj.posting_view(r)["id"], "oracle:13887")

    def test_the_places_are_the_main_place_then_the_others_each_once(self):
        self.assertEqual(cc.oracle_place(req(1, second=[{"Name": "Boston, MA, United States"}, {"Name": "Atlanta, GA, United States"}, "Austin, TX, United States"])),
                         "Atlanta, GA, United States · Boston, MA, United States · Austin, TX, United States")
        self.assertEqual(cc.oracle_place({"PrimaryLocation": None, "secondaryLocations": None}), "")
        self.assertEqual(cc.oracle_place({"PrimaryLocation": "Telangana, India", "PrimaryLocationCountry": "IN"}), "Telangana, India")      # the country code is not a place word

    def test_a_posting_with_several_places_is_allowed_if_any_is_and_the_country_gate_reads_the_names(self):
        ok = cj.judge_consulting(cj.posting_view(cc.records("oracle", "X", "eeih.fa.us2/CX_6", {"jobs": [req(1, "Associate Consultant", "Hyderabad, Telangana, India", second=[{"Name": "Atlanta, GA, United States"}])]})[0]), KW)
        self.assertEqual(ok["decision"], "post")
        out = cj.judge_consulting(cj.posting_view(cc.records("oracle", "X", "eeih.fa.us2/CX_6", {"jobs": [req(2, "Associate Consultant", "Telangana, India")]})[0]), KW)
        self.assertEqual(out["decision"], "rejected")
        self.assertIn("India", out["reason"])

    def test_the_raw_file_name_has_no_slash(self):
        self.assertEqual(cc.raw_name("oracle", "ebqb.fa.us2/CX_1001", "2026-11-03"), "oracle-ebqb.fa.us2_cx_1001-2026-11-03.json")

    def test_the_status_line_of_an_oracle_board_says_how_many_it_lists_and_whether_all_came_back(self):
        st = cc.board_ok("BDO", "oracle", [1, 2], {"total": 5, "complete": False})
        self.assertEqual((st["listed_total"], st["complete"], st["postings"]), (5, False, 2))


class Targets(unittest.TestCase):
    def test_the_six_oracle_boards_are_active_carry_what_the_check_found_and_name_no_secret(self):
        boards = [t for t in DOC["targets"] if t["section"] == "consulting" and t.get("provider") == "oracle"]
        self.assertEqual(sorted(t["consulting"]["board"]["slug"] for t in boards), ["ebqb.fa.us2/CX_1", "ebqb.fa.us2/CX_1001", "eeih.fa.us2/CX_6", "egpy.fa.us2/CX_3001",
                                                                                                      "fa-etqo-saasfaprod1.fa.ocs/CX_1", "hbbq.fa.us2/CX_1"])
        for t in boards:       # BDO, Abt and Hackett were checked on 2026-11-03; ABS Group and Hexaware were added, and checked, on 2026-11-05
            self.assertEqual((t["status"], t["consulting"]["verdict"], t["consulting"]["oracle_terms_checked"]),
                             ("active", "keep", "2026-11-05" if t["id"] in ("consulting-abs-group", "consulting-hexaware") else "2026-11-03"), t["id"])
            self.assertTrue(t["why"] and t["consulting"]["what_answered"], t["id"])
            self.assertEqual(t["data"][1]["call"], True)
            self.assertIn(t["consulting"]["board"]["slug"].split("/")[1], t["data"][1]["url"])
        self.assertEqual(len({t["name"] for t in boards}), len(boards))                # BDO's two sites are two boards under two names

    def test_the_consulting_collector_reads_them_and_the_watch_list_does_not(self):
        names = [b[0] for b in cc.boards_from_targets(DOC) if b[1] == "oracle"]
        self.assertEqual(sorted(names), ["ABS Group", "Abt Associates", "BDO", "BDO (campus site)", "Hexaware Technologies", "The Hackett Group (incl. Archstone Consulting)"])
        with open(lp.config("sources.json")) as f:
            sources = json.load(f)
        watched = {b["company"] for s in sources["sources"] for b in s["boards"]}
        self.assertFalse(set(names) & watched)


if __name__ == "__main__":
    unittest.main()
