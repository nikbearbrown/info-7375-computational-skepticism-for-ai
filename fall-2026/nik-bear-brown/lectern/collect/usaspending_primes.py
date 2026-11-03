#!/usr/bin/env python3
"""usaspending_primes.py — who wins federal Section 508 / digital-accessibility contracts, and who do they subcontract it to? Leads for a small firm, not job postings.

    python3 usaspending_primes.py                       # the current federal fiscal year and the three before it, prime awards and subawards, top leads printed
    python3 usaspending_primes.py --since 2020-10-01    # a longer window
    python3 usaspending_primes.py --no-subawards        # prime awards only

Professor Bear, 2026-11-02, for a friend who is starting a small Section 508 testing firm (the brief: the subcontracting targets are the primes that win 508 work, 'like Booz Allen,
Leidos and Deloitte'; TARGETS.md lane 2). USAspending.gov is the government's own spending data and its API (api.usaspending.gov/api/v2) needs no key and no login; the host has no
robots.txt (it answers 404). One POST a page of 100, a pause between requests, the same host list and user agent as collect.py. No key is used or read.

What it does:
  * Searches prime contract awards (types A-D) and subawards for each of a dozen 508 / accessibility phrases (QUERIES). The API's keyword search is wide: it also matches other text
    of the award, so every row is checked LOCALLY and kept only when the award's own DESCRIPTION has a phrase of federal508_rule (the groups' phrases or opportunity_work_phrases) after
    the physical-access words (building, ramp, wheelchair ...) are ruled out. Rows the API matched elsewhere are counted, not kept.
  * 'strong' is a 508 or work phrase in the description ('SECTION 508 AUDIT, TESTING AND TRAINING SERVICES'); 'weak' is only the generic word 'accessibility'. Leads are ranked by strong awards
    first, then by the dollars on them.
  * Prime awards are grouped by recipient (UEI where given): awards, dollars, agencies, latest end date, and the biggest descriptions. Subawards are grouped by the PRIME that passes
    the work down and by the SUBAWARDEE that does it.

What it cannot tell: whether a recipient is a small business (the award rows do not say), whether the description is the whole scope, and whether a firm would subcontract to anyone. A lead is a company
to look at, not a promise. Award Amount is the amount on the award, not necessarily the 508 part of it.

Writes: <out>/usaspending-primes-<date>.json   the leads and the matching awards (local, not committed)
Exit 0 ran, 2 bad input, 3 nothing could be fetched.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, collections, datetime as dt, json, os, re, sys, time

import collect

URL = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
PAGE = 100                       # the most the API gives a page
PAUSE = 1.2
MAX_PAGES = 10                   # per query: 1,000 rows; a search that has more is reported as not complete
QUERIES = ("section 508", "508 compliance", "508 testing", "508 remediation", "508 audit", "trusted tester", "accessibility testing", "accessibility audit",
           "accessibility remediation", "digital accessibility", "wcag", "vpat")
AWARD_FIELDS = ["Award ID", "Recipient Name", "Recipient UEI", "Description", "Award Amount", "Awarding Agency", "Awarding Sub Agency", "Start Date", "End Date", "Contract Award Type", "NAICS", "PSC"]
SUB_FIELDS = ["Sub-Award ID", "Sub-Awardee Name", "Sub-Award Amount", "Sub-Award Date", "Sub-Award Description", "Prime Recipient Name", "Prime Award ID", "Awarding Agency", "Awarding Sub Agency"]
STRONG_GROUP = "section-508"
# award descriptions use the short forms the rule's not_digital_words do not list ('BLDG. 508 REMEDIATION AND DEMOLITION' is Building 508): a physical-site award is not 508 work
PHYSICAL_SITE = ("bldg", "demolition", "asbestos", "abatement", "hazmat")


def default_since(today=None):
    """The first day of the fourth federal fiscal year back from the current one: the current year (so far) and the three before it. A fiscal year starts on 1 October."""
    today = today or dt.date.today()
    fy = today.year + (1 if today.month >= 10 else 0)
    return dt.date(fy - 4, 10, 1).isoformat()


def search(level, query, since, until, pause=PAUSE, max_pages=MAX_PAGES, post=None):
    """All rows of one keyword search, page by page. -> (rows, complete). complete is False when the search had more pages than max_pages."""
    post = post or collect.post_json
    body = {"filters": {"keywords": [query], "award_type_codes": ["A", "B", "C", "D"], "time_period": [{"start_date": since, "end_date": until}]},
            "fields": SUB_FIELDS if level == "subawards" else AWARD_FIELDS, "limit": PAGE, "page": 1,
            "sort": "Sub-Award Amount" if level == "subawards" else "Award Amount", "order": "desc"}
    if level == "subawards":
        body["spending_level"] = "subawards"
    rows, page = [], 1
    while page <= max_pages:
        if page > 1 or getattr(search, "paused", False):
            time.sleep(pause)
        body["page"] = page
        r = post(URL, body)
        search.paused = True
        got = r.get("results")
        if not isinstance(got, list):
            raise ValueError("no results list in the reply: " + str(r.get("detail") or r)[:120])
        rows.extend(got)
        if not (r.get("page_metadata") or {}).get("hasNext"):
            return rows, True
        page += 1
    return rows, False


def code(v):
    """NAICS and PSC come back as {'code': '541512', 'description': ...}."""
    return (v.get("code") if isinstance(v, dict) else v) or ""


def money(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def classify(description, rule):
    """-> ('strong' | 'weak' | None, [phrases]). Strong: a phrase of the section-508 group or an opportunity_work_phrase in the description. Weak: only the generic word 'accessibility'.
    None: no phrase, or a physical-access word (building, ramp ...) says it is not about digital accessibility."""
    t = (description or "").lower()
    if any(collect.word_in(w.lower(), t) for w in list(rule.get("not_digital_words") or []) + list(PHYSICAL_SITE)):
        return None, []
    strong = [p for g, s in (rule.get("groups") or {}).items() if s.get("enabled") and g == STRONG_GROUP for p in s.get("phrases") or [] if collect.word_in(p.lower(), t)]
    strong += [p for p in rule.get("opportunity_work_phrases") or [] if collect.word_in(p.lower(), t) and p.lower() not in strong]
    if strong:
        return "strong", list(dict.fromkeys(p.lower() for p in strong))
    weak = [p for g, s in (rule.get("groups") or {}).items() if s.get("enabled") and g != STRONG_GROUP for p in s.get("phrases") or [] if collect.word_in(p.lower(), t)]
    return ("weak", list(dict.fromkeys(p.lower() for p in weak))) if weak else (None, [])


def keep(rows, level, rule, seen, kept, counts):
    """Check each row locally and keep the matches. `seen` de-duplicates (a row found by two queries counts once); `kept` collects the matches; `counts` tallies."""
    for r in rows:
        key = (r.get("Prime Award ID"), r.get("Sub-Award ID")) if level == "subawards" else r.get("generated_internal_id") or r.get("Award ID")
        if key in seen:
            continue
        seen.add(key)
        counts["rows"] += 1
        kind, phrases = classify(r.get("Sub-Award Description") if level == "subawards" else r.get("Description"), rule)
        if not kind:
            counts["matched_elsewhere"] += 1
            continue
        counts[kind] += 1
        kept.append({**r, "strength": kind, "phrases": phrases})


def lead_rank(g):
    return (-g["strong_awards"], -g["strong_dollars"], -g["awards"], g["name"])


def group_awards(kept):
    """Prime awards -> one lead per recipient."""
    by = {}
    for r in kept:
        k = r.get("Recipient UEI") or (r.get("Recipient Name") or "").upper()
        g = by.setdefault(k, {"name": r.get("Recipient Name"), "uei": r.get("Recipient UEI"), "awards": 0, "strong_awards": 0, "dollars": 0.0, "strong_dollars": 0.0,
                              "agencies": collections.Counter(), "latest_end": "", "examples": []})
        amt = money(r.get("Award Amount"))
        g["awards"] += 1
        g["dollars"] += amt
        if r["strength"] == "strong":
            g["strong_awards"] += 1
            g["strong_dollars"] += amt
        g["agencies"][r.get("Awarding Sub Agency") or r.get("Awarding Agency") or ""] += 1
        g["latest_end"] = max(g["latest_end"], r.get("End Date") or "")
        g["examples"].append((amt, r.get("Description") or "", r.get("Awarding Agency") or "", code(r.get("NAICS")), code(r.get("PSC")), r.get("Award ID")))
    out = []
    for g in by.values():
        g["agencies"] = [a for a, _ in g["agencies"].most_common(4) if a]
        g["examples"] = [{"description": d[:160], "amount": a, "agency": ag, "naics": n, "psc": p, "award_id": i} for a, d, ag, n, p, i in sorted(g["examples"], reverse=True)[:3]]
        out.append(g)
    return sorted(out, key=lead_rank)


def group_subs(kept, by):
    """Subawards -> leads by the prime that passes the work down (by='prime') or the subawardee that does it (by='sub')."""
    name = "Prime Recipient Name" if by == "prime" else "Sub-Awardee Name"
    other = "Sub-Awardee Name" if by == "prime" else "Prime Recipient Name"
    groups = {}
    for r in kept:
        g = groups.setdefault((r.get(name) or "").upper(), {"name": r.get(name), "awards": 0, "strong_awards": 0, "dollars": 0.0, "strong_dollars": 0.0, "agencies": collections.Counter(),
                                                             "partners": collections.Counter(), "examples": []})
        amt = money(r.get("Sub-Award Amount"))
        g["awards"] += 1
        g["dollars"] += amt
        if r["strength"] == "strong":
            g["strong_awards"] += 1
            g["strong_dollars"] += amt
        g["agencies"][r.get("Awarding Sub Agency") or r.get("Awarding Agency") or ""] += 1
        g["partners"][r.get(other) or ""] += 1
        g["examples"].append((amt, r.get("Sub-Award Description") or "", r.get(other) or "", r.get("Prime Award ID")))
    out = []
    for g in groups.values():
        g["agencies"] = [a for a, _ in g["agencies"].most_common(4) if a]
        g["partners"] = [a for a, _ in g["partners"].most_common(4) if a]
        g["examples"] = [{"description": d[:160], "amount": a, "partner": p, "prime_award_id": i} for a, d, p, i in sorted(g["examples"], reverse=True)[:3]]
        out.append(g)
    return sorted(out, key=lead_rank)


def run(rule, since, until, subawards=True, pause=PAUSE, max_pages=MAX_PAGES, post=None):
    """Every query at each level -> a result dict. One query failing is recorded and does not stop the others."""
    result, failed = {"levels": {}}, []
    levels = ("awards", "subawards") if subawards else ("awards",)
    for level in levels:
        seen, kept, counts, incomplete = set(), [], collections.Counter(), []
        for q in QUERIES:
            try:
                rows, complete = search(level, q, since, until, pause, max_pages, post)
            except Exception as e:
                failed.append({"level": level, "query": q, "reason": f"{type(e).__name__}: {e}"[:200]})
                continue
            counts["by_query_" + q] = len(rows)
            if not complete:
                incomplete.append(q)
            keep(rows, level, rule, seen, kept, counts)
        result["levels"][level] = {"counts": dict(counts), "incomplete_queries": incomplete, "kept": kept}
    result["failed"] = failed
    return result


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--since", default=None, help="first day of the window (default: 1 October three full fiscal years before the current one)")
    ap.add_argument("--no-subawards", action="store_true")
    ap.add_argument("--max-pages", type=int, default=MAX_PAGES)
    ap.add_argument("--out", default=None, help="default runs/<today>")
    a = ap.parse_args(argv)
    today = dt.date.today().isoformat()
    since = a.since or default_since()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", since):
        print(f"INPUT ERROR: --since must be YYYY-MM-DD, not {since!r}", file=sys.stderr)
        return 2
    with open(lp.config("keywords.json"), encoding="utf-8") as f:
        rule = json.load(f)["federal508_rule"]
    res = run(rule, since, today, not a.no_subawards, max_pages=a.max_pages)
    if not any(v["counts"].get("rows") for v in res["levels"].values()):
        print("nothing could be fetched: " + "; ".join(f"{x['level']}/{x['query']}: {x['reason']}" for x in res["failed"][:3]), file=sys.stderr)
        return 3
    aw = res["levels"]["awards"]["kept"]
    leads = {"primes": group_awards(aw)}
    if "subawards" in res["levels"]:
        sk = res["levels"]["subawards"]["kept"]
        leads["primes_that_subcontract"] = group_subs(sk, "prime")
        leads["subawardees"] = group_subs(sk, "sub")
    out = a.out or os.path.join(lp.RUNS, today)
    os.makedirs(out, exist_ok=True)
    dest = os.path.join(out, f"usaspending-primes-{today}.json")
    collect.write_json(dest, {"tool": "lectern usaspending_primes", "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "window": [since, today],
                              "note": "Companies that won or were subcontracted federal Section 508 / accessibility work, from USAspending.gov. Leads to look at, not promises. No people named.",
                              "counts": {k: v["counts"] for k, v in res["levels"].items()}, "incomplete_queries": {k: v["incomplete_queries"] for k, v in res["levels"].items()},
                              "failed": res["failed"], "leads": leads, "matching_awards": aw})
    for level, v in res["levels"].items():
        c = v["counts"]
        print(f"{level}: {c.get('rows', 0)} distinct rows, {c.get('strong', 0)} strong, {c.get('weak', 0)} weak, {c.get('matched_elsewhere', 0)} matched elsewhere in the award and dropped"
              + (f"; NOT complete for {v['incomplete_queries']}" if v["incomplete_queries"] else ""))
    if res["failed"]:
        print(f"{len(res['failed'])} searches failed: " + "; ".join(f"{x['level']}/{x['query']}" for x in res["failed"]), file=sys.stderr)
    for g in leads["primes"][:15]:
        print(f"  {g['name'][:40]:40} {g['strong_awards']:3} strong / {g['awards']:3} awards  ${g['dollars']:>14,.0f}  latest end {g['latest_end']}  {', '.join(g['agencies'][:2])[:50]}")
    print(f"-> {os.path.basename(dest)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
