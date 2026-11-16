# FACTCHECK — tldr-robust-against-what

Status: **GATE F verified 2026-09-23 by Claude (Opus 5.5) against the chapter as written. Every number on screen is the chapter's own; `make_sheet.py` and `scenes.py` assert them at import. Human sign-off pending.**

Source: `chapters/04-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md` (HEAD side of every merge-conflict block), §"Distribution shift, returning from Chapter 2" (Figure 4.5) and §"Towards honest robustness disclosure" (Sections 1–3 template); exercise 6. Section S4 of `youtube/tldr-sections-04-robustness.md`.

**The three rows are the chapter's TEMPLATE values** — a disclosure form printed with blanks, not a measured model. The film says "template" in B00, B12 and B16 and keeps a small dim caption "template values — illustrative" on the LEARN stage from B11 on.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B01 | Course credit: chapter four of INFO 7375, Computational Skepticism for AI, Northeastern | ✓ PASS | course-film convention (spoken + on the cards' course line) | — |
| 2 | B00, B02, B10 | A vendor says "94% accurate and robust"; the question is "robust against what?" | ✓ PASS | Chapter opener (HEAD): "someone hands you this same classifier with a benchmark score of 94% and calls it robust … which 94% — robust against what, measured how, at what perturbation budget"; §Distribution shift: "your first question should be 'robust against what?'" | — |
| 3 | B00, B14, B18, BVDT | "Robustness is a profile, not a number" | ✓ PASS | §Distribution shift: "*robustness is not a single number*. It is a profile." | — |
| 4 | B11, B19 | Row 1: L∞ white-box (FGSM/PGD), ε = 0.03, clean 94%, robust 71% | ✓ PASS (template) | Section 1 table, row 1 | captioned illustrative |
| 5 | B11 | White-box = attacker holds the weights (and gradients) | ✓ PASS | Taxonomy table: "Full access to model weights and gradients" | — |
| 6 | B03, B11 | L∞ budget: no single coordinate moves more than ε (B03 card: "no pixel shifts past it"; ε spoken, shown in B11) | ✓ PASS | §Linearity hypothesis: "no single coordinate of δ can exceed ε" | — |
| 7 | B12, B19 | Row 2: transfer attack, surrogate model trained on the same data, clean 94%, robust 58% | ✓ PASS (template) | Section 1 table, row 2 ("Surrogate: ResNet-50 … Surrogate trained on same data"). The architecture name is left off screen (no model names). **Manuscript note:** this row's "budget" cell names a surrogate, not an ε, so 58 and 71 are not at a comparable budget; the film does not compare them ("nothing in row one told you row two"), and does not claim a transfer attack is stronger than white-box | reported to Bear |
| 8 | B12 | A transfer attack builds the perturbation on a stand-in and aims it at the target; the attacker needs no access to the target | ✓ PASS | Taxonomy: "A surrogate model; no access to the target"; "The attacker does not need access to your model" | — |
| 9 | B14, B16, B19 | Row 3: natural distribution shift, time-shift only, clean 94%, robust 87% | ✓ PASS (template) | Section 1 table, row 3 ("Domain: Q4 2023 vs Q1 2024 … Time-shift only"); the quarter labels are left off screen (nothing datable) → "time shift only" | — |
| 10 | B16, BVDT | Adversarial robustness and shift robustness do not guarantee each other; the rows do not predict each other | ✓ PASS | Figure 4.5 caption (HEAD): "Neither robustness against adversarial attack nor robustness against distribution shift guarantees robustness against the other"; text: "somewhat, but not as much as you'd like". Spoken as "does not guarantee", not "tells you nothing" | softened from the prior draft's "told you nothing" |
| 11 | B13 | A general "robust" is "decoration on the marketing page … the fluency trap wearing a lab coat" | ✓ PASS (paraphrase) | §Distribution shift, verbatim phrase | — |
| 12 | B16, B18, BVDT | The disclosure has three sections: robustness profile, residual risk, monitoring specification (trigger for human review / rollback) | ✓ PASS | §Towards honest robustness disclosure, the three bolded components and the Section 2/3 blanks | — |
| 13 | B18, BVDT | "A claim without this structure is not a claim." | ✓ PASS | Closing italic line of the template | — |
| 14 | B17, BVDT | A robust accuracy is a value AT a budget; at a new budget the number must be re-measured | ✓ PASS (derivation) | The template's column is "Robust accuracy at budget"; the profile names "the adversarially robust accuracy … at each budget". The film shows ε = 0.06 as a hypothetical with **no value** ("?") — no number is invented. 2 × 0.03 = 0.06 asserted | — |
| 15 | B19 | Boundary: what each defense buys and costs is not taught here | ✓ PASS | The six-row toolkit table is its own section (sections file: not sectioned) | — |
| 16 | BHTF | The YOUR TURN exercise (facial recognition, physical access control, five questions) | ✓ PASS | Exercise 6, adapted with three required question types drawn from Sections 1–3 | — |
| 17 | B01 | "Every model card and vendor deck you read says robust" | ✓ PASS (hedged) | Viewer's experience, not a claim about a named product; chapter: "a robustness claim in a model card or deployment approval document is not a number" | — |
| 18 | all | Nothing datable on screen: no model names, versions, quarters, "as of" claims | ✓ PASS | Sweep of the sheet: ResNet-50 and "Q4 2023 vs Q1 2024" deliberately omitted | — |

Deferred (density rule): the six-row toolkit table and its costs (boundary); certified radii (S5); the Bartoldson plateau (S6); the NIST AI RMF citation (true to the chapter, but a citation, not a picture). Not used: every `[verify]` flag in the chapter (none touches this card).
