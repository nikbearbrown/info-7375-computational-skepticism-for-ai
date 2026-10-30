#!/usr/bin/env python3
"""faculty_feed.py: find new business-school faculty listings that mention AI.

What it is: a daily reader for the Chronicle of Higher Education and Inside Higher Ed keyword
RSS feeds. Why: universities do not use the job systems collect.py already reads (Greenhouse,
Ashby, SmartRecruiters), but these two feeds return listings to a plain request, with no login,
and cover every school at once. What it does: runs a set of AI queries plus one query per watched
school (faculty_config.json), keeps the listings that look like faculty or institute-leadership
roles at a business school (or a watched school) with AI in the text, records each with the rule
that fired and the words that matched, saves only the NEW ones (not seen on an earlier run), and
posts a short summary to the Discord channel named in the config (a public channel, by design).

Run from this folder:  python3 faculty_feed.py [--send] [--max-pages N] [--limit-queries N] [--no-save]
Without --send nothing is posted. Writes faculty-runs/: new/new-<date>.json + .md, state/seen.json, run-log.md.
The webhook is a secret kept in the home folder (~/.discord-webhooks/<channel>, mode 600; the channel
professor-bear also falls back to ~/.lectern-webhook). It is never read from, or written to, this repo.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, html, json, os, re, sys, time, urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

HERE = lp.ROOT
CFG = json.load(open(lp.config("faculty_config.json"), encoding="utf-8"))
RUNS = lp.FACULTY_RUNS  # run outputs belong to the class that runs it; never synced

AI_STRONG = re.compile(r"\bartificial intelligence\b|\bmachine learning\b|\bgenerative ai\b|\bgen-?ai\b|\bAI\b|\bLLMs?\b|\blarge language models?\b|\bdeep learning\b|\bAI-[a-z]+", re.I)
AI_STRONG_CASE = re.compile(r"\bAI\b")  # "AI" alone must be upper-case ("ai" is noise)
AI_WEAK = re.compile(r"\bbusiness analytics\b|\bdata science\b|\banalytics\b|\bdecision sciences?\b|\binformation systems?\b|\btechnology management\b", re.I)
BUSINESS = re.compile(r"\bbusiness\b|\bmanagement\b|\bmba\b|\bfinance\b|\baccounting\b|\bmarketing\b|\boperations\b|\binformation systems?\b|\bentrepreneur\w*\b|\bdecision sciences?\b|\bsupply chain\b|\borganizational behavior\b|\beconomics\b", re.I)
FACULTY = re.compile(r"\bprofessors?\b|\blecturers?\b|\bfaculty\b|\binstructors?\b|\bclinical\b|\bprofessor of practice\b", re.I)
LEADERSHIP = re.compile(r"\bchair\b|\bdirector\b|\bhead of\b|\bresearch (scientist|fellow|associate)\b", re.I)
NOT_FACULTY = re.compile(r"\b(engineer|developer|technician|coordinator|recruiter|assistant to|administrative|nurse|librarian|programmer|architect|manager|specialist|analyst|administrator|assistant director|associate director|executive assistant)\b", re.I)


def get(url, delay):
    req = urllib.request.Request(url, headers={"User-Agent": CFG["user_agent"]})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read()
        time.sleep(delay)
        return body, None
    except (urllib.error.URLError, TimeoutError) as e:
        time.sleep(delay)
        return None, f"{type(e).__name__}: {e}"


def parse_feed(body):
    root = ET.fromstring(body)
    ch = root.find("channel")
    out = []
    for it in ch.findall("item"):
        link = (it.findtext("link") or "").strip()
        m = re.search(r"/job/(\d+)/", link)
        desc = html.unescape(re.sub(r"<[^>]+>", " ", it.findtext("description") or ""))
        out.append({"id": m.group(1) if m else link, "title": (it.findtext("title") or "").strip(),
                    "link": link.split("?")[0], "pubDate": it.findtext("pubDate") or "", "snippet": re.sub(r"\s+", " ", desc).strip()[:600]})
    return out


def institution(title):
    return title.split(":", 1)[0].strip() if ":" in title else ""


def classify(item):
    """Return (tier, why) or None. Tiers: A business+AI faculty/leadership; B watched school + AI (school unconfirmed); C watched school + business + analytics only."""
    title = item["title"]
    role = title.split(":", 1)[-1]
    text = role + " " + item["snippet"]
    inst = institution(title).lower()
    watched = next((k for k, v in CFG["watch_schools"].items() if any(a == inst or a in inst for a in v["aliases"])), None)
    ai_words = sorted({m.group(0).lower() if m.group(0) != "AI" else "AI" for m in AI_STRONG.finditer(text) if m.group(0).lower() != "ai" or AI_STRONG_CASE.fullmatch(m.group(0))})
    weak_words = sorted({m.group(0).lower() for m in AI_WEAK.finditer(text)})
    biz_words = sorted({m.group(0).lower() for m in BUSINESS.finditer(text)})
    fac = bool(FACULTY.search(role)) or bool(FACULTY.search(item["snippet"][:200]) and FACULTY.search(role))
    lead = bool(LEADERSHIP.search(role))
    if NOT_FACULTY.search(role) and not FACULTY.search(role):
        return None
    if not (fac or lead):
        return None
    if ai_words and biz_words:
        return "A", {"school": watched, "ai": ai_words, "business": biz_words, "role_kind": "faculty" if fac else "leadership"}
    if watched and ai_words:
        return "B", {"school": watched, "ai": ai_words, "business": biz_words, "role_kind": "faculty" if fac else "leadership"}
    if watched and biz_words and weak_words:
        return "C", {"school": watched, "ai": weak_words, "business": biz_words, "role_kind": "faculty" if fac else "leadership"}
    return None


def run(args):
    today = datetime.now().strftime("%Y-%m-%d")
    delay = CFG["delay_seconds"]
    queries = []
    for q in CFG["ai_queries"]:
        queries.append((q, args.max_pages or CFG["ai_query_pages"]))
    for name, v in CFG["watch_schools"].items():
        queries.append((f'"{v["institution"]}" business', args.max_pages or CFG["school_query_pages"]))
    if args.limit_queries:
        queries = queries[:args.limit_queries]
    seen_path = os.path.join(RUNS, "state", "seen.json")
    os.makedirs(os.path.dirname(seen_path), exist_ok=True)
    seen = json.load(open(seen_path)) if os.path.exists(seen_path) else {}
    first_run = not seen
    fetched, errors, found = 0, [], {}
    cutoff = datetime.now(timezone.utc) - timedelta(days=CFG["max_age_days"])
    for feed_name, base in CFG["feeds"].items():
        for q, pages in queries:
            for p in range(1, pages + 1):
                url = f"{base}?keywords={urllib.parse.quote_plus(q)}&countrycode=US" + (f"&page={p}" if p > 1 else "")
                body, err = get(url, delay)
                if err or body is None:
                    errors.append(f"{feed_name} '{q}' p{p}: {err}"); break
                try:
                    items = parse_feed(body)
                except ET.ParseError as e:
                    errors.append(f"{feed_name} '{q}' p{p}: bad XML ({e})"); break
                fetched += len(items)
                for it in items:
                    try:
                        when = parsedate_to_datetime(it["pubDate"])
                        if when.tzinfo is None: when = when.replace(tzinfo=timezone.utc)
                        if when < cutoff: continue
                    except (TypeError, ValueError):
                        pass
                    res = classify(it)
                    if res:
                        found.setdefault(it["id"], {**it, "tier": res[0], "why": res[1], "feed": feed_name})
                if len(items) < 20:
                    break
    new = {k: v for k, v in found.items() if k not in seen}
    for k, v in found.items():
        seen.setdefault(k, {"first_seen": today, "title": v["title"], "tier": v["tier"]})
    if not args.no_save:
        json.dump(seen, open(seen_path, "w"), indent=2, ensure_ascii=False)
    order = {"A": 0, "B": 1, "C": 2}
    rows = sorted(new.values(), key=lambda r: (order[r["tier"]], r["why"]["school"] is None, r["title"]))
    os.makedirs(os.path.join(RUNS, "new"), exist_ok=True)
    if not args.no_save:
        json.dump({"date": today, "queries": len(queries), "items_fetched": fetched, "matched_total": len(found), "new": rows, "errors": errors},
                  open(os.path.join(RUNS, "new", f"new-{today}.json"), "w"), indent=2, ensure_ascii=False)
        with open(os.path.join(RUNS, "new", f"new-{today}.md"), "w", encoding="utf-8") as f:
            f.write(render_md(rows, today, fetched, len(found), errors))
        with open(os.path.join(RUNS, "run-log.md"), "a", encoding="utf-8") as f:
            f.write(f"- {today}: {len(queries)} queries x {len(CFG['feeds'])} feeds, {fetched} items read, {len(found)} matched, {len(rows)} new, {len(errors)} errors{' (first run: everything counts as new)' if first_run else ''}.\n")
    return rows, errors, fetched, len(found), first_run


TIER_NAME = {"A": "Business wording + AI", "B": "Watched school + AI (school unit not confirmed)", "C": "Watched school + business + analytics only"}


def render_md(rows, today, fetched, matched, errors):
    out = [f"# Faculty listings that mention AI: new on {today}\n", f"{len(rows)} new of {matched} matched ({fetched} feed items read). Private file.\n"]
    for t in "ABC":
        grp = [r for r in rows if r["tier"] == t]
        if not grp: continue
        out.append(f"\n## Tier {t}: {TIER_NAME[t]} ({len(grp)})\n")
        for r in grp:
            star = f" ★ watched: {r['why']['school']}" if r["why"]["school"] else ""
            out.append(f"- **{r['title']}**{star}\n  posted {r['pubDate'][:16]} · matched AI words: {', '.join(r['why']['ai'])} · business words: {', '.join(r['why']['business']) or 'none'} · {r['feed']}\n  {r['link']}\n")
    if errors:
        out.append("\n## Feed errors\n" + "\n".join(f"- {e}" for e in errors) + "\n")
    return "".join(out)


def webhook_url(channel):
    home = os.path.expanduser("~")
    paths = [os.path.join(home, ".discord-webhooks", channel)] + ([os.path.join(home, ".lectern-webhook")] if channel == "professor-bear" else [])
    for p in paths:
        if os.path.isfile(p):
            if os.stat(p).st_mode & 0o077:
                sys.exit(f"refusing: {os.path.basename(p)} is readable by others; chmod 600 it")
            url = "".join(open(p).read().split())
            if re.fullmatch(r"https://(discord|discordapp)\.com/api/webhooks/\d+/[\w-]+", url):
                return url
            sys.exit(f"{os.path.basename(p)} does not hold a Discord webhook URL")
    sys.exit(f"no webhook saved for channel '{channel}'")


def discord(channel, title, text, send):
    """Post one embed. Refuses text with a local path, an email address or a webhook URL (the channel is public)."""
    if re.search(r"/[U]sers/|/home/\w+|[\w.+-]+@[\w-]+\.[\w.]+|discord(app)?\.com/api/webhooks", title + text):
        print("NOT SENT: text contains a local path, email address or webhook URL"); return
    body = f"**Jobs: {title}**\n{text}"       # plain text, not an embed: with embeds switched off in Discord an embed-only post looks empty
    payload = {"username": "Professor Bear", "content": body if len(body) <= 2000 else body[:1990].rstrip() + "\n…", "flags": 4}
    if not send:
        print(f"DRY RUN, #{channel}, nothing sent: {title} ({len(text)} chars)"); return
    req = urllib.request.Request(webhook_url(channel), data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json", "User-Agent": "lectern-faculty-feed/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            print(f"posted to #{channel}: HTTP {r.status}")
    except urllib.error.HTTPError as e:
        print(f"Discord refused it: HTTP {e.code}")


def post_summary(rows, errors, fetched, matched, send):
    msgs = []
    if rows:
        lines = []
        for r in rows[:25]:
            star = "★ " if r["why"]["school"] else ""
            lines.append(f"[{r['tier']}] {star}{r['title'][:110]} ({', '.join(r['why']['ai'][:3])}) {r['link']}")
        chunk, size = [], 0
        for ln in lines:
            if size + len(ln) > 1300 and chunk:
                msgs.append("\n".join(chunk)); chunk, size = [], 0
            chunk.append(ln); size += len(ln) + 1
        if chunk: msgs.append("\n".join(chunk))
        title = f"{len(rows)} new faculty listings mentioning AI"
    else:
        title = None
    if errors and (fetched == 0 or len(errors) > 5):
        msgs.append(f"Feed problem: {len(errors)} requests failed and {fetched} items were read. First error: {errors[0][:200]}")
        title = title or "Faculty feed problem"
    if not msgs:
        print("Nothing new, nothing to post."); return
    for i, m in enumerate(msgs):
        discord(CFG["discord_channel"], (title or "Faculty feed") + (f" ({i+1}/{len(msgs)})" if len(msgs) > 1 else ""), m, send)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--send", action="store_true", help="post the private Discord summary (default: dry run)")
    ap.add_argument("--max-pages", type=int, help="override pages per query (testing)")
    ap.add_argument("--limit-queries", type=int, help="only the first N queries (testing)")
    ap.add_argument("--resend", metavar="NEW_JSON", help="post the listings in an earlier new/*.json file (testing the alert path); fetches nothing")
    ap.add_argument("--no-save", action="store_true", help="do not write state or output files (testing)")
    a = ap.parse_args()
    if a.resend:
        d = json.load(open(a.resend, encoding="utf-8"))
        post_summary(d["new"], d.get("errors", []), d["items_fetched"], d["matched_total"], a.send)
        sys.exit(0)
    rows, errors, fetched, matched, first = run(a)
    if a.no_save:
        for r in rows: print(f"  [{r['tier']}] {r['title'][:100]} | {r['why']['role_kind']} | ai={r['why']['ai'][:3]} biz={r['why']['business'][:3]} school={r['why']['school']}")
    print(f"{fetched} items read, {matched} matched, {len(rows)} new, {len(errors)} errors" + (" (first run)" if first else ""))
    post_summary(rows, errors, fetched, matched, a.send)
