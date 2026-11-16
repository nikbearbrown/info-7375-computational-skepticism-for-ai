# Exam preparation guide: INFO 7375: Computational Skepticism for AI

> **Format update, 2026-11-15:** Nik specified 5 case-style questions × 10 points = 50, plus 10 multiple-answer questions × 5 points = 50. Total: 100. Existing practice papers and their keys are preserved as historical 7-case/6-multiple-answer exercises, not current-format mock exams. The new [exam generator prompt](EXAM-GENERATOR-PROMPT.md) is a local draft with a representative independent assistant-agent check, not a live Claude Project test.

**Student-facing draft for instructor review.** Learn to direct an AI analyst and audit the strength of its conclusions. Use this guide for preparation, not as a prediction of examination questions. It follows the supplied guide’s six-part structure, with course-specific review, vocabulary and audit questions.

## Start here: format and scoring

The current instructor-specified format is **100 points: five cases × 10 = 50, plus ten multiple-answer questions × 5 = 50**. Each case asks **five specific questions tied to that case**, not an open-ended essay: Q1 identifies and justifies a real defect (3), Q2 names and applies its precise term (2), Q3 requests evidence (2), Q4 gives a correction or next step (2), and Q5 explains the consequence plainly (1).

The current public rubric accepts a real defect other than the author’s intended one when it is justified from the case. Your evidence, fix and explanation must address your chosen defect. If no real defect with a reason is identified, the case is capped at 5/10; that is a ceiling, not an automatic score. Do not substitute a cosmetic nitpick for a consequential problem. See the [public rubric](README.md) for details.

The public exam overview names foundations plus chapters 1–13 for cases, and foundations plus chapters 1–7 for the multiple-answer bank. Use the course reading map: the manuscript contains alternate chapter numbers, so a filename alone is not a reliable syllabus.

## 1. What the evidence says

The attached guide is the structural starting point for this plan. The broad study principles below are useful, but the exact schedule is advice, not an experimentally validated recipe for this examination. Numerical effect sizes and precise optimal spacing claims from the source draft are not repeated because they have not been rechecked here against the original papers.

| Technique | Evidence and limitation | Application |
|---|---|---|
| Retrieval practice | Broad support for attempting to recall and then receiving corrective feedback [1,3]. It is not proof that every practice design transfers. | Answer before opening the key; explain the reason after checking. |
| Spacing | Distributed practice is well supported; useful gaps depend on the material and retention interval [1,2]. | Revisit difficult concepts on several days rather than one long session. |
| Interleaving | Benefits depend on the material and similarity of categories [4]. | Mix confusable case types after learning their basic distinctions. |
| Comparing cases | Comparing examples can support abstraction [5]. | State the deciding rule between two similar concepts, not just two definitions. |
| Worked examples | Helpful scaffolding, especially early; support should fade with understanding [6]. | Study one public example, finish a partial answer, then solve independently. |
| Correcting confident errors | Feedback can correct high-confidence mistakes; correction may not persist without later retrieval [7]. | Record confidence and retest important errors after a delay. |
| Pretesting | A first attempt can direct later study [8]. | Try an unfamiliar public question before reading its explanation; low first scores are diagnostic. |
| Multiple true-false practice | Evaluates individual propositions and can reveal partial misconceptions [9]. | Judge each option by its meaning, not by the pattern of other answers. |
| Audit checklists | Results depend on the task and checklist; a checklist is not proof of correctness [10]. | Use the short course-specific questions below, then justify your conclusion. |
| Partner practice and timed writing | Practical advice rather than a validated treatment for this exam [11,12]. | Exchange answers and check against the public rubric; rehearse the announced medium. |
| Sleep | Sleep habits correlate with performance; the cited study does not establish a causal guarantee [13]. | Protect a sustainable sleep schedule across preparation. |
| Writing about worries | Evidence is mixed, and the supplied draft relied on secondary reporting [14]. | Optional; do not substitute it for practice or support you already find useful. |

Targeted rereading is useful when it repairs a gap. The recommendation is not “never reread,” but “do not mistake familiarity for being able to answer.” Begin untimed if the mechanism is new; add timing once you can explain it.

## 2. Study plans

### Set the budget and record what you learn

Earlier practice timing estimates applied to the historical 7-case/6-question papers and should not be treated as timing for the revised format. Use the time printed on the examination and any approved accommodations.

Allocate time from the actual examination instructions, not from a universal formula. Keep some checking time. A missed case should not prevent attempts at the remaining questions. Practise on paper if that is the announced format; confirm permitted materials with the instructor.

Keep an **error log** with: item; your answer; confidence; corrected reasoning; the decisive fact or qualifier; a short rule; next retest date. Keep a **pair list** of terms you confuse. Do not write only the answer letter: record why it is correct.

### Fourteen-day plan

These are adjustable study sessions, not required workloads. Include breaks and adapt around other commitments.

| Day | Work | Suggested duration |
|---|---|---|
| 1 | Attempt public practice 01 cold; then check it and start both logs. | Exam-length sitting plus review |
| 2 | Review cluster 1 below; make two-direction term cards; explain a public worked answer. | 60–75 min |
| 3 | Review cluster 2; complete Q1 independently, then add Q2–Q5 without the key. | 60–75 min |
| 4 | Review cluster 3; answer two cases and ten individual T/F statements. | 60–75 min |
| 5 | Retest confident errors; rewrite vague evidence requests and next instructions. | 45–60 min |
| 6 | Review clusters 4–5; mix cases from different areas. | 60–75 min |
| 7 | Rest or brief spaced retrieval from the pair list. | 0–20 min |
| 8 | Attempt public practice 02 cold, then score every rubric row. | Exam-length sitting plus review |
| 9 | Revisit the oldest errors. Explain why the tempting alternative is not supported. | 45–60 min |
| 10 | Create two new scenarios from public lessons, each with one deliberate defect. Exchange with a peer. | 60–75 min |
| 11 | Practise individual T/F reasoning and two cases from the weakest clusters. | 60–75 min |
| 12 | Full rehearsal using unused public questions or your peer-created set; do not assume a third full case paper exists. | Exam-length sitting plus review |
| 13 | Retest the most consequential remaining errors and explain one mechanism aloud. | 30–45 min |
| 14 | Light retrieval, check logistics, and protect sleep. | 20–30 min |

Course-specific clusters:
1. Probability, calibration and baselines.
2. Data provenance, missingness and evaluation.
3. Robustness, explanations and bias.
4. Fairness criteria and group metrics.
5. Agent verification, delegation, visualization, uncertainty and accountability.

When repeating a question, explain the reasoning before recalling the answer. A familiar score is not evidence that you can transfer the concept to a new case.

### Three-day version

| Day | Work |
|---|---|
| 1 | Diagnose with practice 01. Review the two weakest clusters and make cards only for important gaps. |
| 2 | Solve several mixed cases; inspect feedback; retest earlier mistakes after a break. Practise the full five-question response. |
| 3 | Rehearse with practice 02, review remaining gaps, and stop intensive work early enough to rest. |

Short preparation cannot reproduce two weeks of spacing. Focus on accurate reasoning and targeted reading rather than memorizing complete answers.

## 3. Part A routine: audit the claim

1. Underline the requested action, constraints and decision the person must make.
2. Identify the output’s consequential claims. Distinguish observation, interpretation and recommendation.
3. Compare each claim with the supplied evidence. What is missing, contradictory or stronger than the evidence permits?
4. Choose a substantive defect supported by the case. Quote the relevant fact and name the mechanism. Do not invent unseen facts to make the diagnosis work.
5. Keep the check, next instruction and plain explanation aimed at that same defect.

### Course-specific audit questions

- **Claim:** What result is asserted, and what observation would count against it?
- **Denominator and baseline:** What population, time window, class balance and comparison define the number?
- **Data frame:** Which records were included, joined, dropped or measured after the prediction time?
- **Evaluation:** Was the evidence used to choose the model also used to claim final performance?
- **Uncertainty:** What assumptions justify the interval, probability or causal interpretation?
- **Explanation and fairness:** Which precise criterion was actually measured? Does it support the claim being made?
- **Visualization:** What do axes, aggregation, baselines and omitted variation make easy to miss?
- **Supervision:** What final state, independent evidence and accountable review support the action?

### Write five short answers to the case-specific questions

| Probe | What to write | Self-check |
|---|---|---|
| Q1: defect and reason (3) | “The claim … is not supported because … .” Use the supplied case facts. | Can a marker locate the fact and see why it matters? |
| Q2: precise term (2) | Name the taught concept and explain how it applies to the defect you chose. | Does the term fit this case rather than merely sound relevant? |
| Q3: evidence (2) | One concrete test, comparison or inspection and what result would support or defeat the claim. | Could this check reveal that the claim is wrong? |
| Q4: next instruction (2) | Tell the agent what to do, within which limits, and what to report. Ask for necessary clarification if proceeding would exceed authority. | Does it address your defect rather than offer generic advice? |
| Q5: plain explanation (1) | Tell the named person what they can rely on now, what remains uncertain, and why it matters. | Can a non-expert act on it without learning your jargon? |

A test needs an observable outcome, not necessarily a numerical threshold. An evidence request is not “ask the agent whether it is sure.” A correction is not “be more careful.” Short bullets are fine where the paper permits them.

**Practice prompt:** An analyst says a campus shuttle is more reliable because its average delay fell. List what you would need to know about cancellations and the distribution of delays before accepting that conclusion. This is a study prompt, not an exam answer.

### Short drills

- **Diagnosis drill:** From a public lesson, state one claim, its limit and the precise term in one minute.
- **Evidence drill:** Write a check that distinguishes a correct result from a convincing but wrong one.
- **Instruction drill:** Give one bounded, executable next step with a report requirement.
- **Translation drill:** Explain the same issue without jargon, without changing its meaning.

For a calculation, state the population and assumptions before using the formula. For a philosophical or structural claim, distinguish the argument from what the supplied observation actually establishes. Use the reading-map notes where manuscript versions disagree.

If a public key appears technically wrong, record the disputed wording and your reasoning, then ask the instructor. Do not memorize a contradiction simply because it is in a key. This guide does not replace grading policy.

## 4. Part B routine: use the terms precisely

For each pair, make a card with a definition, deciding question, original example and non-example. Practise both directions: term to explanation, and scenario to term. Start with these review distinctions, then extend them using the instructor’s glossary.

| Terms | Deciding distinction |
|---|---|
| Accuracy / precision / recall | All correct predictions, correct among predicted positives, or caught among actual positives? Write the denominator. |
| Calibration / accuracy | Do probabilities match observed frequencies, or are decisions correct? These answer different questions. |
| Association / causal effect | Was a relationship observed, or is there evidence for what changing an exposure would do? Name the design assumptions. |
| Selection bias / confounding | Who entered the analysis, or what common causes distort the comparison? Both can occur. |
| Overfitting / information leaking from the test rows | Did choices fit the evaluation sample too closely, or did information from the test rows reach training (the book: preprocessing before the split "leaks information")? |
| Selection bias / sampling bias | Did a rule or query decide who got in, or was one group simply harder to reach? |
| Explainability / interpretability | Does the output come with a reason, or can a person build a working understanding from it? |
| Demographic parity / equalized odds | Equal selection rates, or equal true- and false-positive rates conditional on outcomes? |
| Type I / Type II error | Rejecting a true null hypothesis, or failing to reject a false one? |
| Provenance / schema | Where did the data come from and on what terms, or how are the columns defined and what was done to them in the pipeline? (Chapter 3: the schema-and-provenance assumption.) |
| Not significant / no effect | Was the evidence against "no effect" weak, or is there evidence of no effect? ("Failing to reject is not proof of no effect.") |
| Delegation / accountability | Who performs work, and who owns the decision, review and consequences? |

These are study aids, not a complete syllabus or a claim that these particular terms will appear. Prefer the course’s explicitly stated usage, but ask about a factual conflict or a term whose meaning varies across fields.

### Judge each statement independently

1. Identify the claim and its qualifiers.
2. Work out whether the stated conditions are enough. For a number, verify the denominator, units and assumptions.
3. Use a counterexample when evaluating a universal claim. “Always” is not automatically false, and a cautious-sounding sentence is not automatically true.
4. Mark the statement according to its meaning and the printed marking instructions, not a guessed answer pattern.
5. During review, explain why the nearest wrong alternative fails. Retest high-confidence errors later.

The published rules score each of the five statements separately: correctly checked true and correctly left-blank false statements each earn one point. Follow the actual examination’s instructions if revised.

## 5. Common mistakes and fixes

| Mistake | Better practice |
|---|---|
| Remembering the answer rather than the mechanism | Explain an unfamiliar example and a counterexample. |
| Giving only “bias,” “bug” or “unreliable” | State the specific defect, case evidence and precise term. |
| Inventing missing details | State what is unknown and what evidence would settle it. |
| Naming many shallow defects | Develop one consequential, defensible defect coherently. |
| Proposing an unrelated test | Ask whether your check could expose the defect you identified. |
| Treating completion as verification | Identify the observable result and the appropriate source of evidence. |
| Giving an unrestricted “fix everything” instruction | Bound the change and require a specific report or confirmation. |
| Writing technical jargon to a non-expert | Explain the practical consequence in ordinary language. |
| Using an AI answer as proof of understanding | Attempt cold first, then critique help against public sources. |
| Spending the whole sitting on early cases | Use the announced timing and return to difficult items. |
| Treating a study schedule as an exam rule | Check the instructor’s current announcements, accommodations and examination sheet. |

### Final self-check

Can you name a claim, give a reason it is unsupported, use a precise term, ask for discriminating evidence, and give a bounded next step? Can you explain a mistaken T/F choice without looking at its key? If not, return to the relevant lesson and practise that mechanism rather than rereading everything.

## 6. Sources and course resources

### Use the public course materials

- [Exam overview and rubric](README.md).
- [Practice exam 01](practice-exam-01.md) and [practice exam 02](practice-exam-02.md). Open each matching key only after attempting the student file.
- [Reading map](../docs/reading-map.md), [course reading selections](../course.json), and [probability and statistics](../probability-statistics/README.md).
- The exam overview links the tested glossary and additional public multiple-answer bank. Their legacy filenames may say “midterm”; this document is an **exam preparation guide**, not a new midterm specification.

This guide uses the public overview as inspected on 9 November 2026. It does not reproduce private examination questions, solutions, topic allocations or answer patterns. The instructor’s current examination sheet controls scope, duration and permitted materials.

### Research behind the preparation structure

These references come from the supplied study-guide draft. They support general study principles, not a guarantee of a score or the exact schedule above. The original papers and all links have not been independently revalidated in this adaptation; secondary-source limitations are retained. Quantitative claims from the draft have deliberately been omitted.

1. Dunlosky et al. (2013), *Improving Students’ Learning With Effective Learning Techniques*. DOI: [10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266). Broad review of study strategies.
2. Cepeda et al. (2008), *Spacing effects in learning*. [PubMed](https://pubmed.ncbi.nlm.nih.gov/19076480/).
3. Pan & Rickard (2018), *Transfer of test-enhanced learning*. [Author PDF](https://sc-pan.github.io/pdf/PR_2018.pdf).
4. Brunmair & Richter (2019), *Similarity matters: a meta-analysis of interleaved learning*. [PubMed](https://pubmed.ncbi.nlm.nih.gov/31556629/).
5. Alfieri, Nokes-Malach & Schunn (2013), *Learning through case comparisons*. [Author PDF](https://www.lrdc.pitt.edu/Schunn/papers/ContrastingCasesMeta-AlfieriEtAl2013.pdf).
6. Salden et al. (2010), *The expertise reversal effect and worked examples in tutored problem solving*. [Research record](https://researchportal.hw.ac.uk/en/publications/the-expertise-reversal-effect-and-worked-examples-in-tutored-prob/).
7. Butterfield & Metcalfe (2006), *The correction of errors committed with high confidence*. [Article copy](https://core.ac.uk/download/357328401.pdf). Revisit corrections; immediate feedback is not permanent mastery.
8. Pan & Sana (2021), *Pretesting versus posttesting*. [Author PDF](https://sc-pan.github.io/pdf/PS_2021.pdf). The supplied draft relied on a summary rather than full-paper inspection.
9. Research comparing multiple-true-false and multiple-choice formats (2019), *International Journal of STEM Education*. [DOI](https://doi.org/10.1186/s40594-019-0169-0).
10. University of Maryland Experimental Software Engineering Group, [reading techniques for fault detection](https://www.cs.umd.edu/projects/SoftEng/ESEG/topics/rtfault2.html). Transfer to this exam is indirect.
11. Penn Career Services, [case interview guide](https://careerservices.upenn.edu/resources/case-interview-guide/). Practitioner guidance, not experimental evidence for this exam.
12. Kansas State Counseling Services, [suggestions for taking essay tests](https://www.k-state.edu/counseling/resources/self_help/suggestionsfortakingessaytests.html). Practitioner guidance.
13. Okano et al. (2019), *Sleep quality, duration, and consistency are associated with better academic performance in college students*. [MIT record](https://dspace.mit.edu/handle/1721.1/127257). Observational evidence.
14. Ramirez & Beilock (2011), expressive writing before tests, via [a research news summary](https://www.sciencedaily.com/releases/2011/01/110113141605.htm). The supplied draft also reports a replication concern through secondary material; no recommendation here depends on this finding.
