// Requires Playwright and installed Google Chrome. Uses an isolated temporary profile.
// node scripts/render_chapter01_figures.cjs images
const { chromium } = require('playwright');
const fs = require('node:fs');
const path = require('node:path');
if (!process.argv[2]) throw new Error('Supply the chapter image directory.');
const imageDir = path.resolve(process.argv[2]);
(async () => {
  const browser = await chromium.launch({headless:true, channel:'chrome'});
  try {
    const page = await browser.newPage({viewport:{width:1200,height:900},deviceScaleFactor:3.125});
    for (const name of fs.readdirSync(imageDir).filter(n => /^01-the-skeptics-toolkit-fig-\d{2}\.svg$/.test(n)).sort()) {
      const output = path.join(imageDir, name.replace('.svg', '.png'));
      if (fs.existsSync(output + '.verified.json') && JSON.parse(fs.readFileSync(output + '.verified.json','utf8')).verified) throw new Error('Refusing to overwrite a human-verified PNG: ' + output);
      const svg = fs.readFileSync(path.join(imageDir, name), 'utf8');
      const height = Number(svg.match(/height="(\d+)"/)[1]);
      await page.setViewportSize({width:1200,height});
      await page.setContent('<!doctype html><html><head><meta charset="utf-8"><style>body{margin:0}svg{display:block}</style></head><body>'+svg+'</body></html>');
      await page.evaluate(async () => { await document.fonts.load('42px "EB Garamond"'); await document.fonts.load('26px "Inter"'); await document.fonts.ready; });
      const audit = await page.evaluate(() => {
        const svg = document.querySelector('svg'), texts = [...svg.querySelectorAll('text')];
        const rects = [...svg.querySelectorAll('rect')].filter(r => r.hasAttribute('x'));
        const failures=[];
        for (const t of texts) {
          if (!t.textContent.trim()) continue;
          const b=t.getBBox();
          if(b.x < 0 || b.y < 0 || b.x+b.width>svg.viewBox.baseVal.width || b.y+b.height>svg.viewBox.baseVal.height) failures.push('outside canvas: '+t.textContent);
          for(const r of rects) {
            const rb=r.getBBox(), x=Number(t.getAttribute('x')), y=Number(t.getAttribute('y'));
            if(x>rb.x && x<rb.x+rb.width && y>rb.y && y<rb.y+rb.height && (b.x<rb.x || b.x+b.width>rb.x+rb.width || b.y<rb.y || b.y+b.height>rb.y+rb.height)) failures.push('outside box: '+t.textContent);
          }
        }
        return {fontEB:document.fonts.check('42px "EB Garamond"'),fontInter:document.fonts.check('26px "Inter"'),failures};
      });
      console.log(name, JSON.stringify(audit));
      if(audit.failures.length) throw new Error('Live font layout check failed');
      await page.screenshot({path:output});
    }
  } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exit(1)});
