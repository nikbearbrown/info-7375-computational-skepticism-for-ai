"""capture.py — public pages this film shows as themselves (SHOW-THE-THING rung 1). Read-only: no sign-in,
no form. A consent banner is declined if one appears. Pages scroll to the passage the narration names, captured
1600x900 at device scale 2.4 (3840 wide). The Agents of Chaos page is rendered from the paper's own PDF.
Receipts: captures/receipts.json"""
import json, sys
from datetime import datetime, timezone
from pathlib import Path
from playwright.sync_api import sync_playwright
HERE = Path(__file__).resolve().parent
OUT = HERE / "captures"; OUT.mkdir(exist_ok=True)
SHOTS = [
    ("propublica", "https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing", "Prediction Fails Differently", 0, 60),
    ("kleinberg", "https://arxiv.org/abs/1609.05807", "Inherent Trade-Offs in the Fair Determination of Risk Scores", 0, 40),
    # nydfs: dfs.ny.gov answers automated browsers with a Cloudflare block (HTTP 403). Not bypassed; the beat quotes the
    # regulator's sentences (fetched as text 2026-10-10) on a drawn document card instead. See FACTCHECK.md.
]
only = set(sys.argv[1:])
DECLINE = ["Reject all", "Reject All", "Decline", "Reject non-essential", "Necessary only", "Only necessary"]
receipts = []
with sync_playwright() as p:
    b = p.chromium.launch(headless=True, executable_path="/Users/bear/Library/Caches/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-mac-arm64/chrome-headless-shell")
    page = b.new_page(viewport={"width": 1600, "height": 900}, device_scale_factor=2.4)
    for name, url, anchor, _, above in SHOTS:
        if only and name not in only: continue
        rec = {"name": name, "url": url, "anchor": anchor}
        try:
            r = page.goto(url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(3500)
            for label in DECLINE:
                btn = page.get_by_role("button", name=label)
                if btn.count():
                    btn.first.click(timeout=3000); rec["consent"] = f"declined via '{label}'"; page.wait_for_timeout(800); break
            loc = page.get_by_text(anchor, exact=False)
            vis = [i for i in range(loc.count()) if loc.nth(i).is_visible()]
            loc = loc.nth(vis[0] if vis else 0)
            loc.scroll_into_view_if_needed(timeout=10000)
            y = page.evaluate("(el) => el.getBoundingClientRect().top + window.scrollY", loc.element_handle())
            page.evaluate(f"window.scrollTo(0, {max(0, y - above)})"); page.wait_for_timeout(1200)
            page.screenshot(path=str(OUT / f"{name}.png"))
            rec.update(status=r.status if r else None, title=page.title(), at=datetime.now(timezone.utc).isoformat())
        except Exception as e:
            rec["error"] = str(e)[:300]
        receipts.append(rec)
    b.close()
old = []
if (OUT / "receipts.json").exists():
    old = [x for x in json.loads((OUT / "receipts.json").read_text()) if x["name"] not in {r["name"] for r in receipts}]
(OUT / "receipts.json").write_text(json.dumps(old + receipts, indent=2) + "\n")
print(json.dumps(receipts, indent=2))
