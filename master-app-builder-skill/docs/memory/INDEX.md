# Memory Index — Master App Builder Skill

## Canonical documents

| Area | Source of truth | Owner | Status |
|---|---|---|---|
| Scope | `../SRS.md` | DISC / ORCH | Active |
| Skill behaviour | `../../SKILL.md` | ORCH / SUP | Active |
| Project state | `../project_state.md` | ORCH | Active |
| Decisions | `decisions.md` | ORCH / ARC / SUP | Active |
| Risks | `risks.md` | ORCH / SUP | Active |
| References | `references.md` | REF | Active |
| Handover | `session_handover.md` | ORCH | Active |

## Read order at session start
1. `session_handover.md`
2. `../project_state.md`
3. Open items in `decisions.md` and `risks.md`
4. The relevant canonical document for the planned task

## Operating libraries

| Library | Purpose | Read when |
|---|---|---|
| `../rules/` | Canonical workflow, UI, link/integration and delivery principles | Always; read the task-relevant rulebook before planning |
| `../workflows/` | Workflow artefacts; WF-0 is mandatory | Before SRS, design, architecture or implementation |
| `../references/` | Curated primary sources and research protocol | Before external/current/regulatory decisions |
| `../agents/REGISTRY.md` | Agent activation and independence rules | At orchestration and phase gates |
| `../audits/` | Skill/project gap analyses | At major milestone or process changes |
