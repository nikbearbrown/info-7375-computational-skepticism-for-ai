# Source — Saloni's final-project proposal + feedback research prompt

## Student proposal (first name only)
Saloni, INFO 7375 (Computational Skepticism for AI). Final project: a **Job Application
Priority Checker** — a decision-support tool that helps students prioritize which jobs to
apply for based on skills, experience, location, and work-authorization requirements. It
gives a transparent recommendation with an explanation of its reasoning, evaluated with
the course's skeptical instruments (robustness testing, honest visualization) to surface
limitations and improve reliability.

## Feedback research prompt (the reel's content spine)
Evaluate the proposal through a Computational Skepticism lens. Three things make it harder
than it looks: (1) **work authorization is not a neutral feature** — a legally/causally
loaded eligibility gate, not a column like "skills"; (2) **transparent ≠ correct** — a tool
can expose full reasoning and still reason badly; (3) it **overlaps Professor Bear's own
Reallocation Engine** (F-1/OPT job search using SEC Form D, O*NET, BLS) — a reason to hold
it to a real standard.

- **Part 1 — Name the target.** "Prioritize" implies a predictive claim: better by *what*?
  Interview probability, offer probability, sponsorship follow-through, salary, time-to-hire?
  An unnamed target makes "transparency" cosmetic. A simple honest version is an explicit,
  user-adjustable weighted scoring function whose returned sub-scores ARE the explanation —
  the reasoning is the mechanism, not a post-hoc SHAP approximation.
- **Part 2 — Work authorization is a gate.** Model sponsorship as a hard gate with an
  explicit data-confidence flag (confirmed vs inferred-from-USCIS-filings), not a smoothed
  score that hides the eligibility cliff. Failure modes: soft-scoring a disqualifier →
  top-ranking a job the student can't take; using employer sponsorship history as a noisy
  proxy without validity checks; ignoring time-boundedness (OPT/STEM-OPT windows).
- **Part 3 — Robustness: what should break.** Near-threshold sensitivity (does ±10% skill
  match reorder the top 3?), missing-data behavior (blank field silently biasing the score),
  adversarial gaming (inflated self-assessment), distribution shift across job categories.
  Require a written robustness table: perturbation → does the top rec change → is it defensible.
- **Part 4 — Honest visualization.** Show weights + sub-scores, not just a composite; avoid
  false precision ("87.3%" implies unearned accuracy — bucket strong/moderate/weak); shade
  uncertainty on the sponsorship dimension specifically.
- **Part 5 — Connect to the Reallocation Engine (sparingly).** Two transferable moves:
  grade data sources explicitly (confirmed/inferred/self-reported); separate a hard
  eligibility gate from a soft preference score. Point at these as open questions, don't
  hand over a solved architecture.

Reference lineage: the Reallocation Engine; USCIS H-1B Employer Data Hub; O*NET Online;
Rudin, "Stop Explaining Black Box Machine Learning Models" (2019); the course's own
skeptical-instruments framework.

## Real code carried by the reel (Onda code-blocks — real Python from the source)
`priority_score(job, student_profile, weights)` — explicit weighted scoring, returns
(score, sub_scores dict). `sponsorship_compatibility(job, student_profile)` — hard 0/1 gate
plus a data-confidence flag.
