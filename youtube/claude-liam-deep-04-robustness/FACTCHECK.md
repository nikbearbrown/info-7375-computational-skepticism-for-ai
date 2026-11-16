# FACTCHECK — claude-liam-deep-04-robustness

**Gate F not yet run.** This file pre-stages the claims that need verification before GATE P, per DOUBLE-CHECK LAW and the deep-explainer "unverified-source caution" rule. The source chapter is a *rough draft* that carries its own `[verify]` flags and unresolved git merge markers — treat every number as unconfirmed until checked against the primary source, not against the chapter.

| Claim in narration | Beat | Verdict | Note |
|---|---|---|---|
| Panda→gibbon at 94% → 99.3% | B00, A1M | VERIFY | Goodfellow/Shlens/Szegedy 2015 (arXiv:1412.6572). Confidence figures are the chapter's; confirm exact numbers or soften to "high confidence." |
| Δf = ε‖w‖₁ accumulation | A3M | HOLDS (math) | Standard linearity-hypothesis identity; safe. |
| Robustness plateaus ~90%; human accuracy on fooling set plateaus at same line | A5M2 | VERIFY | Bartoldson et al. ICML 2024 (arXiv:2404.09349). Chapter says the 90% plateau + semantic cause **is** confirmed in the abstract. |
| "scale alone can't cross a semantic limit" / 10^30 FLOPs | A5M2 (implied) | **STRIP** | Chapter explicitly flags the 10^30-FLOPs figure as NOT confirmed. Narration deliberately omits the number and keeps only the semantic-ceiling argument. Keep it omitted. |
| Certified radius R = (σ/2)(Φ⁻¹(pA)−Φ⁻¹(pB)) | A5M | HOLDS | Cohen/Rosenfeld/Kolter ICML 2019. On-screen only, small. |
| "features not bugs" | A2V | VERIFY | Ilyas et al. NeurIPS 2019 (arXiv:1905.02175); debate 2023–2025 unsettled — narration keeps it as a claim researchers made, not settled truth (matches chapter's own hedge). |
| Owner identity spoofing = same proxy structure | A6V1–3 | HOLDS (analogy) | Chapter frames cross-domain as *analogy in the diagnostic*, not identical mechanism. Narration says so explicitly (A6R). |
| Lipschitz "as low as 6" | — | OMITTED | Chapter flags as unsourced; narration avoids any specific Lipschitz constant. |

**Datable material stripped (DOUBLE-CHECK LAW):** no model version numbers, no vendor tool lists, no "as of <month>" claims carried into narration. Attack/tool names kept only where they are field-standard mechanisms (PGD, randomized smoothing, α,β-CROWN → generalized to "formal verification").
