#!/usr/bin/env python3
"""microsoft.py — collector for Microsoft careers (Eightfold PCSX API).

Endpoint (verified 2026-10-08, plain GET, no auth, no cookies):
    GET https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&start={n}

- `start` paginates, page size is fixed at 10 (no page-size parameter works).
- `data.count` is the reported total; start past the end returns [] gracefully.
- `query=` filters server-side (e.g. query=education -> 189 results).
- Position fields: id (int, native), displayJobId, name, locations[],
  positionUrl (relative), postedTs (unix seconds), department.

Found via robots.txt (`Allow: /api/pcsx`) after the old gcsservices API went
dark and the careers site moved to apply.careers.microsoft.com (Eightfold).
"""
import datetime

from .common import get_json

BASE = "https://apply.careers.microsoft.com/api/pcsx/search"
DOMAIN = "microsoft.com"
PAGE = 10


def _norm(p):
    locs = p.get("locations") or []
    ts = p.get("postedTs")
    posted = None
    if ts:
        try:
            posted = datetime.datetime.fromtimestamp(
                int(ts), datetime.timezone.utc).strftime("%Y-%m-%d")
        except (ValueError, OSError):
            posted = None
    url = p.get("positionUrl") or ""
    if url.startswith("/"):
        url = "https://apply.careers.microsoft.com" + url
    return {
        "job_id": str(p["id"]),
        "title": (p.get("name") or "").strip(),
        "locations": "; ".join(locs),
        "url": url,
        "posted_at": posted,
        "description": None,  # fetched separately for new IDs only
        "department": p.get("department") or "",
        "display_id": str(p.get("displayJobId") or ""),
    }


def collect(query=None):
    """Return (jobs, reported_total). Raises on transport failure."""
    import time
    jobs, start, reported = [], 0, None
    while True:
        params = {"domain": DOMAIN, "start": start}
        if query:
            params["query"] = query
        data = get_json(BASE, params=params)["data"]
        if reported is None:
            reported = int(data.get("count") or 0)
        batch = data.get("positions") or []
        if not batch:
            break
        jobs.extend(_norm(p) for p in batch)
        start += len(batch)
        if start >= reported:
            break
        time.sleep(1.5)  # extra courtesy: PCSX throttles sustained 1/sec
    return jobs, reported


def fetch_description(job):
    """Fetch the full description for one job (new IDs only)."""
    from .common import polite_get
    import re
    import html as ihtml
    status, body = polite_get(job["url"], timeout=30)
    if status != 200:
        raise RuntimeError(f"detail GET -> HTTP {status}")
    # Eightfold detail pages carry JSON-LD JobPosting; fall back to text strip.
    m = re.search(
        r'<script type="application/ld\+json">(.*?)</script>', body, re.S)
    if m:
        import json as _json
        try:
            ld = _json.loads(m.group(1))
            if isinstance(ld, dict) and ld.get("description"):
                return re.sub(r"\s+", " ",
                              re.sub(r"<[^>]+>", " ", ld["description"])).strip()
        except Exception:
            pass
    text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ",
                                      ihtml.unescape(body))).strip()
    return text[:20000]
