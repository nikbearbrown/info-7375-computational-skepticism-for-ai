# TYPECHECK.md — GATE T

Reel: `claude-liam-lecture-the-skeptics-toolkit`  |  Checked: 2026-10-10T02:16  |  Overall: PASS  |  Beats checked: 71  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [BVDT] narration recites the card (0.94) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BOPEN | bookend | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| BIDEA | bookend | light | min-size §8.1: min text-run height 61px >= floor 41px | PASS | — |
| BDEFS | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | manim | light | min-size §8.1: min text-run height 61px >= floor 41px | PASS | — |
| B02 | manim | light | min-size §8.1: min text-run height 60px >= floor 41px | PASS | — |
| B03 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| B04 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B05 | manim | light | min-size §8.1: min text-run height 51px >= floor 41px | PASS | — |
| B06 | manim | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| B07 | manim | light | min-size §8.1: min text-run height 57px >= floor 41px | PASS | — |
| B08 | manim | light | min-size §8.1: min text-run height 72px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| A2 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | manim | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |
| B10 | manim | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |
| B11 | manim | light | min-size §8.1: min text-run height 59px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B12 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| A3 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | manim | light | min-size §8.1: min text-run height 57px >= floor 41px | PASS | — |
| B14 | manim | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |
| B15 | manim | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |
| B16 | manim | light | min-size §8.1: min text-run height 70px >= floor 41px | PASS | — |
| B17 | manim | light | min-size §8.1: min text-run height 66px >= floor 41px | PASS | — |
| A4 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | manim | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |
| B19 | manim | light | min-size §8.1: min text-run height 59px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B20 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| B21 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B22 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| B23 | manim | light | min-size §8.1: min text-run height 62px >= floor 41px | PASS | — |
| A5 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B24 | manim | light | min-size §8.1: min text-run height 66px >= floor 41px | PASS | — |
| B25 | manim | light | min-size §8.1: min text-run height 69px >= floor 41px | PASS | — |
| B26 | manim | light | min-size §8.1: min text-run height 57px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B27 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| A6 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B28 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B29 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| B30 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px | PASS | — |
| B31 | manim | light | min-size §8.1: min text-run height 62px >= floor 41px | PASS | — |
| B32 | manim | light | min-size §8.1: min text-run height 52px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B33 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px | PASS | — |
| A7 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B34 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B35 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B36 | manim | light | min-size §8.1: min text-run height 53px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B37 | manim | light | min-size §8.1: min text-run height 57px >= floor 41px | PASS | — |
| A8 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B38 | manim | light | min-size §8.1: min text-run height 105px >= floor 41px | PASS | — |
| B39 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B40 | manim | light | min-size §8.1: min text-run height 59px >= floor 41px | PASS | — |
| B41 | manim | light | min-size §8.1: min text-run height 57px >= floor 41px | PASS | — |
| B42 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| B43 | manim | light | min-size §8.1: min text-run height 57px >= floor 41px | PASS | — |
| A9 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B44 | manim | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| B45 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px | PASS | — |
| B46 | manim | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |
| B47 | manim | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| B48 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B49 | manim | light | min-size §8.1: min text-run height 57px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| A10 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B50 | manim | light | min-size §8.1: min text-run height 54px >= floor 41px | PASS | — |
| B51 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| B52 | manim | light | min-size §8.1: min text-run height 47px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B53 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B54 | manim | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| B55 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| BVDT | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | bookend | dark | min-size §8.1: min text-run height 102px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 11 | 0 |
| min-size §8.1 | 71 | 0 |
| overflow §8.2 | 71 | 0 |
| contrast §8.3 | 71 | 0 |
| contrast-local §8.3b | 71 | 0 |
| bbox-overlap §8.6b | 71 | 0 |
| card-clip §8.13 | 71 | 0 |
| kerning §8.4 | 55 | 0 |
| redundancy §8.10 (advisory) | 1 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
