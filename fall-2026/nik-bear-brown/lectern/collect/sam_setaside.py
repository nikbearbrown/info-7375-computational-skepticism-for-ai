#!/usr/bin/env python3
"""sam_setaside.py — SAM.gov's public Contract Opportunities extract, narrowed to the notices a small, woman-owned Section 508 testing firm could bid or subcontract on: VA, the Department of Defense and the FAA, set aside for small business or women-owned small business.

    python3 sam_setaside.py                 # read the file already in runs/sam-cache/ (this makes NO request; sam_opportunities.py is the only reader that fetches it)
    python3 sam_setaside.py --agency VA     # only one of VA, DOD, FAA (repeatable)

Professor Bear, 2026-11-03, for a friend who is starting a small Section 508 testing firm. She said yes to 'filtering SAM.gov for small business and women-owned set-asides at the VA, the
Defense Department, and the FAA'. It reads the same extract as sam_opportunities.py (no key, no login; its terms and robots were read there) and adds three filters to what that reader already does:

  * the agency: 'VETERANS AFFAIRS, DEPARTMENT OF' (VA), 'DEPT OF DEFENSE' (DOD), and the sub-tier 'FEDERAL AVIATION ADMINISTRATION' under the Department of Transportation (FAA);
  * the set-aside: small business (SBA, SBP) or women-owned (WOSB, WOSBSS, EDWOSB, EDWOSBSS). Veteran-owned, 8(a), HUBZone and the rest are counted and left out: they are not what she asked for;
  * the notice is about the work: tier A = 508 or accessibility is the work asked for (the same test as sam_opportunities.py: a phrase in the title, or an opportunity_work_phrase in the description);
    tier B = information-technology or web work (a software, web, IT-services or IT-research NAICS or product code) whose description names Section 508, WCAG or accessibility, so the buyer will
    want it tested (a requirement clause, not a request for testing: the prime who wins it is the lead). Everything else is only counted.

No contact (name, email, phone) is read or kept. A notice is a public solicitation, but the output is a lead list for one firm, so it stays local and gitignored.
Writes: <out>/sam-setaside-<date>.json and .csv (local, not committed). Exit 0 ran, 2 bad input, 3 no cached extract.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, collections, csv, datetime as dt, json, os, sys

import collect
import sam_opportunities as so

SET_ASIDES = {"SBA": "small business", "SBP": "small business (partial)", "WOSB": "women-owned", "WOSBSS": "women-owned (sole source)",
              "EDWOSB": "women-owned, economically disadvantaged", "EDWOSBSS": "women-owned, economically disadvantaged (sole source)"}
SET_ASIDE_ALIAS = {'["SBA"]': "SBA"}      # the extract writes some codes as a JSON list
IT_NAICS = ("5415", "5182", "519290", "519130", "541715", "611420")      # computer systems design, data processing, web portals, IT research, computer training
LEAD_COLUMNS = ["agency", "sub_tier", "office", "title", "solicitation", "type", "tier", "set_aside", "naics", "psc", "posted", "response_deadline", "state", "url", "why"]


def agency_of(rec):
    """-> 'VA' | 'DOD' | 'FAA' | None."""
    a, s = rec["agency"].upper(), rec["sub_tier"].upper()
    if a.startswith("VETERANS AFFAIRS"):
        return "VA"
    if a == "DEPT OF DEFENSE":
        return "DOD"
    if "TRANSPORTATION" in a and s == "FEDERAL AVIATION ADMINISTRATION":
        return "FAA"
    return None


def set_aside_of(rec):
    """-> the readable set-aside if it is one of the asked-for kinds, else None."""
    code = SET_ASIDE_ALIAS.get(rec["set_aside_code"].strip(), rec["set_aside_code"].strip())
    return SET_ASIDES.get(code)


def is_it(rec):
    n, p = rec["naics"].strip(), rec["psc"].strip().upper()
    return n.startswith(IT_NAICS) or p.startswith("D") or p in ("7A21", "7A22", "7A20")


def classify(rec, find, rule, work):
    """-> ('A' | 'B' | None, why). Fills the hit fields as sam_opportunities.strength does."""
    s = so.strength(rec, find, rule, work)
    if s == "title":
        return "A", "508 or accessibility in the title: " + ", ".join(p for _, p in rec["title_hits"])
    if s == "description-work":
        return "A", "the description asks for: " + ", ".join(rec["work_phrases"])
    if s in ("description-mention", "description-accessibility") and is_it(rec):
        return "B", "IT/web work whose description names: " + ", ".join(p for _, p in rec["description_hits"])
    return None, ""


def analyse(path, rule, wanted):
    find, work = so.phrase_finder(rule), so.work_finder(rule)
    counts, aside_left_out, leads = collections.Counter(), collections.Counter(), []
    for rec in so.read_rows(path, counts):
        if rec["active"].lower() != "yes":
            continue
        ag = agency_of(rec)
        if not ag or ag not in wanted:
            continue
        counts["active_" + ag] += 1
        sa = set_aside_of(rec)
        if not sa:
            aside_left_out[rec["set_aside"] or "(none stated)"] += 1
            continue
        counts["asked_for_set_aside_" + ag] += 1
        tier, why = classify(rec, find, rule, work)
        if not tier:
            continue
        leads.append({**rec, "agency_short": ag, "tier": tier, "set_aside": sa, "why": why, "description": rec["description"][:600]})
    leads.sort(key=lambda r: (r["tier"], r["agency_short"], r["response_deadline"] or "9999"))
    return counts, aside_left_out, leads


def write_csv(path, leads):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(LEAD_COLUMNS)
        for r in leads:
            w.writerow([r["agency_short"] if c == "agency" else r.get(c, "") for c in LEAD_COLUMNS])


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--agency", action="append", choices=["VA", "DOD", "FAA"], help="only these (repeatable); default all three")
    ap.add_argument("--cache", default=so.CACHE)
    ap.add_argument("--out", default=None, help="default runs/<today>")
    a = ap.parse_args(argv)
    wanted = set(a.agency or ["VA", "DOD", "FAA"])
    path = os.path.join(a.cache, so.FILE)
    if not os.path.exists(path):
        print("no cached extract: run sam_opportunities.py once to fetch it", file=sys.stderr)
        return 3
    try:
        with open(lp.config("keywords.json"), encoding="utf-8") as f:
            rule = json.load(f)["federal508_rule"]
        counts, left_out, leads = analyse(path, rule, wanted)
    except collect.InputError as e:
        print(f"INPUT ERROR: {e}", file=sys.stderr)
        return 2
    today = dt.date.today().isoformat()
    out = a.out or os.path.join(lp.RUNS, today)
    os.makedirs(out, exist_ok=True)
    stem = os.path.join(out, f"sam-setaside-{today}")
    summary = {"rows_read": counts["rows"], "by_agency_active": {k[7:]: v for k, v in counts.items() if k.startswith("active_")},
               "by_agency_asked_for_set_aside": {k[len("asked_for_set_aside_"):]: v for k, v in counts.items() if k.startswith("asked_for_set_aside_")},
               "left_out_by_set_aside": dict(left_out.most_common(8)), "tier_a": sum(r["tier"] == "A" for r in leads), "tier_b": sum(r["tier"] == "B" for r in leads)}
    collect.write_json(stem + ".json", {"tool": "lectern sam_setaside", "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                                        "note": "Active SAM.gov notices at VA, DoD and the FAA set aside for small business or women-owned small business, about 508/accessibility work (A) or IT/web work that names it (B). Research for one firm, not a feed. No contacts kept.",
                                        "summary": summary, "leads": leads})
    write_csv(stem + ".csv", leads)
    print(f"{summary['rows_read']:,} rows read; active notices at the three agencies: {summary['by_agency_active']}")
    print(f"with a small-business or women-owned set-aside: {summary['by_agency_asked_for_set_aside']}")
    print(f"left out for another or no set-aside (top): {summary['left_out_by_set_aside']}")
    print(f"tier A (508/accessibility is the work): {summary['tier_a']}; tier B (IT/web work that names it): {summary['tier_b']}")
    for r in leads[:15]:
        print(f"  {r['tier']} {r['agency_short']:3} {r['set_aside'][:22]:22} {r['response_deadline'][:10]:10} {r['title'][:70]}")
    print(f"-> {os.path.basename(stem)}.csv / .json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
