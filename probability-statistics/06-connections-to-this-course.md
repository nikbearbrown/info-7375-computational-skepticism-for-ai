# How this connects to the course

Where the ideas in this folder show up when you do the work.

## How many tests is enough? (robustness, lesson 4)

- **The standard error shrinks with the square root of the sample size.** That is the central limit theorem at work (see [sampling, the central limit theorem and inference](03-clt-and-inference.md)). To halve the uncertainty in a measured rate you need four times as many tests.
- **If every test passes, you have not proved the failure rate is zero.** The "rule of three": with n tests and no failures, the failure rate is at most about 3 / n at 95% confidence.

| Tests, all passed | True pass rate is at least (95% confidence) |
|---|---|
| 1 | 5% |
| 10 | 74% |
| 50 | 94.2% |
| 100 | 97.0% |
| 300 | 99.0% |
| 3,000 | 99.9% |

- **How precise is a measured rate?** For a rate near 50%, about 385 tests give ±5 percentage points, 2,401 give ±2, and 9,604 give ±1. A robust accuracy of 71% measured on 100 images could really be anywhere from about 61.5% to 79.0%.
- **Rare failures need many tests.** A failure that happens once in 10,000 will not show up in 100 tests.

## Base rates and Bayes (confidence and calibration, lessons 2 and 11)

A good test's positive result can still be mostly false alarms when the thing it looks for is rare (the disease-test example in [probability](01-probability.md)). A robustness or fairness test needs the base rate of what it is looking for.

## The "clean dataset" (data frame and provenance, lesson 3)

Statistical checks and plots read the data as written; a row that never arrived (the 4% lost in a join) is invisible to them. Reconcile row counts, and ask why each number is the number it is. See [checking and looking at data](04-eda-and-data-quality.md).

## Missing data

**MNAR** (missing not at random) is the formal version of "who did not report, and why." No plot shows it; you find it by thinking about the world the data came from.

## Normality and fat tails

Many real-world quantities are fat-tailed. Averages and "six-sigma" claims can mislead, and the central limit theorem can fail when variance is infinite.

## Many looks at one dataset

Running many checks or tests on one dataset inflates false alarms (see "many tests, more false alarms" in [inference](03-clt-and-inference.md)). The same applies to repeated adversarial testing and to benchmark leaderboards.

## Where to go next

- Lesson 2: [Confidence has to earn its number](../lessons/02-probability-and-calibration/README.md), with the chapter [Probability, uncertainty and the confidence illusion](../chapters/02-probability-uncertainty-and-the-confidence-illusion.md).
- Lesson 3: [The missing rows are part of the result](../lessons/03-data-frame-and-provenance/README.md), with the chapter [Data validation](../chapters/03-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md).
- Lesson 4: [Break the shortcut you just built](../lessons/04-robustness-and-shift/README.md), with the chapter [Robustness](../chapters/04-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md).
- Lesson 11: [Make the sentence no stronger than the evidence](../lessons/11-uncertainty-and-claims/README.md), with the chapter [Communicating uncertainty](../chapters/11-communicating-uncertainty-calibrating-claims-to-evidence.md).
