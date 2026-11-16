# TYPECHECK.md — GATE T

Reel: `claude-liam-deep-10-visualization`  |  Checked: 2026-07-31T23:04  |  Overall: PASS  |  Beats checked: 34  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | BOOKEND | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| A1C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1R | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 8 words in 'right.note') | PASS | — |
| A2C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2R | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3R | REMOTION | no-wordy-card §8.5: ChipGrid: per-element check passed (max 8 words in 'sparkLine') | PASS | — |
| A3M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3M2 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4R | REMOTION | no-wordy-card §8.5: ChipGrid: per-element check passed (max 8 words in 'sparkLine') | PASS | — |
| A4M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4M2 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5V1 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5R | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 7 words in 'sparkLine') | PASS | — |
| A5V2 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5V3 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5V4 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6R | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 9 words in 'sparkLine') | PASS | — |
| A6V1 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6R2 | MANIM | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| A7C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A7R | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 8 words in 'right.note') | PASS | — |
| A7V | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A7R2 | REMOTION | no-wordy-card §8.5: ChipGrid: per-element check passed (max 10 words in 'sparkLine') | PASS | — |
| BVDT | CLOSING | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BHTF | CLOSING | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | CLOSING | min-size §8.1: min text-run height 97px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 29 | 0 |
| min-size §8.1 | 34 | 0 |
| overflow §8.2 | 34 | 0 |
| contrast §8.3 | 34 | 0 |
| contrast-local §8.3b | 34 | 0 |
| bbox-overlap §8.6b | 34 | 0 |
| kerning §8.4 | 15 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
