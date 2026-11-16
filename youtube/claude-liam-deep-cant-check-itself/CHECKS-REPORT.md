# CHECKS-REPORT — You Can't Check a Model With Itself
`claude-liam-deep-cant-check-itself` | 2026-07-28 | Gate: SLATE PREVIZ

---

## Output

`claude-liam-deep-cant-check-itself-slate.mp4` — 416.0s, silent, in the reel folder.  
`art run` exited 2 (GATE V failed). Slate mp4 IS produced and watchable.  
STOP per standing order. Bear reviews before next step.

---

## Beat render ledger

| Beat | Status | Pattern / Note |
|---|---|---|
| B00 | VIDEO → **stale cleared** | ClaudeComposerAsk. Output lines shortened (4→3); media/B00.mp4 deleted for re-render on next compile. |
| A1C | VIDEO 6.0s | FormACard ✓ |
| A1R | VIDEO 15.0s | DeckPattern ✓ |
| A1R2 | VIDEO 12.0s | FormACard (dark) ✓ |
| **A1M** | **SLATE 11.0s** | Manim — scenes.py stub |
| A2C | VIDEO 5.0s | FormACard ✓ |
| **A2M** | **SLATE 15.0s** | Manim — scenes.py stub |
| A2R | VIDEO 14.0s | DeckPattern ✓ |
| **A2V** | **SLATE 13.0s** | VOX — no pantry still |
| **A2M2** | **SLATE 13.0s** | Manim — scenes.py stub |
| A3C | VIDEO 5.0s | FormACard ✓ |
| A3R | VIDEO 15.0s | DeckPattern ✓ |
| **A3M** | **SLATE 17.0s** | Manim — scenes.py stub |
| A3R2 | VIDEO 11.0s | FormACard (dark) ✓ |
| A4C | VIDEO 5.0s | FormACard ✓ |
| A4R | VIDEO 14.0s | DeckPattern ✓ |
| **A4V** | **SLATE 14.0s** | VOX — no pantry still |
| **A4M** | **SLATE 14.0s** | Manim — scenes.py stub |
| A4R2 | VIDEO 11.0s | FormACard ✓ |
| A5C | VIDEO 5.0s | FormACard ✓ |
| **A5V** | **SLATE 11.0s** | VOX run R1 — no pantry still |
| **A5V2** | **SLATE 12.0s** | VOX run R1 — no pantry still |
| A5R | VIDEO 15.0s | DeckPattern ✓ |
| A5SH | VIDEO 14.0s | ClaudeCodeBeat (shell skin) ✓ |
| **A5M** | **SLATE 13.0s** | Manim — scenes.py stub |
| A6C | VIDEO 5.0s | FormACard ✓ |
| A6R | VIDEO 16.0s | DeckPattern ✓ |
| **A6V** | **SLATE 12.0s** | VOX — no pantry still |
| **A6M** | **SLATE 12.0s** | Manim — scenes.py stub |
| **A6R2** | **SLATE 15.0s** | Manim — scenes.py stub |
| BVDT | VIDEO 18.0s | ClaudeVerdictArtifact ✓ |
| BASK | VIDEO 18.0s | ClaudeComposerAsk ✓ |
| BOUT | VIDEO 12.0s | ClaudeTitleOutro ✓ |

20 VIDEO (B00 stale-cleared) / 13 SLATE (8 Manim + 5 VOX pantry). Expected.

---

## GATE BANNED-CARD: PASS ✓

---

## GATE V — visual QC: FAILED (exit 2)

**2 BLOCKERS — B00 edge-bleed** (both sample points, 50% and 85% through the beat)  
`ClaudeComposerAsk` with 4 long output lines caused content to overflow the title-safe bottom edge.  
**Fix applied:** output array shortened from 4 lines to 3 shorter lines in beat_sheet.json. media/B00.mp4 deleted. Will re-render on next `art run`.

**56 MAJOR — underfill on every beat**  
Every beat failed the 55% fill threshold. Analysis from QC contact sheet:

| Category | Beats | Fill observed | Root cause |
|---|---|---|---|
| FormACard single-line (act cards) | A1C,A2C,A3C,A4C,A5C,A6C | 2–3% | Single serif line on cream — intentional generous negative space. This is the design vocabulary, not a defect. |
| FormACard multi-line (dark) | A1R2, A3R2, A4R2 | 8–13% | 2–3 lines on dark ground — intentional generous negative space. |
| DeckPattern (two-column) | A1R,A2R,A3R,A4R,A5R,A6R | 8–28% | Two-column cream layout — restrained by design. |
| Manim SLATE cards | A1M,A2M,A2M2,A3M,A4M,A5M,A6M,A6R2 | 30–31% | Slate card shows beat ID + narration text center — expected at this stage. |
| VOX SLATE cards | A2V,A4V,A5V,A5V2,A6V | 46–49% | Slate with border shows narration + beat ID — will resolve when pantry stills fill these slots. |

**Diagnosis:** systemic gate calibration issue. The Claude brand DESIGN-PRINCIPLES explicitly specify generous negative space and typography-led layouts. Single-line FormACard and DeckPattern cream layouts will never reach 55% pixel coverage — that's the design intent, not a defect. Same class of issue as the Manim dark canvas gate calibration (type_check §8.1/§8.2 early-return).

**The pipeline's own suggestion:** `ART_STRICT=0 downgrades MAJOR to warnings.`

**Bear's decision needed:** 
- Option A: run subsequent compiles with `ART_STRICT=0` to downgrade underfill MAJOR → warnings for this brand.  
- Option B: add `"fill_claim": "generous-negative-space"` to FormACard and DeckPattern beats to make the gate stand down (if the gate supports a claim field).  
- Option C: calibrate the underfill threshold for the `claude` palette/brand — the 55% minimum was set for a different visual register.

---

## FACTCHECK.md — fixes needed (non-blocking, fix before review cut)

| Fix | Detail |
|---|---|
| Verdict column format | SPECULATIVE / UNSOURCED not recognized. Map to: `EXEMPT` with note for SPECULATIVE; `PASS (qualitative)` for UNSOURCED claims stated as "tends to." |
| Status: line | Add `Status: PLAN — Bear signs after watching slate` at top of claim table |
| A1R row missing | Beat mentions "Fable 5 (speculative)" — add a row (claim: model name used as framing device; verdict: EXEMPT — speculative label in narration and modelLabel) |

---

## Beat-lint — WARN flags (non-blocking)

- **6 act cards need motion_claim** (A1C–A6C, 3.5–8.0s band): add `"motion_claim": "title fades in on cue"` to each.
- **3 cards over 8s** (A1R2 12s, A3R2 11s, A4R2 11s): mark as predict/commit dwells. Add `"motion_claim": "predict/commit — viewer sits with the contrast before narration moves on"` to each. All three are genuinely deliberate holds (the ≠ contrast, the upgrade paradox, the throughput bet).

---

## What Bear needs to do

1. **Watch the slate**: `claude-liam-deep-cant-check-itself-slate.mp4` (416s, silent).
2. **Decide on GATE V underfill**: ART_STRICT=0 or gate calibration or fill_claim field — your call.
3. **Approve narration** — any beats to rewrite?
4. **Decide on the 3 predict/commit cards** — confirm the dwells are intentional.
5. **Fix FACTCHECK.md** verdict column (or say "fix it" and I'll do it).
6. On approval: `art run` will re-render B00 (stale cleared), then proceed to Gate D2 + Gate D1 full previz after Kokoro audio.

---

`STANDING ORDER: STOPPED after art run. No art final / no post / no publish.`
