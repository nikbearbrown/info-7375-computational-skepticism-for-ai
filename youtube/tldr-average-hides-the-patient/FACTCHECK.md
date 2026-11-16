# FACTCHECK — tldr-average-hides-the-patient

Status: **GATE F verified 2026-09-23 by Claude (Opus 5.5). Every number is copied from the chapter or recomputed from the chapter's own inputs, and `make_sheet.py` and `scenes.py` assert it at import. Human sign-off pending.**

Source: `chapters/11-communicating-uncertainty-calibrating-claims-to-evidence.md`. The film uses §"Subgroup calibration: where aggregate metrics lie" (the subgroup table, the ECE_g formula, Wong et al. 2021), §"Expected Calibration Error", §"What calibration metrics cannot see" (row 1), "Still puzzling" and exercise A5. All of this material is outside the chapter's merge-conflict blocks. Section S2 of `youtube/tldr-sections-11-communicating-uncertainty.md`.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Course credit: chapter eleven of INFO 7375, Computational Skepticism for AI, Northeastern | ✓ PASS | course-film convention (spoken, and on the cards' course line) | — |
| 2 | B00, B10, B19, BVDT | Global calibration error 0.018 on 12,955 patients | ✓ PASS | chapter table, "Global (aggregate)" row: N 12,955, subgroup-ECE column 0.018 | — |
| 3 | B00, B10, B12, B16, B19, BVDT | Rare-disease cases: 95 patients, ECE 0.103 | ✓ PASS | chapter table, "Rare-disease cases" row | — |
| 4 | B11 | Adults 18–64 at 0.019; children 0–17 at 0.029 | ✓ PASS | chapter table rows (N 8,420 and 1,210) | — |
| 5 | B12 | 65 and over at 0.044; pregnancy-related at 0.071 | ✓ PASS | chapter table rows (N 2,850 and 380) | — |
| 6 | B10, B14, B15, BVDT | The five rows sum to the global N (95 of 12,955) | ✓ PASS | 8,420 + 1,210 + 2,850 + 380 + 95 = 12,955; asserted | — |
| 7 | B10, B16 | 0.103 is "almost six times" the global | ✓ PASS | 0.103 / 0.018 = 5.72; asserted | — |
| 8 | B12, B17, B19, BVDT | The chapter's flag: a subgroup ECE above twice the global | ✓ PASS | table header "Flag (Y if subgroup ECE > 2× global)" | — |
| 9 | B12, B19 | Three of the five rows are above twice the global (0.036) | CORRECTED | 0.044, 0.071 and 0.103 exceed 0.036. 0.019 and 0.029 do not. The chapter's table marks **pediatric (0.029) Y**, which contradicts its own rule; the sections card inherited "four of five". The film applies the stated rule (3 of 5), and the discrepancy is logged for Bear in BUILD-LOG. | film says three |
| 10 | B13 | The unweighted average of the five rows is 0.053, three times the global | ✓ PASS | (0.019+0.029+0.044+0.071+0.103)/5 = 0.0532; 0.0532/0.018 = 2.96; asserted | — |
| 11 | B14 | The global counts patients: each row weighs by its share of N | ✓ PASS | ECE = Σ_m (\|B_m\|/N)·gap: every patient carries weight 1/N, so a row's total weight is N_g/N (chapter's ECE formula) | — |
| 12 | B14 | Adults are about two thirds of the axis; the rare row is under one percent | ✓ PASS | 8,420/12,955 = 0.650; 95/12,955 = 0.0073; asserted | — |
| 13 | B14 | A row's "voice" in the global (share × gap): adults 0.012, rare row 0.0008 | ✓ PASS (derived) | 0.650 × 0.019 = 0.0123; 0.00733 × 0.103 = 0.00076; asserted. Our derivation from the chapter's inputs, not a chapter number | — |
| 14 | B15, B16, BVDT | No error on the rare row, even the worst, can move the global by one hundredth | ✓ PASS (derived) | With the same bins, the pooled bin gap is \|Σ_g n_gm·d_gm\|/n_m, so a change in one group's gaps moves pooled ECE by at most (N_g/N)·max\|Δd\| (triangle inequality). Every gap is ≤ 1, so the most is 95/12,955 = 0.0073 < 0.01. From a perfectly calibrated row to 0.103 the most is 0.00076. Asserted | — |
| 15 | B16 | Spread over everyone, the rare row's error is a film 0.0008 thick; at error 1 it is 0.0073 | ✓ PASS (derived) | row 14 | — |
| 16 | B16, B17, B18 | Divided by its own 95, the row's error is 0.103 | ✓ PASS | ECE_g divides by N_g (chapter's ECE_g formula); the table gives 0.103 | — |
| 17 | B17, B18 | ECE_g = Σ_m (\|B_m^g\|/N_g)·\|acc(B_m^g) − conf(B_m^g)\| | ✓ PASS | chapter's displayed equation (the film writes Σ_m for Σ_{m=1}^{M}) | — |
| 18 | B17, BVDT | Report the global ECE and the full distribution {ECE_g} | ✓ PASS | chapter: "report both the global ECE and the full distribution of {ECE_g}" | — |
| 19 | B18 | In the global, the rare row's 95 patients carry weight 0.0073; in ECE_g, all of it (95/95 = 1) | ✓ PASS (derived) | 95/12,955 = 0.00733; Σ_m \|B_m^g\|/N_g = 1 | — |
| 20 | B18 | The pooled number can sit below the rows' patient-weighted average (0.028): over- and under-confident groups in a shared bin cancel | ✓ PASS (derived) | Patient-weighted mean Σ(N_g/N)·ECE_g = 0.0276. Pooled ≤ that bound by the triangle inequality (same bins); 0.018 < 0.028 is consistent. The chapter does not state its binning; the film says "can", not "does" | — |
| 21 | B03 | ECE is the weighted average gap between stated confidence and outcome, over bins | ✓ PASS | chapter: "the weighted average gap between mean predicted confidence and mean actual accuracy in each bin" | — |
| 22 | B01, B03 | Calibration: "80%" should be right about 80% of the time | ✓ PASS | chapter: "when the model says it is 80% confident, is it actually right about 80% of the time?" | — |
| 23 | B01 | A widely used sepsis alert looked fine in aggregate; an outside check at one hospital found it missed two thirds (67%) of sepsis cases | ✓ PASS | chapter, citing Wong et al. (2021): "aggregate performance that looked acceptable"; missed 1,709 of 2,552 septic patients = 67.0% (Michigan Medicine). "Widely used" is the chapter's "deployed across hundreds of hospitals". The product is not named on screen (nothing datable) | — |
| 24 | B01 | The sepsis case is not presented as the source of the subgroup table | ✓ PASS | The film never links the two. The table cites no dataset, and B10 captions it "the chapter's illustrative table" | — |
| 25 | B19 | What ratio should halt a deployment is a values question the chapter leaves open | ✓ PASS | "Still puzzling": "That threshold is a values question, and I do not yet have a principled way to teach it." | — |
| 26 | B19 | A model calibrated on the wrong label passes every check in the film | ✓ PASS | §"What calibration metrics cannot see": the construct-validity row ("ECE / MCE assume the label is the construct") | — |
| 27 | BHTF | A5's profile: global 0.035 (10 bins); 0.030 / 0.092 / 0.141 at 80% / 15% / 5% | ✓ PASS | exercise A5. The 80% primary share is the remainder (100 − 15 − 5); the chapter does not print it | — |
| 28 | BHTF | (expected answers, not shown) patient-weighted average 0.045 ≥ 0.035; flags 0.092 and 0.141; the tertiary group can move the global by up to 0.05, and by at most 0.007 at 0.141 | EXEMPT | the viewer's exercise; asserted in make_sheet.py for our own check | — |
| 29 | all | Nothing datable on screen: no model names, versions, product names or "as of" | ✓ PASS | sheet sweep | — |

## Kept out on purpose
- **Global base rate.** The table prints 0.041, but the N-weighted rows give 571.4 / 12,955 = 0.0441. The film shows no base rate.
- **The ECE rules of thumb** (0.02–0.05 "well-calibrated", > 0.10 "systematic"). They carry the chapter's own `[verify]`, so they are not in the film.
- **"Overconfidence is the dominant failure mode … extended to LLMs".** This also carries the chapter's `[verify]`, so it is not in the film.
- **The MCE column** (0.176 on the rare row). It is left out under the density rule. For the record: global MCE 0.039 ≤ the largest subgroup bin gap, which is consistent.
- **The Epic model's AUC 0.63 vs 0.76–0.83 and PPV 12%.** These are true per the chapter but are discrimination metrics, not calibration, so they would be a detour.
