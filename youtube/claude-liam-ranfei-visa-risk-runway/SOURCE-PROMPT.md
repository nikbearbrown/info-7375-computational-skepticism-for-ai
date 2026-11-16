# Source — Ranfei's final-project proposal + feedback research prompt

## Student proposal (first name only)
Ranfei, INFO 7375 (Computational Skepticism for AI). Final project: the **Visa-Risk Runway
Engine**, generalizing an earlier working pipeline (`ds-faang-opt`, from the Reallocation
Engine). The original 5-step, data-verified triage flagged FAANG roles GREEN/AMBER/RED for
international students on OPT using: H-1B filing history, SOC + cognitive-demand score,
year-1 filing lag, salary floor, and posting-liveness check. The generalization does two
things at once: (1) widen company coverage FAANG → mid-size tech, fintech, AI-infra startups;
(2) add STEM OPT 24-month extension-window timing alongside the existing initial-OPT April
lottery deadline.

## Feedback research prompt (the reel's content spine)
Two simultaneous generalizations, each quietly breaking an assumption the original pipeline
was calibrated on — and doing both at once hides that they interact. Treat it as **two
separate engineering problems that share a codebase**, not one generalization.

- **Part 1 — Widening the pool is a DATA-CONFIDENCE problem, not a coverage problem.** Each
  of the 5 signals degrades differently outside FAANG. Critically, "no H-1B filing history"
  at a Series A/B startup is *data sparsity*, not "confirmed non-sponsor" — collapsing both
  into RED systematically buries real opportunities at growing companies. Require a
  **confidence dimension per signal, per company tier**, distinct from the signal's value.
  Code: `sponsorship_signal(company)` returns {value, confidence, note}.
- **Part 2 — The STEM OPT extension clock is a DIFFERENT risk model, not a later deadline.**
  It's a **terminal** window (no extension after it). Cap-gap rules changed recently: under
  the H-1B Modernization Final Rule (eff. Jan 17 2025) cap-gap can now extend to ~April 1 of
  the next FY rather than ending Sept 30 — a model assuming the old Sept 30 stop is running
  stale logic. Cap-gap applies to change-of-status filings (not consular processing) and only
  with a timely-filed petition while F-1 status was valid. The 180-day auto-extension while
  STEM OPT is pending still counts against the 24-month total (delays erode runway). Two
  lottery cycles (initial-OPT year + STEM-extension year), each its own eligibility check.
  Code: `compute_risk_windows(student)` → two coupled but distinct clocks; STEM window carries
  `terminal: True`.
- **Part 3 — Recalibrate thresholds, don't port them.** FAANG-tuned GREEN/AMBER/RED cutoffs
  misclassify startups. Show the distribution of raw signal values *within the new pool*
  before choosing cutoffs — a threshold is only as good as the population it came from.
- **Part 4 — Robustness tests specific to the generalization:** tier-stratified sensitivity
  (same raw inputs, FAANG vs startup), regulatory-version test (old Sept 30 vs current
  April 1 cap-gap), sparse-data startup case (zero history → "unknown/low-confidence", not
  RED), terminal-window primacy (STEM terminal deadline outranks initial-OPT deadline).
- **Part 5 — Honest visualization for the generalized pool:** distinguish **confirmed RED**
  (documented non-sponsor) from **unknown/low-confidence** (no data) — must not look the same;
  show which risk window (initial-OPT vs STEM-extension) is the binding constraint; flag any
  classification resting on a stale/unverified regulatory assumption.

Reference lineage: ds-faang-opt / the Reallocation Engine (Ranfei's own prior work); H-1B
Modernization Final Rule (eff. Jan 17 2025) — verify directly against DHS/USCIS; USCIS H-1B
Employer Data Hub / LCA data (lag, non-disclosure limits); STEM OPT regs 8 CFR
214.2(f)(10)(ii)(C); the course's skeptical-instruments framework.
NOTE: a single-source gap-rate figure (90-day vs 100-day filers) is deliberately NOT carried —
flagged as unverified.

## Verified during authoring (DOUBLE-CHECK)
- H-1B Modernization Final Rule effective Jan 17 2025 — confirmed (USCIS). Cap-gap now runs
  Oct 1 to as late as ~April 1 of the next calendar year (was: ended Sept 30) — confirmed
  (MIT ISO summary of the rule). Carried as a *mechanism* ("the rule changed; verify current
  guidance"), not as a timeless date.
