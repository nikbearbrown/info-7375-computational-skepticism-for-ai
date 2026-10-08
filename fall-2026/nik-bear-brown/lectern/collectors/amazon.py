#!/usr/bin/env python3
"""amazon.py — collector for Amazon jobs (search.json endpoint).

Endpoint (verified 2026-10-08, plain GET, no auth):
    GET https://www.amazon.jobs/en/search.json?base_query=&country=USA
        &result_limit=100&offset={n}

- `result_limit=100` is honored; `offset` paginates with no duplicates
  (verified at offsets 0, 1000, 5000, 9900).
- `hits` is the reported total (10,000 for the unfiltered US query).
- Job objects carry the full `description` inline, so no detail fetch.
- If paging ever stops short of `hits`, split by category/country and
  dedupe by job ID (not yet needed).
"""
from .common import get_json

BASE = "https://www.amazon.jobs/en/search.json"
PAGE = 100


def _norm(j):
    loc = j.get("location") or ""
    return {
        "job_id": str(j.get("id")),
        "title": (j.get("title") or "").strip(),
        "locations": loc,
        "url": "https://www.amazon.jobs" + (j.get("job_path") or ""),
        "posted_at": j.get("posted_date") or None,
        "description": (j.get("description") or "").strip() or None,
        "category": j.get("job_category") or "",
        "team": j.get("team") or "",
    }


def collect(country="USA", category=None):
    """Return (jobs, reported_total). Raises on transport failure."""
    jobs, offset, reported = [], 0, None
    seen = set()
    while True:
        params = {"base_query": "", "country": country,
                  "result_limit": PAGE, "offset": offset}
        if category:
            params["category"] = category
        data = get_json(BASE, params=params)
        if reported is None:
            reported = int(data.get("hits") or 0)
        batch = data.get("jobs") or []
        if not batch:
            break
        for j in batch:
            jid = str(j.get("id"))
            if jid not in seen:
                seen.add(jid)
                jobs.append(_norm(j))
        offset += len(batch)
        if offset >= reported:
            break
    return jobs, reported


def fetch_description(job):
    # The listing already carries the full description; nothing to fetch.
    return job.get("description")
