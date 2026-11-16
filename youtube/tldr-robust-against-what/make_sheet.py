#!/usr/bin/env python3
"""make_sheet.py — writes beat_sheet.json for tldr-robust-against-what.

tldr skill (brutalist.art/skills/make/tldr). Section S4 of chapter 4
(youtube/tldr-sections-04-robustness.md): the disclosure template, Section 1 —
clean 94% in every row, robust 71 / 58 / 87 by attack class. The three rows are
the chapter's TEMPLATE values (a form with blanks), not a measured model; the
film captions them "template values — illustrative" once, small, and keeps the
caption on the stage. Every number is the chapter's own; asserted here and in
scenes.py; FACTCHECK.md carries the rows. Re-run, then audio, then ./art run.
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

SLUG = "tldr-robust-against-what"
TITLE = "Robust Against What?"
COURSE = "INFO 7375 · Computational Skepticism · Chapter 4"

# The chapter's disclosure template, Section 1 (§"Towards honest robustness disclosure").
CLEAN = 94
ROWS = [("white-box attack", "ε = 0.03", 71),            # L∞ white-box (FGSM / PGD), ε = 0.03
        ("transfer attack", "surrogate model", 58),      # surrogate trained on the same data
        ("natural shift", "time shift only", 87)]        # time-shift only, no attacker
assert all(0 < r < CLEAN for _, _, r in ROWS)
assert ROWS[2][2] > ROWS[0][2] > ROWS[1][2]              # 87 > 71 > 58: the rows do not order as "attack < no attack"
assert abs(2 * 0.03 - 0.06) < 1e-12                       # B17's hypothetical budget is the chapter's ε doubled (no value shown for it)
# NB: the chapter's transfer row names a surrogate, not an ε — its budget cell is itself unstated (FACTCHECK row 7).

def beat(bid, act, narration, shot, role=None, section=None, learn=None, lane="manim", proof="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": lane, "proof_gate": proof}
    if section is not None: b["section"] = section
    if role: b["role"] = role
    if learn: b["learn"] = learn
    b.update({"narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
              "voice": "am_onyx", "engine": "kokoro", "shot": shot})
    b.update(extra); return b

def manim(cls, intent, show, claim):
    return {"type": "GRAPHIC", "source": "own", "visual_intent": intent, "show": show, "manim": {"class": cls}, "motion_claim": claim}

def remotion(pattern, props, show):
    return {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}

beats = []

B00_N = ("Merhaba. This is Liam, in for Bear, with chapter four of INFO 7375, Computational Skepticism for AI, at Northeastern. "
         "This film is about one word on a vendor's slide: robust. "
         "Robustness is a profile, not a number: one row per attack class, at a stated budget. "
         "You'll watch a template table fill: three robust numbers under one word. "
         "The trap: letting the word stand in for the table.")
B00_EST = round(len(B00_N.split()) / 2.5, 1)
beats.append(beat("B00", "tldr · what", B00_N,
    remotion("ClaudeTldrWhat", {
        "eyebrow": "TL;DR", "heading": "What This Film Is About", "greeting": "Merhaba, Liam", "topic": COURSE,
        "question": "A vendor says the model is 94% accurate and robust. Robust against what?",
        "lines": ["Robustness is a profile, not a number: one row per attack class, at a stated budget.",
                  "Watch a template disclosure table fill: 94% clean in every row; robust 71, 58, 87.",
                  "The trap: letting one word, or one number, stand in for a table with blanks."],
        "cues": [round(B00_EST * f, 1) for f in (0.05, 0.40, 0.60, 0.88)], "durationSeconds": B00_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "'TL;DR.' wordmark; 'Merhaba, Liam'; the course line; heading"},
         {"at": 0.05, "event": "the question writes on"},
         {"at": 0.40, "event": "line 1 lands on 'a profile, not a number'"},
         {"at": 0.60, "event": "line 2 lands on 'watch a disclosure table fill'"},
         {"at": 0.88, "event": "line 3 lands on 'the trap'"}]),
    lane="bookend"))

B01_N = ("Why should you care? Every model card and vendor deck you read says robust, and the word arrives before the evidence does. "
         "Take the word, and you inherit whichever attack nobody tested. "
         "Ask against what, and a marketing sentence turns into a specification you can check. "
         "And it unlocks writing the robustness section of a deployment document yourself, honestly, blanks included.")
B01_EST = round(len(B01_N.split()) / 2.5, 1)
beats.append(beat("B01", "tldr · why", B01_N,
    remotion("ClaudeTldrWhy", {
        "eyebrow": "TL;DR", "heading": "Why You Should Care", "topic": COURSE,
        "lead": "Every model card and vendor deck you read says 'robust' — and the word arrives before the evidence does.",
        "lines": ["Take the word, and you inherit whichever attack nobody tested.",
                  "Ask 'against what?', and a marketing sentence becomes a specification you can check.",
                  "It unlocks writing the robustness section of a deployment document yourself — blanks included."],
        "cues": [round(B01_EST * f, 1) for f in (0.05, 0.38, 0.58, 0.80)], "durationSeconds": B01_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "page turn: same header, heading 'Why You Should Care'"},
         {"at": 0.05, "event": "the stake writes on"},
         {"at": 0.38, "event": "dash 1 on 'take the word'"},
         {"at": 0.58, "event": "dash 2 on 'ask against what'"},
         {"at": 0.80, "event": "dash 3 on 'unlocks'"}]),
    lane="bookend", qc={"sparse_by_design": True, "sparse_reason": "TL;DR card two — text lands on cues by design."}))

beats.append(beat("B02", "the question",
    "The question this film is really asking: robust against what? Not 'is it robust' — a yes or no is the trap. "
    "The word has no slot for the attack, the budget, or the number.",
    remotion("BrutalistHesitantWriter", {
        "text": "94% accurate, and robust.\nIs the model robust?",
        "triggerWords": "Is the model robust", "replacementWords": "Robust against what",
        "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
        "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types '94% accurate, and robust.'"},
         {"at": 0.35, "event": "types 'Is the model robust?'; backspaces the phrase → 'Robust against what?' on the spoken correction"},
         {"at": 0.85, "event": "caret holds"}]),
    lane="bookend", lead_silence_s=0.8,
    motion_claim="The writer types the naive yes/no question and corrects the phrase that makes it the wrong question.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}))

B03_N = ("Four words you'll hear. Clean accuracy: the score on untouched test inputs. "
         "Perturbation budget, epsilon: how far any one input value may move. "
         "Transfer attack: a perturbation built on a stand-in model, aimed at the real one. "
         "Distribution shift: the world drifting from the training data, no attacker required.")
B03_EST = round(len(B03_N.split()) / 2.5, 1)
beats.append(beat("B03", "terms", B03_N,
    remotion("ClaudeDefinitions", {
        "title": "Terms In This Film",
        "terms": [{"term": "clean accuracy", "meaning": "the score on untouched test inputs — the number the vendor quotes"},
                  {"term": "perturbation budget", "meaning": "the most any single input value is allowed to move — no pixel shifts past it"},
                  {"term": "transfer attack", "meaning": "a perturbation built on a stand-in model, then aimed at the real one"},
                  {"term": "distribution shift", "meaning": "the world drifts away from the training data; no attacker required"}],
        "durationSeconds": B03_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'clean accuracy' lands, terracotta"}, {"at": 0.36, "event": "'perturbation budget' lands; first settles"},
         {"at": 0.58, "event": "'transfer attack' lands"}, {"at": 0.80, "event": "'distribution shift' lands"}]),
    lane="bookend", proof="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: prerequisites only — 'profile' (the film's answer) is earned in B18."}))

# ── LEARN section 1 (B10–B19) ────────────────────────────────────────────────
beats.append(beat("B10", "learn 1",
    "One slide. Ninety-four percent accurate, and robust. The ninety-four has a bar; you can see how tall it is. The other word has nothing. "
    "Robust — against what? Against a pixel push nobody can see? Against a stranger holding a copy of your training data? Against next quarter? "
    "The slide doesn't say. Let's make it say.",
    manim("B10_TheSlide",
          "The vendor's sentence in serif at centre: '94% accurate, and robust.' A single ink bar grows to 94 beneath the number, labelled 94%; a terracotta dot lands beside the word 'robust'; the question 'robust against what?' writes below.",
          [{"at": 0.05, "event": "the sentence lands"}, {"at": 0.2, "event": "the 94 bar grows under the number"},
           {"at": 0.45, "event": "terracotta dot beside 'robust' on 'the other word'"}, {"at": 0.75, "event": "'robust against what?' writes"}],
          "The bar is the persistent object (it becomes row one's clean bar); the word has no bar — that gap is the section."),
    role="HOOK", section=1,
    learn={"question": "A slide says 94% accurate and robust. What does the second word measure?",
           "action": "Give the number its bar; look for the word's bar.",
           "observation": "The number has a height; the word has nothing to point at.",
           "inference": "'Robust' has no referent until an attack and a budget are named.",
           "next_question": "What does one named attack do to the 94?"}))

beats.append(beat("B11", "learn 1",
    "Row one. A white-box attack: the attacker holds the weights, and may nudge every pixel by at most epsilon, zero point zero three. "
    "The clean bar stays at ninety-four. The robust bar — accuracy on the attacked inputs — lands at seventy-one. "
    "Same model, same test set. One row, one attack, one budget, one number.",
    manim("B11_WhiteBox",
          "The sentence shrinks to a dim claim line top-left; the 94 bar slides into row one's clean slot and turns dim; the header and legend land (attack class · budget · clean · robust at budget); row one's labels 'white-box attack' and 'ε = 0.03' write; the robust bar grows to 71 in ink with '71%' and a terracotta dot beside it; the caption 'template values — illustrative' lands bottom-left.",
          [{"at": 0.05, "event": "sentence to the claim line; the bar slides into row one"}, {"at": 0.2, "event": "header, legend, row-one labels"},
           {"at": 0.5, "event": "robust bar grows to 71 on 'lands at seventy-one'"}, {"at": 0.85, "event": "dot beside 71%; illustrative caption"}],
          "The first instance: the same bar, now in a row with an attack class and a budget; the robust bar grows to its own height."),
    role="INSTANCE", section=1,
    learn={"question": "What does one named attack, at a named budget, do to the 94?",
           "action": "Fill row one: white-box, ε = 0.03; grow the robust bar.",
           "observation": "Clean stays 94; robust at this budget is 71.",
           "inference": "A robust accuracy is a number in a row: attack class, budget, value.",
           "next_question": "Does a different attack class give the same number?"}))

beats.append(beat("B12", "learn 1",
    "Row two. A transfer attack. The attacker never saw this model. They trained a stand-in on the same data, built the perturbation there, and aimed it here. "
    "Clean: still ninety-four. Robust, in this template: fifty-eight. "
    "Two rows, two numbers. Nothing in row one told you row two.",
    manim("B12_Transfer",
          "Row two's labels 'transfer attack' / 'surrogate model' write; its clean bar grows to 94 (dim) and its robust bar to 58 (ink) with '58%'; the terracotta dot moves to 58; a dim caption bottom-right: 'the attacker never saw the model'.",
          [{"at": 0.05, "event": "row-two labels"}, {"at": 0.4, "event": "clean bar to 94; robust bar to 58 on 'fifty-eight'"},
           {"at": 0.7, "event": "dot beside 58%"}, {"at": 0.85, "event": "caption: the attacker never saw the model"}],
          "The second parametrized instance: vary the attack class, replay the fill; 58 is not 71."),
    role="INSTANCE", section=1,
    learn={"question": "Does a different attack class give the same number?",
           "action": "Fill row two: transfer, surrogate model; grow the bars.",
           "observation": "Clean 94 again; robust 58 — a different number, though the attacker never touched the model.",
           "inference": "Each attack class gets its own robust number; one row does not predict another.",
           "next_question": "So can the vendor fold these back into one word?"}))

beats.append(beat("B13", "learn 1",
    "Now the vendor's move. Take those two bars and fold them back into one word. Robust. "
    "Watch what happens to the numbers. They're gone. Which one was it — seventy-one? Fifty-eight? The word has no slot for the answer. "
    "It sounds like evidence. It is a confident, well-formed word standing in for evidence it does not carry. The fluency trap, in a lab coat.",
    manim("B13_OneWord",
          "The two robust bars and their labels slide together and merge into one ink bar between the rows, labelled with the single word 'robust' (no number); a terracotta X lands beside the word; caption bottom-right: 'the fluency trap in a lab coat'.",
          [{"at": 0.1, "event": "the two robust bars slide together and merge on 'fold them back'"}, {"at": 0.35, "event": "the labels vanish; 'robust' replaces them"},
           {"at": 0.6, "event": "X beside 'robust' on 'no slot for the answer'"}, {"at": 0.9, "event": "caption lands"}],
          "The natural wrong turn walked to its limit: the merge is lossy on screen — two numbers become none."),
    role="NAIVE", section=1,
    learn={"question": "Can two robust numbers be summarized by one word?",
           "action": "Merge the two bars into one labelled 'robust'.",
           "observation": "The numbers disappear; the word cannot say which row it came from.",
           "inference": "The single word is not a summary; it is a deletion.",
           "next_question": "What arrangement keeps every number where it belongs?"}))

beats.append(beat("B14", "learn 1",
    "Here's the reframe. Unfold it. Each row is its own axis. A number lives in its row, with its attack class and its budget, and never leaves it. "
    "That is the representation: not a score, a profile. "
    "Now a third row, and this one has no attacker at all. Natural drift: the same model, inputs from a later time window. Clean, ninety-four again. Robust — blank.",
    manim("B14_UnfoldRows",
          "The merged bar splits back into 71 and 58 in their rows (the reverse morph); row three's labels 'natural shift' / 'time shift only' write; its clean bar grows to 94 (dim); its robust slot shows a dim '?'; caption bottom-right: 'no attacker; the world moved'.",
          [{"at": 0.05, "event": "the merged bar splits back into rows one and two"}, {"at": 0.35, "event": "'a profile' — the rows read as separate axes"},
           {"at": 0.6, "event": "row three: labels, clean bar to 94"}, {"at": 0.85, "event": "the robust slot shows '?'"}],
          "The representation arrives: rows as separate axes; the third row's robust value is deliberately withheld for the predict beat."),
    role="SHIFT", section=1,
    learn={"question": "What arrangement keeps every number where it belongs?",
           "action": "Unfold the merged bar back into rows; add a row with no attacker.",
           "observation": "Each row carries its class, its budget and its number; row three is open.",
           "inference": "Robustness is a profile — one axis per row — not a score.",
           "next_question": "With no attacker at all, where does row three land?"}))

beats.append(beat("B15", "learn 1",
    "Before it lands — commit. The insider got the model down to seventy-one. The stranger, fifty-eight. "
    "Now nobody attacks; the world just moves. Where does row three land? Above seventy-one? Between? Below fifty-eight? "
    "And the harder question: could the two attack rows have told you?",
    manim("B15_Commit",
          "Two dim tick marks land on row three's scale at 58 and 71 (the guides); a terracotta dot sits beside the '?'; the question 'above 71, between, or below 58?' writes lower-left; everything else holds still.",
          [{"at": 0.1, "event": "guide ticks at 58 and 71 on row three"}, {"at": 0.3, "event": "dot beside the '?'"},
           {"at": 0.5, "event": "the question writes"}, {"at": 0.7, "event": "HOLD — nothing moves on 'commit'"}],
          "The predict-before-reveal beat: guides drawn, value withheld."),
    role="INSTANCE", section=1, predict=True,
    learn={"question": "Where does the no-attacker row land relative to 58 and 71?",
           "action": "Draw the guides; hold the picture.",
           "observation": "The viewer commits to a band.",
           "inference": "A prediction makes the reveal evidence about whether rows predict each other.",
           "next_question": "Reveal."}))

beats.append(beat("B16", "learn 1",
    "Eighty-seven, in this template. Above both. And no, the attack rows could not have told you: surviving an attacker does not guarantee surviving time, or the reverse. "
    "Now hand the slide the rest of the form. What was not tested? Blank. What will you watch in production, and when do you pull it? Blank. "
    "The word has nothing to write here.",
    manim("B16_RowThreeLands",
          "Row three's robust bar grows to 87 with '87%' — past both guide ticks; then the collision: the dim claim line's word 'robust' slides down and transforms into two ghost blank fields beneath the table — 'residual risk' and 'monitoring trigger' — which stay empty; a terracotta dot beside 87%.",
          [{"at": 0.0, "event": "the bar grows to 87, past both ticks"}, {"at": 0.3, "event": "dot beside 87% on 'above both'"},
           {"at": 0.5, "event": "the claim's 'robust' morphs into two blank fields on 'the rest of the form'"}, {"at": 0.9, "event": "the blanks hold, empty"}],
          "The aha is the morph: the reveal breaks the one-number reading, and the word meets the form and fills nothing."),
    role="TRANSFORM", section=1,
    learn={"question": "Where does row three land, and what else does the form ask?",
           "action": "Land 87; hand the sentence the residual-risk and monitoring fields.",
           "observation": "87 sits above both attack rows; the two fields stay blank.",
           "inference": "The rows do not predict each other, and a word cannot fill a field.",
           "next_question": "Is a robust number at least fixed once measured?"}))

beats.append(beat("B17", "learn 1",
    "One more thing, and it's the part people skip. Change one thing in row one: the budget. Same attack, double the push. "
    "Is it still seventy-one? Nobody knows. That number was measured at zero point zero three, and it stays there. "
    "A robust accuracy is a number at a budget. Move the budget, and you owe a new measurement.",
    manim("B17_MoveTheBudget",
          "Row one's budget label morphs 'ε = 0.03' → 'ε = 0.06'; its robust bar drains to a ghost bar and '71%' becomes '?'; a terracotta dot beside the new budget; then the budget morphs back to 0.03 and the bar refills to 71; caption bottom-right: 'a number at a budget'.",
          [{"at": 0.1, "event": "budget label → ε = 0.06 on 'double the push'"}, {"at": 0.3, "event": "robust bar drains; '?' on 'nobody knows'"},
           {"at": 0.65, "event": "budget back to 0.03; bar refills to 71"}, {"at": 0.9, "event": "caption lands"}],
          "Post-shift instance: hold everything, vary the budget — the number is bound to it (no invented value is shown)."),
    role="INSTANCE", section=1,
    learn={"question": "Is a robust number fixed once measured?",
           "action": "Double row one's budget and watch its number.",
           "observation": "The number cannot travel with the row; at a new budget it is unknown.",
           "inference": "A robust accuracy is a value AT a budget; the budget is part of the number.",
           "next_question": "Say the whole structure as a rule."}))

beats.append(beat("B18", "learn 1",
    "This deserves its name. Robustness is a profile, not a number. "
    "Section one: for each attack class, the budget, the clean accuracy, and the robust accuracy at that budget. "
    "Section two: the residual risk — what was not tested, in writing. Section three: the monitoring trigger — what you watch, and when a human steps in. "
    "A claim without this structure is not a claim.",
    manim("B18_NameIt",
          "The form gets its section labels: 'Section 1 · profile' over the table, 'Section 2 · residual risk' and 'Section 3 · monitoring trigger' beside the blanks; a bracket-free ink rail draws down the left edge joining the three sections; 'a profile, not a number' lands bold at right; caption: 'no structure, no claim'.",
          [{"at": 0.1, "event": "'a profile, not a number' lands"}, {"at": 0.3, "event": "'Section 1 · profile' over the table"},
           {"at": 0.55, "event": "sections 2 and 3 labelled beside the blanks; the rail draws"}, {"at": 0.9, "event": "caption: no structure, no claim"}],
          "The abstraction arrives as the name for the form the viewer watched fill: three sections, one structure."),
    role="ABSTRACTION", section=1,
    learn={"question": "What is the rule?",
           "action": "Label the three sections of the disclosure and join them with one rail.",
           "observation": "Profile, residual risk, monitoring trigger — the form has a shape.",
           "inference": "A robustness claim is this structure or it is not a claim.",
           "next_question": "So — the slide?"}))

beats.append(beat("B19", "learn 1",
    "Back to the slide. Ninety-four percent: that's the clean column, the one that never moved. Robust — against what? Now you can point. "
    "A white-box push at zero point zero three: seventy-one. A transfer attack: fifty-eight. A time shift: eighty-seven. And two blanks nobody filled. "
    "Not taught here: what each defense buys and what it costs. That's the next reading.",
    manim("B19_Payoff",
          "The dim claim line returns to a full-size sentence at the right; a terracotta dot travels from its '94%' down the clean column, then from its 'robust' down the robust column 71 → 58 → 87, then to the two blanks; an X lands beside 'robust'; boundary caption: 'not taught: what each defense costs'.",
          [{"at": 0.05, "event": "the sentence grows back"}, {"at": 0.25, "event": "dot from '94%' to the clean column on 'never moved'"},
           {"at": 0.45, "event": "dot walks the robust column 71 → 58 → 87 on the spoken numbers"}, {"at": 0.75, "event": "dot to the blanks; X beside 'robust'"},
           {"at": 0.92, "event": "boundary caption"}],
          "The HOOK's sentence and bar resolve against the filled form; the boundary is one dim line."),
    role="PAYOFF", section=1,
    learn={"question": "So — what does the slide's word measure?",
           "action": "Point the word at the rows, one by one.",
           "observation": "Three numbers, three rows, two blanks — and the 94 never moved.",
           "inference": "'Robust against what' has an answer only as a profile.",
           "next_question": ""}))

beats.append(beat("BVDT", "verdict",
    "Let's recap with Claude. Robust is not a number; it is a profile — one row per attack class, at a stated budget, clean and robust accuracy side by side. "
    "The rows are separate axes: seventy-one, fifty-eight and eighty-seven do not predict each other. "
    "Move the budget and the number expires. "
    "And the form has two more sections, residual risk and a monitoring trigger, that a single word never fills. A claim without this structure is not a claim.",
    remotion("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": TITLE,
        "artifactLines": ["Robustness is a profile, not a number: one row per attack class, at a stated budget.",
                          "The rows are separate axes — 71, 58 and 87 do not predict each other.",
                          "A robust accuracy is a number AT a budget; move the budget and the number expires.",
                          "Two more sections — residual risk, monitoring trigger — that one word never fills."]},
        [{"at": 0.0, "event": "artifact page opens"}, {"at": 0.2, "event": "four verdict lines land"}]),
    lane="bookend", lead_silence_s=0.5, qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}))

YT = ("You are reviewing a facial-recognition system proposed for a physical access-control door. The vendor claims the model is 'robust against adversarial examples.' "
      "Write five specific questions that would turn that claim into a usable specification, and for each question say what it tests. "
      "At least one question must ask for an attack class and a perturbation budget; at least one must ask what was NOT tested; "
      "and at least one must ask what will be monitored in production and what triggers a human review.")
beats.append(beat("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT + " "
    "Two things to look for. Does every question name something measurable — an attack class, a budget, a number — rather than asking how robust it is, again? "
    "And did it leave room for the blanks: what was not tested, and what gets watched.",
    remotion("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "INFO 7375 · YOUR TURN", "segment": "Turn The Claim Into A Spec",
        "command": YT, "runningText": "paste this into Claude…",
        "output": ["Check: every question names something measurable — a class, a budget, a number.",
                   "Check: it asked for the blanks — what was not tested, what gets watched."],
        "folderLabel": "@NikBearBrown", "modelLabel": "Fable 5", "effortLabel": "High"},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two rubric lines land"}]),
    lane="bookend"))

beats.append(beat("BOUT", "outro", f"{TITLE} At Nik Bear Brown.",
    remotion("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""},
             [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot. Liam reads the title, then 'At Nik Bear Brown'. No jingle."}]),
    lane="bookend", kind="outro_voice", tail_silence_s=1.0,
    hold_note="spoken outro + 1.0 s silent tail (apad into the mp3); no jingle (OUTRO-LOCK §Voice)"))

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "INFO 7375 · TL;DR", "skill": "tldr", "style_preset": "tldr",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "learn_canvas": "cream", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160, "caption_policy": "none",
    "audience": "INFO 7375 students reading chapter 4, and anyone who has read 'robust' on a model card and moved on",
    "course": "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University",
    "source_doc": "chapters/04-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md, §'Distribution shift, returning from Chapter 2' (Figure 4.5) and §'Towards honest robustness disclosure' (Sections 1–3 template); section S4 of youtube/tldr-sections-04-robustness.md",
    "sections": [{"n": 1, "title": "Robust Against What?", "key_case": "the disclosure template: clean 94% in every row; robust 71 (white-box, ε = 0.03) · 58 (transfer, surrogate model) · 87 (natural shift, time only) — template values, captioned illustrative"}],
    "greeting_language": "Turkish (Merhaba)",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "outro_policy": "OUTRO-LOCK §Voice: spoken title + 'At Nik Bear Brown', 1.0 s silent tail padded into the mp3, no jingle.",
    "bookloop_policy": "Course film: carries the INFO 7375 course credit (spoken in B00, on the cards' course line).",
    "tags": ["robustness", "adversarial examples", "distribution shift", "model cards", "INFO 7375", "computational skepticism", "3Blue1Brown style", "Claude", "Nik Bear Brown"]},
    "beats": beats}
out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"{len(beats)} beats → {out}")
