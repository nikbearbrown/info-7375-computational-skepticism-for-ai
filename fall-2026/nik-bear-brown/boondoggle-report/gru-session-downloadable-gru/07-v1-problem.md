# Gru turn 07-v1-problem

## Professor Bear typed

```
A student designing a change to a real codebase can only give a pasted Gru what they remember or what the repository's docs claim, so the design document gets built on unchecked claims about the student's own code, and the places where the docs and the code disagree, which are exactly where the design risk lives, surface late or not at all.

Evidence from today, on a different project: I ran a pasted Gru on one of my own tools, and three of its hardest questions turned on facts I had to go and read out of the code by hand. The docs said an output folder had a default; the code had none. The docs listed a scheduler that the tool's own privacy rule forbids. And a location rule behaved differently from how I'd described it. Each time, what I'd told Gru first was the docs' version.
```

## Gru replied (verbatim, unedited)

Question 2 is accepted. This is a real problem statement: it names a failure, not a missing tool. The evidence helps too. You gave me three specific contradictions, and each was caught only because you went back and read the code by hand. Recorded as:

> A student designing a change to a real codebase can only give Gru what they remember or what the repository's docs claim. So the design is built on unchecked claims, and the places where docs and code disagree, which are where the design risk is, surface late or not at all.

Your answer has two consequences for the design, and one limit on the evidence. I'm naming all three before we go further.

**Consequence 1: the scan you described in /v0 would repeat your own failure.** You listed what gru-scan reads: README, AGENTS.md or CLAUDE.md, package manifests, tests, CI, existing skills, TODO markers, recent commits. Nearly all of that is either docs or metadata about the code. None of your three contradictions would show up there:
- A default value that doesn't exist is found only in the code that reads the folder path.
- A scheduler the privacy rule forbids needs the docs and the rule read side by side.
- A location rule that behaves differently is about behavior. Reading it statically might catch it. Running it certainly would.

If gru-scan reads only what the docs say, it is a faster way to feed Gru the docs' version of events. That is exactly the problem you just described. So the scan has to read source code, and /v2 has to say how deep it goes: file tree only, a static read of the relevant code, or actually running something. I'm logging this as OQ6. It is the most important open question so far.

**Consequence 2: the provenance labels hide the exact distinction your problem is about.** D2 has three labels: REPO, STUDENT, GRU. Your problem statement says the risk lives where the docs and the code disagree. A single REPO label records "the repo says X" without saying *which part* of the repo. Proposed revision:

- **DOC**: read from documentation (README, AGENTS.md, comments that describe intent)
- **CODE**: read from source, configuration, or tests
- **STUDENT**: said by the student
- **GRU**: Gru's judgment
- **CONFLICT**: a marker, not a source. It is raised whenever two of the above disagree about the same fact, and it is shown to the student as an interview question before any section is written.

With CONFLICT in place, "surfaces late or not at all" becomes "surfaces as the next question." Accept, amend, or reject?

**Limit: the evidence comes from you, not from a student.** It validates the docs-versus-code half of the problem strongly. It says nothing yet about the "only what they remember" half, which is the student's usual situation. A student repo might be three weeks old with a one-line README. There may be no docs to contradict, and the student's memory is the only other source. The tool may still help there, but in a different way: it would check the student against the code, not the docs against the code. Question 3 is where we find out which user this is really for.

---

**Question 3: Who has this problem? Describe one specific user.**

I want one person, not "INFO 7375 students." Answer three things:
- What are they changing, and in what kind of codebase: their own, a team project, or an inherited open-source repo?
- What is their workflow today, from "I have a change to make" to "I have a design document"?
- At what point in that workflow does the unchecked claim get into the document, and when does someone find out?
