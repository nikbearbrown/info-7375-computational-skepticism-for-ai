# TYPECHECK.md — GATE T

Reel: `claude-liam-pick-your-pebble-deep-short`  |  Checked: 2026-08-01T04:40  |  Overall: PASS  |  Beats checked: 16  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | BOOKEND | min-size §8.1: min text-run height 83px >= floor 31px | PASS | — |
| A1C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1R1 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1M1 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2M1 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3R1 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3R2 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3V1 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3V2 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4M1 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4R2 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| BOUT | BOOKEND | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| END | ? | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 13 | 0 |
| min-size §8.1 | 15 | 0 |
| overflow §8.2 | 15 | 0 |
| contrast §8.3 | 15 | 0 |
| contrast-local §8.3b | 15 | 0 |
| bbox-overlap §8.6b | 15 | 0 |
| kerning §8.4 | 3 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
