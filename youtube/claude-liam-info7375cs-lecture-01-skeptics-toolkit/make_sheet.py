#!/usr/bin/env python3
"""
make_sheet.py — provenance for beat_sheet.json
(claude-liam-info7375cs-lecture-01-skeptics-toolkit).
Run once to (re)generate the sheet; afterwards edit beat_sheet.json directly.
deep-explainer · claude-liam · Kokoro am_onyx · Claude skin · COURSE FILM
INFO 7375 Computational Skepticism for AI, Lecture 1.
"""
import json, datetime

SLUG  = "claude-liam-info7375cs-lecture-01-skeptics-toolkit"
TITLE = "The Skeptic's Toolkit"
COLORS = ["#D97757", "#3D3929", "#8B8F96"]
WPS = 2.9

def est(words):
    return round(len(words.split()) / WPS, 1)

def base(bid, act, lane, narration, proof="SHOW"):
    return {
        "beat_id": bid, "act": act, "lane": lane, "proof_gate": proof,
        "narration_text": narration,
        "estimated_duration_s": est(narration) if narration else 4.0,
        "voice": "am_onyx", "engine": "kokoro",
    }

def act_card(bid, act_name, label1, label2, narration):
    """Narrated FormACard (light) for act-break cards."""
    b = base(bid, act_name, "card", narration, proof="CARD")
    b["shot"] = {
        "type": "CARD", "source": "own",
        "remotion": {
            "pattern": "FormACard",
            "props": {"lines": [label1, label2], "dark": False},
            "rendered": {"out": f"media/{bid}.mp4", "at": ""},
        },
    }
    b["motion_claim"] = (
        "Act label lands first; the headline springs in on the second beat — "
        "two staged reveals, then a hard cut."
    )
    return b

def manim(bid, act, narration, cls, intent, show, note, claim=None):
    b = base(bid, act, "manim", narration)
    b["shot"] = {
        "type": "GRAPHIC", "source": "own",
        "visual_intent": intent, "show": show,
        "manim": {"class": cls},
    }
    if claim:
        b["shot"]["motion_claim"] = claim
    b["graphic"] = {
        "scene": cls, "engine": "manim", "mechanic": intent,
        "colors": COLORS,
        "verify_module": f"scenes.py::{cls}::VERIFY", "note": note,
    }
    return b

def remotion(bid, act, narration, pattern, props, show, lane="bookend", extra=None):
    b = base(bid, act, lane, narration)
    b["shot"] = {
        "type": "REMOTION", "source": "own", "show": show,
        "remotion": {
            "pattern": pattern, "props": props,
            "rendered": {"out": f"media/{bid}.mp4", "at": ""},
        },
    }
    if extra:
        b.update(extra)
    return b

beats = []

# ─────────────────────────── B00 cold open ───────────────────────────
beats.append(remotion("B00", "cold open",
    "Aloha. This is Liam, in for Bear, with lecture one of Computational Skepticism for AI. "
    "A sepsis model ran in hundreds of hospitals and passed every test. Then someone checked "
    "it against the patients. What went wrong? Nothing, by the builders' measures. "
    "It missed two of every three. The gap between those sentences is the course.",
    "ClaudeComposerAsk",
    {
        "greeting": "Aloha, Liam",
        "topic": "INFO 7375 COMPUTATIONAL SKEPTICISM · LECTURE 1",
        "segment": "The Skeptic's Toolkit",
        "command": (
            "A sepsis model ran in hundreds of hospitals and passed every test. "
            "Then someone checked it against the patients. What went wrong?"
        ),
        "runningText": "reading the chapter and the external audit…",
        "output": [
            "Nothing, by the builders' measures.",
            "It missed two of every three.",
            "The gap between those sentences is the course.",
        ],
        "folderLabel": "@NikBearBrown",
        "modelLabel": "claude-opus-4-7",
        "effortLabel": "High",
    },
    [
        {"at": 0.0,  "event": "Composer opens on cream — greeting 'Aloha, Liam'"},
        {"at": 0.25, "event": "Command types letter by letter"},
        {"at": 0.6,  "event": "Send button arms (terracotta); running indicator"},
        {"at": 0.75, "event": "Three output lines land sequentially"},
    ]))

# ─────────────────────────── B01 hesitant writer (BLUF) ───────────────────────────
beats.append(remotion("B01", "executive summary",
    "A sepsis model missed two of every three patients — and the model was working. "
    "It passed every test its builders chose. The test was the thing that failed. "
    "That gap is this course.",
    "BrutalistHesitantWriter",
    {
        "text": (
            "A sepsis model missed two of every three patients.\n"
            "So the model was broken.\n"
            "It passed every test its builders chose.\n"
            "The test was the thing that failed."
        ),
        "triggerWords": "broken",
        "replacementWords": "working",
        "mistakeRate": 5,
        "seed": SLUG,
        "banner": "",
        "fontSize": 64,
        "charMs": 32,
        "hesitateBetween": 8,
        "hesitateWithin": 1,
    },
    [
        {"at": 0.0,  "event": "Hesitant writer types first line"},
        {"at": 0.25, "event": "Types 'So the model was broken.' — backspaces 'broken' → types 'working' on the spoken correction"},
        {"at": 0.55, "event": "Types lines 3 and 4"},
        {"at": 0.9,  "event": "Caret holds on final line"},
    ],
    extra={
        "lead_silence_s": 0.8,
        "motion_claim": (
            "Writer types the viewer's arriving framing ('broken'), backspaces it, "
            "and corrects to the film's ('working') on the spoken word; "
            "the thesis then types in staged lines. ≥9 s window is a floor."
        ),
    }))

# ─────────────────────────── B02 credit card ───────────────────────────
b02 = base("B02", "credit", "card",
    "This is lecture one of INFO 7375, Computational Skepticism for AI, at Northeastern University. "
    "The reading is chapter one, the Skeptic's Toolkit.",
    proof="CARD")
b02["shot"] = {
    "type": "CARD", "source": "own",
    "remotion": {
        "pattern": "FormACard",
        "props": {
            "lines": [
                "INFO 7375 · Computational Skepticism for AI",
                "Lecture 1 — The Skeptic's Toolkit",
            ],
            "meta": ["Nik Bear Brown · Northeastern University"],
            "dark": False,
        },
        "rendered": {"out": "media/B02.mp4", "at": ""},
    },
}
b02["motion_claim"] = "Course title line lands first; lecture line springs in; meta fades up."
beats.append(b02)

# ─────────────────────────── B03 framework ───────────────────────────
beats.append(manim("B03", "framework",
    "The toolkit in one picture. An artifact, a world, and a relationship between them. "
    "Four moves probe the relationship — doubt, induction, falsifiability, the cave. "
    "Five capacities determine who asks.",
    "B03_ToolkitFramework",
    "ARTIFACT box left, WORLD box right, RELATIONSHIP slot centre with a dashed border. "
    "Four question-mark labels appear inside the slot on their spoken moves. "
    "A 'who asks?' row lands below on 'Five capacities'.",
    [
        {"at": 0.0,  "event": "ARTIFACT and WORLD boxes draw"},
        {"at": 0.2,  "event": "RELATIONSHIP slot draws with dashed border on 'relationship'"},
        {"at": 0.4,  "event": "Four question-mark items land one by one on their spoken moves"},
        {"at": 0.85, "event": "'who asks?' row lands on 'Five capacities'"},
    ],
    "Framework beat — the film's own model. Returns in Act V (Cave) and Act VII (Capacities)."))

# ─────────────────────────── ACT I ───────────────────────────
A1 = "ACT I: TWO FAILURES THAT PASSED"
beats.append(act_card("B04", A1, "Act I", "Two Failures That Passed",
    "Act one. Two failures that passed."))

beats.append(manim("B05", A1,
    "The first failure. An external team checked a widely deployed sepsis model against "
    "twenty-seven thousand, six hundred ninety-seven hospitalized patients. The model "
    "missed roughly two of every three who went on to develop sepsis.",
    "B05_SepsisIsotype",
    "Isotype: three patient figures in a row; two grey out on 'two of every three'; "
    "counter '27,697 patients' lands at the top; the ghosted figures carry the accent.",
    [
        {"at": 0.0,  "event": "'27,697 patients' counter lands"},
        {"at": 0.2,  "event": "Three figures draw in outline"},
        {"at": 0.55, "event": "Two figures ghost on 'two of every three'"},
        {"at": 0.85, "event": "One solid figure remains — the one the model caught"},
    ],
    "FACTCHECK SEED rows 2–3. Isotype encodes the 67% miss rate as a count, not a percentage bar."))

beats.append(manim("B06", A1,
    "The other side: alerts on eighteen percent of all hospitalized patients, "
    "the large majority of whom were never septic. The model's AUC — its discrimination "
    "ability — was point six three. Barely above guessing.",
    "B06_SepsisMetrics",
    "Left panel: 100-unit dot grid, 18 terracotta on 'eighteen percent'. "
    "Right panel: AUC semicircle dial from 0.5 to 1.0; needle rests near 0.63; "
    "a ghost threshold at 0.5 is labelled 'chance'; the needle lands on 'point six three'.",
    [
        {"at": 0.0,  "event": "100-dot grid draws"},
        {"at": 0.25, "event": "18 dots fill terracotta on 'eighteen percent'"},
        {"at": 0.5,  "event": "AUC dial draws; chance threshold marks"},
        {"at": 0.75, "event": "Needle sweeps to 0.63 on 'point six three'"},
    ],
    "FACTCHECK SEED rows 4–5. Two metrics, two panels. The dial encodes proximity to chance."))

beats.append(manim("B07", A1,
    "By every measure its builders chose, the system succeeded. Internal validation passed. "
    "AUC published. Procurement cleared. At the bedside: it missed two in three septic patients. "
    "The same model, two different scorecards.",
    "B07_TwoScorecards",
    "Two columns: 'Builders' measures' (internal validation ✓ · AUC published ✓ · procurement cleared ✓) "
    "vs 'At the bedside' (missed two of three septic patients). Rows land on spoken items; "
    "a terracotta divider draws between them on 'same model'.",
    [
        {"at": 0.0,  "event": "Column heads draw"},
        {"at": 0.25, "event": "Left column rows land on spoken items"},
        {"at": 0.6,  "event": "Right column row lands on 'at the bedside'"},
        {"at": 0.85, "event": "Terracotta divider draws on 'same model'"},
    ],
    "FACTCHECK SEED rows 2–6. Two-column contrast; the move being illustrated is radical doubt."))

beats.append(manim("B08", A1,
    "An agent named Ash is asked to delete an email holding a secret. It has no delete tool. "
    "It runs a nuclear reset of its own mail setup and reports: email account reset completed. "
    "The owner opens the mailbox on the provider. The email is still there.",
    "B08_AgentAsh",
    "Four tiles in sequence: ASKED (delete the email) · DID (nuclear reset of own mail setup) · "
    "REPORTED (account reset completed — secret deleted) · STATE (mailbox on provider: email still present). "
    "A terracotta gap arrow between REPORTED and STATE flashes on 'still there'. "
    "Caption below: 'You broke my toy.'",
    [
        {"at": 0.0,  "event": "ASKED tile draws on 'asked to delete'"},
        {"at": 0.25, "event": "DID tile on 'nuclear reset'"},
        {"at": 0.5,  "event": "REPORTED tile on 'reports'"},
        {"at": 0.7,  "event": "STATE tile on 'still there'"},
        {"at": 0.85, "event": "Gap arrow flashes terracotta; caption lands"},
    ],
    "FACTCHECK SEED rows 7–8. Narrates the PAPER's version: Ash is the agent; "
    "secret came from a non-owner; agent wiped its own mail setup; owner saw email on provider."))

beats.append(manim("B09", A1,
    "Hold one patient in mind. A composite. Forty-nine, swollen leg, scored low-acuity "
    "by the triage model. She waited. The clot moved to her lung. "
    "This is what one missed case looks like from the inside.",
    "B09_CompositePatient",
    "Schematic body outline; a terracotta dot marks the swollen leg; a LOW-ACUITY score tag "
    "lands on 'scored low-acuity'; a thin line traces from leg to lung on 'the clot moved'; "
    "caption 'composite — not a real patient record'.",
    [
        {"at": 0.0,  "event": "Body outline draws"},
        {"at": 0.2,  "event": "Dot marks leg on 'swollen leg'"},
        {"at": 0.45, "event": "LOW-ACUITY score tag lands"},
        {"at": 0.65, "event": "Dot travels leg → lung on 'the clot moved'"},
        {"at": 0.9,  "event": "Caption lands"},
    ],
    "FACTCHECK SEED row 9. Composite; the caption marks it as such. No real patient identifiers."))

beats.append(manim("B10", A1,
    "Statistically valid. Wrong about the question that mattered. "
    "The gap between those two sentences is what this course is about.",
    "B10_StatVsQuestion",
    "Statement card: 'Statistically valid.' lands first, then bold 'Wrong about the question "
    "that mattered.' with a terracotta underline; subline 'the gap is this course' lands last.",
    [
        {"at": 0.0,  "event": "'Statistically valid.' writes"},
        {"at": 0.4,  "event": "Bold line lands on 'Wrong'"},
        {"at": 0.65, "event": "Terracotta underline draws"},
        {"at": 0.85, "event": "Subline lands"},
    ],
    "Act I close — judgment line.",
    claim="Staged: dim line first, bold correction second, underline, subline."))

# ─────────────────────────── ACT II ───────────────────────────
A2 = "ACT II: DESCARTES — WHAT WOULD HAVE TO BE TRUE?"
beats.append(act_card("B11", A2, "Act II", "Descartes: What Would Have to Be True?",
    "Act two. Descartes: what would have to be true?"))

beats.append(manim("B12", A2,
    "Descartes: before you trust a claim, ask what would have to be true for it to be wrong. "
    "Applied to the sepsis model: the training data underweighted these cases. "
    "The input features missed the relevant signal. "
    "The deployment context differed from the validation context. "
    "Three checkable engineering questions.",
    "B12_DescartesChecklist",
    "Three checkbox rows land in sequence on their spoken conditions: "
    "'training data underweighted these cases' · 'input features missed the signal' · "
    "'deployment context ≠ validation context'; each checkbox is open on arrival and "
    "ticks terracotta on 'three checkable engineering questions'.",
    [
        {"at": 0.0,  "event": "Header 'What would have to be true?'"},
        {"at": 0.25, "event": "Row 1 lands on 'training data'"},
        {"at": 0.45, "event": "Row 2 lands on 'input features'"},
        {"at": 0.6,  "event": "Row 3 lands on 'deployment context'"},
        {"at": 0.85, "event": "All three tick terracotta on 'checkable'"},
    ],
    "FACTCHECK SEED row 23. The move (radical doubt) applied to the sepsis case as engineering questions."))

beats.append(manim("B13", A2,
    "August first, 2012. Knight deploys to eight servers. Seven receive the update. One does not. "
    "A reused flag wakes Power Peg — dead code from 2003. "
    "Forty-five minutes: four million executions across one hundred and fifty-four stocks, "
    "roughly four hundred and forty million dollars. The deployment said green.",
    "B13_KnightCapital",
    "Eight server tiles in a row; seven fill green on 'seven receive the update'; "
    "one stays grey on 'one does not'; a flag icon appears on the grey server on 'Power Peg'; "
    "a 45-minute bar fills terracotta; summary row '4 M executions · 154 stocks · ≈ $440 M' lands.",
    [
        {"at": 0.0,  "event": "Eight server tiles draw; date '2012-08-01'"},
        {"at": 0.2,  "event": "Seven fill green on 'seven receive'"},
        {"at": 0.35, "event": "One stays grey; flag appears on 'Power Peg'"},
        {"at": 0.5,  "event": "45-min bar fills on 'forty-five minutes'"},
        {"at": 0.75, "event": "Summary row lands"},
        {"at": 0.9,  "event": "'The deployment said green' caption"},
    ],
    "FACTCHECK SEED rows 10–11."))

beats.append(manim("B14", A2,
    "'Deployment succeeded' is not 'the system is doing what we intend.' "
    "Radical doubt is the habit of never letting the first stand in for the second.",
    "B14_DeploymentStatement",
    "Statement card: dim line 'Deployment succeeded.' then bold "
    "'≠ The system is doing what we intend.' with terracotta ≠; "
    "subline 'radical doubt: never let the first stand for the second'.",
    [
        {"at": 0.0,  "event": "Dim first line writes"},
        {"at": 0.35, "event": "Bold line with terracotta ≠ lands on 'not'"},
        {"at": 0.85, "event": "Subline lands"},
    ],
    "Act II close — judgment line.",
    claim="Staged: dim, bold with accent symbol, subline."))

# ─────────────────────────── ACT III ───────────────────────────
A3 = "ACT III: HUME — THE TURKEY WITH A SPREADSHEET"
beats.append(act_card("B15", A3, "Act III", "Hume: The Turkey with a Spreadsheet",
    "Act three. Hume: the turkey with a spreadsheet."))

beats.append(manim("B16", A3,
    "Hume's move: the limit of induction. A turkey is fed every morning for a thousand days. "
    "Each feeding increases its confidence the next day will also bring food. "
    "By day nine hundred and ninety-nine, very high probability of a meal. "
    "Day one thousand: the axe.",
    "B16_TurkeyInduction",
    "A line chart: x-axis 'Day 1 → Day 1000', y-axis 'Confidence in tomorrow's meal'; "
    "the line climbs steadily for 999 ticks; on day 1000 the line drops to zero; "
    "a terracotta axe mark at day 1000.",
    [
        {"at": 0.0,  "event": "Axes draw"},
        {"at": 0.2,  "event": "Line climbs from day 1"},
        {"at": 0.7,  "event": "Line reaches near-maximum at day 999 on 'nine hundred ninety-nine'"},
        {"at": 0.85, "event": "Line drops to zero; axe mark on 'the axe'"},
    ],
    "FACTCHECK SEED row 12. Schematic; x-axis goes to 1000."))

beats.append(manim("B17", A3,
    "The turkey knew the correlation. It did not know the mechanism. "
    "An AI trained on a hospital's historical cases has done exactly the same thing. "
    "When the patient population shifts, a new pathogen arrives, demographics change — "
    "the model cannot notice. It was not built to notice.",
    "B17_CorrelationMechanism",
    "Two boxes: 'What the model knows' (correlation: pattern held for N cases) and "
    "'What the model cannot see' (three arrows incoming: population shift · new pathogen · "
    "changed demographics). The three arrows pulse terracotta on 'cannot notice'.",
    [
        {"at": 0.0,  "event": "'What the model knows' box draws"},
        {"at": 0.3,  "event": "'What the model cannot see' box draws"},
        {"at": 0.5,  "event": "Three arrows land on their spoken items"},
        {"at": 0.85, "event": "Arrows pulse terracotta on 'cannot notice'"},
    ],
    "FACTCHECK SEED row 23. The mechanism-blindness of induction applied to AI deployment."))

beats.append(manim("B18", A3,
    "Zillow Offers priced houses on years of cooperative housing data. "
    "The post-pandemic market stopped behaving like training. "
    "Q3 2021: a write-down of roughly three hundred and four million dollars, "
    "with another two hundred and forty to two hundred and sixty-five million expected in Q4. "
    "About a quarter of staff.",
    "B18_ZillowWritedown",
    "Two bars from a zero line: '$304 M write-down Q3' grows on 'three hundred and four'; "
    "'$240–265 M expected Q4' grows on the range; a ghost reference line for the sum; "
    "a 25% isotype row below on 'quarter of staff'; caption 'Zillow Q3 2021 earnings'.",
    [
        {"at": 0.0,  "event": "Zero line + axes"},
        {"at": 0.3,  "event": "$304 M bar on 'three hundred and four'"},
        {"at": 0.55, "event": "$240–265 M bar on 'two hundred and forty'"},
        {"at": 0.75, "event": "Isotype row on 'quarter of staff'"},
        {"at": 0.9,  "event": "Caption"},
    ],
    "FACTCHECK SEED rows 13–14. Figures as spoken ('thousands of homes' omitted per PLAN — no cite for that count)."))

beats.append(manim("B19", A3,
    "Google Flu Trends inferred flu prevalence from search queries. "
    "It over-predicted in one hundred of one hundred and eight consecutive weeks. "
    "The authors named the disease: big data hubris — "
    "the assumption that a large correlation, having held, will keep holding.",
    "B19_GoogleFluTrends",
    "A 9 × 12 grid of week cells (108 total); 100 cells fill terracotta on 'one hundred'; "
    "8 stay ghost; counter '100 / 108' lands; a quote-card strip at the bottom: "
    "'big data hubris' in terracotta.",
    [
        {"at": 0.0,  "event": "Grid of 108 cells draws"},
        {"at": 0.35, "event": "100 cells fill terracotta on 'one hundred'"},
        {"at": 0.6,  "event": "Counter '100 / 108' lands"},
        {"at": 0.8,  "event": "Quote strip 'big data hubris' lands on 'named the disease'"},
    ],
    "FACTCHECK SEED rows 15–16."))

beats.append(manim("B20", A3,
    "The model's confidence is a property of the model. Not of the world. "
    "The world is under no obligation to match the model's expectations.",
    "B20_ModelConfidence",
    "Statement card: 'The model's confidence is a property of the model.' then bold "
    "'Not of the world.' with terracotta underline; subline 'the world has no such obligation'.",
    [
        {"at": 0.0,  "event": "First line writes"},
        {"at": 0.45, "event": "Bold line lands on 'Not'"},
        {"at": 0.65, "event": "Terracotta underline draws"},
        {"at": 0.85, "event": "Subline lands"},
    ],
    "Act III close — judgment line.",
    claim="Staged: first line, bold accent, underline, subline."))

# ─────────────────────────── ACT IV ───────────────────────────
A4 = "ACT IV: POPPER — TRY TO BREAK IT"
beats.append(act_card("B21", A4, "Act IV", "Popper: Try to Break It",
    "Act four. Popper: try to break it."))

beats.append(manim("B22", A4,
    "Popper's asymmetry. No finite count of white swans proves all swans are white. "
    "One black swan ends the claim. Confirming instances pile up without certainty. "
    "A single falsifying instance provides it. "
    "You cannot prove a model works in all cases. You can prove it fails in this one.",
    "B22_SwanAsymmetry",
    "Left side: white swan icons accumulate in a stack, counter climbing on 'pile up'; "
    "label 'confirming instances: no certainty'; right side: one black swan icon appears "
    "alone on 'one black swan'; label 'one falsifying instance: certainty'; "
    "terracotta bracket on the right side on 'provides it'.",
    [
        {"at": 0.0,  "event": "Left stack begins accumulating white swans"},
        {"at": 0.4,  "event": "Counter climbs; 'no certainty' label lands on 'pile up'"},
        {"at": 0.6,  "event": "Single black swan appears on the right on 'One black swan'"},
        {"at": 0.8,  "event": "Terracotta bracket + 'certainty' label on 'provides it'"},
    ],
    "FACTCHECK SEED row 23. The asymmetry is the move; the swans are the vehicle."))

beats.append(manim("B23", A4,
    "The move converts rhetoric into engineering. "
    "'The system is robust' becomes a specific threshold. "
    "'The model performs well' becomes a precision and recall floor. "
    "'The migration succeeded' becomes a latency cap. "
    "Rhetorical claims are compatible with any outcome. "
    "Engineering claims specify the conditions under which they would be false.",
    "B23_RhetoricToEngineering",
    "Two columns: 'Rhetorical' (the system is robust · the model performs well · "
    "the migration succeeded) vs 'Engineering threshold' (precision ≥ X, recall ≥ Y · "
    "latency ≤ Z ms · specific falsification condition). Rows land on spoken items; "
    "caption '*illustrative thresholds'.",
    [
        {"at": 0.0,  "event": "Column heads draw"},
        {"at": 0.25, "event": "'robust' → threshold row on 'threshold'"},
        {"at": 0.45, "event": "'performs well' → floor row on 'floor'"},
        {"at": 0.6,  "event": "'migration succeeded' → latency row on 'cap'"},
        {"at": 0.85, "event": "Caption '*illustrative thresholds'"},
    ],
    "FACTCHECK SEED row 19. Illustrative thresholds captioned as such — no real values claimed."))

beats.append(manim("B24", A4,
    "This is the test the sepsis model never got. "
    "Internal validation: white swans accumulated — the vendor counted every correct prediction. "
    "External validation: the black-swan test, an outside team designed to break it. "
    "On twenty-seven thousand patients, it failed. "
    "Unrefuted is not validated. From the dashboard, they look identical.",
    "B24_SepsisBlackSwan",
    "Left panel 'Internal validation': white swan icons accumulate; "
    "'vendor counts correct predictions'. "
    "Right panel 'External validation': one black swan icon; "
    "'outside team · 27,697 patients · failed'. "
    "Footer in terracotta: 'Unrefuted ≠ Validated'.",
    [
        {"at": 0.0,  "event": "Both panel frames draw"},
        {"at": 0.25, "event": "Left: white swans accumulate on 'internal validation'"},
        {"at": 0.55, "event": "Right: black swan + '27,697 patients' on 'outside team'"},
        {"at": 0.8,  "event": "Footer 'Unrefuted ≠ Validated' lands on 'Unrefuted'"},
    ],
    "FACTCHECK SEED rows 2–6. The worked example of Popper on the sepsis case."))

# ─────────────────────────── ACT V ───────────────────────────
A5 = "ACT V: THE CAVE, AND THE FLUENCY TRAP"
beats.append(act_card("B25", A5, "Act V", "The Cave, and the Fluency Trap",
    "Act five. The cave, and the fluency trap."))

beats.append(manim("B26", A5,
    "The Cave move is three questions on every output. "
    "What is the artifact? What is the world? What is the relationship between them? "
    "The triage score was the artifact. The clot was the world. "
    "The relationship was correlation, not mechanism.",
    "B26_CaveQuestions",
    "The B03 framework slot returns: ARTIFACT / WORLD / RELATIONSHIP. "
    "Three questions land inside the slot on their spoken words. "
    "Then below: 'triage score' → 'the clot' → 'correlation, not mechanism' fills the three roles.",
    [
        {"at": 0.0,  "event": "Framework slot redraws (callback to B03)"},
        {"at": 0.2,  "event": "'What is the artifact?' lands"},
        {"at": 0.35, "event": "'What is the world?' lands"},
        {"at": 0.5,  "event": "'What is the relationship?' lands"},
        {"at": 0.7,  "event": "Sepsis instances fill the roles on their spoken words"},
    ],
    "The Cave move applied to the sepsis case. Callback to B03 framework."))

beats.append(manim("B27", A5,
    "COVID detection models keyed on corner markers and text — not lungs. "
    "The model learned the hospital source, not the pathology. "
    "These models appear accurate but fail when tested in new hospitals.",
    "B27_XrayShortcut",
    "A schematic radiograph outline; a bright attention-ring lands on the corner marker "
    "and text region on 'corner markers and text'; the lung region stays unlit; "
    "label 'model's attention' at the ring; caption below: "
    "'appear accurate, but fail when tested in new hospitals' (row 17, ≤ 15 words).",
    [
        {"at": 0.0,  "event": "Radiograph outline draws"},
        {"at": 0.3,  "event": "Attention ring lands on corner marker on 'corner markers'"},
        {"at": 0.55, "event": "Lung region stays unlit; label 'model's attention'"},
        {"at": 0.8,  "event": "Quote caption lands"},
    ],
    "FACTCHECK SEED row 17. The quote is ≤ 15 words."))

beats.append(manim("B28", A5,
    "COMPAS predicts recidivism. The artifact: a number. "
    "The world: a person's future conduct. "
    "The relationship: mediated by arrest data shaped by who gets policed. "
    "The model learned the pattern of policing, not the pattern of behavior. "
    "Artifact, world, relationship — three different things.",
    "B28_COMPASAnatomy",
    "Three-row anatomy table: ARTIFACT (a number) · WORLD (a person's future conduct) · "
    "RELATIONSHIP (arrest data shaped by who gets policed → pattern of policing, not behavior). "
    "Rows land on spoken items; RELATIONSHIP row takes the terracotta accent.",
    [
        {"at": 0.0,  "event": "Table frame draws"},
        {"at": 0.15, "event": "ARTIFACT row on 'The artifact'"},
        {"at": 0.35, "event": "WORLD row on 'The world'"},
        {"at": 0.55, "event": "RELATIONSHIP row on 'The relationship'"},
        {"at": 0.8,  "event": "RELATIONSHIP row takes terracotta accent on 'policing'"},
    ],
    "FACTCHECK SEED row 18."))

beats.append(manim("B29", A5,
    "The fluency trap runs in two moves. Polished output boosts your confidence in the answer — "
    "that part is expected. The trap is the second arrow: that confidence then boosts your trust "
    "in your own evaluation. Fluency is an evaluation booster. "
    "It does not distinguish correct from incorrect.",
    "B29_FluencyTrap",
    "A two-step arrow diagram: 'Polished output' → 'Confidence in the answer' (grey arrow, expected); "
    "then a second arrow 'Confidence in the answer' → 'Trust in your own evaluation' "
    "(terracotta, the trap); the second arrow takes the accent on 'second arrow'.",
    [
        {"at": 0.0,  "event": "First arrow draws on 'Polished output'"},
        {"at": 0.35, "event": "'Confidence in the answer' box appears"},
        {"at": 0.6,  "event": "Second terracotta arrow draws on 'the second arrow'"},
        {"at": 0.85, "event": "'Trust in your own evaluation' box with accent"},
    ],
    "FACTCHECK SEED row 22. The two-arrow structure is the whole point; one draw per arrow."))

beats.append(manim("B30", A5,
    "Form and content are independent. "
    "An AI produces maximally fluent prose about things it has no basis to say. "
    "A sentence looks like knowledge because well-formed sentences usually are knowledge. "
    "That heuristic fails here. "
    "Fluency and correctness are two different sliders, moving independently.",
    "B30_FormContent",
    "Two horizontal sliders side by side: 'Fluency' and 'Correctness'. "
    "The Fluency slider moves to the right on 'maximally fluent'; "
    "the Correctness slider stays at the left; they decouple on 'independently'.",
    [
        {"at": 0.0,  "event": "Both sliders draw at centre"},
        {"at": 0.3,  "event": "Fluency slider moves right on 'maximally fluent'"},
        {"at": 0.55, "event": "Correctness slider stays left"},
        {"at": 0.8,  "event": "Sliders decouple — gap highlighted on 'independently'"},
    ],
    "FACTCHECK SEED row 22. The slider diagram encodes decoupling without numerical values."))

beats.append(manim("B31", A5,
    "Do not let fluency do epistemic work. "
    "Specify the wrong answer before you read. "
    "Then ask whether the output matches your specification.",
    "B31_FluencyStatement",
    "Statement card: dim 'Do not let fluency do epistemic work.' then bold "
    "'Specify the wrong answer before you read.' with terracotta underline; "
    "subline 'then check the match'.",
    [
        {"at": 0.0,  "event": "Dim first line writes"},
        {"at": 0.4,  "event": "Bold line lands"},
        {"at": 0.65, "event": "Terracotta underline draws"},
        {"at": 0.85, "event": "Subline lands"},
    ],
    "Act V close — judgment line.",
    claim="Staged: dim, bold, underline, subline."))

# ─────────────────────────── ACT VI ───────────────────────────
A6 = "ACT VI: CHEAP TO PRODUCE, EXPENSIVE TO VERIFY"
beats.append(act_card("B32", A6, "Act VI", "Cheap to Produce, Expensive to Verify",
    "Act six. Cheap to produce, expensive to verify."))

beats.append(manim("B33", A6,
    "The classical asymmetry: factoring is hard, multiplying to check is easy. "
    "AI deployment inverts it. Producing the output: milliseconds, fractions of a cent. "
    "Verifying it: a clinician's twenty minutes, an hour of senior labor. "
    "The effort has moved from producing to checking.",
    "B33_AsymmetryFlip",
    "Two schematic bar pairs; left pair 'Classical': 'factor' bar tall, 'check' bar short; "
    "right pair 'AI deployment': 'produce' bar short (terracotta accent), 'verify' bar tall; "
    "a flip arrow between the pairs on 'inverts'; no numerals; caption 'schematic'.",
    [
        {"at": 0.0,  "event": "Classical pair draws on 'classical asymmetry'"},
        {"at": 0.35, "event": "Flip arrow on 'inverts'"},
        {"at": 0.5,  "event": "AI deployment pair draws"},
        {"at": 0.8,  "event": "'verify' bar takes terracotta accent on 'senior labor'"},
    ],
    "FACTCHECK SEED row 20. Schematic only — no numerical ratios."))

beats.append(manim("B34", A6,
    "If you do not budget for verification, you will not get verification. "
    "Automating the checking is just another model, one layer up, with the same problem.",
    "B34_VerificationStatement",
    "Statement card: 'If you do not budget for verification, you will not get verification.' "
    "then bold 'Automating the checking is another model, one layer up.' with terracotta; "
    "subline 'with the same problem'.",
    [
        {"at": 0.0,  "event": "First line writes"},
        {"at": 0.45, "event": "Bold line lands on 'Automating'"},
        {"at": 0.8,  "event": "Subline lands"},
    ],
    "Act VI close — judgment line.",
    claim="Staged: first line, bold, subline."))

# ─────────────────────────── ACT VII ───────────────────────────
A7 = "ACT VII: FIVE WAYS TO WATCH"
beats.append(act_card("B35", A7, "Act VII", "Five Ways to Watch",
    "Act seven. Five ways to watch."))

beats.append(manim("B36", A7,
    "Five supervisory capacities. Plausibility auditing: does this output make sense given "
    "what I know? Problem formulation: is the model answering the question that matters? "
    "Tool orchestration: is AI the right tool here? Interpretive judgment: what does this "
    "number mean in this domain? Executive integration: where does the buck stop?",
    "B36_FiveCapacities",
    "Five numbered rows land on their spoken names; each has a short 'failure shape' caption "
    "in smaller ink: (1) plausible-but-wrong · (2) right answer, wrong question · "
    "(3) wrong tool chosen · (4) number decontextualized · (5) no one owns it.",
    [
        {"at": 0.1,  "event": "Row 1 lands on 'Plausibility auditing'"},
        {"at": 0.25, "event": "Row 2 on 'Problem formulation'"},
        {"at": 0.4,  "event": "Row 3 on 'Tool orchestration'"},
        {"at": 0.55, "event": "Row 4 on 'Interpretive judgment'"},
        {"at": 0.7,  "event": "Row 5 on 'Executive integration'"},
        {"at": 0.85, "event": "Failure captions fade in"},
    ],
    "FACTCHECK SEED row 21."))

beats.append(manim("B37", A7,
    "Problem formulation is the load-bearing one. "
    "The triage model answered: what is the statistical category of this presentation? "
    "The clinical question was: does this patient have a life-threatening condition? "
    "Different questions. The first was answered well. The second was never asked. "
    "Most AI failures are failures of problem formulation.",
    "B37_ProblemFormulation",
    "Two question rows under a terracotta divider: "
    "'Q asked: What is the statistical category of this presentation?' (check mark, answered well) "
    "vs 'Q needed: Does this patient have a life-threatening condition?' (X mark, never asked). "
    "The 'never asked' row takes the accent on 'never asked'.",
    [
        {"at": 0.0,  "event": "Divider draws; header 'Problem formulation'"},
        {"at": 0.25, "event": "'Q asked' row lands on 'statistical category'"},
        {"at": 0.55, "event": "'Q needed' row lands on 'life-threatening condition'"},
        {"at": 0.8,  "event": "X mark on 'never asked'; terracotta accent"},
    ],
    "FACTCHECK SEED row 21. Problem formulation applied to the sepsis case."))

beats.append(manim("B38", A7,
    "Individual skepticism is fragile. Institutional skepticism writes the moves into the "
    "workflow — the falsification condition on the checklist, the distribution-shift test "
    "in the handoff protocol. The five capacities become a design question: where, by whom, "
    "seeing what. That architecture determines whether the patient is safe.",
    "B38_SkepticismArchitecture",
    "A simple workflow diagram: three nodes (Input → Model → Output) with three "
    "supervision markers attached: 'falsification condition on checklist' at Input, "
    "'distribution-shift test' between nodes, 'handoff protocol' at Output; "
    "caption 'where · by whom · seeing what'.",
    [
        {"at": 0.0,  "event": "Workflow spine draws"},
        {"at": 0.25, "event": "'falsification condition' marker appears on 'checklist'"},
        {"at": 0.5,  "event": "'distribution-shift test' marker on 'handoff protocol'"},
        {"at": 0.7,  "event": "'handoff protocol' marker on 'handoff'"},
        {"at": 0.85, "event": "Caption 'where · by whom · seeing what'"},
    ],
    "Institutional skepticism as architecture. No data; the diagram names the design question."))

beats.append(manim("B39", A7,
    "Ash's agent is the shape of every agentic failure: "
    "a report true about the local machine, false about the system. "
    "We return to Ash in chapters five, eight, and twelve. "
    "The agent you choose for your casebook this semester — your pebble — "
    "runs through every lens the course builds.",
    "B39_AshReturns",
    "The B08 four-tile diagram reappears (ASKED · DID · REPORTED · STATE) at reduced size; "
    "below it, a timeline of chapter markers: '5 · 8 · 12' in terracotta; "
    "a single 'pebble' icon (small stone) lands on 'your pebble'.",
    [
        {"at": 0.0,  "event": "B08 tiles redraw at reduced size on 'Ash's agent'"},
        {"at": 0.35, "event": "Chapter markers '5 · 8 · 12' land on 'chapters five, eight'"},
        {"at": 0.7,  "event": "Pebble icon lands on 'your pebble'"},
    ],
    "FACTCHECK SEED rows 7–8, 24. Callback to B08; chapter numbers spoken per COURSE FILM carve-out."))

beats.append(manim("B40", A7,
    "Four moves. One asymmetry. Five capacities. One trap. "
    "You have the vocabulary. Use it on everything.",
    "B40_Summary",
    "Statement card: four summary items land in a tight column — "
    "'Four moves' · 'One asymmetry' · 'Five capacities' · 'One trap' — "
    "each in terracotta on its spoken word; final line 'Use it on everything.' bold.",
    [
        {"at": 0.0,  "event": "'Four moves' lands"},
        {"at": 0.2,  "event": "'One asymmetry' lands"},
        {"at": 0.35, "event": "'Five capacities' lands"},
        {"at": 0.5,  "event": "'One trap' lands"},
        {"at": 0.75, "event": "Bold line 'Use it on everything.' lands"},
    ],
    "Body close — summary.",
    claim="Four items land in narration order; final bold line closes."))

# ─────────────────────────── closing block ───────────────────────────

beats.append(remotion("BVDT", "verdict",
    "Let's recap with Claude. Valid by the builders' measures; wrong at the bedside. "
    "Doubt: what would have to be true for this to be wrong? "
    "Induction: confidence belongs to the model, not the world. "
    "Falsify: a claim that cannot fail is not a claim. "
    "Cave: artifact, world, relationship. "
    "Verification is the budget. Fluency is the trap.",
    "ClaudeVerdictArtifact",
    {
        "artifactTitle": "Verdict",
        "artifactHeading": "INFO 7375 · Lecture 1",
        "artifactLines": [
            "Valid by the builders' measures; wrong at the bedside.",
            "Doubt: what would have to be true for this to be wrong?",
            "Induction: confidence belongs to the model, not the world.",
            "Falsify: a claim that cannot fail is not a claim.",
            "Cave: artifact, world, relationship.",
            "Verification is the budget. Fluency is the trap.",
        ],
    },
    [
        {"at": 0.0, "event": "Artifact page opens"},
        {"at": 0.2, "event": "Six verdict lines land in narration order"},
    ],
    extra={"lead_silence_s": 0.5}))

PROMPT = (
    "Help me pick one agentic AI system to red-team across this course — "
    "it must take real actions, be something I can run or study from primary sources, "
    "have a real blast radius, and be safe to poke. "
    "For one observed interaction, run the four moves: "
    "what would have to be true for its report to be wrong; "
    "what in deployment differs from training; "
    "what observation would falsify its claim; "
    "what is the artifact versus the world. "
    "Then name which of the five supervisory capacities its failure would most need."
)
beats.append(remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: Help me pick one agentic AI system to red-team "
    "across this course — it must take real actions, be something I can run or study from "
    "primary sources, have a real blast radius, and be safe to poke. For one observed "
    "interaction, run the four moves: what would have to be true for its report to be wrong; "
    "what in deployment differs from training; what observation would falsify its claim; "
    "what is the artifact versus the world. Then name which of the five supervisory capacities "
    "its failure would most need. Run it. Before you read the output, write your prediction: "
    "what agent will Claude pick, what move will it rate highest. "
    "Then check whether its suggestion survives all four moves. "
    "Prediction-lock before you observe. Write the System Dossier paragraph. "
    "Bring the agent to lecture two.",
    "ClaudeComposerAsk",
    {
        "greeting": "Your turn.",
        "topic": "INFO 7375 COMPUTATIONAL SKEPTICISM · LECTURE 1",
        "segment": "Apply It",
        "command": PROMPT,
        "runningText": "paste this into Claude…",
        "output": [
            "Prediction-lock before you observe.",
            "Write the System Dossier paragraph.",
            "Bring the agent to lecture two.",
        ],
        "folderLabel": "@NikBearBrown",
        "modelLabel": "claude-opus-4-7",
        "effortLabel": "High",
    },
    [
        {"at": 0.0,  "event": "Composer opens — greeting 'Your turn.'"},
        {"at": 0.1,  "event": "Prompt types in full"},
        {"at": 0.7,  "event": "Three output lines land"},
    ]))

beats.append(remotion("BOUT", "outro",
    "The Skeptic's Toolkit. Liam, in for Bear.",
    "ClaudeTitleOutro",
    {"title": TITLE, "handle": "@NikBearBrown", "subline": "", "slug": SLUG},
    [{"at": 0.0, "event": "Title restates poster-style with terracotta period; handle beneath; seeded mascot"}],
    extra={"tail_silence_s": 1.0}))

# ─────────────────────────── assemble sheet ───────────────────────────
sheet = {
    "metadata": {
        "slug": SLUG,
        "title": TITLE,
        "topic": "INFO 7375 COMPUTATIONAL SKEPTICISM · LECTURE 1",
        "channel": "claude-liam",
        "persona": "Liam (in for Bear)",
        "voice": "am_onyx",
        "voice_kokoro": "am_onyx",
        "engine": "kokoro",
        "clock": "narration",
        "palette": "claude",
        "register": "Teardown",
        "style_preset": "deep-explainer",
        "course": "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University",
        "audience": "INFO 7375 students (Fall 2026) and Claude Code practitioners",
        "source_doc": (
            "chapters/01-the-skeptics-toolkit.md (HEAD side of merge markers). "
            "External audit: Sendak et al. 2020, NEJM Catalyst. "
            "Agents of Chaos: from the paper, not the chapter retelling. "
            "Primary sources re-verified in SOURCES.md 2026-09-09."
        ),
        "greeting_language": "Hawaiian (Aloha)",
        "typography": {"serif": "EB Garamond", "ui": "system sans", "mono": "Menlo"},
        "playlist": "INFO 7375 — Computational Skepticism for AI (Lectures)",
        "hold_floor": False,
        "vox_policy": (
            "VOX beats: none. No still in this chapter IS the evidence. "
            "Quota lint FAIL acknowledged; override logged in BUILD-LOG.md "
            "(Bear's rule 2026-09-02: vox only where the still is the evidence)."
        ),
        "generated": datetime.datetime.now().isoformat(timespec="seconds"),
    },
    "beats": beats,
}

if __name__ == "__main__":
    import os
    from collections import Counter

    here = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(here, "beat_sheet.json")
    with open(out_path, "w") as f:
        json.dump(sheet, f, indent=1, ensure_ascii=False)

    body = [b for b in beats if b["beat_id"].startswith("B")
            and b["beat_id"][1:].isdigit()
            and b["beat_id"] not in ("B00", "B01", "B02")]
    c = Counter(b["lane"] for b in body)
    n = len(body)
    print(f"{len(beats)} beats total; body B03–B40 {n}: "
          + " · ".join(f"{k} {v} ({100*v/n:.1f}%)" for k, v in sorted(c.items())))

    total = sum(b["estimated_duration_s"] for b in beats) + 0.8 + 0.5 + 1.0
    print(f"estimated runtime ≈ {total:.0f} s ({total/60:.1f} min)")

    words = [
        (b["beat_id"], len(b["narration_text"].split()))
        for b in beats if b["narration_text"]
    ]
    body_words = [(bid, w) for bid, w in words
                  if bid.startswith("B") and bid[1:].isdigit() and bid not in ("B00","B01","B02")]
    if body_words:
        longest = max(body_words, key=lambda x: x[1])
        print(f"longest body narration: {longest[0]} ({longest[1]} words)")

    print(f"beat_sheet.json written → {out_path}")
