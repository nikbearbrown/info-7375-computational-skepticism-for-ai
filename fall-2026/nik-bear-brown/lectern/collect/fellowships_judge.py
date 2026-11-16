#!/usr/bin/env python3
"""fellowships_judge.py — which fellowship and residency programs are to be posted? (rules: keywords.json `fellowships_rule`)

Professor Bear, 2026-11-05: 'Add AI fellowships to my job search', then 'Research only, #professor-bear'. The unit is a PROGRAM, read by
collect/fellowships_collect.py from the program's own page, not a posting judged from a title. The first test that fails gives the reason:

  1. not-research   the program's kind is not in fellowships_rule.kinds (a founder program, an accelerator, a school)
  2. no-deadline    no date is known: a program with no deadline cannot be told to be open, so it is held back
  3. closed         the deadline has passed (today is after it)
  4. post           a research kind with a deadline today or later

Stdlib only. No network. Every decision carries its reason. The deadline basis ('page', 'listed') is carried to the post, so a date a person
recorded is never shown as a date the page gave.
"""
import datetime as dt


def judge_fellowship(view, kw, today=None):
    """-> {decision, reason, hits, level, level_words}. The last three keys exist so that publish/channel_feed.py can treat every channel alike."""
    rule = kw["fellowships_rule"]
    today = today or dt.date.today()
    out = {"decision": "not-research", "reason": f"kind {view.get('kind')!r} is not one of {rule['kinds']}", "hits": [], "level": None, "level_words": []}
    if view.get("kind") not in rule["kinds"]:
        return out
    d = view.get("deadline") or ""
    if not d:
        return dict(out, decision="no-deadline", reason="no deadline is known")
    try:
        due = dt.date.fromisoformat(d)
    except ValueError:
        return dict(out, decision="no-deadline", reason=f"deadline {d!r} is not a date")
    if due < today:
        return dict(out, decision="closed", reason=f"the deadline {d} has passed")
    return dict(out, decision="post", reason=f"{view['kind']}, deadline {d} ({view.get('deadline_basis')})")
