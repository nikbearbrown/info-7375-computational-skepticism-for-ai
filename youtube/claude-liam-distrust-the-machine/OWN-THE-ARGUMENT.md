# distrust-the-machine — stop narrating the essay, make the argument

You're right, and it's a third of the film: **12 of 33 beats** defer to a
document the viewer has never seen.

The break is early and it's the worst one. B00 introduces the student properly —
*"a student he's watched for ten years: fast, confident, correct on everything
the rubric rewards, who freezes a few years into a professional life."* Good.
Then B02, the first substantive beat, says:

> **"Picture the student the essay describes."**

The film just described him. Now it asks the viewer to picture a description they
don't have access to, in a document they haven't read. The clause does no work
and costs the whole beat's authority.

That's the pattern in all twelve: **the attribution clause is load-bearing for
nothing.** Delete it and every sentence gets stronger, because Teardown register
is supposed to make an argument and judge it — not report that somebody else made
one.

---

## The rule, stated properly

**Credit once, early. Own it after that.**

1. **B00 names whose argument this is** — provenance, so the film isn't silently
   annexing someone's work. This reel already does that correctly.
2. **After B00 the film makes the argument in its own voice.** Any later
   reference to the source is legitimate only when the source *itself* is the
   subject of that beat — its reception, its self-declared status, its
   invitation. Never when the film is reporting what it says.

Nine of the twelve fail test 2 outright. Three reference the source for a real
reason and just need reframing.

**Honest note on my own work:** I checked the two plans I wrote this week against
this. The Gardner Trap and the p-value reel both pass test 2 — the source doesn't
appear until the closing act, where it *is* the subject. But both **fail test 1**:
neither credits the source in B00 at all. This reel does the opposite. So this is
a symmetric law and I've been breaking the other half of it.

---

## The twelve, with paste-ready replacements

Audio-only edits. The scenes don't change — regenerate these mp3s, re-conform,
recompile. Every replacement is **shorter**, so conform trims (lossless) rather
than stretches.

### Strip the clause — 8 beats

**B02**
> Picture the student. Fast retrieval, confident answers, perfect formatting — everything the rubric rewards, on demand. Then, two or three years into a career, the freeze. The desk is quiet. The tools all work. And nothing on it says what the problem is.

**B10**
> Here's the picture that reframes it. The intelligent response to a forklift is not to practice lifting heavier objects. It's to operate it, maintain it, know what it can and cannot lift — and above all, develop the judgment to know what needs lifting in the first place.

**B14**
> So — seven tiers, and they're labelled version one, a draft. Pattern and association. Embodied. Social. Metacognitive. Causal. Collective. Existential. One thing to say clearly before the diagram: pattern matching is genuine intelligence — just not sufficient intelligence. Now watch what the comparison shows: machine strength across the seven tiers, and where the school day spends its time. The shape is the argument.

**B15**
> And look at what goes unscaffolded — tiers four, five, seven. Plausibility auditing. Problem formulation. Causal reasoning. Interpretive judgment. Wisdom. The refusal matters here: these are not soft skills. They're what separates an AI-amplified human from an AI-confused one. And they are not on the test.

**B16**
> Which lands the hardest sentence in the whole argument: where machines are strongest, training humans to compete directly is now malpractice. Not suboptimal. Malpractice. The strong word is the point — triage means someone finally says which injuries get treated first.

**B19**
> And here's the sharpest reframe of the machine itself: an LLM may be a lossy compression of collective human intelligence — our own writing reflected back. The collective axis is what that adds — not just lossy writing, but missing the friction between writers that shaped the writing. Centuries of what we wrote, argued, got right and wrong, compressed with extraordinary fidelity. Impressive and limited for exactly the same reason.

**B23**
> The result reads like an audit you can't unsee: week after week of graded hours landing on tier one — retrieval, drill, format — with problem formulation appearing exactly nowhere as a graded act. That's one syllabus. The claim is that it's nearly every syllabus. Run yours.

**B12** — act card, `the taxonomy` is fine (the film has built it by now). **No change.**

### Reframe — 3 beats where the source genuinely is the subject

**B13a** — this is about *reception*. An objection was raised against this argument in public. That needs the argument to have been published; it does not need the viewer to have read it.
> One objection this film shouldn't cut — because cutting it would make a video about intellectual honesty that suppresses its sharpest objection. This argument drew a response from someone who knows Gardner personally, who says Gardner himself regretted Multiple Intelligences being taken as an ontology to design curricula by. That's a direct shot at what this taxonomy is doing. The answer: Gardner explicitly clarified that M I describes cognitive capacities — not curriculum design templates. This taxonomy's question is different: not which activities map to which intelligences, but which human capacities machines now make redundant. That reframe changes what you're sorting by.

**B14a** — lead with the limit, not the citation. Put the companion-post credit **on screen**, small, not in the voice.
> One honest limit this film shouldn't pass over. Name it, teach it, measure it — that's the three-stage sequence educational reform keeps failing to complete. Stage one is done here: the taxonomy has a name and a structure. Stage two and three — how to teach for these tiers, and how to measure whether it worked — are unspecified. That's also the standing empirical objection to Gardner's original framework, and it's worn openly: version one. A taxonomy without measurement is a vocabulary, not yet a science.
>
> *On-screen citation only:* `Companion post — "Name it → Teach it → Measure it," theorist.ai`

**B22** — the film accepts a published invitation. Real move; drop the "the essay closes by."
> The taxonomy is published as a draft, and pushback is the point. So we took it up on that. Watch: we asked Claude to triage a syllabus against the seven tiers.

**B26** — same.
> Your turn — and this one takes the taxonomy up on its own request: push back. Here's the prompt: here is a seven-tier triage taxonomy of intelligences — pattern, embodied, social, metacognitive, causal, collective, wisdom — built to ask which intelligences machines endanger and which education neglects. First, attack it: name a human intelligence it misses, a tier you'd reorder, or a case where the machine-strength overlay is wrong. Second, apply it: triage a syllabus or curriculum I give you, tier by graded hour. Third, propose the single highest-leverage change that moves graded time from tier one to tiers four, five, or seven. The taxonomy gets better with more minds on it — be one of them.

---

## Fix prompt

```
Rewrite narration only in
computational-skepticism-for-ai/youtube/claude-liam-distrust-the-machine.

PROBLEM: 12 of 33 beats defer to "the essay" — a document the viewer has never
read. The film reports an argument instead of making it. Worst case is B02, the
first substantive beat: "Picture the student the essay describes" — immediately
after B00 has already described him.

RULE: credit once, early; own it after that. B00 already names the source
correctly and does not change. After B00 the film makes the argument in its own
voice. A later reference to the source is legitimate ONLY when the source itself
is the subject of that beat — its reception, its self-declared draft status, its
invitation to attack. Never when the film is reporting what it says.

Apply the replacement narration in OWN-THE-ARGUMENT.md in this folder, verbatim:
  strip the clause  — B02, B10, B14, B15, B16, B19, B23
  reframe           — B13a, B14a, B22, B26
  no change         — B12 (act card; "the taxonomy" is earned by then)

B14a also moves its companion-post citation OUT of the narration and onto the
screen as a small serif credit line. Add that to the beat's show block.

Then sweep the remaining 21 beats for the same tic — "the author", "the piece",
"the argument goes", "he argues" — and report anything you find before changing
it.

THIS IS AUDIO-ONLY. No Manim or Remotion scene changes. Every replacement is
SHORTER than the original, so conform trims rather than stretches:
  1. regenerate mp3s for the 11 changed beats (Kokoro am_onyx, free)
  2. write measured durations back to actual_duration_s
  3. re-align for the word clock — the show blocks key reveals to spoken phrases
     and several of those phrases moved
  4. recompile; only changed slots rebuild
  5. report the new total runtime (currently 527.8s; expect ~510-515s)

Do not re-render any scene. Do not publish.
```

---

## Worth promoting to the skill

This is the **same law** as the Simon's Ant opening problem, seen from the other
side. There the film assumed the viewer knew who Simon was. Here it assumes the
viewer read the essay. Both are the reel leaning on context the viewer doesn't
have.

Proposed addition to `ai-explainer` SKILL.md, alongside EXECUTIVE-SUMMARY LAW:

> **STANDALONE-ARGUMENT LAW.** The reel makes its source's argument, it does not
> report it. Credit the source once, in the cold open. After that every claim is
> stated in the film's own voice and stands on evidence shown on screen. A later
> reference to the source is legal only where the source *is* the subject — its
> reception, its stated limits, its invitation. Phrases like "the essay
> describes", "the author argues", "the piece claims" in a body beat are a
> defect: the viewer has not read it, and the film is asking them to take a
> document's word for something it could simply show. Corollary, from the other
> direction: a named person or work the argument depends on must be established
> before it is leaned on — the viewer cannot be assumed to know who they are.
