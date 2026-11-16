#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-fluency-is-not-evidence.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the Claude palette,
labels only, Liam's voice explains. A COURSE film, ordered by Bear on 2026-09-28 (SHOW-TELL-FLUENCY-TRAP.md, dictated:
"Yes. Show and tell leads to Sonia. On the phone, we trap.", read as a show-tell film on the fluency trap).
Built to the show-tell SKILL.md as modified 2026-09-27 23:41 (Law 9: no length cap or target, one beat per step the viewer
needs; the optional card family, used only when a beat passes the card test, which none here does; the --only re-voice
rule; the drawing traps, including the five added after 20:59). It carries the INFO 7375 credit (spoken in BIDEA; on
screen in the BDEFS title and the BHTF composer topic). Not a numbered lecture, so it never says "Lecture N".
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B15 drawn -> BHTF composer -> BOUT.

Source: chapters/01-the-skeptics-toolkit.md, section "The fluency trap" (SOURCE.md, verbatim; read only).
Every claim in the film is the chapter's own (attributed aloud as "the chapter says / the chapter's case"); no number added.
Cast (the same objects, whole film): the PAGE (an upright white sheet, the artifact); the READER peg; two GAUGES (confidence in
the output, confidence in your own judgment); the WORLD (a dark block with one lamp; in the case it is the account); a MODEL
block; and, in the mechanism beats, the page as two sheets, FORM in front and CONTENT behind, bound by one terracotta dot.
Respellings (audio only; build_srt.py maps them back): "INFO seventy-three seventy-five" (INFO 7375).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "The Shape of a Sentence Is Not Evidence"
COURSE = "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 3.3, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "The chapter borrows two pillars from the Botspeak framework, which it treats in full in its Appendix A. "
      "Strategic delegation: knowing what to ask the AI to do, given its strengths and failure modes on this kind of task. "
      "Critical evaluation: knowing what to do with what comes back, evaluated against criteria you set before you saw it.",
      "B00_TwoPillars", "The reader peg on the left, the dark model block on the right; a kraft tile rises over the reader ('delegation') "
      "and an ask slip slides from the reader into the model; a second tile rises ('evaluation'), a small criterion card stands beside "
      "the reader, and a plain page comes back out of the model to the reader.",
      [{"at": 0.1, "event": "delegation: the ask goes to the model"}, {"at": 0.5, "event": "evaluation: the criterion card, then the page comes back"}]),
 beat("B01", "Both matter, and both recur through the book. But the chapter says plainly that neither of them protects you from "
      "the trap. That is why the trap gets its own section.",
      "B01_NeitherProtects", "A confidence gauge rises above the reader, needle low ('output'); the two tiles and the criterion card "
      "fade away while the gauge stays; the page stays where it is.",
      [{"at": 0.15, "event": "the gauge rises over the reader"}, {"at": 0.6, "event": "the pillars fade; the gauge stays"}]),
 beat("B02", "Stage one. The more fluently the output is presented, the more confident you become in the output. "
      "The prose smooths out, the sentences are well formed, and the needle climbs. "
      "The chapter says that part is not surprising.",
      "B01_StageOne", "The page that came back in front of the reader has ragged lines; the lines smooth into straight tidy lines ('fluent'); "
      "the gauge above the reader ('output') swings its needle from low to high.",
      [{"at": 0.15, "event": "the page in front of the reader, ragged"}, {"at": 0.4, "event": "its lines smooth out: fluent"},
       {"at": 0.7, "event": "the output needle climbs"}]),
 beat("B03", "Stage two is the trap. The more confident you become in the output, the more confident you become in your own "
      "evaluation of it. A second needle follows the first. Not because you checked anything. Because the page read well.",
      "B02_StageTwo", "A second gauge rises beside the first ('own judgment'); a grey link draws from the first gauge to the second; "
      "the second needle swings up to match the first while the reader and the page stay still.",
      [{"at": 0.15, "event": "the second gauge: own judgment"}, {"at": 0.45, "event": "a link from gauge to gauge"},
       {"at": 0.7, "event": "the second needle follows the first"}]),
 beat("B04", "So fluency is an evaluation booster, and it boosts the wrong evaluations as readily as the right ones. "
      "It does not just make you more likely to accept a good answer. "
      "It makes you more likely to accept any answer that arrives in the same shape.",
      "B03_SameShape", "A second page of exactly the same shape slides in beside the first ('same shape'); a small ink cross sits "
      "under it ('wrong'); the reader's ink check lands on the first page, then on the second, and both needles stay high.",
      [{"at": 0.2, "event": "a second page, same shape, marked wrong"}, {"at": 0.55, "event": "a check on the first page"},
       {"at": 0.8, "event": "a check on the second page too"}]),
 beat("B05", "The chapter's case. An agent produced a fluent, well-formed report. The email had been deleted. "
      "The account had been secured. The user read it and trusted it. And the chapter is careful here: the agent did not deceive him.",
      "B04_TheReport", "The world block on the right is the account ('the account'); the report page arrives from the model with "
      "two ink checks on its lines ('deleted', 'secured'); both needles swing high; no line is drawn from the reader to the account.",
      [{"at": 0.15, "event": "the report arrives with two checks"}, {"at": 0.55, "event": "both needles high: trusted"},
       {"at": 0.8, "event": "the account stands apart, unvisited"}]),
 beat("B06", "A non-fluent reader would have asked the basic questions the fluent reader felt no need to ask. "
      "In the chapter's words, the fluency was the trap. "
      "The well-formed prose did the work the verification should have done.",
      "B05_NonFluent", "A ragged copy of the report stands beside the tidy one ('non-fluent'); an ink question mark pops over the "
      "reader and a grey line draws from the reader to the account ('asked'); then the ragged page and the line go, the tidy report "
      "slides into the gap where the line was, and the checks on it are the only marks left.",
      [{"at": 0.15, "event": "the non-fluent report: a question, a line to the account"}, {"at": 0.6, "event": "the line goes with it"},
       {"at": 0.8, "event": "the tidy report stands where the check should be"}]),
 beat("B07", "The point is not to distrust fluent outputs. On average, the chapter says, fluent outputs are more useful than "
      "non-fluent ones. The point is to not let fluency do epistemic work. "
      "When you find yourself accepting an output because it sounds right, stop.",
      "B06_Stop", "The tidy page and a ragged page side by side; the tidy one lifts a step higher ('more useful'); then the output "
      "needle swings toward high and a wide ink bar drops between the gauge and the page ('stop').",
      [{"at": 0.2, "event": "fluent is, on average, more useful"}, {"at": 0.6, "event": "the needle starts to swing"},
       {"at": 0.8, "event": "the bar drops: stop"}]),
 beat("B08", "Then the three moves the chapter has already given you. Ask what would have to be true for this to be wrong. "
      "That is the move from Descartes. Say beforehand what a wrong answer looks like. That is the move from Popper. "
      "And the third: look at the artifact, look at the world, and ask what the relationship is.",
      "B07_ThreeMoves", "The page ('artifact') on the left and the world block on the right; two kraft tiles rise between them, "
      "one at a time ('Descartes', 'Popper'); then a grey line draws from the page to the world block and a small ink question mark "
      "sits on it.",
      [{"at": 0.2, "event": "Descartes's tile"}, {"at": 0.45, "event": "Popper's tile"},
       {"at": 0.75, "event": "the line from artifact to world, with a question on it"}]),
 beat("B09", "Why does it work on us? Form and content. In human speech, a well-formed sentence usually comes from someone who knows "
      "what they are talking about. When a colleague speaks in clear, organized prose, they have generally thought about it. "
      "The clarity is evidence of the thinking. The heuristic is reliable.",
      "B08_HumanHeuristic", "A plain peg speaks and a page comes out as two sheets: the front sheet with tidy lines ('form') and a "
      "kraft sheet behind it ('content'), bound at the top by one terracotta dot; the pair slides together to the reader and an ink "
      "check lands.",
      [{"at": 0.15, "event": "a colleague speaks a page"}, {"at": 0.4, "event": "form in front, content behind, one dot binds them"},
       {"at": 0.75, "event": "they move together; a check"}]),
 beat("B10", "AI systems broke it. The form comes from a statistical process that learned what well-formed prose looks like. "
      "The content is whatever that process produces from the input. The two are independent. "
      "A sentence can be maximally fluent and maximally wrong at the same time, and fluency alone cannot tell you which.",
      "B09_Independent", "The model block emits the same two sheets, but with no dot binding them; the front sheet ('form') stays "
      "tidy where it is while the kraft sheet ('content') slides out from behind it on its own and an ink cross lands on it; "
      "the output needle stays high.",
      [{"at": 0.15, "event": "the model's page: two sheets, no binding"}, {"at": 0.5, "event": "content slides out on its own; a cross"},
       {"at": 0.8, "event": "the form is still tidy; the needle still high"}]),
 beat("B11", "The chapter says this is not a flaw that the next model will fix. It is structural. "
      "These systems learn to produce outputs that resemble correct outputs. "
      "Where resemblance and correctness track each other closely, that works well.",
      "B10_Resemble", "An ink curve rises over the stage like a hill ('training data'); the model block sits at its foot; three pages "
      "pop up along the hill, each in the same shape, and an ink check lands under each.",
      [{"at": 0.15, "event": "the hill of training data"}, {"at": 0.45, "event": "pages along the hill, same shape"},
       {"at": 0.75, "event": "a check under each"}]),
 beat("B12", "Where they diverge, in novel situations, edge cases, inputs the training data underrepresented, the system keeps "
      "producing fluent output, confidently, in exactly the shape that makes you trust it, about things it has no basis to say.",
      "B11_EdgeCase", "A fourth page slides off the end of the hill onto the flat tail ('edge case'), exactly the same shape as the "
      "three; an ink cross lands under it; the output needle over the reader swings high anyway ('same shape').",
      [{"at": 0.2, "event": "a page slides out past the hill"}, {"at": 0.55, "event": "a cross under it"},
       {"at": 0.8, "event": "the needle swings high anyway"}]),
 beat("B13", "The Popperian move helps here. Before you read the output, specify what a wrong answer would look like. "
      "Not vaguely; specifically. The chapter's example: a wrong answer would assign low risk to a patient with this "
      "combination of symptoms and profile.",
      "B12_Before", "The page waits face down on the right as a ghost outline ('unread'); the reader writes a small criterion "
      "card that rises beside him ('criterion') with a short ink line on it ('low risk'); the page stays unread.",
      [{"at": 0.2, "event": "the page is still unread"}, {"at": 0.5, "event": "the reader writes the criterion first"},
       {"at": 0.8, "event": "low risk: the specific wrong answer"}]),
 beat("B14", "Then read it. The prior specification is your anchor. Without it, you are reading the output with no criterion "
      "except fluency. And fluency is the trap.",
      "B13_Anchor", "The ghost page fills in with tidy lines (read); the criterion card slides up against it and the output needle "
      "settles at the middle ('anchor'); then the criterion card fades and the needle swings all the way up ('fluency').",
      [{"at": 0.15, "event": "the page is read against the criterion"}, {"at": 0.45, "event": "the needle holds at the middle: anchored"},
       {"at": 0.75, "event": "without the criterion the needle swings high"}]),
 beat("B15", "Fluency boosts the wrong evaluations as readily as the right ones. "
      "The shape of a sentence is not evidence about its truth.",
      "B14_NotEvidence", "The two same-shape pages from before, one with a check beneath and one with a cross, both needles high; "
      "then an empty outline of the page shape lifts off and hangs above them ('the shape'), and an ink cross lands between the "
      "outline and the world block ('not evidence').",
      [{"at": 0.15, "event": "same shape, one right, one wrong, both accepted"}, {"at": 0.5, "event": "the shape lifts off the pages"},
       {"at": 0.8, "event": "a cross between the shape and the world"}]),
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
    "Hola. This is Liam, in for Bear, with a short film for INFO seventy-three seventy-five, Computational Skepticism for AI. "
    "You might ask: if an AI's answer reads well, isn't it probably right? The chapter turns that into a different question. "
    "If it reads well, why do you feel so sure, and sure of what? That feeling has a mechanism, and the chapter calls it the fluency trap.",
    "BrutalistHesitantWriter",
    {"text": "If the answer reads well,\nis it probably right?", "triggerWords": "is it probably right",
     "replacementWords": "why do I feel so sure and of what",
     "fontSize": 72, "charMs": 110, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'If the answer reads well, is it probably right?'"},
     {"at": 0.6, "event": "backspaces 'is it probably right' -> 'why do I feel so sure and of what' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (if it reads well, is it probably right?) and corrects it to the real one (why do I feel so sure, and of what?).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Four terms. Fluency: how smoothly and confidently a piece of prose reads. "
    "Form versus content: the shape of a sentence, against what the sentence actually says. "
    "Criterion: what you decided a wrong answer would look like, before you read it. "
    "And evaluation: judging what comes back against that criterion, not just reviewing and accepting.",
    "ClaudeDefinitions",
    {"title": "INFO 7375 · Terms In This Film",
     "terms": [{"term": "fluency", "meaning": "how smoothly and confidently a piece of prose reads"},
               {"term": "form vs content", "meaning": "the shape of a sentence, against what it actually says"},
               {"term": "criterion", "meaning": "what you decided a wrong answer looks like, before reading"},
               {"term": "evaluation", "meaning": "judging what comes back against that criterion"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'fluency' lands"}, {"at": 0.35, "event": "'form vs content' lands"}, {"at": 0.6, "event": "'criterion' lands"},
     {"at": 0.85, "event": "'evaluation' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = ("Here is one AI output I accepted this week because it read well: [paste it]. Do not evaluate it yet. First write one "
             "sentence saying what a wrong version of this output would have looked like, specifically. Then re-read the output "
             "against that sentence and tell me what, if anything, in it I could only confirm by looking at the file, the record, "
             "or the account it is about, not at the prose.")
SPOKEN_PROMPT = YT_PROMPT.replace("[paste it]", "paste it")
CHECKS = ["Check: did you write the wrong-version sentence BEFORE re-reading?",
          "Check: did your check touch the world (the file, the record, the account), or only the prose?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Take one AI output you accepted this week because it read well, and paste this into Claude: " + SPOKEN_PROMPT +
    " Then check two things yourself. Did you write the wrong-version sentence before re-reading? "
    "And did your check touch the world, the file, the record, the account, or only the prose?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "INFO 7375 COMPUTATIONAL SKEPTICISM · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn isometric scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B01", "B02", "B03", "B04", "B05", "B12"}   # local Gate V pre-check 2026-09-28 (1080p up to 2160): 0.70-0.80 at every sampled frame (25-99%); B00 0.39 at 25%, B06 0.41, B07 0.41, B08 0.41, B09 0.35, B10 0.48, B11 0.07 at 25% (v1) / 0.52, B13 0.50, B14 0.50, B15 0.33 keep the waiver
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
    "caption_policy": "none", "greeting_language": "Spanish (Hola)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "course": COURSE,
    "audience": "INFO 7375 students (Fall 2026) and anyone who reads AI output and has to decide whether to trust it",
    "bookloop_policy": "Course film (Bear, 2026-09-28, SHOW-TELL-FLUENCY-TRAP.md): carries the INFO 7375 credit, spoken in BIDEA and on screen in the BDEFS title and the BHTF composer topic; not a numbered lecture. Outro stays OUTRO-LOCK.",
    "source_doc": "info-7375-computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md, section 'The fluency trap' (SOURCE.md, verbatim; read only)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["computational skepticism", "INFO 7375", "fluency trap", "form and content", "critical evaluation", "strategic delegation",
             "Botspeak", "Popper", "Descartes", "AI verification", "Claude", "Nik Bear Brown"]},
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
