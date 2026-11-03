#!/usr/bin/env python3
"""Tests for the California school-district lead list (collect/ca_school_districts.py). No network: a fake opener stands in for the data hub, and the CSV files are made here."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import contextlib, csv, datetime as dt, io, json, os, tempfile, unittest

import collect
import ca_school_districts as cad

HEADER = ["OBJECTID", "Academic Year", "Fed ID", "District Code", "CDS Code", "County Name", "District Name", "District Type", "Grade Low", "Grade High", "Street", "City", "Zip",
          "Enroll Total", "African American", "Students with Disabilities", "Students with Disabilities (%)", "Locale Description", "x", "y"]


def office(name, kind="Unified", enroll="1000", swd="120", pct="12", county="Alameda", city="Hayward", cds="01100170000000"):
    d = dict.fromkeys(HEADER, "")
    d.update({"District Name": name, "District Type": kind, "Enroll Total": enroll, "Students with Disabilities": swd, "Students with Disabilities (%)": pct, "County Name": county,
              "City": city, "Zip": "94544", "CDS Code": cds, "Locale Description": "City: Large", "Street": "1 Secret Street"})
    return d


def write_csv(rows, header=HEADER, bom=True):
    path = tempfile.mkstemp(suffix=".csv")[1]
    with open(path, "w", encoding="utf-8-sig" if bom else "utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    return path


class Resp:
    def __init__(self, status, headers=None, body=b""):
        self.status, self.code, self.headers, self._b = status, status, headers or {}, io.BytesIO(body)

    def read(self, n=-1):
        return self._b.read(n)

    def close(self):
        pass


class Hub:
    """gis.data.ca.gov answers 302 to a storage link, which answers 302 to a signed file link on *.az.arcgis.com, which answers 200 with the file."""
    def __init__(self, body=b"a,b\n1,2\n", chain=None, length=None):
        self.body, self.length, self.calls = body, length, []
        self.chain = chain or ["https://services3.arcgis.com/abc/export", "https://x-prod3.az.arcgis.com/export.csv?sig=SECRET"]

    def __call__(self, url):
        self.calls.append(url)
        if url == cad.URL:
            return Resp(302, {"Location": self.chain[0]})
        if url in self.chain[:-1]:
            return Resp(302, {"Location": self.chain[self.chain.index(url) + 1]})
        return Resp(200, {"Content-Length": str(self.length if self.length is not None else len(self.body))}, self.body)


class Fetch(unittest.TestCase):
    def setUp(self):
        self.cache = tempfile.mkdtemp()

    def test_the_redirects_are_followed_by_hand_to_the_two_allowed_hosts_and_the_file_is_kept(self):
        hub = Hub()
        path, outcome = cad.fetch(self.cache, dt.date(2026, 11, 2), opener=hub)
        self.assertEqual(outcome, "downloaded")
        with open(path, "rb") as f:
            self.assertEqual(f.read(), b"a,b\n1,2\n")
        self.assertEqual(len(hub.calls), 3)
        self.assertEqual(cad.load_meta(self.cache)["fetched_on"], "2026-11-02")

    def test_a_recent_copy_makes_no_request_and_an_old_one_or_refresh_does(self):
        cad.fetch(self.cache, dt.date(2026, 11, 2), opener=Hub())
        again = Hub()
        self.assertEqual(cad.fetch(self.cache, dt.date(2026, 11, 20), opener=again)[1], "cached")
        self.assertEqual(again.calls, [])
        self.assertEqual(cad.fetch(self.cache, dt.date(2026, 11, 20), refresh=True, opener=Hub())[1], "downloaded")
        self.assertEqual(cad.fetch(self.cache, dt.date(2026, 12, 25), opener=Hub())[1], "downloaded")       # 35 days after the refresh

    def test_a_redirect_to_any_other_host_or_to_http_is_refused_before_the_request(self):
        for bad in ("https://evil.example.com/f.csv", "http://gis.data.ca.gov/f.csv", "https://az.arcgis.com.evil.example/f.csv", "https://evilaz.arcgis.com/f.csv", "https://services4.arcgis.com/f.csv"):
            hub = Hub(chain=[bad, bad])
            with self.assertRaises(collect.InputError, msg=bad):
                cad.fetch(tempfile.mkdtemp(), dt.date(2026, 11, 2), opener=hub)
            self.assertEqual(hub.calls, [cad.URL], bad)

    def test_a_short_download_leaves_no_file_and_a_redirect_loop_is_an_error(self):
        c = tempfile.mkdtemp()
        with self.assertRaises(ValueError):
            cad.fetch(c, dt.date(2026, 11, 2), opener=Hub(length=999))
        self.assertEqual(os.listdir(c), [])
        with self.assertRaises(ValueError):
            cad.fetch(tempfile.mkdtemp(), dt.date(2026, 11, 2), opener=lambda url: Resp(302, {"Location": "https://gis.data.ca.gov/loop"}))

    def test_the_signed_link_is_never_in_an_error_message_of_main(self):
        d = tempfile.mkdtemp()
        real = cad._open
        cad._open = lambda url: (_ for _ in ()).throw(urllib_error(url))
        try:
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                self.assertEqual(cad.main(["--cache", d + "/c", "--out", d + "/o", "--exclusions", d + "/none"]), 3)
        finally:
            cad._open = real
        self.assertNotIn("SECRET", err.getvalue())


def urllib_error(url):
    import urllib.error
    return urllib.error.URLError("failed https://x.az.arcgis.com/f.csv?sig=SECRET")


class Read(unittest.TestCase):
    def test_offices_are_read_with_a_bom_and_only_the_needed_fields_are_kept(self):
        rows, bad = cad.read_offices(write_csv([office("Alpha Unified", enroll="12,345", swd="1,500", pct="12.1")]))
        self.assertEqual((len(rows), bad), (1, 0))
        r = rows[0]
        self.assertEqual((r["name"], r["enrollment"], r["students_with_disabilities"], r["tier"]), ("Alpha Unified", 12345, 1500, "A: 10,000 students or more"))
        self.assertNotIn("Secret Street", json.dumps(rows))

    def test_a_row_without_enrollment_is_counted_not_guessed_and_a_missing_column_is_refused(self):
        rows, bad = cad.read_offices(write_csv([office("A", enroll=""), office("B", enroll="n/a"), office("C")]))
        self.assertEqual(([r["name"] for r in rows], bad), (["C"], 2))
        with self.assertRaises(collect.InputError):
            cad.read_offices(write_csv([], header=[h for h in HEADER if h != "Enroll Total"]))

    def test_the_tiers(self):
        self.assertEqual([cad.tier(x)[0] for x in (50000, 10000, 9999, 2000, 1999, 0)], list("AABBCC"))


class Rank(unittest.TestCase):
    ROWS = [dict(name=n, enrollment=e, type="Unified") for n, e in (("Small Unified", 500), ("Beta Unified", 32883), ("Big Unified", 90000), ("Gamma School for the Deaf-North (State Special Schl)", 120),
                                                                         ("Beta Union High", 9289), ("Mid Elementary", 4000))]

    def test_biggest_first_and_excluded_names_are_left_out_by_part_of_the_name_case_folded(self):
        kept, out = cad.rank(self.ROWS, ["beta unified", "Gamma School for the Deaf"])
        self.assertEqual([r["name"] for r in kept], ["Big Unified", "Beta Union High", "Mid Elementary", "Small Unified"])
        self.assertEqual(sorted(r["name"] for r in out), ["Beta Unified", "Gamma School for the Deaf-North (State Special Schl)"])

    def test_nothing_is_left_out_when_nothing_is_asked(self):
        self.assertEqual(len(cad.rank(self.ROWS, [])[0]), 6)
        self.assertEqual(len(cad.rank(self.ROWS, ["", "  "])[0]), 6)

    def test_the_exclusions_file_skips_comments_and_blank_lines_and_a_missing_file_is_empty(self):
        p = tempfile.mkstemp()[1]
        with open(p, "w", encoding="utf-8") as f:
            f.write("# a comment\n\nName One\n  Name Two  \n")
        self.assertEqual(cad.read_exclusions(p), ["Name One", "Name Two"])
        self.assertEqual(cad.read_exclusions(p + ".missing"), [])


class Main(unittest.TestCase):
    def test_main_writes_the_ranked_csv_and_json_without_the_excluded_and_with_no_street(self):
        d = tempfile.mkdtemp()
        os.makedirs(d + "/cache")
        src = write_csv([office("Big Unified", enroll="50000"), office("Beta Unified", enroll="32883"), office("Small Elementary", "Elementary", enroll="300"),
                         office("Alameda County Office of Education", "County Office of Education (COE)", enroll="4300")])
        with open(src, "rb") as f, open(os.path.join(d, "cache", cad.FILE), "wb") as g:
            g.write(f.read())
        with open(os.path.join(d, "cache", cad.FILE + ".meta.json"), "w") as f:
            json.dump({"fetched_on": dt.date.today().isoformat()}, f)
        excl = d + "/ex.txt"
        with open(excl, "w") as f:
            f.write("Beta Unified\n")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.assertEqual(cad.main(["--cache", d + "/cache", "--out", d + "/o", "--exclusions", excl]), 0)
        names = os.listdir(d + "/o")
        csv_name = [n for n in names if n.endswith(".csv")][0]
        with open(os.path.join(d, "o", csv_name), encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual([(r["rank"], r["name"]) for r in rows], [("1", "Big Unified"), ("2", "Alameda County Office of Education"), ("3", "Small Elementary")])
        for n in names:
            with open(os.path.join(d, "o", n), encoding="utf-8") as f:
                self.assertNotIn("Beta Unified", f.read())
                f.seek(0)
                self.assertNotIn("Secret Street", f.read())
        self.assertNotIn("Beta Unified", buf.getvalue())
        self.assertIn("1 left out by request", buf.getvalue())

    def test_a_missing_cache_with_a_failing_fetch_is_exit_3(self):
        d = tempfile.mkdtemp()
        real = cad._open
        cad._open = lambda url: (_ for _ in ()).throw(OSError("down"))
        try:
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(cad.main(["--cache", d + "/c", "--out", d + "/o", "--exclusions", d + "/none"]), 3)
        finally:
            cad._open = real

    def test_no_office_is_left_out_unless_the_person_or_the_command_line_asks(self):
        rows = [dict(name="Beta Unified", enrollment=5, type="Unified"), dict(name="Alpha Unified", enrollment=9, type="Unified")]
        self.assertEqual(len(cad.rank(rows, [])[0]), 2)
        self.assertTrue(cad.EXCLUSIONS.endswith(os.path.join("runs", "lead-exclusions.txt")))


if __name__ == "__main__":
    unittest.main()
