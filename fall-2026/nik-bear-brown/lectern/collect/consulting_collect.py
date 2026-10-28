#!/usr/bin/env python3
"""consulting_collect.py — read the job boards of the consulting firms on the list, for the consulting channel only.

    python3 consulting_collect.py [--out runs/DATE] [--only SLUG]

The firms are the `consulting` section of config/targets.json with status `active` (a board Lectern's own readers can read:
Greenhouse, Ashby, SmartRecruiters). One request per board, a pause between boards, the same host list and user agent as
collect.py. It reads the postings' LISTS (title, place, link), never the ad text: the consulting judge reads titles.

This is deliberately NOT part of collect.py: collect.py reads the watch list for the #professor-bear feed, and the consulting
firms must never enter it (config/sources.json is generated from the `boards` section only; a test checks it).

Writes: <out>/consulting-jobs-<date>.json     every posting found, in the shape publish/consulting_feed.py and the judge read
        <out>/consulting-raw/<provider>-<slug>-<date>.json   each response as the board sent it (kept local, not committed)
Exit 0 ran, 2 bad input, 3 every board failed.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, datetime as dt, json, os, sys, time
from urllib.parse import quote

import collect

PAUSE = 1.2          # seconds between boards: a polite pace, one request per board unless a list has more than one page


def boards_from_targets(doc):
    """[(firm, provider, slug)] for the consulting firms whose board Lectern can read (status active)."""
    return [(t["name"], t["provider"], t["consulting"]["board"]["slug"]) for t in doc["targets"]
            if t.get("section") == "consulting" and t.get("status") == "active"]


def fetch_list(provider, slug):
    """The board's list of postings as the board sent it. Never the ad text."""
    if provider == "greenhouse":
        return collect.get(f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs")
    if provider == "ashby":
        return collect.get(f"https://api.ashbyhq.com/posting-api/job-board/{quote(slug)}")
    if provider == "smartrecruiters":
        return collect.fetch_board("smartrecruiters", slug, want_detail=False)          # the list only: no call per posting
    raise collect.InputError(f"unknown provider {provider!r}")


def records(provider, firm, slug, payload):
    """One board's payload -> [{source, company, source_id, title, url, location_text, department, date_posted}]."""
    out = []
    for j in payload.get("jobs") or []:
        if provider == "greenhouse":
            r = dict(source_id=str(j.get("id")), title=(j.get("title") or "").strip(), url=j.get("absolute_url"),
                     location_text=(j.get("location") or {}).get("name", ""), department="", date_posted=collect.iso_date(j.get("first_published") or j.get("updated_at")))
        elif provider == "ashby":
            locs = [j.get("location") or ""] + [x.get("location") or "" for x in (j.get("secondaryLocations") or [])]
            r = dict(source_id=str(j.get("id")), title=(j.get("title") or "").strip(), url=j.get("jobUrl"), location_text=" · ".join(x for x in locs if x),
                     department=" / ".join(x for x in (j.get("department"), j.get("team")) if x), date_posted=collect.iso_date(j.get("publishedAt")))
        else:   # smartrecruiters list item
            loc = j.get("location") or {}
            r = dict(source_id=str(j.get("id")), title=(j.get("name") or "").strip(), url=f"https://jobs.smartrecruiters.com/{slug}/{j.get('id')}",
                     location_text=loc.get("fullLocation") or ", ".join(x for x in (loc.get("city"), loc.get("region"), (loc.get("country") or "").upper()) if x),
                     department=((j.get("function") or {}).get("label") or ""), date_posted=collect.iso_date(j.get("releasedDate")))
        out.append({"source": provider, "company": firm, **r})
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--targets", default=lp.config("targets.json"))
    ap.add_argument("--out", default=None, help="default runs/<today>")
    ap.add_argument("--only", help="one board slug")
    a = ap.parse_args(argv)
    today = dt.date.today().isoformat()
    out = a.out or os.path.join(lp.RUNS, today)
    try:
        with open(a.targets, encoding="utf-8") as f:
            boards = boards_from_targets(json.load(f))
    except (OSError, json.JSONDecodeError, KeyError) as e:
        print(f"INPUT ERROR: {e}", file=sys.stderr)
        return 2
    boards = [b for b in boards if not a.only or b[2] == a.only]
    raw_dir = os.path.join(out, "consulting-raw")
    os.makedirs(raw_dir, exist_ok=True)
    recs, status = [], []
    for i, (firm, provider, slug) in enumerate(boards):
        if i:
            time.sleep(PAUSE)
        try:
            payload = fetch_list(provider, slug)
            collect.write_json(os.path.join(raw_dir, f"{provider}-{slug.lower()}-{today}.json"), payload)      # raw first
        except Exception as e:                                                                                  # one board failing does not stop the others
            status.append({"company": firm, "provider": provider, "status": "unavailable", "reason": f"{type(e).__name__}: {e}"})
            print(f"  {firm:28} UNAVAILABLE ({type(e).__name__})", file=sys.stderr)
            continue
        got = records(provider, firm, slug, payload)
        recs += got
        status.append({"company": firm, "provider": provider, "status": "ok", "postings": len(got)})
        print(f"  {firm:28} {len(got):4} postings")
    if not any(s["status"] == "ok" for s in status):
        print("every board failed or none is listed: nothing written", file=sys.stderr)
        return 3
    path = os.path.join(out, f"consulting-jobs-{today}.json")
    collect.write_json(path, {"tool": "lectern consulting_collect", "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                              "note": "Every posting on the consulting firms' readable boards: title, place and link only. Not the watch list of the #professor-bear feed.",
                              "sources": status, "records": recs})
    print(f"\n{len(recs)} postings from {sum(1 for s in status if s['status'] == 'ok')} of {len(boards)} boards -> {os.path.basename(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
