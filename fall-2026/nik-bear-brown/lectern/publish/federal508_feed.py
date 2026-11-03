#!/usr/bin/env python3
"""federal508_feed.py — federal Section 508 / digital-accessibility listings that are remote or contract, for the Discord channel #federal-508, DRY RUN.

    python3 federal508_feed.py                       # DRY RUN (the default) on the newest runs/*/federal508-jobs-*.json: counts, a sample, what is held back
    python3 federal508_feed.py --read                # first read the employers' boards (one request each), then the dry run
    python3 federal508_feed.py --jobs PATH           # a particular postings file (the ai-jobs jobs.jsonl also works)
    python3 federal508_feed.py --baseline            # remember today's matches as already posted, send nothing
    python3 federal508_feed.py --send                # post the new ones; refuses unless keywords.json federal508_rule.posting is "on"

Professor Bear, 2026-10-31: 'can we have the job search also look for Federal 508 work ... contract work. Or remote work.' Posting stays OFF until he says go.
The locks are the other channels', written once in channel_feed.py: the rules say "posting": "off"; --send is needed; a first send with no memory of
earlier posts needs --post-all (or --baseline first); ids Discord accepted are remembered in runs/posted-federal508-to-discord.json.

Where the postings come from: collect/federal508_collect.py reads the boards of the employers in config/targets.json (section `federal508`, status `active`).
What is judged, and why each posting is or is not posted, is collect/federal508_jobs.py and keywords.json `federal508_rule`. Only the title, employer, place
and link of the employer's own public posting are posted, with flags (remote, contract, clearance named) taken from the title and place. Run it in ONE place.
Sponsorship, pay and the kind of engagement (employee or 1099) are not checked and never claimed. The post carries no person's name.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import collections, glob, json, os

import channel_feed
import federal508_collect
import federal508_jobs as fj

CHANNEL = "federal-508"
STATE = os.path.join(lp.RUNS, "posted-federal508-to-discord.json")
FOOTER = ("Title, employer and link only, from each employer's own public job board. Remote and contract are read from the words in the title and place: open the posting and read it. "
          "A clearance named in a title is flagged, not hidden. Pay and the kind of engagement are not checked. A person decides; the machine only ranks words.")
KIND = {"federal-contractor": "federal contractor", "civic-tech": "civic tech", "accessibility-specialist": "accessibility firm", "agency": "agency"}


def _loc(v):
    return (v["location_text"] or "").split(" | ")[0].split(";")[0].split(" · ")[0]


def _flags(r):
    clr = ([w for w in r["clearance"] if w != "clearance"] or r["clearance"])[:1]          # 'secret' says more than 'clearance'
    f = (["508 named in the ad text, not the title"] if r["hits"] and all(g == "ad-text" for g, _ in r["hits"]) else []) + (["remote"] if r["remote"] else []) + (["contract"] if r["contract"] else []) + ([("clearance named: " + clr[0]) if clr[0] != "clearance" else "clearance named"] if clr else [])
    return " [" + ", ".join(f) + "]" if f else ""


def row_text(v, r):
    loc = _loc(v)[:40]
    kind = KIND.get(r.get("kind") or "")
    return f"**{v['company']}**{' (' + kind + ')' if kind else ''}: {v['title'][:100]}" + (f" · {loc}" if loc else "") + _flags(r) + f" {v['url']}"


def judge_all(views, kw):
    kinds = fj.load_kinds()
    return [(v, fj.judge_federal508(v, kw, kinds)) for v in views]


def wanted(judged, kw):
    return channel_feed.wanted(judged, kw["federal508_rule"])


def newest_postings():
    found = sorted(glob.glob(os.path.join(lp.RUNS, "*", "federal508-jobs-*.json")))
    return found[-1] if found else None


def _prepare(a):
    """--jobs wins; --read reads the boards into today's run folder first; otherwise the newest saved file."""
    if a.read:
        if federal508_collect.main(["--targets", a.targets] if a.targets else []) != 0:
            return None
        return newest_postings()
    return a.jobs or newest_postings()


def _summary(judged, dec, a, kw):
    posts = [(v, r) for v, r in judged if r["decision"] == "post"]
    by = collections.Counter(v["company"] for v, _ in posts)
    both = sum(1 for _, r in posts if r["remote"] and r["contract"])
    only_r = sum(1 for _, r in posts if r["remote"] and not r["contract"])
    only_c = sum(1 for _, r in posts if r["contract"] and not r["remote"])
    clr = sum(1 for _, r in posts if r["clearance"])
    return ["employers with a post: " + (", ".join(f"{c} {n}" for c, n in by.most_common()) or "none"),
            f"engagement words: remote and contract {both}, remote only {only_r}, contract only {only_c}; clearance named in {clr} of the posts"]


SPEC = {"name": "federal508", "rule_key": "federal508_rule", "channel": CHANNEL, "state": STATE, "prefix": "Federal 508: ", "footer": FOOTER, "group": False,
        "jobs_help": "a federal508-jobs-DATE.json from federal508_collect.py, or the ai-jobs jobs.jsonl (default: the newest runs/*/federal508-jobs-*.json)",
        "load": fj.load_postings, "decisions": ("post", "unstated", "not-digital", "rejected", "no-match"),
        "title": lambda n: f"{n} new federal 508 / accessibility listings (remote or contract)", "row_text": row_text,
        "judge_all": lambda views, kw, a: judge_all(views, kw), "summary_lines": _summary, "prepare": _prepare,
        "extra_args": lambda ap: ap.add_argument("--read", action="store_true", help="first read the employers' boards (one request each)")}


def build_messages(rows):
    return channel_feed.build_messages(rows, SPEC)


def main(argv=None):
    return channel_feed.run(SPEC, argv, description=__doc__)


if __name__ == "__main__":
    raise SystemExit(main())
