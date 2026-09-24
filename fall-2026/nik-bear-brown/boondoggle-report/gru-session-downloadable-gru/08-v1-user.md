# Gru turn 08-v1-user

## Professor Bear typed

```
Labels: accepted as you wrote them. DOC, CODE, STUDENT, GRU, and CONFLICT as a marker that becomes the next interview question.

On OQ6, where I lean, so you can hold me to it in /v2: a static read of the code relevant to each question, never executing it. Running a stranger's code on their laptop to answer a design question is a risk I don't want this tool taking.

3. One user, a composite, not a real person: a Humanitarians AI fellow, three weeks into a team project that someone else started, asked to add an export feature to the team's repository. The repo has a README written by the founder a year ago, a few scripts, some tests, and no design document.

Workflow today: she reads the README, skims a couple of scripts, asks a teammate on Slack what the export folder does, and pastes a summary of all that into a Claude Project running Gru. Gru interviews her, and the design document gets written from her summary.

Where the unchecked claim gets in: at the summary. She paraphrases the README and the teammate's memory; neither is checked against the code. Gru has no way to tell a stale README sentence from a fact. Who finds out, and when: a reviewer at the pull request, or the first user whose export lands somewhere the README said it wouldn't. By then the design document is already the argument for the wrong design.
```

## Gru replied (verbatim, unedited)

Question 3 is recorded, and it answers the limit I raised. Your user isn't working in her own three-week-old code. She's working in someone else's year-old code, with a stale README and a teammate's memory. So the docs-versus-code half of the problem applies to students too, not only to you. The composite is fine as long as it stays labelled as a composite. I'll mark it that way in the summary.

**Decisions logged:**
- **D2 (revised):** Labels are DOC, CODE, STUDENT and GRU. CONFLICT is a marker, and it becomes the next interview question.
- **OQ6, leaning:** A static read of the code relevant to each question. Never execute it. I'll hold you to this in /v2. When we get there, the principle will need its honest cost written down. Your third contradiction, the location rule that behaved differently, is a behavior question, and a static read can miss behavior. So the principle needs a companion rule: when a question depends on runtime behavior, Gru says a static read can't settle it and hands the check to the student as a human task. "Run the export and see where the file lands" is plausibility auditing, done by the human, on her own machine, by her own choice. That fits boondoggling.

Your user brings out two more issues.

**The teammate on Slack is a source with no label.** Right now, "the export folder defaults to /out, according to Priya" would be labelled STUDENT, which records the teammate's memory as if it were her own claim. It's one of the two unchecked claims in your workflow. The option I'd suggest is to allow STUDENT to carry a relay note, `STUDENT (relayed: teammate)`, so a CONFLICT between CODE and a relayed claim reads as what it is. This is a small amendment. Accept or reject.

**OQ1 just got sharper: she's installing into a shared repository she didn't start.** Installing gru writes `.claude/skills/gru*` and `sdd/` into the *team's* repo. Several questions follow:
- Does it show up in her teammates' `git status`?
- Does she commit it?
- Does her design document become a file in the team repo before anyone has reviewed it?
- If a teammate also runs gru, whose gate-state file wins?

For a solo student repo, none of this matters. For your user, it's the first thing a reviewer will ask about. I'm moving OQ1 up. It has to close in /v2 or /s3, not later.

---

**Question 4: What does this system give her that her current setup doesn't?**

Her current setup is a pasted Gru in a Claude Project, fed her summary. If your answer is "it combines Gru with repo access," name what is *new* in that combination, meaning something she couldn't get by pasting more of the code into the Project herself. That's the comparison a skeptical reviewer will make, and it's where "why not just paste the files?" has to be answered.
