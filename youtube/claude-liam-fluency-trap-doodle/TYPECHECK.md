# TYPECHECK.md — GATE T

Reel: `claude-liam-fluency-trap-doodle`  |  Checked: 2026-07-24T08:06  |  Overall: PASS  |  Beats checked: 36  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

> **⚠ STRUCTURAL — §8.4 KERNING:** `scenes.py` calls `Text()` with no `font=` argument.
> Pango will use a system fallback font — the gappy-letter spacing bug (w a v e s  l i k e  t h i s) is active for ALL Manim beats.
> **Fix:** add `font='EB Garamond'` to every `Text()` and `MarkupText()` call in `scenes.py` (or to every helper that calls them).
> Then re-render all Manim beats and re-run GATE T.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B16 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B17 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B19 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B23 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B24 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B25 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B26 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B27 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B28 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B29 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B30 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B31 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B32 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B33 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B34 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B35 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 36 | 0 |
| min-size §8.1 | 36 | 0 |
| overflow §8.2 | 36 | 0 |
| contrast §8.3 | 36 | 0 |
| kerning §8.4 | 0 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
