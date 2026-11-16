# SOURCE.md — the primary source, on disk for Gate F

Provenance: research document pasted by Bear into the Cowork session,
2026-07-21. Inline `[cite N]` markers preserve the source's own citation
anchors (the original used indexed cite tags). FACTCHECK.md rows verify
against this document and the primary sources it names. Note the source's
own closing caveat about a wrong-attribution variant of its court case —
that caveat is load-bearing and became beat B23.

---

# The Fluency Trap: Why Polish Stopped Meaning What It Used to Mean

## The Core Problem

For as long as writing has been graded, hired for, or trusted, people have
used **how something is written** as a proxy for **how much thought went
into it.** A clean, well-structured, grammatically confident essay signaled
a competent mind behind it. A halting, awkward one signaled the opposite.
This was never a perfectly reliable signal — but it was a *cheap and
usually-correct* one, and humans lean on cheap, usually-correct heuristics
constantly, because checking substance directly is expensive and checking
polish is nearly free.

AI breaks the "usually-correct" half of that deal without breaking the
"cheap" half. A model can now produce publication-grade fluency — correct
grammar, varied sentence structure, confident tone, plausible structure —
for a claim that is unverified, an essay whose argument is empty, or a
report whose numbers are invented. The heuristic that used to work (fluency
correlates with effort and competence) still *feels* the same to the
reader, but the thing it used to track has been severed from the thing
producing it.

This isn't a new problem in kind — it's a very old problem (rhetoric versus
substance is literally the founding argument of Western philosophy, going
back to Socrates versus the Sophists) — but it is new in *scale and
asymmetry*. What used to require real skill, or at minimum real effort, to
fake is now available at the cost of a prompt. The interesting question
isn't "is fluency bias real" (it's well-documented) — it's **why it worked
well enough to survive as a heuristic for centuries, and specifically what
AI does to break the mechanism that made it work.**

## Part 1 — The Psychology: Fluency Was Never About the Content, It Was About the Feeling of Ease

Decades of cognitive psychology research on **processing fluency** show
that people systematically mistake the subjective *ease* of processing
something for evidence about its *truth, quality, or trustworthiness* —
independent of the actual content. This isn't a minor bias; it shows up
across domains: [cite 33-1] the ease of processing acts as a heuristic cue
that individuals unconsciously use to assess truthfulness, safety,
familiarity, and value, and trust — a complex judgment that could be made
through careful review of evidence — often gets made heuristically through
this cognitive fluency instead. The mechanism is genuinely subconscious:
[cite 33-1] once someone becomes aware that their sense of ease comes from
something irrelevant to the content, like a comfortable room, the fluency
cue gets discounted — the power of the effect lies specifically in its
invisibility.

The specific, well-replicated version relevant here is the **halo effect of
readability**: readers who find a piece of writing easy to read infer the
author is more intelligent, more careful, more credible — even when the
actual argument is unchanged. A classic demonstration used essay quality
directly: [cite 26-1] undergraduates rated the same set of essays, some
well-written and some poorly written, and researchers found the writing
quality itself shifted judgments of the author's competence, on top of
other surface cues like appearance. The heuristic isn't stupid — in a world
where producing fluent writing reliably required real underlying
competence, "smooth prose implies a competent author" was a good bet. The
bet only fails when the cost of producing smooth prose stops tracking
competence.

**Implementation note:** this is the mechanism you're fighting when you
design any rubric, and it's worth naming explicitly in grading criteria and
hiring rubrics rather than assuming graders will self-correct — [cite 33-1]
the fluency effect only weakens once its influence is made visible to the
person experiencing it — which means the fix is structural (blind grading,
separated rubric lines for substance vs. mechanics) rather than just
"graders should try harder to be objective."

## Part 2 — The Economics: Why Fluency Used to Be an Honest Signal

The psychology explains why people *fall for* fluency. Economics explains
why, historically, it was mostly *rational* to fall for it. **Signaling
theory** (Spence, 1973) formalizes when an observable, low-information-cost
signal can honestly reveal something the observer can't check directly. The
key condition: [cite 44-1] the signal must be costly, otherwise everyone
would use it and it would lose its value, and the cost of acquiring it must
be inversely related to the underlying quality being signaled — high-ability
people find it cheaper to produce the signal than low-ability people do.
That cost-asymmetry is what creates a stable **separating equilibrium**:
[cite 49-1] if signaling costs were uniform across people of different
ability, everyone would invest in the signal to the same degree, and it
would stop distinguishing anyone.

Fluent prose was, for most of history, a classic Spence-style costly
signal. Writing clearly and correctly required either natural ability,
extensive practice, or real effort spent on a specific piece of work — all
three of which correlate (imperfectly, but genuinely) with the underlying
thing employers, teachers, and readers actually cared about: careful
thought, competence, diligence. This is exactly the logic financial
economists use to explain why **annual report readability functions as a
market signal**: [cite 43-1] clearer, more positively-toned corporate
disclosures act as signals of managerial competence and organizational
strength — and firms with genuinely strong underlying performance have less
need to obscure their numbers behind dense, evasive prose.

**What AI does to this equilibrium, in one sentence:** it collapses the
cost of producing the signal toward zero for everyone, regardless of the
underlying quality being signaled, which — per Spence's own framework — is
precisely the condition under which a signal *stops functioning as a signal
at all.* This is worth sitting with, because it's not a claim about AI
being "bad writing" — the writing is often genuinely good. It's a
structural claim: **the signal has been decoupled from the thing it used to
indicate, for reasons that have nothing to do with how good the prose
reads.**

**This has now been measured directly, not just theorized.** A 2025 study
using data from Freelancer.com — a major digital labor platform — tracked
exactly this collapse in real hiring data. Before LLMs became widely
available, employers paid a real premium for customized, tailored
proposals: workers with a one-standard-deviation-higher customization
signal got hired at the same rate as workers who cut their bid by $26,
meaning employers were treating tailored writing as a genuine, valuable
signal of worker quality and were willing to pay for it. After LLM adoption
made that customization nearly free to produce, the researchers ran a
structural model of the new equilibrium and found the market becomes
measurably less meritocratic: workers in the top quintile of underlying
ability get hired 19% less often than in the pre-LLM equilibrium, while
workers in the bottom quintile get hired 14% more often — the exact
"pooling equilibrium" outcome Spence's framework predicts once a costly
signal goes cheap. This is the cleanest available real-world confirmation
that fluency's collapse as a signal isn't a hypothetical risk; it's already
reshaping who gets hired, in a direction that penalizes genuine ability
specifically.

## Part 3 — The Evidence: This Is Already Measurably Happening

This isn't speculative. Recent studies show the fluency-competence link
breaking down concretely, in exactly the domains where it used to be most
trusted:

- **Teachers and expert readers can't reliably tell the difference.**
  [cite 41-1] In two studies, neither novice nor experienced teachers could
  reliably differentiate between AI-generated and student-written texts,
  though experienced teachers did slightly better — and both groups were
  overconfident in their judgments. A separate systematic review across
  multiple domains found similarly poor discrimination: [cite 38-1]
  participants trying to distinguish AI-generated from human-written
  student essays performed at an average classification accuracy of 49.9%,
  essentially the level of random guessing — and in a medical school
  admissions context, [cite 38-1] committee readers identified true
  authorship of personal statements with only 56% accuracy despite showing
  very high interrater agreement with each other — meaning the graders
  agreed confidently with each other while being collectively wrong at
  near-chance rates.
- **When AI submissions do get past detection, they often score *higher*,
  not just "pass."** [cite 41-1] In a study where researchers submitted
  entirely AI-generated assignments into a real exam system across five
  psychology modules, 94% went undetected by expert examiners, and the
  grades given to the AI submissions were significantly higher than those
  achieved by real students.
- **AI-detection tools have a real cost, and it falls disproportionately on
  people whose *natural* writing is already atypical.** [cite 34-1] A
  Stanford study found mainstream AI detectors flagged 61.3% of TOEFL
  essays written by non-native English speakers as AI-generated — the
  detectors are picking up on the same "less varied, more formulaic"
  signal that both non-native writers and AI models produce, which means
  the fluency-bias problem and its detection-side backlash are actually the
  same underlying failure mode wearing two faces.
- **Automated graders built to fix this have their own version of the same
  bias.** Current AI essay-grading tools show [cite 36-1] 65–80% agreement
  with human graders on holistic scoring, but with a documented
  "proportional bias" — lenient scoring on weak essays and harsh scoring on
  strong, unconventional ones — which suggests the substitute grader
  inherited a version of the same halo-effect problem rather than actually
  solving it.
- **This has already produced real lawsuits, not just bad grades.**
  Turnitin's detector [cite 54-1] claims a 98% confidence rating and a
  false positive rate of less than one percent, but independent evidence
  tells a different story — a 2023 analysis found no available AI detection
  tool exceeded 80% accuracy in controlled testing. That gap produced
  concrete harm: an autistic student at Adelphi University had a World
  Civilizations essay flagged as 100% AI-generated by Turnitin while
  [cite 61-1] two other detectors, Grammarly and ZeroGPT, both labeled the
  same essay human-written; the university upheld the violation anyway, and
  a federal judge ruled against the school in early 2026. [cite 54-1]
  Several universities — Vanderbilt, Michigan State, and Northwestern —
  paused or opted out of Turnitin's AI detection tool entirely after their
  own testing raised false-positive concerns, and one Australian university
  [cite 54-1] recorded nearly 6,000 alleged academic-misconduct cases in a
  single year, roughly 90% AI-related, with a substantial share dismissed
  after investigation — before abandoning the tool.

**A note on that last case, since it's directly relevant to everything in
this document:** some accounts of the Adelphi case in circulation online
attribute it to a different student name and a different university and
year than the court record shows. That's worth flagging explicitly rather
than quietly correcting, because it's a live, small-scale example of
exactly the fluency/citation-cascade problem this document is about — a
detail that sounds precise and authoritative gets picked up and reproduced
with a plausible-sounding but wrong attribution, and the wrong version is
just as fluent as the right one. The verifiable version, per court
reporting, is Orion Newby v. Adelphi University, decided February 2026.

**Implementation note:** the TOEFL finding is the sharpest practical
warning in this whole area. Any pipeline built to catch "AI polish masking
empty substance" needs to be tested specifically against non-native,
neurodivergent, and unconventional-but-genuine human writing before
deployment, or it will simply relocate the fluency-bias harm from "AI gets
an undeserved pass" to "atypical humans get an undeserved penalty" — which
is arguably worse, since it's punishing real people for real work. This
isn't limited to non-native writers: the same low-perplexity, low-variance
signature that trips up ESL writers also shows up in the precise, literal,
highly structured prose that's common among autistic writers, and in the
more repetitive, narrowly-focused patterns sometimes seen in ADHD writing —
meaning a detector tuned only on "AI vs. typical fluent human" training
data will misfire hardest on exactly the humans whose natural writing
already looks least "typical."

(Code: `code/naive_ai_score.py` — verbatim, including the comment block.)

## Part 4 — Where It Bites Hardest, and Why Those Domains in Particular

Fluency-as-proxy was never uniformly reliable, but a few domains depended
on it especially heavily, which is exactly where AI's cost-collapse does
the most damage:

- **Education and assessment.** The entire architecture of essay-based
  grading assumes writing quality is a costly, hard-to-fake proxy for
  understanding. That assumption is now false in the specific way Part 2
  predicts, and the evidence in Part 3 shows both teachers and their
  AI-assisted replacements struggling with it.
- **Hiring — cover letters and application essays.** A cover letter used to
  cost real time and skill to write well; a fluent, well-structured one was
  weak-but-real evidence of conscientiousness and communication skill. That
  evidentiary value has collapsed the same way an essay's has.
- **Corporate and financial disclosure.** The signaling-theory research on
  annual report readability was built on the assumption that clear writing
  is genuinely costlier for a struggling firm to produce (since obscuring
  bad news is often the actual strategy, and doing so cleanly is hard).
  AI-smoothed disclosure text threatens to make readability stop
  correlating with underlying firm health the same way it's stopped
  correlating with student understanding.
- **Peer review and science communication.** A fluent, confidently-argued
  paper or grant proposal has always gotten more benefit of the doubt from
  reviewers under time pressure — the exact halo-effect mechanism from
  Part 1 — and that channel is now open to arguments with unverified or
  fabricated substance behind the polish (this connects directly to the
  Gettier-risk problem from the companion computational-epistemology
  framework).
- **Misinformation and scams — where the direction is reversed.**
  Historically, poor grammar and awkward phrasing was itself a *useful,
  low-cost tell* for scam emails and low-effort misinformation — bad
  writing was a costly-to-fix signal of low investment. AI removes that
  tell specifically, which means one of the oldest and cheapest heuristics
  ordinary people used to filter obvious scams is gone, and it's gone
  hardest for the least sophisticated readers who relied on it most.
- **Political communication.** Elected representatives historically read
  written volume and polish in constituent letters as a rough, costly proxy
  for how many people actually cared enough to act — a genuine letter took
  real time to write. Zero-cost, AI-generated constituent letters at scale
  break that proxy exactly the way an AI-written essay breaks a teacher's
  read on effort, leaving representatives less able to trust that written
  communication reflects real constituent sentiment at all.
- **Legal and corporate vetting.** A detailed legal complaint or threat
  letter used to be costly enough to draft that its existence carried some
  signal about how seriously the sender took the matter. AI collapses the
  cost of generating a legally fluent, complex-sounding document to
  seconds, while the cost for a professional to actually read, verify, and
  respond to it stays exactly as high as before — an asymmetry that can be
  used to flood a counterparty with cheap-to-produce, expensive-to-refute
  documents.

## Part 5 — What Actually Substitutes for the Broken Signal

If fluency no longer reliably tracks the thing you actually care about, the
fix isn't a better fluency detector (Part 3 shows those inherit the same
bias) — it's shifting assessment toward things that are still genuinely
costly to fake. But each substitute below has its own way of quietly
reintroducing the exact bias it's meant to fix, so each one needs a named
safeguard, not just adoption.

- **Process evidence over artifact evidence — with a real caveat.** A
  polished final essay is cheap to produce; a version history, an edit log,
  or a set of intermediate drafts showing an argument developing is still
  expensive to fabricate convincingly. But **raw process telemetry is not
  the same thing as high-level process evidence, and the raw version has
  its own equity problem**: keystroke logging, active-typing timers, and
  pause-rate surveillance all encode an implicit "normal" writing rhythm —
  steady accumulation, moderate pauses — that penalizes genuinely different
  but authentic writing processes. An ADHD writer who goes quiet for hours
  and then produces a fast, high-volume burst can look identical to a
  copy-paste event under raw telemetry. A multilingual writer who drafts a
  sentence in their first language, translates it, and pastes the polished
  translation in can look identical to a suspicious paste-in from an
  outside source. **The safeguard:** track only human-curated milestone
  artifacts (an outline, a messy first draft, a revised draft, brief notes
  on what changed and why) and never raw keystroke/pause data — assess the
  conceptual evolution between milestones, not the typing rhythm that
  produced them.
- **Live, unscripted elaboration — with a real caveat.** Asking someone to
  explain or defend a claim in real time still costs genuine understanding
  to fake — but a fully open-ended, unscripted oral exam also reliably
  favors confident, verbally fluent, low-anxiety speakers, which just
  relocates the halo effect from written fluency to spoken fluency. **The
  safeguard:** share the exact question structure and timing in advance so
  the exam tests understanding rather than improvisational performance;
  focus questions on *why* a specific decision was made rather than on
  rapid recall; allow real accommodation (text-chat mode, video-off, extra
  processing time) without treating any of those as evidence of lesser
  understanding.
- **Decoupled rubric lines — made concrete.** Score
  substance/accuracy/argument structure on one axis and prose mechanics on
  a completely separate axis, and don't let a high score on the second
  silently inflate the first:

  | Dimension | What it rewards | What it explicitly ignores |
  |---|---|---|
  | Process traceability | Documented conceptual evolution across milestone drafts | Typing speed, pause length, keystroke pattern |
  | Analytical depth | Identifying non-obvious tradeoffs, gaps, or logical connections | Vocabulary complexity, stylistic flair, sentence variety |
  | Interactive defensibility | Ability to explain and defend a decision under follow-up questions | Vocal delivery, pacing, speech fluency, visible anxiety |
  | Mechanical polish | Basic readability — a binary pass/fail hurdle, not a scored axis | Whether grammar tools or AI copy-editors were used to get there |

  The mechanics row is worth calling out specifically: treating it as a
  **binary hurdle** (readable / not yet readable, with no further points
  available) rather than a **scored axis** removes the exact lever AI-polish
  currently pulls hardest on — there's no partial credit left to earn from
  purely being well-written.
- **Verifiability, not persuasiveness, as the pass bar.** A claim that can
  be traced to a checkable source is a stronger pass condition than a claim
  that merely reads confidently — this is the Gettier-risk logic from the
  companion framework applied to human work as much as AI output.
- **Explicit, disclosed AI-assistance policies rather than pure
  ban-and-detect.** Given that detection tools misfire specifically against
  non-native and atypical writers (Part 3), a policy that asks people to
  disclose and account for AI use, rather than relying on a detector to
  catch it, avoids relocating the harm onto exactly the writers who least
  deserve it.

## Reference Lineage / Further Reading (as given by the source)

**Psychology of the fluency heuristic:** Reber, Winkielman & Schwarz
(1998), Effects of Perceptual Fluency on Affective Judgments, Psychological
Science; Schwarz (2004), Metacognitive Experiences in Consumer Judgment and
Decision Making, Journal of Consumer Psychology; Landy & Sigall (1974) —
the classic essay-quality/halo-effect study; Alter & Oppenheimer's broader
processing-fluency research program.

**Economics of signaling:** Spence (1973), Job Market Signaling, Quarterly
Journal of Economics; Elzahar & Hussainey (2012) and the
annual-report-readability literature; Loughran & McDonald (2014), Journal
of Finance.

**Current empirical evidence:** Fleckenstein et al. (2024) — teachers'
inability to distinguish; "Is it Cake or is it AI?" systematic review
(2026), arXiv:2604.03437; Liang & Zou et al. (Stanford, 2023) — the
TOEFL/61.3% detector-bias study; the UK psychology-module exam study (94%
undetected, outscoring students); Galdin, "Making Talk Cheap: Generative AI
and Labor Market Signaling" (2025), arXiv:2511.08785 — the Freelancer.com
study behind Part 2's figures, verified across arXiv/ResearchGate/RePEc;
Newby v. Adelphi University (decided Feb. 2026) — reported independently by
Inside Higher Ed and multiple outlets.

Course-relevant framing: this is the direct partner problem to the
computational-epistemology/Gettier-risk framework — that framework is about
AI output fooling you with fluent-but-ungrounded claims; this one is about
fluency itself fooling you about a human's (or AI's) underlying competence.

**The source's own source-quality note (kept, load-bearing):** one write-up
fed in during drafting attributed the detector-bias court case to a
different student name, university, and year ("Moira Olmsted, Central
Methodist University, 2023") than court and news reporting show (Orion
Newby, Adelphi University, decided 2026). The mismatch traces to a viral
social-media post that appears to have conflated two different things under
one name. Both the original mismatch and its confident, fluent presentation
are a small live demonstration of exactly the problem this document is
about.
