#!/usr/bin/env python3
"""games_feed.py — early-career game, engine and real-time listings, for the Discord channel #games-3d-simulations.

    python3 games_feed.py --jobs PATH                 # DRY RUN (the default): count, a sample, what would be posted. Sends nothing, reads no webhook.
    python3 games_feed.py --jobs PATH --baseline      # remember today's matches as already posted, send nothing (so a first run does not post the backlog)
    python3 games_feed.py --jobs PATH --send          # post the new ones; refuses unless keywords.json engine_rule.posting is "on"

Professor Bear, 2026-10-28: 'any game jobs that an early-career person who knows Unreal or Godot or Unity, or has any
experience there, could take' go to a second channel, and posting stays OFF until he says go. So three locks: the rules
file says "posting": "off"; --send is needed on the command line; and a first send, with no memory of what was posted,
needs --post-all (or --baseline first) so a backlog is never dumped by accident.

PATH is the ai-jobs snapshot (jobs.jsonl: every posting on the boards it reads) or Lectern's own all-jobs file. Lectern's
six watched boards have no game studio on them, so the ai-jobs file is the one that finds anything. What is judged, and
why each posting is or is not posted, is collect/engine_jobs.py and keywords.json `engine_rule`.

Same safety rules as notify.py: a message with a local path, an email address or a webhook URL is refused; the channel's
webhook is a secret in ~/.discord-webhooks/games-3d-simulations (mode 600), never printed or logged; ids that Discord
accepted are remembered in runs/posted-games-to-discord.json, so nothing is posted twice. Only the title, company, place
and link of the employer's own public posting are posted. Run it in ONE place: if the server posts, never post from a laptop.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import os

import channel_feed
import engine_jobs as ej
import notify

CHANNEL = "games-3d-simulations"
STATE = os.path.join(lp.RUNS, "posted-games-to-discord.json")
FOOTER = ("Title, company and link only, from each employer's own public job board. Early career is read from the words in the title: "
          "open the posting and read it. A person decides; the machine only ranks words.")
load_state, save_state = channel_feed.load_state, channel_feed.save_state


def row_text(v, r):
    loc = (v["location_text"] or "").split(" | ")[0].split(";")[0].split(" · ")[0][:40]
    words = ", ".join(dict.fromkeys([max(r["hits"], key=lambda h: len(h[1]))[1]] + r["level_words"][:1])) if r["hits"] else ""
    return (f"**{v['company']}**: {v['title'][:100]}" + (f" · {loc}" if loc else "") + (f" ({words})" if words else "") + f" {v['url']}")


def judge_all(views, kw, studios=frozenset()):
    return [(v, ej.judge_engine(v, kw, studios)) for v in views]


def wanted(judged, kw):
    return channel_feed.wanted(judged, kw["engine_rule"])


def _summary(judged, dec, a, kw):
    studios = ej.load_studios(a.targets)
    from_list = sum(1 for _, r in judged if r["decision"] == "post" and r["hits"] and r["hits"][0][0].startswith("studio hint"))
    return [f"studio list: {len(studios)} studios from targets.json" + (f"; {from_list} of the {dec['post']} posts come from it, the rest from a title phrase" if studios else " (none: titles only)")]


SPEC = {"name": "games", "rule_key": "engine_rule", "channel": CHANNEL, "state": STATE, "prefix": "Games: ", "footer": FOOTER,
        "jobs_help": "the ai-jobs jobs.jsonl, or a Lectern all-jobs-DATE.json", "load": ej.load_postings,
        "decisions": ("post", "unstated", "senior-or-mid", "rejected", "no-match"),
        "title": lambda n: f"{n} new early-career game and real-time listings", "row_text": row_text,
        "judge_all": lambda views, kw, a: judge_all(views, kw, ej.load_studios(a.targets)), "summary_lines": _summary}


def build_messages(rows):
    return channel_feed.build_messages(rows, SPEC)


def main(argv=None):
    return channel_feed.run(SPEC, argv, description=__doc__)


if __name__ == "__main__":
    raise SystemExit(main())
