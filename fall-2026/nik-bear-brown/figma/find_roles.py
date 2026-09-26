#!/usr/bin/env python3
"""Find advocate / education roles and flexible work terms in one saved Figma jobs file.

    python3 figma/find_roles.py figma/figma-jobs-2026-09-23.json

Standard library only, offline, reads the saved file and nothing else. Prints a Markdown
report. Every row is a word match in the posting, shown with the words around it, so a
person can judge it. Nothing here decides whether a job is a good fit.
"""
import html
import json
import re
import sys

# Role words: looked for in the posting TITLE.
ROLE_TITLE = ["advocate", "educator", "education", "enablement", "evangelist",
              "developer relations", "community", "instructor", "trainer", "curriculum"]
# Topic words: looked for in the posting TEXT (the university / workshop side of the question).
TOPIC_TEXT = ["university", "universities", "campus", "student", "workshop",
              "curriculum", "educate", "education", "teach"]
# Flexible-terms phrases: looked for in the posting TEXT. Bare "contract" is left out on
# purpose: at Figma it appears only as "contract negotiation(s)" or "contract modifications".
FLEX_TEXT = ["part-time", "part time", "contract role", "contract position", "contractor role",
             "temporary", "seasonal", "fixed-term", "fixed term", "freelance", "summer", "hourly"]


def text_of(job):
    raw = html.unescape(html.unescape(job.get("content") or ""))  # Greenhouse double-escapes
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", raw)).strip()


def find(words, text):
    lc = text.lower()
    # whole word, plural allowed: "workshop" also finds "workshops"
    return [w for w in words if re.search(rf"(?<![a-z]){re.escape(w)}s?(?![a-z])", lc)]


def around(text, word, width=70):
    m = re.search(re.escape(word), text, re.I)
    return "…" + text[max(0, m.start() - width):m.end() + width].replace("|", "/") + "…" if m else ""


def main(path):
    with open(path, encoding="utf-8") as f:
        jobs = json.load(f)["jobs"]
    out = [f"# Advocate, education, and flexible-terms scan — `{path}`", "",
           f"Postings in the file: **{len(jobs)}**. Every row below is a word match, not a judgment.", ""]

    role = [(j, find(ROLE_TITLE, j["title"])) for j in jobs]
    role = [(j, w) for j, w in role if w]
    out += ["## 1. Role words in the title", "", f"{len(role)} postings.", "",
            "| id | Title | Location | Words | Terms stated in the posting |", "|---|---|---|---|---|"]
    for j, w in role:
        t = text_of(j)
        terms = "full-time" if re.search(r"full[- ]time", t, re.I) else "not stated"
        pay = re.search(r"(Annual|Hourly) Base (Salary|Pay) Range:\s*\$[\d,]+\s*[—-]\s*\$[\d,]+", t)
        out.append(f"| {j['id']} | {j['title'].strip()} | {j['location']['name']} | {', '.join(w)} | "
                   f"{terms}{'; ' + pay.group(0) if pay else ''} |")

    topic = [(j, find(TOPIC_TEXT, text_of(j))) for j in jobs]
    topic = [(j, w) for j, w in topic if w]
    out += ["", "## 2. University / workshop / education words in the text", "", f"{len(topic)} postings.", "",
            "| id | Title | Words | First match, in context |", "|---|---|---|---|"]
    for j, w in topic:
        out.append(f"| {j['id']} | {j['title'].strip()} | {', '.join(w)} | {around(text_of(j), w[0])} |")

    flex = [(j, find(FLEX_TEXT, text_of(j) + " " + j["title"])) for j in jobs]
    flex = [(j, w) for j, w in flex if w]
    out += ["", "## 3. Flexible-terms words (part-time, contract, temporary, seasonal, summer, hourly…)", "",
            f"{len(flex)} postings.", "",
            "| id | Title | Words | First match, in context |", "|---|---|---|---|"]
    for j, w in flex:
        out.append(f"| {j['id']} | {j['title'].strip()} | {', '.join(w)} | {around(text_of(j) + ' ' + j['title'], w[0])} |")
    print("\n".join(out))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: find_roles.py <figma-jobs-YYYY-MM-DD.json>")
    main(sys.argv[1])
