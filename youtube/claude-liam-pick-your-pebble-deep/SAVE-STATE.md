# SAVE-STATE — claude-liam-pick-your-pebble-deep
_Timestamp: 2026-07-30 (confirmed by Bear)_

## What was built
Full deep-explainer reel for "Pick Your Pebble" — the Agentic Casebook documentary
spine cut. Supersedes the abstract ai-explainer in `claude-liam-pick-your-pebble/`.

Build folder: `computational-skepticism-for-ai/youtube/claude-liam-pick-your-pebble-deep/`

## Files written
- `beat_sheet.json` — 27 beats (B00 + 23 body + BVDT/BHTF/BOUT), FormBCard cueFrame
  fixed (per-item, not top-level array)
- `scenes.py` — 6 Manim scenes, two layout fixes applied
- `PEDAGOGY.md` — VERDICT: PASS
- `BUILD-LOG.md` — design decisions D1–D7

## Bugs fixed during build
1. **A3M1_PredictionLock GATE B FAIL** — POPPER ✕ falsifier text overlap 37%
   Fix: popper_cap → [-4.8,-1.5,0]; popper_lbl → [0.2,-2.2,0] sz=22 (stacked)

2. **A3M3_PAFailure GATE B WARN** — SEVERITY:HIGH ✕ subtitle overlap 18%
   Fix: sev_lbl → [-3.5,-1.95,0] sz=28; sev_sub → [0.2,-2.6,0] sz=22 (stacked)

3. **FormBCard A1F1/A2F1/A2F2 Frame NaN** — cueFrames was a top-level array;
   remotion_scenes.py passes props raw (no Zod defaults), so item.cueFrame = undefined.
   Fix: moved cueFrame onto each item in beat_sheet.json; removed top-level cueFrames.

## Gate state at last `art run` (exit code 0)
- GATE B: PASS (all 6 Manim scenes CLEAN after fixes)
- GATE A (static): PASS (all scenes, including fixed A4M1_Attestation)
- FormBCard: PASS after per-item cueFrame fix
- GATE T: pending read of run output
- CHECKS-REPORT.md: pending

## Missing pantry stills (SHOPPING.md items)
- A3V1 (Tier 2) — Ch8 Fig 8.6, images/08-validating-agentic-ai...-fig-05.png
- A3V2 (Tier 2) — Ch8 Fig 8.11, images/08-validating-agentic-ai...-fig-09.png
- A1V1 (Tier 1 illustrative) — Agents of Chaos study overview
- A4V1 (Tier 1 illustrative) — attestation checklist with gaps
All 4 VOX stills render as FormACard slates until supplied.

## Standing orders
- STOP at slate cut — no art final / art post / 4K / TOPOST / publish
- Bear reviews before any next step
