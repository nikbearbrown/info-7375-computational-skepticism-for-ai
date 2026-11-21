#!/usr/bin/env python3
"""Generate every workflow.json from shared/lib/*.js (the logic), shared/keywords.json and shared/boards.json (the
rules and the watch list) and each folder's fixtures. The JSON is generated so that the logic lives in readable .js
files, is tested in Node against the Python, and cannot drift from what the nodes contain.

  python3 tools/build.py
"""
import hashlib, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
read = lambda *p: open(os.path.join(ROOT, *p), encoding="utf-8").read()
jload = lambda *p: json.load(open(os.path.join(ROOT, *p), encoding="utf-8"))
lib = lambda n: read("shared", "lib", n + ".js").replace("if (typeof module !== 'undefined') module.exports", "// (node export removed in the n8n copy) module.exports")

FOLDERS = {"collect": "01-collect", "filter": "02-filter", "delta": "03-delta", "post": "04-post-to-discord", "daily": "05-daily"}
WF_ID = {k: "lectern" + hashlib.sha1(v.encode()).hexdigest()[:10] for k, v in FOLDERS.items()}
KW = jload("shared", "keywords.json")


def nid(wf, name):
    return hashlib.sha1((wf + name).encode()).hexdigest()[:8] + "-" + hashlib.sha1(name.encode()).hexdigest()[:4]


class WF:
    def __init__(self, key, title):
        self.key, self.title, self.nodes, self.conns = key, title, [], {}

    def add(self, name, type_, params, pos, version=1, **extra):
        n = {"parameters": params, "id": nid(self.key, name), "name": name, "type": type_, "typeVersion": version, "position": pos}
        n.update(extra)
        self.nodes.append(n)
        return name

    def code(self, name, js, pos, each=False):
        return self.add(name, "n8n-nodes-base.code", {"jsCode": js, **({"mode": "runOnceForEachItem"} if each else {})}, pos, 2)

    def noop(self, name, pos):
        return self.add(name, "n8n-nodes-base.noOp", {}, pos)

    def manual(self, name, pos):
        return self.add(name, "n8n-nodes-base.manualTrigger", {}, pos)

    def called(self, name, pos):
        return self.add(name, "n8n-nodes-base.executeWorkflowTrigger", {"inputSource": "passthrough"}, pos, 1.1)

    def note(self, text, pos, w=420, h=200, color=7):
        self.nodes.append({"parameters": {"content": text, "height": h, "width": w, "color": color}, "id": nid(self.key, "note" + text[:20]), "name": "Note " + text[:24].strip("# \n"),
                           "type": "n8n-nodes-base.stickyNote", "typeVersion": 1, "position": pos})

    def link(self, a, b, out=0, inp=0):
        self.conns.setdefault(a, {"main": []})
        m = self.conns[a]["main"]
        while len(m) <= out:
            m.append([])
        m[out].append({"node": b, "type": "main", "index": inp})

    def json(self):
        return {"id": WF_ID[self.key], "name": self.title, "active": False, "nodes": self.nodes, "connections": self.conns,
                "settings": {"executionOrder": "v1"}, "pinData": {}, "tags": [], "meta": {"templateCredsSetupCompleted": False}}


def IF(w, name, expr, pos):
    return w.add(name, "n8n-nodes-base.if", {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict", "version": 2},
                 "conditions": [{"id": nid(w.key, name + "c"), "leftValue": expr, "rightValue": "", "operator": {"type": "boolean", "operation": "true", "singleValue": True}}],
                 "combinator": "and"}, "options": {}}, pos, 2.2)


# ---------------------------------------------------------------- 02 filter
def build_filter():
    w = WF("filter", "Lectern 02 · Filter: keep what the rules keep, say why for the rest")
    fx = jload("02-filter", "fixtures", "views.json")
    w.note("## 02 · Filter\nPort of `judge()` in lectern/collect/collect.py. The rules are `shared/keywords.json` (v%s), never this workflow. "
           "Every posting leaves with a decision AND a reason: kept (which rule), or rejected (which test failed). "
           "Run it on its own with the Manual trigger (synthetic postings), or let 05 · Daily call it." % KW["version"], [-160, -330], 520, 170, 4)
    w.manual("Manual · run on fixtures", [0, 0])
    w.code("Fixture input", "// Synthetic postings in the shape workflow 01 produces. Every company and ad is made up.\nconst FIXTURE = %s;\nreturn [{json: FIXTURE}];" % json.dumps(fx), [220, 0])
    w.called("When called by another workflow", [0, 160])
    w.noop("Run in", [440, 80])
    w.code("Dedupe and validate", lib("judge") + """
// One item per unique posting. A repeat of (source, source_id) is dropped and counted by Assemble; a posting with no
// title, link or parseable date is marked and never reaches the rules.
const run = $input.first().json;
const seen = new Set(), out = [];
for (const v of run.views) {
  const key = v.source + '\\u0000' + v.source_id;
  if (seen.has(key)) continue;
  seen.add(key);
  out.push({json: Object.assign({}, v, {check: validity(v)})});
}
return out;""", [660, 80])
    w.code("Judge (rules = keywords.json v%s)" % KW["version"], lib("judge") + "\nconst KW = %s;\n" % json.dumps(KW) + """
return $input.all().map(it => {
  const v = it.json;
  if (v.check) return {json: Object.assign({}, v, {kept: false, matched: null, reject_reason: v.check})};
  const [m, why] = judge(v, KW);
  return {json: Object.assign({}, v, {kept: Boolean(m), matched: m, reject_reason: why})};
});""", [880, 80])
    IF(w, "Kept?", "={{ $json.kept }}", [1100, 80])
    w.noop("Kept", [1320, 0])
    w.noop("Rejected", [1320, 170])
    w.add("Wait for both", "n8n-nodes-base.merge", {"numberInputs": 2}, [1540, 80], 3.2)
    w.code("Assemble run", """// The run, in the shape workflow 03 reads. Postings in their original order, with the reason for every decision.
const run = $('Run in').first().json;
const rows = $('Judge (rules = keywords.json v%s)').all().map(i => i.json);
const FIELDS = ['source', 'company', 'source_id', 'title', 'text', 'url', 'location_text', 'department', 'date_posted', 'job_ref', 'kept', 'matched', 'reject_reason'];
const records = rows.map(r => { const o = {}; for (const f of FIELDS) o[f] = r[f] === undefined ? null : r[f]; return o; });
const rejected = {};
if (run.views.length > rows.length) rejected.duplicate = run.views.length - rows.length;
for (const r of records) if (r.reject_reason) rejected[r.reject_reason] = (rejected[r.reject_reason] || 0) + 1;
return [{json: {date: run.date, keywords_version: '%s', sources: run.sources, watched: run.watched || [...new Set(run.sources.map(s => s.company))],
  counts: {postings_fetched: run.views.length, postings_unique: records.length, kept: records.filter(r => r.kept).length, rejected}, records}}];""" % (KW["version"], KW["version"]), [1760, 80])
    for a, b in [("Manual · run on fixtures", "Fixture input"), ("Fixture input", "Run in"), ("When called by another workflow", "Run in"), ("Run in", "Dedupe and validate"),
                 ("Dedupe and validate", "Judge (rules = keywords.json v%s)" % KW["version"]), ("Judge (rules = keywords.json v%s)" % KW["version"], "Kept?"),
                 ("Kept", "Wait for both"), ("Assemble run", None)]:
        if b:
            w.link(a, b, 0, 0) if a != "Kept" else w.link(a, b, 0, 0)
    w.link("Kept?", "Kept", 0, 0)
    w.link("Kept?", "Rejected", 1, 0)
    w.link("Rejected", "Wait for both", 0, 1)
    w.link("Wait for both", "Assemble run")
    return w


# ---------------------------------------------------------------- 01 collect
def build_collect():
    w = WF("collect", "Lectern 01 · Collect: read each watched board and normalise what it says")
    fx = jload("01-collect", "fixtures", "payloads.json")
    boards = jload("shared", "boards.json")["boards"]
    w.note("## 01 · Collect\nPort of `fetch_board()` and `normalise()` in lectern/collect/collect.py. **Fixture mode** (default) replays three recorded, made-up "
           "payloads, one per provider; **live mode** calls the public job-board APIs for the boards in `shared/boards.json`. "
           "A board that fails becomes a status row, never a stop. Live: Greenhouse and Ashby only; SmartRecruiters needs its per-posting detail calls (not built), "
           "so it is reported as unavailable rather than judged on empty text.", [-160, -380], 640, 200, 4)
    w.manual("Manual · run on fixtures", [0, 0])
    w.code("Fixture input", "return [{json: {mode: 'fixture'}}];  // change to {mode: 'live'} (optionally only: ['Anthropic']) to read the real boards", [220, 0])
    w.called("When called by another workflow", [0, 160])
    w.noop("Run in", [440, 80])
    w.code("Boards", "const BOARDS = %s;\nconst FIXTURE = %s;\n" % (json.dumps(boards), json.dumps(fx)) + """
const input = $input.first().json, mode = input.mode || 'fixture';
if (mode === 'fixture') return FIXTURE.map((b, i) => ({json: Object.assign({mode}, b), pairedItem: {item: 0}}));
const only = input.only && input.only.length ? new Set(input.only) : null;
return BOARDS.filter(b => !only || only.has(b.company)).map(b => ({json: {mode, provider: b.provider, company: b.company, slug: b.slug}, pairedItem: {item: 0}}));""", [660, 80])
    IF(w, "Live?", "={{ $json.mode === 'live' }}", [880, 80])
    w.noop("Recorded payloads", [1100, 0])
    IF(w, "Live provider supported?", "={{ ['greenhouse', 'ashby'].includes($json.provider) }}", [1100, 200])
    w.add("Fetch board", "n8n-nodes-base.httpRequest", {"method": "GET",
          "url": "={{ $json.provider === 'greenhouse' ? 'https://boards-api.greenhouse.io/v1/boards/' + $json.slug + '/jobs?content=true' : 'https://api.ashbyhq.com/posting-api/job-board/' + encodeURIComponent($json.slug) + '?includeCompensation=true' }}",
          "sendHeaders": True, "headerParameters": {"parameters": [{"name": "User-Agent", "value": "lectern (course project)"}]},
          "options": {"timeout": 30000, "redirect": {"redirect": {"followRedirects": False}}}}, [1320, 140], 4.2, onError="continueRegularOutput")
    w.code("Label fetched board", """// The HTTP node replaced the item with the API's answer: put the board back with it.
const b = $('Boards').item.json;
const r = $json;
if (r.error || !r.jobs) return {json: {provider: b.provider, company: b.company, slug: b.slug, payload: null, error: String(r.error && r.error.message || r.error || 'no jobs in the response')}};
return {json: {provider: b.provider, company: b.company, slug: b.slug, payload: r}};""", [1540, 140], each=True)
    w.code("Not built live", """const b = $json;
const why = {smartrecruiters: 'SmartRecruiters needs its per-posting detail calls, not built in n8n yet',
             google: "Google is read through its own search pages (collect.py's fetch_google, 2026-11-20), not built in n8n yet"};
return {json: {provider: b.provider, company: b.company, slug: b.slug, payload: null, error: why[b.provider] || ('provider ' + b.provider + ' is not built in n8n yet')}};""", [1320, 300], each=True)
    w.add("Collect all", "n8n-nodes-base.merge", {"numberInputs": 3}, [1760, 140], 3.2)
    w.code("Normalise", lib("normalise") + """
const inDate = $('Run in').first().json.date;
const today = new Date().toISOString().slice(0, 10);
const boards = $('Boards').all().map(i => i.json);
const mode = boards.length ? boards[0].mode : 'fixture';
const views = [], sources = [];
for (const it of $input.all()) {
  const b = it.json;
  if (b.error || !b.payload) { sources.push({company: b.company, provider: b.provider, status: 'unavailable', reason: b.error || 'no payload'}); continue; }
  const v = normalise(b.provider, b.company, b.payload);
  views.push(...v);
  sources.push({company: b.company, provider: b.provider, status: 'ok', postings: v.length});
}
if (!sources.some(s => s.status === 'ok')) throw new Error('every source failed: nothing to report');
const strip = ({original, ...rest}) => rest;      // the source's own record is not carried between workflows
return [{json: {date: inDate || (mode === 'fixture' ? '2026-10-19' : today), mode, sources, watched: [...new Set(boards.map(b => b.company))], views: views.map(strip)}}];""", [1980, 140])
    w.link("Manual · run on fixtures", "Fixture input"); w.link("Fixture input", "Run in"); w.link("When called by another workflow", "Run in")
    w.link("Run in", "Boards"); w.link("Boards", "Live?")
    w.link("Live?", "Live provider supported?", 1, 0)      # (reordered below)
    w.conns["Live?"] = {"main": [[{"node": "Live provider supported?", "type": "main", "index": 0}], [{"node": "Recorded payloads", "type": "main", "index": 0}]]}
    w.link("Live provider supported?", "Fetch board", 0, 0); w.link("Live provider supported?", "Not built live", 1, 0)
    w.link("Fetch board", "Label fetched board")
    w.link("Recorded payloads", "Collect all", 0, 0); w.link("Label fetched board", "Collect all", 0, 1); w.link("Not built live", "Collect all", 0, 2)
    w.link("Collect all", "Normalise")
    return w


# ---------------------------------------------------------------- 03 delta
def build_delta():
    w = WF("delta", "Lectern 03 · Delta: what is new, changed or gone since the last published run")
    fx = jload("03-delta", "fixtures", "input.json")
    w.note("## 03 · Delta\nPort of `diff()` and `write_state()` in lectern/publish_delta.py. Input: the published state (or none) and today's filtered run. "
           "Output: new, changed and gone, with the reason for each gone. **A source that could not be read today never closes a posting**: its rows are 'unknown', and they stay in the state. "
           "Closed is not hired.", [-160, -330], 560, 190, 4)
    w.manual("Manual · run on fixtures", [0, 0])
    w.code("Fixture input", "// An earlier published state and a later run that differs from it in every way the diff can see. Synthetic.\nconst FIXTURE = %s;\nreturn [{json: FIXTURE}];" % json.dumps(fx), [220, 0])
    w.called("When called by another workflow", [0, 160])
    w.noop("Run in", [440, 80])
    w.code("Diff", lib("delta") + """
const {state, run} = $input.first().json;
const stateC = state && state.candidates ? state.candidates : {};
const kept = {}, all = {}, sources = {};
for (const r of run.records) { all[keyOf(r)] = r; if (r.kept) kept[keyOf(r)] = slim(r); }
for (const s of run.sources) sources[s.company] = s;
const R = {date: run.date, kw_version: run.keywords_version || run.kw_version, kept, all, sources};
const d = diff(stateC, R);
const unavailable = run.sources.filter(s => s.status !== 'ok').map(s => `${s.company} (${s.status}: ${s.reason || ''})`);
const note = (state && state.kw_version && R.kw_version && state.kw_version !== R.kw_version)
  ? `The filter changed between the published run (${state.kw_version}) and this one (${R.kw_version}). A 'matched' change can come from the filter, not from the posting.` : '';
const lone = state && state.as_of && state.as_of >= run.date ? 'published state is not older than this run; nothing to do' : '';
const why = {}; for (const g of d.gone) why[g.why] = (why[g.why] || 0) + 1;
return [{json: {date: run.date, kw_version: R.kw_version, baseline: state ? `published state as of ${state.as_of}` : 'no earlier run: everything is new', refused: lone || null,
  counts: {kept: Object.keys(kept).length, new: d.new.length, changed: d.changed.length, gone: d.gone.length, gone_by_reason: why},
  new: d.new, changed: d.changed, gone: d.gone, first_time_companies: d.first_time_companies, unavailable, filter_note: note,
  watched: run.watched || [], next_state: nextState(stateC, R)}}];""", [660, 80])
    w.link("Manual · run on fixtures", "Fixture input"); w.link("Fixture input", "Run in"); w.link("When called by another workflow", "Run in"); w.link("Run in", "Diff")
    return w


# ---------------------------------------------------------------- 04 post
def build_post():
    w = WF("post", "Lectern 04 · Post: new listings to the Discord channel, behind a switch")
    fx = jload("04-post-to-discord", "fixtures", "input.json")
    w.note("## 04 · Post\nPort of `build_messages()` in lectern/notify.py. Only companies still on the watch list, most-wanted first, nothing already posted, "
           "and a message with a path, an email address or a webhook URL is refused. **`send` is false by default**: the Discord node runs only when it is true, "
           "and it needs a Discord webhook credential (nothing secret is in this file). The message-building and refusal rules are tested; the Discord node itself is not exercised without a webhook.", [-160, -330], 640, 200, 4)
    w.manual("Manual · run on fixtures", [0, 0])
    w.code("Fixture input", "// New listings in the shape workflow 03 produces. Synthetic. send is false: nothing is posted.\nconst FIXTURE = %s;\nreturn [{json: FIXTURE}];" % json.dumps(fx), [220, 0])
    w.called("When called by another workflow", [0, 160])
    w.noop("Run in", [440, 80])
    w.code("Build messages", lib("messages") + """
const i = $input.first().json;
const label = i.label || ('run ' + (i.date || ''));
const {rows, messages} = buildMessages(i.new || [], i.watched || [], i.first_time_companies || [], i.already || []);
const title = `Jobs: ${rows.length} new possible listings (${label})`;
if (!messages.length) return [{json: {nothing_new: true, rows: [], messages: [], send: false}}];
return messages.map((m, n) => {
  const head = messages.length > 1 ? `${title} (${n + 1}/${messages.length})` : title;
  const content = `**${head}**\\n${m}`;
  const bad = refused(content);
  return {json: {nothing_new: false, rows: n === 0 ? rows.map(r => `${r.source}:${r.source_id}`) : [], message: m, content, refused: bad, send: Boolean(i.send) && !bad}};
});""", [660, 80])
    IF(w, "Send?", "={{ $json.send }}", [880, 80])
    w.add("Discord", "n8n-nodes-base.discord", {"authentication": "webhook", "content": "={{ $json.content }}", "options": {"username": "Professor Bear", "flags": ["SUPPRESS_EMBEDS"]}},
          [1100, 0], 2, credentials={"discordWebhookApi": {"id": "", "name": "Discord webhook for the Lectern channel"}})
    w.noop("Dry run: nothing sent", [1100, 170])
    w.add("Wait for both", "n8n-nodes-base.merge", {"numberInputs": 2}, [1320, 80], 3.2)
    w.code("Result", """const built = $('Build messages').all().map(i => i.json);
if (built.length === 1 && built[0].nothing_new) return [{json: {rows: [], messages: [], sent_count: 0, posted_ids: [], refused: 0}}];
const sent = $('Discord').isExecuted ? $('Discord').all().length : 0;
const rows = built.flatMap(b => b.rows);
return [{json: {rows, messages: built.map(b => b.message), sent_count: sent, refused: built.filter(b => b.refused).length,
  posted_ids: sent === built.length ? rows : []}}];   // an id is recorded as posted only if every message went out""", [1540, 80])
    w.link("Manual · run on fixtures", "Fixture input"); w.link("Fixture input", "Run in"); w.link("When called by another workflow", "Run in"); w.link("Run in", "Build messages")
    w.link("Build messages", "Send?"); w.link("Send?", "Discord", 0, 0); w.link("Send?", "Dry run: nothing sent", 1, 0)
    w.link("Discord", "Wait for both", 0, 0); w.link("Dry run: nothing sent", "Wait for both", 0, 1); w.link("Wait for both", "Result")
    return w


# ---------------------------------------------------------------- 05 daily
def build_daily():
    w = WF("daily", "Lectern 05 · Daily: collect, filter, diff, post, remember")
    w.note("## 05 · Daily\nCalls 01 to 04 in order and keeps two small files: the published state and the ids already posted. "
           "Set the paths and `mode` in **Settings**. Default: fixtures, dry run (nothing sent), state written. Run it twice: the second run finds nothing new. "
           "The state advances only after the whole chain succeeded. Import all five workflows with `tools/import.sh` so the Execute Workflow nodes find their targets.", [-160, -380], 700, 210, 4)
    w.manual("Manual", [0, 0])
    w.add("Every day", "n8n-nodes-base.scheduleTrigger", {"rule": {"interval": [{"field": "days", "triggerAtHour": 7}]}}, [0, 170], 1.2)
    w.code("Settings", """// The only place to edit. mode: 'fixture' replays made-up payloads; 'live' reads the real boards.
return [{json: {mode: 'fixture', only: [], date: '', send: false, allow_first_run_post: false, state_path: '__STATE_PATH__', posted_path: '__POSTED_PATH__'}}];""", [240, 80])
    w.add("Read state", "n8n-nodes-base.readWriteFile", {"operation": "read", "fileSelector": "={{ $json.state_path }}", "options": {}}, [460, 0], 1, onError="continueRegularOutput", alwaysOutputData=True)
    w.add("Extract state", "n8n-nodes-base.extractFromFile", {"operation": "fromJson", "options": {}}, [680, 0], 1, onError="continueRegularOutput", alwaysOutputData=True)
    w.add("Read posted", "n8n-nodes-base.readWriteFile", {"operation": "read", "fileSelector": "={{ $('Settings').first().json.posted_path }}", "options": {}}, [900, 0], 1, onError="continueRegularOutput", alwaysOutputData=True)
    w.add("Extract posted", "n8n-nodes-base.extractFromFile", {"operation": "fromJson", "options": {}}, [1120, 0], 1, onError="continueRegularOutput", alwaysOutputData=True)
    w.code("Remember what exists", """// A missing file is the first run, not an error.
const s = $('Settings').first().json;
const st = $('Extract state').first().json, po = $('Extract posted').first().json;
const state = st && st.data && st.data.candidates ? st.data : null;
const already = po && po.data && Array.isArray(po.data.ids) ? po.data.ids : [];
// With no readable state, everything looks new. With send on, that would post every listing at once: refuse unless asked.
if (!state && s.send && !s.allow_first_run_post) throw new Error('No published state was read, and send is on: the first run would post every kept listing. Run once with send off, or set allow_first_run_post to true.');
return [{json: {mode: s.mode, only: s.only, date: s.date, send: s.send, state_path: s.state_path, posted_path: s.posted_path, state, already}}];""", [1340, 0])
    def call(name, key, pos):
        return w.add(name, "n8n-nodes-base.executeWorkflow", {"source": "database", "workflowId": {"__rl": True, "value": WF_ID[key], "mode": "id"}, "mode": "once", "options": {}}, pos, 1.2)
    w.code("Collect input", "const m = $json; return [{json: {mode: m.mode, only: m.only, date: m.date}}];", [1560, 0])
    call("01 · Collect", "collect", [1780, 0])
    call("02 · Filter", "filter", [2000, 0])
    w.code("Delta input", "const m = $('Remember what exists').first().json; return [{json: {state: m.state, run: $json}}];", [2220, 0])
    call("03 · Delta", "delta", [2440, 0])
    w.code("Post input", """const m = $('Remember what exists').first().json, d = $json;
if (d.refused) throw new Error(d.refused);
return [{json: {new: d.new, watched: d.watched, first_time_companies: d.first_time_companies, already: m.already, send: m.send, date: d.date}}];""", [2660, 0])
    call("04 · Post", "post", [2880, 0])
    w.code("Remember this run", """const m = $('Remember what exists').first().json, d = $('03 · Delta').first().json, p = $json;
const ids = [...new Set([...(m.already || []), ...(p.posted_ids || [])])].sort();
return [{json: {state_path: m.state_path, posted_path: m.posted_path, next_state: d.next_state, posted_ids: ids, wrote_posted: (p.posted_ids || []).length > 0,
  summary: {date: d.date, baseline: d.baseline, kept: d.counts.kept, new: d.counts.new, changed: d.counts.changed, gone: d.counts.gone, gone_by_reason: d.counts.gone_by_reason,
            unavailable: d.unavailable, filter_note: d.filter_note, messages: p.messages.length, sent: p.sent_count, refused: p.refused}}}];""", [3100, 0])
    w.code("State only", "return [{json: $json.next_state}];   // the file holds the state and nothing else", [3320, 0])
    w.add("State to file", "n8n-nodes-base.convertToFile", {"operation": "toJson", "mode": "each", "options": {"fileName": "published-state.json", "format": True}}, [3540, 0], 1.1)
    w.add("Write state", "n8n-nodes-base.readWriteFile", {"operation": "write", "fileName": "={{ $('Remember this run').first().json.state_path }}", "dataPropertyName": "data", "options": {}}, [3760, 0], 1)
    IF(w, "Anything posted?", "={{ $('Remember this run').first().json.wrote_posted }}", [3980, 0])
    w.code("Posted ids only", "return [{json: {ids: $('Remember this run').first().json.posted_ids}}];", [4200, -100])
    w.add("Posted to file", "n8n-nodes-base.convertToFile", {"operation": "toJson", "mode": "each", "options": {"fileName": "posted.json", "format": True}}, [4420, -100], 1.1)
    w.add("Write posted", "n8n-nodes-base.readWriteFile", {"operation": "write", "fileName": "={{ $('Remember this run').first().json.posted_path }}", "dataPropertyName": "data", "options": {}}, [4640, -100], 1)
    w.add("Wait for both", "n8n-nodes-base.merge", {"numberInputs": 2}, [4860, 0], 3.2)
    w.code("Daily summary", "return [{json: $('Remember this run').first().json.summary}];", [5080, 0])
    for a_, b_ in [("Manual", "Settings"), ("Every day", "Settings"), ("Settings", "Read state"), ("Read state", "Extract state"), ("Extract state", "Read posted"), ("Read posted", "Extract posted"),
                 ("Extract posted", "Remember what exists"), ("Remember what exists", "Collect input"), ("Collect input", "01 · Collect"), ("01 · Collect", "02 · Filter"), ("02 · Filter", "Delta input"),
                 ("Delta input", "03 · Delta"), ("03 · Delta", "Post input"), ("Post input", "04 · Post"), ("04 · Post", "Remember this run"), ("Remember this run", "State only"), ("State only", "State to file"),
                 ("State to file", "Write state"), ("Write state", "Anything posted?"), ("Posted ids only", "Posted to file"), ("Posted to file", "Write posted"), ("Write posted", "Wait for both"),
                 ("Wait for both", "Daily summary")]:
        w.link(a_, b_)
    w.link("Anything posted?", "Posted ids only", 0, 0)
    w.link("Anything posted?", "Wait for both", 1, 1)
    return w


def main():
    for key, fn in (("collect", build_collect), ("filter", build_filter), ("delta", build_delta), ("post", build_post), ("daily", build_daily)):
        wf = fn().json()
        path = os.path.join(ROOT, FOLDERS[key], "workflow.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(wf, f, indent=1, ensure_ascii=False)
            f.write("\n")
        print(f"{FOLDERS[key]}/workflow.json  id {WF_ID[key]}  {len(wf['nodes'])} nodes")


if __name__ == "__main__":
    main()
