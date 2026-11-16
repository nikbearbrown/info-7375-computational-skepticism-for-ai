# BUILD-LOG — claude-liam-deep-05-explainability

## Gate: PLAN (awaiting human sign-off)
Deep-explainer plan-stage deliverable. Produced: `beat_sheet.json`, `PLAN.md`, `FACTCHECK.md`, `SOURCES.md`. NOT produced (downstream of this gate): audio, previz, SHOPPING.md (Gate D2 is after audio lock), render.

## Decisions
- Genre fit: chapter is genuinely multi-act (radiologist → SHAP is/isn't → Shapley math → LIME/counterfactual → three words → language game → honesty) → deep-explainer is the correct skill, not ai-explainer.
- Register: Teardown (deep-explainer default) — the chapter is a skepticism argument; narration judges the explanation toolkit, doesn't parrot it.
- Beat mix landed VOX 25.0% / MANIM 28.6% / REMOTION 32.1% / CARD 14.3%. Lint PASS. CARD kept LEAN (4 cards) by folding Acts II/IV/VI openers into spark-lines — leaner than the exemplar's 7 cards, per the CARD ≤~18% doctrine.
- The chapter's core tension (model's internal accounting vs a true account of the world) is carried as a DeckPattern **divergence** twice (A2R, A6R) — bracketing the math and the Ash case, exactly where the instruction pointed.
- Only one vox run (R1, Ash's "deleted" report — the language-game case) — the chapter's one place a continuous pull-back earns drama. All other lane changes hard-cut per the vox-run contract.
- Manim carries the math beats (shortcut correlation, force-sum/Efficiency, Rung-1 ceiling, Shapley formula w/ equation tangent, four axioms w/ equation tangent, LIME local fit, counterfactual nearest-flip, Reichenbach discovery-vs-justification). Remotion carries the rhetorical/structural beats (two divergences, decision-artifact + worked-example + three-words + two-reports + honest-posture ClaudeWindows, three-families ChipGrid, wrong-property threshold).
- One mid-film ASK (A3K) before the Shapley-formula Manim, per ASK→RESULT LAW.

## Source handling (rough-draft caution)
- Read HEAD side of every git merge marker (Chapter-5 numbering; `../images/05-...`). Ignored the `d78899b` Chapter-6 renumbering and the non-HEAD trailing D3-figure "Prompts" block.
- Radiologist case carried as the chapter's declared **composite**, never as a sourced incident.
- Datable "175B parameters" softened to "hundreds of billions."
- Chapter's `[verify]` aphorism ("need co-occurs with misalignment") omitted from narration.
- Ash provider-side persistence mechanics narrated generically (chapter flags them `[verify]`); no provider product/version named.

## MISSING / TODO (post-approval)
- MISSING: FACTCHECK verification pass (Gate F) — several source claims flagged VERIFY (shortcut-learning citations, LIME, Rudin, Reichenbach date, Agents-of-Chaos provider mechanics).
- MISSING: `anim.json` classification pass for the DeckPattern beats (A2R divergence, A5R2 threshold, A6R divergence) — author before build per animated-deck gate.
- MISSING: real Manim scene implementations (scenes named in `shot.manim.scene`; specs in `shot.manim.spec`).
- MISSING: pantry stills (7) — briefs in each beat's `pantry_brief`. Six Tier 1; ONE **Tier 3 (A7V Reichenbach portrait)** needing PD-source confirmation + AI-disclosure sidecar + credit. SHOPPING.md written after audio lock (Gate D2).

## Gate signatures
- PLAN: ____________ (human)   ·   FACTCHECK: ____________   ·   GATE P (narration→audio): ____________

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  A1C (SlateCard): verdict card → headline compressed to ≤12w: 'The Explanation That Made It Worse'
  A1V (SlateCard): verdict card → headline compressed to ≤12w: 'The reasons checked out — so she leaned in'
  A1R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A1M (SlateCard): verdict card → headline compressed to ≤12w: 'It reported the shortcut — and never named it one'
  A2R (DeckPattern): deck note → compressed to ≤12w: ''
  A2M (SlateCard): verdict card → headline compressed to ≤12w: 'One number per feature — summing to the deviation'
  A2M2 (SlateCard): verdict card → headline compressed to ≤12w: 'Four questions on higher rungs — SHAP can't climb'
  A3C (SlateCard): verdict card → headline compressed to ≤12w: 'The Mathematics of a Shapley Value'
  A3M (SlateCard): verdict card → headline compressed to ≤12w: 'φᵢ = average marginal contribution over all orderi'
  A3M2 (SlateCard): verdict card → headline compressed to ≤12w: 'Efficiency · Symmetry · Dummy · Additivity → one u'
  A3R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A3V (SlateCard): verdict card → headline compressed to ≤12w: 'A real number that says nothing about the world'
  A4M (SlateCard): verdict card → headline compressed to ≤12w: 'A local line — random, and only local'
  A4R (ChipGrid): chip grid (structured display, individual chips were already ≤12w)
  A4M2 (SlateCard): verdict card → headline compressed to ≤12w: 'What the model would do — not what should happen'
  A5C (SlateCard): verdict card → headline compressed to ≤12w: 'Three Words That Aren't Synonyms'
  A5R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A5V (SlateCard): verdict card → headline compressed to ≤12w: 'A reason the developer reads ≠ a reason the person'
  A5R2 (DeckPattern): deck note → compressed to ≤12w: 'the contract demands 'explainability' and means 'i'
  A6R (DeckPattern): deck note → compressed to ≤12w: ''
  A6V1 (SlateCard): verdict card → headline compressed to ≤12w: ''The secret has been deleted.''
  A6V2 (SlateCard): verdict card → headline compressed to ≤12w: 'Locally true — every command succeeded'
  A6V3 (SlateCard): verdict card → headline compressed to ≤12w: 'Globally false — the data persists on the provider'
  A6R2 (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A7C (SlateCard): verdict card → headline compressed to ≤12w: 'What Honesty Looks Like'
  A7M (SlateCard): verdict card → headline compressed to ≤12w: 'Discovery vs justification — dressed as each other'
  A7V (SlateCard): verdict card → headline compressed to ≤12w: 'Knowing how to defend it is not understanding it'
  A7R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
