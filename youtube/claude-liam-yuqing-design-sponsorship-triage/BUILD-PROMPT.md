# BUILD-PROMPT — Claude, Defensible (`claude-liam-yuqing-design-sponsorship-triage`)

**Mode: unattended → full-length SLATE PREVIZ to view.** Paste into Claude Code from your
`books/` root (where `brutalist-art/` lives), under
`claude --dangerously-skip-permissions`. Runs start-to-slate-cut without stopping for gates
and leaves you a watchable MP4 to review pacing before any pantry sourcing.

---

```
Build a full-length SLATE PREVIZ of the deep-explainer reel at
books/computational-skepticism-for-ai/youtube/claude-liam-yuqing-design-sponsorship-triage/.
Run UNATTENDED — do not stop for human gates; I am pre-authorizing them. Deliver a
watchable slate cut, not a final.

Read beat_sheet.json, PLAN.md, SOURCES.md, and SOURCE-PROMPT.md first. Then:

1. SCHEMA RECONCILE. Conform beat_sheet.json to runtime/schema/beat_sheet.schema.json
   exactly (field names, scene keys, shot/vox_run/handoff). Do not change content, lanes,
   narration, act order, or the Onda code-block. Keep the spine: ClaudeComposerAsk cold open
   (ask answered) → body → ClaudeVerdictArtifact → ClaudeComposerAsk "Your turn." →
   ClaudeTitleOutro. Enforce FIRST NAME ONLY — "Yuqing" / "Professor Bear"; fail the run if
   a surname appears anywhere.

2. LANE-MIX LINT (report only, don't block). Expected: VOX ~19%, MANIM ~24%, REMOTION ~29%,
   CARD ~29%. Vox share clears the 15–30% band; no same-lane run >2. If you want MANIM nearer
   25%, you may split one Manim beat — otherwise leave as authored.

3. AUDIO (no GATE P stop — unattended, free voice). Generate narration with Kokoro am_onyx
   (generate_audio.py). NO ElevenLabs. Per-beat mp3 durations become the clock; align writes
   the word clock; faster-whisper captions.

4. SLATE PREVIZ (Gate D1) — THE DELIVERABLE. ./brutalist-art/art run
   <reel> --review. The 4 vox beats (B04, B05, B10, B13) render as SLATES (beat id +
   narration line + terracotta PIPELINE pointer). Manim and Remotion beats render for real
   (they're free): the Onda code-block (specialty_occupation_defensibility), the Manim
   fragments (branch reweight-or-new-signal, settled-vs-contested, three-signals-three-
   treatments, overfit-thin-data, converge-new-signal), the ChipGrid, the illustrations
   (has-sponsored-vs-would-survive, surface-defensibility, design-vs-companywide-sponsorship),
   and the ClaudeComposerAsk / Verdict / TitleOutro bookends. Audio is real. Burn in the
   --review overlay.

5. QUICK QC (automated, non-blocking). ffprobe duration + frame count, and sample a few
   frames per act to confirm no obvious clipping/offscreen; log _qc/REPORT.md. Do NOT do
   the full frame-by-frame VISUAL QC LAW pass — that's for the review cut, not this slate.

6. STOP. Output the slate MP4 (and its path) for me to watch. Do NOT source pantry stills,
   do NOT write SHOPPING.md, do NOT run `art final`, do NOT publish. Print a one-screen
   summary: runtime, beat count, lane histogram, the 4 slate slots awaiting stills, and any
   schema-reconcile changes you made.

Honor the standing laws in what you DO render: COLD OPEN (ClaudeComposerAsk first),
ILLUSTRATE (UI only at cold open / ask micro-beats / verdict / handoff / outro), ASK→RESULT
(B06→B07), SHOW-DON'T-TELL, SPARK-LINE, FILL-THE-CANVAS, LOGO bug, HANDOFF (prompt read +
discussed), OUTRO (title restate), IN-FOR-BEAR (Liam signs in at B00, signs off at O01).
Retint deck patterns to the claude stage (cream #F2F0E9, ink #3D3929, accent #D97757). Keep
the specialty-occupation framing as a mechanism ("does the role require a specific relevant
degree"); no approval-rate or filing-count numbers on screen.
```

---

## After you watch the slate cut
The 4 slate slots (B04, B05, B10, B13) are the only things standing between this and a review
cut. When ready, drop stills into `pantry/` (all Tier 1 illustrative — see each beat's
`pantry_note`), re-run `art run` (only changed slots recompile), then the VISUAL QC LAW pass
and `art final`. Never publishes — public is a manual Studio flip.
