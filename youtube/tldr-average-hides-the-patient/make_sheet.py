#!/usr/bin/env python3
"""make_sheet.py — writes beat_sheet.json for tldr-average-hides-the-patient.

tldr skill (brutalist.art/skills/make/tldr). Section S2 of chapter 11
(youtube/tldr-sections-11-communicating-uncertainty.md): "Where the Average Hides
the Patient" — the chapter's subgroup calibration table (§"Subgroup calibration:
where aggregate metrics lie"). The table is the chapter's illustrative table (it
cites no dataset); the film captions it "illustrative" once and never attributes
it to the sepsis model the chapter cites beside it.

Every number is copied from the chapter's table or recomputed here from its
inputs (N, subgroup ECE) and asserted. FACTCHECK.md carries the rows. The printed
global base rate (0.041) does not reconcile with the N-weighted rows (0.044), so
no base rate is shown. The chapter's pediatric flag (Y) contradicts its own rule
(0.029 is not above 2 x 0.018 = 0.036), so the film applies the rule: 3 of 5.
Re-run, then audio, then lock_cards.py, then ./art run.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

SLUG = "tldr-average-hides-the-patient"
TITLE = "Where the Average Hides the Patient"
COURSE = "INFO 7375 · Computational Skepticism · Chapter 11"

# ── the chapter's table (HEAD side; the table sits outside every conflict block) ──
ROWS = ["adults 18–64", "children 0–17", "65 and over", "pregnancy-related", "rare disease"]
N = [8420, 1210, 2850, 380, 95]
ECE = [0.019, 0.029, 0.044, 0.071, 0.103]
BASE = [0.034, 0.012, 0.078, 0.022, 0.420]
GLOBAL_N, GLOBAL_ECE, GLOBAL_BASE_PRINTED = 12955, 0.018, 0.041

assert sum(N) == GLOBAL_N                                                  # rows sum to the global N
share = [n / GLOBAL_N for n in N]
pull = [s * e for s, e in zip(share, ECE)]                                 # each row's weight x gap
# the discrepancy we do NOT show: N-weighted base rate is 0.0441, printed 0.041
assert round(sum(n * b for n, b in zip(N, BASE)) / GLOBAL_N, 4) == 0.0441 and GLOBAL_BASE_PRINTED == 0.041
# B13 NAIVE: the unweighted mean of the five rows
assert round(sum(ECE) / 5, 4) == 0.0532
assert round((sum(ECE) / 5) / GLOBAL_ECE, 1) == 3.0                        # "three times the global"
# B14 SHIFT: shares and pulls
assert round(share[0], 2) == 0.65 and round(share[4] * 100, 2) == 0.73    # adults ~2/3; rare 0.73 %
assert round(pull[0], 3) == 0.012 and round(pull[4], 4) == 0.0008
# B16 TRANSFORM: pooled ECE moves by at most share x |change in the row's gaps| (triangle inequality,
# same bins); from a perfectly calibrated row to 0.103 that is <= 0.00076; any gap is <= 1, so the
# row can never move the global by more than its share, 0.0073 < 0.01
assert pull[4] < 0.001 and share[4] < 0.01 and round(share[4], 4) == 0.0073
assert round(ECE[4] / GLOBAL_ECE, 1) == 5.7                                # "almost six times"
# B12 / B19: the chapter's rule "flag if subgroup ECE > 2x global"
TWICE = 2 * GLOBAL_ECE
flags = [e > TWICE for e in ECE]
assert abs(TWICE - 0.036) < 1e-12 and flags == [False, False, True, True, True]   # 3 of 5 (chapter's table marks pediatric Y too)
# B18: pooled ECE <= patient-weighted mean of subgroup ECEs (same bins) — 0.018 <= 0.0276
assert round(sum(pull), 3) == 0.028 and GLOBAL_ECE <= sum(pull)
# the global MCE 0.039 is likewise <= the largest subgroup bin gap (0.176) — not shown
# B01: Wong et al. (2021) as the chapter reports it — missed 1,709 of 2,552 septic patients
assert round(1709 / 2552 * 100) == 67
# BHTF transfer (exercise A5): 0.030 / 0.092 / 0.141 at 80 / 15 / 5 % (primary share = the rest)
A5 = [(0.80, 0.030), (0.15, 0.092), (0.05, 0.141)]
assert round(sum(s * e for s, e in A5), 4) == 0.0449 and 0.035 <= sum(s * e for s, e in A5)
assert [e > 2 * 0.035 for _, e in A5] == [False, True, True] and abs(0.05 * 0.141 - 0.00705) < 1e-12


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
    "Salaam. This is Liam, in for Bear, with chapter eleven of INFO 7375, Computational Skepticism for AI, at Northeastern. "
    "This film is about a calibration error of zero point zero one eight overall, and zero point one zero three on the rare-disease patients. Same model, both true. "
    "You'll see why ninety-five patients out of nearly thirteen thousand cannot move the average. "
    "The trap: reading the average as a promise to every patient.",
    remotion("ClaudeTldrWhat", {
        "eyebrow": "TL;DR", "heading": "What This Film Is About", "greeting": "Salaam, Liam", "topic": COURSE,
        "question": "The model is calibrated overall. Is it calibrated for every patient?",
        "lines": ["Calibration error 0.018 overall, 0.103 on rare-disease patients: same model, both true.",
                  "You will see why 95 patients out of 12,955 cannot move the average.",
                  "The trap: reading the average as a promise to every patient."],
        "cues": [1.5, 10.0, 17.0, 22.0], "durationSeconds": 26, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "'TL;DR.' wordmark; 'Salaam, Liam'; the course line; heading"},
         {"at": 0.06, "event": "the question writes on"},
         {"at": 0.38, "event": "line 1 lands on 'This film is about'"},
         {"at": 0.66, "event": "line 2 lands on 'You'll see why'"},
         {"at": 0.84, "event": "line 3 lands on 'The trap'"}]),
    lane="bookend"))

beats.append(beat("B01", "tldr · why",
    "Why should you care? Calibration is a promise: when the model says eighty percent, it is right eight times in ten, for the patient in front of you. "
    "Report one global number, and the smallest groups are the ones nobody checks. "
    "A widely used sepsis alert looked fine in aggregate; an outside check at one hospital found it missed two thirds of sepsis cases. "
    "And one number per group makes the hidden row stand up.",
    remotion("ClaudeTldrWhy", {
        "eyebrow": "TL;DR", "heading": "Why You Should Care", "topic": COURSE,
        "lead": "Calibration is a promise: '80%' should be right 8 times in 10, for the patient in front of you.",
        "lines": ["Report one global number, and the smallest groups are the ones nobody checks.",
                  "A widely used sepsis alert looked fine in aggregate; an outside check found it missed 67% of sepsis cases.",
                  "One number per group makes the hidden row stand up."],
        "cues": [0.8, 9.0, 13.5, 21.0], "durationSeconds": 24, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "page turn: same header, heading 'Why You Should Care'"},
         {"at": 0.04, "event": "the stake writes on"},
         {"at": 0.38, "event": "dash 1 on 'Report one global number'"},
         {"at": 0.56, "event": "dash 2 on 'A widely used sepsis alert'"},
         {"at": 0.86, "event": "dash 3 on 'one number per group'"}]),
    lane="bookend", qc={"sparse_by_design": True, "sparse_reason": "TL;DR card two — text lands on cues by design."}))

beats.append(beat("B02", "the question",
    "The question this film is really asking: is the model calibrated group by group? "
    "Not 'for every patient'. One average cannot promise that. Only a number for each group can check it.",
    remotion("BrutalistHesitantWriter", {
        "text": "Error 0.018 overall.\nIs the model calibrated\nfor every patient?",
        "triggerWords": "for every patient", "replacementWords": "group by group",
        "fontSize": 72, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
        "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'Error 0.018 overall.'"},
         {"at": 0.3, "event": "types the question; backspaces 'for every patient' → 'group by group' on the spoken correction"},
         {"at": 0.8, "event": "caret holds on the corrected question"}]),
    lane="bookend", lead_silence_s=0.8,
    motion_claim="The writer types the naive question and corrects the phrase that makes it the wrong question.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}))

beats.append(beat("B03", "terms",
    "Four terms. Calibration: when the model says eighty percent, it is right about eighty percent of the time. "
    "Calibration error, E C E: the weighted average gap between stated confidence and what actually happened. "
    "A subgroup: a named slice of patients, like children, or people over sixty-five. "
    "And a confidence bin: predictions grouped by the confidence they stated.",
    remotion("ClaudeDefinitions", {
        "title": "Terms In This Film",
        "terms": [{"term": "calibration", "meaning": "when the model says 80%, it is right about 80% of the time"},
                  {"term": "calibration error", "meaning": "ECE: the weighted average gap between confidence and outcome"},
                  {"term": "subgroup", "meaning": "a named slice of patients: children, people over 65"},
                  {"term": "confidence bin", "meaning": "predictions grouped by the confidence they stated"}],
        "durationSeconds": 20, "folderLabel": "@NikBearBrown"},
        [{"at": 0.1, "event": "'calibration' lands, terracotta"}, {"at": 0.35, "event": "'calibration error' lands"},
         {"at": 0.65, "event": "'subgroup' lands"}, {"at": 0.85, "event": "'confidence bin' lands"}]),
    lane="bookend", proof="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: prerequisites only — 'subgroup calibration error' is earned in the section."}))

# ── LEARN section 1 (B10–B19) ────────────────────────────────────────────────
beats.append(beat("B10", "learn 1",
    "Here is a calibration report. One model, twelve thousand nine hundred fifty-five patients, and one number: a calibration error of zero point zero one eight. Small. "
    "Now one row from the same report. Rare-disease cases: ninety-five patients, error zero point one zero three. Almost six times bigger. "
    "Both numbers describe the same model. How does the big one hide inside the small one?",
    manim("B10_OneNumber",
          "One wide ink bar spans the whole axis at height 0.018 — the global number over 12,955 patients; the global line and its label land at right; upper-left, the rare-disease row writes on (95 patients, error 0.103) with a terracotta dot; 'both true — how?'; small dim caption 'the chapter's illustrative table'.",
          [{"at": 0.0, "event": "axis; the global bar grows across all 12,955"}, {"at": 0.3, "event": "'global 0.018' label"},
           {"at": 0.55, "event": "rare-disease row: 95 patients, 0.103; dot"}, {"at": 0.85, "event": "'both true — how?'"}],
          "The key case, unsolved: one small number, one big row, same model."),
    role="HOOK", section=1,
    learn={"question": "The global calibration error is 0.018; the rare-disease row is 0.103. How can both be true?",
           "action": "Put the one global number on screen as a bar over all patients, then the one row beside it.",
           "observation": "The row is almost six times the global, yet the global is small.",
           "inference": "The global number is some kind of summary that the row did not move.",
           "next_question": "What happens when we split the global into its rows?"}))

beats.append(beat("B11", "learn 1",
    "First move: split the report into its five rows, one column each, and start every column at the global number. "
    "Adults, eighteen to sixty-four: zero point zero one nine. Right on the global. "
    "Children: zero point zero two nine. A little higher. So far, the global number looks like a fair summary.",
    manim("B11_SplitRows",
          "The wide bar splits into five equal columns, each at the global 0.018; names land under the axis; the adults column settles to 0.019 and the children column climbs to 0.029; value labels ride on each column top.",
          [{"at": 0.05, "event": "the bar splits into five equal columns at 0.018"}, {"at": 0.4, "event": "adults settles to 0.019"},
           {"at": 0.65, "event": "children climbs to 0.029"}, {"at": 0.9, "event": "caption: five rows, one column each"}],
          "First instance: two rows close to the global, shown moving."),
    role="INSTANCE", section=1,
    learn={"question": "Do the rows agree with the global?", "action": "Split the bar into five columns; move two to their row values.",
           "observation": "Adults 0.019 and children 0.029 sit near 0.018.", "inference": "For these rows the global is a fair summary.",
           "next_question": "And the other three rows?"}))

beats.append(beat("B12", "learn 1",
    "Keep going. People over sixty-five: zero point zero four four. Pregnancy-related: zero point zero seven one. Rare disease: zero point one zero three. "
    "Now draw the chapter's flag: a line at twice the global. Three of the five rows are above it. "
    "And the global number never moved.",
    manim("B12_ThreeClimb",
          "The three remaining columns climb one per spoken value — 0.044, 0.071, 0.103; a line draws at twice the global (0.036) with its label; three columns stand above it; the global line holds at 0.018; dot at the rare column's top.",
          [{"at": 0.05, "event": "65 and over climbs to 0.044"}, {"at": 0.25, "event": "pregnancy-related to 0.071"},
           {"at": 0.42, "event": "rare disease to 0.103"}, {"at": 0.6, "event": "the twice-global line draws"},
           {"at": 0.85, "event": "caption: three of five above it"}],
          "Second instance: three rows far from the global; the global line never moves."),
    role="INSTANCE", section=1,
    learn={"question": "What about the other three rows?", "action": "Raise each to its value; draw the twice-global flag line.",
           "observation": "Three rows exceed twice the global; the global stays at 0.018.", "inference": "The global number is not tracking these rows.",
           "next_question": "How is the global computed from the rows?"}))

beats.append(beat("B13", "learn 1",
    "Here's the natural guess: the global is just the average of the rows. Try it. "
    "Add the five errors and divide by five: zero point zero five three. The report says zero point zero one eight. Three times smaller. "
    "So the global is not listening to rows. What is it listening to?",
    manim("B13_AverageRows",
          "A dim line draws across the columns at the unweighted mean 0.053 with its label; upper-left, 'average of the rows: 0.053' against 'the report: 0.018' with a terracotta X beside the first; caption: not the average of rows.",
          [{"at": 0.2, "event": "the row-average line draws at 0.053"}, {"at": 0.55, "event": "'the report: 0.018' beside it"},
           {"at": 0.75, "event": "X beside 'average of the rows'"}, {"at": 0.9, "event": "caption"}],
          "The natural wrong turn walked to where it breaks: 0.053 is not 0.018."),
    role="NAIVE", section=1,
    learn={"question": "Is the global the average of the rows?", "action": "Average the five column heights and draw that line.",
           "observation": "0.053, three times the reported 0.018.", "inference": "The global does not weigh rows equally.",
           "next_question": "What does it weigh?"}))

beats.append(beat("B14", "learn 1",
    "Here's the reframe. The global counts patients, not rows. So make each column as wide as its row is big. "
    "Adults swell to two thirds of the axis. The rare-disease column shrinks to a sliver: ninety-five of twelve thousand nine hundred fifty-five, under one percent. "
    "Now read area, not height. Area is how loudly a row speaks in the global. Adults: zero point zero one two. The rare row: zero point zero zero zero eight.",
    manim("B14_WeighPatients",
          "The five equal columns morph in width to their patient counts (65% · 9% · 22% · 3% · 0.7%) with heights unchanged; labels follow their columns; the rare column becomes a sliver; upper-left readouts 'adults: 0.012' and 'rare disease: 0.0008'; caption 'area: patients times gap'.",
          [{"at": 0.1, "event": "widths morph to patient counts"}, {"at": 0.45, "event": "the rare column is a sliver; dot beside it"},
           {"at": 0.7, "event": "readouts: adults 0.012, rare 0.0008"}, {"at": 0.9, "event": "caption: area"}],
          "The representation: width is patients, height is gap, area is the voice in the global."),
    role="SHIFT", section=1,
    learn={"question": "What does the global weigh?", "action": "Resize every column to its patient count, heights fixed.",
           "observation": "Adults take two thirds of the width; the rare row is a sliver.", "inference": "A row's pull on the global is share times gap: its area.",
           "next_question": "How much could the sliver ever pull?"}))

beats.append(beat("B15", "learn 1",
    "Before it moves, commit. The rare-disease row holds ninety-five of twelve thousand nine hundred fifty-five patients. "
    "Here is a line one hundredth above the global. Is there any error on that row, any error at all, big enough to push the global up to it?",
    manim("B15_Predict",
          "The patient-width state holds; a dim target line draws one hundredth above the global with its label; a terracotta dot beside the sliver; everything holds on 'commit'; caption: any error at all?",
          [{"at": 0.2, "event": "the hundredth line draws"}, {"at": 0.5, "event": "dot beside the sliver"}, {"at": 0.75, "event": "HOLD"}],
          "The predict-before-reveal beat."),
    role="INSTANCE", section=1, predict=True,
    learn={"question": "Can any error on 95 of 12,955 move the global by 0.01?", "action": "Draw the target line; hold.",
           "observation": "The viewer commits.", "inference": "A prediction makes the pour evidence.", "next_question": "Pour it in."}))

beats.append(beat("B16", "learn 1",
    "Pour the sliver across the whole axis. Ninety-five patients' worth of error, spread over everyone: a film zero point zero zero zero eight thick. "
    "Push that row's error all the way to one, the worst there is, and the film is still under a hundredth. It never reaches the line. "
    "Now lift it out and divide by its own ninety-five. Same patients. Same errors. Zero point one zero three.",
    manim("B16_PourAndLift",
          "The sliver tips and spreads (area kept) into a hairline film on top of the global line — 'pull 0.0008'; a readout 'at error 1: 0.0073' stays under the hundredth line; the film gathers back into the sliver; the other columns fade; the sliver widens to the whole axis at height 0.103 — 'divided by its own 95' — against the global line, 'almost six times'.",
          [{"at": 0.05, "event": "the sliver pours into a film across the axis"}, {"at": 0.3, "event": "'at error 1: 0.0073' — under the line"},
           {"at": 0.55, "event": "film gathers back into the sliver"}, {"at": 0.7, "event": "the sliver widens to the whole axis at 0.103"},
           {"at": 0.9, "event": "'almost six times the global'"}],
          "The collision: the same 95 patients' errors, divided by 12,955 then by 95 — hairline, then tower. Narration short."),
    role="TRANSFORM", section=1,
    learn={"question": "Can the rare row move the global?", "action": "Spread its area over the whole axis; then give it its own denominator.",
           "observation": "Spread, it is 0.0008 thick and at most 0.0073 even at error 1; on its own, it stands at 0.103.",
           "inference": "The denominator decides whether the row is heard.", "next_question": "Say it as a formula."}))

beats.append(beat("B17", "learn 1",
    "This deserves a name: subgroup calibration error. Same formula as the global, with one change. "
    "Sum over the confidence bins; weigh each bin by its share; take the gap between accuracy and confidence. But count the shares inside the group: divide by N sub g, the group's own size, not by everyone. "
    "Then report the global and every group's number beside it, and flag any group above twice the global.",
    manim("B17_NameIt",
          "The sliver shrinks to the lower right; the per-subgroup formula writes on term by term; a brace lands under N_g labelled 'the group's own size' with a terracotta dot; 'subgroup calibration error' lands bold; then the reporting rule in two lines.",
          [{"at": 0.1, "event": "the formula writes on"}, {"at": 0.45, "event": "brace under N_g on 'the group's own size'"},
           {"at": 0.6, "event": "'subgroup calibration error'"}, {"at": 0.85, "event": "the reporting rule"}],
          "The abstraction arrives as the name for the lift."),
    role="ABSTRACTION", section=1,
    learn={"question": "What is the rule?", "action": "Write ECE_g with its denominator marked.",
           "observation": "The only change from the global formula is N_g.", "inference": "Every named group gets its own number; the global alone is not a report.",
           "next_question": "What does each symbol mean, exactly?"}))

beats.append(beat("B18", "learn 1",
    "Read the line. Left: the calibration error for group g. Right: a sum over confidence bins. "
    "In each bin, the share of the group that landed there, times the gap between how often it was right and how sure it said it was. "
    "The only new symbol is N sub g, the group's own size. For the rare row: in the global, its ninety-five patients carry a weight of zero point zero zero seven three. In its own number, they carry all of it. "
    "One more thing: the pooled number can sit even below the rows' patient-weighted average, zero point zero two eight, because inside a shared bin, over- and under-confident groups cancel.",
    manim("B18_Tangent",
          "The formula persists at the top; below, the zones write one per sentence: left side, right side, the glossary (bins · share of the group · the gap · N_g), the two worked weights 95/12,955 = 0.0073 and 95/95 = 1, and the cancellation line 0.018 ≤ 0.028.",
          [{"at": 0.05, "event": "left / right sentences"}, {"at": 0.3, "event": "glossary rows"},
           {"at": 0.55, "event": "95/12,955 = 0.0073 and 95/95 = 1"}, {"at": 0.85, "event": "0.018 ≤ 0.028: gaps cancel"}],
          "The equation tangent: formula, sentences, glossary, worked weights."),
    role="TANGENT", section=1,
    learn={"question": "What does each symbol mean?", "action": "Translate both sides; gloss the symbols; plug in the rare row's weights.",
           "observation": "0.0073 in the pool, 1 on its own.", "inference": "The notation is the lift we watched.",
           "next_question": "Back to the report."}))

beats.append(beat("B19", "learn 1",
    "Back to the report. Zero point zero one eight overall. Zero point one zero three on the rare-disease row. Both true. "
    "The global weighs patients, and ninety-five patients are under one percent of the weight. Split it by group and the row stands up. "
    "Not taught here: what ratio should halt a deployment. The chapter calls that a values question. And a model calibrated on the wrong label passes every check in this film.",
    manim("B19_BothTrue",
          "The HOOK state returns (the one wide bar at 0.018 and the rare-disease row); the bar splits straight into patient-width columns that rise to their values; dot beside 'rare disease 0.103'; 'both true' and 'report every group' land; dim boundary caption 'not taught here: when to halt'.",
          [{"at": 0.05, "event": "the HOOK state returns"}, {"at": 0.35, "event": "the bar splits into patient-width columns that rise"},
           {"at": 0.6, "event": "'both true · report every group'"}, {"at": 0.85, "event": "boundary caption"}],
          "The HOOK's objects resolve; the boundary names what was not taught."),
    role="PAYOFF", section=1,
    learn={"question": "So how can 0.018 and 0.103 both be true?", "action": "Split the hook's bar by patient share and let each row stand.",
           "observation": "The rare row is a sliver of the global and a tower on its own.", "inference": "Report the global and every group.",
           "next_question": ""}))

beats.append(beat("BVDT", "verdict",
    "Let's recap with Claude. A global calibration error weighs patients, not groups: ninety-five of twelve thousand nine hundred fifty-five carry under one percent of the weight. "
    "Even at the worst possible error, that row could move the global by less than a hundredth. "
    "Give each group its own denominator and the hidden row stands at zero point one zero three. "
    "Report the global and every group, and flag any group above twice the global.",
    remotion("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": TITLE,
        "artifactLines": ["A global calibration error weighs patients: 95 of 12,955 carry under 1% of the weight.",
                          "Even at the worst possible error, that row moves the global by less than 0.01.",
                          "Give each group its own denominator and the hidden row stands at 0.103.",
                          "Report the global and every group; flag any group above twice the global."]},
        [{"at": 0.0, "event": "artifact page opens"}, {"at": 0.2, "event": "four verdict lines land"}]),
    lane="bookend", lead_silence_s=0.5, qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}))

YT = ("A model reports a global calibration error (ECE) of 0.035 with 10 bins. Three groups: the primary group (80% of patients) at 0.030, "
      "a secondary group (15%) at 0.092, and a tertiary group (5%) at 0.141. "
      "Before computing anything, predict: which groups does the 'more than twice the global' flag catch, and could the tertiary group, at any error at all, move the global by a hundredth? "
      "Then compute each group's pull (share times ECE) and the patient-weighted average, and explain why the global 0.035 can sit below it. "
      "Finally, write one plain-English summary sentence that does not hide the tertiary group.")
beats.append(beat("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT + " "
    "Two things to look for. Did it predict before it computed? If it jumped to numbers, send it back. "
    "And does its summary sentence name the tertiary group's number, not just the global?",
    remotion("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "INFO 7375 · YOUR TURN", "segment": "Split It Yourself",
        "command": YT, "runningText": "paste this into Claude…",
        "output": ["Check: the prediction came before the arithmetic.",
                   "Check: the summary names 0.141, not just 0.035."],
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
    "audience": "INFO 7375 students, and anyone handed a single calibration number and asked to sign off on a deployment",
    "course": "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University",
    "source_doc": "chapters/11-communicating-uncertainty-calibrating-claims-to-evidence.md, §'Subgroup calibration: where aggregate metrics lie' (the subgroup table, ECE_g, Wong et al. 2021), §'What calibration metrics cannot see', 'Still puzzling', exercise A5; section S2 of youtube/tldr-sections-11-communicating-uncertainty.md",
    "sections": [{"n": 1, "title": "Where the Average Hides the Patient", "key_case": "global ECE 0.018 on 12,955 patients vs rare-disease ECE 0.103 on 95 (the chapter's illustrative table)"}],
    "greeting_language": "Arabic/Farsi (Salaam)",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "outro_policy": "OUTRO-LOCK §Voice: spoken title + 'At Nik Bear Brown', 1.0 s silent tail padded into the mp3, no jingle.",
    "bookloop_policy": "Course film: carries the INFO 7375 course credit (spoken in B00, on the cards' course line).",
    "tags": ["calibration", "expected calibration error", "subgroup analysis", "aggregate metrics", "medical AI", "INFO 7375", "3Blue1Brown style", "Claude", "Nik Bear Brown"]},
    "beats": beats}
out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"{len(beats)} beats → {out}")
