# Chapter 5 case: Stay put and get approved

**Chapter:** 5 Model explainability · **Seeded flaw:** feature attribution read as a causal effect and turned into advice · **Key terms:** feature attribution, SHAP / mean absolute Shapley value, feature importance vs causal effect, correlation vs causation, proxy, counterfactual explanation, actionability / recourse, faithfulness

---

# STUDENT PAGE

## 1. Scenario

Tarun is a credit officer at a community bank. About a third of small-loan applicants are declined by the bank's scoring model, and many ask what they could change to be approved. He wants a short, honest explanation he can give them. He asked an AI analyst to explain what drives the model's declines and what applicants can do about it.

## 2. The instruction given to the AI analyst

> "Using the approval model, explain which factors drive declines and tell me what applicants should do to get approved."

## 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **What drives declines: explanation of the loan-approval model**
>
> **Method.** Computed TreeSHAP values for the 14,000 applications in the last quarter and ranked features by mean absolute SHAP value.
> **Ranking (mean |SHAP|, share of total).**
> 1. Months at current address: 0.31 (24%)
> 2. Number of credit inquiries, last 6 months: 0.22 (17%)
> 3. Monthly income: 0.18 (14%)
> 4. Existing debt-to-income ratio: 0.15 (12%)
> 5. Employment length: 0.09 (7%)
> (remaining 9 features: 26%)
> **Interpretation.** Months at current address is the largest driver. Applicants with shorter time at their address are declined because they are a higher default risk; staying in one place **causes** lower default risk.
> **Advice for applicants.** To improve approval chances: (1) stay at your current address another 12 months before applying, (2) avoid new credit inquiries, (3) raise income if possible. Because SHAP is a faithful, exact decomposition, this advice is reliable.

## 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's interpretation and advice? Name the problem with the exact term for it.
2. **(2 points)** Name one check or kind of analysis you would ask for before telling applicants what to change.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Tarun what the ranking does and does not tell him. Use no technical terms.

---

# TA RUBRIC PAGE

Fixed rubric (see README): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

## Case key

**The flaw in one sentence.** SHAP values explain how the model's score depends on its inputs, not what causes default or what would happen if an applicant changed something; the agent treated a feature attribution as a causal effect (and as actionable advice).

**Full-credit terms (2).** Feature importance vs causal effect (attribution is not a causal effect); correlation vs causation (accept as full when it is applied to attribution); actionability / recourse (the missing check); proxy variable (months at address standing in for something else).
**Half-credit near-misses (1).** "SHAP is not reliable", "black box", "the model may be biased", "need a counterfactual" with no explanation, "feature importance is global not local".
**No credit (0).** Multicollinearity (alone); overfitting; "SHAP is too slow".

**Acceptable evidence requests (2), either one.**
1. Ask for counterfactual explanations for declined applicants with feasibility and monotonicity constraints (only changes an applicant can actually make), and state that these describe the model, not real-world default.
2. Ask for causal evidence for the claim (for example an experiment or an adjusted analysis of repayment outcomes), or an audit of whether months-at-address is a proxy for something else.
**Unacceptable (0).** "Recompute SHAP with more samples", "use LIME as well" (same problem), "explain the model more clearly".

**Fix or next step (2).** Rewrite so the report describes what the model does ("the model scores shorter tenure as higher risk"), separates it from any claim about why people default, drops the "stay put" advice, and requests actionable counterfactuals or a proxy audit. 1 point for removing the causal wording without a replacement analysis.

**Scope and plain language (1).** Two sentences, no jargon: the ranking shows what the bank's model looks at, not what would make a person repay; telling people to stay put to get approved is a guess, not a finding.

**Traps.**
- The final sentence ("SHAP is faithful, so the advice is reliable") is the rationalisation. Faithfulness to the model does not make the model faithful to the world.
- Students who say "months at address is a proxy for age or class" are adding the fairness angle correctly; give term credit.
- Do not reward a student for questioning the SHAP calculation itself (the ranking is not the flaw).

**CAP RULE.** If the student does not say that the attribution is not a causal effect or a basis for advice, the case total is capped at **5/10**.

## Scored sample answers

**Strong (9/10).**
1. This confuses feature importance with causal effect. Mean |SHAP| describes how the model uses address tenure; it does not show that staying longer lowers default risk. Tenure may be a proxy for something else (age, renting vs owning), so "stay put" advice is unsupported.
2. A counterfactual explanation with actionability and monotonicity constraints for declined applicants, plus a proxy audit of tenure.
3. "Describe what the model does with each feature without causal language. Generate counterfactual explanations restricted to changes applicants can really make, and test whether tenure is acting as a proxy for another variable. Withdraw the advice to wait twelve months."
4. "The attributions show what the model weighs most, not what causes repayment, so the stay-put advice is not supported."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Correct and thorough; Q4 says "attributions" and "causes repayment" in technical register, so the plain-language point is lost.*

**Typical (6/10).**
1. SHAP only shows correlation, not causation, so you can't tell applicants to stay at an address longer.
2. Get a counterfactual analysis.
3. "Don't give advice from SHAP; do something that shows what actually changes the outcome."
4. "The model uses address a lot but that doesn't mean moving less helps."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6 (term is generic correlation-vs-causation without tying it to attribution; evidence names counterfactuals but without constraints; fix is vague; Q4 is a shrug rather than a statement of what the ranking does show).*

**Fluent but wrong (3/10).**
1. SHAP with a tree model is subject to high-cardinality bias and the marginal vs conditional value function choice; the ranking may be unstable across background datasets. So the 24% could be wrong.
2. Re-run KernelSHAP with several background datasets and report the Jaccard stability of the top features.
3. "Recompute with the conditional value function and three baselines, and report the stability."
4. "The importance numbers might change if we compute them differently."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Fluent explainability vocabulary (value function, Jaccard) aimed at the stability of the ranking, which is not what the agent got wrong. A perfectly stable ranking would still not be a causal effect.*
