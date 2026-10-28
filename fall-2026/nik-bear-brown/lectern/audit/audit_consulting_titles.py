#!/usr/bin/env python3
"""audit_consulting_titles.py — what do the consulting_rule words match, and how noisy is each?

    python3 audit_consulting_titles.py --jobs runs/DATE/consulting-jobs-DATE.json [--out report.md]
    python3 audit_consulting_titles.py --jobs jobs.jsonl                 # the ai-jobs snapshot
    python3 audit_consulting_titles.py --jobs corpus.json                # a list of {firm, title, loc} rows (the research session's sample)

For every role word and every early sign it counts the titles that contain it and what the judge did with them, firm by firm
and word by word, then lists what would be posted, what is held back, and what the vetoes and gates removed, so a person can read
the noise. The clearance veto is shown by its effect: judged with and without it. Read-only. Stdlib only. Lists; judges nothing a
person should judge.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, collections, copy, json

import collect
import consulting_jobs as cj


def load(path):
    with open(path, encoding="utf-8") as f:
        if path.endswith(".jsonl"):
            return [cj.posting_view(json.loads(l)) for l in f if l.strip()]
        data = json.load(f)
    if isinstance(data, list):                                                    # the research session's sample: {firm, title, loc}
        return [{"id": f"{r['firm']}:{i}", "company": r["firm"], "title": r["title"], "url": "", "location_text": r.get("loc") or ""} for i, r in enumerate(data)]
    return [cj.posting_view(r) for r in data["records"]]


def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    return out + ["| " + " | ".join(str(c).replace("|", "/") for c in r) + " |" for r in rows]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--jobs", required=True)
    ap.add_argument("--keywords", default=lp.config("keywords.json"))
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    with open(a.keywords, encoding="utf-8") as f:
        kw = json.load(f)
    rule = kw["consulting_rule"]
    views = load(a.jobs)
    final = [(v, cj.judge_consulting(v, kw)) for v in views]
    dec = collections.Counter(r["decision"] for _, r in final)
    nocl = copy.deepcopy(kw)
    nocl["consulting_rule"]["clearance_words"] = []
    cleared = [(v, cj.judge_consulting(v, nocl)["decision"]) for v, r in final if r["decision"] == "rejected" and "clearance in the title" in r["reason"]]
    by_firm = collections.defaultdict(collections.Counter)
    for v, r in final:
        by_firm[v["company"]][r["decision"]] += 1
        if r["decision"] == "rejected":
            by_firm[v["company"]]["clearance" if "clearance" in r["reason"] else "country/K-12"] += 1
    posts = [(v, r) for v, r in final if r["decision"] == "post"]
    roles = {(v["company"], v["title"]) for v, _ in posts}
    L = [f"# What the consulting_rule words match, in {len(views):,} postings", "",
         f"**What this is.** The consulting judge of keywords.json v{kw['version']} (`consulting_rule`) applied to the titles and places of {len(views):,} postings, word by word, "
         f"so each word's noise can be read before it is trusted. **What was found.** {dec['post']} postings would be posted ({len(roles)} distinct roles at "
         f"{len({v['company'] for v, _ in posts})} firms: a role word and an explicit early sign in the title, no level word, an allowed country, no K-12, no clearance); "
         f"{dec['unstated']} more have a role word and no early sign and are held back; {dec['senior-or-mid']} name a level that is not early career; {dec['not-consulting']} are not consulting roles "
         f"('Software Engineer', 'Service Desk Analyst', a cyber analyst); {dec['rejected']} are removed by a veto or a gate. "
         f"The clearance veto removed {len(cleared)} titles: judged without it, {sum(1 for _, d in cleared if d == 'post')} would have been posted and {sum(1 for _, d in cleared if d == 'unstated')} held back. "
         "The ad text is not in this file, so only the title can be tested.", "",
         "## Firm by firm", ""]
    L += table(["firm", "postings", "post", "held back", "senior or mid", "not consulting", "removed by the country or K-12 gate", "removed by the clearance veto", "no role word"],
               [[f, sum(c[k] for k in ("post", "unstated", "senior-or-mid", "not-consulting", "rejected", "no-match")), c["post"], c["unstated"], c["senior-or-mid"], c["not-consulting"], c["country/K-12"], c["clearance"], c["no-match"]]
                for f, c in sorted(by_firm.items())])
    per = []
    for kind, words in (("role word", rule["role_words"]), ("early sign", rule["early_career"]["words"]), ("level word (vetoes)", rule["early_career"]["veto_words"]), ("not consulting", rule["not_consulting_words"]), ("clearance", rule["clearance_words"])):
        for w in words:
            hits = [(v, r) for v, r in final if collect.word_in(w.lower(), cj.ej.blanked(v["title"], rule))]
            if hits:
                c = collections.Counter(r["decision"] for _, r in hits)
                per.append([kind, w, len(hits), c["post"], c["unstated"], c["senior-or-mid"], c["not-consulting"], c["rejected"], "; ".join(f"{v['company']}: {v['title'][:40]}" for v, _ in hits[:2])])
    L += ["", "## Word by word (only words that occur)", ""]
    L += table(["kind", "word", "titles", "post", "held back", "senior or mid", "not consulting", "removed", "examples"], per)
    L += ["", "## Would be posted (one line per role; cities together)", ""]
    grouped = collections.OrderedDict()
    for v, r in sorted(posts, key=lambda x: (x[0]["company"], x[0]["title"])):
        grouped.setdefault((v["company"], v["title"]), []).append(v["location_text"].split(",")[0])
    L += table(["firm", "title", "cities", "postings"], [[f, t, ", ".join(dict.fromkeys(c)), len(c)] for (f, t), c in grouped.items()])
    L += ["", "## Held back: a role word and no early sign", ""] + table(["firm", "title", "location"], sorted((v["company"], v["title"], v["location_text"][:40]) for v, r in final if r["decision"] == "unstated"))
    L += ["", "## Not consulting roles", ""] + table(["firm", "title", "why"], sorted((v["company"], v["title"], r["reason"]) for v, r in final if r["decision"] == "not-consulting"))
    L += ["", "## Removed by the clearance veto or a gate", ""] + table(["firm", "title", "location", "why"], sorted((v["company"], v["title"], v["location_text"][:30], r["reason"]) for v, r in final if r["decision"] == "rejected"))
    text = "\n".join(L) + "\n"
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text)
        print("wrote", a.out)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
