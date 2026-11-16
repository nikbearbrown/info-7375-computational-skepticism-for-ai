#!/usr/bin/env python3
"""make_sheet.py — writes beat_sheet.json for tldr-features-entering-a-room.

tldr skill (brutalist.art/skills/make/tldr). Section S1 of chapter 5
(youtube/tldr-sections-05-explainability.md): the chapter's worked example —
one loan applicant, three features (income, debt-to-income, zip code),
f̂(x) = 0.72, E[f̂] = 0.55, payout 0.17; income's six-ordering table
+0.08 +0.08 +0.07 +0.09 +0.06 +0.06 → φ_income = 0.073; φ_debt = 0.062,
φ_zip = 0.035 ("Suppose the same calculation produces…"); Efficiency 0.17.
The chapter introduces the example with "Suppose" / "Say" — a constructed
example — so the film captions it "constructed example" once, small, and keeps
it on the stage. Every number is the chapter's own or recomputed from its own
inputs; asserted here and in scenes.py; FACTCHECK.md carries the rows.
Re-run, then lock_cards.py, then ./art run.
"""
import json
from fractions import Fraction as Fr
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent

SLUG = "tldr-features-entering-a-room"
TITLE = "Features Entering a Room"
COURSE = "INFO 7375 · Computational Skepticism · Chapter 5"

# ── the chapter's worked example (§"A worked example") ─────────────────────────
F_X, E_F = 0.72, 0.55
PAYOUT = round(F_X - E_F, 2)
assert PAYOUT == 0.17
# income's six orderings: (order, coalition already in, bump)
ORDERS = [(("income", "debt", "zip"), (), 0.08),
          (("income", "zip", "debt"), (), 0.08),
          (("debt", "income", "zip"), ("debt",), 0.07),
          (("zip", "income", "debt"), ("zip",), 0.09),
          (("debt", "zip", "income"), ("debt", "zip"), 0.06),
          (("zip", "debt", "income"), ("debt", "zip"), 0.06)]
assert len(ORDERS) == factorial(3) == 6
for order, coal, _ in ORDERS:                               # the coalition is exactly who arrived before income
    assert set(order[:order.index("income")]) == set(coal)
PHI_INC = sum(b for *_, b in ORDERS) / 6
assert abs(PHI_INC - 0.07333) < 1e-4 and round(PHI_INC, 3) == 0.073
PHI = {"income": 0.073, "debt": 0.062, "zip": 0.035}       # φ_debt, φ_zip are the chapter's "Suppose" values
assert abs(sum(PHI.values()) - PAYOUT) < 1e-9               # Efficiency check, as the chapter states it
# the weight |S|!(|F|-|S|-1)!/|F|! (exercise W4) and its equivalence with the ordering average
def w(s, n=3): return Fr(factorial(s) * factorial(n - s - 1), factorial(n))
assert w(1) == Fr(1, 6) and w(0) == Fr(2, 6) == w(2)
assert w(0) * 1 + w(1) * 2 + w(2) * 1 == 1                    # 1 empty + 2 singletons + 1 pair: weights sum to 1
WEIGHTED = float(w(0)) * 0.08 + float(w(1)) * 0.07 + float(w(1)) * 0.09 + float(w(2)) * 0.06
assert abs(WEIGHTED - PHI_INC) < 1e-12                       # grouping by coalition gives the same 0.073
# the two levels the film places on the prediction line, recomputed from the chapter's inputs
V_INC = round(E_F + 0.08, 2); V_DEBT_ZIP = round(F_X - 0.06, 2)
assert (V_INC, V_DEBT_ZIP) == (0.63, 0.66)                   # v({income}) = 0.55 + 0.08; v({debt, zip}) = 0.72 − 0.06


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

B00_N = ("Kumusta. This is Liam, in for Bear, with chapter five of INFO 7375, Computational Skepticism for AI, at Northeastern. "
         "This film is about splitting one loan prediction fairly among three features. "
         "A feature's fair share is its average bump over every order it could have entered the room. "
         "You'll watch six orders fill a table, then three bars fill the gap. "
         "The trap: measuring once, and calling that the contribution.")
B00_EST = round(len(B00_N.split()) / 2.5, 1)
beats.append(beat("B00", "tldr · what", B00_N,
    remotion("ClaudeTldrWhat", {
        "eyebrow": "TL;DR", "heading": "What This Film Is About", "greeting": "Kumusta, Liam", "topic": COURSE,
        "question": "How do you split one prediction fairly among three features?",
        "lines": ["A feature's fair share is its average bump over every order it could enter the room.",
                  "Watch six orders fill a table, then three bars fill the 0.17 gap exactly.",
                  "The trap: measure once, first in or last in, and call that the contribution."],
        "cues": [round(B00_EST * f, 1) for f in (0.05, 0.45, 0.68, 0.85)], "durationSeconds": B00_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "'TL;DR.' wordmark; 'Kumusta, Liam'; the course line; heading"},
         {"at": 0.05, "event": "the question writes on"},
         {"at": 0.45, "event": "line 1 lands on 'a feature's fair share'"},
         {"at": 0.68, "event": "line 2 lands on 'you'll watch'"},
         {"at": 0.85, "event": "line 3 lands on 'the trap'"}]),
    lane="bookend"))

B01_N = ("Why should you care? Every SHAP bar in a model report estimates this average. "
         "Read one bump as the answer, and you're arguing over a number that depends on who walked in first. "
         "Know the average, and you can check any SHAP chart: the bars must add up to the gap. "
         "It unlocks the harder question: what a share does not tell you.")
B01_EST = round(len(B01_N.split()) / 2.5, 1)
beats.append(beat("B01", "tldr · why", B01_N,
    remotion("ClaudeTldrWhy", {
        "eyebrow": "TL;DR", "heading": "Why You Should Care", "topic": COURSE,
        "lead": "Every SHAP bar in a model report estimates this average.",
        "lines": ["Read one bump as the answer, and you argue over a number that depends on who walked in first.",
                  "Know the average, and you can check any SHAP chart: the bars must add up to the gap.",
                  "It unlocks the harder question: what a share does not tell you."],
        "cues": [round(B01_EST * f, 1) for f in (0.05, 0.28, 0.58, 0.82)], "durationSeconds": B01_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "page turn: same header, heading 'Why You Should Care'"},
         {"at": 0.05, "event": "the stake writes on"},
         {"at": 0.28, "event": "dash 1 on 'read one bump'"},
         {"at": 0.58, "event": "dash 2 on 'know the average'"},
         {"at": 0.82, "event": "dash 3 on 'unlocks'"}]),
    lane="bookend", qc={"sparse_by_design": True, "sparse_reason": "TL;DR card two — text lands on cues by design."}))

beats.append(beat("B02", "the question",
    "The question this film is really asking: what is income's fair share? "
    "Not how much did income add. That has a different answer depending on who was already in the room.",
    remotion("BrutalistHesitantWriter", {
        "text": "How much did income add?",
        "triggerWords": "How much did income add", "replacementWords": "What is income's fair share",
        "fontSize": 78, "charMs": 22, "hesitateBetween": 5, "hesitateWithin": 1, "mistakeRate": 0, "jitter": 20,
        "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types the naive question"},
         {"at": 0.25, "event": "types 'How much did income add?'; backspaces the phrase → 'What is income's fair share?' on the spoken correction"},
         {"at": 0.85, "event": "caret holds on the corrected question"}]),
    lane="bookend", lead_silence_s=0.8,
    motion_claim="The writer types the naive 'how much did it add' and corrects the phrase that makes it the wrong question.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}))

B03_N = ("Four words you'll hear. A feature: one input the model reads; here, income, debt-to-income ratio, and zip code. "
         "A prediction: the model's output for one person; here, her chance of approval. "
         "The baseline: the model's average prediction across the data. "
         "A coalition: the set of features already in the room.")
B03_EST = round(len(B03_N.split()) / 2.5, 1)
beats.append(beat("B03", "terms", B03_N,
    remotion("ClaudeDefinitions", {
        "title": "Terms In This Film",
        "terms": [{"term": "feature", "meaning": "one input the model reads: income, debt-to-income ratio, zip code"},
                  {"term": "prediction", "meaning": "the model's output for one person; here, her chance of approval"},
                  {"term": "baseline", "meaning": "the model's average prediction across the data"},
                  {"term": "coalition", "meaning": "the set of features already in the room when another arrives"}],
        "durationSeconds": B03_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'feature' lands, terracotta"}, {"at": 0.4, "event": "'prediction' lands; first settles"},
         {"at": 0.62, "event": "'baseline' lands"}, {"at": 0.8, "event": "'coalition' lands"}]),
    lane="bookend", proof="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: prerequisites only — the Shapley value (the film's answer) is earned in B16."}))

# ── LEARN section 1 (B10–B19) ────────────────────────────────────────────────
beats.append(beat("B10", "learn 1",
    "One loan applicant. The model gives her a zero point seven two chance of approval. Across everyone, it averages zero point five five. "
    "So there's a gap of zero point one seven, and three features put it there: income, debt-to-income, zip code. "
    "How much of that gap is income's? It sounds like it should have one answer.",
    manim("B10_OneApplicant",
          "The three feature names write across the top; a prediction line draws along the bottom with ticks at 0.55 (average) and 0.72 (her score); an ink dot slides from 0.55 to 0.72; a ghost span bar fills the gap above the line, labelled '0.17 to split'; the question 'how much of the 0.17 is income's?' writes centre; a terracotta dot lands beside 'income'; 'constructed example' caption bottom-left.",
          [{"at": 0.05, "event": "the prediction line and the 0.55 tick"}, {"at": 0.2, "event": "the dot slides to 0.72 on 'zero point seven two'"},
           {"at": 0.45, "event": "the span '0.17 to split' and the three feature names"}, {"at": 0.75, "event": "the question; dot beside 'income'"}],
          "The line, the dot and the span are the persistent objects: the span is what the three bars fill in B15 and B19."),
    role="HOOK", section=1,
    learn={"question": "One prediction sits 0.17 above the average. How much of that is income's?",
           "action": "Place her score and the average on one line; shade the gap; name the three features.",
           "observation": "One gap, three contributors, no split shown.",
           "inference": "The split has to come from somewhere the model does not print.",
           "next_question": "What does income add if it's the first thing the model learns about her?"}))

beats.append(beat("B11", "learn 1",
    "Picture the features walking into a room, one at a time. With nobody inside, the model knows nothing about her, so it predicts the average: zero point five five. "
    "Income walks in first. Now it knows her income, with the other two still averaged over the data, and the score climbs to zero point six three. "
    "Income added zero point zero eight.",
    manim("B11_IncomeFirst",
          "The feature names move up into a table header ('arrival order · already in · income adds'); row one: 'income' slides into seat one; on the prediction line the dot climbs 0.55 → 0.63 and an ink bump bar grows over that stretch, labelled '+0.08'; the row records 'nobody' and '+0.08' with a small ink bar; debt and zip slide into seats two and three; terracotta dot beside the row's +0.08.",
          [{"at": 0.1, "event": "table header; the room is empty — dot at 0.55"}, {"at": 0.4, "event": "'income' slides into seat one on 'walks in first'"},
           {"at": 0.65, "event": "dot climbs to 0.63; bump bar grows; '+0.08'"}, {"at": 0.85, "event": "row records +0.08; dot beside it"}],
          "The first instance: an arrival and its bump, shown as motion on the line and recorded as a row."),
    role="INSTANCE", section=1,
    learn={"question": "What does income add when it walks into an empty room?",
           "action": "Income arrives first; the prediction moves from the average to 0.63.",
           "observation": "A bump of +0.08, recorded in row one.",
           "inference": "A contribution can be measured as the bump a feature makes on arrival.",
           "next_question": "Is that bump the same if income arrives last?"}))

beats.append(beat("B12", "learn 1",
    "The obvious way to measure income: start from the full room and take income out. Her score is zero point seven two. Without income, zero point six six. "
    "So income is worth zero point zero six. That's the same as income walking in last. "
    "But a moment ago it was worth zero point zero eight. Same feature, same applicant, two answers. Which one is income's?",
    manim("B12_DropItAndSee",
          "Row six fills: 'debt', 'zip', then 'income' last; on the line the dot sits at 0.72, drops to 0.66 as income leaves, and the stretch 0.66–0.72 becomes a second ink bump bar labelled '+0.06'; B11's +0.08 bar dims to the foil; '+0.08 or +0.06?' writes at right with a terracotta X beside it.",
          [{"at": 0.1, "event": "row six: debt and zip arrive"}, {"at": 0.3, "event": "the dot drops 0.72 → 0.66 on 'take income out'"},
           {"at": 0.55, "event": "bump bar 0.66–0.72, '+0.06'; the first bar dims"}, {"at": 0.85, "event": "'+0.08 or +0.06?' and the X"}],
          "The natural wrong turn walked to its limit: 'drop it and see' is a real measurement, and it disagrees with the first one on screen."),
    role="NAIVE", section=1,
    learn={"question": "Can't we just remove income from the full model and see what changes?",
           "action": "Take income out of the full room: 0.72 → 0.66.",
           "observation": "+0.06, not +0.08. Both bars sit on the same line.",
           "inference": "'Drop it and see' measures one room, and a different room gives a different answer.",
           "next_question": "What about the rooms in between?"}))

beats.append(beat("B13", "learn 1",
    "So try the seats in between. Debt walks in, then income: income adds zero point zero seven. "
    "Zip code first, then income: zero point zero nine. "
    "Every room income walks into gives it a different bump. The contribution isn't a property of income alone. It depends on who got there first.",
    manim("B13_MiddleSeats",
          "Rows three and four fill: 'debt' then 'income' (+0.07), 'zip' then 'income' (+0.09); each row's small ink bar grows to its bump; the '+0.08 or +0.06?' line clears; a terracotta dot beside +0.09; caption 'one bump per room'.",
          [{"at": 0.1, "event": "row three: debt, then income, +0.07"}, {"at": 0.45, "event": "row four: zip, then income, +0.09"},
           {"at": 0.75, "event": "four bars of four lengths; dot beside +0.09"}],
          "The second parametrized instance: vary who is already in the room, replay the arrival."),
    role="INSTANCE", section=1,
    learn={"question": "What does income add when it arrives in the middle?",
           "action": "Fill the rows where income arrives second, after debt and after zip.",
           "observation": "+0.07 and +0.09: four rooms, four bumps.",
           "inference": "A feature's bump depends on the coalition it joins.",
           "next_question": "If no single room is the answer, what is?"}))

beats.append(beat("B14", "learn 1",
    "Here's the move. Don't pick a room. Take every order the three could arrive in. That's three factorial: six orders, each equally likely. "
    "Two start with income, two end with it, two put it in the middle. Six bumps. "
    "Before we average them, commit. When we do this for all three features, do their averages fill the zero point one seven exactly, overshoot, or fall short?",
    manim("B14_EveryOrder",
          "The remaining rows two and five fill (income, zip, debt: +0.08; debt, zip, income: +0.06); 'six orders, each equally likely' writes as the header note; the two bump bars on the prediction line fade and the ghost span returns with a '?' beside '0.17 to split'; a terracotta dot beside the '?'; caption 'fill it exactly, or not? commit'.",
          [{"at": 0.1, "event": "rows two and five fill"}, {"at": 0.35, "event": "'six orders, each equally likely'"},
           {"at": 0.6, "event": "the line clears to the span; '?' beside it"}, {"at": 0.8, "event": "HOLD — nothing moves on 'commit'"}],
          "The representation arrives complete: every ordering, one row each; the predict hold sits on the span the bars must fill."),
    role="SHIFT", section=1, predict=True,
    learn={"question": "If no room is privileged, which rooms count?",
           "action": "Fill all 3! = 6 orderings, one row each.",
           "observation": "Six bumps: 0.08, 0.08, 0.07, 0.09, 0.06, 0.06.",
           "inference": "The fair share should weigh every order equally. Predict: will the three averages fill 0.17?",
           "next_question": "Average them — where do the three bars stop?"}))

beats.append(beat("B15", "learn 1",
    "Six bumps, one average: zero point zero seven three. "
    "The same six-order average for debt gives zero point zero six two. For zip code, zero point zero three five. "
    "Now lay them end to end, starting at the average. Look where they stop.",
    manim("B15_AverageThem",
          "The six small bars slide together and merge into one bar of length 0.073, which travels down onto the span at 0.55; the debt bar (0.062) and the zip bar (0.035) grow on after it; the three stop exactly at the 0.72 tick; the ink dot sits at the end; terracotta dot beside '0.72'; caption 'nothing left over'.",
          [{"at": 0.0, "event": "six bars merge into one on 'one average'"}, {"at": 0.3, "event": "the averaged bar lands on the span at 0.55"},
           {"at": 0.5, "event": "debt, then zip, grow on after it"}, {"at": 0.85, "event": "they stop at 0.72; 'nothing left over'"}],
          "The aha is the morph: the table's six bumps become one bar, and three bars fill the HOOK's span exactly."),
    role="TRANSFORM", section=1,
    learn={"question": "Where do the three averaged bars stop?",
           "action": "Merge income's six bumps; add debt's and zip's averages end to end from 0.55.",
           "observation": "0.073 + 0.062 + 0.035 ends exactly at 0.72.",
           "inference": "Averaging over every order both settles the split and uses up the whole gap.",
           "next_question": "What is this average, as a rule?"}))

beats.append(beat("B16", "learn 1",
    "This thing we keep pointing at deserves a name. Group the six rows by who was already in the room: nobody twice, debt once, zip once, both twice. "
    "Weight each bump by its share of the six orders, add, and you get the same zero point zero seven three. "
    "That's the Shapley value. And what you just watched the bars do has a name too: efficiency. The shares add up to the gap.",
    manim("B16_NameIt",
          "The table's coalition and bump columns fold into one weighted sum, 2/6·0.08 + 1/6·0.07 + 1/6·0.09 + 2/6·0.06 = 0.073 (MathTex); beneath it the general Shapley formula writes; the force plot's value labels morph into the efficiency equation φ_income + φ_debt + φ_zip = f̂(x) − E[f̂]; the title becomes 'The Shapley Value'; terracotta dot beside 0.073.",
          [{"at": 0.1, "event": "rows fold into the weighted sum on 'group the six rows'"}, {"at": 0.45, "event": "'= 0.073'; the general formula writes"},
           {"at": 0.7, "event": "title → 'The Shapley Value' on the name"}, {"at": 0.85, "event": "labels morph into the efficiency line"}],
          "The abstraction arrives as an endpoint: the table the viewer filled folds into the formula; the force plot's labels become the efficiency sum."),
    role="ABSTRACTION", section=1,
    learn={"question": "What is the six-order average, as a rule?",
           "action": "Group the orderings by coalition, weight each bump, sum; generalize; name it.",
           "observation": "The weights 2/6, 1/6, 1/6, 2/6 reproduce 0.073; the bars' sum is a second equation.",
           "inference": "The Shapley value is the average marginal contribution over every ordering; Efficiency says the shares sum to f̂(x) − E[f̂].",
           "next_question": "What does each symbol in the formula mean?"}))

beats.append(beat("B17", "learn 1",
    "Read the line. Left side: income's share, phi. Right side: every room income could walk into, the bump it makes there, times a weight. "
    "The equals sign says the share is exactly that weighted average, nothing else. "
    "S is who's already in the room. F is all three features. v of S is the score knowing only S. "
    "And the weight is the fraction of orders where S arrives first: with one feature ahead of income and one behind, "
    "one factorial times one factorial over three factorial. One sixth. Back to the bars.",
    manim("B17_ReadTheFormula",
          "Split stage: the Shapley formula persists at the top; the left band writes 'left: income's fair share', 'right: each room's bump, weighted', '=: exactly that average'; the right band writes a glossary (φᵢ · i's fair share; S · who's already in; |F| · all features, 3; v(S) · score knowing only S); the worked weight 1!·1!/3! = 1/6 and 0!·2!/3! = 2/6 writes at the bottom (MathTex); a terracotta dot moves to the symbol being read.",
          [{"at": 0.05, "event": "LHS / RHS sentences"}, {"at": 0.3, "event": "'=' claim"},
           {"at": 0.45, "event": "glossary rows land one at a time"}, {"at": 0.75, "event": "worked weight = 1/6"}],
          "The equation tangent (five zones, explain never derive): sentences before symbols, a glossary, one worked value."),
    role="TANGENT", section=1,
    learn={"question": "What does each symbol in the Shapley formula mean?",
           "action": "Translate each side to a sentence; gloss φ, S, F, v(S); compute one weight.",
           "observation": "|F| = 3, |S| = 1 gives 1!·1!/3! = 1/6, the share of orders with one feature before income.",
           "inference": "The formula is the ordering average written by coalition.",
           "next_question": "And the second line, the sum?"}))

beats.append(beat("B18", "learn 1",
    "Now the second line. Left side: the three shares, added. Right side: her score minus the average. "
    "The equals sign is the promise: nothing left over, nothing counted twice. "
    "f-hat of x is her score, zero point seven two. The expected f-hat is the baseline, zero point five five. "
    "Plug in: zero point zero seven three, plus zero point zero six two, plus zero point zero three five, is zero point one seven. It holds. "
    "That's what a force plot is: efficiency, drawn.",
    manim("B18_ReadTheSum",
          "The efficiency equation rises to the top; the force plot's bars stay on the line; the left band writes 'left: the three shares, added', 'right: her score minus the average', '=: nothing left, nothing twice'; the right band glosses f̂(x) · her score, 0.72 and E[f̂] · the average, 0.55; the plugged-in sum 0.073 + 0.062 + 0.035 = 0.17 = 0.72 − 0.55 writes over the bars (MathTex); a terracotta dot beside the final 0.17.",
          [{"at": 0.05, "event": "the equation rises; sentences write"}, {"at": 0.35, "event": "the two glossary rows"},
           {"at": 0.6, "event": "the plugged-in sum writes over the bars"}, {"at": 0.85, "event": "dot beside 0.17 on 'it holds'"}],
          "The second tangent: the sum read as a claim, plugged in on the same bars it describes."),
    role="TANGENT", section=1,
    learn={"question": "What does the efficiency line claim?",
           "action": "Read each side as a sentence; gloss f̂(x) and E[f̂]; plug in the three shares.",
           "observation": "0.073 + 0.062 + 0.035 = 0.17 = 0.72 − 0.55.",
           "inference": "The force plot is this equation drawn: the gap is fully accounted for.",
           "next_question": "So, how much of the gap is income's?"}))

beats.append(beat("B19", "learn 1",
    "Back to her score. How much of the zero point one seven is income's? Not the zero point zero eight from the empty room, not the zero point zero six from the full one: "
    "zero point zero seven three, its average over every order. "
    "What this film didn't do: say what zip code's zero point zero three five means in the world. "
    "It's a real number about the model. Whether zip stands in for something else is another question.",
    manim("B19_Payoff",
          "The sum morphs back into the force plot's labels; the question from B10 returns; the ghost +0.08 and +0.06 bars flash back above income's bar and fold into it; a terracotta dot travels along the income bar, then to the zip bar; boundary caption 'not taught: what 0.035 means'.",
          [{"at": 0.05, "event": "labels return; the question returns"}, {"at": 0.3, "event": "the +0.08 and +0.06 ghosts fold into 0.073"},
           {"at": 0.6, "event": "dot to the zip bar on 'zip code's 0.035'"}, {"at": 0.85, "event": "boundary caption"}],
          "The HOOK's line, span and question resolve against the filled force plot; the boundary is one dim line."),
    role="PAYOFF", section=1,
    learn={"question": "So, how much of the 0.17 is income's?",
           "action": "Put the two single-room answers beside the average; move to zip's bar.",
           "observation": "0.073 sits between 0.06 and 0.08; zip's 0.035 is on the same plot.",
           "inference": "The fair share is the average; the plot is precise about the model, and silent about the world.",
           "next_question": ""}))

beats.append(beat("BVDT", "verdict",
    "Let's recap with Claude. How much of a prediction belongs to one feature has no single-room answer: its bump depends on who's already there. "
    "The Shapley value averages that bump over every order the features could arrive in. "
    "The shares then add up exactly to the gap between the prediction and the average. "
    "And that precision is about the model. Zip code's share is a real number, not a fact about the world.",
    remotion("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": TITLE,
        "artifactLines": ["A feature's bump depends on who is already in the room: 0.08 first, 0.06 last.",
                          "The Shapley value averages that bump over every arrival order: 0.073 for income.",
                          "Efficiency: the shares add up exactly to the gap, 0.72 − 0.55 = 0.17.",
                          "The precision is about the model; zip's 0.035 is not a fact about the world."]},
        [{"at": 0.0, "event": "artifact page opens"}, {"at": 0.2, "event": "four verdict lines land"}]),
    lane="bookend", lead_silence_s=0.5, qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}))

YT = ("Build me a tiny model with three features, one of them zip code, and write out its value function v(S) for all eight coalitions. "
      "Before computing anything, predict which feature gets the biggest Shapley value, and why. "
      "Then, for each feature, list all six arrival orders with the bump it adds on arrival, average them, "
      "and check that the three Shapley values add up to v(all) minus v(none). "
      "Finally, zip code has a positive share: tell me what that number does not tell me about the world.")
beats.append(beat("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT + " "
    "Two things to look for. Is every bump read off the eight values of v, and none made up mid-table? "
    "And did it call zip code's share a fact about the model, not a cause in the world?",
    remotion("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "INFO 7375 · YOUR TURN", "segment": "Split Your Own Prediction",
        "command": YT, "runningText": "paste this into Claude…",
        "output": ["Check: every bump is read off the eight v(S) values, none made up mid-table.",
                   "Check: it called zip code's share a fact about the model, not the world."],
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
    "audience": "INFO 7375 students reading chapter 5, and anyone who has read a SHAP bar chart and taken one bar as 'the' contribution",
    "course": "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University",
    "source_doc": "chapters/05-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md, §'The mathematics of Shapley values' (value function, marginal contribution, Shapley value, Efficiency) and §'A worked example' (Figures 5.2–5.4, HEAD side); exercises W4, W5; section S1 of youtube/tldr-sections-05-explainability.md",
    "sections": [{"n": 1, "title": TITLE, "key_case": "one loan applicant: f̂(x) = 0.72, E[f̂] = 0.55, payout 0.17; income's six orderings +0.08 +0.08 +0.07 +0.09 +0.06 +0.06 → φ = 0.073; φ_debt 0.062, φ_zip 0.035; Efficiency 0.17 — the chapter's constructed ('Suppose') example, captioned so"}],
    "greeting_language": "Filipino (Kumusta)",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "outro_policy": "OUTRO-LOCK §Voice: spoken title + 'At Nik Bear Brown', 1.0 s silent tail padded into the mp3, no jingle.",
    "bookloop_policy": "Course film: carries the INFO 7375 course credit (spoken in B00, on the cards' course line).",
    "tags": ["Shapley values", "SHAP", "explainability", "feature attribution", "efficiency axiom", "INFO 7375", "computational skepticism", "3Blue1Brown style", "Claude", "Nik Bear Brown"]},
    "beats": beats}
out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"{len(beats)} beats → {out}")
for b in beats: print(b["beat_id"], len(b["narration_text"].split()), "words")
