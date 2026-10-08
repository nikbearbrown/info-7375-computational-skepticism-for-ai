#!/usr/bin/env python3
"""google.py — collector for Google careers (server-rendered results pages).

Page (verified 2026-10-08, plain GET with browser UA, no auth):
    GET https://www.google.com/about/careers/applications/jobs/results/?page={n}

Job data is server-rendered inside an AF_initDataCallback script block
(key 'ds:1'). Structure:
    data = [records, None, total_count, page_size]
    record = [job_id, title, apply_url, [None, description_html],
              [None, qualifications_html], tenant_path, None, "Google",
              "en-US", locations, ...]
    locations = [[display, [display], city, None, region, country], ...]

- `page=` paginates (1-based), 20 per page, fixed.
- `q=` filters server-side, but the monitor fetches the full list.
- The arrays are POSITIONAL: check_google_job() asserts the fields are
  where we expect them and raises loudly if the layout shifts, instead
  of silently returning blank titles.

A blank/missing ds:1 block raises too — a collector that raises is easier
to deal with than one that returns zero jobs.
"""
import datetime
import html as ihtml
import json
import re

from .common import polite_get

BASE = "https://www.google.com/about/careers/applications/jobs/results/"
PAGE_SIZE = 20


def check_google_job(row):
    """Assert the positional fields are where we expect. Raise if moved."""
    assert isinstance(row, list) and len(row) >= 10, \
        f"record is not a list of >=10 fields: {type(row)}"
    assert isinstance(row[0], str) and row[0].isdigit(), \
        f"job id moved (field 0 = {str(row[0])[:40]!r})"
    assert isinstance(row[1], str) and len(row[1]) > 3, \
        f"title moved (field 1 = {str(row[1])[:40]!r})"
    # field 2 (url) may be None for some postings — a data variation, not a
    # structural change. Anything else there is a layout shift.
    assert row[2] is None or (isinstance(row[2], str) and "careers" in row[2]), \
        f"url moved (field 2 = {str(row[2])[:40]!r})"
    assert isinstance(row[3], list), \
        f"description moved (field 3 = {type(row[3]).__name__})"
    assert isinstance(row[9], list), \
        f"locations moved (field 9 = {type(row[9]).__name__})"


def _extract_ds1(html_text):
    i = html_text.find("key: 'ds:1'")
    if i < 0:
        raise RuntimeError("ds:1 data block not found in page")
    j = html_text.find("data:", i)
    k = html_text.find("[", j)
    depth, in_str, esc, start = 0, False, False, k
    for idx in range(k, len(html_text)):
        c = html_text[idx]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
                if depth == 0:
                    return json.loads(html_text[start:idx + 1])
    raise RuntimeError("unterminated ds:1 data array")


def _plain(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ",
                                      ihtml.unescape(s or ""))).strip()


def _norm(row):
    check_google_job(row)
    desc_html = ""
    if len(row[3]) > 1 and row[3][1]:
        desc_html += row[3][1]
    if len(row) > 4 and isinstance(row[4], list) and len(row[4]) > 1 and row[4][1]:
        desc_html += "\n" + row[4][1]
    locs = []
    for loc in row[9] or []:
        if isinstance(loc, list) and loc:
            locs.append(str(loc[0]))
    posted = None
    for idx in (12, 13, 14):
        if len(row) > idx and isinstance(row[idx], list) and row[idx]:
            try:
                ts = int(row[idx][0])
                if ts > 1_000_000_000:  # unix seconds sanity
                    posted = datetime.datetime.fromtimestamp(
                        ts, datetime.timezone.utc).strftime("%Y-%m-%d")
                    break
            except (ValueError, OSError, TypeError):
                continue
    return {
        "job_id": row[0],
        "title": row[1].strip(),
        "locations": "; ".join(locs),
        "url": row[2] or "",
        "posted_at": posted,
        "description": _plain(desc_html) or None,
    }


def _fetch_page(page):
    status, body = polite_get(BASE, params={"page": page}, timeout=45)
    if status != 200:
        raise RuntimeError(f"Google careers page {page} -> HTTP {status}")
    data = _extract_ds1(body)
    records = data[0] or []
    total = int(data[2]) if len(data) > 2 and data[2] else None
    return records, total, body


def collect():
    """Return (jobs, reported_total). Raises on transport or layout failure."""
    jobs, page, reported, seen = [], 1, None, set()
    while True:
        records, total, _ = _fetch_page(page)
        if reported is None:
            reported = total
        if not records:
            break
        for row in records:
            job = _norm(row)  # raises if the layout moved
            if job["job_id"] not in seen:
                seen.add(job["job_id"])
                jobs.append(job)
        if reported and len(seen) >= reported:
            break
        page += 1
        if page > 500:  # sanity cap: 10,000 jobs
            raise RuntimeError("page cap exceeded; site layout may have changed")
    return jobs, reported


def fetch_description(job):
    # The listing already embeds the description; nothing to fetch.
    return job.get("description")
