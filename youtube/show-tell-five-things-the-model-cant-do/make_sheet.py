#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-five-things-the-model-cant-do.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the Claude palette,
labels only, Liam's voice explains. A COURSE film, ordered by Bear on 2026-09-27 (SHOW-TELL-FIVE-CAPACITIES.md):
"Look at the latest show tell skills to make sure you have the latest changes and updates in it. Make a show
tell film on the five supervisory capacities." Built to the show-tell SKILL.md as modified 2026-09-27 20:59
(Law 9: no length cap or target, one beat per step the viewer needs; the optional card family, used only when a
beat passes the card test, which none here does; the --only re-voice rule; the new drawing traps).
It carries the INFO 7375 credit (spoken in BIDEA; on screen in the BDEFS title and the BHTF composer topic).
Not a numbered lecture, so it never says "Lecture N".
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B09 drawn -> BHTF composer -> BOUT.

Source: chapters/01-the-skeptics-toolkit.md, section "The Five Supervisory Capacities" (SOURCE.md, verbatim; read only).
Every example and number in the film is the chapter's own (attributed aloud as "the chapter's case/example"), no figure added.
Cast (the same objects, whole film): the dark MODEL block; its white OUTPUT slip; the SUPERVISOR peg (terracotta badge);
the WORLD, drawn as the PATIENT peg on a kraft chair; a row of five kraft TILES (the five capacities) that come back as
five plinths in the close; the PRIOR stack of pages; a TRAINING DATA crate; a second, lighter model block; a SPAM crate.
Respellings (audio only; build_srt.py maps them back): "INFO seventy-three seventy-five" (INFO 7375); "five percent" (5%).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Five Things the Model Can't Do for Itself"
COURSE = "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 3.3, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Verification is the problem. A model makes an output, and someone has to check it against the world. "
      "That someone is the supervisor, standing between the model and the world. "
      "The chapter counts five things the supervisor does there that the model cannot do for itself.",
      "B00_Between", "The dark model block arrives on the left ('model') and a white output slip pops out of it; the supervisor peg "
      "rises in the middle ('supervisor'); the patient peg on a kraft chair fades in on the right ('the world'); the slip slides from "
      "the model to the supervisor; five small kraft tiles rise in a row above the supervisor with ink numerals 1 to 5.",
      [{"at": 0.1, "event": "the model and its output"}, {"at": 0.35, "event": "the supervisor rises between model and world"},
       {"at": 0.75, "event": "five tiles rise above the supervisor"}]),
 beat("B01", "One. Plausibility auditing. The chapter's case: a low triage score for a forty-nine-year-old with a swollen leg. "
      "An experienced clinician looks at it, and something twitches. The twitch is the audit: a check against a prior, "
      "the sense built over years of what kinds of cases tend to be what.",
      "B01_Twitch", "The slip ('low score') slides from the model to the supervisor; the patient sits on the chair with a terracotta dot on "
      "the leg; behind the supervisor a stack of pages rises ('prior'); the supervisor peg twitches, a small rock left and right, and "
      "an ink question mark pops up above it.",
      [{"at": 0.15, "event": "the low score arrives"}, {"at": 0.45, "event": "the clinician looks: the twitch"},
       {"at": 0.7, "event": "the prior stack rises behind the supervisor"}]),
 beat("B02", "The model cannot do this for itself. It has its training data. The supervisor has the world. "
      "When nobody audits, the failure is quiet: the score arrives in a credible format, nobody asks whether it makes sense "
      "on its face, and it goes through.",
      "B02_TrainingVsWorld", "A kraft crate rises beside the model ('training data'); a line arcs from the supervisor to the patient "
      "('the world'); then, with the supervisor idle, the slip slides straight past the supervisor to the patient and an ink check "
      "lands on it ('credible format').",
      [{"at": 0.15, "event": "training data beside the model"}, {"at": 0.35, "event": "the supervisor's line to the world"},
       {"at": 0.75, "event": "the slip goes straight through; a check lands"}]),
 beat("B03", "Two. Problem formulation. The chapter says most AI failures are failures of formulation, not performance. "
      "The triage system answered: what statistical category is this presentation? "
      "The clinical question was: how likely is a life-threatening condition? The first was answered well. The second was never asked.",
      "B03_TwoQuestions", "Two question slips beside the supervisor: 'category?' slides into the model and an answered slip pops out with "
      "an ink check; 'life-threatening?' starts toward the model and stops short, and the label 'never asked' lands beside it.",
      [{"at": 0.2, "event": "two questions"}, {"at": 0.5, "event": "the first goes in and is answered"},
       {"at": 0.8, "event": "the second stops short: never asked"}]),
 beat("B04", "Three. Tool orchestration. AI is one tool among many. For each sub-problem, the supervisor picks the tool: "
      "the AI, human judgment, a different model, or, the hardest call, no tool yet: we do not know how to do this well enough to deploy.",
      "B04_WhichTool", "Four kraft plinths in a row: the dark model block ('AI'), a plain peg ('human'), a lighter second model block, and "
      "an empty plinth ('no tool yet'); the supervisor's cursor sweeps along the row, each object swells under it, and it lands on the "
      "empty plinth, which gets a terracotta dot.",
      [{"at": 0.15, "event": "the four plinths"}, {"at": 0.45, "event": "the cursor sweeps the row"},
       {"at": 0.8, "event": "it lands on no tool yet"}]),
 beat("B05", "Saying we should not deploy this here is supervisory work, and often the most valuable work the supervisor does. "
      "The failure runs the other way: AI used because it is available, not because it is right for the task, "
      "because nobody has the mandate to say no.",
      "B05_NoMandate", "The AI block on the left, a sub-problem slip on a plinth on the right; the supervisor draws an ink cross on the "
      "path between them ('not here'); then the supervisor and the cross fade, and the AI block slides onto the sub-problem by itself "
      "('available').",
      [{"at": 0.2, "event": "the supervisor's cross: not here"}, {"at": 0.55, "event": "the failure runs the other way"},
       {"at": 0.8, "event": "the AI block slides in by itself: available"}]),
 beat("B06", "Four. Interpretive judgment. The chapter's example: a five percent false-positive rate is fine for a spam filter, "
      "and catastrophic for a cancer screen. The same number, two meanings. "
      "The number is not the meaning; the meaning is the number in the domain. "
      "The failure: numbers read off a dashboard with no domain translation.",
      "B06_NumberInDomain", "The supervisor holds a slip with one ink hero number, 5%, captioned 'the chapter's example'; a kraft crate on "
      "the left ('spam filter') and the patient on the chair on the right ('cancer screen'); a copy of the slip slides to the crate and "
      "an ink check lands; another slides to the patient and an ink cross lands.",
      [{"at": 0.15, "event": "the hero number"}, {"at": 0.35, "event": "to the spam filter: a check"},
       {"at": 0.5, "event": "to the cancer screen: a cross"}]),
 beat("B07", "Five. Executive integration. Outputs from many tools, many models and many people, synthesized into one decision that "
      "someone stands behind. Somewhere in the organization, the buck has to stop. "
      "If there is no such place, the system has no decision-maker, only outputs.",
      "B07_BuckStops", "Three sources across the top: the model block, the lighter second model, and a plain peg; each emits a slip; "
      "the slips converge on the supervisor standing on a kraft plinth in the middle; one decision slip lands in front with a terracotta "
      "seal ('decision', 'buck stops').",
      [{"at": 0.15, "event": "three sources, three slips"}, {"at": 0.4, "event": "they converge on the supervisor's plinth"},
       {"at": 0.7, "event": "one decision, sealed"}]),
 beat("B08", "The chapter calls this the rarest capacity, and the one most often missing from AI deployments, because no model produces "
      "it and most pipelines have no place for it. The failure: the pipeline produces decisions nobody owns, and when something goes "
      "wrong, accountability dissolves into the architecture.",
      "B08_NoPlace", "The same three sources; the plinth and the supervisor are gone; the three slips converge on the empty middle and "
      "pile up with no seal ('no owner'); then the pile slides apart, one slip back under each source, and the middle is empty again.",
      [{"at": 0.2, "event": "no plinth in the middle"}, {"at": 0.45, "event": "the slips pile with no owner"},
       {"at": 0.8, "event": "the pile slides apart: accountability dissolves"}]),
 beat("B09", "These five are vocabulary for now. By the end of the book, you can look at any deployment and name, for each step, "
      "which capacity is exercised and by whom. Where you cannot name it, you have found a gap. "
      "And in the chapter's words: gaps are where the patients die.",
      "B09_Gap", "The five tiles from the opening, now five kraft plinths in a row with ink numerals 1 to 5; a small supervisor peg pops "
      "onto plinths one, two, three and five ('by whom'); plinth four stays empty and the label 'gap' lands over it; the patient on the "
      "chair slides in beneath the empty plinth.",
      [{"at": 0.15, "event": "five plinths"}, {"at": 0.4, "event": "a peg on four of them"},
       {"at": 0.65, "event": "the empty one: gap"}, {"at": 0.85, "event": "the patient beneath the gap"}]),
]


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 3.3, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
 remotion("BIDEA", "the question",
    "Ciao. This is Liam, in for Bear, with a short film for INFO seventy-three seventy-five, Computational Skepticism for AI. "
    "You might ask what kind of person should supervise an AI. The chapter says that is the wrong question. "
    "Not personality traits, not vibes. The question is what a supervisor can do that the system cannot do for itself.",
    "BrutalistHesitantWriter",
    {"text": "To supervise an AI,\nwhat kind of person do you need?", "triggerWords": "kind of person do you need",
     "replacementWords": "must you do that it can't do for itself",
     "fontSize": 72, "charMs": 110, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'To supervise an AI, what kind of person do you need?'"},
     {"at": 0.6, "event": "backspaces 'kind of person do you need' -> 'must you do that it can't do for itself' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (what kind of person supervises an AI) and corrects it to the real one (what must you do that it can't do for itself).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Four terms. Capacity: something the supervisor can do that the system cannot do for itself. "
    "Prior: the sense, built over years, of what kinds of cases tend to be what kinds of cases. "
    "Formulation: the exact question the system is being asked to answer. "
    "And integration: many outputs made into one decision that someone stands behind.",
    "ClaudeDefinitions",
    {"title": "INFO 7375 · Terms In This Film",
     "terms": [{"term": "capacity", "meaning": "something the supervisor can do that the system cannot"},
               {"term": "prior", "meaning": "the sense, built over years, of what cases tend to be"},
               {"term": "formulation", "meaning": "the exact question the system is asked to answer"},
               {"term": "integration", "meaning": "many outputs made into one decision someone stands behind"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'capacity' lands"}, {"at": 0.35, "event": "'prior' lands"}, {"at": 0.6, "event": "'formulation' lands"},
     {"at": 0.85, "event": "'integration' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = ("Here is one AI deployment I know, or one step of it: [describe it]. For each of the five supervisory capacities, "
             "plausibility auditing, problem formulation, tool orchestration, interpretive judgment and executive integration, "
             "write who exercises it, in one line each, or write 'nobody'. Then tell me which line you are least sure of, and why.")
SPOKEN_PROMPT = YT_PROMPT.replace("[describe it]", "describe it").replace("'nobody'", "nobody")
CHECKS = ["Check: is every 'who' a named role, not 'the team'?",
          "Check: did you write 'nobody' at least once, honestly?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Pick one AI deployment you know, or one step of one, and paste this into Claude: " + SPOKEN_PROMPT +
    " Then check two things yourself. Is every who a named role, not the team? And did you write nobody at least once, honestly?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "INFO 7375 COMPUTATIONAL SKEPTICISM · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn isometric scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B02", "B04", "B06", "B07"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160): 0.63-0.80 at 50% and 85%; B00 0.54/0.77, B01 0.54, B03 0.56/0.47, B05 0.66/0.33, B08 0.45/0.61, B09 0.28/0.38 keep the waiver
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
    "caption_policy": "none", "greeting_language": "Italian (Ciao)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "course": COURSE,
    "audience": "INFO 7375 students (Fall 2026) and anyone who supervises, or is about to deploy, an AI system",
    "bookloop_policy": "Course film (Bear, 2026-09-27, SHOW-TELL-FIVE-CAPACITIES.md): carries the INFO 7375 credit, spoken in BIDEA and on screen in the BDEFS title and the BHTF composer topic; not a numbered lecture. Outro stays OUTRO-LOCK.",
    "source_doc": "info-7375-computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md, section 'The Five Supervisory Capacities' (SOURCE.md, verbatim; read only)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["computational skepticism", "INFO 7375", "supervisory capacities", "plausibility auditing", "problem formulation",
             "tool orchestration", "interpretive judgment", "executive integration", "AI supervision", "AI deployment", "Claude", "Nik Bear Brown"]},
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
