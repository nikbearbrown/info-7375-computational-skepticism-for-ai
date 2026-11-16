"""films.py - the thirteen films of the playlist "Computational Skepticism, Exam Prep".

One film per terminology deck in glossary/decks/. Films are never numbered for the viewer;
the two-digit key is the deck's file prefix and is used only for paths.
"""
from pathlib import Path

COURSE = Path(__file__).resolve().parents[3]
BOOKS = COURSE.parent
TOOLKIT = BOOKS / "brutalist.art"
HERE = COURSE / "youtube" / "exam-prep-deck-films"
PLAYLIST = "Computational Skepticism, Exam Prep"
COURSE_NAME = "INFO 7375 Computational Skepticism for AI"

# nn: (deck file, topic as spoken and shown, card title lines, chapter file, on the exam?)
_F = {
    "01": ("01 The skeptic's toolkit.html", "The Skeptic's Toolkit", ["Key Terms:", "The Skeptic's Toolkit"], "01-the-skeptics-toolkit.md", True),
    "02": ("02 The confidence illusion.html", "The Confidence Illusion", ["Key Terms:", "The Confidence", "Illusion"], "02-probability-uncertainty-and-the-confidence-illusion.md", True),
    "03": ("03 Data validation.html", "Data Validation", ["Key Terms:", "Data Validation"], "03-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md", True),
    "04": ("04 Robustness.html", "Robustness", ["Key Terms:", "Robustness"], "04-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md", True),
    "05": ("05 Model explainability.html", "Model Explainability", ["Key Terms:", "Model Explainability"], "05-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md", True),
    "06": ("06 Bias.html", "Bias", ["Key Terms:", "Bias"], "06-bias-where-it-enters-and-who-is-responsible.md", True),
    "07": ("07 Fairness metrics.html", "Fairness Metrics", ["Key Terms:", "Fairness Metrics"], "07-fairness-metrics-choosing-a-definition-and-defending-it.md", True),
    "08": ("08 Validating agentic AI.html", "Validating Agentic AI", ["Key Terms:", "Validating Agentic AI"], "08-validating-agentic-ai-when-autonomous-systems-misbehave.md", True),
    "09": ("09 Delegation and trust.html", "Delegation and Trust", ["Key Terms:", "Delegation and Trust"], "09-delegation-trust-and-the-supervisory-role.md", True),
    "10": ("10 Visualization under validation.html", "Visualization Under Validation", ["Key Terms:", "Visualization", "Under Validation"], "10-visualization-under-validation-honest-misleading-and-the-choices-between.md", False),
    "11": ("11 Communicating uncertainty.html", "Communicating Uncertainty", ["Key Terms:", "Communicating", "Uncertainty"], "11-communicating-uncertainty-calibrating-claims-to-evidence.md", True),
    "12": ("12 Accountability.html", "Accountability", ["Key Terms:", "Accountability"], "12-accountability-who-is-responsible-when-the-system-fails.md", True),
    "13": ("13 The limits of AI.html", "The Limits of AI", ["Key Terms:", "The Limits of AI"], "13-the-limits-of-ai-what-the-tools-cannot-do.md", False),
}


def slugify(s):
    import re
    return re.sub(r"[^a-z0-9]+", "-", s.lower().replace("'", "")).strip("-")


def film(nn):
    deck, topic, lines, chapter, on_exam = _F[nn]
    title = f"Key Terms: {topic}"
    slug = f"claude-liam-lecture-key-terms-{slugify(topic)}"
    # A film-only edit of a deck (Bear's change for the film) lives in exam-prep-deck-films/decks/ and wins over the study deck.
    film_copy = HERE / "decks" / deck
    deck_path = film_copy if film_copy.exists() else COURSE / "glossary" / "decks" / deck
    return {"nn": nn, "deck_file": deck_path, "study_deck": COURSE / "glossary" / "decks" / deck, "topic": topic, "title": title, "title_lines": lines,
            "chapter": COURSE / "chapters" / chapter, "on_exam": on_exam, "slug": slug, "reel": COURSE / "youtube" / slug,
            "extract": HERE / "extract" / nn}


ALL = sorted(_F)

# Voice-only pronunciations (word or phrase -> IPA) for Kokoro, each checked with the toolkit's phonemizer on 2026-11-11.
# Only what the voice gets wrong is listed. Narration text and captions keep the normal spelling.
# "A-I" is keyed on the Liam dictionary's respelling of AI: after "of" the phonemizer otherwise says "ov-uh-eye".
PRONOUNCE = {
    "COMPAS": "kˈʌmpəs", "MCAR": "ˌɛmkˈɑːɹ", "ECE": "ˌiːsˌiːˈiː", "EDA": "ˌiːdˌiːˈeɪ", "CI": "sˌiːˈaɪ",
    "Lipschitz": "lˈɪpʃɪts", "Searle": "sˈɜːl", "Searle's": "sˈɜːlz", "Bayesian": "bˈeɪziən", "Cauchy": "koʊʃˈiː",
    "Mediocristan": "mˌiːdiˈɑːkɹɪstˌæn", "Extremistan": "ɛkstɹˈiːmɪstˌæn",
    "Descartes": "deɪkˈɑːɹt", "Popperian": "pɑːpˈɪɹiən", "Kantian": "kˈæntiən", "COVID": "kˈoʊvɪd", "Gaussian": "ɡˈaʊsiən",
    "logits": "lˈoʊdʒɪts", "logit": "lˈoʊdʒɪt", "Gebru": "ɡˈɛbɹuː", "Use Disclosure": "jˈuːs dɪsklˈoʊʒɚ",
    "Aleatoric": "ˌeɪliətˈɔːɹɪk", "Epistemic": "ˌɛpɪstˈiːmɪk", "McLuhan": "məklˈuːən", "axes": "ˈæksiːz", "Matthias": "mɑːtˈiːəs",
}
AI_FIX = {"A-I": "ˈeɪaɪ", "A-I's": "ˈeɪaɪz"}

# The short line printed on the title card under the title (the template allows 52 characters).
CARD_LINE = {
    "01": "25 terms for checking what an AI system tells you.",
    "02": "33 terms for what a confident number tells you.",
    "03": "30 terms for what a dataset can and cannot show.",
    "04": "34 terms for testing what a model really learned.",
    "05": "31 terms for judging a model's explanation.",
    "06": "33 terms for where bias enters and who owns it.",
    "07": "31 terms for defending a fairness definition.",
    "08": "32 terms for checking what an AI agent really did.",
    "09": "33 terms for reading a delegation case.",
    "10": "32 terms for honest charts and misleading ones.",
    "11": "34 terms for matching a claim to its evidence.",
    "12": "30 terms for who answers when an AI system fails.",
    "13": "34 terms for what AI tools cannot do.",
}
assert all(len(v) <= 52 for v in CARD_LINE.values())
