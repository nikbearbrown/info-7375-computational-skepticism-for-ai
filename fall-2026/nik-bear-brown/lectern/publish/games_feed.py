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
import argparse, collections, json, os

import engine_jobs as ej
import notify

CHANNEL = "games-3d-simulations"
STATE = os.path.join(lp.RUNS, "posted-games-to-discord.json")
FOOTER = ("Title, company and link only, from each employer's own public job board. Early career is read from the words in the title: "
          "open the posting and read it. A person decides; the machine only ranks words.")


def row_text(v, r):
    loc = (v["location_text"] or "").split(" | ")[0].split(";")[0].split(" · ")[0][:40]
    words = ", ".join(dict.fromkeys([max(r["hits"], key=lambda h: len(h[1]))[1]] + r["level_words"][:1])) if r["hits"] else ""
    return (f"**{v['company']}**: {v['title'][:100]}" + (f" · {loc}" if loc else "") + (f" ({words})" if words else "") + f" {v['url']}")


def build_messages(rows):
    """rows = [(view, judgement)] to post -> [(message text, [ids of the postings in it])], ordered as people read them:
    company, then title. The ids ride with the message so that what Discord accepted is remembered message by message."""
    rows = sorted(rows, key=lambda x: (x[0]["company"], x[0]["title"], x[0]["location_text"]))
    msgs, chunk, ids, size = [], [], [], 0
    for v, r in rows:
        ln = row_text(v, r)
        if size + len(ln) > notify.MAX_CHUNK and chunk:
            msgs.append(["\n".join(chunk), ids]); chunk, ids, size = [], [], 0
        chunk.append(ln); ids.append(v["id"]); size += len(ln) + 1
    if chunk:
        msgs.append(["\n".join(chunk), ids])
    if msgs:
        msgs[-1][0] += "\n\n" + FOOTER
    return [tuple(m) for m in msgs]


def judge_all(views, kw):
    return [(v, ej.judge_engine(v, kw)) for v in views]


def wanted(judged, kw):
    """The judgements that are to be posted: 'post', and 'unstated' too if the rules say so."""
    take = {"post"} | ({"unstated"} if kw["engine_rule"].get("include_unstated_level") else set())
    return [(v, r) for v, r in judged if r["decision"] in take]


def load_state(path):
    if not os.path.exists(path):
        return set()
    with open(path, encoding="utf-8") as f:
        return set(json.load(f))


def save_state(path, ids):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(sorted(ids), f)
    os.replace(tmp, path)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--jobs", required=True, help="the ai-jobs jobs.jsonl, or a Lectern all-jobs-DATE.json")
    ap.add_argument("--keywords", default=lp.config("keywords.json"))
    ap.add_argument("--state", default=STATE, help="the ids already posted (default runs/posted-games-to-discord.json)")
    ap.add_argument("--sample", type=int, default=12, help="how many lines of the preview to print")
    ap.add_argument("--show-unstated", action="store_true", help="also list the postings held back because their title states no level")
    ap.add_argument("--baseline", action="store_true", help="remember the current matches as already posted; send nothing")
    ap.add_argument("--send", action="store_true", help="post to Discord (needs engine_rule.posting = on)")
    ap.add_argument("--post-all", action="store_true", help="allow the first send, with no memory of earlier posts, to post everything that matches")
    a = ap.parse_args(argv)

    with open(a.keywords, encoding="utf-8") as f:
        kw = json.load(f)
    if "engine_rule" not in kw:
        print(f"{a.keywords} has no engine_rule")
        return 2
    judged = judge_all(ej.load_postings(a.jobs), kw)
    dec = collections.Counter(r["decision"] for _, r in judged)
    todo = wanted(judged, kw)
    state_exists = os.path.exists(a.state)
    already = load_state(a.state)
    new = [(v, r) for v, r in todo if v["id"] not in already]
    msgs = build_messages(new)

    print(f"{len(judged):,} postings read from {os.path.basename(a.jobs)} · rules v{kw['version']} · posting is {kw['engine_rule'].get('posting', 'off').upper()}")
    print("  " + " · ".join(f"{k} {dec[k]}" for k in ("post", "unstated", "senior-or-mid", "rejected", "no-match")))
    print(f"  to post: {len(todo)} match; {len(todo) - len(new)} already posted; {len(new)} new, in {len(msgs)} message(s)"
          + ("" if state_exists else " (no memory of earlier posts yet)"))
    new.sort(key=lambda x: (x[0]["company"], x[0]["title"], x[0]["location_text"]))
    for v, r in new[:max(a.sample, 0)]:
        print("   ", row_text(v, r))
    if len(new) > a.sample:
        print(f"    … and {len(new) - a.sample} more")
    if a.show_unstated:
        held = [(v, r) for v, r in judged if r["decision"] == "unstated"]
        print(f"  held back, no level word in the title ({len(held)}):")
        for v, r in sorted(held, key=lambda x: (x[0]["company"], x[0]["title"])):
            print("   ", f"{v['company']}: {v['title'][:80]} · {v['location_text'][:30]}")

    if a.baseline:
        save_state(a.state, already | {v["id"] for v, _ in todo})
        print(f"baseline: {len(todo)} current matches remembered as posted; nothing sent")
        return 0
    if not a.send:
        for i, (m, _) in enumerate(msgs):                               # the safety check on every message, without sending
            notify.post(f"{len(new)} new early-career game and real-time listings" + (f" ({i + 1}/{len(msgs)})" if len(msgs) > 1 else ""),
                        m, False, prefix="Games: ", channel=CHANNEL)
        print("DRY RUN: nothing was sent and no webhook was read.")
        return 0
    if kw["engine_rule"].get("posting") != "on":
        print('NOT SENT: keywords.json engine_rule.posting is not "on". Posting waits for Professor Bear.')
        return 3
    if not state_exists and not a.post_all:
        print("NOT SENT: nothing has been posted from here before. Run --baseline to skip today's backlog, or --post-all to post it.")
        return 3
    if not new:
        print("Nothing new to post.")
        return 0
    title = f"{len(new)} new early-career game and real-time listings"
    posted = set(already)
    for i, (m, ids) in enumerate(msgs):
        if not notify.post(title + (f" ({i + 1}/{len(msgs)})" if len(msgs) > 1 else ""), m, True, prefix="Games: ", channel=CHANNEL):
            if posted != already:                                        # what Discord did accept stays remembered; a failed first try leaves no file,
                save_state(a.state, posted)                              # so it cannot stand in for 'something was posted from here before'
            print("Discord did not accept a message; the postings in it were not remembered, so the next run tries them again.")
            return 1
        posted |= set(ids)
        save_state(a.state, posted)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
