#!/usr/bin/env python3
"""Tests for publish/consulting_feed.py: the same three locks as the games poster (in channel_feed.py), roles in several cities on one
line, a clearance veto that shows its effect, and nothing sent. No network: Discord and the webhook file are stand-ins."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import contextlib, copy, io, json, os, tempfile, unittest

import channel_feed
import consulting_feed
import notify

with open(lp.config("keywords.json")) as _f:
    KW = json.load(_f)


def rec(n, title, loc, company="Made Up Consulting"):
    return {"source": "greenhouse", "company": company, "source_id": str(n), "title": title, "url": f"https://jobs.example.test/{n}", "location_text": loc}


ROWS = [rec(1, "2027 Research Analyst (Economics)", "Boston, Massachusetts, United States"), rec(2, "2027 Research Analyst (Economics)", "Chicago, Illinois, United States"),
        rec(3, "2027 Research Analyst (Economics)", "Washington, District of Columbia, United States"), rec(4, "Summer 2027 Intern, Strategy", "London, England, United Kingdom"),
        rec(5, "Senior Consultant", "Boston, MA"), rec(6, "Business Analyst", "Boston, MA"), rec(7, "Cleared Junior Analyst", "Arlington, VA"),
        rec(8, "Graduate Analyst (m/f/d)", "Stockholm, Sweden"), rec(9, "Associate Software Engineer", "Boston, MA")]


class Feed(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = self.tmp.name
        self.jobs = os.path.join(d, "consulting-jobs-2026-10-28.json")
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
        kw["consulting_rule"]["posting"] = posting
        p = os.path.join(self.tmp.name, f"kw-{posting}.json")
        with open(p, "w") as f:
            json.dump(kw, f)
        return p

    def run_feed(self, *args, posting="off"):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = consulting_feed.main(["--jobs", self.jobs, "--keywords", self.rules(posting), "--state", self.state, *args])
        return code, out.getvalue()

    def test_the_default_is_a_dry_run_that_sends_nothing_reads_no_webhook_and_leaves_no_memory(self):
        code, out = self.run_feed()
        self.assertEqual(code, 0)
        self.assertIn("DRY RUN: nothing was sent and no webhook was read.", out)
        self.assertIn("posting to #consulting-firm is OFF", out)
        self.assertTrue(all(s[0] is False and s[1] == "consulting-firm" and s[2] == "Consulting: " for s in self.sent))
        self.assertFalse(os.path.exists(self.state))

    def test_one_role_in_several_cities_is_one_line_and_every_posting_is_remembered(self):
        _, out = self.run_feed()
        self.assertIn("**Made Up Consulting**: 2027 Research Analyst (Economics) · Boston, Chicago, Washington (research analyst, 2027) https://jobs.example.test/1", out)
        self.assertIn("as 2 line(s)", out)
        msgs = channel_feed.build_messages([(consulting_feed.cj.posting_view(r), consulting_feed.cj.judge_consulting(consulting_feed.cj.posting_view(r), KW)) for r in ROWS[:4]], consulting_feed.SPEC)
        self.assertEqual(sorted(i for _, ids in msgs for i in ids), ["greenhouse:1", "greenhouse:2", "greenhouse:3", "greenhouse:4"])

    def test_what_is_held_back_removed_or_not_consulting_is_not_posted_and_the_veto_shows_its_effect(self):
        _, out = self.run_feed("--show-unstated")
        self.assertIn("post 4 · unstated 1 · senior-or-mid 1 · not-consulting 1 · rejected 2", out)
        self.assertIn("clearance veto: 1 titles removed (1 would have been posted, 0 held back)", out)
        listing = out.split("held back, no level or early sign")[1]
        posted = out.split("to post:")[1].split("held back, no level or early sign")[0]
        self.assertIn("Business Analyst", listing)
        self.assertNotIn("Senior Consultant", posted)
        self.assertNotIn("Stockholm", posted)
        self.assertNotIn("Software Engineer", posted)

    def test_sending_is_refused_while_the_rules_say_off_and_a_first_send_needs_post_all(self):
        code, out = self.run_feed("--send", "--post-all")
        self.assertEqual(code, 3)
        self.assertIn('consulting_rule.posting is not "on"', out)
        code, out = self.run_feed("--send", posting="on")
        self.assertEqual(code, 3)
        self.assertIn("--baseline", out)
        self.assertEqual([s for s in self.sent if s[0]], [])

    def test_baseline_then_a_send_posts_nothing_and_a_new_posting_is_the_only_one_posted_later(self):
        self.run_feed("--baseline")
        with open(self.state) as f:
            self.assertEqual(len(json.load(f)), 4)
        code, out = self.run_feed("--send", posting="on")
        self.assertIn("Nothing new to post.", out)
        with open(self.jobs) as f:
            data = json.load(f)
        data["records"].append(rec(10, "2028 Graduate Analyst, Economics", "Boston, MA"))
        with open(self.jobs, "w") as f:
            json.dump(data, f)
        code, _ = self.run_feed("--send", posting="on")
        sent = [s for s in self.sent if s[0]]
        self.assertEqual((code, len(sent)), (0, 1))
        self.assertEqual((sent[0][1], sent[0][2]), ("consulting-firm", "Consulting: "))
        self.assertIn("2028 Graduate Analyst", sent[0][4])
        self.assertIn("Visa sponsorship is not checked.", sent[0][4])
        self.assertNotIn("2027 Research Analyst", sent[0][4])

    def test_the_default_postings_file_is_the_newest_saved_run(self):
        real = lp.RUNS
        consulting_feed.lp.RUNS = self.tmp.name
        try:
            os.makedirs(os.path.join(self.tmp.name, "2026-10-27"))
            os.makedirs(os.path.join(self.tmp.name, "2026-10-28"))
            for day in ("2026-10-27", "2026-10-28"):
                with open(os.path.join(self.tmp.name, day, f"consulting-jobs-{day}.json"), "w") as f:
                    json.dump({"records": []}, f)
            self.assertTrue(consulting_feed.newest_postings().endswith("consulting-jobs-2026-10-28.json"))
        finally:
            consulting_feed.lp.RUNS = real


if __name__ == "__main__":
    unittest.main()
