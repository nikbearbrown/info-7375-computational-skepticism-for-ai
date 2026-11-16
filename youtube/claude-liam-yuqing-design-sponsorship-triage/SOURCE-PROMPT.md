# Source — Yuqing's final-project proposal + feedback research prompt

## Student proposal (first name only)
Yuqing, INFO 7375 (Computational Skepticism for AI). Final project: a **UX/Product Designer
Sponsorship Triage weights-profile** for the Reallocation Engine. Plan: build a design-track
weighting profile over the engine's existing signals — SEC Form D funding signal, sponsorship
history, ATS hiring-activity data — reweighted for design-track roles rather than the engine's
current general focus, so F-1 UX/Product Design job-seekers can re-rank opportunities by
sponsorship likelihood and spend less time on unsuitable roles.

## Feedback research prompt (the reel's content spine)
A weights-profile ("same signals, different coefficients") is the right architecture ONLY if
the existing signals stay valid proxies for design roles and just need different relative
importance. If a signal behaves differently, or a genuinely new risk factor exists for design,
reweighting is the wrong tool — the project needs a **new signal**, not new coefficients.

- **Part 1 — Specialty-occupation risk is a MISSING SIGNAL, not a weighting problem.** Whether
  a UX/Product Design role qualifies as an H-1B "specialty occupation" at all is contested and
  role-specific (8 CFR §214.2(h)(4)) in a way it isn't for SWE/DS. A "UX Designer" staffed with
  business/marketing grads doesn't survive scrutiny; a role requiring HCI + a relevant technical
  degree is defensible. Diagnostic: does the company's current design team hold HCI/CS/formal
  design degrees (defensible) vs self-taught/varied backgrounds (RFE risk)? Reweighting Form D
  or ATS can't capture this. Add a **specialty-occupation defensibility** signal.
  Code: `specialty_occupation_defensibility(company, role)` → {defensibility, note} from team
  credential ratio + job-description specificity.
- **Part 2 — Which of the 3 inherited signals actually transfer.** SEC Form D funding may need
  a **lag adjustment** (design hires lag engineering at newly-funded startups; cut first in a
  downturn). Sponsorship history is most likely to mislead if reweighted naively — willingness
  is role-specific inside one company; **disaggregate by job family** where LCA data allows,
  not "this company sponsors" as one fact. ATS hiring-activity needs **design-specific base
  rates** (fewer reqs, longer cycles, portfolio step). For each, say: new weight, structural
  adjustment, or unchanged + add the new signal. Don't treat all three as "just reweight."
- **Part 3 — Thin-data risk.** Design-track sponsorship outcomes are a smaller dataset →
  overfitting. How large/representative is the calibration set? Validate against held-out cases;
  if too thin for train/test separation, state it up front, don't paper over with a confident
  three-color output.
- **Part 4 — Robustness tests for THIS extension:** signal-necessity (ablate the new signal —
  how often does it change the outcome?); cross-role stability (same company through general vs
  design profile — where/why do they disagree?); thin-data sensitivity (perturb weights → do
  real classifications flip?); vague-vs-specific posting stress (does defensibility separate
  "creative problem-solver" from HCI-specific postings, or default everything to middling?).
- **Part 5 — Honest visualization.** Surface specialty-occupation defensibility as its OWN
  visible factor, not folded into an aggregate; flag thin-data confidence (design-track score
  should read less certain than general-track at the same nominal color); show the design-
  specific sponsorship record separate from the company-wide record.

Reference lineage: the Reallocation Engine (shared course base); 8 CFR §214.2(h)(4) specialty-
occupation definition; USCIS RFE patterns for UX/design roles (UX vs Graphic Designer
classification, degree-to-role alignment); DOL/USCIS LCA & H-1B disclosure data (title
standardization limits); the course's skeptical-instruments framework.

## Verified during authoring (DOUBLE-CHECK)
- Design/UX H-1B roles face notably higher specialty-occupation scrutiny than SWE; degree-to-
  role match and the hiring team's credential composition are the real diagnostic; a "UX
  Designer" staffed by business/marketing grads doesn't survive scrutiny; defensible degrees
  are HCI / CS-UX / Information Science / design; vague "creative" roles draw denials —
  confirmed (F1Jobs UX/UI-designer H-1B guide; specialty-occupation four-test/RFE practice).
  Carried as the *mechanism* of the missing signal, not as datable numbers.
