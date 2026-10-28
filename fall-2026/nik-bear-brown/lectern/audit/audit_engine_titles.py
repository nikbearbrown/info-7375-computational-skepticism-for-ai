#!/usr/bin/env python3
"""audit_engine_titles.py — what do the engine_rule phrases of keywords.json match, and how noisy is each?

    python3 audit_engine_titles.py --jobs-jsonl jobs.jsonl [--out report.md]      # the ai-jobs snapshot (titles, places, no ad text)
    python3 audit_engine_titles.py --all-jobs runs/DATE/all-jobs-DATE.json        # Lectern's own boards

For every phrase of every group (the groups switched off too, so their cost is visible before anyone switches them on) it
counts the titles that contain it, splits them by level (early career, level not stated, senior or mid) and by the two gates
(country, K-12), and lists the titles so a person can read the noise. Then the full lists: what would be posted, what has no
level word, what the gates dropped. Read-only. Stdlib only. Judges nothing a person should judge: it lists.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, collections, copy, json

import collect
import engine_jobs as ej


def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    return out + ["| " + " | ".join(str(c).replace("|", "/") for c in r) + " |" for r in rows]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--jobs-jsonl")
    ap.add_argument("--all-jobs")
    ap.add_argument("--keywords", default=lp.config("keywords.json"))
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    if bool(a.jobs_jsonl) == bool(a.all_jobs):
        ap.error("give exactly one of --jobs-jsonl or --all-jobs")
    kw = json.load(open(a.keywords, encoding="utf-8"))
    rule = kw["engine_rule"]
    views = ej.load_postings(a.jobs_jsonl or a.all_jobs)
    everything = copy.deepcopy(kw)
    for spec in everything["engine_rule"]["groups"].values():
        spec["enabled"] = True                                    # judge each phrase as if its group were on
    per = {}
    for g, spec in rule["groups"].items():
        for p in spec["phrases"]:
            one = copy.deepcopy(kw)
            one["engine_rule"]["groups"] = {g: {"enabled": True, "phrases": [p]}}
            c = collections.Counter(); ex = []
            for v in views:
                r = ej.judge_engine(v, one)
                if r["decision"] == "no-match":
                    continue
                c[r["decision"]] += 1
                ex.append((v["company"], v["title"], r["decision"]))
            per[(g, p)] = (c, ex)
    final = [(v, ej.judge_engine(v, kw)) for v in views]
    dec = collections.Counter(r["decision"] for _, r in final)
    post = sorted((v["company"], v["title"], v["location_text"][:50], r["reason"], v["url"]) for v, r in final if r["decision"] == "post")
    unst = sorted((v["company"], v["title"], v["location_text"][:50]) for v, r in final if r["decision"] == "unstated")
    rej = sorted((v["company"], v["title"], v["location_text"][:50], r["reason"]) for v, r in final if r["decision"] == "rejected")
    off = {}
    for g, s in rule["groups"].items():                           # a group that is off: the distinct postings it would add
        if not s["enabled"]:
            only = copy.deepcopy(kw)
            only["engine_rule"]["groups"] = {g: {"enabled": True, "phrases": s["phrases"]}}
            off[g] = sum(1 for v in views if ej.judge_engine(v, only)["decision"] in ("post", "unstated"))
    L = [f"# What the engine_rule phrases match, in {len(views):,} postings", "",
         f"**What this is.** The title phrases of keywords.json v{kw['version']} (`engine_rule`) applied to the titles and places of {len(views):,} postings, "
         f"phrase by phrase, so each phrase's noise can be read before it is trusted. **What was found.** {dec['post']} postings would be posted "
         f"(a game, engine or real-time phrase in the title, an early-career word, and an allowed country); {dec['unstated']} more have such a phrase "
         f"and no level word and are held back; {dec['senior-or-mid']} name a level that is not early career; the country and K-12 gates dropped {dec['rejected']}. "
         + (f"Groups switched off in the rules would add, if switched on: " + ", ".join(f"{g} {n}" for g, n in off.items()) + " (early career or no level word, allowed country). " if off else "")
         + "The ad text is not in this file, so 'some engine experience wanted' cannot be tested; only the title can.", "",
         "## Phrase by phrase (all postings, every group)", ""]
    L += table(["group", "on", "phrase", "titles", "early career", "no level word", "senior or mid", "dropped by a gate", "examples (company: title)"],
               [[g, "yes" if rule["groups"][g]["enabled"] else "NO", p, sum(c.values()), c["post"], c["unstated"], c["senior-or-mid"], c["rejected"],
                 "; ".join(f"{co}: {t[:45]}" for co, t, _ in ex[:3])] for (g, p), (c, ex) in per.items()])
    L += ["", "## Would be posted", ""] + table(["company", "title", "location", "why", "link"], post)
    L += ["", "## Held back: a phrase, no level word in the title", ""] + table(["company", "title", "location"], unst)
    L += ["", "## Dropped by the country or K-12 gate", ""] + table(["company", "title", "location", "why"], rej)
    text = "\n".join(L) + "\n"
    if a.out:
        open(a.out, "w", encoding="utf-8").write(text)
        print("wrote", a.out)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
