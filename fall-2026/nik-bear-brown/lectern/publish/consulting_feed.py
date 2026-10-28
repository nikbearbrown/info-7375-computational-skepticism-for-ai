#!/usr/bin/env python3
"""consulting_feed.py — early-career consulting listings, for the Discord channel #consulting-firm.

    python3 consulting_feed.py                       # DRY RUN (the default) on the newest runs/*/consulting-jobs-*.json: counts, a sample, what is held back
    python3 consulting_feed.py --read                # first read the consulting firms' boards (one request each), then the dry run
    python3 consulting_feed.py --jobs PATH           # a particular postings file (the ai-jobs jobs.jsonl also works)
    python3 consulting_feed.py --baseline            # remember today's matches as already posted, send nothing
    python3 consulting_feed.py --send                # post the new ones; refuses unless keywords.json consulting_rule.posting is "on"

Professor Bear, 2026-10-28: 'another search, for consulting jobs', posted to its own channel after Lectern has been through
them, and posting stays OFF until he says go. The locks are the games poster's, written once in channel_feed.py: the rules say
"posting": "off"; --send is needed; a first send with no memory of earlier posts needs --post-all (or --baseline first); ids
Discord accepted are remembered in runs/posted-consulting-to-discord.json, so nothing is posted twice.

Where the postings come from: collect/consulting_collect.py reads the boards of the consulting firms in config/targets.json
(section `consulting`, status `active`) with Lectern's own readers. The ai-jobs snapshot holds one of those firms, so it is not
the source. What is judged, and why each posting is or is not posted, is collect/consulting_jobs.py and keywords.json
`consulting_rule`. Only the title, firm, place and link of the firm's own public posting are posted. Run it in ONE place: if a
server posts to this channel, never post from a laptop. Sponsorship is not checked and is never claimed.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import collections, copy, glob, os

import channel_feed
import consulting_collect
import consulting_jobs as cj

CHANNEL = "consulting-firm"
STATE = os.path.join(lp.RUNS, "posted-consulting-to-discord.json")
FOOTER = ("Title, firm and link only, from each firm's own public job board. Early career is read from the words in the title: open the posting and read it. "
          "Visa sponsorship is not checked. A person decides; the machine only ranks words.")


def _loc(v):
    return (v["location_text"] or "").split(" | ")[0].split(";")[0].split(" · ")[0]


def _words(r):
    return ", ".join(dict.fromkeys([max(r["hits"], key=len)] + r["level_words"][:1])) if r["hits"] else ""


def row_text(v, r):
    loc = _loc(v)[:40]
    return f"**{v['company']}**: {v['title'][:100]}" + (f" · {loc}" if loc else "") + (f" ({_words(r)})" if r["hits"] else "") + f" {v['url']}"


def group_text(items):
    """One role in several cities (Brattle posts each role once per city) -> one line: the cities, and the first posting's link."""
    v, r = items[0]
    cities = list(dict.fromkeys(_loc(x).split(",")[0].strip() for x, _ in items if _loc(x)))
    where = ", ".join(cities[:5]) + (f" +{len(cities) - 5}" if len(cities) > 5 else "")
    return f"**{v['company']}**: {v['title'][:100]}" + (f" · {where}" if where else "") + (f" ({_words(r)})" if r["hits"] else "") + f" {v['url']}"


def judge_all(views, kw):
    return [(v, cj.judge_consulting(v, kw)) for v in views]


def wanted(judged, kw):
    return channel_feed.wanted(judged, kw["consulting_rule"])


def newest_postings():
    found = sorted(glob.glob(os.path.join(lp.RUNS, "*", "consulting-jobs-*.json")))
    return found[-1] if found else None


def _prepare(a):
    """--jobs wins; --read reads the boards into today's run folder first; otherwise the newest saved file."""
    if a.read:
        if consulting_collect.main(["--targets", a.targets] if a.targets else []) != 0:
            return None
        return newest_postings()
    return a.jobs or newest_postings()


def _summary(judged, dec, a, kw):
    posts = [v for v, r in judged if r["decision"] == "post"]
    roles = collections.Counter()
    for v in posts:
        roles[v["company"]] += 1
    distinct = {c: len({v["title"] for v in posts if v["company"] == c}) for c in roles}
    lines = ["firms with a post: " + (", ".join(f"{c} {n} postings ({distinct[c]} roles)" for c, n in roles.most_common()) or "none")]
    nocl = copy.deepcopy(kw)
    nocl["consulting_rule"]["clearance_words"] = []
    cleared = [v for v, r in judged if r["decision"] == "rejected" and "clearance in the title" in r["reason"]]
    would = collections.Counter(cj.judge_consulting(v, nocl)["decision"] for v in cleared)
    lines.append(f"clearance veto: {len(cleared)} titles removed ({would['post']} would have been posted, {would['unstated']} held back)")
    return lines


SPEC = {"name": "consulting", "rule_key": "consulting_rule", "channel": CHANNEL, "state": STATE, "prefix": "Consulting: ", "footer": FOOTER, "group": True,
        "jobs_help": "a consulting-jobs-DATE.json from consulting_collect.py, or the ai-jobs jobs.jsonl (default: the newest runs/*/consulting-jobs-*.json)",
        "load": cj.load_postings, "decisions": ("post", "unstated", "senior-or-mid", "not-consulting", "rejected", "no-match"),
        "title": lambda n: f"{n} new early-career consulting listings", "row_text": row_text, "group_text": group_text,
        "judge_all": lambda views, kw, a: judge_all(views, kw), "summary_lines": _summary, "prepare": _prepare,
        "extra_args": lambda ap: ap.add_argument("--read", action="store_true", help="first read the consulting firms' boards (one request each)")}


def build_messages(rows):
    return channel_feed.build_messages(rows, SPEC)


def main(argv=None):
    return channel_feed.run(SPEC, argv, description=__doc__)


if __name__ == "__main__":
    raise SystemExit(main())
