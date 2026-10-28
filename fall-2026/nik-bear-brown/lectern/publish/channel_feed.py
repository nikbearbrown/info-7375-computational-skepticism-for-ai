#!/usr/bin/env python3
"""channel_feed.py — the part of a dry-run-by-default Discord poster that every channel shares.

publish/games_feed.py (#games-3d-simulations) and publish/consulting_feed.py (#consulting-firm) each describe themselves in a
small `spec` and call run(). What they share, written once so a fix to a lock is one edit:

  * a DRY RUN is the default: it prints the counts, a sample and the safety check on every message, sends nothing, reads no webhook;
  * three locks on sending: the rules file says "posting": "off" until Professor Bear says go; --send must be on the command line;
    a first send with no memory of earlier posts needs --post-all (or --baseline first);
  * ids that Discord accepted are remembered message by message in a state file under runs/, so nothing is posted twice, and a
    failed first send leaves no file behind (a file would stand in for 'something was posted from here before');
  * the same refusals as notify.py: a message with a local path, an email address or a webhook URL is not sent.

The webhook is a secret in ~/.discord-webhooks/<channel> (mode 600) and is read only by notify.post() on a real send.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import argparse, collections, json, os

import notify


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


def wanted(judged, rule):
    """The judgements that are to be posted: 'post', and 'unstated' too if the rules say so."""
    take = {"post"} | ({"unstated"} if rule.get("include_unstated_level") else set())
    return [(v, r) for v, r in judged if r["decision"] in take]


def sort_key(x):
    return (x[0]["company"], x[0]["title"], x[0]["location_text"])


def build_messages(rows, spec):
    """rows = [(view, judgement)] to post -> [(message text, [ids of the postings in it])], ordered as people read them: company, then title.
    With spec["group"], postings of one company with one title (one role in several cities) share one line, and their ids ride with it.
    The ids ride with the message so that what Discord accepted is remembered message by message."""
    rows = sorted(rows, key=sort_key)
    lines = []                                                       # (text, [ids])
    if spec.get("group"):
        i = 0
        while i < len(rows):
            j = i
            while j < len(rows) and (rows[j][0]["company"], rows[j][0]["title"]) == (rows[i][0]["company"], rows[i][0]["title"]):
                j += 1
            lines.append((spec["group_text"](rows[i:j]), [v["id"] for v, _ in rows[i:j]]))
            i = j
    else:
        lines = [(spec["row_text"](v, r), [v["id"]]) for v, r in rows]
    msgs, chunk, ids, size = [], [], [], 0
    for ln, lid in lines:
        if size + len(ln) > notify.MAX_CHUNK and chunk:
            msgs.append(["\n".join(chunk), ids]); chunk, ids, size = [], [], 0
        chunk.append(ln); ids += lid; size += len(ln) + 1
    if chunk:
        msgs.append(["\n".join(chunk), ids])
    if msgs:
        msgs[-1][0] += "\n\n" + spec["footer"]
    return [tuple(m) for m in msgs]


def run(spec, argv=None, description=None):
    ap = argparse.ArgumentParser(description=description, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--jobs", default=None, help=spec["jobs_help"])
    ap.add_argument("--keywords", default=lp.config("keywords.json"))
    ap.add_argument("--targets", help="default: config/targets.json (the list of studios or firms is one of its sections)")
    ap.add_argument("--state", default=spec["state"], help=f"the ids already posted (default {os.path.relpath(spec['state'], lp.ROOT)})")
    ap.add_argument("--sample", type=int, default=12, help="how many lines of the preview to print")
    ap.add_argument("--show-unstated", action="store_true", help="also list the postings held back because their title states no level")
    ap.add_argument("--baseline", action="store_true", help="remember the current matches as already posted; send nothing")
    ap.add_argument("--send", action="store_true", help=f"post to Discord (needs {spec['rule_key']}.posting = on)")
    ap.add_argument("--post-all", action="store_true", help="allow the first send, with no memory of earlier posts, to post everything that matches")
    if spec.get("extra_args"):
        spec["extra_args"](ap)
    a = ap.parse_args(argv)

    with open(a.keywords, encoding="utf-8") as f:
        kw = json.load(f)
    rule = kw.get(spec["rule_key"])
    if rule is None:
        print(f"{a.keywords} has no {spec['rule_key']}")
        return 2
    channel = rule.get("channel", spec["channel"])
    jobs = spec["prepare"](a) if spec.get("prepare") else a.jobs
    if not jobs:
        print("No postings file: give --jobs PATH.")
        return 2
    judged = spec["judge_all"](spec["load"](jobs), kw, a)
    dec = collections.Counter(r["decision"] for _, r in judged)
    todo = wanted(judged, rule)
    state_exists = os.path.exists(a.state)
    already = load_state(a.state)
    new = sorted([(v, r) for v, r in todo if v["id"] not in already], key=sort_key)
    msgs = build_messages(new, spec)

    print(f"{len(judged):,} postings read from {os.path.basename(jobs)} · rules v{kw['version']} · posting to #{channel} is {rule.get('posting', 'off').upper()}")
    print("  " + " · ".join(f"{k} {dec[k]}" for k in spec["decisions"]))
    for line in spec["summary_lines"](judged, dec, a, kw) if spec.get("summary_lines") else []:
        print("  " + line)
    shown = [ln for text, _ in msgs for ln in text.replace("\n\n" + spec["footer"], "").split("\n")]
    print(f"  to post: {len(todo)} match; {len(todo) - len(new)} already posted; {len(new)} new, as {len(shown)} line(s) in {len(msgs)} message(s)"
          + ("" if state_exists else " (no memory of earlier posts yet)"))
    for ln in shown[:max(a.sample, 0)]:
        print("   ", ln)
    if len(shown) > a.sample:
        print(f"    … and {len(shown) - a.sample} more lines")
    if a.show_unstated:
        held = [(v, r) for v, r in judged if r["decision"] == "unstated"]
        print(f"  held back, no level or early sign in the title ({len(held)}):")
        for v, r in sorted(held, key=lambda x: (x[0]["company"], x[0]["title"])):
            print("   ", f"{v['company']}: {v['title'][:80]} · {v['location_text'][:30]}")

    title = spec["title"](len(new))
    if a.baseline:
        save_state(a.state, already | {v["id"] for v, _ in todo})
        print(f"baseline: {len(todo)} current matches remembered as posted; nothing sent")
        return 0
    if not a.send:
        for i, (m, _) in enumerate(msgs):                               # the safety check on every message, without sending
            notify.post(title + (f" ({i + 1}/{len(msgs)})" if len(msgs) > 1 else ""), m, False, prefix=spec["prefix"], channel=channel)
        print("DRY RUN: nothing was sent and no webhook was read.")
        return 0
    if rule.get("posting") != "on":
        print(f'NOT SENT: keywords.json {spec["rule_key"]}.posting is not "on". Posting waits for Professor Bear.')
        return 3
    if not state_exists and not a.post_all:
        print("NOT SENT: nothing has been posted from here before. Run --baseline to skip today's backlog, or --post-all to post it.")
        return 3
    if not new:
        print("Nothing new to post.")
        return 0
    posted = set(already)
    for i, (m, ids) in enumerate(msgs):
        if not notify.post(title + (f" ({i + 1}/{len(msgs)})" if len(msgs) > 1 else ""), m, True, prefix=spec["prefix"], channel=channel):
            if posted != already:                                        # what Discord did accept stays remembered; a failed first try leaves no file,
                save_state(a.state, posted)                              # so it cannot stand in for 'something was posted from here before'
            print("Discord did not accept a message; the postings in it were not remembered, so the next run tries them again.")
            return 1
        posted |= set(ids)
        save_state(a.state, posted)
    return 0
