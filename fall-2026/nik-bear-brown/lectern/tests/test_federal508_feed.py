#!/usr/bin/env python3
"""Tests for publish/federal508_feed.py: the same three locks as the other channels (in channel_feed.py), flags on every line, a person's name nowhere,
and nothing sent. No network: Discord and the webhook file are stand-ins."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import contextlib, copy, io, json, os, tempfile, unittest

import federal508_feed
import notify

with open(lp.config("keywords.json")) as _f:
    KW = json.load(_f)


def rec(n, title, loc, company="Made Up Federal"):
    return {"source": "greenhouse", "company": company, "source_id": str(n), "title": title, "url": f"https://jobs.example.test/{n}", "location_text": loc}


ROWS = [rec(1, "Section 508 Tester (Remote)", "Remote - United States"), rec(2, "Accessibility Consultant", "Reston, VA"), rec(3, "Accessibility Specialist", "Reston, VA"),
        rec(4, "508 Analyst - Secret clearance - Telework", "Arlington, VA"), rec(5, "Accessibility Specialist (Remote)", "London, United Kingdom"),
        rec(6, "Building Accessibility Inspector - Remote", "Remote"), rec(7, "Software Engineer", "Remote")]


class Feed(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = self.tmp.name
        self.jobs = os.path.join(d, "federal508-jobs-2026-10-31.json")
        with open(self.jobs, "w") as f:
            json.dump({"records": ROWS}, f)
        self.state = os.path.join(d, "posted.json")
        self.sent = []
        self.real_post, self.real_hook = notify.post, notify.webhook_url
        notify.webhook_url = lambda channel=None: self.fail("the webhook must not be read here")

        def fake_post(title, text, send, prefix="Jobs: ", channel=notify.CHANNEL):
            self.sent.append((send, channel, prefix, title, text))
            return self.real_post(title, text, False, prefix, channel) if not send else True
        notify.post = fake_post

    def tearDown(self):
        notify.post, notify.webhook_url = self.real_post, self.real_hook
        self.tmp.cleanup()

    def rules(self, posting):
        kw = copy.deepcopy(KW)
        kw["federal508_rule"]["posting"] = posting
        p = os.path.join(self.tmp.name, f"kw-{posting}.json")
        with open(p, "w") as f:
            json.dump(kw, f)
        return p

    def run_feed(self, *args, posting="off"):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = federal508_feed.main(["--jobs", self.jobs, "--keywords", self.rules(posting), "--state", self.state, *args])
        return code, out.getvalue()

    def test_the_default_is_a_dry_run_that_sends_nothing_reads_no_webhook_and_leaves_no_memory(self):
        code, out = self.run_feed()
        self.assertEqual(code, 0)
        self.assertIn("DRY RUN: nothing was sent and no webhook was read.", out)
        self.assertIn("posting to #federal-508 is OFF", out)
        self.assertTrue(all(s[0] is False and s[1] == "federal-508" and s[2] == "Federal 508: " for s in self.sent))
        self.assertFalse(os.path.exists(self.state))

    def test_a_line_carries_the_flags_the_title_and_place_support_and_the_clearance_is_shown_not_hidden(self):
        _, out = self.run_feed()
        self.assertIn("**Made Up Federal**: Section 508 Tester (Remote) · Remote - United States [remote] https://jobs.example.test/1", out)
        self.assertIn("**Made Up Federal**: Accessibility Consultant · Reston, VA [contract] https://jobs.example.test/2", out)
        self.assertIn("[remote, clearance named: secret] https://jobs.example.test/4", out)

    def test_what_is_held_back_foreign_physical_or_unrelated_is_not_posted_and_the_counts_say_so(self):
        _, out = self.run_feed("--show-unstated")
        self.assertIn("post 3 · unstated 1 · not-digital 1 · rejected 1 · no-match 1", out)
        posted = out.split("to post:")[1].split("held back")[0]
        for word in ("London", "Building", "Software Engineer", "Accessibility Specialist · Reston"):
            self.assertNotIn(word, posted)
        self.assertIn("Accessibility Specialist", out.split("held back")[1])
        self.assertIn("engagement words: remote and contract 0, remote only 2, contract only 1; clearance named in 1 of the posts", out)

    def test_sending_is_refused_while_the_rules_say_off_and_a_first_send_needs_post_all(self):
        code, out = self.run_feed("--send", "--post-all")
        self.assertEqual(code, 3)
        self.assertIn('federal508_rule.posting is not "on"', out)
        code, out = self.run_feed("--send", posting="on")
        self.assertEqual(code, 3)
        self.assertIn("--baseline", out)
        self.assertEqual([s for s in self.sent if s[0]], [])

    def test_baseline_then_a_send_posts_nothing_and_a_new_posting_is_the_only_one_posted_later(self):
        self.run_feed("--baseline")
        with open(self.state) as f:
            self.assertEqual(len(json.load(f)), 3)
        code, out = self.run_feed("--send", posting="on")
        self.assertIn("Nothing new to post.", out)
        with open(self.jobs) as f:
            data = json.load(f)
        data["records"].append(rec(10, "VPAT Author, Remote", "Remote"))
        with open(self.jobs, "w") as f:
            json.dump(data, f)
        code, _ = self.run_feed("--send", posting="on")
        sent = [s for s in self.sent if s[0]]
        self.assertEqual((code, len(sent)), (0, 1))
        self.assertEqual((sent[0][1], sent[0][2]), ("federal-508", "Federal 508: "))
        self.assertIn("VPAT Author", sent[0][4])
        self.assertIn("Pay and the kind of engagement are not checked.", sent[0][4])
        self.assertNotIn("Section 508 Tester", sent[0][4])

    def test_the_default_postings_file_is_the_newest_saved_run(self):
        real = lp.RUNS
        federal508_feed.lp.RUNS = self.tmp.name
        try:
            for day in ("2026-10-30", "2026-10-31"):
                os.makedirs(os.path.join(self.tmp.name, day))
                with open(os.path.join(self.tmp.name, day, f"federal508-jobs-{day}.json"), "w") as f:
                    json.dump({"records": []}, f)
            self.assertTrue(federal508_feed.newest_postings().endswith("federal508-jobs-2026-10-31.json"))
        finally:
            federal508_feed.lp.RUNS = real


if __name__ == "__main__":
    unittest.main()
