#!/usr/bin/env python3
"""Tests for the SAM.gov set-aside filter (collect/sam_setaside.py). No network: the CSV files are made here and the extract's real columns are reused."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import json, os, tempfile, unittest

import sam_setaside as ss
import test_sam_opportunities as t

with open(lp.config("keywords.json")) as _f:
    RULE = json.load(_f)["federal508_rule"]

VA = "VETERANS AFFAIRS, DEPARTMENT OF"
DOD = "DEPT OF DEFENSE"
DOT = "TRANSPORTATION, DEPARTMENT OF"


def run(rows, wanted=("VA", "DOD", "FAA")):
    return ss.analyse(t.write_csv(rows), RULE, set(wanted))


def notice(n, agency=VA, code="SBA", title="Plain Notice", desc="Some text.", naics="541512", psc="D302", **kw):
    return t.row(n, title=title, desc=desc, **{"Department/Ind.Agency": agency, "SetASideCode": code, "NaicsCode": naics, "ClassificationCode": psc, **kw})


class Agencies(unittest.TestCase):
    def test_three_agencies_and_nothing_else(self):
        self.assertEqual(ss.agency_of({"agency": VA, "sub_tier": ""}), "VA")
        self.assertEqual(ss.agency_of({"agency": DOD, "sub_tier": "DEPT OF THE ARMY"}), "DOD")
        self.assertEqual(ss.agency_of({"agency": DOT, "sub_tier": "FEDERAL AVIATION ADMINISTRATION"}), "FAA")
        self.assertIsNone(ss.agency_of({"agency": DOT, "sub_tier": "FEDERAL HIGHWAY ADMINISTRATION"}))
        self.assertIsNone(ss.agency_of({"agency": "GENERAL SERVICES ADMINISTRATION", "sub_tier": ""}))

    def test_set_asides(self):
        for code in ("SBA", "SBP", "WOSB", "WOSBSS", "EDWOSB", "EDWOSBSS", '["SBA"]'):
            self.assertTrue(ss.set_aside_of({"set_aside_code": code}), code)
        for code in ("SDVOSBC", "8A", "HZC", "VSA", "NONE", ""):
            self.assertIsNone(ss.set_aside_of({"set_aside_code": code}), code)

    def test_it_work(self):
        self.assertTrue(ss.is_it({"naics": "541511", "psc": ""}))
        self.assertTrue(ss.is_it({"naics": "", "psc": "DA01"}))
        self.assertFalse(ss.is_it({"naics": "236220", "psc": "Y1AA"}))


class Tiers(unittest.TestCase):
    def test_508_in_the_title_is_tier_a(self):
        counts, left, leads = run([notice(1, title="Section 508 Testing Services", naics="541990", psc="R499")])
        self.assertEqual([(r["tier"], r["agency_short"]) for r in leads], [("A", "VA")])

    def test_work_phrase_in_the_description_is_tier_a(self):
        _, _, leads = run([notice(1, desc="The contractor shall provide accessibility testing of web pages.", naics="541990", psc="R499")])
        self.assertEqual([r["tier"] for r in leads], ["A"])

    def test_requirement_clause_in_an_it_notice_is_tier_b(self):
        _, _, leads = run([notice(1, desc="All deliverables shall conform to Section 508 of the Rehabilitation Act.")])
        self.assertEqual([r["tier"] for r in leads], ["B"])

    def test_requirement_clause_in_a_construction_notice_is_not_a_lead(self):
        _, _, leads = run([notice(1, desc="Site shall meet accessibility standards.", naics="236220", psc="Y1AA")])
        self.assertEqual(leads, [])

    def test_wrong_set_aside_or_agency_or_inactive_is_left_out(self):
        rows = [notice(1, code="SDVOSBC", title="Section 508 Testing"), notice(2, agency="GENERAL SERVICES ADMINISTRATION", title="Section 508 Testing"),
                notice(3, title="Section 508 Testing", active="No"), notice(4, code="", title="Section 508 Testing")]
        counts, left, leads = run(rows)
        self.assertEqual(leads, [])
        self.assertEqual(counts["active_VA"], 2)

    def test_agency_filter(self):
        rows = [notice(1, title="Section 508 Testing"), notice(2, agency=DOD, title="Section 508 Testing")]
        _, _, leads = run(rows, wanted=("DOD",))
        self.assertEqual([r["agency_short"] for r in leads], ["DOD"])


class Output(unittest.TestCase):
    def test_no_contact_is_kept_and_csv_matches(self):
        out = tempfile.mkdtemp()
        path = t.write_csv([notice(1, title="Section 508 Testing")])
        cache = tempfile.mkdtemp()
        os.replace(path, os.path.join(cache, ss.so.FILE))
        self.assertEqual(ss.main(["--cache", cache, "--out", out]), 0)
        text = ""
        for f in os.listdir(out):
            with open(os.path.join(out, f), encoding="utf-8") as fh:
                text += fh.read()
        self.assertNotIn("pat@agency.example", text)
        self.assertNotIn("Pat Contact", text)
        self.assertNotIn("555-0100", text)
        self.assertIn("Section 508 Testing", text)

    def test_no_cached_file_exits_3(self):
        self.assertEqual(ss.main(["--cache", tempfile.mkdtemp()]), 3)


if __name__ == "__main__":
    unittest.main()
