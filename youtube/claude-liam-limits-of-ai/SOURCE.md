# SOURCE.md — the primary source, on disk for Gate F

Provenance: research document pasted by Bear into the Cowork session,
2026-07-21: "The Limits of AI: What the Tools Cannot Do — Research
Deepening." It deepens an essay of Bear's (the "three limits" essay) with
the philosophical and technical literature underneath it. Inline
`[cite N]` markers preserve the source's citation anchors. The source's own
Challenger correction (Mason→Lund attribution, per Rogers Commission
testimony, versus the looser circulating version) is load-bearing and
became the precision rule for B23.

---

# The Limits of AI: What the Tools Cannot Do — Research Deepening

## The Core Problem

The essay's claim: there are three limits on AI systems — meaning,
intentionality, the data-world gap — that are not engineering problems
waiting on more scale, more data, or a better architecture. They are
constitutive of what these systems are. A system that manipulates symbols
without a model of their referents doesn't get a model of their referents
by manipulating more symbols, faster. This is the crux worth defending
rigorously, because it's exactly the kind of claim smart people reflexively
try to dissolve with "but it'll improve" — and that objection doesn't touch
the argument.

Every one of these three limits has a real-world historical case where the
"human in the loop" who was supposed to catch the gap did not have the
actual authority to act on what they caught. That pattern — the override
existing on paper and not in practice — is its own well-studied phenomenon,
and it has a name (Part 5).

## Part 1 — Meaning: The Symbol Grounding Problem

Formalized by Stevan Harnad (1990): how do the symbols a system manipulates
get connected to what they're symbols of, rather than just to other
symbols? Harnad's answer: pure symbol manipulation can't bootstrap its own
grounding — you can define every word in a dictionary using other words in
the same dictionary, and a reader who already knows no language gets
nothing from it, no matter how large the dictionary. The clinical case: the
system's outputs are symbols correctly related to other symbols in its
training corpus; whether they're related to this patient's actual body is a
separate question the symbol-relations alone can't answer.

The multimodal-grounding counter-argument (images, sensors, embodiment
might supply real grounding) is a live, unresolved research question — not
settled either way. The essay's operational move is right: don't wait for
the metaphysics; ask whether an engineer can safely ASSUME grounding before
deployment. Bender and Koller's argument makes the strong version formal:
text-only language modeling trains on form without access to meaning — text
prediction alone cannot, in principle, learn meaning in the full sense at
issue, no matter how much text.

A sharpening distinction: two things people mean by "grounding" —
**document grounding** (retrieval, citations, source attribution: links a
claim back to a corpus; genuine auditability value) versus **world
grounding** (the original philosophical problem: links a symbol to the
actual state of affairs the document may only imperfectly and
non-currently describe). A RAG pipeline citing a real clinical guideline is
grounded in the document sense; whether that guideline still describes this
patient, right now, is a separate question. In stable closed-corpus
settings document grounding may be enough; wherever the world changes
faster than the corpus, document grounding can look like world grounding
without being it — the data-world gap re-entering through the back door.

Implementation: never let a system's confidence score stand in for
grounding-confidence. (Code: `code/flag_ungrounded_output.py` — verbatim,
including the document-vs-world note and the closing human-sign-off line.)

## Part 2 — Intentionality: Searle's Own Distinction

Searle — the Chinese Room's Searle — drew exactly this distinction:
**original (intrinsic) intentionality** versus **derived intentionality**.
Original intentionality belongs to a mind as a direct result of its own
mental activity. Derived intentionality is borrowed: [cite 72-1] computers,
languages, or symbols may stand for or represent the world, but only
derivatively — creatures like us program computers, lend meanings to words,
give meaning to symbols. [cite 74-1] Utterances borrow whatever derived
intentionality they have from the original intentionality of human beings
with minds that use them for their purposes.

Applied: an AI system's outputs have derived intentionality at best —
directedness borrowed from the humans who built it and the humans who read
it — never original intentionality of their own. Two deployments of the
same system read as being "about" different things because the directedness
isn't coming from the system; it tracks whoever is currently supplying it.

Two caveats. (1) Boden's warning (per the Stanford Encyclopedia's summary):
intentionality arguments shouldn't carry more weight than they can bear —
intentionality remains poorly understood even for ordinary human cases.
(2) Dennett rejects the framework outright: he has never believed in
original intentionality as a real intrinsic property, treating
intentional-state attributions as useful predictive tools. If Dennett is
right, "original intentionality" stops being a coherent target — but that
doesn't hand AI systems autonomous aboutness; it moves the bar to "is the
output as predictively useful as attributing intentions would suggest,"
which is lower and more answerable. The deployment question is sharper than
the philosophical one: is mere predictive usefulness enough for this use
case, or is the organization smuggling in stronger claims — understanding,
commitment, reasons — the system hasn't earned either way?

A concrete test: for any deployment, ask what intentional content would
survive if the human reader and operator were removed entirely. If the
honest answer is "none beyond the patterns humans read into the output,"
the intentionality is derived in the fullest sense — and the organization
should stop marketing or designing the product as if it had autonomous
understanding. Bites hardest: therapy-style chatbots, legal/HR mediation,
any product users will read as recognizing their motives.

## Part 3 — The Data-World Gap: Named and Measured

Mature technical vocabulary: **distributional shift**, decomposed into
covariate shift (input distribution changes), label shift (outcome
distribution changes), and concept drift (the input-outcome relationship
changes). All three are the clinical case's "other six percent, clustered
at the boundary," in plain language.

The engineering response (from the companion computational-epistemology
toolkit): conformal prediction, calibration tracking (ECE, Brier),
out-of-distribution detectors — not because they close the gap (they
can't), but because they give a statistically honest signal for when the
current case is likely outside the training coverage: the trigger condition
for the human override.

Measured, not theoretical: the **WILDS benchmark** (Koh et al.) was built
from real deployment shifts — hospitals, camera traps, time, geography —
and its central result is that these shifts substantially degrade deployed
performance, with the out-of-distribution gap persisting even after
existing robustness methods. **Guo et al.** on neural calibration: modern
networks are frequently poorly calibrated, and softmax confidence can be
arbitrarily high on inputs far outside the training distribution —
self-reported confidence is often exactly the signal that fails silently at
the boundary. **Rabanser, Günnemann & Lipton**: make systems "fail loudly"
rather than silently under shift — actively test incoming data for
distributional change instead of trusting the model's confidence to
announce the problem. Instrumentation, not repair: the tooling makes the
gap loud enough that an override has something concrete to respond to.

## Part 4 — Turing and Searle: What the Arguments License

Turing (1950) is a methodological proposal — don't demand more evidence for
machine intelligence than we accept for other minds — and citing it as
settling whether imitation constitutes intelligence overclaims it. The
standard replies to the Chinese Room — the Systems Reply and the Robot
Reply — are Parts 1 and 2 argued from the opposite direction; Searle's
response (grounding or systemic complexity still yields only more elaborate
derived intentionality) is why the debate hasn't closed.

## Part 5 — The Override Problem Has a Name: The Moral Crumple Zone

Madeleine Clare Elish coined **moral crumple zone**: [cite 79-1] while the
crumple zone in a car protects the human driver, the moral crumple zone
protects the integrity of the technological system, at the expense of the
nearest human operator. Mechanism: [cite 83-1] as control distributes
across actors in an automated system, social and legal conceptions of
responsibility remain built around a single individual — so when something
goes wrong, a human close to the system absorbs the blame even with limited
actual control. Elish's cases: [cite 88-1] Three Mile Island and Air France
447.

Experimentally: [cite 82-1] a recent large-scale study of human-in-the-loop
oversight found it does not reliably correct algorithmic errors and may
even exacerbate them, with the overseer's political preferences shaping
which errors get through — the "human supervisor" can be exactly the
fictional override: present on the org chart, absent in effect.

The Challenger case — WITH THE PRECISE ATTRIBUTION: the night before the
launch, Morton Thiokol's engineers, Roger Boisjoly among them, had the
O-ring cold-temperature data and argued to delay. Per the official Rogers
Commission testimony, the sentence that ended the argument was Thiokol's
Jerry Mason telling Bob Lund, the VP of Engineering: "take off your
engineering hat and put on your management hat" — NOT (as secondary sources
often have it) NASA or unspecified management saying it to Boisjoly. The
precision matters: the failure wasn't NASA overruling engineers from
outside — it was one Thiokol executive instructing another to stop
reasoning as an engineer, in the same room, on the same team. Management
reconnected the call and told NASA Thiokol was "go." Boisjoly had the
technical authority to detect the limit; he did not have the organizational
authority to act on it — and neither, once the hat came off, did Lund.

An override is real only if three things hold simultaneously (aligned with
NIST AI RMF role/oversight requirements and OECD real-intervention-capacity
guidance):

1. Independent access to a limit signal (drift detection, conformal set
   expansion, OOD score, audit anomaly) — not reducible to the system's own
   confidence. Boisjoly had this.
2. Organizationally binding, not advisory — it shouldn't need to win an ad
   hoc argument in the moment. Challenger is a story of an override heard
   and then overruled by a switch in decision frame, not rebutted on the
   merits.
3. No asymmetric career cost relative to staying silent — Boisjoly's
   professional life after speaking out is the standing counter-argument to
   treating this condition as easy.

## Part 6 — Calibration as a Practice, Not a Metric

The stated-confidence-vs-empirical-accuracy gap is Expected Calibration
Error applied to a human expert. Guo et al.'s definition — predicted
probabilities representative of true correctness likelihood — is the same
target whether the predictor is a network or an engineer signing a
deployment. The closing practice (Good Judgment Project methodology): lock
the prediction before the outcome, score it against reality (Brier-style)
over enough trials for a real base rate, treat the gap as information about
your own judgment. Calibration is trainable, but only through repeated,
scored practice — a team can understand the concept perfectly and still be
miscalibrated, because understanding isn't the same activity as being
scored.

## Part 7 — Turning It Into a Documentation Requirement

Precedents: Model Cards (Mitchell et al.) — intended uses, evaluation, and
limitations as a primary release artifact; Datasheets for Datasets (Gebru
et al.) — the same on the data side. The template:

    Named structural limit: This system is limited by [meaning /
    intentionality / distribution shift]. Performance claims do not imply
    this limit has been solved. The system is authorized for [specific use
    conditions] only. Cases that trigger [named shift/verification signal]
    must be routed to a human with binding stop/defer authority. Outputs
    must not be treated as evidence of intrinsic understanding, intent
    recognition, or real-world grounding beyond the validated scope.

Triage heuristic: failure from misreference → meaning (Part 1); failure
from pretended understanding → intentionality (Part 2); failure from the
world moving out from under the data → the gap (Part 3). Name the one most
likely to break THIS deployment.

Five questions a real override answers in writing: (1) the independent
out-of-scope signal; (2) who by actual role can halt or bypass; (3) the
step-by-step procedure when they do; (4) how retaliation/career cost is
prevented; (5) the audit trail proving the override was available in
practice — was it ever exercised, and what happened.

The no-deploy list — do not deploy when ANY hold: high-stakes and
irreversible before a human can realistically intervene; deployment assumes
world-grounding that can't be independently verified; drift can't be
detected fast enough to matter; calibration can't be prospectively scored
under deployment-like conditions; override authority can't be made
genuinely binding and career-safe. None of the tooling turns an unmanaged
structural limit into a solved problem — it turns it into a visible,
documented, governable one, which is a different and more honest
achievement.

## Reference Lineage (as given by the source)

Harnad (1990) The Symbol Grounding Problem, Physica D · Bender & Koller
(2020) Climbing towards NLU, ACL · Searle (1980) Minds, Brains, and
Programs, BBS · Searle (1983) Intentionality · Stanford Encyclopedia of
Philosophy, "Intentionality" (Boden caveat; Dennett/Searle) · Turing (1950)
Computing Machinery and Intelligence, Mind · Moreno-Torres et al. (2012)
dataset-shift taxonomy, Pattern Recognition · Koh et al., WILDS · Guo et
al. (2017) On Calibration of Modern Neural Networks · Rabanser, Günnemann &
Lipton, Failing Loudly · Elish (2019) Moral Crumple Zones, Engaging
Science, Technology, and Society · Rogers Commission testimony (Challenger;
Mason→Lund attribution) · NIST AI RMF; OECD AI Principles · Mitchell et
al., Model Cards; Gebru et al., Datasheets for Datasets.

Course framing: the third leg of a set with the computational-epistemology
/ Gettier-risk framework and the fluency-as-false-signal framework — all
three are versions of the same claim: a system (or person, or document) can
pass every test it was designed for while the thing that matters sits
outside the test's scope, and naming the scope explicitly is the only
reliable defense.
