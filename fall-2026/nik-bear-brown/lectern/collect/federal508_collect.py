#!/usr/bin/env python3
"""federal508_collect.py — read the job boards of the federal-508 employers on the list, for the federal-508 channel only.

    python3 federal508_collect.py [--out runs/DATE] [--only SLUG]

The employers are the `federal508` section of config/targets.json with status `active` (a board Lectern's own readers can read: Greenhouse, Ashby,
SmartRecruiters, Workday). One request per board (Workday: one per page of 20 postings), a pause between requests, the same host list and user agent as collect.py. It reads the postings' LISTS (title, place,
link), never the ad text: the judge reads titles. (USAJOBS' answer carries each posting's summary and duties; they are kept in the local run file and the judge looks in them only for the phrases that say 508 is the work.) The readers and the record shape are consulting_collect.py's, written once.

This is deliberately NOT part of collect.py: collect.py reads the watch list for the #professor-bear feed, and these employers must never enter it
(config/sources.json is generated from the `boards` section only; a test checks it).

Writes: <out>/federal508-jobs-<date>.json     every posting found, in the shape publish/federal508_feed.py and the judge read
        <out>/federal508-raw/<provider>-<slug>-<date>.json   each response as the board sent it (kept local, not committed)
Exit 0 ran, 2 bad input, 3 every board failed.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, datetime as dt, json, os, re, sys, time

import collect
import consulting_collect as cc
import federal508_jobs as fj

PAUSE = cc.PAUSE


def boards_from_targets(doc):
    """[(employer, provider, slug)] for the employers whose board Lectern can read (status active)."""
    return [(t["name"], t["provider"], t["federal508"]["board"]["slug"]) for t in doc["targets"]
            if t.get("section") == "federal508" and t.get("status") == "active"]


def name_the_places(recs, slug, rule, pause=None):
    """The federal-508 channel: look up the places of the Workday postings whose TITLE already has a Section 508 or accessibility phrase and whose place is only
    a count (consulting_collect.name_places does the look-up and keeps the count if it fails)."""
    return cc.name_places(recs, slug, lambda r: bool(fj.role_hits(r["title"], rule)), pause)


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
    with open(lp.config("keywords.json"), encoding="utf-8") as f:
        rule = json.load(f)["federal508_rule"]
    raw_dir = os.path.join(out, "federal508-raw")
    os.makedirs(raw_dir, exist_ok=True)
    recs, status = [], []
    for i, (name, provider, slug) in enumerate(boards):
        if i:
            time.sleep(PAUSE)
        try:
            payload = cc.fetch_list(provider, slug)
            collect.write_json(os.path.join(raw_dir, cc.raw_name(provider, slug, today)), payload)      # raw first
        except Exception as e:                                                                                  # one board failing does not stop the others
            status.append({"company": name, "provider": provider, "status": "unavailable", "reason": f"{type(e).__name__}: {e}"})
            print(f"  {name:28} UNAVAILABLE ({type(e).__name__})", file=sys.stderr)
            continue
        got = cc.records(provider, name, slug, payload)
        if provider == "workday":
            got = name_the_places(got, slug, rule)
        recs += got
        status.append(cc.board_ok(name, provider, got, payload))
        print(f"  {name:28} {len(got):4} postings" + ("" if status[-1].get("complete", True) else f"  (the board lists {payload['total']}: not all came back)"))
    if not any(s["status"] == "ok" for s in status):
        print("every board failed or none is listed: nothing written", file=sys.stderr)
        return 3
    path = os.path.join(out, f"federal508-jobs-{today}.json")
    collect.write_json(path, {"tool": "lectern federal508_collect", "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                              "note": "Every posting on the federal-508 employers' readable boards: title, place and link only. Not the watch list of the #professor-bear feed.",
                              "sources": status, "records": recs})
    print(f"\n{len(recs)} postings from {sum(1 for s in status if s['status'] == 'ok')} of {len(boards)} boards -> {os.path.basename(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
