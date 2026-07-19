# Decision Log (ADR)

## ADR-001 — Use a repository-backed, layered memory model
- Data: 2026-07-19
- Stato: approvata
- Owner: ORCH / SUP
- Contesto: A multi-agent skill needs durable context across sessions without treating chat history as a source of truth.
- Decisione: Store canonical decisions, risks, evidence, references and handovers in `docs/memory/` with a defined precedence order.
- Alternative considerate: conversation-only memory; single project-state file.
- Conseguenze: more files to maintain; safer continuity and auditable decisions.
- Evidenze / riferimenti: SKILL.md §3
- Sostituisce: N/A
