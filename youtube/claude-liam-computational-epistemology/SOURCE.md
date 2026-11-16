# SOURCE.md — the primary source, on disk for Gate F

Provenance: research document pasted by Bear into the Cowork session,
2026-07-21. This is the reel's primary source; FACTCHECK.md rows verify
against it (and against primary sources where it cites them). Note its own
final caveat — parts of its lineage mix verified formalism with
fabricated-looking empirics; that caveat is itself load-bearing for this
episode (see SOURCES.md editorial decisions).

---

# Computational Epistemology: Knowing What's True in the Age of AI

## The Core Problem

Epistemology has always asked three questions: what is knowledge, how is it
justified, and how do we defend against skeptical doubt. Those questions used
to be answered by philosophers arguing in seminar rooms. Now they have to be
answered by systems — because the volume of propositional claims hitting any
individual has outrun any individual's capacity to apply the classical
apparatus (justification-tracing, source-checking, coherence-checking) by
hand.

Two distinct failure modes sit under "how do we know something in the age of
AI," and they get conflated constantly:

1. First-person verification — you (or a fellow) generated output with an
   LLM. Is it true? Is it grounded? Did the model fabricate a citation, a
   statistic, a mechanism? This is the JTB (justified true belief) problem
   applied to your own pipeline's output.
2. Third-person flood-filtering — the wider information environment is now
   saturated with synthetic text, images, and video, much of it optimized for
   engagement rather than truth, some of it adversarial. This is the
   classical skeptical problem (Cartesian demon, Humean induction) except the
   demon is now a real, cheap, scalable technology rather than a thought
   experiment.

The philosophical vocabulary — internalism/externalism, reliabilism,
coherentism, Bayesian updating, the regress problem — isn't decoration here.
Each one maps to an actual design decision in a verification tool. The
video's arc (definitions → JTB → Gettier → internalism/externalism →
foundationalism/coherentism → skepticism → Bayesian epistemology) is roughly
the right order to build a computational epistemology stack in, because each
stage answers "what broke in the previous stage."

Below: the concept areas in that order, what breaks classically, and what a
computational tool looks like when you try to patch it.

## Part 1 — JTB and the Gettier Problem: Why "the model said so, and it's true" isn't knowledge

Classical justified true belief: S knows P iff P is true, S believes P, and S
is justified in believing P. Gettier's counterexamples show true + justified
belief can still be lucky rather than knowledge — the justification and the
truth come apart, connected only by accident.

This is exactly the failure mode of an LLM output that happens to be correct
via a bad path — a hallucinated-but-coincidentally-correct number, a citation
that doesn't exist but points at a true claim, a plausible-sounding mechanism
that isn't actually the mechanism. Correctness without a traceable
justification path is Gettier-knowledge: it's not safe to build on, even when
it's true, because the same process will fail silently next time.

Implementation note: the fix isn't "check if the output is true," it's "check
if the justification is load-bearing." Concretely: does the claim survive if
you delete the specific evidence cited and try to re-derive it? A
claim-verification pipeline should separate two checks that are usually
collapsed into one "fact-check" pass:

- Truth check: is P actually true (compare against a retrieved source)
- Justification check: does the model's stated reasoning path actually entail
  P, independent of whether P happens to be true

(Code: `code/gettier_check.py` — verbatim.)

The point of formalizing this: most "AI fact-checkers" only run the truth
check. That's necessary but not sufficient — it lets Gettier cases through,
and Gettier cases are the ones that erode trust worst, because they look
identical to real knowledge until they don't.

Formalizing the risk. Give the truth check a score T(C) ∈ [0,1] (how well the
claim matches an external oracle/ground truth) and the justification check a
score S_NLI(D,C) ∈ [0,1] (how well the cited document D actually entails
claim C — a natural language inference / natural logic score, not a
keyword-overlap score). Define a Gettier risk coefficient:

    G_r(C, D) = T(C) · (1 − S_NLI(D, C))

High truth, low entailment → high G_r → this is exactly the case where the
claim is probably right but the given justification doesn't support it, which
is the most dangerous failure mode because it's invisible to a truth-only
checker. This coefficient is more useful than a single blended "confidence"
number precisely because it keeps truth and justification as separate axes —
collapsing them back into one score is what let the problem hide in the first
place. Set a hard entailment threshold τ_NLI below which a claim is rejected
regardless of how true it turns out to be.

## Part 2 — Internalism vs. Externalism: Where does the justification actually have to live?

Internalism: justification must be accessible to the believer's own mind —
you must be able to introspect and produce the reasons. Externalism (esp.
reliabilism, Goldman): justification depends on the belief being produced by
a reliable process, whether or not the believer can articulate why.

This maps directly onto a live design fork in AI verification tooling:

- Internalist tools demand the model show its work — chain-of-thought, cited
  sources, explicit reasoning traces — and evaluate the reasoning itself.
  This is what "cite your sources" and reasoning-trace inspection are doing
  epistemically.
- Externalist tools don't care what the model says about its own reasoning —
  they care whether the process that produced the output is statistically
  reliable (track record, calibration curves, agreement with ground truth
  over many trials), regardless of whether any single output is individually
  explainable.

Why this matters practically: internalist verification (asking a model to
explain itself) is vulnerable to confabulation — the model generates a
plausible-sounding justification post hoc that wasn't actually the process
that produced the answer (this is well-documented in interpretability
research: stated chain-of-thought often doesn't match the actual
computation). So an internalist-only verification tool can be gamed by
fluent-sounding but false self-reports.

The correct architecture is a reliabilist backbone with internalist
annotation: track the process's reliability empirically (externalist, the
load-bearing check), and use the model's stated reasoning as a secondary,
lower-trust signal (internalist, useful for debugging, not for
certification).

(Code: `code/reliabilist_verifier.py` — verbatim.)

Making "reliability" precise. A track record is only as good as its
calibration measure. Two standard metrics do the real work:

- Expected Calibration Error (ECE) — bucket predictions by stated confidence,
  then compare each bucket's stated confidence to its empirical accuracy:
  ECE = Σ_b (|I_b|/N) · |acc(I_b) − conf(I_b)|. A model that says "90%
  confident" and is right 60% of the time in that bucket has an ECE that
  exposes exactly the gap Part 2's internalist/externalist distinction is
  about.
- Brier Score — mean squared error between predicted probability p_i and the
  actual outcome y_i ∈ {0,1}: BS = (1/N) Σ_i (p_i − y_i)². Simpler than ECE,
  penalizes overconfident wrong answers hardest.

Conformal prediction turns a miscalibrated raw score into a statistically
valid guarantee without assuming the model's confidence means anything. On a
held-out calibration set, compute a nonconformity score per example (e.g.
E_i = 1 − p(y_i | x_i)), take the (1−α)(1+1/n) quantile of those scores as
threshold q_{1−α}, and at inference time only accept a claim if its
nonconformity score falls under that threshold. This gives a real,
finite-sample guarantee — "the true answer is in this set with probability
≥ 1−α" — which is a meaningfully stronger claim than "the model said 90%."
One caveat worth keeping: this guarantee is sensitive to prompt phrasing and
distribution shift, so a nonconformity score computed on internal layer
activations tends to be more stable than one computed on raw output logits,
since surface phrasing shifts the logits more than it shifts the underlying
representation.

## Part 3 — Foundationalism vs. Coherentism: What stops the regress?

The regress problem: every justified belief seems to need a further belief to
justify it, threatening infinite regress. Foundationalism stops the regress
at basic beliefs that are self-justifying (sense data, axioms). Coherentism
denies there's a foundation at all — beliefs are justified by mutual support
within a web, not by grounding out in bedrock.

For a verification pipeline this is the difference between two architectures:

- Foundationalist pipeline: ground every claim in a retrieved primary source
  (a PDF, a dataset, a peer-reviewed paper). Retrieval-augmented generation
  (RAG) is explicitly foundationalist epistemology — it tries to stop the
  regress at a document you can point to.
- Coherentist pipeline: don't ground in any single document; instead check
  whether a claim coheres with a large web of other claims the system already
  holds with confidence (cross-model consensus, multi-source triangulation,
  internal consistency across a corpus).

Neither is sufficient alone, and the failure modes are the classical ones:
pure foundationalism is only as good as the "basic belief"
(garbage-in-garbage-out if the retrieved source is itself wrong or the
retrieval mismatches the claim — this is the actual mechanism behind most RAG
hallucination that still cites a source). Pure coherentism can produce a
perfectly self-consistent, mutually-reinforcing structure of falsehoods (a
coherent conspiracy theory is still coherent) — this is precisely the risk
with cross-model consensus tools when multiple LLMs are trained on
overlapping data and share the same blind spots, so their "agreement" is not
independent evidence, it's correlated error.

(Code: `code/consensus.py` — verbatim; the coherentist trap and its
correction.)

Practically: a foundationalist anchor (a real, checkable source) plus a
coherentist cross-check (does it fit everything else you know), with the
coherentist half explicitly discounted for correlated model error, is the
closest thing to a working architecture. Neither half alone is stable — this
is the same conclusion 20th-century epistemology reached about the two
positions individually.

Making the discount rigorous, not just a vibe. The naive move — "average the
models' votes" — implicitly assumes their errors are independent, which is
the Condorcet Jury Theorem's load-bearing assumption. That assumption breaks
the moment models share pretraining corpora, architecture lineage, or
post-training pipelines: two models trained on overlapping web scrapes aren't
two witnesses, they're one witness talking to itself twice. Worth naming
explicitly: a consensus-cascade effect, where a claim that gets dominant
placement in one widely-scraped model's output gets ingested by other models'
training/retrieval pipelines in the next cycle, manufacturing an apparent
multi-source consensus that traces back to a single origin.

The correct fix is to model the shared training ancestry as an explicit
latent confounder L in a small Bayesian network — claim C and lineage bias L
both influence sources S1, S2 — and marginalize it out rather than ignoring
it:

    P(C | S1, S2) ∝ P(C) Σ_L P(L) · P(S1 | C, L) · P(S2 | C, L)

Ignoring L (naive Bayesian updating on "agreement") artificially inflates
confidence exactly when the sources are least independent. An alternative,
simpler version of the same move: Dempster-Shafer discounting — assign each
source a reliability/discount factor d_f ∈ [0,1] based on known
corpus/architecture overlap, and reallocate the discounted mass to
"ignorance" rather than to either verdict, so correlated sources add noise to
your uncertainty rather than false confidence to your belief.

A caution on citing this kind of formalism uncritically: it's easy to find
write-ups of this exact framework that pair the real math above with
fabricated-looking benchmark tables — precise accuracy percentages,
correlation matrices, ECE values — attributed to no dataset, no eval
methodology, no reproducible source. That pattern (correct-sounding math
wrapped around invented empirics) is itself the Gettier-risk /
consensus-cascade problem from Parts 1 and 3, just committed by a document
instead of a model. The formalism is worth using; specific numbers without a
traceable source should be discarded regardless of how authoritative the
table formatting looks.

## Part 3.5 — The Utility Belt [CUT FROM THE EPISODE — datable]

[The source's tooling survey (named hallucination detectors, conformal
prediction libraries, C2PA/watermarking vendors, eval platforms, "as of
mid-2026" claims) was cut from the episode per deep-explainer hard rule 4 —
vendor names and dates would age the reel; the mechanisms are taught by the
surviving acts. See SOURCES.md decision 1. Its one structural point that
survives in spirit: no off-the-shelf tool implements Part 3's
correlated-error discount — "ask three LLMs and average" remains the default
in real pipelines, and that hole is the piece worth building.]

## Part 4 — Skepticism as an Adversarial Model, Not a Mood

Cartesian skepticism (the evil demon / dream argument) and Humean skepticism
(the problem of induction — past regularity doesn't logically guarantee
future regularity) aren't historical curiosities here; they are literally the
threat model for synthetic media.

- Cartesian skepticism → deepfakes and synthetic text at scale. The demon is
  no longer a thought experiment; it is a text-to-video model. The
  philosophical question "how would you know if all your sense-experience
  were being manipulated by a deceiver" is now an engineering question with a
  real adversary and a real cost function.
- Humean skepticism → the problem of induction for AI benchmarks. A model's
  past reliability on a benchmark does not logically guarantee future
  reliability on out-of-distribution inputs — this is not a hand-wavy worry,
  it's the exact structure of Hume's argument, and it's why reliabilist track
  records (Part 2) degrade the moment the input distribution shifts (new
  domain, new adversary, new jailbreak).

The productive response to skepticism historically wasn't "refute the
skeptic" (nobody has), it was mitigated skepticism — Hume's own move, and the
pragmatist move after him: proceed on fallible, revisable grounds because the
alternative (paralysis) is worse, while building habits/institutions that
catch errors over time rather than demanding certainty up front.

This is the actual design philosophy that should govern the tool, not "detect
all fakes" (undecidable in general, symmetric arms race) but "build a
revision-friendly pipeline that assumes error and is cheap to correct," i.e.,
provenance tracking + fast correction loops over binary detection.

Formalizing "revision-friendly," not just gesturing at it. The AGM model of
belief revision (Alchourrón, Gärdenfors, Makinson) gives three precise
operations instead of one vague "update": expansion (K + φ, add a new claim
without checking for contradictions — cheap, provisional), revision (K * φ,
add a new claim while discarding whatever it contradicts, to keep the belief
set consistent), and contraction (K ÷ φ, retract a claim without replacing
it, when it's refuted and you don't yet have a replacement). Most ad hoc
"correction" systems only implement expansion — they append the fix but never
trace what should be retracted downstream. If claims are stored as a
dependency graph (edges = "this claim's validity supports that claim"), a
contraction should recursively walk the graph and flag or quarantine
everything that depended on the retracted node, rather than silently leaving
stale conclusions in place next to their now-invalid premise.

A second sharp, practical rule worth stealing directly: provenance-capped
updating. However confidently a claim is phrased, its allowed influence on
your belief should never exceed the actual, verifiable trustworthiness of the
channel it arrived through:

    r(o) = min(provenance(o), content(o))

where content(o) is how confident the text itself sounds/argues, and
provenance(o) is the independently verified trust ceiling of the source (a
known-good channel, a cryptographically signed document, a peer-reviewed
venue, vs. an anonymous unsigned web page). This single formula is a direct,
computable defense against the oldest trick in persuasion — stylistic
confidence substituting for actual authority — and it's worth implementing as
a hard cap, not a soft weighting, precisely because fluent style is cheap to
fake and provenance is not.

## Part 5 — Bayesian Epistemology: The Actual Load-Bearing Math

Everything above is architecture; Bayesian epistemology is the part that's
directly computable. Belief comes in degrees (credences), not binary
knowledge/no-knowledge, and rational belief revision is updating a prior by
the likelihood of the evidence (Bayes' rule), not lurching to a new binary
verdict on each new fact.

This is the one place classical epistemology and computational tooling are
already the same discipline — calibration, confidence scores, and Bayesian
updating in ML are not inspired by Bayesian epistemology, they are it, just
under a different department.

Implementation note: the practical failure in most "AI confidence scores" is
that they're not actually calibrated probabilities — they're an LLM's stated
confidence, which (per Part 2) is an internalist self-report and is known to
be poorly calibrated (models are frequently overconfident, especially on the
exact hallucinations they should be least sure of). A real Bayesian tool
separates stated confidence from calibrated confidence, and only the latter
should gate action.

    def bayesian_update(prior_belief, evidence_likelihood_true,
                        evidence_likelihood_false):
        numerator = evidence_likelihood_true * prior_belief
        denominator = (numerator +
                       evidence_likelihood_false * (1 - prior_belief))
        return numerator / denominator if denominator > 0 else prior_belief

    def calibrate_stated_confidence(stated_confidence,
                                    historical_calibration_curve):
        bucket = round(stated_confidence, 1)
        return historical_calibration_curve.get(bucket, stated_confidence)
        # if the model says 90% confident but historically that bucket
        # is right 60% of the time, 60% is the number to act on

A verification pipeline that runs multiple independent checks (retrieval
match, entailment check, cross-model check discounted for correlation,
reliabilist track record) should combine them as sequential Bayesian updates
on a single credence, not as a majority vote — a vote throws away exactly the
information (differential reliability of each check) that Bayesian updating
is designed to use.

Two more pieces worth having explicitly, since both turn "check your work"
into something computable rather than a habit:

- Surprise-weighted revision speed. Not every new piece of evidence should
  move your credence by the same amount — an observation that was already
  highly expected under your current belief should barely move it, while a
  genuinely surprising one should move it a lot. Information theory already
  has the right measure: S(o) = −log₂ P(o). High surprise should trigger an
  actual re-check of the belief and anything downstream of it; low surprise
  should just fold in as a minor update. This stops a pipeline from either
  ignoring genuinely disconfirming evidence or overreacting to routine
  confirmation.
- A real decision rule at the end, not just a number. A calibrated credence
  P(C) is only useful if something downstream acts on it consistently. Pick
  an activation threshold τ set by the actual cost asymmetry of the decision
  (a clinical or legal claim should have a much higher τ than a casual
  factual aside). If P(C) ≥ τ: serve the claim. If P(C) < τ: don't force a
  binary answer — abstain, hedge explicitly, route to a human, or invoke a
  more expensive/slower verification pass. The core discipline this enforces:
  a system (or a person) should be structurally allowed to say "not confident
  enough to act on this," rather than every question forcing a
  false-precision answer.

## Reference Lineage / Further Reading (as given by the source)

Classical epistemology: Gettier, "Is Justified True Belief Knowledge?"
(1963); Goldman (reliabilism); BonJour, The Structure of Empirical Knowledge;
Hume, An Enquiry Concerning Human Understanding; Descartes, Meditations on
First Philosophy; contemporary Bayesian epistemology (Bayes/Ramsey/
de Finetti lineage).

Computational extensions: RAG literature and its failure modes; model
calibration literature (LLM overconfidence); chain-of-thought faithfulness /
interpretability research; C2PA provenance; NLI / natural logic for the
entailment score; conformal prediction; Condorcet Jury Theorem and its
independence assumption; Dempster-Shafer evidence theory; AGM belief
revision.

Source's own source-quality note (kept, load-bearing): of the two write-ups
fed into the source's drafting, one was thin on citations for its empirical
claims (treat those as unverified until traced), and the other paired
genuinely correct formalism with an untraceable benchmark table and
error-correlation matrix (math kept, numbers discarded). This is a live
example of the Gettier-risk / consensus-cascade pattern the framework itself
is designed to catch.
