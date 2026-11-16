# flag_ungrounded_output.py — shown on screen in B09 (Onda code-block).
# Verbatim from the source doc (SOURCE.md, Part 1). The beat's highlight:
# document grounding and world grounding are SEPARATE checks, and passing
# both still ends at human semantic sign-off.

def flag_ungrounded_output(response, entity_resolution_confidence, world_state_freshness):
    """
    Distinguishes "the model is fluent" from "the model's output is grounded
    in a current, verified representation of the specific referent."
    Note: entity_resolution_confidence measures DOCUMENT grounding (is this
    claim tied to a real source?), not WORLD grounding (is that source still
    an accurate description of the current state of affairs?) — the second
    check (world_state_freshness) is what catches the gap the first one misses.
    """
    # high token-level confidence is not the same signal as grounding
    if entity_resolution_confidence < 0.7:
        return "FLAG: entity/referent not confidently resolved to a real-world record"
    if world_state_freshness > MAX_STALENESS_THRESHOLD:
        return "FLAG: underlying record may be stale relative to the actual case"
    return "PROCEED: grounding checks passed — still requires human semantic sign-off"
