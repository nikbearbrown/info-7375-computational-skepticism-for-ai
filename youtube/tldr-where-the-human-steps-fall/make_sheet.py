#!/usr/bin/env python3
"""make_sheet.py — writes beat_sheet.json for tldr-where-the-human-steps-fall.

tldr skill (brutalist.art/skills/make/tldr). Section S3 of chapter 9
(youtube/tldr-sections-09-delegation-trust.md): the Paper Summarizer's six-step
Boondoggle Score — Claude owns 2 · 3 · 5, a human owns 1 · 4 · 6 — and why the
human steps are the ones that LOOK like review. No equation lands (the chapter
states the sort in words), so there is no TANGENT.

The representation: under each step, a five-row grid (the five Boondoggle
questions). The chapter prints the questions and a per-step justification but no
per-step grid; the cells are the film's reading of the chapter's own step text
(STEP 1–6 + "What the Boondoggle Score reveals" + "The shape of the rest"),
captioned "cells: our reading of the text" on screen. FACTCHECK.md carries a
row per dark cell. The "looks like work" bars are schematic (captioned). The
paper sentence in B11 is constructed around the chapter's own qualifier.

After ANY re-run of this file, run lock_cards.py (it restores the audio lock).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

SLUG = "tldr-where-the-human-steps-fall"
TITLE = "Where the Human Steps Fall"
COURSE = "INFO 7375 · Computational Skepticism · Chapter 9"

# ── the chapter's Score summary (§"Generating the Boondoggle Score") ──
STEPS = ["taxonomy", "parse", "extract", "audit", "format", "sign-off"]
OWNER = {1: "human", 2: "AI", 3: "AI", 4: "human", 5: "AI", 6: "human"}
assert sorted(k for k, v in OWNER.items() if v == "AI") == [2, 3, 5]
assert sorted(k for k, v in OWNER.items() if v == "human") == [1, 4, 6]
HANDOFFS = [(3, 4), (5, 6)]                                   # the two highest-risk handoffs, both AI → human
assert all(OWNER[a] == "AI" and OWNER[b] == "human" for a, b in HANDOFFS)
ROWS = ["verification", "stakes", "distribution", "reversibility", "audit trail"]
# dark = a high-risk answer (our reading of the chapter's own step text; FACTCHECK rows 9–15)
DARK = {1: {"stakes", "distribution"}, 2: set(), 3: set(), 4: {"verification", "stakes", "distribution"},
        5: set(), 6: {"verification", "stakes", "reversibility"}}
assert all((len(DARK[s]) > 0) == (OWNER[s] == "human") for s in OWNER)   # the grid's dark columns ARE the human steps
QUALIFIER = "on the training set only"
assert len(QUALIFIER.split()) == 5                            # "five words" (B12)
SPOT = (1, 5)                                                 # one in five HIGH entries spot-checked

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

B00_N = ("Bula. This is Liam, in for Bear, with chapter nine of INFO 7375, Computational Skepticism for AI, at Northeastern. "
         "This film is about where the human steps fall. "
         "They fall where checking is expensive and a wrong answer costs, not where the work looks heavy. "
         "You'll watch a six-step summarizer scored on five questions. "
         "The trap: the AI does the hard part, I glance at the result.")
B00_EST = round(len(B00_N.split()) / 2.5, 1)
beats.append(beat("B00", "tldr · what", B00_N,
    remotion("ClaudeTldrWhat", {
        "eyebrow": "TL;DR", "heading": "What This Film Is About", "greeting": "Bula, Liam", "topic": COURSE,
        "question": "The AI parses, extracts and formats. Why does a human own the steps that look like review?",
        "lines": ["Human steps fall where checking is expensive and a wrong answer costs — not where work looks heavy.",
                  "Watch a six-step paper summarizer scored on five questions, one step at a time.",
                  "The trap: “the AI does the hard part, and I glance at the result.”"],
        "cues": [round(B00_EST * f, 1) for f in (0.05, 0.45, 0.68, 0.84)], "durationSeconds": B00_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "'TL;DR.' wordmark; 'Bula, Liam'; the course line; heading"},
         {"at": 0.05, "event": "the question writes on"},
         {"at": 0.45, "event": "line 1 lands on 'they fall where checking is expensive'"},
         {"at": 0.68, "event": "line 2 lands on 'you'll watch'"},
         {"at": 0.84, "event": "line 3 lands on 'the trap'"}]),
    lane="bookend"))

B01_N = ("Why should you care? Every AI pipeline splits its steps between a model and people, usually by what looks like work. "
         "Split it that way, and a dropped qualifier sails through to a reader. "
         "Score each step, and you can say in writing why every human step is human. "
         "And that written reason is exactly what a review committee asks you for.")
B01_EST = round(len(B01_N.split()) / 2.5, 1)
beats.append(beat("B01", "tldr · why", B01_N,
    remotion("ClaudeTldrWhy", {
        "eyebrow": "TL;DR", "heading": "Why You Should Care", "topic": COURSE,
        "lead": "Every AI pipeline you build splits its steps between a model and people — usually by what looks like work.",
        "lines": ["Split it by effort, and a dropped qualifier sails through to a reader.",
                  "Score each step, and you can say in writing why every human step is human.",
                  "That written reason is exactly what a review committee asks you for."],
        "cues": [round(B01_EST * f, 1) for f in (0.05, 0.45, 0.65, 0.84)], "durationSeconds": B01_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "page turn: same header, heading 'Why You Should Care'"},
         {"at": 0.05, "event": "the stake writes on"},
         {"at": 0.45, "event": "dash 1 on 'split it that way'"},
         {"at": 0.65, "event": "dash 2 on 'score each step'"},
         {"at": 0.84, "event": "dash 3 on 'that written reason'"}]),
    lane="bookend", qc={"sparse_by_design": True, "sparse_reason": "TL;DR card two — text lands on cues by design."}))

beats.append(beat("B02", "the question",
    "The real question: which steps are cheap to check, and cheap to undo? Not which look like the most work. "
    "Effort is what the AI saves you. It says nothing about where it fails you.",
    remotion("BrutalistHesitantWriter", {
        "text": "Hand the AI the steps that\nlook like the most work?",
        "triggerWords": "look like the most work", "replacementWords": "are cheap to check and undo",
        "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
        "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'Hand the AI the steps that'"},
         {"at": 0.3, "event": "types the rest; backspaces 'look like the most work' → 'are cheap to check and undo' on the spoken correction"},
         {"at": 0.85, "event": "caret holds on the corrected question"}]),
    lane="bookend", lead_silence_s=0.8,
    motion_claim="The writer types the naive effort question and corrects the phrase that makes it the wrong question.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}))

B03_N = ("Four terms. A handoff: where one step's output passes to the next, often from AI to human. "
         "A confidence tag: high, medium or low, the model's own label on how sure it is. "
         "The solve-verify asymmetry: some answers are far cheaper to check than to produce. "
         "And a supervisory capacity: a named human job that leaves a record.")
B03_EST = round(len(B03_N.split()) / 2.5, 1)
beats.append(beat("B03", "terms", B03_N,
    remotion("ClaudeDefinitions", {
        "title": "Terms In This Film",
        "terms": [{"term": "handoff", "meaning": "where one step's output passes to the next step — often from AI to human"},
                  {"term": "confidence tag", "meaning": "HIGH, MEDIUM or LOW: the model's own label on how sure an extraction is"},
                  {"term": "solve–verify asymmetry", "meaning": "some answers are far cheaper to check than to produce"},
                  {"term": "supervisory capacity", "meaning": "a named human job — plausibility auditing, say — that leaves a record"}],
        "durationSeconds": B03_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'handoff' lands, terracotta"}, {"at": 0.35, "event": "'confidence tag' lands; first settles"},
         {"at": 0.6, "event": "'solve–verify asymmetry' lands"}, {"at": 0.8, "event": "'supervisory capacity' lands"}]),
    lane="bookend", proof="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: prerequisites only — the Boondoggle questions (the film's answer) are earned in B18."}))

# ── LEARN section 1 (B10–B19) ────────────────────────────────────────────────
beats.append(beat("B10", "learn 1",
    "Here's a pipeline. You paste in a research paper, and it hands back a summary where every claim links to a passage in the source. "
    "Six steps: a section taxonomy, parsing, claim extraction, an audit, formatting, and a sign-off. "
    "Three of them look like real work. Three look like somebody glancing at it. "
    "Now the chapter's score assigns the owners, and the humans get the three short bars. "
    "Why would you keep the steps that look easiest?",
    manim("B10_SixSteps",
          "A paper icon at left feeds a row of six step boxes (taxonomy · parse · extract · audit · format · sign-off) that land one per spoken name; under each a schematic 'looks like work' bar grows — tall under 2, 3, 5, short under 1, 4, 6; then boxes 1, 4, 6 fill ink (human-owned) while 2, 3, 5 stay outlined (AI); the question 'three short bars, three human steps — why?' writes in the left column; a terracotta dot beside it.",
          [{"at": 0.05, "event": "paper icon and arrow"}, {"at": 0.3, "event": "six boxes land on their names"},
           {"at": 0.55, "event": "bars grow: tall 2 · 3 · 5, short 1 · 4 · 6"}, {"at": 0.75, "event": "boxes 1 · 4 · 6 fill: human"},
           {"at": 0.9, "event": "the question lands with a dot"}],
          "The six boxes and the bars are the persistent objects; the question is unsolved."),
    role="HOOK", section=1,
    learn={"question": "Why does a human own the three steps that look like the least work?",
           "action": "Lay out the six steps with how much each looks like work, then reveal the owners.",
           "observation": "The human-owned steps are exactly the short bars.",
           "inference": "Whatever decides ownership, it is not how much a step looks like work.",
           "next_question": "What does an AI step actually hand over? Look at step 3."}))

beats.append(beat("B11", "learn 1",
    "Zoom in on step three, claim extraction. The paper says: the model outperformed baselines on the training set only. "
    "The AI pulls out the core claim, the model outperformed baselines, tags it low, and attaches a citation copied word for word. "
    "Step three's rule is that citations are copied, never paraphrased. So checking one is a search. Seconds. And it passes.",
    manim("B11_StepThree",
          "Bars fade; step 3's box thickens. A panel: 'paper:' with the constructed sentence; 'claim:' with the extracted claim and a LOW tag; 'citation:' with the verbatim excerpt; an ink match bar sweeps under the citation and a matching bar under the paper sentence; a check mark and 'found word for word' land with a terracotta dot.",
          [{"at": 0.1, "event": "step 3 box thickens; the paper sentence lands"}, {"at": 0.4, "event": "claim + LOW tag + citation land"},
           {"at": 0.7, "event": "the match bars sweep — a search"}, {"at": 0.88, "event": "check: found word for word"}],
          "First instance: an AI step's handoff check is cheap — a string search."),
    role="INSTANCE", section=1,
    learn={"question": "What does it take to check an AI step?",
           "action": "Run step 3's handoff check on one extraction: is the citation verbatim?",
           "observation": "A search confirms it in seconds, and it passes.",
           "inference": "Step 3's own check is cheap to verify.",
           "next_question": "The check passed. Is the claim right?"}))

beats.append(beat("B12", "learn 1",
    "Step four takes every low or flagged entry and opens the source. The citation is fine. The claim isn't. "
    "It dropped five words, on the training set only, and those five words change what the paper found. "
    "No search catches that. It takes someone who knows how results get reported in this field. Corrected. "
    "And one in five of the high-confidence entries gets opened as well.",
    manim("B12_StepFour",
          "Step 4's box thickens (step 3 relaxes). The same panel: an ink underline lands under 'on the training set only' in the paper sentence with a terracotta dot; an X-free strike under the claim; the claim cross-fades to the corrected claim with the qualifier; 'disposition: corrected'; then five small squares for HIGH entries, one filled — 'HIGH: 1 in 5 opened'.",
          [{"at": 0.1, "event": "step 4 box thickens"}, {"at": 0.3, "event": "the five words underlined, dot"},
           {"at": 0.6, "event": "claim corrected; 'corrected'"}, {"at": 0.85, "event": "five HIGH squares, one opened"}],
          "Second instance: a human step's check needs domain judgment, not a search."),
    role="INSTANCE", section=1,
    learn={"question": "Is the extracted claim right?",
           "action": "Open the source and compare the claim with the sentence it came from.",
           "observation": "Five dropped words change the finding; no string search would see it.",
           "inference": "Step 4's check needs domain judgment: expensive to verify.",
           "next_question": "So what if we skip it and just glance?"}))

beats.append(beat("B13", "learn 1",
    "Now the obvious rule: let the AI do the heavy lifting, and glance at the result. "
    "Step four becomes a glance. Step six becomes a glance. Follow the claim. It leaves step three without its qualifier. A glance waves it through. Formatting makes it tidy. Another glance signs it. "
    "And the reader gets: outperformed baselines. "
    "The bars told us where the effort was. They said nothing about where it would break.",
    manim("B13_JustGlance",
          "The panel clears and the bars return. 'audit' and 'sign-off' cross-fade to 'glance'. A small claim token travels along the rail under the boxes 3 → 4 → 5 → 6, a check landing at each glance; it exits into a summary line at the bottom: 'summary: “outperformed baselines.”' with a terracotta X beside it.",
          [{"at": 0.1, "event": "bars return; the rule lands"}, {"at": 0.3, "event": "audit, sign-off → glance"},
           {"at": 0.45, "event": "the claim token travels 3 → 6"}, {"at": 0.75, "event": "the summary line lands with an X"}],
          "The natural wrong turn, walked to where it breaks: effort bars cannot see the dropped qualifier."),
    role="NAIVE", section=1,
    learn={"question": "What if the human steps are just a glance?",
           "action": "Replace steps 4 and 6 with glances and follow the claim to the reader.",
           "observation": "The qualifier never comes back; the reader gets the wrong finding.",
           "inference": "Effort is the wrong axis: it says where the work is, not where the failure is.",
           "next_question": "What should we measure instead?"}))

beats.append(beat("B14", "learn 1",
    "So ask different questions, five of them, of every step. How costly is it to verify? What does a wrong answer cost? "
    "Is the input the kind the model handles well? Can the output be undone? Does it leave a trail? "
    "Score step three. Verifying it is a search. A mistake gets caught at step four. Unsure extractions arrive tagged. "
    "The next step can undo anything wrong. And the claims, citations and tags stay on the record. Five light cells.",
    manim("B14_FiveQuestions",
          "Five row labels land at left (verification · stakes · distribution · reversibility · audit trail), one per spoken question; step 3's tall bar collapses into a column of five cells, each landing light as Liam gives its reason; the reason for each row cross-fades in the bottom band; caption 'cells: our reading of the text'.",
          [{"at": 0.05, "event": "row labels land on their questions"}, {"at": 0.45, "event": "step 3's bar collapses into a column"},
           {"at": 0.55, "event": "five light cells land, one per reason"}, {"at": 0.9, "event": "caption"}],
          "The representation arrives: a step is scored on five questions, not on effort."),
    role="SHIFT", section=1,
    learn={"question": "What should we measure instead of effort?",
           "action": "Score step 3 on five questions: verification, stakes, distribution, reversibility, audit trail.",
           "observation": "Every cell for step 3 is light.",
           "inference": "A step whose answers are all light is safe to hand to the AI.",
           "next_question": "What does the grid say about step 4?"}))

beats.append(beat("B15", "learn 1",
    "Before step four fills in, commit. Which of the five rows go dark? Verification, stakes, the kind of input, undoing, the trail. "
    "Pick yours.",
    manim("B15_Commit",
          "Step 4's short bar collapses into five empty ghost cells; a terracotta dot beside step 4's box; the prompt 'which rows go dark?' holds; nothing else moves.",
          [{"at": 0.1, "event": "step 4's bar becomes five empty cells"}, {"at": 0.4, "event": "'which rows go dark?'"},
           {"at": 0.6, "event": "HOLD"}],
          "The predict-before-reveal beat."),
    role="INSTANCE", section=1, predict=True,
    learn={"question": "Which of step 4's rows are high risk?",
           "action": "Hold the empty column; ask the viewer to commit.",
           "observation": "The viewer commits a guess.",
           "inference": "A committed prediction turns the reveal into evidence.",
           "next_question": "Fill it."}))

beats.append(beat("B16", "learn 1",
    "Step four. Verifying it takes domain judgment: dark. A wrong call misleads the reader: dark. "
    "Its inputs are the entries the model itself was unsure of: dark. "
    "Now let every bar become its column. The tall bars go light. The short bars go dark.",
    manim("B16_BarsBecomeColumns",
          "Step 4's cells fill: three dark (verification, stakes, distribution), two light. Then the remaining bars (1, 2, 5, 6) each morph into their five-cell columns at once: the tall bars resolve into all-light columns, the short bars into columns with dark cells; the dark columns line up exactly under the ink-filled human boxes; 'dark column = human step' lands.",
          [{"at": 0.05, "event": "step 4: verification dark"}, {"at": 0.2, "event": "stakes dark"}, {"at": 0.33, "event": "distribution dark"},
           {"at": 0.5, "event": "every remaining bar morphs into its column"}, {"at": 0.75, "event": "'dark column = human step'"}],
          "The collision: the effort bars themselves become the risk grid, and the dark cells land under the human boxes."),
    role="TRANSFORM", section=1,
    learn={"question": "Where does the grid go dark?",
           "action": "Fill step 4's column, then morph every effort bar into its column.",
           "observation": "The tall bars become light columns; the short bars become dark ones — under the human boxes.",
           "inference": "The human steps are where the grid goes dark, not where the work looks heavy.",
           "next_question": "Where are the dangerous handoffs, then?"}))

beats.append(beat("B17", "learn 1",
    "Now read across the arrows. Where does a light column hand off to a dark one? Three into four, and five into six. "
    "The score calls those the two highest-risk handoffs. "
    "At three into four, the danger is waving the confident extractions through. That's why one in five of them gets opened anyway. "
    "At five into six, it's signing the summary like a proofread, instead of reading it the way a researcher would.",
    manim("B17_TheSeams",
          "Two ink arrows grow on the rail between columns 3→4 and 5→6; brackets under the grid mark the two seams with labels '3 → 4 · waved through' and '5 → 6 · proofread, not read'; a terracotta dot beside the 3 → 4 arrow; caption 'both run AI → human'.",
          [{"at": 0.1, "event": "arrow 3 → 4"}, {"at": 0.2, "event": "arrow 5 → 6"},
           {"at": 0.45, "event": "'waved through'"}, {"at": 0.75, "event": "'proofread, not read'"}, {"at": 0.9, "event": "caption"}],
          "Post-shift instance: the grid predicts where the risk sits — at the light-to-dark seams."),
    role="INSTANCE", section=1,
    learn={"question": "Which handoffs are the dangerous ones?",
           "action": "Mark every place a light column hands to a dark column.",
           "observation": "Exactly two: 3 → 4 and 5 → 6, both AI to human.",
           "inference": "Risk concentrates where authority passes from AI to human.",
           "next_question": "What is the general rule?"}))

beats.append(beat("B18", "learn 1",
    "This deserves a name. These are the five Boondoggle questions. "
    "A step goes to the AI when it's cheap to verify, its failures are bounded, and its output can be undone at the next human step. "
    "Every dark row pushes a step toward a human. And a mixed column makes a hybrid: the AI works, a human checks at a written handoff. "
    "The split is not aesthetic. It's written down, with its reasons.",
    manim("B18_NameIt",
          "The title cross-fades to 'The Five Boondoggle Questions'; a bracket gathers the five row labels; the bottom band lands 'AI step: cheap to verify · bounded · undone next step'; then 'dark row → toward a human'; a terracotta dot beside the bracket; caption 'not aesthetic: written, with reasons'.",
          [{"at": 0.1, "event": "the name lands; bracket gathers the rows"}, {"at": 0.35, "event": "'AI step: cheap · bounded · undone next step'"},
           {"at": 0.6, "event": "'dark row → toward a human'"}, {"at": 0.9, "event": "caption"}],
          "The abstraction arrives last, as the name for the grid the viewer has been reading."),
    role="ABSTRACTION", section=1,
    learn={"question": "What is the general rule?",
           "action": "Name the five rows and state when a step goes to the AI.",
           "observation": "The AI columns are cheap to verify, bounded and undoable at the next human step.",
           "inference": "Delegation follows the five questions applied honestly, not how the step looks.",
           "next_question": "Back to the puzzle — and what the score leaves out."}))

beats.append(beat("B19", "learn 1",
    "Back to the puzzle. Three short bars, three human steps. Now you can see why: they were short on effort and heavy on judgment. "
    "Two honest limits. The score has a gap. No step integrates work across people, so the moment a second researcher relies on the output, a step seven is required. "
    "And the score is the author's own heuristic, not a validated test. The questions are what survive.",
    manim("B19_StepSeven",
          "The row labels fade; the whole row of boxes and columns slides left one step; the HOOK question returns, now answered 'short on effort, heavy on judgment'; a dashed seventh box '7' with an empty column lands at right with 'missing: executive integration'; a terracotta dot beside it; caption 'a heuristic — not validated'.",
          [{"at": 0.05, "event": "the HOOK question returns"}, {"at": 0.3, "event": "the answer lands under it"},
           {"at": 0.5, "event": "the row slides left; dashed box 7 lands"}, {"at": 0.75, "event": "'missing: executive integration'"},
           {"at": 0.9, "event": "caption: a heuristic, not validated"}],
          "The HOOK's boxes return, resolved; the boundary names the missing step and the instrument's limit."),
    role="PAYOFF", section=1,
    learn={"question": "Why do humans own the steps that look easiest?",
           "action": "Return to the six boxes; add the missing seventh.",
           "observation": "The short-bar steps are the judgment steps; the score itself flags one step it lacks.",
           "inference": "Ownership follows the five questions; a second person adds an integration step.",
           "next_question": ""}))

beats.append(beat("BVDT", "verdict",
    "Let's recap with Claude. In the paper summarizer, the AI owns parsing, extraction and formatting; a human owns the taxonomy, the audit and the sign-off. "
    "The human steps are not the ones that look like work. They are where verifying takes judgment, a wrong call reaches a reader, or the inputs are the model's own doubts. "
    "The two riskiest handoffs both run from AI to human. And the score is a heuristic. The questions are the tool.",
    remotion("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": TITLE,
        "artifactLines": ["AI owns parse, extract, format; a human owns taxonomy, audit, sign-off.",
                          "Human steps fall where verifying takes judgment and a wrong call reaches a reader — not where work looks heavy.",
                          "The two riskiest handoffs, 3 → 4 and 5 → 6, both run from AI to human.",
                          "The score is an unvalidated heuristic; the five questions are the tool."]},
        [{"at": 0.0, "event": "artifact page opens"}, {"at": 0.2, "event": "four verdict lines land"}]),
    lane="bookend", lead_silence_s=0.5, qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}))

YT = ("A graduate student runs a six-step paper summarizer and a faculty supervisor reviews the summary before it goes into a paper. "
      "Before scoring anything, predict what new step this adds, and whether a human or the AI should own it. "
      "Then score that step on five questions, one line each: verification cost, stakes, distribution match, reversibility, audit trail. "
      "Finally, write its handoff condition so that someone who did not build the pipeline could check, for one case, whether it was met.")
beats.append(beat("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT + " "
    "Two things to look for. Did it predict before it scored? If it jumped to the answer, send it back. "
    "And is its handoff condition something a stranger could check, or does it say the supervisor reviews and stop there?",
    remotion("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "INFO 7375 · YOUR TURN", "segment": "Design Step Seven",
        "command": YT, "runningText": "paste this into Claude…",
        "output": ["Check: the prediction came before the scoring.",
                   "Check: a stranger could test the handoff condition — no bare 'reviews'."],
        "folderLabel": "@NikBearBrown", "modelLabel": "Fable 5", "effortLabel": "High"},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two rubric lines land"}]),
    lane="bookend"))

beats.append(beat("BOUT", "outro", f"{TITLE}. At Nik Bear Brown.",
    remotion("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""},
             [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot. Liam reads the title, then 'At Nik Bear Brown'. No jingle."}]),
    lane="bookend", kind="outro_voice", tail_silence_s=1.0,
    hold_note="spoken outro + 1.0 s silent tail (apad into the mp3); no jingle (OUTRO-LOCK §Voice)"))

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "INFO 7375 · TL;DR", "skill": "tldr", "style_preset": "tldr",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "learn_canvas": "cream", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160, "caption_policy": "none",
    "audience": "INFO 7375 students building AI pipelines, and anyone who splits work between a model and people by what looks like work",
    "course": "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University",
    "source_doc": "chapters/09-delegation-trust-and-the-supervisory-role.md — §'The Boondoggle questions', §'A worked walkthrough: the Research Paper Summarizer' → §'Generating the Boondoggle Score' (STEP 1–6 + Score summary), §'What the Boondoggle Score reveals', §'The shape of the rest'; Figures 9.2–9.3 (captions only); section S3 of youtube/tldr-sections-09-delegation-trust.md",
    "sections": [{"n": 1, "title": TITLE, "key_case": "the Paper Summarizer's six-step Boondoggle Score — AI owns 2 · 3 · 5, a human owns 1 · 4 · 6; Step 4 catches a dropped 'on the training set only'"}],
    "greeting_language": "Fijian (Bula)",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "outro_policy": "OUTRO-LOCK §Voice: spoken title + 'At Nik Bear Brown', 1.0 s silent tail padded into the mp3, no jingle.",
    "bookloop_policy": "Course film: carries the INFO 7375 course credit (spoken in B00, on the cards' course line).",
    "tags": ["delegation", "human in the loop", "AI pipelines", "Boondoggle Score", "INFO 7375", "3Blue1Brown style", "Claude", "Nik Bear Brown"]},
    "beats": beats}
out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"{len(beats)} beats → {out}")
