# BUILD-PROMPT — claude-liam-computational-epistemology

Paste-ready Claude Code prompt. Run from `books/`. Free pipeline throughout
(Kokoro `am_onyx`); no paid calls anywhere in this build. Never publishes.

```
Read brutalist-art/skills/make/deep-explainer/SKILL.md completely, then its
three reference files, then the parent chain it names (ai-explainer SKILL.md;
explainer MOTION.md + REMOTION.md). Standing rules #1–#4 in
brutalist-art/EXAMPLES-CAMPAIGN.md govern.

Reel: computational-skepticism-for-ai/youtube/claude-liam-computational-epistemology

State check first: read beat_sheet.json, BUILD-LOG.md, FACTCHECK.md and
report which gates are already signed. Then continue from the first unsigned
gate, in order:

1. GATE F (factcheck) — verify every open row in FACTCHECK.md against the
   source doc and primary sources; apply fixes; present the table. STOP for
   human sign-off.
2. GATE P (narration) — compile the animated slate previz (slates play each
   beat's show events at estimated timing — never a page of text) and present
   it with the lane histogram. STOP for human sign-off. No audio before this
   signature.
3. Audio — python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py
   <reel> (Kokoro am_onyx, free). Measure; actual_duration_s becomes the
   clock; run the align step for the word clock.
4. Gate D2 — write SHOPPING.md from the LOCKED durations per
   deep-explainer/reference/shopping-list.md (tier-tagged; tier-2/3 rights
   checks escalate to the human; motion assets request more than the window).
   Present it. STOP — the human sources the pantry.
5. Gate D1 previz — ./brutalist-art/art run <reel> (full compile: Manim +
   Remotion beats real, vox slots as slates, --review burn-in). Report; the
   human watches.
6. After pantry drops land: run the pantry intake, set shot.focus per still,
   verify sidecars, rerun — only changed slots recompile.
7. VISUAL QC LAW pass per CLAUDE-CODE-VISUAL-QC-CHECK.md (sample frames,
   READ the PNGs, 9-point rubric, _qc/REPORT.md; fix root causes and
   re-render to zero BLOCKER/MAJOR).
8. ./brutalist-art/art final <reel> → clean master. Report and stop. Do not
   publish; do not flip anything public.

Vox-run continuity: R1 (B14→B15) and R2 (B27→B28→B29) carry authored handoff
blocks — first frames must reproduce the prior beat's serialized values.
Render Remotion only via runtime/scripts/remotion_scenes.py, foreground,
--concurrency=1. Log every human note in BUILD-LOG.md before acting on it.
If anything needed is missing, log MISSING: in BUILD-LOG.md and stop that
thread rather than improvising.
```
