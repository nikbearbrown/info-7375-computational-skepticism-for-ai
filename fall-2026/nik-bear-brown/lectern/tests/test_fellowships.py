#!/usr/bin/env python3
"""Tests for the fellowships channel: collect/fellowships_collect.py (find the deadline sentence, robots, fall back to the recorded date),
collect/fellowships_judge.py (research kinds only, open deadlines only) and publish/fellowships_feed.py (the same three locks as the other
channels, a moved deadline posts again, nothing is sent). No network: the fetcher, Discord and the webhook file are stand-ins."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import contextlib, copy, datetime as dt, io, json, os, tempfile, unittest

import fellowships_collect as fc
import fellowships_judge as fj
import fellowships_feed
import notify

with open(lp.config("keywords.json"), encoding="utf-8") as _f:
    KW = json.load(_f)
with open(lp.config("targets.json"), encoding="utf-8") as _f:
    DOC = json.load(_f)
FUTURE = (dt.date.today() + dt.timedelta(days=20)).isoformat()
PAST = (dt.date.today() - dt.timedelta(days=2)).isoformat()


def target(read="page", deadline="2026-11-22", kind="research-residency", i="fellowships-x"):
    return {"id": i, "name": "Test Residency", "section": "fellowships", "status": "active", "data": [{"label": "p", "url": "https://example.test/prog/"}],
            "fellowships": {"kind": kind, "organization": "Example Lab", "place": "Anywhere", "read": read, "deadline_listed": deadline, "deadline_source": "made up", "eligibility": "anyone"}}


def fetcher(pages, robots="User-agent: *\nDisallow: /private\n"):
    def get(url, timeout=30):
        if url.endswith("/robots.txt"):
            if robots is None:
                raise OSError("403")
            return 200, robots
        if url in pages:
            return 200, pages[url]
        raise OSError("404")
    return get


class Deadline(unittest.TestCase):
    def test_a_date_after_a_deadline_cue_is_read(self):
        self.assertEqual(fc.find_deadline("Applications for this round close on November 22, 2026. Apply here."), "2026-11-22")
        self.assertEqual(fc.find_deadline("Deadline: March 3 2027 at noon"), "2027-03-03")
        self.assertEqual(fc.find_deadline("Please apply by January 12, 2026"), "2026-01-12")

    def test_a_date_with_no_cue_or_across_a_sentence_is_not_a_deadline(self):
        self.assertEqual(fc.find_deadline("The round opened on October 19, 2026 and runs to July 2, 2027."), "")
        self.assertEqual(fc.find_deadline("Applications close soon. Results come on December 4, 2026."), "")

    def test_an_impossible_date_is_skipped_for_the_next_one(self):
        self.assertEqual(fc.find_deadline("closes on February 31, 2026; the deadline is March 1, 2027"), "2027-03-01")

    def test_scripts_and_tags_are_not_text(self):
        t = fc.page_text("<html><script>var close = 'May 5, 2030'</script><p>Applications <b>close</b> on May 9, 2027.</p></html>")
        self.assertEqual(fc.find_deadline(t), "2027-05-09")


class Reading(unittest.TestCase):
    def read(self, t, pages, robots="User-agent: *\nDisallow: /private\n"):
        return fc.read_program(t, fetcher(pages, robots), pause=0)

    def test_the_page_date_is_used_and_a_difference_from_the_recorded_date_is_noted(self):
        r = self.read(target(deadline="2026-11-20"), {"https://example.test/prog/": "<p>Applications close on November 22, 2026.</p>"})
        self.assertEqual((r["deadline"], r["deadline_basis"]), ("2026-11-22", "page"))
        self.assertIn("2026-11-20", r["note"])
        self.assertEqual(r["id"], "fellowships-x:2026-11-22")

    def test_a_page_with_no_deadline_sentence_keeps_the_recorded_date_marked_listed(self):
        r = self.read(target(), {"https://example.test/prog/": "<p>Welcome.</p>"})
        self.assertEqual((r["deadline"], r["deadline_basis"]), ("2026-11-22", "listed"))

    def test_a_robots_file_that_cannot_be_read_or_disallows_means_the_page_is_not_fetched(self):
        t = target()
        t["data"][0]["url"] = "https://example.test/private/prog"
        asked = []
        base = fetcher({"https://example.test/private/prog": "<p>closes on May 1, 2027</p>"})
        def spy(url, timeout=30):
            asked.append(url)
            return base(url, timeout)
        r = fc.read_program(t, spy, pause=0)
        self.assertEqual(r["deadline_basis"], "listed")
        self.assertEqual(asked, ["https://example.test/robots.txt"])
        r = self.read(target(), {"https://example.test/prog/": "<p>closes on May 1, 2027</p>"}, robots=None)
        self.assertEqual((r["deadline"], r["deadline_basis"]), ("2026-11-22", "listed"))

    def test_a_program_marked_read_none_is_never_fetched(self):
        def boom(url, timeout=30):
            raise AssertionError("fetched " + url)
        r = fc.read_program(target(read="none"), boom, pause=0)
        self.assertEqual((r["deadline"], r["deadline_basis"]), ("2026-11-22", "listed"))

    def test_a_program_with_no_date_anywhere_is_unread_and_never_invented(self):
        r = fc.read_program(target(read="none", deadline=""), None, pause=0)
        self.assertEqual((r["deadline"], r["deadline_basis"]), ("", "unread"))

    def test_a_redirect_off_the_host_or_to_http_is_refused(self):
        class R(fc._SameHost):
            pass
        h = R("example.test")
        class Req:
            full_url = "https://example.test/a"
        with self.assertRaises(fc._Sink):
            h.redirect_request(Req(), None, 308, "", {}, "https://elsewhere.test/a")
        with self.assertRaises(fc._Sink):
            h.redirect_request(Req(), None, 308, "", {}, "http://example.test/a")


class Judging(unittest.TestCase):
    def view(self, **kw):
        return dict({"kind": "research-residency", "deadline": FUTURE, "deadline_basis": "page"}, **kw)

    def test_a_research_kind_with_an_open_deadline_is_posted(self):
        self.assertEqual(fj.judge_fellowship(self.view(), KW)["decision"], "post")
        self.assertEqual(fj.judge_fellowship(self.view(deadline=dt.date.today().isoformat()), KW)["decision"], "post")      # the last day is still open

    def test_every_other_case_is_held_back_with_a_reason(self):
        for kind in ("founder-program", "accelerator", "school"):
            self.assertEqual(fj.judge_fellowship(self.view(kind=kind), KW)["decision"], "not-research", kind)
        self.assertEqual(fj.judge_fellowship(self.view(deadline=PAST), KW)["decision"], "closed")
        self.assertEqual(fj.judge_fellowship(self.view(deadline=""), KW)["decision"], "no-deadline")
        self.assertEqual(fj.judge_fellowship(self.view(deadline="soon"), KW)["decision"], "no-deadline")
        self.assertIn("passed", fj.judge_fellowship(self.view(deadline=PAST), KW)["reason"])

    def test_the_rule_posts_to_professor_bear_since_the_go_of_2026_11_05(self):
        r = KW["fellowships_rule"]
        self.assertEqual((r["posting"], r["channel"]), ("on", "professor-bear"))
        self.assertEqual(set(r["kinds"]), {"research-residency", "research-fellowship", "postdoctoral-fellowship"})


class TheList(unittest.TestCase):
    def test_only_research_programs_are_active_and_the_others_are_dropped_with_a_reason(self):
        fel = [t for t in DOC["targets"] if t["section"] == "fellowships"]
        self.assertEqual(len(fel), 6)
        for t in fel:
            if t["status"] == "active":
                self.assertIn(t["fellowships"]["kind"], KW["fellowships_rule"]["kinds"], t["id"])
                self.assertTrue(t["fellowships"]["deadline_listed"], t["id"])
            else:
                self.assertEqual(t["status"], "dropped")
                self.assertIn("Dropped 2026-11-05", t["status_note"], t["id"])
                self.assertNotIn(t["fellowships"]["kind"], KW["fellowships_rule"]["kinds"], t["id"])
        self.assertEqual(sorted(t["id"] for t in fel if t["status"] == "active"), ["fellowships-anthropic-residency", "fellowships-cmu-ai4bio"])

    def test_the_programs_cannot_reach_the_job_feed_watch_list(self):
        boards = {t["name"] for t in DOC["targets"] if t["section"] == "boards"}
        self.assertFalse(boards & {t["name"] for t in DOC["targets"] if t["section"] == "fellowships"})
        self.assertEqual({t["id"] for t in fc.programs_from_targets(DOC)}, {"fellowships-anthropic-residency", "fellowships-cmu-ai4bio"})

    def test_a_program_page_a_script_reads_is_on_https_and_only_one_host_is_read(self):
        hosts = {fc.urlparse(t["data"][0]["url"]).hostname for t in DOC["targets"] if t["section"] == "fellowships" and t["status"] == "active" and t["fellowships"]["read"] == "page"}
        self.assertEqual(hosts, {"alignment.anthropic.com"})
        for t in DOC["targets"]:
            if t["section"] == "fellowships" and t["status"] == "active" and t["fellowships"]["read"] == "page":
                self.assertTrue(t["data"][0]["url"].startswith("https://"))


class Feed(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = self.tmp.name
        self.jobs = os.path.join(d, "fellowships-test.json")
        self.write([fc.record(target(deadline=FUTURE), FUTURE, "page"),
                    fc.record(target(i="fellowships-y", deadline=FUTURE, kind="founder-program"), FUTURE, "listed"),
                    fc.record(target(i="fellowships-z", deadline=PAST), PAST, "listed")])
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

    def write(self, recs):
        with open(self.jobs, "w", encoding="utf-8") as f:
            json.dump({"records": recs}, f)

    def rules(self, posting):
        kw = copy.deepcopy(KW)
        kw["fellowships_rule"]["posting"] = posting
        p = os.path.join(self.tmp.name, f"kw-{posting}.json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(kw, f)
        return p

    def run_feed(self, *args, posting="off"):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = fellowships_feed.main(["--jobs", self.jobs, "--keywords", self.rules(posting), "--state", self.state, *args])
        return code, out.getvalue()

    def test_the_default_is_a_dry_run_that_sends_nothing_reads_no_webhook_and_leaves_no_memory(self):
        code, out = self.run_feed()
        self.assertEqual(code, 0)
        self.assertIn("DRY RUN: nothing was sent and no webhook was read.", out)
        self.assertIn("posting to #professor-bear is OFF", out)
        self.assertTrue(all(s[0] is False and s[1] == "professor-bear" and s[2] == "Fellowships: " for s in self.sent))
        self.assertFalse(os.path.exists(self.state))

    def test_only_the_open_research_program_is_a_post_and_a_listed_date_says_so(self):
        _, out = self.run_feed()
        self.assertIn("post 1 · closed 1 · no-deadline 0 · not-research 1", out)
        line = out.split("to post:")[1]
        self.assertIn("**Example Lab**: Test Residency · research residency · deadline", line)
        self.assertNotIn("as listed", line)                       # the one posted program was read from its page
        self.write([fc.record(target(deadline=FUTURE), FUTURE, "listed")])
        _, out = self.run_feed()
        self.assertIn("as listed", out.split("to post:")[1])

    def test_sending_is_refused_while_the_rules_say_off_and_a_first_send_needs_post_all(self):
        code, out = self.run_feed("--send", "--post-all")
        self.assertEqual(code, 3)
        self.assertIn('fellowships_rule.posting is not "on"', out)
        code, out = self.run_feed("--send", posting="on")
        self.assertEqual(code, 3)
        self.assertIn("--baseline", out)
        self.assertEqual([s for s in self.sent if s[0]], [])

    def test_a_moved_deadline_is_posted_again_and_an_unchanged_one_is_not(self):
        self.run_feed("--baseline")
        code, out = self.run_feed("--send", posting="on")
        self.assertIn("Nothing new to post.", out)
        later = (dt.date.fromisoformat(FUTURE) + dt.timedelta(days=7)).isoformat()
        self.write([fc.record(target(deadline=later), later, "page")])
        code, _ = self.run_feed("--send", posting="on")
        sent = [s for s in self.sent if s[0]]
        self.assertEqual((code, len(sent)), (0, 1))
        self.assertEqual((sent[0][1], sent[0][2]), ("professor-bear", "Fellowships: "))
        self.assertIn("Nothing is sent to a program", sent[0][4])
        code, out = self.run_feed("--send", posting="on")
        self.assertIn("Nothing new to post.", out)

    def test_a_message_with_an_email_address_is_refused_by_the_safety_check(self):
        bad = fc.record(target(deadline=FUTURE), FUTURE, "page")
        bad["url"] = "https://example.test/prog?e=a@b.example"
        self.write([bad])
        _, out = self.run_feed()
        self.assertIn("NOT SENT: text contains", out)


if __name__ == "__main__":
    unittest.main()
