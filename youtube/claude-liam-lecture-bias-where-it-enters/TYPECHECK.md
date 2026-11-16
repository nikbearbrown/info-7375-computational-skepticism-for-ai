# TYPECHECK.md — GATE T

Reel: `claude-liam-lecture-bias-where-it-enters`  |  Checked: 2026-10-10T03:11  |  Overall: PASS  |  Beats checked: 99  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [BVDT] narration recites the card (0.95) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BOPEN | bookend | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| BIDEA | bookend | light | min-size §8.1: min text-run height 61px >= floor 41px | PASS | — |
| BDEFS | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | manim | light | min-size §8.1: min text-run height 59px >= floor 41px | PASS | — |
| B02 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B03 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B04 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| B05 | manim | light | min-size §8.1: min text-run height 51px >= floor 41px | PASS | — |
| B06 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| A2 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | manim | light | min-size §8.1: min text-run height 51px >= floor 41px | PASS | — |
| B08 | manim | light | min-size §8.1: min text-run height 52px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B09 | manim | light | min-size §8.1: min text-run height 41px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B10 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | manim | light | min-size §8.1: min text-run height 59px >= floor 41px | PASS | — |
| B12 | manim | light | min-size §8.1: min text-run height 47px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B13 | manim | light | min-size §8.1: min text-run height 347px >= floor 41px | PASS | — |
| A3 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | manim | light | min-size §8.1: min text-run height 51px >= floor 41px | PASS | — |
| B15 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B16 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B17 | manim | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| B18 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B19 | manim | light | min-size §8.1: min text-run height 55px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B20 | manim | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| A4 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | manim | light | min-size §8.1: min text-run height 51px >= floor 41px | PASS | — |
| B22 | manim | light | min-size §8.1: min text-run height 51px >= floor 41px | PASS | — |
| B23 | manim | light | min-size §8.1: min text-run height 52px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B24 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B25 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B26 | manim | light | min-size §8.1: min text-run height 51px >= floor 41px | PASS | — |
| B27 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| A5 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B28 | manim | light | min-size §8.1: min text-run height 60px >= floor 41px | PASS | — |
| B29 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B30 | manim | light | min-size §8.1: min text-run height 47px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B31 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B32 | manim | light | min-size §8.1: min text-run height 55px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| A6 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B33 | manim | light | min-size §8.1: min text-run height 47px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B34 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B35 | manim | light | min-size §8.1: min text-run height 54px >= floor 41px | PASS | — |
| B36 | remotion | light | no-wordy-card §8.5: pull-quote (9 words ≤ 12) | PASS | — |
| B37 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| B38 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B39 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B40 | manim | light | min-size §8.1: min text-run height 296px >= floor 41px | PASS | — |
| B41 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| A7 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B42 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B43 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B44 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B45 | manim | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| B46 | manim | light | min-size §8.1: min text-run height 58px >= floor 41px | PASS | — |
| B47 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| A8 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B48 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B49 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B50 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B51 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B52 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B53 | manim | light | min-size §8.1: min text-run height 88px >= floor 41px | PASS | — |
| B54 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B55 | remotion | light | no-wordy-card §8.5: pull-quote (9 words ≤ 12) | PASS | — |
| A9 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B56 | manim | light | min-size §8.1: min text-run height 1025px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B57 | manim | light | min-size §8.1: min text-run height 61px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B58 | manim | light | min-size §8.1: min text-run height 93px >= floor 41px | PASS | — |
| B59 | manim | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| B60 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B61 | manim | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| B62 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B63 | manim | light | min-size §8.1: min text-run height 54px >= floor 41px | PASS | — |
| B64 | remotion | light | no-wordy-card §8.5: pull-quote (8 words ≤ 12) | PASS | — |
| A10 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B65 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| B66 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B67 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B68 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B69 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B70 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| B71 | manim | light | min-size §8.1: min text-run height 54px >= floor 41px | PASS | — |
| B72 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| A11 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B73 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| B74 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B75 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B76 | manim | light | min-size §8.1: min text-run height 45px >= floor 41px | PASS | — |
| B77 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px | PASS | — |
| B78 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| B79 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B80 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B81 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B82 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BVDT | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | bookend | dark | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 20 | 0 |
| min-size §8.1 | 99 | 0 |
| overflow §8.2 | 99 | 0 |
| contrast §8.3 | 99 | 0 |
| contrast-local §8.3b | 99 | 0 |
| bbox-overlap §8.6b | 99 | 0 |
| card-clip §8.13 | 99 | 0 |
| kerning §8.4 | 74 | 0 |
| redundancy §8.10 (advisory) | 3 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
