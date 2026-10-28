#!/usr/bin/env python3
"""Tests for the judge of the games channel (collect/engine_jobs.py + keywords.json engine_rule). No network."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import copy, json, unittest

import engine_jobs as ej

KW = json.load(open(lp.config("keywords.json")))


def judge(title, location="Austin, TX", kw=KW):
    return ej.judge_engine({"id": "x:1", "company": "Acme Studio", "title": title, "url": "https://jobs.example.test/1", "location_text": location}, kw)


class Match(unittest.TestCase):
    def test_a_game_role_with_an_early_career_word_is_posted_and_says_why(self):
        r = judge("Gameplay Programmer Intern")
        self.assertEqual(r["decision"], "post")
        self.assertEqual(r["reason"], "'gameplay' (game_roles) in the title; early career: 'intern'")

    def test_every_early_career_word_the_pasted_list_implies(self):
        for title in ("Junior Game Designer", "Associate Level Game Designer", "Graduate Technical Artist", "Game Designer I", "Unity Developer (New Grad)",
                      "Godot Developer, Entry-Level", "Tools Programmer Co-op", "Apprentice Technical Artist", "Game Tester"):
            self.assertEqual(judge(title)["decision"], "post", title)

    def test_a_level_that_is_not_early_career_wins_over_an_early_word(self):
        for title in ("Associate Director, Game Design", "Senior Gameplay Programmer", "Lead Technical Artist", "Game Designer II", "Principal Engine Programmer",
                      "Staff Software Engineer, Unreal Ecosystem", "Technical Artist, Sr. Associate"):
            r = judge(title)
            self.assertEqual(r["decision"], "senior-or-mid", title)
            self.assertTrue(r["reason"].startswith("not early career: "), title)

    def test_no_level_word_is_held_back_not_posted(self):
        r = judge("Game Programmer (1 Year Contract)")
        self.assertEqual(r["decision"], "unstated")
        self.assertIn("states no level", r["reason"])

    def test_unity_is_a_word_not_a_substring(self):
        for title in ("Community Manager Intern", "Opportunity Analyst Intern", "Immunity Research Intern", "Unity Catalog Engineer Intern"):
            self.assertEqual(judge(title)["decision"], "no-match", title)
        self.assertEqual(judge("Unity Developer Intern")["decision"], "post")
        self.assertEqual(judge("Unreal Engine Artist Intern")["decision"], "post")

    def test_false_friends_are_blanked(self):
        self.assertEqual(judge("Design Systems Designer Intern")["decision"], "no-match")
        self.assertEqual(judge("Systems Designer Intern")["decision"], "post")

    def test_broad_words_alone_do_not_match(self):
        for title in ("Product Designer Intern", "Producer Intern", "Graphic Designer Intern", "QA Tester Intern", "Games Account Executive, Associate",
                      "Sales Engineer, Gaming (Junior)", "Search Engine Optimization Intern", "3D Print Production Associate", "Simulation Engineer Intern"):
            self.assertEqual(judge(title)["decision"], "no-match", title)

    def test_a_group_that_is_off_is_off_and_one_switch_turns_it_on(self):
        self.assertFalse(KW["engine_rule"]["groups"]["simulation"]["enabled"])
        self.assertEqual(judge("Simulation Engineer Intern")["decision"], "no-match")
        kw = copy.deepcopy(KW)
        kw["engine_rule"]["groups"]["simulation"]["enabled"] = True
        self.assertEqual(judge("Simulation Engineer Intern", kw=kw)["decision"], "post")

    def test_the_company_name_is_not_read(self):
        r = ej.judge_engine({"id": "x:2", "company": "Unity Technologies", "title": "Software Engineer Intern", "url": "u", "location_text": "Austin, TX"}, KW)
        self.assertEqual(r["decision"], "no-match")


class Gates(unittest.TestCase):
    def test_the_country_gate_applies_here_too(self):
        r = judge("Tools Programmer Intern", "Tokyo, Japan")
        self.assertEqual((r["decision"], r["reason"]), ("rejected", "country not allowed: Japan"))
        self.assertEqual(judge("Tools Programmer Intern", "Montreal, Quebec, Canada")["decision"], "post")
        self.assertEqual(judge("Tools Programmer Intern", "Porto Alegre, Rio Grande do Sul, Brazil")["decision"], "post")

    def test_the_k12_gate_applies_here_too(self):
        r = judge("K-12 Game Designer Intern")
        self.assertEqual(r["decision"], "rejected")
        self.assertTrue(r["reason"].startswith("K-12 role"))

    def test_remote_with_no_country_is_kept_as_in_the_main_filter(self):
        self.assertEqual(judge("Game Design Intern", "Remote")["decision"], "post")
        kw = copy.deepcopy(KW)
        kw["location_rule"]["if_no_country_named"] = "reject"
        self.assertEqual(judge("Game Design Intern", "Remote", kw=kw)["decision"], "rejected")

    def test_a_held_back_posting_is_still_gated(self):
        self.assertEqual(judge("Game Programmer", "Seoul, South Korea")["decision"], "rejected")


class Sources(unittest.TestCase):
    def test_the_ai_jobs_shape_and_lecterns_own_shape_give_one_view(self):
        a = ej.posting_view({"id": "greenhouse:epicgames:1", "company": "Epic Games", "title": "Engine Programmer Intern", "url": "u", "locations": ["Cary, NC", "London, UK"]})
        b = ej.posting_view({"source": "greenhouse", "source_id": "1", "company": "Epic Games", "title": "Engine Programmer Intern", "url": "u", "location_text": "Cary, NC · London, UK"})
        self.assertEqual(a["location_text"], b["location_text"])
        self.assertEqual((a["id"], b["id"]), ("greenhouse:epicgames:1", "greenhouse:1"))


if __name__ == "__main__":
    unittest.main()
