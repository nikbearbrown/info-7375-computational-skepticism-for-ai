# SOURCES — claude-liam-deep-11-communicating-uncertainty

**Primary source:** `books/computational-skepticism-for-ai/chapters/11-communicating-uncertainty-calibrating-claims-to-evidence.md` (rough draft; contains `[verify]` flags and **unresolved git merge markers** — HEAD is chapter 11, incoming branch renumbers to 12. Read HEAD only. See FACTCHECK.md).

**Papers / references cited by the chapter (verify against these, not the chapter):**
- Brier, G. W. — *Verification of Forecasts Expressed in Terms of Probability*, Monthly Weather Review, 1950 (the Brier score).
- Murphy, A. H. — *A New Vector Partition of the Probability Score*, J. Applied Meteorology, 1973 (Uncertainty − Resolution + Calibration decomposition).
- Naeini, Cooper, Hauskrecht — *Obtaining Well Calibrated Probabilities Using Bayesian Binning*, AAAI 2015 (ECE / MCE binning definitions).
- Guo, Pleiss, Sun, Weinberger — *On Calibration of Modern Neural Networks*, ICML 2017 (overconfidence of modern deep nets; temperature scaling).
- Minderer, Djolonga, Romijnders, Hubis, Zhai, Houlsby, Tran, Lucic — *Revisiting the Calibration of Modern Neural Networks*, NeurIPS 2021 (newer architectures often better calibrated — rebuts the "dominant regardless of architecture" superlative).
- Wong, Otles, Donnelly, Krumm, McCullough, et al. — *External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients*, JAMA Internal Medicine, 2021 (Epic Sepsis Model; Michigan Medicine cohort).
- Mastrandrea, Field, Stocker, et al. — *Guidance Note for Lead Authors of the IPCC Fifth Assessment Report on Consistent Treatment of Uncertainties*, IPCC, 2010 (calibrated-language / likelihood terms).
- Angelopoulos, A. N. & Bates, S. — *A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification*, 2021 (arXiv:2107.07511).
- Vovk, Gammerman, Shafer — *Algorithmic Learning in a Random World*, Springer, 2005 (conformal prediction foundation).
- Platt, J. — *Probabilistic Outputs for Support Vector Machines* (Platt scaling), 1999; and isotonic regression as the non-parametric alternative (both named by the chapter, not narrated in detail).
- NIST — *AI Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, 2023 (validation-communication context; optional).

**Seeds / determinism:** all Manim + Remotion scenes are deterministic (no generative media of real people). Vox pantry stills are AI-generated illustrative — Tier 1 for all except **A5V (Tier 2)**, which stands in for the real sepsis external-validation failure and requires a disclosure sidecar plus generic (non-identifying) imagery at pantry-fill.

**Corrections applied vs. source:** specific ECE thresholds (~0.02–0.05 / >0.10) omitted (chapter `[verify]`-flagged, not scale-free); "overconfidence dominant regardless of architecture" superlative held — narrated as "well documented, but newer architectures can be better calibrated" (Guo for the phenomenon, Minderer for the limit); no LLM-specific overconfidence claim (chapter `[verify]`-flagged); sepsis figures softened to qualitative and verify-gated to Wong et al.; kCE state-of-practice remark omitted as datable; git merge markers ignored (HEAD/ch11 read only).
