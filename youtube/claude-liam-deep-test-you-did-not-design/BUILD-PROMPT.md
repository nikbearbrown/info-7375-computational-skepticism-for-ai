# BUILD-PROMPT — claude-liam-deep-test-you-did-not-design

Paste-ready Claude Code prompts. Run from `books/`. Free pipeline only (Kokoro `am_onyx`, Manim, Remotion, ffmpeg); never publishes. PASS 1 is done (this folder holds its output); PASS 2 runs after the two human plates land.

## PASS 1 — machine-side everything (done 2026-09-02; rerun to rebuild from scratch)

```
Read brutalist-art/skills/make/deep-explainer/SKILL.md completely, then its
reference/ files, then the parents it names (ai-explainer SKILL.md; explainer
SKILL.md + MOTION.md + REMOTION.md), then VOICE-LOCK.md, OUTRO-LOCK.md,
SLATE-RULE.md and FACTCHECK-SPEC.md at the brutalist-art root. Standing rules
#1–#4 in brutalist-art/EXAMPLES-CAMPAIGN.md govern. Free pipeline only — no
paid calls, never publish.

Reel: computational-skepticism-for-ai/youtube/claude-liam-deep-test-you-did-not-design
Source: SOURCE.md (Bear's skepticism.ai essay, verbatim). Beat sheet, scenes.py,
FACTCHECK/SHOTLIST/PROMPTS/SOURCES/PLAN/CHECKS-REPORT are authored.

1. Audio: python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py <reel>
   (nothing gates it). Then the word clock:
   python3 brutalist-art/runtime/scripts/align.py <reel>
2. Gate D2: write SHOPPING.md from mp3/timings.json — entries ONLY for the two
   human plates (A3V1 Turing portrait, Tier 3; A3V2 Searle 1980 first page,
   Tier 2) with the locked windows and the rights lines. The other five plates
   are already in pantry/ with sidecars.
3. Pantry intake: python3 brutalist-art/runtime/scripts/pantry.py <reel>
   (keeps the hand-written media/*.source.txt sidecars).
4. Gate D1: ./brutalist-art/art run <reel> --height 1080
   Manim renders from <reel>/scenes.py (durations read from the sheet);
   Remotion beats render via remotion_scenes.py in the FOREGROUND (never
   hand-rolled npx renders). Slates must be exactly A3V1 and A3V2.
5. VISUAL QC per brutalist-art/CLAUDE-CODE-VISUAL-QC-CHECK.md — sample frames,
   READ the PNGs, 9-point rubric, log to _qc/REPORT.md; fix root causes in
   scenes.py / beat-sheet props; re-run until zero BLOCKER / MAJOR.
6. Append the render ledger to CHECKS-REPORT.md and the gate signatures to
   BUILD-LOG.md. Stop at the previz. Do not run ./art final, 4K, or post.
```

## PASS 2 — after the two plates land in pantry/

```
Reel: computational-skepticism-for-ai/youtube/claude-liam-deep-test-you-did-not-design
PASS 2 — pantry filled. Free pipeline, never publish.

1. Read BUILD-LOG.md + SHOPPING.md. Refuse on a missing sidecar for A3V1 or
   A3V2 (tier 2/3 law) — a missing rights line is a stop, not a warning.
2. python3 brutalist-art/runtime/scripts/pantry.py <reel>; confirm shot.focus
   per delivered still (A3V1 toward the eyes [0.5, 0.38]; A3V2 top-anchored
   DOCUMENT crop with the title block in frame); log adjustments.
3. If either plate could NOT be cleared, take the drawn fallback in PROMPTS.md,
   strike the SHOPPING.md entry with the replacing scene named, and keep the
   narration unchanged.
4. ./brutalist-art/art run <reel> --height 1080 → full VISUAL QC → then, only
   if zero slates remain: ./brutalist-art/art run <reel> (4K) and
   ./brutalist-art/art final <reel>. Update BUILD-LOG.md and description.txt
   chapter timestamps if durations changed. Report the master path and stop.
```
