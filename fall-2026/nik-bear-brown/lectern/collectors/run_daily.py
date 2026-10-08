#!/usr/bin/env python3
"""run_daily.py — daily run: collect the big four, feed the shared monitor.

Usage:
    python3 -m collectors.run_daily [--db monitor.db] [--only google]

Each collector returns (jobs, reported_total). Descriptions are fetched
only for job IDs not already in the database. Ends with one health line
per source:

    google  fetched=3345  reported=3345  new=12  closed=9  trusted=yes
"""
import argparse
import os
import sys
import traceback

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collectors import amazon, google, microsoft, monitor

COLLECTORS = {
    "google": google,
    "amazon": amazon,
    "microsoft": microsoft,
}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "monitor.db"))
    ap.add_argument("--only", choices=list(COLLECTORS),
                    help="run one collector")
    a = ap.parse_args(argv)

    db = monitor.open_db(a.db)
    targets = [a.only] if a.only else list(COLLECTORS)
    for name in targets:
        mod = COLLECTORS[name]
        try:
            jobs, reported = mod.collect()
        except Exception as e:
            print(f"{name:10} COLLECT FAILED: {type(e).__name__}: {e}")
            traceback.print_exc()
            continue
        # descriptions only for new IDs
        for j in jobs:
            known = db.execute(
                "SELECT 1 FROM jobs WHERE company=? AND job_id=?",
                (name, j["job_id"])).fetchone()
            if not known:
                try:
                    j["description"] = mod.fetch_description(j)
                except Exception as e:
                    print(f"  {name}: detail fetch failed for {j['job_id']}: {e}")
                    j["description"] = None
            else:
                j["description"] = None
        trusted, new_n, closed_n = monitor.record_run(db, name, jobs, reported)
        print(f"{name:10} fetched={len(jobs):,}  reported={reported}  "
              f"new={new_n}  closed={closed_n}  "
              f"trusted={'yes' if trusted else 'NO (incomplete)'}")
    db.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
