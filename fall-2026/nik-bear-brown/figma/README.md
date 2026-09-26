# figma/ — Figma's open jobs, and a recipe for the kind of work I'm looking for

## Executive summary

**What this is.** Two things.
- **An archive:** a dated copy of every job Figma lists on its public job board, one JSON file per day saved.
- **A recipe (a first draft):** it answers one question from that archive: *does Figma have Designer Advocate or education-type work I could do on flexible terms (summer, contract, or part-time), such as going to universities to run workshops, or developing workshops for Figma?*

**Why read it.** A saved copy is evidence: it shows what the board said on a given day. The recipe shows the engine's method on a real question. It checks the record first, says exactly what was matched, and leaves the decision to the person.

**What it found (2026-09-23).** Not on this board, not today.
- **Advocate roles:** Figma lists **2 Designer Advocate roles**, and the posting that states its terms says **full time**. Both are at US hubs, with an annual base salary range of $153,000–$317,000.
- **Workshops:** one of them, *Partnerships*, involves workshops and helping partners educate their customers.
- **Universities:** **no posting mentions universities or campuses.**
- **Flexible terms:** **no posting offers part-time, contract, temporary, seasonal, or freelance terms.** Every "summer" or "hourly" posting is an internship, apart from one full-time role paid hourly.

If flexible or university work with Figma exists, it isn't posted here. That points to the networking side of the search, not the application side.

---

## The archive

| File | Fetched | Jobs |
|---|---|---:|
| `figma-jobs-2026-09-23.json` | 2026-09-23 20:01 UTC | 160 |

Each file is Figma's public Greenhouse API response from
`https://boards-api.greenhouse.io/v1/boards/figma/jobs?content=true`.
The API sends it as one minified line, so it is **indented for reading before it is saved**. The data is unchanged; only the whitespace differs, and that was checked by parsing the file before and after.
It has two top-level keys: `jobs`, one record per posting (id, title, location, URL, first-published and updated dates, departments, offices, full posting text), and `meta.total`.

It was fetched with the Reallocation Engine's `greenhouse-watch` skill in dry-run mode: one request to the allow-listed Greenhouse host, with nothing matched or recorded. To add a day:

```bash
python3 .claude/skills/greenhouse-watch/scripts/greenhouse_watch.py \
  --board figma --resume <any example résumé> --state /tmp/figma.state.json \
  --out /tmp/figma-fetch/ --dry-run
python3 -c "import json,sys; d=json.load(open(sys.argv[1])); json.dump(d, open(sys.argv[2],'w'), indent=2, ensure_ascii=False)" \
  /tmp/figma-fetch/raw-*.json figma/figma-jobs-$(date +%F).json
```

Run it from a clone of the-reallocation-engine, and give `figma/` as the path to this folder.

---

## Recipe: Figma advocate and education work on flexible terms

```yaml
status: DRAFT          # runs on one saved day; open TODOs below
todos_open: 3
last_gate: null
attestation: null
recipe_version: 0.1.0
```

### Purpose

Professor Bear teaches AI, builds AI course tutors, and runs workshops. The question is whether Figma has advocate or education work he could take on **alongside** teaching: summer, contract, or part-time; going to universities to run workshops; or developing workshops for Figma. The recipe checks each day's saved board and answers with word matches the reader can check, not with a model's opinion of fit.

### Inputs

| Input | Where |
|---|---|
| One day's board | `figma/figma-jobs-YYYY-MM-DD.json` (see *The archive*) |
| The words searched for | the three lists at the top of `figma/find_roles.py`: role words (title), topic words (text), flexible-terms phrases (text) |

### Steps

1. **Save today's board** with the two commands above. This is the only step that touches the network.
2. **Scan it:** `python3 figma/find_roles.py figma/figma-jobs-YYYY-MM-DD.json > figma/roles-YYYY-MM-DD.md`. The scan runs offline and uses only Python's standard library. Every row shows the matched words in context.
3. **Compare with the last scan.** `[TODO: DEV]` There's no diff step yet. For now, compare the new `roles-*.md` with the previous one by eye, or use `greenhouse-watch` to see which postings are new.
4. **Keep the relevant postings:** `python3 figma/pick_postings.py figma/figma-jobs-YYYY-MM-DD.json figma/professor-bear-figma <id> <id> …`. This copies the chosen postings into `professor-bear-figma.json` (indented, for checking) and `professor-bear-figma.md` (for reading). Each posting keeps its terms, pay, the words the scan matched, and the full text as plain lines. Which ids to keep is the person's choice.
5. **Gate (human):** read every row and give each one a next action: **apply** (the terms fit), **network** (the team fits but the terms don't, so talk to people instead of applying), or **skip**. Only a person clears this gate.

### Output

`figma/roles-YYYY-MM-DD.md`, with three tables:
- role words in titles, with the terms and pay the posting states;
- university, workshop, or education words in the text;
- flexible-terms words in the text.

The next-action column is left for the person.

### The first run: 2026-09-23 (`roles-2026-09-23.md`)

| What the scan looked for | Postings (of 160) | What the matches actually are |
|---|---:|---|
| Role words in the title (advocate, educator, education, enablement, evangelist, developer relations, community, instructor, trainer, curriculum) | 8 | **2 Designer Advocate roles** (Marketing): the main role and *Partnerships*. The main role says "full time… from one of our US hubs," with travel up to 25%; *Partnerships* is San Francisco and doesn't state its terms. Both list $153,000–$317,000. The other 6 are Customer Enablement roles in Sales, all outside the US. |
| University, campus, student, workshop, curriculum, educate, education, or teach in the text | 10 | *Designer Advocate, Partnerships* is the closest fit. It represents Figma "at partner events, workshops, conferences" and equips partners "to educate and inspire their customers." The others are onboarding, account-management, and enablement roles that run customer workshops or training. **None mentions universities or campuses.** |
| Part-time, contract role or position, temporary, seasonal, fixed-term, freelance, summer, or hourly in the text | 9 | 8 are **internships** (summer or hourly pay). The ninth, *Technical Quality Specialist*, is paid hourly but says it's a full-time role. **Zero** postings offer part-time, contract, temporary, seasonal, fixed-term, or freelance terms. |

**Verified vs. judged.**
- **Record:** every count and quote above comes from the saved file through `find_roles.py`.
- **Judgment:** "the closest fit" and the next step below. Those are a reading of the records, not records.

**Kept as relevant** (in `professor-bear-figma.json` and `.md`): *Designer Advocate* (6176134004) and *Designer Advocate, Partnerships* (6114301004).

**Next action (judgment, for Professor Bear to decide):** **network, don't apply.** The team whose work sounds closest, Figma's Advocacy team (named in the Designer Advocate posting), is visible on this board. The flexible terms aren't. If contract or university work exists, it would come through a conversation with that team, not through this board.

### What it can and can't verify

| Can | Can't |
|---|---|
| Exactly what Figma's public board listed on a saved day, and the words each posting uses | Work Figma arranges **off** its job board: contracts, speaker programs, education partnerships. None of those have to appear here. |
| Whether a posting *states* full-time, and its stated pay range | Employment type when the posting doesn't say it. The Greenhouse API has no employment-type field for Figma, so "not stated" means "not stated," not "flexible." |
| That the matched words appear, shown in context | Synonyms the word lists don't include. The lists were chosen by hand; a posting that says "ambassador" or "speaker" would be missed today. |

### Open TODOs

- `[TODO: DEV]` A day-over-day diff for this scan, so a new advocate or flexible posting stands out on the day it appears.
- `[TODO: DEFINE]` Professor Bear to review the three word lists in `find_roles.py`. Should "ambassador," "speaker," "events," or "design education" be added? Should any be removed?
- `[TODO: DATA SOURCE]` Where else flexible or university work with Figma might be announced, if anywhere, with a named, checkable source. Not guessed.

### Files

| File | Role |
|---|---|
| `find_roles.py` | the scan: offline, standard library only, prints Markdown |
| `roles-2026-09-23.md` | the first run's full report, every row with its context |
| `pick_postings.py` | copies chosen postings into a readable JSON + Markdown pair |
| `professor-bear-figma.json` · `professor-bear-figma.md` | **the relevant postings**: the two Designer Advocate roles from 2026-09-23, with stated terms, pay, matched words, and full text |
| `figma-jobs-2026-09-23.json` | the saved board the report was made from |
