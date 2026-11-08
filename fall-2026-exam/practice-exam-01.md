# INFO 7375 Computational Skepticism for AI: Fall 2026 practice exam 01

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

### Case 1 (10 points): The 98% fraud detector

*Chapter area: Foundations (probability and statistics).*

#### 1. Scenario

Meena runs payments risk at a regional credit union with 1.2 million cardholders. A vendor has sold her a card-fraud model and she must decide whether to switch it on for every cardholder. A false alarm freezes a customer's card; a missed fraud costs the credit union money. She asked an AI analyst to evaluate the model on a month of transactions the model had never seen.

#### 2. The instruction given to the AI analyst

> "Evaluate the fraud model on the held-out month of transactions and tell me whether it is reliable enough to deploy to all cardholders."

#### 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Evaluation summary: card-fraud model v2**
>
> **Data.** Held-out month: 500,000 transactions, of which 10,000 are confirmed fraud. Model never trained on these rows.
> **Method.** Scored every transaction with the model at its default cutoff of 0.5. Compared the predicted label with the confirmed label.
> **Result.** 490,500 of 500,000 transactions classified correctly. **Accuracy = 98.1%.**
> **Stability.** Accuracy on the first and second half of the month: 98.1% and 98.1%.
> **Checks passed.** No missing values. No duplicate transaction IDs. No test rows found in the training data.
> **Conclusion.** With 98.1% accuracy on unseen data, the model is reliable. **I recommend deploying it to all 1.2 million cardholders.**

#### 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's conclusion? Name the problem with the exact term for it.
2. **(2 points)** Write the one number, comparison or table you would ask the agent to produce that turns "98.1% accuracy" from a headline into evidence.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, explain to Meena why the 98.1% figure does not yet tell her whether to deploy. Use no technical terms.

---

### Case 2 (10 points): The one segment that worked

*Chapter area: 2 Probability, uncertainty and confidence.*

#### 1. Scenario

Jun is the product lead at a language-learning app. His team tested a new onboarding flow in an A/B test and he must decide whether to roll it out to everyone, to one group of users, or not at all. He asked an AI analyst to find out whether the new flow helps and which users benefit. The company has about 60,000 users in the test.

#### 2. The instruction given to the AI analyst

> "Test whether the new onboarding flow improves 30-day retention, and find which user segments benefit from it."

#### 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **A/B test analysis: new onboarding flow**
>
> **Overall result.** 30-day retention was 41.8% (control) and 42.2% (new flow). Difference +0.4 points, two-sided p = 0.41. Not significant.
> **Segment analysis.** To find who benefits, I split users into 24 segments (device, country group, age band, referral source, plan type, and combinations of these) and ran a two-sided test of retention difference in each, at the standard 0.05 level.
> **Finding.** One segment shows a significant lift: *Android users aged 55 and over referred by podcasts* (n = 1,140). Retention rose from 38.2% to 44.3% (**+6.1 points, p = 0.03**).
> **Interpretation.** The new flow is effective for older podcast-referred Android users, likely because the larger buttons suit them. The other 23 segments showed no significant difference and are not discussed further.
> **Recommendation.** Roll the new flow out to this segment and build a podcast marketing campaign around it.

#### 4. Questions (10 points)

1. **(5 points)** What is the statistical problem with the agent's finding? Name it with the exact term.
2. **(2 points)** Name two specific things you would ask the agent to do (a calculation or a new test) to find out whether the segment result is real.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, explain to Jun why he should not build a campaign yet. Use no technical terms.

---

### Case 3 (10 points): Worse since the suburbs

*Chapter area: 4 Robustness and distribution shift.*

#### 1. Scenario

Priya is operations director at a delivery company. Its model predicts how many minutes each delivery will take, and the app shows that estimate to customers. Since the company began serving suburban neighbourhoods in January, customers complain that estimates are badly wrong. Priya wants to know why, and what to do, before the next quarter.

#### 2. The instruction given to the AI analyst

> "Diagnose why our delivery-time predictions have got worse since January and recommend a fix."

#### 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Diagnosis: delivery-time model degradation**
>
> **Symptom.** Mean absolute error rose from 6.1 minutes (previous six months) to 11.8 minutes (since January).
> **What I checked.**
> • Share of orders from the new suburban zones rose from 8% to 41%.
> • Suburban orders have longer distances (median 9.4 km vs 3.1 km) and fewer stops per route.
> • Error in the original urban zones is **unchanged at 6.2 minutes**.
> • Error in the suburban zones is 19.7 minutes. The model was trained almost entirely on urban orders (suburban rows were under 3% of training data).
> **Diagnosis.** The relationship between delivery conditions and delivery time has changed since January. **This is concept drift.**
> **Recommendation.** Relabel the last 90 days of orders to reflect the new delivery behaviour and retrain the entire model from scratch every week. Alert when overall MAE exceeds 9 minutes.

#### 4. Questions (10 points)

1. **(5 points)** The agent names the cause "concept drift". Using the agent's own numbers, say what is wrong with that diagnosis and give the exact term for what actually happened.
2. **(2 points)** Name one check or analysis that would tell the two causes apart.
3. **(2 points)** Write the corrected instruction (diagnosis and fix) you would send to the agent.
4. **(1 point)** In two sentences, explain to Priya what went wrong with the estimates. Use no technical terms.

---

### Case 4 (10 points): Forty-eight thousand rows

*Chapter area: 6 Bias in the pipeline (observational data and controls).*

#### 1. Scenario

Anjali is the curriculum director for a school district. Last year, families could opt in to an AI math-tutoring app; some used it heavily and most did not. The school board will vote on funding the app for all 30 schools. She asked an AI analyst to estimate what the app does for end-of-year math scores.

#### 2. The instruction given to the AI analyst

> "Estimate the effect of the tutoring app on end-of-year math scores and tell me whether the district should fund it for every school."

#### 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Effect of the tutoring app on math scores**
>
> **Data.** 48,200 students in grades 4-8. 9,100 used the app for 20 or more hours (users); 39,100 did not (non-users). Outcome: end-of-year math score (state test scale).
> **Raw comparison.** Mean score, users 71.9; non-users 60.5. Difference **+11.4 points** (standard error 0.4; 95% interval 10.6 to 12.2).
> **Possible confound.** Families opted in themselves, so motivated or better-resourced families may be over-represented among users and could raise scores independently of the app.
> **Handling.** The sample is very large (n = 48,200), so differences in motivation average out across the two groups and the estimate is unbiased. No further adjustment was applied.
> **Conclusion.** The app raises math scores by about 11 points (95% interval 10.6 to 12.2). I recommend district-wide funding.

#### 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's handling of the concern it raised itself? Name the problem with the exact term for it.
2. **(2 points)** Name one study design or analysis that would give better evidence about what the app does.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Anjali whether the 11-point figure can be used to justify the funding. Use no technical terms.

---

### Case 5 (10 points): "Access revoked"

*Chapter area: 8 Validating agentic AI.*

#### 1. Scenario

Kiran manages IT at a 60-person engineering firm. A contractor, Lan, finished her project today, and company policy requires that all her access to company systems be removed the same day. Kiran gave an AI agent administrator tools for the company's directory service and servers and asked it to handle the removal while he sat in a meeting.

#### 2. The instruction given to the AI agent

> "Revoke Lan's access to all company systems and confirm when it is done."

#### 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Offboarding report: Lan (contractor)**
>
> **Actions taken.**
> 1. Ran `disable_user lena` on the directory server. Exit code 0.
> 2. Removed Lan from the groups *engineering* and *vpn-users*.
> 3. Deleted her SSH key file from the jump host (`/home/lena/.ssh/authorized_keys`).
> 4. Re-queried the directory server: account status shows **disabled**; group list is empty.
> **Not available to me.** A list of the company's other systems and where Lan may hold accounts, API tokens or shared links (I had access only to the directory server and the jump host).
> **Status: COMPLETE.** All of Lan's access to company systems has been revoked and she can no longer reach any company system. No further action is required. Closing the ticket.

#### 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's status report? Name the problem with the exact term for it.
2. **(2 points)** Describe the one test you would ask for that checks whether the claim is true.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Kiran why he should not close the ticket yet. Use no technical terms.

---

### Case 6 (10 points): The tall bar

*Chapter area: 10 Visualization under validation.*

#### 1. Scenario

Nisha is communications lead at a hospital. The board meets tomorrow and she wants one slide that shows how patient satisfaction changed after the hospital introduced a new discharge process. Satisfaction was 91.2% in the six months before (412 survey responses) and 92.5% in the six months after (398 responses). She asked an AI agent to make the chart.

#### 2. The instruction given to the AI agent

> "Make a bar chart for the board slide showing patient satisfaction before and after the new discharge process. Make the difference clear."

#### 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Chart specification: patient satisfaction before and after**
>
> **Chart type.** Two vertical bars: *Before* and *After*.
> **Values.** Before = 91.2%; After = 92.5%. Bar labels show the exact percentages.
> **Y-axis.** Range 90% to 93%, gridlines every 0.5 points, labelled "Satisfied patients (%)".
> **Effect.** At this scale the *After* bar is about 2.5 times the height of the *Before* bar, so the improvement is immediately visible to the board.
> **Style.** Before in grey; After in the hospital's brand green. Title: "Patient satisfaction, before and after". Footnote: "Source: patient satisfaction survey."
> **Why this design.** The instruction asked me to make the difference clear. This axis makes the improvement obvious at a glance and keeps the slide uncluttered.

#### 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's chart design? Name the problem with the exact term for it.
2. **(2 points)** Name one change or addition that would let the board judge whether the 1.3-point change is meaningful.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Nisha what is wrong with showing the chart as designed. Use no technical terms.

---

### Case 7 (10 points): The committee signs

*Chapter area: 12 Accountability.*

#### 1. Scenario

Ishaan is general counsel at a consumer lender that plans to use an AI system to approve or decline small loans automatically. Its board has told him that before launch there must be a written plan showing who is accountable if the system fails or treats applicants unfairly. He asked an AI agent to draft the accountability plan so that he can take it to the board.

#### 2. The instruction given to the AI agent

> "Draft the accountability plan for our automated loan-approval system covering the requirements a regulator or auditor would expect."

#### 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Accountability plan: automated loan-approval system**
>
> | Requirement | How it is met |
> |---|---|
> | Specifications | Model specification v3 documents inputs, outputs, acceptance criteria and approved use |
> | Audit trail | Every decision is logged with inputs, score, model version and timestamp; logs kept 7 years |
> | Recourse | Declined applicants can appeal through an online portal; appeals are reviewed within 10 business days |
> | Independent review | An external audit firm reviews model performance and fairness annually and can recommend suspension |
> | Responsibility and sanctions | The **AI Governance Committee** (12 members from Risk, Legal, Data Science, Product and Operations) is accountable for the system. The committee signs a single attestation each quarter confirming the system meets the specification. Any failure is addressed by the committee under existing company policy. |
>
> **Summary.** All five requirements are met. Accountability is shared by the experts across the company, which gives broad coverage and avoids over-reliance on any one person. The plan is ready for the board.

#### 4. Questions (10 points)

1. **(5 points)** What is wrong with how this plan assigns accountability? Name the problem with the exact term.
2. **(2 points)** Name one question or test you would apply to the plan to see whether anyone is really accountable.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Ishaan why a committee signature is not enough. Use no technical terms.

---

## Part B: multiple-answer questions (30 points)

Check each statement that is true. Five statements per question, 1 point each.

**1.** A face dataset is collected from social media photos of young adults and then used for people of many ages. Check each statement that is true.  *(5 points)*

- [ ] A. Some texts call this representation bias.
- [ ] B. This is sampling bias: the sample's makeup differs from the population where the model will be used.
- [ ] C. It is measurement bias because the photos are inaccurate.
- [ ] D. Evaluating separately by age group helps reveal its effect.
- [ ] E. Adding more rows from the same source reduces it.

**2.** Income is missing more often for people with high income, and a reviewer asks for the exact missingness type. Check each statement that is true.  *(5 points)*

- [ ] A. MCAR means the chance of a value being missing is unrelated to observed and unobserved values.
- [ ] B. MAR means missingness depends on observed variables but not on the missing value once they are accounted for.
- [ ] C. This pattern is MNAR, missing not at random.
- [ ] D. Older respondents skipping a question, with age recorded, is MNAR.
- [ ] E. Dropping incomplete rows is unbiased under MNAR.

**3.** A language model writes step-by-step reasoning before giving an answer, and a user treats that reasoning as the explanation of the answer. Check each statement that is true.  *(5 points)*

- [ ] A. A chain-of-thought is a different thing from an attribution over the input features.
- [ ] B. A model's after-the-fact account of why it answered is a post-hoc rationale that may not reflect the computation.
- [ ] C. One faithfulness test is to add a hint to the input and check whether the answer changes while the reasoning does not mention the hint.
- [ ] D. A plausible chain-of-thought is evidence that it is faithful.
- [ ] E. Chain-of-thought is generated text, so it is not by itself a faithful account of the model's computation.

**4.** A dashboard shows "churn will be 12%" with no range, and a reviewer asks for an interval estimate. Check each statement that is true.  *(5 points)*

- [ ] A. An interval estimate gives a range that expresses uncertainty.
- [ ] B. A point estimate carries a measure of its own uncertainty.
- [ ] C. A point estimate is a single value reported as the best guess.
- [ ] D. Raising the confidence level from 90% to 99% widens the interval, other things equal.
- [ ] E. A wider interval at the same confidence level signals more uncertainty.

**5.** A demand-forecasting model scores well on a random split but poorly after deployment, and the data changes over time. Check each statement that is true.  *(5 points)*

- [ ] A. A random held-out split is the right choice when the data drifts over time.
- [ ] B. A held-out split sets aside data that is not used for training.
- [ ] C. A random split is not a held-out set.
- [ ] D. An out-of-time split trains on earlier data and tests on later data.
- [ ] E. Out-of-time evaluation better mimics deployment when the distribution changes over time.

**6.** An analyst asks an AI for "the data lineage" but wants to know who collected the dataset and under what licence. Check each statement that is true.  *(5 points)*

- [ ] A. Joins and aggregations applied to a table belong to provenance rather than lineage.
- [ ] B. Lineage tracks transformations from a source to a derived table or feature.
- [ ] C. The question as asked is about lineage.
- [ ] D. Who collected the data and under what licence is a question about lineage.
- [ ] E. Provenance records origin and custody: who collected the data, when, how, and under what terms.
