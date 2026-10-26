#!/usr/bin/env python3
"""Tests for the two gates in collect.judge(): location_rule (allowed countries) and k12_rule. No network.

The gates only ever drop a posting the keywords would have kept, and every drop says why. The cases below are real
shapes of location lines and titles from the saved boards, with made-up companies."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import copy, json, unittest

import collect

KW = json.load(open(lp.config("keywords.json")))
RULE = KW["location_rule"]


def view(title, location, text="Teach people to use the product.", company="Acme"):
    return {"company": company, "title": title, "text": text, "location_text": location}


def decision(location):
    return collect.where(location, RULE)


class Location(unittest.TestCase):
    def test_the_posting_that_prompted_the_rule_is_rejected_for_both_reasons(self):
        m, why = collect.judge(view("K12 Education Account Manager, South Korea (12 months contract)",
                                    "Seoul, Seoul, Korea, republic of"), KW)
        self.assertIsNone(m)
        self.assertEqual(why, "country not allowed: South Korea; K-12 role: 'k12' in the title")

    def test_each_allowed_country_is_kept(self):
        for place in ("Austin, TX", "Remote - United States", "US-Remote", "London, UK", "Toronto, Ontario, Canada", "Sydney, NSW, Australia",
                      "Auckland, New Zealand", "Dublin, Ireland", "Paris, France", "Milan, Italy", "São Paulo, Brazil", "Lisbon, Portugal"):
            self.assertEqual(decision(place)["decision"], "allowed", place)
            m, _ = collect.judge(view("Education Lead", place), KW)
            self.assertIsNotNone(m, place)
            self.assertIsNone(m["location"], place)

    def test_countries_that_are_not_on_the_list_are_rejected_with_the_country_named(self):
        for place, country in (("Tokyo, Japan", "Japan"), ("Remote - Germany", "Germany"), ("Bengaluru", "India"), ("Singapore", "Singapore"),
                               ("Mexico City", "Mexico"), ("Seoul, South Korea", "South Korea")):
            m, why = collect.judge(view("Education Lead", place), KW)
            self.assertIsNone(m, place)
            self.assertEqual(why, "country not allowed: " + country, place)

    def test_a_posting_in_several_places_is_allowed_if_any_one_is(self):
        self.assertEqual(decision("Berlin, Germany | Austin, TX")["countries"], ["United States"])
        self.assertEqual(decision("Stockholm · London")["decision"], "allowed")
        self.assertEqual(decision("Tokyo, Japan · Seoul, South Korea")["decision"], "outside")

    def test_remote_with_no_country_is_kept_and_says_so(self):
        for place in ("Remote", "Hybrid", "N/A", "", "Remote - EMEA", "Remote - Europe", "Home based - Worldwide"):
            m, why = collect.judge(view("Education Lead", place), KW)
            self.assertIsNotNone(m, place)
            self.assertIs(m["location"]["country_named"], False, place)

    def test_remote_in_a_region_of_countries_is_read_by_its_countries(self):
        self.assertEqual(decision("Remote (United States | Canada)")["countries"], ["Canada", "United States"])
        self.assertEqual(decision("Remote - Japan")["decision"], "outside")
        self.assertEqual(decision("Remote - TX")["decision"], "allowed")
        self.assertEqual(decision("Remote, Canada; Remote, United States")["decision"], "allowed")

    def test_a_foreign_place_beside_one_that_cannot_be_read_is_kept_for_a_person_to_see(self):
        d = decision("Amsterdam, Netherlands · Remote - Europe")
        self.assertEqual(d["decision"], "unnamed")
        self.assertEqual(d["countries"], ["Netherlands"])
        self.assertEqual(decision("Seoul, South Korea · Hybrid")["decision"], "outside")   # 'Hybrid' is not a place

    def test_names_that_are_also_american_towns_follow_the_state_code(self):
        for place in ("Lebanon, PA", "Jamaica, NY", "Athens, GA", "Holland, MI", "Berlin, NH", "Lebanon, OR, United States"):
            self.assertEqual(decision(place)["decision"], "allowed", place)
        for place in ("Beirut, Lebanon", "Kingston, Jamaica", "Athens, Greece", "Amsterdam, Holland", "Berlin, Germany"):
            self.assertEqual(decision(place)["decision"], "outside", place)

    def test_new_mexico_is_not_mexico(self):
        self.assertEqual(decision("Albuquerque, New Mexico")["countries"], ["United States"])
        self.assertEqual(decision("Mexico City, Mexico")["countries"], ["Mexico"])

    def test_the_list_is_the_rules_file_and_nothing_else(self):
        rule = copy.deepcopy(KW)
        rule["location_rule"]["allowed_countries"].append("Japan")
        m, _ = collect.judge(view("Education Lead", "Tokyo, Japan"), rule)
        self.assertIsNotNone(m)
        rule["location_rule"]["if_no_country_named"] = "reject"
        m, why = collect.judge(view("Education Lead", "Remote"), rule)
        self.assertEqual((m, why), (None, "no country named in the location"))

    def test_a_posting_the_keywords_reject_keeps_its_old_reason(self):
        m, why = collect.judge(view("Payments Analyst", "Tokyo, Japan", text="Reconcile payments."), KW)
        self.assertEqual((m, why), (None, "no-keyword-match"))

    def test_a_rules_file_without_the_gates_behaves_as_before(self):
        old = {k: v for k, v in KW.items() if k not in ("location_rule", "k12_rule")}
        m, _ = collect.judge(view("K12 Education Lead", "Tokyo, Japan"), old)
        self.assertIsNotNone(m)
        self.assertIsNone(m["location"])


class K12(unittest.TestCase):
    def test_titles_that_say_k12_in_any_spelling_are_rejected_in_any_country(self):
        for title in ("Education Account Executive - Canvas - K12", "Education Renewal Manager - K-12", "Education Lead (K–12)", "Education Director of Schools K -12",
                      "K-12 Education Account Manager - Partnerships", "Kindergarten Teacher Trainer", "Education Content Creator, Elementary School 3 - 5"):
            m, why = collect.judge(view(title, "Austin, TX"), KW)
            self.assertIsNone(m, title)
            self.assertTrue(why.startswith("K-12 role: "), (title, why))

    def test_k8_the_abbreviation_for_kubernetes_is_not_k12(self):
        for title in ("Staff Backend Engineer - K8 (Envoy) Education Platform", "Support Analyst (Cloud K8) Education"):
            m, _ = collect.judge(view(title, "Austin, TX"), KW)
            self.assertIsNotNone(m, title)

    def test_a_company_called_k12_is_not_a_k12_role_by_its_name(self):
        m, _ = collect.judge(view("Education Lead", "Austin, TX", company="K12"), KW)
        self.assertIsNotNone(m)

    def test_k12_in_the_body_alone_is_not_enough_unless_the_rules_say_so(self):
        text = "Our education work spans higher education and K-12 teachers. Teach the product to partners."
        m, _ = collect.judge(view("Education Lead", "San Francisco, CA", text=text), KW)
        self.assertIsNotNone(m)
        rule = copy.deepcopy(KW)
        rule["k12_rule"]["body_phrases"] = ["k-12"]
        m, why = collect.judge(view("Education Lead", "San Francisco, CA", text=text), rule)
        self.assertEqual((m, why), (None, "K-12 role: 'k-12' in the body"))

    def test_words_that_only_look_like_it_are_kept(self):
        for title in ("Education Lead, Higher Education", "Teacher Education Program Manager", "University Outreach Intern, Education Lead", "Education Lead, Schools Partnerships"):
            m, _ = collect.judge(view(title, "Austin, TX"), KW)
            self.assertIsNotNone(m, title)


if __name__ == "__main__":
    unittest.main()
