# Gru turn 11-v1-privacy-decisions

## Professor Bear typed

```
Both are real. Here's what the shipped code does, then my answers.

OQ-6: the skill's own documentation lists a GitHub Action as an acceptable scheduler, so the contradiction is in the shipped docs, not just in my answer. Option (a): drop GitHub Actions. Local launchd and cron only, and the skill docs get corrected. A reduced public keyword input, option (b), would be a different product with a different privacy boundary; not in this document.

OQ-7, the facts:
- Citations record BOTH the value and the path. A real report line reads: skill «Python» (skills.languages[1]) appears in posting content +1.0. Résumé titles and the résumé city («Boston») are quoted the same way.
- Outputs default to search/greenhouse-watch/, and search/ is gitignored except the fictional personas in search/examples/. So the values are written to disk, but to an untracked place.
- The JSON log and the Markdown report carry the same justification lines. There is no difference in rule between them today.

So the rule as actually enforced is "never commit résumé content," not "never write it down." The leak path isn't git; it's the student pasting a report into a course submission or a shared doc. My decision: citations keep the value, because the value is what makes a match checkable in seconds, which was the whole advantage over bookmarks. The protection is the boundary: outputs stay under the gitignored search/ folder, anything shown or committed must come from a persona run, and the report says so at the top. I'd rather state that boundary honestly than strip the value and weaken the one feature that justifies the tool.
```

## Gru replied (verbatim, unedited)

Both decided, and decided the way a decision should be made: you named what you're giving up and why. I'm logging them as **Decided**. Deciding them creates two obligations, and there's one hole in the boundary you just drew.

**OQ-6: Decided. Option (a).** Only launchd and cron, both local. GitHub Actions is removed as a supported scheduler. You also found that the contradiction is in the **shipped skill documentation**, not only in what you told me. So this is a correction to the baseline, not just a design choice, and it becomes a concrete task: fix the skill docs. Option (b) is out of scope as a different product, and that goes in /p2 as an explicit exclusion with that reason.

**OQ-7: Decided. Citations keep the value.** I'll write it into the document as you argued it: the value is what makes a match checkable in seconds, and that's the one advantage over bookmarks that justifies the tool. It's your call, and you've made it explicitly. Two obligations come with it:

1. **The written rule has to change, not just the enforcement.** The engine's rule as you described it says résumé content is never copied into a log. What the code actually enforces is **"never commit résumé content."** If this document records the narrower rule while the engine's rules file keeps the broader one, then the next student, TA, or agent who reads the rules will see the tool breaking them. And the tool will be following a rule nobody wrote down. Update the rule text in the engine to match what's enforced, and cite this decision.

2. **The remaining risk has to be recorded as risk, not as a solved problem.** You named the real leak path: a student pasting a report into a submission or a shared doc. A banner at the top of the report is the only thing guarding it, and a banner depends on the student reading it at the moment they paste. That's a weak control. Weak isn't the same as wrong. But it goes in the /p4 risk register as an accepted risk with a stated mitigation, so nobody later treats the banner as if it solves the problem.

**The hole: "outputs *default* to `search/greenhouse-watch/`."** A default can be changed. If the output location can be changed, the boundary is a default, not a guarantee. A student who writes output to their own project folder, or to `search/examples/` (the one tracked exception), gets real résumé values written somewhere git tracks, with nothing to stop them. It's a small decision, but it's the one your privacy boundary depends on:
- **(a)** Output stays under `search/`. The script refuses any other path.
- **(b)** Output can go anywhere, but the script refuses a tracked path when the input is the real `search/resume.json`.
- **(c)** Output can go anywhere, and this is accepted as a risk.

That's **OQ-8**. It doesn't block /v1, but it has to be answered before /v2, because whichever you pick belongs in a principle.

**Open Questions Log (updated):**
- **OQ-6: Decided (2026-09-24).** Local schedulers only. **Action:** fix the shipped skill docs. Option (b) goes to /p2 as out of scope.
- **OQ-7: Decided (2026-09-24).** Citations keep the value and the path. The boundary is: outputs go to gitignored `search/`, anything shared or committed comes from a persona run, and the report carries a banner. **Actions:** update the engine's rule text to "never commit résumé content"; add the paste-into-submission risk to /p4 as accepted, with the banner as mitigation.
- **OQ-8 (new): Can the output location be changed?** Options a, b, and c above. **Stakes:** the whole privacy boundary depends on outputs staying in the gitignored folder. Owner: you. Due: before /v2. Status: Open.

**7. What is the build scale?** For the corrective version specifically:
- **Who builds it?** You alone? You plus agents? Students as part of the assignment? The course says students are meant to read and change the scheme themselves. Does that make students *maintainers* of the scheme, and if so, is a student's edit to the scheme part of this document's scope?
- **Timeline.** Is there a date the corrective version has to be ready for, such as a class session or assignment release?
- **Budget.** You said the runtime costs nothing. Does anything in the corrective work cost money? For example, paid API calls while building, or rate limits on the three boards that would force a slower fetch pattern.
