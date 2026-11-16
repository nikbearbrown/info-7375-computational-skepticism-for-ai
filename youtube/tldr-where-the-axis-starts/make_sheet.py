#!/usr/bin/env python3
"""make_sheet.py — writes beat_sheet.json for tldr-where-the-axis-starts.

tldr skill (brutalist.art/skills/make/tldr). Section S4 of chapter 10
(youtube/tldr-sections-10-visualization.md): Exercise 1 — a bar chart whose y-axis
runs 91%–96%, Model A 92.1%, Model B 94.3%, B's bar "roughly three times" A's.
Exercise 1 is a CONSTRUCTED exercise, not a documented chart: the film captions it
"Exercise 1 · constructed values" on the stage. Every ratio below is recomputed from
the exercise's own three inputs (A, B, the 91 floor) and asserted here and in
scenes.py; FACTCHECK.md carries the rows. After any re-run: python3 lock_cards.py.
"""
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent

SLUG = "tldr-where-the-axis-starts"
TITLE = "Where the Axis Starts"
COURSE = "INFO 7375 · Computational Skepticism · Chapter 10"

# Exercise 1 (chapter 10, Exercises · Warm-up). Exact arithmetic in tenths of a point.
A, B, TOP, FLOOR = F("92.1"), F("94.3"), F(96), F(91)
def looks(f): return (B - f) / (A - f)                     # the height ratio the eye reads on a floor f
assert (A - FLOOR, B - FLOOR) == (F("1.1"), F("3.3"))       # bar heights on the 91 floor
assert looks(FLOOR) == 3                                     # "roughly three times" — exactly 3.0
assert B - A == F("2.2")                                     # the real gap: 2.2 percentage points
assert round(float(looks(0)), 2) == 1.02                     # zero floor: 94.3 / 92.1 = 1.0239
assert looks(F("89.9")) == 2                                 # predict answer: 4.4 / 2.2
assert round(float(looks(80)), 2) == 1.18                    # 14.3 / 12.1 = 1.1818
assert looks(92) == 23                                       # 2.3 / 0.1
assert FLOOR < A < B < TOP                                   # both values sit inside the 91–96 axis
# the floor at which B looks k× A:  f = (kA − B)/(k − 1)
assert (2 * A - B) / (2 - 1) == F("89.9")
# YOUR TURN (Exercise 3): equal bar fractions h on panels floored at 70 / 85 / 60 (top 100): value = floor + h·(100 − floor)
for h in (F(1, 4), F(1, 2), F(3, 4)):
    v = {g: fl + h * (100 - fl) for g, fl in (("A", 70), ("B", 85), ("C", 60))}
    assert v["B"] > v["A"] > v["C"]

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

B00_N = ("Jambo. This is Liam, in for Bear, with chapter ten of INFO 7375, Computational Skepticism for AI, at Northeastern. "
         "This film is about where a bar chart's axis starts. "
         "A bar measures its distance from the floor, not its value, so the floor sets the ratio you see. "
         "You'll watch two accuracies hold still while the floor slides. "
         "The trap: checking every number and never the floor.")
B00_EST = round(len(B00_N.split()) / 2.5, 1)
beats.append(beat("B00", "tldr · what", B00_N,
    remotion("ClaudeTldrWhat", {
        "eyebrow": "TL;DR", "heading": "What This Film Is About", "greeting": "Jambo, Liam", "topic": COURSE,
        "question": "Model B's bar is three times taller than Model A's. Is B three times better?",
        "lines": ["A bar measures its distance from the axis floor, not its value, so the floor sets the ratio you see.",
                  "Watch 92.1% and 94.3% hold still while the floor slides: three times taller, then nearly equal.",
                  "The trap: checking every number on the chart and never checking where the axis starts."],
        "cues": [round(B00_EST * f, 1) for f in (0.05, 0.45, 0.68, 0.86)], "durationSeconds": B00_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "'TL;DR.' wordmark; 'Jambo, Liam'; the course line; heading"},
         {"at": 0.05, "event": "the question writes on"},
         {"at": 0.45, "event": "line 1 lands on 'a bar measures its distance from the floor'"},
         {"at": 0.68, "event": "line 2 lands on 'two accuracies hold still'"},
         {"at": 0.86, "event": "line 3 lands on 'the trap'"}]),
    lane="bookend"))

B01_N = ("Why should you care? An AI will draw your chart and pick the axis floor for you, with no stake in whether the picture is honest. "
         "Miss the floor, and a two-point gain reaches a decision-maker as three times better. "
         "Check it, and you catch the argument before the chart makes it. "
         "And it unlocks the honest use: a raised floor when the range really is narrow.")
B01_EST = round(len(B01_N.split()) / 2.5, 1)
beats.append(beat("B01", "tldr · why", B01_N,
    remotion("ClaudeTldrWhy", {
        "eyebrow": "TL;DR", "heading": "Why You Should Care", "topic": COURSE,
        "lead": "An AI will draw your chart and pick the axis floor for you, with no stake in whether the picture is honest.",
        "lines": ["Miss the floor, and a 2.2-point gain reaches a decision-maker as 'three times better'.",
                  "Check it, and you catch the argument before the chart makes it.",
                  "It unlocks the honest use: a raised floor when the range really is narrow."],
        "cues": [round(B01_EST * f, 1) for f in (0.04, 0.42, 0.63, 0.80)], "durationSeconds": B01_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "page turn: same header, heading 'Why You Should Care'"},
         {"at": 0.04, "event": "the stake writes on"},
         {"at": 0.42, "event": "dash 1 on 'miss the floor'"},
         {"at": 0.63, "event": "dash 2 on 'check it'"},
         {"at": 0.80, "event": "dash 3 on 'the honest use'"}]),
    lane="bookend", qc={"sparse_by_design": True, "sparse_reason": "TL;DR card two — text lands on cues by design."}))

beats.append(beat("B02", "the question",
    "The question this film is really asking: where does the axis start? Not 'is B three times better'. "
    "That question trusts the bars, and the bars can't answer it until you know what they grow from.",
    remotion("BrutalistHesitantWriter", {
        "text": "B's bar is three times A's.\nIs B three times better?",
        "triggerWords": "Is B three times better", "replacementWords": "Where does the axis start",
        "fontSize": 74, "charMs": 22, "hesitateBetween": 5, "hesitateWithin": 1, "mistakeRate": 0, "jitter": 20,
        "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'B's bar is three times A's.'"},
         {"at": 0.3, "event": "types 'Is B three times better?'; backspaces the phrase → 'Where does the axis start?' on the spoken correction"},
         {"at": 0.8, "event": "caret holds on the corrected question"}]),
    lane="bookend", lead_silence_s=0.8,
    motion_claim="The writer types the naive 'three times better' question and corrects the phrase that makes it the wrong question.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}))

B03_N = ("Three terms you'll hear. The axis floor: the value where the vertical axis starts, the bottom edge every bar grows from. "
         "Accuracy: the share of test cases a model gets right, as a percentage. "
         "And a percentage point: the plain gap between two percentages. Ninety-four point three and ninety-two point one are two point two points apart.")
B03_EST = round(len(B03_N.split()) / 2.5, 1)
beats.append(beat("B03", "terms", B03_N,
    remotion("ClaudeDefinitions", {
        "title": "Terms In This Film",
        "terms": [{"term": "axis floor", "meaning": "the value where the vertical axis starts: the bottom edge every bar grows from"},
                  {"term": "accuracy", "meaning": "the share of test cases a model gets right, as a percentage"},
                  {"term": "percentage point", "meaning": "the plain gap between two percentages: 94.3 and 92.1 are 2.2 points apart"}],
        "durationSeconds": B03_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'axis floor' lands, terracotta"}, {"at": 0.45, "event": "'accuracy' lands; first settles"},
         {"at": 0.68, "event": "'percentage point' lands"}]),
    lane="bookend", proof="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: prerequisites only — 'truncated axis' and the visual-ratio law are earned in B17."}))

# ── LEARN section 1 (B10–B19) ────────────────────────────────────────────────
beats.append(beat("B10", "learn 1",
    "A colleague slides a chart across the desk. Two models. Model A: ninety-two point one percent accurate. Model B: ninety-four point three. "
    "The axis runs from ninety-one to ninety-six. Every label on it is correct. "
    "And B's bar stands three times as tall as A's. So is B three times better? Nothing on this chart is false. Something on it is still lying to you.",
    manim("B10_TheChart",
          "The colleague's chart builds: y-axis 91 at the floor, 96 at the top; bar A grows to 92.1%, bar B to 94.3%, each labelled; the right column reads 'looks ×3.0'; the caption 'Exercise 1 · constructed values' sits small at top right; the question 'three times better?' lands with a terracotta dot.",
          [{"at": 0.05, "event": "axis draws; floor 91, top 96"}, {"at": 0.25, "event": "bar A grows to 92.1%, bar B to 94.3%"},
           {"at": 0.55, "event": "'looks ×3.0' lands on 'three times as tall'"}, {"at": 0.8, "event": "'three times better?' with a dot"}],
          "The bars are the persistent objects; the question is unsolved."),
    role="HOOK", section=1,
    learn={"question": "Every label on this chart is true. Is B three times better?",
           "action": "Build the colleague's chart: axis 91–96, bars at 92.1 and 94.3.",
           "observation": "B's bar is three times A's; the printed numbers are 2.2 points apart.",
           "inference": "The picture and the numbers disagree, and neither is a typo.",
           "next_question": "What exactly is the eye measuring?"}))

beats.append(beat("B11", "learn 1",
    "Measure what the eye measures. These bars don't start at zero; they start at ninety-one. "
    "So A's bar is ninety-two point one minus ninety-one: one point one. B's is ninety-four point three minus ninety-one: three point three. "
    "Three point three over one point one is exactly three. The eye isn't wrong about the bars. It's measuring from the floor.",
    manim("B11_MeasureIt",
          "Floor 91 chart holds; a brace grows beside A's bar labelled '92.1 − 91 = 1.1', then beside B's '94.3 − 91 = 3.3'; the right column writes '3.3 ÷ 1.1 = 3'; caption: the eye measures from the floor.",
          [{"at": 0.15, "event": "floor line highlighted, '91' label"}, {"at": 0.35, "event": "brace on A: 1.1"},
           {"at": 0.55, "event": "brace on B: 3.3"}, {"at": 0.75, "event": "'3.3 ÷ 1.1 = 3'"}],
          "The first instance: the bar heights as measured from the floor, shown."),
    role="INSTANCE", section=1,
    learn={"question": "What is the eye measuring?", "action": "Brace each bar from the floor to its top.",
           "observation": "1.1 and 3.3: exactly three to one.", "inference": "A bar's height is value minus floor.",
           "next_question": "What happens if the floor moves and the values don't?"}))

beats.append(beat("B12", "learn 1",
    "Now change one thing: the floor. Slide it down. Ninety. Eighty. Fifty. Zero. "
    "Watch the labels: ninety-two point one and ninety-four point three never move. "
    "The bars grow toward each other until, on a zero floor, B is one point oh two times A. Same data. The picture went from three times to almost nothing.",
    manim("B12_SlideDown",
          "The floor knob on the right rail slides 91 → 0 while the chart's floor label counts down and both bars grow toward equal height; the 'looks ×' readout counts 3.0 → 1.02; the two value labels ride their bar tops unchanged.",
          [{"at": 0.1, "event": "knob starts down: 90, 80"}, {"at": 0.35, "event": "50: bars converging"},
           {"at": 0.55, "event": "0: looks ×1.02"}, {"at": 0.8, "event": "caption: same numbers, new ratio"}],
          "The second instance: one parameter (the floor) varied continuously; the values are invariant."),
    role="INSTANCE", section=1,
    learn={"question": "What if only the floor moves?", "action": "Slide the floor from 91 to 0 with the values fixed.",
           "observation": "The height ratio falls from 3.0 to 1.02; the printed numbers never change.",
           "inference": "The ratio the eye reads belongs to the floor, not to the data.",
           "next_question": "But every number was true. Isn't that enough?"}))

beats.append(beat("B13", "learn 1",
    "Here's the defense you'll hear: every number on the chart is true, so the chart is honest. Check it. "
    "Ninety-two point one: true. Ninety-four point three: true. An axis from ninety-one to ninety-six: true. "
    "Every check passes, and the eye still reads three times. The numbers are true. The ratio the eye reads is not, and nobody printed that ratio.",
    manim("B13_EveryNumberTrue",
          "Back on the floor-91 chart; the right column lists three checks — '92.1% · true', '94.3% · true', 'axis 91 to 96 · true' — each with an ink check mark; then 'the eye reads ×3' with a terracotta X beside it; caption: true labels, false ratio.",
          [{"at": 0.2, "event": "check 1"}, {"at": 0.35, "event": "check 2"}, {"at": 0.5, "event": "check 3"},
           {"at": 0.7, "event": "'the eye reads ×3' with an X"}, {"at": 0.9, "event": "caption"}],
          "The natural defense walked to its limit: every printed fact checks out, the unprinted ratio does not."),
    role="NAIVE", section=1,
    learn={"question": "If every number is true, is the chart honest?", "action": "Audit each printed label.",
           "observation": "All three labels pass; the ×3 the eye reads was never printed.",
           "inference": "A fact-check of the labels cannot catch a ratio the chart only implies.",
           "next_question": "Where does the ×3 come from, mechanically?"}))

beats.append(beat("B14", "learn 1",
    "Here's the reframe. Go back to a zero floor and draw a line across both bars at ninety-one. "
    "Below the line, each bar holds exactly the same ninety-one. Above it, slivers: one point one and three point three. "
    "Now cut. The shared ninety-one drops away, and what's left is stretched to fill the frame. "
    "A truncated axis is a zoom on the slivers. The floor decides where the slivers begin.",
    manim("B14_TheCut",
          "Zero-floor chart; a dashed ink line at 91 crosses both bars; the parts below turn ghost and each is labelled '91'; the slivers above stay ink with '1.1' and '3.3'; then the ghost parts sink away while the slivers stretch to fill the frame and become the floor-91 bars; 'looks ×3.0' returns.",
          [{"at": 0.1, "event": "cut line at 91"}, {"at": 0.3, "event": "ghost '91' below in both bars; slivers 1.1 and 3.3"},
           {"at": 0.6, "event": "the cut: ghost parts drop, slivers stretch"}, {"at": 0.85, "event": "caption: a zoom on the slivers"}],
          "The representation: every bar = a shared part below the floor (thrown away) + a sliver above it (stretched)."),
    role="SHIFT", section=1,
    learn={"question": "Where does the ×3 come from?", "action": "Split each zero-floor bar at 91; discard below, stretch above.",
           "observation": "Both bars lose the same 91; the slivers are 1.1 and 3.3.",
           "inference": "Subtracting the same amount from both hits the smaller bar harder.",
           "next_question": "So where must the floor sit for any ratio you want?"}))

beats.append(beat("B15", "learn 1",
    "Before it moves, commit. The floor sits at ninety-one, and B looks three times A. "
    "Where does the floor have to go for B to look exactly twice A? Up or down? And by how much: a point or two, or tens of points?",
    manim("B15_Predict",
          "The floor-91 chart holds; a dim dashed guide marks twice A's bar height, and B's top sits above it; the readout shows a target '×2 ?'; a dot on the rail knob; caption: commit before it moves.",
          [{"at": 0.15, "event": "the 2 × A guide line"}, {"at": 0.45, "event": "target ×2 ?"}, {"at": 0.7, "event": "HOLD — nothing moves"}],
          "The predict-before-reveal beat."),
    role="INSTANCE", section=1, predict=True,
    learn={"question": "Which way, and how far, for ×2?", "action": "Hold the picture with a twice-A guide.",
           "observation": "The viewer commits.", "inference": "A prediction turns the sweep into evidence.", "next_question": "Sweep."}))

beats.append(beat("B16", "learn 1",
    "Watch. Down to eighty-nine point nine: exactly twice. That's all it took, one point one. Eighty: one point one eight. Zero: one point oh two. "
    "Now up, toward A itself. At ninety-two, B looks twenty-three times A. "
    "The two numbers never moved. One setting the chart-maker picks did all of it.",
    manim("B16_Sweep",
          "One continuous floor sweep through the persistent chart: 91 → 89.9 (looks ×2.0, the guide meets B's top) → 80 (×1.18) → 0 (×1.02) → up to 92 (×23, A's bar a sliver); the value labels 92.1% and 94.3% ride unchanged throughout; 'the numbers never moved' lands.",
          [{"at": 0.0, "event": "floor to 89.9: ×2.0"}, {"at": 0.25, "event": "80: ×1.18; 0: ×1.02"},
           {"at": 0.55, "event": "up to 92: ×23"}, {"at": 0.8, "event": "'the numbers never moved'"}],
          "The aha: one designer-chosen parameter spans ×1.02 to ×23 on the same data; narration short, the sweep gets the seconds."),
    role="TRANSFORM", section=1,
    learn={"question": "How much of the picture does the floor control?", "action": "Sweep the floor 91 → 89.9 → 80 → 0 → 92.",
           "observation": "The same two values read ×2, ×1.18, ×1.02 and ×23.",
           "inference": "The visible ratio is a design choice; the data only fixes the labels.", "next_question": "Say it as a rule."}))

beats.append(beat("B17", "learn 1",
    "This deserves its name: a truncated axis, and here is its rule. "
    "The ratio your eye reads is B minus the floor, over A minus the floor. "
    "The floor sits in both, so it comes off both, and it hits the smaller bar harder. "
    "Floor at zero, you read the true ratio. Raise it, and the ratio grows without limit as the floor closes on A.",
    manim("B17_NameIt",
          "The floor-91 chart holds at left; the right column assembles the rule term by term — looks = (B − floor) / (A − floor) — with a label under each piece (B's bar · A's bar · the same floor twice); 'truncated axis' lands bold; a terracotta dot beside the denominator on 'closes on A'.",
          [{"at": 0.1, "event": "'truncated axis' lands"}, {"at": 0.3, "event": "the rule writes on"},
           {"at": 0.55, "event": "'the same floor, twice'"}, {"at": 0.8, "event": "dot beside A − floor"}],
          "The abstraction arrives as the name for what was watched."),
    role="ABSTRACTION", section=1,
    learn={"question": "What is the rule?", "action": "Write the height ratio in terms of B, A and the floor.",
           "observation": "The floor appears in the numerator and the denominator.",
           "inference": "Raising the floor always inflates the ratio in favour of the larger value.",
           "next_question": "What does each symbol mean, exactly?"}))

beats.append(beat("B18", "learn 1",
    "Read the line. Left: the ratio the eye reads, B's bar over A's bar. Top: B minus the floor, which is B's bar. Bottom: A minus the floor, which is A's bar. "
    "The floor appears twice, the same number both times. That's the whole trick. "
    "Plug in. Floor ninety-one: three point three over one point one, three. Floor zero: ninety-four point three over ninety-two point one, one point oh two. "
    "Floor eighty-nine point nine: four point four over two point two, two. The numbers the sweep showed you.",
    manim("B18_Tangent",
          "Split stage: the rule persists on the left; the right band writes the LHS sentence, the numerator and denominator glosses, 'the same floor twice'; then three worked values land under the rule: 3.3/1.1 = 3, 94.3/92.1 ≈ 1.02, 4.4/2.2 = 2.",
          [{"at": 0.05, "event": "LHS sentence"}, {"at": 0.2, "event": "numerator gloss"}, {"at": 0.32, "event": "denominator gloss"},
           {"at": 0.45, "event": "'the same floor twice'"}, {"at": 0.6, "event": "worked values land one by one"}],
          "The equation tangent: formula, sentence, glossary, worked values."),
    role="TANGENT", section=1,
    learn={"question": "What does each symbol mean?", "action": "Translate both sides; plug in the three floors.",
           "observation": "The rule reproduces 3, 1.02 and 2.", "inference": "The notation describes the sweep.",
           "next_question": "Back to the colleague's chart."}))

beats.append(beat("B19", "learn 1",
    "Back to the colleague's chart. Floor at ninety-one, three times. Now you can read it: B is two point two percentage points higher, and the picture called it three times. "
    "When the question is how much better, drop the floor to zero, or print the gap. "
    "Truncation isn't banned. Stock prices live on raised floors, because zero means nothing there. The pixels look the same either way. The choice is the difference. "
    "Not taught here: side-by-side panels with different floors.",
    manim("B19_Payoff",
          "The HOOK chart returns at floor 91 (looks ×3.0); a brace between the two bar tops reads '+2.2 points'; the floor slides to 0 and the bars settle nearly equal with '+2.2 points' riding; 'the choice is the difference' lands; boundary caption: not taught here: mismatched panels.",
          [{"at": 0.05, "event": "the HOOK chart returns"}, {"at": 0.2, "event": "'+2.2 points' brace"},
           {"at": 0.4, "event": "floor slides to 0"}, {"at": 0.75, "event": "'the choice is the difference'"}, {"at": 0.9, "event": "boundary caption"}],
          "The HOOK's bars resolve; the boundary names the transfer exercise."),
    role="PAYOFF", section=1,
    learn={"question": "So — is B three times better?", "action": "Read the hook chart with the floor in mind; print the gap; drop the floor.",
           "observation": "2.2 points, pictured as ×3.", "inference": "The floor is an argument; state it or remove it.", "next_question": ""}))

beats.append(beat("BVDT", "verdict",
    "Let's recap with Claude. A bar's height is its value minus the axis floor, so the floor is inside every bar. "
    "On a ninety-one floor, ninety-two point one and ninety-four point three look three to one; on a zero floor, one point oh two. The numbers never moved. "
    "The ratio the eye reads is B minus the floor over A minus the floor, and it grows without limit as the floor nears A. "
    "Truncation is honest when the range is narrow or zero means nothing. The pixels can't tell you which. The choice is the difference.",
    remotion("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": TITLE,
        "artifactLines": ["A bar's height is its value minus the axis floor. The floor is inside every bar.",
                          "Floor 91: 92.1% and 94.3% look 3 to 1. Floor 0: 1.02 to 1. The numbers never moved.",
                          "The eye reads (B − floor) / (A − floor), and it grows without limit as the floor nears A.",
                          "Truncation is honest when the range is narrow or zero means nothing. The choice is the difference."]},
        [{"at": 0.0, "event": "artifact page opens"}, {"at": 0.2, "event": "four verdict lines land"}]),
    lane="bookend", lead_silence_s=0.5, qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}))

YT = ("A dashboard shows three subgroup accuracy charts side by side. Group A's y-axis runs from 70 to 100 percent, Group B's from 85 to 100, Group C's from 60 to 100. "
      "A reviewer says the three groups look about the same. "
      "Before computing anything, predict: if each group's bar reaches the same fraction of its own panel, which group's accuracy is actually highest, and which lowest? "
      "Then use the rule that a bar's height is its value minus its axis floor to check your prediction, name the misleading choice, "
      "and describe the single change that would make the comparison valid.")
beats.append(beat("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT + " "
    "Two things to look for. Did it predict before it computed? If it jumped to numbers, send it back. "
    "And is its fix one shared axis for all three panels, not a note in the footer?",
    remotion("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "INFO 7375 · YOUR TURN", "segment": "Three Panels, Three Floors",
        "command": YT, "runningText": "paste this into Claude…",
        "output": ["Check: the prediction came before the arithmetic.",
                   "Check: the fix is one shared axis, not a footnote."],
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
    "audience": "INFO 7375 students reading chapter 10, and anyone who has approved a bar chart because every number on it was right",
    "course": "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University",
    "source_doc": "chapters/10-visualization-under-validation-honest-misleading-and-the-choices-between.md, §'The deceptive visualization catalog' (truncated axes; inconsistent axes across panels), §'Uncertainty has two faces' (where you start the y-axis is a choice), Exercises 1 and 3; section S4 of youtube/tldr-sections-10-visualization.md",
    "sections": [{"n": 1, "title": "Where the Axis Starts", "key_case": "Exercise 1 (constructed): y-axis 91–96, Model A 92.1%, Model B 94.3% — bars 1.1 and 3.3 on the 91 floor (×3.0), 92.1 and 94.3 on a zero floor (×1.02)"}],
    "greeting_language": "Swahili (Jambo)",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "outro_policy": "OUTRO-LOCK §Voice: spoken title + 'At Nik Bear Brown', 1.0 s silent tail padded into the mp3, no jingle.",
    "bookloop_policy": "Course film: carries the INFO 7375 course credit (spoken in B00, on the cards' course line).",
    "tags": ["data visualization", "truncated axis", "misleading charts", "bar charts", "dashboards", "INFO 7375", "computational skepticism", "3Blue1Brown style", "Claude", "Nik Bear Brown"]},
    "beats": beats}
out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"{len(beats)} beats → {out}")
