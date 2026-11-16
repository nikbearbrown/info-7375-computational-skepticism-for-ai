Build an `ai-explainer` reel — Liam persona — on how to argue without cheating. Run from `books/`.

Home: `computational-skepticism-for-ai/youtube/claude-liam-arguing-in-good-faith/`
Channel: `claude-liam` · Kokoro `am_onyx` · register Teardown · 16:9

Audio is free and local. Generate it, do not gate it, do not ask.

## Source and what to do with it

The source is a six-card social-media carousel: two conduct cards (LISTEN, BE RESPECTFUL) and four fallacy cards (RED HERRING, ANECDOTAL EVIDENCE, AD HOMINEM, FALSE DILEMMA). The card grammar is icon → title → one-line definition → example.

**Keep the grammar. Do not copy the design.** The source cards are dark charcoal with white and red. That is another creator's visual identity and it violates BRAND-LOCKS. Rebuild every card in Claude tokens: cream `#FAF9F5` page, warm ink `#3D3929`, terracotta `#D97757` as the ONE accent, EB Garamond serif for the title, UI sans for the body. One terracotta moment per card — the accent lands on the icon detail or the operative word, never both.

## New Remotion component — `FallacyCard`

There is no component for this. Build one per `REMOTION-STANDARDS.md`: zod schema, demo twin, `Root.tsx`-only registration, `build_scene_index.py` regen, determinism contract, frame-time only.

```
fallacyCardSchema = z.object({
  kind:       z.enum(['fallacy','conduct']),
  title:      z.string(),
  definition: z.string(),
  examples:   z.array(z.string()).min(1).max(2),
  test:       z.string().optional(),   // the one-line check the viewer can run
  icon:       z.enum(['ear','fish','person','crown','heart','scale']),
})
```

Icons are drawn in-component as simple line glyphs — do not import the source artwork. `kind` drives the layout: `fallacy` cards get the terracotta accent on the icon, `conduct` cards get it on the rule line.

## The six cards — exact copy

Three of these are rewritten from the source. Reasons follow the table; the rewrites are not stylistic.

**1 — LISTEN** (`conduct`, icon `ear`)
- definition: `Waiting for someone to finish is not listening.`
- test: `Can you state their position in a form they would accept? If not, you have not heard it yet.`

**2 — GOOD FAITH** (`conduct`, icon `heart`) — *rewritten, see note A*
- definition: `Assume the other person is arguing in good faith until they show you otherwise.`
- test: `Grace is cheap. It also keeps the exchange alive long enough to get somewhere.`

**3 — RED HERRING** (`fallacy`, icon `fish`)
- definition: `Answering an argument by raising a different issue.`
- examples: `A claim about a specific policy answered with a claim about a different group's conduct.` / `A claim about conduct answered with a procedural objection.`
- test: `Does the reply engage the thing that was actually said?`

**4 — ANECDOTAL EVIDENCE** (`fallacy`, icon `person`) — *sharpened, see note B*
- definition: `Using one case to establish a rate.`
- examples: `"My grandfather smoked and lived to ninety."` / `"It has never happened to me, so it is not common."`
- test: `One case can refute "always" or "never". It cannot establish "how often".`

**5 — AD HOMINEM** (`fallacy`, icon `crown`) — *sharpened, see note C*
- definition: `Attacking the arguer instead of the argument. Latin: "against the man".`
- examples: `"You are not qualified, so your reading of the study is worthless."` / `Any insult offered in place of a reason.`
- test: `Would the argument still stand if a different person made it? If yes, the attack was not an answer.`

**6 — FALSE DILEMMA** (`fallacy`, icon `scale`)
- definition: `Two options presented as if they were the only two.`
- examples: `"Either we ship Friday or the quarter is lost."` / `Reducing a contested policy question to being for one group or against another.`
- test: `Name a third option. If one exists, the fork was built, not found.`

### Note A — why GOOD FAITH replaces BE RESPECTFUL

The source card reads: *"Comprehending complex layers of systemic racism and confronting one's own guilt in maintaining a racist status-quo takes a lot of emotional energy and courage."*

That is not a conduct rule. It presupposes that the person you are talking to holds guilt for maintaining a status quo — which is a contested conclusion of the very argument the cards claim to make fair. Assuming your conclusion inside a civility guideline is begging the question wearing etiquette's clothes. In a film about arguing honestly, shipping that card unexamined would be the defect the film exists to name.

The rewrite keeps what the card was reaching for — extend grace, assume effort — without smuggling a premise.

### Note B — the source's anecdote card is wrong as written

The source says anecdotal evidence is *"using a personal example to determine the entire argument."* But a single case is legitimate and often decisive **against a universal claim** — one counterexample kills "never" or "always". The fallacy is using an anecdote to establish a **frequency**. That distinction is the actual teaching, and the source loses it.

### Note C — ad hominem is not the same as challenging a source

Questioning whether a source is reliable is not ad hominem **when reliability is the thing at issue** — that is ordinary evidence assessment. The fallacy is substituting a fact about the speaker for a reason about the claim. Without that line, viewers learn to cry "ad hominem" at every credibility challenge, which is worse than not knowing the term.

## The examples are bidirectional on purpose

Every source example draws from one side of one political argument. That has two costs, and the second is the one that matters:

1. It reads as advocacy, so anyone who disagrees stops watching and learns nothing.
2. **It teaches the wrong lesson.** A fallacy is a content-neutral tool. Illustrated only by one side's opponents' errors, it becomes a weapon for spotting *their* mistakes — which is the exact use that makes fallacy vocabulary useless in real arguments.

So each fallacy card carries one everyday example that makes the mechanism unmistakable, and one contested-topic example phrased so it works whichever direction it is run. The film says this out loud in the verdict: the test of whether you understand a fallacy is whether you can catch yourself committing it.

## Beat structure — ai-explainer, ~16 beats

- **B00** cold open, `ClaudeComposerAsk`. Ask: how do you tell a bad argument from an argument you dislike?
- **B01** the frame: six cards, two about conduct, four about structure.
- **B02–B03** LISTEN and GOOD FAITH — one card beat each, card then the test.
- **B04–B11** the four fallacies — two beats each: card reveal, then the both-directions test enacted.
- **B12** the trap: fallacy names used as weapons. Naming a fallacy is not winning an argument.
- **B13** verdict, `ClaudeVerdictArtifact`.
- **B14** your turn, `ClaudeComposerAsk` — `greeting` is `Your turn.` and `command` is the full runnable prompt. Do not put the greeting in the command field.
- **B15** outro, `ClaudeTitleOutro`, title restated verbatim.

ILLUSTRATE LAW: the Claude UI appears only at B00 and B14. Every card beat is the `FallacyCard` component, not a screenshot.

## Build

1. Write `PLAN.md` and `FACTCHECK.md` first. Fact-check target: the definitions. Ad hominem, red herring, false dilemma and hasty generalisation have standard definitions in any logic text — cite one and match it. Where this film's definition is deliberately narrower than the source card's (notes B and C), record that as a considered choice with the reasoning, not as a correction of fact.
2. Build and register `FallacyCard`, with its demo twin, and verify determinism (same frame twice, identical output).
3. Write the beat sheet. Generate all audio with `runtime/scripts/generate_audio_kokoro.py`, voice `am_onyx`.
4. Render via `runtime/scripts/remotion_scenes.py <reel>`, foreground, `--concurrency=1`. Never hand-roll `npx remotion render`.
5. Compile. Run the `kerning` gate, write `TYPECHECK.md`. Card text is dense — sub-floor font sizes and wordy cards are the likely failure here.
6. QC by opening real frames and reading them.

## Do not

- Do not reproduce the source cards' colours, layout or artwork.
- Do not use `DoodleScene` or `DoodleChart` — DOODLE-BANNED LAW.
- Do not name any person, publication or organisation as an example of a fallacy. The examples are structural.
- Do not publish, stage to TOPOST, or upscale.
