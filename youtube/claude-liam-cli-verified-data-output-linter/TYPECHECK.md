# TYPECHECK.md — GATE T

Reel: `claude-liam-cli-verified-data-output-linter`  |  Checked: 2026-07-27T22:51  |  Overall: **FAIL**  |  Beats checked: 13  |  FAILs: 2

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

> **⚠ STRUCTURAL — §8.4 KERNING:** `scenes.py` calls `Text()` with no `font=` argument.
> Pango will use a system fallback font — the gappy-letter spacing bug (w a v e s  l i k e  t h i s) is active for ALL Manim beats.
> **Fix:** add `font='EB Garamond'` to every `Text()` and `MarkupText()` call in `scenes.py` (or to every helper that calls them).
> Then re-render all Manim beats and re-run GATE T.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| B01 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B02 | ? | min-size §8.1: min text-run height 54px >= floor 35px | PASS | — |
| B03 | ? | min-size §8.1: smallest text run 24px < floor 35px (3.2% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B04 | ? | min-size §8.1: smallest text run 34px < floor 35px (3.2% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B05 | ? | min-size §8.1: min text-run height 54px >= floor 35px | PASS | — |
| B06 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | ? | min-size §8.1: min text-run height 71px >= floor 35px | PASS | — |
| BHTF | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| B09 | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

### B03 (?)
- **min-size §8.1**: smallest text run 24px < floor 35px (3.2% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B04 (?)
- **min-size §8.1**: smallest text run 34px < floor 35px (3.2% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 5 | 0 |
| min-size §8.1 | 13 | 2 |
| overflow §8.2 | 13 | 0 |
| contrast §8.3 | 13 | 0 |
| kerning §8.4 | 0 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
