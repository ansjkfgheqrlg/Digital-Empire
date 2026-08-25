# ADR-005 — Deterministic LocalRuntime as mandatory baseline

- **Status:** Accepted for W5
- **Date:** 2026-08-23

## Decision

The first complete R1 vertical slice runs through a deterministic LocalRuntime with four roles: Planner, Implementer, Critic and Gate. LocalRuntime cannot spawn agents or call tools directly. All repository reads and artifact writes pass through the single-use capability Tool Gateway.

The `repository-adr` skill is the first ACTIVE skill. It reads only listed files and writes one immutable ADR. Quality order is schema, security, correctness, evidence and then conservative NERVE-SAVE compression of the final response.

## Consequences

- The system has a reproducible baseline before RuFlo is introduced.
- RuFlo must beat this baseline rather than replace an undefined reference.
- Local agents are deliberately narrow and are not general-purpose coding agents.
- The local slice currently uses in-memory grants; durable orchestration composition with PostgreSQL remains later work.
