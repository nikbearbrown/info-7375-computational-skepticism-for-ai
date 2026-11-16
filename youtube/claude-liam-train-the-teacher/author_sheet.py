#!/usr/bin/env python3
"""
author_sheet.py — claude-liam-train-the-teacher

Writes beat_sheet.json for the deep-explainer on Nik Bear Brown's May 16 2026
skepticism.ai essay "Not the App. Not the Ban. Train the Teacher." AND on the
adversarial evidence audit commissioned against it (September 7 2026).

The film's subject is the pair. The essay makes a claim; the audit rules on it
piece by piece; the film reports what survived and what did not.

VOX LAW: zero vox beats. The evidence in this story is statutes, cost tables and
effect sizes — text and numbers. A pantry still would be texture, so there is no
pantry and no shopping list. Every beat renders.

SOURCE CARE: where the essay and the audit disagree, the AUDIT governs and the
film says so on screen. No number is hardcoded in a component; every figure
below travels as a prop, so a corrected figure is a one-line fix here.
"""
import json
import os

SLUG = "claude-liam-train-the-teacher"
TITLE = "Train the Teacher"
TOPIC = "EDUCATION AND AI · AUDITED"
VOICE = "am_onyx"

WPS = 2.9  # planning estimate only — measured mp3 durations are the clock


def est(text: str) -> float:
    return round(len(text.split()) / WPS + 0.9, 1)


beats = []


def B(bid, act, lane, narration, element, shot, show, motion_note=None):
    beats.append({
        "beat_id": bid,
        "act": act,
        "lane": lane,
        "narration_text": narration,
        "estimated_duration_s": est(narration),
        "voice": VOICE,
        "engine": "kokoro",
        "voice_kokoro": VOICE,
        "new_visual_element": element,
        "shot": shot,
        "show": show,
    })


def remotion(component, props, motion="hold", stype="REMOTION"):
    return {
        "type": stype,
        "source": "own",
        "motion": motion,
        "remotion": {
            "pattern": component,
            "component": component,
            "props": props,
            "rendered": {"out": "", "at": ""},
        },
    }


def card(title, index):
    return remotion("ReqSegmentCard", {"title": title, "index": index}, motion="hold")


# ===========================================================================
# BOOKENDS — COLD OPEN + OVERVIEW
# ===========================================================================

B("B00", "COLD OPEN", "BOOKEND",
  "Namaste — this is Liam, in for Bear. In May, Bear published an argument about phones, "
  "school technology, and where the money should actually go. Then he did something most "
  "people who publish an argument never do. He had it attacked. Not reviewed. "
  "Attacked — under instructions to fix or kill every number in it. This film is what came back.",
  "ClaudeComposerAsk — the ask, answered",
  remotion("ClaudeComposerAsk", {
      "greeting": "Namaste, Liam",
      "command": "Here is an argument I published. Run an adversarial evidence audit on it. Do not support it — try to break it.",
      "segment": TITLE,
      "topic": TOPIC,
      "runningText": "auditing seven sub-claims…",
      "output": [
          "The recommendation survives.",
          "Four of its sentences do not.",
          "And one whole act of the case is missing.",
      ],
      "folderLabel": "@NikBearBrown",
      "modelLabel": "Opus 5",
      "effortLabel": "High",
  }, motion="type"),
  [{"at": 0.0, "event": "Composer types the ask"},
   {"at": 0.60, "event": "Send arms terracotta"},
   {"at": 0.74, "event": "Three output lines land in sequence"}]),

B("B01", "THE OVERVIEW", "BOOKEND",
  "Here is the whole film in one breath. The essay says the binding constraint on technology "
  "in schools is teacher capability — not the device policy, not the platform. The audit says "
  "that recommendation is defensible. It also says four of the sentences carrying it are wrong, "
  "and the study that would actually prove it has not been run by anyone.",
  "BrutalistHesitantWriter — the overview, corrected on screen",
  remotion("BrutalistHesitantWriter", {
      "text": "This is a film about an essay that was right.\nIt is about how much of the evidence\nfor being right was actually there.",
      "triggerWords": "an essay that was right",
      "replacementWords": "an argument that survived its own audit",
      "face": "serif",
      "fontSize": 58,
      "lineSpacing": 1.32,
      "align": "center",
      "charMs": 42,
      "mistakeRate": 7,
      "seed": SLUG,
  }, motion="type"),
  [{"at": 0.0, "event": "Caret blinks on cream"},
   {"at": 0.22, "event": "'an essay that was right' types out"},
   {"at": 0.54, "event": "The clause turns terracotta and deletes"},
   {"at": 0.66, "event": "'an argument that survived its own audit' types in"},
   {"at": 0.88, "event": "Full line holds"}]),

# ===========================================================================
# ACT I — TWO ANSWERS, ONE QUESTION
# ===========================================================================
A1 = "ACT I — TWO ANSWERS, ONE QUESTION"

B("B02", A1, "CARD",
  "Start with the argument as published, because the audit only means something if you take "
  "the argument seriously first.",
  "ReqSegmentCard — Act I",
  card("Two Answers, One Question", "I"),
  [{"at": 0.0, "event": "Eyebrow ACT · I"},
   {"at": 0.35, "event": "Serif title, terracotta period"},
   {"at": 0.62, "event": "Hairline rule draws"}]),

B("B03", A1, "REMOTION",
  "The policy debate offered two answers to one question. Technology is harming students — what "
  "do we do? Answer one: ban the phone. Answer two: buy a better platform. Both answers arrive "
  "with force. Neither of them reaches the classroom, because neither of them is about the "
  "person standing in it.",
  "TtTwoAnswers — both answers drive in and stop short",
  remotion("TtTwoAnswers", {
      "question": "Technology is harming students. What do we do?",
      "left": {"name": "Ban the phone.", "sub": "Remove the device. Restore the room."},
      "right": {"name": "Buy the platform.", "sub": "Adaptive software. The right tutor. Trust the algorithm."},
      "gapLabel": "neither answer is about the teacher",
      "note": "The essay's opening move: both answers address the equipment.",
      "spark": "One question. Two misses.",
  }, motion="drawon"),
  [{"at": 0.10, "event": "The question lands centre"},
   {"at": 0.28, "event": "Both answer cards drive inward"},
   {"at": 0.50, "event": "Both arrest short of centre — the gap holds"},
   {"at": 0.66, "event": "Terracotta bracket closes on the empty middle"}]),

B("B04", A1, "REMOTION",
  "The best causal evidence on bans comes from one large Florida district. And it found something "
  "uncomfortable. The disciplinary cost lands in year one. The academic benefit shows up in year "
  "two. For a student suspended out of a critical semester, later is not the same as yes.",
  "TtFrontLoaded — the cost track rises a year before the benefit track",
  remotion("TtFrontLoaded", {
      "title": "The cost and the benefit are not on the same clock.",
      "spanLabels": ["YEAR ONE", "YEAR TWO"],
      "costLabel": "disciplinary cost",
      "benefitLabel": "academic benefit",
      "bandLabel": "paid here — collected a year later",
      "note": "Figlio & Özek — one Florida district. The timing is the finding.",
      "spark": "Front-loaded.",
  }, motion="drawon"),
  [{"at": 0.18, "event": "Cost line climbs across year one, then holds"},
   {"at": 0.45, "event": "Benefit line sits flat — visibly doing nothing"},
   {"at": 0.56, "event": "Benefit line rises in year two"},
   {"at": 0.66, "event": "Terracotta band fills the interval where cost exists alone"}]),

B("B05", A1, "REMOTION",
  "Then the essay finds a blank. Phone-ban statutes carve out an exemption for educational "
  "purposes. The teacher is handed the judgement — in the moment, at nine in the morning, with a "
  "room watching. The essay's charge is that the laws hand over the decision without handing over "
  "the definition.",
  "ReqDefinitionDrop — the exemption with its centre missing",
  remotion("ReqDefinitionDrop", {
      "title": "What the exemption says",
      "parts": [
          "an exemption exists for educational purposes",
          "the teacher decides, live, case by case",
          "the decision is enforceable",
      ],
      "missing": "what 'educational purposes' means",
      "missingLabel": "the load-bearing blank",
      "note": "The essay's sharpest move. Act II narrows it.",
      "spark": "A decision without a definition.",
  }, motion="drawon"),
  [{"at": 0.14, "event": "The three given parts land in sequence"},
   {"at": 0.52, "event": "The gap is left visibly open"},
   {"at": 0.68, "event": "The missing term drops into it in terracotta"}]),

B("B06", A1, "REMOTION",
  "So the essay asks for three things. Supervised technology time that replaces what the ban "
  "removed. A definition written before the rule is enforced. And sustained, subject-specific "
  "training for teachers in how AI changes what teaching requires. That is the claim. Now watch "
  "it get taken apart.",
  "ReqLevers — the three asks, standing before the audit",
  remotion("ReqLevers", {
      "title": "The essay's three asks",
      "levers": [
          {"name": "Access", "sub": "supervised, teacher-led technology time — scaled to what the ban removed"},
          {"name": "Definition", "sub": "write what 'educational' means before enforcing what it excludes"},
          {"name": "Training", "sub": "sustained, subject-specific professional learning in AI"},
      ],
      "blocked": [],
      "blockedLabel": "",
      "note": "Three asks. The audit rules on each of them separately.",
      "spark": "The argument, standing.",
  }, motion="drawon"),
  [{"at": 0.12, "event": "Title lands"},
   {"at": 0.30, "event": "Three columns rise on a stagger, terracotta top rules"},
   {"at": 0.64, "event": "Each subtitle types beneath its column"}]),

# ===========================================================================
# ACT II — THEN SOMEBODY AUDITED IT
# ===========================================================================
A2 = "ACT II — THEN SOMEBODY AUDITED IT"

B("B07", A2, "CARD",
  "The audit did not argue with the conclusion. It went after the sentences.",
  "ReqSegmentCard — Act II",
  card("Then Somebody Audited It", "II"),
  [{"at": 0.0, "event": "Eyebrow ACT · II"},
   {"at": 0.35, "event": "Serif title, terracotta period"},
   {"at": 0.62, "event": "Hairline rule draws"}]),

B("B08", A2, "REMOTION",
  "First it refused to rule on the argument as a whole. It cut the claim into seven pieces and "
  "ruled on each one separately — because an argument that is sixty percent right is not sixty "
  "percent true. It has a specific list of parts that hold and a specific list that do not.",
  "TtVerdictGrid — the claim decomposed, each row stamped",
  remotion("TtVerdictGrid", {
      "title": "The claim, decomposed",
      "rows": [
          {"key": "A", "claim": "Ban costs are front-loaded and unevenly distributed", "verdict": "SUPPORTED, NARROWER", "accent": False},
          {"key": "B", "claim": "Teacher support makes or breaks EdTech", "verdict": "SUPPORTED", "accent": False},
          {"key": "C", "claim": "Districts overspend on hardware versus training", "verdict": "UNVERIFIED TODAY", "accent": False},
          {"key": "D", "claim": "Most teachers lack the skills to use AI", "verdict": "SUPPORTED, SELF-REPORT", "accent": False},
          {"key": "E", "claim": "Sustained AI training is affordable inside current budgets", "verdict": "UNCOSTED", "accent": False},
          {"key": "F", "claim": "The continuing-medical-education analogy holds", "verdict": "CUTS BOTH WAYS", "accent": False},
          {"key": "G", "claim": "AI-specific teacher training improves student learning", "verdict": "NO EVIDENCE", "accent": True},
      ],
      "note": "Seven pieces, seven verdicts. The last one is the one that matters.",
      "spark": "Rule on the parts, not the mood.",
  }, motion="drawon"),
  [{"at": 0.10, "event": "Rows land top to bottom on a stagger"},
   {"at": 0.35, "event": "Each verdict stamps in behind its row"},
   {"at": 0.80, "event": "Row G holds in terracotta"}]),

B("B09", A2, "REMOTION",
  "Start with the number the essay opened on. Suspensions up thirty percent for Black boys. The "
  "authors' own account says something narrower. In-school suspensions, for Black students. And "
  "for out-of-school suspensions — the ones that remove a child from the building — no "
  "significant effect at all.",
  "TtCorrection — the opening statistic, struck and restated",
  remotion("TtCorrection", {
      "sourceLabel": "AS PUBLISHED",
      "before": "In the first year of the ban, suspensions increased 30 percent for ",
      "wrong": "Black boys",
      "after": ".",
      "corrected": "About 30 percent — for IN-SCHOOL suspensions, among Black students. No significant effect on out-of-school suspensions.",
      "verdict": "CORRECTED",
      "citation": "Figlio & Özek, authors' own May 2026 account",
      "note": "Narrower subgroup. Narrower outcome. The disparity is still real.",
      "spark": "The sharpest number in the piece.",
  }, motion="drawon"),
  [{"at": 0.14, "event": "The published sentence holds on the page"},
   {"at": 0.36, "event": "Terracotta rule sweeps through 'Black boys'"},
   {"at": 0.50, "event": "The struck span greys out"},
   {"at": 0.60, "event": "The correction card drops in beneath"}]),

B("B10", A2, "REMOTION",
  "The scope shrank too. This is one large Florida district, comparing schools that used phones "
  "more against schools that used them less. Not a statewide evaluation. The overall academic "
  "difference is about one percentile point — and it was not significant for girls, or for "
  "elementary students. So all groups benefited is not what the study says.",
  "ReqLedger — the study's real scope, line by line",
  remotion("ReqLedger", {
      "title": "What the study actually covers",
      "rows": [
          {"tier": "SETTING", "label": "One large Florida district", "verdict": "not the state", "accent": False},
          {"tier": "DESIGN", "label": "Schools with more pre-ban phone use vs. less", "verdict": "quasi-experimental", "accent": False},
          {"tier": "SIZE", "label": "About 1.1 percentile points overall", "verdict": "small", "accent": False},
          {"tier": "SUBGROUP", "label": "Female students · elementary students", "verdict": "not significant", "accent": True},
          {"tier": "UNVERIFIED", "label": "The 3.5 million observation count", "verdict": "could not confirm", "accent": True},
      ],
      "note": "Still worth doing. Just not what the sentence claimed.",
      "spark": "Read the scope, not the headline.",
  }, motion="drawon"),
  [{"at": 0.12, "event": "Rows land in sequence"},
   {"at": 0.55, "event": "The two terracotta rows resolve last"},
   {"at": 0.84, "event": "Note fades up"}]),

B("B11", A2, "REMOTION",
  "Next, the study the essay used as its clincher. Free software, forty-six dollars a student, "
  "all of it teacher training, and it moved state maths scores. The audit read the cost report. "
  "The forty-six dollars covers platform maintenance and implementation support as well. The "
  "intervention was a package, and you cannot pull the training out of it.",
  "TtCorrection — the clincher, restated as a package",
  remotion("TtCorrection", {
      "sourceLabel": "AS PUBLISHED",
      "before": "The only implementation cost was $46 per student — ",
      "wrong": "entirely in teacher professional development",
      "after": ". The platform didn't do it. The training did.",
      "corrected": "$46.23 per student, 2021 dollars — including platform maintenance and implementation support. 63 schools; a 0.10 SD later gain in 8th-grade maths.",
      "verdict": "CORRECTED — PACKAGE, NOT COMPONENT",
      "citation": "Feng, Weiser & Collins, WestEd cost analysis, 2024",
      "note": "A price of zero does not make the software causally irrelevant.",
      "spark": "The clincher, re-read.",
  }, motion="drawon"),
  [{"at": 0.14, "event": "The published claim holds"},
   {"at": 0.36, "event": "Strike sweeps 'entirely in teacher professional development'"},
   {"at": 0.58, "event": "The costed correction drops in"},
   {"at": 0.72, "event": "Citation stamps"}]),

B("B12", A2, "REMOTION",
  "Then the equity statistic. More than half of students without home Wi-Fi get online by phone. "
  "Pull the camera back and look at the denominator. Out of a hundred children, four are "
  "smartphone-only and three have nothing. The fraction is real. But it is a fraction of seven, "
  "not a fraction of the student body.",
  "TtDenominator — the headline pulls back to reveal its denominator",
  remotion("TtDenominator", {
      "headline": "57%",
      "headlineClaim": "\"more than half of students without home Wi-Fi\"",
      "universe": 100,
      "numerator": 4,
      "secondary": 3,
      "numeratorLabel": "smartphone-only",
      "secondaryLabel": "no home access",
      "universeLabel": "home internet via a computer",
      "correction": "57% of the seven — not of the classroom",
      "note": "NCES, 2021 ACS estimates, ages 3–18. The date is a caveat.",
      "spark": "Always ask what the percent is of.",
  }, motion="kenburns"),
  [{"at": 0.05, "event": "'57%' fills the frame"},
   {"at": 0.34, "event": "The camera pulls back; the headline shrinks"},
   {"at": 0.40, "event": "The seven flagged squares land first"},
   {"at": 0.52, "event": "The other ninety-three fill in behind them"},
   {"at": 0.76, "event": "Terracotta correction line lands"}]),

B("B13", A2, "REMOTION",
  "The essay's best line was that every one of those laws leaves the exemption undefined and not "
  "one state fills it in. Texas has no general classroom educational-use exception at all — it "
  "names disability plans, documented medical need, and safety. New York does let a school "
  "authorise a specific educational purpose. The blank is real in places. It is not universal.",
  "TtCorrection — the universal claim, narrowed to a real one",
  remotion("TtCorrection", {
      "sourceLabel": "AS PUBLISHED",
      "before": "Every one of those state laws contains an exemption for educational purposes. ",
      "wrong": "Not one defines it",
      "after": ".",
      "corrected": "Texas names specific exceptions and no general educational-use carve-out. New York permits authorisation for a specific educational purpose.",
      "verdict": "OVERSTATED — NARROW IT",
      "citation": "Texas Education Agency, HB 1481 guidance · New York Education Law §2803",
      "note": "The teacher-judgement problem survives. 'Not one' does not.",
      "spark": "A universal claim needs a universal check.",
  }, motion="drawon"),
  [{"at": 0.14, "event": "The published claim holds"},
   {"at": 0.36, "event": "Strike sweeps 'Not one defines it'"},
   {"at": 0.58, "event": "The two statutes drop in beneath"},
   {"at": 0.74, "event": "Citation stamps"}]),

B("B14", A2, "REMOTION",
  "And the essay said no new law addressed the enforcement problem that killed New York's first "
  "ban a decade ago. New York's own statute does. It bars suspending a student purely for using "
  "a device, and it requires the district to report enforcement by demographic group and file a "
  "plan if the disparities are significant.",
  "ReqRingWord — the claim, and the clause that contradicts it",
  remotion("ReqRingWord", {
      "before": "\"None of the new laws addressed what broke the policy ",
      "word": "the first time",
      "after": ".\"",
      "attribution": "the essay — contradicted by New York Education Law §2803(7)",
      "note": "Paper safeguards are not proof. They are not nothing either.",
      "spark": "Check the statute, not the memory.",
  }, motion="annotate"),
  [{"at": 0.16, "event": "The quoted claim sets"},
   {"at": 0.44, "event": "Terracotta ring draws around 'the first time'"},
   {"at": 0.66, "event": "The contradicting attribution lands beneath"}]),

B("B15", A2, "REMOTION",
  "One more. The thirty-seventy rule — thirty percent on hardware, seventy on people. It is a "
  "real recommendation from a real brief. From two thousand and two. Twenty-four years before "
  "the sentence that cites it, and about human infrastructure generally, not about an AI budget.",
  "TtCorrection — a live recommendation revealed as a historical one",
  remotion("TtCorrection", {
      "sourceLabel": "AS PUBLISHED",
      "before": "WestEd recommends 30 percent on hardware and 70 percent on people — ",
      "wrong": "a current benchmark most districts invert",
      "after": ".",
      "corrected": "Investing in Technology: The Learning Return — WestEd policy brief, August 2002, citing Wahl (2000). Historical guidance about human infrastructure, not a modern AI budget optimum.",
      "verdict": "KEEP THE PRINCIPLE — DATE THE SOURCE",
      "citation": "and it cannot describe how districts spend today",
      "note": "The principle may hold. It has not been retested since.",
      "spark": "An undated citation is a warning sign.",
  }, motion="drawon"),
  [{"at": 0.14, "event": "The published claim holds"},
   {"at": 0.36, "event": "Strike sweeps the currency claim"},
   {"at": 0.58, "event": "The 2002 brief drops in with its real title"},
   {"at": 0.74, "event": "Verdict stamps"}]),

# ===========================================================================
# ACT III — WHAT SURVIVED
# ===========================================================================
A3 = "ACT III — WHAT SURVIVED"

B("B16", A3, "CARD",
  "Five corrections in, the obvious question. Is there anything left?",
  "ReqSegmentCard — Act III",
  card("What Survived", "III"),
  [{"at": 0.0, "event": "Eyebrow ACT · III"},
   {"at": 0.35, "event": "Serif title, terracotta period"},
   {"at": 0.62, "event": "Hairline rule draws"}]),

B("B17", A3, "REMOTION",
  "Yes. The core of it. Sixty studies with causal designs, pooled: coaching moves what teachers "
  "do by about half a standard deviation, and moves what students learn by about a fifth. That "
  "is a real effect from a real synthesis, and it is the strongest brick in the essay's wall.",
  "TtEffectBars — the coaching meta-analysis, both outcomes",
  remotion("TtEffectBars", {
      "title": "Teacher coaching — pooled causal effects",
      "scaleNote": "STANDARD DEVIATIONS · BARS SCALED TO THE LARGER EFFECT",
      "data": [
          {"label": "Instructional practice", "value": 49, "display": "0.49 SD", "accent": False},
          {"label": "Student achievement", "value": 18, "display": "0.18 SD", "accent": True},
      ],
      "caveat": "",
      "note": "Kraft, Blazar & Hogan (2018) — 60 studies, causal designs only.",
      "spark": "The brick that holds.",
  }, motion="drawon"),
  [{"at": 0.12, "event": "Title lands"},
   {"at": 0.28, "event": "Practice bar grows to 0.49"},
   {"at": 0.48, "event": "Achievement bar grows to 0.18 in terracotta"},
   {"at": 0.78, "event": "Source note fades up"}]),

B("B18", A3, "REMOTION",
  "But read the same paper for its warning. The effect is not a constant. Much of the evidence "
  "sits in early literacy and small trials — and as the programmes get bigger, the effect gets "
  "smaller. Whatever coaching does, it does less of it at the scale a district would actually "
  "have to buy.",
  "TtScaleDecay — the effect shrinking as the programme grows",
  remotion("TtScaleDecay", {
      "title": "The effect is not a constant.",
      "unit": "SD",
      "showValue": False,
      "qualitative": ["larger", "smaller"],
      "stops": [
          {"scaleLabel": "Small efficacy trials", "effect": 1.0,
           "caption": "tight conditions, close supervision, often early literacy"},
          {"scaleLabel": "Larger effectiveness studies", "effect": 0.36,
           "caption": "the version a district could actually run"},
      ],
      "note": "Direction, not a number — no pooled effect per scale tier exists.",
      "spark": "Scale decay.",
  }, motion="drawon"),
  [{"at": 0.10, "event": "The bar rises to its small-trial height"},
   {"at": 0.30, "event": "Scale label ticks upward"},
   {"at": 0.55, "event": "The bar shrinks in place, ghost outline left behind"},
   {"at": 0.80, "event": "Reading settles at the lower value"}]),

B("B19", A3, "REMOTION",
  "And here is the study that should stop anyone from saying more training, and stopping there. "
  "Around two hundred fourth-grade teachers. Ninety-three hours of maths professional "
  "development — content, collaboration, individual feedback. Teacher knowledge went up. Some "
  "practices improved. Student achievement did not move.",
  "TtNullResult — one meter climbs, the other does not",
  remotion("TtNullResult", {
      "title": "93 hours. Two outcomes.",
      "inputLabel": "~200 fourth-grade teachers · six districts · randomised",
      "showValues": False,
      "left": {"label": "Teacher knowledge", "value": 58, "caption": "improved, along with some observed practices"},
      "right": {"label": "Student achievement", "value": 0, "caption": "no positive effect"},
      "flatLabel": "no positive effect",
      "note": "IES elementary maths PD evaluation. Design principles, not guarantees.",
      "spark": "The word 'sustained' is not a mechanism.",
  }, motion="drawon"),
  [{"at": 0.14, "event": "Study parameters set"},
   {"at": 0.30, "event": "Left meter fills"},
   {"at": 0.34, "event": "Right meter is given the same window and does not move"},
   {"at": 0.66, "event": "Terracotta flat line draws across the right baseline"}]),

B("B20", A3, "REMOTION",
  "So the honest version of the ASSISTments result is not the training did it. It is that a "
  "package — software, training, a warm-up year, and ongoing support — moved eighth-grade maths "
  "by a tenth of a standard deviation for about forty-six dollars a student. That is still a "
  "good buy. It is just not an argument for training alone.",
  "ReqLedger — the intervention listed as what it actually was",
  remotion("ReqLedger", {
      "title": "What was actually bought",
      "rows": [
          {"tier": "COMPONENT", "label": "The ASSISTments platform", "verdict": "included", "accent": False},
          {"tier": "COMPONENT", "label": "Teacher professional development", "verdict": "included", "accent": False},
          {"tier": "COMPONENT", "label": "A teacher warm-up year", "verdict": "included", "accent": False},
          {"tier": "COMPONENT", "label": "Ongoing implementation support", "verdict": "included", "accent": False},
          {"tier": "RESULT", "label": "8th-grade maths, 63 schools", "verdict": "0.10 SD · $46.23", "accent": True},
      ],
      "note": "Four ingredients, one result. The design cannot separate them.",
      "spark": "Supported implementation.",
  }, motion="drawon"),
  [{"at": 0.12, "event": "Components land one at a time"},
   {"at": 0.62, "event": "The result row lands in terracotta"},
   {"at": 0.84, "event": "Note fades up"}]),

B("B21", A3, "REMOTION",
  "There is one more piece of good news, and it is newer. Give tutors live AI assistance during "
  "a session and mastery of the lesson topic rises four points — nine points for the students of "
  "the lowest-rated tutors. The help lands where the expertise is thinnest. End-of-year maths, "
  "though, showed no significant difference.",
  "TtEffectBars — real-time assistance, both readings and the null",
  remotion("TtEffectBars", {
      "title": "Live AI assistance to tutors",
      "scaleNote": "PERCENTAGE POINTS · LESSON-TOPIC MASTERY",
      "data": [
          {"label": "All students", "value": 4, "display": "+4 points", "accent": False},
          {"label": "Students of lower-rated tutors", "value": 9, "display": "+9 points", "accent": True},
      ],
      "caveat": "End-of-year maths: no significant difference.",
      "note": "Wang et al., Tutor CoPilot (working paper) — 900 tutors, 1,800 students.",
      "spark": "Help arrives where skill is thin.",
  }, motion="drawon"),
  [{"at": 0.12, "event": "Title lands"},
   {"at": 0.30, "event": "The 4-point bar grows"},
   {"at": 0.50, "event": "The 9-point bar grows in terracotta"},
   {"at": 0.76, "event": "The null end-of-year result lands in the note"}]),

B("B22", A3, "REMOTION",
  "Notice what every surviving result has in common. None of them is a study of training. They "
  "are studies of supported implementation — the tool and the human capacity to use it, bought "
  "together, evaluated together. That is a real finding. It is a different finding from the one "
  "the essay claimed.",
  "ReqRingWord — the phrase the evidence actually supports",
  remotion("ReqRingWord", {
      "before": "What the evidence supports is not training. It is ",
      "word": "supported implementation",
      "after": " — the tool and the capacity, bought together.",
      "attribution": "the audit's central correction",
      "note": "Complementary investments, not a spending formula.",
      "spark": "Change the noun, keep the policy.",
  }, motion="annotate"),
  [{"at": 0.18, "event": "The line sets in serif"},
   {"at": 0.46, "event": "Terracotta ring draws around the phrase"},
   {"at": 0.70, "event": "Attribution lands beneath"}]),

# ===========================================================================
# ACT IV — THE HOLE IN THE MIDDLE
# ===========================================================================
A4 = "ACT IV — THE HOLE IN THE MIDDLE"

B("B23", A4, "CARD",
  "Which leaves the sentence the whole essay is built on. And that one has a different problem.",
  "ReqSegmentCard — Act IV",
  card("The Hole in the Middle", "IV"),
  [{"at": 0.0, "event": "Eyebrow ACT · IV"},
   {"at": 0.35, "event": "Serif title, terracotta period"},
   {"at": 0.62, "event": "Hairline rule draws"}]),

B("B24", A4, "REMOTION",
  "The claim is that training teachers in AI improves what students learn. Go looking for the "
  "experiment that shows it. Trials of coaching — yes. Trials of maths training — yes. Trials of "
  "AI tools with tutors — yes. Trials of AI-specific teacher training measured on student "
  "outcomes. Almost none.",
  "TtAbsence — the query, and the results dissolving",
  remotion("TtAbsence", {
      "query": "trials: AI-specific teacher professional development → student outcomes",
      "ghosts": [
          "coaching trials — not AI-specific",
          "maths PD trials — not AI",
          "AI tutoring trials — not teacher training",
          "AI assistance for tutors — not durable skill",
      ],
      "survivorLabel": "what survives the filter",
      "survivor": "almost nothing",
      "verdict": "The absence is the finding.",
      "note": "Not that training fails. That nobody ran the study.",
      "spark": "Look for the study. Notice it is not there.",
  }, motion="drawon"),
  [{"at": 0.08, "event": "The query types into the field"},
   {"at": 0.34, "event": "Candidate rows rise one at a time"},
   {"at": 0.44, "event": "Each dissolves as its disqualifier lands"},
   {"at": 0.72, "event": "'almost nothing' resolves in terracotta"},
   {"at": 0.84, "event": "The verdict line lands"}]),

B("B25", A4, "REMOTION",
  "Which changes what kind of sentence this is. The essay wrote: this is not a philosophical "
  "claim, it is what the evidence shows. The audit's answer is that it is a defensible bet. Those "
  "are both respectable things to publish. They are not the same thing, and the reader deserves "
  "to know which one they are being handed.",
  "TtCorrection — a finding, restated as a bet",
  remotion("TtCorrection", {
      "sourceLabel": "AS PUBLISHED",
      "before": "This is not a philosophical claim. ",
      "wrong": "It is what the evidence shows",
      "after": ".",
      "corrected": "It is a defensible bet, extrapolated from adjacent evidence — coaching, supported implementation, and teacher self-report. The direct study does not exist yet.",
      "verdict": "RECLASSIFIED — BET, NOT FINDING",
      "citation": "and a bet is still worth making; it is just labelled differently",
      "note": "The recommendation survives this. The epistemics of the sentence do not.",
      "spark": "Say which one you are selling.",
  }, motion="drawon"),
  [{"at": 0.14, "event": "The published claim holds"},
   {"at": 0.36, "event": "Strike sweeps 'It is what the evidence shows'"},
   {"at": 0.58, "event": "The reclassification drops in"},
   {"at": 0.74, "event": "Verdict stamps"}]),

B("B26", A4, "REMOTION",
  "The essay's closing analogy has the same shape. Doctors have mandatory continuing education, "
  "so teachers should too — and teaching has no such system. Illinois requires a hundred and "
  "twenty hours for licence renewal. The infrastructure exists. The argument that it should be "
  "better is a different argument from the one the essay made.",
  "ReqRingWord — the analogy's missing premise",
  remotion("ReqRingWord", {
      "before": "\"The infrastructure for continuous professional development ",
      "word": "does not exist for teaching",
      "after": ".\"",
      "attribution": "the essay — Illinois requires 120 hours for licence renewal",
      "note": "Massachusetts counts 50 credits per two-year cycle, not 50 a year.",
      "spark": "The system exists. Argue about its quality.",
  }, motion="annotate"),
  [{"at": 0.16, "event": "The quoted claim sets"},
   {"at": 0.44, "event": "Terracotta ring draws around the false premise"},
   {"at": 0.68, "event": "The Illinois requirement lands beneath"}]),

B("B27", A4, "REMOTION",
  "Even the survey the essay leans on says more than it was asked to. Seventy percent of teachers "
  "not using AI say they lack the knowledge and skills. Ask the same teachers a different question "
  "— what stops you doing professional learning at all — and two-thirds say other "
  "responsibilities, three in five say scheduling. The knowledge gap is real. So is the calendar.",
  "TtEffectBars — the three barriers, and the two questions behind them",
  remotion("TtEffectBars", {
      "title": "Two questions, two answers",
      "scaleNote": "PERCENT CITING THIS BARRIER · SELF-REPORT",
      "data": [
          {"label": "Not using AI: lack the knowledge", "value": 70, "display": "70%", "accent": False},
          {"label": "Won't do PD: other responsibilities", "value": 67, "display": "67%", "accent": True},
          {"label": "Won't do PD: scheduling conflicts", "value": 59, "display": "59%", "accent": True},
      ],
      "caveat": "Row one answers a different survey question from rows two and three.",
      "note": "OECD TALIS 2024, US. Row one is a different survey item.",
      "spark": "Buy the hours as well as the content.",
  }, motion="drawon"),
  [{"at": 0.12, "event": "Title lands"},
   {"at": 0.26, "event": "Knowledge bar grows"},
   {"at": 0.44, "event": "Responsibilities bar grows in terracotta"},
   {"at": 0.60, "event": "Scheduling bar grows"},
   {"at": 0.82, "event": "Self-report caveat fades up"}]),

# ===========================================================================
# ACT V — WHAT WOULD SETTLE IT
# ===========================================================================
A5 = "ACT V — WHAT WOULD SETTLE IT"

B("B28", A5, "CARD",
  "An audit that only subtracts is half an audit. Here is the study that would settle it.",
  "ReqSegmentCard — Act V",
  card("What Would Settle It", "V"),
  [{"at": 0.0, "event": "Eyebrow ACT · V"},
   {"at": 0.35, "event": "Serif title, terracotta period"},
   {"at": 0.62, "event": "Hairline rule draws"}]),

B("B29", A5, "REMOTION",
  "Give every school the same tools and the same basic orientation. Then randomise which schools "
  "also get coaching and protected time to collaborate. That comparison isolates the thing "
  "actually in dispute — not whether technology helps, but whether the support wrapped around it "
  "is what earns the gain.",
  "ReqLevers — the design that isolates the disputed ingredient",
  remotion("ReqLevers", {
      "title": "The study nobody has run",
      "levers": [
          {"name": "Hold constant", "sub": "same tools, same essential orientation, every school"},
          {"name": "Randomise", "sub": "coaching and protected collaborative time, by school"},
          {"name": "Measure", "sub": "student learning on curriculum-aligned tests taken without AI"},
      ],
      "blocked": ["whether the tool alone works — that needs a separate arm"],
      "blockedLabel": "what this design still cannot tell you",
      "note": "Pre-register the outcomes. Power it for achievement, not for teacher confidence.",
      "spark": "Isolate the disputed ingredient.",
  }, motion="drawon"),
  [{"at": 0.12, "event": "Title lands"},
   {"at": 0.30, "event": "Three columns rise on a stagger"},
   {"at": 0.62, "event": "Subtitles type beneath"},
   {"at": 0.80, "event": "The blocked row lands in grey — the honest limit"}]),

B("B30", A5, "REMOTION",
  "And measure six things, not one. Did teachers improve. Did students learn. Did the learning "
  "last. Did the teacher's judgement last once the AI was taken away. Was access equal. And could "
  "the school actually afford to keep doing it.",
  "ReqLedger — the six questions the evaluation has to answer",
  remotion("ReqLedger", {
      "title": "Six questions, six measures",
      "rows": [
          {"tier": "PRACTICE", "label": "Did teachers improve?", "verdict": "blind-scored lessons", "accent": False},
          {"tier": "LEARNING", "label": "Did students learn?", "verdict": "tests taken without AI", "accent": False},
          {"tier": "DURABILITY", "label": "Did the learning last?", "verdict": "delayed transfer tasks", "accent": False},
          {"tier": "DURABILITY", "label": "Did the teacher's judgement last?", "verdict": "new cases, no AI", "accent": True},
          {"tier": "EQUITY", "label": "Was access equal?", "verdict": "outcomes by baseline access", "accent": False},
          {"tier": "COST", "label": "Could the school sustain it?", "verdict": "full delivery cost", "accent": False},
      ],
      "note": "Confidence, time saved and usage are secondary outcomes. Never the headline.",
      "spark": "Assisted performance is not learning.",
  }, motion="drawon"),
  [{"at": 0.10, "event": "Rows land in sequence"},
   {"at": 0.52, "event": "The durability row resolves in terracotta"},
   {"at": 0.86, "event": "Note fades up"}]),

B("B31", A5, "REMOTION",
  "And name what would prove the thesis wrong, because a claim that cannot lose is not a claim. "
  "Run that trial. If the coached schools and the uncoached schools land on the same student "
  "results, then the money belongs in the tools after all, and the essay was wrong.",
  "TtNullResult — the falsifying result, drawn in advance",
  remotion("TtNullResult", {
      "title": "What would prove it wrong",
      "inputLabel": "same tools · same orientation · coaching randomised by school",
      "showValues": False,
      "left": {"label": "Coached schools", "value": 42, "caption": "student achievement"},
      "right": {"label": "Uncoached schools", "value": 42, "caption": "student achievement"},
      "flatLabel": "no gap = the thesis fails",
      "note": "Nobody is running it. The audit's most useful sentence.",
      "spark": "A claim that cannot lose is not a claim.",
  }, motion="drawon"),
  [{"at": 0.14, "event": "The design line sets"},
   {"at": 0.30, "event": "Both meters climb together"},
   {"at": 0.56, "event": "They arrive level — no gap"},
   {"at": 0.70, "event": "Terracotta line names the falsifying outcome"}]),

# ===========================================================================
# CLOSING BLOCK — the your-turn standard
# ===========================================================================

B("B32", "VERDICT", "BOOKEND",
  "So the verdict. The recommendation survives — invest in the capacity to use the tools, not "
  "just the tools. What did not survive is the evidence base as it was described: a subgroup "
  "narrowed, a cost attributed to the wrong ingredient, a universal claim that two statutes "
  "disprove, a benchmark from two thousand and two, and a finding that turns out to be a bet. "
  "The essay is better after the audit than before it. That is what an audit is for.",
  "ClaudeVerdictArtifact — the verdict page",
  remotion("ClaudeVerdictArtifact", {
      "artifactTitle": "verdict.md",
      "artifactHeading": "Train the Teacher",
      "artifactLines": [
          "The recommendation holds: buy capacity alongside tools, not instead of them.",
          "The Florida figure is in-school suspensions, Black students, one district.",
          "The $46.23 bought a package — software, PD, warm-up year, support.",
          "'Not one state defines it' is disproved by Texas and New York.",
          "The 30/70 rule is a 2002 recommendation, not a current measurement.",
          "'What the evidence shows' is really a defensible bet — no direct trial exists.",
          "FALSIFIABLE: randomise coaching on top of identical tools. Equal results kill it.",
      ],
  }, motion="hold"),
  [{"at": 0.0, "event": "Artifact window opens on the cream stage"},
   {"at": 0.18, "event": "Verdict lines land in sequence"},
   {"at": 0.86, "event": "The falsifiability line holds last"}]),

B("B33", "YOUR TURN", "BOOKEND",
  "Your turn. Take something you have published — a post, a memo, a proposal — and do not ask "
  "Claude whether it is good. Ask it to run an adversarial audit: decompose the argument into "
  "separate claims, rule on each one, and find every number that does not mean what the sentence "
  "says it means. Ask it to tell you which of your claims is a finding and which is a bet. That "
  "is the whole method in this film, and it works on anything you wrote.",
  "ClaudeComposerAsk — the viewer's prompt, read aloud",
  remotion("ClaudeComposerAsk", {
      "greeting": "Your turn.",
      "command": "Here is something I published. Run an adversarial evidence audit: decompose it into separate claims, rule on each, verify every number against its actual source, and tell me which claims are findings and which are bets.",
      "segment": TITLE,
      "topic": TOPIC,
      "runningText": "paste this into Claude…",
      "output": [],
      "folderLabel": "@NikBearBrown",
      "modelLabel": "Opus 5",
      "effortLabel": "High",
  }, motion="type"),
  [{"at": 0.0, "event": "Composer types the viewer's prompt"},
   {"at": 0.60, "event": "Send arms terracotta; prompt holds while discussed"},
   {"at": 0.90, "event": "Held full-frame for the pause"}]),

B("B34", "OUTRO", "BOOKEND",
  "Train the Teacher. Liam, in for Bear.",
  "ClaudeTitleOutro — locked card, slug-seeded CLAWD mascot",
  remotion("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG}, motion="hold"),
  [{"at": 0.0, "event": "Poster-serif title, terracotta terminal period"},
   {"at": 0.35, "event": "@NikBearBrown beneath — hardcoded"},
   {"at": 0.55, "event": "Slug-seeded CLAWD mascot; translation and scale only"}]),


# ===========================================================================
sheet = {
    "metadata": {
        "slug": SLUG,
        "title": TITLE,
        "subtitle": "An argument published, then audited — and the sentences that did not survive",
        "topic": TOPIC,
        "purpose": (
            "Films Nik Bear Brown's May 2026 skepticism.ai essay 'Not the App. Not the Ban. "
            "Train the Teacher.' together with the September 2026 adversarial evidence audit "
            "commissioned against it. The film's subject is the pair: what the audit corrected, "
            "what survived, and the study nobody has run."
        ),
        "channel": "claude-liam",
        "handle": "@NikBearBrown",
        "register": "Teardown",
        "prose": "teardown",
        "voice": VOICE,
        "voice_kokoro": VOICE,
        "engine": "kokoro",
        "brand": "claude",
        "aspect": "16:9",
        "fps": 30,
        "skill": "deep-explainer",
        "vox_beats": 0,
        "vox_rationale": (
            "VOX LAW: the evidence in this film is statutes, cost reports and effect sizes. "
            "A pantry still could only be texture here, so there are none and there is no "
            "SHOPPING.md. Every beat renders."
        ),
        "sources": [
            "Nik Bear Brown, 'Not the App. Not the Ban. Train the Teacher.', skepticism.ai, 2026-05-16",
            "Adversarial evidence audit / research brief, 2026-09-07 (supplied)",
        ],
        "source_precedence": "Where the essay and the audit disagree, the AUDIT governs.",
    },
    "beats": beats,
}

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "beat_sheet.json"), "w") as f:
    json.dump(sheet, f, indent=2, ensure_ascii=False)

total = sum(b["estimated_duration_s"] for b in beats)
print(f"{len(beats)} beats — estimated {total:.0f}s ({int(total // 60)}:{int(total % 60):02d})")
lanes = {}
for b in beats:
    lanes[b["lane"]] = lanes.get(b["lane"], 0) + 1
print("lanes:", lanes)
prev = None
run = 0
for b in beats:
    c = b["shot"]["remotion"]["component"]
    run = run + 1 if c == prev else 1
    if run > 2:
        print(f"  WARN consecutive-scheme: {b['beat_id']} is {run}x {c}")
    prev = c
