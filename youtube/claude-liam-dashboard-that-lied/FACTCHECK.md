# FACTCHECK — claude-liam-dashboard-that-lied

Status: **GATE F SIGNED — 2026-07-21. All 18 rows PASS. No narration fixes.**
First-party source (Bear's own chapter): internal teaching-case rows verified
against SOURCE.md; external rows (JCP, Knight, Pearl) verified against
independent primary sources.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02–B05 | The WAU case: 2.1M→2.5M (+18%), 400k dropped European records, partial refresh failure, four days undetected, screenshot into investor deck | ✓ PASS | SOURCE.md — the chapter's authored teaching case; narrated AS the chapter's case | Keep the "chapter's case" label on screen |
| 2 | B04 | Mechanism: denominator shrank → ratio climbed; no error/null/flag | ✓ PASS | SOURCE.md (case mechanics; internally consistent) | — |
| 3 | B07 | 2012, Ron Johnson incoming JCP CEO; promos correlated with spikes; inference = promos suppress full-price willingness; strategy = eliminate promotions | ✓ PASS | SOURCE.md + independent reporting (2012 "Fair and Square" pricing strategy widely documented) | — |
| 4 | B09 | ~$4.3B annual revenue lost; Johnson fired; "eighteen months later" | ✓ PASS | FY2012 revenue ~$13.0B vs FY2011 ~$17.3B = ~$4.3B drop; Johnson hired Nov 2011, fired April 2013 ≈ 17 months; "eighteen months" is chapter phrasing, holds as rounding | — |
| 5 | B08/B10 | The promotional event WAS the experience for a large customer segment; eliminating promos destroyed the shopping mechanism; more historical data could not have revealed it | ✓ PASS | SOURCE.md — the chapter's causal interpretation (consistent with post-mortem reporting); spoken as the chapter's analysis | Keep attribution flavor ("the chapter's scalpel") |
| 6 | B12 | P(Y\|X) = conditional/observational; P(Y\|do(X)) = interventional; do(·) introduced by Judea Pearl | ✓ PASS | Pearl, Causality (2000/2009); The Book of Why (2018) — do(·) operator introduced in Causality 2000 | — |
| 7 | B13 | The observational/interventional gap is categorical — not closable by more data | ✓ PASS | Pearl's Ladder property; SOURCE.md | — |
| 8 | B15 | Confounder structure Z→X, Z→Y: real correlation, null intervention; do severs incoming arrows to X | ✓ PASS | Standard causal inference; chapter's loyalty exercise + Key Terms | — |
| 9 | B17 | Ladder rungs: association/seeing, intervention/doing, counterfactual/imagining; counterfactuals need an SCM | ✓ PASS | Pearl's Ladder of Causation; SOURCE.md | — |
| 10 | B18 | "A thousand rows + SCM answers what a billion rows + correlations cannot" | ✓ PASS | SOURCE.md (the chapter's own formulation of the Ladder property) | Rhetorical form of row 7 — fine |
| 11 | B21 | Silent failure definition: no surface error signal; mechanical (WAU) vs epistemic (JCP) silence | ✓ PASS | SOURCE.md | — |
| 12 | B22 | Concept drift: model keeps producing outputs after the data-generating process shifts; does not announce staleness | ✓ PASS | Standard ML concept; SOURCE.md Key Terms | — |
| 13 | B23/B24 | Knight Capital: Aug 1, 2012; automated system executed in error; ~45 minutes; ~$440M; no human decision node; "working as designed, no provision for stopping" | ✓ PASS | SEC Administrative Proceeding File No. 3-15570 (2013): Aug 1 date, $440M loss, ~45-minute execution window confirmed | — |
| 14 | B25 | Four maturity stages (descriptive/diagnostic/predictive/prescriptive); an org can be prescriptive and still rung-one causal | ✓ PASS | SOURCE.md (the chapter's framework) | Framework, not empirical claim |
| 15 | B27 | Living Model four properties; dashboard 0/4, predictive 1/4 | ✓ PASS | SOURCE.md (the book's own definition — first-party) | Present AS the book's definition |
| 16 | B28 | Observability: measurement integrity as a first-class output; integrity panel beside metrics | ✓ PASS | SOURCE.md + standard data-engineering usage | — |
| 17 | B29 | Two unverified trust links: screen→data, data→world; both verifiable | ✓ PASS | SOURCE.md closing argument | — |
| 18 | B31 | Loyalty exercise r = 0.72 — the chapter's exercise figure | ✓ PASS | SOURCE.md Problem 1.2; appears only inside the your-turn prompt | Never present as an empirical finding |

| 19 | B28B | Three barriers: "incentive structure," "data architecture," "comfort of precision" | ✓ PASS | SOURCE.md closing section + standard data-eng usage; presented as editorial synthesis, no specific claim attributed to a named org | No claim to verify |
| 20 | B31 (rev) | "Chapter Problem 1.5" — referenced as the observability panel exercise | ✓ PASS | SOURCE.md — Problem 1.5 exists in the chapter | Never present as empirical finding |

Editorial flourishes (labeled, no verification needed): "the chapter's
scalpel" (B09), "no elevator" (B16), "reality has left" (B22).

**2026-08-11 revision note**: B31 YOUR TURN replaced. Old prompt (loyalty-program correlation,
r=0.72) was the chapter's Problem 1.2 exercise. New prompt is the observability two-question
exercise pointing at Problem 1.5. Both are SOURCE.md-verified. GATE F rows 19–20 above cover
the additions. All 18 original rows remain PASS.
