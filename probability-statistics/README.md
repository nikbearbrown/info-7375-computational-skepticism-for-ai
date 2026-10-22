# Probability and statistics: the background this course assumes

**What this is:** a short, practical reference for the probability, distributions, central limit theorem, exploratory data analysis (EDA) and basic modeling ideas the course keeps using.
**Why it exists:** this is material you should already know, and a lot of students do not. The course asks questions like "how likely is that," "is ten tests enough," "is this number a base rate or a result," "is this data normal," and "did the dataset lose rows." Each one needs an idea from this folder.
**What is inside:** six short files, to be read in order or used as a lookup. Each is a set of definitions, formulas and worked examples, not a lecture.

| File | What it covers |
|---|---|
| [01-probability.md](01-probability.md) | probability, sets, conditional probability, independence, Bayes' theorem, counting |
| [02-random-variables-and-distributions.md](02-random-variables-and-distributions.md) | random variables, expected value, variance, uniform, normal, binomial, Poisson, beta, fat-tailed |
| [03-clt-and-inference.md](03-clt-and-inference.md) | tail bounds, law of large numbers, **central limit theorem**, standard error, hypothesis tests, p-values, confidence intervals, normality tests |
| [04-eda-and-data-quality.md](04-eda-and-data-quality.md) | **statistical checks**, **EDA and why we do it**, missing data (MCAR, MAR, MNAR), imputation, visualization |
| [05-modeling-basics.md](05-modeling-basics.md) | regression, logistic regression and odds ratios, metrics, resampling, regularization, clustering |
| [06-connections-to-this-course.md](06-connections-to-this-course.md) | where these ideas show up in the lessons and chapters |

## You should be able to

- Explain why P(A|B) is not P(B|A), and work a disease-test (Bayes) problem with counts.
- Say what a random variable and a distribution are, and pick the right named distribution for a situation.
- State the central limit theorem in one sentence, say what it does and does not claim, and use the standard error.
- Say what a p-value is and is not, and what a 95% confidence interval does and does not mean.
- Tell MCAR, MAR and MNAR apart, and say why the third is the dangerous one.
- Say why we plot data before modeling (a person cannot read 100,000 rows, and the human brain is good at pictures), and list the statistical checks that come before the plots.
- Read a logistic-regression coefficient as an odds ratio.
- Explain why 97% accuracy can be useless on a rare event.
- Work out roughly how many tests you need before you trust a measured rate.

## Status and how to use it

**Draft.** Written from earlier probability and statistics course material plus standard references, and **not yet reviewed by Professor Bear.** The central limit theorem, confidence-interval and p-value material was added from standard sources because the earlier course material did not cover it. Check any formula against a textbook before relying on it for graded work.

Use it the way you would a cheat sheet: skim a file, find the idea you are shaky on, work the small example, and move on.
