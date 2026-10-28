#!/usr/bin/env python3
"""Tests for config/targets.json: the single list of targets, and the files generated from it."""
import json, os, sys, unittest

for _p in (os.path.dirname(os.path.abspath(__file__)), os.path.dirname(os.path.dirname(os.path.abspath(__file__)))):
    if os.path.exists(os.path.join(_p, "lectern_paths.py")):
        sys.path.insert(0, _p)
        break
import lectern_paths as lp

DOC = json.load(open(lp.config("targets.json"), encoding="utf-8"))
T = DOC["targets"]
SECTIONS = {"boards", "bigfour", "unreachable", "schools", "research", "games"}
STATUSES = {"active", "removed", "no-reader", "unreadable", "unchecked", "partial", "read-by-hand", "dropped"}


class Targets(unittest.TestCase):
    def test_ids_are_unique_and_every_target_has_a_valid_type_section_and_status(self):
        ids = [t["id"] for t in T]
        self.assertEqual(len(ids), len(set(ids)))
        for t in T:
            self.assertIn(t["type"], DOC["types"], t["id"])
            self.assertIn(t["section"], SECTIONS, t["id"])
            self.assertIn(t["status"], STATUSES, t["id"])

    def test_every_link_is_https_and_a_removed_target_says_why_and_when(self):
        for t in T:
            for d in t["data"]:
                self.assertTrue(d["url"].startswith("https://"), (t["id"], d["url"]))
            if t["status"] == "removed":
                self.assertTrue(t["removed"]["entry"].get("reason"), t["id"])
                self.assertTrue(t["removed"]["on"], t["id"])

    def test_an_active_board_has_a_provider_a_slug_and_both_links(self):
        boards = [t for t in T if t["section"] == "boards" and t["status"] == "active"]
        self.assertTrue(boards)
        for t in boards:
            self.assertIn(t["provider"], ("greenhouse", "ashby", "smartrecruiters"))
            self.assertTrue(t["slug"])
            self.assertEqual([d["label"] for d in t["data"]], ["board page", "API the script calls"])

    def test_the_schools_carry_what_the_faculty_feed_needs(self):
        schools = [t for t in T if t["section"] == "schools"]
        self.assertEqual(len(schools), 21)
        for t in schools:
            self.assertTrue(t["institution"] and t["aliases"], t["id"])

    def test_every_named_reader_is_a_file_that_exists(self):
        for t in T:
            r = (t.get("reader") or "").split(" ")[0]
            if r:
                self.assertTrue(any(os.path.exists(os.path.join(lp.ROOT, sub, r)) for sub in ("", "collect", "publish", "audit")), (t["id"], r))

    def test_the_generated_files_are_in_step_with_targets_json(self):
        import subprocess
        r = subprocess.run([sys.executable, os.path.join(lp.ROOT, "ops", "build_from_targets.py"), "--check"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_a_game_studio_carries_a_verdict_a_feed_name_and_a_reason(self):
        games = [t for t in T if t["section"] == "games"]
        self.assertTrue(games)
        for t in games:
            g = t["games"]
            self.assertIn(g["verdict"], ("keep", "drop", "to-do"), t["id"])
            self.assertEqual(t["status"], {"keep": "active", "drop": "dropped", "to-do": "no-reader"}[g["verdict"]], t["id"])
            self.assertTrue(g["feed_names"] and t["why"], t["id"])

    def test_the_game_studios_cannot_leak_into_the_watch_list_for_the_education_feed(self):
        sources = json.load(open(lp.config("sources.json"), encoding="utf-8"))
        watched = {b["company"] for s in sources["sources"] for b in s["boards"]}
        self.assertFalse(watched & {t["name"] for t in T if t["section"] == "games"})
        self.assertFalse({t["name"] for t in T if t["section"] == "games"} & set(k for k in sources["removed"] if k != "_comment"))

    def test_the_studio_list_the_games_rule_reads_is_the_kept_studios(self):
        import engine_jobs
        studios = engine_jobs.studio_names(DOC)
        self.assertIn("epic games", studios)
        self.assertNotIn("twitch", studios)
        self.assertNotIn("bethesda", studios)
        self.assertEqual(len(studios), sum(1 for t in T if t["section"] == "games" and t["status"] == "active"))

    def test_a_reason_for_every_removal_is_still_visible_to_a_discovery_agent(self):
        removed = [t["name"] for t in T if t["status"] == "removed"]
        self.assertGreaterEqual(len(removed), 12)
        self.assertIn("HubSpot", removed)


if __name__ == "__main__":
    unittest.main()
