# PLAN.md — claude-liam-arguing-in-good-faith

**Skill:** ai-explainer (claude-liam channel, Kokoro am_onyx, Teardown register)
**Source:** six social-media carousel cards — two conduct, four fallacy
**Standing order:** build to slate cut, stop. No art final / TOPOST / publish.

---

## Steps

1. **FACTCHECK.md** — verify all six definitions against a logic reference; record deliberate
   deviations from the source carousel with reasoning.

2. **FallacyCard.tsx** — new Remotion component, registered in Root.tsx only.
   - Zod schema per spec: kind, title, definition, examples (optional), test (optional), icon
   - Inline SVG line-glyph icons (ear, fish, person, crown, heart, scale)
   - Terracotta accent law: fallacy → icon strokes; conduct → test line text
   - Demo twin + determinism check before registration

3. **beat_sheet.json** — 16 beats (B00–B15) per spec.
   - B00: ClaudeComposerAsk cold open
   - B01: FormACard executive summary (BLUF)
   - B02–B03: conduct cards (FallacyCard × 2)
   - B04–B11: four fallacy pairs — card reveal (FallacyCard) then test enacted (FormACard)
   - B12: FormACard — fallacy names as weapons
   - B13: ClaudeVerdictArtifact
   - B14: ClaudeComposerAsk handoff (greeting "Your turn.")
   - B15: ClaudeTitleOutro

4. **Audio** — generate all beats with `runtime/scripts/generate_audio_kokoro.py`, voice `am_onyx`,
   no gating.

5. **Render** — `runtime/scripts/remotion_scenes.py <reel>`, foreground, --concurrency=1.

6. **Compile** — `art run <reel>`. Run kerning gate. Write TYPECHECK.md.

7. **QC** — sample real frames, read 8-point rubric, write CHECKS-REPORT.md.

---

## ILLUSTRATE LAW check

- Claude UI appears only at B00 (cold open) and B14 (handoff). ✓
- All card beats use FallacyCard. ✓
- Test-enacted beats use FormACard (plain serif card). ✓
- No DoodleScene, no DoodleChart (DOODLE-BANNED LAW). ✓
- No screenshots of the source carousel. ✓
- No external names (persons, orgs, publications) as fallacy examples. ✓

---

## Type-gate risk

Card text is dense. Risk areas:
- Definition lines wrapping at large font — auto-fit caps size to usable width
- Test lines are the longest text (up to ~100 chars) — FallacyCard auto-fits
- §8.5 wordy-card: the FallacyCard carries multiple text tiers; not a FormACard so §8.5
  does not apply. But each text tier must stay above the §8.1 floor.

Mitigations already in design:
- Title: height × 0.090 ≈ 97px at 1080 (above floor)
- Definition: height × 0.052 ≈ 56px (above floor)
- Examples: height × 0.048 ≈ 52px (above floor of 48.6)
- Test: height × 0.048 ≈ 52px (above floor)
- All capped by line-length auto-fit so nothing escapes the container
