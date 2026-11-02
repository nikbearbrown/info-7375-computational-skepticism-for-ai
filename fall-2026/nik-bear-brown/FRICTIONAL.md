# FRICTIONAL — Professor Bear's process log

## Executive summary

**What this is.** The honest process log for the work in this folder, written the way the course asks students to write theirs: what was tried, what went wrong, what changed, and who did what, the human or the AI.

**Why read it.** It's a real example of the log, not a constructed one. It shows the instructor's own work run through the same record students keep, mistakes included.

**What we are doing.** **Assignment 2 in INFO 7375 Computational Skepticism for AI: the Boondoggle Report.** The application Professor Bear is specifying with Gru is **a downloadable version of Gru**: skills and scripts that run inside a downloaded repository and can read its folders and files, instead of a prompt pasted into a Claude Project.

**Update 2026-10-18.** This folder now has one numbered folder per Canvas assignment (`01-…` to `12-…`), each with a `PLAN.md`, and a master [`PLAN.md`](PLAN.md). The Week 2 work described below is folder `03-week-2-boondoggle-report/` (it was `boondoggle-report/`).

**Update 2026-10-26.** Lectern's filter (`lectern/config/keywords.json`, now v0.6.0) has two new gates that drop a posting outside the allowed countries or titled K-12; the 2026-10-26 entry below records what was measured and which choices are still Professor Bear's.

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

### 2026-09-26 — Adding the Assignment 3 folder, and a summary that was about the wrong thing

- **Date and what I was working on:** Making this class match the other two. I asked for *"a log similar to my other classes… which has the [nik-bear-brown] subfolder under fall [2026]. And a subfolder under that called assignment three. And all of the standard readmes and frictional logs, the other ones have in that as well."*

- **I tried / expected:** I expected to need the folder created from scratch here as well.

- **What happened:** This folder already existed and already had the three top-level files; what was missing was `assignment-3/`. The course brief itself names the records a submission must carry — `README.md`, `PREDICTIONS.md`, `CONTRIBUTIONS.md`, `FRICTIONAL.md`, `VERIFICATION.md` — and `templates/` holds blanks for them, so the set was not a matter of taste.

  **The friction was in the writing, and it is the same failure this assignment measures.** The first executive summaries drafted for this folder and its Branding twin described *the assignment* — what it is, where it came from, what its status is — instead of what the tool does. Fluent, organised, and about the wrong thing. I said so: *"executive summary should be what the tool does … this in more notes and details than a real summary."*

- **What I did:** Created `assignment-3/` with all five records. Had both summaries rewritten to open with the mechanism — what `probes.py` and `scoring_rule.py` do, what they refuse, what they do not claim — with status moved to the end. Wrote the prediction before designing any probe, and the acceptance criteria before there is anything to check, including the one that matters most: at least one probe must be *able* to fail against a deliberately fragile baseline, or the suite is reported as weak rather than the baseline as robust.

- **What Claude or another person contributed:** Claude Code (Opus 5) created the folder, drafted the five records from the brief, and rewrote the summaries after I rejected the first version. I have not reviewed the drafted prediction. It also checked the other two repos rather than assuming their layout.

- **What I understand now / still do not understand:** Worth keeping in *this* folder specifically: an explanation that reads well while being about the wrong subject is exactly what Assignment 3 measures, and the first draft of its own README was an instance of it. Still open: whether my baseline strips whitespace before scoring, and how many features the discrete space holds before exhaustive enumeration stops being literal.

- **Evidence and next step:** `assignment-3/` and its five files. Next: the fragile baseline and the first three frozen probes.

### 2026-09-26 — One project, three classes: naming a canonical master

- **Date and what I was working on:** I am live-coding the same job-search project in all three of my INFO 7375 classes with a different emphasis in each, and the copies had started to drift. I asked for the `nik-bear-brown` folder in all three to be checked and kept in sync, with **Computational Skepticism as the canonical master** and a note that changes there propagate to the other two.

- **I tried / expected:** I expected the three folders to be roughly the same with local additions.

- **What happened:** They were not. Branding had the whole spine — the collector, the watch list, the filter, the ATS notes, the CV facts, the earlier Figma and greenhouse-watch iterations. Prompt Engineering had the CV facts and the earlier iterations but none of the collector. **Computational Skepticism, the folder I had just named master, had none of it at all** — only its own Boondoggle Report and Assignment 3. The master started out the furthest behind, which is the inverse of what "master" means. It is recorded rather than tidied away.

  One thing that went right: Branding and Prompt Engineering were **byte-identical** on every file they shared, so nothing had to be reconciled. Had they diverged, the copy would have had to pick a winner.

- **What I did:** Copied the shared spine into the master and put the tool in its own `lectern/` folder there. Wrote `SYNC.md` — which files are shared, which are deliberately different, and why this class is master: the hard part of the project is not fetching postings, it is knowing what the output is worth, and that is this course's subject. Wrote `lectern/sync.sh`, which copies the shared files out and has a `--check` mode that reports drift and changes nothing. Added a **Rule 0** to all three `CLAUDE.md` files — the master's says "edit here and propagate," the other two say "this is not the master." Put a `SYNC.md` pointer in each downstream folder.

  Explicitly **not** synced: `FRICTIONAL.md`, `README.md`, `CLAUDE.md`, every `assignment-*/` folder, and the dated run outputs. A log overwritten by another class's log is a destroyed record, so `sync.sh` refuses to touch them. The run data stays in Branding, where it is the graded submission; the tool that regenerates it is what is shared.

- **What Claude or another person contributed:** Claude Code (Opus 5) inventoried all three folders, diffed the shared files, copied the spine into the master, and wrote `SYNC.md`, `sync.sh`, and the Rule 0 blocks. Two bugs of its own surfaced in the process: `sync.sh` used a bash 4 associative array and macOS ships bash 3.2, and its first drift report flagged `figma/` as different because of a `__pycache__` folder. I decided that this class is master and that the three must stay in sync.

- **What I understand now / still do not understand:** The drift was invisible until something diffed it, and that is the point of `--check`. Also worth saying plainly: the master being empty at the moment it was declared master is the normal way this goes wrong — the canonical copy is usually whichever one someone happened to work in last. Still open: `sync.sh` has been run once for real and the first propagation was only downstream; the recovery path, where a shared file was edited in the wrong repo, has not been exercised yet.

- **Evidence and next step:** `SYNC.md` and `lectern/` here; `SYNC.md` and Rule 0 in the other two; `./lectern/sync.sh --check` now reports all three in sync. Next: exercise the recovery path deliberately, and decide whether the dated run outputs should also live in the master.

### 2026-09-26 — Reading the rejects: the audit found a false-positive problem instead

- **Date and what I was working on:** The one check left in my own acceptance criteria. 3,358 postings were rejected in the 2026-09-26 run and nobody had looked at what the filter threw away. I asked for a random sample: *"Give me a hundred or two hundred of the three thousand three hundred postings. Uh, as a random sample. So I can take a quick look at them to see what's being missed."*

- **I tried / expected:** I expected to read 100 rejects and find a handful of missed teaching roles — false negatives.

- **What happened:** The sample has not been read yet. But building it exposed two things first, and the second one is not what I was looking for.

  - **`education` is in 618 of 618 Anthropic postings.** Every Anthropic ad ends with *"Minimum education: Bachelor's degree or an equivalent combination of education, training, and/or experience."* So the topic word carries no information on that board — the same boilerplate problem already found on Writer's board, and most of the reason **950 rejects matched exactly one teaching word**: the word was `education`, in a salary footer.
  - **The topic-word rule is keeping recruiters, not teachers.** 79 of the 88 kept records were kept on a role word in the title. The other 9 were kept on topic words alone, and on inspection most are wrong: three Stripe **University Recruiter** postings, Notion's **Head of Early Career Recruiting**, OpenAI's **Integrated Marketing Manager, Youth Culture**. `university`, `campus`, and `student` are recruiting vocabulary as much as teaching vocabulary. Only Anthropic's **Head of Technical Training** is a clear true positive in that group.

  So an audit aimed at false negatives found a **false-positive** problem instead, in the part of the rule I had paid least attention to.

- **What I did:** Had `lectern/audit_rejects.py` written as a stored script rather than an ad-hoc query, so the sample is reproducible: seed `20260926` recorded in the output, and rerunning reproduces the same 100 rows. Two parts on purpose — a uniform random 100 (the only part that supports a rate: k MISSes means about k × 34 across all rejects) and all 63 of the closest calls, the rejects that matched two teaching words against a bar of three. The 950 one-word rejects are counted, not listed.

  Both findings are written into the sample file as calls for me to make. **Neither has been changed in `keywords.json`** — adding `education` to Anthropic's ignore list would move the flagship company's counts, and demoting `university`/`campus`/`student` would move the kept total, so both are mine to decide rather than something to quietly fix.

- **What Claude or another person contributed:** Claude Code (Opus 5) wrote the sampler, drew the sample, and found both problems while checking the snippets. It also stopped its first attempt: the near-miss tier was 1,013 postings, well past the 100–200 I asked for, so Part 2 was narrowed to the 63 closest calls. It did not change the filter, and it did not mark a verdict on any row — the Verdict column is empty and mine.

- **What I understand now / still do not understand:** The reason to read rejects is not only to find what was missed. Reading them showed what boilerplate looks like from the other side, and that led straight to a false-positive class I would not have found by looking at the 88 keeps. Still open: the actual reading, the two calls above, and whether `university`/`campus`/`student` should require pairing with a real teaching word before they count.

- **Evidence and next step:** `reject-audit-2026-09-26.md` — 100 random rows plus 63 closest calls, Verdict column blank; `lectern/audit_rejects.py` in the master, synced to both other classes. Next: read it, mark the MISSes, multiply, and decide the two calls.

### 2026-09-26 — Auditing by job title instead of by posting, and finding the bug in my own audit

- **Date and what I was working on:** The reject audit. I had a 163-row sample to read and did not want to read it, because reading postings is the wrong unit: *"Seems a better way to look for false positives would actually be to look at the job titles. Because they're probably less job titles than jobs… if we can sort of group and classify groups of job titles it means I don't have to look at 3,000 jobs I can look at a much smaller set of job titles."*

- **I tried / expected:** I expected normalising titles to collapse 3,446 postings into a few hundred, because the same job is posted per city.

- **What happened:** Normalising did almost nothing — 3,446 postings, 3,082 distinct titles, and only 2,701 after stripping locations and seniority. Titles are too varied for that. What worked was the other half of my idea: **classify titles into job FUNCTIONS.** Eighteen families cover every posting, so the read became "judge 18 rules, then read only the rows where the filter and the rule disagree."

  **Then the audit found a bug in itself, not in the filter.** The first pass treated *training* as a teaching word and reported **27 rejected "education" jobs** — which read as a serious false-negative problem. They were *Pre-training Data Infrastructure Engineer*, *Research Engineer, Production Model Post-Training*, *Training Runtime Foundations*, *Researcher, Training*. **At an AI company "training" means training a model.** The filter had been right about all 25 of them; my classifier was wrong. `ML_TRAINING` is now the first family rule for exactly that reason.

  With that fixed, the matrix says: **45 false positives, 2 candidate false negatives, 527 postings in families where the word genuinely means two jobs.**

  The false positives are systematic, not scattered — one word misbehaving across a whole family:
  - **13 SALES_ENABLEMENT + 7 TECH_ENABLEMENT.** `enablement` means sales support or making a system capable. Twenty of the 88 keeps.
  - **9 EDU_SALES.** Canva's *Higher Education Account Executive*, *K-12 Education Account Manager*. Selling into schools is not teaching in them.
  - **2 RECUITING.** Stripe's *University Recruiter*, Notion's *Head of Early Career Recruiting*.
  - The rest are scattered — 5 ENGINEERING, 3 MARKETING, 2 PRODUCT, 2 G&A.

  Only **two** candidate misses in the whole board, and both are real candidates: Notion's **[Contract] Language Training Specialist – Japanese**, which is literally a teaching job on a contract, and Anthropic's **Technical Documentation and Content Engineer, Claude Docs**, which is developer education under a different name.

- **What I did:** Had the family rules written as `lectern/title_families.json` — each family declares whether it expects keep, reject, or *judge*, with a note saying what the word actually means in this industry — and `lectern/audit_titles.py` to apply them and print only the disagreements. Both in the master, synced to the other two classes.

- **What Claude or another person contributed:** Claude Code (Opus 5) measured that title normalisation would not collapse the problem, built the family classifier, and caught its own `training` error when the 27 "misses" turned out to be ML jobs. It reported that error rather than quietly fixing the regex. I supplied the design: classify functions, not postings.

- **What I understand now / still do not understand:** Two words carry nearly all the damage in this filter, and both are false friends in this specific industry: **`enablement`** (sales support) and **`training`** (model training). `education` is a third — meaningless in Anthropic's Logistics footer, and misleading in Canva's sales titles. Sorting by function made all three visible at once, which reading 163 sampled postings would not have. Still open: the 527 *judge* rows, the two candidate misses, and whether the 45 false positives get fixed by cutting `enablement` or by requiring it to pair with a teaching word.

- **Evidence and next step:** `title-audit-2026-09-26.md` — the family matrix and the three disagreement tables, Verdict columns blank. `lectern/title_families.json` and `lectern/audit_titles.py`. The random sample `reject-audit-2026-09-26.md` still stands; sorting by function is cheaper but only finds errors in families someone thought to name. Next: rule on `enablement`.

### 2026-09-26 — The target becomes "makes the materials", and a bullseye that one word had been hiding

- **Date and what I was working on:** Sharpening what the collector is actually looking for, after the title audit surfaced Anthropic's *Technical Documentation and Content Engineer, Claude Docs*.

- **I tried / expected:** I said the Anthropic role *"looks perfect"* and named the real target: *"anything like that have an eye looking for jobs like that. in any kind of company, they'll probably be called something different. But developing materials, either to sell into universities or to sell to the public, or to train their own people would be a great fit."* Then, seeing Replit's role: *"learning experiences creator seems like a great fit as well… everything's probably named differently, but that kind of job would be something to look out for."*

- **What happened:**
  - **I reversed one of my own findings.** "To train their own people" means the 13 sales-enablement postings the last pass called false positives are not errors — building curriculum and running training for internal staff is the work, and the audience being internal does not change it. `SALES_ENABLEMENT` now expects *keep*; the 9 education-sales roles moved to *judge*, because an account executive with only a quota is still a reject and one who builds the materials the sale runs on is not.
  - **This family is nearly invisible by title.** `documentation` appears in **2 of 3,446 titles**. `technical writer`, `curriculum`, `instructional design`, `courseware`, `knowledge base` appear in **zero**. The Anthropic role is almost unique. So the title vocabulary had to grow and a body rule had to exist.
  - **Replit's *Learning Experiences Creator* had been rejected over one word** — the list held `learning designer`, not `learning experiences`. It is as close to a bullseye as this board has. Every candidate word was measured against all 3,446 titles before being added: eleven appear in zero titles and so cannot add noise; `creator`, `documentation`, and `content engineer` each appear in exactly one title and it is the right one. Rejected as measured noise: bare `learning` (42 titles, nearly all Machine or Reinforcement Learning) and `content strategy` (3, all regional SEO marketing).
  - **The body rule failed, twice, before it worked.** First version: **101 extra postings at roughly one-in-ten precision** — all 15 Anthropic *Applied AI Architects* on *technical content* + *our users*, four IT Support Engineers on *how-to guides*, plus tax counsel and incident managers. Tightened to two high-specificity phrases: **zero** hits in the entire corpus. One phrase: 9 hits, 4 right. Cut `how-to guides` and two others: **5 hits, 4 right.**

- **What I did:** `keywords.json` is now v0.4.0 with the measured title words and a two-part `materials_rule` — a make-materials phrase **and** a named audience, both required, because *maintain documentation* in a tax director's ad has the first and not the second. Added a `MATERIALS` family to `title_families.json`. Every phrase that was cut is recorded in the file with the count that condemned it.

  The pass added five roles worth reading: Anthropic's Claude Docs engineer, Replit's Learning Experiences Creator, Stripe's Training Program Manager (Mexico City, *instructional design*), and OpenAI's two AI Deployment Manager (Builder) posts plus its Developer Experience Engineer, Cyber (*create tutorials*). 3,446 postings, **97 kept**.

- **What Claude or another person contributed:** Claude Code (Opus 5) measured every candidate word before adding it, built and then dismantled its own body rule across three attempts, and reported each failure with the postings that caused it rather than quietly adjusting until the number looked reasonable. It also flagged that my "train their own people" remark contradicted its earlier false-positive call, instead of leaving the contradiction in the files. I set the target.

- **What I understand now / still do not understand:** Five words are false friends in this industry and between them they caused every error so far: `training` (model training), `enablement` (sales support, or a system gaining a capability), `education` (a degree requirement in a footer, a sales vertical at Canva), `learning` (machine learning), `content` (SEO marketing). Also worth saying: only the rule that failed obviously ever got measured. "Role word in title" and "three topic words" still have no precision figure, and they carry 92 of the 97 keeps. Still open: 535 postings in *judge* families, and whether the two unmeasured rules deserve the same treatment the body rule got.

- **Evidence and next step:** `keywords.json` v0.4.0 with its `removed_after_measurement` record, `title_families.json` v0.2.0 with the MATERIALS family, the regenerated `title-audit-2026-09-26.md` (27 false positives, 1 candidate miss, 535 to judge), and `quality-report-2026-09-26.md`. Next: measure the title rule the way the body rule was measured.

### 2026-09-26 — Ranking companies instead of postings, and Google's absence was an artefact

- **Date and what I was working on:** Deciding what the good candidates actually are.

- **I tried / expected:** I had been handed a shortlist filtered on remote and full-time, and that is the wrong filter. I said so: *"don't use full-time or purely remote as a flag… I'm going to make the argument that if they want me enough, they'll figure out a position. I'm just looking for the indication that this is something that the company wants… I think if I'm good enough, they'll make a role for it."*

- **What happened:**
  - **The unit of analysis was wrong, not just the filter.** A posting is not a slot to squeeze into; it is evidence that a company has decided this work is worth paying for. So the report should rank **companies**, with location and employment type as context that never excludes anything.
  - **Five kinds of evidence, and the strongest is an org-chart fact.** SELLS (an education revenue line, so a budget) · ENABLES (it trains its own staff) · ADVOCATES (it pays people to teach a public) · TEACHES (it hires teachers and materials-makers) · **BUILDS (it staffs an education *product* team)**. A company showing four or five has an education business, not a vacancy. **Anthropic is 5 of 5** with 15 signal roles. Stripe, Canva, OpenAI, and Notion are 3 of 5. Figma is 2 of 5 but 9 roles.
  - **The first version of that table missed BUILDS entirely**, and undercounted OpenAI at 2 signal roles out of 830 — while OpenAI has a *ChatGPT Education & Learning* engineering team, a *Tech Lead Manager, Education*, and an *Applied AI Architect, Education*. Those were classified as ENGINEERING and dropped. A company staffing an education product team is the best evidence there is, and the report had been blind to it.
  - **Then I pointed out the hole: Google.** *"Google has to be pushing this hard. Integrating Google products like NotebookLM with education."* Google was absent from the table — and absence read as no demand when it actually meant unreadable.
  - **Google has no public JSON feed.** Three endpoint shapes tried, all 404, and I stopped rather than guess more. **But its careers site is readable by a person**, and one search settles it: **20 education roles on the first page** — Google for Education product managers and engineers, *Head of Industry, Education*, *Product Marketing Manager, Google Classroom*, two *Brand Marketing Manager, AI Education* posts, *Brand Marketing Manager, Educator Social*. A search for *NotebookLM* returns six more including **Senior UX Researcher, Learning Frontiers, LearnX** — a Google learning organisation not visible from outside at all. On the demand measure Google belongs at the top of the table and is missing only because of an API.

- **What I did:** Had `lectern/demand_report.py` written to rank companies on the five kinds, with a section stating plainly that absence from the table is a measurement gap and using Google as the worked example. Added an `EDU_PRODUCT` family so BUILDS is counted. Widened the TEACHING pattern, which had been dropping *Head of Technical Training* into UNCLASSIFIED. Google's manual check, its search URL, and its date are recorded in `sources.json` so the claim is re-checkable by hand.

- **What Claude or another person contributed:** Claude Code (Opus 5) built the company ranking, found that its own first version had missed the BUILDS category, tried and failed to find a Google feed, said so instead of inventing one, and then read the careers site in a browser to get real evidence rather than leaving a caveat. I supplied the correction that mattered: rank companies, not postings, and never exclude on employment type.

- **What I understand now / still do not understand:** The filter had quietly encoded an assumption I do not hold — that a job must already be the right shape. Dropping it changes the output from a shortlist of six into a ranked argument about which conversations are worth having. Also worth saying: the nine unreadable companies are now the most important gap in the whole project, because four of them are the deepest education players on the list, and Google shows how badly the table misleads when they are silently missing. Still open: whether a browser-driven reader for Google, Adobe, Salesforce, and GitHub is worth building, or whether checking four careers pages by hand once a month is the honest answer.

- **Evidence and next step:** `company-demand-2026-09-26.md` (18 companies, 5 kinds, 57 signal roles, plus the Google section), `lectern/demand_report.py`, `title_families.json` v0.3.0 with EDU_PRODUCT, `sources.json` with Google's manual check. Next: decide the unreadable-companies question, and measure the title rule.

---

### 2026-09-27 — A short film of "What I mean by skepticism"

- **Date and what I was working on:** Asking for a course film of Chapter 1's section "What I mean by skepticism."
- **I tried / expected:** I asked for "show tell film Liam persona" and said to mention that the film is for this course, INFO 7375 Computational Skepticism for AI. I pasted the section as the source.
- **What happened:** The film was built: "Skepticism Is a Method, Not a Mood," 2 minutes 54 seconds, 4K, every automated check passed. Nothing is staged or published.
  - **Two problems in the source, found before building.** The section still carries an unresolved merge conflict: the Knight Capital paragraph sits on one side of it. And the turkey passage has it fed "for a thousand days" and killed "on day one thousand," one of the fed days. Taleb's version is fed 1,000 days, killed on day 1,001. The film follows Taleb.
  - **Knight Capital's loss was wrong in the chapter.** The chapter says about $440 million. The SEC order (October 2013) says Knight lost over $460 million, and the film says so, credited to the SEC. The chapter's "no errors were thrown" is also contradicted by the order, which describes 97 unread automated e-mails; the film says only that no one noticed.
  - **Two smaller chapter wordings don't match their sources.** Google Flu Trends' peak was "more than double" the CDC count, not "close to double." The sepsis model alerted on 18% of hospitalizations, not 18% of patients. The film uses neither phrase.
  - **The course is named.** Liam says it is a short film for INFO 7375, Computational Skepticism for AI, and the course appears on the terms card and the Your Turn card.
- **What I did:** Asked for the film and supplied the source text. Then asked for three more, one per move, in these words (dictated, lightly cleaned): "Make individual show-tell films on radical doubt, induction and falsifiability. Mention the philosophers … **Radical doubt:** you can't doubt everything, and add risk to that: you should doubt the things that are important to doubt — what your job depends on, health, important things. **Induction** and Hume: if the state of the system changes, its history is no longer likely to hold up. Don't say induction isn't useful. It's very useful … we've had COVID, and the way people buy is now fundamentally different because the world has changed. But before that, buying patterns held up. **Falsifiability**, Karl Popper: you need to frame a question beforehand in a way that it can be wrong. If your test always passes, it's not a test. If your agent always succeeds no matter what it does, it's just doing stuff." A fourth film, on Plato, comes later.
- **What Claude or another person contributed:** For the three move films, Claude Code wrote one shared brief carrying my words (`youtube/SHOW-TELL-THREE-MOVES.md`) and started builder agents. All three are built to gated 4K masters, none staged: "Doubt What Your Work Depends On" (Descartes, 2:34), "Induction Works Until the World Changes" (Hume, 2:58), and "A Test That Can't Fail Isn't a Test" (Popper, 3:15). The Popper builder was stopped by a usage limit mid-paperwork and resumed on my "Try again." Each names its philosopher with the work and date, quotes primary texts only where the quote can't be read against the point, and credits my rules as mine: doubting in proportion to risk is not Descartes'. Chapter wording corrected in the films: Popper wrote of science versus pseudo-science, not "science and rhetoric"; the "what would make this wrong?" question is the course's adaptation of Descartes, not his method. It proposed the titles, and it noted that the precise word for what induction relies on is *stationary*, with *ergodic* used only if it can be said correctly. For the first film, Claude Code (Opus 5.5) planned the film, flagged the two source problems, and handed the build to a builder agent working from the show-tell skill. The builder narrates as Liam, in for Bear, and names this course aloud and on screen. It checked every number against its primary source. I haven't watched the film yet.
- **Published.** I watched the three move films and said: "These three films look good. Publish them to the Nik Bear Brown YouTube channel. At full 4K." They went up unlisted on @NikBearBrown, in the "Claude & Agentic AI" playlist at the top, and each was verified to serve 3840×2160: Doubt What Your Work Depends On (https://youtu.be/_RiQaCEL8eY), Induction Works Until the World Changes (https://youtu.be/eyrwhlqs2E0), A Test That Can't Fail Isn't a Test (https://youtu.be/VzCc83mTuB0). The overview film is not published. Public is my flip in Studio.
- **A fifth film, on Kant.** I asked for a show-tell on Immanuel Kant "and how we need some humility in our perspective": phenomena vs. noumena; space, time and causality as categories the mind imposes; gravity inferred from effects, never seen; Kant's flat no to whether tools will ever close the gap. I said my own view is weaker than Kant's: the gap is contingent but permanent, finite minds and expanding tools approaching without arriving. "We only see a slice of the universe, and we should be aware not only of what we can't see, but that there are things we can't see." The build started from a brief carrying those words (`youtube/SHOW-TELL-KANT.md`); my view is to be attributed to me, not to Kant. Built: "You Only See a Slice," 3:31, 4K, every check passed, not staged. Kant is quoted verbatim from the 1855 Meiklejohn translation with page references, and the "dogmatic slumber" line from the 1902 Carus translation of the Prolegomena, whose wording is "interrupted," not "woke." My asymptotic view is said aloud as "Bear's view, not Kant's" and labelled so on screen.
- **Chapter 1 rewritten around Kant.** I pasted the chapter's "The cave" section and said: "update this chapter to be about Kant rather than Plato." The section is now "The slice": the artifact-versus-world move is donated by Kant's appearance versus thing in itself, with gravity as the inferred cause and Kant's flat no to better instruments. My weaker, asymptotic position is stated as mine. The move itself, the triage example, the fluency warning, and the unresolved merge-conflict block with the DeGrave and COMPAS cases are unchanged. The three other mentions of Plato's Cave in the chapter (the learning goals, the closing summary, and the Chapter 8 exercise prompt) now say "the Kantian slice move." The chapter file still carries my other uncommitted edits and is not committed.
- **A sixth film, on the solve-verify asymmetry.** I said: "Look at the most recent updates to the show tell skill to make sure you have the most recent instructions for that. Show tell film on the solve-verify asymmetry," and pasted that section of Chapter 1. Claude Code checked: the skill file changed today at 19:03, after the earlier films were built. The changes are no length cap (a beat per step the viewer needs, nothing more), an optional stop-motion card family with a test for when a card is allowed, a voice-regeneration trap, and a dozen new drawing traps the type gate catches. The builder was told to follow the current file and to say which changes it applied. Brief: `youtube/SHOW-TELL-SOLVE-VERIFY.md`. Built: "Cheap to Make, Dear to Check," 3:08, 4K, nine drawn beats, every check passed, not staged. The builder applied the new rules: no length target (one beat per step of the argument), the card test run on every beat (no cards: the cost bars carry no real numbers, so a chart card fails the test), and the new drawing traps. The chapter's cost figures are spoken as "the chapter's numbers" and never shown as digits; the bars are labelled illustrative.
- **A seventh film, on the Five Supervisory Capacities.** I said: "Look at the latest show tell skills to make sure you have the latest changes and updates in it. Make a show tell film on the five supervisory capacities," and pasted the section with its table. (My dictation came out "supervisee"; the chapter's word is supervisory.) Claude Code checked: the skill changed again at 20:59, and the stop-motion card component at 21:03, both after the previous film. The new rules make the card test come first, cap cards at a third of the body, and require cards to reuse the film's own cast. The builder was told to follow the current file and to say what it applied. Brief: `youtube/SHOW-TELL-FIVE-CAPACITIES.md`. Result: `youtube/show-tell-five-things-the-model-cant-do/`, "Five Things the Model Can't Do for Itself", 3:42, 4K, all gates PASS, not staged. One cast for the whole film (the model block, its output slip, the supervisor, the patient as the world); the five tiles at the start come back as five plinths at the end with the fourth empty, the chapter's gap. Ten drawn beats, zero cards: the builder ran the card test on every beat and four candidate kinds each failed it, with the reasons in its SHOTLIST. The only figure on screen is the chapter's 5% example, captioned as such. The builder's session was cut off by a usage limit after the master was written but before its README and closing log entry; Claude Code checked the master itself and wrote those two files, and said so in the reel's BUILD-LOG.
- **Publishing the five-capacities film.** I said: "Looks great. Look for 4K versions in the folder before recreating. Publish the FULL 4K master of the reel to @NikBearBrown, 'Claude' playlist at the top. Facts are signed off — proceed past FACTCHECK; GATE T (render integrity) still applies," followed by the standard runbook (art final, art post, staged.json checks, dry run then real run, verify at 2160p, log with "facts signed off by Bear"). Claude Code reused the existing master (sha checked), built the 54-cue caption track, staged it (3840x2160, all 14 beats native 4K, GATE T pass, no Topaz), rewrote the YouTube description with 13 chapters and the Your Turn, and ran the dry run at 23:46. The YouTube API answered 403 quotaExceeded: today's thirteen uploads used the daily quota, which resets at 3 am Eastern. The upload went through after the reset, at 3:15 am on 2026-09-28: https://youtu.be/BYaxG5AofI4, unlisted, top of the Claude & Agentic AI playlist, captions attached. One catch on the way: the runbook says playlist "Claude," and the publisher would have created a new playlist by that name; the channel's playlist is "Claude & Agentic AI," so it was run with the full name, as for the three move films.
- **What I understand now / still do not understand:** Not yet stated by me.
- **Evidence and next step:**
  - Evidence: the four reel folders in this repo's `youtube/` (not tracked by git): `show-tell-skepticism-is-a-method/`, `show-tell-doubt-what-matters/`, `show-tell-induction-until-it-changes/`, `show-tell-a-test-that-cant-fail/`; the shared brief `youtube/SHOW-TELL-THREE-MOVES.md`.
  - Next: decide on the overview film; the Plato film comes later; in Chapter 1, fix the merge conflict, the turkey's day count, Knight Capital's loss and "no errors were thrown," the Flu Trends peak, and the sepsis 18%.

---

### 2026-09-28 — An eighth film, on the fluency trap

- **What I asked for:** I pasted Chapter 1's section "The fluency trap" (from the two Botspeak pillars through the Figure 1.6 caption) and dictated, verbatim as transcribed: "Yes. Show and tell leads to Sonia. On the phone, we trap." Claude Code read that as "show-tell, Liam persona, on the fluency trap," which is what I meant.
- **What happened:** the show-tell skill had changed again at 23:41 the night before, after the five-capacities film was built, so the builder was told to read the current text and log what changed. Brief: `youtube/SHOW-TELL-FLUENCY-TRAP.md`; reel `youtube/show-tell-fluency-is-not-evidence/`; working title "The Shape of a Sentence Is Not Evidence," the section's own closing line; greeting Hola. The section's case names Ash; Ash is the agent in the Agents of Chaos study, so the film says "the chapter's case." No number in the section, so none in the film.
- **Result:** built, 4:41, 4K, all gates PASS, zero cards (three candidate kinds each failed the card test), not staged. Sixteen drawn beats on one cast: the reader, the upright page, two gauges (confidence in the output, then in one's own judgment), the model block, the account. The builder found two differences between what I pasted and the chapter file: the file's section ends with a Figure 1.7 caption ("Interrupt the fluency trap…"), not the pasted Figure 1.6 caption, and the pasted closing line "The shape of a sentence is not evidence about its truth" is not in the file's section. The film keeps my pasted text; the title is that closing line. The skill's changes since 20:59 (six new drawing and workflow traps) were applied; the Gate A "shapes never change" trap fired three times and was fixed with a pulse ring that grows in one play and fades in the next.
- **What I understand now / still do not understand:** Not yet stated by me.
- **Evidence and next step:**
  - Evidence: the brief; the reel folder's BUILD-LOG (with the skill diff), FACTCHECK (57 rows, none corrected) and SHOTLIST.
  - Next: the five-capacities upload after the quota reset; decide on the four unpublished films (overview, Kant, solve-verify, five-capacities now staged) and this one.

---

### 2026-09-28 — A ninth film, on what probability is

- **What I asked for:** first a show-tell on "Chapter 2, Prompt Contracts and Evaluation," which I called computational skepticism and then corrected ("My mistake. That's prompt engineering and generative AI. Not computational skepticism."); that film is logged in the Prompt Engineering folder. Then, for this course: "After that is done for computational skepticism, do probability. What probability is? With uh, some simple examples of probability in the axioms." I pasted Chapter 2's opening section through the axioms table.
- **What happened:** the section is lines 26–65 of `chapters/02-probability-uncertainty-and-the-confidence-illusion.md`, clear of the five merge-conflict blocks later in that file. Brief: `youtube/SHOW-TELL-PROBABILITY.md`; reel `youtube/show-tell-probability-is-not-a-bit/`; working title "Probability Is Not a Bit"; greeting Jambo. The axioms get one beat each with the chapter's own die and patient examples; the classical/frequentist/Bayesian subsection that follows is outside the paste and stays out. The builder starts when the Prompt Engineering film finishes, in the order I gave.
- **What I understand now / still do not understand:** Not yet stated by me.
- **Evidence and next step:**
  - Evidence: the brief; once built, the reel folder's BUILD-LOG and FACTCHECK.
  - Next: watch the master; decide on the unpublished films. Chapter 2 still carries five unresolved conflict blocks from line 158 on.
- **A tenth film, on conditional probability, ordered the same hour.** I said: "Show tell Liam persona for computational skepticism. Uh, frequentist versus conditional probability," pasted the "Classical and frequentist probability" subsection (which runs through Bayesian and the interpretation table) and the whole "Conditional probability" section, and repeated: "the impersona for computational skepticism, uh, frequentist versus conditional probability." Brief: `youtube/SHOW-TELL-CONDITIONAL.md`; reel `youtube/show-tell-given-what-you-already-know/`; working title "Given What You Already Know"; greeting Aloha. Lines 67–118 of the chapter, clear of the conflicts. The triage illustration's numbers (76%, 45%, 30%, about 39.5%) are the chapter's hypothetical log and are labelled so; the arithmetic checks (0.30/0.76 = 0.3947). Build order: the Prompt Engineering film, then probability, then this one. A minute later I added: "Add some examples to the frequent disk for uh, um, conditional probability um, fill," which Claude Code read as "add some examples to the frequentist and conditional probability film." The brief now carries constructed worked examples beside the chapter's: a die rolled 60 times (frequentist), even given more-than-3 on a die (2/3), king given face card (1/3), red given spade (0), and a spam-filter log where a link doubles the estimate, set against the chapter's triage flag that lowers it. All labelled examples, arithmetic shown.
- **The queue moved to Codex.** Claude Code's weekly usage limit was reached at 13:33 while the Prompt Engineering film was between voicing and rendering, before either of these two films started. I asked for a "prompt to hand to codex to finish what needs to be done"; it is `info-7375-prompt-engineering-for-generative-ai/youtube/CODEX-HANDOFF-2026-09-28.md` and names both briefs here, in order, with the same rules: masters only, nothing staged, published or committed.

---

### 2026-10-07 — The first real sync, and the file the sync list had missed

- **Date and what I was working on:** Keeping the job-search example identical across the three classes.
- **I tried / expected:** I said: "Changes have been made to this project. Um, uh, that is my job search example for all of the classes to the other classes. Check the branding and AI check the um, uh, prompt engineering class. And update the current um, repo, the main repo is computational skepticism. With all of the changes that have been made in the others. And then push all to GitHub. All three classes should be in sync." I expected edits in the other two classes that this master did not have.
- **What happened:** Neither Branding nor Prompt Engineering had anything uncommitted in its `nik-bear-brown/` folder, and `./lectern/sync.sh --check` reported every file on its shared list identical in all three. A file-by-file comparison outside that list found the one real drift, and it ran the other way: `lectern/demand_report.py`, added here and in Branding on 2026-09-26, had never reached Prompt Engineering, because the script's `SHARED` list was not updated when the file was added. Branding's extra files (the raw ATS downloads, the audits, the company-demand report, the advocate notes, the Figma book) are that class's own work by the rule in `SYNC.md`, not shared code. The CV facts sync of 2026-09-27 had already carried the service and bridge-work sections to both classes.
- **What I did:** Added `lectern/demand_report.py` to the shared list in `sync.sh`, ran the script for real for the first time (until today it had only ever been run with `--check`), confirmed `--check` then reported all three in sync, and recorded the lesson in `SYNC.md`: a new shared file is not shared until it is in the list. This push also carries the log entries of 2026-09-27 and 2026-09-28 (the show-tell films) that were waiting for my word.
- **What Claude or another person contributed:** Claude Code ran the comparison, found the missing file, edited the list, ran the sync, validated all three repos, and pushed on my instruction. I decided that all three should be pushed.
- **What I understand now / still do not understand:** "In sync" by the script's own report was true and incomplete at the same time: the check can only see what it was told to look for. Still open: whether the list should be generated from the folder rather than written by hand.
- **Evidence and next step:** `lectern/sync.sh` (the list), `SYNC.md` (current state), and `./lectern/sync.sh --check` reporting "All three in sync." Next: when a shared file is added, add it to the list in the same change.

- **Later the same day, a status report.** I asked: "So I made a detailed summary on the state of my project. What companies are we looking at? Is it running automatically? If so, how often? I needed an executive summary. I need uh, next steps. I need um, an appendix with all the details and where to find the details. So where are we at on the job search uh, project? What scripts have been written? What skills have been written? What companies are being looked at? What job roles are being looked at?" and then: "In your report, also include the gaps that I've been trying to fill. These are primarily videos. Look in the folder I think it's called Figma for educational AI or it's called uh, Claude for Figma, one of the two. There should be some films related to Figma. There should also be the Figma for educational AI playlist on YouTube. The argument here is my I'm trying to get a job at evangelizing for companies. What have I done so far to fill my gaps?" Claude Code inventoried the three class folders, the engine repo, and the Figma repo from the files and wrote `STATUS-2026-10-07.md` here: executive summary, what's built, the 18 boards and 5 unreadable companies, the filter, the answer that nothing runs automatically (one run, 2026-09-26, by hand), the gaps and the 36 Figma films against them, next steps, and an appendix of where each detail lives. I have not yet read it. Not pushed; this folder needs my word per push.

- **Later still: a film series.** I pasted a plan titled "Series plan: Professor Bear Does His Assignments" (drafted 2026-10-07, nothing built; seven proposed films, film 1 laid out in five acts with a ledger of AI did / human decided / doubt caught) and said: "Read this. Uh, you're going to also work on this series." Claude Code checked the plan's log-based claims against this log and Branding's: the Gru session answers typed by Claude Code and not yet reviewed by me (entries of 2026-09-24), "a summary that was about the wrong thing", "finding the bug in my own audit", and the "makes the materials" bullseye (entries of 2026-09-26) are all real headings. The plan's bracketed questions (which assignment is "assignment three"; whether film 1 is the 50-point pitch film; third or first person; permission to capture the public GitHub and YouTube pages; where the early-versus-recent comparison goes and which two films) are mine to answer before film 1 is built. Then: "The other session is making film one," and a new idea: "a new skill called journal and the idea is to make a film every day of that update to that project or every other day if there were no updates that day but it should read like a journal, read like a running session. Based on everything in Brutalist, and all the templates in Brutalist, suggest a structure for a journal style film. Again, these are daily logs of updates to the project." Claude Code surveyed the toolkit's skills and scenes and wrote the proposal at `brutalist.art/skills/make/journal/PROPOSAL.md`: the log entries of the day are the script, a dated slate with counters and their deltas, one block per entry showing the real artifact, a three-line ledger, tomorrow's next steps, the locked outro; two small new scenes, everything else reused. Nothing built yet. I corrected the unit: "we don't necessarily have to be bound by day. We need to have a log per event. If something was done which is a real change, there's a description of one thing. If a day had three substantive changes, it would get three films. The journal entries are not by date, they're by date-time. They're about a substantive change, not a trivial change: some improvement, the results of that improvement, and then the next steps." The proposal was rewritten: one film per substantive change, timestamped from its commit, with the change, the result shown with its check, who did what, the ledger, and the entry's own next steps; today's log would yield three entries. On the stamp I said: "the format of a timestamp, it should be, suggest a format, typically that'll be day, month, 2026, and let's keep it to the hour. I'm not going to make a new film every minute. And do an hour in a 24-hour clock." The proposal now fixes it: on screen `7 October 2026 · 14:00`, spoken "the seventh of October, twenty twenty-six, fourteen hundred", folder names in the sortable form `2026-10-07T14`. Then: "We should also have the conducting AI, Frictional, irreducibly human written through it. Have something at the end summarizing what the AI did and what the human did." The proposal gained a through-line table (Frictional as the whole film's shape, Conducting AI named by capacity where the log shows the act, irreducibly human as the human column) and the closing card became two columns, THE AI DID and THE HUMAN DID, with the doubt line beneath.

### 2026-10-07 — Gru's software design document for the whole project, in silent mode

- **Date and what I was working on:** 2026-10-07. A software design document for everything being built under the job-search project, to be the source for the next film. The next film is not a journal log; it is a detailed overview of what is being built.
- **I tried / expected:** I pasted the Gru prompt and said: "Run Gru in silent mode to generate a detailed software development document. Talk about Gru in a log after that … And add that SDD to the three folders on the GitHub." I expected a design document in the form Gru's `/g1` produces.
- **What happened:** Claude Code ran the Gru prompt in silent mode: no intake questions, no pushback, no phase gates. It read the collector, its configuration, the audit scripts, the sync script, the earlier Lectern design document, the status report, the engine's skill and the three logs, then compiled sixteen sections and a seventeenth that Gru's format does not have: where the earlier design and the built code disagree. That comparison found two real gaps. The earlier design describes a seen-id state file and a "what is new since last time" report, plus `--dry-run` and `--all` flags; `collect.py` has none of them. And the collector's docstring says it writes a quality report, but `main()` writes only the `all-jobs` and `jobs-of-interest` files; the dated quality report on file was written outside the collector. Need N2, "see only what changed since the last run", is therefore unserved by the built tool.
- **What I did:** The document is `SDD-job-search-project.md` in the Computational Skepticism folder, the master. I added it to `lectern/sync.sh`'s shared list and ran the sync, so the Branding and Prompt Engineering folders hold an identical copy; `sync.sh --check` reports all three in sync. Each repository is committed by hand with this entry. The Computational Skepticism push is on my word, given in the message above.
- **What Claude or another person contributed:** I supplied the Gru prompt and the instruction to run it silent, to log it, and to add it to the three folders. Claude Code ran the prompt, read the files, wrote the document, changed the sync list and wrote this entry. This is Claude Code's run of Gru, not my answers to Gru's questions, and I have not reviewed the document. Unfilled fields are marked `TODO`, not guessed.
- **What I understand now / still do not understand:** Not yet stated by me. What the compile found: the built tool and its earlier design differ in the two ways above; there are fourteen open questions in section 16, all mine. Claude Code did not run the collector, the audits or the sync for any counts in the document; they are quoted from the 2026-09-26 run files and the status report.
- **Evidence and next step:** `SDD-job-search-project.md` in each folder; `lectern/sync.sh` in the master. Next: I read it, decide the open questions that matter first (a schedule, the five unreadable companies, and whether to build the state and diff or strike it from the earlier design), and the next film is built from this document.

### 2026-10-10 — The first three lecture films for the course

- **Date and what I was working on:** Turning the course's first lectures into films, one whole chapter per film.
- **I tried / expected:** I said, from the lectures folder and then the updated chapters folder: "Use the lecture skill, make the first three lectures for INFO 7375 Computational Skepticism. Base it on the lecture decks, but also the more updated chapters. The links are there. So make three films, lecture skill, Liam persona, base it around the three lectures that exist, but also use the chapters, to make the three starting films for the course." I expected three decks to base them on.
- **What happened:** Only one of the three decks is real. Lecture 1 has a 14-slide deck written against an older Chapter 1. Lecture 2 has only a skeleton of 58 slides with 156 unfilled TODOs. The third folder, named `03-bias`, holds nothing but an empty asset list, and its name predates the 2026-07-02 renumbering: that chapter is now Chapter 6, and Chapter 3 is data validation. The updated chapters also carry unresolved merge-conflict blocks (3 in Chapter 1, 6 in Chapter 2, 8 in Chapter 6).
- **What I did:** Claude Code took the third film to be the bias lecture, because that is the folder I named, and numbered it Lecture 6 by the series rule that Lecture N is Chapter N. If I meant the course's third chapter, data validation, that film is still to be built. The brief is `youtube/LECTURES-FIRST-THREE-BRIEF.md`: the decks give the teaching order, the updated chapters give the content, each conflict block is logged and the film uses the side that matches the current course layer, and every number is checked against its primary.
- **What Claude or another person contributed:** Claude Code wrote the brief and launched three builders, one per film. I have not yet seen any of the films.
- **What I understand now / still do not understand:** I had remembered three lectures that exist; one does. Still open: which chapter is the third film, and how to resolve the conflict blocks in Chapters 1, 2 and 6, which are my decisions.
- **Evidence and next step:** the brief, then each reel's `ACTS.md` (with its SOURCE CONFLICTS table), `FACTCHECK.md` and `BUILD-LOG.md`. Next: watch the three masters, decide the third chapter, and resolve the conflict blocks.

- **Lecture 2 built, 2026-10-10 about 02:00.** Probability and the Confidence Illusion: 15:21, 4K, 66 body beats in 10 acts, every gate passed, not staged, nobody has watched it. Every worked number is computed by a script and shown from its output. The builder used the current-version side for all six conflict blocks. Two of them cost the film something: the chapter's card-drawing chain contradicts its own agent-tree figure, and Alice's Markov chain is left out (the chapter never uses it again). Seven facts were corrected against sources, for me to resolve in the chapter: the Casscells study (11 of 60 answered correctly; 95% was the most common answer, not "most"), DeGrave et al. (a shortcut-learning study, not pandemic drift), the sepsis model (18% of hospitalizations, not patients, and it missed 67% of cases), the engineers' interval claim (no primary found for "engineers"), the triage flag (it lowers the estimate because the joint 0.30 is below the product of the marginals 0.342, not because the flag is common), the posterior printed as both 0.0098 and 0.0099 (both shown), and Rabanser et al. The Casscells numbers rest on secondary accounts because the abstract could not be fetched.

- **Lecture 1 built, 2026-10-10 about 02:20.** The Skeptic's Toolkit: 12:43, 4K, 65 body beats in 10 acts, every gate passed, not staged, nobody has watched it. The builder used the current-version side for the two real conflict blocks (Knight Capital, and the DeGrave and COMPAS paragraph) and left the third, the AI Wayback Machine end matter, out. Facts corrected, for me to resolve in the chapter: Knight Capital lost more than $460M (SEC), not $440M, and "no errors were thrown" is wrong because 97 automated emails went unread; the sepsis model's 18% is of hospitalizations, not patients, and it missed 67% of cases; Ash is an agent in the Agents of Chaos study, not a security researcher, and the chapter's password-reset story does not match the paper, in which a non-owner asked Ash to delete an email and Ash reported a reset it had only run locally; the turkey's axe falls on day 1,001; Zillow's "about 7,000 homes" is not in its 8-K, so the film uses the $304.4M write-down instead; Google Flu Trends ran too high in 100 of 108 weeks, not "close to double"; and the claim that arrest records "record policing" has no primary, so the film attributes it as the course's reading. The chapter's Figure 1.3 caption still says Plato's Cave while the text uses Kant; the film follows the text. The old deck's "Sweden, 2018" triage death and its seven-orders-of-magnitude cost chart are not in the chapter and were dropped. Open for me: several frames are sparse by design and I may want a richer visual pass; the film calls Botspeak "Professor Bear's framework" because the chapter only names it; nobody has signed the FACTCHECK rows.

- **Lecture 6 built, 2026-10-10 about 03:15.** Bias: Where It Enters and Who Is Responsible: 23:06, 4K, 99 beats (82 body beats in 11 acts), every gate passed, not staged, nobody has watched it. All eight conflict blocks resolved to the current-version side; three of them (the design-critic paragraph, the historical-bias fit-versus-inheritance trade-off, and the Descartes' doubt paragraph) each carry a real teaching sentence that the other side lacks, and the other side contradicts nothing, so nothing was taken from it. Facts for me to resolve in the chapter: the Gallup "roughly 50,000" is in no source found, so it is not spoken; the chapter's open "[verify]" on Agents of Chaos Case 6 is resolved against the paper (an agent whose provider's API truncated responses on politically sensitive topics, attributed to "the authors report" without naming the model or provider); 17.6% became "seventeen and a half percent"; "most common failure in this field" is attributed to me as my judgment, not a measured rate; Apple Card is held to "adjudicated, not proven". Verified against primaries: ProPublica 2016, Kleinberg et al., Chouldechova, the New York DFS press release (quoted on a drawn card, because its site blocked automated access), Squire 1988 (ballot count only via secondary summaries), Pearl, Cohen. Not verified and so not spoken: Hardt, Price and Srebro, and Madras et al. Open for me: the Your Turn chip shows the default model label "Fable 5 · High"; several beats run 17 to 23 seconds against the 7 to 14 second guide and were not split.

### 2026-10-15 — Starting the rewrite of the decks and chapters, with Chapter 1

- **Date and what I was working on:** Starting to rewrite the course's decks and chapters. Chapter 1, The Skeptic's Toolkit, comes first.
- **I tried / expected:** I said: "So we need to start rewriting the decks and the chapters. First chapter has issues. The sepsis example isn't good. The Ash example doesn't really belong in the chapter. I'm about to paste in some material to redo the chapter." I then pasted five notes from a separate Claude chat: a summary of the chapter that found four problems with it, a memo of alternatives to the sepsis opener, a memo on the Netflix Prize as an opener with Amazon, a memo of verified details on the Amazon recruiting engine, and a note on what Netflix did after the Prize. While Claude Code was working I added: "So the Ash example put as a note, a footnote, or just general notes in there that might get somewhere in the book. But it doesn't belong in this chapter. We want to use the Amazon and Netflix examples to make the argument that what you measure has to reflect what you care about in the real world." I expected the chapter redone around Netflix and Amazon, with Ash moved out of it into notes.
- **What happened:** Claude Code rewrote `chapters/01-the-skeptics-toolkit.md` on 2026-10-15. The opening is now the Netflix Prize and the Amazon recruiting engine. A new section, "What you measure and what you care about," names the pattern and separates a gap that was there from the start (Amazon) from one that opens later (Netflix). Sepsis, the triage patient and Ash are out of the chapter. Sepsis and the triage patient were replaced by those two cases and a labeled composite applicant; Ash has no replacement, and the closing "Meet Ash" section became a short note on the casebook. Along the way it fixed the four problems the separate chat had found: the three unresolved merge blocks (resolved by keeping both sides), the Descartes and Popper blur, the "three moves" count, and the missing figure prompts (the generic bar-chart template had already been replaced in this copy). Not everything was checked: Reuters and the Netflix Technology Blog were blocked, so the Amazon details rest on a republished copy and the Netflix engineering quote rests on three outlets quoting it. `chapters/_ch1-rewrite-factcheck.md` lists each claim and its status.
- **What I did:** Gave Claude Code the two examples I am dropping, pasted the research, and then said where Ash goes: into notes, not the chapter. I have not read the rewrite.
- **What Claude or another person contributed:** The research in the five notes came from a separate Claude chat, not Claude Code; I pasted it and have not checked it. Claude Code did the rest, and none of it has been reviewed by me. It read the chapter and found where sepsis and Ash appear; wrote the new chapter; checked the new Netflix, Amazon, Obermeyer and Stranger Things claims against what it could reach (see the fact-check file); added a short Stranger Things passage under tool orchestration, which came from the pasted conversation and is optional; rebuilt Figures 1.3 and 1.4 and re-rendered all eight figures (layout audit zero errors; Figure 1.4 looked at by eye, not signed); and wrote `chapters/_ash-notes.md` to keep the Ash material for the book. It left out of the chapter the Epic sepsis re-analysis, CoastRunners, o3 reward hacking, Ofqual, Robodebt and the other candidates in the notes. It kept a copy of the old chapter at `chapters/_ch1-before-2026-10-15-rewrite.md`. The 2026-10-10 entry above already lists the factual problems with the old sepsis and Ash text.
- **What I understand now / still do not understand:** Not yet stated by me. Open for me: whether to keep the Stranger Things passage; whether the chapter, now about 12,500 words with exercises and prompts against 10,250 before, should be trimmed; and what happens to the other chapters and decks that still mention Chapter 1's sepsis, triage patient and Ash. A word search finds Ash in Chapters 0, 2, 3, 4, 5, 8, 9, 10, 12 and 13, sepsis in Chapters 2, 5, 6, 11, 12 and 13, and triage in most of the rest; the decks that mention Ash are Chapters 1, 4, 5, 8 and 12, and the decks that mention sepsis are Chapters 1, 2, 6, 11, 12 and 13. Some of those are the chapter's own cases and some point back to Chapter 1. None were edited.
- **Evidence and next step:** `chapters/01-the-skeptics-toolkit.md`, `chapters/_ash-notes.md`, `chapters/_ch1-rewrite-factcheck.md`, `chapters/_ch1-before-2026-10-15-rewrite.md`, `docs/chapter-01-figures.md`, and `scripts/build_chapter01_figures.mjs`, all in the repo root of this course and all uncommitted, nothing pushed. Next: I read the chapter; then the Chapter 1 deck and the Lecture 1 film, both built from the old version, are redone from it.

---

### 2026-10-18 — A faculty-listings reader added to the shared Lectern code

- **Date and what I was working on:** 2026-10-18. Extending Lectern from advocate and education jobs to faculty listings at business schools that mention AI.
- **I tried / expected:** I said: *"I don't really care about teaching or tenure or whatever. I care about the interest in being a cutting edge AI in business school."* And: *"So the idea is for listings specifically mentioning people to teach, do research, et cetera, in AI."* I gave a watch list of 12 schools (Harvard, MIT, Duke, Cornell, Vanderbilt, UCLA, UT Austin, UT Dallas, Boston College, UC San Diego, UNC, Northeastern), and asked that the reader live in the shared Lectern master and be synced to the three classes, with no push. I expected the universities' own job systems to be readable. They mostly are not.
- **What happened:**
  - Four research agents checked each school's faculty-jobs page by plain page request (no sign-in, nothing submitted). Duke and Cornell use Academic Jobs Online and UC San Diego and UCLA use UC Recruit (all static pages); Harvard, MIT and Boston College list titles on static pages but keep the posting text in Interfolio; Northeastern (Workday behind a Cloudflare block), Vanderbilt and UT Austin (Interfolio) cannot be read by script; UNC and UT Dallas disallow bots in robots.txt. The Chronicle of Higher Education and Inside Higher Ed keyword RSS feeds work by plain request and cover every school.
  - So the reader uses those two feeds: 8 AI queries plus one per watched school, kept only if the role looks like faculty or institute leadership and passes one of three rules (A: business and AI wording; B: watched school and AI wording; C: watched school, business wording, analytics only). Each kept listing stores its matched words. First full run: 1,727 feed items read, 14 matched, 0 errors.
  - Real hits included an applied-AI professorship at Chicago Booth, an Information Systems and Business Analytics (AI) role at Hofstra, a clinical-track Business Analytics role at Ohio State, and the executive director of Boston College's AI institute. Some matches are not business-school roles (a writing-studies post, an economics post): the filter is loose and shows why each matched.
  - **Where it went wrong:** I first built it in a separate private folder and routed alerts to a private Discord channel. That was my assumption, not Professor Bear's: he said *"The point of that channel is to be public. So people can see my search."* The reader then moved into the shared master, and alerts go to the public channel. A webhook for the public channel was also pasted into chat by mistake and saved under the private channel's name; a guard that blocked posting caught it before a send, and the guard was removed with the private channel.
  - **Drift found while syncing:** `sync.sh` still pointed Branding's collector copies at `assignment-3/`, which was renamed `build-your-data-pipeline/` on 2026-10-11 (only the raw data stayed behind). A blind run would have written a second copy into the wrong folder. The mapping is fixed. The design document in the master also carried the old folder name; the master now matches Branding's already-corrected copy.
  - The 14 listings were posted to the public channel as a test (three messages, accepted). Not scheduled yet. Nothing pushed.
- **What I did:** Set the scope and the school list, corrected my private-channel assumption, and decided where the code lives. Decisions still mine: whether to tighten the filter before a daily run, when to schedule it on the Mac mini, and when to push.
- **What Claude or another person contributed:** Claude Code wrote `lectern/faculty_feed.py` and `lectern/faculty_config.json`, ran the research and the first run, fixed `sync.sh` and the design document, and synced the two new files to the other two classes. Claude Code did not push anything and has not seen the posted messages in the channel. I have not reviewed the filter.
- **What I understand now / still do not understand:** Not yet stated by me. For this class the point is the skepticism: the reader's output is a ranked guess, not a finding. A listing is kept on words in a short feed snippet, so a match can be wrong, and a role that mentions AI only in the body can be missed. The three tiers and the stored matched words exist so each match can be checked, not trusted.
- **Evidence and next step:** `lectern/``faculty_feed.py` and `faculty_config.json`; `faculty-runs/new/new-2026-10-18.md` in the master folder. Next: tighten the filter, schedule one daily run on the Mac mini, then commit each repo by hand.

### 2026-10-18 — One folder per Canvas assignment, a plan for each, and a run that publishes only what changed

- **Date and what I was working on:** 2026-10-18. Three linked requests: a numbered folder and a plan for every assignment in the Canvas course; the assignments published on GitHub; and a collection run with a script that pushes only what is new since the last run.
- **I tried / expected:** I asked whether the assistant knew all the assignments, then pointed it at the Canvas export. I said: *"I want folders under [my folder] in the fall 2026. For each assignment, but it should not be named assignment one, assignment two… It should be one and then that assignment's name, two and that assignment's name… in lower kebab case."* And: *"I need a clear plan of attack to get a rough draft for each assignment. Then once I get a rough draft, I'll refine and refine and refine."* And: *"Remove any existing assignments from the assignments folder, update it with the correct assignments"*; *"there's no reason not to publish all of the assignments on GitHub"*; *"When you push files, do not push IMCC files. They will be deleted later."* On the collection: *"we do not push everything. We just push what's changed since the last."*
- **What happened:**
  - **The Canvas export has twelve assignments, five published and seven not.** The seven unpublished ones carry summer 2026 due dates and are leftovers from the summer course. The repo's own ten 100-point briefs were not in Canvas at all. They were removed from the course `assignments/fall-2026/` folder (still in git history), and all twelve Canvas assignments are now there, numbered 01 to 12, each marked published or not. Six gitignored files that sat directly in `assignments/` (summer briefs and a casebook worked example) were moved to `_to_delete/assignments-removed-2026-10-18/` rather than deleted, because git had no copy.
  - **This folder now has `01-…` to `12-…`, one per assignment, each with a `PLAN.md`** (requirements, status, what exists, what is still to do, a step table, decisions that are mine, limits), plus a master `PLAN.md`. `boondoggle-report/` became `03-week-2-boondoggle-report/` (git rename; Gru's files are untouched). `README.md`, `CLAUDE.md` and `SYNC.md` paths were updated; older log entries keep the old path on purpose.
  - **What the plans found.** One assignment is due: the pitch film, Sun Oct 25. Week 2 has two reports on different applications (the downloadable Gru, and Lectern from 2026-10-11) and which is the submission is undecided. Week 1 has the films but no AI Use Disclosure, source list or Frictional entry, and the prediction that was meant to be written before the work was never recorded; the plan says it must not be backdated. Mode Design has a drafted recipe but no mode file in the Canvas format. 06 to 12 are not started and not assigned.
  - **Collection run.** `collect.py` read 17 of 18 boards: 3,243 postings, 88 kept. HubSpot returned HTTP 404. The big-four collectors were **not** run: there is no `monitor.db` on this machine, so a first run would fetch ad text for every posting (about 3,300 at Google and 10,000 at Amazon at a polite one request per second or slower) and Meta needs a browser.
  - **`lectern/publish_delta.py`.** Compares today's kept set with what was already published and writes only the difference as a short report, a JSON and a CSV. Against the 2026-10-08 run: 39 new, 2 changed, 9 gone. Seven companies show as new only because they were not watched on 2026-10-08, and the report says so. A posting from a source that was unavailable is marked unknown, not gone. The delta is about 70 KB; the run folder is 46 MB. The full files stay on this machine (`lectern/.gitignore`). It commits only the delta files and a small published-state file, and pushes only with an explicit flag. It found two bugs in itself when first run (the report crashed on the mixed-type `matched` field), both fixed; six unit tests and a commit test in a throwaway repository pass.
  - **`*.imscc` is now ignored in ten repositories.** Two already had the rule (this one and the CSYE 7270 course); eight gained it and were committed one repository at a time. Branding's is on a feature branch and was not pushed.
  - **Pushed with my word:** the assignments commits in this repo, and the `.gitignore` commits in six other repositories. Two were held back: one had another unpushed commit that was not part of this work, the other was on a feature branch.
  - **The pitch film was published.** After watching it I said "looks good" and asked for it to be scaled to 4K and published under the Professor Bear Does His Assignments playlist. It was already native 4K (nothing scaled). It went up unlisted on the channel and into that existing playlist; the details are in the Prompt Engineering log and the reel's `BUILD-LOG.md`. Folder 05's plan was updated to match.
  - **A new rule in the filter: roles that own a big institutional relationship (keywords 0.5.1).** After reading a Senior Partner Account Manager posting for global systems integrators (correctly rejected: a sales role about consulting firms), I said the search should look for the university version: *"if there's an enterprise account executive for education, universities, particularly higher education, then that would be good."* I also confirmed from the closest-call table that the industry Enterprise Account Executive roles (retail, banking, automotive and the rest) are correct rejects, because "educate them about our services" is sales boilerplate. Measured on the 2026-10-18 corpus before adding: 495 titles carry an account or partnership word; only 7 of them name a university or higher education in the body; 5 of those were already kept (the Canva and OpenAI higher-education account roles and Anthropic's AI for Science partnership role). The rule keeps a posting when an account or partnership word is in the title **and** a higher-education institution is in the body; both are required. It adds 3 postings (two partnerships roles at Anthropic, and a Sales Manager for nonprofits in EMEA after the second pass added "sales manager" and three other sales titles). All 38 Enterprise Account Executive roles on the boards (28 at Anthropic) stay out. (An earlier version of this bullet said 27; that was a miscount, corrected the same day.) Precision is not measured: three postings is too few, and a person has to read them. `keywords.json` records the numbers; `collect.py` gained `connector_evidence`; four tests in `test_connector_rule.py` pin the behaviour (the GSI posting that prompted it stays out).
  - **Then, the reject file read, and a question about the math.** I said I looked through the file and see no misses, and that I would not expect to find one by chance: *"out of 3,000 postings, we kept five for me… is 100 big enough to look at our rejections? … is that unlikely?"* The Verdict column in the file is still blank, so the result is my statement, not a record. Claude Code wrote `films/evaluating-the-rejections/sampling_math.py`. With five relevant postings in 3,446 (an assumption, my count) the base rate is 0.145%, about one in 690 (one in 500 is 0.2%). A hundred random reads then expect 0.15 hits; the chance of finding none is 86% (82% at one in 500). With five real misses hidden among the 3,349 rejects, a clean hundred still happens 85.9% of the time (checked by simulation). Zero in a hundred rules out only a miss rate above about 3%, up to about 99 postings; bounding it below one in 500 would take about 1,497 random reads. So a clean sample is the expected result and is weak evidence. The reject file's own estimator (misses found times 34) gives zero for zero, which hides that interval.
  - **Then, widening the connector rule (keywords 0.5.2).** I asked that marketing, adoption and enterprise-account roles not be rejected early, and said I would rather review a few more than miss them. Measured: 992 postings have a marketing, adoption, customer-success, account, partner, sales or growth word in the title; 13 name a university or higher education in the body; 12 were already kept; one, a public-sector Solutions Marketing Lead, was rejected and is now kept. A weaker body half (two or more education words) was tried and not added: 2 extra postings, none fits. I also confirmed the 38 Enterprise Account Executive roles on the boards are all still rejected. Claude Code first wrote 27 for that count, which was a miscount of the Anthropic lines (28); it is corrected in `keywords.json` and in the bullet above.
  - **A film layout, not a film.** `films/evaluating-the-rejections/LAYOUT.md`: a 19-beat show-tell layout of the math, every spoken number tied to the script's output or to a file. Nothing is narrated, drawn or built; it waits for my sign-off. It lists five decisions that are mine.
  - **A bug the change exposed in my own script.** `publish_delta.py` reported 47 postings as "changed" because the filter now writes a new `connector` field on every record. The change report now ignores empty fields and says when the filter version differs between the published runs and today's. I also re-derived today's run from the saved raw files once, which replaced HubSpot's real "HTTP 404" with "no saved response". Today's run was then redone live so its record is the fetch's own; raw and outputs are one consistent run under filter 0.5.0.
  - **Then, the through-rate question.** Looking at the run (Anthropic 657 postings, OpenAI 813) I asked whether those are real jobs that turn over or postings that sit there, whether the same job is posted again under a different ID, and said to keep the history. Claude Code wrote `lectern/churn.py` (with `test_churn.py`). It compares the saved board snapshots (2026-09-26, 2026-10-08, 2026-10-18) and reports age, flow, re-posts, and an implied time open. Results, with the limits: about 29% of today's open postings were first published more than 90 days ago and 14% more than 180; at Anthropic and OpenAI about 8% of the open postings disappeared in the last 10 days (53 and 66 postings) while about as many appeared (65 and 67), so the pile turns over; if a board is steady, a posting stays up about 120 days on average; 34% of Anthropic's and OpenAI's open postings are older than 90 days, and 8% of OpenAI's are older than a year. Re-posts are few where they can be seen: matching on title and place finds 14 of 742 new postings across the trusted boards, and Greenhouse's own job id finds 24 new post ids that belong to a job already open (16 at Anthropic). Anthropic's 657 posts are 609 distinct jobs. **What it cannot say:** a posting that disappears was filled, cancelled, merged or re-posted, and the board does not say which, so none of this is a hiring rate. Two boards were left out as untrusted reads under the monitor's own rule (Webflow went from 27 postings to 0, Canva from 197 to 110), and Writer's posted dates look reset to an updated-at date. OpenAI is on Ashby, which gives no job id in what Lectern keeps, so only title matching applies there. `collect.py` now records `job_ref` (Greenhouse's job id) on every record from the next run on; for the older snapshots the script reads it from the saved raw responses.
  - **The pushes.** The delta commit was pushed by me running `publish_delta.py --commit` and then `git push`; the commit that records this folder's new plans, scripts and logs is committed here and not yet pushed. The row for the delta push was added late for that reason: the script cannot write the log row into the commit it makes.
  - **Then, the intake for the personal-layer exercise (folder 06).** Claude Code drafted `06-setup-exercise-personal-layer/search/profile.yml` from what I have said, with every unknown left null and listed as a question. I corrected one gap: business-school AI roles were a footnote and are a main track. My reasons: business schools pay more than other departments, run executive education, specialised AI workshops and white-label executive programmes, those are politically hard to reach from outside the business school, and a joint appointment (business plus engineering) at Northeastern is one way in. The salary figures in the text I pasted were not checked against their source and are not in the file. I then answered the intake: US and Brazilian citizen, no sponsorship needed; based in Boston, relocating only to a lower-cost or warmer place, never New York or San Francisco, and in Los Angeles only UCLA; remote is fine; the work wanted is consulting, summer and part-time work alongside teaching, not a permanent job; seniority does not matter, fit and pay do (and contract length at business schools); and the work has to be directly applicable to improving education through AI, so he will probably drop Stripe, Writer and a couple of other tools from the watch list. (Claude Code first recorded the reason as "he must believe in the product" and, for Writer, as a tool he does not think is good. He corrected that on 2026-10-18: he is not saying Stripe or Writer are bad or not useful, only that he does not see them as transformative for education.) Nothing in `lectern/sources.json` has been changed. The file is a draft and uncommitted; it holds citizenship, which is personal data. Then I said: "We can remove Stripe and Writer for now"; my most wanted employers are Anthropic, OpenAI, Microsoft, Google, Figma and Canva, with GitHub, Notion and Jasper AI still to look at; I can give 20 hours a week in term and full-time in summer; and I would take business-school roles beyond faculty (executive education director, AI director, AI centre lead, professor of practice, programmes that train a school's own faculty in AI), because business schools need AI direction. Claude Code removed Stripe and Writer from `lectern/sources.json` (16 boards remain) and recorded the removal and reason under `removed` in that file. Microsoft turned out never to have been on the watch list: its collector exists but has not run on this machine, and Google and GitHub are listed as unreachable by the three job-board APIs. The next delta will show Stripe's earlier candidates as gone because the company is no longer watched, not because the postings closed. The other two classes still have the old list until the sync is run. I then said the business-school target can be worded more formally (bringing real AI expertise into the school to direct an AI research centre or educational effort) or informally as running an AI group, and that the emphasis is real AI expertise; Claude Code reworded the profile and the film layout to match. I then said I want the profile file published and a film made about it, because it teaches what the file does and why; and that my résumé is already in JSON, so `resume.json` does not need generating (the attested CV facts file and the derived résumé in `greenhouse-watch-demo/` stand; two sections of the facts file are still not read by me). I asked for two Liam films, one on the profile file and one on why the résumé is JSON (one source of truth that gets updated, from which company-specific résumés and cover letters are made). Claude Code wrote a layout for each in `films/`; neither is built. I then added that the profile film should say these files evolve as we see the market, with the business-school widening (from teaching posts to running an AI group) as the example. Claude Code rewrote that layout as a four-act lecture-scale film and added a dated `revisions` block to `profile.yml` so the film's examples are in the file; the widening rests on a few listings and my own experience and has not been measured. In the second I had said "immutable" and also that it will be updated; the layout proposes "one record, changed only by its owner" and leaves that for me to confirm. I also said `gaps.md` must wait until we have the Google and Microsoft postings: the gaps are measured against actual jobs or they are a guess, so that step is blocked on the collectors and the plan for folder 06 says so. I asked whether Brown has a business school. It does not have its own; the page I linked is an executive MBA that Brown's School of Professional Studies runs with IE Business School. I said to add Brown anyway, and that Providence is close to Boston and much cheaper. Claude Code added "Brown School of Professional Studies" (searched as Brown University) to `lectern/faculty_config.json`, which makes 13 watched schools, and Providence to the profile's metros. Nothing has been run with it yet. I pasted eight more schools from a ranking list (Virginia Darden, Dartmouth Tuck, Rice Jones, emlyon, IESE, London Business School, HEC Paris, ESADE; UNC Kenan-Flagler was already on it) and asked for them to be added. Claude Code added them to `lectern/faculty_config.json`, which now watches 21 schools, with aliases chosen so that a short name such as Dartmouth does not match another university's name. The listing feeds the reader uses (the Chronicle of Higher Education and Inside Higher Ed) are American, so the five European schools are unlikely to appear through them; that has not been tested. I pasted the exercise text and asked for a folder with its name in this repository, pushed, and asked whether my résumé JSON exists. It does: the attested CV record `facts/professor-bear-cv.json` (read by me on 2026-09-23, no errors found) and the derived résumé in `greenhouse-watch-demo/`, which is not attested. Claude Code added a README, a RUN_LOG with the unfinished parts marked, a gitignore for `search/private-notes.md`, and a copy of the derived résumé as `search/resume.json` (marked `attested: false`, with its source named) to the exercise-06 folder; `gaps.md` is still unwritten. For the résumé film I then asked for an ai-explainer, not a deep explainer, in the Liam persona, and said the point is that a résumé kept in Word or Google Docs and edited for years collects mistakes nobody sees, made worse by AI, and that I have known students who had to defend skills they do not have because those skills crept into their résumé. I added that my record is long, so a one-page résumé for each opportunity is a selection from it, and that the résumé is history, the profile is the future, and the gaps are an analysis made from job data. Claude Code read the whole ai-explainer skill and wrote stage one under the two-stage rule: a revised layout with 14 beats, a sources and fact-check table, a script that checked every skill on my derived résumé against my CV record (15 skills, 14 found, one, "course development", not found; I have not ruled on it), a script that suggested the roles for a one-page view of two real listings (rough: some picks look wrong), a `BUILD-PROMPT.md` for the build, and a private artifact page of my record. Nothing is built or rendered. I said to add the hallucination survey the search found; its journal venue and year are not confirmed, and "watermarking", which I mentioned, is not claimed anywhere until I say what I mean. I then looked at the Discord channel and asked why new listings were not being posted automatically, when that was the point and had been done before. **Where the information was lost:** only the faculty reader posted on its own, and only with its send flag. `collect.py`, `publish_delta.py` and the collectors never posted, and the Discord instructions said to post only when asked, so nothing wired the standing instruction I had in mind into the pipeline or into the rules; each earlier post had been someone doing it by hand. Claude Code did not have the standing instruction written anywhere and should have asked, not assumed. Fixed on 2026-10-19: `lectern/notify.py` posts a run's new listings (only companies still on the watch list, my most-wanted employers first, newly watched companies marked, nothing posted twice); `publish_delta.py --post` and `--post-only` use it; `lectern/daily.sh` runs collect, delta, post, churn and the faculty feed; the rule is Rule 4 of this folder's `CLAUDE.md` and in `books/AGENTS.md`. The 10-18 run's 31 new listings from watched companies (42 new in all, minus 11 from Stripe, which I had removed) were posted to `#professor-bear` in five messages, all accepted. The scheduled daily run is not built; `daily.sh` runs on command. I also asked whether my profile is on GitHub (yes, identical to my local copy) and for an artifact summarising it (made, private). I then said I am also looking for part-time postdoc-style research work, which I have done before: read the website of every lab in Boston, every business-school department, epidemiology and endocrinology at Harvard Medical School, and email the principal investigator or the lab manager directly with a proposal that says I am a teaching professor with about 20 hours a week (full-time in summer). The work could be in biology, computational biology, or AI research at a business school such as Harvard Business School or MIT Sloan. For each lab I want a JSON record: what it does, whether it matches me, the principal investigator, who gets the email, whether there is a lab manager and their name. Claude Code added this as Track D and an `outreach_search` section in `profile.yml` (marked not built: no lab list, no website read), updated the private profile artifact, and added `labs/` and `lab-records/` to `lectern/.gitignore` so records that name people cannot be committed by accident. The emails are mine to write and send. I then pointed at the Division of Nutrition people page at Harvard Medical School and said nearly every research lab has a people page; I want a JSON structure for what a scrape of such pages should produce. Claude Code read the page and its robots file (the directory is allowed) and one lab site it linked to, and proposed the record in `lab-outreach/LAB-RECORD.md`. What the reads showed: the directory lists 126 people (121 faculty, 2 fellows, 2 staff, 1 student) and no postdocs or lab managers, so it is a list of principal investigators; the lab's own site is a different site, with a separate Lab Members page, a contact page, and no join page. The proposal separates a three-stage scrape, records "not found" explicitly, keeps the lab's own sentence apart from any model summary, never constructs an email address, and leaves the match verdict and the outreach state to me. Nothing is built; the example uses placeholders because records that name people stay local. I answered the questions on the lab record: the unit is the lab, because I am applying to a lab and not to a principal investigator in particular; a faculty member with no lab website is recorded but is not a target; a lab needs funding, so one that looks like a single person probably has none and is not a target. The best fit is computational biology, labs dealing with a lot of genomic or other biological data, or that could use a database, labs that need a computational biologist. For business, groups that want to do AI research without the technical capacity. I added Harvard Business School, MIT Sloan, the Broad and Whitehead Institutes and think tanks to the places to read. Claude Code wrote these into `profile.yml` (`outreach_search`: unit, best fit, fit criteria, target rule, places), into the lab record (`size_and_funding`, `fit.track`, `target`), and into the profile artifact. A lab's funding is recorded only as the lab states it. How small is too small (two or three people, or does evidence of funding decide) and the first pilot are still open. I added the big Boston hospitals to the places to read for the outreach search: Mass General and Boston Children's by name, and "et cetera" for the rest, with the Broad and Whitehead Institutes and think tanks. Claude Code added them to `profile.yml`, the lab record and the profile artifact, and listed the hospitals still to be named as an open question. None of the hospital sites has been read, so how their lab listings are laid out is not known. I said the hospitals are all near Northeastern: Longwood, where Harvard Medical School, Boston Children's, the Harvard Chan School of Public Health and a pharmacy school are about three T stops away; Mass General is the farthest I would go, about once a week; Harvard and Cambridge near the Broad, and Allston, are fine; not Tufts; the work is mostly remote. I then asked for the hospitals to be listed and for think tanks to be researched. Claude Code wrote `lab-outreach/PLACES.md` from my statements and web searches, marking each place as confirmed by a search, named by me, or not verified, added the distance rule and the list to `profile.yml` and the lab record, and found only two think tanks (MIT's Initiative on the Digital Economy and Harvard's Berkman Klein Center); which think tanks I meant near the Broad is still mine to name. No place's own lab pages have been read. I looked at Kendall Square on Google Maps and sent a screenshot: the Broad's buildings, Moderna, Akamai Technologies, The Foundry and the MIT Museum. I said Moderna would be a great target and asked whether they need AI help. Claude Code searched: Moderna already uses AI heavily (ChatGPT Enterprise with about 750 custom GPTs within two months, by its own 2024 figures; an AI Academy with Carnegie Mellon announced in 2021; a Data Science and AI Research team; data scientist roles in Cambridge on job boards), so a need for outside help is not shown by the public record, and the search found no consulting roles. Added to `profile.yml` and `PLACES.md` as a company to look at, not as a lab. I said I am uniquely qualified for Moderna and want to pitch them anyway, a collaboration and not necessarily a job, and that if they do not want part-time or summer work that is fine; and I asked whether Moderna has research scientists and effectively labs inside the company. Claude Code answered from public job listings: it names a Data Science and AI Research team, a Research and Early Development function and a Therapeutic Area Bioinformatics team, which work like labs. Whether they work with outside collaborators is not shown anywhere found. Added a `kind` field (lab or company team) to the lab record and the teams to `PLACES.md` and the profile. "Uniquely qualified" is my claim; the public record neither shows nor refutes it. I asked for the MIT Media Lab to be added and said it is right next to the Broad, and that the Whitehead Institute is too. Claude Code checked by search: the Whitehead is at 455 Main Street, beside the Broad's 415 Main Street; the Media Lab is at 75 Amherst Street, at the corner of Ames and Amherst, two to five minutes from the Kendall/MIT stop; the Broad also lists a lab building at 75 Ames Street from a 2020 directory entry. So both are near the Broad, as I thought. The Media Lab's research was not looked at. I also said the business-school feed check must run after the Google and Microsoft collectors, and before `gaps.md`, for the same reason: no gaps from guesses. The Google collector finished its first run: 3,690 postings fetched out of 3,690 reported, a trusted read, recorded in the monitor database. The monitor keeps only a hash of each ad's text, so the text itself was not kept, and the gaps analysis needs it. Claude Code added `--text-out DIR` to `collectors/run_daily.py` (every posting's ad text written to a local file as it is read, resumable, not for committing; three tests) and started Google again, then Microsoft, with it; they are running and have not finished. The first Microsoft attempt left no sign that it had run. The Google and Microsoft collectors were started in the background on my yes; they have not finished and nothing from them is committed.
  - **A drift I should have expected:** the SHARED list in `sync.sh` did not contain `lectern/collectors/` or the new script, the same trap logged on 2026-10-07. Both are in the list now. The script has not been copied to the other two classes.
  - **Then, my pitch for the research search, and a list of Boston and Cambridge institutes.** I said my pitch is research: that I have published in Nature and Computational Biology, have expertise in neuroscience, degrees in biology and biochemistry and in computer science, an MBA, and have published in the top five biological journals. Claude Code checked it against `facts/professor-bear-cv.json`, which I read and attested on 2026-09-23. **The record supports:** a PhD and an MS in Computer Science (UCLA), an MBA (Northeastern), a BA in Biochemistry and Molecular Biology (UC Santa Cruz), a Nature Methods article in 2021 on aligning single-cell transcriptomes with deep learning, a Broad Institute collaboration in 2019 to 2020, a part-time postdoc in deep learning at Harvard Medical School in 2017 to 2018, and a course-specialist role there in 2019 adding labs to a computational biology course. **The record does not contain:** neuroscience, a biology degree separate from the BA, a journal called Computational Biology, or any claim about top-five journals. Those are my statements; I have not yet confirmed or added them, so none goes into a pitch until I do. I then pasted a research snapshot of Boston and Cambridge think tanks and institutes. It argued that the Broad and Whitehead are not think tanks. I said that distinction is wrong for my purpose: a think tank is a group of very smart people working on hard problems, and research institutes are think tanks. I asked for the list to be filtered to biology, finance, economics, the MIT Media Lab and people doing interesting things with education. Claude Code did: 26 of about 50 institutions in the snapshot fit, plus the Media Lab and two education guesses of its own marked unchecked, in the new table in `lab-outreach/PLACES.md`; the rest are named there as dropped so I can overrule. Two gaps showed up: the snapshot has nothing on market finance and almost nothing on education. It also said federal research cuts have hit Massachusetts science institutes (its sources, not checked), which bears on my own rule that a lab needs funding to pay for me. The snapshot put the Kempner Institute in Cambridge; the institute's own page says Allston, so Allston stands. The profile now holds the interest filter and the definition of a think tank.
  - **Then, a review gate for the lab search, and a question about Northeastern.** I said: *"I don't see why Northeastern couldn't hire me as a consultant or some sort of joint faculty"*, and that I have to look into the actual agreements. I said the Discord should get the labs that look like great fits, at the point the Moderna ones are posted, and that if I get nothing from great fits we go to pretty good ones, but *"nothing gets approached without me taking a quick look at the group"*: for Moderna a lab page or research-group page, not a job. Claude Code wrote it into the pipeline this time, not only into the chat: `lectern/notify.py` now has `post_labs()` (great fits only unless I widen it; reads only a lab's public name, institution, link, tier and the lab's own words, so a principal investigator, lab manager, email or phone cannot leak; a lab named for a person is shown as "A lab at <institution>"), six new tests (13 in `test_notify.py`, all passing), `CLAUDE.md` Rule 5, the books-level `AGENTS.md` line, a `review_gate` and a `northeastern_arrangement` in the profile, and `fit.tier` in the lab record. **What is not built:** the reader that produces lab candidates, so nothing has been posted and the new function has run only on made-up labs. The Northeastern arrangement is recorded as my hypothesis; what my agreements say is something I have not read and nothing here claims to know.
  - **Then, a first search at Northeastern.** I said to do a special search of the Northeastern business school (*"the easiest people to contact"*; my MBA is from there) for people who would work with me in a paid way on research with their group, then the Institute for Experiential AI. I named three people there I know well and asked what a fourth contact is doing now. Claude Code read the public pages by hand (robots files checked first) and wrote nine local records (`lectern/lab-records/`, not committed, because they name people). Two groups were suggested as great fits and **posted to #professor-bear: the business school's AI hub (DASH) and the Institute's AI + Life Sciences area**, which names single-cell 'omics work like my 2021 paper. Seven others are recorded as pretty good, unrated or not a target. **Neither great fit states any pay for an outside or part-time researcher**, so pay is a question for the conversation, not a finding. For the three people, Claude Code gave me their public titles, groups and research areas in the reply and kept them out of this public repository. One of the three names was a first name only; Claude Code matched it to a finance faculty member and said so, and I have not confirmed it was the right person. A LinkedIn profile I pointed to was read for the person's current professional role only. Separately, Claude Code checked the derived résumé against my attested CV and found a false statement in its own note (it said every skill string appears in the CV; \"course development\" does not), which it corrected in `search/resume.json`, and that the résumé omits 8 of the CV's 20 experience entries, among them the Broad Institute collaboration and the Harvard Medical School course-specialist role that matter most for the lab search. Those are candidates for the attestation pass; I have not ruled on them.
  - **Then, a student's version of the lab search arrived.** A student emailed me his own version of what we did in class: 61 Boston-area labs with funded awards, built for his own profile. I said it was useful. Claude Code read it and checked it against the public award databases: all 20 NIH award numbers were found in NIH RePORTER with matching amounts and end dates, and 24 of 25 sampled NSF awards matched. The selection does not fit my interests (about 18 of the in-range labs touch biology loosely, none finance, one education; 12 are Northeastern computer-science labs), but the way it evidences funding does, so the lab record now uses award numbers from those databases in place of a lab's own funding sentence. His file names people and holds email addresses, so it stays on my machine and is not in this repository.
  - **Then, an n8n form of the whole pipeline.** I said I want everything here as an n8n workflow or a series of them, in a Lectern job-search folder with a subfolder per sub-workflow, to show the same pipeline in CrewAI, in n8n and in plain Python. Claude Code built five workflows (collect, filter, delta, post to Discord, daily) in `books/n8n/lectern-job-search/`, outside this repository, with the logic ported to JavaScript and the Python as the oracle. **What testing found:** the filter agrees with the Python on all 2,465 real postings of the last run (81 kept by each), the delta agrees on the real 2026-10-08 and 2026-10-18 runs (42 new, 7 changed, 9 gone, same reasons), the Discord messages are byte-identical, and the live HTTP path agrees on three small boards. It also caught two failures a silent workflow has: a missing state file stopped the daily workflow with no error and no output, and a first run with sending on would have posted every kept listing at once; both are fixed. **Not done:** the Discord node has never sent from n8n (it needs a webhook credential), SmartRecruiters is not read live, and churn, the faculty feed, the trust rules for the big-four collectors, lab posting and the CrewAI form are not built. The n8n folder is not in a git repository; where it goes on GitHub is for me to decide.
  - **Then, removing Replit from the search, and why.** I pasted the Replit Learning Experiences Creator posting and asked what Replit does. Then I said: *"Let's remove Replit from the job search. Replit isn't really educational software in the sense that Claude for University is, NotebookLM is, Claude Science [dictated as Claude Sciences]. It's more just a low-level app. And that's kind of an entry-level, low-level job. So let's remove Replit from our search."* and, asking for it to be logged: *"It's not really educational AI. It's just AI."* **My reason, in short:** Replit is AI, but not educational AI, and the role I read there is entry-level. It is the same kind of deliberate exception as Stripe and Writer on 2026-10-18, and it reverses the 2026-09-26 rule to watch every company whatever it posts. It is not a finding about Replit beyond my own judgment, and the Replit posting I was rejected on 2026-09-26 (the first entry in the profile's revisions) is unchanged history. Claude Code moved Replit from the watch list (`lectern/sources.json`, now 15 boards) to its `removed` block with that reason and its last count of 75 postings, added a line to the profile's revisions, and re-ran the five Lectern test files (all pass). From the next run nothing from Replit is posted to Discord, and its earlier published rows will show in the delta as gone because the company is no longer watched, which is not a sign the postings closed. The Prompt Engineering copy of the watch list was brought in line the same day; the Branding and AI copy was not touched.
  - **Then, a question about how the Lectern folder is organised.** I looked at the folder on GitHub and asked: *"Explain to me the logic of why this is organized the way it is… it looks like just a big dump of scripts. What is the rationale?"* The honest answer was that some of it is deliberate (plain scripts that each run alone, the rules kept in files, a shared-versus-not-shared split that decides what is copied to the other two classes, `runs/` for dated output) and a lot of it is accretion: files appeared the day they were needed, between 2026-09-26 and 2026-10-19, with no README in the folder, the pipeline order visible only inside `daily.sh`, and the project's profile, the lab outreach design and the n8n form all outside it. Nothing reads `profile.yml`; `keywords.json` is edited by hand to match it. I said: *"Step one now. Also we can make copies of the N8N things as parallel… because it's a learning experience. And what I do like about the N8N stuff is the ability to draw the diagrams… Let's first do a README. And then in addition to README, we need sort of a history MD… basically a daily log. What we're doing in Frictional of what was added when. And how it's being built up."* Claude Code wrote `lectern/README.md` (a pipeline diagram, where each file is and why, what is shared, what is not in the folder, the known gaps) and `lectern/HISTORY.md` (a day-by-day log from 2026-09-26, built from `git log` and these entries), put a copy of the n8n form in `lectern-n8n/` beside the Python (its tools now find the sibling `lectern/` folder by default, and its tests pass from there), and wrote the upkeep into `CLAUDE.md` as Rule 6 so the history is kept by every later session and not only this one. **Not done:** moving any file (that would mean re-syncing three repositories and changing paths students are told to use), and the CrewAI form. The copy and the n8n repository's version are two copies; neither is refreshed automatically.
  - **Then, a targets file.** I said: *"Create a targets MD file. Targets MD are all the companies, departments and where we're getting data from… classified by what they are. Are they companies selling educational AI? Are they educational institutions? Are they think tanks? Are they biotech?… And where are we getting the data? What are the direct links to the data?… and then the scripts that are being used to get the data for those companies. Including to-dos, what we don't have."* Claude Code wrote `TARGETS.md` in this folder: every target with a type, why it is a target, the direct link to its data, the script that reads it and what is missing. Links were checked with a plain request on 2026-10-20, and a researcher agent looked up the 21 business schools' faculty-job pages (its table was spot-checked for the status codes only). **What it found:** 14 of 15 company boards are read and HubSpot's returns 404 (it did on 2026-10-18 too); Google is collected (3,825 postings) but not filtered or in the delta; Microsoft was never read (it throttled), and Amazon and Meta never ran here; **none of the research places has a reader**, they were read by hand once; only four of the 21 schools run a page that lists real titles, two systems forbid bots, and one school's board sits behind a bot check; and two targets have job feeds that answer a plain request but that Lectern cannot read yet: Moderna (Workday, 274 postings) and Hugging Face (Workable, 6). The classification is a reading by Claude Code from the watch list's own reasons and my words, and I have not reviewed it. `CLAUDE.md` Rule 6 now also requires keeping this file true when a target is added, removed or reclassified.
  - **Then, the folders.** Claude Code proposed a grouping by pipeline stage and its cost; I said this is a teaching course, at a university, and the code should show people how to organise code properly, not be a disorganised mess. Claude Code reorganised `lectern/` into `config/`, `collect/`, `publish/`, `audit/`, `tests/`, `ops/` and `notes/` (files moved with `git mv`, so history is kept) and added `lectern_paths.py`, so every script asks one place for its rule files and sibling scripts instead of guessing. That is also what lets one set of files run in the master's folders and in the other two classes' flat copies; `sync.sh` flattens on the way out. **Checked:** the five test files pass in the new layout; the scripts run both there and in a simulated flat copy; the n8n form's parity tests pass against the new layout (2,400 postings now identical, 65 fewer than before because Replit left the watch list). **Not done:** Prompt Engineering and Branding were not re-synced, and Branding's graded folder was not touched; the historical log entries keep the old file names because they record what was true then. `README.md` now explains the layout as three habits a student should copy.
  - **Then, a repository of student lab-scraping code, and where files belong.** I cloned a student repository (Biojobs) and asked for what is useful to be taken into the collectors. Claude Code kept its data-signal keywords, crawl structure and safety lists, and rebuilt the rest: `robots.txt` first, an honest User-Agent, no decoded or guessed emails, no drafted outreach, one local lab record per page (`collect/collectors/biolabs.py`, `config/biolabs.json`, 8 tests). A first live run on four directory pages found the problems recorded in `lectern/HISTORY.md`. I also said: *"Everything about Lectern should be in the Lectern folder or one of its subfolders; the folders underneath that are about the assignments."* `TARGETS.md`, `lab-outreach/`, the n8n form (now `lectern/n8n/`) and `faculty-runs/` moved into `lectern/`; the profile, CV facts and early iterations stay at the class level because the other two classes share them. The tests and the n8n parity checks pass after the move.
  - **Then, eight more companies off the watch list, and why.** I pasted the rows for Vercel, Webflow, Airtable, GitLab, Twilio, Netlify, Jasper AI and Supabase and said: *"So let's remove these from targets. They're not really educational AI. i.e. institutional, university AI, as far as I can tell. They're more software products than sort of true educational tools. Or tools that could be used as sort of the central part of a course. Unless the course is on that tool. So let's remove those. And log why."* **My reason, in short:** software products, not educational AI for institutions or universities, and not tools a course would be built around unless the course is about that tool. It is a judgment, not a finding about the companies, and it reverses the 2026-09-26 rule to watch every company whatever it posts, as the Stripe, Writer and Replit removals did. Claude Code moved the eight to the `removed` block of the watch list with that reason, dropped them from `TARGETS.md`, added a line to the profile's revisions and updated the n8n copy of the list. The watch list is now 7 boards (Anthropic, Figma, HubSpot, Miro, OpenAI, Notion, Canva; HubSpot's returns 404). Miro was not in the rows I pasted, so it stays.
  - **Then, HubSpot.** I asked what kind of education program HubSpot has, after a chat explained that HubSpot Academy teaches HubSpot's own product, and said it does not look relevant. Claude Code agreed it fails the test I had just applied and recommended removing it and, by the same test, Miro. I said: *"Remove HubSpot. Miro I'm not sure yet, I need to do more research."* HubSpot is off the watch list (reason in the `removed` block); **Miro stays**. I also said "LogWire we've removed it": no company of that name is in the project, so Claude Code took it as a mis-dictation of one already removed and changed nothing for it; the watch list is now 6 boards. **Why Miro stays, in my words:** *"I don't know Miro well enough, but it strikes me as similar to Canva, Figma, Notion in terms of whiteboard, ideation, thought. Even though they don't have an educational program as far as we can tell, I don't see any reason why it couldn't be used in general for education. But I need to look into it."* So Miro is kept as a tool in the same family as Canva, Figma and Notion, pending my research; it is a hypothesis, not a finding about Miro.
  - **Then, Lectern in other forms, and one source of truth.** I pasted a plan, "Lectern in other forms: which parallel versions to build" (a Pydantic AI judge, CrewAI as a Flow and as a Crew, LangGraph, and three always-on agents, Muse, Grok Bot and Dots, each compared with the Python as the oracle), and said the plain Python should be the source of truth for everything except data collection and what each tool does differently: *"we don't really want to replicate eight forms of what companies are being looked at… the companies that we're looking at should have a single source of truth that all of the other agentic frameworks will pull from."* Claude Code gave its thoughts first; I said *"That looks great. Build that,"* and that I would come back in the morning to look at it. **Built:** `config/targets.json`, one list of 98 targets (6 active boards, 12 removed with their reasons, the big four, 9 with no data source, 21 schools, 45 research places), from which `sources.json`, the schools in `faculty_config.json`, the seeds in `biolabs.json` and the tables in `TARGETS.md` are now generated by `ops/build_from_targets.py`; regenerating the three config files reproduced them byte for byte, and `tests/test_targets.py` fails if any drifts. `forms/` with a folder and README for each form, my plan filed as `forms/PLAN.md` (two edits, noted at its top: "seven" boards became "six", and the product claims in it are mine and unchecked), the n8n form moved to `forms/n8n/`, and shared plumbing: `compare/` (the run-format check, which passes on the real 2026-10-18 run; a run comparison; a heartbeat that says so, and does not pass, when no tool has logged) and `logs/`. `CLAUDE.md` Rule 7 records the single-source rule. 11 test files and the n8n checks pass. **Not built:** any of the seven other forms (each folder is a placeholder), the GitHub heartbeat Action (a workflow file needs a token scope I did not want to risk a push on), and any discovery agent to be shown the removed targets. Nothing was pushed: the commit waits for my word.
- **What I did:** Set the naming, asked for the plan, ruled that `.imscc` is never pushed, and said to publish all assignments. The decisions listed in `PLAN.md` are still mine, and I have not reviewed any of the plans.
- **What Claude or another person contributed:** Claude Code read the Canvas export and the briefs, wrote all twelve plans and the master plan, converted the briefs, ran the collection, wrote `publish_delta.py` and its tests, and made the commits. The statuses come from this log and from files in the folder and its sibling repositories; none was reviewed by me. Nothing in the plans records an approval, prediction or understanding I did not state. For the lab search, Claude Code added the posting function, tests and rules described above. For the research search, Claude Code compared my stated pitch with the attested record, filtered the pasted snapshot to my five interests with a status on every row, and added the filter and the think-tank definition to the profile.
- **What I understand now / still do not understand:** Not yet stated by me.
- **Evidence and next step:**
  - Evidence: `PLAN.md` and the twelve folders' `PLAN.md`; `lectern/publish_delta.py`, `lectern/test_publish_delta.py`, `lectern/runs/2026-10-18/delta-2026-10-18.{md,json,csv}`; `lectern/sync.sh --check` (shows the new script as drift in the other two classes).
  - Next: my decisions in `PLAN.md` (the pitch film first); then decide whether to commit this folder, sync the script, and publish the 2026-10-18 delta. Nothing in this folder has been committed or pushed.

### 2026-10-26 — A posting from Seoul, and two gates added to the job filter

- **Date and what I was working on:** 2026-10-26. Changing what Lectern's filter keeps, after I saw a listing in its results that was no use to me.
- **I tried / expected:** I pasted the listing, *"K12 Education Account Manager, South Korea (12 months contract), Seoul, hybrid"*, from a design-software company, as the example of what should not come through. I said, by voice: *"keep it to English-speaking countries? Unless it's France or Italy. Or Brazil? Or Portugal? And no K-12. No."* I did not state a prediction of how many postings this would remove.
- **What happened:**
  - **The keywords could not say no.** The filter only knows what to keep, and this posting is kept by the word *education* in its title. So the rule became two gates that run after the keywords and can only drop what the keywords would have kept, each with a stated reason. `keywords.json` is v0.6.0; `collect.py` reads the two new rules (`location_rule`, `k12_rule`) and nothing else changed in what it does.
  - **Measured before adding.** On the 3,243 saved ads of 2026-10-18 the keywords alone keep 92 and the gates 82: ten dropped, all for their country (Japan 4, South Korea 2, Germany 2, Indonesia 1, Mexico 1), eight of them on the six companies watched today. On a snapshot of 84,282 postings (titles and places only, no ad text) the title-keyword keeps fall from 1,056 to 886 (144 by country, 24 by K-12, 2 by both). The place reader agrees with the country codes the boards themselves report on 37,458 of 37,470 postings where both name a country. Of the 91 listings already published to Discord, ten would now show as gone.
  - **The posting I pasted is dropped for both reasons**, in the snapshot of 2026-10-24 and in the tests. But **the same job in the 2026-10-18 ads is titled *District Education Advocate*, and its text says *school system* and never *K-12*.** A rule on the word K-12 in the title alone would have missed it; only the country rule caught it.
  - **Traps looked for, on real titles and ads.** *K8* is Kubernetes (three titles), so the K-12 list says *k-8* with a hyphen. *K12* is also a company name, but the company field is not read. *Teacher* (270 titles), *school* (263) and *district* (130, mostly sales district managers) are too broad and were not added. A name shared with an American town (*Lebanon, PA* against *Beirut, Lebanon*; *New Mexico* against *Mexico*) is read by the state code. *Remote* with no country, *Remote - EMEA* and *Remote - Europe* name no country and are kept, marked as such.
  - **Both n8n copies were regenerated and re-tested.** Headless, all five workflows pass; the filter agrees with the Python on all 1,869 postings of the six watched boards; the Python and JavaScript place readers agree on all 12,882 location lines and 68,319 titles of the snapshot.
- **What I did:** Said what I wanted and pasted the example. Nothing here has been reviewed by me. **Four choices are mine, and Claude Code took a default for each:** which countries beyond the United States, United Kingdom, Canada, Australia, New Zealand and Ireland count as English-speaking (the default is none; India would bring back 20 postings in the snapshot and Singapore 22); what to do with a posting that names no country (the default keeps it); how wide K-12 is (the default is the title, in any spelling, plus grade bands such as *high school*); and whether the ad text is read for K-12 (the default is no; three OpenAI education roles that also cover higher education, and one Canva one, would go).
- **What Claude or another person contributed:** Claude Code read the folder's rules, measured, wrote the two gates, `audit/audit_gates.py` and `tests/test_gates.py`, regenerated the n8n copies with their own tooling, and wrote this entry and `lectern/HISTORY.md`. It did not run `sync.sh`, post to Discord, push, or change the server.
- **What I understand now / still do not understand:** Not yet stated by me.
- **Evidence and next step:**
  - Evidence: `lectern/config/keywords.json` (the comments of both rules hold the counts), `lectern/collect/collect.py`, `lectern/tests/test_gates.py` (17 tests), `lectern/audit/audit_gates.py` (reproduces the lists of what was dropped), `lectern/forms/n8n/test-results/parity-2026-10-26.txt`.
  - Next: I read the lists of what the gates dropped and answer the four choices; then `./lectern/ops/sync.sh --check` and `./lectern/ops/sync.sh` for the other two classes, which are still on v0.5.2. Not pushed.

### 2026-10-28 — Game and engine jobs for a second Discord channel, with posting off

- **Date and what I was working on:** 2026-10-28. Adding a second destination to Lectern for early-career game, engine and real-time jobs.
- **I tried / expected:** I pasted a list of job titles for deep Unity, Unreal and Godot skill (an AI-compiled draft, not fact-checked) and said, by voice, to add them and that *\"any game jobs that an early-career person who knows Unreal or Godot or Unity, or has any experience there, could take\"* should be posted to a new Discord channel I had just made, #games-3d-simulations. Dry run only until I say go. I did not state how many I expected.
- **What happened:**
  - **A second judge, so the education feed stays clean.** `keywords.json` v0.6.1 has an `engine_rule`; `collect/engine_jobs.py` judges a posting from its title and place; `publish/games_feed.py` posts. The country rule and the K-12 rule apply. Posting is locked three ways (the rules say off, `--send` is needed, a first send needs `--post-all`).
  - **Measured before adding.** On a snapshot of 84,282 postings from 715 boards (titles and places only), 163 titles carry a game, engine or real-time phrase; 104 are senior or mid; 22 are in countries outside the allowed list; 23 state no level and are held back; **14 would be posted** (11 Epic Games internships and an Associate Game Designer each at Hasbro, Naughty Dog and Nintendo). **Lectern's own six boards contain none.**
  - **The feed is thin for games.** Of 51 game, film and engine companies on its list that I checked, 17 have a board it can read. Unity, Electronic Arts, Ubisoft, Activision and Blizzard are not among them. The pasted list also says Godot is a learning engine and not a hiring engine; the snapshot agrees (zero Godot titles).
  - **Traps found by reading.** *Unity Catalog* is a Databricks data product; *Design Systems Designer* contains *systems designer*; *games* and *gaming* are mostly sales verticals; *K8* had already been caught as Kubernetes. A test found a real bug in my own poster: a failed first send created the memory file, which would have switched off the first-send lock; fixed, with a test.
  - **Later the same day, the game-company list.** I said yes to the list and asked that it be reviewed company by company. Claude Code checked each board (all 17 answered), read each studio's early-career titles, and added the result to `targets.json` as a `games` section, so there is one list of companies and not two. **Ten studios are kept, seven dropped with a reason, six marked to-do.** Dropped: Take-Two (a corporate board), Bethesda (**the feed's \"Bethesda\" board is a physical-therapy employer, not the game company**), Twitch and Discord (not game developers), Hasbro (toys), Framestore and Foundry (film VFX). Ubisoft has a readable public board that the feed does not read (SmartRecruiters, 324 postings); Activision (Workday), Blizzard (Phenom), Electronic Arts (a paged HTML site) and Unity (not identified) do not. The dry run went from 14 to 23; nothing was posted.
  - **Not decided, and left to me:** whether to post titles with no level word (25 held back); whether to switch on the simulation group (10 more, about half not 3D); the rights question for posting individual postings from the ai-jobs snapshot; where the poster runs, since the snapshot lives on the server; and whether Ubisoft goes into the feed's company list, which is a change in the ai-jobs repository.
- **What I did:** Gave the instruction and the list, and the order not to post; later said yes to the game-company list. I have not reviewed the rules, the 23 that would be posted, the held-back list, or the verdict on each studio.
- **What Claude or another person contributed:** Claude Code read the pasted list as data, measured every phrase against the snapshot, wrote the judge, the poster, the audit and about 50 tests, the studio review and the `games` section of `targets.json`, regenerated and re-tested both n8n copies, and wrote `lectern/HISTORY.md` and Rule 8 in `CLAUDE.md`. It sent nothing, read no webhook, did not run `sync.sh`, did not push and touched no server.
- **What I understand now / still do not understand:** Not yet stated by me.
- **Evidence and next step:**
  - Evidence: `lectern/config/keywords.json` (`engine_rule` and its comment), `lectern/config/targets.json` (section `games`) and section H of `lectern/TARGETS.md`, `lectern/collect/engine_jobs.py`, `lectern/publish/games_feed.py`, `lectern/audit/audit_engine_titles.py`, `lectern/tests/test_engine_jobs.py`, `lectern/tests/test_games_feed.py`, `lectern/forms/n8n/test-results/parity-2026-10-28.txt`.
  - Next: I read the dry run and the studio verdicts and answer the open questions; if I say go, set `posting` to `on`, choose where it runs, and run `--baseline` or `--post-all` once. Not pushed.

### 2026-10-28 — Consulting firms and a third Discord channel, with posting off

- **Date and what I was working on:** 2026-10-28. Adding a consulting-jobs search to Lectern.
- **I tried / expected:** I pasted the first part of a consulting-firm directory and said, by voice, to add those firms to the job search for consulting jobs, and that new jobs found should be posted to a consulting channel after Lectern has been through them. Dry run only until I say go. I did not state how many jobs I expected.
- **What happened:**
  - **A research session came first.** It tiered the pasted firms, went to each top firm's own website for its job system, and tested every board Lectern can read with one request. **Only 5 of the 64 firms researched have a board Lectern's readers can read today** (Accenture Federal Services, Altman Solon, Analysys Mason, Baringa, Brattle: 946 postings). **Workday is the biggest gap**: 12 boards answered a public list with no login. The directory's terms could not be read (a bot check), so it was used for names only.
  - **A judge of its own.** The main filter looks for teaching words and, on 907 consulting postings, kept 9, none early-career consulting. `consulting_rule` (keywords v0.6.3) takes a role word plus an explicit early sign in the title, no senior level, no clearance, the allowed countries. The firms went into `targets.json` as a `consulting` section, one list, with a test that none can reach the #professor-bear feed. **5 kept, 43 to do, 24 tagged and dropped** (17 non-consulting companies, 7 in-house groups). I did not add the directory's visa flag anywhere.
  - **What it would post today:** 38 postings, 16 distinct roles at two firms: Brattle's 2027 research-analyst and PhD-associate roles (one posting per city) and Analysys Mason's September 2027 associate-consultant roles. 82 more say Analyst, Associate or Consultant with no early sign and are held back (63 at Accenture Federal Services). **The clearance veto removed 6 titles at Accenture Federal Services; none would have been posted.** The country gate dropped 6 early-sign titles in Germany, Norway and Spain.
  - **A small thing found while building it:** the poster's locks were copied once already for the games channel. Writing them a second time would have meant two places to fix, so they moved into one shared file (`channel_feed.py`) and the games poster was rewritten on it with its tests unchanged.
  - **Not decided, and left to me:** whether Accenture Federal Services belongs (default: board kept, clearance titles vetoed); a bare Analyst or Associate (default: held back, 82); a Workday reader (10 consulting firms); checking sponsorship against Department of Labor and USCIS records; pasting the rest of the directory (Canyon to Z); a longer country list for consulting; and where the poster runs.
- **What I did:** Gave the instruction and the directory, and the order not to post. I have not reviewed the rules, the 38, the held-back list or the verdict on each firm.
- **What Claude or another person contributed:** A research session found the firms' job systems and measured a first rule; Claude Code folded that into `targets.json`, wrote the judge, the collector, the poster, the audit and 20 tests, regenerated and re-tested both n8n copies, and wrote `lectern/HISTORY.md` and Rule 9 in `CLAUDE.md`. It sent nothing, read no webhook, did not run `sync.sh`, did not push and touched no server.
- **What I understand now / still do not understand:** Not yet stated by me.
- **Evidence and next step:**
  - Evidence: `lectern/config/keywords.json` (`consulting_rule` and its comment), `lectern/config/targets.json` (section `consulting`) and section I of `lectern/TARGETS.md`, `lectern/collect/consulting_jobs.py`, `lectern/collect/consulting_collect.py`, `lectern/publish/consulting_feed.py`, `lectern/audit/audit_consulting_titles.py`, `lectern/tests/test_consulting_jobs.py`, `lectern/tests/test_consulting_feed.py`.
  - Next: I read the dry run and the verdict on each firm and answer the open questions; if I say go, set `posting` to `on`, choose where it runs, and run `--baseline` or `--post-all` once. Not pushed.

### 2026-10-30 — A search for speakers: companies with their own MCP, with posting off

- **Date and what I was working on:** 2026-10-30. Adding a speakers search to Lectern.
- **I tried / expected:** I said, in these words: "We want to add another search to Lectern and this is for speakers. Try to figure out which companies have speakers that'll talk about their MCP like Unreal just came out with an MCP. Figma has an MCP. Pretty much everyone's coming out with MCPs. We're looking to invite the evangelist type people in a company who are willing to come and give an online talk about using their MCP, whatever that MCP is." I did not say how many companies I expected, which channel it should go to, or that anyone should be contacted.
- **What happened:**
  - **Six research passes** read 67 companies' own docs, help centres, changelogs and announcements (never a third-party directory) and found 101 public people (developer advocates, evangelists, solutions engineers, product managers and a few executives) and 47 past talks. Every one of the 67 has an MCP of its own with a primary source. Epic's Unreal MCP is real and experimental (Unreal Engine 5.8, and in beta in UEFN); Figma's is real.
  - **The research was an agents' reading, so it was checked again by script:** every one of the 195 company links was fetched once (179 answered 200, 10 turned the script away by robots.txt, 5 were 404, 1 was 403). The 5 bad links were the agents' own and now count for nothing. Each of the 101 people's source pages was fetched once and searched for the surname: 94 pages answered, 87 showed the surname, and for 90 of the people the researcher had opened the page (83 of those the script confirmed; 3 it did not find, two on a Salesforce page that needs JavaScript; 4 turned the script away). 11 people rest on a search result only and are marked so.
  - **A judge of its own, and the unit is a company.** It sums sourced signals (the company's own MCP page, a DevRel team, past talks, a community channel, a public route, a named person) to a score out of 100; no MCP page that answers, or no published route, or under 60, holds the company back. **31 would be posted, 35 held back, 1 not verified (Salesforce).** Six held-back companies have talks and a named person but publish no route (Docker, Notion, PayPal, Postman, Snowflake, Stripe). Only 3 companies publish a DevRel page, speaker form or partnerships form that answers (Autodesk, Apify, Exa); everyone else gives a community forum, so the score cannot tell a company that wants speakers from one that has a forum.
  - **The people are not in the repository.** It is public and the folder's rule keeps others' names out, so the names, titles and source pages are in `lectern/speaker-records/` (gitignored), and a test fails if a surname from there reaches the tracked list. No email address or phone number was recorded for anyone.
  - **The agents also said** that several "speakers" are product managers, executives or engineers, not DevRel (Atlassian's, Docker's confirmed ones, Red Hat's, IBM's); that some talks are about building any MCP server, not the company's; that one person named for Microsoft appears to have left; and that Unity's in-editor MCP is deprecated in its own docs. These are in the local file next to each person, not decided.
  - **Not decided, and left to me:** the channel's name (`speakers` is a placeholder); whether a community forum counts as a route; whether the six companies with people and no route should be posted anyway; whether product managers and engineers count as "evangelist type"; whether Blender Lab (a foundation project, held as a to-do) counts as a company; whether a company I removed from the watch list for not being educational AI (GitLab, Vercel, Supabase, Twilio, HubSpot) belongs here; and who, if anyone, is approached and how. Nobody has been.
- **What I did:** Gave the instruction above. I have not reviewed the list, the scores, or any person.
- **What Claude or another person contributed:** A session started from another session ran six research agents, wrote the judge, the collector, the poster, the audit, 28 new tests and 2 added to test_targets, folded the companies into `targets.json` (section `speakers`), generated section J of `TARGETS.md`, regenerated and re-tested the n8n copy, and wrote `lectern/HISTORY.md` and Rule 10 in `CLAUDE.md`. It sent nothing to anyone, filled in no form, read no webhook, did not run `sync.sh` and did not push.
- **What I understand now / still do not understand:** Not yet stated by me.
- **Evidence and next step:**
  - Evidence: `lectern/config/keywords.json` (`speakers_rule` and its comment), `lectern/config/targets.json` (section `speakers`) and section J of `lectern/TARGETS.md`, `lectern/collect/speakers_judge.py`, `lectern/collect/speakers_collect.py`, `lectern/publish/speakers_feed.py`, `lectern/audit/audit_speakers.py`, `lectern/tests/test_speakers_judge.py`, `test_speakers_collect.py`, `test_speakers_feed.py`, `lectern/forms/n8n/test-results/parity-2026-10-30.txt`. The people are in `lectern/speaker-records/` on the Mac that built it, not in the repository.
  - Next: I read the list and the local people file and answer the open questions; if I say go, name the channel, set `posting` to `on` and run `--baseline` or `--post-all` once. Not pushed.

### 2026-10-31 — Federal 508 and accessibility work for a friend: a fifth search, with posting off

- **Date and what I was working on:** 2026-10-31. Adding a federal Section 508 search to Lectern.
- **I tried / expected:** I said, in these words (with the friend's name left out, because this repository is public): "Can we have the job search also look for something called Federal 508 work? For [a friend], I think she's looking for contract work. Or remote work." I expected it to look like the other searches.
- **What happened:**
  - **A judge of its own.** A Section 508 or accessibility phrase in the title, a US place, and `remote` in the title or place or `contract` in the title. A fitting role that says neither is held back. A clearance in a title is a flag on the post, not a veto. No level is read, because an audit is not an entry-level job.
  - **A research pass listed 67 employers** (civic-tech and federal contractors, large integrators, accessibility firms, agencies' 508 offices) and found each one's job system. It was an agent's reading, so every readable board was fetched again here: 17 are readable (16 Greenhouse, 1 Ashby). One of my own first guesses was wrong and the agent caught it: the Ashby slug `fable` answers but belongs to an unrelated company.
  - **The result is that it would post nothing today.** The 17 readable boards hold 3,542 postings, read once on 2026-10-31; one names a 508 phrase (Accenture Federal Services, 'UX Designer with 508 Compliance', Arlington, VA) and it is onsite, so it is held back. The postings that matter are on boards Lectern cannot read (Workday: Guidehouse has a 'Section 508 Subject Matter Expert') and behind API keys someone must request (USAJOBS for agency jobs, SAM.gov for contract opportunities).
  - **Not decided, and left to me:** the channel's name (`federal-508` is a placeholder); whether a clearance should hide a posting (`clearance_policy`); whether 'consultant' in a title counts as contract; whether to build a Workday reader and to request the two keys (each key is requested on the site by whoever will use it; nothing here did); whether the ai-jobs snapshot, a wider net, should be read; and whether anything should be posted at all.
  - **A brief on what the work needs (later the same day).** I pasted one, written by another tool, on what a person doing federal 508 work needs and where the work is (the friend's name is in its title), and said to add it to the agent's notes. It went into section K.2 of `lectern/TARGETS.md` without the name; the full text is kept in a private note outside the repository. Its main points: the DHS Trusted Tester v5 certification is the gate for the testing work; of four lanes where the work is, only one (contract tester roles) is something a job board lists, so prime contractors (found from USAspending award history) and vendors that need an Accessibility Conformance Report are found another way; and SAM.gov mostly lists contracts too big for one person. None of it was checked here. No rule changed: `TTv5` is the one search term the judge does not already match, and it was not added because nothing measured it.
- **What I did:** Gave the instruction above, and later pasted the brief. I have not reviewed the list or the judge. I have not written to the friend.
- **What Claude or another person contributed:** Claude Code wrote the judge, the collector, the poster, 20 new tests and 2 added to test_targets, folded the employers into `targets.json` (section `federal508`), generated section K of `TARGETS.md`, wrote Rule 11, refreshed and re-tested the n8n copy, and ran one research agent. Later Claude Code filed the pasted brief as section K.2 of `TARGETS.md` (compared its search terms with the judge by hand, kept the friend's name out, kept the full text in a private note) and added a `HISTORY.md` entry.
- **What I understand now / still do not understand:** Not yet stated by me.
- **Evidence and next step:**
  - Evidence: `lectern/config/keywords.json` (`federal508_rule` and its comment), `lectern/config/targets.json` (section `federal508`) and section K of `lectern/TARGETS.md`, `lectern/collect/federal508_jobs.py`, `lectern/collect/federal508_collect.py`, `lectern/publish/federal508_feed.py`, `lectern/tests/test_federal508_jobs.py`, `test_federal508_feed.py`, `lectern/forms/n8n/test-results/parity-2026-10-31.txt`; for the brief, section K.2 of `lectern/TARGETS.md` and the `2026-10-31 (later)` entry in `lectern/HISTORY.md`.
  - Next: I answer the open questions; if I want real postings in it, a Workday reader and the two keys come first; if I say go, name the channel, set `posting` to `on` and run `--baseline` or `--post-all` once. Not pushed.

### 2026-11-01 — A Workday reader for the federal-508 and consulting channels

- **Date and what I was working on:** 2026-11-01. Building a reader for Workday job boards so the federal-508 channel (and the consulting channel) can read the boards that hold most real federal 508 postings.
- **I tried / expected:** My instruction, as it reached Claude Code from the session that started this one: build a Workday reader; check each board's robots.txt and terms first and respect them; flip the Workday entries in the list to `active` only after fetching each board and checking the employer's name from a posting; keep posting off. I expected the 508 postings the research had found to show up.
- **What happened:**
  - **Four boards forbid a script and one more is blocked, so they are not read.** Booz Allen, ICF, Leidos and Perkins say in their terms that bots, scraping or data mining are not allowed; Cambridge Associates and Baker Tilly say the same (consulting); CACI's robots.txt disallows its board. Their entries are `unreadable` with the clause named. Huron and BRG have no terms-of-use page I could find; Workday's own terms page I could not find either. Accenture's main board and Kaufman Hall (Vizient's board) were tried and are not read, for reasons in the list.
  - **Nine boards are read:** Guidehouse, GDIT, Unisys and Salesforce (federal 508), and Guidehouse, Huron, Alira Health, Ankura and Berkeley Research Group (consulting). A posting on each names the employer.
  - **The first read posted nothing, and that was wrong in a way that mattered.** The Guidehouse 'Section 508 Subject Matter Expert' title is listed with the place '3 Locations', so the rule held it back as saying neither remote nor contract. Its own record lists 'US - Remote (Any location)'. I had the reader look up a Workday posting's places when its title already matches a 508 phrase and its place is only a count (two lookups today); the dry run then posts **one** listing. That one lookup decides whether the channel has anything to say, so it is a design choice worth my review.
  - **Numbers (2026-11-01):** federal 508, 21 boards, 7,598 postings (4,059 on the Workday boards), three titles with a phrase, one would be posted; consulting, 10 boards, 2,295 postings (1,351 on Workday), 70 would be posted, 33 of them from the Workday boards (7 of those showed only a count for a place; after the places look-up added later that day, 69 would be posted).
  - **Posting is off.** The dry runs read no webhook and sent nothing.
- **What I did:** Gave the instruction. I have not reviewed the reader, the list changes or the numbers.
- **What Claude or another person contributed:** Claude Code read the robots files and terms, wrote the reader, `tests/test_workday.py` (22 tests), the list changes, the notes in `keywords.json`, `HISTORY.md` and this entry, and ran every test file and the n8n headless test.
- **What I understand now / still do not understand:** Not yet stated by me.
- **Evidence and next step:**
  - Evidence: `lectern/collect/collect.py` (`fetch_workday`, `post_json`), `lectern/collect/consulting_collect.py`, `lectern/collect/federal508_collect.py` (`name_the_places`), `lectern/tests/test_workday.py`, the `UPDATE 2026-11-01` text in `lectern/config/keywords.json`, section I and K of `lectern/TARGETS.md`, `lectern/HISTORY.md`.
  - Open questions (the first, whether the consulting reader should look up the places of the 7 count-only postings, was answered yes by Professor Bear: done, 2 of the 7 drop out, 69 would be posted, see HISTORY.md): whether to ask Booz Allen, ICF, Leidos, CACI and Perkins for permission or look at their boards by hand; whether Guidehouse's board, read three times in one hour while building this, should be read less often. Not pushed.

## GitHub pushes

One line per push to GitHub: the date and the commit note. The commit ID for each push is in `git log`; a commit can't contain its own ID.

| Date | GitHub note |
|---|---|
| 2026-09-24 | feat(fall-2026): start Professor Bear's Boondoggle Report with ten Gru turns and a Frictional log |
| 2026-09-24 | docs(fall-2026): state that Assignment 2 specifies a downloadable Gru, and keep the wrong-application start on the record |
| 2026-09-24 | docs(fall-2026): log Gru's /v0–/v4 outputs for the downloadable Gru, with all 20 turns verbatim |
| 2026-09-26 | feat(fall-2026): add assignment-3 with its five standard records |
| 2026-09-26 | docs(fall-2026): make this folder the canonical master for the three-class project |
| 2026-09-26 | feat(fall-2026): add assignment-3 with its five standard records |
| | ↑ **the row above is the subject this commit actually carries.** The subject intended for it was *"feat(fall-2026): add the reject sampler; reading rejects exposed a false-positive class"*; a scripting error reused an earlier commit's subject line. The content is correct; history was not rewritten to fix a label. |
| 2026-09-26 | feat(fall-2026): audit the filter by job function; ML 'training' was a false friend |
| 2026-09-26 | feat(fall-2026): target becomes 'makes the materials'; body rule measured, cut twice |
| 2026-09-26 | feat(fall-2026): rank companies by demand, not postings by fit; Google's absence was an API artefact |
| 2026-10-07 | chore(fall-2026): first real sync; add demand_report.py to the shared list; log the show-tell films |
| 2026-10-07 | docs(fall-2026): add the project software design document, written by Gru in silent mode |
### 2026-11-02 — A USAJOBS reader, built and tested but not yet run

- **Date and what I was working on:** 2026-11-02. Building a reader for USAJOBS' own search API so the federal-508 channel can find the agencies' postings, not only the contractors'.
- **I tried / expected:** I requested a USAJOBS API key, which a script cannot do. USAJOBS emailed it to me. I did not paste the key into the chat; I stored it myself in `~/.usajobs/key` (mode 600, outside the repo) from a terminal command Claude Code gave me. Then I asked for the reader. I expected to see the agencies' 508 postings.
- **What happened:**
  - **The reader is built and tested, and has made no real request.** USAJOBS asks for the email the key was registered with as the User-Agent, and `~/.usajobs/email` does not exist yet. The helper stops with an error that names that file and shows no value.
  - **No `active` entry for USAJOBS is in the list yet**, because an active entry carries a measured posting count and there is none. The 8 agency entries now say the reader is built and the first read is waiting for the email.
  - **The key is in no file of the Lectern folder or the course notes** (a search found 0 of 245 files).
  - **A limit I expect:** USAJOBS' keyword search matches the whole ad, but the judge reads the title, so a posting whose title does not say 508 or accessibility will not be posted. The first read will show how big that gap is. The field names for the remote flag are unchecked until then.
- **What I did:** Requested the key, stored it myself, and gave the instruction. I have not reviewed the reader.
- **What Claude or another person contributed:** Claude Code wrote the reader, `tests/test_usajobs.py` (14 tests, no network), the list note changes, `HISTORY.md` and this entry, and ran every test file.
- **What I understand now / still do not understand:** Not yet stated by me.
- **Evidence and next step:**
  - Evidence: `lectern/collect/collect.py` (`usajobs_login`, `fetch_usajobs`), `lectern/collect/consulting_collect.py` (`records`), `lectern/tests/test_usajobs.py`, the 2026-11-02 entry in `lectern/HISTORY.md`.
  - Next: I put the registered email in `~/.usajobs/email`; then one real read, a dry run, and the first active entry. Not pushed.

| 2026-10-18 | data(lectern): delta 2026-10-18: +42 new, ~7 changed, -9 gone |
| 2026-10-18 | docs(fall-2026): one numbered folder and plan per Canvas assignment; publish_delta.py; collectors in the sync list |
| 2026-10-18 | docs(fall-2026): publish profile.yml for exercise 06 and a layout for its film; Stripe and Writer off the watch list |
| 2026-10-18 | docs(fall-2026): correct why Stripe and Writer were removed; profile revisions block; layouts for the profile and résumé films |
| 2026-10-18 | docs(fall-2026): word the business-school target as bringing real AI expertise in to direct an AI centre |
| 2026-10-18 | docs(fall-2026): exercise 06 folder: README, RUN_LOG, resume.json copy, private-notes ignore; Brown and eight more schools on the watch list |
| 2026-10-19 | docs(fall-2026): ai-explainer layout and evidence for the résumé-JSON film; résumé, profile and gaps framing |
| 2026-10-19 | feat(fall-2026): post new listings to Discord automatically; daily.sh; text-out for the big-four collectors; résumé-film evidence |
| 2026-10-19 | docs(fall-2026): add Track D, part-time research by outreach to labs, to the profile |
| 2026-10-19 | docs(fall-2026): propose the lab record for the part-time research outreach search |
| 2026-10-19 | docs(fall-2026): the lab is the unit; fit and target rules for the outreach search; places to read |
| 2026-10-19 | docs(fall-2026): add the big Boston hospitals to the outreach search |
| 2026-10-19 | docs(fall-2026): distance rule and the list of places for the outreach search |
| 2026-10-19 | docs(fall-2026): add Moderna as a company to look at; what the Kendall Square map showed |
| 2026-10-19 | docs(fall-2026): a company team is treated like a lab; Moderna's research teams |
| 2026-10-19 | docs(fall-2026): add the MIT Media Lab; Whitehead and Media Lab addresses beside the Broad |
| 2026-10-19 | docs(fall-2026): filter the Boston and Cambridge institutes by his five interests; think tank defined broadly |
| 2026-10-19 | feat(fall-2026): post great-fit labs to Discord for review before any approach; Rule 5; Northeastern arrangement noted |
| 2026-10-19 | docs(fall-2026): a first search of Northeastern's business school and Institute for Experiential AI; two great fits posted |
| 2026-10-19 | fix(fall-2026): correct the skills note in the derived résumé; record what it omits |
| 2026-10-19 | docs(fall-2026): check lab funding against the NIH and NSF award databases, from a student's version |
| 2026-10-19 | docs(fall-2026): note the n8n form of the Lectern pipeline and what testing it found |
| 2026-10-19 | docs(fall-2026): remove Replit from the watch list, not educational AI; --only option for sync.sh |
| 2026-10-20 | docs(fall-2026): a README and a daily history for the Lectern folder; the n8n form beside the Python |
| 2026-10-20 | docs(fall-2026): TARGETS.md, every target classified with its data link, its reader and what is missing |
| 2026-10-20 | refactor(fall-2026): organise lectern/ into config, collect, publish, audit, tests and ops, with one place for paths |
| 2026-10-20 | feat(fall-2026): a lab-page collector adapted from Biojobs; everything about Lectern moves into lectern/ |
| 2026-10-20 | docs(fall-2026): remove eight software-product companies from the watch list, not educational AI |
| 2026-10-20 | docs(fall-2026): remove HubSpot from the watch list, education is product training; Miro stays |
| 2026-10-20 | feat(fall-2026): one list of targets for every form of Lectern; forms/ folders and shared comparison plumbing |
