# Three classes, one project — what is shared and what is not

## Executive summary

**What this is.** The rule for keeping one live-coded project consistent across three courses. The same job-search tool is being built in Computational Skepticism, Branding and AI, and Prompt Engineering, with a different emphasis in each. **This folder — `info-7375-computational-skepticism-for-ai/fall-2026/nik-bear-brown/` — is the canonical master.** A change to a shared file is made here first and then propagated to the other two.

**Why read it.** Because three copies of the same tool drift, and drifted copies are worse than one copy: a student reading the Branding version gets a filter that no longer matches the Skepticism version, and neither says which is right. This file names which files are shared, which are deliberately different, and the one command that checks.

**The rule in one line.** Shared code and configuration are edited **here** and copied out. Class-specific writing — assignments, logs, framing — is never copied at all.

**Why this folder is master.** The project's hard part is not the fetching, it is knowing what the output is worth: which matches are noise, what the filter misses, which numbers are records and which are judgments. That is Computational Skepticism's subject. The other two classes consume the tool; this one interrogates it.

---

## The three emphases

| Class | The same tool, asked a different question | Assignment 3 there |
|---|---|---|
| **Computational Skepticism** (master) | *How do we know the output is right?* Probes, counterfactuals, what the filter misses, which values are records and which are judgments | Robustness and explanation — a probe runner and a check of whether a fluent explanation names the feature that actually moves the output |
| **Branding and AI** | *Whose problem does it solve, and what data does the agent need?* The Madison agent, positioning, the data pipeline | Build Your Data Pipeline — Lectern collecting from three ATSs |
| **Prompt Engineering** | *What is the recipe, and which labor belongs to Claude?* The eight-step dream-job recipe, prompts, handoff conditions | The recipe plus a working prototype |

The tool is identical in all three. Only the question changes.

## Shared — canonical here, copied out

| Path | What it is |
|---|---|
| `lectern/collect.py` | The collector: fetch → normalise → filter → dedupe → validate → write, three ATS providers |
| `lectern/sources.json` | The watch list — 18 boards, plus the companies that cannot be read |
| `lectern/keywords.json` | The filter: role, topic, and flexible-terms words, with what was cut and why |
| `lectern/ATS.md` | Which applicant-tracking system each company uses, and an honest "unknown" where it was not verified |
| `facts/professor-bear-cv.json` | The CV as structured facts, attested |
| `figma/` | The first single-company iteration: saved board, scan, kept postings |
| `greenhouse-watch-demo/` | The Reallocation Engine's watcher run on one board |

**Edit these here.** Then run `./lectern/sync.sh` to copy them out and see what changed.

## Not shared — deliberately different

| Path | Why it must not be copied |
|---|---|
| `FRICTIONAL.md` (every copy) | Each class's log records that class's session. Copying one over another destroys the record |
| `assignment-*/` | Different assignments with different briefs, rubrics, and deadlines |
| `boondoggle-report/` | Only Computational Skepticism's Assignment 2 |
| `README.md`, `CLAUDE.md` | Each names its own class, its own emphasis, its own push approval |
| **Run outputs** — `all-jobs-<date>.*`, `jobs-of-interest-<date>.*`, `quality-report-<date>.md` | The data lives in the class whose assignment it is submitted for. Today that is Branding's `assignment-3/`. Copying 3.4 MB of identical JSON into three repos buys nothing; the tool that regenerates it is what is shared |

## How to propagate

From this folder:

```bash
./lectern/sync.sh --check     # report drift, change nothing (safe, do this first)
./lectern/sync.sh             # copy the shared files out to the other two repos
```

It never deletes, never touches a file in the "not shared" list, and never commits — each repo is committed by hand with its own message and its own `FRICTIONAL.md` entry.

## If a shared file was edited in the wrong repo

It happens during a live class. The fix is not to copy it back blindly:

1. `./lectern/sync.sh --check` names the file and shows the difference.
2. Decide which version is right — usually the newer edit, but not always.
3. Bring the correct content **here**, into the master.
4. Run `./lectern/sync.sh` so all three match.
5. Note it in this class's `FRICTIONAL.md`, because a drift that happened is a finding about the workflow.

## Current state

**2026-09-26.** The shared spine was copied into this folder today, which means the master started out *behind* the other two — Branding had the collector, the watch list, and the data; this folder had none of it. That is the inverse of what "master" should mean, and it is recorded rather than tidied away. Branding and Prompt Engineering were byte-identical on every shared file at the time of the copy, so nothing had to be reconciled.

**2026-10-07.** The first real propagation. Professor Bear asked for all three classes to be brought into sync and pushed. `--check` reported every listed file identical, but a file-by-file comparison outside the list found `lectern/demand_report.py` (added to the master and Branding on 2026-09-26) missing from Prompt Engineering: the script's shared list had not been updated when the file was added. The list now carries it, and `sync.sh` was run for real for the first time. Lesson for the workflow: a new shared file is not shared until it is in the `SHARED` array; adding a file to `lectern/` and adding it to the list are one change, not two.
