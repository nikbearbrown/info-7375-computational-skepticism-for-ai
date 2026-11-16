# Professor Bear's feedback — Zening's Computational Skepticism final project
_Source for a deep-explainer reel. FIRST NAME ONLY: "Zening." The reel is Bear's feedback
on the project idea below._

## The student's proposal (Zening)
Topic: "Research-Like Roles in the High Tech Industry." Thesis: LLMs are changing traditional
software-developer and technical roles — tasks that used to be "implement a clearly defined
spec" now require experimentation, hypothesis testing, evaluation, continuous investigation.
These roles aren't labeled "research," but their workflows are increasingly research-like: a
flat management structure (one lead/PM, like a PhD-student/advisor relationship), exploratory
rather than fully-specified projects, small teams doing what once took large teams — with LLMs
handling implementation (code, prototypes, debugging, docs, testing) so humans focus on defining
problems, frameworks, evaluating alternatives, high-level design. Plan: define the characteristics
of a "research-like role," then use the Reallocation Engine to identify matching job postings.

## The core problem
The thesis is genuinely interesting and plausible — a real, observable-in-principle shift. The
gap is between the thesis and the METHOD: a classification/matching task built on an undefended
construct, applied to a causal claim the method can't test. Two things need tightening:
1. "Research-like role" must be operationalized into something FALSIFIABLE *before* looking at
   postings — else the characteristics get tuned (consciously or not) to match whatever postings
   feel research-like.
2. "LLMs are causing this shift" is a claim about change over time AND mechanism. A classifier on
   a cross-sectional snapshot can't show LLMs caused an increase — that needs a comparison the
   current plan lacks.

## Part 1 — operationalize "research-like" BEFORE looking at any postings
The characteristics (flat management, PhD-advisor supervision, exploratory projects, small teams)
are well-articulated conceptually but not yet observable, checkable criteria. Risk: circularity —
build the definition, go looking for confirming examples, and the "characteristics" become a
post-hoc description of the selected postings rather than a definition that could FAIL to match.
Feedback angle: require a coding scheme FINALIZED before any postings are examined — a few
binary/ordinal criteria a third party could apply and get a similar answer (e.g. ambiguous
deliverable; small/inferable team size; single flat reporting line; evaluation/experimentation
emphasis; explicit AI-assisted implementation). Then validation: Zening + one other rater
independently code 20–30 postings and check agreement. LOW inter-rater agreement is itself an
important finding — it would mean "research-like" isn't yet reliably identifiable from posting
text, worth knowing before building a classifier around it.

## Part 2 — posting LANGUAGE is not the same as actual job PRACTICE (the biggest validity risk)
Job postings are marketing documents by recruiters; buzzword inflation is well documented —
"innovative," "fast-paced," "ownership," "experimentation" appear in postings for plenty of
conventional, tightly-specified roles. A posting can hit every research-like buzzword and describe
a conventional feature-ticket job — and vice versa.
Feedback angle: distinguish two claims explicitly:
- "Job postings increasingly USE research-like LANGUAGE" — directly testable from posting text.
- "Jobs are increasingly STRUCTURED in a research-like way" — needs evidence BEYOND posting text
  (Glassdoor/Blind reviews of day-to-day structure, LinkedIn team-size/reporting data, a few
  informational interviews).
If the project only has posting-text data, scope claims to the FIRST (weaker) version and say so —
don't let the stronger claim ride on evidence that only supports the weaker. Exactly the
proxy-validity gap the course's skeptical instruments exist to catch.

## Part 3 — the causal claim needs a comparison the design doesn't have
The thesis attributes the shift to LLMs specifically. But flat structures, small autonomous teams,
and PhD-advisor supervision have existed in R&D-heavy firms, startups, and labs for DECADES,
independent of LLMs — not a new organizational form, even if LLMs make it more broadly feasible.
Without a comparison, the project can't distinguish "LLMs are causing MORE roles to become
research-like" from "research-like roles have always existed at some baseline rate, and this
project is just now noticing them."
Feedback angle: build in at least one comparison:
- TIME: does prevalence of research-like postings rise across before/after widespread LLM
  coding-tool adoption (~2022 on) vs. a stable earlier baseline?
- CROSS-SECTION: do heavy-AI-adoption companies show a higher rate than otherwise-similar
  companies without it, holding size/sector roughly constant?
Either converts "here are postings matching a pattern I defined" into "evidence the pattern is
associated with the thing I claim causes it." Without one, soften the LLM-causation framing to a
hypothesis under investigation, not a premise.

## Part 4 — how this actually uses the Reallocation Engine
The Engine's existing signals (SEC Form D funding, sponsorship history, ATS hiring-activity) target
a DIFFERENT problem (visa-sponsorship risk) than this (role-structure classification). This project
adds a wholly NEW NLP classification layer on the Engine's posting-ingestion pipeline, not an
extension of its scoring logic. Fine — but Zening should state whether the deliverable is (a) a
standalone classifier that could layer onto the Engine's posting data, or (b) a new scored
dimension integrating with the Engine's GREEN/AMBER/RED outputs. Different scope, different
evaluation criteria.

## Part 5 — robustness + honest visualization
1. Inter-rater reliability (Part 1) — report it, even informal; don't present the coding scheme as
   self-evidently objective.
2. Keyword sensitivity — if the classifier leans on specific terms, test whether small changes to
   the keyword list change which postings flag; brittleness to synonyms signals it's capturing
   surface language, not the construct.
3. Base-rate honesty — if "research-like roles are increasing," show counts/rates over time with
   sample sizes / CIs per period; early periods have small samples that can manufacture a trend.
4. Don't conflate correlation with the LLM mechanism in charts — label co-occurrence as
   co-occurrence, not causation, unless the Part 3 comparison supports the stronger claim.

## Close: open questions
End with one or two questions for Zening to resolve herself — what non-posting data source is
feasible within the time budget to validate actual role structure; how to define a defensible
"before LLM adoption" baseline period. Tone: encouraging but exacting — a strong, timely thesis;
push toward a design that can actually distinguish the thesis from a compelling but unsubstantiated
narrative.

## Reference lineage
The Reallocation Engine (clarify scope boundary vs. this new NLP layer); labor-economics job-posting
text-mining literature (O*NET / job-ad skill-demand studies) — precedent for Part 1's posting-
validity concern; recruiting-language-inflation / buzzword-prevalence studies — grounding for Part 2;
difference-in-differences / pre-post comparison design — the toolkit for Part 3's needed comparison;
the course's causal-reasoning framework — anchor for Part 3, same throughline as the stress-index
project's descriptive-vs-causal distinction.
