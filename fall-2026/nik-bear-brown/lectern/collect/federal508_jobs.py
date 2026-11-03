#!/usr/bin/env python3
"""federal508_jobs.py — which postings are federal Section 508 / digital-accessibility jobs a person could take on contract or remotely? (rules: keywords.json `federal508_rule`)

Professor Bear, 2026-10-31, for a friend of his: 'Can we have the job search also look for Federal 508 work ... she's looking for contract work. Or remote
work.' This is the judge for that channel, shaped like consulting_jobs.py and kept apart from collect.judge() on purpose: Lectern's main keep rule looks
for teaching and training words, and an accessibility auditor is not one.

A posting is judged from its TITLE and its place (the boards' lists carry no ad text here). The first test that fails gives the reason:

  1. no-match      no phrase of an enabled group of federal508_rule.groups is in the title ('Section 508 Tester', 'Accessibility Specialist', 'WCAG', ...), and, for a posting
                   that comes WITH its ad text (USAJOBS' list does), no phrase of federal508_rule.opportunity_work_phrases ('508 testing', 'trusted tester' ...: 508 as the work)
                   in that text. The ad text is looked at only when the title has no phrase; every other source is judged from the title alone.
  2. not-digital   a word of not_digital_words is there ('Building Accessibility', 'Wheelchair', 'Paratransit': physical access, not ICT)
  3. rejected      the place names no allowed country (this channel allows the United States only: federal work); a place that names none ('Remote') passes
  4. post          the title or the place says REMOTE, or the title says CONTRACT ('Contractor', '1099', 'Temporary', 'Consultant' ...)
  5. unstated      a fitting role that says neither: held back unless include_unstated_level is true (the key is shared with the other channels' feeds)

A clearance in the title (Secret, Public Trust ...) is NOT a veto here, as it is for consulting: it is a flag the post shows, because a person
without one should see it before reading on, and it is the person's call (clearance_policy: "flag" or "veto"). No level is read: the work is
audit-first, and an audit is not an entry-level job.

Stdlib only. No network. Every decision carries its reason.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import copy, json

import collect
import engine_jobs as ej

def posting_view(row):
    """ej.posting_view, plus the ad text when the posting came with it (USAJOBS: summary and duties), under 'description'."""
    v = ej.posting_view(row)
    if row.get("description"):
        v["description"] = row["description"]
    return v


def load_postings(path):
    """ej.load_postings with this module's posting_view, so the ad text of a posting that has one reaches the judge."""
    with open(path, encoding="utf-8") as f:
        if path.endswith(".jsonl"):
            return [posting_view(json.loads(l)) for l in f if l.strip()]
        return [posting_view(r) for r in json.load(f)["records"]]


def work_hits(text, rule):
    """[('ad-text', phrase)] for the opportunity_work_phrases found in an ad's text, whole words only."""
    t = (text or "").lower()
    return [("ad-text", p) for p in dict.fromkeys(x.lower() for x in rule.get("opportunity_work_phrases") or []) if collect.word_in(p, t)]


def _hits(words, text):
    return [w for w in words or [] if collect.word_in(w.lower(), text)]


def role_hits(title, rule):
    """[(group, phrase)] for every phrase of an enabled group found in the title, after the false friends are blanked."""
    t = ej.blanked(title, rule)
    return [(g, p) for g, spec in (rule.get("groups") or {}).items() if spec.get("enabled")
            for p in spec.get("phrases") or [] if collect.word_in(p.lower(), t)]


def only_allowed(kw):
    """location_rule with this channel's own country list in place of the shared one."""
    loc = copy.deepcopy(kw["location_rule"])
    loc["allowed_countries"] = kw["federal508_rule"].get("allowed_countries") or loc["allowed_countries"]
    return loc


def company_kinds(doc):
    """{case-folded company name: kind} for the employers on the list (targets.json, section `federal508`, status `active`)."""
    out = {}
    for t in doc.get("targets") or []:
        if t.get("section") == "federal508" and t.get("status") == "active":
            for n in (t.get("federal508") or {}).get("feed_names") or [t["name"]]:
                out[n.casefold()] = t["federal508"]["kind"]
    return out


def load_kinds(path=None):
    try:
        with open(path or lp.config("targets.json"), encoding="utf-8") as f:
            return company_kinds(json.load(f))
    except FileNotFoundError:
        return {}


def judge_federal508(view, kw, kinds=None):
    """-> {decision, reason, hits, remote, contract, clearance, federal, kind}. decision is one of no-match, not-digital, rejected, post, unstated."""
    rule = kw["federal508_rule"]
    t = ej.blanked(view["title"], rule)
    place = ej.title_text(view["location_text"])
    hits = role_hits(view["title"], rule) or work_hits(view.get("description"), rule)
    out = {"decision": "no-match", "reason": "no Section 508 or accessibility phrase in the title" + (" or the ad text" if view.get("description") else ""), "hits": hits, "remote": [], "contract": [], "clearance": [], "federal": [],
           "kind": (kinds or {}).get(view["company"].casefold()) or ("agency" if str(view.get("id")).startswith("usajobs:") else None)}
    if not hits:
        return out
    phys = _hits(rule.get("not_digital_words"), t)
    if phys:
        out.update(decision="not-digital", reason=f"not a digital accessibility role: '{phys[0]}' in the title")
        return out
    out["remote"] = _hits(rule.get("remote_words"), t) + _hits(rule.get("remote_words"), place)
    out["contract"] = _hits(rule.get("contract_words"), t)
    out["clearance"] = _hits(rule.get("clearance_words"), t)
    out["federal"] = _hits(rule.get("federal_words"), t)
    blocked = []
    w = collect.where(view["location_text"], only_allowed(kw))
    if w["decision"] == "outside":
        blocked.append("country not allowed: " + ", ".join(w["countries"]))
    elif w["decision"] == "unnamed" and rule.get("if_no_country_named", "keep") == "reject":
        blocked.append("no country named in the location")
    if out["clearance"] and rule.get("clearance_policy") == "veto":
        blocked.append("clearance in the title: " + ", ".join(f"'{x}'" for x in out["clearance"][:2]))
    if blocked:
        out.update(decision="rejected", reason="; ".join(blocked))
        return out
    g, phrase = max(hits, key=lambda h: len(h[1]))
    what = f"'{phrase}' ({g})"
    where_ = "the ad text" if g == "ad-text" else "the title"
    how = ([f"remote: '{out['remote'][0]}'"] if out["remote"] else []) + ([f"contract: '{out['contract'][0]}'"] if out["contract"] else [])
    if how:
        out.update(decision="post", reason=f"{what} in {where_}; " + "; ".join(how))
    else:
        out.update(decision="unstated", reason=f"{what} in {where_}; neither remote nor contract is stated, so held back")
    return out
