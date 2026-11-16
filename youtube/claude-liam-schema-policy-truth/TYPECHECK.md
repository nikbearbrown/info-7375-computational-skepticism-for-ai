# TYPECHECK.md — GATE T

Reel: `claude-liam-schema-policy-truth`  |  Checked: 2026-08-05T03:02  |  Overall: PASS  |  Beats checked: 9  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| B01 | ? | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B02 | ? | min-size §8.1: min text-run height 37px >= floor 35px | PASS | — |
| B03 | ? | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B04 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | ? | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| BVDT | ? | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| BHTF | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 9 | 0 |
| overflow §8.2 | 9 | 0 |
| contrast §8.3 | 9 | 0 |
| contrast-local §8.3b | 9 | 0 |
| bbox-overlap §8.6b | 9 | 0 |
| kerning §8.4 | 4 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
