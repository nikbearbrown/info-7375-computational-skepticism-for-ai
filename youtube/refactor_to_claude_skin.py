#!/usr/bin/env python3
"""
Refactor all 13 Computational Skepticism CLI beat sheets from
NikBearBrown terminal skin → Claude skin (ClaudeComposerAsk /
ClaudeCodeBeat / ClaudeTitleOutro) and write updated beat_sheet.json
files in place. Back up originals to beat_sheet.nbb.json.

Run from: computational-skepticism-for-ai/youtube/
"""

import json, shutil
from pathlib import Path

BASE = Path(__file__).parent

# Per-video thesis questions for B00 ClaudeComposerAsk cold open.
# Format: slug → (greeting, thesis_command, runningText)
THESIS = {
    "claude-liam-cli-calibration-curve-auditor": (
        "Hola, Bear",
        "Does a high AUC actually mean your model's confidence is trustworthy?",
        "auditing the calibration gap…",
    ),
    "claude-liam-cli-base-rate-bayes-calculator": (
        "Jambo, Bear",
        "Your model fires on 18 percent of patients. What's the chance any one alert is real?",
        "computing the base-rate reality…",
    ),
    "claude-liam-cli-fairness-impossibility-demonstrator": (
        "Bonjour, Bear",
        "Can a classifier be simultaneously fair to every group — or is fairness impossible by definition?",
        "deriving the impossibility…",
    ),
    "claude-liam-cli-adversarial-perturbation-detector": (
        "Namaste, Bear",
        "Can one invisible pixel flip a confident AI classifier to the wrong class?",
        "building the adversarial probe…",
    ),
    "claude-liam-cli-agent-self-verification-failure": (
        "Hola, Bear",
        "If an AI agent checks its own work, does it catch its own errors — or just confirm them?",
        "running the self-verification test…",
    ),
    "claude-liam-cli-distribution-shift-detector": (
        "Sawubona, Bear",
        "After 999 days of good predictions, how would you know the world just changed?",
        "computing population stability index…",
    ),
    "claude-liam-cli-confusion-matrix-audit": (
        "Hej, Bear",
        "What does 94 percent accuracy actually hide when most samples are one class?",
        "auditing the confusion matrix…",
    ),
    "claude-liam-cli-llm-prompt-sensitivity-tester": (
        "Olá, Bear",
        "Does rewording one sentence change Claude's legal answer — even when the core question stays the same?",
        "probing prompt sensitivity…",
    ),
    "claude-liam-cli-gate-behavior-test-harness": (
        "Ciao, Bear",
        "What is the difference between a scoring gate and a scoring vote — and how do you prove which one you have?",
        "generating gate-behavior tests…",
    ),
    "claude-liam-cli-entity-resolution-matcher": (
        "Hola, Bear",
        "How many join matches are you losing to legal suffixes — Acme Inc vs ACME Incorporated?",
        "computing join-coverage delta…",
    ),
    "claude-liam-cli-verified-data-output-linter": (
        "Merhaba, Bear",
        "How do you automatically catch a fabricated number in a report before a human reads it?",
        "scanning for unsourced claims…",
    ),
    "claude-liam-cli-reliability-diagram-own-model": (
        "Hola, Bear",
        "When your model says 94 percent confidence — does that mean 94 of 100 predictions at that level are right?",
        "plotting the reliability diagram…",
    ),
    "claude-liam-cli-prediction-lock-harness": (
        "Wagwan, Bear",
        "If you can edit your prediction after seeing the result — is it still a prediction?",
        "building the hash-locked prediction…",
    ),
}

SUBLINES = {
    "claude-liam-cli-calibration-curve-auditor":       "AUC ranks — calibration tells the truth",
    "claude-liam-cli-base-rate-bayes-calculator":      "the base rate is the number the model can't know",
    "claude-liam-cli-fairness-impossibility-demonstrator": "in four lines of Python",
    "claude-liam-cli-adversarial-perturbation-detector": "the model learned the right pattern for the wrong reasons",
    "claude-liam-cli-agent-self-verification-failure": "self-check is the same operation applied to its own output",
    "claude-liam-cli-distribution-shift-detector":     "confidence about the record, not the world",
    "claude-liam-cli-confusion-matrix-audit":          "specify failure before the result means anything",
    "claude-liam-cli-llm-prompt-sensitivity-tester":   "adversarial robustness for language models",
    "claude-liam-cli-gate-behavior-test-harness":      "a gate zeroes — it does not dampen",
    "claude-liam-cli-entity-resolution-matcher":       "coverage you can't trace is not coverage",
    "claude-liam-cli-verified-data-output-linter":     "the two shapes fabrication takes",
    "claude-liam-cli-reliability-diagram-own-model":   "calibration on training doesn't survive a shift",
    "claude-liam-cli-prediction-lock-harness":         "the information lives in the gap",
}


def transform_props_ask(old_props: dict) -> dict:
    """NikBearBrownTerminalAsk → ClaudeComposerAsk props (non-B00 beats)."""
    return {
        "command":      old_props.get("command", ""),
        "topic":        old_props.get("topic", ""),
        "segment":      old_props.get("segment", ""),
        "greeting":     "",
        "runningText":  old_props.get("runningText", "running…"),
        "output":       [],
        "folderLabel":  "@NikBearBrown",
        "modelLabel":   "Fable 5",
        "effortLabel":  "High",
    }


def transform_props_open(old_props: dict, slug: str) -> dict:
    """NikBearBrownOpen → ClaudeComposerAsk props (B00 cold open)."""
    greeting, command, running = THESIS.get(slug, ("Hola, Bear", "", "working…"))
    lines = old_props.get("lines", ["", ""])
    segment = lines[1] if len(lines) > 1 else old_props.get("topic", "")
    return {
        "command":      command,
        "topic":        old_props.get("topic", "COMPUTATIONAL SKEPTICISM"),
        "segment":      segment,
        "greeting":     greeting,
        "runningText":  running,
        "output":       [],
        "folderLabel":  "@NikBearBrown",
        "modelLabel":   "Fable 5",
        "effortLabel":  "High",
    }


def transform_props_code(old_props: dict) -> dict:
    """NikBearBrownCodeBlock → ClaudeCodeBeat props."""
    return {
        "title":      old_props.get("filename", "script.py"),
        "code":       old_props.get("code", ""),
        "sparkLine":  old_props.get("segment", ""),
    }


def transform_props_outro(old_props: dict, title: str, slug: str) -> dict:
    """NikBearBrownOutro → ClaudeTitleOutro props."""
    return {
        "title":   title,
        "handle":  "@NikBearBrown",
        "subline": SUBLINES.get(slug, "build it with a cli"),
    }


PATTERN_MAP = {
    "NikBearBrownOpen":        "ClaudeComposerAsk",
    "NikBearBrownTerminalAsk": "ClaudeComposerAsk",
    "NikBearBrownCodeBlock":   "ClaudeCodeBeat",
    "NikBearBrownOutro":       "ClaudeTitleOutro",
}


def refactor_beat(beat: dict, slug: str, title: str) -> dict:
    shot = beat.get("shot", {})
    remotion = shot.get("remotion", {})
    old_pat = remotion.get("pattern", "")

    if old_pat not in PATTERN_MAP:
        return beat  # pass through unchanged

    new_pat = PATTERN_MAP[old_pat]
    old_props = remotion.get("props", {})

    bid = beat.get("beat_id", "")
    if old_pat == "NikBearBrownOpen":
        new_props = transform_props_open(old_props, slug)
    elif old_pat == "NikBearBrownTerminalAsk":
        new_props = transform_props_ask(old_props)
    elif old_pat == "NikBearBrownCodeBlock":
        new_props = transform_props_code(old_props)
    elif old_pat == "NikBearBrownOutro":
        new_props = transform_props_outro(old_props, title, slug)
    else:
        new_props = old_props

    new_remotion = dict(remotion)
    new_remotion["pattern"] = new_pat
    new_remotion["props"] = new_props
    # clear stale rendered path — will be regenerated
    new_remotion.pop("rendered", None)

    new_shot = dict(shot)
    new_shot["remotion"] = new_remotion

    new_beat = dict(beat)
    new_beat["shot"] = new_shot
    # also clear stale build status so pipeline re-runs the beat
    if "build" in new_beat and new_beat["build"].get("status") == "VIDEO":
        new_beat["build"]["status"] = "NEEDS-RENDER"
        new_beat["build"]["src"] = None
        new_beat["build"]["filled_by"] = None

    # Update narration_text for B00 to match Claude register
    if old_pat == "NikBearBrownOpen":
        _, thesis_q, _ = THESIS.get(slug, ("", "", ""))
        new_beat["narration_text"] = thesis_q or new_beat.get("narration_text", "")

    return new_beat


def refactor_metadata(meta: dict) -> dict:
    m = dict(meta)
    m["style_preset"] = "claude"
    m["palette"] = "claude"
    m.pop("_variant_todo", None)
    # Keep voice NikBearBrown (Teardown register) and kokoro am_onyx
    return m


def refactor_sheet(path: Path) -> None:
    slug = path.parent.name
    print(f"  refactoring {slug}…")

    data = json.loads(path.read_text())
    title = data["metadata"].get("title", slug)

    # back up original as .nbb.json (skip if already backed up)
    backup = path.with_name("beat_sheet.nbb.json")
    if not backup.exists():
        shutil.copy(path, backup)

    data["metadata"] = refactor_metadata(data["metadata"])
    data["beats"] = [refactor_beat(b, slug, title) for b in data["beats"]]

    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"    → written ({len(data['beats'])} beats)")


def main():
    slugs = sorted([
        "claude-liam-cli-calibration-curve-auditor",
        "claude-liam-cli-base-rate-bayes-calculator",
        "claude-liam-cli-fairness-impossibility-demonstrator",
        "claude-liam-cli-adversarial-perturbation-detector",
        "claude-liam-cli-agent-self-verification-failure",
        "claude-liam-cli-distribution-shift-detector",
        "claude-liam-cli-confusion-matrix-audit",
        "claude-liam-cli-llm-prompt-sensitivity-tester",
        "claude-liam-cli-gate-behavior-test-harness",
        "claude-liam-cli-entity-resolution-matcher",
        "claude-liam-cli-verified-data-output-linter",
        "claude-liam-cli-reliability-diagram-own-model",
        "claude-liam-cli-prediction-lock-harness",
    ])

    print(f"Refactoring {len(slugs)} beat sheets to Claude skin…\n")
    missing = []
    for slug in slugs:
        bs = BASE / slug / "beat_sheet.json"
        if not bs.exists():
            print(f"  MISSING: {slug}/beat_sheet.json — skipping")
            missing.append(slug)
            continue
        refactor_sheet(bs)

    print(f"\nDone. {len(slugs) - len(missing)}/{len(slugs)} refactored.")
    if missing:
        print("Missing:", missing)


if __name__ == "__main__":
    main()
