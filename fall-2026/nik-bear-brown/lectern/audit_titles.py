#!/usr/bin/env python3
"""audit_titles.py — audit Lectern's filter by JOB FUNCTION instead of by posting.

    python3 audit_titles.py --all-jobs <all-jobs-DATE.json> --out <file.md> [--families title_families.json]

Professor Bear's design, 2026-09-26: there are far fewer job FUNCTIONS than job postings, so
classifying titles into families turns "read 3,446 postings" into "judge ~18 families, then read
only the disagreements." Each family in title_families.json declares what it EXPECTS — keep,
reject, or judge — and this script reports every posting where the filter and the expectation
disagree. Those disagreements are the entire audit.

It judges nothing. A disagreement is a question: either the filter is wrong, or the family
rule is wrong. Both happen, and the second is easy to mistake for the first.

Stdlib only.
"""
import argparse, json, os, re
from collections import defaultdict


def classify(title, families):
    t = title.lower()
    for f in families:
        if re.search(f["pattern"], t):
            return f["name"]
    return "UNCLASSIFIED"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--all-jobs", required=True)
    ap.add_argument("--families", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "title_families.json"))
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)

    d = json.load(open(a.all_jobs, encoding="utf-8"))
    spec = json.load(open(a.families, encoding="utf-8"))
    fams = spec["families"]
    expect = {f["name"]: f.get("expect", "judge") for f in fams}
    note = {f["name"]: f.get("note", "") for f in fams}
    expect["UNCLASSIFIED"] = "judge"
    note["UNCLASSIFIED"] = "No family matched the title. Either a function nobody listed, or a title too vague to classify."

    tally = defaultdict(lambda: [0, 0])          # family -> [kept, rejected]
    titles = defaultdict(set)
    bucket = defaultdict(list)
    for r in d["records"]:
        f = classify(r["title"], fams)
        tally[f][0 if r["kept"] else 1] += 1
        titles[f].add(r["title"].strip())
        bucket[f].append(r)

    order = [f["name"] for f in fams] + ["UNCLASSIFIED"]
    total = len(d["records"])
    kept_total = sum(v[0] for v in tally.values())

    # the audit: where the filter and the family expectation disagree
    fp = [(f, r) for f in order for r in bucket[f] if r["kept"] and expect[f] == "reject"]
    fn = [(f, r) for f in order for r in bucket[f] if not r["kept"] and expect[f] == "keep"]
    jd = [(f, r) for f in order for r in bucket[f] if expect[f] == "judge"]

    L = [f"# Title audit — Lectern run of {d['generated_at'][:10]}", "", "## Executive summary", "",
         f"**What this is.** Every one of the **{total:,} postings** sorted by what kind of job its title names, "
         f"then compared against what that kind of job *should* do in the filter. The point is scale: there are "
         f"{len(titles) } job functions here and {len(set().union(*titles.values())):,} distinct titles, so instead of "
         f"reading {total:,} postings you judge **{len(fams)} family rules** and then read only the disagreements.", "",
         f"**What it found.** {len(fp)} postings were **kept from families that should never produce a keep** — "
         f"the false positives. {len(fn)} were **rejected from families that should always produce a keep** — the "
         f"candidate false negatives. {len(jd)} sit in families marked *judge*, where the word genuinely means two "
         f"different jobs and only a person can split them.", "",
         "**The most useful thing it found is a bug in itself.** The first version of this audit treated *training* "
         "as a teaching word and duly reported 27 rejected \"education\" jobs — which looked like a serious "
         "false-negative problem. They were **Pre-training, Post-Training, Training Runtime, and Researcher, "
         "Training**: machine-learning jobs. At an AI company *training* means training a model. The filter had "
         "been right about all of them and the audit was wrong. That is why `ML_TRAINING` is the first family "
         "rule and why every false-friend family carries a note explaining what the word actually means here.", "",
         "**How to use it.** Read the two disagreement lists and the *judge* families. For each row: is the filter "
         "wrong, or is the family rule wrong? Both are common. Fix whichever it is — `keywords.json` for the "
         "filter, `title_families.json` for the rule — and note it in the class log.", "",
         "---", "", "## The families", "",
         "`expect` is what the family rule claims should happen. Rows where the tally disagrees with `expect` are "
         "the audit.", "",
         "| Family | expect | kept | rejected | postings | distinct titles | what the word actually means here |",
         "|---|---|---:|---:|---:|---:|---|"]
    for f in order:
        k, rj = tally[f]
        if not (k or rj):
            continue
        flag = ""
        if expect[f] == "reject" and k:  flag = f" **← {k} kept**"
        if expect[f] == "keep" and rj:   flag = f" **← {rj} rejected**"
        L.append(f"| **{f}** | {expect[f]} | {k}{flag} | {rj} | {k+rj} | {len(titles[f])} | {note[f][:200]} |")
    L.append(f"| TOTAL | | {kept_total} | {total-kept_total} | {total:,} | {len(set().union(*titles.values())):,} | |")

    def table(rows, head):
        out = ["", head, "", "| Family | Company | Title | Location | Why the filter decided that | Verdict | Note |",
               "|---|---|---|---|---|---|---|"]
        for f, r in sorted(rows, key=lambda x: (x[0], x[1]["company"], x[1]["title"])):
            why = (", ".join((r.get("matched") or {}).get("role_title") or []) or (r.get("reject_reason") or ""))
            out.append(f"| {f} | {r['company']} | [{r['title'].replace('|','/')[:70]}]({r['url']}) | "
                       f"{(r['location_text'] or '').replace('|','/')[:32]} | {why[:52]} |  |  |")
        return out

    L += table(fp, f"## Kept, but the family says reject — {len(fp)} false positives")
    L += table(fn, f"## Rejected, but the family says keep — {len(fn)} candidate false negatives")
    L += table(jd, f"## The *judge* families — {len(jd)} postings where the word means two different jobs")
    L += ["", "---", "", "## Why this beats sampling postings", "",
          f"A random sample of {total:,} postings is mostly accountants and backend engineers: true negatives, "
          "correctly rejected, and reading them teaches nothing. Sorting by function puts every decision the filter "
          "could plausibly have got wrong into two short lists, and it makes the *systematic* errors visible — one "
          "word behaving badly across a whole family, rather than a scatter of individual mistakes. Both errors found "
          "so far were systematic: `enablement` meaning sales support, and `training` meaning model training.", "",
          "It does not replace reading a random sample. It finds errors in the families someone thought to name; a "
          "teaching job whose title uses none of these words lands in UNCLASSIFIED or in a wrong family, and only a "
          "random read will catch that. Do both, and expect this one to be cheaper.", ""]
    with open(a.out, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"wrote {a.out}")
    print(f"  {len(fams)} families · {len(fp)} false positives · {len(fn)} candidate false negatives · {len(jd)} to judge")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
