# BUILD-LOG — claude-liam-deep-11-communicating-uncertainty

## Gate: PLAN (awaiting human sign-off)
Deep-explainer plan-stage deliverable. Produced: `beat_sheet.json`, `PLAN.md`, `FACTCHECK.md`, `SOURCES.md`, `BUILD-LOG.md`. NOT produced (downstream of this gate): audio, previz, SHOPPING.md (Gate D2 is after audio lock), render.

## Linter (self-check)
```
== claude-liam-deep-11-communicating-uncertainty
   beats=35 body=29 est=523s (~8m43s) jsonOK dupIDs=none
   VOX=24.1%(7) MANIM=27.6%(8) REMOTION=34.5%(10) CARD=13.8%(4)
   vox_lint=PASS  spine=OK  same-lane-warns=none
```
All gates green: jsonOK · vox in 20–25% target band · spine OK (B00 ClaudeComposerAsk → ClaudeVerdictArtifact → "Your turn." ClaudeComposerAsk → ClaudeTitleOutro) · no >2 same-lane run · est ~8m43s within 300–600s.

## Decisions
- Genre fit: chapter is genuinely multi-movement (verb taxonomy → ladder → layered doc → calibration metrics → subgroup/fixes → prose/peer-critique) → deep-explainer is correct, not ai-explainer.
- Register: Teardown (deep-explainer default) — narration judges the writing habit and the metric stack, doesn't parrot them.
- Beat mix landed VOX 24.1% / MANIM 27.6% / REMOTION 34.5% / CARD 13.8%. CARD kept lean per doctrine (≤~18%): Acts III and VI fold their openers into spark-lines (A3R, A6R) instead of SlateCards; Acts I/II/IV/V keep explicit cards.
- **No vox run** this cut — no continuous physical scene earns a 2–3 beat camera move; every VOX is a discrete still, hard-cut. All lane changes hard-cut per the vox-run contract.
- MANIM carries every math/measure beat (three-verbs, ladder, two-axes projection, Brier + decomposition, reliability diagram, subgroup-ECE washout, temperature scaling, conformal coverage); `equation_tangent: true` on the four with real equations (A4M Brier, A5M subgroup ECE, A5M2 temp scaling, A5M3 conformal). REMOTION carries the rhetorical/structural beats (assertibility, ECE trap, reviewer legibility, layered doc, subgroup table, fix-symptom, evidence ladder, prose moves, fluency-trap, specific critique).
- Cold-open ask lands answered in `output` (the 87%/three-verbs hook, answered "the evidence earns C — observe"). Handoff prompt (BHTF) is read aloud verbatim AND discussed, per your-turn contract.
- Title chosen to mirror the exemplar's two-beat reframe form and the chapter's own cold open: "The Number Didn't Change. The Verb Did."

## DOUBLE-CHECK / unverified-source handling
- Source is a rough draft with git merge markers → read HEAD (ch 11) only; incoming ch-12 renumbering ignored.
- Stripped: specific ECE thresholds (chapter `[verify]`), the "overconfidence dominant regardless of architecture" superlative and the LLM-overconfidence extension (chapter `[verify]`), the kCE "hasn't replaced ECE" datable remark. Sepsis figures softened to qualitative and verify-gated (Wong et al. 2021). See FACTCHECK.md.
- No invented persons, numbers, quotes, or institutions. 87% cold-open figure is the chapter's own illustrative device.

## MISSING / TODO (post-approval)
- MISSING: FACTCHECK verification pass (Gate F) — IPCC scheme, Guo/Minderer framing, and the sepsis external-validation figures flagged VERIFY.
- MISSING: real Manim scene implementations (scenes named in `shot.manim.scene`; specs in `shot.manim.spec`) — incl. the four equation-tangent scenes.
- MISSING: `anim.json` classification pass for the DeckPattern beats (A3R2 branch, A4R threshold, A5R2 divergence) — author before build per animated-deck gate.
- MISSING: pantry stills (7) — 6 Tier 1 + 1 Tier 2 (A5V ICU, disclosure sidecar + generic-imagery constraint). Briefs in each beat's `pantry_brief`. SHOPPING.md written after audio lock (Gate D2) — NOT in this plan deliverable.

## Gate signatures
- PLAN: ____________ (human)   ·   FACTCHECK: ____________   ·   GATE P (narration→audio): ____________

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  A1C (SlateCard): verdict card → headline compressed to ≤12w: 'The Verb Is the Claim'
  A1M (SlateCard): verdict card → headline compressed to ≤12w: 'The number is fixed — the verb is the variable'
  A1V (SlateCard): verdict card → headline compressed to ≤12w: 'The verb feels like grammar — it isn't'
  A1R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A2C (SlateCard): verdict card → headline compressed to ≤12w: 'The Frozen Ladder'
  A2M (SlateCard): verdict card → headline compressed to ≤12w: 'hypothesize → … → conclude → prove'
  A2M2 (SlateCard): verdict card → headline compressed to ≤12w: 'Caution × strength — flattened to one usable line'
  A2V (SlateCard): verdict card → headline compressed to ≤12w: 'Evidence at observe — verb at conclude'
  A3R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A3V (SlateCard): verdict card → headline compressed to ≤12w: 'Jargon hides the verb — plain English exposes it'
  A3R2 (DeckPattern): deck note → compressed to ≤12w: 'legible structure: any claim → its evidence → its '
  A4C (SlateCard): verdict card → headline compressed to ≤12w: 'Does the Confidence Track Reality?'
  A4V (SlateCard): verdict card → headline compressed to ≤12w: '80% means: right on 80% of the 80% days'
  A4M (SlateCard): verdict card → headline compressed to ≤12w: 'BS = mean squared (claim − outcome); a proper scor'
  A4R (DeckPattern): deck note → compressed to ≤12w: 'same data, different bin count → a different ECE; '
  A4M2 (SlateCard): verdict card → headline compressed to ≤12w: 'Below the diagonal = overconfident; the shape is t'
  A5C (SlateCard): verdict card → headline compressed to ≤12w: 'Where Aggregate Metrics Lie'
  A5V (SlateCard): verdict card → headline compressed to ≤12w: 'Aggregate looked fine — the deployment was failing'
  A5M (SlateCard): verdict card → headline compressed to ≤12w: 'A small subgroup's failure is outvoted by the aver'
  A5R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A5M2 (SlateCard): verdict card → headline compressed to ≤12w: 'p = softmax(z/T), T>1 flattens — accuracy unchange'
  A5R2 (DeckPattern): deck note → compressed to ≤12w: ''
  A5M3 (SlateCard): verdict card → headline compressed to ≤12w: 'P(y ∈ C(x)) ≥ 1−α — but the coverage is only margi'
  A5R3 (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A6R (ChipGrid): chip grid (structured display, individual chips were already ≤12w)
  A6V (SlateCard): verdict card → headline compressed to ≤12w: 'The mismatches you made are the ones you can't see'
  A6R2 (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A6V2 (SlateCard): verdict card → headline compressed to ≤12w: 'Conclude ships it. Suggest asks for another study.'
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
