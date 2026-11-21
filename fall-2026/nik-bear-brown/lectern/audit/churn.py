#!/usr/bin/env python3
"""churn.py — are these real jobs that turn over, or postings that sit there?

    python3 churn.py                                  # every runs/*/all-jobs-*.json, newest run is "today"
    python3 churn.py --extra path/to/all-jobs-2026-09-26.json   # add a snapshot kept elsewhere
    python3 churn.py --write                          # also write churn-<date>.{md,json} next to today's run

What it can see. Each run is a snapshot of every posting open on a board that day, with the date the board says
it was first published. From snapshots alone it measures:
  age       how long today's open postings have been up (today minus the board's own posted date)
  flow      between two snapshots: postings that appeared, postings that disappeared, and how many
            of the ones that appeared look like a re-post (same company, title, place and department as
            one that disappeared)
  lifetime  if a board's open count is steady, mean days a posting stays up is about
            (average open postings) / (postings closed per day). Little's law. It is printed only with
            the evidence that the board was roughly steady, and marked when it was not.
  age at disappearance   how old closed postings were when we last saw them (a floor on how long they stayed)

What it cannot see. A posting that disappears was filled, cancelled, merged into another, or re-posted under a
new ID. Nothing in a public board says which. So "closed" is never "hired", and the report says so. A board's
posted date can be reset when the company edits or re-posts, which makes postings look younger than they are.
Two or three snapshots give a window, not a trend; the measure improves as runs accumulate.

Stdlib only. Reads the full snapshots, which stay on the machine that made them.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, glob, json, os, re, statistics, sys
from datetime import date

HERE = lp.ROOT


def key_of(r):
    return f"{r['source']}:{r['source_id']}"


def fp(r):
    norm = lambda s: re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()
    return "|".join(norm(r.get(f)) for f in ("title", "location_text", "department"))


def load(path):
    d = json.load(open(path, encoding="utf-8"))
    m = re.search(r"(\d{4}-\d{2}-\d{2})", os.path.basename(path))
    day = m.group(1)
    # a board read through the site's own search (collect.py, read "search", 2026-11-20) is not the board: what comes back depends on the site's
    # ranking, so a posting that drops out of a search has not closed. Those boards are left out of every count here.
    ok = {s["company"] for s in d.get("sources", []) if s.get("status") == "ok" and s.get("read") != "search"}
    recs = {}
    for r in d["records"]:
        if r["company"] in ok:
            recs[key_of(r)] = r
    return {"date": day, "path": os.path.basename(path), "recs": recs, "ok": ok}


def refs_from_raw(raw_dirs, day):
    """Greenhouse's own job id (`internal_job_id`) for each post, read from the saved raw responses. A job can have
    several posts, and a job can be re-posted under a new post id; the all-jobs files from before 2026-10-18 do not
    carry it, the raw files do."""
    out = {}
    for d in raw_dirs:
        for f in glob.glob(os.path.join(d, f"greenhouse-*-{day}.json")):
            for j in (json.load(open(f, encoding="utf-8")).get("jobs") or []):
                if j.get("internal_job_id") is not None:
                    out[("greenhouse", str(j["id"]))] = str(j["internal_job_id"])
    return out


def attach_refs(snap, raw_dirs):
    m = refs_from_raw(raw_dirs, snap["date"])
    for r in snap["recs"].values():
        if not r.get("job_ref"):
            ref = m.get((r["source"], r["source_id"]))
            if ref:
                r["job_ref"] = ref


def days(a, b):
    return (date.fromisoformat(b) - date.fromisoformat(a)).days


def pct(n, d):
    return f"{100 * n / d:.0f}%" if d else "-"


def age_table(snap):
    by = {}
    for r in snap["recs"].values():
        if r.get("date_posted"):
            by.setdefault(r["company"], []).append(days(r["date_posted"], snap["date"]))
    rows = []
    for co, ages in sorted(by.items(), key=lambda x: -len(x[1])):
        n = len(ages)
        recs = [r for r in snap["recs"].values() if r["company"] == co]
        refd = [r for r in recs if r.get("job_ref")]
        rows.append({"company": co, "open": n, "median_days": int(statistics.median(ages)),
                     "distinct_jobs": len({r["job_ref"] for r in refd}) if len(refd) >= 0.9 * len(recs) else None,
                     "date_looks_reset": n >= 20 and not any(a > 30 for a in ages),
                     "over_30": sum(a > 30 for a in ages), "over_90": sum(a > 90 for a in ages),
                     "over_180": sum(a > 180 for a in ages), "over_365": sum(a > 365 for a in ages)})
    return rows


def flow(a, b):
    """Companies readable in BOTH snapshots only."""
    cos = sorted(a["ok"] & b["ok"])
    span = days(a["date"], b["date"])
    rows, totals = [], dict(start=0, end=0, new=0, closed=0, repost=0, dup=0)
    for co in cos:
        A = {k: r for k, r in a["recs"].items() if r["company"] == co}
        B = {k: r for k, r in b["recs"].items() if r["company"] == co}
        new = [r for k, r in B.items() if k not in A]
        closed = [r for k, r in A.items() if k not in B]
        pool = {}
        for r in closed:
            pool.setdefault(fp(r), []).append(r)
        repost = 0
        for r in new:
            f = fp(r)
            if pool.get(f):
                pool[f].pop()
                repost += 1
        seen = {}
        for r in B.values():
            seen[fp(r)] = seen.get(fp(r), 0) + 1
        dup = sum(c - 1 for c in seen.values() if c > 1)      # same title+place+department open under several IDs today
        ages = [days(r["date_posted"], a["date"]) for r in closed if r.get("date_posted")]
        stock = (len(A) + len(B)) / 2
        lam = len(closed) / span if span else 0
        steady = len(A) and abs(len(B) - len(A)) <= 0.10 * len(A)
        # the monitor's own rule: a board whose open count moved by more than 30% either way between two runs is
        # more likely a read problem (a board that came back empty, a partial fetch) than 100 closings
        # (boards under 20 postings are exempt from the ratio: four more postings on a board of six is not a fault)
        trusted = bool(A) and bool(B) and (len(A) < 20 or 0.7 <= len(B) / len(A) <= 1 / 0.7)
        have = lambda X: X and sum(1 for r in X.values() if r.get("job_ref")) >= 0.9 * len(X)
        jr = None
        if have(A) and have(B):
            ra, rb = {r["job_ref"] for r in A.values()}, {r["job_ref"] for r in B.values()}
            jr = {"jobs_start": len(ra), "jobs_end": len(rb), "jobs_closed": len(ra - rb), "jobs_opened": len(rb - ra),
                  "new_post_same_job": sum(1 for k, r in B.items() if k not in A and r.get("job_ref") in ra)}
        rows.append({"company": co, "start": len(A), "end": len(B), "new": len(new), "closed": len(closed), **(jr or {}),
                     "closed_pct_of_start": round(100 * len(closed) / len(A), 1) if A else None,
                     "repost_like": repost, "same_title_open_under_many_ids": dup,
                     "median_age_of_closed_at_last_seen_days": int(statistics.median(ages)) if ages else None,
                     "implied_mean_days_open": round(stock / lam) if lam else None, "roughly_steady": bool(steady),
                     "trusted": trusted})
        if not trusted:
            continue
        for k, v in (("start", len(A)), ("end", len(B)), ("new", len(new)), ("closed", len(closed)),
                     ("repost", repost), ("dup", dup)):
            totals[k] += v
        if jr:
            for k, v in jr.items():
                totals[k] = totals.get(k, 0) + v
            totals["ref_boards"] = totals.get("ref_boards", 0) + 1
    totals["boards"] = sum(r["trusted"] for r in rows)
    return {"from": a["date"], "to": b["date"], "days": span, "companies": cos, "rows": rows, "totals": totals}


def render(today, ages, flows):
    L = [f"# Churn {today['date']}: are these jobs turning over, or sitting there?\n", "## Executive summary\n"]
    tot_open = sum(r["open"] for r in ages)
    o90 = sum(r["over_90"] for r in ages)
    o180 = sum(r["over_180"] for r in ages)
    L.append(f"**What this is.** What the saved board snapshots say about postings that stay up versus postings that turn over, "
             f"for {len(today['ok'])} readable boards and {tot_open:,} open postings on {today['date']}. "
             "Snapshots only: it cannot see hires.\n")
    L.append(f"**Age.** {pct(o90, tot_open)} of today's open postings were first published more than 90 days ago, "
             f"{pct(o180, tot_open)} more than 180 days ago.\n")
    for f in flows:
        t = f["totals"]
        L.append(f"**Flow, {f['from']} to {f['to']} ({f['days']} days; {t['boards']} of {len(f['companies'])} boards trusted).** "
                 f"{t['start']:,} open at the start; **{t['closed']:,} disappeared** ({pct(t['closed'], t['start'])}) and "
                 f"**{t['new']:,} appeared**; {t['repost']:,} of the new ones look like a re-post of one that disappeared."
                 + (" Left out as untrusted reads: " + ", ".join(f"{r['company']} ({r['start']} to {r['end']})" for r in f["rows"] if not r["trusted"]) + "."
                    if any(not r["trusted"] for r in f["rows"]) else "") + "\n")
    for f in flows:
        t = f["totals"]
        if t.get("ref_boards"):
            L.append(f"**Same job under a new post id, {f['from']} to {f['to']} ({t['ref_boards']} Greenhouse boards that carry the job id).** "
                     f"{t['jobs_start']:,} distinct jobs behind {sum(r['start'] for r in f['rows'] if r.get('jobs_start') is not None and r['trusted']):,} posts at the start; "
                     f"**{t['jobs_closed']:,} jobs disappeared** and **{t['jobs_opened']:,} opened**; "
                     f"**{t['new_post_same_job']:,}** new post ids belong to a job that was already open (a re-post, a new location or a second post for the same job).\n")
    L.append("**What it cannot say.** A posting that disappears was filled, cancelled, merged or re-posted under a new ID. "
             "The board does not say which, so none of these numbers is a hiring rate. A board's posted date can reset "
             "when a company edits or re-posts, which makes postings look younger than they are.\n")
    L.append("---\n")
    L.append("## Age of the postings open today\n")
    L.append("| Company | Open posts | Distinct jobs | Median days up | > 30 days | > 90 days | > 180 days | > 365 days |\n|---|---:|---:|---:|---:|---:|---:|---:|")
    for r in ages:
        L.append(f"| {r['company']}{' (date looks reset)' if r['date_looks_reset'] else ''} | {r['open']} | {r['distinct_jobs'] if r['distinct_jobs'] is not None else '-'} | {r['median_days']} | {pct(r['over_30'], r['open'])} | "
                 f"{pct(r['over_90'], r['open'])} | {pct(r['over_180'], r['open'])} | {pct(r['over_365'], r['open'])} |")
    for f in flows:
        L.append(f"\n## Flow between snapshots, {f['from']} to {f['to']} ({f['days']} days)\n")
        L.append("| Company | Open at start | Open now | Disappeared | % of start | Appeared | Re-post-like (same title and place) | New post, same job id | Jobs that disappeared | Same title open under several IDs | Median age of the disappeared (days) | Implied mean days open | Read trusted? |\n"
                 "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|")
        for r in sorted(f["rows"], key=lambda x: -x["start"]):
            L.append(f"| {r['company']} | {r['start']} | {r['end']} | {r['closed']} | {r['closed_pct_of_start']}% | {r['new']} | "
                     f"{r['repost_like']} | {r.get('new_post_same_job', '-')} | {r.get('jobs_closed', '-')} | {r['same_title_open_under_many_ids']} | "
                     f"{r['median_age_of_closed_at_last_seen_days'] if r['median_age_of_closed_at_last_seen_days'] is not None else '-'} | "
                     f"{r['implied_mean_days_open'] if r['implied_mean_days_open'] else '-'}{'' if r['roughly_steady'] else ' (not steady)'} | "
                     f"{'yes' if r['trusted'] else 'NO: open count moved more than 30%'} |")
    L.append("\n## How to read the columns\n")
    L.append("- **Read trusted?** The monitor's own rule: a board whose open count moved by more than 30% either way between two runs is more likely a read problem (an empty or partial fetch) than that many closings, so it is shown but left out of the totals. A real freeze or layoff would be excluded too; the table is where to look.")
    L.append("- **(date looks reset)** Every posting on that board is under 30 days old, so its posted date is probably an updated-at date and its ages say little.")
    L.append("- **Implied mean days open** is (average open postings) divided by (postings that disappeared per day). It is a fair estimate only if the board is roughly steady (its open count moved by 10% or less); rows that are not steady are marked.")
    L.append("- **Median age of the disappeared** is how old they were when last seen: a floor on how long they stayed, because they may have gone any time before the next snapshot.")
    L.append("- **Re-post-like** counts new postings with the same company, title, place and department as one that disappeared. It will miss a re-post whose title changed and will catch a genuinely identical new opening. It is a lead, not a verdict.")
    L.append("- **New post, same job id / Jobs that disappeared** (Greenhouse boards only): Greenhouse gives every job its own id apart from the id of each post. A new post id whose job id was already open is the same job posted again or posted in another place; a job that disappeared lost all its posts. Postings for a job are counted once in the job columns, so these are fewer than the post counts.")
    L.append("- **Same title open under several IDs** is the same title, place and department open more than once today. Some are genuine multiple openings (many identical sales roles); some are duplicates.")
    L.append("\n## Snapshots used\n")
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", default=os.path.join(HERE, "runs"))
    ap.add_argument("--extra", action="append", default=[], help="another all-jobs-<date>.json snapshot")
    ap.add_argument("--extra-raw", action="append", default=[], help="a raw/ folder of saved responses for an --extra snapshot")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args(argv)
    paths = sorted(glob.glob(os.path.join(a.runs, "*", "all-jobs-*.json"))) + a.extra
    snaps = {}
    for p in paths:
        s = load(p)
        if s["date"] not in snaps or len(s["recs"]) > len(snaps[s["date"]]["recs"]):
            snaps[s["date"]] = s
    order = [snaps[d] for d in sorted(snaps)]
    raw_dirs = glob.glob(os.path.join(a.runs, "*", "raw")) + a.extra_raw
    for s in order:
        attach_refs(s, raw_dirs)
    if len(order) < 2:
        sys.exit("need at least two snapshots to measure flow")
    today = order[-1]
    ages = age_table(today)
    flows = [flow(order[i], order[i + 1]) for i in range(len(order) - 1)]
    if len(order) > 2:
        flows.append(flow(order[0], order[-1]))
    md = render(today, ages, flows) + "\n".join(f"- `{s['path']}` ({s['date']}, {len(s['recs']):,} postings on readable boards)" for s in order) + "\n"
    print(md)
    if a.write:
        out = os.path.join(a.runs, today["date"])
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, f"churn-{today['date']}.md"), "w", encoding="utf-8") as f:
            f.write(md)
        with open(os.path.join(out, f"churn-{today['date']}.json"), "w", encoding="utf-8") as f:
            json.dump({"date": today["date"], "snapshots": [s["path"] for s in order], "age": ages, "flow": flows,
                       "note": "Closed is not hired: a posting that disappears was filled, cancelled, merged or re-posted."},
                      f, indent=1)
            f.write("\n")
        print("wrote churn-%s.{md,json}" % today["date"], file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
