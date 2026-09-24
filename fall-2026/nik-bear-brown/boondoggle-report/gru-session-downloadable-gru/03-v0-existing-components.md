# Gru turn 03-v0-existing-components

## Professor Bear typed

```
- The Gru prompt: depends on. One verbatim copy ships inside the toolkit (the version with /build, /verify, and /audit as separate gates); the skills point into its sections and never paraphrase it. Updating Gru means replacing that one file.
- brutalist.art: copies the pattern of. No shared code.
- Claude Code's skill discovery: depends on. A skill is .claude/skills/<name>/SKILL.md in the repo. And one contract I've already been bitten by: Claude Code treats a bare /help or /v0 as its own command, so a typed "/v0" never reaches Gru. Commands have to be typed as /gru v0.
- The Snickerdoodle CLI and recipes/: /build, /verify, and /audit assume them, and most repos won't have them. I'd leave those three commands out of the first version rather than depend on something most users won't have.
- The repo being scanned: Gru expects nothing. Any folder, ideally a git repo. It reads whatever is there — README, AGENTS.md or CLAUDE.md, package manifests, tests, CI, any existing skills, TODO markers, recent commits — and says plainly when there's little to read, so the interview carries the load.
- One more, and you should know it: extends a prototype. Before this conversation, I started building it: a repo-scan script, a gate-state tracker, two format checkers, and a few skills. No design document existed when I did that.
```

## Gru replied (verbatim, unedited)

Question 2 is answered. Here is what I'm recording:

| Component | Relationship | Note |
|---|---|---|
| Gru prompt (the version with separate /build, /verify, /audit gates) | depends on | One verbatim copy. Skills point into its sections and never paraphrase it. |
| brutalist.art toolkit | copies the pattern of | Shares no code |
| Claude Code skill discovery (`.claude/skills/<name>/SKILL.md`) | depends on | External contract you don't own. Commands must be typed `/gru v0`. |
| Snickerdoodle CLI and `recipes/` | not in v1 | /build, /verify, /audit are deferred |
| The scanned repo | reads, expects nothing | Says plainly when there's little to read |
| Your prototype: repo-scan script, gate-state tracker, two format checkers, some skills | extends | Built before any design document existed |

Before question 3, three flags. Two of them are collisions inside your own answers.

**Flag 1: the prototype came before the design.** You named it yourself, which is the right move. The risk is that this SDD ends up describing what you already built and calling it a design. So here is the rule I'll hold from here on. The prototype is evidence, not a specification. When we reach /s1, every prototype component has to map to a Need in /v4 like everything else. Anything that maps to nothing gets flagged, and "I already wrote it" doesn't count as a Need.

This has a useful side effect. The prototype repo is the first thing the scan should run against. If Gru can't produce an honest interview from the repo that built Gru, it won't produce one from a student's repo.

**Flag 2: the verbatim copy conflicts with the `/gru v0` contract.** Your rule is that the skills never paraphrase the prompt. But the prompt tells users to type `/v0`, `/help` and `/claude`. Its Welcome Menu prints exactly the commands that Claude Code intercepts. A verbatim copy teaches every student a command that can't reach Gru.

Your options:
- **(a)** Add a documented translation layer. The entry skill maps `/gru <cmd>` to Gru's `/<cmd>` and prints the menu with the `/gru` prefix. The source file stays untouched, and the rewrite is a declared, testable transform, not a paraphrase.
- **(b)** Edit the source prompt so it uses `/gru` syntax everywhere. That's one file, which you said is the update path anyway.
- **(c)** Document an exception to the no-paraphrase rule for command syntax only.

**Flag 3: the verbatim copy conflicts with dropping /build, /verify and /audit.** The same file advertises those three commands in the menu and in /list. If v1 ships without them, the menu promises commands that don't exist. Whichever option you choose for Flag 2 has to handle this too.

Dropping them doesn't break /claude, and here is why. In the prompt, /claude is available at any SDD stage. The Snickerdoodle PASS requirement only applies on the recipe path. I'll log the deferral for /p2 with a reopen condition, something like "reopen when the Snickerdoodle CLI ships as an installable dependency." Tell me if the condition is different.

You don't need to settle Flags 2 and 3 before question 3. They go to /p5 as open questions, and they have to be closed before /v2 locks the principles.

**Question 3: In one sentence, what are you proposing to ADD?**

Use this format:

> "[THING] is a [WHAT] inserted [WHERE] that produces [OUTPUT]."

The one place I'd expect this sentence to break is **[WHERE]**. You told me Claude Code discovers skills inside the repository. That leaves two different insertion points:

- The student copies or installs the toolkit's `.claude/skills/` into their own repo and runs Claude Code there.
- The student runs Claude Code inside the toolkit repo and points it at a different folder.

These are two products, with different install steps, different scan paths, and different ways to fail. Your sentence has to pick one.

For **[OUTPUT]**, name the artifacts, not the purpose. "Helps students think clearly about design" names a purpose. "An SDD and a Boondoggle Score, each section written only after the user answers that section's interview" names an output.
