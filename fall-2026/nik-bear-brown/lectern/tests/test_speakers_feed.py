#!/usr/bin/env python3
"""Tests for publish/speakers_feed.py: the same three locks as the other channels (in channel_feed.py), a company is one line, no person is
named, and nothing is sent. No network: Discord and the webhook file are stand-ins."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import contextlib, copy, io, json, os, tempfile, unittest

import speakers_feed
import notify

with open(lp.config("keywords.json")) as _f:
    KW = json.load(_f)
U = "https://example.test/"


def lead(n, name, signals, people=1, route=True, verdict="keep"):
    return {"id": f"speakers-{n}", "company": name, "verdict": verdict, "why": "made up", "mcp": {"name": f"{name} MCP", "primary_source": f"{U}{n}/mcp", "status": "GA"},
            "signals": [{"kind": k, "url": f"{U}{n}/{k}/{i}"} for k, i in signals], "people_found": people,
            "contact_route": {"kind": "devrel-page", "url": f"{U}{n}/devrel"} if route else {}}


FULL = [("mcp_docs", 1), ("devrel_team", 1), ("mcp_talk", 1), ("community_channel", 1)]
ROWS = [lead(1, "Alpha Co", FULL), lead(2, "Beta Co", FULL + [("mcp_talk", 2)]), lead(3, "Gamma Co", [("mcp_docs", 1)], people=0), lead(4, "Delta Co", FULL, route=False),
        lead(5, "Epsilon Co", [("devrel_team", 1)]), lead(6, "Zeta Co", FULL, verdict="drop")]


class Feed(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = self.tmp.name
        self.jobs = os.path.join(d, "speakers-leads-2026-10-30.json")
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
        kw["speakers_rule"]["posting"] = posting
        p = os.path.join(self.tmp.name, f"kw-{posting}.json")
        with open(p, "w") as f:
            json.dump(kw, f)
        return p

    def run_feed(self, *args, posting="off"):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = speakers_feed.main(["--jobs", self.jobs, "--keywords", self.rules(posting), "--state", self.state, *args])
        return code, out.getvalue()

    def test_the_default_is_a_dry_run_that_sends_nothing_reads_no_webhook_and_leaves_no_memory(self):
        code, out = self.run_feed()
        self.assertEqual(code, 0)
        self.assertIn("DRY RUN: nothing was sent and no webhook was read.", out)
        self.assertIn("posting to #speakers is OFF", out)
        self.assertTrue(all(s[0] is False and s[1] == "speakers" and s[2] == "Speakers: " for s in self.sent))
        self.assertFalse(os.path.exists(self.state))

    def test_a_company_is_one_line_with_its_mcp_score_and_both_links_and_no_person(self):
        _, out = self.run_feed()
        self.assertIn("**Beta Co**: Beta Co MCP, GA · score 95 · MCP page https://example.test/2/mcp · public route (devrel-page) https://example.test/2/devrel", out)
        self.assertIn("post 2 · unstated 2 · not-mcp 1 · rejected 1", out)
        self.assertNotIn("Delta Co**", out.split("to post:")[1])           # no route: held back
        self.assertNotIn("Gamma Co**", out.split("to post:")[1])           # score 40: held back
        self.assertNotIn("Zeta Co**", out.split("to post:")[1])            # dropped
        self.assertIn("posts by score: Beta Co 95, Alpha Co 90", out)

    def test_what_is_held_back_is_listed_on_request_with_its_reason(self):
        _, out = self.run_feed("--show-unstated")
        self.assertIn("Delta Co", out.split("held back")[1])
        self.assertIn("Gamma Co", out.split("held back")[1])

    def test_sending_is_refused_while_the_rules_say_off_and_a_first_send_needs_post_all(self):
        code, out = self.run_feed("--send", "--post-all")
        self.assertEqual(code, 3)
        self.assertIn('speakers_rule.posting is not "on"', out)
        code, out = self.run_feed("--send", posting="on")
        self.assertEqual(code, 3)
        self.assertIn("--baseline", out)
        self.assertEqual([s for s in self.sent if s[0]], [])

    def test_baseline_then_a_send_posts_nothing_and_a_new_company_is_the_only_one_posted_later(self):
        self.run_feed("--baseline")
        with open(self.state) as f:
            self.assertEqual(sorted(json.load(f)), ["speakers-1", "speakers-2"])
        code, out = self.run_feed("--send", posting="on")
        self.assertIn("Nothing new to post.", out)
        with open(self.jobs) as f:
            data = json.load(f)
        data["records"].append(lead(7, "Eta Co", FULL))
        with open(self.jobs, "w") as f:
            json.dump(data, f)
        code, _ = self.run_feed("--send", posting="on")
        sent = [s for s in self.sent if s[0]]
        self.assertEqual((code, len(sent)), (0, 1))
        self.assertEqual((sent[0][1], sent[0][2]), ("speakers", "Speakers: "))
        self.assertIn("Eta Co", sent[0][4])
        self.assertIn("no person is named here", sent[0][4])
        self.assertNotIn("Alpha Co", sent[0][4])

    def test_a_message_with_an_email_address_is_refused_by_the_safety_check(self):
        rows = [dict(lead(8, "Theta Co", FULL), contact_route={"kind": "devrel-page", "url": "https://example.test/devrel?e=a@b.example"})]
        with open(self.jobs, "w") as f:
            json.dump({"records": rows}, f)
        _, out = self.run_feed()
        self.assertIn("NOT SENT: text contains a local path, email address or webhook URL", out)

    def test_the_default_leads_file_is_the_newest_saved_run(self):
        real = lp.RUNS
        speakers_feed.lp.RUNS = self.tmp.name
        try:
            for day in ("2026-10-29", "2026-10-30"):
                os.makedirs(os.path.join(self.tmp.name, day))
                with open(os.path.join(self.tmp.name, day, f"speakers-leads-{day}.json"), "w") as f:
                    json.dump({"records": []}, f)
            self.assertTrue(speakers_feed.newest_leads().endswith("speakers-leads-2026-10-30.json"))
        finally:
            speakers_feed.lp.RUNS = real


if __name__ == "__main__":
    unittest.main()
