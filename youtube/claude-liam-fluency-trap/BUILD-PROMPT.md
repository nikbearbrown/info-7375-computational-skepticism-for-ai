# BUILD-PROMPT — claude-liam-fluency-trap

Paste-ready Claude Code prompt. Run from `books/`. Free pipeline (Kokoro
am_onyx); no paid calls; never publishes. This is PASS 1 — machine-side
everything; the human shops SHOPPING.md in parallel. (Pass 2 lives at the
bottom.)

```
Read brutalist-art/skills/make/deep-explainer/SKILL.md completely, then its
reference/ files, then the parents it names (ai-explainer SKILL.md; explainer
SKILL.md + MOTION.md + REMOTION.md). Standing rules #1–#4 in
brutalist-art/EXAMPLES-CAMPAIGN.md govern. Free pipeline only — no paid
calls, never publish.

Reel: computational-skepticism-for-ai/youtube/claude-liam-fluency-trap
State: audio LOCKED (36 Kokoro mp3s; timings.json is the clock). GATE P
signed in BUILD-LOG.md. SHOPPING.md is the human's — do not wait on pantry.

1. GATE F close-out: verify every open row in FACTCHECK.md against
   SOURCE.md and the primary sources it names; write verdicts + fixes.
   REAL-PERSON CARE RULES ARE HARD: the court-case student's name is never
   spoken and never appears outside the small citation card (B22); the
   wrong-attribution variant's name (SOURCE.md closing note) never appears
   on screen or in narration at all (B23). If a fix changes narration_text,
   regenerate ONLY those beats:
   python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py <reel>
   --no-gate --only <ids>, then refresh those beats' .srt cues.
2. Author <reel>/scenes.py: one Manim Scene per Manim-lane beat — B06 B09
   B11 B14 B15 B17 B21 B31 — class names exactly as graphic.manim. Follow
   each beat's show[] events; Claude palette (cream #F2F0E9, ink #3D3929,
   terracotta #D97757 as the ONE accent); FILL-THE-CANVAS + SAFE margins.
   Numbers on screen ONLY with their citation line (Freelancer study,
   systematic review, Stanford TOEFL); schematic curves carry no invented
   units.
3. Write SHOTLIST.md (typed work order: every beat's lane, window, slot
   status) and PROMPTS.md (beat-prefixed prompts for the 6 open pantry
   slots, copied from SHOPPING.md) — run.sh Gate-F paperwork.
4. Reconcile Remotion pattern ids against runtime/remotion/src/Root.tsx
   (doctrine names in the sheet: ClaudeComposerAsk, ClaudeVerdictArtifact,
   ClaudeTitleOutro, SegmentCard, deckPatterns/*, illustrations/*,
   code-block). Author missing ones reel-local per slate-filler discipline.
   Code beat B20 reads <reel>/code/naive_ai_score.py — the real file.
5. Run: ./brutalist-art/art run computational-skepticism-for-ai/youtube/claude-liam-fluency-trap
   Remotion only via runtime/scripts/remotion_scenes.py, foreground,
   --concurrency=1. Honor vox-run handoffs (R1 B02→B03, R2 B26→B27) in any
   generated slates — slates animate their show[] events.
6. VISUAL QC per CLAUDE-CODE-VISUAL-QC-CHECK.md on the -slate.mp4 (frames
   at fps=2, READ the PNGs, 9-point rubric, _qc/REPORT.md; zero
   BLOCKER/MAJOR before done).
7. Report in BUILD-LOG.md: rendered vs slate (slates should be exactly the
   6 SHOPPING.md slots), review-cut path, MISSING: lines. Stop.
```

## PASS 2 — after pantry media lands

```
Reel: computational-skepticism-for-ai/youtube/claude-liam-fluency-trap
PASS 2 — pantry filled. Free pipeline, never publish.

1. Read BUILD-LOG.md + SHOPPING.md. Run the pantry intake: conform, treat
   (desat ~80%, contrast, cream seat; grain at assembly; WARMONO for the
   Athens scan), rename to media/<BID> names.
2. Verify per SHOPPING.md: resolution floors vs camera plans; the R1 plate
   (B02/B03 share one Athens scan — confirm it survives the 2.0× tight
   frame); R2 pair (B26 letter / B27 flood — same visual family); the B02
   sidecar (.source.txt: scan URL, license, credit) — refuse on a missing
   tier-2 sidecar.
3. Confirm each vox beat's shot.focus against the delivered stills; adjust
   + log.
4. Rerun ./brutalist-art/art run <reel> — only changed slots recompile.
   Sample frames across the R1 and R2 run boundaries to verify continuity.
5. Full VISUAL QC again (treatment check: desaturated plates, ONE
   terracotta accent per beat, labels inside SAFE).
6. If SHOPPING.md is all-checked and no slates remain:
   ./brutalist-art/art final <reel>; update BUILD-LOG.md + description.txt
   timestamps if durations changed. Report the master path and stop —
   publishing is Bear's manual step.
```
