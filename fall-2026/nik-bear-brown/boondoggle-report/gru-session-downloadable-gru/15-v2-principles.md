# Gru turn 15-v2-principles

## Professor Bear typed

```
Yes, the summary reflects what I'm building. Confirmed.

On OQ9, so it doesn't drift: agreed as you stated it. Labels survive into Score prompts, and an unresolved CONFLICT never goes into a prompt as fact; it becomes a human task first. I'm happy for that to close now.

OQ10 goes to /v2 as you said. Proceed to /v2.
```

## Gru replied (verbatim, unedited)

OQ9 is closed and logged as **D19**. Labels survive into the Score's prompts. An unresolved CONFLICT becomes a human task before it can go into any prompt.

---

**/v2: ARCHITECTURE PRINCIPLES**

The decisions from /v1 reduce to four principles. Everything in D1 through D19 either follows from one of them or is an implementation detail under one of them.

---

**P1. Ask before writing**

**Commitment:** No section file, gate confirmation, or Score step is written from the scan alone. Every section is written only after the student has answered that command's questions, and only she can confirm a gate. (D1)

**Honors:** gru-scan finds `EXPORT_DIR` read in `export.py:88` with no default. The interview question becomes: "The README says exports default to `/out`. The code reads `EXPORT_DIR` and sets no default. Which is the intended design?"

**Violates:** gru writes a draft /s1 section from the scan and asks her to approve it. That's harder to spot than a `--skip-interview` flag, and it's the same failure. Approving a pre-written draft only takes a click. The pressure to formulate is gone, and her answer turns into a rubber stamp.

**Failure state in production:** Design documents that look like they came from an interview but came from inference. That's `/init` with a form around it. A reviewer trusts the document *because* it looks gated.

---

**P2. Provenance travels**

**Commitment:** Every claim carries its source label (DOC, CODE, STUDENT, or GRU) and a citation pinned to a SHA or content hash. The label survives every later transformation, including section files, the one-pager, the decision log, and the Score's prompts. (D2, D6, D15, D19)

**Honors:** /g3's one-pager keeps the labels, even though that makes it less clean to read. A Score prompt that depends on a GRU-labelled judgment is preceded by a human task that confirms it.

**Violates:** Removing labels "for readability" at any output stage. Or relabelling a CODE claim as STUDENT because she agreed with it.

**Failure state in production:** An inference becomes a rule one file later. A Score prompt tells Claude to build against a claim no human ever made.

---

**P3. People resolve disagreements**

**Commitment:** A CONFLICT is a question for a person. Gru never resolves one by giving any source priority. Her resolution is recorded as STUDENT, with her reason. (D8)

**Honors:** A CONFLICT between the docs' scheduler and the privacy rule becomes the next question, and her answer ("the privacy rule governs; the scheduler line in the docs is stale") goes into `decisions.md` with her reason.

**Violates:** "CODE wins unless the student objects." Or any automatic resolution: newest source wins, majority of sources wins, most specific source wins.

**Failure state in production:** Students give way to code that has drifted from its intent. The design document then argues for the bug.

---

**P4. Read, never run**

**Commitment:** gru reads the repository statically and never executes its code. Every read is visible in the read log. Questions that only running the code can settle are handed to the student as human tasks. (OQ6, D5)

**Honors:** "A static read can't confirm where the export file lands at runtime. Run the export once and tell me the path." That becomes a human task for plausibility auditing, on her machine, by her choice.

**Violates:** Running the test suite to answer a design question. Importing a module to check a default. Running a build script "just to see."

**Failure state in production:** A student's laptop runs a stranger's code for a design question, with side effects, network calls, secrets read, and files written into a team repo. Or reads nobody can see: a missed file leaves no trace, so there's nothing to audit.

---

**PRINCIPLE COLLISION TEST**

Two real collisions.

**C1: P1 against P2, label laundering.** P1 encourages Gru to pre-fill questions from the scan ("the code says X; is that the intended design?"). When she answers "yes," what label does the claim carry? If it becomes STUDENT, her agreement has laundered a CODE reading, or worse, a GRU inference, into a claim the design says she made. Over a whole interview, "yes" answers turn most GRU and CODE claims into STUDENT claims, and P2 stops meaning anything.

**Proposed rule:** A claim keeps its original source label. Her confirmation is recorded *next to* it (`CODE, confirmed by STUDENT`), never in place of it. A claim is labelled STUDENT only when she supplies the content herself.

**Proposed primary:** P2. Provenance doesn't change by agreement.

**C2: P4 against the /v1 success condition.** /v1 says gru succeeds when "every disagreement between docs and code was put to her as a question." Under P4, gru can't detect a disagreement that only shows up at runtime. The success condition promises something the principle forbids.

**Proposed fix:** Amend the success condition to: "every disagreement a static read can detect was put to her as a question, and every question that depends on runtime behavior was handed to her as a human task."

**Proposed primary:** P4. Safety isn't traded for coverage.

The fixture supports P4, by the way. You found all three contradictions *by reading the code by hand*. You didn't run anything. So D18's fixture tests whether a static read is enough, and your own evidence says it can be.

---

**OQ10: how gru decides which code is relevant**

Your own fixture adds a requirement here. The scheduler contradiction was **DOC against DOC**: the docs listed a scheduler that the tool's own privacy rule forbids. No code was involved. So the relevance method has to check claims against *other claims*, not only against code. A method that only asks "what code does this question touch?" misses it completely.

The options:

| Method | How it chooses | What it misses |
|---|---|---|
| **(a) Term search** | Searches for the question's terms, such as "export" | Anything renamed. `dump_bundle()` writes the export, so her blind spot is back. |
| **(b) Claim-anchored** | For each DOC or STUDENT claim in scope, reads the code and docs the claim names: folders, config keys, commands, rules | Code no claim mentions |
| **(c) Structural** | Starts at entry points (manifests, CLI mains, CI) and follows imports and calls to a fixed depth | Doc-against-doc conflicts. Dead or dynamically loaded code. |
| **(d) Layered** | (b) first, then (c) for coverage, then (a) as a last resort. The read log tags which method found each file. | Least overall, and the method tag in the log shows her *why* a file was or wasn't read |

My recommendation is **(d)**. Option (b) is what you did by hand when you found all three contradictions. You started from what the docs claimed and went to where the claim would be true or false. Option (c) catches code that no claim mentions. Tagging each file with the method that found it makes a miss explainable, which D18 depends on.

This is your call, not mine. The choice decides what gru can find.

---

**To lock /v2, I need four answers:**
1. Are P1 through P4 accepted as written, or what should change?
2. C1: is the rule "a claim keeps its source, and confirmation is recorded next to it" accepted, with P2 primary?
3. C2: is the success condition amended as proposed, with P4 primary?
4. OQ10: (a), (b), (c), (d), or something else?
