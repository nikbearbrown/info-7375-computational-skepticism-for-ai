#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-induction-until-it-changes.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the Claude palette,
labels only, Liam's voice explains. A COURSE film, Film 2 of SHOW-TELL-THREE-MOVES.md (Bear, 2026-09-27:
"Talk about induction and Hume ... Don't say induction isn't useful. It's very useful. When induction doesn't
hold up, it's because the system has changed"). It carries the INFO 7375 credit (spoken in BIDEA; on screen in
the BDEFS title and the BHTF composer topic). Not a numbered lecture, so it never says "Lecture N".
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Source: chapters/01-the-skeptics-toolkit.md lines 33-97 (SOURCE.md, verbatim) + Bear's words (SOURCE.md),
fact-checked against primaries fetched raw (sources/): Hume, An Enquiry Concerning Human Understanding (1748),
Sections IV-V (Project Gutenberg #9662, Selby-Bigge ed.); US Census Bureau Quarterly Retail E-Commerce Sales
releases (1Q2010, 4Q2019, 1Q2020, 2Q2020) and the Census series as currently revised (FRED ECOMPCTSA);
NIST/SEMATECH e-Handbook 6.4.4.2 (stationarity); Wikipedia "Ergodic process" / "Ergodicity" (definition only).
Cast: the SUN over a horizon and a kraft CALENDAR stack of days (Hume); the HISTORY LINE of online share on a
chart with a kraft PARCEL beside it (the Census data); the quarter STEPS as small grey bars; kraft SHOPS with
grey bars (ergodic); the SYSTEM, a kraft machine with a lever that drops step blocks; a dark MODEL block.
Respellings (audio only; build_srt.py maps them back): "Konnee-cheewa" (Konnichiwa),
"INFO seventy-three seventy-five" (INFO 7375).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Induction Works Until the World Changes"
COURSE = "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.8, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "The move comes from David Hume, in An Enquiry Concerning Human Understanding, from seventeen forty-eight. "
      "The sun has risen every morning of your life. Does that prove it will rise tomorrow? Hume said no. "
      "That the sun won't rise tomorrow is no contradiction. You can picture it. The past gives no logical guarantee.",
      "B00_Sun", "A horizon ('Hume's Enquiry, 1748'); the terracotta sun rises and white day pages land one by one on a calendar "
      "stack on a dark plinth; the sun sets, and tomorrow is only a pale ghost page and a pale ghost sun at the horizon ('tomorrow?').",
      [{"at": 0.1, "event": "the horizon and 'Hume's Enquiry, 1748'"}, {"at": 0.4, "event": "the sun rises; day pages stack up"},
       {"at": 0.75, "event": "tomorrow: a ghost page and a ghost sun"}]),
 beat("B01", "But Hume didn't say stop. Only a fool or a madman, he wrote, would dispute the authority of experience. "
      "We can't prove the future will resemble the past, and we live by it anyway. He called that custom: the great guide of human life.",
      "B01_Custom", "The calendar stack stays; tomorrow's ghost page turns solid, plan lines write onto it and an ink check lands "
      "('custom'); the ghost sun stays at the horizon.",
      [{"at": 0.15, "event": "the stack of days"}, {"at": 0.5, "event": "tomorrow's page turns solid: we act on it"},
       {"at": 0.85, "event": "'custom': the plan gets a check"}]),
 beat("B02", "And most of the time, induction works. For ten years, online shopping's share of U.S. retail sales climbed slowly and steadily: "
      "from about four percent in twenty ten to about eleven percent at the end of twenty nineteen, per the U.S. Census Bureau. "
      "Extend the line one more quarter, and you'd land close, quarter after quarter.",
      "B02_History", "A kraft parcel at the left ('online share'); an ink history line draws quarter by quarter from 4% (2010) to 11% "
      "(2019) on a chart; grey forecast bands, the average step carried forward, lie along the line at three points: the next quarters land inside them.",
      [{"at": 0.15, "event": "the parcel and the chart"}, {"at": 0.5, "event": "the line draws 2010 to 2019, 4% to 11%"},
       {"at": 0.85, "event": "the one-quarter-ahead forecast lands close"}]),
 beat("B03", "Notice what held. Not the number: it kept rising. The rules held. Each quarter added a small step, never more than half a point. "
      "A process whose statistical rules don't change over time is called stationary. These steps were close to it, "
      "and that's what induction quietly relies on.",
      "B03_Steps", "The chart lifts to the top; under it, each quarter's rise drops out as a small grey bar, 39 in a row, "
      "all about the same height ('each step'); a level line runs along their tops ('stationary').",
      [{"at": 0.15, "event": "the line lifts"}, {"at": 0.45, "event": "the steps drop out as small bars"},
       {"at": 0.75, "event": "a level line: stationary"}]),
 beat("B04", "Ergodic is the other half. In an ergodic system, following one shop over a long stretch of time gives the same average "
      "as looking across all the shops at once. That's what lets one history stand in for the whole.",
      "B04_Shops", "Left: one kraft shop and a row of its grey bars over time ('over time'); right: six kraft shops, one bar each "
      "('across shops'); one ink average line draws across both at the same height, meeting at a terracotta dot.",
      [{"at": 0.2, "event": "one shop over time"}, {"at": 0.45, "event": "many shops at once"},
       {"at": 0.8, "event": "the same average line runs through both"}]),
 beat("B05", "Then, in the spring of twenty twenty, COVID changed how people buy. Stores closed or cut back, and shopping moved online. "
      "In a single quarter, online's share jumped from about twelve percent to about sixteen, per the Census Bureau. "
      "A decade of small steps, then one giant one.",
      "B05_Break", "Back on the chart: parcels pile up beside it; the old line carried forward (a grey band) ends near 12%, but the real "
      "line jumps to about 16% ('2020'); a hero '12% → 16%' lands with 'per the Census Bureau'.",
      [{"at": 0.2, "event": "parcels pile up"}, {"at": 0.5, "event": "the line jumps above the old line carried forward"},
       {"at": 0.8, "event": "'12% → 16%', per the Census Bureau"}]),
 beat("B06", "Nothing was wrong with the math. The system that made the history had changed. "
      "Hume saw that nothing forbids it: the course of nature may change, he wrote, and the past may be no rule for the future.",
      "B06_System", "A kraft machine ('the system') with a lever drops small, equal step blocks onto a belt; the lever flips "
      "('changed'); the next block it drops is huge.",
      [{"at": 0.2, "event": "the system drops equal small steps"}, {"at": 0.55, "event": "the lever flips: changed"},
       {"at": 0.8, "event": "a giant block drops"}]),
 beat("B07", "A model trained on the old history makes the same bet. The chapter calls it a system trained on a stationary past, "
      "shipped into a moving present. After the change, the model is exactly as confident as it was the day before.",
      "B07_Model", "A dark model block reads the history line and extends it with a grey forecast band; beside it a grey confidence bar "
      "stays full ('confidence'); the real line jumps away from the forecast ('model').",
      [{"at": 0.2, "event": "the model reads the history"}, {"at": 0.5, "event": "its forecast extends the old line"},
       {"at": 0.8, "event": "the world jumps; the confidence bar stays full"}]),
 beat("B08", "So keep induction. Most of the time, it's the right bet. The honest rule: trust the pattern while the system that made it "
      "stays the same. When the world changes, go back and check.",
      "B08_Rule", "The system machine with its lever at the old setting and a small history line: an ink check ('trust'); the lever "
      "flips, a terracotta lamp lights on the machine, and a scan line runs back over the history ('check').",
      [{"at": 0.2, "event": "same system: trust (a check)"}, {"at": 0.6, "event": "the lever flips; the lamp lights"},
       {"at": 0.85, "event": "go back and check: a scan over the history"}]),
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
    "Konnee-cheewa. This is Liam, in for Bear, with a short film for INFO seventy-three seventy-five, Computational Skepticism for AI. "
    "You might think a skeptic should throw out induction, since the past can't prove the future. Don't. "
    "Induction is one of the most useful tools you have. The real question is when it breaks.",
    "BrutalistHesitantWriter",
    {"text": "Should skeptics\nthrow out induction?", "triggerWords": "throw out induction", "replacementWords": "ask when induction breaks",
     "fontSize": 72, "charMs": 24, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Should skeptics throw out induction?'"}, {"at": 0.6, "event": "backspaces 'throw out induction' -> 'ask when induction breaks' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (should skeptics throw out induction) and corrects it to the real one (should skeptics ask when induction breaks).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. Induction: expecting the future to resemble the past. Stationary: a process whose statistical rules don't change over time. "
    "And ergodic: one long history speaks for the whole system.",
    "ClaudeDefinitions",
    {"title": "INFO 7375 · Terms In This Film",
     "terms": [{"term": "induction", "meaning": "expecting the future to resemble the past"},
               {"term": "stationary", "meaning": "statistical rules don't change over time"},
               {"term": "ergodic", "meaning": "one long history speaks for the whole"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'induction' lands"}, {"at": 0.4, "event": "'stationary' lands"}, {"at": 0.75, "event": "'ergodic' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here is a pattern my team or model relies on: [describe it]. What process in the world produces this pattern? "
             "What would have to change in that process for the pattern to stop holding? "
             "For each change, name one signal I could watch that would tell me it had happened.")
SPOKEN_PROMPT = YT_PROMPT.replace("[describe it]", "describe it")
CHECKS = ["Check: could each change really happen?",
          "Check: could you watch each signal this week?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Pick one pattern your team or your model relies on, and paste this into Claude: " + SPOKEN_PROMPT + " Then check two things yourself. "
    "Could each change really happen? And could you actually watch each signal, starting this week?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "INFO 7375 COMPUTATIONAL SKEPTICISM · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn isometric scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = set()   # filled in from the local Gate V pre-check (BUILD-LOG)
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
    "caption_policy": "none", "greeting_language": "Japanese (Konnichiwa, voiced from the respelling 'Konnee-cheewa')",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "course": COURSE,
    "audience": "INFO 7375 students (Fall 2026) and anyone who relies on a pattern from the past",
    "bookloop_policy": "Course film (Bear, 2026-09-27, SHOW-TELL-THREE-MOVES.md Film 2): carries the INFO 7375 credit, spoken in BIDEA and on screen in the BDEFS title and the BHTF composer topic; not a numbered lecture. Outro stays OUTRO-LOCK.",
    "source_doc": "info-7375-computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md lines 33-97, 'What I mean by skepticism' (the Hume move), plus Bear's words of 2026-09-27 in youtube/SHOW-TELL-THREE-MOVES.md (SOURCE.md, verbatim)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["computational skepticism", "INFO 7375", "Hume", "problem of induction", "induction", "stationary", "ergodic",
             "distribution shift", "COVID", "e-commerce", "Census Bureau", "forecasting", "AI evaluation", "Claude", "Nik Bear Brown"]},
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
