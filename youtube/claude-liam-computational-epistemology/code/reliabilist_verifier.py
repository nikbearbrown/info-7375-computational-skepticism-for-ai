# reliabilist_verifier.py — shown on screen in B18 (Onda code-block).
# Verbatim from the source doc (SOURCE.md, Part 2). The beat's highlight:
# should_trust() — the empirical track record gates trust; a confident
# model with a bad history is still not trusted.

class ReliabilistVerifier:
    """
    Externalist core: track empirical reliability of a given
    generation process/prompt-template/model-version combination,
    independent of any single output's stated justification.
    """
    def __init__(self):
        self.track_record = {}  # (model, prompt_template) -> [outcomes]

    def log_outcome(self, process_id, was_correct: bool):
        self.track_record.setdefault(process_id, []).append(was_correct)

    def reliability(self, process_id):
        history = self.track_record.get(process_id, [])
        if len(history) < 10:
            return None  # insufficient track record, don't trust yet
        return sum(history) / len(history)

    def should_trust(self, process_id, internalist_confidence: float):
        r = self.reliability(process_id)
        if r is None:
            return "INSUFFICIENT_TRACK_RECORD"
        # externalist reliability gates the internalist self-report;
        # a confident model with a bad track record is still not trusted
        return "TRUST" if (r > 0.85) else "VERIFY_MANUALLY"
