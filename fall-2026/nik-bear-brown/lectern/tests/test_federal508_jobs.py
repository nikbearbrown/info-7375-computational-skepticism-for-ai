#!/usr/bin/env python3
"""Tests for the federal-508 judge (collect/federal508_jobs.py + keywords.json federal508_rule) and the collector. No network."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import contextlib, copy, io, json, os, tempfile, unittest

import federal508_collect
import federal508_jobs as fj

with open(lp.config("keywords.json")) as _f:
    KW = json.load(_f)
with open(lp.config("targets.json")) as _f:
    DOC = json.load(_f)


def judge(title, location="Remote - United States", kw=KW, company="Some Employer", kinds=None):
    return fj.judge_federal508({"id": "x:1", "company": company, "title": title, "url": "https://jobs.example.test/1", "location_text": location}, kw, kinds)


class Judge(unittest.TestCase):
    def test_a_508_or_accessibility_title_that_says_remote_in_its_place_is_posted_and_says_why(self):
        r = judge("Section 508 Compliance Tester", "Remote - United States")
        self.assertEqual(r["decision"], "post")
        self.assertEqual(r["reason"], "'508 compliance' (section-508) in the title; remote: 'remote'")

    def test_remote_in_the_title_or_contract_in_the_title_is_enough(self):
        for title, loc, word in (("Accessibility Specialist (Remote)", "Washington, DC", "remote"), ("508 Tester - Contract", "Reston, VA", "contract"),
                                 ("Accessibility Consultant", "Austin, TX", "consultant"), ("WCAG Auditor, 1099", "Chicago, IL", "1099"), ("Digital Accessibility Analyst (Telework)", "Arlington, VA", "telework")):
            r = judge(title, loc)
            self.assertEqual(r["decision"], "post", title)
            self.assertIn(f"'{word}'", r["reason"], title)

    def test_a_fitting_role_that_says_neither_remote_nor_contract_is_held_back_not_posted(self):
        for title in ("Accessibility Specialist", "Senior Section 508 Analyst", "UX Designer with 508 Compliance"):
            r = judge(title, "Arlington, VA")
            self.assertEqual(r["decision"], "unstated", title)
            self.assertIn("neither remote nor contract is stated", r["reason"])

    def test_the_include_switch_posts_the_held_back_roles(self):
        kw = copy.deepcopy(KW)
        kw["federal508_rule"]["include_unstated_level"] = True
        import channel_feed
        r = judge("Accessibility Specialist", "Arlington, VA", kw)
        self.assertEqual(len(channel_feed.wanted([({"id": 1}, r)], kw["federal508_rule"])), 1)

    def test_every_phrase_of_the_section_508_group_matches(self):
        for title in ("Trusted Tester", "VPAT Author", "A11y Engineer", "ICT Accessibility Lead - Remote", "Assistive Technology Specialist, Remote", "WCAG 2.2 Remediation (Remote)", "508 Program Manager, Remote"):
            self.assertEqual(judge(title)["decision"], "post", title)

    def test_titles_with_no_such_phrase_do_not_match(self):
        for title in ("Software Engineer", "Product Designer", "UX Researcher (Remote)", "Customer Access Manager", "Access Control Engineer", "Section 8 Housing Specialist", "Cybersecurity Analyst - Remote"):
            self.assertEqual(judge(title)["decision"], "no-match", title)

    def test_physical_access_is_not_digital_accessibility(self):
        for title, word in (("Building Accessibility Inspector - Remote", "building"), ("Accessibility Coordinator, Paratransit (Remote)", "paratransit"), ("Wheelchair Accessibility Technician", "wheelchair")):
            r = judge(title)
            self.assertEqual((r["decision"], r["reason"]), ("not-digital", f"not a digital accessibility role: '{word}' in the title"), title)

    def test_only_the_united_states_passes_and_a_place_that_names_no_country_passes_too(self):
        r = judge("Accessibility Specialist (Remote)", "London, England, United Kingdom")
        self.assertEqual(r["decision"], "rejected")
        self.assertTrue(r["reason"].startswith("country not allowed: "))
        for loc in ("Remote", "Remote - US", "Remote - United States", "Chicago, IL", ""):
            self.assertEqual(judge("Accessibility Specialist (Remote)", loc)["decision"], "post", loc)
        kw = copy.deepcopy(KW)
        kw["federal508_rule"]["if_no_country_named"] = "reject"
        self.assertEqual(judge("Accessibility Specialist (Remote)", "Remote", kw)["decision"], "rejected")

    def test_a_clearance_is_a_flag_not_a_veto_unless_the_rules_say_so(self):
        r = judge("Section 508 Tester (Secret clearance) - Remote")
        self.assertEqual((r["decision"], r["clearance"]), ("post", ["clearance", "secret"]))
        kw = copy.deepcopy(KW)
        kw["federal508_rule"]["clearance_policy"] = "veto"
        r = judge("Section 508 Tester (Secret clearance) - Remote", kw=kw)
        self.assertEqual(r["decision"], "rejected")
        self.assertTrue(r["reason"].startswith("clearance in the title: "))

    def test_the_company_kind_comes_from_the_list_and_nothing_else(self):
        kinds = fj.company_kinds({"targets": [{"section": "federal508", "status": "active", "name": "Made Up Federal", "federal508": {"kind": "federal-contractor", "feed_names": ["Made Up Federal", "MUF"]}},
                                              {"section": "federal508", "status": "dropped", "name": "Gone", "federal508": {"kind": "civic-tech", "feed_names": ["Gone"]}}]})
        self.assertEqual(kinds, {"made up federal": "federal-contractor", "muf": "federal-contractor"})
        self.assertEqual(judge("508 Tester", company="MUF", kinds=kinds)["kind"], "federal-contractor")
        self.assertIsNone(judge("508 Tester", company="Gone", kinds=kinds)["kind"])

    def test_no_level_is_read_because_an_audit_is_not_an_entry_level_job(self):
        for title in ("Principal Accessibility Consultant", "Senior 508 Tester - Remote", "Accessibility Intern (Remote)"):
            self.assertEqual(judge(title)["decision"], "post", title)

    def test_the_rule_is_off_and_names_its_own_channel(self):
        r = KW["federal508_rule"]
        self.assertEqual((r["posting"], r["channel"]), ("off", "federal-508"))
        self.assertEqual(r["allowed_countries"], ["United States"])


class Collector(unittest.TestCase):
    def test_only_active_employers_with_a_readable_board_are_read(self):
        doc = {"targets": [{"section": "federal508", "status": "active", "name": "A", "provider": "greenhouse", "federal508": {"board": {"slug": "a"}}},
                           {"section": "federal508", "status": "no-reader", "name": "B", "provider": "workday", "federal508": {}},
                           {"section": "consulting", "status": "active", "name": "C", "provider": "greenhouse", "consulting": {"board": {"slug": "c"}}}]}
        self.assertEqual(federal508_collect.boards_from_targets(doc), [("A", "greenhouse", "a")])

    def test_it_writes_every_posting_it_read_and_one_board_failing_does_not_stop_the_others(self):
        real = federal508_collect.cc.fetch_list
        payloads = {"good": {"jobs": [{"id": 7, "title": "Section 508 Tester", "absolute_url": "https://boards.example.test/7", "location": {"name": "Remote"}}]}}

        def fake(provider, slug):
            if slug not in payloads:
                raise RuntimeError("down")
            return payloads[slug]
        federal508_collect.cc.fetch_list = fake
        federal508_collect.PAUSE = 0
        federal508_collect.cc.PAUSE = 0
        try:
            with tempfile.TemporaryDirectory() as d:
                tp = os.path.join(d, "t.json")
                json.dump({"targets": [{"section": "federal508", "status": "active", "name": "Good Co", "provider": "greenhouse", "federal508": {"board": {"slug": "good"}}},
                                       {"section": "federal508", "status": "active", "name": "Bad Co", "provider": "greenhouse", "federal508": {"board": {"slug": "bad"}}}]}, open(tp, "w"))
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    code = federal508_collect.main(["--targets", tp, "--out", d])
                self.assertEqual(code, 0)
                path = [os.path.join(d, f) for f in os.listdir(d) if f.startswith("federal508-jobs-")][0]
                data = json.load(open(path))
                self.assertEqual([r["title"] for r in data["records"]], ["Section 508 Tester"])
                self.assertEqual({s["company"]: s["status"] for s in data["sources"]}, {"Good Co": "ok", "Bad Co": "unavailable"})
        finally:
            federal508_collect.cc.fetch_list = real


if __name__ == "__main__":
    unittest.main()
