# TYPECHECK.md — GATE T

Reel: `claude-liam-deep-07-fairness-metrics`  |  Checked: 2026-07-28T01:28  |  Overall: **FAIL**  |  Beats checked: 31  |  FAILs: 8

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

> **⚠ STRUCTURAL — §8.4 KERNING:** `scenes.py` calls `Text()` with no `font=` argument.
> Pango will use a system fallback font — the gappy-letter spacing bug (w a v e s  l i k e  t h i s) is active for ALL Manim beats.
> **Fix:** add `font='EB Garamond'` to every `Text()` and `MarkupText()` call in `scenes.py` (or to every helper that calls them).
> Then re-render all Manim beats and re-run GATE T.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | BOOKEND | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| A1C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1R | REMOTION | min-size §8.1: smallest text run 31px < floor 35px (3.2% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| A1M | MANIM | kerning §8.4: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A1V | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2K | ASK | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| A2M | MANIM | kerning §8.4: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A2M2 | MANIM | kerning §8.4: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A2R | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 5 words in 'title') | PASS | — |
| A3V1 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3V2 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3R | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3M | MANIM | kerning §8.4: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A4C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4R | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4V | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5M | MANIM | kerning §8.4: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A5V | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5K | ASK | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| A5M2 | MANIM | kerning §8.4: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A5R | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5M3 | MANIM | kerning §8.4: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A6R | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6R2 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6V | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6R3 | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 10 words in 'note') | PASS | — |
| BVDT | CLOSING | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BHTF | CLOSING | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | CLOSING | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

### A1R (REMOTION)
- **min-size §8.1**: smallest text run 31px < floor 35px (3.2% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **overflow §8.2**: 1 text run(s) outside title-safe box (192,108)→(3648,2052) at 3840×2160
- **Fix:** Increase font_size in scenes.py or Remotion component

### A1M (MANIM)
- **kerning §8.4**: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy-letter spacing (w a v e s). Fix: add font='EB Garamond' to every Text()/MarkupText() call.
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### A2M (MANIM)
- **kerning §8.4**: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy-letter spacing (w a v e s). Fix: add font='EB Garamond' to every Text()/MarkupText() call.
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### A2M2 (MANIM)
- **kerning §8.4**: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy-letter spacing (w a v e s). Fix: add font='EB Garamond' to every Text()/MarkupText() call.
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### A3M (MANIM)
- **kerning §8.4**: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy-letter spacing (w a v e s). Fix: add font='EB Garamond' to every Text()/MarkupText() call.
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### A5M (MANIM)
- **kerning §8.4**: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy-letter spacing (w a v e s). Fix: add font='EB Garamond' to every Text()/MarkupText() call.
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### A5M2 (MANIM)
- **kerning §8.4**: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy-letter spacing (w a v e s). Fix: add font='EB Garamond' to every Text()/MarkupText() call.
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### A5M3 (MANIM)
- **kerning §8.4**: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy-letter spacing (w a v e s). Fix: add font='EB Garamond' to every Text()/MarkupText() call.
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 25 | 0 |
| min-size §8.1 | 30 | 1 |
| overflow §8.2 | 30 | 1 |
| contrast §8.3 | 30 | 0 |
| kerning §8.4 | 7 | 7 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
