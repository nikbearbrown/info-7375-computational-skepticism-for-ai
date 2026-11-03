#!/usr/bin/env python3
"""sam_opportunities.py — SAM.gov's public Contract Opportunities extract: which open notices name Section 508 or digital accessibility, and which are new or changed?

    python3 sam_opportunities.py                  # check the extract (at most one check a day), read it, report; saves what it has seen
    python3 sam_opportunities.py --cached         # no request at all: read the file already in runs/sam-cache/
    python3 sam_opportunities.py --no-save        # report without remembering the notices (a dry run of the diff)

Professor Bear, 2026-11-02: use the public extract, not the Get Opportunities API (a personal key without a role is capped at 10 requests a day). The extract
(ContractOpportunitiesFullCSV.csv, about 213 MB, refreshed nightly) needs no login and no key. No key is used or read here: SAM_API_KEY is not needed.

How it behaves, and why:
  * One check a day. If today's check is already recorded, no request is made. Otherwise ONE conditional request (If-None-Match / If-Modified-Since): an unchanged
    file answers 304 and nothing is downloaded; a changed file is streamed to disk (never held in memory), its size checked against Content-Length, then put in place.
  * The official address answers 303 to a signed link on SAM.gov's own storage host; that one redirect is followed, to that host only (collect.py's allowlist).
  * The file is not UTF-8 (a Windows-1252 en dash is in the first 300 KB). The encoding is detected, undecodable bytes are counted, and a row with the wrong number
    of fields is counted and skipped, never guessed at.
  * Only the fields the judge needs are kept. The contact names, emails, phones and faxes in the file are dropped as it is read: this repo is public and the post carries no
    person's name.
  * A notice is surfaced when its TITLE has a federal508_rule phrase, or its DESCRIPTION has a phrase of federal508_rule.opportunity_work_phrases ('508 testing', 'trusted
    tester', 'accessibility remediation' ...: 508 as the WORK asked for). A description that only names Section 508 or WCAG is counted as a mention, and one that only has the
    generic word 'accessibility' is counted too: neither is surfaced, because they are mostly a requirement clause in a notice for something else (2026-11-02: 23 of 23).
    Only notices marked Active are surfaced.
  * New or changed is by NoticeId and a fingerprint of title, type, dates and description: runs/sam-seen.json remembers the surfaced notices.

This is research for the federal-508 channel, not a feed: contract opportunities are solicitations a business bids on, not job postings, and nothing here posts anywhere.

Writes: <out>/sam-opportunities-<date>.json    the new and changed notices (local, not committed), runs/sam-seen.json, runs/sam-cache/ (the raw file and its ETag; local)
Exit 0 ran, 2 bad input or an extract that does not look right, 3 the extract could not be fetched and there is no cached copy.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, codecs, collections, csv, datetime as dt, hashlib, json, os, re, sys, urllib.error, urllib.request
from urllib.parse import urlparse

import collect
import engine_jobs as ej

URL = "https://sam.gov/api/prod/fileextractservices/v1/api/download/Contract%20Opportunities/datagov/ContractOpportunitiesFullCSV.csv?privacy=Public"
STORAGE_HOST = "falextracts.s3.amazonaws.com"
CACHE = os.path.join(lp.RUNS, "sam-cache")
FILE = "ContractOpportunitiesFullCSV.csv"
SEEN = os.path.join(lp.RUNS, "sam-seen.json")

# the extract's column -> the name kept. No contact column is here on purpose.
KEEP = {"NoticeId": "notice_id", "Title": "title", "Sol#": "solicitation", "Department/Ind.Agency": "agency", "Sub-Tier": "sub_tier", "Office": "office",
        "PostedDate": "posted", "Type": "type", "BaseType": "base_type", "ArchiveDate": "archive_date", "ResponseDeadLine": "response_deadline",
        "SetASide": "set_aside", "SetASideCode": "set_aside_code", "NaicsCode": "naics", "ClassificationCode": "psc", "PopCity": "city", "PopState": "state",
        "PopCountry": "country", "Active": "active", "AwardDate": "award_date", "Award$": "award_amount", "Awardee": "awardee", "Link": "url", "Description": "description"}
CHUNK = 1 << 20
DESCRIPTION_KEPT = 2000     # characters of a surfaced notice's description kept in the output


# ---------------------------------------------------------------- fetch
def _open(url, headers):
    """GET without following a redirect. A 303 or 304 is returned as the response (it carries .code and .headers); any other error raises."""
    req = urllib.request.Request(collect._checked(url), headers={"User-Agent": collect.USER_AGENT, **headers})
    try:
        return urllib.request.build_opener(collect._NoRedirect).open(req, timeout=120)
    except urllib.error.HTTPError as e:
        if e.code in (303, 304):
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


def save_meta(meta, cache=CACHE):
    with open(os.path.join(cache, FILE + ".meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=1)


def fetch_extract(cache=CACHE, today=None, opener=None):
    """Make sure runs/sam-cache/ holds the newest extract. -> (path, outcome) with outcome 'checked-today' (no request), 'unchanged' (a 304) or 'downloaded'."""
    opener = opener or _open
    today = today or dt.date.today().isoformat()
    path = os.path.join(cache, FILE)
    meta = load_meta(cache)
    if os.path.exists(path) and meta.get("checked_on") == today:
        return path, "checked-today"
    os.makedirs(cache, exist_ok=True)
    first = opener(URL, {"Accept": "*/*"})
    if _status(first) != 303 or not first.headers.get("Location"):
        raise ValueError(f"the download address did not answer with a redirect (status {_status(first)})")
    where = urlparse(first.headers["Location"])
    if where.scheme != "https" or where.hostname != STORAGE_HOST:
        raise collect.InputError(f"refusing the redirect to {where.hostname!r}: only {STORAGE_HOST}")
    conditional = {}
    if os.path.exists(path) and meta.get("etag"):
        conditional["If-None-Match"] = meta["etag"]
        if meta.get("last_modified"):
            conditional["If-Modified-Since"] = meta["last_modified"]
    r = opener(first.headers["Location"], conditional)
    if _status(r) == 304:
        meta["checked_on"] = today
        save_meta(meta, cache)
        return path, "unchanged"
    if _status(r) != 200:
        raise ValueError(f"the extract answered {_status(r)}")
    want = int(r.headers.get("Content-Length") or 0)
    tmp, got = path + ".part", 0
    try:
        with open(tmp, "wb") as f:
            while True:
                b = r.read(CHUNK)
                if not b:
                    break
                f.write(b)
                got += len(b)
    finally:
        r.close()
    if (want and got != want) or got == 0:
        os.remove(tmp)
        raise ValueError(f"the download stopped short: {got} of {want} bytes")
    os.replace(tmp, path)
    save_meta({"etag": r.headers.get("ETag"), "last_modified": r.headers.get("Last-Modified"), "bytes": got, "fetched_on": today, "checked_on": today}, cache)
    return path, "downloaded"


# ---------------------------------------------------------------- read
def detect_encoding(path):
    """'utf-8-sig' if there is a byte order mark, 'utf-8' if the whole file decodes as UTF-8, otherwise 'cp1252' (the extract's actual encoding)."""
    with open(path, "rb") as f:
        head = f.read(3)
        if head == codecs.BOM_UTF8:
            return "utf-8-sig"
        f.seek(0)
        dec = codecs.getincrementaldecoder("utf-8")("strict")
        try:
            while True:
                b = f.read(CHUNK)
                dec.decode(b, final=not b)
                if not b:
                    return "utf-8"
        except UnicodeDecodeError:
            return "cp1252"


def read_rows(path, counts=None):
    """Yield one dict of the kept fields per well-formed row. `counts` (a Counter) gets rows, malformed, undecodable. Raises InputError if a column is missing."""
    counts = counts if counts is not None else collections.Counter()
    csv.field_size_limit(min(sys.maxsize, 2 ** 31 - 1))
    enc = detect_encoding(path)
    counts["encoding_" + enc] += 1
    with open(path, encoding=enc, errors="replace", newline="") as f:
        rd = csv.reader(f)
        try:
            head = [h.strip().lstrip("﻿") for h in next(rd)]
        except StopIteration:
            raise collect.InputError("the extract is empty")
        missing = [c for c in KEEP if c not in head]
        if missing:
            raise collect.InputError(f"the extract has no column {missing}: it is not the file this was written for")
        at = {c: head.index(c) for c in KEEP}
        while True:
            try:
                row = next(rd)
            except StopIteration:
                return
            except csv.Error:
                counts["malformed"] += 1
                continue
            counts["rows"] += 1
            if len(row) != len(head):
                counts["malformed"] += 1
                continue
            rec = {KEEP[c]: row[i].strip() for c, i in at.items()}
            counts["undecodable"] += sum(v.count("�") for v in rec.values())
            yield rec


# ---------------------------------------------------------------- judge
def phrase_finder(rule):
    """-> find(text) giving [(group, phrase)] for the enabled groups' phrases, whole words only (so '508' in a part number is not 'section 508')."""
    where = {}
    for g, spec in (rule.get("groups") or {}).items():
        if spec.get("enabled"):
            for p in spec.get("phrases") or []:
                where.setdefault(p.lower(), g)
    if not where:
        return lambda text: []
    rx = re.compile(r"(?<![a-z0-9])(" + "|".join(re.escape(p) for p in sorted(where, key=len, reverse=True)) + r")(?![a-z0-9])")
    return lambda text: [(where[p], p) for p in dict.fromkeys(rx.findall(text.lower()))]


def work_finder(rule):
    """-> find(text) giving the opportunity_work_phrases found, whole words only: the phrases that say 508 or accessibility is the work asked for."""
    phrases = sorted({p.lower() for p in rule.get("opportunity_work_phrases") or []}, key=len, reverse=True)
    if not phrases:
        return lambda text: []
    rx = re.compile(r"(?<![a-z0-9])(" + "|".join(re.escape(p) for p in phrases) + r")(?![a-z0-9])")
    return lambda text: list(dict.fromkeys(rx.findall(text.lower())))


def strength(rec, find, rule, work=None):
    """'title' | 'description-work' | 'description-mention' | 'description-accessibility' | None. Fills rec['title_hits'] / rec['description_hits'] / rec['work_phrases'].
    Only the first two are surfaced: a description that names Section 508 without asking for 508 work is a mention (a requirement clause), not an opportunity."""
    blank = (lambda t: ej.blanked(t, rule)) if rule.get("false_friends") else (lambda t: t)
    rec["title_hits"] = find(blank(rec["title"]))
    rec["description_hits"] = find(blank(rec["description"]))
    rec["work_phrases"] = (work or work_finder(rule))(blank(rec["description"]))
    if rec["title_hits"]:
        return "title"
    if rec["work_phrases"]:
        return "description-work"
    if any(g == "section-508" for g, _ in rec["description_hits"]):
        return "description-mention"
    return "description-accessibility" if rec["description_hits"] else None


def fingerprint(rec):
    return hashlib.sha1("\x1f".join(rec[k] for k in ("title", "type", "active", "archive_date", "response_deadline", "description")).encode("utf-8")).hexdigest()


def load_seen(path=SEEN):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}


def diff(surfaced, seen):
    """-> (new, changed, unchanged_count). Each surfaced record gets rec['change'] and rec['fingerprint']."""
    new, changed, same = [], [], 0
    for r in surfaced:
        r["fingerprint"] = fp = fingerprint(r)
        old = seen.get(r["notice_id"])
        if old is None:
            r["change"] = "new"
            new.append(r)
        elif old.get("fingerprint") != fp:
            r["change"] = "changed"
            changed.append(r)
        else:
            same += 1
    return new, changed, same


def analyse(path, rule, seen):
    """Read the whole extract once. -> (stats, surfaced records, new, changed)."""
    find, work = phrase_finder(rule), work_finder(rule)
    counts, types, by, surfaced = collections.Counter(), collections.Counter(), collections.Counter(), []
    for rec in read_rows(path, counts):
        types[rec["type"]] += 1
        s = strength(rec, find, rule, work)
        if rec["active"].lower() == "yes":
            counts["active"] += 1
        if not s:
            continue
        by[s] += 1
        if s in ("title", "description-work") and rec["active"].lower() == "yes":
            rec["strength"] = s
            surfaced.append(rec)
    new, changed, same = diff(surfaced, seen)
    stats = {"rows": counts["rows"], "malformed_rows": counts["malformed"], "undecodable_characters": counts["undecodable"],
             "encoding": [k[9:] for k in counts if k.startswith("encoding_")][0], "active": counts["active"], "types": dict(types.most_common()),
             "matches_by_strength": dict(by), "surfaced": len(surfaced), "new": len(new), "changed": len(changed), "unchanged": same}
    return stats, surfaced, new, changed


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cached", action="store_true", help="no request: read the file already in the cache")
    ap.add_argument("--no-save", action="store_true", help="do not remember the surfaced notices")
    ap.add_argument("--out", default=None, help="default runs/<today>")
    ap.add_argument("--cache", default=CACHE)
    ap.add_argument("--seen", default=SEEN)
    a = ap.parse_args(argv)
    today = dt.date.today().isoformat()
    out = a.out or os.path.join(lp.RUNS, today)
    path = os.path.join(a.cache, FILE)
    try:
        if a.cached:
            if not os.path.exists(path):
                print("no cached extract: run without --cached once", file=sys.stderr)
                return 3
            outcome = "cached (no request)"
        else:
            try:
                path, outcome = fetch_extract(a.cache, today)
            except (OSError, ValueError, urllib.error.URLError, collect.InputError) as e:
                if not os.path.exists(path):
                    print(f"the extract could not be fetched ({type(e).__name__}: {e}) and there is no cached copy", file=sys.stderr)
                    return 3
                print(f"the extract could not be checked ({type(e).__name__}: {e}); reading the cached copy", file=sys.stderr)
                outcome = "cached (the check failed)"
        with open(lp.config("keywords.json"), encoding="utf-8") as f:
            rule = json.load(f)["federal508_rule"]
        stats, surfaced, new, changed = analyse(path, rule, load_seen(a.seen))
    except collect.InputError as e:
        print(f"INPUT ERROR: {e}", file=sys.stderr)
        return 2
    meta = load_meta(a.cache)
    os.makedirs(out, exist_ok=True)
    shown = [dict(r, description=r["description"][:DESCRIPTION_KEPT]) for r in new + changed]
    dest = os.path.join(out, f"sam-opportunities-{today}.json")
    collect.write_json(dest, {"tool": "lectern sam_opportunities", "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                              "note": "New and changed SAM.gov contract notices that name Section 508 or digital accessibility. Research, not a feed. No contacts kept.",
                              "extract": {"outcome": outcome, "etag": meta.get("etag"), "last_modified": meta.get("last_modified"), "bytes": meta.get("bytes")},
                              "stats": stats, "records": shown})
    if not a.no_save:
        seen = load_seen(a.seen)
        seen.update({r["notice_id"]: {"fingerprint": r["fingerprint"], "last_seen": today} for r in surfaced})
        collect.write_json(a.seen, seen)
    print(f"extract: {outcome}; {stats['rows']:,} rows ({stats['encoding']}; {stats['malformed_rows']} malformed, {stats['undecodable_characters']} undecodable characters), {stats['active']:,} active")
    print(f"matches: {stats['matches_by_strength']}; surfaced (active; a phrase in the title or a work phrase in the description): {stats['surfaced']}: {stats['new']} new, {stats['changed']} changed, {stats['unchanged']} unchanged")
    print(f"-> {os.path.basename(dest)}" + ("" if not a.no_save else "  (nothing remembered)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
