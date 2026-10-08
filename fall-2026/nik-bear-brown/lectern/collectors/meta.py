#!/usr/bin/env python3
"""meta.py — collector for Meta careers (Playwright + GraphQL interception).

Approach (per design): do NOT parse the DOM. Load the metacareers.com job
search in a real browser, listen for the GraphQL network responses the page
makes for itself, and extract job data from that JSON.

- The GraphQL doc_id is NOT hardcoded: the page makes its own request with
  its current doc_id, and we capture the response. Hardcoding it breaks
  whenever Meta rotates it.
- Requests are throttled (2s between scroll/paginate actions) and responses
  are cached to disk so a re-run does not re-fetch.

ENVIRONMENT NOTE (2026-10-08): this collector needs a browser with direct
network access. It cannot run on the current Linux VM: the egress proxy
requires auth that Chromium's tunnel does not complete
(ERR_TUNNEL_CONNECTION_FAILED), so Playwright gets no network. Run it on a
machine with direct egress (e.g. Bear's Mac via Claude Code) or revisit when
the proxy situation changes. Meta's site also returns HTTP 400 to plain
fetches and has no usable sitemap, so there is no plain-HTTP fallback today.
"""
import json
import os
import time

CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                         "cache", "meta")


def _cache_path(page_no):
    os.makedirs(CACHE_DIR, exist_ok=True)
    return os.path.join(CACHE_DIR, f"graphql-page-{page_no}.json")


def collect(max_pages=200, use_cache=True):
    """Return (jobs, reported_total). Needs Playwright + network. Raises."""
    from playwright.sync_api import sync_playwright

    captured = []

    def on_response(resp):
        url = resp.url
        if "/graphql" in url and resp.request.method == "POST":
            try:
                ctype = resp.headers.get("content-type", "")
                if "json" in ctype:
                    captured.append(resp.json())
            except Exception:
                pass

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/126.0.0.0 Safari/537.36")
        page.on("response", on_response)
        page.goto("https://www.metacareers.com/jobs",
                  wait_until="networkidle", timeout=60000)

        for n in range(max_pages):
            path = _cache_path(n)
            if use_cache and os.path.exists(path):
                captured.append(json.load(open(path)))
                continue
            # scroll to trigger the next page of results
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)
            if captured:
                with open(path, "w") as f:
                    json.dump(captured[-1], f)
            # stop when scrolling yields nothing new
            if n > 2 and len(captured) >= 2 and captured[-1] == captured[-2]:
                break
        browser.close()

    jobs, seen = [], set()
    for payload in captured:
        for job in _extract_jobs(payload):
            if job["job_id"] not in seen:
                seen.add(job["job_id"])
                jobs.append(job)
    # Meta's GraphQL does not report a clean total; None = unknown.
    return jobs, None


def _extract_jobs(payload):
    """Pull job records out of a captured GraphQL payload.

    Keys off field names (job ID-like fields), never array positions, so a
    reshaped response yields nothing rather than wrong data.
    """
    out = []

    def walk(node):
        if isinstance(node, dict):
            # a job record has an id-ish field plus a title-ish field
            jid = node.get("id") or node.get("jobId") or node.get("job_id")
            title = node.get("title") or node.get("name")
            if jid and title and isinstance(jid, (str, int)):
                out.append({
                    "job_id": str(jid),
                    "title": str(title).strip(),
                    "locations": _loc_str(node.get("locations") or node.get("location")),
                    "url": node.get("url") or node.get("applyUrl") or "",
                    "posted_at": node.get("postedAt") or node.get("createdAt"),
                    "description": None,
                })
                return  # don't descend into a record already taken
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(payload)
    return out


def _loc_str(loc):
    if isinstance(loc, list):
        return "; ".join(str(x) for x in loc if x)
    return str(loc or "")


def fetch_description(job):
    # Detail pages are JS-rendered; descriptions come from the GraphQL
    # payload when present. Nothing separate to fetch today.
    return job.get("description")
