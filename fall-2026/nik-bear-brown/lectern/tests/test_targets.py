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
SECTIONS = {"boards", "bigfour", "unreachable", "schools", "research", "games", "consulting", "speakers", "federal508"}
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

    def test_the_game_studios_and_consulting_firms_cannot_leak_into_the_watch_list_for_the_education_feed(self):
        sources = json.load(open(lp.config("sources.json"), encoding="utf-8"))
        watched = {b["company"] for s in sources["sources"] for b in s["boards"]}
        removed = set(k for k in sources["removed"] if k != "_comment")
        unreachable = {u["company"] for u in sources["unreachable"]}
        for section in ("games", "consulting", "federal508"):
            names = {t["name"] for t in T if t["section"] == section}
            self.assertTrue(names, section)
            for other in (watched, removed, unreachable):
                self.assertFalse(names & other, (section, names & other))
        # the speakers list is different on purpose: Figma, Canva, Miro and Notion are on the #professor-bear watch list AND ship an MCP, and several
        # companies removed from it for not being educational AI (GitLab, Vercel, Supabase, Twilio ...) or with no data source (Salesforce, GitHub ...) ship one
        # too, so names are not compared. Being on the speakers list changes nothing about the watch list: the generator reads only `boards`.
        # the generator turns only the `boards` section into the watch list: nothing in these sections may carry its other triggers
        for t in T:
            if t["section"] in ("games", "consulting", "speakers", "federal508"):
                self.assertNotIn("unreachable", t, t["id"])
                self.assertNotEqual(t["status"], "removed", t["id"])

    def test_a_consulting_firm_carries_a_verdict_a_status_to_match_and_what_the_research_found(self):
        firms = [t for t in T if t["section"] == "consulting"]
        self.assertGreaterEqual(len(firms), 60)
        for t in firms:
            c = t["consulting"]
            self.assertIn(c["verdict"], ("keep", "drop", "to-do"), t["id"])
            self.assertIn(t["status"], {"keep": ("active",), "drop": ("dropped",), "to-do": ("no-reader", "unreadable")}[c["verdict"]], t["id"])
            self.assertTrue(t["why"] and c["feed_names"], t["id"])
            self.assertNotIn("h1b", json.dumps(t).lower(), t["id"])           # a third party's unsourced flag is not stored anywhere
            if c["verdict"] == "keep":
                self.assertIn(t["provider"], ("greenhouse", "ashby", "smartrecruiters", "workday"), t["id"])
                self.assertTrue(t["data"] and c["board"]["slug"], t["id"])
            if c["verdict"] == "to-do":
                self.assertTrue(t["todo"], t["id"])
        self.assertEqual(sum(1 for t in firms if t["status"] == "active"), 10)

    def test_a_federal_508_employer_carries_a_verdict_a_status_to_match_a_kind_and_what_the_research_found(self):
        emps = [t for t in T if t["section"] == "federal508"]
        self.assertGreaterEqual(len(emps), 60)
        self.assertEqual(len({t["name"] for t in emps}), len(emps))
        for t in emps:
            f = t["federal508"]
            self.assertEqual(t["type"], "federal-508-employer", t["id"])
            self.assertIn(f["verdict"], ("keep", "drop", "to-do"), t["id"])
            self.assertIn(t["status"], {"keep": ("active",), "drop": ("dropped",), "to-do": ("no-reader", "unreadable", "unchecked")}[f["verdict"]], t["id"])
            self.assertIn(f["kind"], ("federal-contractor", "civic-tech", "accessibility-specialist", "agency"), t["id"])
            self.assertTrue(t["why"] and f["feed_names"] and f["researched"], t["id"])
            if f["verdict"] == "keep":
                self.assertIn(t["provider"], ("greenhouse", "ashby", "smartrecruiters", "workday", "usajobs"), t["id"])
                self.assertTrue(f["board"]["slug"] and f["board"]["provider"] == t["provider"], t["id"])
                self.assertTrue([k for k in f if k.startswith("postings_20") and isinstance(f[k], int)], t["id"])
            if f["verdict"] == "to-do":
                self.assertTrue(t["todo"], t["id"])
        self.assertEqual(sum(1 for t in emps if t["status"] == "active"), 22)

    def test_the_federal_508_list_names_no_person_and_holds_no_email_address(self):
        import re
        text = json.dumps([t for t in T if t["section"] == "federal508"], ensure_ascii=False)
        self.assertFalse(re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", text))
        self.assertNotIn("mailto:", text)

    def test_a_speaker_company_carries_an_mcp_with_its_own_source_signals_with_links_and_a_status_to_match(self):
        cos = [t for t in T if t["section"] == "speakers"]
        self.assertGreaterEqual(len(cos), 60)
        self.assertEqual(len({t["name"] for t in cos}), len(cos))
        for t in cos:
            s = t["speakers"]
            self.assertIn(s["verdict"], ("keep", "drop", "to-do"), t["id"])
            self.assertIn(t["status"], {"keep": ("active",), "drop": ("dropped",), "to-do": ("unchecked",)}[s["verdict"]], t["id"])
            self.assertEqual(t["type"], "mcp-company", t["id"])
            self.assertTrue(t["why"] and s["product"] and s["researched"], t["id"])
            if s["verdict"] != "drop":
                self.assertTrue(s["mcp"]["name"] and s["mcp"]["primary_source"].startswith("https://"), t["id"])
                self.assertIn("mcp_docs", [g["kind"] for g in s["signals"]], t["id"])
            for g in s["signals"] + ([s["contact_route"]] if s["contact_route"] else []):
                self.assertTrue(g["url"].startswith("https://"), (t["id"], g))
                self.assertIsInstance(g["opened"], bool, (t["id"], g))
            self.assertIsInstance(s["people_found"], int, t["id"])

    def test_the_public_list_names_no_person_and_holds_no_email_address_or_phone_number(self):
        import re
        text = json.dumps([t for t in T if t["section"] == "speakers"], ensure_ascii=False)
        self.assertFalse(re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", text))
        self.assertFalse(re.search(r"(?<!\d)(\+\d{1,3}[ -])?\(?\d{3}\)?[ -]\d{3}[ -]\d{4}(?!\d)", re.sub(r"https?://\S+", "", text)))
        self.assertNotIn("mailto:", text)
        self.assertFalse([k for t in T if t["section"] == "speakers" for k in t["speakers"] if k in ("people", "person", "names", "email", "phone")])
        folder = os.path.join(lp.ROOT, "speaker-records")                      # the local records name people: if they are here, none of the names may leak
        import glob
        recs = [json.loads(l) for p in glob.glob(os.path.join(folder, "people-*.jsonl")) for l in open(p, encoding="utf-8") if l.strip()]
        if not recs:
            self.skipTest("no local speaker-records/ on this machine: the names cannot be checked here")
        low = text.lower()
        leaked = [r["name"] for r in recs if len(r["name"].split()[-1]) > 3 and re.search(r"(?<![a-z])" + re.escape(r["name"].split()[-1].lower()) + r"(?![a-z])", low)]
        self.assertEqual(leaked, [])

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
