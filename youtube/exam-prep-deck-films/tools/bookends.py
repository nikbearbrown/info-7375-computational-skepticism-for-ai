#!/usr/bin/env python3
"""bookends.py - the six bookend beats in the decks' own Northeastern look, rendered to media/<BID>.mp4.

    python3 bookends.py <reel-folder> [--stills]

Bear, 2026-11-12: the films switched from the Brutalist Claude palette (bookends) to the Northeastern
deck look (body); "they should all be in northeastern". So the opening card, the writer, the labels card,
the recap, Your Turn and the outro are drawn here in the deck's own vocabulary: white page (the Northeastern brand spec allows
no dark ground; the first build's black title card failed the contrast checks), Lato, NU red #C8102E as the one accent, the
8 px red top rule. Every frame is a pure function of time t, so the capture is exact and repeatable.

Each clip is exactly as long as the beat's measured audio (the audio is the clock). --stills writes a PNG of
each bookend at 30/60/95% into <reel>/_qc/bookends/ instead of video, for looking at.
"""
import argparse
import base64
import html
import json
import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deck_capture import FPS, encode  # noqa: E402
from films import TOOLKIT  # noqa: E402

sys.path.insert(0, str(TOOLKIT / "runtime" / "scripts"))
from professor_bear import pick  # noqa: E402

LATO = TOOLKIT / "runtime" / "fonts" / "Lato" / "static"
CLAUDE_LOGO = TOOLKIT / "icons" / "logos" / "claude" / "claude-01.svg"
HANDLE = "@NikBearBrown"

PAGE = r"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Lato;font-weight:400;src:url("%(lato_r)s")}
@font-face{font-family:Lato;font-weight:700;src:url("%(lato_b)s")}
:root{--red:#C8102E;--ink:#000;--body:#2D2926;--muted:#545454;--soft:#C4C4C4;--grid:#E3E3E3;--tint:#FBE7EA}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1920px;height:1080px;overflow:hidden;background:#fff;font-family:Lato,sans-serif;-webkit-font-smoothing:antialiased}
.scene{position:absolute;inset:0;display:none;padding:0 120px;background:#fff;color:var(--ink)}
.scene.on{display:block}
.dark{background:#000;color:#fff}
.rule{position:absolute;top:0;left:0;right:0;height:8px;background:var(--red)}
.dark .rule{height:10px}
.eyebrow{font-size:30px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--red)}
.title{font-size:56px;font-weight:400;line-height:1.08;letter-spacing:-.01em;margin-top:22px}
.handle{position:absolute;right:120px;bottom:64px;font-size:30px;color:var(--muted)}
.dark .handle{color:var(--soft)}
.rise{transition:none}
/* opening */
#open .eyebrow{position:absolute;left:120px;top:104px;font-size:30px;letter-spacing:.2em}
#open .portrait{position:absolute;left:120px;top:200px;width:580px;height:580px;object-fit:cover}
#open .who{position:absolute;left:120px;top:812px;font-size:36px}
#open .who2{position:absolute;left:120px;top:862px;font-size:30px;color:var(--muted)}
#open .right{position:absolute;left:800px;top:300px;width:1000px}
#open .t{font-size:96px;line-height:1.02;letter-spacing:-.02em}
#open .bar{width:120px;height:8px;background:var(--red);margin:48px 0 40px}
#open .sub{font-size:38px;line-height:1.3;color:var(--muted)}
/* idea */
#idea .text{position:absolute;left:120px;top:380px;width:1680px;font-size:76px;line-height:1.18;white-space:pre-wrap;letter-spacing:-.01em}
#idea .new{color:var(--red)}
#idea .hl{color:var(--red)}
#idea .caret{display:inline-block;width:5px;height:.95em;background:var(--ink);vertical-align:-.12em;margin-left:3px}
/* labels */
.rows{margin-top:56px}
.row{display:grid;grid-template-columns:520px 1fr;column-gap:40px;align-items:center;min-height:96px;border-top:1.5px solid var(--grid)}
.row:last-child{border-bottom:1.5px solid var(--grid)}
.row>span{justify-self:start}
.tag{display:inline-block;font-size:30px;padding:8px 16px 9px;border:1.5px solid #909090;color:var(--muted)}
.tag.book{background:#2A1A0E;border-color:#2A1A0E;color:#fff}
.badge{display:inline-block;font-size:30px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:9px 12px 8px;border:1px solid var(--soft);color:var(--muted)}
.mean{font-size:34px;color:var(--body);line-height:1.3}
/* recap */
.bullets{list-style:none;margin-top:56px;display:flex;flex-direction:column;gap:30px;max-width:1600px}
.bullets li{display:grid;grid-template-columns:18px 1fr;column-gap:28px;font-size:38px;line-height:1.32;color:var(--body)}
.bullets li::before{content:"";width:18px;height:18px;background:var(--red);margin-top:calc((38px*1.32 - 18px)/2)}
/* your turn */
.box{margin-top:44px;border:2px solid var(--soft);padding:30px 40px 36px;min-height:330px}
.boxhead{display:flex;align-items:center;gap:16px;font-size:30px;color:var(--muted);margin-bottom:22px}
.boxhead img{width:44px;height:44px}
.cmd{font-size:33px;line-height:1.42;color:var(--body);white-space:pre-wrap}
.checks{margin-top:34px;display:flex;flex-direction:column;gap:18px}
.check{display:grid;grid-template-columns:44px 1fr;align-items:center;font-size:32px;color:var(--body)}
.check svg{width:32px;height:32px}
/* outro */
#out .center{position:absolute;left:120px;right:120px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center}
#out .t{font-size:92px;line-height:1.04;letter-spacing:-.02em}
#out .bar{width:120px;height:8px;background:var(--red);margin:48px 0 40px}
#out .h{font-size:52px;color:var(--muted)}
</style></head><body>%(body)s<script>
var C = %(cfg)s;
function ease(x){x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)}
function show(id){document.querySelectorAll('.scene').forEach(function(s){s.classList.toggle('on',s.id===id)})}
function rise(el,t,t0){var p=ease((t-t0)/0.45);el.style.opacity=p;el.style.transform='translateY('+(18*(1-p))+'px)'}
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;')}
function renderIdea(t){
  var I=C.idea, txt=I.text, out;
  if(t<I.typeEnd){var n=0;for(var i=0;i<I.typeTimes.length;i++){if(I.typeTimes[i]<=t)n=i+1}
    out=esc(txt.slice(0,n))+'<span class="caret"></span>'}
  else if(t<I.hlEnd){var a=txt.indexOf(I.trig);out=esc(txt.slice(0,a))+'<span class="hl">'+esc(I.trig)+'</span>'+esc(txt.slice(a+I.trig.length))}
  else{var a2=txt.indexOf(I.trig),pre=txt.slice(0,a2),post=txt.slice(a2+I.trig.length),keep,add;
    var del=Math.min(I.trig.length,Math.floor(Math.max(0,t-I.hlEnd)/I.delStep));
    if(del<I.trig.length){keep=I.trig.slice(0,I.trig.length-del);out=esc(pre)+'<span class="hl">'+esc(keep)+'</span><span class="caret"></span>'+esc(post)}
    else{var t2=t-I.hlEnd-I.trig.length*I.delStep;var m=Math.min(I.rep.length,Math.floor(Math.max(0,t2)/I.repStep)+ (t2>=0?1:0));
      out=esc(pre)+'<span class="new">'+esc(I.rep.slice(0,m))+'</span>'+(m<I.rep.length||t<I.caretOff?'<span class="caret"></span>':'')+esc(post)}}
  document.querySelector('#idea .text').innerHTML=out;
}
window.__render=function(scene,t){
  show(scene);
  if(scene==='idea')renderIdea(t);
  if(scene==='defs')document.querySelectorAll('#defs .row').forEach(function(r,i){rise(r,t,C.defs[i])});
  if(scene==='recap')document.querySelectorAll('#recap li').forEach(function(r,i){rise(r,t,C.recap[i])});
  if(scene==='turn'){var T=C.turn,n=Math.round(T.cmd.length*Math.max(0,Math.min(1,(t-T.t0)/(T.t1-T.t0))));
    document.querySelector('#turn .cmd').innerHTML=esc(T.cmd.slice(0,n))+(n<T.cmd.length?'<span class="caret" style="display:inline-block;width:4px;height:1em;background:#000;vertical-align:-.15em;margin-left:2px"></span>':'');
    document.querySelectorAll('#turn .check').forEach(function(r,i){rise(r,t,T.checks[i])});}
  return true;
};
</script></body></html>"""

CHECK = '<svg viewBox="0 0 32 32"><path d="M5 17 L13 25 L27 8" fill="none" stroke="#C8102E" stroke-width="5" stroke-linecap="square"/></svg>'


def words(s):
    return len(re.findall(r"[^\W_][\w'’-]*", s))


def cues(parts, total, lead=0.0, tail=0.6):
    """Start time of each spoken part, by its share of the words (the audio is one take, so this is an estimate)."""
    w = [max(1, words(p)) for p in parts]
    span = max(0.5, total - lead - tail)
    out, acc = [], 0
    for x in w:
        out.append(round(lead + span * acc / sum(w), 3))
        acc += x
    return out


def build(reel: Path):
    sheet = json.loads((reel / "beat_sheet.json").read_text())
    md = sheet["metadata"]
    B = {b["beat_id"]: b for b in sheet["beats"]}
    bk = md["bookends"]
    for bid in ("BOPEN", "BIDEA", "BDEFS", "BVDT", "BHTF", "BOUT"):
        if not B[bid].get("actual_duration_s"):
            raise SystemExit(f"{bid} has no measured audio; voice the film first")
    D = {bid: B[bid]["actual_duration_s"] for bid in B}
    portrait = pick("1x1", seed=md["slug"], public=True)
    e = html.escape

    # ---- opening ----
    title_html = "<br>".join(e(x) for x in md["lecture_opening_title_lines"])
    s_open = (f'<section class="scene" id="open"><div class="rule"></div><div class="eyebrow">{e(md["playlist"])}</div>'
              f'<img class="portrait" src="{Path(portrait).as_uri()}"><div class="who">Professor Bear</div><div class="who2">Liam, in for Bear · Narration</div>'
              f'<div class="right"><div class="t">{title_html}</div><div class="bar"></div><div class="sub">{e(md["lecture_opening_description"])}</div></div>'
              f'<div class="handle">{HANDLE}</div></section>')

    # ---- idea (writer) ----
    idea = bk["idea"]
    text, trig, rep = idea["text"], idea["triggerWords"], idea["replacementWords"]
    d = D["BIDEA"]
    t, times = 0.8, []
    for ch in text:
        times.append(round(t, 3))
        t += 0.045 + (0.12 if ch in ",." else 0) + (0.25 if ch == "\n" else 0)
    type_end = t
    hl_start = max(type_end + 0.6, 0.5 * d)
    del_step, rep_step = 0.035, 0.05
    need = 0.5 + len(trig) * del_step + len(rep) * rep_step + 0.8
    if hl_start + need > d:
        hl_start = max(type_end + 0.3, d - need)
    cfg_idea = {"text": text, "trig": trig, "rep": rep, "typeTimes": times, "typeEnd": hl_start, "hlEnd": hl_start + 0.5,
                "delStep": del_step, "repStep": rep_step, "caretOff": hl_start + need - 0.4}
    s_idea = '<section class="scene" id="idea"><div class="rule"></div><div class="text"></div>' f'<div class="handle">{HANDLE}</div></section>'

    # ---- labels ----
    rows = []
    for lab in bk["labels"]:
        if lab["kind"] == "tag":
            chip = f'<span class="tag{" book" if lab["key"] == "in the book text" else ""}">{e(lab["key"])}</span>'
        else:
            chip = f'<span class="badge">{e(lab["key"])}</span>'
        rows.append(f'<div class="row">{chip}<div class="mean">{e(lab["meaning"])}</div></div>')
    s_defs = ('<section class="scene" id="defs"><div class="rule"></div><div style="padding-top:96px"><div class="eyebrow">Before the terms</div>'
              '<div class="title">Labels you will see on every slide</div>' f'<div class="rows">{"".join(rows)}</div></div><div class="handle">{HANDLE}</div></section>')
    defs_cues = cues(bk["defs_parts"], D["BDEFS"])[1:]

    # ---- recap ----
    lis = "".join(f"<li>{e(x)}</li>" for x in bk["recap_lines"])
    s_recap = ('<section class="scene" id="recap"><div class="rule"></div><div style="padding-top:96px"><div class="eyebrow">Recap</div>'
               f'<div class="title">What we established</div><ul class="bullets">{lis}</ul></div><div class="handle">{HANDLE}</div></section>')
    recap_cues = cues([bk["recap_lead"]] + bk["recap_lines"], D["BVDT"], lead=B["BVDT"].get("lead_silence_s", 0))[1:]

    # ---- your turn ----
    logo = base64.b64encode(CLAUDE_LOGO.read_bytes()).decode()
    checks = "".join(f'<div class="check">{CHECK}<div>{e(c)}</div></div>' for c in bk["checks"])
    s_turn = ('<section class="scene" id="turn"><div class="rule"></div><div style="padding-top:96px"><div class="eyebrow">Your turn</div>'
              f'<div class="title">{e(bk["segment"])}</div><div class="box"><div class="boxhead"><img src="data:image/svg+xml;base64,{logo}">Paste this into Claude</div>'
              f'<div class="cmd"></div></div><div class="checks">{checks}</div></div><div class="handle">{HANDLE}</div></section>')
    dt = D["BHTF"]
    cfg_turn = {"cmd": bk["command"], "t0": 0.5, "t1": round(dt * 0.84, 3), "checks": [round(dt * 0.86, 3), round(dt * 0.91, 3)]}

    # ---- outro ----
    s_out = (f'<section class="scene" id="out"><div class="rule"></div><div class="center"><div class="t">{e(md["title"])}</div>'
             f'<div class="bar"></div><div class="h">{HANDLE}</div></div></section>')

    cfg = {"idea": cfg_idea, "defs": defs_cues, "recap": recap_cues, "turn": cfg_turn}
    page = PAGE % {"lato_r": (LATO / "Lato-Regular.ttf").as_uri(), "lato_b": (LATO / "Lato-Bold.ttf").as_uri(),
                   "body": s_open + s_idea + s_defs + s_recap + s_turn + s_out, "cfg": json.dumps(cfg)}
    out = reel / "bookends"
    out.mkdir(exist_ok=True)
    (out / "bookends.html").write_text(page)
    plan = {"BOPEN": ("open", None), "BIDEA": ("idea", cfg_idea["caretOff"] + 0.2), "BDEFS": ("defs", (defs_cues[-1] if defs_cues else 0) + 0.6),
            "BVDT": ("recap", recap_cues[-1] + 0.6), "BHTF": ("turn", cfg_turn["checks"][-1] + 0.6), "BOUT": ("out", None)}
    (out / "plan.json").write_text(json.dumps({"portrait": portrait, "plan": plan, "cfg": cfg}, indent=1))
    return out / "bookends.html", plan, D, portrait


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("reel")
    ap.add_argument("--stills", action="store_true")
    a = ap.parse_args()
    reel = Path(a.reel).resolve()
    page, plan, D, portrait = build(reel)
    with sync_playwright() as pw:
        br = pw.chromium.launch(headless=True, args=["--force-color-profile=srgb", "--allow-file-access-from-files"])
        ctx = br.new_context(viewport={"width": 1920, "height": 1080}, device_scale_factor=1 if a.stills else 2)
        pg = ctx.new_page()
        errors = []
        pg.on("pageerror", lambda x: errors.append(str(x)))
        pg.goto(page.as_uri(), wait_until="load")
        pg.evaluate("document.fonts.ready.then(()=>1)")
        fams = pg.evaluate("Array.from(document.fonts).filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight)")
        if not any("Lato" in f for f in fams):
            pg.evaluate("Promise.all(Array.from(document.fonts).map(f=>f.load()))")
            fams = pg.evaluate("Array.from(document.fonts).filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight)")
        if not any("Lato" in f for f in fams):
            raise SystemExit(f"Lato did not load: {fams}")
        pg.wait_for_function("Array.from(document.images).every(i=>i.complete && i.naturalWidth>0)")
        cdp = ctx.new_cdp_session(pg)

        def shot(fmt="jpeg"):
            r = cdp.send("Page.captureScreenshot", {"format": fmt, "quality": 95} if fmt == "jpeg" else {"format": fmt})
            return base64.b64decode(r["data"])

        if a.stills:
            qc = reel / "_qc" / "bookends"
            qc.mkdir(parents=True, exist_ok=True)
            for bid, (scene, _) in plan.items():
                for f in (0.3, 0.6, 0.95):
                    pg.evaluate("([s,t])=>window.__render(s,t)", [scene, D[bid] * f])
                    (qc / f"{bid}_{int(f * 100)}.png").write_bytes(shot("png"))
            print(f"stills in {qc}")
        else:
            for bid, (scene, anim_end) in plan.items():
                frames = []
                n = 1 if anim_end is None else min(round(D[bid] * FPS), round(anim_end * FPS) + 1)
                for i in range(n):
                    pg.evaluate("([s,t])=>window.__render(s,t)", [scene, i / FPS])
                    frames.append(shot())
                total = encode(frames, D[bid], reel / "media" / f"{bid}.mp4")
                print(f"{bid}: {len(frames)} drawn frames, {total / FPS:.2f} s", flush=True)
        if errors:
            raise SystemExit(f"page errors: {errors}")
        br.close()
    print(f"portrait: {portrait}")


if __name__ == "__main__":
    main()
