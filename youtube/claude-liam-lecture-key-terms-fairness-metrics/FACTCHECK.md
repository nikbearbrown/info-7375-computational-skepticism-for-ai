# FACTCHECK - Key Terms: Fairness Metrics

Status: 2026-11-12, checked by Claude. Figures: every spoken figure machine-checked against the words on the slide at that step. Explanations: an independent second pass compared every beat with its slide and the chapter; no beat needed rewording. No human sign-off.

The film teaches from the deck; the deck's numbers are computed in the page or labelled illustrative or simulated on the slide itself (the badge at top right). This file checks that the narration says only what the slide and the chapter support.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | BOPEN | Playlist name, film title, what the film covers | PASS | Playlist as Bear named it 2026-11-11; summary restates the deck's map slide | none |
| 2 | BDEFS | What each tag and badge means: In the book text, In the glossary, Computed, Simulation, Illustrative data, Conceptual | PASS | Deck slide 1 speaker note (tags); the badges are the deck's own evidence labels; seeded = the deck's `rng(seed)` | none |
| 3 | B0101 | Figures spoken: `31` | PASS | Each figure is printed on slide 2 at step 1 (machine check, check_narration.py). Badge: Conceptual illustration. | none |
| 4 | B0101 | Explanation of: GROUP; TERMS; WHAT IT IS ABOUT; Definitions and the theorem | PASS | Second-pass check against slide 2 step 1 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 5 | B0102 | Explanation of: Choosing and defending; What the choice means, and what tools implement it | PASS | Second-pass check against slide 2 step 2 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 6 | B0103 | Explanation of: Beyond groups; Person-level checks, and where the choice moves | PASS | Second-pass check against slide 2 step 3 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 7 | B0104 | Explanation of: Causal fairness and the GE Index; Paths, counterfactuals and a single number | PASS | Second-pass check against slide 2 step 4 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 8 | B0201 | Figures spoken: `200`, `0.60`, `0.30` | PASS | Each figure is printed on slide 3 at step 1 (machine check, check_narration.py). Badge: Computed. | none |
| 9 | B0201 | Explanation of: Base rate; in the book text; prevalence; The share of a group that truly has the positive outcome. | PASS | Second-pass check against slide 3 step 1 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 10 | B0202 | Figures spoken: `72`, `48`, `0.60`, `0.70` | PASS | Each figure is printed on slide 3 at step 2 (machine check, check_narration.py). Badge: Computed. | none |
| 11 | B0202 | Explanation of: in the book text; True-positive rate; 72 / (72 + 48) = 0.60; 42 / (42 + 18) = 0.70 | PASS | Second-pass check against slide 3 step 2 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 12 | B0203 | Figures spoken: `24`, `56`, `0.30`, `0.10` | PASS | Each figure is printed on slide 3 at step 3 (machine check, check_narration.py). Badge: Computed. | none |
| 13 | B0203 | Explanation of: False-positive rate; in the book text; 24 / (24 + 56) = 0.30; 14 / (14 + 126) = 0.10 | PASS | Second-pass check against slide 3 step 3 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 14 | B0204 | Figures spoken: `0.75` | PASS | Each figure is printed on slide 3 at step 4 (machine check, check_narration.py). Badge: Computed. | none |
| 15 | B0204 | Explanation of: Predictive value (PPV); in the book text; precision; 72 / (72 + 24) = 0.75 | PASS | Second-pass check against slide 3 step 4 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 16 | B0301 | Figures spoken: `0.48`, `0.28` | PASS | Each figure is printed on slide 4 at step 1 (machine check, check_narration.py). Badge: Computed. | none |
| 17 | B0301 | Explanation of: Demographic parity; in the book text; statistical parity; The model says yes at the same rate in every group. | PASS | Second-pass check against slide 4 step 1 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 18 | B0302 | Figures spoken: `0.60`, `0.70`, `0.30`, `0.10` | PASS | Each figure is printed on slide 4 at step 2 (machine check, check_narration.py). Badge: Computed. | none |
| 19 | B0302 | Explanation of: in the book text; equal TPR and FPR; Both error rates match across groups.; Equalized odds | PASS | Second-pass check against slide 4 step 2 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 20 | B0303 | Figures spoken: `0.75` | PASS | Each figure is printed on slide 4 at step 3 (machine check, check_narration.py). Badge: Computed. | none |
| 21 | B0303 | Explanation of: Calibration parity; in the book text; predictive parity; CALIBRATION PARITY | PASS | Second-pass check against slide 4 step 3 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 22 | B0401 | Figures spoken: `2.0`, `7.0` | PASS | Each figure is printed on slide 5 at step 1 (machine check, check_narration.py). Badge: Computed. | none |
| 23 | B0401 | Explanation of: Impossibility theorem; in the book text; TELL THESE APART; Calibration parity | PASS | Second-pass check against slide 5 step 1 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 24 | B0402 | Figures spoken: `1` | PASS | Each figure is printed on slide 5 at step 2 (machine check, check_narration.py). Badge: Computed. | none |
| 25 | B0402 | Explanation of: c = p_b(1−p_a) / (p_a(1−p_b)), p_a = 0.60; 0.25; 1; 4 | PASS | Second-pass check against slide 5 step 2 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 26 | B0403 | Figures spoken: `0.50`, `0.09` | PASS | Each figure is printed on slide 5 at step 3 (machine check, check_narration.py). Badge: Computed. | none |
| 27 | B0403 | Explanation of: Threshold; in the glossary; The score cutoff above which the model says yes.; GROUP A · BASE RATE 0.60 | PASS | Second-pass check against slide 5 step 3 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 28 | B0404 | Figures spoken: `0.22`, `0.50`, `0.71`, `0.42` | PASS | Each figure is printed on slide 5 at step 4 (machine check, check_narration.py). Badge: Computed. | none |
| 29 | B0404 | Explanation of: τ = 0.22; TPR 0.84; FPR 0.50; PPV 0.42 | PASS | Second-pass check against slide 5 step 4 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 30 | B0501 | Figures spoken: `44.9%`, `23.5%` | PASS | Each figure is printed on slide 6 at step 1 (machine check, check_narration.py). Badge: Computed. | none |
| 31 | B0501 | Explanation of: COMPAS; in the book text; TELL THESE APART; Equalized odds | PASS | Second-pass check against slide 6 step 1 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 32 | B0502 | Figures spoken: `10` | PASS | Each figure is printed on slide 6 at step 2 (machine check, check_narration.py). Badge: Computed. | none |
| 33 | B0502 | Explanation of: RE-ARREST RATE AT EACH RISK SCORE; Black; White; 1 | PASS | Second-pass check against slide 6 step 2 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 34 | B0503 | Explanation of: Values claim; in the book text; Demographic parity; measured by neither side | PASS | Second-pass check against slide 6 step 3 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 35 | B0504 | Figures spoken: `six` | PASS | Each figure is printed on slide 6 at step 4 (machine check, check_narration.py). Badge: Computed. | none |
| 36 | B0504 | Explanation of: Defended choice; in the book text; 1; Specify the deployment | PASS | Second-pass check against slide 6 step 4 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 37 | B0601 | Figures spoken: `2 of 4`, `0.50` | PASS | Each figure is printed on slide 7 at step 1 (machine check, check_narration.py). Badge: Illustrative data. | none |
| 38 | B0601 | Explanation of: Group fairness; in the book text; TELL THESE APART; Group fairness | PASS | Second-pass check against slide 7 step 1 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 39 | B0602 | Explanation of: in the book text; Individual fairness; x and y: same income, history and debt ratio | PASS | Second-pass check against slide 7 step 2 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 40 | B0603 | Figures spoken: `0.14`, `0.02` | PASS | Each figure is printed on slide 7 at step 3 (machine check, check_narration.py). Badge: Illustrative data. | none |
| 41 | B0603 | Explanation of: Lipschitz condition; in the book text; (D, d)-Lipschitz; THE (D, d) CHECK FOR APPLICANTS x AND y | PASS | Second-pass check against slide 7 step 3 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 42 | B0604 | Figures spoken: `0.32` | PASS | Each figure is printed on slide 7 at step 4 (machine check, check_narration.py). Badge: Illustrative data. | none |
| 43 | B0604 | Explanation of: Similarity metric d; in the book text; d(x, y), zip-code distance included; 0.32 | PASS | Second-pass check against slide 7 step 4 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 44 | B0701 | Explanation of: Unawareness (FTU); in the book text; fairness through unawareness; TELL THESE APART | PASS | Second-pass check against slide 8 step 1 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 45 | B0702 | Figures spoken: `85%` | PASS | Each figure is printed on slide 8 at step 2 (machine check, check_narration.py). Badge: Simulation (seeded). | none |
| 46 | B0702 | Explanation of: Proxy; in the book text; GROUP SHARE WITHIN EACH ZIP CODE (200 PEOPLE); zip Z1 | PASS | Second-pass check against slide 8 step 2 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 47 | B0703 | Figures spoken: `0.30`, `0.02`, `0.32` | PASS | Each figure is printed on slide 8 at step 3 (machine check, check_narration.py). Badge: Simulation (seeded). | none |
| 48 | B0703 | Explanation of: Awareness (FTA); in the book text; fairness through awareness; HOW MUCH DOES GROUP COUNT IN d? | PASS | Second-pass check against slide 8 step 3 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 49 | B0801 | Figures spoken: `0.30` | PASS | Each figure is printed on slide 9 at step 1 (machine check, check_narration.py). Badge: Illustrative data. | none |
| 50 | B0801 | Explanation of: Structural causal model; in the book text; Variables with arrows for which causes which.; Direct effect | PASS | Second-pass check against slide 9 step 1 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 51 | B0802 | Figures spoken: `0.40`, `0.50`, `0.20` | PASS | Each figure is printed on slide 9 at step 2 (machine check, check_narration.py). Badge: Illustrative data. | none |
| 52 | B0802 | Explanation of: Indirect effect; in the book text; disparate impact; Attribute moves a mediator, which moves prediction. | PASS | Second-pass check against slide 9 step 2 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 53 | B0803 | Figures spoken: `0.80` | PASS | Each figure is printed on slide 9 at step 3 (machine check, check_narration.py). Badge: Illustrative data. | none |
| 54 | B0803 | Explanation of: in the book text; A confounder links them with no causal path.; Spurious effect; via C 0.30 | PASS | Second-pass check against slide 9 step 3 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 55 | B0804 | Figures spoken: `+0.20` | PASS | Each figure is printed on slide 9 at step 4 (machine check, check_narration.py). Badge: Illustrative data. | none |
| 56 | B0804 | Explanation of: Counterfactual fairness; in the book text; Same decision for this person in another group.; 1 Abduction: infer the background U | PASS | Second-pass check against slide 9 step 4 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 57 | B0901 | Figures spoken: `Eight`, `0.55` | PASS | Each figure is printed on slide 10 at step 1 (machine check, check_narration.py). Badge: Computed. | none |
| 58 | B0901 | Explanation of: Benefit; in the book text; TELL THESE APART; Within-group | PASS | Second-pass check against slide 10 step 1 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 59 | B0902 | Figures spoken: `0.062` | PASS | Each figure is printed on slide 10 at step 2 (machine check, check_narration.py). Badge: Computed. | none |
| 60 | B0902 | Explanation of: GE Index; in the book text; generalized entropy index; DISTANCE FROM THE MEAN, SQUARED, AVERAGED | PASS | Second-pass check against slide 10 step 2 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 61 | B0903 | Figures spoken: `0`, `2` | PASS | Each figure is printed on slide 10 at step 3 (machine check, check_narration.py). Badge: Computed. | none |
| 62 | B0903 | Explanation of: Alpha (α); in the book text; CHANGE IN THE INDEX; lowest benefit falls 0.2 → 0.1 | PASS | Second-pass check against slide 10 step 3 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 63 | B0904 | Figures spoken: `75%`, `25%` | PASS | Each figure is printed on slide 10 at step 4 (machine check, check_narration.py). Badge: Computed. | none |
| 64 | B0904 | Explanation of: GE decomposition; in the book text; SPLIT OF GE(2): TWO GROUPS OF 200; Group A: n = 200, mean 0.65, GE 0.05 | PASS | Second-pass check against slide 10 step 4 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 65 | B1001 | Figures spoken: `0.45` | PASS | Each figure is printed on slide 11 at step 1 (machine check, check_narration.py). Badge: Computed. | none |
| 66 | B1001 | Explanation of: Pre-processing; in the book text; Change the training data first, for example by reweighting.; TELL THESE APART | PASS | Second-pass check against slide 11 step 1 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 67 | B1002 | Figures spoken: `0.00`, `0.29`, `0.36` | PASS | Each figure is printed on slide 11 at step 2 (machine check, check_narration.py). Badge: Computed. | none |
| 68 | B1002 | Explanation of: in the book text; In-processing; loss = error + λ · (false-positive-rate gap); λ = 0 | PASS | Second-pass check against slide 11 step 2 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 69 | B1003 | Figures spoken: `0.09`, `0.60` | PASS | Each figure is printed on slide 11 at step 3 (machine check, check_narration.py). Badge: Computed. | none |
| 70 | B1003 | Explanation of: in the book text; Post-processing; SHARE OF EACH GROUP FLAGGED; one cutoff 0.50 for both | PASS | Second-pass check against slide 11 step 3 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 71 | B1101 | Explanation of: PAIR 1 · LEFT; Demographic parity; The same share of each group is flagged.; A | PASS | Second-pass check against slide 12 step 1 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 72 | B1102 | Explanation of: PAIR 2 · LEFT; Group fairness; Rates match across whole groups.; totals: 0.50 and 0.50 | PASS | Second-pass check against slide 12 step 2 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 73 | B1103 | Figures spoken: `85%` | PASS | Each figure is printed on slide 12 at step 3 (machine check, check_narration.py). Badge: Computed. | none |
| 74 | B1103 | Explanation of: PAIR 3 · LEFT; Awareness; Name how much group counts in d.; finance 0.02 + group w 0.30 | PASS | Second-pass check against slide 12 step 3 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 75 | B1104 | Explanation of: PAIR 4 · LEFT; Disparate treatment; The attribute itself moves the prediction.; A | PASS | Second-pass check against slide 12 step 4 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 76 | B1201 | Figures spoken: `0.00` | PASS | Each figure is printed on slide 13 at step 1 (machine check, check_narration.py). Badge: Computed. | none |
| 77 | B1201 | Explanation of: “make the model fair”; WHAT THE INSTRUCTION DOES; yes-rate gap; 0.20 | PASS | Second-pass check against slide 13 step 1 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 78 | B1202 | Figures spoken: `0.64`, `0.84` | PASS | Each figure is printed on slide 13 at step 2 (machine check, check_narration.py). Badge: Computed. | none |
| 79 | B1202 | Explanation of: “it is accurate, so it is fair”; group A; 0.64; group B | PASS | Second-pass check against slide 13 step 2 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 80 | B1203 | Figures spoken: `85%` | PASS | Each figure is printed on slide 13 at step 3 (machine check, check_narration.py). Badge: Computed. | none |
| 81 | B1203 | Explanation of: “just drop the race column”; coin flip; 0.50; zip code alone | PASS | Second-pass check against slide 13 step 3 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 82 | B1204 | Figures spoken: `0.02`, `0.32` | PASS | Each figure is printed on slide 13 at step 4 (machine check, check_narration.py). Badge: Computed. | none |
| 83 | B1204 | Explanation of: “treat similar people alike”; D(M(x), M(y)); 0.14; d, finance only | PASS | Second-pass check against slide 13 step 4 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 84 | B1205 | Figures spoken: `0.048`, `0.017` | PASS | Each figure is printed on slide 13 at step 5 (machine check, check_narration.py). Badge: Computed. | none |
| 85 | B1205 | Explanation of: “how unfair is it overall?”; total 0.065; within 0.048 (75%); between 0.017 (25%) | PASS | Second-pass check against slide 13 step 5 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 86 | B1301 | Figures spoken: `Six` | PASS | Each figure is printed on slide 14 at step 1 (machine check, check_narration.py). Badge: Conceptual illustration. | none |
| 87 | B1301 | Explanation of: Do the base rates differ, and by how much?; Who bears the cost of each kind of error here?; Is a dropped column really gone, or do proxies remain? | PASS | Second-pass check against slide 14 step 1 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 88 | B1302 | Explanation of: Before you defend a fairness metric | PASS | Second-pass check against slide 14 step 2 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 89 | B1303 | Explanation of: Before you defend a fairness metric | PASS | Second-pass check against slide 14 step 3 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 90 | B1304 | Explanation of: Before you defend a fairness metric | PASS | Second-pass check against slide 14 step 4 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 91 | B1305 | Explanation of: Before you defend a fairness metric | PASS | Second-pass check against slide 14 step 5 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 92 | B1306 | Explanation of: Before you defend a fairness metric | PASS | Second-pass check against slide 14 step 6 and 07-fairness-metrics-choosing-a-definition-and-defending-it.md | none |
| 93 | BVDT | Six recap lines | PASS | Each restates a body beat; nothing new | none |
| 94 | BHTF | Practice prompt | EXEMPT | A viewer exercise composed from the film's terms; not presented as a run | none |

## Things noticed on the deck itself (not changed; for Bear)

- Slide 4 step 1: the caption calls t/f 'the odds ratio'. TPR divided by FPR is a likelihood ratio, not an odds ratio; the narration says 'the ratio of true-positive rate to false-positive rate'.
- Slide 4 steps 3 and 4, slide 10 steps 2 and 3: badge says Computed, but the note says the rates come from a stated illustrative Beta score model. The numbers do recompute correctly; the narration calls the model illustrative.
- Slide 5: badge says Computed, but the step 2 bars are illustrative (the slide itself says so) and the note says 44.9% and 23.5% come from the course review deck, not the chapter, which only says about 2 times. Narration attributes them to ProPublica as reported.
- Slides 6, 7, 11, 12: the same 0.30 that turns d from 0.02 into 0.32 is labelled 'zip-code distance' on slides 6 and 12 and 'group weight w' on slides 7 and 11. Two meanings for one number.
- Slide 7 step 2: the heading says 'group share within each zip code' but the bar labels are head counts (A 87, B 17; A 13, B 83), not shares. The 170 of 200 = 85% does add up.
- Slide 8 step 3: the caption ends 'Same total, 0.80' with nothing earlier for it to be the same as. It is the sum of the three path products, 0.30 + 0.20 + 0.30.
- Slide 9: steps 1 to 3 use eight scores (mean 0.55, GE(2) 0.062); step 4 switches without saying so to the two groups of 200 from the chapter exercise (mean 0.55, total 0.065). A viewer can take 0.062 and 0.065 for the same quantity.
- Slides 11 and 12: badge says Computed, but the 85% is from the seeded simulation and 0.14, 0.02, 0.32 are illustrative values.
- Slide 1 map: the group names do not match the later slide eyebrows (pre-, in- and post-processing sit under 'Choosing and defending' on the map but under 'The toolkit' later; the GE terms under 'Causal fairness and the GE Index' on the map but 'Measuring unfairness' later).
- Extract note, slide 13: all six steps carry identical all_texts because the whole checklist is on screen from step 1 and each step only adds a tick; narration follows the ticks seen in the stills.
