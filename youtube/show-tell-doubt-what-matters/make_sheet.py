#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-doubt-what-matters.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the Claude palette,
labels only, Liam's voice explains. Film 1 of SHOW-TELL-THREE-MOVES (Bear, 2026-09-27: "Radical doubt. Talk
about Descartes. Talk about how you can't doubt everything, and add risk to that: you should doubt the things
that are important to doubt. You can't doubt everything, but you should doubt what your job depends on —
health, important things."). A COURSE film: the INFO 7375 credit is spoken in BIDEA and shown in the BDEFS
title and the BHTF composer topic; never "Lecture N"; the outro stays OUTRO-LOCK.
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Source: chapters/01-the-skeptics-toolkit.md lines 33-49 + 97 (SOURCE.md, verbatim) and Descartes' own texts
(sources/): Meditations (1641; Latin first edition text + Veitch's English), Discourse on the Method (1637,
Part III, Veitch), Principles of Philosophy (1644, Part I arts. 1-3, Veitch).
Cast: the BELIEF HOUSE (kraft blocks on a dark foundation, Meditations), the doubt LENS (an ink magnifier),
the CLAIM CARDS (white cards on kraft stands), an HOURGLASS (time), the CABIN (the provisional code, Discourse),
the FOREST and a traveller PEG (the forest maxim), the RISK FLOOR (a 3 x 3 isometric grid: chance wrong x
cost if wrong), the CHAIR, the TOWERS (costly claims), and the BALANCE (doubt in proportion to cost).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Doubt What Your Work Depends On"
# On-screen props carry the title WITH its full stop: GATE T §8.9 reads a display string ending in "On" as a
# dangling preposition (truncation). ClaudeTitleOutro strips terminal punctuation and redraws it as its
# terracotta full stop, so the outro renders exactly as without it; bookend_check ignores terminal punctuation.
COURSE = "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.8, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "In his Meditations, published in sixteen forty-one, Day-cart set out, once in his life, to tear down every belief he could find any reason to doubt, and rebuild from the foundations. He says it was safe to go that far because he was after knowledge, not action.",
      "B00_House", "A wall of kraft belief blocks on a dark foundation ('beliefs'); the labels 'Descartes' and 'Meditations, 1641'; cracks appear on every block but one and the cracked blocks lift away, leaving the foundation and one block, which gets a terracotta dot on 'knowledge, not action'.",
      [{"at": 0.1, "event": "the house of beliefs"}, {"at": 0.35, "event": "cracks: any reason to doubt"}, {"at": 0.6, "event": "cracked blocks lift away: tear down"}, {"at": 0.85, "event": "knowledge, not action"}]),
 beat("B01", "This course borrows his move as one question you can ask of any claim: what would have to be true for this to be wrong? The answer isn't a mood. It's a list of things you can go and check.",
      "B01_Lens", "A white claim card on a kraft stand ('claim'); an ink magnifier, the doubt lens, slides over it ('doubt'); a clipboard lands beside it and three rows tick one by one ('checklist').",
      [{"at": 0.15, "event": "the claim card"}, {"at": 0.4, "event": "the lens: what would make it wrong"}, {"at": 0.8, "event": "three rows tick: a list you can check"}]),
 beat("B02", "But you can't run that question on everything. Every check costs time. Doubt every claim you meet, and you never get to act, and the work just waits.",
      "B02_Queue", "A long row of claim cards ('claims'); the lens checks them one at a time, a check over each, while an hourglass drains ('time'); four more cards arrive at the back of the row faster than the lens can check them.",
      [{"at": 0.15, "event": "a row of claims"}, {"at": 0.45, "event": "the lens checks one at a time; the hourglass drains"}, {"at": 0.8, "event": "more keep arriving: the work waits"}]),
 beat("B03", "Day-cart saw this. In his Discourse on the Method, from sixteen thirty-seven, he says that while you pull down your house to rebuild it, you need another house to live in. So while he doubted, he kept a provisional code: a few rules to act by.",
      "B03_Cabin", "The belief house from B00 under rebuilding at the left ('rebuilding'); a small kraft cabin drops in at the right, its window lights ('Discourse, 1637'); three rule pages slide in beside the cabin ('provisional code').",
      [{"at": 0.15, "event": "the house is being rebuilt"}, {"at": 0.5, "event": "another house to live in"}, {"at": 0.85, "event": "a few rules to act by"}]),
 beat("B04", "One rule: a traveler lost in a forest shouldn't wander from side to side, or stand still. Pick a direction and walk straight, and you'll likely end up somewhere better than the middle of the forest. When you can't tell what's true and you have to act, act on what's most probable.",
      "B04_Forest", "An isometric forest of kraft trees with an ink traveller peg in the middle ('lost'); a grey wandering path scribbles and fades; then a straight ink path draws out to the forest edge and the peg walks it to a terracotta dot ('straight on').",
      [{"at": 0.15, "event": "the traveller, lost"}, {"at": 0.35, "event": "wandering side to side"}, {"at": 0.6, "event": "one straight line out"}, {"at": 0.9, "event": "act on the most probable"}]),
 beat("B05", "So aim the doubt. Ask two things about a claim: how likely is it to be wrong, and what would it cost if it were? Together, that's risk. Treat this as a way of thinking, not a measured model.",
      "B05_Grid", "A 3 x 3 isometric floor on a dark plinth; grey axis arrows grow along one edge ('chance wrong') and the other ('cost if wrong'); on 'that's risk' the tiles shade darker toward high chance x high cost; a small label 'not measured'.",
      [{"at": 0.15, "event": "the floor arrives"}, {"at": 0.35, "event": "chance wrong"}, {"at": 0.55, "event": "cost if wrong"}, {"at": 0.9, "event": "not measured"}]),
 beat("B06", "The chair you're sitting on has held you for years, and if it failed, you'd land on the floor. Don't doubt it. Sit down. Most claims in a working day live in this corner: act on them, and fix them if they break.",
      "B06_Chair", "A kraft chair drops onto the low-chance, low-cost corner tile ('chair'); then small kraft claim blocks drop onto the other low tiles ('just act').",
      [{"at": 0.15, "event": "the chair lands in the corner"}, {"at": 0.45, "event": "don't doubt it"}, {"at": 0.75, "event": "most claims land here: just act"}]),
 beat("B07", "A few claims land over here: a triage score on a patient, a medication dose, the number your job depends on. If one of those is wrong, someone pays for it. Those get the doubt.",
      "B07_Towers", "On the high-cost row, three tall dark towers rise one after another ('triage score', 'dose', 'your number'); the doubt lens swings over them ('doubt hard').",
      [{"at": 0.2, "event": "triage score, dose, your number rise"}, {"at": 0.6, "event": "someone pays"}, {"at": 0.85, "event": "the lens goes to them"}]),
 beat("B08", "The rule is proportion. The more it costs to be wrong, the more doubt a claim gets. Cheap to be wrong: act, and watch. Costly to be wrong: stop, and ask what would have to be true for it to be wrong, before the world answers for you.",
      "B08_Balance", "A balance on a grey post: a small kraft cost block on the left pan, one doubt weight on the right, level ('cost if wrong', 'doubt'); the cost block is replaced by a tall dark one and the beam tips; three doubt weights drop onto the right pan and it levels again; the lens comes to the costly block.",
      [{"at": 0.15, "event": "small cost, a little doubt: level"}, {"at": 0.5, "event": "big cost: the beam tips"}, {"at": 0.85, "event": "doubt added until level"}]),
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
    "Salaam. This is Liam, in for Bear, with a short film for INFO seventy-three seventy-five, Computational Skepticism for AI. "
    "You might think a good skeptic doubts everything. You can't, and you shouldn't try. The real question is what to doubt.",
    "BrutalistHesitantWriter",
    {"text": "Should I doubt\neverything?", "triggerWords": "everything", "replacementWords": "what my work depends on",
     "fontSize": 72, "charMs": 150, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Should I doubt everything?'"}, {"at": 0.6, "event": "backspaces 'everything' -> 'what my work depends on' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (should I doubt everything) and corrects it to the real one (should I doubt what my work depends on).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. Radical doubt: asking what would have to be true for a claim to be wrong. Risk: how likely a claim is to be wrong, and what it costs if it is. "
    "And a provisional code: rules you act by while you're still doubting.",
    "ClaudeDefinitions",
    {"title": "INFO 7375 · Terms In This Film",
     "terms": [{"term": "radical doubt", "meaning": "asking what would make a claim wrong"},
               {"term": "risk", "meaning": "how likely it's wrong, and what that costs"},
               {"term": "provisional code", "meaning": "rules to act by while you doubt"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'radical doubt' lands"}, {"at": 0.4, "event": "'risk' lands"}, {"at": 0.75, "event": "'provisional code' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here are five claims my work relied on this week: [paste them]. For each one, help me say what it would cost "
             "if it were wrong, and rank them by that cost. Then, for the top one or two only, ask: what would have to be true "
             "for this to be wrong? List conditions I can check.")
SPOKEN_PROMPT = YT_PROMPT.replace("[paste them]", "paste them")
CHECKS = ["Check: are the top two the ones that could hurt?",
          "Check: could you test each condition this week?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Write down five claims your work relied on this week, and paste this into Claude: " + SPOKEN_PROMPT + " Then check two things yourself. "
    "Are the top two really the ones that could hurt someone? And could you test each condition this week?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "INFO 7375 COMPUTATIONAL SKEPTICISM · YOUR TURN", "segment": TITLE + ".", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn isometric scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B00", "B02", "B03", "B04", "B07"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160): 0.65-0.85 at 50/85%; the rest measure 0.23-0.54 and keep the waiver
for b in B:
    if b["beat_id"] not in FILLS_ON_ITS_OWN:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}
B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE + ".", "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "INFO 7375 · COMPUTATIONAL SKEPTICISM", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Arabic / Persian / Urdu (Salaam)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "course": COURSE,
    "audience": "INFO 7375 students (Fall 2026) and anyone whose work rests on claims they can't all check",
    "bookloop_policy": "Course film (Bear, 2026-09-27): carries the INFO 7375 credit, spoken in BIDEA and on screen in the BDEFS title and the BHTF composer topic; not a numbered lecture. Outro stays OUTRO-LOCK.",
    "source_doc": "info-7375-computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md lines 33-49 and 97 (SOURCE.md, verbatim) + Bear's words in youtube/SHOW-TELL-THREE-MOVES.md; Descartes' Meditations (1641), Discourse on the Method (1637), Principles of Philosophy (1644) in sources/",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["computational skepticism", "INFO 7375", "Descartes", "radical doubt", "Meditations", "Discourse on the Method",
             "provisional morality", "risk", "likelihood and consequence", "AI evaluation", "Claude", "Nik Bear Brown"]},
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
