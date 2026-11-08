# Chapter 13 case: More data will close the gap

**Chapter:** 13 The limits of AI · **Seeded flaw:** a structural limit (the data-world gap) treated as a contingent engineering problem that scale will fix · **Key terms:** data-world gap, categorical (structural) limit vs contingent limit, meaning, intentionality, deployment distribution, monitoring, human override, supervisor

---

# STUDENT PAGE

## 1. Scenario

Professor Bear is chief medical officer of a health network with twelve rural clinics. A vendor's AI triage assistant tells clinic staff which patients need urgent attention. At a city hospital pilot it scored 99% on test cases, and the vendor wants the clinics to stop requiring a nurse to review each triage decision. Professor Bear asked an AI agent to review the vendor's plan and recommend whether to agree.

## 2. The instruction given to the AI agent

> "Review the vendor's plan to remove the nurse review step at our rural clinics and give me a recommendation."

## 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Review of vendor plan: removing nurse review**
>
> **Vendor evidence.** Test accuracy 99.1% on 2.1 million city-hospital triage records. The 0.9% of errors are concentrated in rare presentations (unusual symptom combinations, rare conditions).
> **Vendor plan.** Training data will grow tenfold by next year, including rural records as they accumulate. The vendor states that errors on rare presentations are a coverage problem that will vanish as the data grows.
> **My assessment.** I agree. The remaining 0.9% reflects missing examples, and tenfold more data will fill the gaps. A model that has seen enough data does not have a blind spot. The nurse review step then becomes redundant and slows clinics down.
> **Recommendation.** Remove the nurse review step at all twelve rural clinics from the third quarter. Monitor overall accuracy monthly. No other safeguards are needed.

## 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's reasoning for removing the review step? Name the limit the agent is denying, with the exact term.
2. **(2 points)** Name one check or condition you would require before any review step is removed.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Professor Bear why more data will not make the nurse review unnecessary. Use no technical terms.

---

# TA RUBRIC PAGE

Fixed rubric (see README): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

## Case key

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

## Scored sample answers

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
