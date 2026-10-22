# Modeling basics: regression, classification, resampling, regularization

The standard toolkit for fitting and checking a model, in one pass.

## Correlation and regression

- **Regression:** model how a *dependent* variable (the effect) changes with *independent* variables (the cause or predictor). Purposes: **description, estimation, control**. Steps: select variables, collect data, specify the model, fit, validate and check accuracy. Types: simple linear, multiple linear, logistic, ridge, lasso, polynomial. A common metric: **mean squared error**.
- **Linear regression.** y = β0 + β1 x + ε. β0 is the intercept (predicted y when x = 0); β1 is the slope (change in y per one-unit rise in x); ε is the error. Each observation = a systematic part (β0 + β1 x) + random error. Simple regression has one predictor, multiple regression several. Synonyms: response = regressand = dependent; predictor = regressor = independent = explanatory.
- **Least squares.** Fit by minimizing the sum of squared residuals. **R²** is the share of variance explained. Check residual plots: a visible pattern signals the wrong model form.
- **Interaction term.** Adding female × math lets the effect of math differ by group; the effect of one variable then cannot be read alone. For females (female = 1) the slope on math is (β2 + β3), for males β2.
- **Standardized coefficient:** a coefficient on standardized variables, so effects can be compared across predictors in different units. (It is computed by scaling each variable to mean 0 and standard deviation 1.)

## Classification, logistic regression and metrics

- **The supervised learning problem.** Training data (x1,y1) … (xN,yN): predictors X (inputs, features, covariates) and an outcome y. **Regression:** y is a number. **Classification:** y is one of a few unordered categories. **Goals:** predict unseen cases accurately, understand which inputs matter and how, and assess the quality of predictions. **Inferential** models care about the "why"; **predictive** models about the value.
- **Unsupervised learning:** no outcome variable; find groups or structure; hard to know how well you are doing.
- **Machine learning vs statistical learning vs pattern recognition:** overlapping fields (computer science, statistics, engineering). Statistical learning stresses models, interpretability and uncertainty; machine learning stresses large-scale prediction.
- **Classification.** Assign an observation to a category, trained on known labels. Most models output a *probability* of each class, so it works like regression plus a **threshold**.
- **Logistic regression.** logit(p) = log(p/(1−p)) = β0 + β1 x. The slope is the change in **log-odds** per unit of x. Exponentiate to read it as an **odds ratio**: **exp(β)**.
  - Worked example: β(math) = 0.1563, exp(0.1563) = 1.169, so each extra point multiplies the odds of honors by about 1.17, a **17% rise in the odds** (it is the odds, not the probability).
  - Another: female coefficient 0.98, exp(0.98) = 2.66, so the odds for females are about 2.66 times the odds for males, holding the others fixed.
  - The intercept is the log-odds when all predictors are 0; it is meaningful only if 0 is a realistic value (no student scored below 30).
- **Metrics.**
  - **RMSE / MSE** (regression): square the errors, average, take the root. Smaller is better; it punishes large errors and is **sensitive to outliers**; easy to optimize.
  - **AUC** (binary classification): area under the ROC curve; the probability the model ranks a random positive above a random negative; 0.5 is chance, 1 perfect. Scale-invariant and threshold-invariant, which can be a drawback (it ignores calibration and unequal costs of false positives and negatives).
  - **Log loss** (probability outputs, binary or multi-class): penalizes confident wrong probabilities; ideal is 0.
- **Imbalanced data.** A rare-event classifier with 97% accuracy may be useless: always predicting "no meteorite impact" scores 99.99999%+. Use metrics that respect the rare class.

## Resampling and validation

- **Resampling** reuses the data to (1) estimate how precise a statistic is, (2) run significance tests by shuffling labels, (3) validate models.
- **Bootstrap:** repeatedly draw n points *with replacement*, compute the statistic each time, and use the spread of results as its standard error or interval. Pseudocode: repeat B times: sample n points with replacement; compute the statistic; store it. Then take the standard deviation or percentiles of the B stored values.
- **Jackknife:** leave one point out at a time.
- **Permutation test** (exact, randomization test): shuffle the labels many times to see how often chance alone gives a result as extreme as the real one.
- **k-fold cross-validation:** split the data into k parts; train on k−1, test on the held-out part; rotate through all k; average the results. The usual wrong way: doing preprocessing or feature selection on all the data before splitting, which leaks information; do it *inside* each training fold.

## Regularization, model selection, bias and variance

- **Regularization.** Add a penalty to the loss to prevent **overfitting**: minimize Σ loss + λ · R(f), where λ controls how heavy the penalty is. It imposes a kind of Occam's razor, and from a Bayesian view it corresponds to a prior on the parameters. Three approaches:
  - **Subset selection:** keep only the predictors believed to matter.
  - **Shrinkage:** fit all predictors but shrink coefficients toward 0. **Ridge** (L2 penalty) shrinks all and rarely sets any exactly to zero; **lasso** (L1) can set some exactly to zero, so it also **selects variables**. Choose λ by cross-validation.
  - **Dimension reduction:** project the p predictors onto M < p combinations (principal components regression, partial least squares).
- **Model selection tools:** best subset, forward and backward stepwise selection; Mallow's Cp, AIC, BIC, adjusted R²; validation set and cross-validation.
- **Bias–variance trade-off.** A flexible model has low bias and high variance (it fits noise); a rigid one has high bias and low variance. Test error is lowest in between.
- **Beyond linear:** polynomials, splines, generalized additive models, decision trees, bagging, random forests, boosting, support vector machines.
- **Bagging, boosting, stacking:** ensemble methods. Bagging averages models trained on bootstrap samples; boosting trains models in sequence, each fixing the last one's errors; stacking trains a model to combine other models' predictions.
- **Parametric vs non-parametric:** a parametric model assumes a fixed functional form with a fixed number of parameters (linear regression); a non-parametric one assumes less and grows more complex with data (k-nearest neighbors, trees).

## Unsupervised learning

- Looks for **undetected patterns in unlabeled data**. Two main methods: **principal component analysis (PCA)** and **cluster analysis**.
- **Cluster analysis** groups similar items and can reveal anomalies that fit no group.
- Supervised learning infers p(x|y); unsupervised learning infers p(x), the density of the inputs.
- **k-means:** pick k centers; assign each point to its nearest center; recompute each center as the mean of its points; repeat until nothing changes.
