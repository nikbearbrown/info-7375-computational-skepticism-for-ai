# TYPECHECK.md — GATE T

Reel: `claude-liam-cli-prediction-lock-harness`  |  Checked: 2026-07-27T22:41  |  Overall: PASS  |  Beats checked: 13  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

> **⚠ STRUCTURAL — §8.4 KERNING:** `scenes.py` calls `Text()` with no `font=` argument.
> Pango will use a system fallback font — the gappy-letter spacing bug (w a v e s  l i k e  t h i s) is active for ALL Manim beats.
> **Fix:** add `font='EB Garamond'` to every `Text()` and `MarkupText()` call in `scenes.py` (or to every helper that calls them).
> Then re-render all Manim beats and re-run GATE T.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| B01 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B02 | ? | min-size §8.1: min text-run height 56px >= floor 35px | PASS | — |
| B03 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | ? | min-size §8.1: min text-run height 56px >= floor 35px | PASS | — |
| B06 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | ? | min-size §8.1: min text-run height 71px >= floor 35px | PASS | — |
| BHTF | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B09 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 5 | 0 |
| min-size §8.1 | 13 | 0 |
| overflow §8.2 | 13 | 0 |
| contrast §8.3 | 13 | 0 |
| kerning §8.4 | 0 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
