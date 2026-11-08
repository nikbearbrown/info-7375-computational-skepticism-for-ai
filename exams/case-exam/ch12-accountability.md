# Chapter 12 case: The committee signs

**Chapter:** 12 Accountability · **Seeded flaw:** accountability assigned to a committee with a collective attestation, so no named human can bear a sanction · **Key terms:** accountability, five accountability requirements (specifications, audit trail, recourse, independent review, sanctions), named accountable human, attestation, gate, segregation of duties

---

# STUDENT PAGE

## 1. Scenario

Mr. Eze is general counsel at a consumer lender that plans to use an AI system to approve or decline small loans automatically. Its board has told him that before launch there must be a written plan showing who is accountable if the system fails or treats applicants unfairly. He asked an AI agent to draft the accountability plan so that he can take it to the board.

## 2. The instruction given to the AI agent

> "Draft the accountability plan for our automated loan-approval system covering the requirements a regulator or auditor would expect."

## 3. Agent output

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

## 4. Questions (10 points)

1. **(5 points)** What is wrong with how this plan assigns accountability? Name the problem with the exact term.
2. **(2 points)** Name one question or test you would apply to the plan to see whether anyone is really accountable.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Mr. Eze why a committee signature is not enough. Use no technical terms.

---

# TA RUBRIC PAGE

Fixed rubric (see README): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

## Case key

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

## Scored sample answers

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
