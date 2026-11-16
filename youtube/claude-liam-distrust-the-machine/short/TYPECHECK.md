# TYPECHECK.md — GATE T

Reel: `claude-liam-distrust-the-machine-short`  |  Checked: 2026-08-13T12:29  |  Overall: PASS  |  Beats checked: 17  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | — | no video | SKIP | — |
| B01 | BOOKEND | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | remotion | — | no-wordy-card §8.5: 2 element(s), 20 words — within budget. Detail: 'left.note' (9 words);… | PASS | — |
| B04 | BOOKEND | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | BOOKEND | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | remotion | — | no-wordy-card §8.5: 2 element(s), 18 words — within budget. Detail: 'left.note' (10 words)… | PASS | — |
| B11 | remotion | — | no-wordy-card §8.5: 2 element(s), 14 words — within budget. Detail: 'left.note' (8 words);… | PASS | — |
| B12 | BOOKEND | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B16 | remotion | — | no-wordy-card §8.5: pull-quote (12 words ≤ 12) | PASS | — |
| B17 | BOOKEND | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | manim | — | no video | SKIP | — |
| B21 | BOOKEND | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | ask | — | no video | SKIP | — |
| B27 | BOOKEND | — | no video | SKIP | — |
| BHTF | ? | — | no video | SKIP | — |
| BOUT | ? | — | no video | SKIP | — |
| END | ? | — | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 10 | 0 |
| min-size §8.1 | 0 | 0 |
| overflow §8.2 | 0 | 0 |
| contrast §8.3 | 0 | 0 |
| contrast-local §8.3b | 0 | 0 |
| bbox-overlap §8.6b | 0 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
