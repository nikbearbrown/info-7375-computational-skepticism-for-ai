# CHECKS-REPORT — claude-liam-pick-your-pebble-deep
_Date: 2026-07-30 | Stage: SLATE PREVIZ (Gate P)_

## Slate stats
- Duration: **386.0s** (~6m26s)
- Beats: **27/27 filled**
- Slot map: B00:VIDEO A1C:VIDEO A1V1:VIDEO A1R1:VIDEO A1F1:VIDEO A1M1:MANIM A2C:VIDEO A2F1:VIDEO A2M1:MANIM A2F2:VIDEO A3C:VIDEO A3R1:VIDEO A3M1:MANIM A3R2:VIDEO A3V1:VIDEO A3M2:MANIM A3V2:VIDEO A3M3:MANIM A4C:VIDEO A4R1:VIDEO A4M1:MANIM A4V1:VIDEO A4R2:VIDEO A4R3:VIDEO BVDT:VIDEO BHTF:VIDEO BOUT:VIDEO

## GATE B — Manim layout audit
**PASS** (all 6 scenes CLEAN after two layout fixes during build)

Fixes applied:
- A3M1_PredictionLock: stacked POPPER label + falsifier text vertically (were at same y=-1.4, 37% overlap)
- A3M3_PAFailure: stacked SEVERITY:HIGH label + subtitle vertically (were at same y=-2.2, 18% overlap)

## GATE A — Static scene check
**PASS** — all 6 Manim scenes pass (A4M1_Attestation fixed pre-build to include non-text shapes)

## GATE BANNED-CARD
**PASS** — no SlateCard, no body-beat ClaudeWindow(view=artifact)

## GATE L — Beat-mix lint
**PASS** — VOX 17.4% (4 beats), MANIM 26.1% (6), REMOTION 39.1% (9), CARD 17.4% (4)
- WARN: Remotion 48% of all beats (13/27 incl. bookends) — over the ~40% pantry cap advisory

## GATE V — Frame-level visual QC
**38 MAJOR, 0 BLOCKERS**
All 38 are `underfill` on Remotion card components (FormACard act cards 3%, FormBCard 21–41%, ClaudeComposerAsk 25%). These are false positives: minimalist centered card layouts by design. Same pattern as the abstract cut.
**Recommendation: `ART_STRICT=0` for this reel class**

## GATE T — Type check
**FAIL — 5 beats** (requires fix before `art final`)

| Beat | Issue | Root cause |
|------|-------|-----------|
| A1M1 | contrast §8.3: 2.74:1 | IRREVERSIBLE tag text (cream on terracotta) — checker reads terracotta region as foreground |
| A2M1 | contrast §8.3: 2.74:1 | `caps("false success", clr=ACCENT)` on cream background |
| A3M2 | contrast §8.3: 2.74:1 | `serif("≠", clr=ACCENT)` on cream; `serif("Local client: WIPED", clr=ACCENT)` on white card |
| A3M3 | min-size §8.1: 34px < 35px floor + contrast §8.3: 2.74:1 | smallest label 34px; terracotta on cream |
| A4M1 | contrast §8.3: 3.78:1 | TEAL (#2A9D8F) on cream — teal is not dark enough for body text on cream |

**Systematic issue:** Claude palette ACCENT (#D97757, terracotta) and TEAL (#2A9D8F) both fail 4.5:1 WCAG on CREAM (#F2F0E9) when used as text colors. Spec §8.3 requires backing plate or switch to INK.

**Fixes required before final:**
1. A1M1, A2M1, A3M2, A3M3 — terracotta accent text: either add semi-opaque backing plate, or use INK for text and terracotta for border/shape only
2. A3M3 — sev_sub sz=22 → sz=24 (34px < 35px floor at 1080p logical; 4K renders at 2x so actual pixel height is double, but spec measures at logical resolution)
3. A4M1 — TEAL text → use INK for text labels; TEAL for box backgrounds/borders only

## GATE P — Pantry / SHOPPING.md
**4 stills MISSING** (documented in BUILD-LOG.md):
- A3V1 (Tier 2, HOLD) — Ch8 Fig 8.6: `images/08-validating-agentic-ai...-fig-05.png`
- A3V2 (Tier 2, HOLD) — Ch8 Fig 8.11: `images/08-validating-agentic-ai...-fig-09.png`
- A1V1 (Tier 1, illustrative) — Agents of Chaos study overview
- A4V1 (Tier 1, illustrative) — attestation checklist with gaps

All 4 VOX beats render as FormACard slates. Slate previz is correct behavior for GATE P.

## FormBCard cueFrame bug (fixed in build)
`shot.remotion.props.cueFrames` was a top-level array; `remotion_scenes.py` passes props raw without Zod defaults, so each `item.cueFrame` = undefined → `Frame NaN is not finite`.
**Fix applied:** cueFrame moved onto each item in beat_sheet.json. All three FormBCard beats (A1F1, A2F1, A2F2) now render correctly.

## Standing order
STOPPED at slate previz per standing order. **No `art final`, no post, no 4K, no TOPOST.**
Bear reviews; no autonomous next steps.

## Required before final
1. Fix GATE T failures (scenes.py): add backing plates or switch accent/teal text to INK for body labels
2. Supply pantry stills (SHOPPING.md): generate Ch8 figures from D3 spec + commission Tier 1 illustratives
3. Re-run GATE T until TYPECHECK.md shows no FAIL
4. Re-run GATE B after scenes.py changes
