# REBUILD-PROMPT.md — claude-liam-a-p-value-is-not-a-verdict

Paste-ready. Run from `books/` in a local Claude Code session.
This is a REBUILD of an already-shipped reel — the beat sheet, narration, and
fact-check are LOCKED. The job is to re-render every visual clean, recompile,
gate, and re-stage. Written 2026-08-30 after the TOPOST review found
text-on-top-of-text in B15.

---

```
Rebuild the deep-explainer reel at
computational-skepticism-for-ai/youtube/claude-liam-a-p-value-is-not-a-verdict/.

READ FIRST:
  brutalist-art/skills/make/deep-explainer/SKILL.md
  brutalist-art/skills/make/ai-explainer/SKILL.md
  the reel's BUILD-LOG.md — ALL of it, especially the 2026-08-30 HUMAN
    FEEDBACK entry (B15 text-on-text) and the Simon's Ant layout-law entry
  the reel's FACTCHECK.md

LOCKED — DO NOT TOUCH:
  beat_sheet.json narration, beat order, lane mix, and durations. 25 beats:
  B00 B01–B21 BVDT BHTF BOUT. Do not re-author anything. The B20 source-audit
  gate was already run and B20 ships as written.
  mp3/beat-*.mp3 — all 25 exist and are the measured master clock. REUSE them.
  Regenerate a beat's audio ONLY if its file is missing or ffprobe says it is
  corrupt, and then write the new measured duration back to actual_duration_s.

CHANNEL: claude-liam, Kokoro am_onyx. FREE — no ElevenLabs, no Higgsfield,
no paid call of any kind. This reel requests NO media from the human: the five
former vox slots (B05 B08 B13 B16 B19) were converted to Manim fallbacks and
stay Manim. pantry/ is empty and stays empty.

STEP 1 — ledger
  ./brutalist-art/art todo computational-skepticism-for-ai/youtube/claude-liam-a-p-value-is-not-a-verdict
  Confirm 25 beats, zero gen-AI requests, zero vox slots. Any drift → stop and report.

STEP 2 — Manim scenes (13), re-rendered from the EXISTING scenes.py
  scenes.py is current and already contains the 2026-08-30 B15 fix
  (B15_WallWithDoors: door_w 3.4, door labels size 24, and the door labels are
  INSIDE check_overlaps). Do not regress any of that. Re-render all 13 Manim
  beats fresh into manim/, then copy into place per the sheet.

  LAYOUT LAW (Simon's Ant): no hardcoded move_to([x,y,0]); labels attach with
  next_to(..., buff=...); rows arrange(); text in a box gets width from the
  box; the bbox-overlap assertion runs at the end of every construct() and it
  must include EVERY visible Text — a label omitted from the check is how the
  B15 defect shipped. If any scene's overlap check skips a mobject, add it
  before rendering.

  PANGO SPACE-COLLAPSE (this Mac): Manim Text() drops some single spaces —
  words fuse in the render though the source is correct. After rendering,
  READ frames and look for fused words; the fix is doubling the space at the
  fused boundary in the source string and re-rendering. Never ship a frame you
  haven't looked at.

  Palette: cream #FAF9F5, ink #3D3929, ONE terracotta #D97757 moment per beat.
  MUTE is not a hiding place — never recolor a label to sneak it past a gate.

  The four REVERSAL beats keep their reversals (do not soften to captions):
    B07 the switch is drawn and STRUCK THROUGH; bar descends to 57.2%
    B11 the 10x10 alarm grid physically SORTS into 8 ink / 92 terracotta
    B15 the IMPOSSIBLE wall opens two doors and RELABELS to UNBUILT
    B20 the search sweep PASSES THROUGH the paper; quoted figures hollow

STEP 3 — Remotion scenes (12: 7 body + 5 bookends)
  ONLY via:
    python3 brutalist-art/runtime/scripts/remotion_scenes.py \
        computational-skepticism-for-ai/youtube/claude-liam-a-p-value-is-not-a-verdict
  Foreground, --concurrency=1. Never hand-roll npx remotion render.
  Patterns: ClaudeComposerAsk (B00, B10, BHTF) · DeckPattern (B01, B04, B09,
  B21) · ChipGrid (B06, B14, B17) · ClaudeVerdictArtifact (BVDT, five
  artifactLines — verify no overflow in the rendered frame) ·
  ClaudeTitleOutro (BOUT). Match every props object to the component's zod
  schema before rendering.

STEP 4 — compile
  ./brutalist-art/art run computational-skepticism-for-ai/youtube/claude-liam-a-p-value-is-not-a-verdict
  Expect ~369s runtime. compile.py is already pinned to -ar 48000 after
  loudnorm; verify anyway:
    ffprobe the cut → audio MUST be 48000 Hz AAC. 96000 Hz = the old loudnorm
    bug resurfaced — stop and report, do not ship it.

STEP 5 — gates, with eyes
  GATE T: python3 brutalist-art/runtime/scripts/type_check.py → TYPECHECK.md,
          zero FAIL.
  VISUAL QC: sample every beat at 15/50/85% AND read the PNGs. You are looking
  specifically for the two defects this reel has actually shipped with:
    (a) text on top of text — any label touching or overprinting another
        (B15's door labels vs the wall label is the worked example);
    (b) fused words from the Pango bug.
  Fix root causes in scenes.py, re-render, recompile, re-check. An mp4 probe
  is a file check and never counts as QC.
  GATE AUDIO: listen-check the TAIL — sample audio levels in the last 30s.
  BVDT, BHTF, and BOUT are all narrated; a silent tail is a failure.

STEP 6 — final + re-stage
  ./brutalist-art/art final computational-skepticism-for-ai/youtube/claude-liam-a-p-value-is-not-a-verdict
  python3 brutalist-art/runtime/scripts/stage_publish.py \
      computational-skepticism-for-ai/youtube/claude-liam-a-p-value-is-not-a-verdict
  Copy the staged master + <slug>.srt + <slug>.md into books/youtube/TOPOST/
  (replacing the existing ones) and update the reel's entry in
  books/youtube/TOPOST/staged.json with a note: "full visual rebuild
  <date>: all 13 Manim + 12 Remotion beats re-rendered; audio reused".

DO NOT PUBLISH to YouTube. Staging to TOPOST is the end of this job; Bear
reviews from there.

Log everything in BUILD-LOG.md, human feedback first. REPORT: runtime, audio
sample-rate check, TYPECHECK status, per-beat QC summary (name any frame you
fixed and why), and confirmation of the TOPOST re-stage.
```

---

## Notes for whoever runs this

- **This is a re-render, not a re-think.** Everything creative is locked; if a
  visual can't be built without changing narration or beat order, stop and
  report instead of improvising.
- The 2026-08-30 B15 patch is already in `scenes.py` — the rebuild inherits it.
  The point of rebuilding is one clean generation of every clip through the
  tightened checks, not re-fixing B15.
- The five converted vox beats are permanently Manim. If any tool asks for
  pantry stills, something is reading a stale plan — the current
  `beat_sheet.json` wins.
