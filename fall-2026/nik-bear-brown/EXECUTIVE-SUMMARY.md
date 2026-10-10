# Executive Summary: Computational Skepticism for AI

**Project status as of October 10, 2026 — prepared by Muse**

## 1. The Idea

Computational skepticism is Bear's method: use AI tools in public, on real work, while continuously auditing whether their conclusions hold up. The project is a worked example of that method applied to a concrete question — how a working professor finds and prepares for education, advocate, teaching-materials, and related work at AI and design-tool companies. Instead of trusting any single tool's answer, Bear is building the instrumentation himself: job-board collectors that pull every posting daily, filters that surface teaching-related roles, and audits that test whether the pipeline's own output is correct. The project lives in the repo `nikbearbrown/info-7375-computational-skepticism-for-ai` under `fall-2026/nik-bear-brown/`, is live-coded across three Northeastern courses (Computational Skepticism verifies whether the output is right; Prompt Engineering examines how the AI work is conducted; Branding and AI presents the result), and is documented in a film series as it is built.

## 2. The Market

The buyers are universities — institutions deciding which AI tools to put in front of students and faculty, a procurement landscape worth tracking because it determines where education-related jobs get created. The sellers are the 47 companies in Bear's October 2026 market map ("Companies Selling Educational AI to Universities"), spanning seven categories: frontier labs, LMS/SIS platforms, publishers, library tools, teaching/integrity tools, online learning/OPM providers, and creative tools. Ten of those companies are Bear's priority monitoring targets because they both sell into education and hire for education-adjacent roles:

| Company | Education offering |
|---|---|
| Anthropic | Claude for Education / Enterprise |
| OpenAI | ChatGPT Edu |
| Google | Gemini for Education / Enterprise, NotebookLM |
| Microsoft | M365 Copilot Chat in education licenses, M365 Copilot add-on, GitHub Education |
| Amazon | Bedrock, AWS for higher education |
| Meta | Bear uses a Meta tool for educational AI (exact product unspecified) |
| Notion | Notion for Education |
| Figma | Figma for Education |
| Canva | Canva for Campus |
| Miro | Miro for Education |

The market map itself is a five-page PDF artifact with the offerings table, buyer map, market postures, and references.

## 3. What Bear Is Doing

Bear is running four parallel tracks. **First**, he is building job-search infrastructure: daily collectors over all ten target companies' job boards, a SQLite monitor that diffs native job IDs to detect new and closed postings, and a "daily recipe" he triggers by typing a phrase — the system collects, diffs, logs, and pushes to GitHub. **Second**, he is producing a film series documenting the project (course assignments plus capability tests), rendered with his brutalist.art toolkit. **Third**, he is operating his YouTube channel (@NikBearBrown, ~735 videos) as the public lab where the work is published and tested. **Fourth**, he maintains the underlying tooling: the brutalist.art open-source film toolkit, the lectern job-board watcher shared across three courses, and a verified headless 3D/game pipeline (Blender + Godot).

## 4. Detailed Status

### 4.1 Job-search infrastructure (the daily recipe)

- **Design locked:** Bear pasted a full collector/monitor specification on 2026-10-08 — every collector returns `(jobs, reported_total)` with source-native IDs; the monitor requires two consecutive trusted runs before marking a job closed; a run is trusted only if it fetches ≥90% of the source-reported total and ≥70% of the previous trusted run; descriptions fetched only for unseen IDs; one request per second with jitter; no logins.
- **Six-company baseline (2026-10-08):** Anthropic 645, Figma 151, Miro 24, OpenAI 812, Notion 133, Canva 126 — 1,891 postings total, 58 kept by the education filter. Pushed to the course repo under `lectern/runs/2026-10-08/`.
- **Figma diff vs 2026-09-23 snapshot:** 23 new native IDs (including a Designer Advocate in Berlin), 32 no longer present.
- **Google collector:** verified working — 3,345/3,345 trusted on 2026-10-08; re-ran 2026-10-09 at 3,344/3,347 trusted with 112 new postings. A layout variation (some records carry no URL) was caught by the fail-loud assertions and handled.
- **Amazon collector:** verified working — 9,993 of 10,000 reported, trusted, in the monitor.
- **Microsoft collector:** endpoint discovered (`apply.careers.microsoft.com/api/pcsx/search`, via robots.txt; 2,371 reported positions, 10-per-page). The API throttles hard (~1 request per 5+ seconds); sustained pulls hit HTTP 429. Collector hardened with backoff, checkpoint resume, and IncompleteRead retry. ~1,700 jobs in the monitor; latest full run did not complete trusted. Still being worked.
- **Meta collector:** written per spec (Playwright, GraphQL response interception, no DOM parsing, no hardcoded doc_id) but cannot execute from the Linux VM — the egress proxy blocks Chromium's network tunnel. Needs a browser-capable environment; a self-contained Mac-side prompt was prepared.
- **Daily recipe:** Bear types "run daily recipe" and the routine runs start to finish. Not yet on an automatic schedule — it fires on his command.

### 4.2 Assignment films (INFO 7375 Branding and AI)

- **Assignment 4 ("Scale Your Thing & Add Intelligence"):** all four slate cuts rendered, QC'd (94 frames read), and delivered to Drive on 2026-10-07, ahead of the 2026-10-09 11:59 PM EDT deadline — Part 1 "Opportunity matcher" (292.8s), Part 2 "Showing the output" (216.1s), Part 3 "Proving it scales" (188.7s), Part 4 "Packaging it" (197.6s). All four Drive links verified live on 2026-10-09. Submission status is Bear's to confirm.
- **Assignments 2 & 3:** six films delivered and QC-clean; content for A2 Parts 3–4 and A3 Part 4 remains undefined awaiting Bear's decision.
- **Capability films:** "Muse's bounds" and "The secure VM is a personal VM" delivered; awaiting Bear's verdict.

### 4.3 Market intelligence

47-company market map delivered as a five-page PDF (offerings table, buyer map, market postures, references). The ten priority targets are the monitoring list, not the full map.

### 4.4 YouTube channel (@NikBearBrown)

- Read-only audit complete (735 videos, 38 playlists): heavy duplication, dead entries, missing descriptions.
- Playlist reorder script + newcomer-first order spec delivered; Bear runs it on his own machine with his own OAuth credentials.
- One playlist incident open: "Claude making a film about Muse" needs Bear's manual re-add to "Muse for Educational AI."
- Five Ogilvy title+description style drafts written and delivered 2026-10-10 for style approval — nothing goes live until he approves.

### 4.5 Tooling

- **brutalist.art:** open-source Brutalist explainer-film toolkit (Kokoro TTS + Manim + Remotion); the lecture skill's ONE LOOK rule (stage `#F2F0E9`, ink `#3D3929`, terracotta `#D97757`, EB Garamond) governs all film work; a verified 3× text-oversampling helper fixes a systematic spacing bug.
- **lectern:** job-board watcher shared across three courses via `sync.sh`; six ATS boards covered.
- **Blender 4.5.9 + Godot 4.7:** both verified working headless on the VM (Blender proved with a scripted coin-and-pipe render; Godot proven by the Jumpman extension and walkthrough video).

### 4.6 HPC lecture-film series

13 chapter directories; three reels were in progress when collaborator AP's session ran out of tokens on 2026-10-02. Two review cuts done, one partial package, ten untouched. Bear asked Muse to finish all thirteen.

## 5. Open Items and Next Steps

1. **Microsoft collector:** complete one trusted full pull (throttling is the blocker, not the code).
2. **Meta collector:** run in a browser-capable environment (Mac via the prepared prompt).
3. **Repo push + FRICTIONAL log:** the 2026-10-08 run's outputs and collectors are pushed; the log entry and final Microsoft numbers go out once the trusted pull lands.
4. **A4 submission:** confirm filed by the 2026-10-09 11:59 PM EDT deadline.
5. **YouTube:** Bear's verdicts pending on all delivered films; manual playlist re-add; Ogilvy style approval for the five drafts.
6. **Jumpman extension:** commit `37448a1` still local — the GitHub token 403s on `walker-jumpman-clawd` writes; needs a token scope fix or Bear pushes it himself.
7. **HPC series:** ten chapters untouched.
