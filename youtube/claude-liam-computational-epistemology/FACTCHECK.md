# FACTCHECK — claude-liam-computational-epistemology

Status: **Gate F CLOSED — 2026-07-21. All 20 rows verified; no narration changes; no audio regeneration needed.**

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B06 | Classical definition of knowledge = justified true belief; "for two thousand years, that held" | ✓ | Standard tripartite analysis; lineage to Plato's Theaetetus is a common gloss and contested in detail | — |
| 2 | B07 | Edmund Gettier, 1963, three pages, counterexamples to JTB | ✓ | Gettier, "Is Justified True Belief Knowledge?", Analysis 23(6), 1963 — famously ~3 pages | — |
| 3 | B08 | A hallucinated citation with a coincidentally-correct number is a Gettier case; the same process fails silently later | ✓ | Source doc Part 1 (mechanism claim, not empirical stat) | — |
| 4 | B10/B11 | Truth check and entailment check are separable; high-truth/low-entailment is invisible to a truth-only checker; G_r = T·(1−S_NLI) | ✓ | Source doc Part 1; formula reproduced verbatim | — |
| 5 | B16 | Models' stated reasoning often diverges from actual computation (confabulation), per interpretability research | ✓ | Source doc Part 2; kept soft/unquantified | Keep hedged phrasing |
| 6 | B17 | Calibration = bucket stated confidence vs empirical accuracy; 90-says/60-lands is ILLUSTRATIVE | ✓ | ECE definition, source Part 2; pair labeled illustrative on screen | Never present 90/60 as measured |
| 7 | B18 | Under 10 trials → insufficient track record (in the shown code) | ✓ | Source doc's own code; it's a design choice, shown as code not law | — |
| 8 | B20 | Regress problem; foundationalism vs coherentism as the two classical exits | ✓ | Standard epistemology; source Part 3 | — |
| 9 | B21 | RAG is foundationalist in structure; its known failure is a wrong/mismatched source that still cites | ✓ | Source doc Part 3 | — |
| 10 | B22 | A coherent structure of falsehoods is possible (conspiracy-wall case) | ✓ | Classical objection to pure coherentism; source Part 3 | — |
| 11 | B23 | Naive multi-model voting assumes error independence (Condorcet); shared training lineage breaks it | ✓ | Source doc Part 3; mechanism, no stats | — |
| 12 | B25 | Shared lineage modeled as a latent common cause; ignoring it inflates confidence exactly when sources are least independent | ✓ | Source doc Part 3 formalism | — |
| 13 | B27 | Descartes, deceiving demon, Meditations (1641); "four centuries" | ✓ | Meditations on First Philosophy, 1641 | — |
| 14 | B29 | Hume, problem of induction, Enquiry (1748); track records degrade under distribution shift as the same structure | ✓ | Source doc Part 4; Enquiry Concerning Human Understanding | — |
| 15 | B30 | "Mitigated skepticism" is Hume's own move; binary fake-detection framed as an unwinnable arms race | ✓ | Hume's term (Enquiry §XII); arms-race framing is the source's design claim — spoken as stance, not theorem | Keep as editorial stance |
| 16 | B31 | Provenance cap r(o)=min(provenance, content), presented as a hard cap | ✓ | Source doc Part 4 | — |
| 17 | B33 | Degrees of belief + Bayes-rule updating; ML calibration IS Bayesian epistemology under another department | ✓ | Source doc Part 5; the identity claim is editorial — spoken with attitude, defensible | — |
| 18 | B34 | Sequential updates preserve differential check reliability; majority vote discards it | ✓ | Source doc Part 5 | — |
| 19 | B35 | Surprise S(o) = −log₂P(o); high surprise should trigger downstream re-check | ✓ | Source doc Part 5; standard information-theoretic surprisal | — |
| 20 | B36 | Threshold from cost asymmetry; abstention as a designed outcome | ✓ | Source doc Part 5 | — |

Editorial flourishes (labeled as such, no verification needed): "luck wearing
its costume" (B08), "one witness talking to itself three times" (B23 — the
source's own phrase, adapted), "the demon shipped" (B28), "the math of paying
attention" (B35).

## Gate F verdict — 2026-07-21
All 20 rows verified. Zero narration edits required. Gate F CLOSED. Ready for pass-1 render.
