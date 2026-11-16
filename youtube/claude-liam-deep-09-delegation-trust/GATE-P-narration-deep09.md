# GATE P — Narration Review · deep-09 "It Runs Beautifully. Nobody's Watching."

**Reel:** `claude-liam-deep-09-delegation-trust` · Chapter 9, *Computational Skepticism for AI*
**Voice at GATE P:** Kokoro Liam `am_onyx` (free default) · Register: Teardown · Liam in for Bear
**Estimated runtime:** ~9m26s (36 beats / 30 body) — *estimate only; measured audio is the clock*
**Gate status:** PLAN ✅ approved (default) · FACTCHECK ✅ pass · **GATE P — this is the review surface. No audio generated yet.**

> Read this as the spoken track. If a line reads wrong out loud, flag the beat id and I'll revise, then we generate audio. Nothing below is datable — Gru/tool names, model/vendor strings, and the overtrust-prevalence claim were all stripped or hedged per DOUBLE-CHECK + Gate F.

---

## COLD OPEN

**B00** · *bookend · ClaudeComposerAsk* — 28s
Jambo — this is Liam, in for Bear. Here's the whole chapter in one experiment. Two teams build the same loan-scoring pipeline — same data, same model, same fairness metrics. Diff the code, you can't tell them apart. Both ship. Then the committee asks each team one question: who is responsible if a decision is challenged? One team answers in writing. The other goes quiet. Nothing in the code differed. One thing did. So what was the single variable that decided the rollout?

---

## ACT I — The Two Teams

**A1C** · *card* — 6s
Act one. A controlled experiment that ran itself — two teams, one pipeline, one difference.

**A1R** · *Remotion · divergence* — 13s
Same data. Same model. Same fairness metrics. Same monitoring. On paper, the same system. The only difference lived in the documentation — one sentence versus a page. That page is the whole story.

**A1M** · *Manim · responsibility trace* — 16s
The committee asks one question: who is responsible? Follow team one's pipeline. The AI produced the score. The officer reviews. But review means what — checked how, against what criteria? The accountability arrow runs to a word nobody defined, and dead-ends. Team two's arrow lands on a named human.

**A1V** · *vox · committee room* — 15s
Picture the room. The committee waits. The team that can't answer isn't incompetent — their pipeline runs, loans get scored, decisions get made. They simply cannot say, in writing, what their own system does. So the rollout is tabled. Not for a bad model. For a missing sentence.

---

## ACT II — Contract, Not Partition

**A2C** · *card* — 6s
Act two. The load-bearing idea — and everything else hangs off it.

**A2K** · *ask micro-beat* — 3s
*(silent — composer types the Manim request)*

**A2R** · *Remotion · divergence* — 16s
The mistake almost everyone makes is to treat delegation as a partition — the AI does this slice, I do that slice, like cutting a pie. A partition only names who touches what. A contract has boundaries, obligations, and a clause for when a party fails to deliver. Delegation is the contract.

**A2M** · *Manim · testable vs untestable* — 17s
Here's the test. The AI produces a reasonable result, the human reviews it. Hand that to five officers and you get five behaviors, all called reviewing — no fact of the matter about whether it worked. Now: score zero to one; accept, re-score, or override with one of four codes. A stranger reads the log and knows exactly what happened.

**A2V** · *vox · circled procedure doc* — 16s
This is the unglamorous part, and the unglamour is the point. Write the condition. Circle every interpretive word — reasonable, review, appropriate. Replace each with a criterion a stranger could check. Nobody gets promoted for this. It's the entire difference between a supervised pipeline and one that only looks supervised.

**A2R2** · *Remotion · ClaudeWindow artifact* — 15s
One honest wrinkle. Some conditions are testable only by a qualified reviewer — verify the citation is accurate in the domain-specific sense. That's real, but narrower than anyone-can-check. The line isn't a clean binary; it's graded. The standard still holds — honest documentation just says which tier a handoff sits in.

---

## ACT III — Five Capacities, Five Artifacts

**A3R** · *Remotion · ClaudeWindow artifact (act-opener spark-line)* — 17s
Act three. Five supervisory capacities — and here's the reframe that stings: none is a trait you have. Each is an operational form the pipeline either contains or does not. Plausibility auditing is a checklist. Problem formulation is a written spec. If the artifact is missing, the capacity did not happen.

**A3V** · *vox · lone supervisor at monitors* — 16s
Engineers hear supervisory capacity and reach for words like judgment and experience — words that describe a person, not a task. But watch what's actually happening. Interpretive judgment isn't a feeling in the reviewer's chest. It's a line in the audit trail: the decision was X because the score was Y, in this context, meaning Z.

**A3R2** · *Remotion · ClaudeWindow artifact* — 16s
So the map carries eight items per step. Name, owner, inputs, outputs — items one through four, standard engineering. Then handoff condition, failure mode, verification, audit trail — items five through eight. The first four any competent team writes. The last four are the supervisory additions almost everyone omits.

**A3M** · *Manim · broken vs unsupervised* — 17s
And here's the trap. A pipeline missing items one to four is broken — it won't run, so the gap announces itself. A pipeline missing five to eight is unsupervised — and it runs beautifully. The failure that costs you is the one that never stops the pipeline. It surfaces downstream, usually found by the person it harmed.

---

## ACT IV — The Boondoggle Questions

**A4C** · *card* — 6s
Act four. Before the map — which sub-tasks should the AI touch at all? Five questions.

**A4R** · *Remotion · ChipGrid* — 17s
Five questions, asked of every sub-task. Verification cost — can a human check it cheaply, or does checking cost as much as doing it. Stakes — the price of being wrong. Distribution match — in-distribution, or a tail case. Reversibility — can the action be undone. Audit trail — does it leave a reviewable trace.

**A4M** · *Manim · reversibility gate* — 16s
Reversibility is the sharpest one. A reversible action — a draft you can discard — tolerates a high error rate. An irreversible one — a delete, a send, a wire transfer — should sit behind an explicit human-approval gate, almost without exception. Not a vote the AI can win. A gate a human has to open.

**A4V** · *vox · approval-stamp desk* — 16s
And verification cost isn't a character test — it's economics acting on attention. When checking an output costs as much as producing it, the cost structure itself quietly pushes the supervisor toward accepting rather than checking. Expensive-to-verify tasks are dangerous precisely because the pressure to wave them through is structural.

**A4M2** · *Manim · three buckets* — 17s
The five answers sort each sub-task into three buckets — appropriate for the AI, human-only, or hybrid with verification at a named handoff. But the output isn't the bucket. It's the written justification for the choice. And a caveat I owe you: this score is one engineer's heuristic, not a validated instrument. The questions matter more than any number.

---

## ACT V — The Paper Summarizer

**A5C** · *card* — 6s
Act five. Enough abstraction. Watch the map fall out of one real pipeline.

**A5R** · *Remotion · ClaudeWindow artifact* — 17s
A research-paper summarizer with citation verification. Six steps. The AI owns parsing, extraction, formatting — the pattern work. A human owns the taxonomy, the plausibility audit, and the final sign-off — the judgment work. Three of six steps are irreducibly human. And notice: the human steps are the ones that look like review, not work.

**A5M** · *Manim · two riskiest handoffs* — 17s
The two highest-risk handoffs are both AI-to-human. Step three into four: the danger is the researcher waves through a high-confidence extraction and a domain-critical qualification vanishes. Step five into six: treating a sign-off as proofreading instead of interpretation — and a misleading framing ships.

### Vox run R1 — the dropped qualifier *(one continuous camera move; hard-cut in and out)*

**A5V1** · *vox · 1/3 · the fluent claim* — 12s
Watch it happen at reading speed. Step three hands up a clean, confident summary. The claim reads: this method outperformed the baselines. Fluent. Specific. It looks exactly right — which is the whole problem.

**A5V2** · *vox · 2/3 · the dropped qualifier* — 14s
Now open the source. The paper didn't say outperformed the baselines. It said outperformed them on the training set only. Five words the model dropped — and with them, the entire meaning of the result. The proxy read fluent. The truth had a qualifier.

**A5V3** · *vox · 3/3 · the human catch* — 13s
Step four is the human catch. Open the PDF, verify no qualification was dropped, spot-check one in five high-confidence entries, then sign. That is not proofreading. It is the step where the pipeline earns the word supervised — or quietly loses it.

**A5R2** · *Remotion · ClaudeWindow artifact* — 17s
Notice what the score never contains: reasonable, human reviews, check for accuracy. Every human action names what's checked, against what, at what granularity. Looks good is not a handoff condition — tattoo that somewhere. And the score flags one gap: no step does executive integration. Fine for one user. The moment a second person relies on the output, a step is missing.

---

## ACT VI — Trust You Can Watch

**A6M** · *Manim · calibration axis (act-opener)* — 17s
Act six. There is a property you can monitor in deployment, and most deployments don't. Calibrated trust: the supervisor's reliance should match the AI's actual reliability on this kind of case. Too little reliance is undertrust — you lose the value. Too much is overtrust — you accept what you shouldn't. Only the middle is calibration.

**A6R** · *Remotion · attrition* — 18s
Overtrust is the quiet one. It's automation complacency — monitoring degrades under a low rate of signals — documented at length in the human-automation literature. It produces no immediate flags. Just uncaught errors, surfacing later, often found by the affected user. Whether it's the most common failure in AI today, I hold as a working hypothesis, not a finding.

**A6K** · *ask micro-beat* — 3s
*(silent — composer types the Manim arithmetic request)*

**A6M2** · *Manim · calibration as arithmetic (equation tangent)* — 17s
Here's calibration as arithmetic — an illustrative case. Two hundred decisions: the human overrode fourteen, a seven percent override rate. But a forty-case audit finds six real errors — about fifteen percent. The human is overriding half as often as the AI is wrong. That gap is overtrust, and it's sitting right there in the audit trail.

**A6V** · *vox · unwatched dashboard* — 15s
And this is the field's most closable failure. The disposition data — confirmed, corrected, unverifiable — is already in the log. Nobody has to build anything. Someone just has to look. The gap isn't between having the data and collecting it. It's between having it and reading it.

**A6R2** · *Remotion · ClaudeWindow artifact* — 17s
Which is what the AI Use Disclosure is for — a supervisory log, if it's four things: granular per step, honest about corrections, time-stamped, tied to evidence. When the disclosure records that step three dropped a qualifier and a human caught it — that's not embarrassing. That's the data proving the pipeline works.

---

## CLOSING BLOCK (your-turn standard)

**BVDT** · *verdict · ClaudeVerdictArtifact* — 42s (0.5s lead silence)
Let's recap with Claude. The verdict on delegation. A delegation is not a partition of labor — it's a contract, and its load-bearing clause is the handoff condition, which has exactly one property: it has to be testable, even if only by a qualified reviewer. The five supervisory capacities aren't traits — they're jobs with artifacts, and if the artifact is missing, the capacity didn't happen. The map's last four items separate a supervised pipeline from one that merely looks supervised — because the failure that costs you is the one that never stops the pipeline. And trust calibration is a property you can watch in the audit trail — the field's most closable gap is simply reading the data you already have.

**BHTF** · *your turn · ClaudeComposerAsk (Liam reads the prompt)* — 44s
Your turn. Here's the prompt — paste it into Claude. It reads: Take one AI pipeline you actually run. First, before you fix anything, reconstruct its delegation map as it is — for each step, the owner, the inputs, the outputs, and be honest about whether the handoff is vague or testable. Then rewrite it: give every step a handoff condition a stranger could check on a sample case, and name what happens when it fails. End quote. That's the chapter, compressed. The point isn't the tidy final map. It's the reconstruction — because writing down what your pipeline actually does, as opposed to what you remember it doing, is usually where you find the step nobody was supervising. Run it on something you rely on.

**BOUT** · *outro · ClaudeTitleOutro* — 8s
It Runs Beautifully. Nobody's Watching. Delegation and trust, from Computational Skepticism for AI. Liam, in for Bear.

---

*After you approve this narration, the next step is audio generation (Kokoro, free) → audio-lock → SHOPPING.md (Gate D2) → slate previz (Gate D1). Those run through the `brutalist-art` toolkit on your Mac.*
