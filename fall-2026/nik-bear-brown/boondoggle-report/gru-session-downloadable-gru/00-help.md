# Gru turn 00-help

## Professor Bear typed

```
/help
```

## Gru replied (verbatim, unedited)

I'm Gru.

I help you build Software Design Documents that actually work. Then I tell you exactly which parts Claude should build and which parts only you can build, in the order they need to happen, with explicit handoff conditions between every step.

That second part is called boondoggling. It is programming as conducting. You are Gru. Claude is the minions. The minions are excellent. They will execute exactly what they understood you to mean. Your job is to be precise about what you mean, in the right sequence, and to verify the output before the next step begins.

Before we write anything, I need to understand what you are proposing to build. Not the problem it solves, and not the ecosystem it lives in. The thing itself. That is where we start.

Every command runs in two modes:
- **Default (interactive):** I ask before I act, push back on weak input, and hold the line on phase gates.
- **/silent:** append it to any command for clean output immediately.

**PROBLEM & VISION**
```
/v0   or  /brief         — Problem formulation gate (start here)
                           One sentence: what are you proposing to build?
                           /v1 does not begin until this exists.
/v1   or  /intake        — Problem intake
/v2   or  /principles    — Architecture principles
/v3   or  /flows         — Core user flows + system interaction map
/v4   or  /needs         — User and business needs (UX Goals)
```

**SYSTEMS & ARCHITECTURE**
```
/s1   or  /components    — Core component documentation
/s2   or  /integrations  — External integrations and dependencies
/s3   or  /data          — Data architecture and state management
/s4   or  /edge          — Edge cases and failure states
```

**DOMAIN & API**
```
/d1   or  /domain        — Domain model and entity definitions
/d2   or  /api           — API contract documentation
/d3   or  /dataflow      — Data flow and sequence diagrams
```

**SCOPE & PRODUCTION**
```
/p1   or  /features      — Component list with priority tagging
/p2   or  /outofscope    — Out-of-scope section
/p3   or  /infra         — Infrastructure and deployment requirements
/p4   or  /risks         — Technical and design risk register
/p5   or  /openlog       — Open Questions Log
```

**BUILD & FINALIZATION**
```
/g1   or  /fulldoc       — Compile full SDD draft
/g2   or  /critique      — SDD audit against the 7 Failure Modes
/g3   or  /onepager      — One-page executive summary
/g4   or  /newengineer   — New Engineer Onboarding Test
/tasks                   — Implementation task document
```

**BOONDOGGLING**
```
/claude  or  /boondoggle — Generate the Boondoggle Score: Claude's
                           prompts and human tasks, sequenced by
                           dependency, with explicit handoff conditions.
                           Available at any stage, not only after /g1.
```

**RECIPE & PIPELINE**
```
/recipe  or  /build       — Build a working thing: Claude writes the script
                            and iterates with you, inserting typed [TODO]
                            items (DATA SOURCE / DEFINE / DEV / APPROVE /
                            REPORT FIELD), until the recipe reaches RUNNABLE.
                            Ends at "I think it works." Does not go to
                            /claude directly. Hand off to /snickerdoodle.
/snickerdoodle or /verify — Test & verification phase gate. Proposes AI tests
                            (machine-verifiable) and human tests (judgment),
                            runs them, and logs each result to the
                            verification chain as a gate decision. RUNNABLE
                            in, VERIFIED out. Only a PASS opens /claude.
/audit                    — Audit EXISTING recipes: generate a Claude Code
                            agent prompt that rewrites recipes/ to the
                            standard format, inserts typed [TODO]s, and
                            iterates until RUNNABLE. For existing or
                            n8n-sourced recipes, not new builds.
                            RUNNABLE output → /snickerdoodle → /claude.
```

**REFINEMENT TOOLS**
```
/problemstatement        — Write or stress-test a problem statement
/constraints             — Define and pressure-test system constraints
/comparable              — Comparable systems analysis
/flowtest                — Stress-test a core user flow
/scopecheck              — MoSCoW priority audit
/failmodes               — Run the 7 Failure Mode diagnostic
/security                — Security posture review
/changelog               — Generate a version control changelog entry
```

**UTILITY**
```
/silent  — Append to any command for clean output, no pushback, no gates.
/show    — Live example in both silent and interactive modes.
/list    — Full command reference table.
```

Type any command to begin, or paste your problem description and tell me where it breaks down.
