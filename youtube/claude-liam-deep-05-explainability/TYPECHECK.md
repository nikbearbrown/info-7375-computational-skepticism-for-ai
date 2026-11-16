# TYPECHECK.md — GATE T

Reel: `claude-liam-deep-05-explainability`  |  Checked: 2026-07-28T00:51  |  Overall: **FAIL**  |  Beats checked: 33  |  FAILs: 9

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

> **⚠ STRUCTURAL — §8.4 KERNING:** `scenes.py` calls `Text()` with no `font=` argument.
> Pango will use a system fallback font — the gappy-letter spacing bug (w a v e s  l i k e  t h i s) is active for ALL Manim beats.
> **Fix:** add `font='EB Garamond'` to every `Text()` and `MarkupText()` call in `scenes.py` (or to every helper that calls them).
> Then re-render all Manim beats and re-run GATE T.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | BOOKEND | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| A1C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1V | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1R | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1M | MANIM | kerning §8.4: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A2R | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 11 words in 'title') | PASS | — |
| A2M | MANIM | kerning §8.4: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A2M2 | MANIM | kerning §8.4: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A3C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3K | ASK | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| A3M | MANIM | kerning §8.4: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A3M2 | MANIM | kerning §8.4: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A3R | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3V | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4M | MANIM | kerning §8.4: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A4R | REMOTION | no-wordy-card §8.5: ChipGrid: per-element check passed (max 12 words in 'chips[0]') | PASS | — |
| A4M2 | MANIM | kerning §8.4: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A5C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5R | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5V | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5R2 | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 11 words in 'note') | PASS | — |
| A6R | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 10 words in 'left.note') | PASS | — |
| A6V1 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6V2 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6V3 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6R2 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| A7C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A7M | MANIM | kerning §8.4: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A7V | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A7R | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | CLOSING | overflow §8.2: 1 text run(s) outside title-safe box (192,108)→(3648,2052) at 3840×2160 | **FAIL** | Move text inside title-safe 90% box |
| BHTF | CLOSING | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | CLOSING | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

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

### A3M2 (MANIM)
- **kerning §8.4**: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy-letter spacing (w a v e s). Fix: add font='EB Garamond' to every Text()/MarkupText() call.
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### A4M (MANIM)
- **kerning §8.4**: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy-letter spacing (w a v e s). Fix: add font='EB Garamond' to every Text()/MarkupText() call.
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### A4M2 (MANIM)
- **kerning §8.4**: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy-letter spacing (w a v e s). Fix: add font='EB Garamond' to every Text()/MarkupText() call.
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### A7M (MANIM)
- **kerning §8.4**: scenes.py has no font= in Text() — Pango uses system fallback, causing gappy-letter spacing (w a v e s). Fix: add font='EB Garamond' to every Text()/MarkupText() call.
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### BVDT (CLOSING)
- **overflow §8.2**: 1 text run(s) outside title-safe box (192,108)→(3648,2052) at 3840×2160
- **Fix:** Move text inside title-safe 90% box

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 28 | 0 |
| min-size §8.1 | 33 | 0 |
| overflow §8.2 | 33 | 1 |
| contrast §8.3 | 33 | 0 |
| kerning §8.4 | 8 | 8 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
