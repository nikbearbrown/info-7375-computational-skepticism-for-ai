#!/usr/bin/env python3
"""Tests for the Google board (collect.fetch_google / google_view, added 2026-11-20) and churn leaving a search board out. No network."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import json, os, tempfile, unittest

import churn
import collect

with open(lp.config("keywords.json")) as _f:
    KW = json.load(_f)


def row(n, title="Developer Advocate, Gemini", place="Mountain View, CA, USA", ts=1795132800):
    """A made-up record in the positional layout of Google's 'ds:1' block (as collectors/google.py describes it)."""
    r = [str(n), title, f"https://www.google.com/about/careers/applications/signin?jobId={n}",
         [None, "<p>Teach developers and students to build with Gemini at universities.</p>"], [None, "<ul><li>Workshops</li></ul>"],
         "applications/jobs", None, "Google", "en-US", [[place, [place], "Mountain View", None, "CA", "US"]], None, None, [ts]]
    return r


def page(rows, total=None):
    data = [rows, None, len(rows) if total is None else total, 20]
    return "<html><script>AF_initDataCallback({key: 'ds:1', hash: '2', data:" + json.dumps(data) + ", sideChannel: {}});</script></html>"


class FakeSite:
    def __init__(self, pages):
        self.pages, self.urls = pages, []

    def __call__(self, url, timeout=45):
        self.urls.append(url)
        return self.pages[len(self.urls) - 1]


class GoogleBoard(unittest.TestCase):
    def setUp(self):
        self._get, self._pause = collect.get_page, collect.GOOGLE_PAUSE

    def tearDown(self):
        collect.get_page = self._get

    def test_one_request_a_term_never_a_second_page_and_a_posting_counts_once(self):
        site = FakeSite([page([row(1), row(2, "Software Engineer")], total=57), page([row(2, "Software Engineer"), row(3, "Education Program Manager")])])
        collect.get_page = site
        out = collect.fetch_google(["developer advocate", "education"], pause=0)
        self.assertEqual(len(site.urls), 2)
        self.assertTrue(all("page=" not in u for u in site.urls), site.urls)          # robots.txt disallows the paged results
        self.assertEqual([r[0] for r in out["jobs"]], ["1", "2", "3"])
        self.assertEqual(out["searched"][0], {"term": "developer advocate", "total": 57, "read": 2})
        self.assertEqual((out["read"], out["complete"]), ("search", False))

    def test_no_terms_is_an_input_error_not_an_empty_board(self):
        with self.assertRaises(collect.InputError):
            collect.fetch_google([])

    def test_a_row_becomes_a_posting_the_judge_reads(self):
        v = collect.normalise("google", "Google", {"jobs": [row(7)]})[0]
        self.assertEqual((v["source"], v["source_id"], v["date_posted"]), ("google", "7", "2026-11-20"))
        self.assertEqual(v["url"], "https://www.google.com/about/careers/applications/jobs/results/7")
        self.assertIn("Mountain View, CA, USA", v["location_text"])
        self.assertIn("universities", v["text"])
        m, why = collect.judge(v, KW)
        self.assertTrue(m, why)

    def test_a_moved_layout_raises_instead_of_returning_nothing(self):
        bad = row(1)
        bad[1] = None
        collect.get_page = FakeSite([page([bad])])
        with self.assertRaises(AssertionError):
            collect.fetch_google(["advocate"], pause=0)


class ChurnLeavesSearchOut(unittest.TestCase):
    def test_a_board_read_by_search_is_not_counted(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "all-jobs-2026-11-20.json")
            json.dump({"sources": [{"company": "Acme", "status": "ok"}, {"company": "Google", "status": "ok", "read": "search"}],
                       "records": [{"source": "greenhouse", "company": "Acme", "source_id": "1"}, {"source": "google", "company": "Google", "source_id": "2"}]},
                      open(p, "w"))
            s = churn.load(p)
        self.assertEqual(s["ok"], {"Acme"})
        self.assertEqual(list(s["recs"]), ["greenhouse:1"])


if __name__ == "__main__":
    unittest.main()
