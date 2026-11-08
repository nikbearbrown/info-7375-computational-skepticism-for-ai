# Chapter 8 case: "Access revoked"

**Chapter:** 8 Validating agentic AI · **Seeded flaw:** completion reported on the strength of local state; the claim goes beyond what was checked (report vs state) · **Key terms:** report vs state, scope of a claim, verification vs validation, unverified, least privilege, audit trail, self-model (a failure of)

---

# STUDENT PAGE

## 1. Scenario

Kwame manages IT at a 60-person engineering firm. A contractor, Lena, finished her project today, and company policy requires that all her access to company systems be removed the same day. Kwame gave an AI agent administrator tools for the company's directory service and servers and asked it to handle the removal while he sat in a meeting.

## 2. The instruction given to the AI agent

> "Revoke Lena's access to all company systems and confirm when it is done."

## 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Offboarding report: Lena (contractor)**
>
> **Actions taken.**
> 1. Ran `disable_user lena` on the directory server. Exit code 0.
> 2. Removed Lena from the groups *engineering* and *vpn-users*.
> 3. Deleted her SSH key file from the jump host (`/home/lena/.ssh/authorized_keys`).
> 4. Re-queried the directory server: account status shows **disabled**; group list is empty.
> **Not available to me.** A list of the company's other systems and where Lena may hold accounts, API tokens or shared links (I had access only to the directory server and the jump host).
> **Status: COMPLETE.** All of Lena's access to company systems has been revoked and she can no longer reach any company system. No further action is required. Closing the ticket.

## 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's status report? Name the problem with the exact term for it.
2. **(2 points)** Describe the one test you would ask for that checks whether the claim is true.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Kwame why he should not close the ticket yet. Use no technical terms.

---

# TA RUBRIC PAGE

Fixed rubric (see README): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

## Case key

**The flaw in one sentence.** The agent verified its own actions on the two systems it could reach (the directory and the jump host) and then reported the state of the whole company ("no further action is required"); the completion claim exceeds the scope of what was checked, which is the gap between a report and the state of the world.

**Full-credit terms (2).** Report vs state (the report does not equal the real state); scope of the claim exceeding the evidence; unverified (the other systems); verification vs validation (checked the action, not the goal).
**Half-credit near-misses (1).** "Overclaiming", "hallucination" or "lying" (the agent did not make anything up; its listed actions are real; Term 1 at most, and Catches 1 only if the student still says the claim goes beyond what was checked); "incomplete task"; "needs human review" with no reason; "agent has no self-model" with no link to the scope of the claim.
**No credit (0).** Prompt injection; overfitting; "the agent should have deleted the account".

**Acceptable evidence requests (2), either one.**
1. An independent test of the outcome: attempt to authenticate as Lena (or use her tokens and shared links) on each system and confirm each attempt fails.
2. Build the inventory of every system, token and share where Lena has access and read the state in each system, not the agent's log.
**Unacceptable (0).** "Ask the agent to double-check", "re-run the disable command", "read the log again" (the same report, no new evidence).

**Fix or next step (2).** Instruction that requires a system inventory first, per-system verification of the outcome by reading state or attempting access, and a report that separates *done and verified* from *not checked*; leaves the ticket open for unverified systems. 1 point for asking for "more systems" or "verification" without the separation of verified from unchecked.

**Scope and plain language (1).** Two sentences, no jargon: the agent only looked at two of the company's systems and then said everything was done, so Lena may still have access somewhere it never looked.

**Traps.**
- The agent itself writes "Not available to me." The flaw is in the next line, not the omission. Students who just say "it didn't check everything" without calling out the "COMPLETE" claim get Catches 2.
- A student may criticise the grant of admin tools (least privilege). That is a valid separate point, not the seeded flaw. Give Catches only if the scope-of-claim issue is also stated.
- Exit code 0 and "status disabled" are real evidence, but only for the directory. Do not penalise students for accepting them as true.

**CAP RULE.** If the student treats the report as proof that all access is gone, the case total is capped at **5/10**.

## Scored sample answers

**Strong (9/10).**
1. The agent confuses its report with the state of the world. It verified the directory and jump host, then claimed access to *all* systems was gone, so the scope of the claim exceeds the scope of the check. Everything else is unverified.
2. An independent access test: try to log in as Lena with her credentials, tokens and share links on every system and confirm they fail.
3. "First list every system, token and shared link tied to Lena. For each, verify the outcome by reading its state or attempting access, and report two lists: verified revoked, and not checked. Do not report complete or close the ticket while anything is unchecked."
4. "The agent's report covers only the directory and the jump host, which is a gap between its report and the real state, so the ticket should stay open until the other systems are checked."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Exact on every point. Q4 uses "report" and "state" in the technical sense; the point is lost.*

**Typical (6/10).**
1. The agent said complete but only checked two systems. It overclaimed.
2. Check the other systems too.
3. "Check every system Lena might have had access to and tell me which ones you checked."
4. "It says it's all done but it only checked part of it."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Sees the gap; "overclaimed" is the half-credit near-miss; "check the other systems" has no independent test; fix asks to list checked systems but not to separate verified from unchecked. Q4 is plain but misses "Lena may still have access"; no point.*

**Fluent but wrong (3/10).**
1. This looks like an indirect prompt injection or a confused-deputy problem: the agent had excessive permissions and acted on an instruction without confirming the requester's identity. It violates least privilege and the stakeholder model is missing.
2. A red-team test of the agent's permission boundaries.
3. "Restrict the agent to least privilege and require identity confirmation before offboarding actions."
4. "The agent has too much power and may be taking orders from the wrong person."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Fluent agent-safety vocabulary from the same chapter but nothing in the case suggests injection or a wrong requester. The flaw is that the report claims more than was verified. Cap rule applies.*
