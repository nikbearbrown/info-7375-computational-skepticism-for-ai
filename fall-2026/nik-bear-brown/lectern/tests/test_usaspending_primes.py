#!/usr/bin/env python3
"""Tests for the USAspending prime-leads reader (collect/usaspending_primes.py). No network: a fake `post` stands in for api.usaspending.gov."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import collections, contextlib, io, json, os, tempfile, unittest

import collect
import usaspending_primes as up

with open(lp.config("keywords.json")) as _f:
    RULE = json.load(_f)["federal508_rule"]


def award(n, desc, recipient="ACME LLC", uei="UEI1", amount="1000", agency="Department of Veterans Affairs", end="2027-01-01", naics="541512", psc="DA01"):
    return {"internal_id": str(n), "Award ID": f"A{n}", "generated_internal_id": f"CONT_AWD_A{n}", "Recipient Name": recipient, "Recipient UEI": uei, "Description": desc,
            "Award Amount": amount, "Awarding Agency": agency, "Awarding Sub Agency": agency, "Start Date": "2024-01-01", "End Date": end,
            "NAICS": {"code": naics, "description": "x"}, "PSC": {"code": psc, "description": "y"}}


def sub_award(n, desc, prime="BIG PRIME INC", sub="SMALL SUB LLC", amount="500"):
    return {"internal_id": f"S{n}", "Sub-Award ID": f"S{n}", "Prime Award ID": f"P{n}", "Sub-Awardee Name": sub, "Sub-Award Amount": amount, "Sub-Award Date": "2025-01-01",
            "Sub-Award Description": desc, "Prime Recipient Name": prime, "Awarding Agency": "Department of Defense", "Awarding Sub Agency": "Army"}


class Fake:
    """Answers each keyword with its own rows, `size` to a page, and records every request."""
    def __init__(self, by_query, size=2):
        self.by_query, self.size, self.calls = by_query, size, []

    def __call__(self, url, body):
        self.calls.append((url, json.loads(json.dumps(body))))
        rows = self.by_query.get(body["filters"]["keywords"][0], [])
        p = body["page"]
        chunk = rows[(p - 1) * self.size:p * self.size]
        return {"results": chunk, "page_metadata": {"page": p, "hasNext": p * self.size < len(rows)}}


class Search(unittest.TestCase):
    def test_it_pages_until_the_api_says_there_is_no_next_page(self):
        f = Fake({"section 508": [award(i, "SECTION 508 TESTING") for i in range(5)]}, size=2)
        rows, complete = up.search("awards", "section 508", "2023-10-01", "2026-11-03", pause=0, post=f)
        self.assertEqual((len(rows), complete, len(f.calls)), (5, True, 3))

    def test_a_search_with_more_pages_than_the_cap_is_reported_not_complete(self):
        f = Fake({"wcag": [award(i, "WCAG") for i in range(10)]}, size=2)
        rows, complete = up.search("awards", "wcag", "2023-10-01", "2026-11-03", pause=0, max_pages=2, post=f)
        self.assertEqual((len(rows), complete), (4, False))

    def test_the_request_asks_for_contracts_in_the_window_and_subawards_in_their_own_level(self):
        f = Fake({})
        up.search("awards", "vpat", "2023-10-01", "2026-11-03", pause=0, post=f)
        up.search("subawards", "vpat", "2023-10-01", "2026-11-03", pause=0, post=f)
        (u1, a), (u2, s) = f.calls
        self.assertEqual(u1, "https://api.usaspending.gov/api/v2/search/spending_by_award/")
        self.assertEqual((a["filters"]["award_type_codes"], a["filters"]["time_period"], a["limit"]), (["A", "B", "C", "D"], [{"start_date": "2023-10-01", "end_date": "2026-11-03"}], 100))
        self.assertNotIn("spending_level", a)
        self.assertEqual((s["spending_level"], "Sub-Awardee Name" in s["fields"]), ("subawards", True))

    def test_a_reply_without_a_results_list_is_an_error(self):
        with self.assertRaises(ValueError):
            up.search("awards", "wcag", "2023-10-01", "2026-11-03", pause=0, post=lambda u, b: {"detail": "bad filter"})

    def test_the_host_is_allowed_for_https_only(self):
        collect._checked(up.URL)
        with self.assertRaises(collect.InputError):
            collect._checked("http://api.usaspending.gov/api/v2/x")

    def test_the_window_starts_on_1_october_of_the_fiscal_year_four_back_so_it_holds_the_current_year_and_three_more(self):
        import datetime
        self.assertEqual(up.default_since(datetime.date(2026, 11, 3)), "2023-10-01")        # FY2027 began 2026-10-01: FY2024 is the first of the four
        self.assertEqual(up.default_since(datetime.date(2026, 9, 30)), "2022-10-01")        # still FY2026


class Classify(unittest.TestCase):
    def test_a_508_phrase_in_the_description_is_strong_and_the_generic_word_is_weak(self):
        self.assertEqual(up.classify("SECTION 508 AUDIT, TESTING AND TRAINING SERVICES", RULE)[0], "strong")
        self.assertEqual(up.classify("Trusted Tester certification support", RULE)[0], "strong")
        self.assertEqual(up.classify("Website accessibility improvements", RULE)[0], "weak")
        self.assertEqual(up.classify("INFORMATION TECHNOLOGY,ENTERPRISE SERVICES", RULE), (None, []))

    def test_physical_access_words_rule_a_description_out(self):
        for d in ("Building accessibility ramp construction", "Wheelchair accessible vehicle", "Section 508 ... paratransit accessibility",
                  "BLDG. 508 REMEDIATION AND DEMOLITION SERVICES", "Section 508 remediation of asbestos"):
            self.assertEqual(up.classify(d, RULE)[0], None, d)

    def test_a_part_number_is_not_section_508(self):
        self.assertEqual(up.classify("NUT 5310-508 ASSEMBLY", RULE)[0], None)


class Leads(unittest.TestCase):
    def kept(self, rows, level="awards"):
        seen, kept, counts = set(), [], collections.Counter()
        up.keep(rows, level, RULE, seen, kept, counts)
        return kept, counts

    def test_rows_the_api_matched_elsewhere_are_counted_and_dropped_and_a_repeat_counts_once(self):
        kept, c = self.kept([award(1, "SECTION 508 SUPPORT"), award(1, "SECTION 508 SUPPORT"), award(2, "INFORMATION TECHNOLOGY,ENTERPRISE SERVICES"), award(3, "Web accessibility")])
        self.assertEqual((len(kept), c["rows"], c["strong"], c["weak"], c["matched_elsewhere"]), (2, 3, 1, 1, 1))

    def test_prime_leads_are_ranked_by_strong_awards_then_dollars_and_name_the_agencies_and_examples(self):
        kept, _ = self.kept([award(1, "SECTION 508 TESTING", "ONE INC", "U1", "100"), award(2, "SECTION 508 AUDIT", "TWO INC", "U2", "9000"), award(3, "SECTION 508 SUPPORT", "TWO INC", "U2", "1000"),
                             award(4, "Website accessibility", "THREE INC", "U3", "99999999")])
        leads = up.group_awards(kept)
        self.assertEqual([g["name"] for g in leads], ["TWO INC", "ONE INC", "THREE INC"])
        two = leads[0]
        self.assertEqual((two["awards"], two["strong_awards"], two["dollars"], two["strong_dollars"]), (2, 2, 10000.0, 10000.0))
        self.assertEqual((two["agencies"], two["latest_end"], two["examples"][0]["description"], two["examples"][0]["naics"]), (["Department of Veterans Affairs"], "2027-01-01", "SECTION 508 AUDIT", "541512"))

    def test_subawards_are_grouped_by_the_prime_that_passes_work_down_and_by_the_sub_that_does_it(self):
        kept, c = self.kept([sub_award(1, "Section 508 testing of the portal", "BIG A", "SUB X", "300"), sub_award(2, "508 remediation of PDFs", "BIG A", "SUB Y", "700"),
                             sub_award(3, "Provide IT support", "BIG B", "SUB X", "99")], level="subawards")
        self.assertEqual(c["matched_elsewhere"], 1)
        primes, subs = up.group_subs(kept, "prime"), up.group_subs(kept, "sub")
        self.assertEqual((primes[0]["name"], primes[0]["strong_awards"], primes[0]["dollars"], sorted(primes[0]["partners"])), ("BIG A", 2, 1000.0, ["SUB X", "SUB Y"]))
        self.assertEqual([g["name"] for g in subs], ["SUB Y", "SUB X"])

    def test_a_bad_amount_counts_as_zero(self):
        self.assertEqual((up.money(None), up.money("x"), up.money("12.5")), (0.0, 0.0, 12.5))


class Run(unittest.TestCase):
    def test_one_failing_search_is_recorded_and_the_others_still_run(self):
        good = Fake({"section 508": [award(1, "SECTION 508 SUPPORT")]})

        def post(url, body):
            if body["filters"]["keywords"][0] == "wcag":
                raise OSError("down")
            return good(url, body)
        res = up.run(RULE, "2023-10-01", "2026-11-03", subawards=False, pause=0, post=post)
        self.assertEqual([(x["level"], x["query"]) for x in res["failed"]], [("awards", "wcag")])
        self.assertEqual(len(res["levels"]["awards"]["kept"]), 1)

    def test_main_writes_a_file_with_leads_and_no_people_and_exit_3_when_nothing_is_fetched(self):
        real = collect.post_json
        d = tempfile.mkdtemp()
        try:
            collect.post_json = Fake({"section 508": [award(1, "SECTION 508 SUPPORT SERVICES", "FIRM ONE LLC", "U1", "5000")], "accessibility remediation": []}, size=50)
            real_sleep, up.time.sleep = up.time.sleep, lambda s: None
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(up.main(["--out", d, "--no-subawards"]), 0)
            finally:
                up.time.sleep = real_sleep
            name = [f for f in os.listdir(d) if f.startswith("usaspending-primes-")][0]
            with open(os.path.join(d, name), encoding="utf-8") as f:
                doc = json.load(f)
            self.assertEqual(doc["leads"]["primes"][0]["name"], "FIRM ONE LLC")
            self.assertNotIn("primes_that_subcontract", doc["leads"])
            collect.post_json = lambda url, body: (_ for _ in ()).throw(OSError("down"))
            up.time.sleep = lambda s: None
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(up.main(["--out", d, "--no-subawards"]), 3)
                self.assertEqual(up.main(["--since", "yesterday"]), 2)
        finally:
            collect.post_json = real
            up.time.sleep = real_sleep

    def test_no_key_is_used_or_read(self):
        with open(up.__file__, encoding="utf-8") as f:
            src = f.read()
        for gone in ("api_key", "os.environ", "getenv", "Authorization"):
            self.assertNotIn(gone, src)


if __name__ == "__main__":
    unittest.main()
