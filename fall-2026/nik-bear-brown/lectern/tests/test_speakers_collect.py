#!/usr/bin/env python3
"""Tests for collect/speakers_collect.py: the leads file holds no person, a link is read once with robots.txt first, an error page is never
parsed, and the local people check reports counts without names. No network: the opener is a stand-in."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import contextlib, io, json, os, tempfile, unittest, urllib.error

import speakers_collect as sc

DOC = {"targets": [
    {"id": "speakers-a", "name": "A Co", "section": "speakers", "status": "active", "why": "made up",
     "speakers": {"verdict": "keep", "product": "A", "mcp": {"name": "A MCP", "primary_source": "https://a.example.test/mcp", "status": "GA"},
                  "signals": [{"kind": "mcp_docs", "url": "https://a.example.test/mcp"}, {"kind": "devrel_team", "url": "https://a.example.test/devrel"}],
                  "people_found": 1, "contact_route": {"kind": "devrel-page", "url": "https://a.example.test/devrel"}}},
    {"id": "consulting-x", "name": "X", "section": "consulting", "status": "active", "why": "", "consulting": {}}]}

PAGES = {"https://a.example.test/mcp": (200, "<html>The A MCP server lets Jane Doe...</html>"), "https://a.example.test/devrel": (404, ""),
         "https://b.example.test/talk": (200, "<html>Talk by Dana Roe about the Model Context Protocol</html>")}


class Resp:
    def __init__(self, status, body):
        self.status, self.body, self.headers = status, body.encode(), {"Content-Type": "text/html"}
    def read(self, n=-1):
        return self.body
    def __enter__(self):
        return self
    def __exit__(self, *a):
        return False


class Opener:
    def __init__(self, robots="User-agent: *\nAllow: /"):
        self.calls, self.robots = [], robots
    def __call__(self, req, timeout=0):
        url = req.full_url
        self.calls.append(url)
        if url.endswith("/robots.txt"):
            return Resp(200, self.robots)
        status, body = PAGES.get(url, (404, ""))
        if status != 200:
            raise urllib.error.HTTPError(url, status, "x", {}, io.BytesIO(b""))
        return Resp(status, body)


class Collect(unittest.TestCase):
    def reader(self, opener=None):
        return sc.Reader(delay=0, opener=opener or Opener(), sleep=lambda s: None)

    def test_only_the_speakers_section_becomes_leads_and_no_person_is_in_them(self):
        leads = sc.leads_from_targets(DOC)
        self.assertEqual([l["company"] for l in leads], ["A Co"])
        self.assertEqual(leads[0]["people_found"], 1)
        self.assertNotIn("Jane", json.dumps(leads))

    def test_a_link_is_read_once_after_robots_and_the_term_is_recorded(self):
        op = Opener()
        res = sc.check_urls(sc.urls_of(sc.leads_from_targets(DOC)[0]), self.reader(op))
        self.assertEqual(res["https://a.example.test/mcp"], {"status": "200", "term": True})
        self.assertEqual(res["https://a.example.test/devrel"], {"status": "404", "term": None})        # an error page is never parsed
        self.assertEqual(op.calls.count("https://a.example.test/mcp"), 1)
        self.assertEqual(op.calls[0], "https://a.example.test/robots.txt")

    def test_a_page_robots_disallows_is_not_fetched(self):
        op = Opener(robots="User-agent: *\nDisallow: /")
        res = sc.check_urls(["https://a.example.test/mcp"], self.reader(op))
        self.assertEqual(res["https://a.example.test/mcp"]["status"], "robots")
        self.assertNotIn("https://a.example.test/mcp", op.calls)

    def test_a_link_that_is_not_https_is_refused_without_a_request(self):
        op = Opener()
        self.assertEqual(self.reader(op).get("http://a.example.test/mcp"), ("refused", ""))
        self.assertEqual(op.calls, [])

    def test_the_surname_check_is_weak_on_purpose(self):
        self.assertTrue(sc.surname_seen("Dana Roe", "Talk by Dana Roe"))
        self.assertFalse(sc.surname_seen("Dana Roe", "Talk by Dana Rowe"))
        self.assertFalse(sc.surname_seen("", "anything"))

    def test_the_people_check_reports_counts_and_the_output_holds_no_name(self):
        people = [{"company_id": "speakers-a", "name": "Dana Roe", "source_url": "https://b.example.test/talk"}]
        res = sc.check_people(people, self.reader())
        self.assertEqual(res, [{"company_id": "speakers-a", "source_url": "https://b.example.test/talk", "status": "200", "surname_seen": True}])
        self.assertNotIn("Dana", json.dumps(res))

    def test_main_writes_the_leads_file_and_flags_a_people_count_that_disagrees(self):
        with tempfile.TemporaryDirectory() as d:
            tp, rec = os.path.join(d, "targets.json"), os.path.join(d, "records")
            os.makedirs(rec)
            with open(tp, "w") as f:
                json.dump(DOC, f)
            with open(os.path.join(rec, "p.jsonl"), "w") as f:
                f.write(json.dumps({"company_id": "speakers-b", "name": "Dana Roe", "source_url": "https://b.example.test/talk"}) + "\n")
            real = sc.Reader
            sc.Reader = lambda: real(delay=0, opener=Opener(), sleep=lambda s: None)
            try:
                out = io.StringIO()
                with contextlib.redirect_stdout(out):
                    code = sc.main(["--targets", tp, "--out", os.path.join(d, "run"), "--people", "--records", rec])
            finally:
                sc.Reader = real
            self.assertEqual(code, 0)
            self.assertIn("MISMATCH A Co: targets.json says people_found=1, records hold 0 opened", out.getvalue())
            with open(os.path.join(d, "run", os.listdir(os.path.join(d, "run"))[0])) as f:
                leads = json.load(f)
            self.assertEqual(len(leads["records"]), 1)
            self.assertNotIn("Dana", json.dumps(leads))
            self.assertTrue(os.path.exists(os.path.join(rec, f"people-check-{__import__('datetime').date.today().isoformat()}.json")))


if __name__ == "__main__":
    unittest.main()
