# FACTCHECK — tldr-hold-one-fair

Status: **GATE F verified 2026-09-23 by Claude (Opus 5.5): every number recomputed from the chapter's own inputs (base rates, TPR, FPR) in Python this session; `make_sheet.py` and `scenes.py` assert every value at import. Human sign-off pending.**

Source: `chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md`, §"Three definitions" and §"The arithmetic — the actual proof, not a gesture" (the Bayes/odds derivation and both numeric tables). HEAD side of every merge-conflict block; the film uses nothing that exists only on the `d78899b` side. Exercise 6 seeds BHTF. Section S1 of `youtube/tldr-sections-07-fairness-metrics.md`.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B01 | Course credit: chapter seven of INFO 7375, Computational Skepticism for AI, Northeastern | ✓ PASS | course-film convention (spoken + on the cards' course line) | — |
| 2 | B00, B02, BVDT | When base rates differ, calibration (equal PPV) and equalized odds (equal TPR and FPR) cannot both hold, except with perfect prediction | ✓ PASS | Chapter: "The only escapes are p_a = p_b (equal base rates) or perfect prediction (t = 1, f = 0)"; Chouldechova 2017 / KMR 2017 as cited by the chapter | — |
| 3 | B10 | Group A base rate 60%, group B base rate 30% | ✓ PASS | Chapter: "p_a = 0.6 in group a and p_b = 0.3 in group b" | — |
| 4 | B10, B03 | Calibration, for a yes/no flag, means equal PPV across groups; equalized odds means equal TPR and FPR | ✓ PASS | Chapter: calibration "for a binary score, forces equal PPV across groups"; equalized-odds equations (Hardt, Price, Srebro 2016) | — |
| 5 | B10 | The numbers are the chapter's constructed ("Suppose …") values, captioned on screen "the chapter's constructed numbers" | ✓ PASS | Chapter: "Suppose the underlying base rate …"; the two tables are illustrative | — |
| 6 | B11 | Group A at TPR 0.60, FPR 0.30: flagged pile 0.36 : 0.12 = 3 : 1, PPV 0.75 | ✓ PASS | 0.6·0.60 = 0.36; 0.4·0.30 = 0.12; 0.36/0.48 = 0.75; chapter's calibration table, group A | — |
| 7 | B12 | Group B at A's rates (0.60, 0.30): pile 0.18 : 0.21, PPV 0.46 | ✓ PASS (derived) | Not a chapter row: computed from the chapter's inputs p_b = 0.3 with group A's TPR/FPR. 0.3·0.60 = 0.18; 0.7·0.30 = 0.21; 0.18/0.39 = 0.4615 → 0.46; asserted | — |
| 8 | B13, B19 | TPR 0.70 and FPR 0.15 in both groups gives PPV 0.88 (A) and 0.67 (B) | ✓ PASS | Chapter's equalized-odds table. 0.42/0.48 = 0.875 → 0.88; 0.21/0.315 = 0.667 → 0.67 | — |
| 9 | B13 | 0.70 / 0.15 is a "better model" than 0.60 / 0.30 (more hits, fewer false alarms) | ✓ PASS (framing) | Arithmetic: 0.70 > 0.60 and 0.15 < 0.30. The chapter presents this table as a threshold choice, not a better model; the film frames it as the natural "tune harder" fix and does not claim the chapter says so. See manuscript note in BUILD-LOG | — |
| 10 | B13 | Pile odds 0.42 : 0.06 = 7 : 1 and 0.21 : 0.105 = 2 : 1 | ✓ PASS | 0.6·0.7, 0.4·0.15; 0.3·0.7, 0.7·0.15; asserted | — |
| 11 | B14, B17, B18 | Pile odds = base-rate odds × TPR/FPR, i.e. v/(1−v) = p/(1−p) · t/f | ✓ PASS | Chapter's odds identity, derived from its Bayes line v = pt/(pt + (1−p)f); asserted for all five configurations | — |
| 12 | B14 | Base-rate odds 1.5 (A) and 0.43 (B); TPR/FPR 4.67 in both; 7 = 1.5 × 4.67, 2 = 0.43 × 4.67 | ✓ PASS | 0.6/0.4 = 1.5; 0.3/0.7 = 3/7 = 0.4286; 0.70/0.15 = 14/3 = 4.667; 1.5·14/3 = 7; (3/7)·(14/3) = 2 | — |
| 13 | B15, B16 | Holding PPV at 0.75 requires B's FPR to go DOWN (0.15 → 0.10) while A's rises to 0.30 and A's TPR falls to 0.60 | ✓ PASS | Chapter's calibration table: A 0.60/0.30, B 0.70/0.10; the move from the equalized-odds table to it is the film's animation between the chapter's two rows | — |
| 14 | B16, B18 | Pinned: both piles 3 : 1; TPR/FPR must be 2 (A) and 7 (B) | ✓ PASS | 1.5·2 = 3; (3/7)·7 = 3; chapter's cross-group coefficient p_b(1−p_a)/(p_a(1−p_b)) = 2/7 and 2 = (2/7)·7 | — |
| 15 | B17 | The only exits: equal base rates, or no false alarms | ✓ PASS | Chapter (row 2). Spoken "no false alarms at all"; the chapter says perfect prediction (t = 1, f = 0) — f = 0 is the part that lets PPV = 1 in both groups | — |
| 16 | B18 | (3/7)·7 = 3 ⇒ v = 0.75; 1.5·2 = 3 ⇒ v = 0.75 | ✓ PASS | odds 3 ⇒ v = 3/4 | — |
| 17 | B19, BVDT | Yes-rates (positive-prediction rates) 0.48 vs 0.28 and 0.48 vs 0.32: equal yes-rates fails in both tables | ✓ PASS | Chapter tables; 0.36 + 0.12 = 0.48; 0.21 + 0.07 = 0.28; 0.42 + 0.06 = 0.48; 0.21 + 0.105 = 0.315 → 0.32 (the chapter's half-up rounding) | — |
| 18 | B19, BVDT, B01 | Which test gives is a values claim someone has to sign, not a technical question | ✓ PASS (paraphrase) | Chapter: "which one gives is not a technical question. It is a claim about which error you are less willing to make"; "Someone always decides" | — |
| 19 | B19 | "Not taught here: the three-way proof" (KMR: calibration + balance for positives + balance for negatives) | ✓ PASS | Chapter names the KMR three-way version without proving it; the film names it as its boundary | — |
| 20 | BHTF | Exercise transfer: base rates 40% and 20%; the odds identity as the check | ✓ PASS | Chapter Exercise 6 (40% population X, 20% population Y); base-rate odds 2/3 and 1/4 asserted | — |
| 21 | B01 | Loan models, hiring screens and risk scores face fairness audits | ✓ PASS | Chapter opening: "a loan approval tool, a recidivism predictor, a hiring screen" | — |
| 22 | all | Nothing datable on screen: no model names, product names, versions, or "as of"; no COMPAS framing (that is chapter 6's AUDIT-side film) | ✓ PASS | Sweep of the sheet and scenes | — |

Left out on purpose: the COMPAS case and its numbers (the parallel chapter-6 film owns the audit side); the chapter's thresholds (0.5 / 0.6) because the two tables' threshold labels do not reconcile (BUILD-LOG, manuscript notes); demographic parity is shown failing in both tables, not proved incompatible in general.
