#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-cheap-to-make-dear-to-check.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the Claude palette,
labels only, Liam's voice explains. A COURSE film, ordered by Bear on 2026-09-27 (SHOW-TELL-SOLVE-VERIFY.md):
"Look at the most recent updates to the show tell skill ... Show tell film on the solve-verify asymmetry."
Built to the show-tell SKILL.md as modified 2026-09-27 19:03 (Law 9: no length cap or target, one beat per step
the viewer needs; the optional card family, used only when a beat passes the card test, which none here does).
It carries the INFO 7375 credit (spoken in BIDEA; on screen in the BDEFS title and the BHTF composer topic).
Not a numbered lecture, so it never says "Lecture N".
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Source: chapters/01-the-skeptics-toolkit.md, section "The solve-verify asymmetry" (SOURCE.md, verbatim; read only).
Every cost in the film is the chapter's own framing, spoken as "the chapter's numbers", with no figure added.
Cast: the COST METER (two grey bars, 'solve' and 'verify', that recur in every beat); a kraft NUMBER crate and two
FACTOR tiles (the folklore); the dark MODEL block and its white OUTPUT slip; a kraft PATIENT peg on a chair and a
CLINICIAN peg with a CLOCK; the SERVER stack (the system of record) and a QUERY line; a GRID of slips with checks;
a CHECKER block of the same shape; a HUMAN peg whose one check goes to the server, not the report.
Respellings (audio only; build_srt.py maps them back): "INFO seventy-three seventy-five" (INFO 7375).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Cheap to Make, Dear to Check"
COURSE = "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.8, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Start with a piece of computer-science folklore, and it's true. Hand someone a very large number and ask for its factors: "
      "that is hard. Hand them the factors and ask them to multiply: that is easy, and the check is done. "
      "Most of cryptography is built on this asymmetry. Solving is dear. Verifying is cheap.",
      "B00_Folklore", "A kraft crate ('big number') on the left; the cost meter's 'solve' bar creeps out long while two small factor tiles "
      "emerge ('factors'); then the tiles multiply back: the 'verify' bar is a short stub and an ink check lands at once.",
      [{"at": 0.1, "event": "the big number crate"}, {"at": 0.35, "event": "factoring: the solve bar grows long"},
       {"at": 0.7, "event": "multiplying back: the verify bar is a stub, a check lands"}]),
 beat("B01", "Now put a model in the picture. The asymmetry inverts. Producing the output is cheap. The model runs, the result appears, "
      "and in the chapter's numbers the latency is milliseconds and the cost is fractions of a cent. The solve bar barely moves.",
      "B01_Inverts", "The dark model block arrives ('model'); a white output slip pops out of it in one blink ('output'); the cost meter's "
      "'solve' bar is a sliver; the 'verify' bar waits, empty.",
      [{"at": 0.15, "event": "the model"}, {"at": 0.5, "event": "the output pops out"}, {"at": 0.75, "event": "solve: a sliver"}]),
 beat("B02", "Verifying it is expensive. Take the chapter's triage score. To check it, you need a clinician, with twenty minutes, "
      "a stethoscope, and a body of training the model does not have. The verify bar keeps growing.",
      "B02_Clinician", "The output slip sits beside a kraft patient peg on a chair ('patient'); a clinician peg walks in ('clinician'); a clock "
      "wedge fills beside them while the 'verify' bar grows long; a check lands only at the end.",
      [{"at": 0.15, "event": "the patient and the score"}, {"at": 0.4, "event": "the clinician arrives"},
       {"at": 0.6, "event": "the clock fills; the verify bar grows"}, {"at": 0.9, "event": "the check lands"}]),
 beat("B03", "Or take an agent's report that an email was deleted. To verify it, you query the provider's servers, examine the actual "
      "data state, and compare it with what the agent claimed. In the chapter's numbers, the output cost a fraction of a cent. "
      "The verification costs an hour of senior labor.",
      "B03_Report", "The model block with its report slip ('report'); a server stack on the right ('system of record'); a human peg draws a "
      "query line to the server, its lights come on, a record page comes back beside the report ('compare'); the 'verify' bar grows long.",
      [{"at": 0.15, "event": "the report"}, {"at": 0.4, "event": "the query reaches the server"},
       {"at": 0.65, "event": "the record comes back: compare"}, {"at": 0.85, "event": "verify: long"}]),
 beat("B04", "This is not a complaint. It is an observation about where the costs sit, and where they will keep sitting for the foreseeable "
      "future. Side by side: with a proof, verifying is the short bar. With a deployed model, it is the long one. "
      "The bars compare kinds of work, not measured costs.",
      "B04_WhereCostsSit", "Two cost meters side by side: 'proof' (solve long, verify short) and 'model' (solve short, verify long), labelled "
      "'illustrative'; a time arrow draws under the model's meter and the same pair repeats along it.",
      [{"at": 0.2, "event": "proof: verify short"}, {"at": 0.45, "event": "model: verify long"},
       {"at": 0.75, "event": "the pair repeats along the time arrow"}]),
 beat("B05", "If you do not budget for verification, you will not get verification. The system produces outputs at scale. "
      "Verification does not happen at scale. A small budget checks a few. The rest go out unchecked, and every one of them looks like a success.",
      "B05_AtScale", "The model streams slips into a grid; a short 'budget' bar beside a human peg; the peg marks two slips with a terracotta "
      "dot ('verified'); every slip in the grid carries an ink check regardless ('looks right').",
      [{"at": 0.15, "event": "slips stream into a grid"}, {"at": 0.45, "event": "the budget bar is short; two get verified"},
       {"at": 0.8, "event": "every slip carries a check"}]),
 beat("B06", "They stay indistinguishable. Until one of them is the patient, or the loan, or the warrant, or the email that did not "
      "actually get deleted. Under the check it was carrying, that one was wrong the whole time.",
      "B06_TheOne", "The same grid of checked slips; one slip lifts and turns over; an ink cross is on its underside ('wrong'); "
      "the others keep their checks ('looked the same').",
      [{"at": 0.3, "event": "one slip lifts"}, {"at": 0.6, "event": "it turns over: a cross"}, {"at": 0.85, "event": "the rest look the same"}]),
 beat("B07", "So automate the verification? That is the wrong fix. A checker that is another model has the same problem, sitting one layer up. "
      "Its verdict is cheap to produce and just as expensive to verify. Same shape, one layer up.",
      "B07_Checker", "A second dark block of the same shape drops onto the model ('checker'); it emits a check slip; a second cost meter appears "
      "beside it with the same shape as the first ('same shape').",
      [{"at": 0.2, "event": "the checker lands on the model"}, {"at": 0.5, "event": "it emits a verdict"},
       {"at": 0.75, "event": "its meter has the same shape"}]),
 beat("B08", "The right fix is design. Build the system so that the verification a human can perform tells you what you need to know. "
      "One human check, placed where it counts: at the system of record, not at the report. "
      "That is the check you budget for, and the one that is cheap enough to scale.",
      "B08_OneCheck", "The model and its report slip; the server stack ('system of record'); a human peg's check line aims at the report first and "
      "an ink cross fades over it ('not the report'), then swings to the server, whose lights come on and a check lands ('one check'); "
      "the 'verify' bar is short.",
      [{"at": 0.2, "event": "the human and the report"}, {"at": 0.5, "event": "not the report: the line swings to the server"},
       {"at": 0.8, "event": "one check; verify is short"}]),
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
    "Bonjour. This is Liam, in for Bear, with a short film for INFO seventy-three seventy-five, Computational Skepticism for AI. "
    "You might think checking an answer is cheaper than making one. In mathematics it often is. "
    "When a model makes the answer, it runs the other way: making is cheap, and checking is the expensive part.",
    "BrutalistHesitantWriter",
    {"text": "Is checking an answer\ncheaper than making one?", "triggerWords": "cheaper than making one",
     "replacementWords": "still cheaper when a model makes one",
     "fontSize": 72, "charMs": 110, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Is checking an answer cheaper than making one?'"},
     {"at": 0.6, "event": "backspaces 'cheaper than making one' -> 'still cheaper when a model makes one' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (is checking cheaper than making) and corrects it to the real one (is it still cheaper when a model makes the answer).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Four terms. Verify: check an output against the world, not against the output. "
    "Asymmetry: when making and checking cost different amounts. "
    "System of record: the store that holds the actual state. "
    "And budget: the time and people you set aside to verify.",
    "ClaudeDefinitions",
    {"title": "INFO 7375 · Terms In This Film",
     "terms": [{"term": "verify", "meaning": "check an output against the world, not the output"},
               {"term": "asymmetry", "meaning": "making and checking cost different amounts"},
               {"term": "system of record", "meaning": "the store that holds the actual state"},
               {"term": "budget", "meaning": "the time and people set aside to verify"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'verify' lands"}, {"at": 0.35, "event": "'asymmetry' lands"}, {"at": 0.6, "event": "'system of record' lands"},
     {"at": 0.85, "event": "'budget' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = ("Here is one AI output I act on: [describe it]. Help me price it honestly: what it cost to produce, and what it would "
             "cost to actually verify against the world, in time and in who has to do it. Then name the one check a human could do in "
             "five minutes that would tell me the most, and say whether it checks the world or only the report.")
SPOKEN_PROMPT = YT_PROMPT.replace("[describe it]", "describe it")
CHECKS = ["Check: did you price the verification honestly?",
          "Check: is the five-minute check against the world, not the report?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Take one AI output you act on, and paste this into Claude: " + SPOKEN_PROMPT + " Then check two things yourself. "
    "Did you price the verification honestly, in time and in people? And is your five-minute check against the world, or only against the report?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "INFO 7375 COMPUTATIONAL SKEPTICISM · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn isometric scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B00", "B03", "B04", "B06", "B08"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160): 0.59-0.89 at 50% and 85%; B01, B02, B05, B07 measure 0.44-0.55 at 50% and keep the waiver
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
    "caption_policy": "none", "greeting_language": "French (Bonjour)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "course": COURSE,
    "audience": "INFO 7375 students (Fall 2026) and anyone who acts on an AI output without pricing what it would cost to check it",
    "bookloop_policy": "Course film (Bear, 2026-09-27, SHOW-TELL-SOLVE-VERIFY.md): carries the INFO 7375 credit, spoken in BIDEA and on screen in the BDEFS title and the BHTF composer topic; not a numbered lecture. Outro stays OUTRO-LOCK.",
    "source_doc": "info-7375-computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md, section 'The solve-verify asymmetry' (SOURCE.md, verbatim; read only)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["computational skepticism", "INFO 7375", "solve-verify asymmetry", "verification", "AI verification", "system of record",
             "verification budget", "AI agents", "triage", "AI deployment", "Claude", "Nik Bear Brown"]},
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
