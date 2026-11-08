# INFO 7375 Computational Skepticism for AI: Fall 2026 practice exam 02: ANSWER KEY

**Read this only after you have finished the matching exam, [practice-exam-02.md](practice-exam-02.md).** Practice only; the real exam uses different cases and questions.

How cases are scored: catches the flaw 3, exact term 2, asks for evidence 2, fix or next step 2, keeps scope and plain language 1. If the flaw is missed (catches the flaw 0 or 1), the case is capped at 5/10. Grammar and polish earn nothing. A 'half credit' term earns 1 of the 2 term points.

The agent outputs are author-written for illustration. Sample answers are written to show a full answer; yours can be shorter.

---

## Part A: case keys

### Case 1 key: Grading its own homework

*Chapter area: 1 The skeptic's toolkit.*

Fixed scoring (see the README in this folder): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

#### Case key

**The flaw in one sentence.** The summaries and the verdicts both come from Model A, so the check is circular: it measures whether the model agrees with itself (and models favour their own output), not whether the summaries match the articles.

**Full-credit terms (2).** Circularity / circular validation; self-preference bias (as applied to an LLM judging itself); "no independent evidence"; LLM-as-judge validated against nothing.
**Half-credit near-misses (1).** "Conflict of interest", "bias" (unspecified), "the model is grading itself" with no term, "needs a ground truth" with no mention of the self-judging problem, "reproducibility" for the temperature-0 line.
**No credit (0).** Overfitting; small sample; hallucination (the summaries may hallucinate, but that is not the flaw in this evidence).

**Acceptable evidence requests (2), either one.**
1. Have humans read a random sample of summaries against the articles and score faithfulness against a written rubric (the reference standard), then compare the model's verdicts to the human verdicts.
2. Use a different judge, but only after measuring that judge's agreement with human scores on a labelled sample.
**Unacceptable (0).** "Run it again", "run it at a higher temperature", "ask a bigger model from the same vendor" with no human comparison, "use more articles".

**Fix or next step (2).** Instruction that makes a human-scored random sample the reference standard and reports the judge's agreement or error rate against it, with a confidence interval. 1 point if a human check is requested without sampling or without comparing it to the model's verdicts.

**Scope and plain language (1).** Two sentences, no jargon, along the lines of "the same system wrote the summaries and marked them, so it is like a student marking their own exam; someone else has to check a sample."

**Traps.**
- The "temperature 0, verdicts did not change" line is a distractor: repeatability is not accuracy. A student who attacks only that line has not found the flaw (Catches 1 at most).
- "It's cheap and automated" is the agent's rationalisation. Students who accept cost as a reason for no human reading miss the point.
- A student may say "LLMs hallucinate so 94% is too high." That guesses at the direction of error without naming why the evidence is empty. Catches 1.

**CAP RULE.** If the student does not see that the model is validating its own output, the case total is capped at **5/10**.

#### Scored sample answers

**Strong (9/10).**
1. The check is circular: Model A wrote the summaries and then judged them, so there is no independent evidence, and models show self-preference bias toward their own text. The 94% measures self-agreement, not accuracy against the articles.
2. A random sample of, say, 100 summaries read by two humans against the articles, compared with Model A's yes/no.
3. "Draw a random sample of 100 summaries, have two human raters score each against the article using this rubric, report the human-judged accuracy with an interval, and report how often Model A's verdict agrees with the humans. Do not use Model A's own verdict as the accuracy figure."
4. "The 94% is circular, because the same model wrote and judged the summaries; we need independent evidence from a human-scored sample first."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Complete and precise. Q4 repeats "circular" and "independent evidence" to a library director; the plain-language point is lost.*

**Typical (6/10).**
1. The model is checking its own work, which is a conflict of interest, so the 94% can't be trusted much.
2. Get some people to look at the summaries.
3. "Have humans check the summaries too and compare."
4. "The AI graded itself, so the number may be too optimistic."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Sees the circularity but uses "conflict of interest" instead of circularity/independent evidence; the human check has no sampling or comparison to the model's verdicts; the stakeholder line is correct but leaves out the "marks its own exam" step the TA needed to see.*

**Fluent but wrong (3/10).**
1. The agent's 94% lacks statistical rigour: with n = 200 the sampling error is about ±3 points, and the check shows no variance across seeds. This is an inadequate confidence interval.
2. Re-run the check with ten different random seeds and report the standard error.
3. "Re-run the evaluation with ten seeds and report 94% with a 95% interval."
4. "The result is uncertain because the sample is small."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Correct statistics vocabulary, wrong problem. A narrower interval around a circular number is still circular. Re-running the same judge is the unacceptable evidence request, and the evidence point is given only for asking for an interval.*

---

### Case 2 key: The follow-up call feature

*Chapter area: 3 Data validation and provenance.*

Fixed scoring (see the README in this folder): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

#### Case key

**The flaw in one sentence.** `follow_up_calls_count` is logged after discharge, and nurses make those calls because patients look likely to return, so the feature carries information about the outcome that will not exist at the time the model must predict: target (temporal) leakage.

**Full-credit terms (2).** Data leakage; target leakage; temporal leakage ("uses information from the future"); "feature not available at prediction time".
**Half-credit near-misses (1).** "Feature is too correlated with the label", "the feature is a proxy for the label", "data quality", "bad feature", "information the model shouldn't have" without time.
**No credit (0).** Overfitting; class imbalance (11.4% is mild and not the flaw); multicollinearity; correlation vs causation.

**Acceptable evidence requests (2), either one.**
1. Audit each feature's timestamp against the prediction time (discharge) and drop any feature recorded after it; re-run and report the new AUC. Dropping or ablating only the one feature, with no timestamp audit and no temporal split, earns **1**.
2. Re-evaluate with a temporal split (train on earlier discharges, test on later ones) using only features available at discharge.
**Unacceptable (0).** "Run cross-validation" (leakage survives it), "tune hyperparameters", "get more data", "regularise".

**Fix or next step (2).** Instruction that states the prediction time, restricts features to those available at that time, asks for provenance (when and why each feature is recorded), and re-reports. 1 point for removing the feature without the prediction-time rule or the re-evaluation.

**Scope and plain language (1).** Two sentences, no jargon: the model uses a clue that only appears after the patient has gone home (the nurse calls), so it cannot help decide who to call; its score is inflated.

**Traps.**
- A very high AUC (0.94) for a hard task is the tell; some students will say "too good to be true" without a reason. That is Catches 1 at most.
- The random row split is a secondary weakness (rows from the same patient can appear in both sets). Credit it as a supporting point; the main answer is the feature.
- Students may call the feature "causal" or say that calls cause readmissions. Wrong direction.

**CAP RULE.** If the student does not identify `follow_up_calls_count` (or a post-discharge feature) as unavailable at prediction time, the case total is capped at **5/10**.

#### Scored sample answers

**Strong (9/10).**
1. Target leakage, specifically temporal leakage: follow_up_calls_count is recorded after discharge and is partly caused by nurses already expecting a readmission, so the model is using future information. The 0.94 is inflated.
2. Remove follow_up_calls_count and any other post-discharge feature, re-run on a temporal split, and compare AUC with and without it.
3. "State that predictions are made at discharge. For each feature, give the table and timestamp it comes from and exclude any recorded after discharge. Evaluate on a temporal split (train earlier, test later) and report the AUC and sensitivity again."
4. "The 0.94 comes from target leakage: the model sees call counts that are logged after discharge, so it cannot be used at discharge."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Complete and exact. Q4 says "target leakage" and "0.94" to a care manager; the plain-language point is lost.*

**Typical (6/10).**
1. One feature, follow_up_calls_count, is too closely tied to the outcome and basically gives away the answer. That is a data leakage problem.
2. Drop that feature and see what happens to the AUC.
3. "Remove follow_up_calls_count and re-run the model."
4. "A feature in the model is a giveaway so the score looks better than it really is."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Finds the feature and says leakage, but gives no reason about time (so the term is only half: "giveaway" ≈ proxy); asks for an ablation but no temporal split or prediction-time rule; plain-language answer misses "after the patient leaves".*

**Fluent but wrong (3/10).**
1. The model is overfitting: AUC 0.94 against an 11.4% positive rate is suspiciously high, and gradient-boosted trees with default settings have high capacity. The generalisation gap is not reported.
2. Nested cross-validation with early stopping and an L2 penalty.
3. "Run nested cross-validation, tune the regularisation, and report the train and test AUC."
4. "The model learned the training patients too well and may not work on new ones."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Notices that 0.94 is too good, which is right, and uses overfitting vocabulary fluently, but the cause is a post-discharge feature. Regularisation and cross-validation leave the leak in place. Cap rule would also hold at 5.*

---

### Case 3 key: Stay put and get approved

*Chapter area: 5 Model explainability.*

Fixed scoring (see the README in this folder): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

#### Case key

**The flaw in one sentence.** SHAP values explain how the model's score depends on its inputs, not what causes default or what would happen if an applicant changed something; the agent treated a feature attribution as a causal effect (and as actionable advice).

**Full-credit terms (2).** Feature importance vs causal effect (attribution is not a causal effect); correlation vs causation (accept as full when it is applied to attribution); actionability / recourse (the missing check); proxy variable (months at address standing in for something else).
**Half-credit near-misses (1).** "SHAP is not reliable", "black box", "the model may be biased", "need a counterfactual" with no explanation, "feature importance is global not local".
**No credit (0).** Multicollinearity (alone); overfitting; "SHAP is too slow".

**Acceptable evidence requests (2), either one.**
1. Ask for counterfactual explanations for declined applicants with feasibility and monotonicity constraints (only changes an applicant can actually make), and state that these describe the model, not real-world default.
2. Ask for causal evidence for the claim (for example an experiment or an adjusted analysis of repayment outcomes), or an audit of whether months-at-address is a proxy for something else.
**Unacceptable (0).** "Recompute SHAP with more samples", "use LIME as well" (same problem), "explain the model more clearly".

**Fix or next step (2).** Rewrite so the report describes what the model does ("the model scores shorter tenure as higher risk"), separates it from any claim about why people default, drops the "stay put" advice, and requests actionable counterfactuals or a proxy audit. 1 point for removing the causal wording without a replacement analysis.

**Scope and plain language (1).** Two sentences, no jargon: the ranking shows what the bank's model looks at, not what would make a person repay; telling people to stay put to get approved is a guess, not a finding.

**Traps.**
- The final sentence ("SHAP is faithful, so the advice is reliable") is the rationalisation. Faithfulness to the model does not make the model faithful to the world.
- Students who say "months at address is a proxy for age or class" are adding the fairness angle correctly; give term credit.
- Do not reward a student for questioning the SHAP calculation itself (the ranking is not the flaw).

**CAP RULE.** If the student does not say that the attribution is not a causal effect or a basis for advice, the case total is capped at **5/10**.

#### Scored sample answers

**Strong (9/10).**
1. This confuses feature importance with causal effect. Mean |SHAP| describes how the model uses address tenure; it does not show that staying longer lowers default risk. Tenure may be a proxy for something else (age, renting vs owning), so "stay put" advice is unsupported.
2. A counterfactual explanation with actionability and monotonicity constraints for declined applicants, plus a proxy audit of tenure.
3. "Describe what the model does with each feature without causal language. Generate counterfactual explanations restricted to changes applicants can really make, and test whether tenure is acting as a proxy for another variable. Withdraw the advice to wait twelve months."
4. "The attributions show what the model weighs most, not what causes repayment, so the stay-put advice is not supported."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Correct and thorough; Q4 says "attributions" and "causes repayment" in technical register, so the plain-language point is lost.*

**Typical (6/10).**
1. SHAP only shows correlation, not causation, so you can't tell applicants to stay at an address longer.
2. Get a counterfactual analysis.
3. "Don't give advice from SHAP; do something that shows what actually changes the outcome."
4. "The model uses address a lot but that doesn't mean moving less helps."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6 (term is generic correlation-vs-causation without tying it to attribution; evidence names counterfactuals but without constraints; fix is vague; Q4 is a shrug rather than a statement of what the ranking does show).*

**Fluent but wrong (3/10).**
1. SHAP with a tree model is subject to high-cardinality bias and the marginal vs conditional value function choice; the ranking may be unstable across background datasets. So the 24% could be wrong.
2. Re-run KernelSHAP with several background datasets and report the Jaccard stability of the top features.
3. "Recompute with the conditional value function and three baselines, and report the stability."
4. "The importance numbers might change if we compute them differently."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Fluent explainability vocabulary (value function, Jaccard) aimed at the stability of the ranking, which is not what the agent got wrong. A perfectly stable ranking would still not be a causal effect.*

---

### Case 4 key: Equal rates

*Chapter area: 7 Fairness metrics.*

Fixed scoring (see the README in this folder): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

#### Case key

**The flaw in one sentence.** Equal shortlisting rates are demographic parity; equalized odds requires equal true-positive rates and equal false positive rates across groups, which needs the true qualification labels and was never computed.

**Full-credit terms (2).** Demographic parity (statistical parity) named as what was measured, and equalized odds (equal TPR and FPR) as the policy; both must appear for 2.
**Half-credit near-misses (1).** Only one of the two terms right; "disparate impact" or "four-fifths rule" as the measure (acceptable as a name for the rate comparison, but not the policy); "equal opportunity" for equalized odds (it is only the TPR half); "wrong fairness metric" with no names.
**No credit (0).** "Calibration" mixed up with equalized odds; "bias in the data" in general; "the sample is small".

**Acceptable evidence requests (2), either one.**
1. Compute true-positive rate and false positive rate for women and for men using a trusted qualification label, and compare them.
2. Build the per-group confusion matrices (or error rates) from outcomes such as later job performance or recruiter ground truth, and report the gap with an interval.
**Unacceptable (0).** "Compute the selection rate again with other thresholds", "check intersectional groups" (a good idea but does not test the stated policy), "compute accuracy per group" (accuracy parity is a different criterion).

**Fix or next step (2).** Instruction that defines equalized odds as equal TPR and FPR, requires a stated source for the qualification label (and its limits), and reports compliance only after both rates are compared. 1 point if TPR and FPR are named but the label source is not.

**Scope and plain language (1).** Two sentences, no jargon: the audit shows women and men are shortlisted at the same rate, but not whether qualified women and qualified men are treated alike, nor whether the same share of unqualified people get through.

**Traps.**
- The four-fifths rule is *correctly* used by the agent for selection rates. A student who says the 0.99 ratio is wrong is wrong. The flaw is that the rate comparison cannot show equalized odds.
- Some students write "equalized odds = equal outcomes"; this is half-credit at best because equalized odds conditions on the true label.
- Because the impossibility result means parity and equalized odds can conflict when base rates differ, a student who mentions it correctly deserves the term point; do not require it.

**CAP RULE.** If the student agrees that equal selection rates show equalized odds, the case total is capped at **5/10**.

#### Scored sample answers

**Strong (9/10).**
1. The agent measured demographic parity (equal selection rates). The policy is equalized odds, which requires equal true-positive and false positive rates across groups. Equal rates can hide that qualified women are shortlisted less often and unqualified men more often.
2. TPR and FPR by gender against a qualification label such as later performance ratings.
3. "Define the qualified/unqualified label and its source, compute TPR and FPR for each gender with intervals, and report whether both gaps are within a stated tolerance. Do not state compliance until both rates are checked."
4. "The audit shows the model picks women and men at the same rate, but a demographic-parity result does not tell us whether qualified people of each gender get an equal chance."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Complete. Q4 uses "demographic-parity result", which the officer would not know.*

**Typical (6/10).**
1. They used the wrong fairness measure. Equal selection rate is not the same as equalized odds, which looks at error rates.
2. Look at the error rates for each group.
3. "Check the error rates for men and women and say whether they are equal."
4. "Equal numbers hired does not mean the model is equally good for both."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6 (does not name demographic parity; "error rates" instead of TPR and FPR; no label source). The last answer is plain but never says what the audit did show (equal rates); no point.*

**Fluent but wrong (3/10).**
1. The audit ignores intersectionality: it checks gender only, with no intersectional subgroup, and the four-fifths rule is a legal test of disparate impact not a statistical test of significance. The result is not robust.
2. Re-run the audit by gender-by-race intersection with a chi-squared test.
3. "Repeat the four-fifths test for every intersection of gender and race and add a chi-squared test."
4. "The audit needs more groups to be sure."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Raises real fairness vocabulary (intersectional, disparate impact) but never notices that the policy criterion was not computed. Repeating selection-rate tests on more groups still never tests equalized odds.*

---

### Case 5 key: Every box has a tool

*Chapter area: 9 Delegation, trust and the supervisory role.*

Fixed scoring (see the README in this folder): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

#### Case key

**The flaw in one sentence.** The map names who (or which tool) does each step but states no handoff condition between steps (what must be true of an output before the next step uses it, who checks it and who signs), so errors flow unchecked from the claim form to a letter in the claimant's inbox with no accountable human.

**Full-credit terms (2).** Handoff condition (contract, acceptance criterion at each handoff); delegation map missing the supervisory capacities (plausibility auditing / interpretive judgment checkpoints); "partition without a contract".
**Half-credit near-misses (1).** "No human in the loop"; "automation bias" or "rubber-stamping" (a risk, not the missing structure); "needs oversight"; "human on request is too weak"; "no error handling".
**No credit (0).** "Tools are inaccurate"; "use better models"; privacy issues; "too fast".

**Acceptable evidence requests (2), either one.**
1. Seeded-error test: insert known-bad claims (a wrong photo assessment, a coverage exclusion, an impossible payout) and see which step catches each; if none do, the map fails.
2. Run the Boondoggle questions on each sub-task (cost of error, reversibility, verifiability, who is accountable) and show the answers for steps 4 and 5.
**Unacceptable (0).** "Test each tool's accuracy again", "benchmark the models", "ask the agent if the map is safe".

**Fix or next step (2).** Instruction that, for every handoff, states the input and output specification, an acceptance criterion, a named human owner who signs for it, and a log entry; and puts human review before the irreversible step (step 5 emailing a denial). 1 point for adding human review without the contract details.

**Scope and plain language (1).** Two sentences, no jargon: a name on each step does not say what is checked between steps, so a mistake early on goes straight into a letter to the customer with nobody having looked at it.

**Traps.**
- "Every step has an owner" is the agent's false comfort; "Tool A" is not an accountable owner. Students must say who is accountable.
- Step 6 ("human, on request") will tempt students to say the map has a human. The key point is that the human is not on the path and nobody asks.
- The 85% saving is not the flaw. A student who attacks the estimate has not found it.

**CAP RULE.** If the student does not say that the handoffs between steps lack checks, criteria or accountable owners, the case total is capped at **5/10**.

#### Scored sample answers

**Strong (9/10).**
1. The map partitions the work but gives no handoff condition: nothing says what must be true of each output before the next tool uses it, and no human owns or signs a handoff. Plausibility auditing and interpretive judgment are absent, so an error in step 2 flows to the emailed letter in step 5.
2. A seeded-error test: put known-bad claims through the pipeline and see whether any step stops them.
3. "For each handoff, write the input and output specification, the acceptance criterion, the named human who signs, and the log entry. Put a human review before step 5, because the email cannot be recalled. Then list which known-bad cases each check would catch."
4. "Giving each step to a tool does not say who checks the work between steps, so errors can reach customers; the plan needs a defined handoff condition for each step."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Complete. Q4 ends in "handoff condition", a course term; the plain-language point is lost.*

**Typical (6/10).**
1. There is not enough human oversight. The adjuster is only there when asked, so the pipeline can make mistakes with no checks.
2. Test the pipeline with some wrong claims.
3. "Add human review steps to the map, especially before the letter is sent."
4. "Nobody checks the AI's work before it goes to customers."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Sees the missing checks but uses "oversight" generically (no handoff condition or contract); the test is named without seeded errors; fix puts review in but gives no specification, acceptance criterion or signer. Q4 is plain but incomplete; no point.*

**Fluent but wrong (3/10).**
1. The map suffers from poor trust calibration: each tool's accuracy has not been stated, so the executive committee cannot calibrate their trust. The agent should report precision, recall and the expected calibration error for each of the five tools.
2. Benchmarks for each tool with a reliability diagram.
3. "Add accuracy, recall and calibration figures for each tool to the table."
4. "We don't know how good each tool is."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Uses calibration and trust vocabulary correctly but misreads the gap: the problem is the missing structure between the tools, and accuracy figures would not create a check or an owner. Cap rule applies.*

---

### Case 6 key: "This proves it"

*Chapter area: 11 Communicating uncertainty.*

Fixed scoring (see the README in this folder): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

#### Case key

**The flaw in one sentence.** The verbs (proves, demonstrates, concludes) claim a strength that one county, one season, a before-and-after comparison and no comparison group cannot warrant; the right verb is closer to *observe* (or *suggest*), and the claim reaches a statewide forecast beyond its scope.

**Full-credit terms (2).** Verb taxonomy / verb ladder (naming that "prove/demonstrate" outrank the evidence); warranted assertion (claim in proportion to evidence); overclaiming with scope of the claim named.
**Half-credit near-misses (1).** "Overclaiming" or "overstating" with no reference to the verb; "correlation not causation"; "confounding"; "too certain"; "not generalisable".
**No credit (0).** Statistical significance or p-value talk; "small sample" (14 schools are not the issue; the design is); "bias".

**Acceptable evidence requests (2 for two of these, 1 for one).**
1. A comparison group (a county without the policy, or the same county in earlier seasons).
2. Replication in another season or county, or a robustness / sensitivity check for rival explanations (a milder flu season, school closures, vaccination changes).
3. A stated analysis of the other things that changed over the same time (rival hypotheses).
**Unacceptable (0).** "Get a bigger p-value", "more precise decimals", "ask the model to be more confident".

**Fix or next step (2).** Instruction that asks the agent to choose the verb from the evidence ladder, state the conditions of observation (14 schools, one county, one season, no comparison group), and name the limits. Verb choice: *observe* (best), *suggest* or an association phrasing such as "was associated with" (acceptable). 1 point for restating the limits without a verb choice, or for choosing *find* alone. 0 for *show*, *demonstrate*, *conclude* or *prove*.

**Scope and plain language (1).** Two sentences, no jargon: absences fell by about a fifth in these schools after the policy; this does not by itself show the masks caused it, nor that the same would happen statewide.

**Traps.**
- The 22% fall is a real observation. A student who disputes it is wrong; the flaw is the verb attached to it.
- "Consistent across all 14 schools" sounds like replication but is the same county and the same season. Students who accept it as a reason for "find" or "show" are over-reading.
- Students may recommend dropping the recommendation to adopt the policy. The key is calibrating the claim, not deciding the policy.

**CAP RULE.** If the student endorses "prove" or "demonstrate" for this evidence, the case total is capped at **5/10**.

#### Scored sample answers

**Strong (9/10).**
1. The verbs overstate the evidence: "proves", "demonstrates" and "concludes" sit at the top of the verb ladder, but the data are one county, one season and a before-and-after with no comparison group. A warranted assertion here is "we observe" that absences fell 22%; the statewide forecast goes beyond the scope.
2. A comparison county without the policy, and the same analysis in other seasons to rule out a mild flu year.
3. "Write the paragraph with the verb the evidence supports. State 14 schools, one county, one season and no comparison group. Use 'we observe that absences fell 22%' and 'this is consistent with an effect of masks but does not isolate it'. Do not make a statewide prediction."
4. "The claim should be limited to what we observe in these schools, with rival explanations not yet excluded and no warrant for a statewide forecast."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Complete. Q4 is in the vocabulary of the course (rival explanations, warrant), not plain language.*

**Typical (6/10).**
1. It overclaims. It says proves but this is only correlation: there could be other reasons absences went down.
2. A control group.
3. "Say that the result is suggestive and not proven and add the limitations."
4. "Absences went down but we don't know it was the masks."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. "Overclaims" and "correlation" are the half-credit near-misses (no verb ladder); only one of the two requested items is given (a comparison group); "suggestive" is a usable verb but no conditions of observation are required; Q4 omits the statewide limit.*

**Fluent but wrong (3/10).**
1. The paragraph needs a significance test: with 14 schools the claim of a 22% reduction has no p-value and no confidence interval, so "proves" is unsupported. It should report the test statistic and a Bonferroni-corrected interval.
2. A paired t-test with a 95% confidence interval and a power calculation.
3. "Add a paired t-test, confidence interval and p-value to the paragraph."
4. "The result needs to be tested statistically."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Statistical vocabulary, used in a way that ignores the design problem. A significant p-value on a before-and-after with no comparison would still not warrant "proves". The student did not link the verb to the evidence. Cap rule applies.*

---

### Case 7 key: More data will close the gap

*Chapter area: 13 The limits of AI.*

Fixed scoring (see the README in this folder): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

#### Case key

**The flaw in one sentence.** The agent treats the system's blind spots as a coverage problem that more data will remove, but the gap between the data and the world is structural: whatever is not in the data cannot be learned from the data, so a human who watches the deployment distribution and can override remains necessary.

**Full-credit terms (2).** Data-world gap; categorical (structural) limit, not a contingent one; "structural blind spot that data cannot cover"; "the system's competence is over the data, not the world". If the headline term is distribution shift but the student also says more data cannot close the gap, give 2.
**Half-credit near-misses (1).** Distribution shift or external validity or population mismatch (these are the practical instances; credit when the student says the rural population differs and monitoring is needed, but does not say that more data cannot close the gap); "edge cases"; "model can't be perfect"; "need human in the loop".
**No credit (0).** Overfitting; class imbalance (the 0.9% is not an accuracy-metric problem); "the vendor is biased".

**Acceptable evidence requests (2), either one.**
1. An external validation on rural clinic data before any override is removed (for example a shadow-mode run where the AI triages and the nurse still reviews, then comparing disagreements), with results for rare presentations specifically.
2. Defined monitoring of the deployment distribution (rural case mix versus training) with a stated trigger for restoring human review.
**Unacceptable (0).** "Wait until the data has grown tenfold and check accuracy again", "ask the vendor for a higher accuracy figure", "monitor overall accuracy monthly" (the agent's own plan).

**Fix or next step (2).** Instruction that rejects "more data removes the gap", keeps the nurse override at least until shadow-mode results from the rural clinics exist, requires slice-level metrics for rare presentations, and defines monitoring and an override trigger. 1 point for keeping the override without the shadow-mode or monitoring detail.

**Scope and plain language (1).** Two sentences, no jargon: the system only knows what it has been shown, and a rural clinic will always see cases it was never shown; a nurse is the safeguard for exactly those cases.

**Traps.**
- "Distribution shift" is true here and tempting. It earns half the term credit only. The seeded issue is the claim that scale makes the limit vanish.
- The 99.1% figure is real but from city records. Students who say the rural population needs external validation add a good evidence request; do not use it as a substitute for the categorical-limit point.
- "A model that has seen enough data does not have a blind spot" is the sentence to attack. Students who quote it and rebut it should get catch credit.

**CAP RULE.** If the student accepts that more data will make the review unnecessary, the case total is capped at **5/10**.

#### Scored sample answers

**Strong (9/10).**
1. The agent denies the data-world gap: a system's competence is over its data, not the world, and what is not in the data (new rural presentations) cannot be learned from it. This is a structural limit, not a contingent one that tenfold more data removes.
2. A shadow-mode run in the rural clinics with the nurse still reviewing, reporting disagreements on rare presentations, and a monitoring trigger for case-mix changes.
3. "Do not recommend removing review. Require a shadow-mode trial at the rural clinics with slice results for rare presentations, define monitoring of the rural case mix against the training data, set the trigger that restores the nurse override, and say that more data narrows but cannot close the gap."
4. "The data-world gap means the system can only be as good as what it was shown, so the review stays; a rural clinic will see cases the data never contained."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Complete. Q4 uses "data-world gap" to a physician; the plain-language point is lost.*

**Typical (6/10).**
1. The rural clinics are different from the city hospital, so there will be distribution shift and the 99% might not hold. The nurse is still needed.
2. Test it at a rural clinic first.
3. "Recommend keeping the nurse review until the model is tested at rural clinics."
4. "The model was tested in the city, not in the countryside, so we should not drop the nurse yet."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Right action and a valid concern (distribution shift is the half-credit near-miss) but never rebuts the claim that more data will close the gap; the test is not specified as shadow mode or slice-based; the stakeholder line is plain but is about the pilot site, not the limit.*

**Fluent but wrong (3/10).**
1. The accuracy figure is not trustworthy because of class imbalance: the rare presentations are the minority class, so the 99.1% accuracy hides low sensitivity on urgent cases. The agent should compute recall per class.
2. A confusion matrix with recall and precision for urgent cases.
3. "Report per-class recall, precision and F1 for the urgent class and decide on that basis."
4. "The accuracy number hides how it does on the serious cases."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. A sensible foundations point (and an acceptable extra), but the agent's reasoning flaw is the belief that scale removes the gap. Per-class recall on city data cannot tell whether rural cases the model never saw are handled. Cap rule applies.*

---

## Part B: multiple-answer keys

T = true (should be checked), F = false (should be blank).

**1.** Key: A=F B=T C=F D=T E=T  (bank `MA-jargon.56`)

- A (false): A proxy is an ordinary input that stands in for one.
- B (true): Protected attributes are the characteristics fairness rules refer to.
- C (false): Other correlated inputs can still carry the information.
- D (true): Unawareness removes the column but not correlated information.
- E (true): A proxy is an input correlated enough with a protected attribute to carry its information.

**2.** Key: A=F B=T C=T D=T E=T  (bank `MA-jargon.15`)

- A (false): The two check different things.
- B (true): The type is right but the value is implausible.
- C (true): The type does not match the declared type.
- D (true): Schema concerns shape and type, not meaning.
- E (true): Semantic checks use domain meaning.

**3.** Key: A=F B=F C=T D=T E=T  (bank `MA-jargon.46`)

- A (false): A counterfactual describes an altered input that flips the outcome; a saliency map scores existing inputs.
- B (false): The map describes the model's reliance, not the patient's biology.
- C (true): Attribution divides a prediction among inputs.
- D (true): Shapley values attribute a prediction to features using a game-theoretic definition.
- E (true): Saliency is a sensitivity of the output to the input.

**4.** Key: A=F B=T C=F D=T E=T  (bank `MA-jargon.3`)

- A (false): They have different meanings and different assumptions.
- B (true): A credible interval is a posterior probability statement.
- C (false): That reading belongs to a credible interval.
- D (true): Confidence refers to the long-run behaviour of the procedure.
- E (true): The posterior, and so the interval, combines prior and likelihood.

**5.** Key: A=T B=T C=T D=T E=F  (bank `MA-jargon.35`)

- A (true): The proportion of fraud moved.
- B (true): The optimal threshold depends on the prior.
- C (true): The class prior changed.
- D (true): Fraud looks the same as before.
- E (false): Concept drift would need P(y | x) to change.

**6.** Key: A=T B=F C=T D=T E=F  (bank `MA-jargon.69`)

- A (true): Accuracy is an observed rate.
- B (false): One is a stated probability and the other an observed rate.
- C (true): Confidence is the model's stated probability.
- D (true): A calibrated 90 percent confidence is right about 90 percent of the time.
- E (false): That model is overconfident, so it is poorly calibrated.
