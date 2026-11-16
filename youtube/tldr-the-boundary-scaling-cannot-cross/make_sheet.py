#!/usr/bin/env python3
"""make_sheet.py — writes beat_sheet.json for tldr-the-boundary-scaling-cannot-cross.

tldr skill (brutalist.art/skills/make/tldr). Section S1 of chapter 13
(youtube/tldr-sections-13-limits-of-ai.md): the data-world gap is categorical,
not frequent — every enlargement of the sample is still a region with an edge,
and the edge is where the gap lives (Figure 13.1, "scaling moves the boundary of
the sample; it never removes it", rebuilt from its caption — the PNG is not in
images/). Key case: Taleb's turkey (1,000 fed mornings, confidence rising
monotonically, day 1,001 Thanksgiving) and the chapter's transfer ("ten thousand
routine cases with 99.7% accuracy may still be a turkey"). No equation lands
(complementarity is stated in words), so there is no TANGENT.

Numbers: only the chapter's (1,000 · 1,001 · 10,000 · 99.7% · 94% · three
patients · six months · 1748) and values recomputed from them below. Regions and
the confidence curve are schematic (captioned). The 94% / three-patient clinic is
the chapter's labelled COMPOSITE — captioned on screen in B18. The two [verify]
flags (Irreducibly Human dependency; calibration ranges) stay out.

After ANY re-run of this file, run lock_cards.py (it restores the audio lock).
"""
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent

SLUG = "tldr-the-boundary-scaling-cannot-cross"
TITLE = "The Boundary Scaling Cannot Cross"
COURSE = "INFO 7375 · Computational Skepticism · Chapter 13"

# ── the chapter's numbers, and what is recomputed from them (FACTCHECK.md) ──
FED_DAYS, EVENT_DAY = 1000, 1001
assert EVENT_DAY == FED_DAYS + 1
TURKEY_GAP = Fraction(1, EVENT_DAY)                     # one morning in 1,001
assert float(TURKEY_GAP) < 0.001                        # "under a tenth of a percent" (0.0999%)
CASES, ACC = 10_000, Fraction(997, 1000)                # "ten thousand routine cases with 99.7% accuracy"
assert CASES * (1 - ACC) == 30                          # 30 misses inside the sample (not spoken; FACTCHECK row)
CLINIC_ACC, HARMED, MONTHS = 94, 3, 6                   # the chapter's composite opener
HUME_YEAR = 1748

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

B00_N = ("Aloha. This is Liam, in for Bear, with chapter thirteen of INFO 7375, Computational Skepticism for AI, at Northeastern. "
         "This film is about why more data can't make a model safe everywhere. "
         "Data covers a region of the world, and every region has an edge. "
         "You'll watch the sample grow and the edge move, and never vanish. "
         "The trap: treating the gap as an amount that shrinks.")
B00_EST = round(len(B00_N.split()) / 2.5, 1)
beats.append(beat("B00", "tldr · what", B00_N,
    remotion("ClaudeTldrWhat", {
        "eyebrow": "TL;DR", "heading": "What This Film Is About", "greeting": "Aloha, Liam", "topic": COURSE,
        "question": "If more data makes a model better, why can't enough data make it safe?",
        "lines": ["Data covers a region of the world, and every region has an edge.",
                  "You will watch the sample grow and the edge move — and never vanish.",
                  "The trap: treating the gap as an amount that shrinks. It is a place: past the edge."],
        "cues": [round(B00_EST * f, 1) for f in (0.05, 0.55, 0.72, 0.86)], "durationSeconds": B00_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "'TL;DR.' wordmark; 'Aloha, Liam'; the course line; heading"},
         {"at": 0.05, "event": "the question writes on"},
         {"at": 0.55, "event": "line 1 lands on 'data covers a region'"},
         {"at": 0.72, "event": "line 2 lands on 'you'll watch'"},
         {"at": 0.86, "event": "line 3 lands on 'the trap'"}]),
    lane="bookend"))

B01_N = ("Why should you care? Every validation number you report was measured inside the sample's edge. "
         "Read ninety-nine point seven percent as a fact about the world, and you'll miss the case that matters. "
         "Know where the edge is, and you know which cases need a human. "
         "That is the supervisor's job, and no amount of scaling does it for you.")
B01_EST = round(len(B01_N.split()) / 2.5, 1)
beats.append(beat("B01", "tldr · why", B01_N,
    remotion("ClaudeTldrWhy", {
        "eyebrow": "TL;DR", "heading": "Why You Should Care", "topic": COURSE,
        "lead": "Every validation number you report was measured inside the sample's edge.",
        "lines": ["Read 99.7% as a fact about the world, and you will miss the case that matters.",
                  "Know where the edge is, and you know which cases need a human.",
                  "That is the supervisor's job — and no amount of scaling does it for you."],
        "cues": [round(B01_EST * f, 1) for f in (0.05, 0.3, 0.6, 0.8)], "durationSeconds": B01_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "page turn: same header, heading 'Why You Should Care'"},
         {"at": 0.05, "event": "the stake writes on"},
         {"at": 0.3, "event": "dash 1 on 'read ninety-nine point seven'"},
         {"at": 0.6, "event": "dash 2 on 'know where the edge is'"},
         {"at": 0.8, "event": "dash 3 on 'that is the supervisor's job'"}]),
    lane="bookend", qc={"sparse_by_design": True, "sparse_reason": "TL;DR card two — text lands on cues by design."}))

beats.append(beat("B02", "the question",
    "The real question: can enough data cross its own edge? Not close the gap. "
    "Closing sounds like an amount, a hole you fill. An edge is a place: wherever the data stopped.",
    remotion("BrutalistHesitantWriter", {
        "text": "Can enough data\nclose the gap?",
        "triggerWords": "close the gap", "replacementWords": "cross its own edge",
        "fontSize": 78, "charMs": 22, "hesitateBetween": 5, "hesitateWithin": 1, "mistakeRate": 0, "jitter": 20,
        "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'Can enough data'"},
         {"at": 0.25, "event": "types 'close the gap?'; backspaces it → 'cross its own edge' on the spoken correction"},
         {"at": 0.6, "event": "caret holds on the corrected question"}]),
    lane="bookend", lead_silence_s=0.8,
    motion_claim="The writer types the naive quantity question and corrects the phrase that makes it the wrong question.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}))

B03_N = ("Three terms. A sample: the cases a model learned from, a part of the world, never all of it. "
         "In-distribution: a new case that looks like the cases in the sample. "
         "And distribution shift: when the cases a system meets stop looking like its sample.")
B03_EST = round(len(B03_N.split()) / 2.5, 1)
beats.append(beat("B03", "terms", B03_N,
    remotion("ClaudeDefinitions", {
        "title": "Terms In This Film",
        "terms": [{"term": "sample", "meaning": "the cases a model learned from: a part of the world, never all of it"},
                  {"term": "in-distribution", "meaning": "a new case that looks like the cases in the sample"},
                  {"term": "distribution shift", "meaning": "when the cases a system meets stop looking like its sample"}],
        "durationSeconds": B03_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'sample' lands, terracotta"}, {"at": 0.45, "event": "'in-distribution' lands; first settles"},
         {"at": 0.72, "event": "'distribution shift' lands"}]),
    lane="bookend", proof="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: prerequisites only — the data-world gap (the film's answer) is earned in B17."}))

# ── LEARN section 1 (B10–B19) ────────────────────────────────────────────────
beats.append(beat("B10", "learn 1",
    "A turkey is fed every morning for a thousand days. Each morning is evidence that the human cares about it, and its confidence climbs. "
    "It never once dips. Day one thousand is the most confident it has ever been. "
    "Day one thousand and one is Thanksgiving. So here's the puzzle: would more days of data have saved it?",
    manim("B10_BestDay",
          "Left: axes 'day 0 · 500 · 1,000' and 'confidence' (no scale); an ink dot rides a monotonically rising curve from day 0 to 1,000. "
          "A dashed 'day 1,001' line appears just past the axis with a terracotta dot. Right: the puzzle — 'Would more days of data have saved it?' — and three short facts.",
          [{"at": 0.05, "event": "axes draw; the dot starts riding the curve"}, {"at": 0.3, "event": "'never dips'; the curve reaches day 1,000"},
           {"at": 0.7, "event": "dashed day-1,001 line, terracotta dot"}, {"at": 0.85, "event": "the puzzle lands"}],
          "The key case, unsolved: confidence highest on the last safe day."),
    role="HOOK", section=1,
    learn={"question": "The turkey's evidence was never wrong for a thousand days. Why did it fail?",
           "action": "Ride the confidence curve day by day to 1,000, then mark day 1,001.",
           "observation": "Confidence rises every day and peaks on the last safe morning.",
           "inference": "More days made the turkey more confident, not safer.",
           "next_question": "Would more data have saved it? What does 'more data' do to a sample?"}))

beats.append(beat("B11", "learn 1",
    "Now a system instead of a turkey. It's tested on ten thousand routine cases, and it gets ninety-nine point seven percent of them right. "
    "Draw those cases as a region: that's the sample. "
    "Draw everything the system could meet once it's deployed as a bigger region around it: that's the world. "
    "And notice: the sample has an edge.",
    manim("B11_TheSample",
          "The turkey panel clears. Left: '10,000 routine cases', '99.7% right'. Right: the WORLD (dim outline, 'the world') draws; the SAMPLE — an ink-edged region with dim case-dots — grows inside it; 'sample' labels it; a terracotta dot sits on its edge.",
          [{"at": 0.05, "event": "the two facts land"}, {"at": 0.35, "event": "the sample grows, case-dots inside"},
           {"at": 0.6, "event": "the world draws around it"}, {"at": 0.85, "event": "dot on the edge"}],
          "First instance: a real validation number drawn as a region with an edge."),
    role="INSTANCE", section=1,
    learn={"question": "What does a validation number cover?",
           "action": "Draw the tested cases as a region inside the region of everything deployment could bring.",
           "observation": "The sample is a region; the world is bigger; the sample has an edge.",
           "inference": "99.7% is a fact about the inside of that region.",
           "next_question": "What happens to the edge when we add data?"}))

beats.append(beat("B12", "learn 1",
    "Add more data. The sample grows, and its edge moves out. Add more again. It moves out again. "
    "Each time, the part of the world the data never reached gets smaller. "
    "And each time, look where the edge is: still there, just further out.",
    manim("B12_MoreData",
          "The sample grows twice (more case-dots each time); the edge travels outward. Left: a bar per enlargement for 'not yet reached' — three ink bars, each shorter. A terracotta dot rides the new edge.",
          [{"at": 0.05, "event": "enlargement 1: edge moves out; bar 2"}, {"at": 0.35, "event": "enlargement 2: edge moves out again; bar 3"},
           {"at": 0.65, "event": "'not yet reached' shrinks"}, {"at": 0.85, "event": "dot on the edge: still there"}],
          "Second instance, one parameter varied (sample size), shown moving: the edge persists."),
    role="INSTANCE", section=1,
    learn={"question": "What does more data do?",
           "action": "Enlarge the sample twice.",
           "observation": "The uncovered part shrinks; the edge moves out and is still there.",
           "inference": "Scaling moves the edge.",
           "next_question": "Keep going — does the gap shrink to nothing?"}))

beats.append(beat("B13", "learn 1",
    "Here's the obvious conclusion, and a serious critic makes it. The gap is shrinking. Keep scaling, and it shrinks to nothing, so the limit is only a frequency. "
    "But the turkey's gap was one morning in a thousand and one: under a tenth of a percent. "
    "Tiny, and it was the only morning that mattered. Measuring how much is uncovered was the wrong measurement.",
    manim("B13_ScaleItEnough",
          "Left: the critic's line — 'scale it enough, and / the gap shrinks to nothing?' — and a dim dashed extrapolation through the three bar tops down to zero at 'enough'. Then 'turkey: 1 morning in 1,001' and 'under 0.1% — and it mattered'; a terracotta X beside the extrapolation's zero.",
          [{"at": 0.1, "event": "the critic's line"}, {"at": 0.3, "event": "the dashed trend runs to zero"},
           {"at": 0.6, "event": "turkey: 1 morning in 1,001"}, {"at": 0.85, "event": "X beside 'shrinks to nothing'"}],
          "The natural wrong turn — the functionalist's frequency argument — walked to where it breaks."),
    role="NAIVE", section=1,
    learn={"question": "If the uncovered part keeps shrinking, doesn't the limit vanish?",
           "action": "Extrapolate the shrinking bars to zero; then measure the turkey's gap the same way.",
           "observation": "The turkey's gap was under a tenth of a percent and it was the whole story.",
           "inference": "The size of the uncovered part is the wrong measurement.",
           "next_question": "If not how much, then what?"}))

beats.append(beat("B14", "learn 1",
    "So stop measuring how much. Look at where. The sample is everything the data reached. The excluded part is everything it didn't. "
    "Grow one, and the other shrinks by exactly that much: they're complementary, two sides of one line. "
    "And that line, the edge, is defined by where the data stopped. The gap doesn't live in the middle. It lives at the edge.",
    manim("B14_WatchTheEdge",
          "Left: three rows — 'sample: what the data reached', 'excluded: what it did not', 'edge: where the data stopped' — then bold 'the gap lives at the edge'. Right: 'excluded' labels the ring; the sample grows once more while the ring shrinks; a terracotta dot rides the edge.",
          [{"at": 0.1, "event": "'sample' row; 'excluded' labels the ring"}, {"at": 0.35, "event": "grow: the ring shrinks by what the sample gained"},
           {"at": 0.6, "event": "'edge: where the data stopped'"}, {"at": 0.85, "event": "'the gap lives at the edge'"}],
          "The representation: sample and excluded region as complements; the edge is the object."),
    role="SHIFT", section=1,
    learn={"question": "Where is the gap, if not an amount?",
           "action": "Label the excluded ring and grow the sample once more.",
           "observation": "Sample and excluded trade exactly; the edge travels with both.",
           "inference": "The edge is defined by where the data stopped; the gap lives there.",
           "next_question": "Where would the turkey's day 1,001 sit in this picture?"}))

beats.append(beat("B15", "learn 1",
    "Before it moves, commit. Put the turkey's thousand mornings into this picture: every fed morning is a case in its sample. "
    "Where does day one thousand and one land, inside or outside? "
    "And if we added more fed mornings, would that move it in?",
    manim("B15_Commit",
          "The turkey curve returns left with its day-1,001 marker (terracotta dot); the right panel holds the world with the generic sample ghosted; an ink pointer runs from the curve to the world; 'inside or outside?' lands; everything holds.",
          [{"at": 0.1, "event": "turkey curve back; the generic sample ghosts"}, {"at": 0.4, "event": "pointer: the mornings are going in"},
           {"at": 0.6, "event": "'inside or outside?'"}, {"at": 0.8, "event": "HOLD — nothing moves on 'commit'"}],
          "The predict-before-reveal beat."),
    role="INSTANCE", section=1, predict=True,
    learn={"question": "Where does day 1,001 land among the turkey's mornings?",
           "action": "Hold the picture; name the move.",
           "observation": "The viewer commits: inside or outside, and whether more mornings help.",
           "inference": "A prediction makes the move evidence.",
           "next_question": "Move them."}))

beats.append(beat("B16", "learn 1",
    "Watch. Every fed morning lands inside. The last one is the edge. Day one thousand and one lands outside. "
    "Now add more fed mornings. The edge moves, along the routine. The event doesn't come in. "
    "More mornings like these can't contain the morning that wasn't one.",
    manim("B16_MorningsMoveIn",
          "The turkey curve's day-dots fly into the world panel and settle into a long, flat sample — 'fed mornings' — wrapped by an ink edge; the terracotta day-1,001 dot flies to a spot above it, outside. Then the sample stretches along the routine (more dots at both ends): the edge moves; the event stays out. 'more fed mornings' · 'still outside'.",
          [{"at": 0.05, "event": "the mornings fly in; the edge wraps them"}, {"at": 0.3, "event": "day 1,001 lands outside"},
           {"at": 0.5, "event": "more fed mornings: the sample stretches"}, {"at": 0.8, "event": "'still outside'"}],
          "The aha: the turkey's curve IS a sample with an edge; enlarging it along the routine never reaches the event."),
    role="TRANSFORM", section=1,
    learn={"question": "Do more fed mornings move day 1,001 inside?",
           "action": "Pour the curve's mornings into the world; stretch the sample with more of them.",
           "observation": "The edge moves along the routine; the event stays outside.",
           "inference": "A sample of fed mornings cannot contain the morning that was not a feeding — the exclusion is what made it a sample.",
           "next_question": "Say it as a rule."}))

beats.append(beat("B17", "learn 1",
    "This thing we keep pointing at deserves its name: the data-world gap. "
    "The parts of the world not in the data are not learnable from the data. Not because the data is small, but because the sample and what it excluded are complementary by construction. "
    "Scaling moves the edge. It never removes it. "
    "David Hume made the underlying point in seventeen forty-eight: you can't justify expecting the unseen to resemble the seen by pointing at the seen.",
    manim("B17_NameIt",
          "Left: 'the data-world gap' lands bold with a terracotta dot beside it; under it 'not in the data →' / 'not learnable from the data'; then 'scaling moves the edge; it never removes it'; then dim 'after Hume (1748), Enquiry §IV'. Right: the turkey world holds with 'sample' and 'excluded' labels; the edge is retraced.",
          [{"at": 0.1, "event": "the name lands"}, {"at": 0.3, "event": "the statement, two lines"},
           {"at": 0.55, "event": "'complementary by construction'; the edge retraced"}, {"at": 0.85, "event": "after Hume (1748)"}],
          "The abstraction arrives as the name for what was watched."),
    role="ABSTRACTION", section=1,
    learn={"question": "What is the rule?",
           "action": "Name the gap; state it in the chapter's words beside the picture.",
           "observation": "Sample and excluded are complements; the edge is defined by the exclusion.",
           "inference": "No enlargement crosses a boundary defined by what the enlargement did not reach.",
           "next_question": "Does the same shape explain a real validation?"}))

beats.append(beat("B18", "learn 1",
    "Same shape, higher stakes. The chapter opens on a composite case, not a single incident: a clinical system at ninety-four percent accuracy, every threshold met, "
    "and within six months of going live, three patients harmed. "
    "The ninety-four percent was real, over the question the data could answer. The three patients were in a region the data could not reach. "
    "In distribution, accuracy holds. At the edge, it says nothing.",
    manim("B18_NinetyFour",
          "Right: the turkey sample morphs into a clinic's sample with '94%' inside; three ink dots appear outside the edge; '3 harmed' with a terracotta dot beside. Left: 'tested: does this match the data?' / 'harmed: what is going on with this patient?'. Caption: 'a composite, not one incident'.",
          [{"at": 0.1, "event": "the sample morphs; caption 'a composite'"}, {"at": 0.3, "event": "94% inside"},
           {"at": 0.55, "event": "three dots outside the edge; '3 harmed'"}, {"at": 0.8, "event": "the two questions"}],
          "Post-shift instance: a real validation number read on the new representation."),
    role="INSTANCE", section=1,
    learn={"question": "Does the edge explain a validated system that harmed people?",
           "action": "Put the 94% inside the sample and the three harms outside it.",
           "observation": "The accuracy and the harms sit on opposite sides of the edge.",
           "inference": "Accuracy is a fact about the inside; the edge is where the supervisor must look.",
           "next_question": "Back to the turkey: would more data have saved it?"}))

beats.append(beat("B19", "learn 1",
    "Back to the turkey. Would more days of data have saved it? More fed mornings raise the curve and move the edge. They never carry it across. "
    "Its confidence peaked on the last safe day, because confidence is measured inside the edge. "
    "The question that saves it isn't how much data. It's whether tomorrow is inside. Watching for that shift, and overriding when a case lands outside, is the supervisor's job. "
    "Not taught here: meaning and intentionality, which ride on this same gap.",
    manim("B19_Tomorrow",
          "The HOOK's turkey curve returns left with the day-1,001 marker; right: the turkey's sample and the event outside. 'more data: the edge moves' and 'never across' land; 'is tomorrow inside?' lands bold; a terracotta dot on the event; dim caption 'not taught here: meaning, intent'.",
          [{"at": 0.05, "event": "the HOOK's curve and the turkey world"}, {"at": 0.3, "event": "sample stretches once more; the event stays out"},
           {"at": 0.6, "event": "'is tomorrow inside?'"}, {"at": 0.9, "event": "boundary caption"}],
          "The HOOK's curve resolved: the question is location, not quantity."),
    role="PAYOFF", section=1,
    learn={"question": "Would more days of data have saved the turkey?",
           "action": "Return to the curve and the day-1,001 marker with the sample picture beside it.",
           "observation": "More mornings raise the curve and move the edge, never across.",
           "inference": "The saving question is whether a case is inside the edge — the supervisor's check.",
           "next_question": ""}))

beats.append(beat("BVDT", "verdict",
    "Let's recap with Claude. Data covers a region of the world: the sample. Every sample has an edge. "
    "More data moves the edge outward. It never removes it, because the sample and what it excluded are complementary by construction. "
    "What the data excluded isn't learnable from the data. So accuracy is a fact about inside the edge, "
    "and whether a case is inside is the supervisor's call.",
    remotion("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": TITLE,
        "artifactLines": ["Data covers a region of the world — the sample — and every sample has an edge.",
                          "More data moves the edge outward. It never removes it: sample and excluded are complementary by construction.",
                          "What the data excluded is not learnable from the data.",
                          "Accuracy is a fact about inside the edge; whether a case is inside is the supervisor's call."]},
        [{"at": 0.0, "event": "artifact page opens"}, {"at": 0.2, "event": "four verdict lines land"}]),
    lane="bookend", lead_silence_s=0.5, qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}))

YT = ("Two systems each score 99.7% on ten thousand routine test cases. One predicts how long employees take to walk to work. "
      "The other predicts the losses on financial returns. "
      "Before explaining anything, predict for each: are the cases it has not seen drawn from Mediocristan, where outliers do not dominate, or Extremistan, where one case can outweigh all the rest? "
      "Then describe each sample and its edge, and name one case that would sit past that edge. "
      "Finally, explain why adding more routine cases cannot move that case inside.")
beats.append(beat("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT + " "
    "Two things to look for. Did it predict before it explained? If it jumped to the answer, send it back. "
    "And in the last part, does it argue from where the edge is, or does it just say the model needs more data?",
    remotion("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "INFO 7375 · YOUR TURN", "segment": "Find The Edge",
        "command": YT, "runningText": "paste this into Claude…",
        "output": ["Check: the prediction came before the explanation.",
                   "Check: it argued from the edge, not from 'more data'."],
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
    "audience": "INFO 7375 students about to sign off a validation, and anyone who has heard 'it just needs more data'",
    "course": "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University",
    "source_doc": "chapters/13-the-limits-of-ai-what-the-tools-cannot-do.md — §'Three categorical limits' (the functionalist objection, the Hume argument, Figure 13.1 caption, Limit 3, Mediocristan/Extremistan, Taleb's turkey, the 99.7% transfer); §'Skepticism as safety mechanism' (94% and three patients); the composite opener; Exercise 3b; section S1 of youtube/tldr-sections-13-limits-of-ai.md",
    "sections": [{"n": 1, "title": TITLE, "key_case": "Taleb's turkey — 1,000 fed mornings, confidence rising monotonically, day 1,001 Thanksgiving; the chapter's transfer: 10,000 routine cases at 99.7% may still be a turkey"}],
    "greeting_language": "Hawaiian (Aloha)",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "outro_policy": "OUTRO-LOCK §Voice: spoken title + 'At Nik Bear Brown', 1.0 s silent tail padded into the mp3, no jingle.",
    "bookloop_policy": "Course film: carries the INFO 7375 course credit (spoken in B00, on the cards' course line).",
    "tags": ["data-world gap", "distribution shift", "Taleb's turkey", "Hume", "induction", "limits of AI", "INFO 7375", "3Blue1Brown style", "Claude", "Nik Bear Brown"]},
    "beats": beats}
out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"{len(beats)} beats → {out}")
