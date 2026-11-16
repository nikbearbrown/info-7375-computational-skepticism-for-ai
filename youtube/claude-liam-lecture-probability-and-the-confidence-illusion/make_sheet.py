#!/usr/bin/env python3
"""make_sheet.py: beat_sheet.json + SHOTLIST.md for claude-liam-lecture-probability-and-the-confidence-illusion.
Lecture 2 of 13, INFO 7375 Computational Skepticism for AI. Source: chapters/02-probability-uncertainty-and-the-confidence-illusion.md
(read only; HEAD side of every merge block; see ACTS.md). Numbers follow FACTCHECK.md. Carries audio forward when narration is unchanged."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from beats_data import ACTS, BODY
SLUG = HERE.name
TITLE = "Probability and the Confidence Illusion"
SPOKEN_TITLE = "Probability and the Confidence Illusion."
SERIES = "Computational Skepticism for AI"
PLAYLIST = "INFO 7375 — Computational Skepticism for AI (Lectures)"
COURSE = "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University"
BOOKENDS = {"BOPEN", "BIDEA", "BDEFS", "BVDT", "BHTF", "BOUT"}

def common(bid, act, narration):
    return {"beat_id": bid, "act": act, "narration_text": narration,
            "estimated_duration_s": round(len(narration.split()) / 2.6 + 0.6, 2),
            "voice": "am_onyx", "engine": "kokoro", "persona": "liam"}

def manim(bid, act, narration, cls, about, runner, reason, gate="SHOW", motion=None):
    b = common(bid, act, narration)
    b.update(lane="manim", proof_gate=gate, routing={"about": about, "runner_up": runner, "reason": reason},
             shot={"type": "GRAPHIC", "source": "own", "visual_intent": about, "motion_claim": motion or reason,
                   "show": [{"at": 0.1, "event": "the cast is on the stage"}, {"at": 0.5, "event": "the spoken step lands as motion"},
                            {"at": 0.9, "event": "hold the result"}], "manim": {"class": cls}})
    b["qc"] = {"sparse_by_design": True, "sparse_reason": "Drawn diagram on the cream stage; negative space is the style, the motion carries the claim."}
    return b

def remotion(bid, act, narration, pattern, props, about, runner, reason, gate="SHOW"):
    b = common(bid, act, narration)
    b.update(lane="bookend" if bid in BOOKENDS else "remotion", proof_gate=gate,
             routing={"about": about, "runner_up": runner, "reason": reason},
             shot={"type": "REMOTION", "source": "own", "visual_intent": about, "motion_claim": reason,
                   "show": [{"at": 0.12, "event": "establish"}, {"at": 0.4, "event": "the spoken content lands"}, {"at": 0.85, "event": "hold"}],
                   "remotion": {"pattern": pattern, "props": props}})
    return b

bopen = common("BOPEN", "Opening",
    f"{SERIES}. {SPOKEN_TITLE} Learn why a confident number is not a correct number, and the four questions that check it before you trust it.")
bopen.update(lane="bookend", proof_gate="CARD",
    routing={"about": "Film identity and payoff", "runner_up": "Minimal title card", "reason": "The lecture skill's approved first beat."},
    shot={"type": "CARD", "source": "own", "template": "lecture-title-slide-16x9", "narration_contract": "playlist-title-summary-v1",
          "motion": "hold", "visual_intent": "Professor Bear portrait, exact film title, series position and payoff, visible from frame zero.",
          "show": [{"at": 0, "event": "Complete populated lecture opener visible for the whole narration"}]},
    qc={"sparse_by_design": True, "sparse_reason": "Identity card; teaching motion starts in BIDEA."})

bidea = remotion("BIDEA", "Opening",
    "Hola. This is Liam, in for Bear, with a lecture for INFO seventy-three seventy-five, Computational Skepticism for AI. "
    "A model hands you a score of point nine four, and the answer looks settled. It is not settled yet.",
    "BrutalistHesitantWriter",
    {"text": "The model gave a score of point nine four,\nso the answer is almost surely right",
     "triggerWords": "almost surely right", "replacementWords": "only as good as its record",
     "fontSize": 64, "charMs": 30, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
    "The belief the film corrects", "Overview card", "The writer types the newcomer's belief and corrects one phrase into the lecture's thesis.")
bidea.update(lead_silence_s=0.8)
bidea["qc"] = {"sparse_by_design": True, "sparse_reason": "Hesitant-writer opening: the correction is the motion."}

TERMS = [("Event", "A set of outcomes you care about"), ("Classifier", "A model that sorts cases into classes"),
         ("Confidence score", "The number a model attaches to its answer"), ("Held-out data", "Cases kept back from training"),
         ("Distribution", "How often each value occurs"), ("Variance", "How spread out values are")]
bdefs = remotion("BDEFS", "Terms",
    "Six terms. An event is a set of outcomes you care about. A classifier is a model that sorts cases into classes. A confidence score is the number it attaches to its answer. "
    "Held-out data is cases kept back from training. A distribution is how often each value occurs. And variance is how spread out values are.",
    "ClaudeDefinitions", {"title": "Terms In This Lecture", "terms": [{"term": t, "meaning": m} for t, m in TERMS], "folderLabel": "@NikBearBrown"},
    "Prerequisite vocabulary", "Library icon row", "Six words the acts lean on, one plain line each.", "CARD")
bdefs["qc"] = {"sparse_by_design": True, "sparse_reason": "Terms card: six prerequisites, one line each."}

B = [bopen, bidea, bdefs]
cur_act = None; n = 0
for ai, name, narr, about, runner, reason in BODY:
    if ai != cur_act:
        cur_act = ai
        aid = f"A{ai}"
        B.append(manim(aid, ACTS[ai-1], ACTS[ai-1] + ".", f"{aid}_Title", f"Act title: {ACTS[ai-1]}", "FormACard",
                       "A drawn act title on the same stage keeps one look; the numeral turns once.", gate="CARD",
                       motion="the act numeral ticks as the title lands"))
    n += 1
    bid = f"B{n:02d}"
    cls = bid + "_" + "".join(w for w in name.replace("'", "").split())
    if name == "Run It":
        lines = (HERE / "evidence/bayes_run.stdout.txt").read_text().rstrip("\n").split("\n")
        b = remotion(bid, ACTS[ai-1], narr, "CCPlainShell",
                     {"title": "python3 bayes_run.py (recorded output)", "fontSize": 40, "startCue": 6, "lineGap": 14, "lines": lines},
                     about, runner, "SHOW-THE-THING rung 1: the real script's real output, line by line, labelled as recorded output.")
        b["shot"]["evidence"] = "evidence/bayes_run.py, evidence/bayes_run.stdout.txt"
    else:
        b = manim(bid, ACTS[ai-1], narr, cls, about, runner, reason)
    B.append(b)

recaps = ["Probability is a degree of belief, conditional on what you know.",
          "A chain of steps is a product, so confidence shrinks along it.",
          "A positive from a rare-event test is mostly false alarms.",
          "A stated probability is only as good as its calibration curve.",
          "Averages fail when one rare cost dominates.",
          "Ask four questions: base rate, calibration, cost, what changed."]
recap = remotion("BVDT", "Recap", "Let's recap with Claude. " + " ".join(recaps), "ClaudeVerdictArtifact",
    {"artifactTitle": "Recap", "artifactHeading": "INFO 7375 · Lecture 2", "artifactLines": recaps, "brandLabel": "@NikBearBrown", "lectureLayout": True},
    "Six-line recap", "Summary diagram", "One bare sentence per act-level idea; nothing new.")
recap["lead_silence_s"] = 0.5
PROMPT = ("I am auditing a confident number: a vendor's accuracy claim for a detector. First ask me for its base rate, sensitivity and specificity. "
          "Then compute, showing the arithmetic, what fraction of everything it flags is genuinely positive. Name the missing number, "
          "and state the condition under which the reported confidence would be false.")
task = remotion("BHTF", "Your turn", PROMPT, "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "INFO 7375 COMPUTATIONAL SKEPTICISM · LECTURE 2 · YOUR TURN", "segment": "Audit One Confident Number", "command": PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: the arithmetic uses a base rate, not the accuracy figure alone.", "Check: it names one number the vendor did not report."],
     "folderLabel": "@NikBearBrown", "largeText": True},
    "Transfer task", "Worksheet", "The viewer gets a usable prompt and two checks of their own.")
outro = remotion("BOUT", "Outro", SPOKEN_TITLE + " At Nik Bear Brown.", "ClaudeTitleOutro",
    {"title": TITLE, "slug": SLUG, "subline": "", "handle": "@NikBearBrown", "lectureLayout": True},
    "Locked title and channel sign-off", "None", "The exact title spoken over the locked outro.")
outro.update(kind="outro_voice", tail_silence_s=1.0)
outro["qc"] = {"sparse_by_design": True, "sparse_reason": "Locked outro centres only title, handle and mascot."}
B += [recap, task, outro]

old = {}
if (HERE / "beat_sheet.json").exists():
    old = {x["beat_id"]: x for x in json.loads((HERE / "beat_sheet.json").read_text()).get("beats", [])}
for x in B:
    prior = old.get(x["beat_id"], {})
    if prior.get("narration_text") == x["narration_text"]:
        for key in ("audio_file", "actual_duration_s"):
            if key in prior: x[key] = prior[key]
    if x["shot"]["type"] == "REMOTION":
        x["shot"]["remotion"]["props"]["durationSeconds"] = x.get("actual_duration_s", x["estimated_duration_s"])

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "spoken_title": SPOKEN_TITLE,
    "topic": "Why a confident number is not a correct number: conditioning, Bayes, calibration, heavy tails",
    "skill": "lecture", "style_preset": "lecture", "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro", "clock": "narration", "palette": "claude",
    "register": "Teardown", "fps": 24, "width": 3840, "height": 2160, "aspect_ratio": "16:9", "caption_policy": "sidecar",
    "course": COURSE, "audience": "INFO 7375 students (Fall 2026) and Claude Code practitioners",
    "series_title": SERIES, "playlist": PLAYLIST, "series_numbered": True, "series_video_number": 2, "series_video_count": 13,
    "series_entry_video": "Video 1 · The Skeptic's Toolkit",
    "lecture_opening_description": "Why confident numbers fail, and four checks",
    "lecture_opening_title_lines": ["Probability and the", "Confidence Illusion"],
    "lecture_opening_template": "lecture-title-slide-16x9",
    "source_doc": "info-7375-computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md (HEAD side of each merge block)",
    "bookend_exempt": ["cold-open"], "bookend_exempt_reason": "lecture skill: opens on the narrated card then the hesitant writer; no composer cold open.",
    "tags": ["probability", "Bayes theorem", "base rate", "calibration", "heavy tails", "INFO 7375", "Computational Skepticism", "Liam", "Lecture"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")

rows = [f"# SHOTLIST — {TITLE}", "",
 "**What.** One row per beat: what the sentence is about, the lane picked, the runner-up auditioned, and why the pick wins (BEST-BEAT LAW).",
 "**Why.** The pick must be the picture a viewer understands with the sound off; a runner-up proves the beat was auditioned.",
 "**Found.** 66 body beats: 65 Manim drawings and 1 real script run (CCPlainShell), plus 10 act titles and 6 bookends. Library asked first (`./art scenes`): no registered scene carries these numbers, so the mechanisms are drawn; where the claim is a moving quantity (a running mean, a reliability diagram, a grid of people) Manim is the lane because the motion is the claim. No tool, app or site is the subject, so no capture is needed. Isometric lane auditioned for the tool-call chain, alert fatigue and the two engineers: the tree, the table and the portraits carry the claim with less decoration; the isometric inbox is used for alert fatigue only if it passes its own drawing laws.", "",
 "| beat | about | lane picked | runner-up | why this one wins |", "|---|---|---|---|---|"]
for x in B:
    r = x["routing"]
    pick = x["shot"].get("manim", {}).get("class") or x["shot"].get("remotion", {}).get("pattern") or x["shot"].get("template")
    lane = "Manim" if x["shot"]["type"] == "GRAPHIC" else ("Remotion" if x["shot"]["type"] == "REMOTION" else "Card")
    rows.append(f"| {x['beat_id']} | {r['about']} | {lane} · `{pick}` | {r['runner_up']} | {r['reason']} |")
rows += ["", "## Tool beats and their SHOW-THE-THING rung", "", "| beat | tool | rung | what is on screen |", "|---|---|---|---|",
         "| Run It | Python (this reel's own script) | 1 · run | `evidence/bayes_run.py` and its verbatim stdout, labelled recorded output |",
         "| (none) | any product UI | — | No product is shown. The sepsis model, the classifier and the pipeline are described, never drawn as a product screen. |"]
(HERE / "SHOTLIST.md").write_text("\n".join(rows) + "\n")
words = sum(len(x["narration_text"].split()) for x in B)
print(len(B), "beats;", words, "words;", round(sum(x.get("actual_duration_s", x["estimated_duration_s"]) for x in B) / 60, 1), "min est")
