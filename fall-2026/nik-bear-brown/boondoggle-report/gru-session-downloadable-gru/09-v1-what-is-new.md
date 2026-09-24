# Gru turn 09-v1-what-is-new

## Professor Bear typed

```
Relay note: accepted. STUDENT (relayed: teammate).

4. Why not just paste the files? Two things she can't get that way:

First, she doesn't choose what gets read. Pasting files reproduces her blind spots: she pastes the README and the two scripts she already looked at, and the file that contradicts the README is the one she didn't think to paste. Gru reading the repo per question means the export question reads the code that actually writes the export, whether or not she knew it existed.

Second, every claim comes back checkable, and disagreements come back as questions. In a Project, "the export folder defaults to /out" is just a sentence in her summary. Here it arrives as STUDENT (relayed: teammate), next to CODE citing the file and line where the folder is set, and if they disagree, CONFLICT is the next thing Gru asks her. She can verify any line of the design document by opening the cited file.

Everything else (gates saved as files, the document living next to the code) is convenience. Those two are the reason to build it.
```

## Gru replied (verbatim, unedited)

Question 4 is recorded, and it holds up against "why not just paste the files?" I'm keeping it in your own terms:

1. **Gru, not the student, decides what gets read.** For each question it reads the code that is relevant to that question, whether or not she knew the code existed.
2. **Every claim comes back checkable.** Each one carries a source label and a citation, and any disagreement comes back as the next question.

Each of the two has a hidden assumption, and I'm naming them now. Before we get there, I disagree with one line in your answer.

**Assumption in the first claim: her blind spots get replaced by Claude's.** "Reads the code that actually writes the export" assumes the search finds it. Claude's search has its own blind spots. It greps for "export" and misses the function called `dump_bundle()` that does the writing. The difference is that *her* blind spots are at least hers. If Gru's search fails, she can't see that it failed, so "whether or not she knew it existed" can't be checked. The fix is to make what wasn't read visible. Each section file keeps a **read log** for each question: files read, search terms used, and files matched but not opened. That way she can plausibility-audit the scan itself: "It never looked in `scripts/`. That's where the exporter lives." Without the read log, claim 1 is something she has to take on faith. Accept or amend?

**Assumption in the second claim: file and line citations go stale.** "She can verify any line of the design document by opening the cited file" is true until a teammate pushes. After that, line 42 is something else, and a correct citation looks wrong. Pin every CODE and DOC citation to the commit SHA it was read at. For a folder that isn't a git repo, pin it to a content hash of the file. That also gives you drift detection for free: if the cited file has changed since the citation was made, Gru can say so. Accept or amend?

**Where I disagree: the gate-state file is not a convenience.** You called "gates saved as files" a convenience. In a Claude Code session, the conversation compacts, sessions end, and she comes back tomorrow in a fresh context. In a pasted Project, the conversation history held the gates. Here the file is the only thing that does. Without it, "never skip a gate" becomes "never skip a gate within one session," and the phase gates are Gru's teaching method. I'd put the gate-state file with your two reasons as a MUST-BUILD. The document living next to the code can stay a convenience. You can overrule this, but if you do, /v2 gets a documented exception, not a quiet downgrade.

---

**Question 5: What category of system is this? Name it plainly.**

/v0 gave me a draft category, "an interview-driven design-document generator." I now think "generator" is the wrong word. It suggests the tool produces the document from the repo, which D1 rules out. My counter-draft is **"a repo-grounded design interviewer that writes a Software Design Document."** Confirm it, sharpen it, or replace it. Use the plain name you'd give a student who asks what gru is.
