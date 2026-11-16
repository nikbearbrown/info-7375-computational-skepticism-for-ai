# gettier_check.py — shown on screen in B10 (Onda code-block).
# Verbatim from the source doc (SOURCE.md, Part 1). The point the beat makes:
# truth and entailment are SEPARATE scores; high truth + low entailment is
# the Gettier-risk case a truth-only checker cannot see.

def gettier_check(claim, cited_source, model_reasoning):
    """
    Returns whether a claim's justification is load-bearing,
    not just whether the claim happens to be true.
    """
    truth_score = verify_against_source(claim, cited_source)  # retrieval-grounded
    entailment_score = check_entailment(model_reasoning, claim)  # does reasoning -> claim?
    source_exists = source_is_real(cited_source)  # citations get fabricated

    if truth_score > 0.8 and entailment_score < 0.4:
        return "GETTIER_RISK"  # true, but justification doesn't support it
    if not source_exists:
        return "FABRICATED_JUSTIFICATION"
    if truth_score > 0.8 and entailment_score > 0.7:
        return "SAFE"
    return "UNVERIFIED"
