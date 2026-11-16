# PROMPTS — claude-liam-do-chatbots-pass

Beat-prefixed prompts for the 7 pantry stills. All drops go into pantry/ as <BID>.png;
pipeline renames to media/ on intake.

## A2 — Alan Turing portrait (Tier 3, archival)
Rights check required. Well-known option: the 1951 Elliot & Fry photograph
(National Portrait Gallery reference). Confirm public domain / fair educational use
before sourcing. May reuse the still already sourced for claude-liam-chinese-room A2.
NO AI generation for Tier 3 — must be documented archival source.

## A7 — 1960s mainframe / teletype terminal (Tier 1, generic)
"Black and white documentary-style photograph of a 1960s-era mainframe computer or
teletype terminal, side profile or three-quarter view, minimal background, no person
required, slightly worn paper-tape reader visible, high contrast editorial feel."
AI-generated is fine; add disclosure sidecar (A7.source.txt: "AI-generated image").

## A9 — Joseph Weizenbaum portrait (Tier 3, archival)
Rights check required. Academic or book-jacket portrait, preferably ~1970s–1980s era.
MIT affiliation context preferred. NO AI generation for Tier 3.
Note: imagery is somewhat available but quality varies — verify resolution before use.

## A10 — Kenneth Colby portrait (Tier 3, archival)
Rights check required. Academic portrait, ~1970s era, Stanford affiliation context.
Imagery is scarce — AI fallback is permitted ONLY if no creditable archival source
is available; if AI-generated, label explicitly in the disclosure sidecar (A10.source.txt).

## A16 — Goostman-era chat window / boyish avatar (Tier 1, generic)
"Period-appropriate chat interface circa 2010–2014, retro UI aesthetic, small avatar
icon suggesting a young person (no identifiable face), simple text bubbles on screen.
Must NOT be a screenshot of or exact replica of any specific proprietary product UI."
AI-generated fine; add disclosure sidecar. Avoid any current-era UI styling.

## A21 — Modern fluent chat window (Tier 1, generic)
"Clean modern chat interface, light neutral color scheme, natural flowing text exchange
visible on screen, no specific product branding visible, warm editorial lighting,
slightly shallow depth of field."
AI-generated fine; add disclosure sidecar. No logos, no product-specific chrome.

## A29 — Person absorbed at a glowing screen (Tier 1, generic)
"Close-up editorial photograph of a person at a glowing laptop or desktop screen,
absorbed in reading, warm indirect ambient light, slightly blurred background,
no identifiable face required, hands resting near keyboard."
AI-generated fine; add disclosure sidecar. Callback texture to A7 (cool/warm shift).

---

## Rights and disclosure rules
- Tier 3 (A2, A9, A10): archival portraits require rights check by Bear before use.
  If AI fallback is used for A10, A10.source.txt must read: "AI-generated portrait
  of Kenneth Colby; no authentic archival source found."
- Tier 1 (A7, A16, A21, A29): AI-gen permitted; disclosure sidecar required
  (<BID>.source.txt: "AI-generated image; no specific person depicted").
- Focus points for Ken Burns: set shot.focus in beat_sheet.json after dropping stills.
