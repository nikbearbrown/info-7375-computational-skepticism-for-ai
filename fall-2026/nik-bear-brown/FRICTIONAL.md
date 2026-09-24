# FRICTIONAL — Professor Bear's process log

## Executive summary

**What this is.** The honest process log for the work in this folder, written the way the course asks students to write theirs: what was tried, what went wrong, what changed, and who did what, the human or the AI.

**Why read it.** It's a real example of the log, not a constructed one. It shows the instructor's own work run through the same record students keep, mistakes included.

**What we are doing.** **Assignment 2 in INFO 7375 Computational Skepticism for AI: the Boondoggle Report.** The application Professor Bear is specifying with Gru is **a downloadable version of Gru**: skills and scripts that run inside a downloaded repository and can read its folders and files, instead of a prompt pasted into a Claude Project.

**What it records so far.** One working session on 2026-09-24, which went wrong before it went right.
- **Getting Gru running took three tries.** The command line swallowed `/help` as its own command, then failed on a revoked login. Pasting the prompt into a fresh conversation, the brief's own fallback, worked.
- **Mistake 1: the wrong application.** Claude Code read Professor Bear's folder in his *other* class (Prompt Engineering), assumed the work was greenhouse-watch, and ran 14 Gru turns specifying it. Professor Bear stopped it. The turns are kept.
- **Mistake 2: building before specifying.** When Professor Bear described the real application, Claude Code started building a downloadable Gru toolkit outside this repo before any design document existed. Also kept, uncommitted.
- **Where it stands:** the Boondoggle Report on the downloadable Gru has **not started**. Next is a fresh Gru session at `/v0`.

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

---

## GitHub pushes

One line per push to GitHub: the date and the commit note. The commit ID for each push is in `git log`; a commit can't contain its own ID.

| Date | GitHub note |
|---|---|
| 2026-09-24 | feat(fall-2026): start Professor Bear's Boondoggle Report with ten Gru turns and a Frictional log |
| 2026-09-24 | docs(fall-2026): state that Assignment 2 specifies a downloadable Gru, and keep the wrong-application start on the record |
