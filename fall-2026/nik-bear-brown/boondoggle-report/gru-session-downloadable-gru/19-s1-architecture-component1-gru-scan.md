# Gru turn 19-s1-architecture-component1-gru-scan

## Professor Bear typed

```
1. (ii), one skill per job. Six folders, and OQ4 closes: the folder names are job names.
2. /g1 serves U6. Confirmed.
3. No. The prototype has no ./gru entry script. The scripts are only run directly with python3 today. Component 9 is new.
4. The inventory and the order are right. Nothing missing that I can see.

And I'll close OQ11 and OQ12 now so they don't block later:
- OQ11, what a claim is: one bullet. Every section file writes its claims as a bulleted list, one claim per bullet, and prose around them carries no claims. That makes "every claim is labelled" testable: every bullet in a claims list has exactly one source label, and CODE and DOC bullets also carry a pinned citation and an excerpt. No percentage.
- OQ12, who confirmed: a handle she chooses at install, stored in the state file. gru may suggest her git user.name, but only uses it if she says yes. Her full name never goes in by default.

Start with component 1.
```

## Gru replied (verbatim, unedited)

**Logged:**
- **D30:** Skill architecture (ii), six job-named folders. This closes OQ4.
- **D31:** /g1 serves U6.
- **D32:** `./gru` is a new component. Today the prototype scripts are run directly with `python3`.
- **D33 (closes OQ11):** One claim per bullet, in a bulleted claims list. Each bullet has exactly one label. CODE and DOC bullets also carry a pinned citation and an excerpt.
- **D34 (closes OQ12):** The confirmer is recorded as a handle she chooses at install. Her `user.name` is suggested but used only if she says yes. Her full name is never recorded by default.

D33 leaves a residual risk, which I'm recording now so it doesn't get lost. "Every bullet is labelled" can be checked by a script. "Prose carries no claims" and "one claim per bullet" can't. A sentence like "Since exports default to `/out`, the new format writes there too" puts an unlabelled claim into prose, and only a reader will catch it. That makes it a plausibility-audit item for her and her reviewer, and it goes to /p4 by name. Checker one can flag the obvious cases, such as prose that contains a file path, a code identifier, or a number. It can't prove the prose contains no claims.

---

**/s1 · COMPONENT 1: `gru-scan`**

**Maps to:** U2 (disagreements come to her), U3 (the scan can be audited), and U1 (provenance at a glance, because every citation and excerpt starts here). **Flow placement:** primary flow step 4, before every question. Its orientation pass runs once per design. Both pass.

---

**THE PROBLEM IT SOLVES**
Whatever the student pastes into a Project carries her blind spots, and nothing in that setup checks a claim against the code. `gru-scan` decides what gets read for each question, independent of what she already knows about. It returns what it found as labelled, cited, excerpted claims, together with a full record of what it read, how it found each file, and what it didn't read.

**HOW IT WORKS**

Every step is assigned to either a script or the model. This split is where Flow Honesty flag C applies.

| Operation | Done by | What it does |
|---|---|---|
| **Orientation pass** | Script (the prototype's `repo_scan`, extended) | Runs once per design and again when HEAD moves. Maps structure: languages, layout, entry points, declared commands, tests, CI, docs, skills, TODOs, and the N most recent commits. Builds two indexes: an **entry-point index** for method (c) and a **doc-claim index** (every doc file, broken into candidate claim sentences) for method (b). |
| **Claim extraction** | Model | Picks out the doc-claim sentences relevant to the current question, plus any STUDENT answers already given. |
| **(b) Claim-anchored read** | Script finds, model reads | For each claim in scope, the model names its anchors: paths, config keys, env var names, commands, identifiers. The script finds where each anchor appears in code **and in other docs**, since the scheduler case was DOC against DOC. |
| **(c) Structural read** | Script | From the entry points relevant to the question, follows imports or calls to depth *d*. Python uses `ast`. Other languages: see decision 3. |
| **(a) Term search** | Script | Searches the question's terms as a last resort. Any file found only by (a) is marked as such. |
| **Pinning and excerpts** | Script | Each cited range is pinned to the commit SHA if the file is clean, or to a content hash marked `uncommitted` if it isn't (D25). Excerpts are pulled by line range and redacted **before** the model or any file sees them. |
| **Support or contradiction judgment** | Model | Decides for each claim whether the read code supports it, contradicts it, or is silent. **Absence counts as a finding.** "Reads `EXPORT_DIR`, and no default is assigned anywhere in the files read" is exactly the finding your fixture depends on. |
| **Conflict candidates** | Model | Pairs of claims that disagree (DOC and CODE, DOC and DOC, STUDENT and anything) go to `gru-section`, which asks. The scan never asks and never resolves. |

**Inputs:** repo path; the question's ID and text; claims in scope; the orientation indexes; HEAD SHA and dirty-file list.

**Outputs:**
- **Claims list:** one bullet each, `LABEL | claim | path:lines @ SHA or hash [uncommitted] | redacted excerpt | method tag`
- **Conflict candidates:** claim pairs, each with its evidence
- **Read log entry** for the question: files read with a b/c/a tag, anchors and search terms used, files matched but not opened, deny-list skips with reasons, redactions (path, line, and pattern type, **never the value**), and whether the read budget was hit
- **Orientation cache:** raw, and never shared. See decision 1.

**State changes:** It appends the read log to the working section record and writes the orientation cache. It **never** touches gate state, section content, or anything else in her repo.

**Error signals:**
- Not a git repo: content-hash mode is announced once.
- Binary or oversized file: skipped and logged.
- Language unsupported for (c): falls back to (a), logged as `c-unavailable`.
- Read budget exhausted: stops, and logs every match it didn't read.
- An anchor found nowhere: reported as a finding ("no code references `/out`").

**Retry behavior:** The script half is deterministic. The same question at the same SHA gives the same candidate files. The model half can vary between runs, so the read log records which files were actually read each time, not just which were eligible.

---

**PRINCIPLE ALIGNMENT**
- **P4:** Static only. It applies the deny-list, redacts before any excerpt leaves the script, records env var names only, and doesn't follow symlinks out of the repo.
- **P2:** Labels, citations and excerpts are attached *where the claim is found*, so everything later only has to keep them, not reconstruct them.
- **P1:** It produces evidence and conflict candidates. It never writes section content and never asks a question on its own.
- **P3:** It reports disagreement and never ranks sources. The contradiction judgment says what disagrees with what. It never says which source is right.

---

**EDGE CASES**

| # | Situation | Expected behavior | Priority |
|---|---|---|---|
| 1 | **A symlink in her repo points outside it** (`config -> ~/.ssh/`) | Not followed. Logged as `skipped: symlink leaves repo`. | **Must-Fix.** Without this, a static read can leak her home directory into a reviewable log. |
| 2 | **A secret-shaped value is the very thing a claim is about** ("the endpoint is `https://…?token=…`") | Excerpt redacted. The claim is marked `value redacted: verify locally` and becomes a human task. | **Must-Fix** |
| 3 | **The code is renamed or loaded indirectly** (`dump_bundle()`, config-driven dispatch, dynamic import) | (b) finds it if a claim names the config key. (c) misses dynamic loads. (a) misses renames. Whatever is missed shows as "anchor found nowhere" or as matches not opened. | Important. This is the residual risk U3 exists for. |
| 4 | **The DOC claim has no anchor** ("exports are handled carefully") | Recorded as `no anchor`, and `gru-section` asks her to make the claim specific. | Important |
| 5 | **Large repo or monorepo** | Budget bound. The truncation and every unread match are logged. | Important |
| 6 | **Vendored or generated code** (`node_modules/`, `vendor/`, `build/`) | Skipped by rule and logged. If a claim's only anchor is there, that's reported. | Important |
| 7 | **A recent commit diff contains a secret that was later reverted** | Diff excerpts are redacted like any other file. | **Must-Fix** |
| 8 | **The tree is dirty mid-change** | Content hash plus `uncommitted`, per file (D25) | Important |

**Critical edge cases:** 1, 2 and 7. Each could expose secrets through a file D11 makes reviewable.

---

**SCOPE BOUNDARY**
`gru-scan` does **not**:
- ask the student anything
- resolve or rank a CONFLICT
- write section content
- execute any code in the repo
- open deny-listed files
- follow symlinks outside the repo
- make network calls
- read git history beyond the N most recent commits
- write anywhere except the read log and its orientation cache

**PROTOTYPE GAP**
The prototype's `repo_scan` is roughly the orientation pass without the two indexes. Everything else is new: per-question reads (b), (c) and (a), method tags, pinning, excerpts, redaction, the symlink rule, absence findings, and conflict candidates.

---

**Four decisions before I mark component 1 documented:**

1. **Where the orientation cache lives.** D11 says raw scan output stays excluded, but `/gru share` removes the exclude line for `sdd/`. If the cache is inside `sdd/`, sharing exposes it. **Proposal:** put it in `.gru/` at the repo root, with its own exclude line that `share` never touches and `uninstall` removes.
2. **Read budget per question.** A fixed number of files, a fixed number of lines, or both? What's the default? I'd start at 25 files or 3,000 lines, whichever comes first, adjustable per question, and always logged when hit.
3. **Languages for method (c) in v1.** Python via `ast` is standard library and reliable. JavaScript and TypeScript would need regex heuristics. **Proposal:** (c) is Python-only in v1. Other languages fall back to (a), logged as `c-unavailable`, and /p2 records a reopen condition.
4. **Recent commits.** How many does the orientation pass read, and does it read the diffs or only the messages? Diffs are where reverted secrets live (edge case 7).
