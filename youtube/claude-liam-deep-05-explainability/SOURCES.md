# SOURCES — claude-liam-deep-05-explainability

**Primary source:** `books/computational-skepticism-for-ai/chapters/05-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md` (rough draft; contains `[verify]` flags and unresolved git merge markers — HEAD side read, see FACTCHECK.md).

**Papers / works referenced by the chapter (verify against these, not the chapter):**
- Scott M. Lundberg & Su-In Lee — *A Unified Approach to Interpreting Model Predictions*, NeurIPS 2017 (arXiv:1705.07874) — SHAP.
- L. S. Shapley — *A Value for n-Person Games*, in *Contributions to the Theory of Games II*, Princeton, 1953, 307–317 — the game-theoretic foundation.
- Marco Tulio Ribeiro, Sameer Singh, Carlos Guestrin — *"Why Should I Trust You?": Explaining the Predictions of Any Classifier*, KDD 2016 (DOI:10.1145/2939672.2939778) — LIME.
- Judea Pearl & Dana Mackenzie — *The Book of Why*, Basic Books, 2018 — the ladder of causation (Rung 1 association, Rung 2 intervention, Rung 3 counterfactual).
- Cynthia Rudin — *Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead*, *Nature Machine Intelligence* 1:206–215, 2019 (DOI:10.1038/s42256-019-0048-x).
- Robert Geirhos et al. — *Shortcut Learning in Deep Neural Networks*, *Nature Machine Intelligence* 2:665–673, 2020 (DOI:10.1038/s42256-020-00257-z).
- Alex J. DeGrave, Joseph D. Janizek, Su-In Lee — *AI for radiographic COVID-19 detection selects shortcuts over signal*, *Nature Machine Intelligence* 3:610–619, 2021 (DOI:10.1038/s42256-021-00338-7).
- Kjersti Aas, Martin Jullum, Anders Løland — *Explaining individual predictions when features are dependent*, *Artificial Intelligence* 298:103502, 2021 (DOI:10.1016/j.artint.2021.103502) — correlated-feature / conditional-SHAP problem.
- Ludwig Wittgenstein — *Philosophical Investigations*, Blackwell, 1953 — language games (application to model self-report is the chapter author's own reading).
- Hans Reichenbach — *Experience and Prediction*, 1938 — context of discovery vs. context of justification.
- Shapira et al. — *Agents of Chaos*, 2026 (arXiv:2602.20021, https://agentsofchaos.baulab.info/) — the Ash agent case. **Provider-side persistence mechanics flagged [verify] by the chapter; keep generic until checked.**

**Seeds / determinism:** all Manim and Remotion scenes are deterministic (no generative media of real people in the built scenes). Vox pantry stills are AI-generated; disclosure sidecars required at pantry-fill.

**Rights / provenance:**
- Tier 1 stills (A1V, A3V, A5V, A6V1–3): generic/illustrative, no real referent, no rights escalation.
- **Tier 3 (A7V — Hans Reichenbach portrait):** real named historical person. AI-generated portrait based on a public-domain Wikimedia photograph. Requires PD confirmation of the source photo + AI-disclosure/provenance sidecar + on-screen credit before use. Only rights escalation in the episode.

**Corrections applied vs. source:**
- "175 billion parameters" softened to "hundreds of billions of parameters" (strip datable specific).
- "Need co-occurs with misalignment" aphorism (chapter's own `[verify]`) omitted from narration — held as working intuition, not asserted.
- Ash provider-side mechanics narrated generically; no specific provider product/version named.
- Axiom naming clash (Additivity vs. Linearity) resolved to "Additivity" only in narration.
- All git merge markers resolved to HEAD (Chapter-5 numbering); non-HEAD D3-figure "Prompts" section ignored.
