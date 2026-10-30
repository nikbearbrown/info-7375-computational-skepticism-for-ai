#!/usr/bin/env python3
"""speakers_collect.py — turn the `speakers` section of config/targets.json into a leads file, and (with --check) re-read every link.

    python3 speakers_collect.py [--out runs/DATE] [--check] [--people]

The companies are the `speakers` section of config/targets.json (one list, Rule 7). Each carries its MCP (name, primary source) and
its sourced signals: the company's own MCP docs page, a DevRel team page, talks about the MCP, a community channel, and the public
contact route the company itself publishes. The research that filled it is a person's (or an agent's) reading; this script is what
checks it again:

  --check    fetch every link of every company with status `active` or `unchecked`, ONE request per link: robots.txt first, an honest
             User-Agent, a pause between requests, an error page never parsed. It records the HTTP status and whether the page's
             text mentions MCP or the Model Context Protocol (a JavaScript-only page can answer 200 and show neither: that is
             recorded as 'term not seen', not as a failure). The judge then counts a signal only if its link answered 2xx.
  --people   read the LOCAL speaker-records/ (never tracked: it names people) and fetch each person's source page once, to see
             whether the page mentions the person's surname. Writes speaker-records/people-check-<date>.json and prints counts only.
             It also compares each company's people_found with the number of people in the records whose source page the researcher opened.

Nothing is sent to anyone, no form is filled, and no email address or phone number is read, kept or guessed.

Writes: <out>/speakers-leads-<date>.json   every company on the list, in the shape publish/speakers_feed.py and the judge read
Exit 0 ran, 2 bad input.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, datetime as dt, glob, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request, urllib.robotparser

import collect

USER_AGENT = "lectern-speakers/0.1 (course project; reads public pages once to check a link)"
PAUSE = 1.5
MCP_TERM = re.compile(r"\bmcp\b|model context protocol", re.I)
RECORDS = os.path.join(lp.ROOT, "speaker-records")          # local, gitignored: it names people


def local_signals(folder=RECORDS):
    """{company_id: [signal]} from speaker-records/signals-*.jsonl: signals whose link or title carries a person's name, kept out of the
    public targets.json and merged into the leads file here (which is not tracked). {} if the folder does not exist."""
    out = {}
    for p in sorted(glob.glob(os.path.join(folder, "signals-*.jsonl"))):
        with open(p, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    out.setdefault(r["company_id"], []).append({k: v for k, v in r.items() if k not in ("company_id", "company")})
    return out


def leads_from_targets(doc, local=None):
    """[lead record] for every company of the `speakers` section. Names of people are never in targets.json; `local` is local_signals()."""
    local = local or {}
    out = []
    for t in doc["targets"]:
        if t.get("section") != "speakers":
            continue
        s = t["speakers"]
        out.append({"id": t["id"], "company": t["name"], "verdict": s["verdict"], "status": t["status"], "why": t["why"],
                    "product": s.get("product", ""), "mcp": s.get("mcp") or {}, "todo": t.get("todo", ""),
                    "signals": (s.get("signals") or []) + [x for x in local.get(t["id"], []) if x.get("kind") != "contact_route"],
                    "people_found": s.get("people_found", 0), "contact_route": s.get("contact_route") or {}, "researched": s.get("researched", "")})
        for x in local.get(t["id"], []):
            if x.get("kind") == "contact_route" and not out[-1]["contact_route"]:
                out[-1]["contact_route"] = {"kind": x.get("route_kind", ""), "url": x["url"], "opened": x.get("opened", False)}
    return out


def urls_of(rec):
    urls = [(rec.get("mcp") or {}).get("primary_source")] + [s.get("url") for s in rec.get("signals") or []] + [(rec.get("contact_route") or {}).get("url")]
    return list(dict.fromkeys(u for u in urls if u))


class Reader:
    """One polite fetcher: honest User-Agent, robots.txt first, a pause between requests, errors never parsed."""
    def __init__(self, delay=PAUSE, opener=None, sleep=time.sleep):
        self.delay, self.robots, self.last, self.open, self.sleep = delay, {}, 0.0, opener or urllib.request.urlopen, sleep

    def allowed(self, url):
        p = urllib.parse.urlparse(url)
        key = f"{p.scheme}://{p.netloc}"
        if key not in self.robots:
            rp = urllib.robotparser.RobotFileParser()
            try:
                with self.open(urllib.request.Request(key + "/robots.txt", headers={"User-Agent": USER_AGENT}), timeout=15) as r:
                    rp.parse(r.read().decode("utf-8", "replace").splitlines())
            except urllib.error.HTTPError as e:
                rp.parse([] if e.code in (404, 410) else ["User-agent: *", "Disallow: /"])      # no file: allowed; blocked or unreadable: not
            except Exception:
                rp.parse(["User-agent: *", "Disallow: /"])
            self.robots[key] = rp
        return self.robots[key].can_fetch(USER_AGENT, url)

    def get(self, url):
        """-> (status, text). status is 'robots' if disallowed, 'error' on a failure; text only for 2xx HTML."""
        if not url.startswith("https://"):
            return "refused", ""
        if not self.allowed(url):
            return "robots", ""
        wait = self.delay - (time.time() - self.last)
        if wait > 0:
            self.sleep(wait)
        self.last = time.time()
        try:
            with self.open(urllib.request.Request(url, headers={"User-Agent": USER_AGENT}), timeout=25) as r:
                if "html" not in (r.headers.get("Content-Type", "") or "").lower():
                    return str(r.status), ""
                return str(r.status), r.read(2_000_000).decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            return str(e.code), ""
        except Exception:
            return "error", ""


def check_urls(urls, reader):
    """{url: {status, term}}: the HTTP status, and whether MCP / Model Context Protocol appears in the page text ('' if no text was read)."""
    out = {}
    for u in urls:
        status, text = reader.get(u)
        out[u] = {"status": status, "term": bool(MCP_TERM.search(text)) if text else None}
    return out


def read_records(folder=RECORDS):
    """The local people records -> [dict]. One JSON object per line, in speaker-records/people-*.jsonl."""
    recs = []
    for p in sorted(glob.glob(os.path.join(folder, "people-*.jsonl"))):
        with open(p, encoding="utf-8") as f:
            recs += [json.loads(l) for l in f if l.strip()]
    return recs


def surname_seen(name, text):
    """Does the page mention the person's surname (the last word of the name)? A weak check on purpose: it says 'seen' or 'not seen'."""
    last = re.sub(r"[^\w\-']", "", (name or "").split()[-1]) if (name or "").split() else ""
    return bool(last) and bool(re.search(r"(?<!\w)" + re.escape(last) + r"(?!\w)", text, re.I))


def check_people(people, reader):
    """[{company_id, source_url, status, surname_seen}] — no names in the output."""
    cache, out = {}, []
    for p in people:
        u = p.get("source_url") or ""
        if u not in cache:
            cache[u] = reader.get(u)
        status, text = cache[u]
        out.append({"company_id": p.get("company_id"), "source_url": u, "status": status, "surname_seen": surname_seen(p.get("name"), text) if text else None})
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--targets", default=lp.config("targets.json"))
    ap.add_argument("--out", default=None, help="default runs/<today>")
    ap.add_argument("--check", action="store_true", help="re-read every link once (robots.txt first)")
    ap.add_argument("--people", action="store_true", help="re-read the source page of each person in the local speaker-records/")
    ap.add_argument("--people-only", action="store_true", help="with --people: check the people and leave the leads file as it is")
    ap.add_argument("--records", default=RECORDS, help="the local folder of people records and withheld signals (default speaker-records/)")
    a = ap.parse_args(argv)
    today = dt.date.today().isoformat()
    out = a.out or os.path.join(lp.RUNS, today)
    try:
        with open(a.targets, encoding="utf-8") as f:
            leads = leads_from_targets(json.load(f), local_signals(a.records))
    except (OSError, json.JSONDecodeError, KeyError) as e:
        print(f"INPUT ERROR: {e}", file=sys.stderr)
        return 2
    if not leads:
        print("INPUT ERROR: config/targets.json has no `speakers` section", file=sys.stderr)
        return 2
    reader = Reader()
    if a.check:
        todo = [r for r in leads if r["status"] in ("active", "unchecked")]
        for i, r in enumerate(todo):
            r["checks"] = check_urls(urls_of(r), reader)
            bad = [u for u, c in r["checks"].items() if not str(c["status"]).startswith("2")]
            print(f"  {r['company']:24} {len(r['checks']):2} links, {len(bad)} not 2xx" + (f" ({', '.join(str(r['checks'][u]['status']) for u in bad)})" if bad else ""))
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, f"speakers-leads-{today}.json")
    if not a.people_only:
        collect.write_json(path, {"tool": "lectern speakers_collect", "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                                  "note": "Every company on the speakers list with its sourced signals. Links re-checked: " + ("yes" if a.check else "no") + ". No person is named here.",
                                  "records": leads})
        print(f"{len(leads)} companies -> {os.path.basename(path)}" + ("" if a.check else " (links not re-checked; add --check)"))
    if a.people:
        people = read_records(a.records)
        res = check_people(people, reader)
        os.makedirs(a.records, exist_ok=True)
        collect.write_json(os.path.join(a.records, f"people-check-{today}.json"), {"generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "checks": res})
        seen = sum(1 for r in res if r["surname_seen"])
        print(f"people: {len(people)} records; source page answered 2xx for {sum(1 for r in res if str(r['status']).startswith('2'))}; surname seen on the page for {seen}")
        counts = {}
        for p in people:                                                  # people_found counts only people whose source page the researcher opened
            if p.get("opened"):
                counts[p.get("company_id")] = counts.get(p.get("company_id"), 0) + 1
        for r in leads:
            if (r["people_found"] or 0) != counts.get(r["id"], 0):
                print(f"  MISMATCH {r['company']}: targets.json says people_found={r['people_found']}, records hold {counts.get(r['id'], 0)} opened")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
