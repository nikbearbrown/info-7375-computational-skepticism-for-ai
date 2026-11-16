#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-skepticism-is-a-method.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. A COURSE film (Bear, 2026-09-27: "show tell film
Liam persona mention the film is for .../info-7375-computational-skepticism-for-ai"), so it carries
the INFO 7375 credit (spoken in BIDEA; on screen in the BDEFS title and the BHTF composer topic).
It is not a numbered lecture, so it never says "Lecture N".
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Source: chapters/01-the-skeptics-toolkit.md lines 33-97, "What I mean by skepticism" (SOURCE.md, verbatim),
fact-checked against primaries fetched raw (sources/): SEC order 34-70694 (Knight Capital), Lazer et al.,
Science 2014 (Google Flu Trends), Wong et al., JAMA Intern Med 2021 (sepsis model, Europe PMC record).
Cast: the CLAIM (a white page on a dark plinth), the TOOLBOX (kraft open box) holding three kraft MOVE tags
1, 2, 3; kraft CHECK crates (Descartes); eight dark SERVERS (Knight); a kraft TURKEY and a feeding tray, a
confidence curve (Hume); a 108-tile WEEK grid (Google Flu Trends); white SWANS and one black swan (Popper);
three kraft BEDS with alert lamps (the sepsis model); a kraft BEAM on two dark posts with a weight (the close).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Skepticism Is a Method, Not a Mood"
COURSE = "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.8, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Not the eye roll. Not the person who is against everything. A method: a few moves you perform on a claim. They can be taught, and you can see whether someone did them. Three philosophers each donate one move.",
      "B00_Method", "A white claim page on a dark plinth arrives at the right ('claim'); a kraft toolbox drops in at the left ('method'); three kraft move tags, 1, 2, 3, rise out of the toolbox one after another.",
      [{"at": 0.1, "event": "the claim arrives"}, {"at": 0.4, "event": "the toolbox drops in"}, {"at": 0.75, "event": "tags 1, 2, 3 rise"}]),
 beat("B01", "The hard part isn't doubting what looks suspicious. It's doubting what looks right: fluent, specific, neatly formatted. That's when the moves matter most, and when the urge to skip them is strongest. The enemy isn't laziness. It's confidence.",
      "B01_Confidence", "The claim page fills with neat grey lines and an ink check stamps onto it ('looks right'); a grey confidence bar beside it grows segment by segment to full ('confidence'); the three move tags sink back into the toolbox.",
      [{"at": 0.15, "event": "lines, then the check: looks right"}, {"at": 0.45, "event": "the confidence bar fills"}, {"at": 0.7, "event": "the tags sink back: skipped"}]),
 beat("B02", "Move one is from Day-cart. Take the claim and ask: what would have to be true for this to be wrong? The answers aren't a feeling. They're a checklist: the training data, the inputs, the setting it runs in. Each one, you can check.",
      "B02_Doubt", "Tag 1 rises out of the toolbox to the claim ('Descartes'); three kraft crates drop into a row under the claim ('data', 'inputs', 'setting'); an ink check lands on each crate in turn.",
      [{"at": 0.1, "event": "tag 1 goes to the claim"}, {"at": 0.45, "event": "three crates: data, inputs, setting"}, {"at": 0.85, "event": "a check on each"}]),
 beat("B03", "In twenty twelve, the trading firm Knight Capital put new code on eight servers. A technician missed one, and no one noticed. On that eighth server, old code, unused since two thousand three, woke up. In about forty five minutes it made over four million trades, and Knight lost more than four hundred sixty million dollars, per the SEC. Ask what would make done wrong, and you check all eight.",
      "B03_Knight", "Eight dark servers in a row ('8 servers'); a white code page drops onto seven of them and each light turns terracotta; the eighth stays grey ('missed'); then the eighth's light flashes and white order slips pour out of it; a hero '$460M+' lands with 'per the SEC'; ink checks sweep over all eight.",
      [{"at": 0.1, "event": "code drops on seven servers"}, {"at": 0.3, "event": "the eighth is missed"}, {"at": 0.5, "event": "old code wakes; orders pour out"}, {"at": 0.75, "event": "$460M+, per the SEC"}, {"at": 0.9, "event": "check all eight"}]),
 beat("B04", "Move two is from Hume. A model that was right a thousand times has no guarantee about the next time. Picture a turkey, fed every morning for a thousand days. Each meal makes it surer of the next. On day one thousand and one, the farmer comes with an axe.",
      "B04_Turkey", "A kraft turkey beside a feeding tray; a day counter climbs 'day 1' to 'day 1,000' while an ink confidence curve rises ('confidence'); on 'day 1,001' the grain is gone and the curve drops straight down to a terracotta dot.",
      [{"at": 0.2, "event": "the turkey and the tray"}, {"at": 0.45, "event": "days climb; the curve rises"}, {"at": 0.85, "event": "day 1,001: the curve drops"}]),
 beat("B05", "Big systems do it too. Google Flu Trends estimated flu from web searches. From August twenty eleven, it ran too high in one hundred of one hundred and eight weeks, per a paper in Science. A turkey with a spreadsheet. Its confidence belonged to the model, not to the world.",
      "B05_Flu", "A grid of 108 week tiles; 100 of them fill grey, one after another, and 8 stay pale ('weeks too high'); a hero '100 of 108' lands with 'per Science, 2014'; the turkey slides in beside the grid.",
      [{"at": 0.15, "event": "the week grid"}, {"at": 0.4, "event": "100 of 108 fill: too high"}, {"at": 0.75, "event": "the turkey arrives: a turkey with a spreadsheet"}]),
 beat("B06", "Move three is from Popper. A claim that can't be wrong isn't a claim yet. And piling up successes never proves one. No count of white swans proves that all swans are white. One black swan disproves it.",
      "B06_Swans", "Tag 3 goes to the claim ('Popper'); white swans glide in one by one into a row with a count ('white swans'); the claim keeps its check; then one black swan glides in ('black swan') and the check on the claim becomes an ink cross.",
      [{"at": 0.15, "event": "tag 3 to the claim"}, {"at": 0.45, "event": "white swans pile up"}, {"at": 0.85, "event": "one black swan: the check becomes a cross"}]),
 beat("B07", "So hunt for the black swan. A sepsis alert model was running in hundreds of U.S. hospitals without an adequate outside test. When outside researchers ran one, on twenty seven thousand six hundred ninety seven patients, it missed about two of every three sepsis cases.",
      "B07_Sepsis", "Three kraft hospital beds, each with a patient and an alert lamp ('sepsis cases'); a scan line sweeps them ('outside test'); only the first lamp lights terracotta; ink crosses land by the other two ('missed'); a hero '2 of 3' with 'per JAMA Intern Med, 2021'.",
      [{"at": 0.15, "event": "three beds, three lamps"}, {"at": 0.5, "event": "the outside test sweeps"}, {"at": 0.8, "event": "two of three missed"}]),
 beat("B08", "You don't have to believe any of these philosophers. The moves are tools, like a load test on a beam. The test finds a flaw, or it comes back clean. Either way, you've learned something.",
      "B08_Beam", "A kraft beam on two dark posts ('beam'); a dark weight lowers onto it; the beam bows slightly and holds; an ink check lands ('load test'); the toolbox with its three tags sits at the left.",
      [{"at": 0.15, "event": "the beam and posts"}, {"at": 0.45, "event": "the weight lowers: the test"}, {"at": 0.8, "event": "it holds: a check"}]),
]


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.8, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
 remotion("BIDEA", "the question",
    "Hallo. This is Liam, in for Bear, with a short film for INFO seventy-three seventy-five, Computational Skepticism for AI. "
    "You might think skepticism is just doubting everything. That's a mood. Here, skepticism is a method: a set of moves you run on a claim.",
    "BrutalistHesitantWriter",
    {"text": "Is skepticism\njust doubting everything?", "triggerWords": "just doubting everything", "replacementWords": "a set of moves on a claim",
     "fontSize": 72, "charMs": 24, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Is skepticism just doubting everything?'"}, {"at": 0.6, "event": "backspaces 'just doubting everything' -> 'a set of moves on a claim' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (is skepticism just doubting everything) and corrects it to the real one (is skepticism a set of moves on a claim).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. Radical doubt: asking what would make a claim wrong. Induction: trusting a pattern because it held in the past. "
    "And falsifiable: a claim that names the result that would prove it wrong.",
    "ClaudeDefinitions",
    {"title": "INFO 7375 · Terms In This Film",
     "terms": [{"term": "radical doubt", "meaning": "asking what would make a claim wrong"},
               {"term": "induction", "meaning": "trusting a pattern because it held in the past"},
               {"term": "falsifiable", "meaning": "names the result that would prove it wrong"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'radical doubt' lands"}, {"at": 0.4, "event": "'induction' lands"}, {"at": 0.75, "event": "'falsifiable' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here is an AI answer I rely on: [paste it]. Run three moves on it. One: what would have to be true for it to be wrong? "
             "List conditions I can check. Two: what may have changed since the evidence behind it was gathered? "
             "Three: rewrite it as a falsifiable claim that names the result that would prove it false.")
SPOKEN_PROMPT = YT_PROMPT.replace("[paste it]", "paste it")
CHECKS = ["Check: could you actually test each condition?",
          "Check: does the rewrite name what would prove it false?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Take one confident AI answer you rely on, and paste this into Claude: " + SPOKEN_PROMPT + " Then check two things yourself. "
    "Could you actually test each condition? And does the rewrite name a result that would prove it false?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "INFO 7375 COMPUTATIONAL SKEPTICISM · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn isometric scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B04"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160): B04 measures 0.77 at 50-99%; the rest measure 0.34-0.68 at 50% and keep the waiver
for b in B:
    if b["beat_id"] not in FILLS_ON_ITS_OWN:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}
B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "INFO 7375 · COMPUTATIONAL SKEPTICISM", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "course": COURSE,
    "audience": "INFO 7375 students (Fall 2026) and anyone who relies on confident AI output",
    "bookloop_policy": "Course film (Bear, 2026-09-27): carries the INFO 7375 credit, spoken in BIDEA and on screen in the BDEFS title and the BHTF composer topic; not a numbered lecture. Outro stays OUTRO-LOCK.",
    "source_doc": "info-7375-computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md lines 33-97, 'What I mean by skepticism' (SOURCE.md, verbatim; the manuscript carries an unresolved merge conflict around the Knight Capital paragraph, HEAD side used as Bear pasted it)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["computational skepticism", "INFO 7375", "Descartes", "Hume", "Popper", "falsifiability", "problem of induction",
             "radical doubt", "Knight Capital", "Google Flu Trends", "sepsis model", "black swan", "AI evaluation",
             "Claude", "Nik Bear Brown"]},
    "beats": B}

# keep measured audio fields across re-runs (audio-first: never lose the clock)
old = {}
p = HERE / "beat_sheet.json"
if p.exists():
    for ob in json.load(open(p))["beats"]:
        old[ob["beat_id"]] = ob
for b in B:
    ob = old.get(b["beat_id"])
    if ob and ob.get("narration_text") == b["narration_text"]:
        for k in ("actual_duration_s", "audio_file"):
            if k in ob:
                b[k] = ob[k]
        if b["beat_id"] == "BDEFS" and "actual_duration_s" in ob:
            b["shot"]["remotion"]["props"]["durationSeconds"] = ob["actual_duration_s"]
p.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(sum(b.get("actual_duration_s") or b["estimated_duration_s"] for b in B)), "s")
