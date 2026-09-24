# Gru turn 14-v1-problem-summary

## Professor Bear typed

```
You're right on both. No escape clause: all three surface unprompted, or v1 is not confirmed; a diagnosed miss goes back to the scan and is recorded separately as evidence that the read log works. And yes to one decision log spanning sections, sdd/decisions.md, with D and OQ numbers, where each was raised, decided, and applied. Section files cite them by number.

9. Claude Code's own /init. What I'm rejecting from it specifically: it writes a description of the project, and instructions for future sessions, from the code alone, without asking the people who own the intent. The result reads as the team's intent, but it's the model's inference with no label. Worse, it lands in CLAUDE.md, where every later session treats it as an instruction, so an unchecked inference becomes a rule. I'm keeping its scanning. I'm rejecting the writing without asking, and the lack of any mark separating what the code says from what someone decided.
```

## Gru replied (verbatim, unedited)

Recorded. The fixture has no escape clause now: all three surface without prompting, or v1 isn't confirmed. A diagnosed miss is recorded separately as evidence that D5 works. The decision log is `sdd/decisions.md`.

Question 9 is recorded:

> **Rejected from `/init`:** writing a description of the project and instructions for future sessions from the code alone, without asking the people who own the intent, and with no mark separating what the code says from what someone decided. **Kept:** the scanning.

Your answer to question 9 points at a gap in gru's own design, so I'm raising it before the summary.

**The /init failure can come back one step later, in the Boondoggle Score.** You rejected /init because an unlabelled inference ends up where later sessions treat it as an instruction. Now look at what the Score is. Its prompting rule 2 says every Claude prompt includes the relevant SDD context inline, pasted directly. The Score's prompts *are* instructions to Claude. If a GRU-labelled judgment or a still-open CONFLICT gets pasted into a Score prompt as plain specification, the label is gone, and gru has done exactly what you reject /init for. It has just done it one file later.

So the labels have to survive into the Score. Any claim that goes into a Claude prompt either keeps its label, or it's shown to the student as a human task before the prompt is written. An unresolved CONFLICT never goes into a prompt as fact. Logging this as **OQ9**. It must close before /claude is designed.

---

**/v1 PROBLEM SUMMARY**

> gru is a **repo-grounded design interviewer** for **a student or fellow designing a change to a codebase she didn't write**. It solves **design documents built on unchecked claims about the code** through **a static read of the repository for each question, whose findings arrive as labelled, cited claims and whose disagreements arrive as questions she must answer.** It occupies the space between **a pasted Gru in a Claude Project, which asks everything and reads nothing,** and **Claude Code's `/init`, which reads everything and asks nothing.** It succeeds when **every claim in her design document carries a source label and a pinned citation, and every disagreement between docs and code was put to her as a question before its section was written,** without **her having to know which file to paste.**

**Intake record**

| # | Question | Answer |
|---|---|---|
| 1 | Name | gru everywhere: folder, entry script, hub skill, `gru-*` phase skills, `/gru` command |
| 2 | Problem | Design built on remembered and documented claims no one checked. Doc and code disagreements surface late or never. Evidence: three contradictions found by hand today. |
| 3 | User | Composite: a Humanitarians AI fellow three weeks into an inherited team repo, adding an export feature. The unchecked claim gets in at her summary. A PR reviewer or a user finds it after the design is already the argument. |
| 4 | What's new | (1) Gru chooses what gets read, not her. (2) Every claim comes back labelled and cited, and disagreements come back as questions. |
| 5 | Category | A repo-grounded design interviewer that writes an SDD and a Boondoggle Score |
| 6 | Deployment | Her repo, invisible to git until `/gru share`. Python 3.9 or later, standard library only. macOS and Linux. Git recommended. |
| 7 | Scale | Solo builder with an existing prototype. No date. Gated on two dogfood runs. Users bring their own Claude Code access. |
| 8 | Systems | Claude Code and git (depends on). Pasted-Gru Project (replaces: match the reasoning trail, beat it on gates that last). Slack (none, on purpose). |
| 9 | Rejected | `/init`'s unlabelled writing without asking. Its scanning is kept. |

**Decision log** (becomes `sdd/decisions.md`)

| ID | Decision | Raised | Applies in |
|---|---|---|---|
| D1 | Scan feeds the interview, never replaces it | v0 | v2 |
| D2 | Labels DOC / CODE / STUDENT / GRU, with CONFLICT as a marker that becomes the next question. `STUDENT (relayed: role)` allowed. | v0, v1 Q2–3 | v2, s1 |
| D3 | Translation layer: `/gru <cmd>` maps to `/<cmd>`. The menu uses the prefix. Deferred commands show "not in this version." | v0 | s1 |
| D4 | /build, /verify, /audit deferred. Reopen when the Snickerdoodle CLI is installable. | v0 | p2 |
| D5 | Read log for every question: files read, search terms, matched-not-opened | v1 Q4 | s1, s3 |
| D6 | Citations pinned to commit SHA or content hash. Drift flagged. | v1 Q4 | s3 |
| D7 | Gate-state file is MUST-BUILD | v1 Q4 | p1 |
| D8 | The student resolves a CONFLICT, never a default to CODE. Recorded as STUDENT with her reason. | v1 Q5 | v2 |
| D9 | Install into her repo's `.claude/skills/`, listed in `.git/info/exclude`. `sdd/` excluded. A name collision stops the install. | v1 Q6 | s2, p3 |
| D10 | Python 3.9 or later, stdlib only. Git recommended. macOS and Linux. Native Windows goes to /p2. | v1 Q6 | p2, p3 |
| D11 | `/gru share` un-excludes after confirmation. All of `sdd/` is reviewable. Raw scan output stays excluded. | v1 Q7 | s1, s3 |
| D12 | Prompt content hash recorded at every gate. A change is announced. | v1 Q7 | s3 |
| D13 | POSIX `sh` entry shim that hands off to Python | v1 Q7 | p3 |
| D14 | An existing `sdd/` stops the install. The alternate name goes in the state file. | v1 Q7 | s3 |
| D15 | Relay labels name roles, never people | v1 Q8 | v2 |
| D16 | Each section file keeps its pushback and answers in order | v1 Q8 | s3 |
| D17 | One cross-section log, `sdd/decisions.md`. Section files cite by number. | v1 Q9 | s3 |
| D18 | v1 release gate: five exit conditions, plus the fixture surfacing all three contradictions unprompted. No escape clause. | v1 Q7–9 | p1, g4 |

**Open questions**

| ID | Question | Must close before |
|---|---|---|
| OQ2 | Is the Score overwritten or kept as versions when /claude reruns? | /s3 |
| OQ3 | Can she re-answer a confirmed gate? What happens to the sections after it? | /s3 |
| OQ4 | Skill folder names: codes or aliases? | /s1 |
| OQ5 | Install source: course-repo subfolder or its own repo | after v1 (/p3) |
| OQ6 | Scan depth. Leaning toward a static read, never executing. Behavior questions are handed to her as a human task. | /v2 |
| OQ9 | Do labels survive into Boondoggle prompts? An unresolved CONFLICT never becomes specification. | /claude design |
| **OQ10** | **How does gru decide which code is "relevant" to a question?** | **/v2** |

---

**The biggest unresolved question in the problem definition: OQ10.**

Your whole answer to "why not just paste the files?" depends on one phrase: *the code relevant to each question.* Claim 1 says gru reads what she wouldn't have thought to paste. D5 lets her see what it read. The fixture will test whether it found the right files. But nothing yet says *how* it picks them.

Does it search by the terms in the question? Follow imports out from the entry points? Read every file that the docs being checked mention? Or look first at the files each DOC claim names? Each of these misses different things. A scan that searches only for "export" is her blind spot moved into the tool, only harder to see. The fixture will tell you whether the method works, but it can't design the method for you. That decision has to be made in /v2, before /s1 documents the component that does it.

Does this summary reflect what you're building? If yes, we go to /v2 and turn D1, D2, D8, D15 and OQ6 into locked architecture principles, each with its failure state named. If not, tell me what's wrong with it.
