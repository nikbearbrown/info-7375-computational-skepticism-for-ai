#!/usr/bin/env node
// Runs the JavaScript place reader and K-12 reader (shared/lib/judge.js) over a list of strings.
// usage: node tools/js_where.js <keywords.json> <input.json>   where input = {"locations": [...], "titles": [...]}
const fs = require('fs'), path = require('path');
const {where, k12Hits} = require(path.join(__dirname, '..', 'shared', 'lib', 'judge.js'));
const kw = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const input = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
process.stdout.write(JSON.stringify({
  locations: input.locations.map(t => where(t, kw.location_rule)),
  titles: input.titles.map(t => k12Hits(t, '', kw.k12_rule).title),
}));
