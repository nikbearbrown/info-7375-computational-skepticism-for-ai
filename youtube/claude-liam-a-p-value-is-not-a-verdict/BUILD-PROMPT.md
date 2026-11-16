# BUILD-PROMPT.md — claude-liam-a-p-value-is-not-a-verdict

Paste-ready. Run from `books/` in a local Claude Code session.

---

```
Build the deep-explainer reel at
computational-skepticism-for-ai/youtube/claude-liam-a-p-value-is-not-a-verdict/.

READ FIRST:
  brutalist-art/skills/make/deep-explainer/SKILL.md
  brutalist-art/skills/make/deep-explainer/reference/vox-beats.md
  brutalist-art/skills/make/deep-explainer/reference/shopping-list.md
  brutalist-art/skills/make/ai-explainer/SKILL.md
  brutalist-art/skills/make/nopunt/SKILL.md
  the reel's FACTCHECK.md and BUILD-LOG.md

The beat sheet is authored and the plan gate is signed. Do not re-author
narration, re-order beats, or change the lane mix.

CHANNEL: claude-liam, Kokoro am_onyx. FREE — no ElevenLabs call anywhere.

*** GATE B20 — READ THIS BEFORE ANYTHING ELSE ***
B20 states that a citation in the source's own correction addendum does not
appear in the cited paper (Kirchenbauer et al., On the Reliability of Watermarks
for Large Language Models, arXiv:2306.04634 / ICLR 2024). The quoted figures are
"AUC above roughly 0.85 at 200 tokens and above roughly 0.9 at 600 tokens."

Open the published PDF and search it. Report what you find, verbatim, with the
page or section. Then:
  - figures NOT present  -> B20 ships as written. Continue.
  - figures present      -> STOP. Do not render B20. Report back; Act V will be
                            rebuilt around the California retraction alone.
This is an accusation against a source. It does not ship on a research pass.

STEP 1 — keys and ledger
  ./brutalist-art/art keys
  ./brutalist-art/art todo computational-skepticism-for-ai/youtube/claude-liam-a-p-value-is-not-a-verdict
  Confirm 25 beats, 5 human-supplied vox slots, ZERO gen-AI requests. If any beat
  reports shot.source of ai/gen/genai, something has drifted — stop and report.

STEP 2 — CHECKS-REPORT.md before anything compiles
  N SHOW / N justified-HOLD / N PUNT-flagged, plus the teaching-arc checklist.
  Any PUNT is a violation — resolve or justify in BUILD-LOG.md.

STEP 3 — audio (the master clock)
  python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
      computational-skepticism-for-ai/youtube/claude-liam-a-p-value-is-not-a-verdict
  Write measured durations back to actual_duration_s, then align for the word
  clock. Report total runtime.

STEP 4 — Manim scenes (8)
  B02_GreenListBoost · B03_OneProportionZ · B07_GradientNotSwitch ·
  B11_PositivePredictiveValue · B12_ForensicsVersusScreening ·
  B15_WallWithDoors · B18_PrincipalAgent · B20_TheNumberThatIsntThere

  Build each from its graphic.production_viz.mechanic verbatim. Cream #FAF9F5,
  ink #3D3929, ONE terracotta #D97757 moment per beat.

  Four of these perform a REVERSAL and the reversal is the beat — do not
  soften any of them into a caption:
    B07  the "one paraphrase kills it" switch is drawn and STRUCK THROUGH; the
         bar then descends smoothly and halts at 57.2%
    B11  a 10x10 grid of alarms must physically SORT into 8 ink and 92 terracotta
    B15  the wall labelled IMPOSSIBLE opens two doors and RELABELS to UNBUILT
    B20  a search sweep traverses the paper and must visibly PASS THROUGH without
         stopping, then the quoted figures hollow to outline

  LAYOUT LAW — this reel is built after the Simon's Ant post-mortem. No element
  is positioned with a hardcoded move_to([x, y, 0]). Labels attach with
  next_to(target, DIR, buff=...); rows are VGroup(...).arrange(); text inside a
  box gets an explicit width derived from the box. Call the bbox-overlap
  assertion helper at the end of every construct().

  MUTE IS NOT A HIDING PLACE. If GATE T's mask fix has landed, MUTE text is
  checked like INK. Do not colour a label MUTE to get it past a validator.

STEP 5 — Remotion scenes (7 body + 5 bookends)
  Render ONLY via:
    python3 brutalist-art/runtime/scripts/remotion_scenes.py \
        computational-skepticism-for-ai/youtube/claude-liam-a-p-value-is-not-a-verdict
  Foreground, --concurrency=1. Never hand-roll npx remotion render.
  Patterns: ClaudeComposerAsk (B00, B10, BHTF) · DeckPattern (B01 threshold,
  B04/B09/B21 divergence) · ChipGrid (B06, B14, B17) ·
  ClaudeVerdictArtifact (BVDT) · ClaudeTitleOutro (BOUT).
  Match every props object to that component's zod schema before rendering.
  BVDT has FIVE artifactLines — confirm the component handles five without
  overflow before rendering, and reduce to four by merging lines 2 and 3 if not.

STEP 6 — GATE D2, tier-0 library pass THEN the shopping list
  Five vox stills: B05 B08 B13 B16 B19. All five are REAL PUBLISHED DOCUMENTS —
  a Nature paper page, an EU Code of Practice page, a Patterns paper page, an
  ICML paper page, and the source brief's own addendum. None is a stock photo and
  none may be replaced by one.
    python3 brutalist-art/runtime/scripts/pantry_search.py "<terms>"
  then write SHOPPING.md from the LOCKED durations (never before step 3).
  All five are drawon/annotate — the plate HOLDS and the terracotta pen moves. No
  Ken Burns except B19. Every one has a GRAPHIC/own fallback already written in
  shot.vox.shopping.fallback; if a page cannot be cleared, CONVERT the beat, do
  not slate it.

STEP 7 — GATE D1, the full-length slate previz
  ./brutalist-art/art run computational-skepticism-for-ai/youtube/claude-liam-a-p-value-is-not-a-verdict
  Vox slots render as slates; Manim and Remotion render for real; audio is real.
  This is a PREVIZ. Report the runtime and hand it to the human to WATCH.

STEP 8 — pantry fill, then gates
  GATE T   python3 brutalist-art/runtime/scripts/type_check.py -> TYPECHECK.md,
           zero FAIL. Blocks run and final.
  VISUAL QC LAW: sample frames at >=2fps plus each beat at 15/50/85%, actually
           READ the PNGs, audit the 9-point rubric, log _qc/REPORT.md. Fix root
           causes in scene source and re-render until zero BLOCKER and zero MAJOR.
           An mp4 probe is a FILE check and never counts as QC.
  GATE SHARPNESS: no rotation on any pixel-art rect.

STEP 9 — final
  ./brutalist-art/art final computational-skepticism-for-ai/youtube/claude-liam-a-p-value-is-not-a-verdict

DO NOT PUBLISH. Do not touch books/youtube/TOPOST/.

REPORT: the B20 gate result verbatim, runtime, measured lane histogram,
TYPECHECK status, _qc summary, SHOPPING.md open items, any MISSING: lines.
```

---

## Notes for whoever runs this

- **The B20 gate is the first thing, not the last.** If the figures turn out to
  be in the paper, three beats change and it's better to know before audio.
- Nothing here has been rendered. Step 1 is genuinely step 1.
- The five stills are the critical path but steps 1–7 run without them; the
  previz is watchable with slates in those slots.
- This reel is the first built after the Simon's Ant layout post-mortem. If the
  bbox-overlap assertion helper doesn't exist yet, write it here — it's eight
  lines and it's the whole reason that reel shipped with `PHOEBOSTON` in it.
