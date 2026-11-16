# TYPECHECK.md — GATE T

Reel: `claude-liam-ra-06-disclosure-and-ship`  |  Checked: 2026-07-24T06:31  |  Overall: PASS  |  Beats checked: 7  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 1.6× expected advance.  Wordy budget: 2 elements.

> **⚠ STRUCTURAL — §8.4 KERNING:** `scenes.py` calls `Text()` with no `font=` argument.
> Pango will use a system fallback font — the gappy-letter spacing bug (w a v e s  l i k e  t h i s) is active for ALL Manim beats.
> **Fix:** add `font='EB Garamond'` to every `Text()` and `MarkupText()` call in `scenes.py` (or to every helper that calls them).
> Then re-render all Manim beats and re-run GATE T.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B01 | ? | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 11 words in 'artifactLines… | PASS | — |
| B02 | ? | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 11 words in 'artifactLines… | PASS | — |
| B03 | ? | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 12 words in 'artifactLines… | PASS | — |
| BVDT | ? | min-size §8.1: min text-run height 37px >= floor 35px | PASS | — |
| BHTF | ? | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 3 | 0 |
| min-size §8.1 | 7 | 0 |
| overflow §8.2 | 7 | 0 |
| contrast §8.3 | 7 | 0 |
| kerning §8.4 | 0 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
