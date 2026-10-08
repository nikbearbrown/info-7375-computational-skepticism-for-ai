#!/usr/bin/env python3
"""monitor.py — shared SQLite monitor every collector feeds into.

Rules (from the design):
1. New IDs get first_seen. Seen-again IDs get last_seen updated.
2. A job is marked closed only after missing from TWO consecutive trusted runs.
3. A run is trusted only if it fetched >=90% of reported_total AND >=70% of
   the previous trusted run's count. Untrusted runs update last_seen but
   never close anything, and they log a warning.

Descriptions are fetched only for new IDs (callers pass description=None
for known IDs; the monitor keeps the stored desc_hash).
"""
import hashlib
import sqlite3
from datetime import datetime, timezone

SCHEMA = """
CREATE TABLE IF NOT EXISTS jobs (
  company TEXT, job_id TEXT, title TEXT, locations TEXT, url TEXT,
  posted_at TEXT, desc_hash TEXT,
  first_seen TEXT, last_seen TEXT,
  missed_runs INTEGER DEFAULT 0, status TEXT DEFAULT 'open',
  PRIMARY KEY (company, job_id)
);
CREATE TABLE IF NOT EXISTS runs (
  company TEXT, run_at TEXT, fetched INTEGER, reported_total INTEGER, trusted INTEGER
);
"""


def open_db(path):
    db = sqlite3.connect(path)
    db.executescript(SCHEMA)
    return db


def record_run(db, company, jobs, reported_total):
    """Upsert jobs, update run health. Returns (trusted, new_count, closed_count)."""
    now = datetime.now(timezone.utc).isoformat()
    prev = db.execute(
        "SELECT fetched FROM runs WHERE company=? AND trusted=1 "
        "ORDER BY run_at DESC LIMIT 1", (company,)).fetchone()

    complete = reported_total is None or len(jobs) >= 0.9 * reported_total
    stable = prev is None or len(jobs) >= 0.7 * prev[0]
    trusted = bool(complete and stable)
    db.execute("INSERT INTO runs VALUES (?,?,?,?,?)",
               (company, now, len(jobs), reported_total, int(trusted)))

    seen, new_count = set(), 0
    for j in jobs:
        seen.add(j["job_id"])
        desc = j.get("description")
        h = hashlib.sha256(desc.encode()).hexdigest() if desc else None
        cur = db.execute("SELECT 1 FROM jobs WHERE company=? AND job_id=?",
                         (company, j["job_id"])).fetchone()
        if cur is None:
            new_count += 1
        db.execute("""
            INSERT INTO jobs (company, job_id, title, locations, url, posted_at,
                              desc_hash, first_seen, last_seen)
            VALUES (?,?,?,?,?,?,?,?,?)
            ON CONFLICT(company, job_id) DO UPDATE SET
              title=excluded.title,
              last_seen=excluded.last_seen,
              desc_hash=COALESCE(excluded.desc_hash, jobs.desc_hash),
              missed_runs=0,
              status='open'
        """, (company, j["job_id"], j["title"], j["locations"], j["url"],
              j.get("posted_at"), h, now, now))

    closed_count = 0
    if trusted:
        rows = db.execute(
            "SELECT job_id, missed_runs FROM jobs WHERE company=? AND status='open'",
            (company,)).fetchall()
        for job_id, missed in rows:
            if job_id not in seen:
                missed = (missed or 0) + 1
                status = "closed" if missed >= 2 else "open"
                if status == "closed":
                    closed_count += 1
                db.execute(
                    "UPDATE jobs SET missed_runs=?, status=? WHERE company=? AND job_id=?",
                    (missed, status, company, job_id))
    else:
        print(f"  WARNING: untrusted run for {company} "
              f"(fetched={len(jobs)}, reported={reported_total}) — nothing closed")
    db.commit()
    return trusted, new_count, closed_count
