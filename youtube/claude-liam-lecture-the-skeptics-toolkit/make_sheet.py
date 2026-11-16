#!/usr/bin/env python3
"""make_sheet.py — builds beat_sheet.json for the lecture. Safe to re-run: it carries audio_file / actual_duration_s forward
and fills every Remotion beat's durationSeconds from the measured audio.

  narration.py        every spoken line (the clock)
  lanes/*.json        per-beat lane decisions written by the act builders:
                      { "B03": {"lane": "manim", "class": "B03_GoodColumn", "visual_intent": "...", "motion_claim": "...",
                                "show": [{"at": 0.2, "event": "..."}], "runner_up": "...", "why": "...", "sparse": true},
                        "B14": {"lane": "remotion", "pattern": "CCPlainShell", "props": {...}, ...} }
                      A Remotion props value of "__AUDIO__" under durationSeconds is replaced by the measured audio.
A body beat with no lane entry is written as a pending Manim beat (compiles as a slate until a scene exists).
"""
import json, glob
from pathlib import Path
import narration as N

HERE = Path(__file__).resolve().parent
OUT = HERE / "beat_sheet.json"
prev = {}
if OUT.exists():
    for b in json.loads(OUT.read_text())["beats"]:
        prev[b["beat_id"]] = b

lanes = {}
for f in sorted(glob.glob(str(HERE / "lanes" / "*.json"))):
    lanes.update(json.loads(Path(f).read_text()))

def est(n):  # words / 2.5 per second
    return round(len(n.split()) / 2.5, 1)

def carry(b):
    p = prev.get(b["beat_id"])
    if p:
        for k in ("actual_duration_s", "audio_file"):
            if k in p:
                b[k] = p[k]
    return b

def fill_audio(props, dur):
    if isinstance(props, dict):
        return {k: (round(dur, 2) if v == "__AUDIO__" else fill_audio(v, dur)) for k, v in props.items()}
    if isinstance(props, list):
        return [fill_audio(v, dur) for v in props]
    return props

def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate, "narration_text": narration,
         "estimated_duration_s": est(narration), "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    carry(b)
    dur = b.get("actual_duration_s")
    if dur:
        b["shot"]["remotion"]["props"] = fill_audio(b["shot"]["remotion"]["props"], dur)
    return b

beats = []

# ── BOPEN ─ narrated portrait/title card (template lecture-title-slide-16x9) ──────────────────────────────
beats.append(carry({"beat_id": "BOPEN", "act": "Opening", "lane": "bookend", "proof_gate": "CARD", "narration_text": N.BOPEN,
    "estimated_duration_s": est(N.BOPEN), "voice": "am_onyx", "engine": "kokoro", "persona": "liam",
    "shot": {"type": "CARD", "source": "own", "template": "lecture-title-slide-16x9", "narration_contract": "playlist-title-summary-v1",
             "motion": "hold", "visual_intent": "Film identity and short teaching description, visible immediately; Liam speaks playlist, title, summary",
             "show": [{"at": 0, "event": "Complete portrait/title/series card visible"}]},
    "qc": {"sparse_by_design": True, "sparse_reason": "Approved identity card; teaching motion resumes in BIDEA."}}))

# ── BIDEA ─ hesitant writer ─────────────────────────────────────────────────────────────────────────────
beats.append(remotion("BIDEA", "the question", N.BIDEA, "BrutalistHesitantWriter",
    {"text": "A skeptic is someone\nwho distrusts everything.",
     "triggerWords": "distrusts everything", "replacementWords": "performs a method",
     "fontSize": 70, "charMs": 24, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 4, "jitter": 20,
     "seed": N.SLUG, "banner": "", "brandLabel": "@NikBearBrown"},
    [{"at": 0.0, "event": "types the naive definition"}, {"at": 0.6, "event": "backspaces 'distrusts everything', types 'performs a method'"}],
    lead_silence_s=0.8,
    motion_claim="The writer types the newcomer's definition and corrects it into the real one.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}))

# ── BDEFS ───────────────────────────────────────────────────────────────────────────────────────────────
beats.append(remotion("BDEFS", "terms", N.BDEFS, "ClaudeDefinitions",
    {"title": "Terms In This Lecture",
     "terms": [{"term": "Validation", "meaning": "checking a model on data it did not train on"},
               {"term": "Induction", "meaning": "trusting a pattern because it held before"},
               {"term": "Falsifiable", "meaning": "names the result that would prove it wrong"},
               {"term": "Agent", "meaning": "an AI that takes actions with tools"}],
     "durationSeconds": "__AUDIO__", "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'Validation' lands"}, {"at": 0.35, "event": "'Induction' lands"}, {"at": 0.6, "event": "'Falsifiable' lands"}, {"at": 0.82, "event": "'Agent' lands"}],
    gate="CARD", qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one plain line each."}))

# ── BODY ─ one best visual per beat (lanes/*.json) ──────────────────────────────────────────────────────
for bid, ai, text in N.BODY:
    act = f"{N.ACTS[ai][0]} · {N.ACTS[ai][1]}"
    L = lanes.get(bid)
    if L is None and bid.startswith("A") and bid[1:].isdigit():
        L = {"lane": "remotion", "pattern": "FormACard", "props": {"lines": [N.ACTS[ai][1]]}, "proof_gate": "CARD",
             "visual_intent": "Act title", "motion_claim": "Act divider", "show": [{"at": 0.1, "event": "act title"}],
             "runner_up": "first picture of the act carrying the title", "why": "short act-title boundary (one breath per act)",
             "sparse": True, "sparse_reason": "Brief act-title card."}
    if L is None:
        b = {"beat_id": bid, "act": act, "lane": "manim", "proof_gate": "SHOW", "narration_text": text,
             "estimated_duration_s": est(text), "voice": "am_onyx", "engine": "kokoro",
             "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": "PENDING — no lane entry yet", "show": [],
                      "manim": {"class": f"{bid}_Pending"}, "motion_claim": "pending"},
             "pending": True}
        beats.append(carry(b))
        continue
    lane = L["lane"]
    b = {"beat_id": bid, "act": act, "lane": lane, "proof_gate": L.get("proof_gate", "SHOW"), "narration_text": text,
         "estimated_duration_s": est(text), "voice": "am_onyx", "engine": "kokoro"}
    if lane == "manim":
        b["shot"] = {"type": "GRAPHIC", "source": "own", "visual_intent": L["visual_intent"], "show": L.get("show", []),
                     "manim": {"class": L["class"]}, "motion_claim": L["motion_claim"]}
    else:  # remotion / capture / card
        b["shot"] = {"type": "REMOTION", "source": "own", "visual_intent": L["visual_intent"], "show": L.get("show", []),
                     "remotion": {"pattern": L["pattern"], "props": L.get("props", {})}, "motion_claim": L["motion_claim"]}
    if L.get("sparse", True):
        b["qc"] = {"sparse_by_design": True, "sparse_reason": L.get("sparse_reason",
                   "Lecture body beat: one object or scene on a cream stage with the voice carrying the explanation; only underfill/clustered are waived.")}
    for k in ("lead_silence_s", "tail_silence_s", "kind"):
        if k in L:
            b[k] = L[k]
    b["lecture"] = {"runner_up": L.get("runner_up", ""), "why": L.get("why", "")}
    carry(b)
    dur = b.get("actual_duration_s")
    if dur and lane != "manim":
        b["shot"]["remotion"]["props"] = fill_audio(b["shot"]["remotion"]["props"], dur)
    beats.append(b)

# ── BVDT ─ recap (one bare sentence per act-ish, 6 lines: the card paginates in twos) ───────────────────────
def _pages():
    d = prev.get("BVDT", {}).get("actual_duration_s")
    if not d: return []
    full = N.BVDT_NARRATION; lead = 0.5
    def t(i):  # seconds at which line i starts (char share of narration x audio, after the lead pause)
        return lead + (d - lead) * full.index(N.BVDT_LINES[i]) / len(full)
    return [0, int(max(0, t(2) - 0.4) * 30), int(max(0, t(4) - 0.4) * 30)]
beats.append(remotion("BVDT", "verdict", N.BVDT_NARRATION, "ClaudeVerdictArtifact",
    {"artifactTitle": "Recap", "lecturePageFrames": _pages(), "durationSeconds": "__AUDIO__", "brandLabel": "@NikBearBrown", "lectureLayout": True, "artifactHeading": "INFO 7375 · Lecture 1", "artifactLines": N.BVDT_LINES},
    [{"at": 0.0, "event": "artifact page opens"}, {"at": 0.2, "event": "six recap lines land in narration order"}],
    lead_silence_s=0.5, qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}))

# ── BHTF ─ your turn ───────────────────────────────────────────────────────────────────────────────────────
beats.append(remotion("BHTF", "your turn", N.BHTF_NARRATION, "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "INFO 7375 COMPUTATIONAL SKEPTICISM · LECTURE 1 · YOUR TURN", "segment": "Run the Four Moves", "largeText": True, "command": N.BHTF_PROMPT,
     "runningText": "paste this into Claude…", "output": N.BHTF_CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.12, "event": "the prompt types in full"},
     {"at": 0.85, "event": "two check lines land"}]))

# ── BOUT ─ channel outro (claude-liam → ClaudeTitleOutro, OUTRO-LOCK) ───────────────────────────────────────────
bout = {"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
        "narration_text": f"{N.TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
        "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                 "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": N.TITLE, "slug": N.SLUG, "handle": "@NikBearBrown", "subline": "", "lectureLayout": True}}},
        "kind": "outro_voice", "tail_silence_s": 1.0,
        "qc": {"sparse_by_design": True, "sparse_reason": "Locked outro centres only title, handle and a small mascot; no filler."}}
beats.append(carry(bout))

sheet = {"metadata": {
    "slug": N.SLUG, "title": N.TITLE, "topic": "INFO 7375 COMPUTATIONAL SKEPTICISM · LECTURE 1", "skill": "lecture", "style_preset": "lecture",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "sidecar", "greeting_language": "German (Hallo)",
    "course": "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University",
    "audience": "INFO 7375 students (Fall 2026) and Claude Code practitioners",
    "source_doc": "/Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md",
    "source_sha256": "f88b551ad76c3ac563a88b224b82f8b6b41875be1ab30f9ba72e5434497b3825",
    "playlist": "INFO 7375 — Computational Skepticism for AI (Lectures)", "chapter_number": 1,
    "series_title": "Computational Skepticism for AI", "series_video_number": 1, "series_video_count": 13,
    "series_entry_video": "Video 1 · The Skeptic's Toolkit",
    "lecture_opening_description": "Four moves for checking any AI output",
    "lecture_opening_template": "lecture-title-slide-16x9",
    "tags": ["skepticism", "AI evaluation", "verification", "falsifiability", "Nik Bear Brown", "Northeastern"]},
    "beats": beats}
OUT.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
pend = sum(1 for b in beats if b.get("pending"))
print(len(beats), "beats;", pend, "pending; est", round(sum(b.get("actual_duration_s") or b["estimated_duration_s"] for b in beats)), "s")
