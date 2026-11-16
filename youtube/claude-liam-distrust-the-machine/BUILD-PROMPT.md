# BUILD-PROMPT — claude-liam-distrust-the-machine

Paste-ready Claude Code prompts. Run from `books/`. Free pipeline; never
publishes. PASS 1 now; PASS 2 after pantry fills.

## PASS 1 — machine-side everything (human is shopping)

```
Read brutalist-art/skills/make/deep-explainer/SKILL.md completely, then its
reference/ files, then the parents it names (ai-explainer SKILL.md; explainer
SKILL.md + MOTION.md + REMOTION.md). Standing rules #1–#4 in
brutalist-art/EXAMPLES-CAMPAIGN.md govern. Free pipeline only — no paid
calls, never publish.

Reel: computational-skepticism-for-ai/youtube/claude-liam-distrust-the-machine
State: audio LOCKED (28 Kokoro mp3s, 6:41; timings.json is the clock).
GATE P signed in BUILD-LOG.md. SHOPPING.md is the human's — don't wait.

1. GATE F close-out: verify FACTCHECK.md rows. This is a FIRST-PARTY
   source (Bear's own essay, SOURCE.md): internal-argument rows verify
   against SOURCE.md; row 6 (Gardner 1983, seven-later-nine) verifies
   independently. HARD RULES: tier names verbatim from SOURCE.md; tier
   CONTENT limited to what the essay states (no invented tier
   descriptions); B19's narration keeps the essay's hedge ("may be a
   lossy compression"); the B22/B23 syllabus triage stays labeled
   illustrative with no real institution named. Narration fixes →
   regenerate only those beats (generate_audio_kokoro.py <reel> --no-gate
   --only <ids>) + refresh their .srt cues.
2. Author <reel>/scenes.py: Manim scenes B09_OffTheChart B13_GardnersFrame
   B14_SevenTiers B19_LossyCompression B20_TheBetween — names exactly as
   graphic.manim; follow show[] events; Claude palette, ONE terracotta
   accent, FILL-THE-CANVAS + SAFE. Schematic bars carry no invented
   magnitudes; B14's tier labels are the essay's names verbatim.
3. Write SHOTLIST.md + PROMPTS.md (Gate-F paperwork) from the beat sheet
   + SHOPPING.md.
4. Reconcile Remotion pattern ids against runtime/remotion/src/Root.tsx;
   author missing patterns reel-local per slate-filler discipline. The
   B23 result artifact (triaged syllabus card) is an authored Remotion
   scene — generic course rows, tier chips, the zero-results search
   highlight; no media dependency.
5. Run: ./brutalist-art/art run computational-skepticism-for-ai/youtube/claude-liam-distrust-the-machine
   (remotion_scenes.py foreground only). Honor the vox-run handoff
   (R1 B05→B06) in generated slates.
6. VISUAL QC per CLAUDE-CODE-VISUAL-QC-CHECK.md; zero BLOCKER/MAJOR.
7. Report in BUILD-LOG.md (slates should be exactly the 4 SHOPPING.md
   files) and stop.
```

## PASS 2 — after pantry media lands

```
Reel: computational-skepticism-for-ai/youtube/claude-liam-distrust-the-machine
PASS 2 — pantry filled. Free pipeline, never publish.

1. Read BUILD-LOG.md + SHOPPING.md. Pantry intake: conform, treat, rename.
   WARMONO preset if B05 arrived as LOC archival (then require its
   .source.txt sidecar; refuse without it).
2. Verify floors vs camera plans; B05 serves the R1 pair at 1.9× tight →
   full-room reveal; B02 must show NO face (composite-student rule).
3. Confirm shot.focus per delivered still; adjust and log.
4. Rerun ./brutalist-art/art run <reel>; sample frames across the R1
   boundary for continuity.
5. Full VISUAL QC; then ./brutalist-art/art final <reel> if no slates
   remain. Update BUILD-LOG.md + description.txt timestamps if durations
   changed. Report the master path and stop.
```
