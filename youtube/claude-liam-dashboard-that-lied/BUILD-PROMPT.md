# BUILD-PROMPT — claude-liam-dashboard-that-lied

Paste-ready Claude Code prompts. Run from `books/`. Free pipeline; never
publishes. PASS 1 now; PASS 2 after pantry fills.

## PASS 1 — machine-side everything (human is shopping)

```
Read brutalist-art/skills/make/deep-explainer/SKILL.md completely, then its
reference/ files, then the parents it names (ai-explainer SKILL.md; explainer
SKILL.md + MOTION.md + REMOTION.md). Standing rules #1–#4 in
brutalist-art/EXAMPLES-CAMPAIGN.md govern. Free pipeline only — no paid
calls, never publish.

Reel: computational-skepticism-for-ai/youtube/claude-liam-dashboard-that-lied
State: audio LOCKED (33 Kokoro mp3s, 7:32; timings.json is the clock).
GATE P signed in BUILD-LOG.md. SHOPPING.md is the human's — don't wait.

1. GATE F close-out: verify FACTCHECK.md rows. External rows (J.C. Penney
   $4.3B + timeline; Knight Capital $440M / 45 min / SEC order; Pearl
   attribution) verify against independent sources. The WAU case rows
   verify against SOURCE.md only — it is the chapter's authored teaching
   case and stays labeled as such on screen. Narration fixes → regenerate
   only those beats (generate_audio_kokoro.py <reel> --no-gate --only)
   and refresh their .srt cues.
2. Author <reel>/scenes.py: Manim scenes B03_GreenLine B04_VanishingDenominator
   B10_RemoveThePromos B12_DoOperator B13_CategoryBoundary B15_ConfounderDAG
   B17_TheLadder B22_ConceptDrift — names exactly as graphic.manim; follow
   each beat's show[] events; Claude palette, ONE terracotta accent,
   FILL-THE-CANVAS + SAFE. B12/B13 are one equation-tangent group (the
   equation card persists). Schematic graphics carry no invented units;
   the case numbers stay labeled "the chapter's case".
3. Write SHOTLIST.md + PROMPTS.md (Gate-F paperwork) from the beat sheet
   + SHOPPING.md.
4. Reconcile Remotion pattern ids against runtime/remotion/src/Root.tsx;
   author missing patterns reel-local per slate-filler discipline.
5. Run: ./brutalist-art/art run computational-skepticism-for-ai/youtube/claude-liam-dashboard-that-lied
   (remotion_scenes.py foreground only). Honor vox-run handoffs
   (R1 B07→B08, R2 B23→B24) in generated slates.
6. VISUAL QC per CLAUDE-CODE-VISUAL-QC-CHECK.md; zero BLOCKER/MAJOR.
7. Report in BUILD-LOG.md (slates should be exactly the 5 SHOPPING.md
   files) and stop.
```

## PASS 2 — after pantry media lands

```
Reel: computational-skepticism-for-ai/youtube/claude-liam-dashboard-that-lied
PASS 2 — pantry filled. Free pipeline, never publish.

1. Read BUILD-LOG.md + SHOPPING.md. Pantry intake: conform, treat, rename.
2. Verify floors vs camera plans; the two run plates (B07 serves B07+B08 at
   1.9× tight; B23 serves B23+B24 and must read UNMANNED wide); adjust
   shot.focus to the delivered stills and log.
3. Rerun ./brutalist-art/art run <reel>; sample frames across R1/R2
   boundaries for continuity.
4. Full VISUAL QC; then ./brutalist-art/art final <reel> if no slates
   remain. Update BUILD-LOG.md + description.txt timestamps if durations
   changed. Report the master path and stop.
```
