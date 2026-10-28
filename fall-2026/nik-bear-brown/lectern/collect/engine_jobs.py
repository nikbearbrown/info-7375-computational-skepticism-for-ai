#!/usr/bin/env python3
"""engine_jobs.py — which postings are early-career game, engine and real-time 3D jobs? (rules: keywords.json `engine_rule`)

Professor Bear, 2026-10-28: 'any game jobs that an early-career person who knows Unreal or Godot or Unity, or has any
experience there, could take' should go to a second Discord channel, #games-3d-simulations. This is the judge for that
channel, kept apart from collect.judge() on purpose: those postings are not education jobs and must never enter the
#professor-bear stream.

A posting is judged from its TITLE, its place and (for the K-12 gate) nothing else, because the feed it is meant for
(the ai-jobs snapshot) keeps no ad text. In this order, and the first test that fails gives the reason:

  1. no-match      the title has none of the phrases of an enabled group in engine_rule.groups
  2. senior-or-mid a level word that is not early career is in the title ('Senior', 'Lead', 'II', 'Manager', ...)
  3. rejected      the same two gates as the main filter: the place names no allowed country, or the title says K-12
  4. post          an early-career word is in the title ('Intern', 'Junior', 'Associate', 'Graduate', 'Engineer I', ...)
  5. unstated      the title says nothing about level; posted only if engine_rule.include_unstated_level is true

A second way into step 1, for a studio on the list (config/targets.json, section `games`, status `active`): an early-career title
with a craft word ('Software Engineer Intern', 'Associate Producer') and none of the non-craft words ('Marketing', 'Counsel',
'Supply Chain') counts as a game job even though it names no game or engine, because the employer is a game studio.

Stdlib only. No network. Every decision carries its reason.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import json, re

import collect


def title_text(title):
    """Lower-case, dashes unified ('K–12'), accents kept: the form the phrases are written in."""
    return re.sub("[‐-―−]", "-", (title or "").lower())


def blanked(title, rule):
    """The title in the form phrases are matched against, with the false friends ('unity catalog', 'early stage') blanked out."""
    t = title_text(title)
    for ff in rule.get("false_friends") or []:
        t = t.replace(ff.lower(), " ")
    return t


def role_hits(title, rule):
    """[(group, phrase)] for every phrase of an enabled group found in the title, after the false friends are blanked."""
    t = blanked(title, rule)
    return [(g, p) for g, spec in (rule.get("groups") or {}).items() if spec.get("enabled")
            for p in spec.get("phrases") or [] if collect.word_in(p.lower(), t)]


def level_of(title, rule):
    """-> ('senior-or-mid' | 'early' | 'unstated', [the words that decided it]). A level word that is not early career wins:
    'Associate Director' is a director."""
    t = blanked(title, rule)
    ec = rule.get("early_career") or {}
    veto = [w for w in ec.get("veto_words") or [] if collect.word_in(w.lower(), t)]
    if veto:
        return "senior-or-mid", veto
    early = [w for w in ec.get("words") or [] if collect.word_in(w.lower(), t)]
    return ("early", early) if early else ("unstated", [])


def studio_names(doc):
    """The studios on the list: the case-folded names the feed uses for them (targets.json, section `games`, status `active`)."""
    out = set()
    for t in doc.get("targets") or []:
        if t.get("section") == "games" and t.get("status") == "active":
            out.update(n.casefold() for n in (t.get("games") or {}).get("feed_names") or [t["name"]])
    return out


def load_studios(path=None):
    """The studio list from config/targets.json, or an empty set where that file does not exist (the other classes' flat copies)."""
    try:
        with open(path or lp.config("targets.json"), encoding="utf-8") as f:
            return studio_names(json.load(f))
    except FileNotFoundError:
        return set()


def studio_craft(title, spec):
    """The craft word that makes an early-career title at a studio a game job, or None if there is none or a non-craft word is there."""
    t = title_text(title)
    craft = [w for w in spec.get("craft_words") or [] if collect.word_in(w.lower(), t)]
    non = [w for w in spec.get("non_craft_words") or [] if collect.word_in(w.lower(), t)]
    return craft[0] if craft and not non else None


def posting_view(row):
    """One posting from either file this can read -> {id, company, title, url, location_text}.
    The ai-jobs snapshot (`locations` list, `id`) and Lectern's own all-jobs records (`location_text`, `source` + `source_id`)."""
    loc = row.get("location_text")
    if loc is None:
        loc = " · ".join(row.get("locations") or [])
    return {"id": row.get("id") or f"{row.get('source')}:{row.get('source_id')}", "company": row.get("company") or "",
            "title": row.get("title") or "", "url": row.get("url") or "", "location_text": loc}


def load_postings(path):
    """A file of postings -> views. .jsonl = the ai-jobs snapshot (one canonical posting per line);
    .json = Lectern's own all-jobs file ({"records": [...]})."""
    with open(path, encoding="utf-8") as f:
        if path.endswith(".jsonl"):
            return [posting_view(json.loads(l)) for l in f if l.strip()]
        return [posting_view(r) for r in json.load(f)["records"]]


def judge_engine(view, kw, studios=frozenset()):
    """-> {decision, reason, hits, level, level_words}. decision is one of no-match, senior-or-mid, rejected, post, unstated.
    `studios` is the case-folded studio list from load_studios(); without it only the title phrases count."""
    rule = kw["engine_rule"]
    hits = role_hits(view["title"], rule)
    out = {"decision": "no-match", "reason": "no engine or game phrase in the title", "hits": hits, "level": None, "level_words": []}
    level, words = level_of(view["title"], rule)
    hint = rule.get("studio_hint") or {}
    if not hits and studios and hint.get("enabled") and level == "early" and view["company"].casefold() in studios:
        craft = studio_craft(view["title"], hint)
        if craft:
            hits = [(f"studio hint: {view['company']}", craft)]
            out["hits"] = hits
    if not hits:
        return out
    out.update(level=level, level_words=words)
    if level == "senior-or-mid":
        out.update(decision="senior-or-mid", reason="not early career: " + ", ".join(f"'{w}'" for w in words[:2]) + " in the title")
        return out
    blocked = []
    loc_rule = kw.get("location_rule")
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
    g, phrase = max(hits, key=lambda h: len(h[1]))                # the most specific phrase names the reason
    what = f"'{phrase}' ({g})"
    if level == "early":
        out.update(decision="post", reason=f"{what} in the title; early career: " + ", ".join(f"'{w}'" for w in words[:2]))
    else:
        out.update(decision="unstated", reason=f"{what} in the title; the title states no level")
    return out
