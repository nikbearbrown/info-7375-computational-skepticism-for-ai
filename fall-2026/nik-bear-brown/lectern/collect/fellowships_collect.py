#!/usr/bin/env python3
"""fellowships_collect.py — read the program pages of the fellowships and residencies on the list, for the fellowships feed only.

    python3 fellowships_collect.py [--out runs/DATE] [--targets PATH]

The programs are the `fellowships` section of config/targets.json with status `active`. A program is a PAGE with an application
window, not a job posting, so this is not a board reader. For a program marked `read: "page"` it:
  1. fetches the host's robots.txt (one request) and stops if the page is disallowed for this user agent;
  2. fetches the program page (one request, same host only, https only, at most 3 redirects, a size cap);
  3. looks in the page's text for the sentence that gives the deadline ('close(s) on November 22, 2026', 'deadline: ...').
A program marked `read: "none"` (a page a script may not or cannot read) is not fetched: its deadline is the date a person recorded
in targets.json, and the record says so ('as listed'). Nothing here logs in, fills a form or contacts a program.

Writes <out>/fellowships-<date>.json  {"records": [view, ...]} in the shape publish/channel_feed.py reads (id, company, title,
location_text, url) plus kind, deadline (ISO date or ""), deadline_basis ("page", "listed" or "unread") and eligibility.
Exit 0 ran, 2 bad input.

This is deliberately NOT part of collect.py: the programs must never enter the #professor-bear job feed's watch list (config/sources.json is
generated from the `boards` section only).
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, datetime as dt, html, json, os, re, time, urllib.request, urllib.robotparser
from urllib.parse import urljoin, urlparse

import collect

PAUSE = 1.2
MAX_BYTES = 2_000_000
MAX_REDIRECTS = 3
MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
DATE = r"(?P<m>" + "|".join(m.capitalize() for m in MONTHS) + r")\s+(?P<d>\d{1,2}),?\s+(?P<y>20\d\d)"
# 'close on', 'closes', 'deadline', 'due', 'apply by', 'applications ... until': a cue, up to 60 characters that are not the end of a sentence, then a date
CUE = r"(?:clos(?:e|es|ed|ing)|deadline|due|apply by|submitted by|until)"
DEADLINE_RE = re.compile(rf"\b{CUE}\b[^.!?\n]{{0,60}}?{DATE}", re.I)


class _Sink(Exception):
    pass


def page_text(raw):
    """Visible text of an HTML page: scripts and styles dropped, tags dropped, entities decoded, whitespace folded."""
    t = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", " ", raw)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def find_deadline(text):
    """The first date that a deadline cue introduces -> ISO date, or "" when none. Never a date that merely appears on the page."""
    for m in DEADLINE_RE.finditer(text):
        try:
            return dt.date(int(m.group("y")), MONTHS.index(m.group("m").lower()) + 1, int(m.group("d"))).isoformat()
        except ValueError:
            continue
    return ""


class _SameHost(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to https on the same host (the trailing-slash 308 is the usual one)."""
    def __init__(self, host):
        self.host = host

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        u = urlparse(urljoin(req.full_url, newurl))
        if u.scheme != "https" or u.hostname != self.host:
            raise _Sink(f"redirect to {u.scheme}://{u.hostname} refused")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch(url, timeout=30):
    """-> (status, text). https only, redirects only within the host, a size cap. HTML or plain text only."""
    u = urlparse(url)
    if u.scheme != "https" or not u.hostname:
        raise ValueError(f"not an https address: {url!r}")
    req = urllib.request.Request(url, headers={"User-Agent": collect.USER_AGENT, "Accept": "text/html,text/plain"})
    with urllib.request.build_opener(_SameHost(u.hostname)).open(req, timeout=timeout) as r:
        ctype = (r.headers.get("Content-Type") or "").lower()
        if "html" not in ctype and "text" not in ctype:
            raise ValueError(f"not a text page: Content-Type {ctype!r}")
        body = r.read(MAX_BYTES + 1)
        if len(body) > MAX_BYTES:
            raise ValueError("page larger than the size cap")
        return r.status, body.decode(r.headers.get_content_charset() or "utf-8", errors="replace")


def robots_allows(url, fetcher=fetch):
    """True when the host's robots.txt lets this user agent fetch the page. A robots.txt that cannot be fetched at all (403, error) means NO: nothing readable."""
    u = urlparse(url)
    try:
        status, text = fetcher(f"https://{u.hostname}/robots.txt")
    except Exception:
        return False
    if status != 200:
        return False
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(text.splitlines())
    return rp.can_fetch("lectern", url) and rp.can_fetch("*", url)


def programs_from_targets(doc):
    return [t for t in doc["targets"] if t.get("section") == "fellowships" and t.get("status") == "active"]


def record(t, deadline, basis, note=""):
    f = t["fellowships"]
    url = t["data"][0]["url"] if t.get("data") else ""
    return {"id": f"{t['id']}:{deadline or 'no-date'}", "program": t["id"], "company": f["organization"], "title": t["name"],
            "location_text": f.get("place", ""), "url": url, "kind": f["kind"], "deadline": deadline, "deadline_basis": basis,
            "eligibility": f.get("eligibility", ""), "note": note}


def read_program(t, fetcher=fetch, pause=PAUSE):
    """One program -> one record. A page that cannot be read falls back to the recorded date and says 'listed' (never invents one)."""
    f = t["fellowships"]
    listed = f.get("deadline_listed", "")
    if f.get("read") != "page" or not t.get("data"):
        return record(t, listed, "listed" if listed else "unread", "not fetched: " + f.get("deadline_source", "no page a script may read"))
    url = t["data"][0]["url"]
    if not robots_allows(url, fetcher):
        return record(t, listed, "listed" if listed else "unread", "robots.txt does not allow it (or could not be read): not fetched")
    time.sleep(pause)
    try:
        _, raw = fetcher(url)
    except Exception as e:
        return record(t, listed, "listed" if listed else "unread", f"the page did not answer ({type(e).__name__})")
    d = find_deadline(page_text(raw))
    if d:
        note = "" if d == listed or not listed else f"the page says {d}; the date recorded was {listed}"
        return record(t, d, "page", note)
    return record(t, listed, "listed" if listed else "unread", "the page names no deadline sentence; the recorded date is kept")


def main(argv=None, fetcher=fetch):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--targets", default=lp.config("targets.json"))
    ap.add_argument("--out", default=None, help="default: runs/<today>")
    a = ap.parse_args(argv)
    with open(a.targets, encoding="utf-8") as f:
        doc = json.load(f)
    progs = programs_from_targets(doc)
    if not progs:
        print("no active program in the fellowships section")
        return 2
    today = dt.date.today().isoformat()
    out = a.out or os.path.join(lp.RUNS, today)
    os.makedirs(out, exist_ok=True)
    recs = []
    for i, t in enumerate(progs):
        if i:
            time.sleep(PAUSE)
        r = read_program(t, fetcher)
        recs.append(r)
        print(f"  {t['name']}: deadline {r['deadline'] or 'none'} ({r['deadline_basis']})" + (f" · {r['note']}" if r["note"] else ""))
    path = os.path.join(out, f"fellowships-{today}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"date": today, "records": recs}, f, indent=2, ensure_ascii=False)
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
