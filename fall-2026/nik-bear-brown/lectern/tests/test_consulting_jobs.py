#!/usr/bin/env python3
"""Tests for the consulting judge (collect/consulting_jobs.py + keywords.json consulting_rule) and the collector. No network."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import contextlib, copy, io, json, os, tempfile, unittest

import collect
import consulting_collect
import consulting_jobs as cj

with open(lp.config("keywords.json")) as _f:
    KW = json.load(_f)
with open(lp.config("targets.json")) as _f:
    DOC = json.load(_f)


def judge(title, location="Boston, Massachusetts, United States", kw=KW):
    return cj.judge_consulting({"id": "x:1", "company": "Some Firm", "title": title, "url": "https://jobs.example.test/1", "location_text": location}, kw)


class Judge(unittest.TestCase):
    def test_a_role_word_and_an_explicit_early_sign_is_posted_and_says_why(self):
        r = judge("2027 Research Analyst - Competition - London", "London, England, United Kingdom")
        self.assertEqual(r["decision"], "post")
        self.assertEqual(r["reason"], "'research analyst' in the title; early sign: '2027'")

    def test_every_kind_of_early_sign_the_research_found(self):
        for title in ("Summer 2027 Transaction Advisory Services Intern", "Associate Consultant, September 2027 - Transformation", "Digital Advisory Associate (Sept 2027 Graduate Programme)",
                      "Research Analyst Graduate Program - Sydney", "Junior Consultant", "Energy Analyst Intern (Economics)", "University Associate, Disputes & Economics",
                      "Analyst, Campus Hire", "Strategy Analyst (Entry Level)", "Stage Consultant - 6 mois", "Analyst Trainee"):
            self.assertEqual(judge(title, "Paris, France")["decision"], "post", title)

    def test_a_bare_analyst_associate_or_consultant_is_held_back_not_posted(self):
        for title in ("Business Analyst", "Associate", "Consultant", "Human Capital Consultant", "Strategy Advisor", "SAP Finance Consultant - 100% onsite in St. Louis, MO"):
            r = judge(title)
            self.assertEqual(r["decision"], "unstated", title)
            self.assertIn("held back", r["reason"])

    def test_a_level_that_is_not_early_career_wins_even_beside_an_early_word(self):
        for title in ("Senior Consultant", "Senior Associate", "Associate Director, Strategy", "Consulting Manager", "Managing Consultant", "Partner, Consulting",
                      "Principal Analyst", "Consultant II", "Summer Associate to Senior Consultant Track"):
            r = judge(title)
            self.assertEqual(r["decision"], "senior-or-mid", title)
            self.assertTrue(r["reason"].startswith("not early career: "), title)

    def test_roles_that_are_not_consulting_are_named_as_such(self):
        for title, word in (("Associate Software Engineer-Hire-to-Train Program", "software"), ("Clinical Research Associate", "clinical research"), ("Service Desk Support Analyst", "service desk"),
                            ("Attack Sensing & Warning Analyst Junior", "attack sensing"), ("Business Analyst / Tester", "tester"), ("Business & Office Management Intern, Associate", "office management"),
                            ("Tax Associate, Business Incentives Group - Summer 2027 (Atlanta)", "tax"), ("Assurance Intern, Risk Advisory Services - Summer 2027 (Boston)", "assurance"),
                            ("Audit Associate - Fall 2027", "audit")):
            r = judge(title)
            self.assertEqual((r["decision"], r["reason"]), ("not-consulting", f"not a consulting role: '{word}' in the title"), title)

    def test_tax_audit_and_assurance_are_whole_words_and_the_firm_is_not_read(self):
        # added 2026-11-04: 14 of the 21 posts the Oracle boards gave were BDO tax and assurance campus roles, audit and tax work, not consulting
        self.assertEqual(judge("Taxonomy Analyst Intern")["decision"], "post")
        r = cj.judge_consulting({"id": "x", "company": "Tax Audit Assurance Partners", "title": "Summer Analyst Intern", "url": "u", "location_text": "Boston, MA, United States"}, KW)
        self.assertEqual(r["decision"], "post")
        for w in ("assurance", "audit", "tax"):
            self.assertIn(w, KW["consulting_rule"]["not_consulting_words"])

    def test_a_clearance_in_the_title_is_vetoed_whatever_the_level(self):
        for title in ("Cleared Change Management Consultant", "Data Analyst in California (Secret Cleared)", "Junior Analyst, TS/SCI with Polygraph", "Consultant - Active Secret Clearance required", "Analyst, Public Trust"):
            r = judge(title)
            self.assertEqual(r["decision"], "rejected", title)
            self.assertTrue(r["reason"].startswith("clearance in the title: "), title)

    def test_without_the_veto_the_same_title_is_judged_on_its_level(self):
        kw = copy.deepcopy(KW)
        kw["consulting_rule"]["clearance_words"] = []
        self.assertEqual(judge("Cleared Change Management Consultant", kw=kw)["decision"], "unstated")
        self.assertEqual(judge("Junior Analyst, TS/SCI", kw=kw)["decision"], "post")

    def test_the_country_gate_treats_consulting_offices_like_every_other_posting(self):
        r = judge("Internship Strategy Consulting (m/f/d)", "Stockholm, Sweden")
        self.assertEqual((r["decision"], r["reason"]), ("rejected", "country not allowed: Sweden"))
        self.assertEqual(judge("2027 Research Analyst - International Arbitration - Singapore", "Singapore")["decision"], "rejected")
        for place in ("Paris, France", "Milan, Italy", "São Paulo, Brazil", "Lisbon, Portugal", "London, England, United Kingdom", "Sydney, New South Wales, Australia", "Toronto, Ontario, Canada"):
            self.assertEqual(judge("Summer Analyst Intern", place)["decision"], "post", place)

    def test_consulting_allows_five_more_countries_than_the_main_rule_and_the_main_rule_is_not_changed(self):
        # added 2026-11-05 (Professor Bear: a longer country list for consulting): the five countries whose early-sign titles the main list had dropped
        self.assertEqual(KW["consulting_rule"]["extra_allowed_countries"], ["Germany", "Netherlands", "Norway", "Poland", "Spain"])
        for place in ("Munich, Germany", "Amsterdam, Netherlands", "Oslo, Norway", "Warsaw, Poland", "Madrid, Spain"):
            r = judge("Summer Analyst Intern", place)
            self.assertEqual(r["decision"], "post", place)
        self.assertEqual(judge("Summer Analyst Intern", "Stockholm, Sweden")["decision"], "rejected")
        self.assertEqual(collect.where("Munich, Germany", KW["location_rule"])["decision"], "outside")      # the main rule's own list is untouched
        self.assertNotIn("Germany", KW["location_rule"]["allowed_countries"])
        kw = copy.deepcopy(KW)
        kw["consulting_rule"]["extra_allowed_countries"] = []
        self.assertEqual(judge("Summer Analyst Intern", "Munich, Germany", kw=kw)["decision"], "rejected")

    def test_audit_remediation_is_consulting_but_an_audit_title_is_not(self):
        # added 2026-11-05 (Professor Bear: Audit Remediation counts as consulting); 'audit' stays a not-consulting word for every other title
        self.assertEqual(KW["consulting_rule"]["not_consulting_exceptions"], ["audit remediation"])
        self.assertEqual(judge("Audit Remediation Analyst")["decision"], "unstated")
        self.assertEqual(judge("Summer 2027 Audit Remediation Analyst")["decision"], "post")
        self.assertEqual(judge("Senior Audit Remediation Analyst")["decision"], "senior-or-mid")
        for title in ("Audit Associate - Fall 2027", "Audit Analyst Intern, Summer 2027"):
            r = judge(title)
            self.assertEqual((r["decision"], r["reason"]), ("not-consulting", "not a consulting role: 'audit' in the title"), title)
        # an exception cancels only the word it contains: 'tax' beside it still counts
        self.assertEqual(judge("Tax and Audit Remediation Analyst Intern")["decision"], "not-consulting")

    def test_the_k12_gate_applies_here_too(self):
        r = judge("K-12 Education Consultant Intern")
        self.assertEqual(r["decision"], "rejected")
        self.assertTrue(r["reason"].startswith("K-12 role"))

    def test_early_stage_is_not_an_internship_and_words_are_whole_words(self):
        self.assertEqual(judge("Early Stage Consultant")["decision"], "unstated")
        for title in ("Product Designer Intern", "Account Executive, Summer Sales", "Opportunity Lead"):
            self.assertEqual(judge(title)["decision"], "no-match", title)

    def test_the_company_name_is_not_read(self):
        r = cj.judge_consulting({"id": "x", "company": "Consulting Associates Group", "title": "Software Engineer Intern", "url": "u", "location_text": "Boston, MA"}, KW)
        self.assertEqual(r["decision"], "no-match")


class Collector(unittest.TestCase):
    def test_the_boards_it_reads_are_the_kept_firms_of_targets_json_and_none_is_on_the_watch_list(self):
        boards = consulting_collect.boards_from_targets(DOC)
        self.assertEqual(sorted(b[0] for b in boards), ["ABS Group", "Abt Associates", "Accenture Federal Services", "Alira Health", "Altman Solon", "Analysys Mason", "Ankura", "BDO", "BDO (campus site)", "Baringa",
                                                        "Berkeley Research Group", "Brattle Group", "Guidehouse", "Hexaware Technologies", "Huron Consulting", "The Hackett Group (incl. Archstone Consulting)"])
        self.assertEqual({b[1] for b in boards}, {"greenhouse", "smartrecruiters", "workday", "oracle"})
        with open(lp.config("sources.json")) as f:
            sources = json.load(f)
        watched = {b["company"] for s in sources["sources"] for b in s["boards"]}
        self.assertFalse({b[0] for b in boards} & watched)

    def test_a_greenhouse_list_and_a_smartrecruiters_list_become_one_shape(self):
        gh = consulting_collect.records("greenhouse", "Brattle Group", "thebrattlegroup", {"jobs": [{"id": 1, "title": "2027 Research Analyst", "absolute_url": "https://x.test/1", "location": {"name": "Boston"}, "updated_at": "2026-10-01T10:00:00-04:00"}]})
        sr = consulting_collect.records("smartrecruiters", "Analysys Mason", "AnalysysMason1", {"jobs": [{"id": "77", "name": "Associate Consultant", "location": {"city": "London", "country": "gb"}, "releasedDate": "2026-10-02T00:00:00.000Z"}]})
        self.assertEqual((gh[0]["source"], gh[0]["title"], gh[0]["location_text"], gh[0]["date_posted"]), ("greenhouse", "2027 Research Analyst", "Boston", "2026-10-01"))
        self.assertEqual((sr[0]["url"], sr[0]["location_text"]), ("https://jobs.smartrecruiters.com/AnalysysMason1/77", "London, GB"))
        self.assertEqual(cj.posting_view(gh[0])["id"], "greenhouse:1")

    def test_one_board_failing_does_not_stop_the_others_and_all_failing_writes_nothing(self):
        real = consulting_collect.fetch_list
        with tempfile.TemporaryDirectory() as d:
            def fake(provider, slug):
                if slug == "baringa":
                    raise OSError("down")
                if provider == "workday":
                    return {"total": 1, "complete": True, "jobs": [{"title": "Junior Analyst", "externalPath": "/job/Boston/Junior-Analyst_1", "locationsText": "Boston, MA", "bulletFields": ["1"]}]}
                if provider == "oracle":
                    return {"total": 1, "complete": True, "jobs": [{"Id": "9", "Title": "Junior Analyst", "PostedDate": "2026-11-02", "PrimaryLocation": "Boston, MA, United States", "secondaryLocations": []}]}
                return {"jobs": [{"id": 5, "title": "Junior Analyst", "absolute_url": "u", "location": {"name": "London"}}]} if provider == "greenhouse" else {"jobs": []}
            consulting_collect.fetch_list = fake
            consulting_collect.PAUSE = 0
            try:
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(consulting_collect.main(["--out", d]), 0)
                    out = [f for f in os.listdir(d) if f.startswith("consulting-jobs-")][0]
                    with open(os.path.join(d, out)) as f:
                        data = json.load(f)
                    self.assertEqual({s["company"] for s in data["sources"] if s["status"] == "unavailable"}, {"Baringa"})
                    self.assertGreaterEqual(len(data["records"]), 3)
                    consulting_collect.fetch_list = lambda p, s: (_ for _ in ()).throw(OSError("down"))
                    self.assertEqual(consulting_collect.main(["--out", os.path.join(d, "none")]), 3)
            finally:
                consulting_collect.fetch_list = real
                consulting_collect.PAUSE = 1.2


if __name__ == "__main__":
    unittest.main()
