#!/usr/bin/env python3
"""check_narration.py - machine check of one deck's narration.json against its deck.json.

    python3 check_narration.py <extract/NN>

Exit 0 = PASS (warnings may remain: read them). Exit 2 = FAIL.
"""
import json
import re
import sys
from pathlib import Path

BODY_MIN, BODY_MAX = 16, 58          # words per body beat
BANNED = [r"\bthis chapter\b", r"\bthe chapter\b", r"\bthe book\b", r"\bthis deck\b", r"\bthe deck\b", r"\bthis slide\b",
          r"\bnext slide\b", r"\b(?<!changelog )slides?\b", r"\bclick (to|or|on|the|here|again)\b", r"\b(each|every|next|one|per) click\b", r"\bas we saw\b", r"\blast video\b", r"\bnext video\b",
          r"\bprevious video\b", r"\bvideo \w+ of\b", r"\bchapter (one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|\d+)\b",
          r"\bdelve\b", r"\bgame.?changer\b", r"\bunlock\b", r"\bdive in\b", r"\blet's dive\b", r"\bI am Bear\b", r"\bI'm Bear\b"]
BAD_CHARS = set("()[]{}|=%$→≠≈×÷<>+/\\*_#@&^~—–")


def words(s):
    return len(re.findall(r"[^\W_][\w'’-]*", s))


def lint(text, where, errs, warns):
    if re.search(r"\d", text):
        errs.append(f"{where}: digits in narration (spell every number as words): {text!r}")
    bad = sorted({c for c in text if c in BAD_CHARS})
    if bad:
        errs.append(f"{where}: characters the voice cannot say {bad}: {text!r}")
    for pat in BANNED:
        m = re.search(pat, text, re.I)
        if m:
            errs.append(f"{where}: banned phrase {m.group(0)!r}")
    if re.search(r"\b[A-Z]\b(?! [a-z])", text) and re.search(r"\bP of\b", text):
        warns.append(f"{where}: 'P of ...' is spoken badly; say 'the probability of ...'")


def main():
    d = Path(sys.argv[1])
    deck = json.loads((d / "deck.json").read_text())
    try:
        nar = json.loads((d / "narration.json").read_text())
    except Exception as e:  # noqa: BLE001
        print(f"FAIL: narration.json missing or not JSON: {e}")
        sys.exit(2)
    errs, warns = [], []
    global BODY_MAX
    BODY_MAX = int(nar.get("body_max", BODY_MAX))   # a film whose beats carry a worked example may raise the cap

    need = [(s["index"], st["k"]) for s in deck["slides"] for st in s["steps"]]
    texts = {(s["index"], st["k"]): " ".join(st["all_texts"] + [s["title"], s["notes"], s["source"]]) for s in deck["slides"] for st in s["steps"]}
    got = {}
    for b in nar.get("beats", []):
        key = (b.get("slide"), b.get("step"))
        if key in got:
            errs.append(f"beat {key} appears twice")
        got[key] = b
    for key in need:
        if key not in got:
            errs.append(f"missing beat for slide {key[0]} step {key[1]}")
    for key in got:
        if key not in need:
            errs.append(f"beat {key} does not exist in the deck")
    total = 0
    for key in need:
        b = got.get(key)
        if not b:
            continue
        t = (b.get("narration") or "").strip()
        n = words(t)
        total += n
        w = f"slide {key[0]} step {key[1]}"
        if n < BODY_MIN or n > BODY_MAX:
            errs.append(f"{w}: {n} words (allowed {BODY_MIN} to {BODY_MAX})")
        lint(t, w, errs, warns)
        for fig in b.get("figures", []) or []:
            if str(fig) not in texts[key]:
                errs.append(f"{w}: figure {fig!r} is not on the slide at this step")
        if not isinstance(b.get("figures", []), list):
            errs.append(f"{w}: figures must be a list")

    op = (nar.get("opening_summary") or "").strip()
    if not (8 <= words(op) <= 40):
        errs.append(f"opening_summary: {words(op)} words (allowed 8 to 40)")
    lint(op, "opening_summary", errs, warns)
    desc = (nar.get("opening_description") or "").strip()
    if not (3 <= len(desc) <= 64):
        errs.append(f"opening_description: {len(desc)} characters (allowed 3 to 64)")

    idea = nar.get("idea") or {}
    it = (idea.get("narration") or "").strip()
    if not it.startswith("Hallo. This is Liam, in for Bear."):
        errs.append("idea.narration must start exactly: 'Hallo. This is Liam, in for Bear.'")
    if not (35 <= words(it) <= 70):
        errs.append(f"idea.narration: {words(it)} words (allowed 35 to 70)")
    lint(it, "idea.narration", errs, warns)
    txt, trig, rep = idea.get("text") or "", idea.get("triggerWords") or "", idea.get("replacementWords") or ""
    if not trig or trig not in txt:
        errs.append("idea.triggerWords must appear verbatim in idea.text")
    if not rep:
        errs.append("idea.replacementWords is empty")
    for name, v in (("triggerWords", trig), ("replacementWords", rep)):
        if v and v[-1] in ".,;:!?":
            errs.append(f"idea.{name} must not end in punctuation")
    if len(txt) > 70 or txt.count("\n") > 1:
        errs.append("idea.text: at most two lines and 70 characters")
    if rep and len(txt) - len(trig) + len(rep) > 80:
        errs.append("idea.text after the correction is too long (over 80 characters)")

    rl = nar.get("recap_lines") or []
    if len(rl) != 6:
        errs.append(f"recap_lines: need exactly 6, got {len(rl)}")
    for i, line in enumerate(rl):
        if not (4 <= words(line) <= 16) or len(line) > 84:
            errs.append(f"recap_lines[{i}]: {words(line)} words, {len(line)} characters (allowed 4 to 16 words, 84 characters)")
        lint(line, f"recap_lines[{i}]", errs, warns)

    yt = nar.get("your_turn") or {}
    cmd = (yt.get("command") or "").strip()
    if not (35 <= words(cmd) <= 75):
        errs.append(f"your_turn.command: {words(cmd)} words (allowed 35 to 75)")
    lint(cmd, "your_turn.command", errs, warns)
    ch = yt.get("checks") or []
    if len(ch) != 2 or not all(c.startswith("Check: ") and len(c) <= 78 for c in ch):
        errs.append("your_turn.checks: exactly two lines, each starting 'Check: ' and at most 78 characters")
    seg = (yt.get("segment") or "").strip()
    if not (3 <= len(seg) <= 40):
        errs.append("your_turn.segment: 3 to 40 characters, Title Case")

    for w in warns:
        print("WARN ", w)
    for e in errs:
        print("ERROR", e)
    est = total / 2.55
    print(f"{d.name}: {len(need)} body beats, {total} words, about {est/60:.1f} min of body narration; {len(errs)} errors, {len(warns)} warnings")
    print("PASS" if not errs else "FAIL")
    sys.exit(0 if not errs else 2)


if __name__ == "__main__":
    main()
