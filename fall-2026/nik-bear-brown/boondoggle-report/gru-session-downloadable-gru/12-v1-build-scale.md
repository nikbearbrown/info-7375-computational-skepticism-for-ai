# Gru turn 12-v1-build-scale

## Professor Bear typed

```
1. OQ7: a named path. /gru share, which removes the sdd/ exclude line only after she confirms, and says what will now be visible to git. Everything in sdd/ is for review, including the gate-state file and the read logs: they're the evidence a reviewer needs to trust the document. The raw scan output stays excluded.
2. Accepted. Each confirmed gate records the Gru prompt's content hash, and a changed hash is announced at the next command.
3. A thin shim: the entry script is POSIX sh and hands off to Python immediately. No bash 4.
4. An existing sdd/ stops the install, and she picks another folder name, which the state file then records.

7.
Timeline: the first user is me, running it on this toolkit's own repository, as you suggested, before anyone else touches it. Students and fellows get it only after I've done that and confirmed v1. I'm not giving you a date I don't have; course dates live in Canvas.
Budget: the build costs me nothing beyond the Claude subscription I already have. For users, the course syllabus says Claude Code access through Northeastern is assumed for INFO 7375 students. Fellows and anyone else need their own Claude Code access, and yes, that goes in the README before they clone anything.
```

## Gru replied (verbatim, unedited)

All four of those are closed:

- **D11 (closes OQ7):** `/gru share` removes the `sdd/` exclude line only after she confirms, and it says what will become visible to git. Everything in `sdd/` is for review, including the gate-state file and the read logs. Raw scan output stays excluded.
- **D12:** Each confirmed gate records the Gru prompt's content hash. A changed hash is announced at the next command.
- **D13:** The entry script is a POSIX `sh` shim that hands off to Python immediately. No bash 4.
- **D14:** An existing `sdd/` stops the install. She picks another folder name, and the state file records it.

Once D11 commits the read logs and relayed claims to a team repository, one detail comes with it. `STUDENT (relayed: teammate)` has to stay a *role*, never a name. Otherwise "Priya thinks the export defaults to /out, and she's wrong" becomes permanent git history in a shared repo, and possibly a public one. This is a small rule for /v2. Accept or amend?

Question 7 is recorded:

> **Scale:** solo builder, with a prototype that already exists. **Budget:** no build cost beyond your existing Claude subscription. Users bring their own Claude Code access. INFO 7375 assumes Northeastern access per the syllabus, and fellows and everyone else must supply their own, stated in the README before they clone. **Timeline:** no date. Release is gated on you running v1 on this toolkit's own repository first.

I won't push for a date you don't have. A made-up date is worse than none. But a gate in place of a date only works if the gate is testable, and "I've confirmed v1" isn't yet. Two issues:

**The exit condition needs to be written down.** What has to be true after your own run for v1 to count as confirmed? A draft for you to cut:
- /v0 through /v4 completed on the toolkit repo, with section files written
- every CODE and DOC claim carries a pinned citation, and every question has a read log
- the gates survive a closed session and a fresh start the next day
- at least one real CONFLICT surfaced, resolved, and recorded with your reason
- `/gru share` shows exactly what becomes visible, and teammates' `git status` stays clean before you run it

Logging this as **OQ8**. It must close before /p1.

**Your own repo is the weakest test of your own problem.** Your user is a fellow in *someone else's* year-old code. On the toolkit's repo, you wrote the code a few weeks ago and you know where everything is, so the scan can miss and you'll quietly fill the gap. But you already have a better test case, and you told me about it in question 2. That's the tool where a pasted Gru ran today and you found **three contradictions by hand**:
- an output-folder default that doesn't exist
- a scheduler the privacy rule forbids
- a location rule that behaves differently

That's a fixture with a known answer. Run gru on that repo. If it surfaces all three as CONFLICTs without you pointing at them, the problem statement is tested. If it misses one, its read log should show you why. I'd make that a second dogfood run, and part of OQ8's exit condition. Accept or reject?

---

**Question 8: Name three systems this user already relies on, and for each one, the specific capability gru must integrate with or replace.**

Two are already in hand:
- **Claude Code.** gru depends on its skill discovery and file reading.
- **git.** gru depends on commit SHAs for citations and on `.git/info/exclude` for staying invisible.

Your user's workflow from question 3 gives two candidates for the third:
- **The Claude Project running a pasted Gru.** This is the thing gru *replaces*. Name exactly which capability it has to match or beat, beyond repo reading. For example, the Project keeps the whole interview in one visible conversation, while gru splits it across section files and sessions.
- **Slack**, as the channel teammates' memories arrive through. gru doesn't integrate with it and shouldn't. If you name it, the capability is "none, and on purpose," which belongs in /p2.

Pick the third system and name its capability.
