# Gru turn 16-v2-locked-v3-flows

## Professor Bear typed

```
1. P1 through P4 accepted, with one amendment to P4. "Read, never run" also has to mean "never read secrets." A static read can do harm without executing anything: opening .env files, key files, or credentials, and then quoting them into a read log that D11 makes reviewable in a team repo. P4's commitment should say gru never opens .env files, private keys, or credential stores, records only the names of environment variables and never their values, and says in the read log that it skipped them.
2. C1: accepted. A claim keeps its source; her confirmation is recorded next to it. P2 is primary.
3. C2: accepted. The success condition is amended as you wrote it. P4 is primary.
4. OQ10: (d), layered, with the method tag in the read log. You're right that (b) is what I actually did by hand.

That locks /v2 from my side. Go to /v3.
```

## Gru replied (verbatim, unedited)

/v2 is locked from your side. I accept the P4 amendment, and it's the right catch. Your amendment protects secrets by file name, though, and secrets don't only live in files with obvious names. Before I write the final P4, here are two layers the amendment doesn't cover.

**Layer 2: secrets inside files gru is *supposed* to read.** A filename deny-list stops gru from opening `.env`, `*.pem` and `credentials.json`. It doesn't stop it reading `config.py` with a hard-coded API key, a CI workflow with a token pasted inline, a notebook's output cell, or a diff in "recent commits" where someone committed a key and then reverted it. Under method (d), gru will read those files, because they're relevant. So P4 needs a second rule. **Any secret-shaped value in a file gru does read is redacted before anything is written to a read log, section file, or Score, and the redaction is recorded.**

**Layer 3: a check at the exit.** D11 makes all of `sdd/` reviewable. `/gru share` is the one point every document passes through before git can see it, so it should run a secret-pattern check over `sdd/` and refuse to un-exclude if anything matches. Pattern matching will miss things, so that residual risk goes to /p4 by name. It doesn't disappear.

**P4, final wording (pending your accept):**
> **Read, never run.** gru reads the repository statically and never executes its code. It never opens `.env` files, private keys, or credential stores. It records environment variable names, never their values. It redacts secret-shaped values in any file it does read before writing anything. It records every skip and redaction in the read log. `/gru share` refuses to proceed if a secret pattern matches anywhere in `sdd/`. Questions that only running the code can settle are handed to the student as human tasks.

**Logged:** D20 (C1): a claim keeps its source, confirmation is recorded next to it, and P2 is primary. D21 (C2): the success condition is amended and P4 is primary. D22 (OQ10): layered relevance (b), then (c), then (a), with each file tagged by the method that found it. OQ6 and OQ10 are closed.

---

**/v3: CORE USER FLOWS**

This is drafted from the record, and the steps I couldn't ground are marked **[?]**. Her feature is the export.

**PRIMARY FLOW: install to shared design document**

| # | User action | System response | State change |
|---|---|---|---|
| 1 | Clones the course repo | none | Toolkit checkout on disk |
| 2 | From her team repo root, runs the install command **[? exact form]** | Checks for a git repo, `.claude/skills/gru*` collisions, and an existing `sdd/`. Prints what it will write. | Skill links written, exclude lines added, `sdd/` created, state file initialized with the prompt hash and folder name |
| | *Decision point:* collision or existing `sdd/` | Stops and names the collision. Never overwrites. | none |
| 3 | Opens Claude Code in her repo, types `/gru help` | The hub reads the state file and renders the menu with the `/gru` prefix. Deferred commands show "not in this version." The current gate shows as none. | none |
| 4 | `/gru v0` | For each question: layered read, then the question with labelled, cited, method-tagged claims | Read log appended |
| 5 | Answers a question | If a source disagrees, the CONFLICT is the next question. Otherwise the next /v0 question. | Answer and pushback appended to the section's working record |
| 6 | Resolves a CONFLICT | Records her resolution as STUDENT with her reason | `decisions.md` entry |
| 7 | Confirms the V0 summary | Writes the /v0 section file | State file: gate v0 confirmed, prompt hash, repo SHA |
| 8 | Closes the laptop. Next day, `/gru v1`. | The hub reads the state, checks the prompt hash, and checks drift in every cited file | Drift and hash change announced before the first question |
| 9 | `/gru s1` before /v4 is confirmed | Says what's missing and returns to the current phase | none |
| 10 | Continues through /v4. Phase 1 gate. | Gate question | State file: phase 1 confirmed |
| 11 | `/gru claude` at any stage | Score for what exists. Labels survive. Each unresolved CONFLICT becomes a human task. | Score file written **[? OQ2: overwrite or version]** |
| 12 | `/gru share` | Secret check, then lists exactly what becomes visible to git, then asks her to confirm | `sdd/` exclude line removed |
| 13 | `git add sdd/` and commits in her export PR | none (git's job) | Design document reviewed alongside the change |

**INTEGRATION FLOWS**

| System | Protocol and data | If unavailable or unexpected | Who owns the failure |
|---|---|---|---|
| Claude Code skill discovery | Reads `.claude/skills/<name>/SKILL.md` | Skills not found (wrong folder, version change): `/gru` does nothing, silently | Anthropic's contract. Detection is gru's job. **[?]** |
| git | `rev-parse HEAD`, `.git/info/exclude` | Not a repo: content-hash fallback (D6). Detached HEAD: SHA still valid. **Dirty working tree: see flag A.** | gru |
| Toolkit checkout (link target) | Symlinked skill folders and the Gru prompt file | Moved or deleted: every link breaks. Pulled: the prompt hash changes (D12). | Student, with detection by gru **[?]** |
| Filesystem (her repo) | Static reads under the P4 rules | Unreadable or huge files: skipped and logged | gru |

**ADMINISTRATIVE FLOWS**

| Operator | Flow | Status |
|---|---|---|
| Bear (maintainer) | Replaces the Gru prompt file. Students see the hash change announced at their next command. | Defined (D12) |
| Student | Updates the toolkit by `git pull` in the course repo | Defined by implication. The course repo is the channel (OQ5). |
| Student | **Uninstalls gru from a team repo** | **Missing: see flag B** |
| Student | Restarts a design, or re-answers a confirmed gate | Open (OQ3) |

---

**Three flags from the flows:**

**A. Dirty working tree.** She's in the middle of the export change, so `export.py` has uncommitted edits. gru reads the edited file and pins the citation to `HEAD`. The SHA says one version and the quote comes from another. A reviewer who checks out that SHA finds a different line and decides the document is wrong. **Proposal:** when the cited file is dirty, pin to a content hash and mark it `uncommitted`. Only clean files get the SHA.

**B. No uninstall.** Install writes links, exclude lines, and a folder into a team repo. A tool that writes into someone else's repo needs a documented way to undo that exactly: remove the links, remove only the exclude lines it added, and leave `sdd/` alone unless she says otherwise. Is this `/gru uninstall` in v1, or /p2?

**C. The Flow Honesty Test finds the step that depends on the model.** *If this were a CLI with no UI, would it solve the problem?* Mostly yes. The scan, labels, pinned citations, state file, share check, and format checkers are deterministic scripts. **The step that isn't deterministic is step 5: detecting that two sources disagree.** Comparing "exports default to `/out`" with `os.environ["EXPORT_DIR"]` is Claude reading and judging, not a script checking. If the model misses a disagreement, the miss is silent. The read log shows the file was read, but not that the disagreement in it was overlooked. Scripts can check that a citation *exists*. They can't check that the cited line *says what the claim says*. **Proposal:** every CODE and DOC claim carries the quoted excerpt, redacted, next to its citation. Then she can plausibility-audit each claim at a glance, without opening files, and the gap between "cited" and "supports the claim" is where she can see it. The fixture tests the rest.

---

**To lock /v3:**
1. Is the final wording of P4 accepted, including layers 2 and 3?
2. What's the exact form of the install command (step 2), and how should gru detect that its skills weren't discovered or its links are broken?
3. Flag A: are dirty files pinned by content hash and marked `uncommitted`?
4. Flag B: uninstall in v1, or /p2?
5. Flag C: are quoted, redacted excerpts required next to every CODE and DOC citation?
