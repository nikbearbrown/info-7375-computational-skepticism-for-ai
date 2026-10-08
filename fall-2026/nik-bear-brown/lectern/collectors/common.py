#!/usr/bin/env python3
"""common.py — shared polite HTTP for the big-four collectors.

One request per second with random jitter, a descriptive User-Agent, no
logins, no cookies. Host allowlist keeps every collector inside its own
career site. Stdlib only.
"""
import json
import random
import time
import urllib.parse
import urllib.request

USER_AGENT = "lectern (course project; daily job-board monitor)"

ALLOWED = {
    "apply.careers.microsoft.com",
    "www.amazon.jobs",
    "www.google.com",
}

_last_request_at = [0.0]


def polite_get(url, params=None, timeout=30, retries=3):
    """GET url with 1 req/sec + jitter. Returns (status, body_text).

    Retries on 429 (rate limit) with 30s backoff, up to `retries` times.
    """
    if params:
        url = url + ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
    host = urllib.parse.urlparse(url).hostname
    if host not in ALLOWED:
        raise ValueError(f"refusing host {host!r}: not in allowlist")

    for attempt in range(retries + 1):
        wait = 1.0 + random.uniform(0, 0.5) - (time.time() - _last_request_at[0])
        if wait > 0:
            time.sleep(wait)
        req = urllib.request.Request(url, headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json, text/html;q=0.9",
            "Accept-Language": "en-US,en;q=0.9",
        })
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = r.read().decode("utf-8", errors="replace")
                _last_request_at[0] = time.time()
                return r.status, body
        except urllib.error.HTTPError as e:
            _last_request_at[0] = time.time()
            if e.code == 429 and attempt < retries:
                time.sleep(30 * (attempt + 1))
                continue
            return e.code, e.read().decode("utf-8", errors="replace")
    raise RuntimeError(f"GET {url} -> persistent HTTP 429 after {retries} retries")


def get_json(url, params=None, timeout=30):
    status, body = polite_get(url, params=params, timeout=timeout)
    if status != 200:
        raise RuntimeError(f"GET {url} -> HTTP {status}")
    return json.loads(body)
