#!/usr/bin/env python3
"""Tests for notify.py: what gets posted to the public channel, and what never does."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import json, os, tempfile, unittest

import notify


def row(i, co="Anthropic", title="Educator", **kw):
    r = {"source": "greenhouse", "company": co, "source_id": str(i), "title": title, "location_text": "Remote",
         "url": f"https://jobs.example.com/{i}", "matched": {"role_title": ["educator"], "kept_because": "role word in title"}}
    r.update(kw)
    return r


class Notify(unittest.TestCase):
    def test_unwatched_companies_are_never_posted(self):
        rows, msgs = notify.build_messages([row(1), row(2, co="Stripe")], watched={"Anthropic"})
        self.assertEqual([r["company"] for r in rows], ["Anthropic"])
        self.assertNotIn("Stripe", "".join(msgs))

    def test_priority_companies_come_first(self):
        rows, _ = notify.build_messages([row(1, co="Replit"), row(2, co="Figma"), row(3, co="Anthropic")], {"Replit", "Figma", "Anthropic"})
        self.assertEqual([r["company"] for r in rows], ["Anthropic", "Figma", "Replit"])

    def test_already_posted_listings_are_skipped(self):
        rows, _ = notify.build_messages([row(1), row(2)], {"Anthropic"}, already={"greenhouse:1"})
        self.assertEqual([r["source_id"] for r in rows], ["2"])

    def test_long_lists_are_chunked_and_the_footer_ends_the_last(self):
        _, msgs = notify.build_messages([row(i, title="T" * 90) for i in range(40)], {"Anthropic"})
        self.assertGreater(len(msgs), 1)
        self.assertTrue(all(len(m) <= notify.MAX_CHUNK + 400 for m in msgs))
        self.assertTrue(msgs[-1].endswith(notify.FOOTER))

    def test_newly_watched_companies_are_marked_so_they_are_not_read_as_fresh(self):
        _, msgs = notify.build_messages([row(1, co="Replit")], {"Replit"}, first_time={"Replit"})
        self.assertIn("(newly watched)", msgs[0])

    def test_a_message_with_a_local_path_or_email_is_refused(self):
        self.assertFalse(notify.post("t", "see /Users/someone/file", send=False))
        self.assertFalse(notify.post("t", "write to a.b@example.com", send=True))

    def test_a_post_is_plain_text_so_it_shows_with_embeds_switched_off(self):
        p = notify.payload("3 new", "line one\nline two", prefix="Speakers: ")
        self.assertNotIn("embeds", p)
        self.assertEqual(p["content"], "**Speakers: 3 new**\nline one\nline two")
        self.assertEqual(p["flags"], 4)                                  # SUPPRESS_EMBEDS: no link-preview cards
        self.assertLessEqual(len(notify.payload("t", "x" * 5000)["content"]), 2000)

    def test_a_dry_run_records_nothing_as_posted(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "posted.json")
            n = notify.post_new([row(1)], {"Anthropic"}, set(), p, "run x", send=False)
            self.assertEqual(n, 0)
            self.assertFalse(os.path.exists(p))


def lab(i, tier="great", **kw):
    c = {"lab_id": f"lab-{i}", "display_name": f"Genomics group {i}", "institution": "Broad Institute", "page_url": f"https://labs.example.org/{i}",
         "tier": tier, "kind": "lab", "reason": "Builds tools for single-cell data."}
    c.update(kw)
    return c


class Labs(unittest.TestCase):
    def test_only_great_fits_are_posted_unless_he_widens_it(self):
        rows, _ = notify.build_lab_messages([lab(1), lab(2, tier="pretty_good")])
        self.assertEqual([r["lab_id"] for r in rows], ["lab-1"])
        rows, _ = notify.build_lab_messages([lab(1), lab(2, tier="pretty_good")], tiers=notify.LAB_TIERS)
        self.assertEqual(len(rows), 2)

    def test_people_fields_are_never_read_or_posted(self):
        c = lab(1, pi={"name": "Dr Zed Quux", "email": {"value": "zed@example.org"}}, people={"lab_manager": {"name": "Ann Lee"}})
        _, msgs = notify.build_lab_messages([c])
        text = "".join(msgs)
        for secret in ("Quux", "zed@example.org", "Ann Lee"):
            self.assertNotIn(secret, text)

    def test_a_lab_named_for_a_person_is_shown_by_its_institution_not_the_name(self):
        _, msgs = notify.build_lab_messages([lab(1, display_name="Quux Lab", avoid_names=["Quux"])])
        self.assertNotIn("Quux", msgs[0])
        self.assertIn("A lab at Broad Institute", msgs[0])

    def test_posted_labs_are_skipped_and_the_footer_says_nothing_was_sent(self):
        rows, msgs = notify.build_lab_messages([lab(1), lab(2)], already={"lab-1"})
        self.assertEqual([r["lab_id"] for r in rows], ["lab-2"])
        self.assertTrue(msgs[-1].endswith(notify.LAB_FOOTER))

    def test_a_lab_with_no_page_is_not_posted(self):
        rows, _ = notify.build_lab_messages([lab(1, page_url="")])
        self.assertEqual(rows, [])

    def test_an_email_in_the_reason_blocks_the_post_and_a_dry_run_records_nothing(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "labs.json")
            self.assertEqual(notify.post_labs([lab(1, reason="write to a.b@example.com")], p, send=True), 0)
            self.assertEqual(notify.post_labs([lab(2)], p, send=False), 0)
            self.assertFalse(os.path.exists(p))


if __name__ == "__main__":
    unittest.main()
