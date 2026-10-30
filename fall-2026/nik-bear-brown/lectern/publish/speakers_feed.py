#!/usr/bin/env python3
"""speakers_feed.py — companies whose people may give an online talk about their MCP, for a Discord channel (#speakers), DRY RUN.

    python3 speakers_feed.py                       # DRY RUN (the default) on the newest runs/*/speakers-leads-*.json: counts, a sample, what is held back
    python3 speakers_feed.py --read                # first build the leads file from config/targets.json (--check-links also re-reads every link)
    python3 speakers_feed.py --jobs PATH           # a particular leads file
    python3 speakers_feed.py --baseline            # remember today's matches as already posted, send nothing
    python3 speakers_feed.py --send                # post the new ones; refuses unless keywords.json speakers_rule.posting is "on"

Professor Bear, 2026-10-30: a search for speakers, 'the evangelist type people in a company who are willing to come and give an
online talk about using their MCP'. Nothing is posted and nothing is sent to anyone until he says go: the locks are the other
channels', written once in channel_feed.py: the rules say "posting": "off"; --send is needed; a first send with no memory of earlier
posts needs --post-all (or --baseline first); ids Discord accepted are remembered in runs/posted-speakers-to-discord.json.

The unit is a COMPANY (the judge is collect/speakers_judge.py, the rules keywords.json `speakers_rule`). A post carries the company,
its MCP, the link to the company's own page for it, the score and the link to the public route the company publishes for developer
relations or community. It NEVER carries a person's name: people are found and kept in the local, untracked speaker-records/, and
Professor Bear decides whom to approach, by hand. No email address or phone number is ever stored or posted, and the safety check in
notify.post() refuses a message that holds one. Run it in ONE place.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import glob, os

import channel_feed
import speakers_collect
import speakers_judge as sj

CHANNEL = "speakers"
STATE = os.path.join(lp.RUNS, "posted-speakers-to-discord.json")
FOOTER = ("Company, MCP and links only, each from the company's own public pages; no person is named here. The score counts sourced signals "
          "(a public MCP page, a DevRel team, past talks, a public route); it says how likely a company is to send someone, not that anyone agreed. "
          "A person decides; the machine only ranks words.")


def row_text(v, r):
    status = f", {r['mcp_status']}" if r.get("mcp_status") else ""
    route = r.get("route") or {}
    return (f"**{v['company']}**: {v['title'][:80]}{status} · score {r['score']} · MCP page {v['url']}"
            + (f" · public route ({route['kind']}) {route['url']}" if route.get("url") else ""))


def judge_all(rows, kw):
    return [(v, sj.judge_speaker(v, rec, kw)) for v, rec in rows]


def newest_leads():
    found = sorted(glob.glob(os.path.join(lp.RUNS, "*", "speakers-leads-*.json")))
    return found[-1] if found else None


def _prepare(a):
    """--jobs wins; --read builds today's leads file from targets.json first; otherwise the newest saved file."""
    if a.read:
        args = (["--targets", a.targets] if a.targets else []) + (["--check"] if a.check_links else [])
        if speakers_collect.main(args) != 0:
            return None
        return newest_leads()
    return a.jobs or newest_leads()


def _summary(judged, dec, a, kw):
    posts = sorted([(r["score"], v["company"]) for v, r in judged if r["decision"] == "post"], reverse=True)
    top = ", ".join(f"{c} {s}" for s, c in posts[:8]) or "none"
    return [f"posts by score: {top}", f"min_score {kw['speakers_rule']['min_score']}; the score is the sum of sourced signals (collect/speakers_judge.py)"]


SPEC = {"name": "speakers", "rule_key": "speakers_rule", "channel": CHANNEL, "state": STATE, "prefix": "Speakers: ", "footer": FOOTER, "group": False,
        "jobs_help": "a speakers-leads-DATE.json from speakers_collect.py (default: the newest runs/*/speakers-leads-*.json)",
        "load": sj.load_postings, "decisions": ("post", "unstated", "not-mcp", "rejected"),
        "title": lambda n: f"{n} new speaker leads (companies with an MCP)", "row_text": row_text,
        "judge_all": lambda rows, kw, a: judge_all(rows, kw), "summary_lines": _summary, "prepare": _prepare,
        "extra_args": lambda ap: (ap.add_argument("--read", action="store_true", help="first build the leads file from config/targets.json"),
                                  ap.add_argument("--check-links", action="store_true", help="with --read: also re-read every link once (robots.txt first)"))}


def build_messages(rows):
    return channel_feed.build_messages(rows, SPEC)


def main(argv=None):
    return channel_feed.run(SPEC, argv, description=__doc__)


if __name__ == "__main__":
    raise SystemExit(main())
