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

Two gates sit after the keywords (v0.6.0, both rules in keywords.json): a posting the keywords would keep is rejected,
with the reason, if its place names no allowed country (`location_rule`) or it is a K-12 role (`k12_rule`).
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, csv, datetime as dt, html, json, os, re, sys, time, unicodedata, urllib.error, urllib.request
from urllib.parse import quote

ALLOWED = {"boards-api.greenhouse.io", "api.ashbyhq.com", "api.smartrecruiters.com"}
# Workday boards, one host each, only the ones whose robots.txt and terms were read and allow it (see TARGETS.md section K and I, HISTORY.md 2026-11-01).
# Not here on purpose: bah.wd1 (Booz Allen terms forbid bots), icf.wd5 and leidos.wd5 (terms forbid scraping), caci.wd1 (robots.txt disallows its board),
# cambridgeassociates.wd5 and bakertilly.wd5 (terms forbid automated access), perkins.wd503 (terms forbid robots), accenture.wd103 (its list has no place and is capped at a count that is not
# the true one), vizient.wd1 (a different employer's board: none of its 227 titles names Kaufman Hall).
WORKDAY_HOSTS = {"guidehouse.wd1.myworkdayjobs.com", "gdit.wd5.myworkdayjobs.com", "unisys.wd5.myworkdayjobs.com", "salesforce.wd12.myworkdayjobs.com",
                 "huron.wd1.myworkdayjobs.com", "alirahealth.wd3.myworkdayjobs.com", "ankura.wd5.myworkdayjobs.com", "thinkbrg.wd5.myworkdayjobs.com"}
ALLOWED |= WORKDAY_HOSTS
# USAJOBS' own public search API (developer.usajobs.gov), for the federal-508 channel: it needs a key and the registered email, both kept outside the repo (see usajobs_login).
ALLOWED.add("data.usajobs.gov")
# SAM.gov's public Contract Opportunities extract (collect/sam_opportunities.py): the download address on sam.gov answers 303 to a signed link on its own storage host.
ALLOWED |= {"sam.gov", "falextracts.s3.amazonaws.com"}
HERE = lp.ROOT
TODAY = dt.date.today().isoformat()
USER_AGENT = "lectern (course project)"


class InputError(Exception):
    pass


# ---------------------------------------------------------------- fetch
class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def _checked(url):
    from urllib.parse import urlparse
    p = urlparse(url)
    if p.scheme != "https" or p.hostname not in ALLOWED:
        raise InputError(f"refusing host {p.hostname!r}: not in {sorted(ALLOWED)}")
    return url


def get(url, timeout=30):
    req = urllib.request.Request(_checked(url), headers={"User-Agent": USER_AGENT})
    with urllib.request.build_opener(_NoRedirect).open(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def get_json(url, timeout=30, headers=None):
    """A GET that answers JSON only (the same guards as post_json): one posting's own record on a Workday board. `headers` replace the defaults key by key."""
    req = urllib.request.Request(_checked(url), headers={"User-Agent": USER_AGENT, "Accept": "application/json", **(headers or {})})
    with urllib.request.build_opener(_NoRedirect).open(req, timeout=timeout) as r:
        if "json" not in (r.headers.get("Content-Type") or "").lower():
            raise ValueError(f"not JSON: Content-Type {r.headers.get('Content-Type')!r}")
        return json.loads(r.read().decode("utf-8"))


def post_json(url, body, timeout=30):
    """POST a JSON body, answer parsed. Same host list, no redirects (a redirect to a sign-in page is an error, not a board), and a reply
    that is not JSON is an error: an HTML error page is never parsed."""
    req = urllib.request.Request(_checked(url), data=json.dumps(body).encode("utf-8"), method="POST",
                                 headers={"User-Agent": USER_AGENT, "Accept": "application/json", "Content-Type": "application/json"})
    with urllib.request.build_opener(_NoRedirect).open(req, timeout=timeout) as r:
        if "json" not in (r.headers.get("Content-Type") or "").lower():
            raise ValueError(f"not JSON: Content-Type {r.headers.get('Content-Type')!r}")
        return json.loads(r.read().decode("utf-8"))


WORKDAY_SLUG = re.compile(r"^([a-z0-9-]+)\.(wd\d+)/([A-Za-z0-9_-]+)$")
WORKDAY_PAGE = 20          # postings a request (the most the public list is known to give)
WORKDAY_DISPLAY_CAP = 2000
WORKDAY_MAX_PAGES = 250    # 5,000 postings: a stop in case a board never says it has ended


def workday_parts(slug):
    """'guidehouse.wd1/External' -> (host, tenant, site)."""
    m = WORKDAY_SLUG.match(slug or "")
    if not m:
        raise InputError(f"not a Workday board id (tenant.wdN/site): {slug!r}")
    return f"{m.group(1)}.{m.group(2)}.myworkdayjobs.com", m.group(1), m.group(3)


def workday_places(slug, external_path):
    """The places one Workday posting names, from its own record: its main location and its additional locations. One request.
    The list says '3 Locations' and nothing more; this is how a posting is found to include 'US - Remote (Any location)'."""
    host, tenant, site = workday_parts(slug)
    if not re.match(r"^/job/[^/]+/[^/]+$", external_path or ""):
        raise InputError(f"not a posting address: {external_path!r}")
    info = (get_json(f"https://{host}/wday/cxs/{tenant}/{site}{external_path}").get("jobPostingInfo") or {})
    return [x for x in [info.get("location")] + list(info.get("additionalLocations") or []) if x]


def fetch_workday(slug, pause=1.2):
    """Every posting on one Workday board's public list: one POST a page of 20, a pause between pages, never the ad text.
    -> {"total": the count the board gives, "jobs": [...], "pages": n, "complete": bool}. The list is read until it ends or says it is done."""
    host, tenant, site = workday_parts(slug)
    url = f"https://{host}/wday/cxs/{tenant}/{site}/jobs"
    jobs, seen, total, pages = [], set(), None, 0
    while pages < WORKDAY_MAX_PAGES:
        if pages:
            time.sleep(pause)
        page = post_json(url, {"appliedFacets": {}, "limit": WORKDAY_PAGE, "offset": len(seen), "searchText": ""})
        pages += 1
        got = page.get("jobPostings")
        if not isinstance(got, list):
            raise ValueError("no jobPostings list in the reply")
        if total is None:
            total = int(page.get("total") or 0)
        fresh = [j for j in got if j.get("externalPath") not in seen]      # the list can shift while it is read: a posting counts once
        seen.update(j.get("externalPath") for j in fresh)
        jobs.extend(fresh)
        if not got or len(seen) >= total:
            break
    # a total of exactly 2000 is the board's display cap, not a count (Accenture's list went on past it): not complete
    return {"total": total or 0, "jobs": jobs, "pages": pages, "complete": len(jobs) >= (total or 0) and total != WORKDAY_DISPLAY_CAP}


USAJOBS_DIR = os.path.join(os.path.expanduser("~"), ".usajobs")
USAJOBS_QUERIES = ("508", "accessibility", "WCAG", "assistive technology", "VPAT", "a11y")   # USAJOBS' Keyword search: it matches the whole ad, the judge then reads the TITLE
USAJOBS_PAGE = 500          # results a request (the most the API gives)
USAJOBS_MAX_PAGES = 20      # a stop per query in case a search never says it has ended


def usajobs_login(home=None):
    """(key, email) from <home or ~/.usajobs>/key and /email, both made by the person, mode 600 like the Discord webhooks. USAJOBS asks for the key in an
    Authorization-Key header and the registered email as the User-Agent. Nothing here ever prints either value: an error names the file, never its content."""
    d = home or USAJOBS_DIR
    out = []
    for name, shape in (("key", r"[A-Za-z0-9+/=_-]{20,}"), ("email", r"[^@\s]+@[^@\s]+\.[^@\s]+")):
        path = os.path.join(d, name)
        try:
            mode = os.stat(path).st_mode & 0o777
            with open(path, encoding="utf-8") as f:
                v = f.read().strip()
        except OSError:
            raise InputError(f"{path} not found: USAJOBS needs the {'key it sent' if name == 'key' else 'email the key was registered with (it is the User-Agent)'} in that file")
        if mode & 0o077:
            raise InputError(f"{path} is readable by others (mode {mode:o}): chmod 600 it")
        if not re.fullmatch(shape, v):
            raise InputError(f"{path} does not have the shape of a USAJOBS {name} (value not shown)")
        out.append(v)
    return tuple(out)


USAJOBS_AD_CHARS = 8000     # characters of an ad's summary, duties and qualifications kept for the judge


def _ad_text(d, det):
    """The posting's own summary, major duties and qualification summary, joined. The judge looks in it only for the phrases that say 508 is the WORK asked for."""
    duties = det.get("MajorDuties")
    parts = [det.get("JobSummary"), " ".join(duties) if isinstance(duties, list) else duties, d.get("QualificationSummary")]
    return plain(" ".join(p for p in parts if p))[:USAJOBS_AD_CHARS]


def _usajobs_item(d):
    """The fields of one USAJOBS search result that the judge and the feed need: title, agency, places, dates, the remote flag, and the ad's summary and duties (kept in the
    local run files only, never in a post). No contact, pay or application text."""
    det = ((d.get("UserArea") or {}).get("Details") or {})
    names = lambda k: [x.get("Name") for x in (d.get(k) or []) if x.get("Name")]
    return {"id": d.get("PositionID"), "title": d.get("PositionTitle"), "url": d.get("PositionURI"), "organization": d.get("OrganizationName"),
            "department": d.get("DepartmentName"), "places": [{"name": x.get("LocationName"), "country": x.get("CountryCode")} for x in (d.get("PositionLocation") or [])],
            "published": d.get("PublicationStartDate"), "closes": d.get("ApplicationCloseDate"), "offering": names("PositionOfferingType"), "schedule": names("PositionSchedule"),
            "remote_indicator": det.get("RemoteIndicator"), "telework_eligible": det.get("TeleworkEligible"), "clearance": det.get("SecurityClearance"),
            "ad_text": _ad_text(d, det)}


def fetch_usajobs(slug="search", pause=1.2, login=None):
    """What USAJOBS' search API finds for USAJOBS_QUERIES: one GET a page of up to 500, a pause between requests, each posting once. `login` is (key, email) or read from ~/.usajobs.
    -> {"total": postings found (each once), "jobs": [...trimmed...], "pages": n, "complete": bool, "queries": {query: the count USAJOBS gave}}."""
    if slug != "search":
        raise InputError(f"unknown USAJOBS board {slug!r}")
    key, email = login or usajobs_login()
    head = {"User-Agent": email, "Authorization-Key": key}
    jobs, seen, counts, pages, complete = [], {}, {}, 0, True
    for q in USAJOBS_QUERIES:
        got_q, page_no, want = 0, 1, None
        while page_no <= USAJOBS_MAX_PAGES:
            if pages:
                time.sleep(pause)
            r = (get_json(f"https://data.usajobs.gov/api/search?Keyword={quote(q)}&ResultsPerPage={USAJOBS_PAGE}&Page={page_no}", headers=head).get("SearchResult") or {})
            pages += 1
            items = r.get("SearchResultItems")
            if not isinstance(items, list):
                raise ValueError("no SearchResultItems list in the reply")
            if want is None:
                want = int(r.get("SearchResultCountAll") or 0)
            for it in items:
                got_q += 1
                d = it.get("MatchedObjectDescriptor") or {}
                oid = str(it.get("MatchedObjectId") or d.get("PositionID"))
                if oid in seen:
                    seen[oid]["matched_by"].append(q)
                    continue
                seen[oid] = {**_usajobs_item(d), "object_id": oid, "matched_by": [q]}
                jobs.append(seen[oid])
            if not items or got_q >= want:
                break
            page_no += 1
        counts[q] = want or 0
        complete = complete and got_q >= (want or 0)
    return {"total": len(jobs), "jobs": jobs, "pages": pages, "complete": complete, "queries": counts}


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
                     department=" / ".join(d.get("name", "") for d in (j.get("departments") or [])),
                     # the underlying job, which can have several posts and can be re-posted under a new post id
                     job_ref=str(j["internal_job_id"]) if j.get("internal_job_id") is not None else None)
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
        v.setdefault("job_ref", None)
        v.update(source=provider, company=company, date_posted=iso_date(v["date_raw"]), original=j)
        out.append(v)
    return out


# ---------------------------------------------------------------- filter
def word_in(word, text):
    return re.search(r"(?<![a-z0-9])" + re.escape(word.lower()) + r"(?![a-z0-9])", text) is not None


def materials_evidence(body_lc, kw):
    """The body says the job is to MAKE teaching materials FOR a named audience. Both halves required:
    'maintain documentation' in a tax ad has the first and not the second (SDD P3 — the rule is the file)."""
    rule = kw.get("materials_rule") or {}
    if not rule:
        return None
    vo = [p for p in rule.get("verb_object", []) if p.lower() in body_lc]
    au = [p for p in rule.get("audience", []) if p.lower() in body_lc]
    if len(vo) >= rule.get("min_verb_object", 1) and len(au) >= rule.get("min_audience", 1):
        return {"verb_object": vo[:6], "audience": au[:6]}
    return None


def connector_evidence(title_lc, body_lc, kw):
    """A role that owns a big institutional relationship: an account or partnership word in the TITLE and a
    higher-education institution in the BODY. Both halves required (see keywords.json connector_rule)."""
    rule = kw.get("connector_rule") or {}
    if not rule:
        return None
    tw = [w for w in rule.get("title_words", []) if word_in(w, title_lc)]
    iw = [w for w in rule.get("institution_words", []) if word_in(w, body_lc)]
    return {"title": tw, "institution": iw[:6]} if tw and iw else None


def fold(s):
    """Lower-case with accents removed ('São Paulo' -> 'sao paulo'), so the place lists can be written in plain letters."""
    s = unicodedata.normalize("NFKD", s or "").lower()
    return "".join(ch for ch in s if not unicodedata.combining(ch))


_PLACES = {}


def places_of(rule):
    """Compile location_rule once: folded name -> country for its three tables, plus the regexes that find them."""
    hit = _PLACES.get(id(rule))
    if hit and hit[0] is rule:
        return hit[1]
    allowed = set(rule.get("allowed_countries") or [])
    tables = {"names": {}, "places": {}, "codes": {}}
    for country, spec in rule["countries"].items():
        for kind, table in tables.items():
            for w in spec.get(kind) or []:
                w = fold(w).strip()
                # a string two countries share goes to an allowed one: a stray posting costs less than a lost one
                if w and (w not in table or (country in allowed and table[w] not in allowed)):
                    table[w] = country
    alt = lambda words: "|".join(re.escape(w) for w in sorted(words, key=lambda w: (-len(w), w)))   # longest first: 'new mexico' before 'mexico'
    found = set(tables["names"]) | set(tables["places"])
    seps = [fold(s) for s in rule.get("separators") or []]
    work = [fold(w) for w in rule.get("workplace_words") or []]
    compiled = {"allowed": allowed, **tables, "seps": seps,
                "words": re.compile(r"(?<![a-z0-9])(?:" + alt(found) + r")(?![a-z0-9])") if found else None,
                "codes_rx": re.compile(r"(?:,|-|\()\s*(" + alt(tables["codes"]) + r")\s*(?=$|[,\-()])") if tables["codes"] else None,
                "work_rx": re.compile(r"(?<![a-z0-9])(?:" + alt(work) + r")(?![a-z0-9])") if work else None}
    _PLACES[id(rule)] = (rule, compiled)
    return compiled


def _one_place(seg, t):
    """One place ('Austin, TX') -> ('allowed' | 'outside', [countries]), or ('workplace' | 'unnamed', []).
    Evidence in this order: a country's own name, then a state or province code after a comma ('Athens, GA' is Georgia,
    USA), then a city or region. A name that a US town shares ('Lebanon, PA') sits among the cities, so the code beats it."""
    hits = [m.group(0) for m in t["words"].finditer(seg)] if t["words"] else []
    named = [t["names"][h] for h in hits if h in t["names"]]
    if not named:
        m = t["codes_rx"].search(seg) if t["codes_rx"] else None
        named = [t["codes"][m.group(1)]] if m else [t["places"][h] for h in hits if h in t["places"]]
    if named:
        ok = sorted({c for c in named if c in t["allowed"]})
        return ("allowed", ok) if ok else ("outside", sorted(set(named)))
    rest = t["work_rx"].sub(" ", seg) if t["work_rx"] else seg
    return ("workplace", []) if not re.sub(r"[^a-z]+", "", rest) else ("unnamed", [])


def where(location_text, rule):
    """Which countries a location line names. A posting in several places is allowed if ANY of them is; a line that
    names no country at all ('Remote') is 'unnamed', and so is a mix of one foreign place and one that cannot be read.
    -> {"decision": "allowed" | "outside" | "unnamed", "countries": [...]}"""
    t = places_of(rule)
    s = fold(location_text)
    for sep in t["seps"]:
        s = s.replace(sep, "\n")
    ok, out, unnamed = set(), set(), False
    for seg in (x.strip() for x in s.split("\n")):
        if not seg:
            continue
        kind, cs = _one_place(seg, t)
        if kind == "allowed":
            ok.update(cs)
        elif kind == "outside":
            out.update(cs)
        elif kind == "unnamed":
            unnamed = True
    if ok:
        return {"decision": "allowed", "countries": sorted(ok)}
    return {"decision": "outside" if out and not unnamed else "unnamed", "countries": sorted(out)}


def k12_hits(title, body, rule):
    """Phrases of k12_rule found in the title (and, if the rule lists any, the body)."""
    dash = lambda s: re.sub("[‐-―−]", "-", s.lower())      # 'K–12' with an en dash is still K-12
    t, b = dash(title), dash(body)
    return {"title": [p for p in rule.get("title_phrases") or [] if word_in(p.lower(), t)],
            "body": [p for p in rule.get("body_phrases") or [] if word_in(p.lower(), b)]}


def judge(v, kw):
    """Keep on a role word in the title, >=N topic words in the body, materials evidence, or connector evidence.
    A posting the keywords would keep is still rejected, with the reason, if its place names no allowed country
    (location_rule) or it is a K-12 role (k12_rule). Both gates read only the rules file."""
    ignore = {w.lower() for w in (kw.get("ignore_words_by_company") or {}).get(v["company"], [])}
    tl, bl = v["title"].lower(), v["text"].lower()
    role = [w for w in kw["role_title"] if w.lower() not in ignore and word_in(w, tl)]
    topic = [w for w in kw["topic_text"] if w.lower() not in ignore and word_in(w, bl)]
    flex = [w for w in kw["flex_text"] if word_in(w, bl)]
    need = kw["keep_rule"]["topic_text_min_if_no_title_match"]
    mats = materials_evidence(bl, kw)
    conn = connector_evidence(tl, bl, kw)
    if role:
        why = "role word in title"
    elif len(topic) >= need:
        why = f"{len(topic)} topic words in body (>= {need})"
    elif mats:
        why = "body says it produces teaching materials for a named audience"
    elif conn:
        why = "account or partnership role whose body names higher education"
    else:
        return None, ("no-keyword-match" if not (role or topic) else
                      f"only {len(topic)} topic words, no role word in title")
    blocked, place = [], None
    loc_rule = kw.get("location_rule")
    if loc_rule:
        w = where(v.get("location_text") or "", loc_rule)
        if w["decision"] == "outside":
            blocked.append("country not allowed: " + ", ".join(w["countries"]))
        elif w["decision"] == "unnamed" and loc_rule.get("if_no_country_named", "keep") == "reject":
            blocked.append("no country named in the location")
        elif w["decision"] == "unnamed":
            place = {"country_named": False, "countries_seen": w["countries"],
                     "kept_because": "the location names no country, so the rule keeps it (if_no_country_named)"}
    k12_rule = kw.get("k12_rule")
    if k12_rule:
        h = k12_hits(v["title"], v["text"], k12_rule)
        if h["title"] or h["body"]:
            blocked.append("K-12 role: " + " and ".join(
                [f"'{p}' in the title" for p in h["title"][:2]] + [f"'{p}' in the body" for p in h["body"][:2]]))
    if blocked:
        return None, "; ".join(blocked)
    return {"role_title": role, "topic_text": topic, "flex_text": flex, "materials": mats, "connector": conn,
            "kept_because": why, "title_only": bool(role and not topic), "location": place}, None


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
    ap.add_argument("--sources", default=lp.config("sources.json"))
    ap.add_argument("--keywords", default=lp.config("keywords.json"))
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
                                               "location_text", "department", "date_posted", "date_raw", "job_ref")}
                            | {"kept": bool(r.get("matched")), "reject_reason": r.get("reject_reason")}
                            for r in all_recs]})
    write_csv(os.path.join(a.out, f"all-jobs-{TODAY}.csv"), rows_for_csv(all_recs, with_match=False))

    # JOBS OF INTEREST — the kept postings, with matched words and the source's own record
    write_json(os.path.join(a.out, f"jobs-of-interest-{TODAY}.json"),
               {**meta, "note": "Postings kept by keywords.json. `matched` is Lectern's; `original` is the "
                                "source's own record with its own field names, unmodified.",
                "records": [{k: r[k] for k in ("source", "company", "source_id", "title", "url",
                                               "location_text", "department", "date_posted", "date_raw", "job_ref",
                                               "matched", "text", "original")} for r in kept]})
    write_csv(os.path.join(a.out, f"jobs-of-interest-{TODAY}.csv"), rows_for_csv(kept, with_match=True))

    print(f"\nfetched {len(views)} · unique {len(all_recs)} · kept {len(kept)} · rejected {sum(rejects.values())}")
    print(f"  all-jobs-{TODAY}.json/.csv · jobs-of-interest-{TODAY}.json/.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
