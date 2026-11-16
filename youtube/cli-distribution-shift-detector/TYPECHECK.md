# TYPECHECK.md — GATE T

Reel: `cli-distribution-shift-detector`  |  Checked: 2026-07-24T09:18  |  Overall: PASS  |  Beats checked: 10  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | no-wordy-card §8.5: NikBearBrownTerminalAsk: per-element check passed (max 8 words in 'out… | PASS | — |
| B01 | ? | no video | SKIP | — |
| B02 | ? | no-wordy-card §8.5: NikBearBrownTerminalAsk: per-element check passed (max 0 words in 'n/a… | PASS | — |
| B03 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |
| B05 | ? | no-wordy-card §8.5: NikBearBrownTerminalAsk: per-element check passed (max 0 words in 'n/a… | PASS | — |
| B06 | ? | no video | SKIP | — |
| B07 | ? | no video | SKIP | — |
| B08 | ? | no video | SKIP | — |
| B09 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 5 | 0 |
| min-size §8.1 | 6 | 0 |
| overflow §8.2 | 6 | 0 |
| contrast §8.3 | 6 | 0 |
| kerning §8.4 | 1 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
