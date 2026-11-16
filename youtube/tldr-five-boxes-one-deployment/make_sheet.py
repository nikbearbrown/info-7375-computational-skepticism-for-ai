#!/usr/bin/env python3
"""make_sheet.py — writes beat_sheet.json for tldr-five-boxes-one-deployment.

tldr skill (brutalist.art/skills/make/tldr). Section S5 of chapter 12
(youtube/tldr-sections-12-accountability.md): the chapter's five accountability
requirements (§"The five accountability requirements…" + its checklist table,
BODY list — not the LLM Exercise's renamed list) run as an audit instrument
against the chapter's Application A2 content-moderation description. A2 is an
exercise scenario, so it is captioned "constructed" once, small. The Irreducibly
Human tier taxonomy (the chapter's one [verify]) stays OUT of the film.
SyRI (§"The regulatory landscape") is the post-shift real INSTANCE.

Every count is asserted below; FACTCHECK.md carries the rows.
Re-run → lock_audio.py (after audio) → ./art run.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

SLUG = "tldr-five-boxes-one-deployment"
TITLE = "Five Boxes, One Deployment"
COURSE = "INFO 7375 · Computational Skepticism · Chapter 12"

# ── the chapter's A2 text, verbatim (Application A2) ─────────────────────────
A2 = ["The system flags posts for review.",
      "Moderators can appeal a flag by contacting the support team.",
      "The company's trust and safety team reviews reported issues periodically.",
      "The system has been running for 18 months."]
# ── the chapter's checklist (body list + "How to verify it is present" + "Failure mode if absent") ──
REQS = ["Specifications", "Audit trail", "Recourse", "Independent review", "Sanctions"]
PROBE = {"Specifications": "A reviewer can read the spec and predict what counts as success",
         "Audit trail": "Pull a random recent incident; can the chain be reconstructed in under an hour?",
         "Recourse": "An external party can read the channel description and use it",
         "Independent review": "Named reviewer; documented review cadence; visible halt authority",
         "Sanctions": "Pull the policy; can a specific named role lose something specific for a specific failure?"}
# which A2 sentence (if any) a word-matching reader would file under each box
WORDS = {"Specifications": 0, "Audit trail": None, "Recourse": 1, "Independent review": 2, "Sanctions": None}
# does the A2 text supply what the probe asks for? (our reading — FACTCHECK rows 9–14)
PASSES = {"Specifications": False,      # a task verb; no acceptance criteria, no signer
          "Audit trail": False,         # silent: no log described
          "Recourse": False,            # channel is for moderators, via "support"; nothing for the flagged poster
          "Independent review": False,  # the company's own team, "periodically", no named reviewer, no halt authority
          "Sanctions": False}           # silent: no consequence named
assert len(REQS) == 5 and len(A2) == 4
assert sum(v is not None for v in WORDS.values()) == 3            # B12/B13: three boxes hold words
assert sum(v is None for v in WORDS.values()) == 2                # two are blank
assert sum(PASSES.values()) == 0                                  # B16: zero of five
assert "18 months" in A2[3] and all("18" not in s for s in A2[:3])  # 18 months is not filed under any box
assert "no incident" not in " ".join(A2).lower()                  # the text never claims no incidents

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

B00_N = ("Sawubona. This is Liam, in for Bear, with chapter twelve of INFO 7375, Computational Skepticism for AI, at Northeastern. "
         "This film is about auditing one deployment against five accountability requirements. "
         "A requirement counts when its test passes, not when its word appears. "
         "You'll watch a four-sentence description meet a five-box checklist. "
         "The trap: mistaking a word, or eighteen months of running, for a ticked box.")
B00_EST = round(len(B00_N.split()) / 2.5, 1)
beats.append(beat("B00", "tldr · what", B00_N,
    remotion("ClaudeTldrWhat", {
        "eyebrow": "TL;DR", "heading": "What This Film Is About", "greeting": "Sawubona, Liam", "topic": COURSE,
        "question": "It has been running for 18 months. Is it accountable?",
        "lines": ["A requirement counts when its test passes, not when its word appears.",
                  "Watch a four-sentence description meet the five-box accountability checklist.",
                  "The trap: mistaking a word, or eighteen months of running, for a ticked box."],
        "cues": [round(B00_EST * f, 1) for f in (0.05, 0.50, 0.66, 0.84)], "durationSeconds": B00_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "'TL;DR.' wordmark; 'Sawubona, Liam'; the course line; heading"},
         {"at": 0.05, "event": "the question writes on"},
         {"at": 0.50, "event": "line 1 lands on 'a requirement counts'"},
         {"at": 0.66, "event": "line 2 lands on 'you'll watch'"},
         {"at": 0.84, "event": "line 3 lands on 'the trap'"}]),
    lane="bookend"))

B01_N = ("Why should you care? The AI systems you use come with paragraphs like this one, and they read like accountability. "
         "Take the words at face value, and the person who was flagged has nowhere to go. "
         "Run the tests, and a reassuring paragraph becomes a list of named gaps. "
         "And it unlocks auditing any deployment you meet with five questions.")
B01_EST = round(len(B01_N.split()) / 2.5, 1)
beats.append(beat("B01", "tldr · why", B01_N,
    remotion("ClaudeTldrWhy", {
        "eyebrow": "TL;DR", "heading": "Why You Should Care", "topic": COURSE,
        "lead": "The AI systems you use come with paragraphs like this one, and they read like accountability.",
        "lines": ["Take the words at face value, and the person who was flagged has nowhere to go.",
                  "Run the tests, and a reassuring paragraph becomes a list of named gaps.",
                  "It unlocks auditing any deployment you meet with five questions."],
        "cues": [round(B01_EST * f, 1) for f in (0.05, 0.38, 0.62, 0.82)], "durationSeconds": B01_EST, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "page turn: same header, heading 'Why You Should Care'"},
         {"at": 0.05, "event": "the stake writes on"},
         {"at": 0.38, "event": "dash 1 on 'take the words'"},
         {"at": 0.62, "event": "dash 2 on 'run the tests'"},
         {"at": 0.82, "event": "dash 3 on 'unlocks'"}]),
    lane="bookend", qc={"sparse_by_design": True, "sparse_reason": "TL;DR card two — text lands on cues by design."}))

beats.append(beat("B02", "the question",
    "The question this film is really asking: does it pass the five checks? Not 'does it sound accountable'. "
    "A paragraph can mention an appeal and a review team, and still fail every one.",
    remotion("BrutalistHesitantWriter", {
        "text": "Four sentences, 18 months running.\nDoes it sound accountable?",
        "triggerWords": "sound accountable", "replacementWords": "pass the five checks",
        "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
        "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'Four sentences, 18 months running.'"},
         {"at": 0.35, "event": "types 'Does it sound accountable?'; backspaces the phrase → 'pass the five checks' on the spoken correction"},
         {"at": 0.85, "event": "caret holds"}]),
    lane="bookend", lead_silence_s=0.8,
    motion_claim="The writer types the naive question and corrects the phrase that makes it the wrong question.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}))

B03_N = ("Four words you'll hear. A specification: the written task, and what counts as success. "
         "An audit trail: a log of every action, with times. "
         "Recourse: a channel for the people affected to contest a decision. "
         "And a sanction: a consequence that lands on a named person.")
beats.append(beat("B03", "terms", B03_N,
    remotion("ClaudeDefinitions", {
        "title": "Terms In This Film",
        "terms": [{"term": "specification", "meaning": "the written task, and what counts as success"},
                  {"term": "audit trail", "meaning": "a log of every action: inputs, outputs, decisions, times"},
                  {"term": "recourse", "meaning": "a channel for the people affected to contest a decision"},
                  {"term": "sanction", "meaning": "a consequence that lands on a named, accountable person"}],
        "durationSeconds": round(len(B03_N.split()) / 2.5, 1), "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'specification' lands, terracotta"}, {"at": 0.35, "event": "'audit trail' lands"},
         {"at": 0.58, "event": "'recourse' lands"}, {"at": 0.8, "event": "'sanction' lands"}]),
    lane="bookend", proof="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: prerequisites only — 'present when the test passes' is earned in the section."}))

# ── LEARN section 1 (B10–B19) ────────────────────────────────────────────────
beats.append(beat("B10", "learn 1",
    "Here is a whole deployment, in four sentences. The system flags posts for review. "
    "Moderators can appeal a flag by contacting the support team. "
    "The company's trust and safety team reviews reported issues periodically. "
    "The system has been running for eighteen months. "
    "It sounds careful: an appeal, a review team, a long run. So, when it flags the wrong post, is anyone accountable?",
    manim("B10_TheParagraph",
          "The chapter's A2 description writes on sentence by sentence (six wrapped lines, left); on 'eighteen months' an 18-segment month bar grows under it with its label; a terracotta dot beside the last sentence; 'accountable?' lands at right; small dim 'constructed exercise case'.",
          [{"at": 0.05, "event": "sentence 1 writes on"}, {"at": 0.2, "event": "sentence 2"}, {"at": 0.4, "event": "sentence 3"},
           {"at": 0.58, "event": "sentence 4; the 18-month bar grows"}, {"at": 0.85, "event": "'accountable?' lands"}],
          "The key case, unsolved: a paragraph and a clock, no checklist yet."),
    role="HOOK", section=1,
    learn={"question": "A deployment with an appeal, a review team and 18 months of running: is anyone accountable?",
           "action": "Put the four sentences and the 18-month bar on screen.",
           "observation": "Every sentence sounds like care; none is tested yet.",
           "inference": "We need something the paragraph has to answer to.",
           "next_question": "What would the paragraph have to answer to?"}))

beats.append(beat("B11", "learn 1",
    "Give the paragraph something to answer to: the chapter's five requirements. "
    "Specifications. Audit trail. Recourse. Independent review. Sanctions. Five empty boxes. "
    "First sentence: the system flags posts for review. That says what the system does. Call it a specification, and pencil in a tick.",
    manim("B11_FiveBoxes",
          "The six lines condense into four quoted fragments at right; the 18-month bar shrinks to the bottom-left; five grey-outlined boxes draw down the left, each name landing on its spoken word; the first fragment slides into the Specifications row and a dim pencil tick draws in its box; a terracotta dot beside 'Specifications'.",
          [{"at": 0.05, "event": "the paragraph condenses into four fragments"}, {"at": 0.25, "event": "five boxes draw, one per spoken name"},
           {"at": 0.7, "event": "'flags posts for review' slides into row 1"}, {"at": 0.88, "event": "a pencil tick"}],
          "The objects and the rules: five boxes, four sentences; the first sentence filed by its words."),
    role="INSTANCE", section=1,
    learn={"question": "Which box does 'flags posts for review' belong in?",
           "action": "Draw the five boxes; file the first sentence where its words fit.",
           "observation": "It names what the system does, so it lands in Specifications with a tick.",
           "inference": "Reading by words, a sentence can fill a box.",
           "next_question": "Where do the other sentences go?"}))

beats.append(beat("B12", "learn 1",
    "Next. Moderators can appeal a flag: that sounds like recourse, so in it goes, tick. "
    "The trust and safety team reviews reported issues: that sounds like independent review. Tick. "
    "Audit trail and sanctions? The paragraph never mentions them. Those two boxes stay blank.",
    manim("B12_FileTheRest",
          "The appeal fragment slides into the Recourse row, a pencil tick draws; the review fragment slides into the Independent review row, a tick draws; 'not mentioned' lands dim in the Audit trail and Sanctions rows; the eighteen-month fragment stays behind with the bar.",
          [{"at": 0.08, "event": "'appeal … support team' slides into Recourse; tick"}, {"at": 0.38, "event": "'reviews periodically' slides into Independent review; tick"},
           {"at": 0.72, "event": "'not mentioned' in the two blank rows"}],
          "The second instance: the same filing move, two more rows; two rows get nothing."),
    role="INSTANCE", section=1,
    learn={"question": "Where do sentences two and three go?",
           "action": "File each by the words it uses.",
           "observation": "Recourse and review get ticks; audit trail and sanctions stay blank.",
           "inference": "Three boxes hold words; two hold nothing.",
           "next_question": "So how accountable is it?"}))

beats.append(beat("B13", "learn 1",
    "Here's the reading most of us would give. Three boxes hold words. Two are blank, but it's been running for eighteen months; surely we'd have heard. "
    "Three out of five, plus a track record: mostly accountable. "
    "But look where the eighteen months went. It has no box. It's a clock, not a check.",
    manim("B13_TheEasyReading",
          "The right column writes the tally — 'three boxes hold words', 'two are blank', '18 months, still running', bold 'mostly accountable?'; the eighteen-month bar pulses; a terracotta X lands beside its label; caption 'a clock, not a check'.",
          [{"at": 0.1, "event": "tally line 1"}, {"at": 0.3, "event": "'two are blank'; '18 months, still running'"},
           {"at": 0.55, "event": "'mostly accountable?'"}, {"at": 0.8, "event": "X beside the bar: no box"}],
          "The natural wrong turn, walked: count the words, lean on the clock."),
    role="NAIVE", section=1,
    learn={"question": "Three boxes with words plus 18 months: is that mostly accountable?",
           "action": "Tally the ticks; try to file the 18 months.",
           "observation": "The tally looks like 3 of 5; the 18 months fits no box.",
           "inference": "Word-matching gives a score; nothing yet says the score means anything.",
           "next_question": "What would make a tick mean something?"}))

beats.append(beat("B14", "learn 1",
    "Here's the move. Beside every box, the chapter gives a test of whether it's really there. "
    "Specifications: could a reviewer predict what counts as success? Audit trail: could you rebuild an incident in under an hour? "
    "Recourse: could an outsider find the channel and use it? Review: someone named, outside the team, able to halt it? "
    "Sanctions: can a named role lose something? "
    "Run the first. Flags posts, for what? No criteria. The tick comes out.",
    manim("B14_EachBoxHasATest",
          "The tally clears; the five tests write into the right column, each on its row as it is spoken; then row 1 runs: its pencil tick uncreates and its failure mode writes under the test — '“the model said so” is the audit'; terracotta dot beside the Specifications test.",
          [{"at": 0.05, "event": "tally clears"}, {"at": 0.12, "event": "test 1"}, {"at": 0.3, "event": "test 2"}, {"at": 0.48, "event": "test 3"},
           {"at": 0.62, "event": "test 4"}, {"at": 0.72, "event": "test 5"}, {"at": 0.85, "event": "row 1 runs: the tick comes out; failure mode writes"}],
          "The representation: each box carries its own test; a tick is a passed test, not a matched word."),
    role="SHIFT", section=1,
    learn={"question": "What would make a tick mean something?",
           "action": "Put the chapter's verification test beside each box; run the first.",
           "observation": "'Flags posts for review' names no success criteria, so the specification tick comes out.",
           "inference": "A box is filled by a passed test, not by a word.",
           "next_question": "What happens to the two ticks that sounded most like accountability?"}))

beats.append(beat("B15", "learn 1",
    "Two ticks left, recourse and review, the two sentences that sounded most like accountability. "
    "Before the tests run, commit. When we're done, how many of the five boxes still hold a tick? Two? One? None?",
    manim("B15_Commit",
          "The two ticked rows are bracketed by an ink rule between the columns; their tests hold; a terracotta dot beside the recourse test; caption 'how many ticks survive? commit'. Nothing else moves.",
          [{"at": 0.1, "event": "bracket draws beside the two ticked rows"}, {"at": 0.4, "event": "dot on the recourse test"},
           {"at": 0.6, "event": "HOLD on 'commit'"}],
          "The predict-before-reveal beat."),
    role="INSTANCE", section=1, predict=True,
    learn={"question": "How many ticks survive their tests?",
           "action": "Hold the two ticked rows under their tests.",
           "observation": "The viewer commits to a number.",
           "inference": "A committed prediction turns the next beat into evidence.",
           "next_question": "Run the tests."}))

beats.append(beat("B16", "learn 1",
    "Recourse. The appeal belongs to moderators, and it goes to support. The person whose post was flagged? Nothing they can find and use. The tick comes out. "
    "Review. The company's own team, now and then, no named reviewer, no power to halt. Out. "
    "The blank boxes were never in. Zero of five.",
    manim("B16_RunTheTests",
          "Row 3 runs: its tick uncreates, failure mode 'routes to support, no resolution' writes; row 4 runs: tick out, 'the company grades its own work'; rows 2 and 5 write their failure modes 'review reconstructs nothing' and 'no one bears the cost'; the tally at bottom-right writes 'ticked: 0 of 5' with a terracotta dot beside it.",
          [{"at": 0.05, "event": "recourse test runs; tick out; failure mode"}, {"at": 0.45, "event": "review test runs; tick out"},
           {"at": 0.75, "event": "blank rows light their failure modes"}, {"at": 0.88, "event": "'ticked: 0 of 5'"}],
          "The collision: the words that filled the boxes meet the tests; every tick comes out."),
    role="TRANSFORM", section=1,
    learn={"question": "Do the recourse and review ticks survive?",
           "action": "Run each test against its sentence.",
           "observation": "Neither sentence gives the test what it asks for; both ticks come out; the blanks fail too.",
           "inference": "Zero of five: every word was a mention, not a requirement.",
           "next_question": "Is this just an exercise, or does it happen to real systems?"}))

beats.append(beat("B17", "learn 1",
    "This isn't only an exercise. SyRI, a Dutch welfare-fraud scoring system, had recourse and independent review too, on paper and not in function. "
    "In twenty twenty, a court in The Hague struck it down. The court supplied the review and the sanction the system had never built in: "
    "late, from outside, after the harm had landed.",
    manim("B17_SyRI",
          "The A2 column clears; the right column heads 'SyRI · Dutch welfare-fraud scoring' and 'struck down · The Hague · 2020'; Recourse and Independent review rows read 'on paper, not in function'; a terracotta dot travels from the court line to the Review and Sanctions rows, which read 'supplied by the court, late'; a divider rule draws between the columns.",
          [{"at": 0.05, "event": "SyRI heads the right column"}, {"at": 0.25, "event": "recourse and review: on paper"},
           {"at": 0.5, "event": "the court line"}, {"at": 0.7, "event": "review and sanctions: supplied by the court, late"}],
          "A real instance of the same shape: two boxes with words and no function; the tests arrived from a court."),
    role="INSTANCE", section=1,
    learn={"question": "Does a real deployment fail the same way?",
           "action": "Run the same five rows on SyRI.",
           "observation": "Recourse and review existed on paper, not in function; a court supplied review and sanction after the harm.",
           "inference": "Words in the boxes do not stop the harm; the tests arrive anyway, late and from outside.",
           "next_question": "What is the rule we have been using?"}))

beats.append(beat("B18", "learn 1",
    "This deserves its name. A requirement is present when its test passes, not when its word appears. "
    "Five boxes, five tests: an audit instrument you can carry to any deployment. "
    "And the chapter's verdict on a regime that can't tick all five: accountability is a slogan, not a practice.",
    manim("B18_NameIt",
          "The five boxes and names hold at left; a rule draws beside them; the right column writes 'present when the test passes,' / 'not when the word appears' (bold), then 'five tests: an audit instrument', then 'can't tick all five:' / 'a slogan, not a practice' (bold) with a terracotta dot beside it.",
          [{"at": 0.1, "event": "the rule draws"}, {"at": 0.2, "event": "'present when the test passes, not when the word appears'"},
           {"at": 0.5, "event": "'five tests: an audit instrument'"}, {"at": 0.8, "event": "'a slogan, not a practice'"}],
          "The abstraction arrives as the name for what the viewer just watched."),
    role="ABSTRACTION", section=1,
    learn={"question": "What rule have we been using?",
           "action": "State it beside the five boxes.",
           "observation": "Present means the test passes; five tests make an instrument.",
           "inference": "A regime that cannot tick all five is a slogan, not a practice.",
           "next_question": "Back to the four sentences."}))

beats.append(beat("B19", "learn 1",
    "Back to the four sentences. An appeal, a review team, eighteen months. Every sentence is true, and not one passes its test. "
    "And eighteen months without an audit trail is eighteen months nobody could reconstruct. "
    "What the tests don't tell you is who has to hold each box, and why it has to be a person. That's not taught here.",
    manim("B19_BackToTheParagraph",
          "The four fragments return to the right column beside the five empty boxes; each empty box gets its failure mode in dim beneath its name; the 18-month bar returns and its label becomes '18 months nobody could rebuild'; terracotta dot beside it; caption 'not taught: who must hold each box'.",
          [{"at": 0.05, "event": "the four sentences return"}, {"at": 0.35, "event": "boxes empty, failure modes beneath"},
           {"at": 0.6, "event": "the 18-month bar returns; its label turns"}, {"at": 0.9, "event": "boundary caption"}],
          "The HOOK's paragraph and clock return, resolved; the boundary names what was not taught."),
    role="PAYOFF", section=1,
    learn={"question": "So, is anyone accountable?",
           "action": "Put the HOOK's paragraph and bar back beside the tested boxes.",
           "observation": "Four true sentences, zero passed tests; the 18 months was never evidence.",
           "inference": "Accountability here is a slogan, not a practice.",
           "next_question": ""}))

beats.append(beat("BVDT", "verdict",
    "Let's recap with Claude. Five requirements: specifications, audit trail, recourse, independent review, sanctions. "
    "A box ticks when its test passes, not when its word appears. "
    "The four-sentence description passes none of the five; SyRI's recourse and review existed on paper and not in function. "
    "Eighteen months is a clock, not a check. A regime that can't tick all five is a slogan, not a practice.",
    remotion("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": TITLE,
        "artifactLines": ["Five requirements: specifications, audit trail, recourse, independent review, sanctions.",
                          "A box ticks when its test passes, not when its word appears.",
                          "The four-sentence description passes none; SyRI's recourse and review existed on paper only.",
                          "Eighteen months is a clock, not a check. Can't tick all five: a slogan, not a practice."]},
        [{"at": 0.0, "event": "artifact page opens"}, {"at": 0.2, "event": "four verdict lines land"}]),
    lane="bookend", lead_silence_s=0.5, qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}))

YT = ("Pick an AI system I use and find its public description of how its decisions are reviewed and appealed. "
      "Before reading closely, predict how many of five requirements it passes: specifications, audit trail, recourse, independent review, sanctions. "
      "Then run each test: could a reviewer predict what counts as success; could an incident be rebuilt in under an hour; "
      "could an outsider find and use the appeal channel; is a named reviewer outside the team able to halt it; can a named role lose something? "
      "For each failed box, name the failure mode. Where the description is silent, say so.")
beats.append(beat("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT + " "
    "Two things to look for. Did it count silence as a failed test, not a pass? "
    "And does every tick quote the sentence that passes the test, rather than a word that merely sounds right?",
    remotion("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "INFO 7375 · YOUR TURN", "segment": "Run The Five Tests",
        "command": YT, "runningText": "paste this into Claude…",
        "output": ["Check: silence counted as a failed test, not a pass.",
                   "Check: every tick quotes the sentence that passes the test."],
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
    "audience": "INFO 7375 students, and anyone who has read an AI system's 'we review and you can appeal' paragraph and felt reassured",
    "course": "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University",
    "source_doc": "chapters/12-accountability-who-is-responsible-when-the-system-fails.md — §'The five accountability requirements and the tiers they depend on' + checklist table (body list); Application A2; SyRI paragraph of §'The regulatory landscape'. Section S5 of youtube/tldr-sections-12-accountability.md",
    "sections": [{"n": 1, "title": TITLE, "key_case": "Application A2's four-sentence content-moderation description run through the five-requirement checklist (constructed exercise case); SyRI as the real post-shift instance"}],
    "greeting_language": "Zulu (Sawubona)",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "outro_policy": "OUTRO-LOCK §Voice: spoken title + 'At Nik Bear Brown', 1.0 s silent tail padded into the mp3, no jingle.",
    "bookloop_policy": "Course film: carries the INFO 7375 course credit (spoken in B00, on the cards' course line).",
    "tags": ["accountability", "AI audit", "recourse", "independent review", "SyRI", "INFO 7375", "Computational Skepticism", "3Blue1Brown style", "Claude", "Nik Bear Brown"]},
    "beats": beats}
out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"{len(beats)} beats → {out}")
