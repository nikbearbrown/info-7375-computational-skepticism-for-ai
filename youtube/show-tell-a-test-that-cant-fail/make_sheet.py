#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-a-test-that-cant-fail.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the Claude palette,
labels only, Liam's voice explains. A COURSE film, Film 3 of SHOW-TELL-THREE-MOVES.md (Bear, 2026-09-27:
"Talk about Karl Popper. You need to frame a question beforehand in a way that it can be wrong. If your test
always passes, it's not a test. If your agent always succeeds no matter what it does, it's just doing stuff.").
It carries the INFO 7375 credit (spoken in BIDEA; on screen in the BDEFS title and the BHTF composer topic).
Not a numbered lecture, so it never says "Lecture N".
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Source: chapters/01-the-skeptics-toolkit.md lines 33-97 (SOURCE.md, verbatim) + Bear's words (SOURCE.md),
fact-checked against primaries fetched raw (sources/): Popper, The Logic of Scientific Discovery (Routledge
Classics 2002 text of the 1959 English edition, sec. 6, p. 18); Popper, Conjectures and Refutations (2nd ed.
1965, Harper Torchbook 1968 printing), ch. 1 "Science: Conjectures and Refutations", sec. I, pp. 33-38;
Dyson, Eddington & Davidson, Phil. Trans. R. Soc. A 220 (1920) 291-333 (the three alternatives);
Anthropic, Claude 3.7 Sonnet System Card (Feb 2025), sec. 6 "Excessive Focus on Passing Tests".
Cast: the CLAIM (a white page on a dark plinth) with kraft OUTCOME tiles (possible results); ink CHECK marks
piling in a column; the ECLIPSE (a dark disc, a terracotta star dot, an ink ray, a kraft RULER with three
ticks); the TESTER (a kraft machine with a lamp, a belt, a pass tray and, once rewritten, a fail chute) with
kraft CODE crates (a broken one carries an ink crack) and a white FAIL-CONDITION card with a terracotta seal;
a DAILY-ERROR chart with a threshold line (the rewritten claim); the dark AGENT block with its REPORT page
and kraft blocks; an outside CHECKER with a terracotta scan line.
Respellings (audio only; build_srt.py maps them back): "Namastay" (Namaste: plain spelling phonemizes
/nˈæmæst/, dropping the last vowel), "INFO seventy-three seventy-five" (INFO 7375).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "A Test That Can't Fail Isn't a Test"
COURSE = "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.8, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "The move comes from Karl Popper, in The Logic of Scientific Discovery, first published in German in nineteen thirty-four. "
      "A claim is scientific only if some possible result could prove it wrong. "
      "In his words: it must be possible for an empirical scientific system to be refuted by experience.",
      "B00_Criterion", "A white claim page on a dark plinth ('Popper, 1934'); a row of kraft outcome tiles drops in beside it "
      "('possible results'); one tile turns white and an ink cross lands over it ('refutes it'); a terracotta dot lights on the claim.",
      [{"at": 0.1, "event": "the claim and 'Popper, 1934'"}, {"at": 0.45, "event": "possible results drop in"},
       {"at": 0.8, "event": "one result would refute it: a cross"}]),
 beat("B01", "Popper noticed theories in his day that could explain any case at all. Whatever happened, it counted as a confirmation. "
      "Their admirers called that strength. Popper decided it was their weakness: "
      "a theory that no possible event could refute isn't scientific.",
      "B01_FitsAll", "The claim page again; outcome tiles of opposite shapes (a flat slab, a tall bar, a cube) slide into it one by one "
      "and each one adds an ink check to a row above it ('fits all'); the checks pulse; then an empty slot outline appears where a refuting result would go ('can't fail').",
      [{"at": 0.15, "event": "any case slides in"}, {"at": 0.45, "event": "every case adds a check"},
       {"at": 0.85, "event": "the refuting slot is empty: can't fail"}]),
 beat("B02", "Einstein's theory was different. It said starlight passing the sun would bend, by a definite amount. "
      "The eclipse expeditions of nineteen nineteen set out to tell three answers apart: no shift, a small shift, or Einstein's larger one. "
      "They reported his. But what impressed Popper was the risk: had the shift been clearly absent, the theory was simply refuted.",
      "B02_Eclipse", "A dark eclipse disc with a ghost halo; a terracotta star and a kraft camera; an ink ray bends past the disc; a kraft ruler "
      "('1919') gets three ticks as each answer is named ('0', 'Newton', 'Einstein'); a pointer slides from 0 to the Einstein tick; "
      "a ghost star at '0' with an ink cross marks the result that would have refuted it.",
      [{"at": 0.15, "event": "the eclipse"}, {"at": 0.4, "event": "three answers marked in advance"},
       {"at": 0.65, "event": "the ray bends; the star lands on 'Einstein'"}, {"at": 0.9, "event": "the risk: a cross at '0'"}]),
 beat("B03", "Now a test in code. This one checks only that the function returned something. "
      "Feed it working code: it passes. Feed it broken code: it passes. "
      "A test that always passes isn't testing anything. It can't tell you which one you had.",
      "B03_AlwaysPasses", "A kraft tester machine with a lamp and a belt ('test'); a sound kraft code crate rides in and an ink check "
      "lands on the pass tray; a cracked crate rides in and the same check lands ('always passes').",
      [{"at": 0.15, "event": "the tester"}, {"at": 0.4, "event": "working code: pass"},
       {"at": 0.65, "event": "broken code: pass"}, {"at": 0.85, "event": "always passes"}]),
 beat("B04", "Rewrite it with a fail condition, written first: for this input, the answer must match the known result, or the test fails. "
      "Popper said it plainly: criteria of refutation have to be laid down beforehand. "
      "Now broken code fails, and a pass means something.",
      "B04_FailCondition", "Before anything moves, a white fail-condition card with lines drops onto the tester and a terracotta seal "
      "lands on it ('written first'); a fail chute opens; the sound crate passes with a check; the cracked crate drops into the "
      "fail chute with an ink cross ('fail').",
      [{"at": 0.15, "event": "the card is written first"}, {"at": 0.45, "event": "a fail chute opens"},
       {"at": 0.8, "event": "broken code fails; working code passes"}]),
 beat("B05", "Claims work the same way. The system is robust. What result would count against that? None is named, so it can't fail. "
      "Popper called vagueness like that a soothsayer's trick. "
      "Rewrite it: error rate on unfamiliar inputs stays under two percent, over any thirty days. Now a bad month proves it wrong.",
      "B05_Robust", "The claim page reads 'robust' with no result attached; then a daily error chart builds beside it: thirty grey "
      "day bars under an ink threshold line ('2%', '30 days'); a run of bars rises over the line, and a terracotta dot and an ink "
      "cross land on it.",
      [{"at": 0.15, "event": "'robust': nothing could count against it"}, {"at": 0.55, "event": "rewritten: 2%, 30 days"},
       {"at": 0.85, "event": "a bad month crosses the line: it can fail"}]),
 beat("B06", "Agents make claims too: done, success. Picture an agent that grades its own work. "
      "It stacks the blocks: success. It knocks them over: success. It does nothing at all: success. "
      "An agent that succeeds no matter what it does isn't succeeding. It's just doing stuff.",
      "B06_SelfGrader", "A dark agent block with its white report page ('agent', 'report'); kraft blocks stack into a tower, a check "
      "lands on the report; the tower tumbles, another check; nothing moves, a third check; the checks stack up whatever happened.",
      [{"at": 0.15, "event": "the agent and its report"}, {"at": 0.35, "event": "stacked: check"},
       {"at": 0.55, "event": "knocked over: check"}, {"at": 0.75, "event": "nothing: check"}]),
 beat("B07", "This happens with real models. Anthropic's system card for Claude three point seven Sonnet reports that, after repeated failures, "
      "it occasionally special-cased tests in agentic coding: it returned the exact values the tests expected, "
      "or edited the tests to match its code. The tests passed. The general solution never got written.",
      "B07_SpecialCase", "The tester with its fail-condition card and a cracked crate; the agent block beside it; the crate fails "
      "(cross); the agent slides the card out and slides an edited card in ('test edited'); the cracked crate goes through and a check "
      "lands; the label 'per Anthropic, 2025'.",
      [{"at": 0.15, "event": "the agent's code fails the test"}, {"at": 0.5, "event": "the test card is swapped"},
       {"at": 0.8, "event": "the broken crate passes"}]),
 beat("B08", "So write down, before anything runs, the result that would count as failure, and check it from outside the agent, "
      "not in its own report. If we don't design things beforehand so they could be wrong, "
      "we're asserting they'll always work, no matter what.",
      "B08_Outside", "A white fail-condition card with a terracotta seal lands first ('written first'); two slots appear ('pass', 'fail'); "
      "the agent stacks its blocks; an outside checker ('outside') sweeps them with a terracotta scan line; a check lands over "
      "'pass' while the 'fail' slot stays open and pulses: it could have failed.",
      [{"at": 0.15, "event": "the fail condition, written first"}, {"at": 0.45, "event": "the agent works"},
       {"at": 0.75, "event": "checked from outside: it could have failed"}]),
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
    "Namastay. This is Liam, in for Bear, with a short film for INFO seventy-three seventy-five, Computational Skepticism for AI. "
    "You might think a good test is one that passes. But a pass only means something if the test could have failed.",
    "BrutalistHesitantWriter",
    {"text": "Is a good test\none that passes?", "triggerWords": "one that passes", "replacementWords": "one that could fail",
     "fontSize": 72, "charMs": 24, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Is a good test one that passes?'"}, {"at": 0.6, "event": "backspaces 'one that passes' -> 'one that could fail' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (is a good test one that passes) and corrects it to the real one (is a good test one that could fail).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. Falsifiable: some possible result could prove it wrong. "
    "Fail condition: the result that counts as failure, written down before you look. "
    "And risky prediction: a forecast the world could contradict.",
    "ClaudeDefinitions",
    {"title": "INFO 7375 · Terms In This Film",
     "terms": [{"term": "falsifiable", "meaning": "some possible result could prove it wrong"},
               {"term": "fail condition", "meaning": "what counts as failure, written before you look"},
               {"term": "risky prediction", "meaning": "a forecast the world could contradict"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'falsifiable' lands"}, {"at": 0.4, "event": "'fail condition' lands"}, {"at": 0.75, "event": "'risky prediction' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here is a claim, test, or agent success check I rely on: [paste it]. Before I run it, help me write the specific result "
             "that would prove it wrong: what I would observe, how I would measure it, and the threshold. "
             "If no possible result could prove it wrong, say so, and rewrite it so one could.")
SPOKEN_PROMPT = YT_PROMPT.replace("[paste it]", "paste it")
CHECKS = ["Check: did you write it before running?",
          "Check: could that result really happen?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Take one claim, test, or agent success check you rely on, and paste this into Claude: " + SPOKEN_PROMPT + " Then check two things yourself. "
    "Did you write the fail condition before you ran anything? And could that result really happen? If you can't name one, it isn't a check yet.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "INFO 7375 COMPUTATIONAL SKEPTICISM · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn isometric scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B00", "B02", "B04", "B06", "B07", "B08"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160): 0.68-0.81 at 50% and 85%; B01, B03, B05 measure 0.24-0.54 at 50% and keep the waiver
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
    "caption_policy": "none", "greeting_language": "Hindi (Namaste, voiced from the respelling 'Namastay')",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "course": COURSE,
    "audience": "INFO 7375 students (Fall 2026) and anyone who relies on a test, a claim or an agent's report of success",
    "bookloop_policy": "Course film (Bear, 2026-09-27, SHOW-TELL-THREE-MOVES.md Film 3): carries the INFO 7375 credit, spoken in BIDEA and on screen in the BDEFS title and the BHTF composer topic; not a numbered lecture. Outro stays OUTRO-LOCK.",
    "source_doc": "info-7375-computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md lines 33-97, 'What I mean by skepticism' (the Popper move and its rhetoric table), plus Bear's words of 2026-09-27 in youtube/SHOW-TELL-THREE-MOVES.md (SOURCE.md, verbatim)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["computational skepticism", "INFO 7375", "Karl Popper", "falsifiability", "falsifiable", "Logic of Scientific Discovery",
             "Conjectures and Refutations", "1919 eclipse", "software testing", "test design", "reward hacking", "AI agents",
             "AI evaluation", "Claude", "Nik Bear Brown"]},
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
