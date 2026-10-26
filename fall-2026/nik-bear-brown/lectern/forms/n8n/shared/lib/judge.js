// Port of lectern/collect.py: word_in(), materials_evidence(), connector_evidence(), fold(), places_of(), where(), k12_hits(),
// judge(), and the dedupe and validity checks from main(). Pure functions: no n8n globals. The rules are keywords.json, never this file.
const escRe = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
function wordIn(word, text) {
  return new RegExp('(?<![a-z0-9])' + escRe(word.toLowerCase()) + '(?![a-z0-9])').test(text);
}

function materialsEvidence(bodyLc, kw) {
  const rule = kw.materials_rule || {};
  if (!Object.keys(rule).length) return null;
  const vo = (rule.verb_object || []).filter(p => bodyLc.includes(p.toLowerCase()));
  const au = (rule.audience || []).filter(p => bodyLc.includes(p.toLowerCase()));
  const minVo = rule.min_verb_object === undefined ? 1 : rule.min_verb_object;
  const minAu = rule.min_audience === undefined ? 1 : rule.min_audience;
  if (vo.length >= minVo && au.length >= minAu) return {verb_object: vo.slice(0, 6), audience: au.slice(0, 6)};
  return null;
}

function connectorEvidence(titleLc, bodyLc, kw) {
  const rule = kw.connector_rule || {};
  if (!Object.keys(rule).length) return null;
  const tw = (rule.title_words || []).filter(w => wordIn(w, titleLc));
  const iw = (rule.institution_words || []).filter(w => wordIn(w, bodyLc));
  return (tw.length && iw.length) ? {title: tw, institution: iw.slice(0, 6)} : null;
}

// Lower-case with accents removed ('São Paulo' -> 'sao paulo'), so the place lists can be written in plain letters.
function fold(s) {
  return (s || '').normalize('NFKD').toLowerCase().replace(/[̀-ͯ᪰-᫿᷀-᷿⃐-⃿︠-︯]/g, '');
}

const PLACES = new WeakMap();
const byLength = (a, b) => b.length - a.length || (a < b ? -1 : a > b ? 1 : 0);   // longest first: 'new mexico' before 'mexico'

// Compile location_rule once: folded name -> country for its three tables, plus the regexes that find them.
function placesOf(rule) {
  if (PLACES.has(rule)) return PLACES.get(rule);
  const allowed = new Set(rule.allowed_countries || []);
  const tables = {names: {}, places: {}, codes: {}};
  for (const [country, spec] of Object.entries(rule.countries)) {
    for (const kind of Object.keys(tables)) {
      for (let w of spec[kind] || []) {
        w = fold(w).trim();
        // a string two countries share goes to an allowed one: a stray posting costs less than a lost one
        if (w && (!(w in tables[kind]) || (allowed.has(country) && !allowed.has(tables[kind][w])))) tables[kind][w] = country;
      }
    }
  }
  const alt = words => [...words].sort(byLength).map(escRe).join('|');
  const found = new Set([...Object.keys(tables.names), ...Object.keys(tables.places)]);
  const work = (rule.workplace_words || []).map(fold);
  const compiled = {allowed, ...tables, seps: (rule.separators || []).map(fold),
    words: found.size ? new RegExp('(?<![a-z0-9])(?:' + alt(found) + ')(?![a-z0-9])', 'g') : null,
    codesRx: Object.keys(tables.codes).length ? new RegExp('(?:,|-|\\()\\s*(' + alt(Object.keys(tables.codes)) + ')\\s*(?=$|[,\\-()])') : null,
    workRx: work.length ? new RegExp('(?<![a-z0-9])(?:' + alt(work) + ')(?![a-z0-9])', 'g') : null};
  PLACES.set(rule, compiled);
  return compiled;
}

// One place ('Austin, TX') -> ['allowed' | 'outside', [countries]], or ['workplace' | 'unnamed', []].
// Evidence in this order: a country's own name, then a state or province code after a comma, then a city or region.
function onePlace(seg, t) {
  const hits = t.words ? [...seg.matchAll(t.words)].map(m => m[0]) : [];
  let named = hits.filter(h => h in t.names).map(h => t.names[h]);
  if (!named.length) {
    const m = t.codesRx ? t.codesRx.exec(seg) : null;
    named = m ? [t.codes[m[1]]] : hits.filter(h => h in t.places).map(h => t.places[h]);
  }
  if (named.length) {
    const ok = [...new Set(named.filter(c => t.allowed.has(c)))].sort();
    return ok.length ? ['allowed', ok] : ['outside', [...new Set(named)].sort()];
  }
  const rest = t.workRx ? seg.replace(t.workRx, ' ') : seg;
  return rest.replace(/[^a-z]+/g, '') === '' ? ['workplace', []] : ['unnamed', []];
}

// Which countries a location line names: a posting in several places is allowed if ANY of them is.
// -> {decision: 'allowed' | 'outside' | 'unnamed', countries: [...]}
function where(locationText, rule) {
  const t = placesOf(rule);
  let s = fold(locationText);
  for (const sep of t.seps) s = s.split(sep).join('\n');
  const ok = new Set(), out = new Set();
  let unnamed = false;
  for (const seg of s.split('\n').map(x => x.trim())) {
    if (!seg) continue;
    const [kind, cs] = onePlace(seg, t);
    if (kind === 'allowed') cs.forEach(c => ok.add(c));
    else if (kind === 'outside') cs.forEach(c => out.add(c));
    else if (kind === 'unnamed') unnamed = true;
  }
  if (ok.size) return {decision: 'allowed', countries: [...ok].sort()};
  return {decision: (out.size && !unnamed) ? 'outside' : 'unnamed', countries: [...out].sort()};
}

// Phrases of k12_rule found in the title (and, if the rule lists any, the body).
function k12Hits(title, body, rule) {
  const dash = s => s.toLowerCase().replace(/[‐-―−]/g, '-');   // 'K–12' with an en dash is still K-12
  const t = dash(title), b = dash(body);
  return {title: (rule.title_phrases || []).filter(p => wordIn(p.toLowerCase(), t)),
          body: (rule.body_phrases || []).filter(p => wordIn(p.toLowerCase(), b))};
}

// Returns [matched, rejectReason]; exactly one is null. A posting the keywords would keep is still rejected, with the
// reason, if its place names no allowed country (location_rule) or it is a K-12 role (k12_rule).
function judge(v, kw) {
  const ignore = new Set(((kw.ignore_words_by_company || {})[v.company] || []).map(w => w.toLowerCase()));
  const tl = v.title.toLowerCase(), bl = v.text.toLowerCase();
  const role = kw.role_title.filter(w => !ignore.has(w.toLowerCase()) && wordIn(w, tl));
  const topic = kw.topic_text.filter(w => !ignore.has(w.toLowerCase()) && wordIn(w, bl));
  const flex = kw.flex_text.filter(w => wordIn(w, bl));
  const need = kw.keep_rule.topic_text_min_if_no_title_match;
  const mats = materialsEvidence(bl, kw);
  const conn = connectorEvidence(tl, bl, kw);
  let why;
  if (role.length) why = 'role word in title';
  else if (topic.length >= need) why = `${topic.length} topic words in body (>= ${need})`;
  else if (mats) why = 'body says it produces teaching materials for a named audience';
  else if (conn) why = 'account or partnership role whose body names higher education';
  else return [null, (!(role.length || topic.length) ? 'no-keyword-match' : `only ${topic.length} topic words, no role word in title`)];
  const blocked = [];
  let place = null;
  const locRule = kw.location_rule;
  if (locRule) {
    const w = where(v.location_text || '', locRule);
    if (w.decision === 'outside') blocked.push('country not allowed: ' + w.countries.join(', '));
    else if (w.decision === 'unnamed' && (locRule.if_no_country_named || 'keep') === 'reject') blocked.push('no country named in the location');
    else if (w.decision === 'unnamed') place = {country_named: false, countries_seen: w.countries,
      kept_because: 'the location names no country, so the rule keeps it (if_no_country_named)'};
  }
  const k12Rule = kw.k12_rule;
  if (k12Rule) {
    const h = k12Hits(v.title, v.text, k12Rule);
    if (h.title.length || h.body.length) blocked.push('K-12 role: ' + [...h.title.slice(0, 2).map(p => `'${p}' in the title`), ...h.body.slice(0, 2).map(p => `'${p}' in the body`)].join(' and '));
  }
  if (blocked.length) return [null, blocked.join('; ')];
  return [{role_title: role, topic_text: topic, flex_text: flex, materials: mats, connector: conn,
           kept_because: why, title_only: Boolean(role.length && !topic.length), location: place}, null];
}

// The per-posting checks in collect.main(): returns a reject reason, or null if the posting goes on to judge().
function validity(v) {
  if (!v.title) return 'missing-title';
  if (!v.url) return 'missing-url';
  if (!v.date_posted) return 'unparseable-date';
  return null;
}
if (typeof module !== 'undefined') module.exports = {wordIn, judge, validity, materialsEvidence, connectorEvidence, fold, where, k12Hits};
