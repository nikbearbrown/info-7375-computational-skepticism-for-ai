#!/usr/bin/env python3
"""make_sheet.py — writes beat_sheet.json for tldr-hold-one-fair.

tldr skill (brutalist.art/skills/make/tldr). Section S1 of chapter 7
(youtube/tldr-sections-07-fairness-metrics.md): the impossibility of calibration
(equal PPV) and equalized odds (equal TPR and FPR) when base rates differ, taught
on the CHOICE side — hold one test fair and watch the other break — with the
chapter's own two arithmetic tables (§"The arithmetic — the actual proof, not a
gesture"). The two tables are the chapter's constructed ("Suppose …") numbers,
captioned "constructed numbers" once on screen. Every number is recomputed here
from the chapter's inputs (p, TPR, FPR) and asserted; FACTCHECK.md carries the
rows. Re-run, then audio, then lock_cards.py, then ./art run.
"""
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

HERE = Path(__file__).resolve().parent

SLUG = "tldr-hold-one-fair"
TITLE = "Hold One Fair, Watch the Other Break"
COURSE = "INFO 7375 · Computational Skepticism · Chapter 7"

# ── the chapter's inputs ─────────────────────────────────────────────────────
PA, PB = 0.6, 0.3                                   # base rates, group A and group B
CAL = {"A": (0.60, 0.30), "B": (0.70, 0.10)}        # calibration-satisfying table: (TPR, FPR)
EO = {"A": (0.70, 0.15), "B": (0.70, 0.15)}         # equalized-odds-satisfying table
SAME = (0.60, 0.30)                                  # B12: group A's rates copied onto group B (derived, not in the chapter)

def ppv(p, t, f): return p * t / (p * t + (1 - p) * f)
def yes(p, t, f): return p * t + (1 - p) * f         # positive-prediction rate
def odds(x): return x / (1 - x)
def r2(x): return str(Decimal(repr(round(x, 6))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))   # the chapter's half-up rounding

# calibration table: PPV 0.75 / 0.75, positive rate 0.48 / 0.28
assert abs(ppv(PA, *CAL["A"]) - 0.75) < 1e-12 and abs(ppv(PB, *CAL["B"]) - 0.75) < 1e-12
assert r2(yes(PA, *CAL["A"])) == "0.48" and r2(yes(PB, *CAL["B"])) == "0.28"
assert abs(PB * 0.70 - 0.21) < 1e-12 and abs(PB * 0.70 + (1 - PB) * 0.10 - 0.28) < 1e-12      # the chapter's own check line
# equalized-odds table: PPV 0.88 / 0.67, positive rate 0.48 / 0.32
assert abs(ppv(PA, *EO["A"]) - 0.875) < 1e-12 and r2(ppv(PA, *EO["A"])) == "0.88"
assert abs(ppv(PB, *EO["B"]) - 2 / 3) < 1e-12 and r2(ppv(PB, *EO["B"])) == "0.67"
assert r2(yes(PA, *EO["A"])) == "0.48" and abs(yes(PB, *EO["B"]) - 0.315) < 1e-12 and r2(yes(PB, *EO["B"])) == "0.32"
# B12 (derived from the chapter's inputs): group A's rates on group B
assert abs(PB * 0.60 - 0.18) < 1e-12 and abs((1 - PB) * 0.30 - 0.21) < 1e-12 and r2(ppv(PB, *SAME)) == "0.46"
# B11: group A's pile, 0.36 dark vs 0.12 grey, three to one
assert abs(PA * 0.60 - 0.36) < 1e-12 and abs((1 - PA) * 0.30 - 0.12) < 1e-12
# the odds identity v/(1-v) = p/(1-p) * t/f, every configuration
for p, (t, f) in [(PA, CAL["A"]), (PB, CAL["B"]), (PA, EO["A"]), (PB, EO["B"]), (PB, SAME)]:
    assert abs(odds(ppv(p, t, f)) - odds(p) * t / f) < 1e-9
# base-rate odds: 1.5 and 3/7 ≈ 0.43; hits over false alarms: 2 vs 7 (calibration), 14/3 ≈ 4.67 both (equalized odds)
assert abs(odds(PA) - 1.5) < 1e-12 and abs(odds(PB) - 3 / 7) < 1e-12 and r2(odds(PB)) == "0.43"
assert abs(CAL["A"][0] / CAL["A"][1] - 2) < 1e-12 and abs(CAL["B"][0] / CAL["B"][1] - 7) < 1e-9
assert abs(EO["A"][0] / EO["A"][1] - 14 / 3) < 1e-9 and r2(14 / 3) == "4.67"
assert abs(odds(PA) * 14 / 3 - 7) < 1e-9 and abs(odds(PB) * 14 / 3 - 2) < 1e-9       # piles 7 : 1 and 2 : 1
assert abs(odds(PA) * 2 - 3) < 1e-9 and abs(odds(PB) * 7 - 3) < 1e-9                  # piles 3 : 1 both
# the cross-group coefficient p_b(1-p_a) / (p_a(1-p_b)) = 2/7: A's t/f must be 2/7 of B's to keep PPV equal
assert abs(PB * (1 - PA) / (PA * (1 - PB)) - 2 / 7) < 1e-12 and abs(2 - (2 / 7) * 7) < 1e-9
# B18 worked value: (3/7) * 7 = 3 -> v = 3/4
assert abs((3 / 7) * 7 - 3) < 1e-12 and abs(3 / 4 - 0.75) < 1e-12
# BHTF transfer (Exercise 6): base rates 0.4 and 0.2 -> base-rate odds 2/3 and 1/4
assert abs(odds(0.4) - 2 / 3) < 1e-12 and abs(odds(0.2) - 0.25) < 1e-12


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

beats.append(beat("B00", "tldr · what",
    "Kumusta. This is Liam, in for Bear, with chapter seven of INFO 7375, Computational Skepticism for AI, at Northeastern. "
    "This film is about two fairness tests that sound compatible and are not. "
    "When base rates differ, hold one fair and the other breaks. "
    "You'll watch the chapter's own numbers do it, both ways. "
    "The trap: thinking a better model fixes it.",
    remotion("ClaudeTldrWhat", {
        "eyebrow": "TL;DR", "heading": "What This Film Is About", "greeting": "Kumusta, Liam", "topic": COURSE,
        "question": "Can one classifier give a flag the same meaning in both groups and make its mistakes evenly?",
        "lines": ["When base rates differ, you cannot have both: hold one fair and the other breaks.",
                  "Pin PPV at 0.75 in both groups and the error rates split; pin the error rates and PPV splits.",
                  "The trap: treating it as a tuning problem. It is a theorem, so the choice is yours to defend."],
        "cues": [1.5, 9.0, 13.0, 17.0], "durationSeconds": 22, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "'TL;DR.' wordmark; 'Kumusta, Liam'; the course line; heading"},
         {"at": 0.06, "event": "the question writes on"},
         {"at": 0.4, "event": "line 1 lands on 'When base rates differ'"},
         {"at": 0.6, "event": "line 2 lands on 'You'll watch'"},
         {"at": 0.8, "event": "line 3 lands on 'The trap'"}]),
    lane="bookend"))

beats.append(beat("B01", "tldr · why",
    "Why should you care? Every audit of a loan model, a hiring screen or a risk score reports some fairness number. "
    "Think the others can be tuned to match it, and you will promise what no model can deliver. "
    "See the trade, and you can say which test you chose and who pays for it. "
    "That makes fairness a decision you sign, not a setting you find.",
    remotion("ClaudeTldrWhy", {
        "eyebrow": "TL;DR", "heading": "Why You Should Care", "topic": COURSE,
        "lead": "Every audit of a loan model, a hiring screen or a risk score reports some fairness number.",
        "lines": ["Think the others can be tuned to match, and you promise what no model can deliver.",
                  "See the trade, and you can say which test you chose and who pays for it.",
                  "That makes fairness a decision you sign, not a setting you find."],
        "cues": [0.8, 7.0, 12.0, 16.0], "durationSeconds": 20, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "page turn: same header, heading 'Why You Should Care'"},
         {"at": 0.05, "event": "the stake writes on"},
         {"at": 0.35, "event": "dash 1 on 'Think the others'"},
         {"at": 0.6, "event": "dash 2 on 'See the trade'"},
         {"at": 0.82, "event": "dash 3 on 'a decision you sign'"}]),
    lane="bookend", qc={"sparse_by_design": True, "sparse_reason": "TL;DR card two — text lands on cues by design."}))

beats.append(beat("B02", "the question",
    "The question this film is really asking: can one model pass both tests when base rates differ? "
    "Not whether we can tune it harder. Tuning moves the model. The base rates belong to the world.",
    remotion("BrutalistHesitantWriter", {
        "text": "Can one model pass both tests\nif we just tune it harder?",
        "triggerWords": "if we just tune it harder", "replacementWords": "when base rates differ",
        "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
        "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'Can one model pass both tests'"},
         {"at": 0.3, "event": "types 'if we just tune it harder?'; backspaces the phrase → 'when base rates differ' on the spoken correction"},
         {"at": 0.85, "event": "caret holds on the corrected question"}]),
    lane="bookend", lead_silence_s=0.8,
    motion_claim="The writer types the naive question and corrects the phrase that makes it the wrong question.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}))

beats.append(beat("B03", "terms",
    "Four terms. Base rate: the share of a group that is truly positive. "
    "True-positive rate: of the true positives, the share the model flags. "
    "False-positive rate: of the true negatives, the share it flags anyway. "
    "And PPV: of everyone flagged, the share who are truly positive.",
    remotion("ClaudeDefinitions", {
        "title": "Terms In This Film",
        "terms": [{"term": "base rate", "meaning": "the share of a group that is truly positive"},
                  {"term": "true-positive rate", "meaning": "of the true positives, the share the model flags (TPR)"},
                  {"term": "false-positive rate", "meaning": "of the true negatives, the share it flags anyway (FPR)"},
                  {"term": "PPV", "meaning": "of everyone flagged, the share who are truly positive"}],
        "durationSeconds": 17, "folderLabel": "@NikBearBrown"},
        [{"at": 0.1, "event": "'base rate' lands, terracotta"}, {"at": 0.3, "event": "'true-positive rate' lands; first settles"},
         {"at": 0.55, "event": "'false-positive rate' lands"}, {"at": 0.8, "event": "'PPV' lands"}]),
    lane="bookend", proof="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: prerequisites only — the trade (and the odds identity) is earned in the section."}))

# ── LEARN section 1 (B10–B19) ────────────────────────────────────────────────
beats.append(beat("B10", "learn 1",
    "Two groups. In group A, sixty percent are truly positive. In group B, thirty percent. One model flags people in both. "
    "We want two things. First: a flag means the same in both groups, the same share of the flagged truly positive. That is calibration. "
    "Second: mistakes land evenly, equal true-positive and false-positive rates. That is equalized odds. "
    "Can we tune our way to both?",
    manim("B10_TwoAsks",
          "Two unit squares (group A, group B) draw; each splits into a positive column whose WIDTH is the base rate (0.6, 0.3) and a negative column; '+' and '−' above the columns; at right the two asks write on — '1 · a flag means the same' and '2 · mistakes land evenly' — each with an ink '?' beside it; one terracotta dot on the thin B positive column; caption 'constructed numbers, from the chapter'.",
          [{"at": 0.0, "event": "the two squares draw"}, {"at": 0.15, "event": "column splits slide to 0.6 and 0.3 on the spoken base rates"},
           {"at": 0.45, "event": "ask 1 writes on 'a flag means the same'"}, {"at": 0.7, "event": "ask 2 writes on 'mistakes land evenly'"},
           {"at": 0.9, "event": "'?' beside each; caption"}],
          "The squares' column widths are the base rates — the persistent objects of the whole section; the question is unsolved."),
    role="HOOK", section=1,
    learn={"question": "Two groups with different base rates, one model: can it pass calibration and equalized odds together?",
           "action": "Draw each group as a square whose positive column is as wide as its base rate; write the two asks.",
           "observation": "B's positive column is half as wide as A's; nothing is flagged yet.",
           "inference": "Whatever the model does, it does inside these two fixed shapes.",
           "next_question": "What does a flag look like inside group A?"}))

beats.append(beat("B11", "learn 1",
    "Start with group A. Flag sixty percent of its true positives, and thirty percent of its true negatives. "
    "Those flags fill the columns from the bottom. Now gather everyone flagged into one pile: the dark part is truly positive, the grey part is not. "
    "Point three six against point one two. Three to one. So a flag in group A is right seventy-five percent of the time.",
    manim("B11_GroupA",
          "In A's square the positive column fills ink from the bottom to 0.60, the negative column fills grey to 0.30; readout 'TPR 0.60 · FPR 0.30' under the square; copies of the two fills slide right and join into one horizontal pile bar (ink 0.75 · grey 0.25) labelled 'A'; MathTex '0.36 : 0.12 = 3 : 1'; readout 'PPV 0.75'; a terracotta dot on the pile.",
          [{"at": 0.05, "event": "positive column fills to 0.60"}, {"at": 0.2, "event": "negative column fills to 0.30"},
           {"at": 0.45, "event": "the two fills slide into one pile bar"}, {"at": 0.7, "event": "0.36 : 0.12 = 3 : 1"}, {"at": 0.88, "event": "PPV 0.75"}],
          "The fills and the pile are the instance: PPV is the dark share of the flagged pile, shown by moving the flags into it."),
    role="INSTANCE", section=1,
    learn={"question": "What does 'a flag means 75%' look like?",
           "action": "Fill A's columns to TPR 0.60 and FPR 0.30; gather the flagged into one pile.",
           "observation": "The pile is 0.36 dark to 0.12 grey — three to one.",
           "inference": "PPV is the dark share of the flagged pile.",
           "next_question": "What if group B gets exactly the same rates?"}))

beats.append(beat("B12", "learn 1",
    "Now group B, with the same rates: sixty percent of its true positives flagged, thirty percent of its true negatives. "
    "The mistakes are perfectly even. But B's positive column is thin. Its pile is point one eight against point two one, more grey than dark. "
    "A flag in group B is right only forty-six percent of the time. Same rates, different meaning.",
    manim("B12_GroupB",
          "B's columns fill to the same heights (0.60, 0.30); readout 'TPR 0.60 · FPR 0.30'; B's fills slide into a second pile bar under A's (ink 0.46 · grey 0.54); MathTex '0.18 : 0.21'; readout 'PPV 0.46'; ask 2 gets an ink check, ask 1 a terracotta X.",
          [{"at": 0.05, "event": "B's columns fill to A's heights"}, {"at": 0.4, "event": "B's pile forms under A's; its dark/grey boundary sits left of A's"},
           {"at": 0.7, "event": "PPV 0.46"}, {"at": 0.85, "event": "check beside ask 2, X beside ask 1"}],
          "Second instance, one parameter changed (the base-rate width): the pile boundaries visibly misalign."),
    role="INSTANCE", section=1,
    learn={"question": "Same error rates in group B — same meaning?",
           "action": "Fill B's columns to A's heights and build B's pile under A's.",
           "observation": "Heights match; the pile is 0.18 dark to 0.21 grey; PPV 0.46 against 0.75.",
           "inference": "Equal error rates did not give equal meaning — the width did it.",
           "next_question": "Can a better model close the gap?"}))

beats.append(beat("B13", "learn 1",
    "The obvious fix: a better model. More hits, fewer false alarms, seventy percent and fifteen percent, the same in both groups. "
    "Both piles get cleaner: eighty-eight percent dark in A, sixty-seven in B. "
    "The gap is still there. A better model moved both numbers up. It did not bring them together.",
    manim("B13_BetterModel",
          "Both squares' fills morph to TPR 0.70 · FPR 0.15 (ink columns rise, grey columns fall); both piles morph (A 0.88, B 0.67); readouts morph; the two dark/grey boundaries still misaligned — a short ink bracket spans the gap between them; caption 'better model, same gap'.",
          [{"at": 0.1, "event": "fills morph in both squares at once"}, {"at": 0.45, "event": "piles morph to 0.88 and 0.67"},
           {"at": 0.75, "event": "bracket across the boundary gap"}, {"at": 0.9, "event": "caption"}],
          "The natural fix walked to its limit: the whole picture improves and the misalignment survives."),
    role="NAIVE", section=1,
    learn={"question": "Will a better model close the gap?",
           "action": "Raise hits to 0.70 and cut false alarms to 0.15, equally in both groups.",
           "observation": "PPV climbs to 0.88 and 0.67; the boundaries stay apart.",
           "inference": "Improving the model does not align the piles while the widths differ.",
           "next_question": "What actually sets the mix of a pile?"}))

beats.append(beat("B14", "learn 1",
    "So read the pile as a ratio. Dark over grey is a width ratio times a height ratio. "
    "The widths are the base rates: one point five to one in group A, point four three to one in group B. They belong to the world. "
    "The heights, hits over false alarms, are the only thing the model controls. Here they match, four point six seven. So the piles cannot.",
    manim("B14_WidthsTimesHeights",
          "The squares hold still (column widths = the world, fill heights = the model); at right, under the piles, two MathTex lines assemble factor by factor: 'A: 7 = 1.5 × 4.67' and 'B: 2 = 0.43 × 4.67'; a terracotta dot in B's thin positive column.",
          [{"at": 0.1, "event": "the odds lines give way to factor lines"}, {"at": 0.3, "event": "the width ratios 1.5 and 0.43 write in; 'world'"},
           {"at": 0.6, "event": "4.67 writes into both lines; 'model'"}, {"at": 0.85, "event": "dot in B's thin positive column"}],
          "The representation: the pile's mix = world's widths × model's heights — read straight off the squares."),
    role="SHIFT", section=1,
    learn={"question": "What sets the mix of a pile?",
           "action": "Split dark over grey into width ratio × height ratio on the squares.",
           "observation": "Widths 1.5 and 0.43 are fixed by the groups; heights 4.67 are the model's.",
           "inference": "With equal heights and unequal widths, the piles must differ.",
           "next_question": "So what happens if we pin the piles equal instead?"}))

beats.append(beat("B15", "learn 1",
    "Now pin the other test. Make a flag mean seventy-five percent in both groups: three to one in both piles. "
    "Group B's width is the small one. Before anything moves, commit. "
    "To reach three to one, must B's false-alarm column go up, or down? And what has to happen in group A?",
    manim("B15_Commit",
          "An ink pointer lands under the piles at 0.75; the target '3 : 1' writes beside the piles; a terracotta dot on B's grey column; everything else holds still; caption \"B's false alarms: up or down?\".",
          [{"at": 0.1, "event": "the 0.75 pointer lands under the piles"}, {"at": 0.35, "event": "dot on B's false-alarm column"},
           {"at": 0.6, "event": "HOLD — nothing moves on 'commit'"}, {"at": 0.85, "event": "caption"}],
          "The predict-before-reveal beat: the target is visible, the answer is not."),
    role="INSTANCE", section=1, predict=True,
    learn={"question": "To make B's flag mean 75%, which way must its false alarms move?",
           "action": "Mark the 0.75 target on both piles; hold.",
           "observation": "The viewer commits to a direction.",
           "inference": "A prediction makes the next move evidence.",
           "next_question": "Pin it: what happens to the error rates?"}))

beats.append(beat("B16", "learn 1",
    "Pin it. B's false alarms fall to ten percent. A's rise to thirty, and its hits fall to sixty. "
    "Both piles: three to one. The flags mean the same. "
    "Now look at the columns. They no longer match. Release the pin, and the piles split again.",
    manim("B16_PinOneBreakOther",
          "One continuous morph of the persistent objects: B's grey column drops 0.15 → 0.10 while A's ink column falls 0.70 → 0.60 and grey rises 0.15 → 0.30; both piles slide to 0.75 and their boundaries align over the 0.75 pointer; the height lines morph to '3 = 1.5 × 2' and '3 = 0.43 × 7'; ask 1 flips to a check, ask 2 to a terracotta X; then the fills swing back to 0.70/0.15 and the piles split again (0.88 / 0.67), and swing once more to the pinned state.",
          [{"at": 0.05, "event": "the columns move — B's false alarms fall, A's rise"}, {"at": 0.3, "event": "the piles align at 0.75"},
           {"at": 0.5, "event": "heights now 2 vs 7; ask 2 breaks"}, {"at": 0.7, "event": "release: the piles split again"},
           {"at": 0.9, "event": "pin again — the seesaw"}],
          "The aha is the morph: one alignment is bought by breaking the other, back and forth, on the same objects."),
    role="TRANSFORM", section=1,
    learn={"question": "What does pinning PPV equal cost?",
           "action": "Move the columns until both piles are three to one; release; pin again.",
           "observation": "Piles align only when the heights split (2 vs 7); equal heights split the piles.",
           "inference": "With different widths, the model can align piles or heights, never both.",
           "next_question": "Can we write that as a rule?"}))

beats.append(beat("B17", "learn 1",
    "This deserves its own line. The odds that a flag is right equal the base-rate odds, times hits over false alarms. "
    "Write it once for each group. Pin the left sides equal, and with different base-rate odds, hits over false alarms cannot match. "
    "Pin those equal, and the left sides split. The only exits: equal base rates, or no false alarms at all.",
    manim("B17_TheIdentity",
          "The piles and height lines clear; MathTex v/(1−v) = p/(1−p) · t/f assembles at right term by term, each with a dim word beneath ('pile', 'widths', 'heights'); a terracotta dot beside p/(1−p); then two small exits land: 'p_A = p_B' and 'f = 0', each with an ink dot.",
          [{"at": 0.1, "event": "the identity writes on 'odds that a flag is right'"}, {"at": 0.35, "event": "dim words under each factor"},
           {"at": 0.6, "event": "dot beside the base-rate odds"}, {"at": 0.85, "event": "the two exits"}],
          "The abstraction arrives as the name for the widths × heights picture the viewer already read."),
    role="ABSTRACTION", section=1,
    learn={"question": "What is the rule behind the seesaw?",
           "action": "Write the odds identity beside the squares; name each factor by its shape.",
           "observation": "Flag odds = base-rate odds × t/f in each group.",
           "inference": "Calibration and equalized odds both hold only if base rates are equal or there are no false alarms.",
           "next_question": "What does each symbol mean, and does it reproduce 0.75?"}))

beats.append(beat("B18", "learn 1",
    "Read the line. v is PPV, the dark share of the pile, so v over one minus v is dark to grey. "
    "p over one minus p is the base-rate odds, the column widths. t over f is hits over false alarms, the column heights. "
    "The equals sign says the pile is exactly widths times heights. "
    "Plug in group B: three sevenths times seven is three, and three to one is seventy-five percent. Group A: one point five times two, also three.",
    manim("B18_Tangent",
          "Split stage: the identity persists left; the right band writes 'left: dark over grey in the pile', 'right: widths × heights', '= : exactly, in every group'; a glossary (v · PPV; p · base rate; t, f · TPR, FPR); then MathTex worked values under the identity: (3/7)·7 = 3 → v = 0.75 and 1.5·2 = 3.",
          [{"at": 0.05, "event": "LHS sentence"}, {"at": 0.25, "event": "RHS sentence"}, {"at": 0.45, "event": "'=' claim"},
           {"at": 0.6, "event": "glossary rows"}, {"at": 0.82, "event": "the worked values land"}],
          "The equation tangent: one spotlight across identity, sentences, glossary and worked values."),
    role="TANGENT", section=1,
    learn={"question": "What does each symbol mean?",
           "action": "Translate both sides; gloss v, p, t, f; plug in both groups.",
           "observation": "(3/7)·7 = 3 and 1.5·2 = 3: both piles three to one, PPV 0.75.",
           "inference": "The notation is the picture: widths times heights.",
           "next_question": "Back to the two groups: which test breaks?"}))

beats.append(beat("B19", "learn 1",
    "Back to the two groups. Pin the meaning, and the errors split: sixty and thirty against seventy and ten. "
    "Pin the errors, and the meaning splits: eighty-eight against sixty-seven. "
    "A third test, equal yes-rates, fails both times: forty-eight against twenty-eight, then forty-eight against thirty-two. "
    "Tuning only chose which test breaks. Choosing that is a values claim, and someone has to sign it. Not taught here: the three-way proof.",
    manim("B19_Payoff",
          "The HOOK's squares return, pinned (0.60/0.30 vs 0.70/0.10), piles aligned; the asks list gains '3 · equal yes-rates' with a terracotta X and 'yes 0.48 · 0.28'; the fills swing to 0.70/0.15 — ask 1 X, ask 2 check, 'yes 0.48 · 0.32', ask 3 still X; 'one must give: you choose' lands; dim boundary caption 'not taught here: the three-way proof'.",
          [{"at": 0.05, "event": "the HOOK objects, pinned"}, {"at": 0.3, "event": "the fills swing: the other test breaks"},
           {"at": 0.5, "event": "ask 3 and the yes-rates"}, {"at": 0.75, "event": "'one must give: you choose'"}, {"at": 0.92, "event": "boundary caption"}],
          "The HOOK's persistent squares resolve the question: every setting breaks at least one test; the choice is named."),
    role="PAYOFF", section=1,
    learn={"question": "So — can we tune our way to both?",
           "action": "Swing the same squares between the two pinned states; add the yes-rate test.",
           "observation": "Each state passes one test and fails two.",
           "inference": "Tuning picks which test breaks; picking is a values claim.",
           "next_question": ""}))

beats.append(beat("BVDT", "verdict",
    "Let's recap with Claude. When two groups have different base rates, one model cannot give a flag the same meaning in both and also make its mistakes evenly. "
    "The flagged pile is widths times heights: the world sets the widths, the model sets only the heights. "
    "Pin the meaning and the error rates split; pin the error rates and the meaning splits. "
    "Tuning picks which test breaks. Picking is a values claim you have to defend.",
    remotion("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": TITLE,
        "artifactLines": ["With different base rates, a flag cannot mean the same in both groups while the mistakes land evenly.",
                          "The flagged pile is widths times heights: the world sets the widths, the model only the heights.",
                          "Pin PPV and the error rates split; pin the error rates and PPV splits.",
                          "Tuning picks which test breaks. Picking is a values claim you have to defend."]},
        [{"at": 0.0, "event": "artifact page opens"}, {"at": 0.2, "event": "four verdict lines land"}]),
    lane="bookend", lead_silence_s=0.5, qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}))

YT = ("A care-coordination model flags patients for follow-up. Forty percent of population X truly need it; twenty percent of population Y. "
      "Before computing anything, predict: if a flag must mean the same thing in both populations, must Y's false-positive rate be higher or lower than X's, at the same true-positive rate? "
      "Then check it with the odds identity: PPV odds = base-rate odds × TPR / FPR. "
      "Finally, say which fairness test you would prioritize here, and who bears the cost of each kind of error.")
beats.append(beat("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT + " "
    "Two things to look for. Did it predict the direction before doing any arithmetic? "
    "And in the last answer, does it name who pays for each error, not just a metric?",
    remotion("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "INFO 7375 · YOUR TURN", "segment": "Pin It Yourself",
        "command": YT, "runningText": "paste this into Claude…",
        "output": ["Check: it predicted the direction before any arithmetic.",
                   "Check: it named who pays for each error, not just a metric."],
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
    "audience": "INFO 7375 students reading chapter 7, and anyone asked to make a model 'fair' on every metric at once",
    "course": "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University",
    "source_doc": "chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md, §'Three definitions' and §'The arithmetic — the actual proof, not a gesture' (both numeric tables; Figure 7.1 HEAD caption); Exercise 6 for BHTF; section S1 of youtube/tldr-sections-07-fairness-metrics.md",
    "sections": [{"n": 1, "title": "Hold One Fair, Watch the Other Break",
                  "key_case": "base rates 0.6 / 0.3; calibration table TPR 0.60/0.70 · FPR 0.30/0.10 · PPV 0.75/0.75 · yes 0.48/0.28; equalized-odds table TPR 0.70/0.70 · FPR 0.15/0.15 · PPV 0.88/0.67 · yes 0.48/0.32 — constructed, captioned"}],
    "greeting_language": "Filipino (Kumusta)",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "outro_policy": "OUTRO-LOCK §Voice: spoken title + 'At Nik Bear Brown', 1.0 s silent tail padded into the mp3, no jingle.",
    "bookloop_policy": "Course film: carries the INFO 7375 course credit (spoken in B00, on the cards' course line).",
    "tags": ["fairness metrics", "impossibility theorem", "calibration", "equalized odds", "base rates", "INFO 7375", "3Blue1Brown style", "Claude", "Nik Bear Brown"]},
    "beats": beats}
out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"{len(beats)} beats → {out}")
for b in beats:
    print(b["beat_id"], len(b["narration_text"].split()), "words")
