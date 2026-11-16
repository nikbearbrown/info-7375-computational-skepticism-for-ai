#!/usr/bin/env python3
"""make_sheet.py — writes beat_sheet.json for tldr-the-99-percent-test.

tldr skill (brutalist.art/skills/make/tldr). Section S1 of chapter 2
(youtube/tldr-sections-02-probability-confidence.md): "The Test That Is 99%
Accurate". Every number is the chapter's own or recomputed here from the
chapter's inputs (base rate 1/10,000, 99% for both rates) and asserted at import;
FACTCHECK.md carries the rows. Re-run, then audio, then ./art run.
"""
import json, sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent

SLUG = "tldr-the-99-percent-test"
TITLE = "The Test That Is 99% Accurate"
COURSE = "INFO 7375 · Computational Skepticism · Chapter 2"

# ── the chapter's inputs ────────────────────────────────────────────────────
N = 10_000
PRIOR = F(1, 10_000)          # "About one person in ten thousand has it."
SENS = F(99, 100)             # "correctly identifies people who are sick"
SPEC = F(99, 100)             # "correctly returns negative on 99% of healthy people"
FPR = 1 - SPEC

# the count (chapter: "one true positive, and about one hundred false positives")
TRUE_POS = 1                                         # the chapter's count: the one sick person is caught
FALSE_POS_EXACT = FPR * (N - 1)                      # 0.01 × 9,999 = 99.99
FALSE_POS = round(FALSE_POS_EXACT)                   # ≈ 100 (lit on screen)
assert FALSE_POS_EXACT == F(9999, 100) and FALSE_POS == 100
COUNT_SHARE = F(TRUE_POS, TRUE_POS + FALSE_POS)      # 1/101
assert abs(float(COUNT_SHARE) - 0.00990099) < 1e-8   # the chapter's term table: ≈ 0.0099

# Bayes, the chapter's line: 0.0001×0.99 / (0.0001×0.99 + 0.9999×0.01)
NUM = PRIOR * SENS
DEN = PRIOR * SENS + (1 - PRIOR) * FPR
POST = NUM / DEN
assert NUM == F(99, 1_000_000)                        # 0.000099
assert DEN == F(10098, 1_000_000)                     # 0.010098 (≈ 0.0101, the table's P(positive))
assert abs(float(POST) - 0.0098039) < 1e-6            # the chapter's prose: ≈ 0.0098
assert round(float(POST), 2) == 0.01 and round(float(COUNT_SHARE), 2) == 0.01   # both "about one percent"
# the lift the test gives (Figure 2.6 caption: "raises the probability of disease a hundredfold")
assert 97 < float(POST / PRIOR) < 99                  # 98.04× — "almost a hundredfold"
# odds form: posterior odds = prior odds × 99 exactly
assert (POST / (1 - POST)) / (PRIOR / (1 - PRIOR)) == SENS / FPR == 99

# the instances: 100 sick → 99 positive; 100 healthy → 1 positive
assert SENS * 100 == 99 and FPR * 100 == 1

# YOUR TURN (not shown in the film; FACTCHECK row): PPV across base rates at 99/99
def ppv(p): return p * SENS / (p * SENS + (1 - p) * FPR)
assert ppv(F(1, 100)) == F(1, 2)                      # the coin-flip point the viewer is asked to find
assert abs(float(ppv(F(1, 1000))) - 0.0902) < 1e-4 and abs(float(ppv(F(1, 100_000))) - 0.00099) < 1e-5

# Sepsis scale-shift (chapter, citing Wong et al., JAMA Internal Medicine 181(8), 2021)
SEPSIS_ALERT = 18; SEPSIS_SENS = 33; SEPSIS_MISSED = 67
assert SEPSIS_SENS + SEPSIS_MISSED == 100


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
    "Ahoj. This is Liam, in for Bear, with chapter two of INFO 7375, Computational Skepticism for AI, at Northeastern. "
    "This film is about a test that is ninety-nine percent accurate, and a positive result that means about one percent. "
    "Count ten thousand people, and the positives come mostly from the healthy: about a hundred false, one true. "
    "The trap: reading the test's accuracy as the answer, and forgetting how rare the disease was.",
    remotion("ClaudeTldrWhat", {
        "eyebrow": "TL;DR", "heading": "What This Film Is About", "greeting": "Ahoj, Liam", "topic": COURSE,
        "question": "The test is 99% accurate and it says positive. Is the patient 99% likely to be sick?",
        "lines": ["A 99% accurate test, a 1-in-10,000 disease, a positive result: about a 1% chance of disease.",
                  "Count 10,000 people: the positives come mostly from the healthy. About 100 false, 1 true.",
                  "The trap: reading the test's accuracy as the answer and forgetting how rare the disease was."],
        "cues": [1.5, 9.0, 15.0, 21.0], "durationSeconds": 27, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "'TL;DR.' wordmark; 'Ahoj, Liam'; the course line; heading"},
         {"at": 0.06, "event": "the question writes on"},
         {"at": 0.33, "event": "line 1 lands on 'a test that is ninety-nine percent accurate'"},
         {"at": 0.56, "event": "line 2 lands on 'count ten thousand people'"},
         {"at": 0.78, "event": "line 3 lands on 'the trap'"}]),
    lane="bookend"))

beats.append(beat("B01", "tldr · why",
    "Why should you care? Every alert you will ever triage, fraud, an intrusion, a screening flag, is this test. "
    "When the thing you hunt is rare, even an excellent detector fires mostly on the innocent. "
    "Miss that, and your team learns the alarms mean nothing, then ignores the real one. "
    "See the base rate, and you know what a flag is worth before you act on it.",
    remotion("ClaudeTldrWhy", {
        "eyebrow": "TL;DR", "heading": "Why You Should Care", "topic": COURSE,
        "lead": "Every alert you will ever triage — fraud, an intrusion, a screening flag — is this test.",
        "lines": ["When the thing you hunt is rare, even an excellent detector fires mostly on the innocent.",
                  "Miss that, and your team learns the alarms mean nothing, then ignores the real one.",
                  "See the base rate, and you know what a flag is worth before you act on it."],
        "cues": [1.0, 7.0, 12.0, 17.0], "durationSeconds": 21, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "page turn: same header, heading 'Why You Should Care'"},
         {"at": 0.06, "event": "the stake writes on"},
         {"at": 0.35, "event": "dash 1 on 'the thing you hunt is rare'"},
         {"at": 0.58, "event": "dash 2 on 'miss that'"},
         {"at": 0.8, "event": "dash 3 on 'see the base rate'"}]),
    lane="bookend", qc={"sparse_by_design": True, "sparse_reason": "TL;DR card two — text lands on cues by design."}))

beats.append(beat("B02", "the question",
    "The real question: how likely is a positive to mean disease? "
    "Not how likely a sick person is to test positive. That is the ninety-nine percent on the box. Flip the question, and the answer changes.",
    remotion("BrutalistHesitantWriter", {
        "text": "The test is 99% accurate.\nIt says positive. How likely\nis a sick person to test positive?",
        "triggerWords": "a sick person to test positive", "replacementWords": "a positive to mean disease",
        "fontSize": 64, "charMs": 26, "hesitateBetween": 7, "hesitateWithin": 1, "mistakeRate": 5, "jitter": 20,
        "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'The test is 99% accurate.'"},
         {"at": 0.35, "event": "types the naive question; backspaces 'a sick person to test positive' → 'a positive to mean disease'"},
         {"at": 0.85, "event": "caret holds on the corrected question"}]),
    lane="bookend", lead_silence_s=0.8,
    motion_claim="The writer types the naive question and corrects the phrase that makes it the wrong question.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}))

beats.append(beat("B03", "terms",
    "Three terms. Base rate: how common the condition is before any test. Here, one in ten thousand. "
    "False positive: a positive result on someone who is actually healthy. "
    "And the vertical bar, read 'given': P of A given B is the chance of A, counting only the cases where B happened.",
    remotion("ClaudeDefinitions", {
        "title": "Terms In This Film",
        "terms": [{"term": "base rate", "meaning": "how common the condition is before any test; here, 1 in 10,000"},
                  {"term": "false positive", "meaning": "a positive result on someone who is actually healthy"},
                  {"term": "P(A | B)", "meaning": "read 'A given B': the chance of A, counting only cases where B happened"}],
        "durationSeconds": 17, "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'base rate' lands, terracotta"}, {"at": 0.42, "event": "'false positive' lands; first settles"},
         {"at": 0.68, "event": "'P(A | B)' lands"}]),
    lane="bookend", proof="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: prerequisites only — Bayes' theorem is earned in the section."}))

# ── LEARN section 1 (B10–B19) ────────────────────────────────────────────────
beats.append(beat("B10", "learn 1",
    "One patient. A disease that about one person in ten thousand has. A test the company says is ninety-nine percent accurate. "
    "The result comes back positive. "
    "So how likely is it that this patient is sick? The rail at the bottom is where the answer goes. For now it holds a question mark.",
    manim("B10_OnePositive",
          "One ink dot (the patient) at left with a 'positive' tag; right: the two facts 'disease: 1 in 10,000' and 'test: 99% accurate'; the chance rail (0% · 50% · 100%) draws along the bottom right, and a '?' sits over its middle.",
          [{"at": 0.0, "event": "the patient dot"}, {"at": 0.25, "event": "the two facts land on their clauses"},
           {"at": 0.5, "event": "'positive' tag on 'comes back positive'"}, {"at": 0.75, "event": "the rail draws; '?' holds"}],
          "The key case, unsolved: one patient, one positive, an empty rail."),
    role="HOOK", section=1,
    learn={"question": "A 99% accurate test says positive. How likely is the patient sick?",
           "action": "Put the patient, the two facts and an empty answer rail on screen.",
           "observation": "Two numbers are given; the answer is not.",
           "inference": "Whatever the answer is, it has to be built from these two numbers.",
           "next_question": "What does 'ninety-nine percent accurate' actually promise?"}))

beats.append(beat("B11", "learn 1",
    "First, what the ninety-nine percent promises. Take a hundred people who really are sick, one square each. Run the test. "
    "Ninety-nine light up positive. One slips through. "
    "That is the test's hit rate on the sick: ninety-nine out of a hundred, exactly as printed.",
    manim("B11_TheSick",
          "The patient dot grows into a 10×10 block of 100 squares, all marked 'sick'; a scan line sweeps across; 99 squares fill ink ('positive'), one stays pale; the tally 'sick → positive: 99 of 100' lands on the right.",
          [{"at": 0.1, "event": "the dot becomes a block of 100 sick"}, {"at": 0.35, "event": "the scan sweeps; 99 fill ink"},
           {"at": 0.6, "event": "one square stays pale"}, {"at": 0.8, "event": "tally: 99 of 100"}],
          "First instance: the test on the sick, shown moving."),
    role="INSTANCE", section=1,
    learn={"question": "What does the test do to people who are sick?", "action": "Run it on 100 sick people.",
           "observation": "99 test positive; 1 is missed.", "inference": "99% is a rate among the sick.",
           "next_question": "And on people who are healthy?"}))

beats.append(beat("B12", "learn 1",
    "Now a hundred healthy people. Ninety-nine percent accurate also means the test clears ninety-nine of them. "
    "One lights up anyway: a false positive. One in a hundred. Small. Remember that one. "
    "Real tests print two separate rates here; this example uses one number for both jobs.",
    manim("B12_TheHealthy",
          "The same block turns to 100 healthy; the scan sweeps again; 99 stay pale and one fills ink — the false positive, with a terracotta dot beside it; tally 'healthy → positive: 1 of 100'; dim caption 'one number, two jobs — simplified'.",
          [{"at": 0.1, "event": "the block recolors to healthy"}, {"at": 0.35, "event": "the scan sweeps; one fills ink"},
           {"at": 0.55, "event": "dot beside the false positive"}, {"at": 0.85, "event": "caption: one number, two jobs"}],
          "Second instance: the test on the healthy; the simplification marked once."),
    role="INSTANCE", section=1,
    learn={"question": "What does the test do to healthy people?", "action": "Run it on 100 healthy people.",
           "observation": "99 clear; 1 lights up falsely.", "inference": "The test has a 1% false-alarm rate on the healthy.",
           "next_question": "So what does a positive mean?"}))

beats.append(beat("B13", "learn 1",
    "The obvious answer: the test is ninety-nine percent accurate, it said positive, so about ninety-nine percent. "
    "Most engineers say above ninety. In a classic 1978 study, most of sixty Harvard physicians and students answered about ninety-five, on a one-in-a-thousand version. "
    "But look at what the ninety-nine measured: positive, given sick. We were asked the other way round: sick, given positive.",
    manim("B13_TheObviousAnswer",
          "The knob slides along the rail to 99%; a ghost band marks 90–100% ('most answers'); the left side writes P(positive | sick) = 0.99, then beneath it P(sick | positive) = ? ; the two conditions swap places in a short morph and an X lands beside the '='-link between them.",
          [{"at": 0.1, "event": "knob slides to 99%"}, {"at": 0.35, "event": "band: most answers land 90–100%"},
           {"at": 0.65, "event": "P(+ | sick) = 0.99 writes"}, {"at": 0.85, "event": "flipped: P(sick | +) = ?  — X beside the link"}],
          "The natural wrong turn, walked to where it breaks: the bar was read backwards."),
    role="NAIVE", section=1,
    learn={"question": "Isn't the answer just 99%?", "action": "Slide the knob to 99% and write what 99% measured.",
           "observation": "99% is P(positive | sick); the question is P(sick | positive).",
           "inference": "The obvious answer answers a different question.",
           "next_question": "How do we get from one to the other?"}))

beats.append(beat("B14", "learn 1",
    "So stop looking at one patient. Picture everyone who takes the test: ten thousand people, one square each. "
    "On average, one of them is sick. There, one square. The other nine thousand nine hundred ninety-nine are healthy. "
    "Now both facts we just watched can act on the whole crowd at once.",
    manim("B14_TenThousand",
          "A 100×100 grid of 10,000 pale squares builds row-band by row-band; one square turns terracotta-dotted — the one sick person; labels '10,000 people', '1 sick', '9,999 healthy' land on the right; the rail stays empty at '?'.",
          [{"at": 0.1, "event": "the grid of 10,000 builds"}, {"at": 0.45, "event": "one square marked sick"},
           {"at": 0.7, "event": "'9,999 healthy' lands"}, {"at": 0.9, "event": "the crowd holds"}],
          "The representation: the population, counted, one square per person."),
    role="SHIFT", section=1,
    learn={"question": "What if we count people instead of reasoning about one?", "action": "Lay out 10,000 people, one square each.",
           "observation": "One sick square in a sea of 9,999 healthy.", "inference": "The base rate is now a visible count.",
           "next_question": "What happens when the test runs on all of them?"}))

beats.append(beat("B15", "learn 1",
    "Before anything lights up: commit. The test is about to run on all ten thousand. "
    "The sick one will light. One in a hundred of the healthy will light too. "
    "Of all the squares that light, what share will be the sick one? Pick a number. Lock it in.",
    manim("B15_Commit",
          "The grid holds; an empty dashed 'positives' pen draws on the right; a '?' sits in it; the rail's '?' pulses once; nothing else moves.",
          [{"at": 0.1, "event": "the empty pen draws"}, {"at": 0.5, "event": "HOLD — nothing moves on 'lock it in'"}],
          "The predict-before-reveal beat."),
    role="INSTANCE", section=1, predict=True,
    learn={"question": "Of all the positives, what share is the sick one?", "action": "Hold the picture; name the run.",
           "observation": "The viewer commits a number.", "inference": "A locked prediction turns the run into evidence.",
           "next_question": "Run it."}))

beats.append(beat("B16", "learn 1",
    "Run it. The sick square lights. Now one percent of the healthy: about a hundred squares, scattered everywhere. "
    "Pull every lit square into the pen. "
    "One sick. About a hundred healthy. The positive you are holding is one of a hundred and one. "
    "About one percent.",
    manim("B16_ThePile",
          "The sick square lights; 100 pale squares across the grid fill ink, scattered; then every lit square flies from the grid into the pen and packs into a block of 101 — one terracotta-dotted, 100 ink; the tally '1 of 101'; the knob slides from '?' down the rail to about 1%.",
          [{"at": 0.05, "event": "the sick square lights"}, {"at": 0.25, "event": "100 healthy squares light across the grid"},
           {"at": 0.5, "event": "every lit square flies into the pen"}, {"at": 0.8, "event": "'1 of 101'; knob to ≈ 1%"}],
          "The collision: the hit rate and the false-alarm rate meet in one pile; narration short."),
    role="TRANSFORM", section=1,
    learn={"question": "What share of the positives is the sick one?", "action": "Light the sick square and 1% of the healthy; gather every lit square.",
           "observation": "1 true positive among about 101 positives.",
           "inference": "A positive is about 1% likely to mean disease: the healthy crowd outnumbers the sick even after a 99% filter.",
           "next_question": "Can we write the pile down as a rule?"}))

beats.append(beat("B17", "learn 1",
    "What we just did deserves its name. The chance of disease given a positive is the sick square's share of the pile. "
    "On top: how common the disease is, times how often the sick test positive. "
    "Underneath: the whole pile. That same piece, plus the healthy share times the false alarm rate. "
    "That is Bayes' theorem. And look where the base rate sits: on top, with the same weight as the test.",
    manim("B17_NameIt",
          "The grid fades; the pile of 101 holds at left; Bayes' theorem in the disease form assembles on the right — the numerator P(D)P(+|D) lands with a line 'top: the one sick square', the denominator with 'bottom: the whole pile'; a terracotta dot lands beside P(D) as 'the base rate, on top'.",
          [{"at": 0.1, "event": "grid fades; pile holds"}, {"at": 0.3, "event": "numerator writes on 'on top'"},
           {"at": 0.55, "event": "denominator writes on 'underneath'"}, {"at": 0.85, "event": "dot beside P(D): the prior on top"}],
          "The abstraction arrives as the name for the pile; each term maps to squares already seen."),
    role="ABSTRACTION", section=1,
    learn={"question": "What is the rule behind the pile?", "action": "Write the sick share of the pile as a fraction of probabilities.",
           "observation": "Top: prior × hit rate. Bottom: every way to get a positive.",
           "inference": "Posterior is proportional to prior times likelihood; the prior cannot be dropped.",
           "next_question": "What does each symbol mean, and do the numbers agree with the count?"}))

beats.append(beat("B18", "learn 1",
    "Read the line. Left: the chance of disease, given a positive. On top: the base rate, one in ten thousand, times the hit rate, point nine nine. "
    "Underneath: that same piece, plus the healthy share times the false alarm rate, point zero one. Every way to get a positive, added up. "
    "Plug in the numbers: about point zero zero nine eight. "
    "The count said one in a hundred and one, because it let the test catch the sick person for certain. Both are about one percent.",
    manim("B18_ReadTheLine",
          "Split stage: the compact theorem P(D|+) = P(D)P(+|D) / P(+) persists left; the right band writes a glossary — P(D) prior 0.0001 · P(+|D) hit rate 0.99 · P(+|H) false alarms 0.01 · P(+) the whole pile ≈ 0.0101; then the left works the numbers: 0.0001×0.99 / (0.0001×0.99 + 0.9999×0.01) = 0.000099 / 0.010098 ≈ 0.0098; caption: the count said 1/101 ≈ 0.0099.",
          [{"at": 0.05, "event": "compact theorem; LHS highlighted"}, {"at": 0.25, "event": "glossary rows land"},
           {"at": 0.55, "event": "worked fraction writes"}, {"at": 0.75, "event": "≈ 0.0098"}, {"at": 0.9, "event": "1/101 ≈ 0.0099 caption"}],
          "The equation tangent: formula, glossary, worked values; the count and the formula reconciled."),
    role="TANGENT", section=1,
    learn={"question": "What does each symbol mean?", "action": "Gloss each term; plug in the chapter's numbers.",
           "observation": "0.000099 / 0.010098 ≈ 0.0098; the count gave 1/101 ≈ 0.0099.",
           "inference": "The formula is the count written down; the small gap is the 99% hit rate vs a sure catch.",
           "next_question": "Back to the patient."}))

beats.append(beat("B19", "learn 1",
    "Back to our patient. Before the test: one in ten thousand. After a positive: about one in a hundred. "
    "The test did real work, almost a hundredfold. And the answer is still about one percent. Both are true. "
    "The same shape shows up at hospital scale: one widely used sepsis model, checked externally, alerted on eighteen percent of all patients, and still missed two thirds of the sepsis. "
    "Not found here: how common a disease must be before a positive is a coin flip.",
    manim("B19_BackToThePatient",
          "The patient dot and 'positive' tag return at left; the knob sits at ≈ 1%; a dim before-marker at 0.01% and the line 'before: 1 in 10,000 → after: ≈ 1 in 100'; 'almost 100× — still ≈ 1%' lands; one dim line 'hospital scale: alerts on 18% of patients'; boundary caption 'not found here: the coin-flip point'.",
          [{"at": 0.05, "event": "the patient returns; knob at ≈ 1%"}, {"at": 0.3, "event": "before → after lands"},
           {"at": 0.5, "event": "'almost 100×, still ≈ 1%'"}, {"at": 0.72, "event": "hospital-scale line"}, {"at": 0.92, "event": "boundary caption"}],
          "The HOOK's objects resolve; the boundary becomes the YOUR TURN."),
    role="PAYOFF", section=1,
    learn={"question": "So how likely is this patient sick?", "action": "Put the patient back beside the rail at its earned value.",
           "observation": "About 1% — up almost a hundredfold from the base rate.",
           "inference": "A positive raises the chance; the base rate decides how far it can go.", "next_question": ""}))

beats.append(beat("BVDT", "verdict",
    "Let's recap with Claude. A ninety-nine percent accurate test, a one-in-ten-thousand disease, a positive result: about a one percent chance of disease. "
    "Ninety-nine percent is positive given sick; the question was sick given positive. "
    "Count ten thousand people: one true positive, about a hundred false. "
    "Bayes writes the count down, and the base rate sits on top, with the same weight as the test.",
    remotion("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": TITLE,
        "artifactLines": ["A 99% accurate test, a 1-in-10,000 disease, a positive result: about a 1% chance of disease.",
                          "99% is P(positive | sick). The question was P(sick | positive).",
                          "Count 10,000 people: 1 true positive, about 100 false. The healthy crowd wins the pile.",
                          "Bayes writes the count down. The base rate sits on top, with the same weight as the test."]},
        [{"at": 0.0, "event": "artifact page opens"}, {"at": 0.2, "event": "four verdict lines land"}]),
    lane="bookend", lead_silence_s=0.5, qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}))

YT = ("Take a test that catches 99% of sick people and clears 99% of healthy ones. "
      "Before computing anything, predict the base rate at which a positive result becomes a coin flip: a 50% chance of disease. "
      "Then compute the chance of disease given a positive at base rates of 1 in 100, 1 in 1,000, 1 in 10,000 and 1 in 100,000 — "
      "first by counting a population, then with Bayes' theorem. "
      "Finally, name one detector in my own field and the base rate it works against.")
beats.append(beat("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT + " "
    "Two things to look for. Did it lock a prediction before it computed? If it jumped to numbers, send it back. "
    "And did the counting and Bayes agree at every base rate?",
    remotion("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "INFO 7375 · YOUR TURN", "segment": "Find The Coin Flip",
        "command": YT, "runningText": "paste this into Claude…",
        "output": ["Check: the prediction came before the arithmetic.",
                   "Check: counting and Bayes agree at every base rate."],
        "folderLabel": "@NikBearBrown", "modelLabel": "Fable 5", "effortLabel": "High"},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two rubric lines land"}]),
    lane="bookend"))

beats.append(beat("BOUT", "outro", "The Test That Is Ninety-Nine Percent Accurate. At Nik Bear Brown.",
    remotion("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""},
             [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot. Liam reads the title, then 'At Nik Bear Brown'. No jingle."}]),
    lane="bookend", kind="outro_voice", tail_silence_s=1.0,
    hold_note="spoken outro + 1.0 s silent tail (apad into the mp3); no jingle (OUTRO-LOCK §Voice). '99%' spoken as 'ninety-nine percent' for the TTS."))

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "INFO 7375 · TL;DR", "skill": "tldr", "style_preset": "tldr",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "learn_canvas": "cream", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160, "caption_policy": "none",
    "audience": "INFO 7375 students, and anyone who has read a flag, an alert or a screening result as if its accuracy were the answer",
    "course": "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University",
    "source_doc": "chapters/02-probability-uncertainty-and-the-confidence-illusion.md, §'The test that is 99% accurate, and the patient it kills', §'Bayes' theorem — the bookkeeping made explicit', §'The false-positive structure is everywhere' (Figures 2.5, 2.6; Glimmer 2.3); section S1 of youtube/tldr-sections-02-probability-confidence.md",
    "sections": [{"n": 1, "title": "The Test That Is 99% Accurate", "key_case": "base rate 1/10,000, 99% for both rates, one positive → 1 true + ≈100 false positives among 10,000 → ≈ 1%"}],
    "greeting_language": "Czech (Ahoj)",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "outro_policy": "OUTRO-LOCK §Voice: spoken title + 'At Nik Bear Brown', 1.0 s silent tail padded into the mp3, no jingle.",
    "bookloop_policy": "Course film: carries the INFO 7375 course credit (spoken in B00, on the cards' course line).",
    "tags": ["Bayes theorem", "base rate", "false positives", "base rate fallacy", "INFO 7375", "computational skepticism", "3Blue1Brown style", "Claude", "Nik Bear Brown"]},
    "beats": beats}
out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"{len(beats)} beats → {out}")
