# Gru turn 04-v0-one-sentence

## Professor Bear typed

```
The downloadable Gru is a set of Claude Code skills and standard-library scripts, installed by one command into the student's own repository's .claude/skills/ folder, that reads that repository's files before each interview question and produces, in a sdd/ folder of that repository, one design-document file per Gru command written only after the student has answered that command's questions, with every claim labelled as read from the repo, said by the student, or Gru's judgment, plus a Boondoggle Score file and a state file recording which gates the student confirmed.

For flags 2 and 3 I'd take (a), the translation layer, and it has to cover the three deferred commands too: the menu shows them as "not in this version" rather than dropping them silently.
```

## Gru replied (verbatim, unedited)

That sentence passes the test. It names a thing (skills plus scripts), a place (the student's own `.claude/skills/`), and outputs (files in `sdd/`). It also answers the insertion-point question I expected to break it.

It's still carrying too much, though. Two clauses in it aren't describing the thing. They're commitments:

- "reads that repository's files before each interview question" and "written only after the student has answered"
- "every claim labelled as read from the repo, said by the student, or Gru's judgment"

These two are the most important ideas in the proposal, and that's why they don't belong here. Inside the /v0 sentence they're description, and description gets quietly dropped when a deadline is close. In /v2 each one becomes a principle with an example that honors it, an example that violates it, and a named production failure state. That makes them enforceable.

The three labels are also the best idea in this proposal. They turn "the scan feeds the interview" into something a format checker can test: every claim either has a source label or it doesn't.

One precision fix. "One design-document file per Gru command" is ambiguous. `/help`, `/list` and `/show` produce nothing. `/g2`, `/g3` and `/g4` audit or summarize the SDD instead of adding sections to it. I've narrowed it to *section-producing* commands. If you meant audits to get their own files too, tell me.

---
**V0 SUMMARY**

**Ecosystem:** Claude Code running in a user's terminal, where skills are folders of instructions and scripts that Claude Code finds inside a repository. The toolkit ships as a public GitHub repository built like the brutalist.art toolkit, and it is installed by INFO 7375 students, Humanitarians AI fellows, and anyone else who clones it.

**Existing components touched:**
- Gru prompt, the version with separate /build, /verify, /audit gates (depends on; one verbatim copy, reached through a declared translation layer)
- Claude Code skill discovery, `.claude/skills/<name>/SKILL.md` (depends on; external contract; commands are typed `/gru <cmd>`)
- brutalist.art toolkit (copies the pattern of; no shared code)
- The student's repository (reads anything, expects nothing; also the write target for `.claude/skills/` and `sdd/`)
- Your prototype: repo-scan script, gate-state tracker, two format checkers, some skills (extends; evidence, not specification)
- Snickerdoodle CLI and `recipes/` (not in v1)

**Proposal:**
> Downloadable Gru is a set of Claude Code skills and standard-library scripts, installed by one command into a student repository's `.claude/skills/` folder, that produces in that repository's `sdd/` folder one design-document file per section-producing Gru command, a Boondoggle Score file, and a gate-state file recording which gates the student confirmed.

---

**Decisions logged:**
- **D1:** The scan feeds the interview and never replaces it. Goes to /v2 as a principle.
- **D2:** Every claim carries a source label: REPO, STUDENT, or GRU. Goes to /v2 as a principle.
- **D3:** A translation layer, option (a). `/gru <cmd>` maps to Gru's `/<cmd>`. The menu is rendered with the `/gru` prefix. /build, /verify and /audit appear as "not in this version." The source prompt stays untouched. Flags 2 and 3 are closed.
- **D4:** /build, /verify and /audit are deferred. Goes to /p2 with the reopen condition "when the Snickerdoodle CLI ships as an installable dependency."

**Open questions for /p5** (none of these block /v1):
- **OQ1:** Installing into the student's repo is a write. What happens if `.claude/skills/` already has a skill with the same name, or `sdd/` already exists?
- **OQ2:** /claude can run at any stage, so the Score will be regenerated. Is it overwritten, or kept as versions?
- **OQ3:** Can a student re-answer a confirmed gate? If so, what happens in the state file to the sections written after it?

---

Does this reflect what you're proposing to build? If yes, we proceed to /v1. If not, what's wrong with the sentence?
