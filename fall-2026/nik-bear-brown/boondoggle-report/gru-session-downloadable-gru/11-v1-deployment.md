# Gru turn 11-v1-deployment

## Professor Bear typed

```
Accepted, both the rewrite and the principle. That's the course's whole argument: a disagreement is a question for a person, not a verdict for the code. Her resolution goes in as STUDENT with her reason.

6.
Why her repository: Claude Code discovers skills and reads files relative to where it's running, so running inside her repo keeps the reading, the pinned SHAs, and the sdd/ folder all with the code under review, and lets her design document be reviewed in the same pull request as the change it describes. Running from inside the toolkit would make every citation a path into someone else's checkout.

The shared-repo cost, and my answer to OQ1: installing must not change her teammates' git status. The install writes the skill links into .claude/skills/ and lists them in the repo's local, uncommitted exclude file (.git/info/exclude), so they're invisible to git. sdd/ is also excluded by default. Committing her design document to the team repo is her decision, made on purpose, not something the tool does. If a skill with the same name already exists, the install stops and says so; it never overwrites.

Minimum environment: Python 3.9 or later, standard library only. Git recommended, not required (content hashes cover a plain folder). macOS and Linux in v1. Windows only through WSL; native Windows (the bash entry script, symlinks) goes to /p2 as a decision.
```

## Gru replied (verbatim, unedited)

Question 6 is recorded. "Every citation would be a path into someone else's checkout" is the reason, and it's a good one. The pinned SHAs only mean something if they're SHAs of *her* repo.

**Logged:**
- **D8:** Rule accepted. A CONFLICT is a question for a person, not a verdict for the code. Her resolution is recorded as STUDENT, with her reason.
- **D9:** Install target is her repo. Skills go into `.claude/skills/` and are listed in `.git/info/exclude`. `sdd/` is excluded by default. Committing is her deliberate act. A name collision stops the install and never overwrites.
- **D10:** Python 3.9 or later, standard library only. Git recommended, not required. macOS and Linux in v1. Native Windows goes to /p2 as a recorded decision; WSL only.

OQ1 is mostly closed. Four things are still open, and one of them contradicts your own reason for the install target.

**1. `sdd/` excluded by default conflicts with "reviewed in the same pull request."** You chose her repo so the design document could ride in the PR with the change it describes. Excluding it by default is the right safety choice for a shared repo. But once `sdd/` is in `.git/info/exclude`, a plain `git add sdd/` does nothing, and a student who has never met the exclude file won't know why her design document won't stage. The deliberate act needs a named, documented path. That could be `git add -f sdd/<file>`, or a `/gru` subcommand that removes the exclude line after she confirms. It also forces a second decision: *which* files in `sdd/` are meant for review. Section files and the Score, yes. What about the gate-state file and the read logs? Logging this as **OQ7**. It must close before /s3.

**2. Skill links point into her clone of the course repo.** If she runs `git pull` in the course repo halfway through her design, the Gru prompt changes underneath her. Gates confirmed under one version, next section written under another. Her document would be governed by two different rulebooks and nothing would record it. My suggestion is that the gate-state file records the Gru prompt's content hash at every confirmed gate. When the hash changes, Gru says so at the next command and doesn't silently carry on. Accept or amend?

**3. The macOS bash trap.** macOS ships bash 3.2. An entry script that uses bash 4 features (associative arrays, `mapfile`, `${var,,}`) works on Linux and your Mac with Homebrew bash, then breaks on a fresh student Mac. Either keep the entry script to bash 3.2 or POSIX `sh`, or make it a thin shim that hands off to Python right away. Logged as a constraint for /p3.

**4. An existing `sdd/` folder.** You covered skill name collisions but not this one. A team repo could already have an `sdd/` for something else. Does the install stop here too, or write to a different folder name?

---

**Question 7: What is the build scale?**

So far I have you as solo builder, with a prototype that already exists. What I still need:

1. **Timeline.** When do the first students or fellows run this? Is that tied to a course week, and on what date? "After v1 ships" isn't a date.
2. **Budget, for both sides.** Your build cost is one question. The other side is that every user needs Claude Code access, which means a paid plan or API credits. Who pays for a fellow's Claude Code usage while gru interviews her? If the answer is "she does," that constraint belongs in the README before she clones anything.
