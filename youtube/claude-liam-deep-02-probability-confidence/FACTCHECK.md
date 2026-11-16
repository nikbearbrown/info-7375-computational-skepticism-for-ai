# FACTCHECK — claude-liam-deep-02-probability-confidence

**Gate F not yet run.** This file pre-stages the claims that need verification before GATE P, per DOUBLE-CHECK LAW and the deep-explainer "unverified-source caution" rule. The source chapter is a *rough draft* carrying unresolved git merge markers (`<<<<<<< HEAD … ======= … >>>>>>>`). **The HEAD side was read; the other side (card-drawing example, Alice's Markov chain, the "defective item / factory" phrasings) was ignored.** Treat every number as unconfirmed until checked against the primary source, not against the chapter.

## Illustrative arithmetic (invented-for-teaching — safe to keep, NOT empirical claims)
These are the chapter's own clean pedagogical numbers, explicitly invented "to keep the arithmetic clean." They assert nothing about the world, so they carry no verification burden — but the narration frames them as illustrations, never as measured facts.

| Example | Beat | Numbers | Verdict |
|---|---|---|---|
| Triage flag lowers the odds | A2R | 76% flagged, 45% serious, 30% both → ≈39.5% | HOLDS (illustrative; narrated as "just under half" / "below forty percent") |
| Agent tool-call chain | A3M | 0.9 · 0.85 · 0.8 = 0.612 | HOLDS (illustrative) |
| Independence trap | A3R | 0.9³ = 0.729 vs 0.612 | HOLDS (arithmetic) |
| Fleet / total probability | A3M2 | .4/.3/.3 × .02/.03/.05 → 0.032 | HOLDS (illustrative) |
| Disease test / count bodies | B00, A4M, A4R | 1-in-10,000 base rate, 99% accurate → ~1/101 ≈ 1% | HOLDS (canonical textbook example; the chapter's headline demo) |

## Empirical claims / named studies (VERIFY against primary source before GATE P)

| Claim in narration | Beat | Verdict | Note |
|---|---|---|---|
| "Trained clinicians make the same slip" (Harvard house officers ~95% on the 1-in-1000 version) | A4M, A4R | VERIFY | Casscells, Schoenberger & Graboys, *NEJM* 299 no.18 (1978). Narration keeps only the qualitative "trained clinicians miss it too" — the exact 95% figure is NOT spoken. Confirm before restoring any number. |
| Hospital sepsis model "alerted on nearly a fifth of all patients while missing most of the sepsis" | A4R2 | VERIFY | Wong et al., *JAMA Internal Medicine* 181 no.8 (2021): alert on ~18% of hospitalized patients; sensitivity ~33% (missed 67%). Narration **softens to "nearly a fifth" / "missing most"** and omits the exact 18%/33% per DOUBLE-CHECK LAW; restore precise figures only after checking the primary source. No vendor/model name spoken. |
| Pre-/during-pandemic medical imaging drift; models "kept predicting, fluent and confident" | A5V | VERIFY | DeGrave, Janizek & Lee, *Nature Machine Intelligence* 3 (2021) — shortcut learning in COVID radiography. Narration keeps the **mechanism only** (signatures shifted, confidence unmoved), strips the year, names no dataset. |
| Modern deep nets overconfident at the high end; "says 99 when it should say 85" | A6M | HOLDS | Guo, Pleiss, Sun & Weinberger, *On Calibration of Modern Neural Networks*, ICML 2017 (arXiv:1706.04599). Well-documented; the 99/85 pair is illustrative, not a quoted measurement. |
| Temperature scaling: softmax(z/T), T>1, fixes confidence not ranking | A6M2 | HOLDS (math) | Same paper. Standard identity; safe on-screen. |
| Human 90% intervals contain truth "about half the time"; engineers score 0.4–0.6 | A6V | VERIFY (soft) | Chapter's own calibration-baseline claim; matches the overconfidence literature. Narration keeps "about half the time" (qualitative), no hard fraction spoken. |
| Frank Ramsey — died at 26; probability as a property of a person's belief; *Truth and Probability* (1926) | A7V | VERIFY | Biographical (Ramsey 1903–1930). **Real named person → Tier 3 pantry asset → RIGHTS FLAG:** portrait must be AI-generated from a confirmed public-domain photograph (Wikimedia) with an AI-generated disclosure sidecar. Dates on the SlateCard eyebrow (1903–1930) VERIFY. |
| Three probability axioms; conditional-probability definition; chain rule; total probability theorem; Bayes; CLT requires independence + finite variance | A1M, A2M, A3M, A3M2, A4R, A7M | HOLDS (math) | Standard results; safe. |
| Hume's problem of induction ↔ distribution shift | A5M, A5R | HOLDS (framing) | Standard philosophical framing carried by the chapter; narrated as analogy, not a measured claim. |

**Datable material stripped (DOUBLE-CHECK LAW):** no "as of 2021/2022", no model version numbers, no vendor/tool names carried into narration. "Before a pandemic / during it" kept as mechanism only (no year). Named mechanisms retained only where field-standard (base rate, sensitivity/specificity, softmax, temperature scaling, central limit theorem).

**Precision-about-precision note (from the chapter's own HEAD-side flag):** the chapter admits "99% accurate" is doing double duty as both sensitivity and specificity. The narration keeps the loose shortcut for clean counting (as the chapter does) but never claims they are one number — A4R explicitly labels the 0.99 as *sensitivity*.
