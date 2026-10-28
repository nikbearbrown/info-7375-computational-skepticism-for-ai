#!/usr/bin/env python3
"""Tests for publish/games_feed.py: dry run by default, three locks on sending, nothing posted twice, unsafe text refused.
No network: Discord and the webhook file are replaced by stand-ins, and no real webhook is ever read."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import contextlib, copy, io, json, os, tempfile, unittest

import games_feed
import notify

KW = json.load(open(lp.config("keywords.json")))


def row(n, title, locs=("Cary, North Carolina, United States",), company="Made Up Games"):
    return {"id": f"greenhouse:madeup:{n}", "company": company, "title": title, "url": f"https://jobs.example.test/{n}", "locations": list(locs)}


ROWS = [row(1, "Gameplay Programmer Intern"), row(2, "Associate Game Designer"), row(3, "Senior Game Designer"), row(4, "Tools Programmer Intern", ("Tokyo, Japan",)),
        row(5, "Level Designer"), row(6, "Product Manager Intern"), row(7, "Technical Artist Intern", ("Montreal, Canada",))]


class Feed(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = self.tmp.name
        self.jobs = os.path.join(d, "jobs.jsonl")
        with open(self.jobs, "w") as f:
            f.write("\n".join(json.dumps(r) for r in ROWS) + "\n")
        self.state = os.path.join(d, "posted.json")
        self.sent = []
        self.real_post, self.real_hook = notify.post, notify.webhook_url
        notify.webhook_url = lambda channel=None: self.fail("the webhook must not be read here")

        def fake_post(title, text, send, prefix="Jobs: ", channel=notify.CHANNEL):
            self.sent.append((send, channel, prefix, title, text))
            return self.real_post(title, text, False, prefix, channel) if not send else True      # the real safety check, never a real send
        notify.post = fake_post

    def tearDown(self):
        notify.post, notify.webhook_url = self.real_post, self.real_hook
        self.tmp.cleanup()

    def rules(self, posting):
        kw = copy.deepcopy(KW)
        kw["engine_rule"]["posting"] = posting
        p = os.path.join(self.tmp.name, f"kw-{posting}.json")
        with open(p, "w") as f:
            json.dump(kw, f)
        return p

    def run_feed(self, *args, posting="off", jobs=None):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = games_feed.main(["--jobs", jobs or self.jobs, "--keywords", self.rules(posting), "--state", self.state, *args])
        return code, out.getvalue()

    def test_the_default_is_a_dry_run_that_sends_nothing_and_reads_no_webhook(self):
        code, out = self.run_feed()
        self.assertEqual(code, 0)
        self.assertIn("DRY RUN: nothing was sent and no webhook was read.", out)
        self.assertIn("post 3", out)                                        # rows 1, 2 and 7: intern/associate + an allowed country
        self.assertTrue(all(s[0] is False for s in self.sent))
        self.assertFalse(os.path.exists(self.state))                        # a dry run leaves no memory behind
        self.assertTrue(all(s[1] == "games-3d-simulations" for s in self.sent))

    def test_the_dry_run_sample_names_company_title_place_link_and_nothing_else(self):
        _, out = self.run_feed()
        self.assertIn("**Made Up Games**: Gameplay Programmer Intern · Cary, North Carolina, United States (gameplay, intern) https://jobs.example.test/1", out)
        self.assertNotIn("Senior Game Designer", out)
        self.assertNotIn("Tokyo", out)

    def test_sending_is_refused_while_the_rules_say_posting_is_off(self):
        code, out = self.run_feed("--send", "--post-all")
        self.assertEqual(code, 3)
        self.assertIn('NOT SENT: keywords.json engine_rule.posting is not "on"', out)
        self.assertEqual([s for s in self.sent if s[0]], [])

    def test_a_first_send_with_no_memory_needs_post_all(self):
        code, out = self.run_feed("--send", posting="on")
        self.assertEqual(code, 3)
        self.assertIn("--baseline", out)
        self.assertEqual([s for s in self.sent if s[0]], [])

    def test_baseline_remembers_the_backlog_and_sends_nothing(self):
        code, _ = self.run_feed("--baseline")
        self.assertEqual(code, 0)
        with open(self.state) as f:
            self.assertEqual(sorted(json.load(f)), ["greenhouse:madeup:1", "greenhouse:madeup:2", "greenhouse:madeup:7"])
        code, out = self.run_feed("--send", posting="on")                   # memory exists now, so a send is allowed and finds nothing new
        self.assertEqual(code, 0)
        self.assertIn("Nothing new to post.", out)
        self.assertEqual([s for s in self.sent if s[0]], [])

    def test_a_send_posts_once_and_remembers_so_nothing_goes_twice(self):
        code, _ = self.run_feed("--send", "--post-all", posting="on")
        self.assertEqual(code, 0)
        sent = [s for s in self.sent if s[0]]
        self.assertEqual(len(sent), 1)
        self.assertEqual(sent[0][1:3], ("games-3d-simulations", "Games: "))
        self.assertIn("Associate Game Designer", sent[0][4])
        self.assertIn(games_feed.FOOTER, sent[0][4])
        with open(self.state) as f:
            self.assertEqual(len(json.load(f)), 3)
        code, out = self.run_feed("--send", posting="on")
        self.assertIn("Nothing new to post.", out)
        self.assertEqual(len([s for s in self.sent if s[0]]), 1)

    def test_a_new_posting_the_next_day_is_the_only_one_posted(self):
        self.run_feed("--send", "--post-all", posting="on")
        with open(self.jobs, "a") as f:
            f.write(json.dumps(row(8, "Engine Programmer Intern")) + "\n")
        self.sent.clear()
        code, _ = self.run_feed("--send", posting="on")
        self.assertEqual(code, 0)
        sent = [s for s in self.sent if s[0]]
        self.assertEqual(len(sent), 1)
        self.assertIn("Engine Programmer Intern", sent[0][4])
        self.assertNotIn("Associate Game Designer", sent[0][4])

    def test_text_with_an_email_address_or_a_local_path_is_not_sent_and_not_remembered(self):
        bad = os.path.join(self.tmp.name, "bad.jsonl")
        with open(bad, "w") as f:
            f.write(json.dumps(row(9, "Game Design Intern (apply to someone@example.test)")) + "\n")
        notify.post = lambda *a, **k: self.real_post(*a[:2], False, *a[3:4], **{**k, "channel": k.get("channel", notify.CHANNEL)}) and False
        code, out = self.run_feed("--send", "--post-all", posting="on", jobs=bad)
        self.assertEqual(code, 1)
        self.assertIn("NOT SENT", out)
        self.assertFalse(os.path.exists(self.state))

    def test_when_discord_refuses_the_second_message_only_the_first_is_remembered(self):
        many = os.path.join(self.tmp.name, "many.jsonl")
        with open(many, "w") as f:
            f.write("\n".join(json.dumps(row(200 + i, f"Gameplay Programmer Intern {i}")) for i in range(40)) + "\n")
        calls = []

        def flaky(title, text, send, prefix="Jobs: ", channel=notify.CHANNEL):
            calls.append(text)
            return len(calls) == 1
        notify.post = flaky
        code, out = self.run_feed("--send", "--post-all", posting="on", jobs=many)
        self.assertEqual(code, 1)
        with open(self.state) as f:
            remembered = json.load(f)
        self.assertGreater(len(remembered), 0)
        self.assertLess(len(remembered), 40)
        self.assertEqual(len(remembered), calls[0].count("https://jobs.example.test/"))

    def test_held_back_postings_are_posted_only_if_the_rules_say_so(self):
        kw = copy.deepcopy(KW)
        kw["engine_rule"]["include_unstated_level"] = True
        todo = games_feed.wanted(games_feed.judge_all([games_feed.ej.posting_view(r) for r in ROWS], kw), kw)
        self.assertIn("greenhouse:madeup:5", [v["id"] for v, _ in todo])
        todo = games_feed.wanted(games_feed.judge_all([games_feed.ej.posting_view(r) for r in ROWS], KW), KW)
        self.assertNotIn("greenhouse:madeup:5", [v["id"] for v, _ in todo])

    def test_messages_split_and_carry_their_own_ids(self):
        many = [games_feed.ej.posting_view(row(100 + i, f"Gameplay Programmer Intern {i}")) for i in range(40)]
        msgs = games_feed.build_messages([(v, games_feed.ej.judge_engine(v, KW)) for v in many])
        self.assertGreater(len(msgs), 1)
        self.assertEqual(sum(len(ids) for _, ids in msgs), 40)
        self.assertTrue(all(len(text) < 2000 for text, _ in msgs))
        self.assertTrue(msgs[-1][0].endswith(games_feed.FOOTER))


class NotifyChannel(unittest.TestCase):
    def test_notify_post_defaults_to_professor_bear_and_names_the_channel_it_was_given(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            notify.post("t", "plain text", False)
            notify.post("t", "plain text", False, channel="games-3d-simulations")
        self.assertIn("DRY RUN, #professor-bear", out.getvalue())
        self.assertIn("DRY RUN, #games-3d-simulations", out.getvalue())


if __name__ == "__main__":
    unittest.main()
