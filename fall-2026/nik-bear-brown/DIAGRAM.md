# Project diagram — Lectern job-board watcher, three-class sync

## Executive summary

The Lectern tool (`lectern/collect.py`) is a job-board watcher for teaching-related and advocacy roles in AI and education. It reads 18 boards across three applicant-tracking systems (Greenhouse, Ashby, SmartRecruiters), runs a seven-step pipeline — fetch → write raw → normalise → deduplicate → validate → keyword-filter → write outputs — and produces JSON and CSV files a human can act on. Five additional Tier 1 targets (Adobe, Salesforce, GitHub, Google, Shopify) are unreachable because their ATS is unknown; the documentation says so rather than omitting them.

The shared code and configuration are canonical in this folder (Computational Skepticism) and propagated to two other class repos — Branding and AI, and Prompt Engineering — by `lectern/sync.sh`. Sync never commits; each repo is committed and pushed by hand. Every git push to this folder requires Professor Bear's explicit approval, and the FRICTIONAL.md log must be updated in the same commit.

There are five human approval gates: (A) any change to the shared configuration, (B) reviewing outputs before propagating, (C) approving the sync after seeing the drift check, (D) approving each git push, and (E) writing and signing the FRICTIONAL.md entry. Claude Code runs every command; the human decides when and whether.

---

```mermaid
flowchart TD
    BEAR(["👤 Professor Bear\nhuman"])
    CC(["🤖 Claude Code"])

    subgraph CFG["Shared configuration — edited here, never downstream"]
        SRC[/"sources.json\n18 boards · 3 ATSs"/]
        KW[/"keywords.json\nrole · topic · flex terms  v0.2.1"/]
        ATSF[/"ATS.md\nverified slugs · 9 unknowns"/]
    end

    subgraph BOARDS["Job boards — three ATS providers"]
        subgraph GH["Greenhouse · 11 boards · 1 API call each"]
            GHB["Anthropic · Figma · HubSpot · Vercel\nWebflow · Miro · Airtable · Stripe\nGitLab · Twilio · Netlify"]
        end
        subgraph AH["Ashby · 6 boards · 1 API call each"]
            AHB["OpenAI · Notion · Replit\nWriter · Jasper AI · Supabase"]
        end
        subgraph SM["SmartRecruiters · 1 board"]
            SMB["Canva\n1 listing call + 1 per posting  (~249 calls total)"]
        end
        subgraph UN["Unreachable — ATS unknown"]
            UNB[/"Adobe · Salesforce · GitHub\nGoogle · Shopify\n4 of 5 are Tier 1 targets"/]
        end
    end

    subgraph PIPE["lectern/collect.py — seven pipeline steps"]
        direction TB
        ST1["① fetch_board\nGET from three allowed hosts only\nHTTPS · Greenhouse / Ashby / SmartRecruiters"]
        ST2["② write raw/\nAPI response verbatim before anything parses it\nP2 — raw first, always"]
        ST3["③ normalise\nuniform internal schema from three different formats"]
        ST4["④ deduplicate\nby source + source_id"]
        ST5["⑤ validate\ntitle present · url present · date parseable"]
        ST6["⑥ judge — keyword filter\nrole word in title\nOR ≥ 3 topic words in body\nflex_text annotates only, never keeps"]
        ST7["⑦ write outputs\nJSON + CSV  (atomic replace via .tmp)"]
        ST1 --> ST2 --> ST3 --> ST4 --> ST5 --> ST6 --> ST7
    end

    subgraph OUT["Outputs written to canonical master"]
        OA[/"all-jobs-{date}.json  /  .csv\nevery posting fetched · ad text omitted for size"/]
        OB[/"jobs-of-interest-{date}.json  /  .csv\nkept postings · matched words · full ad text · original record"/]
        OC[/"quality-report-{date}.md\ncounts · rejects by reason · source status"/]
        OD[/"raw/{provider}-{slug}-{date}.json\nAPI responses exactly as sent — the re-derivability record"/]
    end

    subgraph SYNC["lectern/sync.sh — never deletes, never commits"]
        SHC["--check\nreport drift · change nothing · safe to run first"]
        SHA["no flag\ncopy shared files out to the other two repos"]
        SHC --> SHA
    end

    subgraph CLASSES["Three class repositories"]
        C1["📘 Computational Skepticism\ncanonical master — this folder\nlectern/ · facts/ · figma/\ngreenhouse-watch-demo/\nassignment-3/ · boondoggle-report/"]
        C2["📗 Branding and AI\nlectern files land in assignment-3/\nfacts/ · figma/ · greenhouse-watch-demo/"]
        C3["📙 Prompt Engineering\nlectern files land in lectern/\nfacts/ · figma/ · greenhouse-watch-demo/"]
    end

    GA{"🔑 GATE A\nHuman approves\nconfiguration change\nedited here only\nnever downstream"}
    GB{"🔑 GATE B\nHuman reviews\nquality-report and\njobs-of-interest\nbefore propagating"}
    GC{"🔑 GATE C\nHuman approves\nsync propagation\nafter seeing --check diff"}
    GD{"🔑 GATE D\nHuman approves\neach git push\nword required every time\nno standing approval"}
    GE{"🔑 GATE E\nHuman writes and signs\nFRICTIONAL.md entry\nmust be in the same commit"}

    PUSH[/"git push\nstages fall-2026/nik-bear-brown/ only\neach repo committed by hand"/]

    %% Config flow
    BEAR -- "directs config changes" --> GA
    GA -- "approved" --> CFG
    CC -- "reads" --> CFG
    CC -- "runs" --> PIPE

    %% Board → pipeline
    GHB & AHB & SMB --> ST1
    UNB -. "not fetched\nTODO: DATA SOURCE" .-> ST1

    %% Pipeline → outputs
    ST2 --> OD
    ST7 --> OA & OB & OC
    OA & OB & OC --> C1

    %% Review → sync
    C1 --> GB
    GB -- "approved" --> CC
    CC -- "runs --check first" --> SHC
    SHC -- "drift shown to human" --> GC
    GC -- "approved" --> SHA
    SHA --> C2 & C3

    %% Push gates
    C1 & C2 & C3 --> GD
    GD -- "word given" --> GE
    GE -- "FRICTIONAL.md entry written\nin same commit" --> PUSH
    PUSH --> BEAR
```

## FigJam

[Lectern — agentic diagram (fall 2026)](https://www.figma.com/board/xFbHv4o4SrmA0BekS5Sw1Q)
