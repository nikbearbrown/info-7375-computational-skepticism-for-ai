# TYPECHECK.md — GATE T

Reel: `claude-liam-computational-epistemology`  |  Checked: 2026-07-24T07:48  |  Overall: PASS  |  Beats checked: 40  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 1.6× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| B01 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | ? | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B07 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B09 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B10 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| B12 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B13 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B16 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B17 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| B18 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B19 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| B21 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B23 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| B24 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B25 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| B26 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B27 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B28 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B29 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B30 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B31 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| B32 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B33 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| B34 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B35 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| B36 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B37 | ? | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B38 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B39 | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 24 | 0 |
| min-size §8.1 | 40 | 0 |
| overflow §8.2 | 40 | 0 |
| contrast §8.3 | 40 | 0 |
| kerning §8.4 | 11 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
