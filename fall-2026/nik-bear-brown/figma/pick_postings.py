#!/usr/bin/env python3
"""Copy chosen postings out of one saved Figma jobs file into a readable JSON + Markdown pair.

    python3 figma/pick_postings.py figma/figma-jobs-2026-09-23.json figma/professor-bear-figma \
        6176134004 6114301004

Writes <out>.json (indented, for checking) and <out>.md (for reading). Each posting keeps
its id, title, location, link, dates, and department, plus the posting text as plain text
(Greenhouse sends it as escaped HTML). Offline, standard library only. Choosing which ids
are relevant is the person's call; this script only copies them.
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import find_roles  # the same word lists and matcher as the scan


def plain(content):
    raw = html.unescape(html.unescape(content or ""))  # Greenhouse double-escapes
    raw = re.sub(r"<\s*(br|/p|/li|/h\d)\s*/?>", "\n", raw, flags=re.I)
    raw = re.sub(r"<\s*li[^>]*>", "- ", raw, flags=re.I)
    raw = re.sub(r"<[^>]+>", "", raw)
    lines = [re.sub(r"[ \t ]+", " ", l).strip() for l in raw.splitlines()]
    return "\n".join(l for l in lines if l)


def stated(text):
    terms = "full-time (stated)" if re.search(r"full[- ]time", text, re.I) else "not stated in the posting"
    m = re.search(r"(Annual|Hourly) Base (?:Salary|Pay) Range:\s*(\$[\d,.]+)\s*[—–-]\s*(\$[\d,.]+)", text)
    pay = f"{m.group(2)}–{m.group(3)} ({m.group(1).lower()} base)" if m else None
    travel = re.search(r"travel(ing)? up to \d+%", text, re.I)
    return terms, pay, (travel.group(0) if travel else None)


def main(src, out, ids):
    with open(src, encoding="utf-8") as f:
        jobs = {str(j["id"]): j for j in json.load(f)["jobs"]}
    missing = [i for i in ids if i not in jobs]
    if missing:
        sys.exit(f"not in {src}: {', '.join(missing)}")
    picked = []
    for i in ids:
        j = jobs[i]
        text = plain(j.get("content"))
        terms, pay, travel = stated(text)
        picked.append({
            "id": j["id"], "title": j["title"].strip(), "location": j["location"]["name"],
            "department": [d["name"] for d in j.get("departments", [])],
            "url": j["absolute_url"], "first_published": j.get("first_published"),
            "updated_at": j.get("updated_at"),
            "terms": terms, "pay": pay, "travel": travel,
            "matched_words": {  # record: what the scan in find_roles.py matched, not a judgment of fit
                "role_words_in_title": find_roles.find(find_roles.ROLE_TITLE, j["title"]),
                "topic_words_in_text": find_roles.find(find_roles.TOPIC_TEXT, text),
                "flexible_terms_in_text": find_roles.find(find_roles.FLEX_TEXT, text + " " + j["title"]),
            },
            "posting_text": text.splitlines(),  # one line per list item, so it reads on GitHub
        })
    record = {"source_file": src, "count": len(picked), "postings": picked}
    with open(out + ".json", "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, ensure_ascii=False)
        f.write("\n")
    md = [f"# Chosen Figma postings — from `{src}`", ""]
    for p in picked:
        md += [f"## {p['title']}", "",
               f"- **Where:** {p['location']} · **Department:** {', '.join(p['department'])}",
               f"- **Terms:** {p['terms']}" + (f" · **Travel:** {p['travel']}" if p["travel"] else ""),
               f"- **Pay:** {p['pay'] or 'not stated'}",
               "- **Matched words (from the scan):** " + "; ".join(f"{k.replace('_', ' ')}: {', '.join(v) or 'none'}" for k, v in p["matched_words"].items()),
               f"- **Posted:** {p['first_published']} · **Updated:** {p['updated_at']}",
               f"- **Link:** {p['url']}", "", "<details><summary>Full posting text</summary>", "",
               "\n\n".join(p["posting_text"]), "", "</details>", ""]
    with open(out + ".md", "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"wrote {out}.json and {out}.md ({len(picked)} postings)")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit("usage: pick_postings.py <figma-jobs-YYYY-MM-DD.json> <out-prefix> <id> [<id> …]")
    main(sys.argv[1], sys.argv[2], sys.argv[3:])
