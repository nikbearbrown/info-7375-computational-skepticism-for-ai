#!/usr/bin/env python3
"""audit_gates.py — what do the two gates in keywords.json (location_rule, k12_rule) change?

    python3 audit_gates.py --raw runs/2026-10-18/raw [--out report.md]      # saved board responses: the whole filter, before and after
    python3 audit_gates.py --jobs-jsonl jobs.jsonl [--out report.md]        # a big sample with place fields but no ad text: the gates only

A gate is a rule that throws away a posting the keywords would have kept, so the only honest way to judge one is to
read what it threw away. With --raw this runs the filter twice over the same postings, once as keywords.json says and
once with the two gates removed, and lists every posting that only the gates dropped, with the reason the filter gave.
With --jobs-jsonl (the ai-jobs snapshot: `locations`, `country_codes`, `title`, no ad text) it checks the place reader
against the country codes the boards themselves report, and lists the K-12 titles it finds.

Read-only. Stdlib only. Judges nothing a person should judge: it lists.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, collections, glob, json, os, re

import collect


def load_views(raw_dir):
    """Every saved board response in raw_dir -> normalised, de-duplicated, valid postings (what collect.main() judges)."""
    cfg = json.load(open(lp.config("sources.json"), encoding="utf-8"))
    company = {(s["provider"], b["slug"].replace(" ", "_").lower()): b["company"] for s in cfg["sources"] for b in s["boards"]}
    watched = set(company.values())
    views, seen = [], set()
    for path in sorted(glob.glob(os.path.join(raw_dir, "*.json"))):
        m = re.match(r"(greenhouse|ashby|smartrecruiters)-(.+)-\d{4}-\d{2}-\d{2}\.json$", os.path.basename(path))
        if not m:
            continue
        provider, slug = m.groups()
        try:
            payload = json.load(open(path, encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for v in collect.normalise(provider, company.get((provider, slug), slug), payload):
            key = (v["source"], v["source_id"])
            if key in seen or not (v["title"] and v["url"] and v["date_posted"]):
                continue
            seen.add(key)
            views.append(v)
    return views, watched


def md_table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(str(c).replace("|", "/") for c in r) + " |" for r in rows]
    return out


def report_raw(raw_dir, kw):
    before_kw = {k: v for k, v in kw.items() if k not in ("location_rule", "k12_rule")}
    views, watched = load_views(raw_dir)
    rows = []
    for v in views:
        b, _ = collect.judge(v, before_kw)
        a, why = collect.judge(v, kw)
        rows.append((v, b, a, why))
    kept_b = [r for r in rows if r[1]]
    kept_a = [r for r in rows if r[2]]
    dropped = [r for r in kept_b if not r[2]]
    by_gate = collections.Counter()
    for _, _, _, why in dropped:
        loc, k12 = "country not allowed" in why or "no country named" in why, "K-12 role" in why
        by_gate["both" if loc and k12 else "country only" if loc else "K-12 only"] += 1
    unnamed = [r for r in kept_a if (r[2].get("location") or {}).get("country_named") is False]
    w = lambda rs: sum(1 for r in rs if r[0]["company"] in watched)
    L = ["# What the two gates change: " + os.path.basename(os.path.dirname(raw_dir.rstrip("/"))), "",
         f"**What this is.** The filter (rules v{kw['version']}) run twice over the same {len(rows):,} saved postings: as written, and with the "
         f"country rule and the K-12 rule taken out. Every posting that only the two gates dropped is listed below with the reason the filter gave, "
         f"so a person can read what was lost. **What was found.** The keywords alone keep {len(kept_b)}; with the gates {len(kept_a)} "
         f"({len(dropped)} dropped: {dict(by_gate)}). On the companies on today's watch list: {w(kept_b)} kept before, {w(kept_a)} after. "
         f"{len(unnamed)} kept postings name no country in their location and were kept because the rule says to.", "",
         "## Counts", ""]
    L += md_table(["", "all boards in the folder", "watch list today"],
                  [["postings", len(rows), w(rows)], ["kept by the keywords alone", len(kept_b), w(kept_b)],
                   ["kept with the gates", len(kept_a), w(kept_a)], ["dropped by a gate", len(dropped), w(dropped)]])
    L += ["", "## Dropped by a gate", ""]
    L += md_table(["company", "title", "location", "why it was dropped", "on watch list"],
                  [[v["company"], v["title"], v["location_text"], why, "yes" if v["company"] in watched else "no"]
                   for v, _, _, why in sorted(dropped, key=lambda r: (r[0]["company"], r[0]["title"]))])
    L += ["", "## Kept although the location names no country", ""]
    L += md_table(["company", "title", "location"], [[v["company"], v["title"], v["location_text"]] for v, _, _, _ in unnamed])
    return "\n".join(L) + "\n"


def report_jsonl(path, kw):
    rule = kw["location_rule"]
    iso = {c["iso2"]: name for name, c in rule["countries"].items() if c.get("iso2")}
    allowed = set(rule["allowed_countries"])
    rows = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    conf, wrong, unnamed, k12 = collections.Counter(), collections.defaultdict(collections.Counter), collections.Counter(), []
    for r in rows:
        text = " · ".join(r.get("locations") or [])
        d = collect.where(text, rule)
        truth = None
        if r.get("country_codes"):
            truth = "allowed" if any(iso.get(c) in allowed or c == "PR" for c in r["country_codes"]) else "outside"
        conf[(truth or "no codes reported", d["decision"])] += 1
        if truth and d["decision"] in ("allowed", "outside") and d["decision"] != truth:
            wrong[(truth, d["decision"])][(text[:90], ",".join(r["country_codes"]), ", ".join(d["countries"]))] += 1
        if d["decision"] == "unnamed":
            unnamed[text] += 1
        h = collect.k12_hits(r["title"], "", kw["k12_rule"])
        if h["title"]:
            k12.append((r["company"], r["title"], text[:60], ", ".join(h["title"])))
    n = len(rows)
    ok = sum(v for (t, d), v in conf.items() if t != "no codes reported" and t == d)
    known = sum(v for (t, d), v in conf.items() if t != "no codes reported" and d != "unnamed")
    L = [f"# The place reader and the K-12 rule on {n:,} postings", "",
         f"**What this is.** The location rule of keywords.json v{kw['version']} applied to the `locations` of {n:,} postings (no ad text in this "
         f"snapshot, so only the gates can be tested), checked against the country codes the boards themselves report where they report one. "
         f"**What was found.** Where a board reports a code and the reader names a country, they agree on {ok:,} of {known:,}. The disagreements are "
         f"listed below: the boards report only one code for a posting in several places, and Puerto Rico has its own code but is treated as the United States. "
         f"{len(k12)} titles say K-12.", "", "## Decision by what the board reported", ""]
    L += md_table(["board's own code", "reader says", "postings"], [[t, d, v] for (t, d), v in sorted(conf.items())])
    for (t, d), c in wrong.items():
        L += ["", f"## Board says {t}, reader says {d} ({sum(c.values())})", ""]
        L += md_table(["location", "board code", "reader's countries", "postings"], [[a, b, cc, v] for (a, b, cc), v in c.most_common(25)])
    L += ["", "## Locations that name no country (most common)", ""]
    L += md_table(["location", "postings"], list(unnamed.most_common(40)))
    L += ["", "## K-12 titles", ""]
    L += md_table(["company", "title", "location", "phrase"], sorted(k12))
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raw", help="a runs/<date>/raw folder of saved board responses")
    ap.add_argument("--jobs-jsonl", help="a jobs.jsonl with locations and country_codes (the ai-jobs snapshot)")
    ap.add_argument("--keywords", default=lp.config("keywords.json"))
    ap.add_argument("--out", help="write the Markdown here instead of printing it")
    a = ap.parse_args(argv)
    if bool(a.raw) == bool(a.jobs_jsonl):
        ap.error("give exactly one of --raw or --jobs-jsonl")
    kw = json.load(open(a.keywords, encoding="utf-8"))
    for k in ("location_rule", "k12_rule"):
        if k not in kw:
            ap.error(f"{a.keywords} has no {k}: there is nothing to audit")
    text = report_raw(a.raw, kw) if a.raw else report_jsonl(a.jobs_jsonl, kw)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text)
        print("wrote", a.out)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
