#!/usr/bin/env python3
"""Build the two draft sets (student form + key) from the bank and new_questions.py. Seeded; standard library only.
Run from this folder:  python3 build.py"""
import json, random, pathlib
import new_questions as N

HERE = pathlib.Path(__file__).resolve().parent
BANK = {q["id"]: q for q in next(v for v in json.load(open(HERE.parent / "question-bank/questions.json")).values() if isinstance(v, list))}
LABELS = "ABCDE"
CAUSATION_BANK_IDS = ["MA-ch06.52", "MA-ch06.58", "MA-ch06.60", "MA-ch06.72", "MA-ch06.75", "MA-ch06.76", "MA-ch06.77",
                      "MA-ch06.79", "MA-ch06.80", "MA-ch06.86"]

def from_bank(i):
    q = BANK[i]
    return dict(id=i, source=q["source"], section=f'chapter {q["chapter"]}', stem=q["stem"],
                st=[(s["text"], s["correct"], s["explanation"]) for s in q["statements"]], order=False)

def from_new(q, section):
    return dict(id=q["id"], source=q["source"], section=section, stem=q["stem"], st=list(q["st"]), order=True)

def build(slug, title, qs, seed, note):
    rnd = random.Random(seed)
    qs = list(qs); rnd.shuffle(qs)
    for q in qs:
        if q["order"]:
            rnd.shuffle(q["st"])
    head = (f"# INFO 7375 Computational Skepticism for AI: {title}\n\n**DRAFT FORM. {note} Not the real exam; not signed off by the instructor.**\n\n"
            f"{len(qs)} questions, 5 points each, {5*len(qs)} points. Name: ______________________\n\n"
            "**Scoring.** Five statements, each true or false, 1 point each. The student checks the statements they believe are true. "
            "A statement scores 1 point if it is checked and true, or unchecked and false; otherwise 0. Read every statement on its own "
            "and decide whether it is true by itself. Strong words (always, never, every, proves) are often what makes a statement false, "
            "but a strong-sounding statement is not false for sounding strong.\n\n---\n")
    keyhead = (f"# INFO 7375 Computational Skepticism for AI: {title}: KEY\n\nTotal {5*len(qs)} points. "
               "Statement key: T = true (check it), F = false (leave it blank).\n\n---\n")
    form, key = [head], [keyhead]
    for n, q in enumerate(qs, 1):
        stem = q["stem"]
        block = f"**{n}.** {stem}  *(5 points)*\n\n" + "\n".join(f"- [ ] {LABELS[i]}. {t}" for i, (t, c, w) in enumerate(q["st"])) + "\n"
        form.append(block)
        keys = " ".join(f"{LABELS[i]}={'T' if c else 'F'}" for i, (t, c, w) in enumerate(q["st"]))
        why = "\n".join(f"- {LABELS[i]} ({'true' if c else 'false'}): {w}" for i, (t, c, w) in enumerate(q["st"]))
        key.append(block + f"\n**Key:** {keys}  |  `{q['id']}`  |  *{q['section']}*  |  source: {q['source']}\n\n{why}\n")
    (HERE / f"{slug}.md").write_text("\n".join(form))
    (HERE / f"{slug}-KEY.md").write_text("\n".join(key))
    return qs

p = build("prompting-exam", "prompting practice exam", [from_new(q, "prompting") for q in N.PROMPTING], 7375,
          "Questions about writing prompts that name the quantity, supply the inputs, and can be checked.")
c = build("causation-rungs-1-2", "causation practice set: association and intervention",
          [from_bank(i) for i in CAUSATION_BANK_IDS] + [from_new(q, "causation, rungs 1 and 2") for q in N.CAUSATION], 7376,
          "Covers rung 1 (association), rung 2 (intervention) and why the difference matters. No counterfactuals.")
print(len(p), len(c))
