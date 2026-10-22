# Sampling, the central limit theorem and inference

Why a sample can tell you about a population, how sure you can be, and how a test of a claim works.

## Tail bounds, the law of large numbers and the central limit theorem

**Tail bounds**
- **Markov**: for X ≥ 0, P(X ≥ a) ≤ E[X]/a. **Chebyshev**: P(|X − μ| ≥ kσ) ≤ 1/k². Both give only power-law decay and need little else.
- **Chernoff bound.** For a sum of **independent** random variables it bounds the tail **exponentially**, much tighter than Markov or Chebyshev, but it needs independence. The recipe is Markov's inequality applied to e^(tX), then optimized over t. For a sum X of independent Bernoulli(p) variables with mean μ = np: P(X ≥ (1+δ)μ) ≤ [e^δ / (1+δ)^(1+δ)]^μ. It has an additive form (bounds absolute error) and a multiplicative form (bounds error relative to the mean). It is related to Bernstein and Hoeffding inequalities.

**Law of large numbers**: as the sample grows, the sample mean settles toward the true mean μ.

**Central limit theorem (CLT)**
- **Statement:** take independent, identically distributed observations with mean μ and finite variance σ². As the sample size n grows, the distribution of the **sample mean** approaches a normal distribution: X̄ ≈ Normal(μ, σ²/n). Equivalently, (X̄ − μ) / (σ/√n) approaches the standard normal.
- **It is about the average, not the data.** The raw data stays skewed or lumpy; the *averages* of many samples become bell-shaped.
- **Standard error** = σ/√n (estimated by s/√n): how much a sample mean wobbles from sample to sample. Quadrupling n halves it.
- **Rule of thumb:** n of about 30 or more is often enough if the data are not very skewed. This is a guideline, not a theorem; heavy skew or outliers need more.
- **Where it fails:** very heavy tails or infinite variance (for example the Cauchy distribution); strongly dependent observations.
- **Why it matters:** it is why normal-based confidence intervals and tests work on non-normal data, and why proportions behave like normals (a binomial count is a sum of Bernoulli trials, so the sample proportion p̂ ≈ Normal(p, p(1−p)/n)).

## Statistical inference, estimation and hypothesis testing

- **Statistical inference:** using a sample to draw conclusions about a population, and to quantify uncertainty.
  - *Advantages:* generalize from a small sample, quantify confidence, find patterns, test hypotheses, compare groups.
  - *Limits:* only as reliable as the sample; a non-representative sample gives biased results; outliers distort; the choice of method changes the answer; results are estimates.
  - *Techniques named:* descriptive statistics; inferential statistics (t-test, ANOVA, regression, chi-square); Bayesian inference (Bayes' theorem, MCMC); maximum likelihood; hypothesis testing; resampling (bootstrap, permutation); dimension reduction (PCA, t-SNE, ICA); regularization (L1, L2, ridge, lasso).
- **Hypothesis testing.** Assume the **null hypothesis H0** is true, and ask whether the data would be a "small probability event" under it. If so, reject H0.
  - **Significance level α:** how small counts as small; commonly 0.1, 0.05 or 0.01.
  - **Steps:** (1) state H0 and the alternative H1; (2) assuming H0, build a test statistic T; (3) given α, find the critical value (rejection region); (4) compute T from the sample; (5) see whether T falls in the rejection region and conclude.
  - Common tests: **t-test, ANOVA, Mann–Whitney, Wilcoxon signed-rank**.
  - "Small probability" is a convention, not a logical contradiction.
- **What a p-value is.** The probability, *assuming H0 is true*, of seeing data at least as extreme as yours. It is **not** the probability that H0 is true.
- **Errors.** *Type I:* reject a true H0 (probability α). *Type II:* fail to reject a false H0 (probability β). *Power* = 1 − β. Failing to reject is not proof of no effect.
- **Many tests, more false alarms.** Run 20 independent tests at α = 0.05 and you expect about one false positive. Adjust for multiple comparisons.
- **t-test vs Z-test:** the t-test uses the t-distribution; the Z-test uses the normal. A **z-score** is z = (x − μ) / σ. Use t when σ is estimated from a small sample; the t-distribution has heavier tails and approaches the normal as n grows.
- **Confidence interval for a mean:** x̄ ± t × s/√n. **Correct reading:** if you repeated the study many times, 95% of intervals built this way would contain the true mean. It does **not** mean there is a 95% chance this particular interval contains it, A 95% interval that excludes 0 corresponds to rejecting "no effect" at the 5% level (two-sided); that, not "a 95% chance the effect is real," is how an interval relates to a test.
- **Normality testing.** Checks whether a sample is well modeled by a normal distribution. A normal sample is assumed by the t-test and ANOVA. Three tests, each giving a p-value (below the threshold, such as 0.05, means "not normal"):
  - **Shapiro–Wilk:** compares ordered sample values with normal expectations.
  - **Anderson–Darling:** compares the sample and normal cumulative distributions with extra weight on the **tails**; described as one of the most powerful.
  - **Kolmogorov–Smirnov:** the **maximum gap** between the sample and normal cumulative distributions; simple, widely used, less powerful.
  - **Q–Q plot:** observed quantiles against expected normal quantiles; points near a straight line mean approximately normal. Use it beside any test.
  - Normality can be framed three ways: goodness of fit (descriptive), a frequentist test against "the data are normal," and a Bayesian comparison (Bayes factor).
  - With a very large sample, these tests flag trivial departures; with a small one, they miss real ones. By the CLT the mean of a large sample can be treated as normal even if the data are not.
