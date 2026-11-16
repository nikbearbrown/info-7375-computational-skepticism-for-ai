# TYPECHECK.md — GATE T

Reel: `cli-adversarial-perturbation-detector`  |  Checked: 2026-07-24T02:58  |  Overall: PASS  |  Beats checked: 13  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 1.6× expected advance.  Wordy budget: 2 elements.

> **⚠ STRUCTURAL — §8.4 KERNING:** `scenes.py` calls `Text()` with no `font=` argument.
> Pango will use a system fallback font — the gappy-letter spacing bug (w a v e s  l i k e  t h i s) is active for ALL Manim beats.
> **Fix:** add `font='EB Garamond'` to every `Text()` and `MarkupText()` call in `scenes.py` (or to every helper that calls them).
> Then re-render all Manim beats and re-run GATE T.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| NBB00 | ? | no video | SKIP | — |
| B00 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | ? | no video | SKIP | — |
| B02 | ? | no-wordy-card §8.5: NikBearBrownTerminalAsk: per-element check passed (max 0 words in 'n/a… | PASS | — |
| B03 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | no video | SKIP | — |
| B05 | ? | no-wordy-card §8.5: NikBearBrownTerminalAsk: per-element check passed (max 0 words in 'n/a… | PASS | — |
| B06 | ? | no video | SKIP | — |
| B07 | ? | no video | SKIP | — |
| B08 | ? | no video | SKIP | — |
| NBB01 | ? | no video | SKIP | — |
| NBB02 | ? | no video | SKIP | — |
| NBB03 | ? | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 4 | 0 |
| min-size §8.1 | 0 | 0 |
| overflow §8.2 | 0 | 0 |
| contrast §8.3 | 0 | 0 |
| kerning §8.4 | 0 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
