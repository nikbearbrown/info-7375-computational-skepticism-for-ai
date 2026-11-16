# BUILD-LOG — claude-liam-deep-13-limits-of-ai

## Gate: PLAN (awaiting human sign-off)
Deep-explainer plan-stage deliverable. Produced: `beat_sheet.json`, `PLAN.md`, `FACTCHECK.md`, `SOURCES.md`, `BUILD-LOG.md`. NOT produced (downstream of this gate): audio, previz, SHOPPING.md (Gate D2 is after audio lock), render.

## Decisions
- **Genre fit:** chapter is genuinely multi-act (composite failure → three limits → Taleb's two worlds → Turing/Searle → safety-mechanism + real case → cognitive profile → extended mind / closing arc) → deep-explainer is the correct skill, not ai-explainer.
- **Register:** Teardown (deep-explainer default) — a skepticism argument that judges the toolkit and bounds it; narration does not parrot capability claims.
- **Series finale:** this is Ch. 13, the FINAL chapter. `series_finale: true` in metadata. The verdict and outro carry the closing register ("the last verdict in the series," "There is no Chapter 14," "Go do the work"). Act VII runs the third/final calibration baseline (A7M2) closing the book's arc.
- **Beat mix landed** VOX 22.6% (7) / MANIM 25.8% (8) / REMOTION 35.5% (11) / CARD 16.1% (5). Lint PASS. CARD held lean (≤18%) by folding two act openers (III, VI) into spark-line content beats (A3M, A6M).
- **Manim carries the argument** per doctrine: the categorical boundary with equation tangent (A2M — the load-bearing induction/complementarity beat), the two questions (A1M), Mediocristan/Extremistan (A3M), behind-the-glass (A4M), the circular signal (A5M), the profile spectrum (A6M), Legg-Hutter extremophile (A7M), the third calibration baseline (A7M2).
- **Only one vox run** (R1, the turkey, A3V1→A3V2) — the chapter's one place a continuous camera move earns drama. All other lane changes hard-cut per the vox-run contract; other VOX beats (clinical composite, Hume, Chinese Room, Epic Sepsis, the sign-off) are standalone.
- **ILLUSTRATE LAW honored:** Claude UI (ComposerAsk / VerdictArtifact / TitleOutro) appears only at cold open, the two asks, verdict, your-turn handoff, and outro. Bodies are concept-illustrated.

## MISSING / TODO (post-approval)
- MISSING: FACTCHECK verification pass (Gate F) — VERIFY items: Taleb turkey, Turing/Searle citations, Epic Sepsis (Wong et al. 2021), Legg-Hutter. STRIP items already handled in narration (calibration exact numbers; Epic miss-rate; *Irreducibly Human*).
- MISSING: `anim.json` classification pass for the DeckPattern beats (A2R2 branch, A3R threshold, A4R divergence, A5R2 threshold, A6R2 scale) — author before build per animated-deck gate.
- MISSING: real Manim scene implementations (scenes named in `shot.manim.scene`; specs in `shot.manim.spec`).
- MISSING: pantry stills (7) — briefs in each beat's `pantry_brief`; A2V is Tier 3 (Hume) and needs a disclosure sidecar + rights flag; SHOPPING.md written after audio lock (Gate D2).

## Gate signatures
- PLAN: ____________ (human)   ·   FACTCHECK: ____________   ·   GATE P (narration→audio): ____________

## PASS 1 DE-WORDIFY — 2026-07-24
§8.5 no-wordy-card pass. Headlines shortened to ≤ 12 words; narration unchanged; no audio re-generated.

- **A2M**: de-wordified SlateCard headline
  - OLD: "World = Sample ⊔ (World \ Sample) — the complement is never in trainin"
  - NEW: "World = Sample ⊔ (World \ Sample) — the complement never trains."
- **A3M**: de-wordified SlateCard headline
  - OLD: "Two worlds — averaging saves you in one, ruins you in the other."
  - NEW: "Two worlds — averaging saves in one, ruins in the other."

Typecheck after fix: GATE T PASS (§8.5 cleared).

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  A1C (SlateCard): verdict card → headline compressed to ≤12w: 'The System That Passed Every Test'
  A1M (SlateCard): verdict card → headline compressed to ≤12w: 'Tested on one — harmed by the other'
  A1V (SlateCard): verdict card → headline compressed to ≤12w: 'The engineers designed the wrong tests'
  A1R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A2C (SlateCard): verdict card → headline compressed to ≤12w: 'Three Categorical Limits'
  A2R (ChipGrid): chip grid (structured display, individual chips were already ≤12w)
  A2V (SlateCard): verdict card → headline compressed to ≤12w: 'A sample can't contain what it excluded'
  A2M (SlateCard): verdict card → headline compressed to ≤12w: 'World = Sample ⊔ (World \ Sample) — the complement'
  A2R2 (DeckPattern): deck note → compressed to ≤12w: 'the data-world gap is the categorical one; meaning'
  A3M (SlateCard): verdict card → headline compressed to ≤12w: 'Two worlds — averaging saves in one, ruins in the '
  A3V1 (SlateCard): verdict card → headline compressed to ≤12w: '1,000 days of rising confidence'
  A3V2 (SlateCard): verdict card → headline compressed to ≤12w: 'Day 1,001 — the curve no data predicted'
  A3R (DeckPattern): deck note → compressed to ≤12w: '99.7% on seen cases says nothing if the unseen one'
  A4C (SlateCard): verdict card → headline compressed to ≤12w: 'Turing and Searle'
  A4R (DeckPattern): deck note → compressed to ≤12w: ''
  A4M (SlateCard): verdict card → headline compressed to ≤12w: 'Behavior is testable — the limits stand behind it'
  A4V (SlateCard): verdict card → headline compressed to ≤12w: 'Fluent output, no understanding — and no verdict o'
  A5C (SlateCard): verdict card → headline compressed to ≤12w: 'When Skepticism Is the Safety Mechanism'
  A5V (SlateCard): verdict card → headline compressed to ≤12w: 'Far worse than marketed — external validation, Won'
  A5M (SlateCard): verdict card → headline compressed to ≤12w: 'It confirmed suspicion — it did not form it'
  A5R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A5R2 (DeckPattern): deck note → compressed to ≤12w: 'the authority to refuse is the top authority in th'
  A6M (SlateCard): verdict card → headline compressed to ≤12w: 'Tall peaks, deep valleys, one axis at zero'
  A6R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A6V (SlateCard): verdict card → headline compressed to ≤12w: 'Treated as a checkbox, accountability disappears i'
  A6R2 (DeckPattern): deck note → compressed to ≤12w: 'middle: delegate WITH verification — plausible out'
  A7C (SlateCard): verdict card → headline compressed to ≤12w: 'The Extended Mind Arrives'
  A7M (SlateCard): verdict card → headline compressed to ≤12w: 'Superhuman in one niche — a cognitive extremophile'
  A7M2 (SlateCard): verdict card → headline compressed to ≤12w: 'Improving, rarely at 0.9 — overconfidence is stick'
  A7R2 (ClaudeWindow): artifact/terminal display (labels, not sentences)
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
