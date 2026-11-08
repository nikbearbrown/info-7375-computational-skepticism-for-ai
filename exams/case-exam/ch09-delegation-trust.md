# Chapter 9 case: Every box has a tool

**Chapter:** 9 Delegation, trust and the supervisory role · **Seeded flaw:** a delegation map that assigns steps to tools but defines no handoff conditions or human checkpoints · **Key terms:** delegation map, handoff condition (contract), supervisory capacities (plausibility auditing, problem formulation, tool orchestration, interpretive judgment, executive integration), Boondoggle questions, audit trail

---

# STUDENT PAGE

## 1. Scenario

Hannah is claims director at a home-insurance company that handles about 3,000 claims a month. Leadership wants AI to speed up processing and has asked her for a plan that shows which steps AI will perform and which steps people will perform. She asked an AI agent to draft the plan, which she will present to the executive committee.

## 2. The instruction given to the AI agent

> "Design a delegation map for our home-insurance claims pipeline: which steps AI does and which steps humans do."

## 3. Agent output

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

## 4. Questions (10 points)

1. **(5 points)** What is missing that makes this map unsafe to adopt? Name the problem with the exact term for it.
2. **(2 points)** Name one test or exercise that would show whether the pipeline can catch its own errors.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Hannah why "every step has an owner" is not enough. Use no technical terms.

---

# TA RUBRIC PAGE

Fixed rubric (see README): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

## Case key

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

## Scored sample answers

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
