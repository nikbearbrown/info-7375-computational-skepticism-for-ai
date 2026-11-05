#!/usr/bin/env python3
"""consulting_collect.py — read the job boards of the consulting firms on the list, for the consulting channel only.

    python3 consulting_collect.py [--out runs/DATE] [--only SLUG]

The firms are the `consulting` section of config/targets.json with status `active` (a board Lectern's own readers can read:
Greenhouse, Ashby, SmartRecruiters, Workday, Oracle). One request per board (Workday: one per page of 20 postings; Oracle: one per page of 25), a pause between
requests, the same host list and user agent as collect.py. It reads the postings' LISTS (title, place, link), never the ad text: the consulting judge reads titles.

This is deliberately NOT part of collect.py: collect.py reads the watch list for the #professor-bear feed, and the consulting
firms must never enter it (config/sources.json is generated from the `boards` section only; a test checks it).

Writes: <out>/consulting-jobs-<date>.json     every posting found, in the shape publish/consulting_feed.py and the judge read
        <out>/consulting-raw/<provider>-<slug>-<date>.json   each response as the board sent it (kept local, not committed)
Exit 0 ran, 2 bad input, 3 every board failed.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, datetime as dt, json, os, re, sys, time
from urllib.parse import quote

import collect
import consulting_jobs as cj

PAUSE = 1.2          # seconds between boards: a polite pace, one request per board unless a list has more than one page


def boards_from_targets(doc):
    """[(firm, provider, slug)] for the consulting firms whose board Lectern can read (status active)."""
    return [(t["name"], t["provider"], t["consulting"]["board"]["slug"]) for t in doc["targets"]
            if t.get("section") == "consulting" and t.get("status") == "active"]


def fetch_list(provider, slug):
    """The board's list of postings as the board sent it. Never the ad text."""
    if provider == "greenhouse":
        return collect.get(f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs")
    if provider == "ashby":
        return collect.get(f"https://api.ashbyhq.com/posting-api/job-board/{quote(slug)}")
    if provider == "smartrecruiters":
        return collect.fetch_board("smartrecruiters", slug, want_detail=False)          # the list only: no call per posting
    if provider == "workday":
        return collect.fetch_workday(slug, pause=PAUSE)                                  # the list only: one POST a page, a pause between pages
    if provider == "oracle":
        return collect.fetch_oracle(slug, pause=PAUSE)                                   # the list only: one GET a page of 25, a pause between pages
    if provider == "usajobs":
        return collect.fetch_usajobs(slug, pause=PAUSE)                                  # USAJOBS' search API: a key and an email from ~/.usajobs, the list only
    raise collect.InputError(f"unknown provider {provider!r}")


def raw_name(provider, slug, today):
    """The file a board's response is kept in: a Workday id has a slash ('guidehouse.wd1/External')."""
    return f"{provider}-{re.sub(r'[^a-z0-9._-]+', '_', slug.lower())}-{today}.json"


def workday_posted(text, today=None):
    """'Posted Today' / 'Posted Yesterday' / 'Posted 3 Days Ago' -> an ISO date; 'Posted 30+ Days Ago' and anything else -> None (not a date)."""
    today = today or dt.date.today()
    t = (text or "").lower()
    if "today" in t:
        return today.isoformat()
    if "yesterday" in t:
        return (today - dt.timedelta(days=1)).isoformat()
    m = re.search(r"posted (\d+) days? ago", t)
    return (today - dt.timedelta(days=int(m.group(1)))).isoformat() if m else None


def workday_place(j):
    """A Workday list item's place. The list gives 'US - TX, San Antonio', a count ('2 Locations': no place named) or nothing at all; when
    it gives nothing the place is read from the city in the posting's own address (/job/<city>/<title>_<id>)."""
    loc = (j.get("locationsText") or "").strip()
    if loc:
        return loc
    m = re.match(r"/job/([^/]+)/", j.get("externalPath") or "")
    return re.sub(r"\s+", " ", m.group(1).replace("-", " ")).strip() if m else ""


def oracle_place(j):
    """An Oracle list item's places in the words the judges read: the main place (it names its country, 'Atlanta, GA, United States'), then each other place the
    posting names. The reply's two-letter country code is not used: 'IN' is not a word the country reader knows."""
    places = []
    for x in [j.get("PrimaryLocation")] + list(j.get("secondaryLocations") or []):
        if isinstance(x, dict):
            x = x.get("Name") or x.get("LocationName") or x.get("name")
        x = (x or "").strip()
        if x and x not in places:
            places.append(x)
    return " · ".join(places)


def truthy(v):
    return v is True or str(v).strip().lower() in ("true", "yes", "y", "1")


def usajobs_place(j):
    """A USAJOBS result's places in the words the judges read: each place with its country, and 'Remote' when USAJOBS marks the posting remote. USAJOBS' telework
    flag is NOT turned into a word: 'telework eligible' means an office job that may be done from home some days, which is not remote work."""
    places = []
    for x in j.get("places") or []:
        name = (x.get("name") or "").strip()
        if name and x.get("country") and x["country"].lower() not in name.lower():
            name = f"{name}, {x['country']}"
        if name and name not in places:
            places.append(name)
    if truthy(j.get("remote_indicator")):
        places.append("Remote")
    return " · ".join(places)


def records(provider, firm, slug, payload):
    """One board's payload -> [{source, company, source_id, title, url, location_text, department, date_posted}]."""
    out = []
    for j in payload.get("jobs") or []:
        if provider == "greenhouse":
            r = dict(source_id=str(j.get("id")), title=(j.get("title") or "").strip(), url=j.get("absolute_url"),
                     location_text=(j.get("location") or {}).get("name", ""), department="", date_posted=collect.iso_date(j.get("first_published") or j.get("updated_at")))
        elif provider == "workday":
            host, _tenant, site = collect.workday_parts(slug)
            ref = (j.get("bulletFields") or [None])[0]
            r = dict(external_path=j.get("externalPath"), source_id=str(ref or j.get("externalPath")), title=(j.get("title") or "").strip(), url=f"https://{host}/en-US/{site}{j.get('externalPath')}",
                     location_text=workday_place(j), department="", date_posted=workday_posted(j.get("postedOn")))
        elif provider == "oracle":
            host, site = collect.oracle_parts(slug)
            r = dict(source_id=str(j.get("Id")), title=(j.get("Title") or "").strip(), url=f"https://{host}/hcmUI/CandidateExperience/en/sites/{site}/job/{j.get('Id')}",
                     location_text=oracle_place(j), department="", date_posted=collect.iso_date(j.get("PostedDate")))
        elif provider == "usajobs":
            # the employer is the agency that posts it, so the posting is shown under its name, not under 'USAJOBS'
            r = dict(source_id=str(j.get("object_id") or j.get("id")), title=(j.get("title") or "").strip(), url=j.get("url"), location_text=usajobs_place(j),
                     department=j.get("department") or "", date_posted=collect.iso_date(j.get("published")), matched_by=j.get("matched_by"),
                     remote_indicator=j.get("remote_indicator"), telework_eligible=j.get("telework_eligible"), closes=collect.iso_date(j.get("closes")),
                     description=j.get("ad_text") or "")
            firm_here = j.get("organization") or firm
            out.append({"source": provider, "company": firm_here, **r})
            continue
        elif provider == "ashby":
            locs = [j.get("location") or ""] + [x.get("location") or "" for x in (j.get("secondaryLocations") or [])]
            r = dict(source_id=str(j.get("id")), title=(j.get("title") or "").strip(), url=j.get("jobUrl"), location_text=" · ".join(x for x in locs if x),
                     department=" / ".join(x for x in (j.get("department"), j.get("team")) if x), date_posted=collect.iso_date(j.get("publishedAt")))
        else:   # smartrecruiters list item
            loc = j.get("location") or {}
            r = dict(source_id=str(j.get("id")), title=(j.get("name") or "").strip(), url=f"https://jobs.smartrecruiters.com/{slug}/{j.get('id')}",
                     location_text=loc.get("fullLocation") or ", ".join(x for x in (loc.get("city"), loc.get("region"), (loc.get("country") or "").upper()) if x),
                     department=((j.get("function") or {}).get("label") or ""), date_posted=collect.iso_date(j.get("releasedDate")))
        out.append({"source": provider, "company": firm, **r})
    return out


COUNT_PLACE = re.compile(r"^\d+ locations?$", re.I)


def name_places(recs, slug, wanted, pause=None):
    """A Workday list gives a count ('3 Locations') where a posting has several places, and a country or a 'Remote' among them is invisible. For the postings
    whose place is only a count AND that `wanted(record)` says matter (the channel's own judge would post them), one request to the posting's own record gives
    its places. Nothing else is fetched, and a failed request keeps the count. Mutates and returns recs."""
    for r in recs:
        if r.get("source") != "workday" or not COUNT_PLACE.match((r.get("location_text") or "").strip()) or not wanted(r):
            continue
        time.sleep(PAUSE if pause is None else pause)
        try:
            places = collect.workday_places(slug, r.get("external_path"))
        except Exception as e:
            print(f"    places of '{r['title']}' not read ({type(e).__name__}): the count stays", file=sys.stderr)
            continue
        if places:
            r["location_text"] = " · ".join(places)
            r["places_from_posting"] = True
    return recs


def name_the_places(recs, slug, kw, pause=None):
    """The consulting channel: look up the places of the Workday postings that the consulting judge would post on their title and a count alone."""
    return name_places(recs, slug, lambda r: cj.judge_consulting(cj.posting_view(r), kw)["decision"] == "post", pause)


def board_ok(name, provider, got, payload):
    """The status line of a board that answered. A Workday or Oracle list says how many postings it holds: if fewer came back, the line says so."""
    st = {"company": name, "provider": provider, "status": "ok", "postings": len(got)}
    if provider in ("workday", "oracle", "usajobs"):
        st.update(listed_total=payload["total"], complete=bool(payload["complete"]))
        if provider == "usajobs":
            st["queries"] = payload["queries"]
    return st


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--targets", default=lp.config("targets.json"))
    ap.add_argument("--out", default=None, help="default runs/<today>")
    ap.add_argument("--only", help="one board slug")
    a = ap.parse_args(argv)
    today = dt.date.today().isoformat()
    out = a.out or os.path.join(lp.RUNS, today)
    try:
        with open(a.targets, encoding="utf-8") as f:
            boards = boards_from_targets(json.load(f))
    except (OSError, json.JSONDecodeError, KeyError) as e:
        print(f"INPUT ERROR: {e}", file=sys.stderr)
        return 2
    boards = [b for b in boards if not a.only or b[2] == a.only]
    with open(lp.config("keywords.json"), encoding="utf-8") as f:
        kw = json.load(f)
    raw_dir = os.path.join(out, "consulting-raw")
    os.makedirs(raw_dir, exist_ok=True)
    recs, status = [], []
    for i, (firm, provider, slug) in enumerate(boards):
        if i:
            time.sleep(PAUSE)
        try:
            payload = fetch_list(provider, slug)
            collect.write_json(os.path.join(raw_dir, raw_name(provider, slug, today)), payload)      # raw first
        except Exception as e:                                                                                  # one board failing does not stop the others
            status.append({"company": firm, "provider": provider, "status": "unavailable", "reason": f"{type(e).__name__}: {e}"})
            print(f"  {firm:28} UNAVAILABLE ({type(e).__name__})", file=sys.stderr)
            continue
        got = records(provider, firm, slug, payload)
        if provider == "workday":
            got = name_the_places(got, slug, kw)
        recs += got
        status.append(board_ok(firm, provider, got, payload))
        print(f"  {firm:28} {len(got):4} postings" + ("" if status[-1].get("complete", True) else f"  (the board lists {payload['total']}: not all came back)"))
    if not any(s["status"] == "ok" for s in status):
        print("every board failed or none is listed: nothing written", file=sys.stderr)
        return 3
    path = os.path.join(out, f"consulting-jobs-{today}.json")
    collect.write_json(path, {"tool": "lectern consulting_collect", "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                              "note": "Every posting on the consulting firms' readable boards: title, place and link only. Not the watch list of the #professor-bear feed.",
                              "sources": status, "records": recs})
    print(f"\n{len(recs)} postings from {sum(1 for s in status if s['status'] == 'ok')} of {len(boards)} boards -> {os.path.basename(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
