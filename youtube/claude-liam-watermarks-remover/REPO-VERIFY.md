# REPO-VERIFY — claude-liam-watermarks-remover

Repo: `guillaumemeyer/watermarks-remover` · local clone `books/github/watermarks-remover`
Verified: 2026-08-14. Every scene below is Rung 1 — computed from the repo, no hand-authored counts.

---

## Scene 1 — `GitHubRepoHero`

```
git remote -v ; git rev-list --count HEAD ; head -60 README.md
```

| Prop | Value |
|---|---|
| owner/repo | `guillaumemeyer/watermarks-remover` |
| headline | Agent skill + stdlib Python scripts to strip multi-vendor AI provenance marks from text and files |
| release | v0.4.0 |
| commits | 49 |
| license | present (`LICENSE`), CI badge green, `SECURITY.md` + `CODE_OF_CONDUCT.md` present |

## Scene 2 — `GitHubStructureMap`

```
wc -l skills/remove-ai-marks/scripts/*.py | sort -rn
git ls-files skills tests .github | ...
```

| Path | LOC |
|---|---|
| `container_meta.py` | 855 |
| `image_meta.py` | 668 |
| `text_unicode.py` | 449 |
| `rewrite_text.py` | 436 |
| `common.py` | 428 |
| `audit_website.py` | 265 |
| `clean_ctrlregen.py` | 212 |
| `clean_file.py` | 186 |
| `clean_image.py` | 153 |
| `audit_lib.py` | 150 |
| `score_synthid.py` | 133 |
| `inspect_file.py` | 119 |
| `audit_dir.py` | 108 |
| `clean_text.py` | 84 |
| `inspect_image.py` | 72 |
| `inspect_text.py` | 52 |
| **scripts total** | **4,370** |

`skills/` 26 files / 5,155 lines · `tests/` 14 files / **1,858 lines** · `.github/` 7 files / 217 lines · references + SKILL.md **512 lines of docs**.

**Assertion:** LOC sums match `wc -l`. Test-to-script ratio is 1,858 : 4,370 — roughly 0.43, which is a real test suite, not a token one.

## Scene 3 — `GitHubCallChain`

Real edges, every one a literal `from X import` / `import X` line:

```
audit_dir      → audit_lib, common
audit_lib      → common, container_meta, image_meta, inspect_file, text_unicode
audit_website  → audit_lib, common
clean_ctrlregen→ common
clean_file     → common, container_meta, image_meta, text_unicode
clean_image    → common, image_meta
clean_text     → common, text_unicode
container_meta → common, image_meta
image_meta     → common
inspect_file   → common, container_meta, image_meta, text_unicode
inspect_image  → common, image_meta
inspect_text   → common, text_unicode
rewrite_text   → common, text_unicode
```

Imported-by: **`common` 13** · `text_unicode` 6 · `image_meta` 6 · `container_meta` 3 · `audit_lib` 2 · `inspect_file` 1.

**Load-bearing file: `common.py`** — 428 LOC, imported by 13 of 16 scripts. Every path routes through it.

**The shape worth naming on screen:** the graph is a clean three-tier fan — one shared core, two format engines (`text_unicode`, `image_meta`), and thin CLI leaves. `inspect_*` and `clean_*` are paired at every layer, so **inspection and removal are separate entry points against the same engine.** You can run the whole thing read-only.

## Scene 4 — `GitHubChurn`

```
git log --date=format:'%m-%d' --pretty=%ad | sort | uniq -c
```

| Day | Commits |
|---|---|
| 2026-08-11 | **11** |
| 2026-08-12 | 20 |
| 2026-08-13 | 17 |
| 2026-08-14 | 1 |

**Assertion:** sums to 49 == `git rev-list --count HEAD`. No `frozen` year — the entire history is four days.

**The fact the churn beat exists for:** the first eleven commits land on **11 August 2026** — the day Anthropic announced global text watermarking. From standing start to v0.4.0 with CI, a test suite and two Dockerfiles in **four days**.

## Scene 5 — `GitHubCodeViewer` — THE READ GATE

File: `skills/remove-ai-marks/references/ethics.md`, 32 lines, read in full.

This is the deliberate substitution for reading a strip implementation, and it is the *better* read for a Teardown: the interesting design decision in this repo is not how the bytes come off, it's that the author wrote a scope boundary and shipped it as a reference the agent loads. Byte-exact slices to render:

- **L5–L10, "Appropriate"** — privacy, engineering hygiene (invisible Unicode breaking diffs, search and paste), research, cleaning your own drafts.
- **L12–L16, "Not appropriate"** — *"Academic fraud or misrepresenting AI assistance where disclosure is required"* · *"Circumventing lawful transparency or platform disclosure rules"* · *"Claiming cleaned content is 'human-written' for compliance theater."*
- **L18** — *"A removed mark does not mean the content was never AI-assisted. Use this toolkit honestly."*
- **L22–L26, "Honesty in reports"** — the three-way split the tool must report: verifiable removals, best-effort statistical rewrite (**"no gold undetection claim"**), and out-of-scope channels.
- **L28** — *"Do not imply that a successful C2PA/metadata strip means 'no AI provenance left.' Soft-bound and SynthID-class media signals can survive."*

**Assertion:** every rendered line byte-identical to `git show main:skills/remove-ai-marks/references/ethics.md` at the stated range.

**The Teardown judgment:** a removal tool that ships a document telling you removal proves nothing is making the same argument this channel has been making all week from the other direction. The detector's silence is not evidence of absence — and neither is the remover's success.

## Scene 6 — `GitHubCodeDiff`

Commit: `256d90d` — *"Refuse binary input in the text-only tools (#24)"*, the HEAD commit.  
Verified: `git show 256d90d --stat` and `git show 256d90d -- skills/remove-ai-marks/scripts/inspect_text.py`, 2026-08-14.

**Displayed file:** `skills/remove-ai-marks/scripts/inspect_text.py`  
**Badge (full commit):** `8 files · +482 −16`  
**Hunk chosen:** `@@ -28,9 +28,14 @@` — `--force-text` argument added to parser, `allow_binary` wired into `read_text_input` call.

Camera-worthy hunk (byte-exact from `git show 256d90d -- inspect_text.py`):

```
 28    action="store_true",
 29    help="Flag emoji presentation selectors/ZWJ even after an emoji base (paranoid)",
 30 )
+31 p.add_argument(
+32     "--force-text",
+33     action="store_true",
+34     help="Scan even when the input looks like a binary container",
+35 )
 36 args = p.parse_args()
 37
-38 text = read_text_input(args.path)
+38 text = read_text_input(args.path, allow_binary=args.force_text)
```

**Why this hunk:** shows the public surface of the guard — a new `--force-text` flag wired to `allow_binary`. The implementation (`looks_binary`, `guard_binary`) in common.py is 100 lines of additions; the inspect_text.py hunk is 14 lines and captures the design decision (opt-in bypass) without requiring scroll.

**Narration note:** the `clean_text.py` pre-guard bug is more dramatic (writes mangled bytes back, corrupts .docx silently), but the file stat for clean_text.py is `8 +-`. inspect_text.py at `7 +-` carries the same design signal more cleanly.

**Assertion:** rendered gutters and ± lines match `git show 256d90d` byte-exactly; badge `8 files · +482 −16` matches `--stat` output.

---

## Scripting gaps

None. All six scenes are fully verified.

## What the reel does NOT do

Not a restriction on the repo, a choice about what makes the better film: the body carries **structure, history, scope and dependency posture**, not strip mechanics. The removal implementations (`text_unicode.py`, `image_meta.py`, `container_meta.py`) appear in the StructureMap and CallChain as nodes with real LOC — named, sized, and placed — and are not opened line-by-line. The READ gate spends itself on `ethics.md` instead, which is where the actual design decision lives.

## The dependency finding

```
grep -rhE "^(import|from) " skills --include="*.py" | awk '{print $2}' | sort -u
cat requirements-dev.txt
```

Every import across all 16 scripts: `__future__`, `argparse`, `collections`, `dataclasses`, `gzip`, `io`, `json`, `os`, `pathlib`, `re`, `struct`, `subprocess`, `sys`, `tempfile`, `typing`, `unicodedata`, `urllib.*` — **plus the repo's own modules and nothing else.** `requirements-dev.txt` pins exactly two packages: `pytest==9.1.1` and `pip-audit==2.10.1`, both test tooling.

**The core is pure Python standard library.** No model, no GPU, no third-party package. Layer B (statistical rewrite) and CtrlRegen are optional and isolated behind their own requirements files and Dockerfiles.

That is the reel's verdict beat, and it is a fact about the dependency graph, not an instruction: **the marks a major lab shipped worldwide come off with `re` and `unicodedata`.**

---

## Plan

**Title:** Four Days, No Dependencies
**Skill:** `git-explainer` at deep length · **Channel:** `claude-liam`, Kokoro `am_onyx`, free · **Register:** Teardown
**Reel:** `computational-skepticism-for-ai/youtube/claude-liam-watermarks-remover/`
**Estimated runtime:** 7:00–8:00 · ~40 beats

Six scenes in the fixed order, Manim for the four quantitative beats (LOC hotspot, the import fan, the four-day churn, the dependency count). Rung 1 throughout — no gen-AI, no doodle, no pantry, no rights escalations.

**Owning book:** `computational-skepticism-for-ai`. This is the fourth piece in the arc — the Nature paper's claim, the forensic-readiness score, the KGW reference implementation, and now the counter-tool. It belongs with its siblings.

Gates: author `beat_sheet.json` → factcheck → **GATE P** (full-length slate previz, no audio spend) → hand back. Never publishes.
