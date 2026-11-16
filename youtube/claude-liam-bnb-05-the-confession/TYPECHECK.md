# TYPECHECK.md — GATE T

Reel: `claude-liam-bnb-05-the-confession`  |  Checked: 2026-07-27T19:58  |  Overall: **FAIL**  |  Beats checked: 7  |  FAILs: 1

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

> **⚠ STRUCTURAL — §8.4 KERNING:** `scenes.py` calls `Text()` with no `font=` argument.
> Pango will use a system fallback font — the gappy-letter spacing bug (w a v e s  l i k e  t h i s) is active for ALL Manim beats.
> **Fix:** add `font='EB Garamond'` to every `Text()` and `MarkupText()` call in `scenes.py` (or to every helper that calls them).
> Then re-render all Manim beats and re-run GATE T.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| B01 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | ? | overflow §8.2: 1 text run(s) outside title-safe box (192,108)→(3648,2052) at 3840×2160 | **FAIL** | Move text inside title-safe 90% box |
| BHTF | ? | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| BOUT | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

### BVDT (?)
- **overflow §8.2**: 1 text run(s) outside title-safe box (192,108)→(3648,2052) at 3840×2160
- **Fix:** Move text inside title-safe 90% box

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 3 | 0 |
| min-size §8.1 | 7 | 0 |
| overflow §8.2 | 7 | 1 |
| contrast §8.3 | 7 | 0 |
| kerning §8.4 | 0 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
