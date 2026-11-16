# TYPECHECK.md — GATE T

Reel: `claude-liam-ranfei-visa-risk-runway`  |  Checked: 2026-07-24T08:17  |  Overall: PASS  |  Beats checked: 28  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ASK | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| BC1 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 8 words in 'note') | PASS | — |
| B02 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| BC2 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | ASK | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| B06 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| BC3 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | ASK | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| B12 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| BC4 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| BC5 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | REMOTION | no-wordy-card §8.5: ChipGrid: per-element check passed (max 3 words in 'sparkLine') | PASS | — |
| B15 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| BC6 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B16 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| B17 | REMOTION | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 9 words in 'artifactLines[… | PASS | — |
| B18 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | REMOTION | min-size §8.1: min text-run height 52px >= floor 35px | PASS | — |
| BHTF | ASK | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | CARD | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 22 | 0 |
| min-size §8.1 | 28 | 0 |
| overflow §8.2 | 28 | 0 |
| contrast §8.3 | 28 | 0 |
| kerning §8.4 | 7 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
