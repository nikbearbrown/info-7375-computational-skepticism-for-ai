# Random variables and probability distributions

How chance is described with numbers, and the named distributions you will meet.

## Random variables

- A **random variable** is a function from the sample space to numbers: it turns each outcome into a value (heads = 1, tails = 0).
- **Discrete** (a countable list of values) is described by a **probability mass function (PMF)**. **Continuous** (any value in an interval) is described by a **probability density function (PDF)**; probabilities are areas under the curve. (For a continuous variable, the probability of any one exact value is 0.)
- The **distribution** says how probability is spread over the values.
- Two variables can have the same distribution and still differ in how they relate to other variables.
- **CDF** (cumulative distribution function): P(X ≤ x).

## Expected value and spread

- **Expected value:** the average gain or loss if you repeat the procedure many times. Multiply each outcome by its probability and add: E[X] = Σ x · P(x).
- **Roulette example:** a $1 bet on one number wins $35 with probability 1/38 and loses $1 with probability 37/38: 35(1/38) − 1(37/38) ≈ **−$0.053**. Nobody loses exactly 5.3 cents; the average is a long-run property. The same method values a lottery ticket.
- **Linearity:** E[X + Y] = E[X] + E[Y] always, even for dependent variables.
- **Variance** measures spread: Var(X) = E[(X − μ)²] = E[X²] − μ². **Standard deviation** σ = √Var, in the data's own units.

## Probability distributions

What to know first:

- **Probability** is the likelihood of one event (0 to 1). A **probability distribution** is the set of all possible values of a random variable together with their probabilities.
- It matters because it lets you predict, analyze uncertainty, and support decisions, hypothesis tests and modeling.
- The ones to know: **uniform, normal, binomial, Poisson, beta, fat-tailed**, plus **exponential** and **Bernoulli**. One line on each:

| Distribution | What it models | Key facts |
|---|---|---|
| **Bernoulli(p)** | one yes/no trial | mean p, variance p(1−p) |
| **Binomial(n, p)** | number of successes in n independent trials | PMF C(n,k) p^k (1−p)^(n−k); mean np; variance np(1−p) |
| **Poisson(λ)** | count of events in a fixed interval at a steady rate | mean = variance = λ; approximates a binomial with large n and small p |
| **Uniform(a, b)** | every value in [a, b] equally likely | density 1/(b−a); mean (a+b)/2; variance (b−a)²/12 |
| **Normal(μ, σ²)** | bell curve; sums and averages of many small effects | symmetric; about 68% within 1σ, 95% within 2σ, 99.7% within 3σ; z-score z = (x−μ)/σ |
| **Exponential(λ)** | waiting time between events | mean 1/λ; "memoryless" |
| **Beta(α, β)** | an unknown probability or proportion on [0,1] | mean α/(α+β); the standard prior for a success rate |
| **Fat-tailed** (power-law, Cauchy) | extremes far more common than a normal predicts | averages and variances can be unstable or undefined; the central limit theorem can fail |

- **Beta in practice.** Thompson sampling handles the multi-armed bandit (explore vs exploit) by giving each arm a Beta(α, β) belief about its success rate, starting at Beta(1,1) (uniform). Each pull adds the reward to α and the miss to β. It picks the arm with the highest *sampled* value, so uncertainty drives exploration.
- **Related, not the same:** a **fat-tailed distribution** is about extreme *magnitudes*; **long-tail inputs** in the robustness chapter is about many rare *kinds* of case. They are cousins, not twins.

## Joint, marginal and conditional distributions

- A **joint distribution** gives the probability that several random variables take particular values together. Two variables: **bivariate**; more: **multivariate**. It can be written as a joint CDF, a joint PDF (continuous) or a joint PMF (discrete).
- The **marginal distribution** of one variable is its distribution ignoring the others. The **conditional distribution** is a variable's distribution given values of the others.
- X and Y are independent exactly when the joint distribution equals the product of the marginals.
