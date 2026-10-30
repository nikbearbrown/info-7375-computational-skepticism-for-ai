#!/usr/bin/env python3
"""audit_speakers.py — read the speaker leads the way the judge does, and show what each score is made of.

    python3 audit_speakers.py [--leads runs/DATE/speakers-leads-DATE.json] [--min-score N]

Read-only. For every company: the decision, the score and its parts, which sourced signals it has and which are missing, and (when the
leads file was written with --check) which links did not answer 2xx. Then the same list with each signal REMOVED one at a time, to show
which single signal a company's place depends on, and a count of how many companies a different min_score would post. It judges nothing a
person should judge: it lists. Stdlib only. No person is named.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, collections, copy, glob, json, os

import speakers_judge as sj


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--leads", default=None, help="default: the newest runs/*/speakers-leads-*.json")
    ap.add_argument("--keywords", default=lp.config("keywords.json"))
    ap.add_argument("--min-score", type=int, default=None)
    a = ap.parse_args(argv)
    path = a.leads or (sorted(glob.glob(os.path.join(lp.RUNS, "*", "speakers-leads-*.json"))[-1:]) or [None])[0]
    if not path:
        print("No leads file: run python3 collect/speakers_collect.py first.")
        return 2
    with open(a.keywords, encoding="utf-8") as f:
        kw = json.load(f)
    if a.min_score is not None:
        kw["speakers_rule"]["min_score"] = a.min_score
    rows = sj.load_postings(path)
    judged = [(v, rec, sj.judge_speaker(v, rec, kw)) for v, rec in rows]
    dec = collections.Counter(r["decision"] for _, _, r in judged)
    print(f"{len(judged)} companies from {os.path.basename(path)} · min_score {kw['speakers_rule']['min_score']} · " + " · ".join(f"{k} {n}" for k, n in dec.most_common()))
    print("\ncompany · decision · score · parts · missing")
    allsig = ["mcp_docs", "devrel_team", "mcp_talk", "community_channel", "named_people", "contact_route"]
    for v, rec, r in sorted(judged, key=lambda x: (-x[2]["score"], x[0]["company"])):
        miss = [k for k in allsig if k not in r["parts"]]
        print(f"  {v['company'][:28]:28} {r['decision']:9} {r['score']:3}  " + ", ".join(f"{k} {n}" for k, n in r["parts"].items()) + (f"   missing: {', '.join(miss)}" if miss else ""))
        bad = [u for u, c in (rec.get("checks") or {}).items() if not str(c.get("status", "")).startswith("2")]
        if bad:
            print(f"      links not 2xx: {', '.join(bad)}")
    print("\nposted companies that lose their place if one signal is removed (min_score margin):")
    margin = collections.Counter()
    for v, rec, r in judged:
        if r["decision"] != "post":
            continue
        need = [k for k, n in r["parts"].items() if r["score"] - n < kw["speakers_rule"]["min_score"] or k in ("mcp_docs", "contact_route")]
        if need:
            print(f"  {v['company'][:28]:28} depends on: {', '.join(need)}")
            margin.update(need)
    print("\nhow many would post at other minimums: " + ", ".join(f"{m}: {sum(1 for _, _, r in judged if r['score'] >= m and 'mcp_docs' in r['parts'] and 'contact_route' in r['parts'] and r['decision'] != 'rejected')}" for m in (40, 50, 60, 70, 80)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
