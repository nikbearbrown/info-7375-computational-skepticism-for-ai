# 02 · Filter

**What it does.** Takes the collected postings, drops repeats of the same (source, id), marks any posting with no title, link or parseable date, and applies the keyword rules: keep on a role word in the title, enough topic words in the body, evidence that the job makes teaching materials for a named audience, or an account or partnership title whose body names higher education. Then two gates drop a posting the keywords would have kept: its place names no allowed country (English-speaking countries plus France, Italy, Brazil and Portugal), or its title says K-12. Every posting leaves with a decision and a reason.

**Output (one item):** `{date, keywords_version, sources, watched, counts: {postings_fetched, postings_unique, kept, rejected: {reason: n}}, records: [...]}`, each record with `kept`, `matched` (the words and which rule) and `reject_reason`.

**Python counterpart:** `judge()`, `where()`, `k12_hits()` and the per-posting checks in `collect.py`. **Logic:** `shared/lib/judge.js`. **Rules:** `shared/keywords.json` (v0.6.1), copied from the Python master; the rules are never edited in the workflow.

**Tested.** Headless: all 17 synthetic records identical to the Python's, covering all four keep rules and the reject reasons (no keyword, one topic word, no link, no date, duplicate, country not allowed, K-12 role, both). Real data: with rules v0.5.2, **all 2,465 postings from the 2026-10-18 run identical** to the Python (81 kept by each); with v0.6.0, **all 1,869 postings of the six boards on today's watch list identical** on every field, keep decision and matched words (60 kept by each). The place and K-12 readers also agree on all 12,882 distinct location lines and 68,319 distinct titles of an 84,282-posting snapshot.

**Limits.** A filter agreement says the port is faithful, not that the filter is right: the rules' own measured weaknesses (see `keywords.json`) carry over unchanged.
