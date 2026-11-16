# FACTCHECK — claude-liam-deep-07-fairness-metrics

**Gate F not yet run.** This file pre-stages the claims that need verification before GATE P, per DOUBLE-CHECK LAW and the deep-explainer "unverified-source caution" rule. The source chapter is a *rough draft* carrying unresolved git merge markers — **narration is written from the HEAD side only** (the `<<<<<<< HEAD` block), and every number is treated as unconfirmed until checked against the primary source, not against the chapter.

| Claim in narration | Beat | Verdict | Note |
|---|---|---|---|
| Impossibility theorem: dem. parity, equalized odds, calibration parity cannot all hold when base rates differ | B00, A2M, A2R, BVDT | HOLDS (math) | Core result; the four-line proof is Bayes' rule (Chouldechova 2017). Argument is safe; see numbers below. |
| Proved 2016, independently, by two teams | A2R, BVDT | VERIFY | Kleinberg, Mullainathan, Raghavan (ITCS 2017; arXiv 2016) — 3-way version. Chouldechova (2017; arXiv 2016) — 2-way. Narration says "proved twice in 2016" — confirm the arXiv-2016 dating is the intended anchor vs the 2017 proceedings year. |
| PPV odds identity v/(1−v) = p/(1−p)·t/f | A2M | HOLDS (math) | Standard Bayes rearrangement; derivation is self-contained and correct. |
| Base rates 0.6/0.3; PPV 0.75/0.75; TPR 0.70/0.70, FPR 0.15/0.15; PPV 0.88/0.67 | A2M2 | HOLDS as illustrative | These are the chapter's worked example. Narration frames them as "take base rates of 0.6 and 0.3…" (illustrative), not as empirical facts. Arithmetic checks (e.g. Group B PPV = 0.3·0.70/(0.3·0.70+0.7·0.10)=0.75). Keep labeled illustrative on-screen. |
| COMPAS, Broward County FL, 2016; FPR substantially higher for Black defendants; Northpointe replied "calibrated" | A3V1, A3V2, A3R, A3M | VERIFY | Angwin/Larson/Mattu/Kirchner, "Machine Bias," ProPublica, 2016-05-23 (data: github.com/propublica/compas-analysis). Northpointe reply: Dieterich/Mendoza/Brennan 2016. Confirm the FPR-disparity direction and the calibration reply against primaries. |
| "~2× the FPR" magnitude | A3M | SOFTENED | Chapter states ~2×; narration says "far higher" / "well above" and the Manim shows an illustrative gap labeled VERIFY. Do NOT assert the exact multiple until confirmed against the ProPublica analysis. |
| Individual fairness = (D,d)-Lipschitz; guarantee hinges on d | A5M, A5V | HOLDS | Dwork, Hardt, Pitassi, Reingold, Zemel (2012). Equation and the d-dependence are the chapter's central point. |
| Counterfactual fairness; abduction–action–prediction; three causal paths | A5M2 | HOLDS | Kusner, Loftus, Russell, Silva (2017); Pearl's ladder Rung 3. Framed as requiring a committed causal graph (chapter's own bound). |
| GE Index; exact within/between decomposition; needs cardinal benefit; not causal | A5M3 | HOLDS | Speicher et al., KDD 2018. Decomposition and limitations stated per chapter. |
| Equalized-odds definition attribution | A1R | HOLDS | Hardt, Price, Srebro, NeurIPS 2016. |
| Mill: *Utilitarianism* (1861) vs *On Liberty* (1859); fairness not one quantity | A4V | HOLDS | AI Wayback section; well-established. Portrait is AI-generated from a PD photo — disclosure sidecar required (see SOURCES / pantry). |
| Toolkit: pre/in/post-processing; none resolves the theorem; none reaches upstream structural bias | A6R | HOLDS | Chapter's toolkit table; argument-level, no datable specifics. |
| Construct gap: re-arrest ≠ the construct society cares about | A6R3 | HOLDS | Chapter's persistent-limits section; argument, not a number. |

**Datable / unconfirmed material stripped (DOUBLE-CHECK LAW):** no product/model version numbers; no exact FPR multiple asserted (softened to "far higher"); the table figures kept explicitly illustrative, not empirical. No chapter `[verify]`-flagged number is asserted as fact. Git merge markers ignored — HEAD side read throughout (figure captions, the individual-fairness computational-hardness note, the counterfactual restatement).
