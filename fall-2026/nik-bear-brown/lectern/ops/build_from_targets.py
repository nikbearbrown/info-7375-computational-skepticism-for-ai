#!/usr/bin/env python3
"""build_from_targets.py: make the files that depend on the list of targets from config/targets.json.

config/targets.json is the single list of what Lectern watches. Three config files and the tables in TARGETS.md are
generated from it, so they cannot drift from it:
  config/sources.json   the boards (per provider), the unreachable companies and the removed ones, with the reasons
  config/faculty_config.json   the watched schools (names, institutions, aliases); the queries are left as they are
  config/biolabs.json   the seeds and the unreadable seeds; the rules and keywords are left as they are
  TARGETS.md   the tables between the <!-- targets:... --> markers; the prose around them is written by hand

  python3 ops/build_from_targets.py            # write them
  python3 ops/build_from_targets.py --check    # change nothing; exit 1 if any file differs from what targets.json says
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
import lectern_paths as lp


def load(path):
    return json.load(open(path, encoding="utf-8"))


def dumps(obj):
    """Indented JSON, with a list of short scalars kept on one line so the config files stay readable."""
    text = json.dumps(obj, indent=2, ensure_ascii=False)
    def squash(m):
        one = re.sub(r"\s*\n\s*", " ", m.group(0))
        return one if len(one) <= 110 else m.group(0)
    text = re.sub(r"\[\n(?:\s+(?:\"[^\"\n]*\"|-?\d+(?:\.\d+)?|true|false|null),?\n)+\s*\]", squash, text)
    return text + "\n"


def targets_doc():
    return load(lp.config("targets.json"))


def derive_sources(doc, current):
    out = json.loads(json.dumps(current))
    by_provider = {}
    for t in doc["targets"]:
        if t["section"] == "boards" and t["status"] == "active":
            e = {"company": t["name"], "slug": t["slug"], "tier": t.get("tier")}
            e.update(t.get("counts", {}))
            e["why_watched"] = t["why"]
            by_provider.setdefault(t["provider"], []).append(e)
    for prov in out["sources"]:
        prov["boards"] = by_provider.pop(prov["provider"], [])
    assert not by_provider, f"no provider block for {list(by_provider)}"
    un = sorted((t for t in doc["targets"] if "unreachable" in t), key=lambda t: t["unreachable"]["rank"])
    lst = []
    for t in un:
        u = {k: v for k, v in t["unreachable"].items() if k != "rank"}
        e = {"company": t["name"], "ats": u.pop("ats")}
        if t.get("tier") is not None:
            e["tier"] = t["tier"]
        e["why_watched"] = t["why"]
        e.update(u)
        lst.append(e)
    out["unreachable"] = lst
    removed = {"_comment": current["removed"]["_comment"]}
    for t in doc["targets"]:
        if t["status"] == "removed":
            removed[t["name"]] = t["removed"]["entry"]
    out["removed"] = removed
    return out


def derive_faculty(doc, current):
    out = json.loads(json.dumps(current))
    out["watch_schools"] = {t["name"]: {"institution": t["institution"], "aliases": t["aliases"]} for t in doc["targets"] if t["section"] == "schools"}
    return out


def derive_biolabs(doc, current):
    out = json.loads(json.dumps(current))
    seeds = sorted((t["lab_seed"] for t in doc["targets"] if "lab_seed" in t), key=lambda s: s["order"])
    out["seeds"] = [{"name": s["name"], "url": s["url"], "checked": s["checked"]} for s in seeds if s["readable"]]
    out["unreadable"] = [{"name": s["name"], "url": s["url"], "checked": s["checked"]} for s in seeds if not s["readable"]]
    return out


def replace_keys(text, new_obj, keys):
    """Replace only the top-level values named in `keys`, leaving every other byte of a hand-formatted file alone."""
    dec = json.JSONDecoder()
    for k in keys:
        m = re.search(r'^  "' + re.escape(k) + r'":\s*', text, re.M)
        _, end = dec.raw_decode(text, m.end())
        v = new_obj[k]
        if isinstance(v, list) and v and all(isinstance(x, dict) for x in v):      # one record per line, as the file is written
            body = "[\n" + ",\n".join("    " + json.dumps(x, ensure_ascii=False).replace('": ', '": ').replace("{\"", "{\"") for x in v) + "\n  ]"
        else:
            body = json.dumps(v, indent=2, ensure_ascii=False).replace("\n", "\n  ")
        text = text[:m.end()] + body + text[end:]
    return text


def md_link(label, url):
    return f"[{label}]({url})"


def cells(t):
    return " · ".join(md_link(d["label"], d["url"]) if not d.get("call") else f"`{d['url'].replace('https://', '')}`" for d in t["data"]) or "no link verified"


def table(rows, header):
    return "\n".join([header[0], header[1]] + rows)


def derive_tables(doc):
    T, label = doc["targets"], {k: v["label"] for k, v in doc["types"].items()}
    def sec(s, status=None):
        return [t for t in T if t["section"] == s and (status is None or t["status"] == status)]
    out = {}
    boards = sec("boards", "active")
    out["boards"] = table([f"| {t['name']} | {label[t['type']]} | {t['provider'].capitalize() if t['provider'] != 'smartrecruiters' else 'SmartRecruiters'} | "
                           f"{md_link(t['data'][0]['url'].replace('https://', ''), t['data'][0]['url'])} | `{t['data'][1]['url'].replace('https://', '')}` | {t['status_note']}{'; to-do: ' + t['todo'] if t['todo'] else ''} |" for t in boards],
                          ("| Company | Type | Provider | Board page (people) | API the script calls (data) | Status and to-do |", "|---|---|---|---|---|---|"))
    out["bigfour"] = table([f"| {t['name']} | {label[t['type']]} ({t['why']}) | {cells(t)} | {t['status_note']}. To-do: {t['todo']} |" for t in sec("bigfour")],
                           ("| Company | Type | Data (direct link) | Status and to-do |", "|---|---|---|---|"))
    out["unreachable"] = table([f"| {t['name']} | {label[t['type']]} | {cells(t)} | {t['status_note']} | {t['todo']} |" for t in sec("unreachable")],
                               ("| Company | Type | Careers page | What is known | To-do |", "|---|---|---|---|---|"))
    out["schools"] = table([f"| {t['name']} | {cells(t)} | {t['faculty_jobs']['system']} | {t['faculty_jobs']['titles_readable_by_script']} | {t['faculty_jobs']['robots']} | {t['status_note']} |" for t in sec("schools")],
                           ("| School | Faculty-jobs page (direct link) | System | Titles readable by a script? | Robots file | Notes and to-do |", "|---|---|---|---|---|---|"))
    out["research"] = table([f"| {t['name']} | {label[t['type']]} | {t['why']} | {cells(t)} | {t['status_note']}{'. To-do: ' + t['todo'] if t['todo'] else ''} |" for t in sec("research")],
                            ("| Target | Type | Why | Data (direct link) | Status and to-do |", "|---|---|---|---|---|"))
    def games_row(t):
        g = t.get("games") or {}
        a = (g.get("answers_2026_10_28") or {}).get("postings")
        e = g.get("early_career_by_title_2026_10_24")
        ec = (f"{e['early_career']}: {e['matched_by_a_phrase']} by a phrase, {e['added_by_the_list']} added by the list, "
              f"{e['outside_allowed_countries']} outside the countries, {e['not_a_craft_role']} not a craft role") if e else "not read by the feed"
        return (f"| {t['name']} | **{g.get('verdict', '')}** | {(t['provider'] + ': ') if t.get('provider') else ''}{cells(t)} | "
                f"{a if a is not None else 'not read'} | {ec} | {t['why']} | {t['todo'] or 'none'} |")
    out["games"] = table([games_row(t) for t in sec("games")],
                         ("| Studio | Verdict | Board (provider) and its links | Postings answering 2026-10-28 | Early-career titles in the 2026-10-24 snapshot | Why this verdict; the noise | To-do |", "|---|---|---|---|---|---|---|"))
    def consulting_row(t):
        c = t.get("consulting") or {}
        n = (c.get("postings_2026_10_28") or "")
        return (f"| {t['name']} | {c.get('tier') or '-'} | **{c.get('verdict', '')}** | {c.get('system') or '-'} | {cells(t)} | {n or '-'} | {t['why']} | {t['todo'] or 'none'} |")
    out["consulting"] = table([consulting_row(t) for t in sec("consulting")],
                              ("| Firm | Tier | Verdict | System | Board or careers page | Postings 2026-10-28 | Why this verdict; what answered | To-do |", "|---|---|---|---|---|---|---|---|"))
    def speakers_row(t):
        s = t.get("speakers") or {}
        m = s.get("mcp") or {}
        kinds = {}
        for g in s.get("signals") or []:
            kinds[g["kind"]] = kinds.get(g["kind"], 0) + 1
        sig = ", ".join(f"{k} {n}" for k, n in sorted(kinds.items())) or "none"
        route = s.get("contact_route") or {}
        return (f"| {t['name']} | **{s.get('verdict', '')}** | {s.get('product', '')} | {md_link(m['name'], m['primary_source']) if m.get('primary_source') else (m.get('name') or 'none found')} "
                f"({m.get('status') or 'unknown'}) | {sig} | {s.get('people_found', 0)} | {md_link(route['kind'], route['url']) if route.get('url') else 'none published'} | {t['why']} | {t['todo'] or 'none'} |")
    out["speakers"] = table([speakers_row(t) for t in sec("speakers")],
                            ("| Company | Verdict | Product | MCP (primary source) and its status | Sourced signals | People found (names are local only) | Public route | Why this verdict | To-do |", "|---|---|---|---|---|---|---|---|---|"))
    def f508_row(t):
        f = t.get("federal508") or {}
        n = f.get("postings_2026_10_31")
        hits = f.get("accessibility_titles_2026_10_31")
        return (f"| {t['name']} | {f.get('kind', '')} | **{f.get('verdict', '')}** | {f.get('system') or '-'} | {cells(t)} | {n if n is not None else '-'} | "
                f"{hits if hits is not None else '-'} | {t['why']} | {t['todo'] or 'none'} |")
    out["federal508"] = table([f508_row(t) for t in sec("federal508")],
                              ("| Employer | Kind | Verdict | System | Board or careers page | Postings 2026-10-31 | Titles with a 508 or accessibility phrase | Why this verdict; what answered | To-do |", "|---|---|---|---|---|---|---|---|---|"))
    out["removed"] = table([f"| {t['name']} | {t['removed']['on'] or 'earlier'} | {t['removed']['entry'].get('reason', '')} |" for t in T if t["status"] == "removed"],
                           ("| Removed | On | Reason, as recorded |", "|---|---|---|"))
    return out


def splice(md, tables):
    for name, body in tables.items():
        pat = re.compile(rf"(<!-- targets:{name} -->\n)(.*?)(\n<!-- /targets:{name} -->)", re.S)
        if not pat.search(md):
            continue
        md = pat.sub(lambda m: m.group(1) + body + m.group(3), md)
    return md


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    doc = targets_doc()
    jobs = [("sources.json", derive_sources, None), ("faculty_config.json", derive_faculty, ["watch_schools"]), ("biolabs.json", derive_biolabs, ["seeds", "unreadable"])]
    drift = []
    for name, fn, keys in jobs:
        path = lp.config(name)
        cur = load(path)
        old_text = open(path, encoding="utf-8").read()
        new = dumps(fn(doc, cur)) if keys is None else replace_keys(old_text, fn(doc, cur), keys)
        if new != old_text:
            drift.append(name)
            if not a.check:
                open(path, "w", encoding="utf-8").write(new)
    mdp = os.path.join(lp.ROOT, "TARGETS.md")
    if os.path.exists(mdp):
        cur = open(mdp, encoding="utf-8").read()
        new = splice(cur, derive_tables(doc))
        if new != cur:
            drift.append("TARGETS.md")
            if not a.check:
                open(mdp, "w", encoding="utf-8").write(new)
    if a.check:
        print("in step with targets.json" if not drift else "DIFFERS from targets.json: " + ", ".join(drift))
        return 1 if drift else 0
    print("wrote: " + (", ".join(drift) if drift else "nothing to change"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
