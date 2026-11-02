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

    def test_only_a_few_fields_are_kept_and_never_the_ad_text(self):
        out, _ = self.read({"508": [result(1, remote="True")]})
        text = json.dumps(out)
        for gone in ("LONG AD TEXT", "MORE AD TEXT", "QualificationSummary"):
            self.assertNotIn(gone, text)
        self.assertEqual((out["jobs"][0]["title"], out["jobs"][0]["organization"], out["jobs"][0]["remote_indicator"]), ("Accessibility Specialist", "Department of Examples", "True"))

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

    def test_the_status_line_says_what_usajobs_counted_for_each_query(self):
        payload = {"jobs": [], "total": 5, "complete": False, "pages": 3, "queries": {"508": 5}}
        st = cc.board_ok("USAJOBS (all federal agencies)", "usajobs", [], payload)
        self.assertEqual((st["listed_total"], st["complete"], st["queries"]), (5, False, {"508": 5}))


if __name__ == "__main__":
    unittest.main()
