# BUILD-LOG — claude-liam-pick-your-pebble-deep
_Date: 2026-07-30 | Genre: deep-explainer | Channel: claude-liam (am_onyx, Kokoro, free)_

## Source material
- Worked example: `assignments/agentic-casebook-WORKED-EXAMPLE.md`
- Spec: `assignments/agentic-casebook-red-team.md`
- Chapter: `chapters/08-validating-agentic-ai-when-autonomous-systems-misbehave.md`
- Study: Shapira et al., arXiv:2602.20021 (Agents of Chaos, 2026)

## Design decisions

**D1 — Supersedes abstract cut**: This reel is the documentary spine version of
"Pick Your Pebble" — spine is the worked casebook (Case G-01), not the abstract
rules. The abstract cut in `claude-liam-pick-your-pebble/` is retained but superseded.

**D2 — Beat mix (23 body beats)**:
- VOX 17.4% (4 beats) — in 15-30% PASS band
- MANIM 26.1% (6 beats) — in 25-40% PASS band
- REMOTION 39.1% (9 beats) — in 30-45% PASS band
- CARD 17.4% (4 beats)
- Lint: PASS — no >2 consecutive same-lane outside vox run

**D3 — Missing Ch 8 figures**: Both book figures are missing from `images/`:
- `08-validating-agentic-ai-when-autonomous-systems-misbehave-fig-05.png` (Fig 8.6, Case #1 failure chain)
- `08-validating-agentic-ai-when-autonomous-systems-misbehave-fig-09.png` (Fig 8.11, false-success catch)
- These are listed on SHOPPING.md as Tier 2 items (specific book artifacts, need to be generated from the D3 spec in the chapter or exported from the build pipeline)
- VOX beats A3V1 and A3V2 render as slates until these are supplied

**D4 — No vox run**: A3V1 (fig-05) and A3V2 (fig-09) are separated by Manim beat A3M2 (the report-vs-world animation). No frame continuity needed — these are separate compositions and hard-cut between them is correct.

**D5 — FormBCard cueFrames**: Set as estimated values in the beat sheet. Will be calibrated to actual MP3 durations after audio generation and locked in SHOPPING.md.

**D6 — Manim scenes (6 total)**:
- A1M1_BlastRadius — 5 tool-surface categories + IRREVERSIBLE tags
- A2M1_CandidateFailureMode — TASK vs AGENT SCOPE gap (terracotta FALSE SUCCESS)
- A3M1_PredictionLock — Taxonomy → Prediction, Popper falsifier
- A3M2_ReportVsWorld — ARTIFACT ≠ WORLD (the honesty gap)
- A3M3_PAFailure — PA primary + PF secondary + SEVERITY: HIGH
- A4M1_Attestation — TESTED (teal) vs NOT TESTED (mute)

**D7 — VOX stills (4 total, 2 missing)**:
- A1V1: Agents of Chaos study overview (Tier 1 illustrative, kenburns) — MISSING
- A3V1: Ch8 fig-05 Case #1 failure chain (Tier 2 book artifact, drawon) — MISSING
- A3V2: Ch8 fig-09 false-success catch (Tier 2 book artifact, kenburns) — MISSING
- A4V1: Attestation gaps visualization (Tier 1 illustrative, hold) — MISSING

## Gate log
- GATE P: beat sheet authored 2026-07-30; slate previz pending
- SHOPPING.md: written after audio lock (post art run)
- FACTCHECK.md: bypassed with ART_FACTS=0 for previz only

## MISSING items (for SHOPPING.md)
- MISSING: A3V1 pantry still — Ch8 fig-05 (08-validating-agentic-ai...-fig-05.png); generate from D3 spec in ch08 or export from svg-to-png pipeline
- MISSING: A3V2 pantry still — Ch8 fig-09 (08-validating-agentic-ai...-fig-09.png); generate from D3 spec in ch08 or export from svg-to-png pipeline
- MISSING: A1V1 pantry still — multi-agent environment mockup (Tier 1, illustrative)
- MISSING: A4V1 pantry still — attestation checklist with gaps (Tier 1, illustrative)
