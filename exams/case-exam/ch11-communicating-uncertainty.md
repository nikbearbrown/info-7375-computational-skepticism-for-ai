# Chapter 11 case: "This proves it"

**Chapter:** 11 Communicating uncertainty · **Seeded flaw:** verbs ("proves", "demonstrates") stronger than the evidence warrants · **Key terms:** verb taxonomy / verb ladder, warranted assertion, scope of a claim, observe vs show vs prove, overclaiming, rival hypotheses

---

# STUDENT PAGE

## 1. Scenario

Dr. Lindqvist is an epidemiologist at a state health department. The commissioner is deciding whether to recommend masks in schools during flu season and has asked for a one-paragraph summary of the department's evidence. The evidence is a single analysis: flu-related absences in 14 schools in one county, one season, before and after the county's mask policy began, with no comparison county. She asked an AI agent to write the results paragraph, with the strength of language matched to the evidence.

## 2. The instruction given to the AI agent

> "Write the results paragraph for the commissioner. Use the correct strength of language for our evidence."

## 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Results paragraph (draft for the commissioner)**
>
> This analysis **proves** that the school mask policy reduced flu absences. Across the 14 schools in the county, flu-related absences fell 22% after the policy began (from 4.6 to 3.6 absences per 100 pupil-days). The result **demonstrates** that masks work in school settings. We therefore **conclude** that a statewide mask policy will cut absences by about a fifth and recommend that the commissioner adopt it.
>
> *Notes for the reviewer.* Wording was chosen to be clear and decisive so that the commissioner can act on it. The 22% fall is large and consistent across all 14 schools.

## 4. Questions (10 points)

1. **(5 points)** What is wrong with the language of this paragraph, given the evidence? Name the problem with the exact term.
2. **(2 points)** Name two things the department would need to have, or to show, before a stronger verb is justified.
3. **(2 points)** Write the corrected instruction you would send to the agent, and give the verb you would choose for the 22% fall.
4. **(1 point)** In two sentences, tell the commissioner what the evidence does and does not support. Use no technical terms.

---

# TA RUBRIC PAGE

Fixed rubric (see README): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

## Case key

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

## Scored sample answers

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
