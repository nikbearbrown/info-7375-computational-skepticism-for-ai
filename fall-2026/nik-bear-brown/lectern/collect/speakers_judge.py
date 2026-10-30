#!/usr/bin/env python3
"""speakers_judge.py — which companies are worth inviting to give an online talk about their MCP? (rules: keywords.json `speakers_rule`)

Professor Bear, 2026-10-30: 'We want to add another search to Lectern and this is for speakers ... which companies have speakers
that'll talk about their MCP ... invite the evangelist type people in a company who are willing to come and give an online talk
about using their MCP.' This is the judge for that channel. Unlike the job channels the unit is a COMPANY, not a posting, and the
evidence is a list of sourced signals, not words in a title. It is kept apart from collect.judge() on purpose.

A lead is a company record from collect/speakers_collect.py: its MCP (name, primary source), its sourced signals, how many named
people were found (the names themselves stay in the local, untracked speaker-records/, never here), and its public contact route.
In this order, and the first test that fails gives the reason:

  1. rejected   the research dropped the company (verdict 'drop': no MCP of its own was found, or only a third-party server);
                a company whose verdict is 'to-do' (a question for Professor Bear is open) is held back, not scored
  2. not-mcp    no 'mcp_docs' signal: the company's OWN public page for the MCP, with a link. Without it nothing else is counted
  3. unstated   (held back) no public contact route the company itself publishes (a DevRel or community page, a speaker or
                partnerships form, a public handle its own page lists): a lead nobody can reach in public is not posted
  4. unstated   (held back) the score is below speakers_rule.min_score
  5. post       the score is at or above min_score

The score is the sum of weights for signals that have a link (speakers_rule.weights). A route counts 10 if it is a DevRel page, a speaker
form or a partnerships form, and 5 if it is only a community forum or a public handle. If the collector re-checked the links (`--check`),
a signal counts only if its link answered 2xx, or turned the script away (robots, 401, 403, 429) for a page the researcher opened; a 404
never counts. If the links were not re-checked, every signal counts as researched and the reason says 'links not re-checked'. A score says how likely the company is to send someone; it is not a judgement of the people.

Stdlib only. No network. Every decision carries its reason and the parts of the score.
"""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import json


def lead_view(rec):
    """One lead record -> {id, company, title, url, location_text} for the shared poster: the MCP's name stands in for the title,
    its primary source for the link, and there is no place."""
    return {"id": rec.get("id") or f"speakers:{rec.get('company', '')}", "company": rec.get("company") or "",
            "title": (rec.get("mcp") or {}).get("name") or "", "url": (rec.get("mcp") or {}).get("primary_source") or "", "location_text": ""}


def load_postings(path):
    """The leads file written by speakers_collect.py ({"records": [...]}) -> [(view, record)]. The record rides along: the judge needs its signals."""
    with open(path, encoding="utf-8") as f:
        return [(lead_view(r), r) for r in json.load(f)["records"]]


REFUSED = ("robots", "401", "403", "429", "error")       # the page did not answer a script; that is not the page being gone


def counted(sig, checks):
    """Does this signal count? It needs an https link. If the links were re-checked it also needs a 2xx answer, or a refusal of the script
    (robots, 401, 403, 429, a failed connection) for a page the researcher OPENED: a page that turns scripts away is not a page that is not
    there. A 404 or 410 never counts."""
    url = (sig or {}).get("url") or ""
    if not url.startswith("https://"):
        return False
    if checks is None:
        return True
    status = str((checks.get(url) or {}).get("status", ""))
    return status.startswith("2") or (status in REFUSED and bool(sig.get("opened")))


def score_of(rec, rule):
    """-> (score, parts, kinds). parts = {name: points}; kinds = the signal kinds that counted."""
    w, checks = rule["weights"], rec.get("checks")
    by_kind = {}
    for s in rec.get("signals") or []:
        if counted(s, checks):
            by_kind.setdefault(s.get("kind"), []).append(s)
    parts = {}
    for k in ("mcp_docs", "devrel_team", "community_channel"):
        if by_kind.get(k):
            parts[k] = w[k]
    talks = len(by_kind.get("mcp_talk") or [])
    if talks:
        parts["mcp_talk"] = w["mcp_talk"] + min(talks - 1, w["mcp_talk_extra_max"] // w["mcp_talk_extra_each"]) * w["mcp_talk_extra_each"]
    if (rec.get("people_found") or 0) >= 1:
        parts["named_people"] = w["named_people"]
    route = rec.get("contact_route") or {}
    if counted(route, checks):
        if route.get("kind") in rule["contact_route_kinds"]:
            parts["contact_route"] = w["contact_route"]                       # a DevRel page, a speaker form, a partnerships form
        elif route.get("kind") in rule["contact_route_weak_kinds"]:
            parts["contact_route"] = w["contact_route_weak"]                  # a community forum or a public handle: a route, but not for speakers
    return sum(parts.values()), parts, sorted(by_kind)


def judge_speaker(view, rec, kw):
    """-> {decision, reason, score, parts, mcp_status, route}. decision is one of rejected, not-mcp, unstated, post."""
    rule = kw["speakers_rule"]
    route = rec.get("contact_route") or {}
    out = {"decision": "rejected", "reason": "", "score": 0, "parts": {}, "mcp_status": (rec.get("mcp") or {}).get("status", ""),
           "route": {"kind": route.get("kind", ""), "url": route.get("url", "")}}
    if rec.get("verdict") == "drop":
        out["reason"] = "dropped by the research: " + (rec.get("why") or "no reason recorded")[:120]
        return out
    if rec.get("verdict") == "to-do":
        out.update(decision="unstated", reason="waiting for a decision, not posted: " + (rec.get("todo") or "see targets.json")[:120])
        return out
    score, parts, kinds = score_of(rec, rule)
    out.update(score=score, parts=parts)
    note = "" if rec.get("checks") is not None else " (links not re-checked)"
    if "mcp_docs" not in parts:
        out.update(decision="not-mcp", reason="no sourced public page for the company's own MCP" + (" that answered" if rec.get("checks") is not None else ""))
        return out
    if "contact_route" not in parts:
        out.update(decision="unstated", reason=f"score {score}: no public contact route the company itself publishes, so held back{note}")
        return out
    if score < rule["min_score"]:
        out.update(decision="unstated", reason=f"score {score} is below {rule['min_score']}: " + ", ".join(f"{k} {v}" for k, v in parts.items()) + note)
        return out
    out.update(decision="post", reason=f"score {score}: " + ", ".join(f"{k} {v}" for k, v in parts.items()) + note)
    return out
