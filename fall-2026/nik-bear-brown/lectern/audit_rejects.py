#!/usr/bin/env python3
"""audit_rejects.py — draw a reviewable sample of the postings Lectern rejected.

    python3 audit_rejects.py --all-jobs <all-jobs-DATE.json> --raw <raw dir> --out <file.md> [--n 100] [--seed 20260926]

The filter's false NEGATIVES cannot be counted by a script: only a person reading a
posting can say "that one should have been kept." This draws the sample for that reading
and records the seed, so the same sample can be drawn again and the judgment re-checked.

Two parts, on purpose:
  Part 1  a UNIFORM random sample of every reject — the only sample that supports a rate
  Part 2  every near-miss (rejects that matched 1-2 topic words) — where misses actually live

Stdlib only. Writes Markdown with a blank Verdict column. Judges nothing itself.
"""
import argparse, json, os, random, re, sys


def load_texts(raw_dir):
    """source_id -> first N chars of the posting body, from the saved responses."""
    import html
    def plain(s):
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(html.unescape(s or "")))).strip()
    texts = {}
    for fn in sorted(os.listdir(raw_dir)):
        if not fn.endswith(".json"):
            continue
        try:
            payload = json.load(open(os.path.join(raw_dir, fn), encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for j in payload.get("jobs") or []:
            jid = str(j.get("id"))
            body = (j.get("content") or j.get("descriptionHtml") or j.get("descriptionPlain")
                    or " ".join((v or {}).get("text") or ""
                                for v in (((j.get("jobAd") or {}).get("sections")) or {}).values()))
            texts[jid] = plain(body)
    return texts


def topic_hits(text, topics):
    t = text.lower()
    return [w for w in topics
            if re.search(r"(?<![a-z0-9])" + re.escape(w.lower()) + r"(?![a-z0-9])", t)]


def row(r, texts, topics, snippet=220):
    body = texts.get(str(r["source_id"]), "")
    hits = topic_hits(body, topics)
    # the sentence around the first topic word is the most useful 200 characters
    frag = ""
    if hits:
        m = re.search(r"(?<![a-z0-9])" + re.escape(hits[0]) + r"(?![a-z0-9])", body, re.I)
        if m:
            s = max(0, m.start() - snippet // 2)
            frag = ("…" if s else "") + body[s:s + snippet].replace("|", "/") + "…"
    return (f"| {r['company']} | [{r['title'].replace('|', '/')}]({r['url']}) | "
            f"{(r['location_text'] or '').replace('|', '/')[:38]} | {', '.join(hits[:5]) or '—'} | "
            f"{frag or '—'} |  |  |")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--all-jobs", required=True)
    ap.add_argument("--raw", required=True)
    ap.add_argument("--keywords", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "keywords.json"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--n", type=int, default=100, help="size of the uniform random sample")
    ap.add_argument("--seed", type=int, default=20260926, help="recorded in the file so the sample is reproducible")
    a = ap.parse_args(argv)

    d = json.load(open(a.all_jobs, encoding="utf-8"))
    topics = json.load(open(a.keywords, encoding="utf-8"))["topic_text"]
    rejects = [r for r in d["records"] if not r["kept"]]
    # Part 2 is the CLOSEST calls only — rejects that matched the most topic words without clearing
    # the bar. The wider "matched 1 topic word" tier is over 900 postings, too many to read and too
    # thin to be worth it; its size is reported instead.
    closest = [r for r in rejects if "only 2 topic words" in (r.get("reject_reason") or "")]
    one_word = [r for r in rejects if "only 1 topic words" in (r.get("reject_reason") or "")]
    near = closest
    texts = load_texts(a.raw)

    random.seed(a.seed)
    sample = random.sample(rejects, min(a.n, len(rejects)))
    date = d["generated_at"][:10]
    hdr = ("| Company | Title | Location | Teaching words in the body | Around the first one | Verdict | Note |\n"
           "|---|---|---|---|---|---|---|")

    L = [f"# Reject audit — Lectern run of {date}", "", "## Executive summary", "",
         f"**What this is.** A reviewable sample of the **{len(rejects):,} postings Lectern rejected** on {date}, "
         f"so a person can answer the one question no script can: *did the filter miss anything?*", "",
         "**Why read it.** Every accuracy number so far describes what the filter *kept*. Nothing has measured "
         "what it threw away. Until someone reads rejects, the collector has no false-negative rate in either "
         "direction — and a filter that quietly drops the right jobs looks identical to one that works.", "",
         "**How to use it.** Scan the titles. In the Verdict column write **MISS** if the posting should have been "
         "kept, **ok** if rejecting it was right, and **?** if you cannot tell without opening the link. Leave a "
         "note on anything surprising. Fill in Part 1 first: it is the only part that supports a rate.", "",
         f"**Two parts.** Part 1 is a **uniform random sample of {len(sample)}** drawn from all {len(rejects):,} "
         f"rejects with seed `{a.seed}` — rerunning the script reproduces exactly this list. Part 2 is **every one "
         f"of the {len(near)} closest calls**, the rejects that mentioned two teaching words without clearing "
         f"the bar of three. Part 1 gives the rate; Part 2 is where a miss is most likely to be hiding. "
         f"A further {len(one_word):,} rejects matched exactly one teaching word — too many to read and too "
         f"thin to be worth it, so their count is reported rather than their contents.", "",
         "**Read the reason it was rejected as a warning, not a verdict.** A posting rejected for `no-keyword-match` "
         "can still be a job about teaching — the filter matches strings, and a Technical Curriculum Lead whose ad "
         "never uses any of the words is invisible to it.", "",
         "---", "",
         "## Part 1 — uniform random sample (the rate)", "",
         f"{len(sample)} of {len(rejects):,} rejects, seed `{a.seed}`. If *k* of these are MISSes, the estimated "
         f"false-negative count across all rejects is about **k × {len(rejects)/len(sample):.0f}**. That is the "
         "number worth knowing.", "", hdr]
    L += [row(r, texts, topics) for r in sorted(sample, key=lambda r: (r["company"], r["title"]))]
    L += ["", f"## Part 2 — the {len(near)} closest calls", "",
          "Each of these mentioned **two** teaching words in its body and was rejected because the rule needs three, "
          "or a role word in the title. They are the closest thing in the run to a coin flip, so they are the "
          "cheapest place to find a real miss — but they are **not** a random sample and support no rate. "
          f"(The {len(one_word):,} postings that matched exactly one word are not listed.)", "", hdr]
    L += [row(r, texts, topics) for r in sorted(near, key=lambda r: (r["company"], r["title"]))]
    L += ["", "---", "",
          "## After the reading", "",
          "1. Count the MISSes in Part 1 and multiply as above — that is the estimate, and it belongs in the run's "
          "quality report next to the kept count.",
          "2. For each MISS, name the word that *would* have caught it. If several share a word, that word goes in "
          "`keywords.json` — and, per the rule the filter already follows, gets measured afterwards for the noise "
          "it adds.",
          "3. A MISS that no word would have caught is the more interesting finding: it means the posting describes "
          "teaching without using teaching vocabulary, which is a limit of keyword matching rather than a gap in "
          "this list.",
          "4. Record the count, the changes, and the date in the class `FRICTIONAL.md`. An audit that happened and "
          "was not written down did not happen.", ""]
    with open(a.out, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"wrote {a.out} — {len(sample)} random + {len(near)} near-misses, from {len(rejects)} rejects, seed {a.seed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
