# TYPECHECK.md — GATE T

Reel: `claude-liam-a-p-value-is-not-a-verdict`  |  Checked: 2026-08-31T12:40  |  Overall: PASS  |  Beats checked: 25  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 10 words in 'note') | PASS | — |
| B02 | MANIM | light | min-size §8.1: min text-run height 234px >= floor 41px | PASS | — |
| B03 | MANIM | light | min-size §8.1: min text-run height 108px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B04 | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 12 words in 'left.note') | PASS | — |
| B05 | MANIM | light | min-size §8.1: min text-run height 44px >= floor 41px | PASS | — |
| B06 | REMOTION | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 7 words in 'chips[2]') | PASS | — |
| B07 | MANIM | light | min-size §8.1: min text-run height 492px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B08 | MANIM | light | min-size §8.1: min text-run height 43px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B09 | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 12 words in 'left.note') | PASS | — |
| B10 | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B11 | MANIM | light | min-size §8.1: min text-run height 52px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B12 | MANIM | light | min-size §8.1: min text-run height 59px >= floor 41px | PASS | — |
| B13 | MANIM | light | min-size §8.1: min text-run height 71px >= floor 41px | PASS | — |
| B14 | REMOTION | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 8 words in 'title') | PASS | — |
| B15 | MANIM | light | min-size §8.1: hand-drawn pattern (B15_WallWithDoors) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B16 | MANIM | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B17 | REMOTION | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 7 words in 'chips[0]') | PASS | — |
| B18 | MANIM | light | min-size §8.1: min text-run height 80px >= floor 41px | PASS | — |
| B19 | MANIM | light | min-size §8.1: min text-run height 91px >= floor 41px | PASS | — |
| B20 | MANIM | light | min-size §8.1: min text-run height 78px >= floor 41px | PASS | — |
| B21 | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 11 words in 'left.note') | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | BOOKEND | light | min-size §8.1: min text-run height 52px >= floor 41px (individual-char fallback at 2×) | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 7 | 0 |
| min-size §8.1 | 25 | 0 |
| overflow §8.2 | 25 | 0 |
| contrast §8.3 | 25 | 0 |
| contrast-local §8.3b | 25 | 0 |
| bbox-overlap §8.6b | 25 | 0 |
| card-clip §8.13 | 25 | 0 |
| kerning §8.4 | 13 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
