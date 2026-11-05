# INFO 7375 Computational Skepticism: glossary for the exam (causal inference terms)

**Status: DRAFT v0.1, 2026-11-05.** Written by Claude from the instructor's dictation. **The instructor has not signed it off.** Video links are placeholders: the instructor will add them.

## Executive summary

**What this is.** A glossary of terms you will meet when you read about causes, confounders and observational data. Each entry says what the term means, why it matters, and where to learn more.

**What it is not.** **None of these terms is on the exam, and no exam question asks you to define one.** The glossary is for your own time: the videos and readings are recommended, not required.

**What is on the exam (from the instructor's notes; to be confirmed).** Recognizing which variables in a described situation are confounders (a confounder is a predictor that affects both the treatment and the outcome); knowing what observational data means; the idea of controlling for a variable (compare within groups of similar people, then average across the groups); what randomization does; and the effect of a treatment as a degree of change in a chance.

**How to use it.** Look up a word when you run into it. The entries are in alphabetical order. A term in *italics* has its own entry.

## General reading

- Hernán and Robins, *Causal Inference: What If* (free online): https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/
- Pearl and Mackenzie, *The Book of Why*: https://bayes.cs.ucla.edu/WHY/
- Brady Neal, *Introduction to Causal Inference* (course): https://www.bradyneal.com/causal-inference-course

## The entries

### Adjustment set
**What it is.** The set of variables you control for so that what is left of the difference between treated and untreated people reflects the treatment's effect. Which set works depends on the *causal diagram*; the *backdoor criterion* is a test for it.
**Why it matters.** "Control for everything you have" is bad advice: controlling for a *mediator* or a *collider* can make an estimate worse.
**Where to learn more.** Video: [link to be added by the instructor]

### Backdoor criterion (and backdoor path)
**What it is.** A *backdoor path* is a route in a *causal diagram* from the treatment to the outcome that starts with an arrow *into* the treatment, such as website ← experience → interview. Association flows along it and can make a treatment look effective, or ineffective, even if it does nothing. A set of variables meets the **backdoor criterion** if it blocks every backdoor path and contains no effect of the treatment; then controlling for that set removes the confounding.
**Why it matters.** It gives a precise test for whether the variables you measured are enough to control for confounding.
**Where to learn more.** Video: [link to be added by the instructor]

### Causal diagram (DAG)
**What it is.** A picture in which each variable is a node and each arrow points from a cause to its effect, with no loops. It writes down your *assumptions* about how the variables are generated.
**Why it matters.** The data alone cannot tell you the arrows (see *identifiability*); the diagram makes the assumptions visible so others can check them.
**Where to learn more.** Video: [link to be added by the instructor]

### Collider
**What it is.** A variable with two arrows pointing into it: it is caused by two other variables. Controlling for a collider, or looking only at cases where it takes a particular value, can create an association between its causes that was not there before. Example: a scholarship awarded for being tutored or for high scores.
**Why it matters.** It is a reason not to control for everything. A collider is not a confounder.
**Where to learn more.** Video: [link to be added by the instructor]

### Consistency
**What it is.** The assumption that the outcome we see for a person who received a treatment is the outcome they would have had under that treatment, which needs the treatment to be well defined ("had a website" means one clear thing). It is usually listed together with *exchangeability* and *positivity* as the conditions for identifying a treatment's effect from observational data (see *identifiability*), and often with *interference*: the two together are called the stable unit treatment value assumption (SUTVA).
**Why it matters.** If the treatment is vague, an estimated effect has no clear meaning: "had a website" could mean a one-page résumé or a large portfolio, and the effect of each could differ.
**Not to be confused with.** The statistical idea that an estimator is *consistent* when it gets closer to the true value as the sample grows. That is a different use of the word.
**Where to learn more.** Video: [link to be added by the instructor]

### Counterfactual
**What it is.** What would have happened to the same person if the treatment had been different. We can never observe both versions for one person. It is the top rung of Pearl's ladder of causation.
**Why it matters.** Questions such as "would this applicant have been interviewed without the website?" are counterfactual, and they need assumptions beyond association.
**Where to learn more.** Video: [link to be added by the instructor]

### Do-operator (intervention)
**What it is.** Notation, do(X = x), for setting the treatment by force instead of observing it, as when everyone is *made* to get a referral. It separates "seeing" X from "doing" X.
**Why it matters.** Causal questions are about doing; observational data show only seeing, which is why a randomized assignment or an assumption is needed.
**Where to learn more.** Video: [link to be added by the instructor]

### Effect modification (interaction)
**What it is.** The treatment's effect differs between groups, for example a website helps applicants with little experience more than applicants with a lot.
**Why it matters.** It is not confounding. A single average effect can hide that the effect is large for some groups and small for others.
**Where to learn more.** Video: [link to be added by the instructor]

### Exchangeability
**What it is.** The treated and untreated groups are comparable: apart from the treatment, the untreated would have fared the same as the treated had they received it. Randomization gives it on average. When we control for confounders we are aiming for *conditional* exchangeability: comparable within each group of similar people.
**Why it matters.** It is the idea behind "comparing like with like".
**Where to learn more.** Video: [link to be added by the instructor]

### Frontdoor criterion
**What it is.** A way to estimate an effect even when the confounder was not measured, by following the effect through a measured variable that sits between the treatment and the outcome (a *mediator*). It holds only under strict conditions: the treatment must affect the outcome entirely through that variable, and the variable must not share unblocked common causes with the treatment.
**Why it matters.** It shows that unmeasured confounding is not always fatal, and how much has to be assumed to get around it.
**Where to learn more.** Video: [link to be added by the instructor]

### Identifiability
**What it is.** A causal effect is identifiable if, given your assumptions, it can be computed from the data you could collect. If it is not, no amount of data will settle it.
**Why it matters.** The two toy worlds with the hidden coin are the standard example: both give identical data, so the effect is not identifiable from observation alone. You need information about how the variables are generated, or an intervention. The usual conditions for identifying an effect from observational data are conditional *exchangeability* (no unmeasured confounding within groups), *positivity* and *consistency*, and in many settings the absence of *interference*.
**Where to learn more.** Video: [link to be added by the instructor]

### Instrumental variable
**What it is.** A variable that affects the treatment but affects the outcome only through the treatment, and shares no other causes with the outcome. It can let you estimate an effect despite unmeasured confounding. Example: a state grant that pays for officers' salaries and so changes how many officers a county hires.
**Why it matters.** It is the standard example of a variable that affects the treatment but is not a confounder.
**Where to learn more.** Video: [link to be added by the instructor]

### Interference
**What it is.** One person's treatment affects another person's outcome. The usual assumption is **no interference**: each person's outcome depends only on the treatment that person received. Together with *consistency* it is called the stable unit treatment value assumption (SUTVA). Examples where it fails: interview slots are limited, so when one applicant makes a website and wins a slot another applicant loses it; a vaccinated person protects the people around them; one student's tutoring shifts the grading curve for classmates.
**Why it matters.** With interference, comparing treated and untreated people does not measure one person's effect, because the untreated are also changed by other people's treatment (a spillover).
**Where to learn more.** Video: [link to be added by the instructor]

### Inverse probability weighting
**What it is.** Give each person a weight equal to one divided by the probability that they received the treatment they got, given their characteristics, so that the weighted treated and untreated groups look alike.
**Why it matters.** It is one way to control for many confounders at once without forming many small groups.
**Where to learn more.** Video: [link to be added by the instructor]

### Matching
**What it is.** Pair each treated person with a similar untreated person and compare within the pairs.
**Why it matters.** It is a direct way to compare like with like, an alternative to *stratification*.
**Where to learn more.** Video: [link to be added by the instructor]

### Mediator
**What it is.** A variable on the path from treatment to outcome: treatment → mediator → outcome. Example: the number of tutoring sessions attended.
**Why it matters.** It is part of *how* a treatment works, not a confounder. Controlling for it removes part of the effect you are trying to measure.
**Where to learn more.** Video: [link to be added by the instructor]

### Positivity (overlap)
**What it is.** Within every group of similar people, some receive the treatment and some do not. Every kind of person you want to compare has a chance of both.
**Why it matters.** If every highly experienced applicant has a website, there is nobody without one to compare against in that group, and *stratification* has nothing to compare there.
**Where to learn more.** Video: [link to be added by the instructor]

### Propensity score
**What it is.** The probability that a person receives the treatment given their characteristics. It squeezes many confounders into one number, used to match, weight or stratify.
**Why it matters.** It makes controlling for many variables manageable.
**Where to learn more.** Video: [link to be added by the instructor]

### Simpson's paradox
**What it is.** A trend that appears in every group reverses, or disappears, when the groups are combined. It often comes from a confounder that makes the groups very different in size or make-up.
**Why it matters.** It is the clearest warning that overall averages can mislead.
**Where to learn more.** Video: [link to be added by the instructor]

### Standardization
**What it is.** Combining the within-group effects (or rates) into one number using the weights of a chosen reference population, such as the overall mix of groups, so that the comparison does not depend on how the groups happen to be mixed. It is the "average across the groups" step in controlling for a confounder. Demographers use it too, for example in age-standardized death rates.
**Why it matters.** It lets you compare fairly when groups have different make-ups.
**Where to learn more.** Video: [link to be added by the instructor]

### Stratification
**What it is.** Split the data into groups (strata) of people who are similar on a variable, such as little, moderate or a lot of experience; compare treated and untreated people within each group; then combine the results (see *standardization*).
**Why it matters.** It is the simplest way to control for a confounder. Its limits: too many strata leave few people in each, and it needs *positivity*.
**Where to learn more.** Video: [link to be added by the instructor]
