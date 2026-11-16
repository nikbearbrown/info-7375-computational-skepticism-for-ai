# TYPECHECK.md — GATE T

Reel: `claude-liam-deep-10-visualization-short`  |  Checked: 2026-07-31T23:18  |  Overall: PASS  |  Beats checked: 15  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | BOOKEND | min-size §8.1: min text-run height 83px >= floor 31px | PASS | — |
| A1C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1R | REMOTION | no-wordy-card §8.5: 2 element(s), 14 words — within budget. Detail: 'left.note' (6 words);… | PASS | — |
| A2C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3M2 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5V2 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5V3 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5V4 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A7C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| BOUT | CLOSING | min-size §8.1: min text-run height 144px >= floor 31px | PASS | — |
| END | ? | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 12 | 0 |
| min-size §8.1 | 14 | 0 |
| overflow §8.2 | 14 | 0 |
| contrast §8.3 | 14 | 0 |
| contrast-local §8.3b | 14 | 0 |
| bbox-overlap §8.6b | 14 | 0 |
| kerning §8.4 | 1 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
