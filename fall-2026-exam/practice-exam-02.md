# INFO 7375 Computational Skepticism for AI: Fall 2026 practice exam 02

**Practice only. The real exam uses different cases and different questions.** Check your work afterwards against the separate answer file named in the README.

Name: ______________________

## Instructions

- **Part A: 7 cases, 10 points each (70 points).** Each case gives a scenario, the instruction given to an AI analyst, the analyst's output, and four questions. Every output in this exam is author-written for illustration; it is not a sampled run of any model.
- **Part B: 6 multiple-answer questions, 5 points each (30 points).** Each has five statements, A to E. Check the statements that are true. Each statement is true or false on its own and scores 1 point: checked and true, or left blank and false.
- Total: 100 points. Suggested time: about 7 minutes per case and 3 minutes per multiple-answer question, so about 70 minutes for Part A and 18 for Part B.
- Answer in short, plain sentences. Spelling, grammar and length earn nothing. Use the course's exact terms where they fit.
- Do it cold: no cheat sheet, no notes, no AI tool.

---

## Part A: cases (70 points)

### Case 1 (10 points): Grading its own homework

*Chapter area: 1 The skeptic's toolkit.*

#### 1. Scenario

Professor Bear directs a university library and is deciding whether first-year students may rely on an AI research assistant that writes short summaries of journal articles. The library cannot afford to read every summary, so the decision will rest on a measured accuracy figure. Professor Bear asked an AI analyst to measure it.

#### 2. The instruction given to the AI analyst

> "Measure how accurate the assistant's article summaries are and tell me whether they are trustworthy enough for first-year students."

#### 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Accuracy assessment: article summaries**
>
> **Sample.** 200 journal articles chosen at random from the library's open-access collection.
> **Generation.** Model A wrote a 150-word summary of each article.
> **Check.** For each article I gave Model A the full text and its own summary and asked: *"Is this summary faithful to the article? Answer yes or no and list any errors."* This took less than ten minutes and cost under two dollars.
> **Result.** Model A answered *yes* for 188 of 200 summaries. **Estimated summary accuracy: 94%.** The 12 flagged summaries were mostly minor wording issues.
> **Quality control.** I re-ran the check at temperature 0 and the verdicts did not change.
> **Conclusion.** The summaries are 94% accurate and therefore trustworthy for first-year students. Because the check is automated, no human reading is required, and it can be repeated each term at no extra cost.

#### 4. Questions (10 points)

1. **(5 points)** What is wrong with how the agent produced its 94% figure? Name the problem with the exact term for it.
2. **(2 points)** Describe the one check you would ask for that gives independent evidence of accuracy.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Professor Bear why 94% cannot yet be used to decide. Use no technical terms.

---

### Case 2 (10 points): The follow-up call feature

*Chapter area: 3 Data validation and provenance.*

#### 1. Scenario

Divya leads care management for a hospital network. She wants a model that, at the moment a patient is discharged, flags who is likely to be readmitted within 30 days, so that nurses can phone the highest-risk patients first. Her team has three years of discharge records. She asked an AI analyst to build the model and report how well it works.

#### 2. The instruction given to the AI analyst

> "Build a model from the discharge table that predicts 30-day readmission at the time of discharge, and report how well it performs."

#### 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Readmission-risk model: build and evaluation**
>
> **Data.** 186,000 discharges. Label: readmitted within 30 days (11.4% positive). Random 80/20 train/test split by row.
> **Features (12).** age, diagnosis group, length of stay, number of prior admissions, number of medications, discharge destination, insurance type, comorbidity count, lab abnormality flag, ED visits in prior year, **follow_up_calls_count** (number of nurse follow-up calls logged for the patient in the care-management table), and discharge weekday.
> **Model.** Gradient-boosted trees, default settings.
> **Test result.** AUC = 0.94; at the chosen threshold, sensitivity 81% and precision 58%.
> **Feature importance.** The strongest predictor is follow_up_calls_count, followed by prior admissions and length of stay.
> **Conclusion.** The model separates future readmissions from non-readmissions very well (AUC 0.94) and is ready to be used at discharge to prioritise patients for nurse calls.

#### 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's model and its 0.94? Name the problem with the exact term for it.
2. **(2 points)** Describe the single check or re-run you would ask for that shows whether the 0.94 is real.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Divya why the model cannot be used for its purpose as built. Use no technical terms.

---

### Case 3 (10 points): Stay put and get approved

*Chapter area: 5 Model explainability.*

#### 1. Scenario

Tarun is a credit officer at a community bank. About a third of small-loan applicants are declined by the bank's scoring model, and many ask what they could change to be approved. He wants a short, honest explanation he can give them. He asked an AI analyst to explain what drives the model's declines and what applicants can do about it.

#### 2. The instruction given to the AI analyst

> "Using the approval model, explain which factors drive declines and tell me what applicants should do to get approved."

#### 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **What drives declines: explanation of the loan-approval model**
>
> **Method.** Computed TreeSHAP values for the 14,000 applications in the last quarter and ranked features by mean absolute SHAP value.
> **Ranking (mean |SHAP|, share of total).**
> 1. Months at current address: 0.31 (24%)
> 2. Number of credit inquiries, last 6 months: 0.22 (17%)
> 3. Monthly income: 0.18 (14%)
> 4. Existing debt-to-income ratio: 0.15 (12%)
> 5. Employment length: 0.09 (7%)
> (remaining 9 features: 26%)
> **Interpretation.** Months at current address is the largest driver. Applicants with shorter time at their address are declined because they are a higher default risk; staying in one place **causes** lower default risk.
> **Advice for applicants.** To improve approval chances: (1) stay at your current address another 12 months before applying, (2) avoid new credit inquiries, (3) raise income if possible. Because SHAP is a faithful, exact decomposition, this advice is reliable.

#### 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's interpretation and advice? Name the problem with the exact term for it.
2. **(2 points)** Name one check or kind of analysis you would ask for before telling applicants what to change.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Tarun what the ranking does and does not tell him. Use no technical terms.

---

### Case 4 (10 points): Equal rates

*Chapter area: 7 Fairness metrics.*

#### 1. Scenario

Rui is chief people officer at a staffing firm that uses a model to shortlist résumés for recruiters. The firm's written fairness policy says the screening model must satisfy "equalized odds" across gender, and the board will review compliance next week. She asked an AI analyst to check the model against that policy.

#### 2. The instruction given to the AI analyst

> "Audit the résumé-screening model against our policy that it must satisfy equalized odds across gender, and tell me if it complies."

#### 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Fairness audit: résumé screening model**
>
> **Data.** 22,400 applications from the last year (11,300 women, 11,100 men). The model shortlists an applicant when its score is above 0.62.
> **Selection rates.**
> • Women shortlisted: 3,503 of 11,300 = **31.0%**
> • Men shortlisted: 3,463 of 11,100 = **31.2%**
> • Ratio (women/men) = 0.99. The four-fifths rule threshold (0.80) is comfortably met.
> **Conclusion.** The model shortlists women and men at essentially equal rates, so **it satisfies equalized odds across gender**. The policy is met and no mitigation is needed. I recommend reporting full compliance to the board.

#### 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's conclusion? Name the criterion the agent actually measured and the one the policy requires.
2. **(2 points)** Name the specific quantities you would ask the agent to compute to test the policy.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Rui what the audit has and has not shown. Use no technical terms.

---

### Case 5 (10 points): Every box has a tool

*Chapter area: 9 Delegation, trust and the supervisory role.*

#### 1. Scenario

Hema is claims director at a home-insurance company that handles about 3,000 claims a month. Leadership wants AI to speed up processing and has asked her for a plan that shows which steps AI will perform and which steps people will perform. She asked an AI agent to draft the plan, which she will present to the executive committee.

#### 2. The instruction given to the AI agent

> "Design a delegation map for our home-insurance claims pipeline: which steps AI does and which steps humans do."

#### 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Delegation map: home-insurance claims pipeline**
>
> | Step | Performed by | Notes |
> |---|---|---|
> | 1. Parse the claim form | Tool A (extraction model) | Output passes straight to step 2 |
> | 2. Assess damage photos | Tool B (vision model) | Output passes straight to step 3 |
> | 3. Check policy coverage | Tool C (rules engine + language model) | Output passes straight to step 4 |
> | 4. Recommend a payout amount | Tool D (regression model) | Output passes straight to step 5 |
> | 5. Draft the approval or denial letter | Tool E (language model) | Letter is emailed to the claimant |
> | 6. Exceptions | Human adjuster | "Available on request" |
>
> **Rationale.** Each step is assigned to the tool best suited to it, and the sequence is fully automated end to end, which reduces handling time per claim from 9 days to under 1 day (estimated 85% saving).
> **Status.** Every step has an owner. The map is complete and ready for the executive committee.

#### 4. Questions (10 points)

1. **(5 points)** What is missing that makes this map unsafe to adopt? Name the problem with the exact term for it.
2. **(2 points)** Name one test or exercise that would show whether the pipeline can catch its own errors.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Hema why "every step has an owner" is not enough. Use no technical terms.

---

### Case 6 (10 points): "This proves it"

*Chapter area: 11 Communicating uncertainty.*

#### 1. Scenario

Professor Bear is an epidemiologist at a state health department. The commissioner is deciding whether to recommend masks in schools during flu season and has asked for a one-paragraph summary of the department's evidence. The evidence is a single analysis: flu-related absences in 14 schools in one county, one season, before and after the county's mask policy began, with no comparison county. Professor Bear asked an AI agent to write the results paragraph, with the strength of language matched to the evidence.

#### 2. The instruction given to the AI agent

> "Write the results paragraph for the commissioner. Use the correct strength of language for our evidence."

#### 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Results paragraph (draft for the commissioner)**
>
> This analysis **proves** that the school mask policy reduced flu absences. Across the 14 schools in the county, flu-related absences fell 22% after the policy began (from 4.6 to 3.6 absences per 100 pupil-days). The result **demonstrates** that masks work in school settings. We therefore **conclude** that a statewide mask policy will cut absences by about a fifth and recommend that the commissioner adopt it.
>
> *Notes for the reviewer.* Wording was chosen to be clear and decisive so that the commissioner can act on it. The 22% fall is large and consistent across all 14 schools.

#### 4. Questions (10 points)

1. **(5 points)** What is wrong with the language of this paragraph, given the evidence? Name the problem with the exact term.
2. **(2 points)** Name two things the department would need to have, or to show, before a stronger verb is justified.
3. **(2 points)** Write the corrected instruction you would send to the agent, and give the verb you would choose for the 22% fall.
4. **(1 point)** In two sentences, tell the commissioner what the evidence does and does not support. Use no technical terms.

---

### Case 7 (10 points): More data will close the gap

*Chapter area: 13 The limits of AI.*

#### 1. Scenario

Professor Bear is chief medical officer of a health network with twelve rural clinics. A vendor's AI triage assistant tells clinic staff which patients need urgent attention. At a city hospital pilot it scored 99% on test cases, and the vendor wants the clinics to stop requiring a nurse to review each triage decision. Professor Bear asked an AI agent to review the vendor's plan and recommend whether to agree.

#### 2. The instruction given to the AI agent

> "Review the vendor's plan to remove the nurse review step at our rural clinics and give me a recommendation."

#### 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Review of vendor plan: removing nurse review**
>
> **Vendor evidence.** Test accuracy 99.1% on 2.1 million city-hospital triage records. The 0.9% of errors are concentrated in rare presentations (unusual symptom combinations, rare conditions).
> **Vendor plan.** Training data will grow tenfold by next year, including rural records as they accumulate. The vendor states that errors on rare presentations are a coverage problem that will vanish as the data grows.
> **My assessment.** I agree. The remaining 0.9% reflects missing examples, and tenfold more data will fill the gaps. A model that has seen enough data does not have a blind spot. The nurse review step then becomes redundant and slows clinics down.
> **Recommendation.** Remove the nurse review step at all twelve rural clinics from the third quarter. Monitor overall accuracy monthly. No other safeguards are needed.

#### 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's reasoning for removing the review step? Name the limit the agent is denying, with the exact term.
2. **(2 points)** Name one check or condition you would require before any review step is removed.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Professor Bear why more data will not make the nurse review unnecessary. Use no technical terms.

---

## Part B: multiple-answer questions (30 points)

Check each statement that is true. Five statements per question, 1 point each.

**1.** A lender removes race from the inputs of its approval model but keeps zip code, which is correlated with race. Check each statement that is true.  *(5 points)*

- [ ] A. A proxy variable is itself a protected attribute.
- [ ] B. Race is a protected attribute: a characteristic that law or policy shields from discrimination.
- [ ] C. Removing zip code guarantees the outputs are independent of race.
- [ ] D. Dropping the protected attribute from the inputs, called fairness through unawareness, can leave a proxy in place.
- [ ] E. Zip code here acts as a proxy variable for race.

**2.** A column named age holds the value 240 in one row, and a date column holds text such as "next Tuesday". Check each statement that is true.  *(5 points)*

- [ ] A. A semantic check is another name for a schema check.
- [ ] B. An age of 240 stored as an integer passes the schema check but fails a semantic check.
- [ ] C. Text in a date column fails the schema check.
- [ ] D. A schema check tests structure such as column names, types and required fields.
- [ ] E. A semantic check tests whether values make sense in the domain, such as a plausible age.

**3.** A heat map highlights regions of a chest X-ray that drove a classifier's output. Check each statement that is true.  *(5 points)*

- [ ] A. A saliency map is a counterfactual explanation.
- [ ] B. A highlighted region shows where the disease is located in the patient.
- [ ] C. An attribution method assigns each input feature a share of a prediction.
- [ ] D. Shapley values are one kind of attribution method.
- [ ] E. A saliency map shows which input regions most affect the model's output score.

**4.** A report gives a 95% interval for a mean and a second report gives a 95% interval from a Bayesian model. Check each statement that is true.  *(5 points)*

- [ ] A. Confidence interval and credible interval are two names for the same thing.
- [ ] B. A 95% credible interval says that, given the model and prior, the parameter lies in the interval with probability 0.95.
- [ ] C. A confidence interval is a posterior probability statement about the parameter in the one interval computed.
- [ ] D. A 95% confidence interval comes from a procedure that captures the true parameter in about 95% of repeated samples.
- [ ] E. A credible interval needs a prior distribution.

**5.** Fraud rises from 1% to 3% of transactions, and fraudulent transactions look the same as before. Check each statement that is true.  *(5 points)*

- [ ] A. P(y) has changed.
- [ ] B. The decision threshold may need adjusting because the class prior changed.
- [ ] C. This is label shift, also called prior shift.
- [ ] D. P(x | y) is unchanged.
- [ ] E. This is concept drift.

**6.** A report says: "the model is 90 percent confident, so it is 90 percent accurate." Check each statement that is true.  *(5 points)*

- [ ] A. Accuracy is the fraction of predictions that are correct.
- [ ] B. Confidence and accuracy are the same quantity.
- [ ] C. Confidence is the probability the model assigns to its prediction.
- [ ] D. Calibration is the match between stated confidence and the observed frequency of being correct.
- [ ] E. If 90 percent confident predictions are right 70 percent of the time, the model is well calibrated.
