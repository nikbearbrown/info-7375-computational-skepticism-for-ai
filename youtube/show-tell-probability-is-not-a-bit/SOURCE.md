# Source excerpt

The film follows the section “What probability actually is — and why two engineers can disagree without either being wrong” through “The three axioms,” including the axioms table, from Chapter 2 of *Computational Skepticism for AI*. The authoritative read-only source is `../../chapters/02-probability-uncertainty-and-the-confidence-illusion.md`, lines 26–65.

## Verbatim excerpt

Most of you came up through a Boolean education. A bit is one or zero. A program either runs or doesn't. A test passes or fails. A theorem is proved or it isn't. Even when you allow uncertainty in — error bars, tolerances, noise floors — it tends to come in as a small wobble around an essentially yes-or-no answer.

Probability is a different animal. The output is not "true" or "false." The output is a degree of belief — a number between zero and one that tells you how confident you should be, given what you currently know.

Here is the thing that takes some adjustment. Two engineers can look at exactly the same evidence, end up at different probabilities, and both be reasoning correctly. Not both be right in some mushy relativistic way. Correctly. The reason is that they walked in with different priors — different starting beliefs about the world before the evidence arrived. Probability is always conditional on your information state, and different people have different information states.

This bothers some people deeply. It should bother you a little, because it is a real shift. The Boolean instinct works fine in deterministic systems. It misleads you in any system where you are working from a model rather than from the world itself — and every machine learning system, every AI deployment, every statistical inference, is a model rather than the world.

### The three axioms

Before we go further, we need the formal scaffolding. It is light and you will use it constantly.

A **sample space** $\Omega$ is the set of all possible outcomes of an experiment. Rolling a die: $\Omega = \{1, 2, 3, 4, 5, 6\}$. Whether a patient has a disease: $\Omega = \{\text{sick}, \text{healthy}\}$.

An **event** is any subset of the sample space — any collection of outcomes we might care about. "The die shows an even number" is the event $\{2, 4, 6\}$.

A **probability measure** $P$ assigns a number to every event. To be a legitimate probability measure, $P$ must satisfy three axioms:

1. **Nonnegativity**: $P(A) \geq 0$ for every event $A$.
2. **Normalization**: $P(\Omega) = 1$. Something has to happen.
3. **Additivity**: If $A$ and $B$ are disjoint — they cannot both occur — then $P(A \cup B) = P(A) + P(B)$.

That is the entire foundation. Everything else — conditional probability, Bayes' theorem, the central limit theorem — is derived from these three rules. When you forget why some formula is true, come back here.

Two useful consequences follow immediately. First, $P(\emptyset) = 0$: the probability of nothing happening is zero. Second, $P(A^c) = 1 - P(A)$: the probability of $A$ not happening is one minus the probability of it happening.

| Axiom | Formal Statement | Plain English Meaning |
|---|---|---|
| **Nonnegativity** | $P(A) \geq 0$ | Probabilities are never negative. |
| **Normalization** | $P(\Omega) = 1$ | Something must happen — the total is always 1. |
| **Additivity** | $P(A \cup B) = P(A) + P(B)$ for disjoint $A, B$ | Probabilities of mutually exclusive outcomes add directly. |

*Every probability calculation in this book is a consequence of these three rules.*
