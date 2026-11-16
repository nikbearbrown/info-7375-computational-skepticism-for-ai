# TYPECHECK.md — GATE T

Reel: `claude-liam-distrust-the-machine`  |  Checked: 2026-08-13T12:13  |  Overall: PASS  |  Beats checked: 33  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B01 | BOOKEND | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | remotion | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 11 words in 'right.note') | PASS | — |
| B03 | remotion | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 6 words in 'left.note') | PASS | — |
| B04 | BOOKEND | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | remotion | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 6 words in 'note') | PASS | — |
| B06 | remotion | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 10 words in 'right.note') | PASS | — |
| B07 | remotion | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 11 words in 'note') | PASS | — |
| B08 | BOOKEND | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | manim | light | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B10 | remotion | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 11 words in 'sparkLine') | PASS | — |
| B11 | remotion | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 8 words in 'left.note') | PASS | — |
| B12 | BOOKEND | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | manim | light | min-size §8.1: min text-run height 353px >= floor 35px | PASS | — |
| B13a | remotion | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 8 words in 'sparkLine') | PASS | — |
| B14 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14a | remotion | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 11 words in 'chips[2]') | PASS | — |
| B15 | remotion | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 7 words in 'sparkLine') | PASS | — |
| B16 | remotion | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 12 words in 'note') | PASS | — |
| B17 | BOOKEND | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | manim | light | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B19 | manim | light | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| B20 | manim | light | min-size §8.1: min text-run height 68px >= floor 35px | PASS | — |
| B21 | BOOKEND | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | ask | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B23 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B24 | remotion | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 9 words in 'right.note') | PASS | — |
| B25 | BOOKEND | light | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B26 | BOOKEND | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B27 | BOOKEND | dark | min-size §8.1: min text-run height 66px >= floor 35px | PASS | — |
| BVDT | ? | light | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| BHTF | ? | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| BOUT | ? | dark | min-size §8.1: min text-run height 66px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 20 | 0 |
| min-size §8.1 | 33 | 0 |
| overflow §8.2 | 33 | 0 |
| contrast §8.3 | 33 | 0 |
| contrast-local §8.3b | 33 | 0 |
| bbox-overlap §8.6b | 33 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 2 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
