# TYPECHECK.md — GATE T

Reel: `computational-skepticism-practice-project-walkthrough`  |  Checked: 2026-11-15T18:17  |  Overall: PASS  |  Beats checked: 12  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B00] narration recites the card (0.82) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BIDEA | bookend | light | min-size §8.1: min text-run height 57px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BDEFS | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B00 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| BHTF | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | bookend | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 9 | 0 |
| min-size §8.1 | 12 | 0 |
| overflow §8.2 | 12 | 0 |
| contrast §8.3 | 12 | 0 |
| contrast-local §8.3b | 12 | 0 |
| bbox-overlap §8.6b | 12 | 0 |
| card-clip §8.13 | 12 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 8 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
