# The Boondoggle Report — a downloadable Gru

**Class:** INFO 7375 Computational Skepticism for AI, Fall 2026 · **Assignment 2** ([`BRIEF.md`](BRIEF.md))
**Application being specified:** a downloadable version of Gru — skills and scripts that run inside a downloaded repository and can read its folders and files, instead of a prompt pasted into a Claude Project.

## Executive summary

**What this is.** Professor Bear's worked example of Assignment 2. The assignment asks for a small real application to be specified with Gru, one gated command at a time, then a Boondoggle Score splitting the build between Claude and the human, then a reflection on that split.

**What the application is.** Gru today is a long prompt that someone pastes into a Claude Project. It can only know what the person tells it. The downloadable version is the same Gru, packaged the way Professor Bear's `brutalist.art` toolkit is packaged: skills, scripts, and one entry point, installed into a repository so that Gru reads the code, docs, and history itself before it asks the person anything.

**Where it stands.** `/v0` through `/v4` are confirmed and the Phase 1 gate is passed, in the session in [`gru-session-downloadable-gru/`](gru-session-downloadable-gru/README.md). `/s1` (components) is in progress. **Claude Code typed Professor Bear's answers in that session and confirmed its gates for him. He has not reviewed them yet.** Gru's section outputs are copied verbatim into [`../FRICTIONAL.md`](../FRICTIONAL.md).

**What is in this folder so far, and why.** A false start, kept deliberately:
- **The wrong application.** Turns 00–13 in [`gru-session/`](gru-session/README.md) specify *greenhouse-watch*, a job-board watcher from Professor Bear's Prompt Engineering class. Claude Code chose it after reading that class's example folder and assuming it was the task. Professor Bear caught it and stopped the session.
- **Why it's kept.** The course log keeps mistakes. The turns are still verbatim Gru output, and they show the gates working: Gru rejected two versions of the `/v0` sentence and found real design problems in that tool. But they are not the submission.
- **A second mistake.** Before any design document existed, Claude Code also started *building* a downloadable Gru toolkit outside this repository. That is the opposite of what Gru teaches (specify, then build). It is logged in [`../FRICTIONAL.md`](../FRICTIONAL.md), kept, and uncommitted.

**Next.** Professor Bear reviews the answers given for him. Then finish `/s1`, run `/claude` for the Boondoggle Score, and build the tool from it.

---

## Where each deliverable stands (the downloadable Gru)

| Deliverable | Status |
|---|---|
| `/v0` problem formulation | ✅ confirmed ([turn 05](gru-session-downloadable-gru/05-v0-confirmed.md)) |
| `/v1` problem intake | ✅ confirmed ([turn 14](gru-session-downloadable-gru/14-v1-problem-summary.md)) |
| The own-voice paragraph after the Problem Summary | 🟡 drafted by Claude Code, not yet Professor Bear's words ([`PARAGRAPH-AFTER-V1-DRAFT.md`](PARAGRAPH-AFTER-V1-DRAFT.md)) |
| `/v2` principles, `/v3` flows, `/v4` needs, Phase 1 gate | ✅ confirmed (turns [15](gru-session-downloadable-gru/15-v2-principles.md)–[18](gru-session-downloadable-gru/18-phase1-gate-s1-inventory.md)) |
| `/s1` components | 🟡 in progress: component 1 of 11 drafted ([turn 19](gru-session-downloadable-gru/19-s1-architecture-component1-gru-scan.md)) |
| Professor Bear's review of the answers and gate confirmations Claude Code gave for him | ⬜ |
| `/claude` Boondoggle Score | ⬜ |
| Reflection, prompts A–D | ⬜ |

## The false start: greenhouse-watch (wrong application, kept for the record)

Everything in this section describes the mistaken session, not the assignment's application.

### Its confirmed `/v0` sentence

> greenhouse-watch is a Claude Code skill that a student runs as an entry point to the Reallocation Engine, beside the role scorer and feeding nothing into it, reading one company's public job board on Greenhouse, Ashby, or SmartRecruiters plus the student's résumé JSON and remembering which job ids it saw last run, that produces a notice, not a verdict: a Markdown report and a JSON log listing only the postings new since the last run that match the résumé under a written string-match scheme, each with the résumé field and posting field behind every match.

### Open questions Gru logged in that session

Copied from Gru's own log (turns 05–13); Gru's wording is authoritative. These concern greenhouse-watch, not the downloadable Gru.

| # | Question |
|---|---|
| OQ-1 | Which posting fields the match scheme may use (it must exclude repeated company text), and the match threshold |
| OQ-2 | The name "greenhouse-watch" misleads, since the skill also reads Ashby and SmartRecruiters |
| OQ-3 | Should `location_mode` default to soft or hard? |
| OQ-4 | The `priya-nair` persona file has a calendar that doesn't match a running visa clock |
| OQ-5 | Do the three job platforms keep company text in a separate field, or inside the job description? |
| OQ-6 | Scheduling with a GitHub Action contradicts keeping the résumé on the student's laptop (decided: local schedulers only) |
| OQ-7 | Match citations copy résumé values into the log (decided: keep the values; never commit them) |
| OQ-8 | The output folder can be anywhere, so the privacy boundary is only a convention (decided: refuse unless gitignored or a persona) |

## How the Gru session was run

For the downloadable Gru, see [`gru-session-downloadable-gru/README.md`](gru-session-downloadable-gru/README.md). For the false start, see [`gru-session/README.md`](gru-session/README.md): the prompt, the method, what differs from running Gru in a Claude Project, and who typed Professor Bear's side of the conversation.
