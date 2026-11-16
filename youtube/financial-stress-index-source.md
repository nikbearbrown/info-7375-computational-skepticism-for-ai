# Professor Bear's feedback — Mickey's Computational Skepticism final project
_Source for a deep-explainer reel. FIRST NAME ONLY: "Mickey." The reel is Bear's feedback
on the project idea below._

## The student's proposal (Mickey)
Study what is really behind changes in financial stress, measured by a national financial
stress index. The headline number collapses very different things — credit markets, bank
funding, interest rates, volatility, leverage, investor risk appetite — into one figure.
The project looks INSIDE the index to identify which parts matter most, when they matter, and
whether stress is concentrated in a few indicators or spread across the system, using three
methods: contribution analysis, machine learning, and topological data analysis (TDA). Mickey
has said he wants to develop this into a publishable paper "very soon."

## The core problem
It's a genuinely good question and the three-method toolkit is ambitious and well-matched to a
doctoral finance project. Where it can go wrong isn't the ambition — it's that **most financial
stress indices are constructed in a way that makes clean attribution close to impossible**, and
each method has a specific, documented failure mode on this data. And the stated publication
pressure is exactly the condition under which overclaiming and method-shopping happen — so the
skeptical instruments here are the actual difference between a defensible paper and a
retracted-in-review one.

## Part 1 — the attribution problem is STRUCTURAL, not a modeling choice
Most indices (STLFSI, OFR FSI) are the first principal component / a weighted composite of
underlying indicators that are themselves highly correlated (credit spreads move with vol, which
moves with funding stress — during crises "everything correlates to 1"). **When inputs are
collinear, there is no single correct decomposition of how much each contributed.** True of
contribution analysis, Shapley/SHAP importance, and regression decomposition alike.
- SHAP splits credit "fairly" between correlated indicators — well-behaved but misleading: if
  credit spreads and VIX are 0.9 correlated in a crisis, SHAP may report each 40% important when
  the honest statement is "these two are so entangled here that individual attribution isn't
  meaningful."
- Regression decomposition (variance decomposition, LMG relative importance) gives DIFFERENT
  attributions than Shapley — not because one is wrong, but because they encode different
  definitions of "contribution" under collinearity. Pick one and justify it, OR run several and
  report agreement/disagreement AS a finding.
Feedback angle: lead with an explicit multicollinearity diagnostic (VIF / correlation heatmap of
the underlying indicators, ESPECIALLY within crisis subperiods) before any contribution analysis,
and state which definition of "contribution" each method uses. A VIF that SPIKES during crises is
itself a finding — direct evidence that "which indicator matters most" is less well-posed exactly
in the periods the project cares about most.

## Part 2 — the ML component faces a small-N crisis problem
Saying importance "changes during crises" requires enough independent crisis episodes to estimate
that change. The modern-era sample is tiny — 2008 GFC, 2020 COVID, arguably 2022 rate shock:
three or four episodes. So **crisis-period feature importance is really importance estimated on
three data points**, however sophisticated the model. Crisis-window importance estimates will have
very high variance; small shifts to the window boundaries could reorder which indicator "mattered
most"; a model that "finds crisis-specific patterns" may just be overfitting 2008/2020 individually
and presenting it as a general "importance shifts during stress" claim.
Feedback angle: require a robustness check that perturbs crisis-window boundaries (±1 month) and
re-computes the importance ranking — if the ranking is unstable under small shifts, report that as
a limitation, don't smooth it over. And ask whether the ML claims are validated out-of-sample in
any real sense, given how few episodes exist to hold out.

## Part 3 — topological methods need their OWN sensitivity analysis
TDA on financial time series is legitimate but **persistence diagrams / Betti numbers are highly
sensitive to preprocessing** — embedding dimension and delay (time-series → point-cloud), distance
metric, filtration range, window length. It's easy to produce a striking "topological signature of
2008" that is mostly an artifact of one parameter choice.
Feedback angle: require a parameter-sensitivity sweep as a FIRST-CLASS methodological step — show
the qualitative conclusion ("stress becomes topologically concentrated in crises") holds across a
range of embedding dims and window lengths, not just the cleanest-looking diagram. And ask whether
the TDA findings are cross-validated against the Part 1 contribution analysis: convergence = real
evidence; divergence = investigate, don't quietly report only the more publishable method.

## Part 4 — descriptive attribution vs. causal language
This is a decomposition/attribution project, not causal identification — the write-up must stay
disciplined about that. "Credit market stress accounts for 40% of the index variance in this
window" is defensible/descriptive. "Credit market stress CAUSED the spike" is causal — and none of
the three methods are designed to support it (all describe statistical association/decomposition
within a constructed index, not exogenous shocks).
Feedback angle: audit the draft for causal verbs ("drove," "caused," "triggered") wherever the
method is actually descriptive, and either soften the language or add an explicit caveat
distinguishing decomposition from causal identification.

## Part 5 — honest visualization under collinearity
- Stacked-area / waterfall "contribution by indicator" charts imply a cleanliness of separation
  collinear inputs don't support — where VIF shows serious collinearity, communicate uncertainty
  (banded/fuzzy contributions or an explicit annotation), not crisp percentage splits.
- Persistence diagrams / Betti curves need the parameter-sensitivity result shown ALONGSIDE the
  headline — small multiples across a few parameter choices, not one clean diagram.
- Cross-method comparison charts (Shapley vs regression vs TDA) should show agreement AND
  disagreement explicitly, not cherry-pick the method whose story is being told.

## Close: publication note + open questions
Given the publication goal: reviewers in finance/econometrics will specifically probe collinearity
handling and crisis-sample size — building these checks in NOW is protective of the publication
goal, not a delay. End with one or two open questions for Mickey to resolve himself (which specific
published index construction to use as the base and why; how to handle the case where TDA and
contribution analysis substantively disagree). Tone: encouraging but exacting — sharpen it into
something that holds up under peer review, not just course grading.

## Reference lineage
STLFSI / OFR FSI construction methodologies (state which base index and why — PCA weighting affects
which attribution methods are even coherent); Lundberg & Lee, SHAP (2017) — cite its own caveats on
correlated features; LMG relative-importance decomposition — the regression-based cross-check;
persistent-homology-in-finance literature — the parameter-sensitivity concern is a known, openly
discussed limitation there; the course's causal-reasoning framework — the anchor for Part 4's
decomposition-vs-causal distinction.
