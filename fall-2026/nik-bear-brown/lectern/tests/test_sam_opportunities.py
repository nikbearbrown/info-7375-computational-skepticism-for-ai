#!/usr/bin/env python3
"""Tests for the SAM.gov contract-opportunities reader (collect/sam_opportunities.py). No network: a fake opener stands in for SAM.gov, and the CSV files are made here."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import collections, csv, io, json, tempfile, unittest

import collect
import sam_opportunities as sam

with open(lp.config("keywords.json")) as _f:
    RULE = json.load(_f)["federal508_rule"]

HEADER = ["NoticeId", "Title", "Sol#", "Department/Ind.Agency", "CGAC", "Sub-Tier", "FPDS Code", "Office", "AAC Code", "PostedDate", "Type", "BaseType", "ArchiveType",
          "ArchiveDate", "SetASideCode", "SetASide", "ResponseDeadLine", "NaicsCode", "ClassificationCode", "PopStreetAddress", "PopCity", "PopState", "PopZip", "PopCountry",
          "Active", "AwardNumber", "AwardDate", "Award$", "Awardee", "PrimaryContactTitle", "PrimaryContactFullname", "PrimaryContactEmail", "PrimaryContactPhone",
          "PrimaryContactFax", "SecondaryContactTitle", "SecondaryContactFullname", "SecondaryContactEmail", "SecondaryContactPhone", "SecondaryContactFax",
          "OrganizationType", "State", "City", "ZipCode", "CountryCode", "AdditionalInfoLink", "Link", "Description"]


def row(n, title="Plain Notice", desc="Some text.", active="Yes", **kw):
    d = dict.fromkeys(HEADER, "")
    d.update(NoticeId=f"id{n}", Title=title, Description=desc, Active=active, Type="Solicitation", PostedDate="2026-11-01 09:00:00", PopCountry="USA",
             PrimaryContactFullname="Pat Contact", PrimaryContactEmail="pat@agency.example", PrimaryContactPhone="555-0100", Link=f"https://sam.gov/opp/id{n}/view")
    d.update(kw)
    return [d[h] for h in HEADER]


def write_csv(rows, encoding="cp1252", header=HEADER, bom=False):
    buf = io.StringIO(newline="")
    w = csv.writer(buf)
    w.writerow(header)
    w.writerows(rows)
    path = tempfile.mkstemp(suffix=".csv")[1]
    with open(path, "wb") as f:
        f.write((b"\xef\xbb\xbf" if bom else b"") + buf.getvalue().encode(encoding, errors="replace"))
    return path


def slurp(path):
    with open(path, "rb") as f:
        return f.read()


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


class Response:
    def __init__(self, status, headers=None, body=b""):
        self.status, self.code, self.headers, self._b = status, status, headers or {}, io.BytesIO(body)

    def read(self, n=-1):
        return self._b.read(n)

    def close(self):
        pass


class FakeSam:
    """The two-step download: the official address answers 303 to the storage host; the storage host answers 200 with the file, or 304 when the validator matches."""
    def __init__(self, body=b"a,b\n1,2\n", etag='"v1"', location="https://falextracts.s3.amazonaws.com/x/file.csv?sig=1", length=None):
        self.body, self.etag, self.location, self.length, self.calls = body, etag, location, length, []

    def __call__(self, url, headers):
        self.calls.append((url, dict(headers)))
        if url == sam.URL:
            return Response(303, {"Location": self.location})
        if headers.get("If-None-Match") == self.etag:
            return Response(304, {})
        return Response(200, {"ETag": self.etag, "Last-Modified": "Mon, 02 Nov 2026 04:30:28 GMT", "Content-Length": str(self.length if self.length is not None else len(self.body))}, self.body)


class Fetch(unittest.TestCase):
    def setUp(self):
        self.cache = tempfile.mkdtemp()

    def test_a_first_fetch_follows_the_one_redirect_and_keeps_the_file_and_its_validators(self):
        fake = FakeSam()
        path, outcome = sam.fetch_extract(self.cache, "2026-11-02", fake)
        self.assertEqual(outcome, "downloaded")
        self.assertEqual(slurp(path), b"a,b\n1,2\n")
        meta = sam.load_meta(self.cache)
        self.assertEqual((meta["etag"], meta["fetched_on"], meta["checked_on"], meta["bytes"]), ('"v1"', "2026-11-02", "2026-11-02", 8))
        self.assertEqual(len(fake.calls), 2)

    def test_a_second_run_the_same_day_makes_no_request_at_all(self):
        sam.fetch_extract(self.cache, "2026-11-02", FakeSam())
        again = FakeSam()
        self.assertEqual(sam.fetch_extract(self.cache, "2026-11-02", again)[1], "checked-today")
        self.assertEqual(again.calls, [])

    def test_the_next_day_an_unchanged_file_is_a_304_and_nothing_is_downloaded(self):
        sam.fetch_extract(self.cache, "2026-11-02", FakeSam())
        fake = FakeSam()
        path, outcome = sam.fetch_extract(self.cache, "2026-11-03", fake)
        self.assertEqual(outcome, "unchanged")
        self.assertEqual(fake.calls[1][1]["If-None-Match"], '"v1"')
        self.assertIn("If-Modified-Since", fake.calls[1][1])
        self.assertEqual(slurp(path), b"a,b\n1,2\n")
        self.assertEqual(sam.load_meta(self.cache)["checked_on"], "2026-11-03")
        self.assertEqual(sam.load_meta(self.cache)["fetched_on"], "2026-11-02")

    def test_the_next_day_a_changed_file_replaces_the_old_one(self):
        sam.fetch_extract(self.cache, "2026-11-02", FakeSam())
        path, outcome = sam.fetch_extract(self.cache, "2026-11-03", FakeSam(body=b"a,b\n3,4\n", etag='"v2"'))
        self.assertEqual((outcome, slurp(path), sam.load_meta(self.cache)["etag"]), ("downloaded", b"a,b\n3,4\n", '"v2"'))

    def test_a_redirect_to_any_other_host_is_refused_before_a_second_request(self):
        for bad in ("https://evil.example.com/file.csv", "http://falextracts.s3.amazonaws.com/file.csv", "https://falextracts.s3.amazonaws.com.evil.example/file.csv"):
            fake = FakeSam(location=bad)
            with self.assertRaises(collect.InputError, msg=bad):
                sam.fetch_extract(self.cache, "2026-11-02", fake)
            self.assertEqual(len(fake.calls), 1)

    def test_a_download_that_stops_short_leaves_no_file_and_no_record_of_one(self):
        with self.assertRaises(ValueError):
            sam.fetch_extract(self.cache, "2026-11-02", FakeSam(length=999))
        self.assertEqual(sorted(__import__("os").listdir(self.cache)), [])

    def test_an_address_that_does_not_redirect_is_an_error(self):
        with self.assertRaises(ValueError):
            sam.fetch_extract(self.cache, "2026-11-02", lambda url, headers: Response(200, {}, b"<html>"))

    def test_the_two_hosts_are_on_the_allowlist_and_http_is_not_accepted(self):
        collect._checked(sam.URL)
        collect._checked("https://falextracts.s3.amazonaws.com/x")
        with self.assertRaises(collect.InputError):
            collect._checked("http://sam.gov/x")


class Read(unittest.TestCase):
    def test_encoding_is_detected_utf8_bom_or_windows_1252(self):
        self.assertEqual(sam.detect_encoding(write_csv([row(1)], "utf-8")), "utf-8")
        self.assertEqual(sam.detect_encoding(write_csv([row(1)], "utf-8", bom=True)), "utf-8-sig")
        self.assertEqual(sam.detect_encoding(write_csv([row(1, desc="Amendment 0001 – Revision")], "cp1252")), "cp1252")

    def test_a_windows_1252_dash_is_read_as_a_dash_and_the_contacts_are_never_kept(self):
        c = collections.Counter()
        recs = list(sam.read_rows(write_csv([row(1, desc="Amendment 0001 – Revision")]), c))
        self.assertEqual(recs[0]["description"], "Amendment 0001 – Revision")
        self.assertEqual((c["undecodable"], c["malformed"], c["rows"]), (0, 0, 1))
        text = json.dumps(recs)
        for gone in ("Pat Contact", "pat@agency.example", "555-0100"):
            self.assertNotIn(gone, text)
        self.assertFalse([k for k in recs[0] if "contact" in k.lower()])

    def test_bytes_that_cannot_be_decoded_are_counted_not_hidden(self):
        path = write_csv([row(1, desc="ok")])
        with open(path, "rb") as f:
            data = f.read().replace(b"ok", b"o\x81")                           # 0x81 is not defined in Windows-1252
        with open(path, "wb") as f:
            f.write(data)
        c = collections.Counter()
        list(sam.read_rows(path, c))
        self.assertEqual(c["undecodable"], 1)

    def test_a_row_with_the_wrong_number_of_fields_is_counted_and_skipped(self):
        path = write_csv([row(1), row(2)[:-3], row(3) + ["extra"], row(4)])
        c = collections.Counter()
        recs = list(sam.read_rows(path, c))
        self.assertEqual(([r["notice_id"] for r in recs], c["malformed"], c["rows"]), (["id1", "id4"], 2, 4))

    def test_a_file_without_an_expected_column_is_refused(self):
        bad = [h for h in HEADER if h != "NoticeId"]
        with self.assertRaises(collect.InputError):
            list(sam.read_rows(write_csv([], header=bad)))
        with self.assertRaises(collect.InputError):
            list(sam.read_rows(write_csv([], header=[])))


class Judge(unittest.TestCase):
    def kind(self, title="Plain", desc=""):
        rec = {"title": title, "description": desc}
        return sam.strength(rec, sam.phrase_finder(RULE), RULE), rec

    def test_a_phrase_in_the_title_wins_and_a_part_number_is_not_section_508(self):
        self.assertEqual(self.kind("Section 508 Testing Services")[0], "title")
        self.assertEqual(self.kind("53--NUT,PLAIN,ASSEMBLED WASHER 508")[0], None)
        self.assertEqual(self.kind("Hose 5330-508 assembly", "NSN 5310-00-508")[0], None)

    def test_a_section_508_phrase_in_the_description_is_surfaced_and_a_bare_accessibility_word_is_only_counted(self):
        self.assertEqual(self.kind("Website refresh", "The contractor shall meet Section 508 requirements.")[0], "description-508")
        self.assertEqual(self.kind("Janitorial", "Provides accessibility for visitors.")[0], "description-accessibility")
        k, rec = self.kind("Website refresh", "WCAG and VPAT required")
        self.assertEqual((k, sorted(p for _, p in rec["description_hits"])), ("description-508", ["vpat", "wcag"]))

    def test_the_fingerprint_changes_with_the_deadline_and_the_description_but_not_with_the_contact(self):
        a = {k: "x" for k in ("title", "type", "active", "archive_date", "response_deadline", "description")}
        b = dict(a, response_deadline="y")
        c = dict(a, description="y")
        self.assertEqual(len({sam.fingerprint(a), sam.fingerprint(b), sam.fingerprint(c)}), 3)


class Analyse(unittest.TestCase):
    def setUp(self):
        self.path = write_csv([row(1, "Section 508 Remediation Services"), row(2, "Website", "Must meet Section 508"), row(3, "Grease trap cleaning"),
                               row(4, "Section 508 Tester", active="No"), row(5, "Cafeteria", "good accessibility")])

    def test_only_active_title_or_section_508_notices_are_surfaced_and_the_rest_counted(self):
        stats, surfaced, new, changed = sam.analyse(self.path, RULE, {})
        self.assertEqual(sorted(r["notice_id"] for r in surfaced), ["id1", "id2"])
        self.assertEqual((stats["rows"], stats["active"], stats["new"], stats["changed"]), (5, 4, 2, 0))
        self.assertEqual(stats["matches_by_strength"], {"title": 2, "description-508": 1, "description-accessibility": 1})
        self.assertEqual(stats["encoding"], "utf-8")                       # plain ASCII is valid UTF-8; the dash test above is the Windows-1252 one

    def test_a_notice_seen_before_is_not_new_and_a_changed_one_is_changed(self):
        _, surfaced, _, _ = sam.analyse(self.path, RULE, {})
        seen = {r["notice_id"]: {"fingerprint": r["fingerprint"]} for r in surfaced}
        stats, _, new, changed = sam.analyse(self.path, RULE, seen)
        self.assertEqual((stats["new"], stats["changed"], stats["unchanged"]), (0, 0, 2))
        seen["id2"] = {"fingerprint": "old"}
        stats, _, new, changed = sam.analyse(self.path, RULE, seen)
        self.assertEqual(([r["notice_id"] for r in changed], stats["unchanged"]), (["id2"], 1))


class Main(unittest.TestCase):
    def run_main(self, *extra):
        d = tempfile.mkdtemp()
        sam.shutil_path = None
        args = ["--cached", "--cache", d + "/cache", "--seen", d + "/seen.json", "--out", d + "/out", *extra]
        return d, args

    def test_a_cached_run_reports_remembers_and_keeps_no_contact_and_a_second_run_finds_nothing_new(self):
        import os, shutil, contextlib
        d, args = self.run_main()
        os.makedirs(d + "/cache")
        shutil.copy(write_csv([row(1, "Section 508 Remediation Services"), row(2, "Grease trap cleaning")]), d + "/cache/" + sam.FILE)
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(sam.main(args), 0)
        out = [f for f in os.listdir(d + "/out") if f.startswith("sam-opportunities-")]
        doc = load(os.path.join(d, "out", out[0]))
        self.assertEqual([r["notice_id"] for r in doc["records"]], ["id1"])
        self.assertNotIn("pat@agency.example", json.dumps(doc))
        self.assertEqual(list(load(d + "/seen.json")), ["id1"])
        with contextlib.redirect_stdout(io.StringIO()):
            sam.main(args)
        self.assertEqual(load(os.path.join(d, "out", out[0]))["stats"]["new"], 0)

    def test_no_save_remembers_nothing_and_a_missing_cache_is_exit_3(self):
        import os, shutil, contextlib
        d, args = self.run_main("--no-save")
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(sam.main(args), 3)
        os.makedirs(d + "/cache")
        shutil.copy(write_csv([row(1, "Section 508 Remediation Services")]), d + "/cache/" + sam.FILE)
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(sam.main(args), 0)
        self.assertFalse(os.path.exists(d + "/seen.json"))

    def test_no_key_is_used_or_read(self):
        with open(sam.__file__, encoding="utf-8") as f:
            src = f.read()
        for gone in ("api_key=", "os.environ", "getenv", "api.sam.gov", "Authorization"):
            self.assertNotIn(gone, src)


if __name__ == "__main__":
    unittest.main()
