# Master Knowledge Document — Master build Architecture

## Purpose
This document is the navigable synthesis layer for the knowledge pack. It does not replace the canonical source files; it explains how they compose into an operating architecture.

## Core operating model
A project begins with **WF-0**, the user/business workflow. Requirements derive from the workflow; architecture, UX, data, API contracts and tests must each link back to it. ORCH coordinates the smallest sufficient team, while SUP independently controls phase gates.

The architecture has three layers:

1. **Kernel:** `SKILL.md`, governance controls, ORCH and SUP.
2. **Specialists:** operating agents activated by task risk and scope.
3. **Tools and memory:** deterministic scripts, tests, canonical records and reference evidence.

## Memory-first delivery
The repository, not the chat, is the durable system of record. `memory/MEMORY-INDEX.md` points to checkpoints, ADRs, session handovers, plans, architecture records, risks and references. Each increment follows **Read → Plan → Write → Verify**. Decisions are not silently overwritten; superseding decisions receive a new ADR.

## Knowledge-pack map

| Area | Canonical location | Operational use |
|---|---|---|
| Principles | `01-principles/` | Constraints governing planning, depth, traceability and memory |
| Patterns | `02-patterns/` | Reusable conductor, pipeline, validation and iteration shapes |
| Anti-patterns | `03-anti-patterns/` | Failure prevention and review prompts |
| Processes | `04-processes/` | Repeatable lifecycle actions and gates |
| Decision trees | `05-decision-trees/` | When to add stages, agents, scripts or stricter schemas |
| Case studies | `06-case-studies/` | Evidence-based lessons from prior work |
| Templates | `07-templates/` | Consistent reusable artefact shapes |
| Glossary | `08-glossary/` | Shared terminology |
| FAQ | `09-faq/` | Fast answers to recurring design questions |
| External sources | `10-references/` and `governance/REFERENCE-LIBRARY.md` | Primary-source research discipline |

## Delivery lifecycle

```text
Workflow WF-0 → SRS → architecture/ADR → design → vertical implementation
→ independent review → tests → SUP gate → release/hand-off → observe/improve
```

No stage is a ceremonial document: every stage has inputs, owner, expected artefacts, failure paths, verification evidence and an exit gate.

## Self-improvement boundary
The improvement loop is **observe → plan → approved change → verify → close/escalate**. `scripts/validate_skill.py` produces deterministic findings; `scripts/self_improve.py` creates a bounded plan. The loop cannot autonomously alter credentials, scope, dependencies, production infrastructure or architecture without the responsible approval gate.

## Evidence standard
A claim is accepted only when linked to one or more of: a versioned artefact, a reproducible command result, an approved decision, an explicit user confirmation, or a precise external source recorded by REF. Tests, metrics, benchmarks and deployments are reported only when actually run.

## Reading order
1. `governance/README.md`
2. `workflows/README.md` and the applicable WF-0
3. `memory/MEMORY-INDEX.md`
4. the relevant principle/pattern/process/decision tree
5. agent specification and test/evidence records
