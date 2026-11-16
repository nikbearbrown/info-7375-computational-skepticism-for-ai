# TYPECHECK.md — GATE T

Reel: `claude-liam-vox-bias-pipe`  |  Checked: 2026-07-27T15:27  |  Overall: PASS  |  Beats checked: 24  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B01 | ? | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| AB02 | ? | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| B02 | ? | min-size §8.1: min text-run height 56px >= floor 35px | PASS | — |
| B03 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| AB04 | ? | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| B04 | ? | min-size §8.1: min text-run height 66px >= floor 35px | PASS | — |
| AB05 | ? | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| B05 | ? | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| B06 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| AB07 | ? | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| B07 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| AB08 | ? | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| B08 | ? | min-size §8.1: min text-run height 60px >= floor 35px | PASS | — |
| AB09 | ? | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| B09 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| AB10 | ? | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| B10 | ? | min-size §8.1: min text-run height 60px >= floor 35px | PASS | — |
| AB11 | ? | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| B11 | ? | min-size §8.1: min text-run height 59px >= floor 35px | PASS | — |
| AB12 | ? | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| B12 | ? | min-size §8.1: min text-run height 44px >= floor 35px | PASS | — |
| B13 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| HANDOFF | ? | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| OUTRO | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 3 | 0 |
| min-size §8.1 | 24 | 0 |
| overflow §8.2 | 24 | 0 |
| contrast §8.3 | 24 | 0 |
| kerning §8.4 | 9 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
