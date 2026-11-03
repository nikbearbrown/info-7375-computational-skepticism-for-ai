#!/usr/bin/env python3
"""ca_school_districts.py — California school districts and county offices of education, as a lead list for a small Section 508 testing firm (one of the non-federal markets).

    python3 ca_school_districts.py                   # read the cached file (fetched at most once a month), rank, write the lead files, print the top
    python3 ca_school_districts.py --refresh         # fetch the file again even if the cached copy is recent
    python3 ca_school_districts.py --exclude NAME    # also leave out any office whose name contains NAME (repeatable)

Professor Bear, 2026-11-02, for a friend who is starting a small Section 508 testing firm: 'start with schools' (her brief: school districts and county offices of education, and the
schools for the deaf and blind). The source is the California Department of Education's own list of district offices (2025-26) as published on the state's open-data hub,
gis.data.ca.gov: 1,009 rows (elementary, unified and high school districts, the 56 county offices of education, charter authorizers and the state special schools), each with its
enrollment and the number of students with disabilities. It has no website, no contact and no person in it.

Not used, on purpose: the CDE's own directory download (sd.cde.ca.gov) answers a script with a bot-detection challenge and is left alone; the Urban Institute and data.ca.gov APIs have
`Disallow: /api/` in their robots.txt. The hub's download address is not disallowed (its robots.txt asks for a 60-second crawl delay between requests, so this makes ONE request,
at most once a month: the file is a school year's data). The address answers with redirects (gis.data.ca.gov, then services3.arcgis.com, then a signed link on ArcGIS's own storage, *.az.arcgis.com); they are followed by hand,
https only, to those hosts and nowhere else, and the signed link is never printed. The robots.txt of services3.arcgis.com answers 403, so it could not be read: it is only the redirect step of the hub's own advertised download.

Leads are ranked by enrollment (bigger offices have more public pages and more to remediate), with the share of students with disabilities beside it. That is a size ranking, not a
measure of need or of any legal deadline: whether an office is covered by a particular deadline depends on a population figure that is not in this file.

Names the person asked to leave out are NOT in this repo: they are read from runs/lead-exclusions.txt (one name per line, local, not committed) and from --exclude.

Writes: <out>/ca-school-district-leads-<date>.json and .csv    the ranked list (local, not committed); runs/ca-districts-cache/ (the raw file)
Exit 0 ran, 2 bad input or a file that does not look right, 3 the file could not be fetched and there is no cached copy.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, collections, csv, datetime as dt, io, json, os, sys, urllib.error, urllib.request
from urllib.parse import urlparse

import collect

URL = "https://gis.data.ca.gov/api/download/v1/items/9abf6c0c6a5040d29a99e211b27e3414/csv?layers=0"
CACHE = os.path.join(lp.RUNS, "ca-districts-cache")
FILE = "ca-district-offices-2025-26.csv"
EXCLUSIONS = os.path.join(lp.RUNS, "lead-exclusions.txt")
HOSTS = {"gis.data.ca.gov", "services3.arcgis.com"}     # the hub, and the ArcGIS service its download link redirects through (its robots.txt answers 403: nothing readable, nothing else is asked of it)
MAX_AGE_DAYS = 30
MAX_HOPS = 4
NEEDED = ["CDS Code", "County Name", "District Name", "District Type", "City", "Zip", "Enroll Total", "Students with Disabilities", "Students with Disabilities (%)", "Locale Description"]
TIERS = ((10000, "A: 10,000 students or more"), (2000, "B: 2,000 to 9,999"), (0, "C: under 2,000"))


def host_ok(url):
    p = urlparse(url)
    return p.scheme == "https" and (p.hostname in HOSTS or (p.hostname or "").endswith(".az.arcgis.com"))


def _open(url):
    """GET without following a redirect: a 3xx is returned as the response (.code, .headers); any other error raises."""
    req = urllib.request.Request(url, headers={"User-Agent": collect.USER_AGENT, "Accept": "*/*"})
    try:
        return urllib.request.build_opener(collect._NoRedirect).open(req, timeout=120)
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 303, 307, 308):
            return e
        raise


def _status(r):
    return getattr(r, "status", None) or getattr(r, "code", None)


def load_meta(cache=CACHE):
    try:
        with open(os.path.join(cache, FILE + ".meta.json"), encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}


def fetch(cache=CACHE, today=None, refresh=False, opener=None):
    """-> (path, outcome): 'cached' (no request) or 'downloaded'. One request chain at most, never more than once in MAX_AGE_DAYS unless refresh."""
    opener = opener or _open
    today = today or dt.date.today()
    path = os.path.join(cache, FILE)
    meta = load_meta(cache)
    if os.path.exists(path) and not refresh and meta.get("fetched_on"):
        if (today - dt.date.fromisoformat(meta["fetched_on"])).days < MAX_AGE_DAYS:
            return path, "cached"
    os.makedirs(cache, exist_ok=True)
    url = URL
    for _ in range(MAX_HOPS):
        if not host_ok(url):
            raise collect.InputError(f"refusing {urlparse(url).hostname!r}: only gis.data.ca.gov and *.az.arcgis.com, over https")
        r = opener(url)
        st = _status(r)
        if st in (301, 302, 303, 307, 308):
            url = r.headers.get("Location") or ""
            continue
        if st != 200:
            raise ValueError(f"the file answered {st}")
        break
    else:
        raise ValueError("too many redirects")
    want, got, tmp = int(r.headers.get("Content-Length") or 0), 0, path + ".part"
    try:
        with open(tmp, "wb") as f:
            while True:
                b = r.read(1 << 20)
                if not b:
                    break
                f.write(b)
                got += len(b)
    finally:
        r.close()
    if got == 0 or (want and got != want):
        os.remove(tmp)
        raise ValueError(f"the download stopped short: {got} of {want} bytes")
    os.replace(tmp, path)
    with open(os.path.join(cache, FILE + ".meta.json"), "w", encoding="utf-8") as f:
        json.dump({"fetched_on": today.isoformat(), "bytes": got}, f, indent=1)
    return path, "downloaded"


def to_int(v):
    try:
        return int(float(str(v).replace(",", "")))
    except (TypeError, ValueError):
        return None


def tier(enrollment):
    for floor, name in TIERS:
        if enrollment is not None and enrollment >= floor:
            return name
    return TIERS[-1][1]


def read_offices(path):
    """-> (rows, bad): the file's offices as small dicts (no contact, no demographics beyond students with disabilities), and how many rows had no usable enrollment."""
    with open(path, encoding="utf-8-sig", newline="") as f:
        rd = csv.DictReader(f)
        missing = [c for c in NEEDED if c not in (rd.fieldnames or [])]
        if missing:
            raise collect.InputError(f"the file has no column {missing}: it is not the file this was written for")
        rows, bad = [], 0
        for r in rd:
            e = to_int(r["Enroll Total"])
            if e is None:
                bad += 1
                continue
            swd = to_int(r["Students with Disabilities"])
            rows.append({"name": r["District Name"].strip(), "type": r["District Type"].strip(), "county": r["County Name"].strip(), "city": r["City"].strip(), "zip": r["Zip"].strip(),
                         "cds_code": r["CDS Code"].strip(), "enrollment": e, "students_with_disabilities": swd, "swd_percent": r["Students with Disabilities (%)"].strip(),
                         "locale": r["Locale Description"].strip(), "tier": tier(e)})
    return rows, bad


def read_exclusions(path=EXCLUSIONS):
    try:
        with open(path, encoding="utf-8") as f:
            return [l.strip() for l in f if l.strip() and not l.lstrip().startswith("#")]
    except OSError:
        return []


def rank(rows, exclude):
    """-> (kept, left_out): offices whose name contains an excluded name (case-folded) are left out; the rest are sorted by enrollment, biggest first."""
    ex = [x.casefold() for x in exclude if x.strip()]
    kept, out = [], []
    for r in rows:
        (out if any(x in r["name"].casefold() for x in ex) else kept).append(r)
    kept.sort(key=lambda r: (-r["enrollment"], r["name"]))
    return kept, out


def write_csv(path, rows):
    cols = ["rank", "name", "type", "county", "city", "zip", "enrollment", "students_with_disabilities", "swd_percent", "tier", "locale", "cds_code"]
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for i, r in enumerate(rows, 1):
            w.writerow([i] + [r[c] for c in cols[1:]])


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--exclude", action="append", default=[], help="leave out any office whose name contains this (repeatable)")
    ap.add_argument("--out", default=None, help="default runs/<today>")
    ap.add_argument("--cache", default=CACHE)
    ap.add_argument("--exclusions", default=EXCLUSIONS)
    a = ap.parse_args(argv)
    today = dt.date.today()
    try:
        try:
            path, outcome = fetch(a.cache, today, a.refresh)
        except (OSError, ValueError, urllib.error.URLError, collect.InputError) as e:
            path = os.path.join(a.cache, FILE)
            if not os.path.exists(path):
                print(f"the file could not be fetched ({type(e).__name__}: {str(e).split('?')[0][:150]}) and there is no cached copy", file=sys.stderr)
                return 3
            print(f"the file could not be fetched ({type(e).__name__}); reading the cached copy", file=sys.stderr)
            outcome = "cached (the fetch failed)"
        rows, bad = read_offices(path)
    except collect.InputError as e:
        print(f"INPUT ERROR: {e}", file=sys.stderr)
        return 2
    exclude = read_exclusions(a.exclusions) + a.exclude
    kept, out = rank(rows, exclude)
    outdir = a.out or os.path.join(lp.RUNS, today.isoformat())
    os.makedirs(outdir, exist_ok=True)
    stem = os.path.join(outdir, f"ca-school-district-leads-{today.isoformat()}")
    write_csv(stem + ".csv", kept)
    collect.write_json(stem + ".json", {"tool": "lectern ca_school_districts", "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "source": "California Department of Education district offices 2025-26, via gis.data.ca.gov",
                                        "note": "A size ranking of California school districts and county offices of education, not a measure of need or of any deadline. Names asked to be left out are not listed.",
                                        "counts": {"rows": len(rows) + bad, "unusable": bad, "left_out": len(out), "kept": len(kept), "by_type": dict(collections.Counter(r["type"] for r in kept)),
                                                   "by_tier": dict(collections.Counter(r["tier"] for r in kept))}, "leads": kept})
    print(f"file: {outcome}; {len(rows) + bad} offices, {bad} without usable enrollment, {len(out)} left out by request, {len(kept)} kept")
    for t, n in sorted(collections.Counter(r["tier"] for r in kept).items()):
        print(f"  {t}: {n}")
    print("  by type: " + "; ".join(f"{t} {n}" for t, n in collections.Counter(r["type"] for r in kept).most_common()))
    for r in kept[:12]:
        print(f"  {r['enrollment']:>8,}  {r['name'][:38]:38} {r['type'][:22]:22} {r['county']:14} {r['swd_percent']}% with disabilities")
    print(f"-> {os.path.basename(stem)}.csv / .json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
