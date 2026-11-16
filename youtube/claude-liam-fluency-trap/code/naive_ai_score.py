# naive_ai_score.py — shown on screen in B20 (Onda code-block).
# Verbatim from the source doc (SOURCE.md, Part 3). The beat's highlight:
# the trailing comment block — the detector measures formulaic-ness, and
# formulaic-ness is also the profile of real, atypical human writers.

# A simple illustration of why surface-level detectors inherit the bias
# they're supposed to catch: they're measuring formulaic-ness, not authorship.
def naive_ai_score(text_features):
    """
    text_features: dict with keys like 'perplexity', 'burstiness',
    'sentence_length_variance', 'vocabulary_diversity'
    Returns a score where LOW variance/perplexity looks "more AI".
    """
    # low burstiness (uniform sentence rhythm) and low perplexity
    # (predictable word choices) both push the score toward "AI-generated"
    score = (
        (1 - text_features['burstiness']) * 0.4 +
        (1 - text_features['perplexity_normalized']) * 0.4 +
        (1 - text_features['sentence_length_variance']) * 0.2
    )
    return score

# The problem: formulaic, low-variance writing is ALSO the profile of
# - non-native speakers taught rigid sentence templates
# - technical/legal writing that intentionally minimizes variance
# - anyone writing under time pressure using safe, practiced structures
# A detector tuned only on "AI vs. native fluent human" training data
# will misfire hardest on exactly these groups.
