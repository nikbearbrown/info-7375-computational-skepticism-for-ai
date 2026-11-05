#!/usr/bin/env python3
"""consulting_jobs.py — which postings are early-career consulting jobs? (rules: keywords.json `consulting_rule`)

Professor Bear, 2026-10-28: 'another search, for consulting jobs', for the consulting firms of a directory he pasted, with its
own Discord channel, #consulting-firm, and posting off until he says go. This is the judge for that channel, shaped like
engine_jobs.py and kept apart from collect.judge() on purpose: Lectern's main keep rule looks for teaching and training words,
and on 907 consulting postings it kept 9 and none was an early-career consulting job.

A posting is judged from its TITLE and its place (the boards' lists carry no ad text here). The first test that fails gives the reason:

  1. no-match        no role word of consulting_rule.role_words in the title
  2. not-consulting  a word of not_consulting_words is there ('Software Engineer Intern', 'Service Desk Analyst', 'Tax Associate'), unless a phrase of
                     not_consulting_exceptions that contains it is too ('Audit Remediation')
  3. senior-or-mid   a level word that is not early career ('Senior', 'Manager', 'Partner', 'Managing', 'II', ...)
  4. rejected        a clearance is named in the title (clearance_words), or the same two gates as the main filter:
                     the place names no allowed country (consulting_rule.extra_allowed_countries are allowed here and nowhere else), or the title says K-12
  5. post            an explicit early sign is in the title (early_career.words: intern, summer, graduate, junior, a start year ...)
  6. unstated        a role word and no early sign ('Analyst', 'Associate', 'Consultant'): held back unless include_unstated_level is true

Stdlib only. No network. Every decision carries its reason.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py

import collect
import engine_jobs as ej

posting_view, load_postings = ej.posting_view, ej.load_postings

_LOCATION_RULES = {}


def location_rule_for(kw):
    """The main location_rule with consulting_rule.extra_allowed_countries added to its allowed list (Professor Bear, 2026-11-05: a longer country list for
    consulting). Built once per rules object, because collect.places_of compiles by the identity of the rule it is given. The main rule is never changed."""
    base = kw.get("location_rule")
    extra = [c for c in kw["consulting_rule"].get("extra_allowed_countries") or [] if base and c not in (base.get("allowed_countries") or [])]
    if not base or not extra:
        return base
    hit = _LOCATION_RULES.get(id(base))
    if hit and hit[0] is base and hit[1] == tuple(extra):
        return hit[2]
    derived = dict(base, allowed_countries=list(base.get("allowed_countries") or []) + extra)
    _LOCATION_RULES[id(base)] = (base, tuple(extra), derived)
    return derived


def judge_consulting(view, kw):
    """-> {decision, reason, hits, level, level_words}. decision is one of no-match, not-consulting, senior-or-mid, rejected, post, unstated."""
    rule = kw["consulting_rule"]
    t = ej.blanked(view["title"], rule)
    roles = [w for w in rule.get("role_words") or [] if collect.word_in(w.lower(), t)]
    out = {"decision": "no-match", "reason": "no consulting role word in the title", "hits": roles, "level": None, "level_words": []}
    if not roles:
        return out
    # a phrase of not_consulting_exceptions ('audit remediation': federal financial-management consulting) cancels the not-consulting word it contains
    exceptions = [e.lower() for e in rule.get("not_consulting_exceptions") or [] if collect.word_in(e.lower(), t)]
    notc = [w for w in rule.get("not_consulting_words") or [] if collect.word_in(w.lower(), t) and not any(collect.word_in(w.lower(), e) for e in exceptions)]
    if notc:
        out.update(decision="not-consulting", reason=f"not a consulting role: '{notc[0]}' in the title")
        return out
    level, words = ej.level_of(view["title"], rule)
    out.update(level=level, level_words=words)
    if level == "senior-or-mid":
        out.update(decision="senior-or-mid", reason="not early career: " + ", ".join(f"'{w}'" for w in words[:2]) + " in the title")
        return out
    blocked = []
    clear = [w for w in rule.get("clearance_words") or [] if collect.word_in(w.lower(), t)]
    if clear:
        blocked.append("clearance in the title: " + ", ".join(f"'{w}'" for w in clear[:2]))
    loc_rule = location_rule_for(kw)
    if loc_rule:
        w = collect.where(view["location_text"], loc_rule)
        if w["decision"] == "outside":
            blocked.append("country not allowed: " + ", ".join(w["countries"]))
        elif w["decision"] == "unnamed" and loc_rule.get("if_no_country_named", "keep") == "reject":
            blocked.append("no country named in the location")
    k12 = collect.k12_hits(view["title"], "", kw["k12_rule"]) if kw.get("k12_rule") else {"title": [], "body": []}
    if k12["title"]:
        blocked.append("K-12 role: " + " and ".join(f"'{p}' in the title" for p in k12["title"][:2]))
    if blocked:
        out.update(decision="rejected", reason="; ".join(blocked))
        return out
    what = "'" + max(roles, key=len) + "'"
    if level == "early":
        out.update(decision="post", reason=f"{what} in the title; early sign: " + ", ".join(f"'{w}'" for w in words[:2]))
    else:
        out.update(decision="unstated", reason=f"{what} in the title; no early sign, so held back")
    return out
