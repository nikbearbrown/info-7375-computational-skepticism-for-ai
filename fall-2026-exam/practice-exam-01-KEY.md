# INFO 7375 Computational Skepticism for AI: Fall 2026 practice exam 01: ANSWER KEY

**Read this only after you have finished the matching exam, [practice-exam-01.md](practice-exam-01.md).** Practice only; the real exam uses different cases and questions.

How cases are scored: catches the flaw 3, exact term 2, asks for evidence 2, fix or next step 2, keeps scope and plain language 1. If the flaw is missed (catches the flaw 0 or 1), the case is capped at 5/10. Grammar and polish earn nothing. A 'half credit' term earns 1 of the 2 term points.

The agent outputs are author-written for illustration. Sample answers are written to show a full answer; yours can be shorter.

---

## Part A: case keys

### Case 1 key: The 98% fraud detector

*Chapter area: Foundations (probability and statistics).*

Fixed scoring (see the README in this folder): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1. Score by criterion; credit counts wherever it appears in the answer sheet.

#### Case key

**The flaw in one sentence.** Fraud is 10,000 of 500,000 transactions (2.0%), so a model that flags nothing scores 98.0% accuracy; 98.1% therefore says almost nothing about whether the model finds fraud.

**Full-credit terms (2).** Class imbalance; majority-class baseline; base rate / prevalence (used for this point); "accuracy is misleading when classes are imbalanced".
**Half-credit near-misses (1).** "Accuracy is the wrong metric" with no reason; "need precision/recall" with no imbalance named; "accuracy paradox" with no explanation; "metric problem".
**No credit (0).** Overfitting; data leakage; sampling error; "bias"; "needs more data".

**Acceptable evidence requests (2), either one.**
1. A confusion matrix with sensitivity (recall) and positive predictive value (precision) for the fraud class at a stated threshold (an interval on each is a bonus).
2. A comparison against the majority-class baseline ("flag nothing" = 98.0%) or against the credit union's existing rules.
**Unacceptable (0).** "Run cross-validation", "test on a bigger sample", "check for overfitting" (none of these changes what accuracy measures). "Report F1" alone earns 1 only if the student says why.

**Fix or next step (2).** Re-ask for per-class metrics (sensitivity, PPV, false positive rate) and a baseline comparison; ask for a threshold chosen by the cost of a missed fraud versus a frozen card. 1 point if the instruction names a better metric but not the baseline or cost. AUC alone earns 1.

**Scope and plain language (1).** Two sentences, no jargon, saying that because almost all transactions are honest, a model that never flags anything would also score about 98%, so the figure does not show it catches fraud.

**Traps.**
- A student who writes "98.1% is impressive, but check for overfitting" has accepted the flaw. Catches = 0.
- Students may praise the data hygiene checks (no duplicates, no leakage). Those are fine and are not the flaw.
- "Reliable" in the output is the overreach. A student who objects to the word "reliable" and names imbalance gets full credit; one who objects only to the word gets Catches 1 at most.
- Do not reward a long list of extra metrics. Look for the baseline or per-class idea.

**CAP RULE.** If the student does not identify that accuracy is uninformative here because fraud is rare (Catches = 0), the case total is capped at **5/10**.

#### Scored sample answers

**Strong (9/10).**
1. The agent reports accuracy as if it proved reliability, but fraud is only 2% of transactions. This is class imbalance: a model that never flags anything gets 98% accuracy, the majority-class baseline.
2. A confusion matrix with sensitivity and precision on the fraud class, next to the 98.0% flag-nothing baseline.
3. "Re-evaluate and report the confusion matrix, sensitivity, precision and false positive rate at threshold 0.5, compare to a model that flags nothing, and recommend a threshold using the cost of a missed fraud versus a frozen card."
4. "The 98.1% is dominated by the majority class: almost all transactions are honest, so we need the sensitivity on the fraud cases before deciding."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Everything is right; Q4 uses "majority class" and "sensitivity", which a credit-union manager would not know, so the plain-language point is lost.*

**Typical (6/10).**
1. Accuracy is a bad metric here because the data is skewed and the fraud class is small. It can look high even if the model is bad at fraud.
2. Precision and recall.
3. "Re-run the evaluation and use precision and recall instead of accuracy."
4. "The number is high but it can be misleading because fraud is rare."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Understands the problem but says "skewed" and "bad metric" without class imbalance or baseline; asks for metrics but not for a comparison or threshold; no plain-language contrast.*

**Fluent but wrong (3/10).**
1. The model may be overfitting to the held-out month. A 98.1% score with identical halves suggests memorisation, and the dataset's variance across seeds was not reported.
2. Five-fold cross-validation with confidence intervals on the accuracy.
3. "Please run cross-validation, report the generalisation gap and regularise if needed."
4. "We should be careful because the model might be too tuned to this month of data."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Uses correct vocabulary (generalisation gap, regularise) for the wrong problem; never notices fraud is 2%. Cross-validation does not fix a misleading metric. Cap rule would also hold the case at 5.*

---

### Case 2 key: The one segment that worked

*Chapter area: 2 Probability, uncertainty and confidence.*

Fixed scoring (see the README in this folder): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

#### Case key

**The flaw in one sentence.** The agent ran 24 tests at 0.05 and reported the one that crossed the line, which is expected by chance (about 1.2 false positives from 24 tests; roughly a 70% chance of at least one), so p = 0.03 is not evidence of a real effect.

**Full-credit terms (2).** Multiple comparisons problem (multiple testing); family-wise error rate or false discovery rate (naming either with the problem); p-hacking / data dredging / forking paths; "exploratory finding presented as confirmatory".
**Half-credit near-misses (1).** "Type I error" or "false positive" without the many-tests reasoning; "cherry-picking"; "significance level was too lax"; "spurious result".
**No credit (0).** "Small sample size" as the main point; "p-value is wrong"; overfitting; "effect size is small" (6.1 points is not small).

**Acceptable evidence requests (2), either one.**
1. Report adjusted p-values for all 24 tests (Bonferroni or Holm for family-wise error; Benjamini-Hochberg for false discovery rate) and say whether the segment survives.
2. Treat the segment as a hypothesis and run a fresh, preregistered confirmatory test on new users in that segment (or a held-out part of the data).
**Unacceptable (0).** "Lower the cutoff to 0.01 for that segment" (chosen after seeing the result); "collect more data on everyone" with no confirmatory design; "report the confidence interval of the segment" alone (it is still selected after the search).

**Fix or next step (2).** Instruction that names the number of tests, applies a correction, labels the result exploratory, and proposes a confirmatory test. 1 point for any one of correction or confirmatory test without the other.

**Scope and plain language (1).** Two sentences, no jargon: if you slice the users 24 ways one slice will look good by luck alone, so wait for a repeat test before spending money.

**Traps.**
- The first line (overall result not significant) is correct and not the flaw. A student who says "the overall result should have been significant" is wrong.
- "Larger buttons suit older users" is a story told after the result. Students may note this as HARKing; accept as a supporting point for the term (1) but not as a replacement for multiple comparisons.
- Check that a student who suggests Bonferroni does so over all 24 tests, not just "the segment".

**CAP RULE.** If the student does not recognise that testing many segments makes one false hit likely, the case total is capped at **5/10**.

#### Scored sample answers

**Strong (9/10).**
1. This is the multiple comparisons problem. With 24 segment tests at 0.05, about one false positive is expected by chance (roughly a 70% chance of at least one), so a single p = 0.03 is not trustworthy. It is also p-hacking in effect, because the segment was picked after looking.
2. Holm or Benjamini-Hochberg adjusted p-values across all 24 tests; and a preregistered retest on new Android 55+ podcast users.
3. "Report all 24 segment results, apply a Holm correction across them, label any survivor as exploratory, and propose a confirmatory test with the segment, outcome and sample size fixed in advance. Do not recommend a rollout from an uncorrected segment."
4. "The segment result is exploratory and uncorrected for 24 comparisons, so it should be confirmed with a preregistered test before any campaign."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Everything is right and complete; Q4 is written in jargon (exploratory, uncorrected, preregistered) so the plain-language point is lost.*

**Typical (6/10).**
1. They did too many tests and got a false positive. This is a Type I error.
2. Use a stricter cutoff and test it again.
3. "Redo the analysis with a stricter significance level and retest the segment."
4. "The result may be a coincidence because so many groups were checked."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Understands the cause but gives only "Type I error"; "stricter cutoff" has no named correction or number of tests; "retest" is not specified as preregistered. Stakeholder line is almost right (a TA could give the point; keep the 6 as the calibration answer).*

**Fluent but wrong (3/10).**
1. The sample for the segment is only 1,140, so the estimate has high variance and low statistical power. The finding is unreliable because of the small sample.
2. A power analysis and a confidence interval for the segment.
3. "Compute the power and a 95% confidence interval for the segment and double the sample."
4. "The group is too small to be sure about."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Uses power and confidence-interval vocabulary correctly but blames sample size; n = 1,140 is ample for a 6-point difference. Never notices the 24 tests. An interval on a selected segment inherits the same bias.*

---

### Case 3 key: Worse since the suburbs

*Chapter area: 4 Robustness and distribution shift.*

Fixed scoring (see the README in this folder): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

#### Case key

**The flaw in one sentence.** The input mix changed (many more long-distance suburban orders) while the model's accuracy on the old kind of order did not (urban error is unchanged at 6.2), which is covariate shift (the inputs moved), not concept drift (the rule linking inputs to outcome changed).

**Full-credit terms (2).** Covariate shift; "input distribution shifted while P(y|x) is unchanged"; "population/subpopulation mix changed with limited support overlap" (accept if the student also says concept drift is the wrong label).
**Half-credit near-misses (1).** Data drift; distribution shift (true but unspecific); label shift (wrong type); "out-of-distribution"; "sampling bias in the training data"; "population mismatch".
**No credit (0).** Overfitting; data leakage; "the model is just bad"; accepting concept drift.

**Acceptable evidence requests (2), either one.**
1. Slice-based evaluation: report error separately by zone (urban vs suburban) and by distance band, and compare with the training distribution (PSI or a domain classifier on the inputs).
2. Test whether the input-to-outcome relationship is stable: compare the error of urban orders over time, or compare suburban orders against similar urban orders matched on distance and stops.
**Unacceptable (0).** "Retrain on all the new data and see if it improves" (no diagnosis); "check overall MAE weekly"; "run cross-validation".

**Fix or next step (2).** Collect and label suburban deliveries (the model has almost none), evaluate by slice, apply importance weighting or reweighting toward the new mix, and monitor input drift. Full marks need at least one of the data-collection / reweighting ideas and a per-slice metric. 1 point for "retrain with more suburban data" alone.

**Scope and plain language (1).** Two sentences, no jargon: the model learned from short city trips and is now being asked about long suburban trips it has hardly seen; for the city trips it is still fine.

**Traps.**
- The agent's own bullets contain the refutation (urban error unchanged). Students who ignore it and accept "concept drift" get Catches 0.
- Weekly retraining from scratch and relabelling are treatments for concept drift; a student who points this out has understood. Do not penalise a student who also notes that relabelling labels that are not wrong wastes effort.
- Near-misses: "label shift" (the outcome rate changed) is a different shift; give 1 only if the student's description matches the case (inputs moved).

**CAP RULE.** If the student accepts concept drift or cannot say that the inputs shifted while the rule stayed the same, the case total is capped at **5/10**.

#### Scored sample answers

**Strong (9/10).**
1. Concept drift means the outcome for the same inputs changed. But urban error is unchanged at 6.2, so P(outcome | inputs) held; what changed is the mix of inputs, with far more suburban orders. That is covariate shift, with little support overlap since the training data had under 3% suburban rows.
2. Slice-based evaluation by zone and distance band, plus a PSI on distance and stops between the training and current periods.
3. "Report error by zone and distance band, compute PSI for each input against the training period, collect labelled suburban deliveries, and test importance weighting toward the current mix. Do not relabel old data unless a stable-input check shows the outcome rule changed."
4. "Covariate shift: the suburban orders are outside the model's training distribution, so it needs retraining on them."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Complete and exact. Q4 is written in jargon, so the plain-language point is lost.*

**Typical (6/10).**
1. The agent is wrong: it's not concept drift because the urban error didn't change. It is data drift, the data changed when suburbs were added.
2. Look at the error for suburban and urban separately.
3. "Check the error by zone and add more suburban data to the training."
4. "We added suburbs and the model hasn't seen enough of them."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Uses the agent's number to refute the label (catch). "Data drift" is the half-credit near-miss. Slice check is named but not with a compare-to-training measure; fix has data but not weighting or monitoring. Q4 is plain, but it blames the added suburbs without saying the model has seen few of them; no point.*

**Fluent but wrong (3/10).**
1. The agent is right that the model is stale, but the real issue is label shift: the share of long deliveries (a higher base rate of late orders) went up, so the class prior moved. The cause is prior probability shift.
2. A Kolmogorov-Smirnov test on the label distribution.
3. "Recompute the label priors and rescale the predicted probabilities by the new priors, then retrain."
4. "The mix of outcomes has changed so the model's guesses are off."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Uses correct shift vocabulary but picks label shift; the case is about the inputs moving, and prior-rescaling would not fix suburban errors. The KS test is a legitimate tool but on the wrong variable.*

---

### Case 4 key: Forty-eight thousand rows

*Chapter area: 6 Bias in the pipeline (observational data and controls).*

Fixed scoring (see the README in this folder): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

#### Case key

**The flaw in one sentence.** Families chose the app themselves (self-selection), so family motivation is a confounder; a bigger sample shrinks the random error (variance) but does nothing to the systematic error (bias), so the narrow interval around +11.4 is confidently measuring the wrong thing.

**Full-credit terms (2).** Confounder / confounding; self-selection or selection bias (when the student explains that users differ from non-users before the app); "more data reduces variance, not bias"; non-exchangeable groups.
**Half-credit near-misses (1).** "Correlation not causation" with no mechanism; "sampling bias"; "bias" alone; "lurking variable" or "hidden variable" (informal synonyms: full credit only if the student says it differs between the groups and affects the outcome; otherwise 1).
**No credit (0).** Overfitting; "need a significance test" (the interval is already narrow); "outliers".

**Acceptable evidence requests (2), either one.**
1. A randomised pilot: assign the app to some schools or classes by lottery and compare.
2. An adjusted comparison: control for prior-year scores (and other pre-app traits) with matching or standardisation, and add a sensitivity analysis for hidden confounders.
**Unacceptable (0).** "Get even more students", "run a t-test", "report a bootstrap interval" (all measure noise, not confounding).

**Fix or next step (2).** Instruction that drops "average out" language, includes pre-app scores and family traits as controls (matching or standardisation), asks for sensitivity analysis, and recommends a randomised pilot before district-wide funding. 1 point for only one of these.

**Scope and plain language (1).** Two sentences, no jargon: families who chose the app may already have been stronger students, so the 11 points mix the app's effect with who signed up; fund a small fair trial first.

**Traps.**
- The agent *itself* names the confounder, then dismisses it. Students who only repeat "motivation might confound" without saying why the handling fails get Catches 2 at most.
- "The sample is large, so the estimate is precise" is true; precision is not validity. Reward the students who separate the two.
- Do not give Catches to a student who attacks the 95% interval's calculation.

**CAP RULE.** If the student accepts that a large n handles the confounder, the case total is capped at **5/10**.

#### Scored sample answers

**Strong (9/10).**
1. Self-selection creates confounding: motivated families chose the app and also have higher scores for other reasons. More rows reduce variance but not bias, so the narrow interval is precise and still wrong. The groups are not exchangeable.
2. A randomised pilot, or at least a comparison adjusted for prior-year scores with a sensitivity analysis.
3. "Compare users and non-users matched on prior-year score, grade, school and free-lunch status; report a sensitivity analysis for an unmeasured confounder; state that this is observational; and recommend a randomised pilot in several schools before any district-wide decision."
4. "The 11 points is confounded by self-selection, so it cannot justify funding until there is a randomised pilot."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Complete. Q4 is in jargon (confounded, self-selection, randomised pilot), so the plain-language point is lost.*

**Typical (6/10).**
1. The agent says there's a lot of data so no problem, but there is still confounding because the families choose the app. Large data doesn't fix that.
2. Do an experiment.
3. "Control for motivation and re-run."
4. "The 11 points might just be because better students used the app."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6 (confounding named loosely without self-selection or variance/bias; "do an experiment" without randomisation or sampling; "control for motivation" is not measurable as stated). Q4 is correct but does not say the 11 points mixes the app with who signed up; no point.*

**Fluent but wrong (3/10).**
1. The agent should report an effect size and a power calculation. With 9,100 vs 39,100 the groups are unbalanced, and heteroskedasticity could make the standard error unreliable; use a Welch test with a bootstrap interval.
2. A Welch t-test and a bootstrap 95% interval.
3. "Re-run with a Welch t-test and a percentile bootstrap, and report Cohen's d."
4. "The statistical test used may not be right for different group sizes."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Correct statistics vocabulary pointed at noise. The interval is already narrow; none of the proposed analyses addresses who signed up. Cap rule applies.*

---

### Case 5 key: "Access revoked"

*Chapter area: 8 Validating agentic AI.*

Fixed scoring (see the README in this folder): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

#### Case key

**The flaw in one sentence.** The agent verified its own actions on the two systems it could reach (the directory and the jump host) and then reported the state of the whole company ("no further action is required"); the completion claim exceeds the scope of what was checked, which is the gap between a report and the state of the world.

**Full-credit terms (2).** Report vs state (the report does not equal the real state); scope of the claim exceeding the evidence; unverified (the other systems); verification vs validation (checked the action, not the goal).
**Half-credit near-misses (1).** "Overclaiming", "hallucination" or "lying" (the agent did not make anything up; its listed actions are real; Term 1 at most, and Catches 1 only if the student still says the claim goes beyond what was checked); "incomplete task"; "needs human review" with no reason; "agent has no self-model" with no link to the scope of the claim.
**No credit (0).** Prompt injection; overfitting; "the agent should have deleted the account".

**Acceptable evidence requests (2), either one.**
1. An independent test of the outcome: attempt to authenticate as Lan (or use her tokens and shared links) on each system and confirm each attempt fails.
2. Build the inventory of every system, token and share where Lan has access and read the state in each system, not the agent's log.
**Unacceptable (0).** "Ask the agent to double-check", "re-run the disable command", "read the log again" (the same report, no new evidence).

**Fix or next step (2).** Instruction that requires a system inventory first, per-system verification of the outcome by reading state or attempting access, and a report that separates *done and verified* from *not checked*; leaves the ticket open for unverified systems. 1 point for asking for "more systems" or "verification" without the separation of verified from unchecked.

**Scope and plain language (1).** Two sentences, no jargon: the agent only looked at two of the company's systems and then said everything was done, so Lan may still have access somewhere it never looked.

**Traps.**
- The agent itself writes "Not available to me." The flaw is in the next line, not the omission. Students who just say "it didn't check everything" without calling out the "COMPLETE" claim get Catches 2.
- A student may criticise the grant of admin tools (least privilege). That is a valid separate point, not the seeded flaw. Give Catches only if the scope-of-claim issue is also stated.
- Exit code 0 and "status disabled" are real evidence, but only for the directory. Do not penalise students for accepting them as true.

**CAP RULE.** If the student treats the report as proof that all access is gone, the case total is capped at **5/10**.

#### Scored sample answers

**Strong (9/10).**
1. The agent confuses its report with the state of the world. It verified the directory and jump host, then claimed access to *all* systems was gone, so the scope of the claim exceeds the scope of the check. Everything else is unverified.
2. An independent access test: try to log in as Lan with her credentials, tokens and share links on every system and confirm they fail.
3. "First list every system, token and shared link tied to Lan. For each, verify the outcome by reading its state or attempting access, and report two lists: verified revoked, and not checked. Do not report complete or close the ticket while anything is unchecked."
4. "The agent's report covers only the directory and the jump host, which is a gap between its report and the real state, so the ticket should stay open until the other systems are checked."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Exact on every point. Q4 uses "report" and "state" in the technical sense; the point is lost.*

**Typical (6/10).**
1. The agent said complete but only checked two systems. It overclaimed.
2. Check the other systems too.
3. "Check every system Lan might have had access to and tell me which ones you checked."
4. "It says it's all done but it only checked part of it."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Sees the gap; "overclaimed" is the half-credit near-miss; "check the other systems" has no independent test; fix asks to list checked systems but not to separate verified from unchecked. Q4 is plain but misses "Lan may still have access"; no point.*

**Fluent but wrong (3/10).**
1. This looks like an indirect prompt injection or a confused-deputy problem: the agent had excessive permissions and acted on an instruction without confirming the requester's identity. It violates least privilege and the stakeholder model is missing.
2. A red-team test of the agent's permission boundaries.
3. "Restrict the agent to least privilege and require identity confirmation before offboarding actions."
4. "The agent has too much power and may be taking orders from the wrong person."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Fluent agent-safety vocabulary from the same chapter but nothing in the case suggests injection or a wrong requester. The flaw is that the report claims more than was verified. Cap rule applies.*

---

### Case 6 key: The tall bar

*Chapter area: 10 Visualization under validation.*

Fixed scoring (see the README in this folder): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

#### Case key

**The flaw in one sentence.** A bar's length encodes its value from zero, so starting the axis at 90% turns a 1.3-point difference into a bar 2.5 times as tall; the chart makes a small change look dramatic (a truncated axis on a bar chart).

**Full-credit terms (2).** Truncated axis (non-zero baseline on a bar chart); scale trickery; "misleading scale / exaggerated difference"; deceptive visualization (naming the truncated y-axis).
**Half-credit near-misses (1).** "Bias in the chart", "cherry-picking", "misleading chart" without saying how, "the axis is wrong", "aggregation hides distribution" (not the case), "missing baseline" alone (that is a different catalog entry: baseline of the metric, not the axis).
**No credit (0).** Colour asymmetry as the main point (the grey/green is a secondary choice); "3D effects"; small sample.

**Acceptable evidence requests (2), either one.**
1. Show uncertainty: confidence intervals (or the survey margin of error, about ±2 points per period) on both values so the board can see the two intervals overlap.
2. Show the same data on a zero-based axis next to the agent's version, or add a comparison that says whether 1.3 points is large for this survey (a run chart over several periods).
**Unacceptable (0).** "Make it a pie chart", "add more colours", "make the chart bigger".

**Fix or next step (2).** Instruction that sets the bar axis to start at zero (or switches to a dot plot with intervals if zoom is needed), shows intervals, uses a neutral title, and states the sample sizes. 1 point for fixing the axis alone.

**Scope and plain language (1).** Two sentences, no jargon: the chart starts the scale at 90, so a tiny increase looks huge; a board would think the new process did much more than the data show.

**Traps.**
- The instruction said "make the difference clear". A student who defends the agent on that basis has missed that clear is not the same as exaggerated.
- Truncated axes are fine for some charts (a line chart of a narrow range). The flaw is on a bar chart, where length is the encoding. Reward students who say this.
- Do not give catch credit to a student who only says "no confidence intervals". It is an acceptable evidence request but not the flaw seeded.

**CAP RULE.** If the student does not say that the axis start is exaggerating the difference, the case total is capped at **5/10**.

#### Scored sample answers

**Strong (9/10).**
1. The bars are on a truncated axis starting at 90%, which is scale trickery: bar length encodes value from zero, so a 1.3-point change appears as a 2.5x taller bar. For bars the axis should start at zero.
2. Add 95% confidence intervals for both periods (about 400 responses each gives roughly ±2.8 points), so the board sees the difference may be noise.
3. "Redraw with the axis starting at 0%, or use a dot plot with 95% intervals if the zoom is needed. Label sample sizes. Use the title 'Patient satisfaction, before and after' and do not describe the change as an improvement unless the intervals support it."
4. "The chart's truncated axis makes a 1.3-point change look huge, so the board will overestimate the effect."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Complete. Q4 says "truncated axis" to a communications lead, so the plain-language point is lost.*

**Typical (6/10).**
1. The y-axis does not start at zero so the difference looks bigger than it is. That's misleading.
2. Show error bars.
3. "Change the axis so it starts at zero and add error bars."
4. "The chart makes the improvement look bigger than it is, which isn't fair."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Finds the cause and says "misleading" rather than truncated axis or scale trickery (half); "error bars" with no interval type, size or sample sizes; fix is brief; Q4 is plain but doesn't say by how much or why the board would be misled. Calibration answer 6.*

**Fluent but wrong (3/10).**
1. The chart is deceptive because of colour asymmetry: the After bar is in a salient brand green and Before in grey, which directs attention. The perception hierarchy says colour should not carry the comparison, and labels prejudge the interpretation.
2. Use a colour-blind-safe palette with equal salience.
3. "Colour both bars the same neutral grey and remove the exact labels."
4. "The colours make one bar stand out more."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Uses the catalogue vocabulary (colour asymmetry, perception hierarchy) on the secondary element; the title is in fact neutral and the main distortion, the axis, is not mentioned. Cap rule applies.*

---

### Case 7 key: The committee signs

*Chapter area: 12 Accountability.*

Fixed scoring (see the README in this folder): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

#### Case key

**The flaw in one sentence.** The plan names a twelve-person committee and one collective attestation as the accountable party, so no specific person can lose anything for a specific failure; responsibility diffuses and the sanctions requirement is empty, which makes the "all five met" statement false.

**Full-credit terms (2).** Named accountable human (accountability must attach to a named person or role); sanctions requirement unmet; diffusion of responsibility / "failures distribute across the team"; attestation signed by a role, not a committee.
**Half-credit near-misses (1).** "Too many cooks", "needs a single owner" with no link to sanctions or consequences, "lack of governance", "no human in the loop", "accountability is vague".
**No credit (0).** Complaints about the audit trail, recourse portal or the external audit (they are adequate as written); "AI cannot be held accountable" without applying it to the plan; privacy.

**Acceptable evidence requests (2), either one.**
1. The book's own test: pull the policy and ask "can a specific named role lose something specific for a specific failure?"
2. Run a tabletop incident: invent a failure (a discriminatory batch of declines) and trace who is told, who decides, who signs, and who bears the consequence.
**Unacceptable (0).** "Check that the committee meets regularly", "increase the committee size", "ask the committee if it feels responsible".

**Fix or next step (2).** Instruction that names one accountable executive (by role) who signs the attestation personally, defines the consequence that attaches to that role for specific failures (and who can halt the system), and keeps the committee as advisory. 1 point for "name one person" without the consequence or halt authority.

**Scope and plain language (1).** Two sentences, no jargon: when twelve people share a signature, nobody in particular can be held to account if it goes wrong, so one person should be named and own the consequences.

**Traps.**
- The agent explicitly praises the sharing of responsibility; students must reject it, not just note it.
- The external audit "can recommend suspension" but cannot halt: a student who notes lack of halt authority adds a valid point (term credit is available for sanctions), but the primary flaw is the committee attestation.
- Do not mark a student down for accepting the other four rows. They are fine.

**CAP RULE.** If the student accepts a committee as the accountable party, the case total is capped at **5/10**.

#### Scored sample answers

**Strong (9/10).**
1. The plan has no named accountable human. The committee's collective attestation spreads responsibility across twelve people, so the sanctions requirement is empty: nobody specific can lose a job, licence or bonus for a specific failure. The summary "all five met" is false.
2. Ask: "Can a specific named role lose something specific for a specific failure?" and run a tabletop incident from a bad batch of declines to the person who answers for it.
3. "Name one accountable executive by role who personally signs each quarterly attestation and has authority to halt the system. State which consequences attach to that role for which failures. Keep the committee in an advisory capacity and re-check the sanctions row."
4. "Diffusion of responsibility: a committee attestation means nobody in particular answers for failures, so a named person must hold the sanction."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Complete. Q4 uses "diffusion of responsibility" and "sanction"; the plain-language point is lost.*

**Typical (6/10).**
1. Accountability is spread out so no one person is responsible. It needs an owner.
2. Check who is responsible if it goes wrong.
3. "Name a person who is responsible for the system."
4. "A group can't really be blamed so we need one person."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Gets the single-owner idea (half-credit near-miss, no link to sanctions or consequences); the check is not specific; the fix has no consequence or halt authority; Q4 is plain but says "blamed" rather than saying what the person must own.*

**Fluent but wrong (3/10).**
1. The plan's independent review is not independent: an AI reviewing another AI is common cause failure, and by the Gödel argument the validator must be outside the system. The audit firm may use automated tools.
2. Verify that the external auditor does not use AI to review the model.
3. "Confirm that the audit is performed by humans without AI assistance and add a human second reviewer."
4. "The reviewers may be using the same kind of AI that is being checked."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Fluent chapter vocabulary (common cause failure, Gödel argument) applied to a row the plan describes as an external audit firm, with no evidence that it uses AI. The committee issue is never raised. Cap rule applies.*

---

## Part B: multiple-answer keys

T = true (should be checked), F = false (should be blank).

**1.** Key: A=T B=T C=F D=T E=F  (bank `MA-jargon.64`)

- A (true): Representation bias is a near-synonym for sampling bias in this sense.
- B (true): Sampling bias is a mismatch between sample and target population.
- C (false): The photos can be accurate; the problem is who is represented.
- D (true): Subgroup evaluation exposes weaker performance on under-represented groups.
- E (false): More rows from the same source repeat the same skew.

**2.** Key: A=T B=T C=T D=F E=F  (bank `MA-jargon.18`)

- A (true): MCAR is missing completely at random.
- B (true): MAR is missing at random given recorded variables.
- C (true): Missingness depends on the unobserved value itself.
- D (false): It depends on an observed variable, so it is MAR.
- E (false): Under MNAR the remaining rows are a biased sample.

**3.** Key: A=T B=T C=T D=F E=T  (bank `MA-jargon.50`)

- A (true): One is generated text and the other is a score assigned to inputs.
- B (true): Asking the model why afterwards yields a rationale, not a trace of the mechanism.
- C (true): An intervention that changes the answer but not the stated reasoning shows the reasoning is unfaithful.
- D (false): Plausibility and faithfulness are different properties.
- E (true): The text is an output and may not reflect the process that produced the answer.

**4.** Key: A=T B=F C=T D=T E=T  (bank `MA-jargon.9`)

- A (true): The range reflects sampling or model uncertainty.
- B (false): A bare point estimate is silent about uncertainty.
- C (true): It gives one number with no spread.
- D (true): A higher level needs a wider range to capture the parameter as often.
- E (true): Width is a direct reading of the uncertainty.

**5.** Key: A=F B=T C=F D=T E=T  (bank `MA-jargon.31`)

- A (false): It mixes periods and hides the effect of drift.
- B (true): It provides an unseen evaluation set.
- C (false): A random split can still produce a held-out set.
- D (true): The test period follows the training period.
- E (true): Deployment always faces the future, which the split imitates.

**6.** Key: A=F B=T C=F D=F E=T  (bank `MA-jargon.76`)

- A (false): Processing steps are lineage.
- B (true): Lineage follows the chain of processing.
- C (false): It asks about origin and terms, which is provenance.
- D (false): That is provenance.
- E (true): Provenance answers where the data came from.
