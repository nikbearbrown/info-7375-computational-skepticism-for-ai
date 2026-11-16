# SOURCES — claude-liam-financial-stress-index
_"Everything Correlates to One"_

## Primary source

- **financial-stress-index-source.md** — Professor Bear's feedback on Mickey's Computational Skepticism final project. Sole source for all claims. All beats derive from this document.

## Referenced works (per source lineage)

The source document names the following published works and databases as the reference lineage for this project. These are cited by the source as the expert scaffolding Bear would ask Mickey to engage:

### Index construction methodology
- **STLFSI** — St. Louis Fed Financial Stress Index; first principal component of 18 weekly data series. Construction methodology determines which attribution methods are coherent.
- **OFR FSI** — Office of Financial Research Financial Stress Index; weighted composite. Same attribution constraint applies.
- Which specific index Mickey uses shapes which decomposition methods are well-posed — the choice should be stated and justified.

### Attribution methods
- **Lundberg & Lee (2017), "A unified approach to interpreting model predictions" (SHAP)** — The primary source for SHAP values. Critically: the paper itself contains caveats on correlated features, which the source document flags as the exact limitation Mickey must engage.
- **LMG relative-importance decomposition** — Lindemann, Merenda & Gold (1980); the regression-based cross-check to SHAP. Encodes a different definition of "contribution" under collinearity, yielding different rankings. Source: "Regression decomposition (variance decomposition, LMG relative importance) gives DIFFERENT attributions."

### Topological data analysis
- **Persistent homology in finance literature** — The parameter-sensitivity concern (embedding dimension, delay, filtration range) is openly discussed in this literature. Source: "the parameter-sensitivity concern is a known, openly discussed limitation there."
- Persistence diagrams / Betti numbers: standard TDA outputs on financial time series.

### Causal reasoning
- **The course's causal-reasoning framework** — The anchor for Part 4's decomposition-vs-causal distinction, as specified in the source lineage section.

## What this reel does NOT cite

This reel is Liam delivering Bear's feedback — it does not present or evaluate the underlying finance literature directly. All claims about methods (SHAP, LMG, VIF, TDA) are pedagogical characterizations drawn from the source document's feedback. The reel should not be read as a literature review.
