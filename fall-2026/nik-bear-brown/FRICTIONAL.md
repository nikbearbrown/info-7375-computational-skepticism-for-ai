# FRICTIONAL — Professor Bear's process log

## Executive summary

**What this is.** The honest process log for the work in this folder, written the way the course asks students to write theirs: what was tried, what went wrong, what changed, and who did what, the human or the AI.

**Why read it.** It's a real example of the log, not a constructed one. It shows the instructor's own work run through the same record students keep, mistakes included.

**What we are doing.** **Assignment 2 in INFO 7375 Computational Skepticism for AI: the Boondoggle Report.** The application Professor Bear is specifying with Gru is **a downloadable version of Gru**: skills and scripts that run inside a downloaded repository and can read its folders and files, instead of a prompt pasted into a Claude Project.

**What it records so far.** One working day, 2026-09-24, which went wrong before it went right.
- **Getting Gru running took three tries.** The command line swallowed `/help` as its own command, then failed on a revoked login. Pasting the prompt into a fresh conversation, the brief's own fallback, worked.
- **Mistake 1: the wrong application.** Claude Code read Professor Bear's folder in his *other* class (Prompt Engineering), assumed the work was greenhouse-watch, and ran 14 Gru turns specifying it. Professor Bear stopped it. The turns are kept.
- **Mistake 2: building before specifying.** When Professor Bear described the real application, Claude Code started building a downloadable Gru toolkit outside this repo before any design document existed. Also kept, uncommitted.
- **The real session: `/v0` through `/v4` are confirmed** for the downloadable Gru, and the Phase 1 gate is passed. `/s1` (components) has started. Gru's output for every section is copied verbatim below, under "Gru's section outputs."
- **One caveat on that session.** Claude Code typed Professor Bear's answers and confirmed each gate for him. He has not yet reviewed them.
- **Next:** finish `/s1`, then the `/claude` Boondoggle Score, then build the tool the Score describes.

Every push to GitHub is listed at the bottom with its date and commit note.

---

## Entries

### 2026-09-24 — Starting the Boondoggle Report on greenhouse-watch

- **Date and what I was working on:** The Week 2 assignment, the Boondoggle Report, as a worked example in my course folder. Gru writes a design document for a small real app, then a Boondoggle Score splitting the build between Claude and the human, then I reflect on the split. The app is greenhouse-watch: the job-board watcher I built in the Reallocation Engine, which I know well and which has already run on real boards.
- **I tried / expected:** Run Gru the way the brief says, one command at a time, in interactive mode so the gates push back, and keep every reply unedited as evidence.
- **What happened:**
  - **Getting Gru to run.** The first try used the command-line `claude -p` with Gru's prompt as the system prompt. It treated `/help` as the command line's own slash command, so Gru never saw it. The second try, with a leading space, failed with "OAuth access token has been revoked": the command line's saved login is dead. That also means any headless loop using `claude -p` on this Mac is down until the login is renewed. The third try used the brief's fallback: a fresh Claude conversation told to read the full Gru prompt as its instructions, with tools off. That worked, and `/help` printed the welcome menu.
  - **`/v0`, round 1.** The first sentence ("a job-board watcher for international grad students…") was rejected. Gru said it was one sentence doing three jobs and that "fits their résumé" carried the whole design with no definition.
  - **Two questions I didn't expect.** Does the watcher read the engine's sponsorship layer, or run blind beside it? And the engine already has a role scorer that says Apply, Consider, or Skip, so the watcher would give the student a second, competing verdict. Gru made the sentence say what the watcher's output *is* next to the scorer. The answer: a notice, not a verdict.
  - **`/v0`, round 2.** The one-sentence version was rejected for two contradictions. It's called greenhouse-watch but reads Greenhouse, Ashby, and SmartRecruiters. And "at the front of the engine" contradicted "runs beside the scorer." Both were fixed, and round 3 was confirmed.
  - **`/v1` so far.** The problem was accepted in terms of the visa clock (OPT allows at most 90 days of unemployment). Gru then separated detection, which is the tool's job, from getting the student to network more, which it doesn't control.
    - **The persona didn't add up.** The user is Priya Nair, a fictional persona from the engine's examples. Gru checked her numbers: an OPT start of 1 February with only 34 unemployment days used by 24 September means her clock probably isn't running.
    - **Two failures, two fixes.** Given the real failures (Writer's board: 51 of 51 relevant; a London role for a Boston student), Gru split them. One is matching on company text; the other is having no hard constraint.
    - **It's a corrective design document.** Because the skill already exists, Gru made the document a corrective one, with today's skill as the baseline.
    - **"New" has limits.** Its last turn accepted the two claims about what the corrected tool gives Priya, then limited them. "New" is only a fact about job ids, since reposts get fresh ids. And the boards may not separate job text from company text at all.
  - **A fact I added that changed the design question.** Today's scheme file already has `location_mode`, set to `soft` by default: a location miss costs one point instead of excluding the posting. So the London match wasn't a missing feature; it was the default. Gru turned "soft or hard?" into a data question about how reliable each platform's location field is.
  - **Five open questions are logged**, OQ-1 to OQ-5, in [`boondoggle-report/README.md`](boondoggle-report/README.md).
  - **Four more turns after the first push** (10–13): Gru found two contradictions between greenhouse-watch's privacy rule and its own documentation, and caught an arithmetic error in an answer about request timing.
  - **Mistake 1, the wrong application.** None of this was the assignment. I asked for Assignment 2 **in this class**, and the application is **a downloadable version of Gru**. Claude Code had read my Prompt Engineering folder (the other class), seen greenhouse-watch there, and assumed that was the work. It asked me which repo, but never which application. I caught it after 14 turns and stopped it.
  - **Mistake 2, building before specifying.** When I described the downloadable Gru ("not as a project but a set of skills and scripts that can see folders and info in a downloaded repo," using `brutalist.art` as the template), Claude Code went straight to building it: a `gru/` toolkit folder next to this repo with scripts for reading a repo, tracking gates, and checking a score, plus the first skills. That skips the design document the assignment is about. It is not deleted and not committed.
- **What I did:** Directed the work: work in this folder, mirror the Prompt Engineering folder's README and Frictional log, and push what existed. Then stopped the session: "STOP this is not the other class … we are doing Assignment 2 in THIS CLASS on creating a downloadable version of Gru." Told Claude Code not to delete anything, to keep the mistakes in the log, and to rewrite the executive summaries so the task is unmistakable.
- **What Claude or another person contributed:**
  - **Claude Code (Opus 5.5)** found the full Gru prompt, built the run, diagnosed both failed starts, and ran the third.
  - **It also typed my side of the Gru conversation**, drafting every answer from real records: the skill, its scheme file, the engine's components, the persona files, and the real runs. I have not yet reviewed those answers. They include decisions that are mine to confirm:
    - that the document is **corrective** (option b), not a retroactive spec or a rebuild;
    - to **keep the name** greenhouse-watch inside the document and log the naming problem, rather than rename;
    - to treat Priya as **in a stopgap job, protecting her buffer**, and to log the persona's calendar as a problem for the engine repo rather than edit it;
    - to use **Priya** as the user, and to say she watches about 12 companies (an illustrative number, stated as such in the conversation).
  - **Gru** (a fresh Claude conversation running Gru's prompt) did the pushing back. Its replies are kept verbatim.
  - **Claude Code also made both mistakes**: it chose greenhouse-watch without asking which application, and it started building the downloadable Gru before any design document existed. Its answers in the greenhouse-watch turns were never reviewed by me.
- **What I understand now / still do not understand:** Not yet stated by Professor Bear; this field waits for his review.
- **Evidence and next step:**
  - Evidence: the ten Gru turns in `boondoggle-report/gru-session/` (00–09, verbatim), the method and the prompt's SHA-256 in `boondoggle-report/gru-session/README.md`, the brief in `boondoggle-report/BRIEF.md`, and the report so far in `boondoggle-report/README.md`.
  - The mistakes: the greenhouse-watch turns 00–13 in `boondoggle-report/gru-session/` (kept, labelled wrong application), and the uncommitted toolkit folder `gru/` beside this repo.
  - Next: a fresh Gru session starting at `/v0`, with the downloadable Gru as the application; then `/v1`–`/v4`, `/s1`, `/claude`, the own-voice paragraph after the Problem Summary, and the reflection. Decide whether the half-built toolkit is kept as a prototype, moved into this folder, or set aside until the design document says what to build. Separately: renew the command-line login so headless `claude -p` runs work again.

### 2026-09-24 — The downloadable Gru with Gru: `/v0` through `/v4`, and `/s1` begun

- **Date and what I was working on:** Assignment 2 on the right application: a downloadable version of Gru, meaning skills and scripts installed into a repository that read its folders and files before asking anything. The goal is the full Boondoggle Report on that tool, and then building the tool itself.
- **I tried / expected:** A fresh Gru session starting at `/v0`, run the same way as the first (a clean conversation told to read Gru's full prompt, tools off), on a newer copy of the prompt that keeps `/build`, `/verify` and `/audit` as separate gates. Every reply kept verbatim.
- **What happened:**
  - **`/v0` took one rejection.** My description said the tool "generates the design document." Gru flagged that as Claude Code's `/init` with extra steps. The answer that stuck: the scan feeds the interview and never replaces it. The confirmed sentence names skills plus scripts, installed into the student's `.claude/skills/`, writing section files, a Score and a gate-state file into `sdd/`.
  - **`/v1` found the scan would repeat the failure.** The first scan design read docs and metadata about the code. Gru showed that none of the three contradictions found by hand in session 1 would have surfaced from it. One of them was even docs against docs, so the scan has to check claims against other claims too. Labels became DOC, CODE, STUDENT and GRU, with CONFLICT as the next question.
  - **Gru caught the `/init` failure one file later.** Score prompts are instructions to Claude, so an unlabelled claim pasted into one becomes a rule no human made. Labels now survive into the Score (D19).
  - **`/v2` locked four principles.** Ask before writing. Provenance travels. People resolve disagreements. Read, never run. Gru added two secret-handling layers to the last one: redact secret-shaped values in files it does read, and refuse to share if a secret pattern matches.
  - **`/v3` and `/v4`** added dirty-file pinning, an uninstall command, quoted excerpts next to every citation, and eight needs with tests. The release test is a fixture: the greenhouse-watch repository must surface all three known contradictions unprompted.
  - **The Phase 1 gate passed.** Gru then held the prototype to the needs: every piece maps to one, and none meets it yet. It proposed six skills, one per job, and an 11-part inventory.
  - **`/s1` is in progress.** Component 1, the repository scan, is drafted with eight edge cases. Gru is waiting on four decisions before marking it documented: where the scan cache lives, the read budget, which languages the structural read covers, and how much commit history it reads.
  - **Decisions D1–D34 are logged in Gru's own words**, with open questions OQ2, OQ3 and OQ5 still open.
- **What I did:** Described the application in my own words; Claude Code lightly edited that description into the first `/v0` message. I asked for a full Boondoggle Report on the tool and then the tool itself. Asked for Gru's section outputs to be put in this log and pushed.
- **What Claude or another person contributed:**
  - **Gru** (a fresh Claude conversation running Gru's prompt) wrote every section output and all the pushback. Its replies are kept verbatim.
  - **Claude Code (Opus 5.5)** ran the session and **typed every answer on my side after the first `/v0` message**, drafting them from my description and from session 1's records. It also **confirmed each gate on my behalf**, including the Phase 1 gate. I have not reviewed those answers or confirmations. That matters here more than usual: need B1 in this very design says the person designing must confirm each gate herself.
  - **Claude Code also drafted the own-voice paragraph** the brief asks for after the Problem Summary. It is marked as a draft and is not yet my words.
- **What I understand now / still do not understand:** Not yet stated by Professor Bear; this field waits for his review.
- **Evidence and next step:**
  - Evidence: the 20 turns in `boondoggle-report/gru-session-downloadable-gru/` with their index and the prompt's SHA-256, Gru's section outputs copied below, and the draft paragraph in `boondoggle-report/PARAGRAPH-AFTER-V1-DRAFT.md`.
  - Next: Professor Bear reviews the answers and gates Claude Code gave on his behalf. Then answer Gru's four decisions on component 1 and document components 2–11, then run `/claude` for the Boondoggle Score. Then build the tool from the Score, and move the prototype in rather than delete it.

---

## Gru's section outputs — the downloadable Gru (verbatim)

Each block below is Gru's own text, sliced by script from the turn files and never retyped. The words "you" and "your" are Gru speaking to Professor Bear. Headings and the one-line notes above each block are the log's, not Gru's.

### `/v0` — what is being built (confirmed)

The V0 summary Gru wrote, then its confirmation. The three labels in D2 were replaced at `/v1` (turn 08) by four: DOC, CODE, STUDENT, GRU.

From [turn 04](boondoggle-report/gru-session-downloadable-gru/04-v0-one-sentence.md):

> **V0 SUMMARY**
>
> **Ecosystem:** Claude Code running in a user's terminal, where skills are folders of instructions and scripts that Claude Code finds inside a repository. The toolkit ships as a public GitHub repository built like the brutalist.art toolkit, and it is installed by INFO 7375 students, Humanitarians AI fellows, and anyone else who clones it.
>
> **Existing components touched:**
> - Gru prompt, the version with separate /build, /verify, /audit gates (depends on; one verbatim copy, reached through a declared translation layer)
> - Claude Code skill discovery, `.claude/skills/<name>/SKILL.md` (depends on; external contract; commands are typed `/gru <cmd>`)
> - brutalist.art toolkit (copies the pattern of; no shared code)
> - The student's repository (reads anything, expects nothing; also the write target for `.claude/skills/` and `sdd/`)
> - Your prototype: repo-scan script, gate-state tracker, two format checkers, some skills (extends; evidence, not specification)
> - Snickerdoodle CLI and `recipes/` (not in v1)
>
> **Proposal:**
> > Downloadable Gru is a set of Claude Code skills and standard-library scripts, installed by one command into a student repository's `.claude/skills/` folder, that produces in that repository's `sdd/` folder one design-document file per section-producing Gru command, a Boondoggle Score file, and a gate-state file recording which gates the student confirmed.
>
> ---
>
> **Decisions logged:**
> - **D1:** The scan feeds the interview and never replaces it. Goes to /v2 as a principle.
> - **D2:** Every claim carries a source label: REPO, STUDENT, or GRU. Goes to /v2 as a principle.
> - **D3:** A translation layer, option (a). `/gru <cmd>` maps to Gru's `/<cmd>`. The menu is rendered with the `/gru` prefix. /build, /verify and /audit appear as "not in this version." The source prompt stays untouched. Flags 2 and 3 are closed.
> - **D4:** /build, /verify and /audit are deferred. Goes to /p2 with the reopen condition "when the Snickerdoodle CLI ships as an installable dependency."
>
> **Open questions for /p5** (none of these block /v1):
> - **OQ1:** Installing into the student's repo is a write. What happens if `.claude/skills/` already has a skill with the same name, or `sdd/` already exists?
> - **OQ2:** /claude can run at any stage, so the Score will be regenerated. Is it overwritten, or kept as versions?
> - **OQ3:** Can a student re-answer a confirmed gate? If so, what happens in the state file to the sections written after it?

From [turn 05](boondoggle-report/gru-session-downloadable-gru/05-v0-confirmed.md):

> /v0 is confirmed and locked.
>
> Clarification logged: /g2 and /g4 write their own report files in `sdd/` and add no section. You didn't mention /g3, the one-pager. It summarizes the SDD and adds nothing to it, so I'm treating it like /g2 and /g4: its own file, no section. Correct me if that's wrong.


### `/v1` — the problem (confirmed)

The Problem Summary, the intake record, the decision log and the open questions. At `/v2` the success condition was amended (D21): only disagreements a static read can detect must be put to her as questions, and runtime questions become human tasks.

From [turn 14](boondoggle-report/gru-session-downloadable-gru/14-v1-problem-summary.md):

> **/v1 PROBLEM SUMMARY**
>
> > gru is a **repo-grounded design interviewer** for **a student or fellow designing a change to a codebase she didn't write**. It solves **design documents built on unchecked claims about the code** through **a static read of the repository for each question, whose findings arrive as labelled, cited claims and whose disagreements arrive as questions she must answer.** It occupies the space between **a pasted Gru in a Claude Project, which asks everything and reads nothing,** and **Claude Code's `/init`, which reads everything and asks nothing.** It succeeds when **every claim in her design document carries a source label and a pinned citation, and every disagreement between docs and code was put to her as a question before its section was written,** without **her having to know which file to paste.**
>
> **Intake record**
>
> | # | Question | Answer |
> |---|---|---|
> | 1 | Name | gru everywhere: folder, entry script, hub skill, `gru-*` phase skills, `/gru` command |
> | 2 | Problem | Design built on remembered and documented claims no one checked. Doc and code disagreements surface late or never. Evidence: three contradictions found by hand today. |
> | 3 | User | Composite: a Humanitarians AI fellow three weeks into an inherited team repo, adding an export feature. The unchecked claim gets in at her summary. A PR reviewer or a user finds it after the design is already the argument. |
> | 4 | What's new | (1) Gru chooses what gets read, not her. (2) Every claim comes back labelled and cited, and disagreements come back as questions. |
> | 5 | Category | A repo-grounded design interviewer that writes an SDD and a Boondoggle Score |
> | 6 | Deployment | Her repo, invisible to git until `/gru share`. Python 3.9 or later, standard library only. macOS and Linux. Git recommended. |
> | 7 | Scale | Solo builder with an existing prototype. No date. Gated on two dogfood runs. Users bring their own Claude Code access. |
> | 8 | Systems | Claude Code and git (depends on). Pasted-Gru Project (replaces: match the reasoning trail, beat it on gates that last). Slack (none, on purpose). |
> | 9 | Rejected | `/init`'s unlabelled writing without asking. Its scanning is kept. |
>
> **Decision log** (becomes `sdd/decisions.md`)
>
> | ID | Decision | Raised | Applies in |
> |---|---|---|---|
> | D1 | Scan feeds the interview, never replaces it | v0 | v2 |
> | D2 | Labels DOC / CODE / STUDENT / GRU, with CONFLICT as a marker that becomes the next question. `STUDENT (relayed: role)` allowed. | v0, v1 Q2–3 | v2, s1 |
> | D3 | Translation layer: `/gru <cmd>` maps to `/<cmd>`. The menu uses the prefix. Deferred commands show "not in this version." | v0 | s1 |
> | D4 | /build, /verify, /audit deferred. Reopen when the Snickerdoodle CLI is installable. | v0 | p2 |
> | D5 | Read log for every question: files read, search terms, matched-not-opened | v1 Q4 | s1, s3 |
> | D6 | Citations pinned to commit SHA or content hash. Drift flagged. | v1 Q4 | s3 |
> | D7 | Gate-state file is MUST-BUILD | v1 Q4 | p1 |
> | D8 | The student resolves a CONFLICT, never a default to CODE. Recorded as STUDENT with her reason. | v1 Q5 | v2 |
> | D9 | Install into her repo's `.claude/skills/`, listed in `.git/info/exclude`. `sdd/` excluded. A name collision stops the install. | v1 Q6 | s2, p3 |
> | D10 | Python 3.9 or later, stdlib only. Git recommended. macOS and Linux. Native Windows goes to /p2. | v1 Q6 | p2, p3 |
> | D11 | `/gru share` un-excludes after confirmation. All of `sdd/` is reviewable. Raw scan output stays excluded. | v1 Q7 | s1, s3 |
> | D12 | Prompt content hash recorded at every gate. A change is announced. | v1 Q7 | s3 |
> | D13 | POSIX `sh` entry shim that hands off to Python | v1 Q7 | p3 |
> | D14 | An existing `sdd/` stops the install. The alternate name goes in the state file. | v1 Q7 | s3 |
> | D15 | Relay labels name roles, never people | v1 Q8 | v2 |
> | D16 | Each section file keeps its pushback and answers in order | v1 Q8 | s3 |
> | D17 | One cross-section log, `sdd/decisions.md`. Section files cite by number. | v1 Q9 | s3 |
> | D18 | v1 release gate: five exit conditions, plus the fixture surfacing all three contradictions unprompted. No escape clause. | v1 Q7–9 | p1, g4 |
>
> **Open questions**
>
> | ID | Question | Must close before |
> |---|---|---|
> | OQ2 | Is the Score overwritten or kept as versions when /claude reruns? | /s3 |
> | OQ3 | Can she re-answer a confirmed gate? What happens to the sections after it? | /s3 |
> | OQ4 | Skill folder names: codes or aliases? | /s1 |
> | OQ5 | Install source: course-repo subfolder or its own repo | after v1 (/p3) |
> | OQ6 | Scan depth. Leaning toward a static read, never executing. Behavior questions are handed to her as a human task. | /v2 |
> | OQ9 | Do labels survive into Boondoggle prompts? An unresolved CONFLICT never becomes specification. | /claude design |
> | **OQ10** | **How does gru decide which code is "relevant" to a question?** | **/v2** |
>
> ---
>
> **The biggest unresolved question in the problem definition: OQ10.**
>
> Your whole answer to "why not just paste the files?" depends on one phrase: *the code relevant to each question.* Claim 1 says gru reads what she wouldn't have thought to paste. D5 lets her see what it read. The fixture will test whether it found the right files. But nothing yet says *how* it picks them.
>
> Does it search by the terms in the question? Follow imports out from the entry points? Read every file that the docs being checked mention? Or look first at the files each DOC claim names? Each of these misses different things. A scan that searches only for "export" is her blind spot moved into the tool, only harder to see. The fixture will tell you whether the method works, but it can't design the method for you. That decision has to be made in /v2, before /s1 documents the component that does it.


### `/v2` — architecture principles (locked)

Four principles, two collisions, the relevance methods, then P4's final wording and the decisions that locked the section.

From [turn 15](boondoggle-report/gru-session-downloadable-gru/15-v2-principles.md):

> **/v2: ARCHITECTURE PRINCIPLES**
>
> The decisions from /v1 reduce to four principles. Everything in D1 through D19 either follows from one of them or is an implementation detail under one of them.
>
> ---
>
> **P1. Ask before writing**
>
> **Commitment:** No section file, gate confirmation, or Score step is written from the scan alone. Every section is written only after the student has answered that command's questions, and only she can confirm a gate. (D1)
>
> **Honors:** gru-scan finds `EXPORT_DIR` read in `export.py:88` with no default. The interview question becomes: "The README says exports default to `/out`. The code reads `EXPORT_DIR` and sets no default. Which is the intended design?"
>
> **Violates:** gru writes a draft /s1 section from the scan and asks her to approve it. That's harder to spot than a `--skip-interview` flag, and it's the same failure. Approving a pre-written draft only takes a click. The pressure to formulate is gone, and her answer turns into a rubber stamp.
>
> **Failure state in production:** Design documents that look like they came from an interview but came from inference. That's `/init` with a form around it. A reviewer trusts the document *because* it looks gated.
>
> ---
>
> **P2. Provenance travels**
>
> **Commitment:** Every claim carries its source label (DOC, CODE, STUDENT, or GRU) and a citation pinned to a SHA or content hash. The label survives every later transformation, including section files, the one-pager, the decision log, and the Score's prompts. (D2, D6, D15, D19)
>
> **Honors:** /g3's one-pager keeps the labels, even though that makes it less clean to read. A Score prompt that depends on a GRU-labelled judgment is preceded by a human task that confirms it.
>
> **Violates:** Removing labels "for readability" at any output stage. Or relabelling a CODE claim as STUDENT because she agreed with it.
>
> **Failure state in production:** An inference becomes a rule one file later. A Score prompt tells Claude to build against a claim no human ever made.
>
> ---
>
> **P3. People resolve disagreements**
>
> **Commitment:** A CONFLICT is a question for a person. Gru never resolves one by giving any source priority. Her resolution is recorded as STUDENT, with her reason. (D8)
>
> **Honors:** A CONFLICT between the docs' scheduler and the privacy rule becomes the next question, and her answer ("the privacy rule governs; the scheduler line in the docs is stale") goes into `decisions.md` with her reason.
>
> **Violates:** "CODE wins unless the student objects." Or any automatic resolution: newest source wins, majority of sources wins, most specific source wins.
>
> **Failure state in production:** Students give way to code that has drifted from its intent. The design document then argues for the bug.
>
> ---
>
> **P4. Read, never run**
>
> **Commitment:** gru reads the repository statically and never executes its code. Every read is visible in the read log. Questions that only running the code can settle are handed to the student as human tasks. (OQ6, D5)
>
> **Honors:** "A static read can't confirm where the export file lands at runtime. Run the export once and tell me the path." That becomes a human task for plausibility auditing, on her machine, by her choice.
>
> **Violates:** Running the test suite to answer a design question. Importing a module to check a default. Running a build script "just to see."
>
> **Failure state in production:** A student's laptop runs a stranger's code for a design question, with side effects, network calls, secrets read, and files written into a team repo. Or reads nobody can see: a missed file leaves no trace, so there's nothing to audit.
>
> ---
>
> **PRINCIPLE COLLISION TEST**
>
> Two real collisions.
>
> **C1: P1 against P2, label laundering.** P1 encourages Gru to pre-fill questions from the scan ("the code says X; is that the intended design?"). When she answers "yes," what label does the claim carry? If it becomes STUDENT, her agreement has laundered a CODE reading, or worse, a GRU inference, into a claim the design says she made. Over a whole interview, "yes" answers turn most GRU and CODE claims into STUDENT claims, and P2 stops meaning anything.
>
> **Proposed rule:** A claim keeps its original source label. Her confirmation is recorded *next to* it (`CODE, confirmed by STUDENT`), never in place of it. A claim is labelled STUDENT only when she supplies the content herself.
>
> **Proposed primary:** P2. Provenance doesn't change by agreement.
>
> **C2: P4 against the /v1 success condition.** /v1 says gru succeeds when "every disagreement between docs and code was put to her as a question." Under P4, gru can't detect a disagreement that only shows up at runtime. The success condition promises something the principle forbids.
>
> **Proposed fix:** Amend the success condition to: "every disagreement a static read can detect was put to her as a question, and every question that depends on runtime behavior was handed to her as a human task."
>
> **Proposed primary:** P4. Safety isn't traded for coverage.
>
> The fixture supports P4, by the way. You found all three contradictions *by reading the code by hand*. You didn't run anything. So D18's fixture tests whether a static read is enough, and your own evidence says it can be.
>
> ---
>
> **OQ10: how gru decides which code is relevant**
>
> Your own fixture adds a requirement here. The scheduler contradiction was **DOC against DOC**: the docs listed a scheduler that the tool's own privacy rule forbids. No code was involved. So the relevance method has to check claims against *other claims*, not only against code. A method that only asks "what code does this question touch?" misses it completely.
>
> The options:
>
> | Method | How it chooses | What it misses |
> |---|---|---|
> | **(a) Term search** | Searches for the question's terms, such as "export" | Anything renamed. `dump_bundle()` writes the export, so her blind spot is back. |
> | **(b) Claim-anchored** | For each DOC or STUDENT claim in scope, reads the code and docs the claim names: folders, config keys, commands, rules | Code no claim mentions |
> | **(c) Structural** | Starts at entry points (manifests, CLI mains, CI) and follows imports and calls to a fixed depth | Doc-against-doc conflicts. Dead or dynamically loaded code. |
> | **(d) Layered** | (b) first, then (c) for coverage, then (a) as a last resort. The read log tags which method found each file. | Least overall, and the method tag in the log shows her *why* a file was or wasn't read |
>
> My recommendation is **(d)**. Option (b) is what you did by hand when you found all three contradictions. You started from what the docs claimed and went to where the claim would be true or false. Option (c) catches code that no claim mentions. Tagging each file with the method that found it makes a miss explainable, which D18 depends on.
>
> This is your call, not mine. The choice decides what gru can find.

From [turn 16](boondoggle-report/gru-session-downloadable-gru/16-v2-locked-v3-flows.md):

> **P4, final wording (pending your accept):**
> > **Read, never run.** gru reads the repository statically and never executes its code. It never opens `.env` files, private keys, or credential stores. It records environment variable names, never their values. It redacts secret-shaped values in any file it does read before writing anything. It records every skip and redaction in the read log. `/gru share` refuses to proceed if a secret pattern matches anywhere in `sdd/`. Questions that only running the code can settle are handed to the student as human tasks.
>
> **Logged:** D20 (C1): a claim keeps its source, confirmation is recorded next to it, and P2 is primary. D21 (C2): the success condition is amended and P4 is primary. D22 (OQ10): layered relevance (b), then (c), then (a), with each file tagged by the method that found it. OQ6 and OQ10 are closed.


### `/v3` — core user flows (locked)

The primary, integration and administrative flows with Gru's three flags, then the decisions that locked the section.

From [turn 16](boondoggle-report/gru-session-downloadable-gru/16-v2-locked-v3-flows.md):

> **/v3: CORE USER FLOWS**
>
> This is drafted from the record, and the steps I couldn't ground are marked **[?]**. Her feature is the export.
>
> **PRIMARY FLOW: install to shared design document**
>
> | # | User action | System response | State change |
> |---|---|---|---|
> | 1 | Clones the course repo | none | Toolkit checkout on disk |
> | 2 | From her team repo root, runs the install command **[? exact form]** | Checks for a git repo, `.claude/skills/gru*` collisions, and an existing `sdd/`. Prints what it will write. | Skill links written, exclude lines added, `sdd/` created, state file initialized with the prompt hash and folder name |
> | | *Decision point:* collision or existing `sdd/` | Stops and names the collision. Never overwrites. | none |
> | 3 | Opens Claude Code in her repo, types `/gru help` | The hub reads the state file and renders the menu with the `/gru` prefix. Deferred commands show "not in this version." The current gate shows as none. | none |
> | 4 | `/gru v0` | For each question: layered read, then the question with labelled, cited, method-tagged claims | Read log appended |
> | 5 | Answers a question | If a source disagrees, the CONFLICT is the next question. Otherwise the next /v0 question. | Answer and pushback appended to the section's working record |
> | 6 | Resolves a CONFLICT | Records her resolution as STUDENT with her reason | `decisions.md` entry |
> | 7 | Confirms the V0 summary | Writes the /v0 section file | State file: gate v0 confirmed, prompt hash, repo SHA |
> | 8 | Closes the laptop. Next day, `/gru v1`. | The hub reads the state, checks the prompt hash, and checks drift in every cited file | Drift and hash change announced before the first question |
> | 9 | `/gru s1` before /v4 is confirmed | Says what's missing and returns to the current phase | none |
> | 10 | Continues through /v4. Phase 1 gate. | Gate question | State file: phase 1 confirmed |
> | 11 | `/gru claude` at any stage | Score for what exists. Labels survive. Each unresolved CONFLICT becomes a human task. | Score file written **[? OQ2: overwrite or version]** |
> | 12 | `/gru share` | Secret check, then lists exactly what becomes visible to git, then asks her to confirm | `sdd/` exclude line removed |
> | 13 | `git add sdd/` and commits in her export PR | none (git's job) | Design document reviewed alongside the change |
>
> **INTEGRATION FLOWS**
>
> | System | Protocol and data | If unavailable or unexpected | Who owns the failure |
> |---|---|---|---|
> | Claude Code skill discovery | Reads `.claude/skills/<name>/SKILL.md` | Skills not found (wrong folder, version change): `/gru` does nothing, silently | Anthropic's contract. Detection is gru's job. **[?]** |
> | git | `rev-parse HEAD`, `.git/info/exclude` | Not a repo: content-hash fallback (D6). Detached HEAD: SHA still valid. **Dirty working tree: see flag A.** | gru |
> | Toolkit checkout (link target) | Symlinked skill folders and the Gru prompt file | Moved or deleted: every link breaks. Pulled: the prompt hash changes (D12). | Student, with detection by gru **[?]** |
> | Filesystem (her repo) | Static reads under the P4 rules | Unreadable or huge files: skipped and logged | gru |
>
> **ADMINISTRATIVE FLOWS**
>
> | Operator | Flow | Status |
> |---|---|---|
> | Bear (maintainer) | Replaces the Gru prompt file. Students see the hash change announced at their next command. | Defined (D12) |
> | Student | Updates the toolkit by `git pull` in the course repo | Defined by implication. The course repo is the channel (OQ5). |
> | Student | **Uninstalls gru from a team repo** | **Missing: see flag B** |
> | Student | Restarts a design, or re-answers a confirmed gate | Open (OQ3) |
>
> ---
>
> **Three flags from the flows:**
>
> **A. Dirty working tree.** She's in the middle of the export change, so `export.py` has uncommitted edits. gru reads the edited file and pins the citation to `HEAD`. The SHA says one version and the quote comes from another. A reviewer who checks out that SHA finds a different line and decides the document is wrong. **Proposal:** when the cited file is dirty, pin to a content hash and mark it `uncommitted`. Only clean files get the SHA.
>
> **B. No uninstall.** Install writes links, exclude lines, and a folder into a team repo. A tool that writes into someone else's repo needs a documented way to undo that exactly: remove the links, remove only the exclude lines it added, and leave `sdd/` alone unless she says otherwise. Is this `/gru uninstall` in v1, or /p2?
>
> **C. The Flow Honesty Test finds the step that depends on the model.** *If this were a CLI with no UI, would it solve the problem?* Mostly yes. The scan, labels, pinned citations, state file, share check, and format checkers are deterministic scripts. **The step that isn't deterministic is step 5: detecting that two sources disagree.** Comparing "exports default to `/out`" with `os.environ["EXPORT_DIR"]` is Claude reading and judging, not a script checking. If the model misses a disagreement, the miss is silent. The read log shows the file was read, but not that the disagreement in it was overlooked. Scripts can check that a citation *exists*. They can't check that the cited line *says what the claim says*. **Proposal:** every CODE and DOC claim carries the quoted excerpt, redacted, next to its citation. Then she can plausibility-audit each claim at a glance, without opening files, and the gap between "cited" and "supports the claim" is where she can see it. The fixture tests the rest.

From [turn 17](boondoggle-report/gru-session-downloadable-gru/17-v3-locked-v4-needs.md):

> /v3 is locked.
>
> **Logged:**
> - **D23:** P4 final, all three layers.
> - **D24:** `./gru install <path>` runs from the toolkit checkout. Detection has two halves: the hub checks itself first inside a session, and `./gru doctor <path>` works from outside. The README tells her to run `doctor` if `/gru` does nothing.
> - **D25:** Dirty files are pinned by content hash and marked `uncommitted`.
> - **D26:** `./gru uninstall <path>` is in v1. It removes only what it wrote and leaves `sdd/` alone unless she says otherwise.
> - **D27:** A quoted, redacted excerpt goes next to every CODE and DOC citation.
>
> One note for /s4, not a blocker. "Only the exclude lines it added" means install has to *remember* which lines those were. A marked block in `.git/info/exclude` (`# gru:begin` … `# gru:end`) makes uninstall exact. That includes the case where `/gru share` has already removed the `sdd/` line, so uninstall must not add it back.


### `/v4` — user and business needs, and the Phase 1 gate question

Eight needs, each with a test, the component filter, three flags, and the gate question.

From [turn 17](boondoggle-report/gru-session-downloadable-gru/17-v3-locked-v4-needs.md):

> **/v4: USER AND BUSINESS NEEDS**
>
> **User Needs (the student)**
>
> **U1. Provenance at a glance.** The student must be able to see, for every claim in her design document, whether it came from the docs, the code, herself, or Gru, along with the exact excerpt it rests on, when she or a reviewer questions a line, *without* opening the repository to hunt for it.
> *Test:* A format checker passes only if every claim has a label, and every CODE or DOC claim has a pinned citation plus an excerpt.
>
> **U2. Disagreements come to her.** The student must be asked about every disagreement a static read detects between docs, code, and her own answers, before the affected section is written, when she starts a design in a codebase she didn't write, *without* knowing in advance which files contradict each other.
> *Test:* The fixture. All three known contradictions surface as CONFLICTs without prompting (D18).
>
> **U3. The scan can be audited.** The student must be able to see what gru read for each question, how it found each file, and what it skipped or redacted, when she suspects the scan missed something, *without* rerunning it or trusting it on faith.
> *Test:* Every question in every section file has a read log with method tags (b, c, or a), skips, and redactions.
>
> **U4. The design survives the session.** The student must be able to resume a design in a new session with every confirmed gate, decision, and piece of reasoning intact, when a session ends or context compacts, *without* re-answering confirmed questions or losing why a decision was made.
> *Test:* Close the session. The next day, `/gru v1` reports v0 as confirmed, checks the prompt hash and citation drift, and cites the relevant D-numbers.
>
> **U5. A build plan with nothing unchecked in it.** The student must be able to generate a Boondoggle Score at any stage, when she is ready to hand work to Claude, *without* any unchecked claim entering a Claude prompt as fact.
> *Test:* Every claim inside a Score prompt keeps its label. No unresolved CONFLICT appears in any prompt. Each one appears as a preceding human task.
>
> **U6. Review on her terms.** The student must be able to put her design document up for review in the same pull request as the change it describes, when *she* decides to, *without* committing secrets or anything she hasn't seen listed.
> *Test:* `/gru share` lists every file that will become visible, refuses on any secret-pattern match, and removes the exclude line only after she confirms.
>
> **Operator Needs**
>
> **O1. Leave no trace in a shared repo.** A student installing into a team repository she doesn't own must be able to install, diagnose, and uninstall gru, *without* changing teammates' `git status` or overwriting anything.
> *Test:* `git status` is identical before install, after install, and after uninstall. A name or `sdd/` collision stops the install. `doctor` reports broken links.
>
> **O2. One file changes the rules, visibly.** The maintainer must be able to update Gru by replacing one prompt file, when Gru's method changes, *without* students' in-progress designs silently switching rulebooks.
> *Test:* Replace the file. Each confirmed gate still shows the hash it was confirmed under, and the next command announces the change.
>
> **Business Need**
>
> **B1. Evidence of thinking, not only a document.** The course must be able to verify that a design document came through the interview, meaning the student confirmed each gate herself and her answers are in her own words, when reviewing or grading it, *without* taking the document's rigor on faith.
> *Test:* The state file shows a confirmation for each gate. The section files hold her answers and Gru's pushback in order (D16). A section with no recorded answers fails the format checker.
>
> That's eight: six user, one operator split in two, and one business need.
>
> ---
>
> **COMPONENT FILTER**
>
> | Component | Serves | Status |
> |---|---|---|
> | Repo-scan script, layered with method tags | U2, U3 | Prototype exists. It must be checked against D22: does it do (b), then (c), then (a)? |
> | Gate-state tracker | U4, O2, B1 | Prototype exists. It must now record the prompt hash per gate (D12). |
> | **Two format checkers** | **U1? U5? B1?** | **Prototype exists. I can't map them: see flag 1.** |
> | **"A few skills"** | **?** | **Prototype exists. I can't map them: see flag 1.** |
> | Hub skill with translation layer and self-check | Entry point for all of them, plus O1 | Designed (D3, D24) |
> | Phase skills (`gru-v0` …) | U1, U2, U4, B1 | Designed. Naming is still open (OQ4). |
> | Redaction and secret-skip | U3, U6 (P4) | Designed (D23) |
> | `decisions.md` writer | U4, B1 | Designed (D17) |
> | Score generator (`/gru claude`) | U5 | Designed (D19) |
> | `/gru share` with the secret check | U6 | Designed (D11, D23) |
> | `install` / `uninstall` / `doctor` | O1 | Designed (D24, D26) |
> | **Menu line "not in this version"** | **None** | **See flag 2** |
> | **/g2, /g3, /g4 and the eight refinement tools** | **None** | **See flag 3** |
>
> **Flag 1: prototype components I can't map.** Rule 1 says no component is documented before it maps to a Need. You've told me the prototype has two format checkers and a few skills, but not *what they check* or *which skills*. Name each one and its job, and I'll map it or flag it. That doesn't mean it's wrong. It means it was built before a Need existed to justify it, which is exactly the case this check exists for.
>
> **Flag 2: "not in this version" serves no Need.** It's honest and cheap, but no U, O or B requires it. You have two options. Tie it to U4 as part of the menu being truthful about what exists, or accept it as a scope note with no Need behind it. I'd pick the first option, but the decision should be on record.
>
> **Flag 3: most of Gru's command library serves no Need here.** Because the prompt is verbatim and the translation layer maps every command, `/gru g2`, `/gru comparable`, `/gru security` and the rest will *work* in v1. Yet none of the eight Needs asks for them, and nobody has decided whether they write files, carry labels, or sit behind gates. So it's a decision for you:
> - **(a)** All of Gru's commands run in v1, and each one follows P2 (labels) and D11 (reviewable). That's more surface to test.
> - **(b)** v1 supports the section path (/v0 through /p5, /g1, /claude) plus /help and /list. Everything else shows as "not in this version," exactly like the deferred commands.
> - **(c)** Something in between. Name which.
>
> This choice drives /p1. A MUST-BUILD list of 40 commands is a very different project from a list of 18.
>
> ---
>
> **When flags 1–3 are answered, this is the PHASE 1 GATE:**
>
> > Before systems and architecture: the problem summary is confirmed, principles P1–P4 are locked with their collisions resolved, the primary flow is documented along with its integration and administrative flows, and eight Needs are written and mapped to components. Does this reflect what you're building toward?
>
> We don't start /s1 until you confirm it.


### Phase 1 gate (confirmed)

Gru's record of the gate passing.

From [turn 18](boondoggle-report/gru-session-downloadable-gru/18-phase1-gate-s1-inventory.md):

> The Phase 1 gate is confirmed. Systems and architecture start now.
>
> **Logged:**
> - **D28:** The "not in this version" line serves U4. The menu has to be truthful about what exists.
> - **D29:** v1 scope is /v0 through /p5, /g1, /claude, /help and /list. Every other command shows "not in this version."
> - **Prototype audit:** every piece maps to a Need, and none of them meets its Need yet. I'll hold /s1 to that. Each component below is documented against its Need, not against what the prototype currently does. The prototype's gap then shows up as a difference between the two, not as the design itself.
>
> Two things in your prototype description conflict with locked decisions, plus one gap in scope:
>
> **1. Checker one requires "a share of paragraphs" to carry labels. P2 says *every claim*.** A threshold is exactly how P2 would erode: 80% labelled means one in five claims has no source. It also shows that we never defined what a *claim* is. Is it a paragraph, a sentence, or a bullet? Until that's defined, "every claim" can't be tested, and it will stay a percentage. This goes to /d1's shared vocabulary as the first term to define. For now I'm logging it as **OQ11**. It must close before checker one's rules are specified in /s1.
>
> **2. The gate-state tracker records "a named person," and D11 makes that file reviewable in a team repo that may be public.** B1 needs to show that *she* confirmed each gate. It doesn't need her full name in git history. Options:
> - her git identity (`user.name`), whatever she has set
> - a handle she chooses at install
> - a role ("design author") plus a git-signed commit
>
> Logging this as **OQ12**. It must close before /s3.
>
> **3. /g1 is in scope but maps to no Need.** Scope (b) includes it, and the component filter has nothing for it. The natural mapping is U6. The compiled SDD is what a reviewer reads in the pull request. Confirm or correct that.


### `/s1` — components (in progress)

The architecture choice and the 11-component inventory, then component 1 as drafted. Gru has not marked component 1 documented: it is waiting on four decisions.

From [turn 18](boondoggle-report/gru-session-downloadable-gru/18-phase1-gate-s1-inventory.md):

> **/s1: Before a single component is documented**
>
> OQ4 (codes or aliases for skill folder names) was due to close before /s1. Before you answer it, it rests on an assumption I want to make explicit. It assumes **one skill folder per command**. Under D29, that's 17 section commands plus /g1, /claude, scan, and the hub, so about 21 folders. Each one points into the same verbatim prompt, and each one could drift from it.
>
> What changes from one command to the next is **the section of the prompt**, not the machinery. Every section command does the same four things: scan, ask with labelled claims, handle CONFLICTs, then write the section and gate it. So the more basic question is how many skills there should be:
>
> | Option | Shape | Cost |
> |---|---|---|
> | **(i) One per command** | `gru-v0` … `gru-p5`, `gru-g1`, `gru-claude`, `gru-scan`, hub. About 21 folders. | 21 things to keep aligned with one prompt file. OQ4 matters a lot. |
> | **(ii) One per job** | `gru` (hub, routing, self-check), `gru-scan`, `gru-section` (runs any /v0 to /p5 command against its prompt section), `gru-compile` (/g1), `gru-score` (/claude), `gru-share`. Six folders. | `gru-section` has to handle /v0's hard gate and /v1's one-question-at-a-time rule as prompt-driven behavior, not code. |
> | **(iii) Hub only** | One skill. Everything else is scripts. | Claude Code sees one large instruction file. Discovery is simplest, and the context load is heaviest. |
>
> My recommendation is **(ii)**. It follows your own rule that skills point into the prompt and never paraphrase it. It keeps the number of places that can drift to six. And OQ4 mostly goes away, because the job names (`section`, `score`, `share`) are neither codes nor aliases.
>
> The cost is honest. Your prototype's `v0` and `intake` skills would become two sections run by `gru-section`, not two folders. They're being rewritten for the new labels anyway, so the rework is small.
>
> ---
>
> **Proposed /s1 component inventory under (ii), in documentation order**
>
> | # | Component | Serves | Prototype |
> |---|---|---|---|
> | 1 | `gru-scan`: layered relevance, method tags, P4 skip and redaction, read log, excerpts | U2, U3, U1 | Structural pass only. Missing D22 and redaction. |
> | 2 | `gru-section`: runs any section command, labelled claims, CONFLICT as next question, section file with pushback in order | U1, U2, U4, B1 | `v0` and `intake` skills on old labels |
> | 3 | State tracker: gates, confirmer, prompt hash, SHA, folder name | U4, O2, B1 | Gates plus who and when. No hash. |
> | 4 | `decisions.md` writer: D and OQ numbers, raised, decided, applied | U4, B1 | none |
> | 5 | `gru` hub: translation layer, truthful menu, self-check, gate enforcement, drift and hash announcements | All, O1, O2, U4 | Hub on old labels |
> | 6 | `gru-score`: labels survive, CONFLICTs become human tasks | U5 | none |
> | 7 | `gru-compile` (/g1) | U6 (pending confirmation) | none |
> | 8 | `gru-share` with the secret check | U6 | none |
> | 9 | `./gru` shim: install, uninstall, doctor | O1 | Unknown. Does the prototype have an entry script? |
> | 10 | Checker one: SDD shape, all claims labelled, excerpts, answers present | U1, B1 | Shape checks. Old labels, threshold, no excerpts. |
> | 11 | Checker two: Score format, labels inside prompts, no CONFLICT used as fact | U5 | Format only |
>
> The scan goes first because U2 depends on it most and the prototype is furthest from it. Everything downstream consumes its read log and its claims.

From [turn 19](boondoggle-report/gru-session-downloadable-gru/19-s1-architecture-component1-gru-scan.md):

> **Logged:**
> - **D30:** Skill architecture (ii), six job-named folders. This closes OQ4.
> - **D31:** /g1 serves U6.
> - **D32:** `./gru` is a new component. Today the prototype scripts are run directly with `python3`.
> - **D33 (closes OQ11):** One claim per bullet, in a bulleted claims list. Each bullet has exactly one label. CODE and DOC bullets also carry a pinned citation and an excerpt.
> - **D34 (closes OQ12):** The confirmer is recorded as a handle she chooses at install. Her `user.name` is suggested but used only if she says yes. Her full name is never recorded by default.
>
> D33 leaves a residual risk, which I'm recording now so it doesn't get lost. "Every bullet is labelled" can be checked by a script. "Prose carries no claims" and "one claim per bullet" can't. A sentence like "Since exports default to `/out`, the new format writes there too" puts an unlabelled claim into prose, and only a reader will catch it. That makes it a plausibility-audit item for her and her reviewer, and it goes to /p4 by name. Checker one can flag the obvious cases, such as prose that contains a file path, a code identifier, or a number. It can't prove the prose contains no claims.
>
> ---
>
> **/s1 · COMPONENT 1: `gru-scan`**
>
> **Maps to:** U2 (disagreements come to her), U3 (the scan can be audited), and U1 (provenance at a glance, because every citation and excerpt starts here). **Flow placement:** primary flow step 4, before every question. Its orientation pass runs once per design. Both pass.
>
> ---
>
> **THE PROBLEM IT SOLVES**
> Whatever the student pastes into a Project carries her blind spots, and nothing in that setup checks a claim against the code. `gru-scan` decides what gets read for each question, independent of what she already knows about. It returns what it found as labelled, cited, excerpted claims, together with a full record of what it read, how it found each file, and what it didn't read.
>
> **HOW IT WORKS**
>
> Every step is assigned to either a script or the model. This split is where Flow Honesty flag C applies.
>
> | Operation | Done by | What it does |
> |---|---|---|
> | **Orientation pass** | Script (the prototype's `repo_scan`, extended) | Runs once per design and again when HEAD moves. Maps structure: languages, layout, entry points, declared commands, tests, CI, docs, skills, TODOs, and the N most recent commits. Builds two indexes: an **entry-point index** for method (c) and a **doc-claim index** (every doc file, broken into candidate claim sentences) for method (b). |
> | **Claim extraction** | Model | Picks out the doc-claim sentences relevant to the current question, plus any STUDENT answers already given. |
> | **(b) Claim-anchored read** | Script finds, model reads | For each claim in scope, the model names its anchors: paths, config keys, env var names, commands, identifiers. The script finds where each anchor appears in code **and in other docs**, since the scheduler case was DOC against DOC. |
> | **(c) Structural read** | Script | From the entry points relevant to the question, follows imports or calls to depth *d*. Python uses `ast`. Other languages: see decision 3. |
> | **(a) Term search** | Script | Searches the question's terms as a last resort. Any file found only by (a) is marked as such. |
> | **Pinning and excerpts** | Script | Each cited range is pinned to the commit SHA if the file is clean, or to a content hash marked `uncommitted` if it isn't (D25). Excerpts are pulled by line range and redacted **before** the model or any file sees them. |
> | **Support or contradiction judgment** | Model | Decides for each claim whether the read code supports it, contradicts it, or is silent. **Absence counts as a finding.** "Reads `EXPORT_DIR`, and no default is assigned anywhere in the files read" is exactly the finding your fixture depends on. |
> | **Conflict candidates** | Model | Pairs of claims that disagree (DOC and CODE, DOC and DOC, STUDENT and anything) go to `gru-section`, which asks. The scan never asks and never resolves. |
>
> **Inputs:** repo path; the question's ID and text; claims in scope; the orientation indexes; HEAD SHA and dirty-file list.
>
> **Outputs:**
> - **Claims list:** one bullet each, `LABEL | claim | path:lines @ SHA or hash [uncommitted] | redacted excerpt | method tag`
> - **Conflict candidates:** claim pairs, each with its evidence
> - **Read log entry** for the question: files read with a b/c/a tag, anchors and search terms used, files matched but not opened, deny-list skips with reasons, redactions (path, line, and pattern type, **never the value**), and whether the read budget was hit
> - **Orientation cache:** raw, and never shared. See decision 1.
>
> **State changes:** It appends the read log to the working section record and writes the orientation cache. It **never** touches gate state, section content, or anything else in her repo.
>
> **Error signals:**
> - Not a git repo: content-hash mode is announced once.
> - Binary or oversized file: skipped and logged.
> - Language unsupported for (c): falls back to (a), logged as `c-unavailable`.
> - Read budget exhausted: stops, and logs every match it didn't read.
> - An anchor found nowhere: reported as a finding ("no code references `/out`").
>
> **Retry behavior:** The script half is deterministic. The same question at the same SHA gives the same candidate files. The model half can vary between runs, so the read log records which files were actually read each time, not just which were eligible.
>
> ---
>
> **PRINCIPLE ALIGNMENT**
> - **P4:** Static only. It applies the deny-list, redacts before any excerpt leaves the script, records env var names only, and doesn't follow symlinks out of the repo.
> - **P2:** Labels, citations and excerpts are attached *where the claim is found*, so everything later only has to keep them, not reconstruct them.
> - **P1:** It produces evidence and conflict candidates. It never writes section content and never asks a question on its own.
> - **P3:** It reports disagreement and never ranks sources. The contradiction judgment says what disagrees with what. It never says which source is right.
>
> ---
>
> **EDGE CASES**
>
> | # | Situation | Expected behavior | Priority |
> |---|---|---|---|
> | 1 | **A symlink in her repo points outside it** (`config -> ~/.ssh/`) | Not followed. Logged as `skipped: symlink leaves repo`. | **Must-Fix.** Without this, a static read can leak her home directory into a reviewable log. |
> | 2 | **A secret-shaped value is the very thing a claim is about** ("the endpoint is `https://…?token=…`") | Excerpt redacted. The claim is marked `value redacted: verify locally` and becomes a human task. | **Must-Fix** |
> | 3 | **The code is renamed or loaded indirectly** (`dump_bundle()`, config-driven dispatch, dynamic import) | (b) finds it if a claim names the config key. (c) misses dynamic loads. (a) misses renames. Whatever is missed shows as "anchor found nowhere" or as matches not opened. | Important. This is the residual risk U3 exists for. |
> | 4 | **The DOC claim has no anchor** ("exports are handled carefully") | Recorded as `no anchor`, and `gru-section` asks her to make the claim specific. | Important |
> | 5 | **Large repo or monorepo** | Budget bound. The truncation and every unread match are logged. | Important |
> | 6 | **Vendored or generated code** (`node_modules/`, `vendor/`, `build/`) | Skipped by rule and logged. If a claim's only anchor is there, that's reported. | Important |
> | 7 | **A recent commit diff contains a secret that was later reverted** | Diff excerpts are redacted like any other file. | **Must-Fix** |
> | 8 | **The tree is dirty mid-change** | Content hash plus `uncommitted`, per file (D25) | Important |
>
> **Critical edge cases:** 1, 2 and 7. Each could expose secrets through a file D11 makes reviewable.
>
> ---
>
> **SCOPE BOUNDARY**
> `gru-scan` does **not**:
> - ask the student anything
> - resolve or rank a CONFLICT
> - write section content
> - execute any code in the repo
> - open deny-listed files
> - follow symlinks outside the repo
> - make network calls
> - read git history beyond the N most recent commits
> - write anywhere except the read log and its orientation cache
>
> **PROTOTYPE GAP**
> The prototype's `repo_scan` is roughly the orientation pass without the two indexes. Everything else is new: per-question reads (b), (c) and (a), method tags, pinning, excerpts, redaction, the symlink rule, absence findings, and conflict candidates.
>
> ---
>
> **Four decisions before I mark component 1 documented:**
>
> 1. **Where the orientation cache lives.** D11 says raw scan output stays excluded, but `/gru share` removes the exclude line for `sdd/`. If the cache is inside `sdd/`, sharing exposes it. **Proposal:** put it in `.gru/` at the repo root, with its own exclude line that `share` never touches and `uninstall` removes.
> 2. **Read budget per question.** A fixed number of files, a fixed number of lines, or both? What's the default? I'd start at 25 files or 3,000 lines, whichever comes first, adjustable per question, and always logged when hit.
> 3. **Languages for method (c) in v1.** Python via `ast` is standard library and reliable. JavaScript and TypeScript would need regex heuristics. **Proposal:** (c) is Python-only in v1. Other languages fall back to (a), logged as `c-unavailable`, and /p2 records a reopen condition.
> 4. **Recent commits.** How many does the orientation pass read, and does it read the diffs or only the messages? Diffs are where reverted secrets live (edge case 7).

---

## Evidence

Where to check each claim in this log. Commits are listed in the push table below; their IDs are in `git log`, and links are added one push later, because a commit can't link to itself.

| What | Where |
|---|---|
| The brief | `boondoggle-report/BRIEF.md` |
| Every Gru turn, verbatim | `boondoggle-report/gru-session/00-help.md` … `09-v1-what-it-gives-priya.md` |
| How Gru was run, the prompt's SHA-256, the two false starts | `boondoggle-report/gru-session/README.md` |
| The confirmed `/v0` sentence and the open questions (both for the wrong application) | `boondoggle-report/README.md`, under "The false start" |
| First push: the greenhouse-watch start | [`ed99b3d`](https://github.com/nikbearbrown/info-7375-computational-skepticism-for-ai/commit/ed99b3d) |
| Second push: the correction to the downloadable Gru, mistakes kept | [`1491155`](https://github.com/nikbearbrown/info-7375-computational-skepticism-for-ai/commit/1491155) |
| Every turn of the session on the downloadable Gru, verbatim | `boondoggle-report/gru-session-downloadable-gru/00-help.md` … `19-s1-architecture-component1-gru-scan.md` |
| How that session was run, and its prompt's SHA-256 | `boondoggle-report/gru-session-downloadable-gru/README.md` |
| Gru's section outputs, `/v0` through `/s1` so far | This file, under "Gru's section outputs" |
| The own-voice paragraph after `/v1`, drafted by Claude Code and not yet Professor Bear's words | `boondoggle-report/PARAGRAPH-AFTER-V1-DRAFT.md` |

---

## GitHub pushes

One line per push to GitHub: the date and the commit note. The commit ID for each push is in `git log`; a commit can't contain its own ID.

| Date | GitHub note |
|---|---|
| 2026-09-24 | feat(fall-2026): start Professor Bear's Boondoggle Report with ten Gru turns and a Frictional log |
| 2026-09-24 | docs(fall-2026): state that Assignment 2 specifies a downloadable Gru, and keep the wrong-application start on the record |
| 2026-09-24 | docs(fall-2026): log Gru's /v0–/v4 outputs for the downloadable Gru, with all 20 turns verbatim |
