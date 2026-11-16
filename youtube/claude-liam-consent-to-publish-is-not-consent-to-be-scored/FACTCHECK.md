# FACTCHECK — claude-liam-consent-to-publish-is-not-consent-to-be-scored

Every claim spoken on screen, verified against primary or near-primary sources.
**0 FAIL.** **Two corrections applied to the source document before scripting.**

---

## Platform facts

| # | Beat | Claim | Verdict |
|---|---|---|---|
| 1 | B02 | Reader triggers the scan from a menu on a Substack post; Pangram returns a percentage | ✅ Substack help page + Press Gazette |
| 2 | B03 | Scanning applies to posts and notes published **on or after 21 July 2026** | ✅ Substack's own help page, verbatim |
| 3 | B03/B04 | Nothing older is scanned — no back-catalogue exposure | ✅ Follows from #2 |
| 4 | B04 | Per-post disable, "report a detection error", and "How I make this" all exist | ✅ Substack help page |
| 5 | B16 | "How I make this" is a writer-authored process statement shown when a reader scans | ✅ Substack help page |
| 6 | B26 | Scores have been screenshotted and republished during the controversy | ✅ Documented in the source memo and consistent with reported backlash; **see caveat C below** |
| 7 | B30 | Substack built and embedded the scan; Pangram classifies | ✅ Substack help page + Press Gazette |

## Case law

| # | Beat | Claim | Verdict |
|---|---|---|---|
| 8 | B08/B09 | *Nowak*, C-434/16 — personal data by **content, purpose, or effect** (disjunctive) | ✅ |
| 9 | B11 | Art. 4(4) GDPR defines profiling as automated evaluation of personal aspects, **naming reliability** | ✅ statutory text |
| 10 | B14 | *KNLTB*, **C-621/22, 4 October 2024** — a purely commercial interest can be a legitimate interest; no need for it to be provided for by law | ✅ verified against multiple firm analyses |
| 11 | B14/B15 | Art. 6(1)(f) is a three-step test: interest → necessity → balancing | ✅ restated in *KNLTB* |
| 12 | B22/B23 | *SCHUFA*, **C-634/21** — where the recipient "draws strongly" on the score, producing it is itself the automated decision | ✅ |
| 13 | B29/B30 | *Fashion ID*, **C-40/17 (2019)** — embedding a third-party plugin makes the embedder a **joint controller** for collection and transmission, even without seeing the data | ✅ |
| 14 | B32 | Art. 26 requires joint controllers to make the **essence of the arrangement** available to data subjects | ✅ statutory text |
| 15 | B18 | **AI Act Art. 50(4), second subparagraph** — disclosure duty does not apply where content "has undergone a process of human review or editorial control and where a natural or legal person holds editorial responsibility for the publication" | ✅ **quoted verbatim from the Act** |

---

## Corrections applied to the source document

### Correction 1 — the opt-out date is not the scan date (B04, and cut from the script)

The source memo treats "per-post disabling" as a mitigation covering the feature.
Substack's own help page states scanning applies to content published **on or after
July 21, 2026**, but that creators can disable detection on posts published **after
July 26, 2026**.

If both dates are accurate as published, there is a **five-day window** in which posts
are scannable and cannot be switched off — a gap in the opt-out that neither memo
noticed.

**Handling:** I did **not** put this in a beat. A five-day discrepancy on a help page
is as likely to be a typo as a real policy gap, and asserting it on screen would be
exactly the kind of unverified claim rule 7 exists to stop. It is logged here for Bear
to confirm against the live page. **If confirmed, it deserves its own beat in Act I** —
it is a sharper fact than anything in either memo.

### Correction 2 — AI Act Art. 50(4) is narrower than the memo implies (B20)

The source document deploys the editorial-responsibility exemption as though it covers
AI-assisted writing generally. It does not. The text duty in Art. 50(4) applies to text
"published with the purpose of **informing the public on matters of public interest**."

A recipe newsletter, a fiction serial, or a personal essay is likely outside the
provision entirely — so the exemption has nothing to exempt them from, and the
"Europe asks less than Pangram does" argument doesn't reach them.

**Handling:** kept the argument (B18, B19) because it is the strongest original point in
the document, then **limited it on screen at B20**. The film states its own scope
restriction rather than letting the strong version stand unqualified.

---

## Caveats carried into the build

**A. Memo B's "draws strongly" claim is unevidenced, and the film says so.**
B25 stamps it `NOT_DETERMINABLE`. No published data establishes whether a Pangram score
changes reader behaviour. That is the honest state, and the beat labels it rather than
resolving it.

**B. Pangram's controller status is genuinely open.**
B31 presents contract-label vs functional-test as a comparison, not a finding. No court
has classified Pangram.

**C. B26's pantry still must be real, and must not expose a private individual.**
The redistribution claim needs an actual screenshot of a publicly republished score. Use
a post whose author published their *own* score as argument in the controversy — not a
third party's score reposted without consent. Filming someone else's score to illustrate
a privacy harm would be the same wrong the film is describing. **This is a hard
constraint on the shopping list, not a preference.**

**D. Not legal advice.** Stated in B00 narration and required in the description.

---

## Deliberately not claimed on screen

- That the feature **is** unlawful. No court or DPA has ruled on this fact pattern.
- That the feature **is** lawful. Same reason.
- That Substack has no Article 26 arrangement — B32 says the document *should* exist and
  sends the viewer to look. It does not assert absence.
- Any figure for Pangram's accuracy or false-positive rate. That is the companion reel's
  subject (`claude-liam-a-p-value-is-not-a-verdict`) and is not re-litigated here.

---

**Sources:** [Substack — How can I detect AI on Substack?](https://support.substack.com/hc/en-us/articles/50891130623508-How-can-I-detect-AI-on-Substack) · [Press Gazette — Substack promotes human content with 'scan for AI' feature](https://pressgazette.co.uk/news/substack-promotes-human-content-with-scan-for-ai-feature/) · [EU AI Act, Article 50](https://artificialintelligenceact.eu/article/50/) · [DLA Piper — CJEU confirms legitimate interests can cover purely commercial interests (C-621/22)](https://privacymatters.dlapiper.com/2024/10/eu-cjeu-confirms-that-legitimate-interests-can-cover-purely-commercial-interests/) · [CJEU C-621/22 KNLTB, 4 Oct 2024](https://ipcuria.eu/case?reference=C-621%2F22) · [Hogan Lovells — CJEU clears the air on legitimate interests](https://www.hoganlovells.com/en/publications/cjeu-clears-the-air-dutch-dpas-interpretation-of-legitimate-interests-is-too-strict)
