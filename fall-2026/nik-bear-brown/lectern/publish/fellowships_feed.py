#!/usr/bin/env python3
"""fellowships_feed.py — research fellowships and residencies that are still open, for the Discord channel #professor-bear.

    python3 fellowships_feed.py                       # DRY RUN (the default) on the newest runs/*/fellowships-*.json: counts, a sample, what is held back
    python3 fellowships_feed.py --read                # first read the program pages (one robots.txt and one page each), then the dry run
    python3 fellowships_feed.py --jobs PATH           # a particular fellowships file
    python3 fellowships_feed.py --baseline            # remember today's matches as already posted, send nothing
    python3 fellowships_feed.py --send                # post the new ones; refuses unless keywords.json fellowships_rule.posting is "on"

Professor Bear, 2026-11-05: 'Add AI fellowships to my job search', then 'Research only, #professor-bear'. Posting stays OFF until he says
go. The locks are the other channels', written once in channel_feed.py: the rules say "posting": "off"; --send is needed; a first send with no
memory of earlier posts needs --post-all (or --baseline first); ids Discord accepted are remembered in runs/posted-fellowships-to-discord.json.
An id holds the program and its deadline, so a program whose deadline moves is posted again, and one that is unchanged is not.

Where the programs come from: collect/fellowships_collect.py reads the program pages of the programs in config/targets.json (section
`fellowships`, status `active`). What is judged, and why, is collect/fellowships_judge.py and keywords.json `fellowships_rule`. Only the program's
name, organization, place, kind, deadline and link are posted; eligibility and pay are the program's own words and are not checked. Run it in ONE
place: if a server posts to this channel, never post from a laptop.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import datetime as dt, glob, json, os

import channel_feed
import fellowships_collect
import fellowships_judge as fj

CHANNEL = "professor-bear"
STATE = os.path.join(lp.RUNS, "posted-fellowships-to-discord.json")
FOOTER = ("Name, organization, place and deadline come from each program's own public page, or are marked 'as listed' when a person recorded the date. "
          "Eligibility and pay are the program's words and are not checked. Nothing is sent to a program. A person decides; the machine only ranks words.")


def _date(iso):
    d = dt.date.fromisoformat(iso)
    return f"{d.strftime('%b')} {d.day}, {d.year}"


def row_text(v, r):
    basis = "" if v.get("deadline_basis") == "page" else " as listed"
    where = (v.get("location_text") or "").split(";")[0][:50]
    return (f"**{v['company']}**: {v['title']} · {v['kind'].replace('-', ' ')} · deadline {_date(v['deadline'])}{basis}"
            + (f" · {where}" if where else "") + f" {v['url']}")


def load(path):
    with open(path, encoding="utf-8") as f:
        doc = json.load(f)
    return doc["records"] if isinstance(doc, dict) else doc


def newest():
    found = sorted(glob.glob(os.path.join(lp.RUNS, "*", "fellowships-*.json")))
    return found[-1] if found else None


def _prepare(a):
    if a.read:
        if fellowships_collect.main(["--targets", a.targets] if a.targets else []) != 0:
            return None
        return newest()
    return a.jobs or newest()


def _summary(judged, dec, a, kw):
    return [f"{v['title']}: {r['decision']} · {r['reason']}" for v, r in judged]


SPEC = {"name": "fellowships", "rule_key": "fellowships_rule", "channel": CHANNEL, "state": STATE, "prefix": "Fellowships: ", "footer": FOOTER, "group": False,
        "jobs_help": "a fellowships-DATE.json from fellowships_collect.py (default: the newest runs/*/fellowships-*.json)",
        "load": load, "decisions": ("post", "closed", "no-deadline", "not-research"),
        "title": lambda n: f"{n} open research fellowship{'s' if n != 1 else ''} and residenc{'ies' if n != 1 else 'y'}", "row_text": row_text,
        "judge_all": lambda views, kw, a: [(v, fj.judge_fellowship(v, kw)) for v in views], "summary_lines": _summary, "prepare": _prepare,
        "extra_args": lambda ap: ap.add_argument("--read", action="store_true", help="first read the program pages (one robots.txt and one page each)")}


def build_messages(rows):
    return channel_feed.build_messages(rows, SPEC)


def main(argv=None):
    return channel_feed.run(SPEC, argv, description=__doc__)


if __name__ == "__main__":
    raise SystemExit(main())
