# Gru turn 10-v1-category

## Professor Bear typed

```
Read log: accepted as written. It's the only way she can audit the scan.
Pinned citations: accepted. Commit SHA in a git repo, content hash otherwise, and drift flagged.
Gate-state file: you're right and I was wrong. It's MUST-BUILD. Without it the gates only last one session.

5. Your counter-draft, sharpened by one word: a repo-grounded design interviewer that writes a Software Design Document and a Boondoggle Score. What I'd tell a student: "gru is Gru that can read your repository. It still asks you everything; it just checks your answers against the code."
```

## Gru replied (verbatim, unedited)

All three are logged:
- **D5:** Every question writes a read log to its section file: files read, search terms used, files matched but not opened.
- **D6:** Citations are pinned to the commit SHA, or to a content hash if the folder isn't a git repo. Drift is flagged.
- **D7:** The gate-state file is MUST-BUILD. It sits with your two core reasons.

Question 5 is recorded:

> **Category:** a repo-grounded design interviewer that writes a Software Design Document and a Boondoggle Score.

The category is right. The sentence you'd say to a student has one phrase that teaches the wrong lesson, and she'll take it literally.

**"It just checks your answers against the code" makes the code the referee.** Go back to your own evidence. The docs listed a scheduler that the tool's privacy rule forbids. Which one was wrong? If the scheduler exists in the code, the *code* may be the bug, and the doc may describe what the founder intended. A CONFLICT tells you two sources disagree. It doesn't tell you which one is right. Deciding that is interpretive judgment, and it belongs to the student. If students learn that "gru checks you against the code," they'll give up the argument every time CODE disagrees with them, including the times they're right and the code has drifted from the intent.

Suggested rewrite:

> "gru is Gru that can read your repository. It still asks you everything. It just shows you where your answers, the docs, and the code disagree, and makes you decide."

This also becomes a /v2 principle candidate. **Gru never resolves a CONFLICT by defaulting to CODE. The student resolves it, and her resolution is recorded with a STUDENT label and her reason.** Accept, amend, or reject?

---

**Question 6: What is the deployment target, and why?**

The *where* is recorded: the student's own repository, installed by one command, running under Claude Code in her terminal. What I still need:

1. **Why the student's repo**, as opposed to running Claude Code inside the gru toolkit and pointing it at her repo from outside. You chose this in /v0. Name the reason, now that we know installing writes into a shared team repo, as OQ1 showed.
2. **The minimum environment.** "Standard-library scripts" in which language and at which minimum version? Is git required, or only recommended, given D6's content-hash fallback? And which operating systems? Your fellows won't all be on a Mac. If Windows isn't supported in v1, say so now, so that it goes into /p2 as a decision and not into a bug report.
