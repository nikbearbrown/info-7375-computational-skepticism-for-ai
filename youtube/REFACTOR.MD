# REFACTOR.MD — computational-skepticism-for-ai

Generated 2026-07-19. Book: `computational-skepticism-for-ai`.
Routing (from `YouTube.json`): topic **Artificial Intelligence** · channel **@NikBearBrown** ·
target playlist **"Claude for Artificial Intelligence"** (refactored cuts get this new playlist;
the original "Brutalist Artificial Intelligence" playlists are untouched).

---

## Laws digest — read both files once before starting any reel

1. `brutalist-art/CLAUDE-BRAND.md` — palette, accent law, brand fidelity rules
2. `brutalist-art/skills/make/ai-explainer/SKILL.md` — cold-open law, greeting slot, Wagwan
   rule, ASK→RESULT law, HANDOFF law, REBUILD law, GATE P, ClaudeComposerAsk schema,
   ClaudeTitleOutro schema, channel table (Liam = `am_onyx`, Teardown register)

---

## What was found

**19 in-scope reels** — all `claude-liam-vox-*` folders. These are staged refactor copies:
`palette=claude` and audio already present from the original `vox-*` build, but each has
**skin_warnings** confirming B01 is still a CARD title (not `ClaudeComposerAsk`) and the final
beat is still `OutroCTA` (not `ClaudeTitleOutro`). No handoff beats exist. No ASK→RESULT
micro-beats have been inserted. Audio files for all original inner beats exist in `mp3/`.

**Excluded (do not touch):**
- `vox-*` (19) — source originals; used as reference only, never modified
- `nbb-vox-*` (19) — brand-variant echoes of the canonical reels
- `nbb-cli-*` (8) — brand-variant echoes of CLI reels
- `cli-*` (8) — CLI explainers in a different format; separate scope
- `claude-liam-cli-*` (13) — already properly built claude-liam CLI reels
- `claude-liam-gru-*` (6), `claude-liam-bd-*` (4), `claude-liam-bnb-*` (6),
  `claude-liam-bs-*` (5), `claude-liam-cb-*` (6) — built directly as claude-liam;
  no vox source to refactor from

---

## Inventory table

Process **one reel at a time, in order**. Wait for `next` / `skip` / `stop` after each.

| # | Reel folder (in `youtube/`) | Title | Greeting | Cold-open question | Handoff prompt |
|---|---|---|---|---|---|
| 1 | `claude-liam-vox-same-net-same-hole` | Why Two AIs Checking Each Other Is One Blind Spot Twice | Hola, Liam | "Why does adding a second AI checker just double the blind spot?" | `"explain why two AI models trained on the same data have correlated failure modes — and what genuine independence requires in a checker"` |
| 2 | `claude-liam-vox-heavy-tail-yank` | Why One Data Point Can Beat Your Thousand-Point Average | Olá, Liam | "Why can one data point overpower a thousand-observation average?" | `"simulate a running average on a heavy-tailed distribution and show me when and why it never converges"` |
| 3 | `claude-liam-vox-calibration-curve` | Why an Accurate Model Can Still Lie Every Time It Says 99% | Bonjour, Liam | "Why can a 94%-accurate model still lie about its confidence?" | `"plot a reliability diagram for a model I describe and tell me where its confidence claims are wrong"` |
| 4 | `claude-liam-vox-confidence-gauge` | Why Fluent Answers Make You Worse at Checking Them | Ciao, Liam | "Why do fluent AI answers make you worse at evaluating them?" | `"write a checklist for evaluating AI answers that is not fooled by how fluently they read"` |
| 5 | `claude-liam-vox-bias-pipe` | Why Fixing the Model Didn't Fix the Bias | Hallo, Liam | "Why does fixing the model not fix the bias?" | `"map all the paths bias can travel from a protected attribute to model output — show which intervention blocks which path"` |
| 6 | `claude-liam-vox-prediction-lock` | Why a Prediction You Can Edit Is Worth Nothing | Hej, Liam | "Why is a prediction you can edit after the fact worth nothing?" | `"build a prediction-lock workflow — I make a guess, it gets timestamped and locked, then I see the result and measure the gap"` |
| 7 | `claude-liam-vox-two-clocks` | Why the Study Method That Feels Best Teaches the Least | Hei, Liam | "Why does the study method that feels best teach the least?" | `"design an experiment that would distinguish storage strength from retrieval performance — what would the two learning curves look like over time?"` |
| 8 | `claude-liam-vox-shapley-room` | Why Fair Credit-Splitting Has Exactly One Answer | Ahoj, Liam | "Why is there exactly one fair way to split credit between model features?" | `"compute Shapley values for a simple 3-feature model I describe — walk through the coalitions and marginal contributions step by step"` |
| 9 | `claude-liam-vox-agent-deleted` | Why the AI Wasn't Lying When It Said 'Deleted' | Cześć, Liam | "Why can an AI say 'deleted' and still be wrong?" | `"explain the gap between an agent's local state and the actual world state — use the deleted-email case as the worked example"` |
| 10 | `claude-liam-vox-panda-proxy` | The Model Isn't Broken — It's Honest About What It Learned | Privet, Liam | "Why did the model flip a panda to gibbon without touching its shape?" | `"decompose an image classifier's decision into the features it actually learned versus the features humans assume it learned"` |
| 11 | `claude-liam-vox-chart-lie` | Watch Me Lie With a Chart Without Changing a Single Number | Yassou, Liam | "How do you lie with a chart without changing any numbers?" | `"take this dataset and produce three charts that each tell a different story without changing a single data point"` |
| 12 | `claude-liam-vox-injection-wall` | Why Prompt Injection Can't Be Patched | Merhaba, Liam | "Why can't prompt injection ever be fully patched?" | `"demonstrate a prompt injection attack on a simple document-reading agent — then explain why no input filter can stop it at the model level"` |
| 13 | `claude-liam-vox-error-cascade` | You Validated Each Agent at 1%. The System Fails at 30%. | Shalom, Liam | "Why does a multi-agent pipeline fail even when each agent passes validation?" | `"calculate the compound error rate for a pipeline of 5 agents each with a 1% error rate — show me at what chain length the system becomes unreliable"` |
| 14 | `claude-liam-vox-vigilance-decay` | The Better the AI Works, the Worse You Watch It | Salaam, Liam | "Why does a nearly-perfect AI make its human supervisor more dangerous?" | `"model how a human reviewer's error-detection rate changes as an AI system's per-item accuracy increases from 80% to 99%"` |
| 15 | `claude-liam-vox-calibration-useless` | Why a Perfectly Calibrated Model Can Be Perfectly Useless | Jambo, Liam | "Why can a perfectly calibrated model be completely useless?" | `"explain the difference between a calibrated model and a discriminating model — give me an example where calibration is perfect but every prediction is worthless"` |
| 16 | `claude-liam-vox-subgroup-hidden` | Why the Average That Clears the Model Hides the Patient It Harms | Namaste, Liam | "Why does a model that's calibrated on average still harm specific patients?" | `"decompose aggregate calibration data into subgroup curves — show me how a small group's badly calibrated curve gets absorbed by the large group's good one"` |
| 17 | `claude-liam-vox-missing-mnar` | Why Some Missing Data Lies About Itself | Annyeong, Liam | "Why does missing data lie about why it is missing?" | `"given a dataset where high-income values are missing in proportion to their own value, show me how imputing from the visible mean makes the bias permanent"` |
| 18 | `claude-liam-vox-race-column` | Why Deleting the Race Column Doesn't Delete Race | Sawadee, Liam | "Why doesn't deleting the race column make a model race-blind?" | `"show how correlated features reconstruct a deleted sensitive attribute — use zip code and surname frequency as proxies for the deleted column"` |
| 19 | `claude-liam-vox-channel-reset` | The Impersonator the Agent Caught — Then Believed | Aloha, Liam | "Why did the AI catch an impersonator in one channel, then trust them in the next?" | `"describe how an AI agent's trust judgment can fail to transfer across conversation channel boundaries — what would a safer architecture require?"` |

---

## Per-video procedure (apply to each reel, one at a time)

> Start by reading `brutalist-art/CLAUDE-BRAND.md` and `brutalist-art/skills/make/ai-explainer/SKILL.md` in full if you haven't in this session.

### Step 1 — Read the reel's current `beat_sheet.json`

- Confirm `metadata.skin_warnings` (B01 = CARD title, last beat = OutroCTA).
- Note the reel's title and slug.
- List all beats with `"source": "own"` and `"type": "GRAPHIC"` or `"DOCUMENT"` — these are the
  ASK→RESULT insertion points (every generated visual gets a composer micro-beat before it).

### Step 2 — Replace B01 (open) → `ClaudeComposerAsk`

Using the greeting and question from the inventory table:

```json
{
  "beat_id": "B01",
  "act": "COLD OPEN",
  "shot": {
    "type": "GRAPHIC",
    "source": "remotion",
    "remotion": {
      "pattern": "ClaudeComposerAsk",
      "props": {
        "greeting": "<greeting from table>",
        "command": "<cold-open question from table>",
        "eyebrow": "COMPUTATIONAL SKEPTICISM · <HOOK>",
        "segment": "<Title in Title Case>"
      }
    }
  },
  "narration_text": "<greeting>, this is Liam, in for Bear. <question>",
  "engine": "kokoro",
  "voice": "am_onyx"
}
```

`<HOOK>` = the reel's two-to-four-word premise (e.g., "THE FLUENCY TRAP", "COMMON-CAUSE FAILURE").
Derive from the title — it's the subtitle that would print on a magazine cover.

### Step 3 — Apply ASK→RESULT law to all inner GRAPHIC beats

For every beat identified in Step 1 (every `source: "own"` GRAPHIC or DOCUMENT beat after B01):

Insert a NEW beat immediately BEFORE it. The new beat is a silent or one-line composer micro-beat:

```json
{
  "beat_id": "<Xnn>",
  "act": "<same act as the following beat>",
  "shot": {
    "type": "GRAPHIC",
    "source": "remotion",
    "remotion": {
      "pattern": "ClaudeComposerAsk",
      "props": {
        "greeting": "The ask,",
        "command": "<realistic Claude prompt that could generate the following scene>",
        "eyebrow": "COMPUTATIONAL SKEPTICISM · <HOOK>",
        "segment": "<Title in Title Case>"
      }
    }
  },
  "narration_text": "",
  "engine": "kokoro",
  "voice": "am_onyx",
  "estimated_duration_s": 3
}
```

The `command` must be a **realistic Claude prompt** — one that a viewer could paste into the Claude
app to reproduce the scene. E.g., before a split-track Manim of two groups' score distributions:
`"write a Manim scene: two group score distributions on the same axis, one threshold slider, live TPR/FPR dials"`.

Do NOT re-render or rewrite the following beat — the existing media and audio are kept as the RESULT.

**Beat ID scheme for inserted beats:** prefix the following beat's ID with `A`. E.g., new beat
before B04 → `AB04`; before B07 → `AB07`. Re-sequence all beat_ids after insertion so they are
in document order (you may use A-prefix to avoid renumbering the whole sheet).

### Step 4 — Insert HANDOFF beat (second-to-last)

Insert a HANDOFF beat immediately before the final outro beat. Using the handoff prompt from the
inventory table:

```json
{
  "beat_id": "HANDOFF",
  "act": "HANDOFF",
  "shot": {
    "type": "GRAPHIC",
    "source": "remotion",
    "remotion": {
      "pattern": "ClaudeComposerAsk",
      "props": {
        "greeting": "Your turn.",
        "command": "<handoff prompt from table>",
        "eyebrow": "COMPUTATIONAL SKEPTICISM · <HOOK>",
        "segment": "<Title in Title Case>"
      }
    }
  },
  "narration_text": "Your turn. <Read the handoff prompt aloud, then add one sentence of context — what the viewer will discover when they run it>.",
  "engine": "kokoro",
  "voice": "am_onyx",
  "estimated_duration_s": 8
}
```

**HANDOFF LAW**: narration must READ the prompt aloud AND discuss it. A bare "take this into
your session" is wrong. The viewer must hear the prompt as a sentence.

### Step 5 — Replace final beat → `ClaudeTitleOutro`

Replace the `OutroCTA` beat with:

```json
{
  "beat_id": "OUTRO",
  "act": "OUTRO",
  "shot": {
    "type": "GRAPHIC",
    "source": "remotion",
    "remotion": {
      "pattern": "ClaudeTitleOutro",
      "props": {
        "title": "<full video title — same as metadata.title>",
        "handle": "@NikBearBrown"
      }
    }
  },
  "narration_text": "<Title>. Liam, in for Bear.",
  "engine": "kokoro",
  "voice": "am_onyx",
  "estimated_duration_s": 6
}
```

### Step 6 — Remove `skin_warnings` and `_variant_todo` from metadata

These are now addressed. Also set:
```json
"metadata.refactored": "2026-07-19",
"metadata.refactor_status": "BEAT_SHEET_DONE"
```

### Step 7 — GATE P (pedagogy review before audio spend)

Write or append to `<reel>/PEDAGOGY.md`:

```
## Refactor addendum — <date>
- Cold open: ClaudeComposerAsk with question "<question>"
- ASK→RESULT beats inserted: <list beat IDs>
- Handoff prompt: "<prompt>"
- Outro: ClaudeTitleOutro
- Inner beats: UNCHANGED
VERDICT: PASS
```

Do not generate any audio before `VERDICT: PASS` is written.

### Step 8 — Generate audio for NEW beats only

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
  computational-skepticism-for-ai/youtube/<reel-slug> \
  --only B01 <all AB* IDs> HANDOFF OUTRO
```

Existing `mp3/beat-B*.mp3` files for inner beats are NOT regenerated.
Update `metadata.total_estimated_duration_seconds` after audio is measured.

### Step 9 — Conform and render to `claude-cut.mp4`

```bash
python3 brutalist-art/runtime/scripts/compile.py \
  computational-skepticism-for-ai/youtube/<reel-slug> \
  --output-name claude-cut
```

The compile uses measured audio durations as the master clock. Existing media for inner beats
is reused; new beats get PIPELINE slates if their Remotion components haven't rendered yet.

Render Remotion scenes for new beats (ClaudeComposerAsk × N, ClaudeTitleOutro):

```bash
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
  computational-skepticism-for-ai/youtube/<reel-slug> \
  --concurrency=1
```

Then re-compile:

```bash
python3 brutalist-art/runtime/scripts/compile.py \
  computational-skepticism-for-ai/youtube/<reel-slug> \
  --output-name claude-cut
```

### Step 10 — QC and report

Sample frames: open the review cut and read at minimum:
- Frame 0s: cold open (ClaudeComposerAsk visible, greeting correct, question correct)
- One ASK→RESULT pair (ask beat → existing visual beat)
- Handoff beat (prompt readable, narration says the prompt aloud)
- Outro frame (title re-stated, handle correct)

Report: beat_ids changed · new audio generated · estimated runtime · any issues.
Then **STOP** and wait for the human.

---

## Human interface

After each reel report:

- `next` → move to the next reel in the inventory table
- `skip` → mark this reel skipped and move on
- `stop` → summarize progress and halt
- feedback → fix this reel, re-render only the changed beats, re-report

## Posting (gated — never auto-post)

Only after **explicit per-video human approval**:

- Title: `<video title> | Computational Skepticism for AI`
- Playlist: `"Claude for Artificial Intelligence"` on **@NikBearBrown**
- Description: include the cold-open question and the handoff prompt verbatim — they are the
  description's most useful content
- Caption track: `<slug>.srt` (measured-window SRT from the compile)
- The video goes unlisted; **public is a manual Studio flip by the human**

Use the existing posting tooling at
`brutalist-art/youtube/posting-to-youtube/` conventions and the credentials at
`brutalist-art/youtube/credentials/nikbearbrown/`.

---

## Status tracking

Add a `status` column here as you work through the table:

| # | Slug | Status | Notes |
|---|---|---|---|
| 1 | claude-liam-vox-same-net-same-hole | — | |
| 2 | claude-liam-vox-heavy-tail-yank | — | |
| 3 | claude-liam-vox-calibration-curve | — | |
| 4 | claude-liam-vox-confidence-gauge | — | |
| 5 | claude-liam-vox-bias-pipe | — | |
| 6 | claude-liam-vox-prediction-lock | — | |
| 7 | claude-liam-vox-two-clocks | — | |
| 8 | claude-liam-vox-shapley-room | — | |
| 9 | claude-liam-vox-agent-deleted | — | |
| 10 | claude-liam-vox-panda-proxy | — | |
| 11 | claude-liam-vox-chart-lie | — | |
| 12 | claude-liam-vox-injection-wall | — | |
| 13 | claude-liam-vox-error-cascade | — | |
| 14 | claude-liam-vox-vigilance-decay | — | |
| 15 | claude-liam-vox-calibration-useless | — | |
| 16 | claude-liam-vox-subgroup-hidden | — | |
| 17 | claude-liam-vox-missing-mnar | — | |
| 18 | claude-liam-vox-race-column | — | |
| 19 | claude-liam-vox-channel-reset | — | |

---

*computational-skepticism-for-ai: 19 videos in scope (excluded: vox-* originals ×19,
nbb-* variants ×27, cli-* ×8, claude-liam-cli-* ×13, gru/bd/bnb/bs/cb series ×27)*
