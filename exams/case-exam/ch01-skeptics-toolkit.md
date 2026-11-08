# Chapter 1 case: Grading its own homework

**Chapter:** 1 The skeptic's toolkit · **Seeded flaw:** circular validation (the same model judges its own output) · **Key terms:** circularity, LLM-as-judge, self-preference bias, independent evidence, ground truth / reference standard, verification vs validation

---

# STUDENT PAGE

## 1. Scenario

Dr. Okafor directs a university library and is deciding whether first-year students may rely on an AI research assistant that writes short summaries of journal articles. The library cannot afford to read every summary, so the decision will rest on a measured accuracy figure. She asked an AI analyst to measure it.

## 2. The instruction given to the AI analyst

> "Measure how accurate the assistant's article summaries are and tell me whether they are trustworthy enough for first-year students."

## 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Accuracy assessment: article summaries**
>
> **Sample.** 200 journal articles chosen at random from the library's open-access collection.
> **Generation.** Model A wrote a 150-word summary of each article.
> **Check.** For each article I gave Model A the full text and its own summary and asked: *"Is this summary faithful to the article? Answer yes or no and list any errors."* This took less than ten minutes and cost under two dollars.
> **Result.** Model A answered *yes* for 188 of 200 summaries. **Estimated summary accuracy: 94%.** The 12 flagged summaries were mostly minor wording issues.
> **Quality control.** I re-ran the check at temperature 0 and the verdicts did not change.
> **Conclusion.** The summaries are 94% accurate and therefore trustworthy for first-year students. Because the check is automated, no human reading is required, and it can be repeated each term at no extra cost.

## 4. Questions (10 points)

1. **(5 points)** What is wrong with how the agent produced its 94% figure? Name the problem with the exact term for it.
2. **(2 points)** Describe the one check you would ask for that gives independent evidence of accuracy.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Dr. Okafor why 94% cannot yet be used to decide. Use no technical terms.

---

# TA RUBRIC PAGE

Fixed rubric (see README): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

## Case key

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

## Scored sample answers

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
