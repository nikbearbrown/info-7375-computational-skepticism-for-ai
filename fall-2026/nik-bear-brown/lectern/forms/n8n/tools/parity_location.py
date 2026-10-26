#!/usr/bin/env python3
"""Parity test for the two gates: the Python place reader and K-12 reader (lectern/collect/collect.py: where(), k12_hits())
and their JavaScript ports (shared/lib/judge.js) must give the same answer for every location line and every title.

Needs a jobs.jsonl with `locations` and `title` (the ai-jobs snapshot) and a Lectern checkout. Example:
  python3 tools/parity_location.py --jobs-jsonl PATH/jobs.jsonl
"""
import argparse, json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def _default_lectern():
    """The Python Lectern, when this folder sits inside it (as in the course repository: lectern/forms/n8n/)."""
    d = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))      # lectern/, which holds forms/n8n/
    return d if os.path.exists(os.path.join(d, "lectern_paths.py")) else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lectern", default=_default_lectern())
    ap.add_argument("--jobs-jsonl", required=True)
    ap.add_argument("--keywords", help="default: <lectern>/config/keywords.json")
    a = ap.parse_args()
    if not a.lectern:
        ap.error("--lectern is required (or put this folder beside a lectern/ folder)")
    sys.path.insert(0, os.path.abspath(a.lectern))
    import lectern_paths as lp
    import collect
    kwp = a.keywords or lp.config("keywords.json")
    kw = json.load(open(kwp, encoding="utf-8"))
    rows = [json.loads(l) for l in open(a.jobs_jsonl, encoding="utf-8") if l.strip()]
    locations = sorted({" · ".join(r.get("locations") or []) for r in rows} | {loc for r in rows for loc in r.get("locations") or []})
    titles = sorted({r["title"] for r in rows})
    py_loc = [collect.where(t, kw["location_rule"]) for t in locations]
    py_k12 = [collect.k12_hits(t, "", kw["k12_rule"])["title"] for t in titles]
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as t:
        json.dump({"locations": locations, "titles": titles}, t, ensure_ascii=False)
    out = subprocess.run(["node", os.path.join(HERE, "js_where.js"), kwp, t.name], capture_output=True, text=True, check=True).stdout
    os.unlink(t.name)
    js = json.loads(out)
    bad_loc = [(locations[i], py_loc[i], js["locations"][i]) for i in range(len(locations)) if py_loc[i] != js["locations"][i]]
    bad_k12 = [(titles[i], py_k12[i], js["titles"][i]) for i in range(len(titles)) if py_k12[i] != js["titles"][i]]
    print(f"location lines: {len(locations):,}   titles: {len(titles):,}   K-12 titles found: {sum(1 for x in py_k12 if x)}")
    if not bad_loc and not bad_k12:
        print(f"PARITY: Python and JavaScript agree on all {len(locations):,} location lines and all {len(titles):,} titles")
        return 0
    for name, bad in (("location", bad_loc), ("K-12 title", bad_k12)):
        if bad:
            print(f"DIFFERENT on {len(bad)} {name}s, e.g.:")
            for b in bad[:5]:
                print("   ", b)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
