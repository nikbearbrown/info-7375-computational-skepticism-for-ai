# consensus.py — shown on screen in B24 (Onda code-block).
# Verbatim from the source doc (SOURCE.md, Part 3). The beat's highlight:
# independence_weight — correlated agreement is discounted, not averaged.

def cross_model_consensus(claim, models: list):
    """
    NAIVE (coherentist trap): treat agreement across models as
    independent confirmation. This overestimates confidence when
    models share training data / architecture lineage.
    """
    votes = [m.evaluate(claim) for m in models]
    naive_confidence = sum(votes) / len(votes)  # WRONG if models correlated

    # CORRECTED: weight by estimated independence of error sources.
    # Same base model family / same training cutoff / same retrieval corpus
    # = low independence = discount the agreement.
    independence_weight = estimate_error_independence(models)
    corrected_confidence = naive_confidence * independence_weight
    return corrected_confidence
