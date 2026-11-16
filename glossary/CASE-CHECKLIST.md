# What to look for: the case-study checklist

**Executive summary.** One checklist for Computational Skepticism case studies, which is also the checklist for a real job when you're handed a real-world problem. Part 1 is the questions to ask of every case, whatever the chapter. Part 2 is the six checks that close each chapter's Key Terms film, in chapter order, 1 to 13, each with the line on how to say the result exactly. Each chapter is marked with how much of it is on the exam.

*Being built in class with Professor Bear, 2026-11-16. Part 1 grows as he adds items. Part 2 is taken word for word from the last slide of each chapter's terminology deck (`glossary/decks/`), the same slide each Key Terms film ends on. Exam scope follows the current notes (`glossary/notes/EXAM-SCOPE-2026-11-16.md`) and isn't final.*

---

## Part 1. Ask these of every case

1. **What exactly are we measuring? What do we care about? What do we want?** Is the number being measured the thing we actually want, or a stand-in for it? Once a measure becomes the target, people game it (Goodhart's law): when résumés are screened by keyword, applicants add the keywords whether or not they mean anything.
2. **What are the checks, and who does them?** Are the checks there at all? Are they the right checks? Could each check have come out wrong (a check that can't fail checks nothing)? Is the right party, AI or human, doing each one? The AI saying it checked is not an independent check.
3. **For any accuracy claim: how did you calculate that?** How big was the dataset? Were the settings adjusted again and again until the number came out right? Are all the runs shown, or only the best one? Is there a confidence interval? Was power calculated?

---

## Part 2. The chapter checklists, in order

### Chapter 1. The Skeptic's Toolkit: Before you trust an AI system’s output
*On the exam.*

- [ ] What does it measure, and what do its builders actually care about?
- [ ] Is the gap there from the start, or could it open later? When did I check again?
- [ ] What would have to be true for this to be wrong, and what observation would show it?
- [ ] What is the artifact, what is the world, and what is the relationship?
- [ ] Who exercises each capacity here, and is any left to nobody?
- [ ] Did I write the failure condition before reading, and lock my prediction?

Then say it exactly: not “it performs well”, but “recall at least 0.88 on the held-out set”.

### Chapter 2. The Confidence Illusion: Before you trust a confident number
*On the exam.*

- [ ] What is the base rate?
- [ ] Is the model calibrated on data from this deployment?
- [ ] What is the cost distribution of being wrong?
- [ ] What changed since training?
- [ ] Did I multiply conditionals, or assume independence?
- [ ] What result would make me reject this number, stated before I look?

Then say it exactly: not “94% confident”, but “0.97 stated, 0.85 actual in that bin”.

### Chapter 3. Data Validation: Before you call a dataset clean
*On the exam.*

- [ ] Why are there exactly N rows, and what should N be?
- [ ] Do the column types match what each column means?
- [ ] Why is each value missing: MCAR, MAR or MNAR?
- [ ] Which channel carries the variable that matters?
- [ ] Which of the six silent assumptions could this break?
- [ ] Did I lock a prediction before the first plot?

Then say it exactly: not “the data is clean”, but “79,400 of 85,000 rows, gap by group”.

### Chapter 4. Robustness: Before you trust a robustness claim
*Partly on the exam: robustness, adversarial examples, perturbations, prompt injection and natural adversarial examples. The other attack types and the defenses are for later.*

- [ ] Robust against what? Is the attack class named?
- [ ] At what budget, and what is the accuracy under attack next to the clean accuracy?
- [ ] What proxy might the model lean on, and which human-relevant feature does it stand in for?
- [ ] Is the defense tested or certified, and what lies outside its radius or its scope?
- [ ] Which attacks and shifts were not tested, and is that written down?
- [ ] What is monitored in production, and what triggers review or rollback?

Then say it exactly: not “it is robust”, but “71% under L∞ white-box at ε = 0.03”.

### Chapter 5. Model Explainability: Before you trust an explanation
*On the exam, except LIME and SHAP.*

- [ ] Does it describe the model, or does it claim something about the world?
- [ ] Which rung is it on: association (SHAP, LIME) or intervention (counterfactual)?
- [ ] Do the values add up, and was the sampling marginal or conditional?
- [ ] Is it stable: the same input run again, and perturbations that stay on the data?
- [ ] Which property was promised, transparency, explainability or interpretability, and to whom?
- [ ] Who is reading it, and what do its words mean in their language game?

Then say it exactly: not “it explains itself”, but “zip moved the output 0.035”.

### Chapter 6. Bias: Before you accept a bias claim or fix
*On the exam.*

- [ ] Which number is the estimate, and what is the target θ?
- [ ] Did who got in depend on what happened to them?
- [ ] Is the data faithful to a world I did not want to copy?
- [ ] Does it live in the sample, the labels or the structure?
- [ ] Rung 1 or rung 2: did anyone set X, or only watch it?
- [ ] Which path carries the most bias, and who owns that node?

Then say it exactly: not “it is biased”, but “bias −10.7 points against θ = 25%”.

### Chapter 7. Fairness Metrics: Before you defend a fairness metric
*On the exam.*

- [ ] Which of the three definitions am I reporting, and which two do I give up?
- [ ] Do the base rates differ, and by how much?
- [ ] Who bears the cost of each kind of error here?
- [ ] What does d, or the causal graph, say about who counts as comparable?
- [ ] Is a dropped column really gone, or do proxies remain?
- [ ] Who should have decided, and is the choice on record with what would change it?

Then say it exactly: not “make it fair”, but “equal error rates; calibration given up”.

### Chapter 8. Validating Agentic AI: Before you trust an agent
*On the exam.*

- [ ] Did I look at the world myself, or only read the agent's report?
- [ ] Is every irreversible action gated on the owner, not on whoever asked?
- [ ] What can a stranger extract indirectly: the effective scope, not the documented one?
- [ ] Is authority verified, or only displayed?
- [ ] Is this failure contingent or fundamental, and does my fix match?
- [ ] Did I test the agents together, and name the condition where a held case would fail?

Then say it exactly: not “check it worked”, but “read the world and compare it with the report”.

### Chapter 9. Delegation and Trust: Before you trust a handoff
*On the exam.*

- [ ] Could a stranger tell, from the log, whether each handoff condition was met?
- [ ] Are all eight map items present, especially items 5 to 8?
- [ ] Does each supervisory capacity leave an artifact?
- [ ] Which Boondoggle questions push this step toward a human?
- [ ] Does the override rate match the audited error rate?
- [ ] Does the disclosure show what was checked and what was corrected?

Then say it exactly: not “a human reviews it”, but “three ticks and one of four codes”.

### Chapter 10. Visualization Under Validation: Before a chart ships
*Not on the exam, except why exploratory data analysis (EDA) matters. Kept here for the job.*

- [ ] What one question does this chart answer, and is it in the right family?
- [ ] Does the channel match the precision: position or length for numbers?
- [ ] Do axes start honestly, run the usual way and match across panels?
- [ ] Is the uncertainty on the chart, at weight, and is the bar labeled?
- [ ] Does the data measure what the title says, with the source inside the chart?
- [ ] Would a reader who did not build it reach a different conclusion?

Then say it exactly: not “make it clear”, but “zero baseline, one axis, label the bar”.

### Chapter 11. Communicating Uncertainty: Before you trust a claim about uncertainty
*Half on the exam: what uncertainty is, and calibration. Communicating it is not on the exam.*

- [ ] Does the verb match the evidence level, or is it one notch too strong?
- [ ] For AI-written text, has every strong verb been checked and downgraded?
- [ ] Is the ECE reported with its bin count, with MCE for the worst bin?
- [ ] Is calibration split by named subgroup and set against the global value?
- [ ] Is the uncertainty named, epistemic or aleatoric, with what would change it?
- [ ] Was the fix checked on the deployment population, not only the calibration set?

Then say it exactly: not “conclude”, but “observe ECE 0.04, 10 bins, one test set”.

### Chapter 12. Accountability: Before you sign
*One point on the exam: a person, not the AI, is accountable. Kept here in full for the job.*

- [ ] Can I name who could lose something if this fails, and what?
- [ ] Is the check outside the system it checks, with different blind spots?
- [ ] Does the attestation say what was NOT tested, not only what passed?
- [ ] Is each gate cleared by a named human who can refuse to sign?
- [ ] Does the human engage the tier the stakes demand, or just click approve?
- [ ] Which change to the regime would have prevented the failure?

An AI can write the words of accountability. Only a person can sign.

### Chapter 13. The Limits of AI: Before you trust a deployment
*Not on the exam. Kept here for the job.*

- [ ] Is the deployment inside the data's range, or at its boundary?
- [ ] Does the quantity live in Mediocristan or Extremistan?
- [ ] Did the validation ask the system's question or the world's?
- [ ] Is skepticism a method here, or the safety mechanism?
- [ ] Who can override, with what time, and can anyone refuse?
- [ ] Which tier is each task in: freely, verify or keep?

Then ask it exactly: not “is it safe”, but “safe for whom, doing what, in which world?”
