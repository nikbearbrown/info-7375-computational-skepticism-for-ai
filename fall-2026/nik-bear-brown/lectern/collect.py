#!/usr/bin/env python3
"""collect.py — Lectern: fetch every posting from the watch list, keep the ones about teaching.

    python3 collect.py                 # fetch all sources, filter, write outputs
    python3 collect.py --only ashby    # one provider
    python3 collect.py --from-raw raw/ # no network; re-filter saved responses (the re-derivability check)
    python3 collect.py --no-detail     # skip SmartRecruiters' per-posting detail calls (fast, no ad text)

Writes: all-jobs-<date>.{json,csv}  every posting found, ad text omitted for size
        jobs-of-interest-<date>.{json,csv}  the kept postings, with matched words and full text
        quality-report-<date>.md    counts, rejects by reason, completeness, limits
        raw/<provider>-<slug>-<date>.json   each response as the API sent it

Design: SDD.md. P1 every kept record carries the source's own fields under `original`.
P2 the raw response is written before anything parses it. P3 the filter is keywords.json and
every match is published. P4 one source failing does not stop the others. P5 a company with no
match today stays on the watch list. Stdlib only. Exit 0 ran, 2 bad input, 3 every source failed.
"""
import argparse, csv, datetime as dt, html, json, os, re, sys, time, urllib.error, urllib.request
from urllib.parse import quote

ALLOWED = {"boards-api.greenhouse.io", "api.ashbyhq.com", "api.smartrecruiters.com"}
HERE = os.path.dirname(os.path.abspath(__file__))
TODAY = dt.date.today().isoformat()


class InputError(Exception):
    pass


# ---------------------------------------------------------------- fetch
def get(url, timeout=30):
    from urllib.parse import urlparse
    p = urlparse(url)
    if p.scheme != "https" or p.hostname not in ALLOWED:
        raise InputError(f"refusing host {p.hostname!r}: not in {sorted(ALLOWED)}")

    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k):
            return None

    req = urllib.request.Request(url, headers={"User-Agent": "lectern (course project)"})
    with urllib.request.build_opener(NoRedirect).open(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch_board(provider, slug, want_detail=True):
    """Return the provider's raw payload for one board. Raises on failure."""
    if provider == "greenhouse":
        return get(f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true")
    if provider == "ashby":
        return get(f"https://api.ashbyhq.com/posting-api/job-board/{quote(slug)}?includeCompensation=true")
    if provider == "smartrecruiters":
        base = f"https://api.smartrecruiters.com/v1/companies/{quote(slug)}/postings"
        listing, offset = [], 0
        while True:
            page = get(f"{base}?limit=100&offset={offset}")
            got = page.get("content") or []
            listing.extend(got)
            offset += len(got)
            if not got or offset >= int(page.get("totalFound") or 0):
                break
        if not want_detail:
            return {"jobs": listing, "_detail": False}
        out = []
        for j in listing:
            try:
                out.append(get(f"{base}/{j['id']}"))
            except Exception as e:                       # a failed detail call keeps the listing record
                out.append({**j, "_detail_error": str(e)})
            time.sleep(0.05)
        return {"jobs": out, "_detail": True}
    raise InputError(f"unknown provider {provider!r}")


# ---------------------------------------------------------------- normalise
def plain(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(html.unescape(s or "")))).strip()


def iso_date(v):
    if not v:
        return None
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", str(v))
    return m.group(0) if m else None


def normalise(provider, company, payload):
    """One raw payload -> internal views. `original` is the source's record, untouched (P1)."""
    out = []
    for j in payload.get("jobs") or []:
        if provider == "greenhouse":
            v = dict(source_id=str(j.get("id")), title=(j.get("title") or "").strip(),
                     text=plain(j.get("content")), location_text=(j.get("location") or {}).get("name", ""),
                     date_raw=j.get("first_published") or j.get("updated_at"), url=j.get("absolute_url"),
                     department=" / ".join(d.get("name", "") for d in (j.get("departments") or [])))
        elif provider == "ashby":
            locs = [j.get("location") or ""] + [x.get("location") or "" for x in (j.get("secondaryLocations") or [])]
            v = dict(source_id=str(j.get("id")), title=(j.get("title") or "").strip(),
                     text=plain(j.get("descriptionHtml") or j.get("descriptionPlain")),
                     location_text=" · ".join(x for x in locs if x), date_raw=j.get("publishedAt"),
                     url=j.get("jobUrl"),
                     department=" / ".join(x for x in (j.get("department"), j.get("team")) if x))
        else:  # smartrecruiters
            secs = ((j.get("jobAd") or {}).get("sections") or {})
            cf = {f.get("fieldLabel"): f.get("valueLabel") for f in (j.get("customField") or [])}
            loc = j.get("location") or {}
            v = dict(source_id=str(j.get("id")), title=(j.get("name") or "").strip(),
                     text=plain(" ".join((x or {}).get("text") or "" for x in secs.values())),
                     location_text=loc.get("fullLocation") or "", date_raw=j.get("releasedDate"),
                     url=j.get("postingUrl"),
                     department=" / ".join(x for x in ((j.get("function") or {}).get("label"), cf.get("Org")) if x))
        v.update(source=provider, company=company, date_posted=iso_date(v["date_raw"]), original=j)
        out.append(v)
    return out


# ---------------------------------------------------------------- filter
def word_in(word, text):
    return re.search(r"(?<![a-z0-9])" + re.escape(word.lower()) + r"(?![a-z0-9])", text) is not None


def judge(v, kw):
    """Keep on a role word in the title, or >=N topic words in the body. flex_text only annotates."""
    ignore = {w.lower() for w in (kw.get("ignore_words_by_company") or {}).get(v["company"], [])}
    tl, bl = v["title"].lower(), v["text"].lower()
    role = [w for w in kw["role_title"] if w.lower() not in ignore and word_in(w, tl)]
    topic = [w for w in kw["topic_text"] if w.lower() not in ignore and word_in(w, bl)]
    flex = [w for w in kw["flex_text"] if word_in(w, bl)]
    need = kw["keep_rule"]["topic_text_min_if_no_title_match"]
    if role:
        why = "role word in title"
    elif len(topic) >= need:
        why = f"{len(topic)} topic words in body (>= {need})"
    else:
        return None, ("no-keyword-match" if not (role or topic) else
                      f"only {len(topic)} topic words, no role word in title")
    return {"role_title": role, "topic_text": topic, "flex_text": flex,
            "kept_because": why, "title_only": bool(role and not topic)}, None


# ---------------------------------------------------------------- write
def rows_for_csv(records, with_match):
    cols = ["source", "company", "source_id", "title", "url", "location_text", "department",
            "date_posted", "date_posted_raw"]
    if with_match:
        cols += ["matched_role_title", "matched_topic_text", "matched_flex_text", "kept_because", "title_only"]
    else:
        cols += ["kept", "reject_reason"]
    out = [cols]
    for r in records:
        row = [r["source"], r["company"], r["source_id"], r["title"], r["url"], r["location_text"],
               r["department"], r["date_posted"] or "", r["date_raw"] or ""]
        if with_match:
            m = r["matched"]
            row += ["; ".join(m["role_title"]), "; ".join(m["topic_text"]), "; ".join(m["flex_text"]),
                    m["kept_because"], str(m["title_only"])]
        else:
            row += ["yes" if r.get("matched") else "no", r.get("reject_reason") or ""]
        out.append(row)
    return out


def write_json(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(tmp, path)


def write_csv(path, rows):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(rows)
    os.replace(tmp, path)


# ---------------------------------------------------------------- main
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sources", default=os.path.join(HERE, "sources.json"))
    ap.add_argument("--keywords", default=os.path.join(HERE, "keywords.json"))
    ap.add_argument("--out", default=HERE)
    ap.add_argument("--only", help="one provider: greenhouse | ashby | smartrecruiters")
    ap.add_argument("--from-raw", metavar="DIR", help="no network; re-filter saved responses")
    ap.add_argument("--no-detail", action="store_true", help="skip SmartRecruiters per-posting detail calls")
    a = ap.parse_args(argv)

    try:
        cfg = json.load(open(a.sources, encoding="utf-8"))
        kw = json.load(open(a.keywords, encoding="utf-8"))
        for k in ("role_title", "topic_text", "keep_rule"):
            if k not in kw:
                raise InputError(f"keywords.json is missing {k!r}")
    except (OSError, json.JSONDecodeError) as e:
        print(f"INPUT ERROR: {e}", file=sys.stderr)
        return 2
    except InputError as e:
        print(f"INPUT ERROR: {e}", file=sys.stderr)
        return 2

    raw_dir = a.from_raw or os.path.join(a.out, "raw")
    os.makedirs(raw_dir, exist_ok=True)
    boards = [(s["provider"], b["company"], b["slug"]) for s in cfg["sources"]
              for b in s["boards"] if not a.only or s["provider"] == a.only]

    views, status, run_at = [], [], dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    for provider, company, slug in boards:
        path = os.path.join(raw_dir, f"{provider}-{slug.replace(' ', '_').lower()}-{TODAY}.json")
        try:
            if a.from_raw:
                if not os.path.exists(path):
                    status.append({"company": company, "provider": provider, "status": "skipped",
                                   "reason": "no saved response for today"})
                    continue
                payload = json.load(open(path, encoding="utf-8"))
            else:
                payload = fetch_board(provider, slug, want_detail=not a.no_detail)
                write_json(path, payload)                              # P2: raw first
        except Exception as e:
            status.append({"company": company, "provider": provider, "status": "unavailable",
                           "reason": f"{type(e).__name__}: {e}"})      # P4: keep going
            print(f"  {company:12} UNAVAILABLE ({type(e).__name__})", file=sys.stderr)
            continue
        v = normalise(provider, company, payload)
        views.extend(v)
        status.append({"company": company, "provider": provider, "status": "ok", "postings": len(v)})
        print(f"  {company:12} {len(v):4} postings")

    if not any(s["status"] == "ok" for s in status):
        print("every source failed — nothing written", file=sys.stderr)
        return 3

    seen, kept, rejects, all_recs = set(), [], {}, []
    for v in views:
        key = (v["source"], v["source_id"])
        if key in seen:
            rejects["duplicate"] = rejects.get("duplicate", 0) + 1
            continue
        seen.add(key)
        if not v["title"]:
            v["reject_reason"] = "missing-title"
        elif not v["url"]:
            v["reject_reason"] = "missing-url"
        elif not v["date_posted"]:
            v["reject_reason"] = "unparseable-date"
        else:
            m, why = judge(v, kw)
            if m:
                v["matched"] = m
                kept.append(v)
            else:
                v["reject_reason"] = why
        if v.get("reject_reason"):
            rejects[v["reject_reason"]] = rejects.get(v["reject_reason"], 0) + 1
        all_recs.append(v)

    counts = {"boards_requested": len(boards), "boards_ok": sum(1 for s in status if s["status"] == "ok"),
              "postings_fetched": len(views), "postings_unique": len(all_recs),
              "kept": len(kept), "rejected": rejects}
    meta = {"tool": "lectern", "generated_at": run_at, "keywords_version": kw["version"],
            "sources": status, "counts": counts}

    # ALL jobs — every posting found, ad text omitted for size (the raw/ files hold the text)
    write_json(os.path.join(a.out, f"all-jobs-{TODAY}.json"),
               {**meta, "note": "Every posting found on every watched board. Ad text is omitted here for "
                                "file size; the full text is in raw/ exactly as each API sent it.",
                "records": [{k: r[k] for k in ("source", "company", "source_id", "title", "url",
                                               "location_text", "department", "date_posted", "date_raw")}
                            | {"kept": bool(r.get("matched")), "reject_reason": r.get("reject_reason")}
                            for r in all_recs]})
    write_csv(os.path.join(a.out, f"all-jobs-{TODAY}.csv"), rows_for_csv(all_recs, with_match=False))

    # JOBS OF INTEREST — the kept postings, with matched words and the source's own record
    write_json(os.path.join(a.out, f"jobs-of-interest-{TODAY}.json"),
               {**meta, "note": "Postings kept by keywords.json. `matched` is Lectern's; `original` is the "
                                "source's own record with its own field names, unmodified.",
                "records": [{k: r[k] for k in ("source", "company", "source_id", "title", "url",
                                               "location_text", "department", "date_posted", "date_raw",
                                               "matched", "text", "original")} for r in kept]})
    write_csv(os.path.join(a.out, f"jobs-of-interest-{TODAY}.csv"), rows_for_csv(kept, with_match=True))

    print(f"\nfetched {len(views)} · unique {len(all_recs)} · kept {len(kept)} · rejected {sum(rejects.values())}")
    print(f"  all-jobs-{TODAY}.json/.csv · jobs-of-interest-{TODAY}.json/.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
