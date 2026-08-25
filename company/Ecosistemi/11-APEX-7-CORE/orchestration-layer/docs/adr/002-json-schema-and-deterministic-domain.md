# ADR-002 — JSON Schema boundaries and deterministic domain

- **Status:** Accepted for W2
- **Date:** 2026-08-23

## Context

Python and the future TypeScript RuFlo bridge need one versioned boundary contract. Workflow state, budgets, DAG validation and side-effect semantics must remain independent of LLM and infrastructure behavior.

## Decision

1. JSON Schema Draft 2020-12 under `contracts/schemas/v1/` is the external contract source of truth.
2. Unknown boundary properties are rejected.
3. The Python domain uses standard deterministic value objects and a single Transition Registry.
4. No domain module imports FastAPI, SQLAlchemy, RuFlo, an LLM SDK or a storage adapter.
5. Budget uses reserve/commit/release semantics; actual usage cannot exceed reservation.
6. Plans are DAGs with bounded tasks, explicit completion criteria, capability lists and side-effect contracts.
7. Cancellation enters `CANCEL_REQUESTED`; it is never an immediate success claim.

## Consequences

- Python and TypeScript models can later be generated or checked from the same schemas.
- Runtime results cannot directly mutate domain state.
- Persistence and API adapters remain future work in W3/W4.
- Format checks requiring network resolution are avoided; all schema references use local registered resources.
