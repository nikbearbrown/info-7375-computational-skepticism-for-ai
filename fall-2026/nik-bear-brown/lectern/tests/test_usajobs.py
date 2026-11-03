#!/usr/bin/env python3
"""Tests for the USAJOBS reader (collect.usajobs_login / fetch_usajobs, consulting_collect.records for provider usajobs) and how the federal-508 judge sees its postings.
No network, and a made-up key and email in a temporary folder: the real ones in ~/.usajobs are never read here."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import json, os, stat, tempfile, unittest

import collect
import consulting_collect as cc
import federal508_jobs as fj

with open(lp.config("keywords.json")) as _f:
    KW = json.load(_f)

KEY, EMAIL = "A" * 20 + "b9/+=" * 4, "someone@example.org"


def login_dir(key=KEY, email=EMAIL, mode=0o600):
    d = tempfile.mkdtemp()
    for name, v in (("key", key), ("email", email)):
        if v is not None:
            path = os.path.join(d, name)
            with open(path, "w") as f:
                f.write(v + "\n")
            os.chmod(path, mode)
    return d


def result(n, title="Accessibility Specialist", places=(("Washington, District of Columbia", "United States"),), remote=None, org="Department of Examples", extra=None):
    d = {"PositionID": f"X-{n}", "PositionTitle": title, "PositionURI": f"https://www.usajobs.gov/job/{n}", "OrganizationName": org, "DepartmentName": "Department of Things",
         "PositionLocation": [{"LocationName": a, "CountryCode": b} for a, b in places], "PublicationStartDate": "2026-10-30T00:00:00.0000", "ApplicationCloseDate": "2026-11-20",
         "PositionOfferingType": [{"Name": "Permanent"}], "PositionSchedule": [{"Name": "Full-time"}], "QualificationSummary": "LONG AD TEXT " * 50,
         "UserArea": {"Details": {"JobSummary": "MORE AD TEXT", "RemoteIndicator": remote, "TeleworkEligible": "True", **(extra or {})}}}
    return {"MatchedObjectId": str(1000 + n), "MatchedObjectDescriptor": d}


class FakeApi:
    """Stands in for collect.get_json: answers each Keyword with its own list of results, `size` to a page."""
    def __init__(self, by_query, size=2):
        self.by_query, self.size, self.calls = by_query, size, []

    def __call__(self, url, timeout=30, headers=None):
        self.calls.append((url, headers))
        from urllib.parse import urlparse, parse_qs
        q = parse_qs(urlparse(url).query)
        items = self.by_query.get(q["Keyword"][0], [])
        page = int(q["Page"][0])
        return {"SearchResult": {"SearchResultCountAll": len(items), "SearchResultItems": items[(page - 1) * self.size:page * self.size]}}


class Login(unittest.TestCase):
    def test_a_key_and_an_email_in_files_only_the_owner_can_read_are_returned(self):
        self.assertEqual(collect.usajobs_login(login_dir()), (KEY, EMAIL))

    def test_a_missing_or_wrong_file_is_an_error_that_names_the_file_and_never_shows_a_value(self):
        for d in (login_dir(email=None), login_dir(key=None), login_dir(key="short"), login_dir(email="not an address"), login_dir(mode=0o644)):
            with self.assertRaises(collect.InputError) as c:
                collect.usajobs_login(d)
            msg = str(c.exception)
            self.assertTrue(("key" in msg or "email" in msg) and d in msg, msg)
            for secret in (KEY, EMAIL, "short", "not an address"):
                self.assertNotIn(secret, msg)

    def test_the_host_is_allowed_for_https_only(self):
        self.assertEqual(collect._checked("https://data.usajobs.gov/api/search?Keyword=508"), "https://data.usajobs.gov/api/search?Keyword=508")
        with self.assertRaises(collect.InputError):
            collect._checked("http://data.usajobs.gov/api/search")
        with self.assertRaises(collect.InputError):
            collect._checked("https://www.usajobs.gov/api/search")


class Fetch(unittest.TestCase):
    def setUp(self):
        self.real = collect.get_json

    def tearDown(self):
        collect.get_json = self.real

    def read(self, by_query, size=2):
        collect.get_json = FakeApi(by_query, size)
        out = collect.fetch_usajobs("search", pause=0, login=(KEY, EMAIL))
        return out, collect.get_json

    def test_it_pages_each_query_and_counts_a_posting_found_by_two_queries_once(self):
        a, b, c = result(1), result(2, "Section 508 Tester"), result(3, "WCAG Reviewer")
        out, api = self.read({"508": [b, a, c], "accessibility": [a, b]}, size=2)
        self.assertEqual([j["id"] for j in out["jobs"]], ["X-2", "X-1", "X-3"])
        self.assertEqual(out["total"], 3)
        self.assertEqual(out["jobs"][1]["matched_by"], ["508", "accessibility"])
        self.assertEqual(out["queries"]["508"], 3)
        self.assertEqual(out["queries"]["a11y"], 0)
        self.assertTrue(out["complete"])
        self.assertEqual(out["pages"], len(api.calls))
        self.assertEqual(len(api.calls), 2 + 1 + 1 + 1 + 1 + 1)           # '508' two pages, '508'... the other five queries one each

    def test_the_key_and_the_email_go_in_the_headers_and_never_in_the_address(self):
        _, api = self.read({"508": [result(1)]})
        for url, headers in api.calls:
            self.assertTrue(url.startswith("https://data.usajobs.gov/api/search?Keyword="))
            self.assertNotIn(KEY, url)
            self.assertNotIn(EMAIL, url)
            self.assertEqual((headers["Authorization-Key"], headers["User-Agent"]), (KEY, EMAIL))

    def test_the_summary_duties_and_qualifications_are_kept_for_the_judge_and_nothing_else_of_the_ad(self):
        duties = ["Performs Section 508 testing of web applications.", "Writes reports."]
        out, _ = self.read({"508": [result(1, remote="True", extra={"MajorDuties": duties, "ApplicationInstructions": "SECRET HOW TO APPLY", "AgencyContactEmail": "hr@agency.example"})]})
        job = out["jobs"][0]
        self.assertIn("MORE AD TEXT", job["ad_text"])
        self.assertIn("Performs Section 508 testing of web applications.", job["ad_text"])
        self.assertIn("LONG AD TEXT", job["ad_text"])
        text = json.dumps(out)
        for gone in ("SECRET HOW TO APPLY", "hr@agency.example"):
            self.assertNotIn(gone, text)
        self.assertEqual((job["title"], job["organization"], job["remote_indicator"]), ("Accessibility Specialist", "Department of Examples", "True"))

    def test_the_ad_text_is_capped(self):
        out, _ = self.read({"508": [result(1, extra={"JobSummary": "x" * 20000})]})
        self.assertLessEqual(len(out["jobs"][0]["ad_text"]), collect.USAJOBS_AD_CHARS)

    def test_a_search_that_gave_fewer_than_it_counted_is_not_complete(self):
        def lying(url, timeout=30, headers=None):
            return {"SearchResult": {"SearchResultCountAll": 9, "SearchResultItems": [result(1)] if "Page=1" in url else []}}
        collect.get_json = lying
        out = collect.fetch_usajobs("search", pause=0, login=(KEY, EMAIL))
        self.assertFalse(out["complete"])

    def test_a_reply_without_a_results_list_is_an_error_and_an_unknown_board_is_refused(self):
        collect.get_json = lambda url, timeout=30, headers=None: {"error": "denied"}
        with self.assertRaises(ValueError):
            collect.fetch_usajobs("search", pause=0, login=(KEY, EMAIL))
        with self.assertRaises(collect.InputError):
            collect.fetch_usajobs("anything-else", pause=0, login=(KEY, EMAIL))

    def test_it_pauses_between_requests(self):
        slept, real = [], collect.time.sleep
        collect.time.sleep = slept.append
        try:
            collect.get_json = FakeApi({"508": [result(1)]})
            collect.fetch_usajobs("search", pause=0.4, login=(KEY, EMAIL))
        finally:
            collect.time.sleep = real
        self.assertEqual(slept, [0.4] * (len(collect.USAJOBS_QUERIES) - 1))

    def test_the_collector_asks_for_the_login_and_a_missing_one_stops_before_any_request(self):
        collect.get_json = lambda *a, **k: self.fail("a request was made")
        real, collect.USAJOBS_DIR = collect.USAJOBS_DIR, tempfile.mkdtemp()
        try:
            with self.assertRaises(collect.InputError):
                cc.fetch_list("usajobs", "search")
        finally:
            collect.USAJOBS_DIR = real


class Records(unittest.TestCase):
    def recs(self, *results):
        payload = {"jobs": [collect._usajobs_item(r["MatchedObjectDescriptor"]) | {"object_id": r["MatchedObjectId"], "matched_by": ["508"]} for r in results]}
        return cc.records("usajobs", "USAJOBS (all federal agencies)", "search", payload)

    def test_a_posting_is_shown_under_the_agency_that_posts_it_with_a_place_and_a_link(self):
        r = self.recs(result(1, places=(("Washington, District of Columbia", "United States"), ("Denver, Colorado", "United States"))))[0]
        self.assertEqual((r["source"], r["company"], r["source_id"]), ("usajobs", "Department of Examples", "1001"))
        self.assertEqual(r["location_text"], "Washington, District of Columbia, United States · Denver, Colorado, United States")
        self.assertEqual((r["url"], r["date_posted"], r["closes"]), ("https://www.usajobs.gov/job/1", "2026-10-30", "2026-11-20"))

    def test_remote_is_said_only_when_usajobs_marks_the_posting_remote_not_for_telework(self):
        remote, onsite = self.recs(result(1, remote="True"), result(2, remote="False"))
        self.assertTrue(remote["location_text"].endswith(" · Remote"))
        self.assertNotIn("Remote", onsite["location_text"])
        self.assertEqual(onsite["telework_eligible"], "True")                # kept to read, but it is not a word the judge sees
        self.assertNotIn("telework", onsite["location_text"].lower())

    def test_the_federal_508_judge_posts_a_remote_one_holds_back_an_onsite_one_and_calls_the_poster_an_agency(self):
        remote, onsite, abroad = self.recs(result(1, "Section 508 Accessibility Specialist", remote="True"), result(2, "Section 508 Accessibility Specialist"),
                                           result(3, "Section 508 Accessibility Specialist", places=(("Berlin, Germany", "Germany"),)))
        jr, jo, ja = (fj.judge_federal508(fj.posting_view(x), KW, {}) for x in (remote, onsite, abroad))
        self.assertEqual((jr["decision"], bool(jr["remote"]), jr["kind"]), ("post", True, "agency"))
        self.assertEqual(jo["decision"], "unstated")
        self.assertEqual(ja["decision"], "rejected")

    def test_the_record_carries_the_ad_text_as_its_description(self):
        r = self.recs(result(1, extra={"MajorDuties": ["Section 508 testing"]}))[0]
        self.assertIn("Section 508 testing", r["description"])
        self.assertEqual(fj.posting_view(r)["description"], r["description"])
        self.assertNotIn("description", fj.posting_view({k: v for k, v in r.items() if k != "description"}))

    def test_a_work_phrase_in_the_ad_text_makes_a_plain_title_a_match_and_a_requirement_clause_does_not(self):
        work, clause, none = self.recs(result(1, "IT Specialist (APPSW)", remote="True", extra={"MajorDuties": ["Conducts Section 508 testing and accessibility audits."]}),
                                       result(2, "IT Specialist (APPSW)", remote="True", extra={"MajorDuties": ["Builds software that meets Section 508."]}),
                                       result(3, "IT Specialist (APPSW)", remote="True"))
        jw, jc, jn = (fj.judge_federal508(fj.posting_view(x), KW, {}) for x in (work, clause, none))
        self.assertEqual(jw["decision"], "post")
        self.assertTrue(all(g == "ad-text" for g, _ in jw["hits"]))
        self.assertIn("in the ad text", jw["reason"])
        self.assertEqual((jc["decision"], jn["decision"]), ("no-match", "no-match"))
        self.assertIn("or the ad text", jc["reason"])

    def test_a_title_phrase_still_wins_and_a_view_without_ad_text_is_judged_from_the_title_alone(self):
        t = fj.judge_federal508(fj.posting_view(self.recs(result(1, "Section 508 Tester", remote="True"))[0]), KW, {})
        self.assertEqual((t["decision"], {g for g, _ in t["hits"]}), ("post", {"section-508"}))
        plain = {"id": "x:1", "company": "Acme", "title": "Developer", "url": "", "location_text": "US - Remote"}
        self.assertEqual(fj.judge_federal508(plain, KW, {})["reason"], "no Section 508 or accessibility phrase in the title")

    def test_the_feed_says_when_the_phrase_was_in_the_ad_and_not_the_title(self):
        import federal508_feed
        r = self.recs(result(1, "IT Specialist (APPSW)", remote="True", extra={"MajorDuties": ["Performs 508 testing."]}))[0]
        v = fj.posting_view(r)
        line = federal508_feed.row_text(v, fj.judge_federal508(v, KW, {}))
        self.assertIn("508 named in the ad text, not the title", line)
        self.assertIn("remote", line)

    def test_the_status_line_says_what_usajobs_counted_for_each_query(self):
        payload = {"jobs": [], "total": 5, "complete": False, "pages": 3, "queries": {"508": 5}}
        st = cc.board_ok("USAJOBS (all federal agencies)", "usajobs", [], payload)
        self.assertEqual((st["listed_total"], st["complete"], st["queries"]), (5, False, {"508": 5}))


if __name__ == "__main__":
    unittest.main()
