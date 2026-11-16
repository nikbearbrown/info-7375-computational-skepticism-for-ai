#!/usr/bin/env python3
"""make_sheet.py — writes beat_sheet.json for tldr-both-audits-were-right.

tldr skill (brutalist.art/skills/make/tldr). Section S3 of chapter 6
(youtube/tldr-sections-06-bias-where-it-enters.md): COMPAS, ProPublica vs
Northpointe, both audits correct. The AUDIT side of the impossibility — what each
audit divided by — not the CHOICE side (that is chapter 7's film).

The chapter's inputs: base rates 30% (group 1) and 50% (group 2); a calibrated
score ("a score of 50 means 50% … in both groups"); the identity
v/(1−v) = p/(1−p)·t/f. The film builds a CONSTRUCTED 20-person-per-group
population on those base rates with a two-box calibrated score (high box → 60%
reoffend, low box → 20%, in both groups), captioned "constructed" on screen.
Every derived number (FPR, FNR, box shares, t/f) is recomputed and asserted here
and in scenes.py; FACTCHECK.md carries the rows. Re-run, then audio, then
lock_cards.py, then ./art run.
"""
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent

SLUG = "tldr-both-audits-were-right"
TITLE = "Both Audits Were Right"
COURSE = "INFO 7375 · Computational Skepticism · Chapter 6"

# ═══════════ the constructed population (chapter base rates 30% / 50%) ═══════════
# per group: (high-box size, high-box reoffenders, low-box size, low-box reoffenders)
G = {1: (5, 3, 15, 3), 2: (15, 9, 5, 1)}
def stats(g, moved=0):
    H, hr, L, lr = G[g]
    H, L = H - moved, L + moved                    # `moved` non-reoffenders walk from high to low
    n = H + L; r = hr + lr; neg = n - r
    return dict(n=n, r=r, neg=neg, p=F(r, n), hi_share=F(hr, H), lo_share=F(lr, L),
                fp=H - hr, fpr=F(H - hr, neg), fn=lr, fnr=F(lr, r), tpr=F(hr, r), ppv=F(hr, H))
S1, S2 = stats(1), stats(2)
assert S1["n"] == S2["n"] == 20
assert S1["p"] == F(3, 10) and S2["p"] == F(1, 2)                      # the chapter's 30% and 50%
assert S1["hi_share"] == S2["hi_share"] == F(3, 5)                      # calibrated: high means 60% in both
assert S1["lo_share"] == S2["lo_share"] == F(1, 5)                      # calibrated: low means 20% in both
assert (S1["fp"], S1["neg"], S2["fp"], S2["neg"]) == (2, 14, 6, 10)     # ProPublica's read: 2 of 14 vs 6 of 10
assert (S1["fn"], S1["r"], S2["fn"], S2["r"]) == (3, 6, 1, 10)          # misses: 3 of 6 vs 1 of 10
for s in (S1, S2):                                                      # the chapter's identity, exactly
    v, p, t, f = s["ppv"], s["p"], s["tpr"], s["fpr"]
    assert v / (1 - v) == p / (1 - p) * t / f
assert S1["tpr"] / S1["fpr"] == F(7, 2) and S2["tpr"] / S2["fpr"] == F(3, 2)   # t/f = 3.5 vs 1.5
assert S1["p"] / (1 - S1["p"]) == F(3, 7) and S2["p"] / (1 - S2["p"]) == 1
# B16 — the repair attempt: move group 2's flagged non-reoffenders to low, one at a time
T = [stats(2, m) for m in range(5)]
assert [(t["fp"], t["neg"]) for t in T] == [(6, 10), (5, 10), (4, 10), (3, 10), (2, 10)]
assert [t["hi_share"] for t in T] == [F(9, 15), F(9, 14), F(9, 13), F(9, 12), F(9, 11)]
assert round(float(T[4]["hi_share"]) * 100) == 82 and T[4]["lo_share"] == F(1, 9)
assert T[4]["fpr"] > S1["fpr"]                                          # 2/10 vs 2/14: nearly closed, not closed

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

B00_N = ("Kumusta. This is Liam, in for Bear, with chapter six of INFO 7375, Computational Skepticism for AI, at Northeastern. "
         "This film is about one risk score and two audits that disagreed. "
         "When base rates differ, a score cannot be calibrated and make equal errors at once. "
         "You'll watch forty people counted two ways. "
         "The trap: assuming one audit got the arithmetic wrong.")
B00_EST = round(len(B00_N.split()) / 2.5, 1)
beats.append(beat("B00", "tldr · what", B00_N,
    remotion("ClaudeTldrWhat", {
        "eyebrow": "TL;DR", "heading": "What This Film Is About", "greeting": "Kumusta, Liam", "topic": COURSE,
        "question": "ProPublica said the risk score was biased. Its maker said it was fair. How can both be right?",
        "lines": ["When base rates differ, one score can't be calibrated and make equal errors.",
                  "Watch forty people counted two ways: by score box, then by outcome.",
                  "The trap: assuming one audit got the arithmetic wrong."],
        "cues": [round(B00_EST * f, 1) for f in (0.05, 0.50, 0.72, 0.88)], "durationSeconds": B00_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "'TL;DR.' wordmark; 'Kumusta, Liam'; the course line; heading"},
         {"at": 0.05, "event": "the question writes on"},
         {"at": 0.50, "event": "line 1 lands on 'when base rates differ'"},
         {"at": 0.72, "event": "line 2 lands on 'you'll watch forty people'"},
         {"at": 0.88, "event": "line 3 lands on 'the trap'"}]),
    lane="bookend"))

B01_N = ("Why should you care? Every fairness audit divides by something, and the headline never says what. "
         "Read one audit, and you judge a tool on half the arithmetic. "
         "Ask for cleaner data, and you wait forever, because this is a theorem, not a data problem. "
         "And it unlocks reading two opposite audits and saying exactly what each one measured.")
B01_EST = round(len(B01_N.split()) / 2.5, 1)
beats.append(beat("B01", "tldr · why", B01_N,
    remotion("ClaudeTldrWhy", {
        "eyebrow": "TL;DR", "heading": "Why You Should Care", "topic": COURSE,
        "lead": "Every fairness audit divides by something — and the headline never says what.",
        "lines": ["Read one audit, and you judge a tool on half the arithmetic.",
                  "Ask for cleaner data, and you wait forever: this is a theorem, not a data problem.",
                  "It unlocks reading two opposite audits and naming what each one measured."],
        "cues": [round(B01_EST * f, 1) for f in (0.05, 0.30, 0.52, 0.80)], "durationSeconds": B01_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "page turn: same header, heading 'Why You Should Care'"},
         {"at": 0.05, "event": "the stake writes on"},
         {"at": 0.30, "event": "dash 1 on 'read one audit'"},
         {"at": 0.52, "event": "dash 2 on 'ask for cleaner data'"},
         {"at": 0.80, "event": "dash 3 on 'unlocks'"}]),
    lane="bookend", qc={"sparse_by_design": True, "sparse_reason": "TL;DR card two — text lands on cues by design."}))

beats.append(beat("B02", "the question",
    "The question this film is really asking: how can both be right? "
    "Asking which audit got it wrong is the trap. It sends you hunting for an arithmetic error that isn't there.",
    remotion("BrutalistHesitantWriter", {
        "text": "Two audits, opposite verdicts.\nWhich audit got it wrong?",
        "triggerWords": "Which audit got it wrong", "replacementWords": "How can both be right",
        "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
        "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'Two audits, opposite verdicts.'"},
         {"at": 0.35, "event": "types 'Which audit got it wrong?'; backspaces the phrase → 'How can both be right?' on the spoken correction"},
         {"at": 0.85, "event": "caret holds"}]),
    lane="bookend", lead_silence_s=0.8,
    motion_claim="The writer types the naive who-cheated question and corrects the phrase that makes it the wrong question.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}))

B03_N = ("Four terms you'll hear. Base rate: the share of a group who actually reoffend. "
         "Calibrated: a score that means the same chance in every group. "
         "False positive rate: of the people who never reoffend, the share flagged high risk. "
         "False negative rate: of the people who do reoffend, the share called low risk. The misses.")
B03_EST = round(len(B03_N.split()) / 2.5, 1)
beats.append(beat("B03", "terms", B03_N,
    remotion("ClaudeDefinitions", {
        "title": "Terms In This Film",
        "terms": [{"term": "base rate", "meaning": "the share of a group who actually reoffend"},
                  {"term": "calibrated", "meaning": "a score that means the same chance of reoffending in every group"},
                  {"term": "false positive rate", "meaning": "of the people who never reoffend, the share flagged high risk"},
                  {"term": "false negative rate", "meaning": "of the people who do reoffend, the share called low risk: the misses"}],
        "durationSeconds": B03_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'base rate' lands, terracotta"}, {"at": 0.32, "event": "'calibrated' lands; first settles"},
         {"at": 0.55, "event": "'false positive rate' lands"}, {"at": 0.78, "event": "'false negative rate' lands"}]),
    lane="bookend", proof="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: prerequisites only — the impossibility (the film's answer) is earned in B17."}))

# ── LEARN section 1 (B10–B19) ────────────────────────────────────────────────
beats.append(beat("B10", "learn 1",
    "One risk score, used by courts in Broward County, Florida. In 2016 ProPublica audited it: Black defendants who never reoffended were flagged high risk more often than white defendants who never reoffended. Biased. "
    "The maker, Northpointe, audited the same tool: within each score, the same share reoffended in both groups. Fair. "
    "Same tool, same people, opposite verdicts. Somebody's arithmetic is wrong. Right?",
    manim("B10_TwoHeadlines",
          "Forty grey dots in two rows at the bottom — the same people; ProPublica's headline lands top-left ('errors fell unevenly' → 'biased'), an ink line drops from it to the dots; Northpointe's headline lands top-right ('each score meant the same' → 'fair'), its line drops to the same dots; a terracotta dot beside the caption's question 'which one is wrong?'.",
          [{"at": 0.05, "event": "the forty dots land"}, {"at": 0.2, "event": "ProPublica headline + its line to the dots on 'biased'"},
           {"at": 0.55, "event": "Northpointe headline + its line to the same dots on 'fair'"}, {"at": 0.85, "event": "caption 'which one is wrong?' with the dot"}],
          "Two verdicts drawn onto one set of dots: the HOOK's dots are the persistent object for the whole section."),
    role="HOOK", section=1,
    learn={"question": "Two audits of the same tool reached opposite verdicts. Which one is wrong?",
           "action": "Point both headlines at the same forty people.",
           "observation": "Same tool, same people, opposite verdicts.",
           "inference": "If the data is shared, the disagreement must be in the arithmetic — or in what each audit counts.",
           "next_question": "What do the people actually look like, group by group?"}))

beats.append(beat("B11", "learn 1",
    "Let's build a small version we can count. Group one: twenty people. Six of them will reoffend. That's a base rate of thirty percent, the chapter's number. "
    "Dark dots reoffend; grey dots don't. Now the score sorts them into two boxes. "
    "Five land in high risk, and three of those five reoffend: sixty percent. Fifteen land in low, and three of them reoffend: twenty percent.",
    manim("B11_GroupOne",
          "The headlines clear; group one's twenty dots slide into the left panel; six darken to ink (reoffend); header 'group 1 · base rate 30%'; two box outlines draw ('high', 'low'); the dots sort into them — 5 high (3 ink), 15 low (3 ink); readouts '60%' and '20%' land right of the boxes; a terracotta dot beside '60%'; small dim caption 'constructed · 20 per group'.",
          [{"at": 0.1, "event": "twenty dots into the left panel"}, {"at": 0.3, "event": "six darken on 'six of them will reoffend'"},
           {"at": 0.55, "event": "boxes draw; dots sort into high / low"}, {"at": 0.8, "event": "'60%' and '20%' land on the spoken shares"}],
          "First instance: the base rate is a count of dark dots; the score is a sort into boxes; the box share is readable."),
    role="INSTANCE", section=1,
    learn={"question": "What does a calibrated score do to one group of twenty?",
           "action": "Mark the six who reoffend; sort the twenty into high and low boxes.",
           "observation": "High box: 3 of 5 reoffend (60%). Low box: 3 of 15 (20%).",
           "inference": "A score's box has a share; that share is what 'the score means' for this group.",
           "next_question": "Does the same score mean the same thing in a group with a different base rate?"}))

beats.append(beat("B12", "learn 1",
    "Group two: twenty people, and ten reoffend. Fifty percent. Same score, same boxes. "
    "Fifteen land in high, and nine of them reoffend: sixty percent. Five land in low; one reoffends: twenty percent. "
    "Look across. High means sixty percent in both groups. Low means twenty in both. That's Northpointe's audit, and it passes.",
    manim("B12_GroupTwo",
          "Group two's twenty dots (waiting as a ghost row in the right panel) darken ten to ink; header 'group 2 · base rate 50%'; its boxes draw and the dots sort — 15 high (9 ink), 5 low (1 ink); readouts '60%' / '20%'; a thin ink line joins the two '60%' readouts across the panels and 'Northpointe: calibrated' lands beneath with a terracotta dot.",
          [{"at": 0.1, "event": "ten darken on 'ten reoffend'"}, {"at": 0.35, "event": "dots sort into the boxes"},
           {"at": 0.6, "event": "'60%' / '20%' land"}, {"at": 0.85, "event": "line across the two 60s; 'Northpointe: calibrated' + dot"}],
          "Second instance: vary one parameter (the base rate), replay the sort; the box shares come out identical."),
    role="INSTANCE", section=1,
    learn={"question": "Does the same score mean the same thing when the base rate is 50%?",
           "action": "Sort group two with the same rule; read each box.",
           "observation": "High: 9 of 15 = 60%; low: 1 of 5 = 20% — exactly group one's shares.",
           "inference": "The score is calibrated in both groups; Northpointe's audit is correct.",
           "next_question": "So ProPublica's audit must be the one with the error?"}))

beats.append(beat("B13", "learn 1",
    "So ProPublica must have fudged it. Let's redo their count on these same dots. "
    "Their question starts from the grey dots, the people who never reoffended. Group one has fourteen, and two of them sit in the high box. "
    "Group two has ten, and six sit in high. Two in fourteen, against six in ten. "
    "The arithmetic is clean. Nobody fudged anything.",
    manim("B13_RedoTheCount",
          "'fudged?' writes under the ProPublica label; the dark dots in both panels fade to ghost so only the grey dots remain; the grey dots in each high box pulse; readouts 'flagged, never reoffended: 2 of 14' (left) and '6 of 10' (right) land under the boxes; 'fudged?' gets a terracotta X beside it.",
          [{"at": 0.1, "event": "'fudged?' appears"}, {"at": 0.3, "event": "dark dots fade — only the never-reoffended remain"},
           {"at": 0.55, "event": "'2 of 14' / '6 of 10' land on the spoken counts"}, {"at": 0.85, "event": "X beside 'fudged?' on 'nobody fudged anything'"}],
          "The natural wrong turn walked to its end on screen: the recount reproduces ProPublica's gap from the same dots — no error to find."),
    role="NAIVE", section=1,
    learn={"question": "Did ProPublica make an arithmetic error?",
           "action": "Recount their way on the same dots: keep only the never-reoffended; count how many sit in high.",
           "observation": "2 of 14 in group one, 6 of 10 in group two — a real gap from the same data.",
           "inference": "Both audits compute correctly on identical data; the disagreement is not an error.",
           "next_question": "Then what is different between the two counts?"}))

beats.append(beat("B14", "learn 1",
    "Here's the reframe. Same dots, two filters. "
    "Northpointe's filter: look inside one box and ask what share reoffended. The denominator is the box. "
    "ProPublica's filter: look at one outcome, the people who never reoffended, and ask what share got flagged. The denominator is the outcome. "
    "And the misses split the same way: three of six in group one, one of ten in group two.",
    manim("B14_TwoFilters",
          "The ghosted dark dots return; Northpointe's filter: the low boxes dim and a bracket-free ink underline marks the high boxes, '60% · 60%' holds; then ProPublica's filter: dark dots ghost again, '2 of 14 · 6 of 10' holds; then the misses: grey dots ghost, the dark dots in the low boxes stay — 'misses: 3 of 6' / '1 of 10' land; a small legend 'box ÷ vs outcome ÷' writes; one terracotta dot beside 'the denominator'.",
          [{"at": 0.1, "event": "Northpointe filter: low boxes dim; high boxes read 60 · 60"},
           {"at": 0.4, "event": "ProPublica filter: only the never-reoffended; 2 of 14 · 6 of 10"},
           {"at": 0.75, "event": "the misses: 3 of 6 · 1 of 10"}, {"at": 0.9, "event": "all dots back; three readouts stand"}],
          "The representation: one set of dots read through two filters — divide by the box, or divide by the outcome."),
    role="SHIFT", section=1,
    learn={"question": "What is different between the two counts?",
           "action": "Apply Northpointe's filter (a box), then ProPublica's (an outcome), then the misses.",
           "observation": "The same dots give equal box shares and unequal outcome shares.",
           "inference": "The audits divide by different things; each can be right about its own denominator.",
           "next_question": "Can one score satisfy both denominators at once?"}))

beats.append(beat("B15", "learn 1",
    "Before anything moves, commit. Keep high meaning sixty percent in both groups. "
    "Can you also make the two false positive rates match? Yes? No? Only with a better model? "
    "Pick one.",
    manim("B15_Commit",
          "Everything holds; a dim guide line marks group one's '2 of 14' level on a small rate bar under each panel; the question 'hold 60% — equal false positives too?' writes at the bottom; a terracotta dot beside it; nothing else moves.",
          [{"at": 0.1, "event": "the two false-positive bars draw: 2/14 and 6/10"}, {"at": 0.35, "event": "the question writes"},
           {"at": 0.6, "event": "dot beside the question; HOLD on 'pick one'"}],
          "The predict-before-reveal beat: both constraints on screen, the answer withheld."),
    role="INSTANCE", section=1, predict=True,
    learn={"question": "Holding calibration, can the false positive rates also be equal?",
           "action": "Draw both rates as bars; hold the picture.",
           "observation": "The viewer commits: yes, no, or only with a better model.",
           "inference": "A committed prediction turns the next move into evidence.",
           "next_question": "Try it: what happens when we push group two's false positives down?"}))

beats.append(beat("B16", "learn 1",
    "Try it. To cut group two's false positives, move its grey dots out of the high box. One. Two. Three. Four. "
    "ProPublica's gap nearly closes: two in ten, against two in fourteen. "
    "And the high box? Nine of eleven reoffend. Eighty-two percent. "
    "Every dot that closes one gap opens the other.",
    manim("B16_MoveTheDots",
          "Group two's four flagged grey dots walk, one at a time, from the high box down into the low box; group two's false-positive bar shrinks 6/10 → 2/10 toward group one's 2/14 guide, while the high box's readout climbs 60% → 64% → 69% → 75% → 82% and the low box's 20% drops to 11%; the Northpointe line across the two high readouts breaks (an X beside it, terracotta).",
          [{"at": 0.05, "event": "first grey dot drops on 'one'"}, {"at": 0.35, "event": "four dots moved; FP bar at 2 of 10"},
           {"at": 0.6, "event": "high readout lands at 82% on 'eighty-two percent'"}, {"at": 0.8, "event": "the 60–60 line breaks; X on 'calibration just broke'"}],
          "The aha is the morph: the same four dots carry ProPublica's gap closed and Northpointe's gap opened, in one motion."),
    role="TRANSFORM", section=1,
    learn={"question": "What happens to calibration when we push group two's false positives down?",
           "action": "Move group two's flagged never-reoffended dots from high to low, one at a time.",
           "observation": "False positives 6/10 → 2/10; the high box's share 60% → 82%; the low box's 20% → 11%.",
           "inference": "With these base rates, the move that equalizes errors is the move that breaks calibration.",
           "next_question": "Is that just this repair, or is it forced?"}))

beats.append(beat("B17", "learn 1",
    "Is that just a bad repair, or is it forced? The chapter gives one line. "
    "For each group: v over one minus v equals p over one minus p, times t over f. "
    "v is Northpointe's sixty percent. f is ProPublica's number. p is the base rate. "
    "Lock v in both groups, and group one needs t over f of three and a half; group two, one and a half. "
    "The base rate forces it. Calibration and equal error rates cannot coexist when base rates differ.",
    manim("B17_TheLine",
          "The panels shrink and dim into the upper corners; the identity writes in MathTex at centre; each symbol gets its referent beside it ('Northpointe's 60%' under v, 'base rate' under p, 'ProPublica's' under f); the two groups' plug-ins write beneath: 1.5 = 3/7 · 3.5 and 1.5 = 1 · 1.5; the name lands: 'calibration + equal errors: impossible when base rates differ'; a terracotta dot beside it.",
          [{"at": 0.1, "event": "the identity writes"}, {"at": 0.3, "event": "v, f, p get their referents"},
           {"at": 0.6, "event": "both plug-ins write: 3.5 vs 1.5"}, {"at": 0.9, "event": "the name lands, with the dot"}],
          "The abstraction arrives as the name for what the dots did: the base rate locks t/f once v is locked."),
    role="ABSTRACTION", section=1,
    learn={"question": "Is the break forced, or just this repair?",
           "action": "Write the chapter's identity; plug in both groups at v = 60%.",
           "observation": "t/f must be 3.5 in group one and 1.5 in group two.",
           "inference": "With v held equal and base rates unequal, the error-rate ratio must differ — equal error rates cannot hold.",
           "next_question": "Read the line: what is each piece, and is there any way out?"}))

beats.append(beat("B18", "learn 1",
    "Read the line. Left: Northpointe's number, as odds. "
    "First factor: the base rate, as odds. Neither audit chose it; the world handed it over. "
    "Second factor, t over f: how hard the high flag leans toward the people who reoffend. ProPublica's number lives in f. "
    "The equals sign is the lock. Fix the left, and the base rate dictates the rest. "
    "Two ways out: equal base rates, or a perfect score.",
    manim("B18_ReadTheLine",
          "Split stage: the identity persists on the left; five zones write into the right band — 'left: Northpointe's number, as odds' · 'p/(1−p): the base rate — nobody chose it' · 't/f: how hard the flag leans' · 'f: ProPublica's number' · '=: the lock'; then the two escapes write under the equation: p_a = p_b, or t = 1, f = 0; a terracotta dot beside 'the lock'.",
          [{"at": 0.1, "event": "zone 1: the left side"}, {"at": 0.3, "event": "zone 2: the base rate"},
           {"at": 0.5, "event": "zones 3–4: t/f and f"}, {"at": 0.7, "event": "zone 5: the lock, with the dot"},
           {"at": 0.85, "event": "the two escapes write"}],
          "The tangent explains the symbols (never derives): the equation stays on the main side, the zones fill the side band."),
    role="TANGENT", section=1,
    learn={"question": "What is each piece of the line, and is there a way out?",
           "action": "Name the five zones; write the two escapes.",
           "observation": "Only the base rate is outside both audits' control; the escapes are equal base rates or a perfect score.",
           "inference": "Short of those, no model and no data set satisfies both audits.",
           "next_question": "So — back to the two headlines."}))

beats.append(beat("B19", "learn 1",
    "Back to the two headlines. ProPublica: two in fourteen against six in ten. Correct. "
    "Northpointe: sixty percent in both high boxes. Correct. "
    "Both audits were right, because they divided by different things, and base rates of thirty and fifty percent guarantee those two things can't both be equal. "
    "Not a data-quality problem. A theorem. "
    "Not taught here: which one to hold, and that the recorded outcome was re-arrest, not crime.",
    manim("B19_BothRight",
          "The original forty dots and both headlines return (the HOOK's objects); under ProPublica '2 of 14 · 6 of 10' and a check; under Northpointe '60% · 60%' and a check; the question caption from B10 is replaced by 'both right — different denominators'; a terracotta dot beside it; boundary caption: 'not taught: which to hold'.",
          [{"at": 0.05, "event": "headlines and dots return"}, {"at": 0.2, "event": "ProPublica's numbers + check on 'correct'"},
           {"at": 0.4, "event": "Northpointe's numbers + check on 'correct'"}, {"at": 0.65, "event": "'both right — different denominators' + dot"},
           {"at": 0.9, "event": "boundary caption"}],
          "The HOOK's headlines and dots resolve: both verdicts stand, each with its denominator; the boundary is one dim line."),
    role="PAYOFF", section=1,
    learn={"question": "So which audit was wrong?",
           "action": "Put each audit's number back under its headline.",
           "observation": "Both numbers are correct on the same dots.",
           "inference": "Both audits were right; with unequal base rates their fairness definitions cannot both hold.",
           "next_question": ""}))

beats.append(beat("BVDT", "verdict",
    "Let's recap with Claude. ProPublica and Northpointe were both doing correct arithmetic on the same people. "
    "Northpointe divided by the score box: high meant the same chance in both groups. "
    "ProPublica divided by the outcome: people who never reoffended were flagged at different rates. "
    "When base rates differ, thirty against fifty percent, both can't hold. v over one minus v equals p over one minus p, times t over f, locks them apart. "
    "It's a theorem, not a data problem. So picking between them is a values claim, not a calculation.",
    remotion("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": TITLE,
        "artifactLines": ["Both audits did correct arithmetic on the same people.",
                          "Northpointe divided by the score box: high meant 60% in both groups.",
                          "ProPublica divided by the outcome: the never-reoffended were flagged at different rates.",
                          "Unequal base rates lock the two apart: a theorem, not a data problem."]},
        [{"at": 0.0, "event": "artifact page opens"}, {"at": 0.2, "event": "four verdict lines land"}]),
    lane="bookend", lead_silence_s=0.5, qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}))

YT = ("A hypothetical hospital uses a readmission-risk flag. Audit A reports: among patients flagged high risk, 40% are readmitted, in both Group X and Group Y. "
      "Audit B reports: among patients who were never readmitted, Group Y was flagged twice as often as Group X. "
      "Group X's readmission base rate is 20%; Group Y's is 40%. "
      "Using v/(1−v) = p/(1−p) · t/f, decide whether both audits can be correct at the same time. "
      "Then say what each audit divided by, and name one fact you would need before calling the flag biased.")
beats.append(beat("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT.replace("v/(1−v) = p/(1−p) · t/f", "v over one minus v equals p over one minus p, times t over f") + " "
    "Two things to look for. Did it name each audit's denominator, the flagged patients or the never-readmitted ones, before judging either? "
    "And did it use the base rates, twenty and forty percent, before calling anyone wrong?",
    remotion("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "INFO 7375 · YOUR TURN", "segment": "Two Audits, One Flag",
        "command": YT, "runningText": "paste this into Claude…",
        "output": ["Check: it named each audit's denominator before judging either.",
                   "Check: it used the base rates, 20% and 40%, before calling anyone wrong."],
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
    "audience": "INFO 7375 students reading chapter 6, and anyone who has read two fairness audits of one tool reach opposite verdicts",
    "course": "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University",
    "source_doc": "chapters/06-bias-where-it-enters-and-who-is-responsible.md (HEAD side), §'The dataset as epistemic artifact' (COMPAS paragraphs, the 30%/50% sketch, the identity v/(1−v) = p/(1−p)·t/f), the fairness-criterion table, Figure 6.5; exercise W3; section S3 of youtube/tldr-sections-06-bias-where-it-enters.md",
    "sections": [{"n": 1, "title": TITLE, "key_case": "COMPAS: ProPublica (unequal false-positive rates) vs Northpointe (calibrated within each score) — rebuilt as a constructed 20-per-group population at the chapter's base rates 30% / 50%, two-box calibrated score (60% / 20%), FPR 2/14 vs 6/10"}],
    "greeting_language": "Filipino (Kumusta)",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "outro_policy": "OUTRO-LOCK §Voice: spoken title + 'At Nik Bear Brown', 1.0 s silent tail padded into the mp3, no jingle.",
    "bookloop_policy": "Course film: carries the INFO 7375 course credit (spoken in B00, on the cards' course line).",
    "tags": ["COMPAS", "fairness impossibility", "calibration", "false positive rate", "base rates", "algorithmic bias", "INFO 7375", "computational skepticism", "3Blue1Brown style", "Claude", "Nik Bear Brown"]},
    "beats": beats}
out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"{len(beats)} beats → {out}")
for b in beats:
    print(b["beat_id"], len(b["narration_text"].split()), "words")
