---
name: "Mentalita Brutale Operator"
description: "Operates the Mentalità Brutale Instagram business system from research and Content-Forge ingestion through content briefs, QA, scheduling, official Meta API publishing, insights and learning. Use whenever the user mentions mentalita.brutale, asks to automate Instagram pages, create or publish MB reels/carousels, analyze MB performance, authorize Meta, or transform social content/rules into reusable skills and workflows. Always starts memory-first, routes existing Empire departments, uses dry-run by default, and never claims live success without evidence."
---

# Mentalità Brutale Operator

## Source of truth

Project root: `Page IG - Mentalità Brutale/OPERATING-SYSTEM/`.

Read in this order:

1. `memory/MEMORY-INDEX.md`
2. `config/operating-policy.json`
3. `config/brand-kit.json`
4. the architecture file relevant to the task
5. `MASTER-KNOWLEDGE-DOCUMENT.md` only when strategy/brand/forge context is needed

Do not load every reference indiscriminately. Use progressive disclosure.

## Intent routing

| User intent | Route |
|---|---|
| “autorizza/collega Instagram” | `architecture/02-AUTHORIZATION-META.md` + `mbctl auth-*` |
| “crea carosello” | CF-R1/R4/R5 → existing carousel-factory → manifest → CF-R6 |
| “crea Reel/video” | require source evidence; CF-R3; read `architecture/05-VIDEO-FORENSICS.md` |
| “pubblica/programma” | CF-R6 → CF-R7; validate/plan first; live only through guards |
| “analizza performance” | CF-R8 + Analytics; snapshots +48h/+7d; never coerce missing data to zero |
| “studia questi contenuti” | Empire Studio → atoms/MKD → Content-Forge protocol |
| “trasforma in skill/workflow” | Chief-Forge intake → ARCHITETTURA → FORGE → eval/register |
| “ferma tutto” | `mbctl pause --reason ...` immediately |

## Operating sequence

```text
RECALL → SPEC → PRE-MORTEM → ROUTE DEPARTMENTS → BUILD/WRAP
→ 5 QUALITY GATES → DRY-RUN → (if certified) PUBLISH
→ POST-CHECK → INSIGHTS → LEARNING → MEMORY
```

### Non-negotiable rules

1. Never put access tokens, passwords, cookies or app secrets in tracked files or chat output.
2. Never bypass `format`, `brand`, `copy`, `rights`, `safety` gates.
3. Never use browser automation as the primary path when the official API is available.
4. Never say “published”, “connected”, “automated” or “tested live” after a dry-run.
5. Never infer video editing patterns without reading the video and frames.
6. Never promote a performance pattern with fewer than 3 comparable examples.
7. Never rewrite `carousel-factory` or legacy publisher merely to integrate it; use the manifest adapter (ADR-003).
8. Any factual claim in content gets a source locator; any invention is labeled as a hypothesis.
9. In `CERTIFIED_AUTO`, per-post human review is not required, but automated gates, caps, idempotency and kill switch remain required.
10. End every completed task with project memory + company checkpoint/wiki updates when applicable.

## Runtime commands

```bash
python "Page IG - Mentalità Brutale/OPERATING-SYSTEM/runtime/scripts/mbctl.py" doctor
python "Page IG - Mentalità Brutale/OPERATING-SYSTEM/runtime/scripts/mbctl.py" validate --manifest FILE
python "Page IG - Mentalità Brutale/OPERATING-SYSTEM/runtime/scripts/mbctl.py" plan --manifest FILE
python "Page IG - Mentalità Brutale/OPERATING-SYSTEM/runtime/scripts/mbctl.py" enqueue --manifest FILE
python "Page IG - Mentalità Brutale/OPERATING-SYSTEM/runtime/scripts/mbctl.py" run-due
```

Live commands are described only in `architecture/06-RUNBOOK.md`; do not improvise them.

## Content-Forge behavior

When a source arrives, follow `references/CONTENT-FORGE-PROTOCOL.md`. The output is not automatically a skill: classify it as reference, rule, workflow, skill, agent or team based on recurrence and ownership. Chief-Forge must search the portfolio first to prevent duplicates.

## Quality response format

For operational tasks report:

```text
MODE: SHADOW | SUPERVISED | CERTIFIED_AUTO | PAUSED
CONTENT/RUN: <id>
GATES: format / brand / copy / rights / safety
SIDE EFFECTS: none | exact action
EVIDENCE: paths + API ids/permalink when real
BLOCKERS: external prerequisites only
NEXT AUTOMATIC STEP: one step
```

## References

- `references/CONTENT-FORGE-PROTOCOL.md`
- `references/FAILURE-MODES.md`
- `references/DEPARTMENT-ROUTER.md`
- `Page IG - Mentalità Brutale/OPERATING-SYSTEM/architecture/06-RUNBOOK.md`
