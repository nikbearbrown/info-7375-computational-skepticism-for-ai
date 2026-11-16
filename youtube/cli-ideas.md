# Computational Skepticism for AI — CLI Video Ideas ("X with Claude")

## Assignment crosswalk (read first)

Every build below is also a **graded-assignment scaffold** — the same instrument the course assesses,
run on camera. The four assignments these map to:

- **A1 — The Agentic Casebook: Red-Team One System** (100 pts, AUDIT). Pick one real agentic system, run
  three of the book's ten lenses on it, name who owns each break. These builds *demonstrate the lens* a
  student then applies to their own Pebble.
- **A2 — Build It, Then Break It: A Skeptic's Portfolio** (100 pts, BUILD). Build a small artifact, then
  turn two of six instruments on *your own* work. Several builds below *are* the instrument's deliverable
  (an actual reliability diagram, a probe suite, a fairness-impossibility computed on real numbers).
- **PR25 — Progress Report** (25 pts, brutalist explainer video) toward the capstone: the `/v0` scope, the
  verified-data plan, phase gates, one uncut real run.
- **CAP250 — A Working Professional Contribution to the Reallocation Engine** (250 pts). Several builds
  below map to a *named contribution* (a calibration-curve harness, a gate-behavior test harness, an
  entity-resolver, an output linter).

Quick map:

| Build | Serves | The move it teaches |
|---|---|---|
| 01 Calibration Curve Auditor | **A2** (calibration instrument) · **CAP250** (calibration-curve harness) · A1 Ch2 | discrimination ≠ calibration; catch the decorative number |
| 02 Base-Rate Bayes Calculator | **A1** Ch2 lens · A2 uncertainty | price a confidence number against its base rate |
| 03 Fairness Impossibility | **A2** (bias/fairness instrument) · **A1** Ch7 lens | the impossibility, on your own numbers |
| 04 Adversarial Perturbation | **A2** (robustness probe) · **A1** Ch4 lens | the proxy the model actually learned |
| 05 Agent Self-Verification Failure | **A1** Ch8 lens (false-success) | the report-vs-world gap that defines agentic failure |
| 06 Distribution Shift (PSI) | **A2** (robustness / shifted re-plot) · A1 Hume lens | confidence is about the record, not the world |
| 07 Confusion Matrix Audit | **A1** four-moves (Popper) · A2 build-note | specify what failure looks like *before* the result |
| 08 Prompt Sensitivity Tester | **A2** (robustness probe suite) · **A1** Ch4 lens | prompt sensitivity = adversarial robustness for LLMs |
| 09 Gate-Behavior Test Harness | **CAP250** (named contribution) · A1 Ch8/Ch9 | a gate zeroes the composite — it is not a vote |
| 10 Entity-Resolution Matcher | **CAP250** (named contribution) | before/after join-coverage; flip "Unknown" into a tier |
| 11 Verified-Data Output Linter | **CAP250** (attestation) · **A1** Ch11 verb audit | flag unsourced sentences + over-warranted verbs |
| 12 Reliability Diagram On *Your* Model | **A2** (the calibration deliverable) | the 25-pt instrument report, on your own build |
| 13 The Prediction-Lock Harness | **A1 + A2** (the honesty floor) | a prediction you can edit is worth nothing |

**House rule for the assignment-native builds (09–13):** they follow the same beat structure as 01–08
(Hook · artifact · prompt seed · read/check · human supplies · output medium · the change · teardown ·
exclusions · score) and add an **Assignment tie-in** line naming the exact rubric component they produce.

---

## Candidate 01 — Build a Calibration Curve Auditor with Claude Code
- Source: computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Assignment tie-in: **A2** — this is the *Calibration (Ch 2 + Ch 11)* instrument, the exact deliverable (reliability diagram + Brier + ECE + temperature scaling). **CAP250** — a *calibration-curve harness for the sponsorship scorer* is a named contribution. **A1** — the concept behind the Ch 2 base-rate lens.
- Hook: A classifier returns 0.94, 0.91, 0.88 — a column of confident numbers that looks done. But does 0.94 mean 94% of cases scored 0.94 are actually positive? The calibration curve answers that. Most deployed models never show it.
- The artifact: A Python script (~40 lines) that loads a binary classifier's predicted probabilities and ground truth labels (or generates synthetic data), bins predictions into deciles, computes the empirical positive rate per bin, and renders a Manim animation of the calibration curve vs. the perfect-calibration diagonal — highlighting the overconfidence zone where the model's probability exceeds the empirical rate.
- Prompt seed: `claude "Write a Python script that: (1) generates synthetic binary classification data with 1000 samples, true positive rate 0.15, using sklearn.datasets.make_classification; (2) trains a logistic regression and a random forest; (3) computes calibration curves (sklearn.calibration.calibration_curve, n_bins=10) for each; (4) plots both curves vs. the perfect-calibration diagonal; (5) prints the Brier score for each model. Label which model is overconfident and which is underconfident."`
- Read / check: Verify that the random forest is overconfident (common in practice — outputs cluster near 0 and 1). Check that the Brier score is lower for the better-calibrated model. Confirm that the calibration curve x-axis is mean predicted probability per bin and y-axis is fraction of positives.
- Human supplies: sklearn-capable Python environment. For a richer OUTPUT beat, the human can substitute a real classifier's predictions (e.g., a pre-trained model's output on a held-out test set) — but synthetic data is fully acceptable.
- Output medium: Manim (animated) — the perfect-calibration diagonal draws first; then the two model curves animate in; the overconfidence gap (model says 0.9, empirical rate is 0.6) fills with a shaded region; Brier scores annotate each curve.
- The change: Apply Platt scaling (logistic regression on the raw scores) to the overconfident model. Re-plot the calibration curve. Show the overconfidence gap closing.
- Teardown angle: A high-AUC model can be systematically overconfident — its ranking is correct but its probability estimates are wrong. Calibration and discrimination are independent properties. Deploying on the score alone is a confidence illusion.
- Exclusions: Isotonic regression calibration, full Bayesian calibration, reliability diagrams for multi-class.
- Score: 9/10

## Candidate 02 — Build a Base-Rate Bayes Calculator with Claude Code
- Source: computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Assignment tie-in: **A1** — this *is* the Ch 2 lens (find the system's confidence number, find the real base rate, run Bayes on one flag, state the Popperian falsification condition). **A2** — supports the calibration/uncertainty instrument.
- Hook: A sepsis model fires on 18% of all hospitalized patients — but only 1–2% of hospitalized patients have sepsis. A positive alert has only a 9% chance of being a true positive. The math is Bayes' theorem applied to base rates — and almost no clinician runs it.
- The artifact: A ~25-line Python script that computes P(disease | positive test) via Bayes' theorem across a grid of base rates (0.1%–20%) and sensitivities (70%–99%), then renders a Manim heatmap animation where the posterior probability surface shows how catastrophically it collapses at low base rates — even for high-sensitivity tests.
- Prompt seed: `claude "Write a Python function bayes_ppv(prevalence, sensitivity, specificity) that returns the positive predictive value using Bayes' theorem. Then compute a 10x10 grid: prevalence from 0.001 to 0.20 (10 steps) and sensitivity from 0.70 to 0.99 (10 steps), holding specificity=0.82 (the sepsis model's published value). Print as a pandas DataFrame with prevalence as rows and sensitivity as columns. Highlight cells where PPV < 0.10 with a marker."`
- Read / check: Verify the formula: PPV = (sensitivity × prevalence) / (sensitivity × prevalence + (1−specificity) × (1−prevalence)). At prevalence=0.02, sensitivity=0.82, specificity=0.82: confirm PPV ≈ 0.09 (9%). Check that the heatmap has its lowest values at low prevalence, not at low sensitivity.
- Human supplies: Nothing — fully synthetic. The sepsis model parameters come from Wong et al. 2021 JAMA Internal Medicine (stated in the chapter).
- Output medium: Manim (animated) — the heatmap populates cell by cell; a threshold line at PPV=0.10 draws across; the entire left column (low base rate) lights up red; a callout shows the sepsis model's specific operating point.
- The change: Vary specificity from 0.70 to 0.99 and fix sensitivity=0.82. Show that improving specificity has a much larger effect on PPV at low prevalence than improving sensitivity.
- Teardown angle: The confidence the model radiates is a property of the model's training — it has no access to the base rate of the deployment population. The base rate is the most important number in the deployment context and the one the model cannot know.
- Exclusions: ROC curve construction, F1 score, multi-class confusion matrices.
- Score: 9/10

## Candidate 03 — Build a Fairness Impossibility Demonstrator with Claude Code
- Source: computational-skepticism-for-ai/chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Assignment tie-in: **A2** — the *Bias & fairness (Ch 6 + Ch 7)* instrument: show the impossibility on your own numbers, then write a defended choice. **A1** — the Ch 7 lens (surface a values decision the system made silently).
- Hook: Three fairness definitions — demographic parity, equalized odds, calibration parity — each sound reasonable. Chouldechova 2016 proved you cannot satisfy all three when base rates differ. Build the arithmetic proof in four lines of Python.
- The artifact: A ~50-line Python script that constructs a binary classifier scenario with two groups (base rates 0.6 and 0.3), computes all three fairness metrics, and demonstrates algebraically why achieving calibration forces a violation of equalized odds. Then renders a Manim triangle diagram where the three fairness criteria are nodes and a red X sweeps the impossible combination.
- Prompt seed: `claude "Write a Python script that demonstrates the Chouldechova fairness impossibility. Set up a binary classifier: group A base rate 0.6, group B base rate 0.3. Assume a calibrated classifier (PPV equal across groups). Compute the implied true-positive rate and false-positive rate for each group. Show numerically that equalizing TPR and FPR simultaneously (equalized odds) is impossible when base rates differ. Print all computed values and the violation clearly."`
- Read / check: Verify the identity (v/(1-v)) = (p/(1-p)) × (t/f) holds for each group. Confirm that calibration forces PPV equality. Check that the TPR/FPR ratio difference follows from the base rate ratio. The numerical example should match Chouldechova 2017's algebra within rounding.
- Human supplies: Nothing — fully synthetic. The base rates and parameters come directly from the chapter's worked example.
- Output medium: Manim (animated) — a triangle with three nodes (DP, EO, CP); red X marks appear as each combination is tested; a table populates showing the forced violation; the arithmetic identity animates in as the explanation.
- The change: Test demographic parity as a fourth constraint. Show that adding it violates at least one of the other two. Then show the only degenerate escape: equal base rates (set p_A = p_B = 0.3 and confirm all three can be simultaneously satisfied).
- Teardown angle: The engineer who "just optimizes" is still choosing — whatever loss function they use embeds a values claim about which fairness criterion to sacrifice. Making that choice invisible does not make it neutral.
- Exclusions: Individual fairness (Lipschitz condition), counterfactual fairness, full COMPAS case history beyond the illustration.
- Score: 9/10

## Candidate 04 — Build an Adversarial Perturbation Detector with Claude Code
- Source: computational-skepticism-for-ai/chapters/04-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Assignment tie-in: **A2** — the *Robustness probe (Ch 4)* instrument: a break that reveals the proxy, framed features-not-bugs. **A1** — the Ch 4 lens on someone else's system.
- Hook: A pixel-level perturbation invisible to the human eye flips a panda classifier to "gibbon" at 99.9% confidence. The model did not break — it was honest about what it learned. Can you build the perturbation and see it happen?
- The artifact: A Python script (~60 lines) using PyTorch + torchvision that: loads a pretrained ResNet-50, runs the Fast Gradient Sign Method (FGSM) on a sample image with ε=0.01, shows the original prediction and the adversarial prediction, and renders a Manim three-panel animation: original image | perturbation (amplified ×50) | adversarial image, with confidence scores animating under each.
- Prompt seed: `claude "Write a Python script using PyTorch and torchvision that: (1) loads pretrained ResNet-50; (2) downloads a sample ImageNet image of a panda from a URL or uses torchvision's sample data; (3) runs FGSM with epsilon=0.01 using the cross-entropy loss gradient w.r.t. the input; (4) prints the top-3 predicted classes and confidence scores for both the original and adversarial images; (5) saves the perturbation tensor amplified 50× as a PNG. No training required."`
- Read / check: Verify the original image is classified correctly (panda). Verify the adversarial image changes class with high confidence. Confirm ε=0.01 is visually imperceptible (pixel values shift by <3/255). Check that FGSM uses sign(∇_x L), not the raw gradient.
- Human supplies: PyTorch environment with torchvision. A sample panda image URL or local file. Screen-recording of the terminal during the script run (the class flip is the authentic OUTPUT beat). The perturbation PNG can serve as a slate if the Manim render is not built.
- Output medium: Manim (animated) — three panels: original image, amplified perturbation heatmap, adversarial image. Confidence bars below each animate in. A label "model sees: panda → gibbon" appears with an arrow.
- The change: Increase ε from 0.01 to 0.1. Show that at ε=0.1 the perturbation becomes slightly visible (image looks "noisy") but the confidence in the wrong class increases further. Annotate the accuracy-robustness trade-off numerically.
- Teardown angle: The model did not fail — it succeeded at what it was trained to do (match statistical patterns in pixel space). The problem is that those patterns diverge from the semantic categories humans use. Adversarial examples reveal the proxy, not a bug.
- Exclusions: PGD attacks, adversarial training as a defense, certified robustness, ℓ₂ vs. ℓ∞ norm comparison.
- Score: 8/10

## Candidate 05 — Build an Agent Self-Verification Failure Demo with Claude Code
- Source: computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Assignment tie-in: **A1** — the *Agentic false-success (Ch 8)* lens made runnable: the agent says done, the world disagrees, and self-verification confirms the error. This is the beating heart of the AUDIT — check the world, not the artifact.
- Hook: Ash's agent reported the email was deleted. It wasn't. The agent re-prompted itself to verify and confirmed the deletion again. This is not a quirk — it is what self-verification *is* for a system that retrieves from its own distribution.
- The artifact: A Python script using the Anthropic SDK that: (1) asks Claude to solve a known-hard reasoning puzzle (Game of 24 with a deliberately wrong seed); (2) captures the wrong answer; (3) asks Claude to verify its own answer; (4) shows whether the verification catches the error or confirms it. Renders a Manim two-panel: the ASK beat on the left (question → answer), the VERIFY beat on the right (same question → confirmation or correction).
- Prompt seed: `claude "Write a Python script using the Anthropic SDK that runs two API calls to claude-3-5-haiku: (1) ASK: 'Using 3, 3, 8, 8 with +−×÷ and each number exactly once, make 24.' (2) VERIFY: 'You previously answered [paste answer]. Verify this is correct by checking the arithmetic step by step.' Print both responses. Count how many times the model confirms a wrong answer vs. catches it."`
- Read / check: Run the script 5 times. Record how often the verification catches the error vs. confirms the wrong answer. A correct verification rate well below 100% supports the chapter's claim. Note: this is an empirical test — the result may vary.
- Human supplies: Anthropic API key. Screen-recording of the terminal (the five runs, the confirmation pattern printing) is the authentic OUTPUT beat.
- Output medium: Screen-recording mp4 of the terminal — five run outputs printing sequentially, a tally line at the end: "Caught: X/5, Confirmed wrong: Y/5."
- The change: Replace the VERIFY prompt with one that forces the model to check against a deterministic calculator: "Evaluate [expression] using Python's eval() to verify." Show whether tool-augmented verification catches more errors. This is the CHANGE beat that shows tool use relocating rather than eliminating the problem.
- Teardown angle: Self-verification is more retrieval against the same distribution that produced the error. It is not a fundamentally different operation — it is the same operation applied to its own output. Tool-augmented verification works because the tool (Python eval) is outside the probabilistic stack.
- Exclusions: Full Stechly et al. 2024 benchmark replication, multi-step planning tasks, agentic execution beyond the two-call demo.
- Score: 8/10

## Candidate 06 — Build a Distribution Shift Detector with Claude Code
- Source: computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Assignment tie-in: **A2** — the *Robustness probe* distribution-shift probe and the "re-plot on a shifted slice" move; the PSI table *is* a robustness profile's monitoring column. **A1** — the Hume lens (is this confidence about the world or only the record so far?).
- Hook: The turkey was fed for 999 days. Hume's problem: the model's confidence is a property of the model, not the world. Population Stability Index (PSI) is the industry-standard tool for catching when a model's training distribution has drifted away from the current population.
- The artifact: A Python script that computes PSI between a training-time feature distribution and a deployment-time distribution (synthetic or real), renders a Manim bar chart animation where each feature's PSI value grows; features with PSI > 0.2 (major drift) are flagged in red and trigger a "retrain alert."
- Prompt seed: `claude "Write a Python function psi(expected, actual, buckets=10) that computes the Population Stability Index between two numeric distributions. Use equal-width bucketing on the training distribution. PSI = sum((actual_pct - expected_pct) * ln(actual_pct / expected_pct)). Generate: a training distribution N(0,1) with 5000 samples and three deployment distributions: no shift N(0,1), moderate shift N(0.5, 1), major shift N(1.5, 1.2). Print PSI for each and flag >0.2 as 'major drift'."`
- Read / check: Verify PSI ≈ 0 for no-shift case, PSI ≈ 0.1 for moderate, PSI > 0.25 for major drift. Confirm the formula uses natural log and the correct PSI threshold conventions (0.1 = minor, 0.2 = major). Check that bucketing is on the training distribution, not the combined.
- Human supplies: Nothing — fully synthetic. No live data required.
- Output medium: Manim (animated) — three horizontal bar charts growing left to right (one per scenario); a threshold line at PSI=0.2 draws; the major-drift bar turns red and a "retrain alert" label pulses.
- The change: Apply PSI to five features simultaneously. Show which features drift most. Add a composite "model risk score" that averages PSI across features. This is the CHANGE beat that extends the single-feature demo to a realistic monitoring dashboard.
- Teardown angle: The model's confidence did not update when the distribution shifted — it cannot update, because it has no mechanism for detecting that the world changed. PSI is the external check the model cannot perform on itself.
- Exclusions: Covariate shift vs. concept drift distinction, KL divergence as an alternative, domain adaptation methods.
- Score: 8/10

## Candidate 07 — Build a Confusion Matrix Audit Pipeline with Claude Code
- Source: computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md + LLM Exercise (Popperian falsifiability applied to model metrics)
- Lane: BUILD (Claude Code)
- Assignment tie-in: **A1** — the four classical moves, specifically *Popper*: state what failure looks like before the result means anything. **A2** — models the build note's pre-registered suspect (name the failure mode before you probe).
- Hook: "The model achieves 94% accuracy" — what would it look like if it were *bad*? Popper's move: you must specify what failure looks like before the result means anything. A confusion matrix makes failure visible in a way that accuracy cannot.
- The artifact: A Python script that trains a classifier on imbalanced data (e.g., 5% positive class), computes the full confusion matrix, and renders a Manim animation of the confusion matrix cells filling in with counts and rates — showing that a 95%-accurate model achieves this by predicting "negative" for nearly every case (a trivial classifier).
- Prompt seed: `claude "Write a Python script using sklearn that: (1) generates imbalanced binary data: 9500 negatives, 500 positives, 20 features; (2) trains a logistic regression AND a DummyClassifier(strategy='most_frequent'); (3) computes confusion matrices for both; (4) prints accuracy, precision, recall, F1, and the full confusion matrix for each. Label which model is the 'trivial' one."`
- Read / check: Verify that the DummyClassifier achieves ~95% accuracy (9500/10000). Confirm its recall on the positive class is 0% — it catches no positives. Verify the logistic regression has lower accuracy but materially higher recall. Check that F1 scores correctly reflect the trade-off.
- Human supplies: sklearn environment. Nothing else required.
- Output medium: Manim (animated) — two 2×2 confusion matrix grids animate in side by side: DummyClassifier (all mass in TN cell) and LogReg (spread across all four cells). Recall bars appear below each. A label "same accuracy, opposite purpose" appears.
- The change: Set the positive-class weight to 10× in the logistic regression. Show how the confusion matrix shifts toward higher recall at the cost of more false positives. Then ask: which error is worse in this domain? That question cannot be answered by the math.
- Teardown angle: Accuracy is a rhetorical claim compatible with any outcome when the class distribution is imbalanced. The Popperian move is to specify, before deployment, what failure looks like — and the confusion matrix is that specification made visible.
- Exclusions: ROC-AUC construction, precision-recall curves, cost-sensitive learning frameworks.
- Score: 8/10

## Candidate 08 — Build an LLM Prompt Sensitivity Tester with Claude Code
- Source: computational-skepticism-for-ai/chapters/04-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Assignment tie-in: **A2** — the *Robustness probe* prompt-sensitivity probe, named directly in the assignment's probe suite. **A1** — the Ch 4 lens applied to an LLM-based Pebble.
- Hook: Adversarial robustness in image classifiers and prompt sensitivity in LLMs share the same structure: a small, semantically invisible perturbation flips the output. Is Claude's answer to a legal question the same if you add one sentence of context?
- The artifact: A Python script using the Anthropic SDK that sends 10 semantic variants of the same question (varying phrasing, added context, reordered sentences) to claude-3-5-haiku, extracts the key claim from each response, and computes a pairwise agreement score. Renders a Manim heatmap of the 10×10 agreement matrix with the diagonal highlighted.
- Prompt seed: `claude "Write a Python script using the Anthropic SDK that sends 10 prompt variants of 'What is the standard statute of limitations for a personal injury claim in the United States?' to claude-3-5-haiku. Variants should differ only in phrasing, added context sentences, or ordering — not in core question. For each response, extract the stated time period (a number of years). Print a 10×10 agreement matrix: entry (i,j) = 1 if response i and j give the same time period, 0 otherwise. Print the agreement rate."`
- Read / check: Verify the 10 prompt variants are semantically equivalent (no substantive change). Check that the extraction logic handles "2 years," "two years," "24 months" as equivalent. Confirm the agreement matrix is symmetric. A perfect-agreement result (10/10) is informative; so is any variation.
- Human supplies: Anthropic API key. Screen-recording of the terminal (10 API calls returning, matrix printing) is the authentic OUTPUT beat.
- Output medium: Screen-recording mp4 of the terminal, optionally supplemented by a Manim heatmap of the agreement matrix if variation is found.
- The change: Repeat with a deliberately misleading added sentence: "Note: statutes of limitations have been extended recently." Record whether the adversarial context shifts the model's stated answer. This is the LLM analog of the FGSM perturbation.
- Teardown angle: LLM prompt sensitivity is the NLP instance of adversarial robustness. The model is not using "the correct answer" — it is sampling from a distribution conditioned on all the tokens in the prompt, including irrelevant ones.
- Exclusions: Formal adversarial NLP (TextFooler, BERT-attack), jailbreaking, red-teaming for safety.
- Score: 7/10

---

## Assignment-native builds (09–13) — the deliverable *is* the video

These map to a specific rubric component. A student who builds one on camera has produced a gradeable
artifact, not just an illustration.

## Candidate 09 — Build a Gate-Behavior Test Harness with Claude Code
- Source: the-reallocation-engine/chapters/16-the-build-and-the-honest-run.md + 11-the-bayesian-role-scorer.md; computational-skepticism-for-ai/chapters/09-delegation-trust-and-the-supervisory-role.md
- Lane: BUILD (Claude Code)
- Assignment tie-in: **CAP250** — a *gate-behavior unit-test harness* is a named contribution (high value, tight scope). **A1** — the Ch 8/Ch 9 lens: a gate with no failure path is decoration; prove the handoff condition is testable.
- Hook: A scoring pipeline has a "liveness gate" and a "visa-timeline gate." A gate is supposed to *zero* the composite when it fails — not shave a few points off. Most pipelines quietly treat their gates as votes. One unit test tells them apart.
- The artifact: A ~50-line pytest harness that feeds a scorer three fixtures — a live role that passes, a dead posting that must be gated, and a role past the OPT window that must be gated — and asserts the composite score is exactly 0 (not merely lower) whenever a gate fails. It fails loudly on a gate-as-vote implementation and passes on a correct one.
- Prompt seed: `claude "Write a pytest suite for a job-scoring function score(role) that must treat two conditions as hard gates: posting_live == False and months_to_start > opt_window. Write three fixtures (live+in-window; dead posting; past OPT window). Assert that score()==0 whenever either gate fails, and score()>0 only when both pass. Include one intentionally wrong 'gate-as-vote' implementation and show the suite failing on it, then the correct implementation passing."`
- Read / check: Confirm the suite FAILS on the vote-style scorer (it returns a nonzero score for a dead posting) and PASSES on the gate-style scorer. Verify the assertion is `== 0`, not `< threshold`. This is the capstone's named build failure, caught by a test.
- Human supplies: A Python env with pytest. The real scorer from the engine repo for a live OUTPUT beat (or the two toy implementations for a self-contained demo). Screen-record the red-then-green test run.
- Output medium: Screen-recording mp4 of the terminal — the suite runs red on the vote implementation, the fix lands, the suite runs green. Onda code-block of the one assertion that carries the whole test.
- The change: Add a fixture where liveness is *unknown* (the checker errored, not "returned empty"). Assert the scorer refuses to produce a score rather than guessing — the stop condition. This is EMPTY-vs-ERROR made executable.
- Teardown angle: "It looks done" is not a handoff condition. A gate is a claim with a testable failure path, and the only way to know your gate is a gate and not a vote is to write the test that fails when it degrades to a vote.
- Exclusions: Full engine integration, property-based testing frameworks, CI wiring.
- Score: 9/10

## Candidate 10 — Build an Employer-Name Entity Resolver with Claude Code
- Source: the-reallocation-engine/chapters/05-verifying-the-data.md + 07-who-sponsors-the-80-days-sponsorship-scorer.md
- Lane: BUILD (Claude Code)
- Assignment tie-in: **CAP250** — an *entity-resolution / employer-name-matching module* is a named contribution; it flips artifact-"Unknown" sponsorship tiers into real ones and must emit before/after join-coverage counts.
- Hook: "Acme, Inc." in the visa data and "ACME Incorporated" in the funding data are the same company — and a naive join misses it, so the candidate sees "sponsorship: Unknown" for a firm that sponsors every year. The fix is boring string normalization, and it is worth more coverage than any model.
- The artifact: A ~70-line Python module that normalizes employer names (case, punctuation, legal suffixes like Inc/LLC/Corp/Ltd), joins two small fixture tables (a DOL-style list and an SEC-style list), and **prints before/after join-coverage counts plus a sample of rescued rows**. Fuzzy matching above the exact-normalized tier is gated behind an explicit `--allow-fuzzy` flag that prints a human-review prompt.
- Prompt seed: `claude "Write a Python module normalize_employer(name) that lowercases, strips punctuation, and removes legal suffixes (inc, llc, corp, ltd, co, incorporated, limited). Then join two CSV fixtures on the normalized name: dol_sponsors.csv and sec_fundings.csv. Print: rows matched before normalization, rows matched after, the delta, and 5 example rows that were rescued by normalization. Do NOT enable fuzzy matching unless a --allow-fuzzy flag is passed; if it is, print each fuzzy match as a 'needs human confirmation' line rather than auto-accepting."`
- Read / check: Verify the before/after counts are real counts from the fixtures, not asserted. Confirm the rescued-rows sample actually differs only by suffix/case. Confirm `--allow-fuzzy` never auto-accepts — it only proposes. This is the verified-data contract in miniature: every number traces.
- Human supplies: Two small fixture CSVs (can be synthetic but structurally real). Screen-record the coverage delta printing.
- Output medium: Screen-recording mp4 of the terminal — the before/after coverage numbers and the rescued-rows sample. Optional Manim: two columns of names collapsing into matched pairs.
- The change: Turn on `--allow-fuzzy` and show a false positive it proposes (two genuinely different firms with similar names). Narrate why fuzzy matching must never run without a human sign-off — the false join would greenlight the wrong company.
- Teardown angle: The highest-leverage fix in an evidence system is often not the model — it is the join. But a join that fabricates matches to look complete is worse than one that honestly reports "Unknown." Coverage you can't trace is not coverage.
- Exclusions: Full record-linkage frameworks (dedupe, splink), embedding-based matching, production DOL/USCIS/SEC ingestion.
- Score: 9/10

## Candidate 11 — Build a Verified-Data Output Linter with Claude Code
- Source: the-reallocation-engine/chapters/03-the-verified-data-contract.md; computational-skepticism-for-ai/chapters/11-communicating-uncertainty-calibrating-claims-to-evidence.md
- Lane: BUILD (Claude Code)
- Assignment tie-in: **CAP250** — supports the *verified-data attestation* (flag any number that doesn't trace to a record). **A1** — the Ch 11 verb-audit lens made automatic. **PR25** — a fast check for the progress report's record-vs-inference boundary.
- Hook: The verified-data contract says never invent a count, a rate, or a coverage number. But how do you catch a fabricated number in a 400-line report? You lint for it: a sentence that states a figure with no citation, or a verb that outruns its evidence.
- The artifact: A ~60-line Python linter that scans a markdown report for two smells — (1) a sentence containing a number/percentage with no adjacent source tag or citation, and (2) an over-warranted verb from the taxonomy (`proves`, `demonstrates`, `shows`) not backed by a linked figure — and prints a line-numbered report of flagged sentences with the licensed downgrade.
- Prompt seed: `claude "Write a Python script that reads a markdown file and flags two things: (1) any sentence containing a digit or percent sign that has no citation marker ([n], (source), or a nearby 'per <file>') — print it as UNSOURCED NUMBER; (2) any sentence using the verbs proves/demonstrates/shows/conclusively without a linked figure or table — print it as OVER-WARRANTED VERB and suggest the downgrade (show->suggest, proves->is consistent with). Print line numbers and a summary count."`
- Read / check: Run it on a report you wrote. Verify it flags a real unsourced number (not false-positive on years/section numbers). Confirm the verb list matches the chapter's taxonomy (hypothesize → suggest → observe → find → show → demonstrate → conclude → prove). A clean report should pass; a fabricated one should light up.
- Human supplies: A markdown report to lint (their own capstone draft is the authentic input). Screen-record the linter flagging real lines.
- Output medium: Screen-recording mp4 of the terminal — flagged lines printing with line numbers and suggested downgrades. Onda code-block of the two regexes.
- The change: Add a `--strict` mode that exits non-zero if any unsourced number is found — wire it as a pre-commit hook so a report with a fabricated number cannot be committed. This is the honesty floor made mechanical.
- Teardown angle: The verified-data contract is enforceable, not just aspirational. A number without a traceable source and a verb without evidence are the two shapes fabrication takes — and both are detectable before a human ever reads the report.
- Exclusions: Full NLP claim-extraction, LLM-based fact-checking, citation-graph validation.
- Score: 8/10

## Candidate 12 — Build the Reliability Diagram for YOUR Own Model with Claude Code
- Source: computational-skepticism-for-ai/chapters/02 + 11; the BUILD assignment's Calibration instrument
- Lane: BUILD (Claude Code)
- Assignment tie-in: **A2** — this is the *instrument report itself* (25 pts): a reliability diagram + ECE + Brier + temperature scaling + a shifted-distribution re-plot, computed on the student's *own* artifact. Candidate 01 teaches the concept on synthetic data; this one produces the graded deliverable on a real build.
- Hook: You trained a small classifier this week. It reports confidence. You have never checked whether that confidence means anything. Before you probe anything else, plot your own reliability diagram — and predict your ECE before you compute it.
- The artifact: A ~50-line script that takes the student's *own* model's held-out predictions + labels, bins by stated confidence, plots the reliability diagram vs. the diagonal, computes **ECE and Brier**, fits **temperature scaling**, and **re-plots on a deliberately shifted slice** of the student's data — the beat that exposes a decorative confidence number.
- Prompt seed: `claude "I have a trained classifier and a held-out set. Write a script that loads my predictions.csv (columns: predicted_prob, true_label), bins into 10 confidence bins, plots the reliability diagram against the diagonal, computes ECE and Brier score, fits temperature scaling on a validation split, and re-plots. Then take the subset of rows where feature X is above its median as a 'shifted slice' and recompute ECE on that slice. Print both ECE values and label which regime the model is overconfident in."`
- Read / check: The prediction-lock: write your guessed ECE *before* running. Verify the diagram is computed from your real predictions (the honesty floor — a diagram not computed from real predictions is a zero). Confirm ECE rises on the shifted slice if the model is fragile.
- Human supplies: **Their own model's predictions** — this is the point; synthetic data does not earn the A2 component. Screen-record the two ECE numbers printing and the gap between the guessed and true ECE.
- Output medium: Two reliability-diagram plots (in-distribution and shifted), an ECE/Brier table, the temperature-scaled re-plot. Screen-capture of the run for the honest-run beat.
- The change: Apply temperature scaling and show the in-distribution ECE fall — then show it barely moves on the shifted slice. Calibration on your training distribution does not survive a distribution shift; say so.
- Teardown angle: You are the least reliable auditor of your own model's confidence, because you made it. The reliability diagram is the instrument that makes your own overconfidence visible — and the shifted slice is where the decorative number gets caught.
- Exclusions: Isotonic regression, multi-class calibration, conformal prediction (a separate Ch 11 beat).
- Score: 9/10

## Candidate 13 — Build the Prediction-Lock Harness with Claude Code
- Source: computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md (the prediction-lock / Frictional method); both 100-pt assignments
- Lane: BUILD (Claude Code)
- Assignment tie-in: **A1 + A2** — the *prediction-lock* is a graded honesty component in both (10 pts: "predictions on the record before probing"). This harness makes an unlocked prediction impossible to backfill.
- Hook: A prediction you can edit after the result is worth nothing — the sentence slides to meet the outcome and the gap that could have taught you collapses to zero. So take the edit away: hash and timestamp the prediction before you look.
- The artifact: A ~30-line CLI that takes a written prediction, stamps it with a timestamp and a SHA-256 hash, and writes it to an append-only log; a second command records the observed outcome and prints the prediction, the outcome, and whether the hash still verifies (proving the prediction wasn't edited after the fact).
- Prompt seed: `claude "Write a Python CLI predlock with two subcommands: (1) 'lock <text>' — appends {utc_timestamp, text, sha256(text)} as a JSON line to predlock.log and prints the hash; (2) 'resolve <hash> <outcome_text>' — finds the locked prediction by hash, appends the outcome with its own timestamp, and prints prediction vs. outcome side by side plus 'HASH VERIFIED' if the stored text still hashes to the given hash. Never allow editing a locked line."`
- Read / check: Lock a prediction, try to edit the log line, then resolve — confirm the hash no longer verifies if the text was tampered with. This is the mechanism behind the graded honesty line: a surprise you predicted against beats a confirmation you assumed.
- Human supplies: Nothing — self-contained. Screen-record locking a prediction before a probe (e.g., before running Candidate 12), then resolving it after.
- Output medium: Screen-recording mp4 of the terminal — lock (hash prints), the probe runs, resolve (prediction vs. outcome, HASH VERIFIED). A clean, tiny demo that pairs with any other candidate as its opening beat.
- The change: Wire `predlock lock` as the first line of your instrument scripts so no probe runs without a locked prediction. The prediction-lock stops being a rule you remember and becomes a step you can't skip.
- Teardown angle: The information in an audit lives in the gap between prediction and outcome. Leave the prediction editable and the gap collapses to zero — you learn nothing and the grade knows it. The lock is cheap; the honesty it buys is the whole point.
- Exclusions: Cryptographic signing/PKI, blockchain timestamping, multi-user attestation.
- Score: 8/10
