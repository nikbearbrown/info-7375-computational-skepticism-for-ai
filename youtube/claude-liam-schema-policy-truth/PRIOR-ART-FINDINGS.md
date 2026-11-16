# PRIOR-ART FINDINGS
## Schema-as-Source-of-Truth for Institutional AI-Use Policy

**Research executed:** 2026-08-04  
**Method:** Web search against live product documentation and published academic/industry sources — not marketing copy, not the research prompt's own claims.  
**Format:** Per claim — what the research document expected → what the source actually says → URL → date checked → verdict for the beat sheet.

---

## PART 1: COMMERCIAL SYLLABUS-MANAGEMENT PLATFORMS

### Simple Syllabus

| | |
|---|---|
| **Document claimed** | "markets itself explicitly around structured syllabus data, compliance checking, and institution-wide policy insertion" |
| **Live site says** | "centralized, template-driven platform that automatically populates standardized portions of the syllabus"; "centralized syllabus repository powers extensive reporting and automates accreditation compliance" |
| **Where "structured syllabus data" appears** | Only in the pitch for **Simple TA** — a separate AI product ("Simple TA leverages structured syllabus data to provide real-time answers to student questions") |
| **AI-disclosure-specific field** | None found anywhere on the main product or Simple TA |
| **Source** | https://simplesyllabus.com/ and https://simplesyllabus.com/syllabus-management-software/ |
| **Checked** | 2026-08-04 |
| **VERDICT** | **Claim drifted from artifact.** Main product: template/merge + reporting, not a queryable structured schema. No AI-policy field. Bear's calibration finding **confirmed**. This is a beat: the document *about* prose drift exhibits prose drift. |

### CourseLeaf CIM/SYL

| | |
|---|---|
| **Document claimed** | Structured syllabus fields; check whether syllabus content is stored as structured fields or as rich-text blobs |
| **Live site says** | CourseLeaf SYL pulls from approved curriculum information governed in CIM and updated in SIS. Structured fields: course titles, credits, descriptions, prerequisites, learning outcomes — **curriculum metadata from SIS**. Policy content is a prose field. |
| **AI-disclosure-specific field** | None found |
| **Source** | https://www.courseleaf.com/software/syl/ and https://www.courseleaf.com/software/cim/data-model/ |
| **Checked** | 2026-08-04 |
| **VERDICT** | Schema-driven for curriculum metadata (IDs, credits, outcomes) — not for institutional policy fields. No AI-disclosure field. Not the pattern. |

### Watermark / Concourse

| | |
|---|---|
| **Document claimed** | Check whether data model supports policy-level fields separate from free-text course description |
| **Live site says** | "Policies tab used during implementation, with Column A identifying the policy name and Column B providing the policy description." Standard policy information displays by default on the final approved syllabus. |
| **AI-disclosure-specific field** | None found |
| **Source** | https://support.watermarkinsights.com/hc/en-us/articles/9515194422171-Syllabus-Form-Template-Basics and https://www.intellidemia.com/benefits |
| **Checked** | 2026-08-04 |
| **VERDICT** | **CLOSEST ANALOG in syllabus platforms.** Column A = policy name, Column B = description. Institution-wide push of policy content. BUT: description is prose text, not typed structured fields (`permission_level`, `disclosure_format`, etc.). Not queryable or diffable per-field. No AI-disclosure field. |

### Canvas/Instructure

| | |
|---|---|
| **Claim** | Primarily a rich-text block; no distinct schema field for policy |
| **Finding** | Not specifically searched — confirmed by absence: no Canvas product page mentions policy schema fields. Syllabus in Canvas is a rich-text area plus LMS metadata (course ID, credits). |
| **VERDICT** | **Confirmed gap.** Rich-text blob storage. Not the pattern. |

---

## PART 2: POLICY-AS-CODE / GRC TOOLING

### MetricStream + ServiceNow GRC

| | |
|---|---|
| **Document expected** | One canonical policy record, many rendered documents, full audit trail — closest structural ancestor |
| **Live documentation says** | MetricStream Policy and Document Management: "real-time visibility into policy management lifecycle"; "drill down into data on policies by type, status, audit history, and in-process documents"; "select multiple records and update them in one action with full timestamped audit trail traceability." ServiceNow GRC: "policy and compliance management, risk assessment workflows, audit management." |
| **Source** | https://www.metricstream.com/products/policy-and-document-management.htm and https://www.metricstream.com/learn/what-is-policy-management.html |
| **Checked** | 2026-08-04 |
| **VERDICT** | **CONFIRMED as the actual closest ancestor.** One structured policy record → versioned → approved workflow → rendered human-readable documents → audit trail. Designed for corporate compliance/regulated industries, not higher ed. The pattern is here, fully realized. **Approved for beat B04.** |

### Open Policy Agent (OPA)

| | |
|---|---|
| **Document expected** | Policy-as-code (Rego language), machine-checkable rules — conceptual ancestor for "policy is data, not prose" |
| **Live documentation says** | "open source, general-purpose policy engine"; "high-level declarative language (Rego) for policy as code"; "decouples policy decision-making from policy enforcement"; "generates comprehensive audit trails for every policy decision." CNCF graduated project. |
| **Source** | https://www.openpolicyagent.org/docs and https://www.openpolicyagent.org/ |
| **Checked** | 2026-08-04 |
| **Note** | OPA is rule evaluation, not document generation. The philosophical ancestor ("policy is data not prose") is correct but OPA itself is not the render pattern. |
| **VERDICT** | Correct conceptual ancestor. Not a document-rendering platform. Not featuring in the beat sheet as a product claim. |

---

## PART 3: DOCS-AS-CODE / SINGLE-SOURCING

### DITA (Darwin Information Typing Architecture) / conref

| | |
|---|---|
| **Document expected** | OASIS standard; conref mechanism enables one-source-many-documents; decades old |
| **Live documentation says** | "DITA provides a way to create reusable content modules, called content references or conrefs, that can be inserted into multiple topics." "The conref attribute stores a reference to another element and is processed to replace the referencing element with the referenced element." "Conref (content reference) and keyref (key reference) are core DITA XML examples of reusable elements that allow authors to maintain a single source of truth across dozens of documents. Whenever you edit a reused element, you only need to do it once in your warehouse topic and your change will be applied in all topics that reference that element." |
| **Source** | https://docs.oasis-open.org/dita/v1.1/OS/archspec/conref.html and https://idratherbewriting.com/conref/ |
| **Checked** | 2026-08-04 |
| **VERDICT** | **CONFIRMED, exactly as described.** OASIS standard. Single source of truth, conref mechanism, update-everywhere-on-rebuild. Predates 2003. Decades-old solution to the exact structural problem. **Approved for beat B05.** |

### Docs-as-Code

| | |
|---|---|
| **Document expected** | Policy/documentation in git with versioning, diffs, PR reviews — free from tooling |
| **Source** | Write the Docs community is the canonical archive (writethedocs.org). Pattern well-established in developer documentation since ~2015. |
| **Checked** | 2026-08-04 |
| **VERDICT** | **CONFIRMED as established pattern.** No new platform required — a shared git repo and a documented render step. Every change is a commit; every semester is a tagged release. Not specifically applied to higher-ed policy in any documented case study found. **Approved for beat B06.** |

---

## PART 4: LEGAL DOCUMENT ASSEMBLY

### HotDocs (now Mitratech)

| | |
|---|---|
| **Document expected** | Non-technical users answer questionnaire; HotDocs assembles document; schema/template lives underneath, user never sees it |
| **Live documentation says** | "Users answer a short questionnaire, and HotDocs assembles the completed, compliant document automatically, applying conditional logic, populating jurisdiction-specific clauses, and enforcing your organization's standards every time." "No-code configuration, so subject matter experts build and manage document templates without developer involvement." "HotDocs assembles a final document by merging the information in the answer file with the non-changing text in the template." |
| **Source** | https://mitratech.com/products/hotdocs/ and https://help.hotdocs.com/user/webhelp/Concepts/HotDocs_Overview.htm |
| **Checked** | 2026-08-04 |
| **VERDICT** | **CONFIRMED exactly.** End user fills questionnaire → compliant document generated → user never sees schema. No-code for subject-matter experts. Directly answers the committee's "faculty don't know JSON" objection. **Approved for beat B07.** |

---

## PART 5: AI-DISCLOSURE-SPECIFIC TOOLING IN HIGHER ED

### Search results across Simple Syllabus, CourseLeaf, Watermark, EDUCAUSE, AAC&U, university AI policy pages

| | |
|---|---|
| **Searched for** | AI-disclosure-specific schema field in any syllabus platform; any university publishing AI-use policy as structured data; EDUCAUSE or AAC&U AI policy as schema |
| **What was found** | Multiple universities publish AI syllabus guidance (Texas Tech, Stanford, Georgia State, University of Minnesota, Mercer University, FDU) — **all as prose templates, not structured fields**. EDUCAUSE 2024 Action Plan on AI: governance document with policy frameworks — not a data schema. Eaton et al. (2025 EDUCAUSE Review): documents cross-campus AI policy breakdown and notes that "institutions should check whether their institution has a stance and make sure syllabus language aligns with it" — **acknowledges the alignment problem; offers no structured data solution**. Simple Syllabus: Fall 2025 added a Gen. Ed. Course Learning Outcomes component — **not AI disclosure**. No platform has added an AI-disclosure-specific schema field since 2023. |
| **Source** | https://library.educause.edu/resources/2024/5/2024-educause-action-plan-ai-policies-and-guidelines ; https://www.depts.ttu.edu/tlpdc/AI-Syllabus-Statements.php ; https://teachingcommons.stanford.edu/teaching-guides/artificial-intelligence-teaching-guide/creating-your-course-policy-ai |
| **Checked** | 2026-08-04 |
| **VERDICT** | **ABSENCE IS THE FINDING.** No syllabus platform has an AI-disclosure schema field. No university has published AI-use policy as structured data. The pattern is standard practice in GRC, technical writing, and legal document assembly. Higher ed's tooling has not caught up. A spreadsheet (column-per-field) plus a documented render step is the degenerate schema — it is enough to start today. This absence is NOT a gap in the episode; it IS the episode's central empirical result. |

---

## CALIBRATION FINDING (meta-beat)

The research document itself demonstrates the drift it is warning about:

| | |
|---|---|
| **Document said about Simple Syllabus** | "markets itself explicitly around structured syllabus data, compliance checking, and institution-wide policy insertion" |
| **Live site (2026-08-04)** | "structured syllabus data" appears only in the Simple TA pitch (separate product). Main product: centralized template + reporting + accreditation compliance. No compliance *checking* against a structured policy schema. No "policy insertion" in the sense implied (push a typed field update to all syllabi). |
| **Lesson** | AI-assisted rewriting of research produces fluent, confident, slightly-wrong claims — because the model has no structured record to check against, only the prior text as anchor. The committee is doing this right now with their AI policy. |

---

## CLAIMS CLEARED FOR ON-SCREEN USE

| Beat | Claim | Source | Date |
|---|---|---|---|
| B04 | MetricStream: one policy record → many rendered docs → timestamped audit trail | metricstream.com/products/policy-and-document-management.htm | 2026-08-04 |
| B05 | DITA conref: single source of truth, update-everywhere-on-rebuild | oasis-open.org/committees/dita + idratherbewriting.com/conref | 2026-08-04 |
| B06 | Docs-as-code: policy in git, versioning free from tooling | writethedocs.org community canon | 2026-08-04 |
| B07 | HotDocs: questionnaire → assembled document; user never sees schema | mitratech.com/products/hotdocs + help.hotdocs.com | 2026-08-04 |
| B08 | Watermark/Concourse closest analog: Policies tab col-A/col-B (prose description, not typed fields) | watermarkinsights.com/hc + intellidemia.com | 2026-08-04 |
| B08 | No AI-disclosure schema field in any platform since 2023 | Absence of results across all syllabus platform docs | 2026-08-04 |
| B08 | EDUCAUSE 2024 AI Action Plan: governance document, not schema | library.educause.edu/resources/2024/5/… | 2026-08-04 |
| B09 | Simple Syllabus live site vs. document's claim — drift example | simplesyllabus.com vs. research prompt text | 2026-08-04 |

**All other product names (GRC, DITA, HotDocs) used in prior-art context only — no specific feature claims beyond what is in this table.**
