# FACTCHECK (Gate F) — Probability and the Confidence Illusion

**What.** Every number and named claim in the narration and on screen, checked against its primary or recomputed by script (`evidence/evidence.py`, stdout in `evidence/evidence.stdout.txt`, seeded).
**Why.** The source chapter is a rough draft; several of its facts are loose or wrong. Verdicts: PASS, CORRECTED (the film says something different from the chapter), QUALIFIED (kept, with the limit said), EXEMPT (constructed or illustrative, labelled as such on screen).
**Found.** 7 CORRECTED / QUALIFIED claims, listed first. Everything else PASS or EXEMPT. Primaries were fetched 2026-10-10; links in SOURCES.md.

## Corrections to the chapter

| # | Beat | Claim in the chapter | Verdict | Source | Fix in the film |
|---|---|---|---|---|---|
| C1 | B26 | Casscells et al.: "most answered around 95%" with an "off by two orders of magnitude" gloss | CORRECTED | Casscells, Schoenberger, Graboys, NEJM 299(18):999–1001, 1978, via secondary accounts of the abstract: 60 participants; disease 1 in 1,000, false-positive rate 5%, correct answer about 2% (1.96%); 11 of 60 correct; the most common answer, 27 of 60 (45%), was 95%. 95% was a plurality, not most. (NEJM full text not retrievable; PubMed was cookie-blocked.) | Says "eleven answered correctly; the most common answer, from twenty-seven, was ninety-five percent", and states the study's own 1-in-1,000 and 5% parameters; no "orders of magnitude" claim |
| C2 | B46 | "Models trained on pre-2020 imaging were deployed in 2021; COVID altered the signatures" (DeGrave et al.) | CORRECTED | DeGrave, Janizek, Lee, Nature Machine Intelligence 3(7):610–619, 2021, doi 10.1038/s42256-021-00338-7: using explainable-AI methods, COVID-19 chest-radiograph detectors relied on confounding factors rather than pathology (shortcuts from how the training data was collected), so they look accurate in testing and fail at new hospitals | The chapter's pre-2020/2021 mechanism is not said. The film states the paper's finding: shortcuts instead of pathology, failure at new hospitals. The B46 picture is labelled as an illustration of the mechanism |
| C3 | B57 | Engineers' 90% intervals contain the truth 0.4–0.6 of the time, "two to three times more sure than warranted" | CORRECTED | Soll & Klayman 2004 (substantial overconfidence in interval estimates); Alpert & Raiffa 1982; Russo & Schoemaker; a widely cited review gives true values inside such intervals 30–60% of the time (secondary: McKenzie et al. 2008 and the Soll–Klayman literature). No primary found for the chapter's "engineers" or "two to three times" | Says "far less often than ninety: reviews put it between thirty and sixty percent", and on screen shows ten intervals illustrated, not a measured sample. The "two to three times" gloss is dropped |
| C4 | B18 | Seeing the flag "lowered" the estimate "because the flag is common and most flagged cases are not serious" | CORRECTED | Computed: P(flag)·P(acute) = 0.76 × 0.45 = 0.342 > P(both) = 0.30, so the flag is negatively associated with acuity in this log; P(acute | not flagged) = 0.15 / 0.24 = 0.625. Being common does not by itself lower a probability | Film gives the joint-below-product reason |
| C5 | B32 | Posterior printed 0.0098 in prose and 0.0099 in the term table | QUALIFIED | Exact: 99/10,098 = 1/102 = 0.0098039; the head count 1/(1+99.99) = 1/101 = 0.0099 because it lets the test catch the sick person for certain | Both shown, with the reason |
| C6 | B39 | "Alert on 18% of all hospitalized patients" | CORRECTED | Wong et al., JAMA Intern Med 181(8), 2021: 27,697 patients, 38,455 hospitalizations; score ≥ 6 occurred in 18% of hospitalizations (6,971 of 38,455), not 18% of patients | Says "eighteen percent of hospitalizations" |
| C7 | B66 | Rabanser et al. and a 2024 preprint support "current methods detect a subset of shifts" | QUALIFIED | Rabanser, Günnemann, Lipton, NeurIPS 2019 compared shift-detection methods; the "open problem" judgment is the chapter's. The 2024 preprint (Amoukou et al.) was not fetched and is not spoken | Says methods were compared and that catching every harmful shift without outcomes remains open |

## All claims

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B01 | A classifier's column 0.94, 0.91, 0.88 | EXEMPT | Chapter's illustration of a scoring column; labelled constructed on screen | — |
| 2 | B04 | Plausibility auditing: hearing the wrong note in a number before you can prove it wrong | EXEMPT | Bear's named capacity, defined in one plain sentence per the SELF-CONTAINED LAW; attributed as his phrase in README | — |
| 3 | B09–B11 | Sample space, event, three axioms, P(∅)=0, P(Aᶜ)=1−P(A) | PASS | Kolmogorov axioms, standard; chapter states them; die example derived | — |
| 4 | B12 | Drawing yellow from five distinct balls is 1/5 | PASS | Classical probability, computed | — |
| 5 | B13 | Seven heads in twenty tosses is 7/20 = 0.35; frequency settles for a stable process | PASS | Chapter; the convergence run is seeded in `scenes.py` | — |
| 6 | B15 | P(A\|B) = P(A∩B)/P(B) | PASS | Definition | — |
| 7 | B16–B17 | 76% flagged, 45% acute, 30% both; P(A\|B)=0.30/0.76≈0.395 | PASS | `evidence.stdout.txt`: 0.39473684 | Numbers are the chapter's invented log, said as a log |
| 8 | B20 | 0.9, 0.85, 0.8 → 0.612 | EXEMPT | 0.612 computed (0.6120000000000001); chapter says the numbers are invented | Labelled "constructed numbers" |
| 9 | B22 | 0.9³ = 0.729, a gap of 11.7 points | PASS | Computed; spoken "nearly twelve points" | — |
| 10 | B23–B24 | Total probability; 0.4·0.02+0.3·0.03+0.3·0.05 = 0.032 | PASS | Computed exactly with Fractions | — |
| 11 | B25 | Disease 1 in 10,000; test "99% accurate" | EXEMPT | Chapter's illustrative case | Labelled illustrative |
| 12 | B27–B29 | 10,000 people: 1 sick, 9,999 healthy; 0.01 × 9,999 = 99.99 ≈ 100 false positives; 101 positives, 1 sick → ~1% | PASS | Computed | — |
| 13 | B31–B32 | Bayes: 0.0001·0.99 / (0.0001·0.99 + 0.9999·0.01) = 0.000099/0.010098 = 0.0098 = 1/102 | PASS | `evidence/bayes_run.stdout.txt` | Shown as recorded output |
| 14 | B33 | The positive raised the probability about 98 times (odds 99 times) | PASS | 0.0098039/0.0001 = 98.04; odds 0.99/0.01 = 99 | — |
| 15 | B34 | "99% accurate" doing double duty; sensitivity and specificity are two numbers | PASS | HEAD side of block 3; standard definitions | — |
| 16 | B35 | P(A\|D)=25%, P(B\|D)=28.1%, P(C\|D)=46.9%; spoken "forty-seven" | PASS | Computed exactly: 0.25, 0.28125, 0.46875 | — |
| 17 | B36 | PPV at 99/99: base 1/100 → 50%, 1/1,000 → 9.0%, 1/10,000 → 0.98%, 1/100,000 → 0.099% | PASS | `evidence.stdout.txt` | Spoken "a tenth of a percent" for 0.099 |
| 18 | B37 | Rare-class detectors yield mostly false alarms; only escapes are a higher base rate or lower sensitivity | PASS | Follows from Bayes (computed in B36); chapter's statement | Domain base-rate ranges from the chapter not used (no source) |
| 19 | B39 | Sepsis model: alert in 18% of hospitalizations (6,971 of 38,455), sepsis 7% (2,552), PPV 12% | PASS | Wong et al. 2021 (JAMA IM), fetched | 7% computed 6.6%; see C6 |
| 20 | B40 | Missed 67% (1,709 of 2,552); sensitivity 33% | PASS | Wong et al.; 1,709/2,552 = 66.97%; 843 caught is computed (2,552 − 1,709) | — |
| 21 | B43 | Hume 1748: past regularity does not logically guarantee the future | PASS | An Enquiry Concerning Human Understanding (1748), standard reading; no quotation used | — |
| 22 | B45 | A model's confidence does not move when inputs shift | PASS | Mechanism, labelled "shape only" on screen; supported by the cited literature | — |
| 23 | B51 | Guo et al., ICML 2017: modern networks poorly calibrated, unlike a decade earlier; depth, width, weight decay, batch norm influence it | PASS | arXiv:1706.04599 abstract, fetched | — |
| 24 | B52 | Temperature scaling divides logits by one learned T; T > 1 softens | PASS | Same paper; computed in `evidence.py` | — |
| 25 | B50, B53 | Simulated classifier: 20,000 cases, 74.6% accurate, top bin states 0.97 and is right 0.855; fitted T = 2.19; after, top bin 0.942 vs 0.937; accuracy unchanged | PASS | `evidence/evidence.stdout.txt` and `calib.json`, seed 7; labelled "our simulation" on screen | The chapter's 99 → 85 example is not presented as a measurement |
| 26 | B48 | 70% on 1,000 cases → about 700 positives | PASS | Definition of calibration | — |
| 27 | B58–B59 | CLT needs independence and finite variance; independence fails in networks and autocorrelated series; heavy tails break variance | PASS | Standard statement | — |
| 28 | B60 | Seeded 5,000 draws: Gaussian mean 0.009; Cauchy mean −6.798; single draw −43,455 moved it by −11.9 | PASS | `evidence.stdout.txt` (seed 11) | Labelled our simulation |
| 29 | B61 | Security alerts: $10 per false alarm, $500,000 per missed breach | EXEMPT | The chapter's exercise numbers; spoken as "made-up numbers" | Labelled constructed |
| 30 | B63 | No clean way to tell before the catastrophe that a loss is heavy-tailed; assume heavy tails when errors can harm people | EXEMPT | The author's admission and heuristic, stated as such ("a heuristic and not a calculation") | — |
| 31 | BOPEN–BHTF | Course credit and series position strings | PASS | LECTURE-CREDIT.md and the brief | — |
| 32 | all | Nothing datable: no model names, versions, vendors or "as of" claims | PASS | Sweep of the sheet | — |

Real organisations named: none as subjects of a claim except as authors of cited studies (Harvard physicians in Casscells; Wong et al.'s validation is described without the product or health-system name).
