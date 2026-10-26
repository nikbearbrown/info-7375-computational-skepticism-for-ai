#!/usr/bin/env python3
"""Write the synthetic fixtures and the expected outputs for every workflow. The expected outputs come from the
PYTHON Lectern (collect.py, publish_delta.py, notify.py): the Python is the oracle the n8n workflows are tested against.

Every fixture company and posting is made up. Nothing here is a real company's ad.

  python3 tools/make_fixtures.py --lectern LECTERN_DIR
"""
import argparse, json, os, subprocess, sys, copy

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def _default_lectern():
    """The Python Lectern, when this folder sits inside it (as in the course repository: lectern/forms/n8n/)."""
    d = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))      # lectern/, which holds forms/n8n/
    return d if os.path.exists(os.path.join(d, "lectern_paths.py")) else None



def dump(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, ensure_ascii=False, sort_keys=False)
        f.write("\n")


def payloads():
    gh = {"jobs": [
        {"id": 1001, "title": "Developer Educator", "content": "&lt;p&gt;Teach developers &amp; run workshops.&lt;/p&gt;", "location": {"name": "Remote - US"},
         "departments": [{"name": "Education"}], "first_published": "2026-10-01T10:00:00-04:00", "absolute_url": "https://jobs.example.test/g/1001", "internal_job_id": 5001},
        {"id": 1002, "title": "Staff Backend Engineer", "content": "&lt;p&gt;Build services. Partner with universities, campus programs, student interns and classroom pilots.&lt;/p&gt;",
         "location": {"name": "Boston, MA"}, "departments": [{"name": "Engineering"}, {"name": "Platform"}], "first_published": "2026-10-02T09:30:00-04:00",
         "absolute_url": "https://jobs.example.test/g/1002", "internal_job_id": 5002},
        {"id": 1003, "title": "Payments Analyst", "content": "&lt;p&gt;Reconcile payments every day.&lt;/p&gt;", "location": {"name": "Remote"}, "departments": [],
         "first_published": "2026-10-02T09:30:00-04:00", "absolute_url": "https://jobs.example.test/g/1003", "internal_job_id": 5003},
        {"id": 1001, "title": "Developer Educator (repost)", "content": "&lt;p&gt;Same id, listed twice.&lt;/p&gt;", "location": {"name": "Remote - US"},
         "departments": [], "first_published": "2026-10-01T10:00:00-04:00", "absolute_url": "https://jobs.example.test/g/1001", "internal_job_id": 5001},
        {"id": 1005, "title": "Finance Analyst", "content": "&lt;p&gt;Our customers include one university.&lt;/p&gt;", "location": {"name": "Remote"}, "departments": [{"name": "Finance"}],
         "first_published": "2026-10-03T09:30:00-04:00", "absolute_url": "https://jobs.example.test/g/1005", "internal_job_id": 5005},
        {"id": 1006, "title": "Education Programs Lead", "content": "&lt;p&gt;No link on this one.&lt;/p&gt;", "location": {"name": "Remote"}, "departments": [],
         "first_published": "2026-10-03T09:30:00-04:00", "internal_job_id": 5006},
        {"id": 1007, "title": "Education Programs Lead", "content": "&lt;p&gt;Run education programs.&lt;/p&gt;", "location": {"name": "Tokyo, Japan"}, "departments": [{"name": "Education"}],
         "first_published": "2026-10-04T09:30:00-04:00", "absolute_url": "https://jobs.example.test/g/1007", "internal_job_id": 5007},               # country not allowed
        {"id": 1008, "title": "K12 Education Lead", "content": "&lt;p&gt;Own the school programme.&lt;/p&gt;", "location": {"name": "Remote - US"}, "departments": [{"name": "Education"}],
         "first_published": "2026-10-04T09:30:00-04:00", "absolute_url": "https://jobs.example.test/g/1008", "internal_job_id": 5008},               # K-12 role
        {"id": 1009, "title": "K-12 Education Account Manager, South Korea (12 months contract)", "content": "&lt;p&gt;Own the school system lifecycle.&lt;/p&gt;",
         "location": {"name": "Seoul, Seoul, Korea, republic of"}, "departments": [{"name": "Education"}], "first_published": "2026-10-04T09:30:00-04:00",
         "absolute_url": "https://jobs.example.test/g/1009", "internal_job_id": 5009},                                                              # both
        {"id": 1010, "title": "Learning Designer", "content": "&lt;p&gt;Design lessons.&lt;/p&gt;", "location": {"name": "S\u00e3o Paulo, Brazil"}, "departments": [{"name": "Learning"}],
         "first_published": "2026-10-04T09:30:00-04:00", "absolute_url": "https://jobs.example.test/g/1010", "internal_job_id": 5010},               # an accent, an allowed country
    ]}
    ab = {"jobs": [
        {"id": "a-2001", "title": "Curriculum Lead", "descriptionHtml": "&lt;p&gt;Own curriculum &amp; courseware for the academy.&lt;/p&gt;", "location": "Boston, MA",
         "secondaryLocations": [{"location": "Remote"}], "publishedAt": "2026-10-03T09:00:00.000+00:00", "jobUrl": "https://jobs.example.test/a/2001", "department": "Learning", "team": "Content"},
        {"id": "a-2002", "title": "Strategic Account Manager", "descriptionPlain": "You will own our largest university relationships and manage each higher education partnership.",
         "location": "New York, NY", "secondaryLocations": [], "publishedAt": "2026-10-04T09:00:00.000+00:00", "jobUrl": "https://jobs.example.test/a/2002", "department": "Sales", "team": None},
        {"id": "a-2003", "title": "Content Specialist", "descriptionHtml": "&lt;p&gt;Instructional design and curriculum development for developers &amp; partners.&lt;/p&gt;",
         "location": "Remote", "secondaryLocations": [], "publishedAt": "2026-10-04T10:00:00.000+00:00", "jobUrl": "https://jobs.example.test/a/2003", "department": "Marketing", "team": "Content"},
        {"id": "a-2004", "title": "Education Partnerships Manager", "descriptionHtml": "<p>No published date.</p>", "location": "Remote", "secondaryLocations": [],
         "jobUrl": "https://jobs.example.test/a/2004", "department": "Sales", "team": None},
        {"id": "a-2005", "title": "Developer Advocate", "descriptionHtml": "<p>Advocate for developers.</p>", "location": "Berlin, Germany", "secondaryLocations": [{"location": "Boston, MA"}],
         "publishedAt": "2026-10-04T11:00:00.000+00:00", "jobUrl": "https://jobs.example.test/a/2005", "department": "Developer Relations", "team": None},           # several places, one allowed
    ]}
    sr = {"jobs": [
        {"id": "sr-3001", "name": "Education Program Manager", "jobAd": {"sections": {"companyDescription": {"text": "We teach."}, "jobDescription": {"text": "<p>Run education programs.</p>"}}},
         "customField": [{"fieldLabel": "Org", "valueLabel": "Learning"}], "location": {"fullLocation": "New York, NY, US"}, "releasedDate": "2026-10-05T12:00:00.000Z",
         "postingUrl": "https://jobs.example.test/s/3001", "function": {"label": "Education"}},
        {"id": "sr-3003", "name": "Education Program Manager", "jobAd": {"sections": {"jobDescription": {"text": "<p>Run education programs.</p>"}}}, "customField": [],
         "location": {"fullLocation": "Taipei, Taiwan"}, "releasedDate": "2026-10-05T12:00:00.000Z", "postingUrl": "https://jobs.example.test/s/3003", "function": {"label": "Education"}},   # country not allowed
        {"id": "sr-3002", "name": "Warehouse Associate", "jobAd": {"sections": {"jobDescription": {"text": "Pack boxes."}}}, "customField": [], "location": {"fullLocation": "Reno, NV, US"},
         "releasedDate": "2026-10-05T12:00:00.000Z", "postingUrl": "https://jobs.example.test/s/3002", "function": {"label": "Operations"}},
    ], "_detail": True}
    return [
        {"provider": "greenhouse", "company": "ExampleCo Labs", "slug": "examplelabs", "payload": gh},
        {"provider": "ashby", "company": "ExampleCo Ashby", "slug": "Example Ashby", "payload": ab},
        {"provider": "smartrecruiters", "company": "ExampleCo Recruiters", "slug": "examplesr", "payload": sr},
    ]


def strip_original(v):
    return {k: x for k, x in v.items() if k != "original"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lectern", default=_default_lectern())
    a = ap.parse_args()
    if not a.lectern:
        ap.error("--lectern is required (or put this folder beside a lectern/ folder)")
    sys.path.insert(0, os.path.abspath(a.lectern))
    import lectern_paths as lp   # the Python Lectern's own map of where its files are (config/, collect/, publish/, audit/)
    import collect, publish_delta as pd, notify
    kw = json.load(open(lp.config("keywords.json"), encoding="utf-8"))
    src = json.load(open(lp.config("sources.json"), encoding="utf-8"))
    dump(os.path.join(ROOT, "shared", "keywords.json"), kw)
    boards = [{"provider": s["provider"], "company": b["company"], "slug": b["slug"], "tier": b.get("tier")} for s in src["sources"] for b in s["boards"]]
    dump(os.path.join(ROOT, "shared", "boards.json"), {"_comment": "The watch list, copied from lectern/sources.json (the master). Edit it there, never here.", "boards": boards})

    # ---- 01 collect: raw payloads -> normalised views
    pl = payloads()
    views = []
    for p in pl:
        views.extend(collect.normalise(p["provider"], p["company"], p["payload"]))
    dump(os.path.join(ROOT, "01-collect", "fixtures", "payloads.json"), pl)
    dump(os.path.join(ROOT, "01-collect", "expected.json"), {"views": [strip_original(v) for v in views], "status": [
        {"company": p["company"], "provider": p["provider"], "status": "ok", "postings": len(p["payload"]["jobs"])} for p in pl]})

    # ---- 02 filter: normalised views -> kept / rejected, as collect.main does
    seen, recs, rejects = set(), [], {}
    for v in views:
        k = (v["source"], v["source_id"])
        if k in seen:
            rejects["duplicate"] = rejects.get("duplicate", 0) + 1
            continue
        seen.add(k)
        reason, matched = None, None
        if not v["title"]: reason = "missing-title"
        elif not v["url"]: reason = "missing-url"
        elif not v["date_posted"]: reason = "unparseable-date"
        else:
            m, why = collect.judge(v, kw)
            matched, reason = (m, None) if m else (None, why)
        if reason:
            rejects[reason] = rejects.get(reason, 0) + 1
        recs.append({**{f: v[f] for f in ("source", "company", "source_id", "title", "text", "url", "location_text", "department", "date_posted", "job_ref")},
                     "kept": bool(matched), "matched": matched, "reject_reason": reason})
    kept_because = {r["source_id"]: r["matched"]["kept_because"] for r in recs if r["kept"]}
    need = {"role word in title", "body says it produces teaching materials for a named audience", "account or partnership role whose body names higher education"}
    got = set(kept_because.values())
    assert need <= got and any("topic words" in x for x in got), f"fixtures do not cover every keep rule: {got}"
    for r in ("no-keyword-match", "missing-url", "unparseable-date", "duplicate"):
        assert r in rejects, f"fixtures do not cover reject {r}: {rejects}"
    assert any(str(k).startswith("only ") for k in rejects), f"no 'only N topic words' reject: {rejects}"
    assert any(str(k).startswith("country not allowed") for k in rejects), f"no 'country not allowed' reject: {rejects}"
    assert any(str(k).startswith("K-12 role") for k in rejects), f"no 'K-12 role' reject: {rejects}"
    assert any(" and " not in str(k) and "country not allowed" in str(k) and "K-12 role" in str(k) for k in rejects), f"no reject for both gates: {rejects}"
    assert any(r["kept"] and (r["matched"].get("location") or {}).get("country_named") is False for r in recs), "no kept posting with an unnamed location"
    sources = [{"company": p["company"], "provider": p["provider"], "status": "ok", "postings": len(p["payload"]["jobs"])} for p in pl]
    dump(os.path.join(ROOT, "02-filter", "fixtures", "views.json"), {"date": "2026-10-19", "sources": sources, "views": [strip_original(v) for v in views]})
    dump(os.path.join(ROOT, "02-filter", "expected.json"), {"counts": {"postings_fetched": len(views), "postings_unique": len(recs), "kept": sum(r["kept"] for r in recs), "rejected": rejects},
                                                            "keywords_version": kw["version"], "records": recs})

    # ---- 03 delta: an earlier published state and a later run that differs in each way
    earlier = [copy.deepcopy(r) for r in recs if r["kept"]]
    stale = {k: v for k, v in zip(("source", "company", "source_id"), ("greenhouse", "ExampleCo Labs", "1999"))}
    earlier.append({**earlier[0], **stale, "title": "Developer Educator (closed)", "url": "https://jobs.example.test/g/1999", "text": "Gone from the board."})            # no longer on the board
    earlier.append({**earlier[0], "source": "greenhouse", "company": "ExampleCo Labs", "source_id": "1003", "title": "Payments Analyst", "url": "https://jobs.example.test/g/1003", "text": "Was kept earlier."})   # still on board, now rejected
    earlier.append({**earlier[0], "source": "greenhouse", "company": "ExampleCo Labs", "source_id": "1007", "title": "Education Programs Lead", "url": "https://jobs.example.test/g/1007", "text": "Was kept before the country rule."})   # still on board, now rejected by a gate
    earlier.append({**earlier[0], "source": "ashby", "company": "ExampleCo Down", "source_id": "z-1", "title": "Educator", "url": "https://jobs.example.test/z/1", "text": "Its board is down today."})  # unavailable source
    earlier = [r for r in earlier if r["source_id"] != "a-2002"]                                                                                                   # a-2002 becomes new
    for r in earlier:
        if r["source_id"] == "1002":
            r["title"] = "Backend Engineer"                                                                                                                         # changed title
        if r["source_id"] == "a-2001":
            r["text"] = r["text"] + " Older wording."                                                                                                               # changed ad text
    later_sources = sources + [{"company": "ExampleCo Down", "provider": "ashby", "status": "unavailable", "reason": "HTTPError: 503"}]
    dump(os.path.join(ROOT, "03-delta", "fixtures", "earlier-kept.json"), {"date": "2026-10-18", "kw_version": kw["version"], "records": earlier})
    state = json.loads(subprocess.run(["node", os.path.join(ROOT, "tools", "js_state.js")], input=json.dumps({"records": earlier, "date": "2026-10-18", "kw_version": kw["version"]}),
                                      capture_output=True, text=True, check=True).stdout)
    later_run = {"date": "2026-10-19", "kw_version": kw["version"], "sources": later_sources, "records": recs}
    dump(os.path.join(ROOT, "03-delta", "fixtures", "input.json"), {"state": state, "run": later_run})
    pstate = {pd.key_of(r): {**pd.slim(r), "fp": pd.fingerprint(pd.slim(r))} for r in earlier}
    prun = {"date": "2026-10-19", "kw_version": kw["version"], "kept": {pd.key_of(r): pd.slim(r) for r in recs if r["kept"]},
            "all": {pd.key_of(r): r for r in recs}, "sources": {s["company"]: s for s in later_sources}}
    new, changed, gone = pd.diff(pstate, prun)
    summ = lambda r: {"key": pd.key_of(r), "why": r.get("why"), "fields": sorted(c["field"] for c in r.get("changes", []))}
    base_cos = {v["company"] for v in pstate.values()}
    expected = {"new": sorted((summ(r) for r in new), key=lambda x: x["key"]), "changed": sorted((summ(r) for r in changed), key=lambda x: x["key"]),
                "gone": sorted((summ(r) for r in gone), key=lambda x: x["key"]), "first_time_companies": sorted({r["company"] for r in new if r["company"] not in base_cos})}
    dump(os.path.join(ROOT, "03-delta", "expected.json"), expected)

    # ---- 04 post: messages for the new listings (nothing is sent)
    watched = sorted({s["company"] for s in sources})
    nr = [pd.slim(r) for r in recs if r["kept"] and f"{r['source']}:{r['source_id']}" in {x["key"] for x in expected["new"]}]
    already = [f"{nr[0]['source']}:{nr[0]['source_id']}"] if nr else []
    rows, msgs = notify.build_messages(nr, set(watched), {"ExampleCo Ashby"}, set(already))
    dump(os.path.join(ROOT, "04-post-to-discord", "fixtures", "input.json"), {"new": nr, "watched": watched, "first_time_companies": ["ExampleCo Ashby"], "already": already, "send": False})
    dump(os.path.join(ROOT, "04-post-to-discord", "expected.json"), {"rows": [f"{r['source']}:{r['source_id']}" for r in rows], "messages": msgs})
    print("fixtures and expected outputs written. kept:", sorted(kept_because.items()), "rejects:", rejects)
    print("delta expected: new", [x["key"] for x in expected["new"]], "changed", [(x["key"], x["fields"]) for x in expected["changed"]], "gone", [(x["key"], x["why"][:40]) for x in expected["gone"]])


if __name__ == "__main__":
    main()
