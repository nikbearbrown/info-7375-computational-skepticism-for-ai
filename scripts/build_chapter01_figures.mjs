#!/usr/bin/env node
// Original chapter-specific figure source. No network, generated data, or paid APIs.
// node scripts/build_chapter01_figures.mjs OUTPUT_DIRECTORY BRUTALIST_FONT_DIRECTORY
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { resolve, join } from 'node:path';

const [outArg, fontArg] = process.argv.slice(2);
if (!outArg || !fontArg) throw new Error('Supply an output directory and the Brutalist runtime/fonts directory.');
const out = resolve(outArg);
const fontDir = resolve(fontArg);
mkdirSync(out, { recursive: true });
const fonts = [
  ['Inter', 'Inter/static/Inter_28pt-Regular.ttf', 400],
  ['Inter', 'Inter/static/Inter_28pt-Medium.ttf', 500],
  ['EB Garamond', 'EB_Garamond/static/EBGaramond-Regular.ttf', 400],
];
const embedded = fonts.map(([name, path, weight]) => `@font-face{font-family:'${name}';font-weight:${weight};src:url(data:font/ttf;base64,${readFileSync(join(fontDir, path)).toString('base64')}) format('truetype');}`).join('\n');
const ink = '#2a1a0e', accent = '#C8102E', secondary = '#545454', border = '#D4D4D4';
const esc = s => String(s).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const text = (x, y, s, size = 26, fill = ink, weight = 400, anchor = 'start', family = 'Inter') => `<text x="${x}" y="${y}" font-family="${family}" font-size="${size}" font-weight="${weight}" fill="${fill}" text-anchor="${anchor}">${esc(s)}</text>`;
const lines = (x, y, rows, size = 25, fill = ink, gap = 36) => rows.map((s, i) => text(x, y + gap * i, s, size, fill)).join('\n');
const rect = (x, y, w, h, stroke = border, fill = '#FFFFFF', width = 2) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${fill}" stroke="${stroke}" stroke-width="${width}"/>`;
const line = (x1, y1, x2, y2, stroke = ink, dash = '') => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${stroke}" stroke-width="2"${dash ? ` stroke-dasharray="${dash}"` : ''}/>`;
const arrow = (x1, y1, x2, y2) => `${line(x1, y1, x2, y2)}<path d="M ${x2 - 10} ${y2 - 7} L ${x2} ${y2} L ${x2 - 10} ${y2 + 7}" fill="none" stroke="${ink}" stroke-width="2"/>`;
const down = (x, y1, y2) => `${line(x, y1, x, y2)}<path d="M ${x - 7} ${y2 - 10} L ${x} ${y2} L ${x + 7} ${y2 - 10}" fill="none" stroke="${ink}" stroke-width="2"/>`;
const label = (x, y, s) => text(x, y, s, 20, secondary, 500);
const card = (x, y, w, h, title, body) => rect(x, y, w, h) + text(x + 24, y + 42, title, 28, ink, 500) + lines(x + 24, y + 90, body);
const foot = (s, y) => line(48, y - 28, 1152, y - 28, border) + text(48, y, s, 21, secondary);

function save(n, title, subtitle, desc, h, content) {
  const file = join(out, `01-the-skeptics-toolkit-fig-${String(n).padStart(2, '0')}.svg`);
  if (existsSync(`${file}.verified.json`) && JSON.parse(readFileSync(`${file}.verified.json`, 'utf8')).verified) {
    throw new Error(`Refusing to regenerate a human-verified figure: ${file}`);
  }
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="${h}" viewBox="0 0 1200 ${h}" role="img" aria-labelledby="title desc">
<title id="title">${esc(title)}</title><desc id="desc">${esc(desc)}</desc>
<defs><style>${embedded}</style></defs>
<rect width="1200" height="${h}" fill="#FFFFFF"/>
${text(48, 60, title, 42, ink, 400, 'start', 'EB Garamond')}
${text(48, 100, subtitle, 23, secondary)}
${line(48, 126, 1152, 126, border)}
${content}
</svg>\n`;
  writeFileSync(file, svg);
  console.log(file);
}

save(1, 'Turn doubt into an inspection', 'Descartes: name the conditions that would make the claim wrong.',
  'A success claim branches into checks of coverage, inputs, and context. Each check requires evidence before a human decides whether to accept, investigate, or stop.', 710,
  rect(48, 158, 1104, 84, ink) + text(76, 211, 'Claim: “The system completed the task.”', 32, ink, 500) +
  down(600, 243, 273) + line(220, 273, 980, 273) + [220, 600, 980].map(x => down(x, 273, 310)).join('') +
  card(48, 310, 344, 198, 'Coverage', ['Was this kind of case', 'represented in the', 'validation evidence?']) +
  card(428, 310, 344, 198, 'Inputs', ['Was the relevant', 'signal present and', 'measured correctly?']) +
  card(808, 310, 344, 198, 'Context', ['Does the deployed', 'system match the', 'one that was tested?']) +
  [220, 600, 980].map(x => line(x, 508, x, 539)).join('') + line(220, 539, 980, 539) + down(600, 539, 568) +
  rect(48, 568, 1104, 74, accent) + text(76, 614, 'Attach evidence to each check. Then accept, investigate, or stop.', 27) +
  text(48, 682, 'A clean result supports this check; it does not prove universal safety.', 21, secondary));

save(2, 'The pattern persists. Until it does not.', 'Hume: past observations do not logically guarantee the next outcome.',
  'A schematic expectation curve rises with repeated feeding and stays high before the surprise. At the regime boundary the observed outcome differs from the prediction; no probability values or measured data are shown.', 700,
  label(70, 184, 'Expectation based on past feeding') +
  line(95, 220, 95, 490) + arrow(95, 490, 1120, 490) +
  `<path d="M 115 452 C 300 375 520 290 775 271" stroke="${accent}" stroke-width="5" fill="none"/>` +
  `<path d="M 775 271 C 835 267 935 264 1080 262" stroke="${accent}" stroke-width="5" stroke-dasharray="10 8" fill="none"/>` +
  text(370, 237, 'Repeated feeding strengthens the expectation.', 24) +
  line(870, 210, 870, 490, ink, '7 7') + text(892, 217, 'Conditions change', 22, ink, 500) +
  text(904, 328, 'Prediction:', 23, secondary) + text(904, 362, 'another meal', 27) +
  rect(898, 397, 244, 62, ink) + text(919, 437, 'Outcome: no meal', 24, ink, 500) +
  label(116, 532, 'Past observations') + label(909, 532, 'Next observation') +
  text(70, 593, 'The surprise belongs to the world. The confidence belonged to the model.', 27) +
  foot('Conceptual timeline, not measured probabilities. No guarantee of automatic uncertainty detection.', 666));

save(3, 'Three moves you can carry into a review', 'Different questions expose different weaknesses in the same claim.',
  'Three parallel rows map Descartes to assumptions and evidence, Hume to changed conditions, and Popper to an observable falsifier. The fourth move, artifact versus world, follows in the next section.', 620,
  label(72, 175, 'Move') + label(350, 175, 'Question to ask') + label(855, 175, 'Leave behind') +
  [0, 1, 2].map(i => line(48, 201 + 116 * i, 1152, 201 + 116 * i, border)).join('') +
  text(72, 253, 'Descartes', 30, ink, 500) + lines(350, 241, ['What assumptions could make', 'this claim wrong?']) + lines(855, 241, ['A checkable', 'assumption list']) +
  text(72, 369, 'Hume', 30, ink, 500) + lines(350, 357, ['What changed since the', 'evidence was collected?']) + lines(855, 357, ['A context-shift', 'check']) +
  text(72, 485, 'Popper', 30, ink, 500) + lines(350, 473, ['What observation would', 'show that the claim fails?']) + lines(855, 473, ['A test with a', 'failure condition']) +
  foot('Next: Kant’s slice adds the artifact–world distinction to make four moves.', 584));

save(4, 'The artifact is not the world', 'Kant’s slice: inspect the relationship, not only the representation.',
  'Two rows pair what a system measured with what mattered. The Netflix Prize measured error in predicting star ratings, while what mattered was a member finding something to watch and staying subscribed. The Amazon recruiting engine measured resemblance to past résumés, while what mattered was whether a person can do the job. A verification bridge checks the thing that mattered. The figure is a schematic of the two cases, not captured results.', 860,
  label(48, 176, 'Artifact: what the system measured') + label(706, 176, 'World: what mattered') +
  card(48, 192, 446, 186, 'Netflix Prize', ['Error in predicting star', 'ratings on a frozen set', 'of earlier ratings.']) +
  card(706, 192, 446, 186, 'Netflix Prize', ['Does a member find', 'something to watch tonight', 'and keep subscribing?']) +
  arrow(510, 285, 688, 285) + text(598, 257, 'Check against', 21, secondary, 400, 'middle') +
  card(48, 406, 446, 186, 'Amazon recruiting', ['Resemblance to a decade', 'of submitted résumés.']) +
  card(706, 406, 446, 186, 'Amazon recruiting', ['Can this person', 'do the job?']) +
  arrow(510, 499, 688, 499) + text(598, 471, 'Check against', 21, secondary, 400, 'middle') +
  down(600, 592, 622) +
  rect(48, 622, 1104, 150, accent) + text(76, 666, 'The verification bridge', 29, ink, 500) +
  lines(76, 709, ['Check the thing that mattered, not only the number that stood in for it:', 'retention for the contest, job performance for the screen.'], 26) +
  foot('Schematic of the two cases in the chapter. Not captured results.', 830));

save(5, 'Where does the verification work live?', 'A contrast between a checkable mathematical witness and a deployed AI claim.',
  'Two comparisons show producing and checking factors versus producing an AI report and checking the relevant world state. The figure shows types of work, not benchmarked costs or a universal complexity claim.', 670,
  label(70, 176, 'Mathematical example') +
  card(48, 198, 492, 153, 'Produce', ['Search for factors of a', 'large integer.']) +
  card(660, 198, 492, 153, 'Verify', ['Multiply the proposed factors;', 'compare with the integer.']) + arrow(557, 274, 642, 274) +
  label(70, 414, 'AI deployment example') +
  card(48, 436, 492, 153, 'Produce', ['Generate a report that says', 'the task was completed.']) +
  card(660, 436, 492, 153, 'Verify', ['Inspect actual state, context,', 'and relevant consequences.']) + arrow(557, 512, 642, 512) +
  foot('Qualitative comparison, not measured time or cost. Budget for checking the world.', 635));

save(6, 'Five capacities. One accountable decision.', 'These are complementary supervisory responsibilities, not a rigid sequence.',
  'Five rows connect concrete human responsibilities to executive integration: plausibility auditing, problem formulation, tool orchestration, interpretive judgment, and executive integration. AI can prepare evidence but people own framing and the decision.', 870,
  [
    ['1', 'Plausibility auditing', 'Does this result make sense in this domain?'],
    ['2', 'Problem formulation', 'Are we answering the question that matters?'],
    ['3', 'Tool orchestration', 'Which tool fits, or should we not deploy yet?'],
    ['4', 'Interpretive judgment', 'What does this result mean in this context?'],
    ['5', 'Executive integration', 'Who weighs the evidence and owns the decision?'],
  ].map(([n, title, question], i) => {
    const y = 162 + i * 104;
    return rect(48, y, 1104, 86, n === '5' ? accent : border) + text(73, y + 53, n, 31, accent, 500) + text(128, y + 51, title, 27, ink, 500) + text(503, y + 51, question, 24);
  }).join('') +
  text(48, 737, 'AI can gather, compare, and organize evidence.', 27) +
  text(48, 780, 'Humans should set the question, judge the stakes, and own the decision.', 27, ink, 500) +
  text(48, 840, 'For each capacity, name the responsible person and the evidence they will see.', 21, secondary));

save(7, 'Interrupt the fluency trap', 'A polished answer can increase confidence without adding evidence.',
  'The trap moves from fluent output to confidence in the answer and then confidence in one’s own evaluation. A separate evidence-first path specifies a failure condition before reading, checks it afterward, and records the result.', 700,
  label(48, 174, 'The trap: confidence grows in two stages') +
  card(48, 204, 326, 183, 'Fluent output', ['Clear language.', 'Specific details.', 'A confident tone.']) +
  card(437, 204, 326, 183, '“The answer is right.”', ['Confidence in', 'the output grows.']) +
  card(826, 204, 326, 183, '“My review is right.”', ['Confidence in my', 'own evaluation grows.']) +
  arrow(389, 289, 421, 289) + arrow(778, 289, 810, 289) +
  label(48, 457, 'The interruption: criteria first, evidence second') +
  rect(48, 484, 1104, 116, accent) +
  text(76, 529, 'Before reading', 26, ink, 500) + text(400, 529, 'After reading', 26, ink, 500) + text(796, 529, 'Record', 26, ink, 500) +
  text(76, 571, 'Name a failure condition.', 23) + text(400, 571, 'Test against evidence.', 23) + text(796, 571, 'Pass, fail, or unknown.', 23) +
  foot('Conceptual mechanism. Neither awkward nor fluent wording establishes whether a claim is true.', 658));

save(8, 'Make skepticism part of the workflow', 'A checkpoint works only when someone owns it and can see the evidence.',
  'A team workflow has three stages: before the run, during the run, and before action. Humans lock predictions and limits, AI executes in scope and preserves traces, and a named human compares actual state with the claim. Unresolved checks loop back for revision.', 750,
  label(48, 180, 'Before the run') + label(437, 180, 'During the run') + label(826, 180, 'Before action') +
  card(48, 211, 326, 254, 'Human frames', ['Define success.', 'Lock a prediction.', 'Set failure conditions.', 'Assign review ownership.', 'Bound the test safely.']) +
  card(437, 211, 326, 254, 'AI executes', ['Stay within scope.', 'Capture inputs/actions.', 'Preserve tool results.', 'Report uncertainties.', 'Hand over the evidence.']) +
  card(826, 211, 326, 254, 'Human verifies', ['Inspect actual state.', 'Compare with the claim.', 'Apply domain judgment.', 'Accept, revise, or stop.', 'Record the decision.']) +
  arrow(389, 337, 421, 337) + arrow(778, 337, 810, 337) +
  line(990, 465, 990, 535) + line(990, 535, 212, 535) + down(212, 535, 567) +
  rect(48, 567, 1104, 80, accent) + text(76, 617, 'If the check fails or remains unknown: stop, revise, and run a new test.', 27) +
  foot('Keep the original prediction. Append the observation and what changed your mind.', 712));
