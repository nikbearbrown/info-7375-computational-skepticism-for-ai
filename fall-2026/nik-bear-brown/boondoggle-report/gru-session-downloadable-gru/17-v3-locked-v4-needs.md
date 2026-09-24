# Gru turn 17-v3-locked-v4-needs

## Professor Bear typed

```
1. P4 final wording: accepted, all three layers.
2. The install command is run from the toolkit checkout and pointed at her repo: `./gru install <path to her repo>`. Detection has two halves, because if Claude Code never discovers the skills, nothing inside Claude Code can say so. Inside a session, the hub's first act is to check that its own files resolve (the links aren't broken, the Gru prompt file is where it should be) and report a broken install before anything else. Outside, from the terminal, `./gru doctor <path>` checks the links, the exclude lines, and the state file, and the README tells her to run it the moment `/gru` does nothing.
3. Flag A: accepted. Dirty files are pinned by content hash and marked uncommitted; only clean files get the SHA.
4. Flag B: uninstall is in v1. A tool that writes into someone else's repository has to be able to undo exactly what it wrote. `./gru uninstall <path>` removes the links and only the exclude lines it added, and leaves sdd/ alone unless she says otherwise.
5. Flag C: required. A quoted, redacted excerpt next to every CODE and DOC citation. That's the part of the model's work she can audit at a glance.

Lock /v3. Go to /v4.
```

## Gru replied (verbatim, unedited)

/v3 is locked.

**Logged:**
- **D23:** P4 final, all three layers.
- **D24:** `./gru install <path>` runs from the toolkit checkout. Detection has two halves: the hub checks itself first inside a session, and `./gru doctor <path>` works from outside. The README tells her to run `doctor` if `/gru` does nothing.
- **D25:** Dirty files are pinned by content hash and marked `uncommitted`.
- **D26:** `./gru uninstall <path>` is in v1. It removes only what it wrote and leaves `sdd/` alone unless she says otherwise.
- **D27:** A quoted, redacted excerpt goes next to every CODE and DOC citation.

One note for /s4, not a blocker. "Only the exclude lines it added" means install has to *remember* which lines those were. A marked block in `.git/info/exclude` (`# gru:begin` … `# gru:end`) makes uninstall exact. That includes the case where `/gru share` has already removed the `sdd/` line, so uninstall must not add it back.

---

**/v4: USER AND BUSINESS NEEDS**

**User Needs (the student)**

**U1. Provenance at a glance.** The student must be able to see, for every claim in her design document, whether it came from the docs, the code, herself, or Gru, along with the exact excerpt it rests on, when she or a reviewer questions a line, *without* opening the repository to hunt for it.
*Test:* A format checker passes only if every claim has a label, and every CODE or DOC claim has a pinned citation plus an excerpt.

**U2. Disagreements come to her.** The student must be asked about every disagreement a static read detects between docs, code, and her own answers, before the affected section is written, when she starts a design in a codebase she didn't write, *without* knowing in advance which files contradict each other.
*Test:* The fixture. All three known contradictions surface as CONFLICTs without prompting (D18).

**U3. The scan can be audited.** The student must be able to see what gru read for each question, how it found each file, and what it skipped or redacted, when she suspects the scan missed something, *without* rerunning it or trusting it on faith.
*Test:* Every question in every section file has a read log with method tags (b, c, or a), skips, and redactions.

**U4. The design survives the session.** The student must be able to resume a design in a new session with every confirmed gate, decision, and piece of reasoning intact, when a session ends or context compacts, *without* re-answering confirmed questions or losing why a decision was made.
*Test:* Close the session. The next day, `/gru v1` reports v0 as confirmed, checks the prompt hash and citation drift, and cites the relevant D-numbers.

**U5. A build plan with nothing unchecked in it.** The student must be able to generate a Boondoggle Score at any stage, when she is ready to hand work to Claude, *without* any unchecked claim entering a Claude prompt as fact.
*Test:* Every claim inside a Score prompt keeps its label. No unresolved CONFLICT appears in any prompt. Each one appears as a preceding human task.

**U6. Review on her terms.** The student must be able to put her design document up for review in the same pull request as the change it describes, when *she* decides to, *without* committing secrets or anything she hasn't seen listed.
*Test:* `/gru share` lists every file that will become visible, refuses on any secret-pattern match, and removes the exclude line only after she confirms.

**Operator Needs**

**O1. Leave no trace in a shared repo.** A student installing into a team repository she doesn't own must be able to install, diagnose, and uninstall gru, *without* changing teammates' `git status` or overwriting anything.
*Test:* `git status` is identical before install, after install, and after uninstall. A name or `sdd/` collision stops the install. `doctor` reports broken links.

**O2. One file changes the rules, visibly.** The maintainer must be able to update Gru by replacing one prompt file, when Gru's method changes, *without* students' in-progress designs silently switching rulebooks.
*Test:* Replace the file. Each confirmed gate still shows the hash it was confirmed under, and the next command announces the change.

**Business Need**

**B1. Evidence of thinking, not only a document.** The course must be able to verify that a design document came through the interview, meaning the student confirmed each gate herself and her answers are in her own words, when reviewing or grading it, *without* taking the document's rigor on faith.
*Test:* The state file shows a confirmation for each gate. The section files hold her answers and Gru's pushback in order (D16). A section with no recorded answers fails the format checker.

That's eight: six user, one operator split in two, and one business need.

---

**COMPONENT FILTER**

| Component | Serves | Status |
|---|---|---|
| Repo-scan script, layered with method tags | U2, U3 | Prototype exists. It must be checked against D22: does it do (b), then (c), then (a)? |
| Gate-state tracker | U4, O2, B1 | Prototype exists. It must now record the prompt hash per gate (D12). |
| **Two format checkers** | **U1? U5? B1?** | **Prototype exists. I can't map them: see flag 1.** |
| **"A few skills"** | **?** | **Prototype exists. I can't map them: see flag 1.** |
| Hub skill with translation layer and self-check | Entry point for all of them, plus O1 | Designed (D3, D24) |
| Phase skills (`gru-v0` …) | U1, U2, U4, B1 | Designed. Naming is still open (OQ4). |
| Redaction and secret-skip | U3, U6 (P4) | Designed (D23) |
| `decisions.md` writer | U4, B1 | Designed (D17) |
| Score generator (`/gru claude`) | U5 | Designed (D19) |
| `/gru share` with the secret check | U6 | Designed (D11, D23) |
| `install` / `uninstall` / `doctor` | O1 | Designed (D24, D26) |
| **Menu line "not in this version"** | **None** | **See flag 2** |
| **/g2, /g3, /g4 and the eight refinement tools** | **None** | **See flag 3** |

**Flag 1: prototype components I can't map.** Rule 1 says no component is documented before it maps to a Need. You've told me the prototype has two format checkers and a few skills, but not *what they check* or *which skills*. Name each one and its job, and I'll map it or flag it. That doesn't mean it's wrong. It means it was built before a Need existed to justify it, which is exactly the case this check exists for.

**Flag 2: "not in this version" serves no Need.** It's honest and cheap, but no U, O or B requires it. You have two options. Tie it to U4 as part of the menu being truthful about what exists, or accept it as a scope note with no Need behind it. I'd pick the first option, but the decision should be on record.

**Flag 3: most of Gru's command library serves no Need here.** Because the prompt is verbatim and the translation layer maps every command, `/gru g2`, `/gru comparable`, `/gru security` and the rest will *work* in v1. Yet none of the eight Needs asks for them, and nobody has decided whether they write files, carry labels, or sit behind gates. So it's a decision for you:
- **(a)** All of Gru's commands run in v1, and each one follows P2 (labels) and D11 (reviewable). That's more surface to test.
- **(b)** v1 supports the section path (/v0 through /p5, /g1, /claude) plus /help and /list. Everything else shows as "not in this version," exactly like the deferred commands.
- **(c)** Something in between. Name which.

This choice drives /p1. A MUST-BUILD list of 40 commands is a very different project from a list of 18.

---

**When flags 1–3 are answered, this is the PHASE 1 GATE:**

> Before systems and architecture: the problem summary is confirmed, principles P1–P4 are locked with their collisions resolved, the primary flow is documented along with its integration and administrative flows, and eight Needs are written and mapped to components. Does this reflect what you're building toward?

We don't start /s1 until you confirm it.
