# FACTCHECK.md — claude-liam-watermarks-remover
## Four Days, No Dependencies

Status: **GATE F SIGNED — 2026-08-14 by Bear (Claude Code session). 19 rows, all ✓ PASS or CORRECTED or EXEMPT.**
All structural counts verified from the repo clone at `books/github/watermarks-remover HEAD 256d90d`. Ethics.md quotations are byte-exact against `git show`. External date claim (Anthropic announcement) is flagged EXEMPT — Bear to verify before ship.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B00, B01, B04, B15–B17, BVDT | 49 commits | ✓ PASS | `git rev-list --count HEAD → 49` | — |
| 2 | B00, B04–B07, B34 | 4,370 LOC in 16 scripts | ✓ PASS | `wc -l skills/remove-ai-marks/scripts/*.py | sort -rn → 4370 total (16 files)` | — |
| 3 | B07 Manim bars | container_meta 855, image_meta 668, text_unicode 449, rewrite_text 436, common 428 | ✓ PASS | `wc -l` per-file from clone; same source as row 2 | — |
| 4 | B00, B04, B18, B19 | 1,858 lines of tests | ✓ PASS | `git ls-files tests/ | xargs wc -l → 1858 total` (includes fixtures; see Part 1 detail) | — |
| 5 | B04 | 512 lines of docs | ✓ PASS | `wc -l skills/remove-ai-marks/references/*.md skills/remove-ai-marks/SKILL.md → 512` | — |
| 6 | B04, B18, B19 | 2 Dockerfiles | ✓ PASS | `find . -name "Dockerfile*" → Dockerfile.ctrlregen, Dockerfile.synthid` | — |
| 7 | B04 | 7 tags v0.0.1–v0.4.0 | CORRECTED | `git for-each-ref refs/tags → 7 entries`; draft said "first tag v0.4.0" — fixed to "Seven tags from v0.0.1 to v0.4.0" | — |
| 8 | B15–B18 | 11/20/17/1 commits by day | ✓ PASS | `git log --date=format:'%m-%d' --pretty=%ad | sort | uniq -c → 11/20/17/1, total 49` | — |
| 9 | B18, on-screen | v0.4.0 tagged Aug 13 | CORRECTED | `git for-each-ref → v0.4.0 2026-08-13`; draft had Aug 14 — fixed | — |
| 10 | B17 Manim | Tag marker at Aug 13 cumulative=48 | CORRECTED | Same ref; draft placed tag at Aug 14 — moved to Aug 13 in `animated_graphics.py` | — |
| 11 | B09, B11, B12 | common.py imported by 13 scripts | ✓ PASS | `grep -rhE "^(import|from) " skills --include='*.py' | awk '{print $2}' | grep "^common$" | wc -l → 13` | — |
| 12 | B12 | text_unicode and image_meta each imported by 6; container_meta 3, audit_lib 2, inspect_file 1 | ✓ PASS | Same grep, per-module filters | — |
| 13 | B20, B21 | ethics.md 32 lines | ✓ PASS | `wc -l ethics.md → 32` | — |
| 14 | B23 | L5–L10 Appropriate section (verbatim) | ✓ PASS | Byte-exact vs `git show main:skills/.../ethics.md` | — |
| 15 | B24 | L12–L16 Not appropriate section (verbatim) | ✓ PASS | Byte-exact vs same source | — |
| 16 | B25 | L18 "A removed mark does not mean…" (verbatim) | ✓ PASS | Byte-exact first sentence; bold markers stripped for display | — |
| 17 | B26 | L22–L26 Honesty in reports (paraphrase) | ✓ PASS | Content matches source; paraphrase is labeled, not claimed verbatim | — |
| 18 | B27 | L28 "Do not imply…Soft-bound…" (partial quote) | EXEMPT | First two sentences only; tail omitted and inner quotes simplified; narration says "verbatim" — Bear to decide: (a) remove "Verbatim:" or (b) extend display | Remove "Verbatim:" from narration or extend on-screen to full L28 |
| 19 | B18 | "Anthropic announced global text watermarking" on Aug 11, 2026 | EXEMPT | External event — not verifiable from git; stated as coincidence; B19 narration frames it explicitly as such | Bear to verify before ship |

---

Reel HEAD: `256d90d` · repo clone: `books/github/watermarks-remover`  
All commands run from the clone root unless noted.  
Status key: **PASS** verified from repo · **CORRECTED** wrong in draft, fixed before this file · **NOTE** editorial disclosure · **EXTERNAL** not verifiable from git

---

## Part 1 — Structural counts

### 49 commits
**PASS**
```
git rev-list --count HEAD
→ 49
```
Beats: B00, B01, B04, B15, B16, B17, BVDT.

---

### 4,370 LOC in 16 scripts
**PASS**
```
wc -l skills/remove-ai-marks/scripts/*.py | sort -rn
→ 4370 total (16 files)
```
Beats: B00, B04, B05, B06 (GitHubStructureMap), B07 (Manim), B34.

---

### Top-5 script LOC (B07 Manim bar chart)
**PASS**

| Script | LOC | Beat |
|---|---|---|
| `container_meta.py` | 855 | B07 bar, B05/B06 body text |
| `image_meta.py` | 668 | B07 bar |
| `text_unicode.py` | 449 | B07 bar |
| `rewrite_text.py` | 436 | B07 bar |
| `common.py` | 428 | B07 bar, B09/B11/B12 |

Source: `wc -l skills/remove-ai-marks/scripts/*.py | sort -rn`

---

### 1,858 lines of tests
**PASS** — with counting method disclosure

`wc -l tests/*.py` yields 1,832. The figure 1,858 (B00, B04, B18, B19) uses:
```
git ls-files tests/ | xargs wc -l
→ 1858 total
```
Difference: `git ls-files tests/` includes 4 fixture files in `tests/fixtures/`
(`sample_ai.html`, `sample_ai.md`, `sample_meta.svg`, `sample_watermarked.txt`)
that `tests/*.py` does not. The 1,858 figure is from REPO-VERIFY.md (Rung 1) and
counts all tracked files in `tests/`; that is the correct number for "lines in
the test suite including fixtures."

---

### 512 lines of docs
**PASS**
```
wc -l skills/remove-ai-marks/references/*.md skills/remove-ai-marks/SKILL.md
→ 512 total (5 reference files + SKILL.md)
```
Beat: B04.

---

### 2 Dockerfiles
**PASS**
```
find . -name "Dockerfile*"
→ ./Dockerfile.ctrlregen
→ ./Dockerfile.synthid
```
Beats: B04, B18, B19.

---

### CI badge green
**PASS** — REPO-VERIFY.md scene 1 confirms CI badge green at verification time
(2026-08-14). The badge is a live shield; content is correct at clone date.
Not re-polled after 2026-08-14.

---

## Part 2 — Commit churn

### 11 / 20 / 17 / 1 by day
**PASS**
```
git log --date=format:'%m-%d' --pretty=%ad | sort | uniq -c
→ 11  08-11
→ 20  08-12
→ 17  08-13
→  1  08-14
   total: 49 = git rev-list --count HEAD ✓
```
Beats: B15, B16, B17, B18.

---

### v0.4.0 tag date — CORRECTED
**CORRECTED** — original draft had B18 on-screen "v0.4.0 tagged Aug 14". Wrong.
```
git for-each-ref --format='%(refname:short) %(creatordate:short)' refs/tags | sort
→ v0.4.0 2026-08-13
```
v0.4.0 points to commit `c267d78` (2026-08-13). Two commits follow the tag:
`e7e3b4e` (Aug 13, docs shields) and `256d90d` (Aug 14, HEAD).

Fix applied: B18 on-screen text changed to "v0.4.0 tagged Aug 13". B16 narration
updated from "One on August 14. Then the tag." to "Seventeen on August 13 —
including the v0.4.0 tag. One more on August 14, after the tag, and that is HEAD."

---

### 7 tags, not 1 — CORRECTED
**CORRECTED** — original draft B04 narration said "v0.4.0 as the first release
tag" and on-screen showed "v0.4.0 — first tag, first version, four days". Wrong.
```
git for-each-ref --format='%(refname:short) %(creatordate:short)' refs/tags | sort
→ v0.0.1 2026-08-11
→ v0.1.0 2026-08-11
→ v0.2.0 2026-08-12
→ v0.3.0 2026-08-12
→ v0.3.1 2026-08-12
→ v0.3.2 2026-08-12
→ v0.4.0 2026-08-13
```
v0.4.0 is the seventh tag. The first was v0.0.1 on Aug 11.

Fix applied: B04 narration rewritten to "Seven tags from v0.0.1 to v0.4.0 — the
author iterated through four release cycles in the same window." On-screen line
changed to "v0.0.1 through v0.4.0 — 7 tags in four days".

---

### B17 Manim tag marker — CORRECTED
**CORRECTED** — original B17_FourDayChurn.DAYS placed `"v0.4.0"` tag annotation
at Aug 14 (cumulative=49). Tag is Aug 13 (cumulative=48).

Fix applied in `animated_graphics.py`:
```python
("Aug 13", 48, "v0.4.0", True),   # tag — created 2026-08-13
("Aug 14", 49, "HEAD",   False),   # 256d90d — one commit after tag
```

---

## Part 3 — Architecture (import counts)

### common.py imported by 13 scripts
**PASS**
```
grep -rhE "^(import|from) " skills --include="*.py" \
  | awk '{print $2}' | grep "^common$" | wc -l
→ 13
```
Beats: B09, B11, B12.

### text_unicode and image_meta each imported by 6
**PASS** — same grep, filter `^text_unicode$` → 6; `^image_meta$` → 6.
Beat: B12.

### container_meta imported by 3, audit_lib by 2, inspect_file by 1
**PASS** — same grep, respective filters.
Beat: B12.

---

## Part 4 — ethics.md quotations

### 32 lines
**PASS**
```
wc -l skills/remove-ai-marks/references/ethics.md
→ 32
```
Beats: B20, B21.

### L5–L10 "Appropriate" section (B23)
**PASS** — byte-exact against `git show main:skills/remove-ai-marks/references/ethics.md`:
```
L5   ## Appropriate
L6   (empty)
L7   - Privacy: strip tool/device/AI provenance from your own files before sharing
L8   - Engineering hygiene: remove invisible Unicode that breaks diffs, search, or paste
L9   - Research: understand how text and C2PA marks work across vendors
L10  - Cleaning your own drafts where policy allows unmarked local copies
```
B23 on-screen paraphrases; narration reads the bullet text. Any verbatim display
is byte-identical to the source.

### L12–L16 "Not appropriate" section (B24)
**PASS**
```
L12  ## Not appropriate
L13  (empty)
L14  - Academic fraud or misrepresenting AI assistance where disclosure is required
L15  - Circumventing lawful transparency or platform disclosure rules
L16  - Claiming cleaned content is "human-written" for compliance theater
```
B24 on-screen and narration match line-for-line.

### L18 (B25)
**PASS**
```
L18  A removed mark does **not** mean the content was never AI-assisted. Use this toolkit honestly.
```
Beat B25 renders this as two display lines, quoting "A removed mark does not mean
the content was never AI-assisted." and "Use this toolkit honestly." — the `**not**`
Markdown bold markers are stripped for display, content is otherwise verbatim.

### L22–L26 "Honesty in reports" (B26)
**PASS**
```
L22  Always separate:
L23  (empty)
L24  1. **Verifiable** removals (Unicode counts, metadata actions)
L25  2. **Best-effort** statistical rewrite (no gold undetection claim)
L26  3. **Optional / out-of-scope** channels (optional external pixel removal via CtrlRegen; …)
```
B26 paraphrases L26 for readability; L24 and L25 are rendered verbatim (bold
markers stripped). Any condensation is labeled "out-of-scope channels" without
claiming to quote L26 verbatim.

### L28 (B27) — NOTE: partial quote
**NOTE**
```
L28  Do not imply that a successful C2PA/metadata strip means "no AI provenance left."
     Soft-bound and SynthID-class media signals can survive. Point users at vendor
     verify tools when they need residual checks (see README *Residual risk after a clean*).
```
B27 on-screen displays only the first two sentences and omits the "Point users…"
sentence. The displayed text retains the inner quotes around "no AI provenance left"
in the source; the on-screen prop omits them for rendering simplicity. **Not
claimed verbatim.** Beat B27 narration says "verbatim" but applies only to the
first two sentences — the word "verbatim" should be removed from the narration
or scoped to the two displayed sentences. Bear to decide; the factual content is
correct as far as it goes.

---

## Part 5 — HEAD commit (Scene 6)

### 8 files · +482 −16 (B29, B30, B31)
**PASS**
```
git show 256d90d --stat
→ 8 files changed, 482 insertions(+), 16 deletions(-)
```

### 253 lines in tests/test_binary_guard.py (B31)
**PASS**
```
git show 256d90d --stat | grep test_binary_guard
→ tests/test_binary_guard.py | 253 ++++…
wc -l tests/test_binary_guard.py
→ 253
```

### --force-text hunk (B29 GitHubCodeDiff)
**PASS** — byte-exact from `git show 256d90d -- skills/remove-ai-marks/scripts/inspect_text.py`:
6 additions (+p.add_argument / --force-text / action / help / ) plus 1 deletion
(-read_text_input(args.path)) replaced by 1 addition (+read_text_input(args.path,
allow_binary=args.force_text)). Gutter numbers 28–30 context, + additions, 36–37
context, -/+ at 38 — match `git show` output exactly.

---

## Part 6 — Dependencies

### stdlib-only in core — CORRECTED CATEGORIES
**PASS** (core claim) — **CORRECTED** (enumerated list)

Full import list, computed from:
```
grep -rhE "^(import|from) " skills --include="*.py" | awk '{print $2}' | sort -u
```
Stdlib entries: `__future__`, `argparse`, `collections`, `dataclasses`, `gzip`,
`io`, `json`, `os`, `pathlib`, `re`, `struct`, `subprocess`, `sys`, `tempfile`,
`typing`, `unicodedata`, `urllib.error`, `urllib.parse`, `urllib.request`,
`xml.etree.ElementTree`, `zipfile`, `zlib`.

Own-repo entries: `audit_lib`, `common`, `container_meta`, `image_meta`,
`inspect_file`, `text_unicode`. No third-party packages.

**CORRECTED:** Original REPO-VERIFY.md stdlib list omitted `xml.etree.ElementTree`,
`zipfile`, `zlib`. These are all stdlib; the core claim ("stdlib only") is correct.
The B33 Manim CATEGORIES had `codecs` (not present in any import) and was missing
`xml.etree.ElementTree`, `zipfile`, `zlib`. Fixed in `animated_graphics.py` and
`beat_sheet.json`.

### requirements-dev.txt: pytest + pip-audit only
**PASS**
```
cat requirements-dev.txt
→ pytest==9.1.1
→ pip-audit==2.10.1
```
Beat: BVDT (LOCKED narration). No third-party runtime dependency pinned here.

### Test ratio 0.43 (B19)
**PASS** — 1,858 ÷ 4,370 = 0.4253 ≈ 0.43.

---

## Part 7 — The date coincidence

### Aug 11, 2026 as first commit date
**PASS**
```
git log --date=format:'%Y-%m-%d' --pretty=%ad | tail -1
→ 2026-08-11
git log --date=format:'%m-%d' --pretty=%ad | sort | uniq -c | head -1
→ 11  08-11
```

### "Anthropic announced global text watermarking" on Aug 11, 2026
**EXTERNAL** — not verifiable from the git repository. This is an external event
claim. B18 narration (LOCKED) states it as a date coincidence. B19 narration
explicitly says: "The date coincidence is verifiable from git log — we are stating
it as a coincidence, not a claim about the author's motive." That framing is
correct. The external date claim is sourced from the context window at session
time; Bear should verify it independently before the reel ships.

---

## Part 8 — BVDT locked narration

> "Every import across all sixteen scripts is standard library. The only pinned
> dependencies are pytest and pip-audit. The marks a major lab shipped worldwide
> come off with re and unicodedata."

Every clause verified:
- "sixteen scripts" — 16 Python files in `skills/remove-ai-marks/scripts/` **PASS**
- "every import is standard library" — see Part 6 **PASS**
- "only pinned dependencies are pytest and pip-audit" — see Part 6 **PASS**
- "come off with re and unicodedata" — text_unicode.py (the text strip engine)
  imports re and unicodedata; both are stdlib **PASS**

---

## Summary of corrections made to beat_sheet.json and animated_graphics.py

| ID | Where | Error | Fix |
|---|---|---|---|
| C1 | B04 narration | "v0.4.0 as the first release tag" | Rewritten: "Seven tags from v0.0.1 to v0.4.0" |
| C2 | B04 on-screen | "v0.4.0 — first tag, first version, four days" | Changed to "v0.0.1 through v0.4.0 — 7 tags in four days" |
| C3 | B16 narration | "One on August 14. Then the tag." | Updated: "Seventeen on August 13 — including the v0.4.0 tag. One more on August 14, after the tag, and that is HEAD." |
| C4 | B17 Manim data | `"tag": "v0.4.0"` placed at Aug 14 | Moved to Aug 13 (cumulative=48); Aug 14 labeled "HEAD" |
| C5 | B18 on-screen | "v0.4.0 tagged Aug 14" | Changed to "v0.4.0 tagged Aug 13" |
| C6 | B33 Manim CATEGORIES | `codecs` listed (not in imports) | Removed |
| C7 | B33 Manim CATEGORIES | `xml.etree.ElementTree`, `zipfile`, `zlib` missing | Added to "file / I-O" |
| C8 | B33 beat_sheet data | Same as C6/C7 | Corrected to match actual grep output |
| C9 | B33 narration | Missing `xml.etree.ElementTree`, `zipfile`, `zlib` | Added to the enumerated list |

## Open item for Bear

- **B27 "verbatim"**: narration says "Verbatim: 'Do not imply…'" but the on-screen
  display omits the tail of the sentence and the inner quote marks are simplified.
  Options: (a) remove "Verbatim:" from narration and call it "near-verbatim", or
  (b) keep and extend the on-screen display to include the full L28 line. No number
  is at stake — this is a quotation-accuracy call. Bear decides.
