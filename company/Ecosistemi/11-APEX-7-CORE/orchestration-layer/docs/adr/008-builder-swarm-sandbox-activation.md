# ADR-008 — Activate Builder Swarm in sandbox with deterministic execution

- **Status:** Accepted for W8
- **Date:** 2026-08-23

## Decision

The eight Builder Team roles are operationally activated in an isolated, immutable work-item sandbox. Stage execution uses deterministic local handlers because provider-backed RuFlo execution is not certified. RuFlo is used only to register all eight roles in a transient hierarchical coordination swarm; no provider credentials are forwarded and no generative task is executed.

Testing and Security run concurrently after implementation. Gatekeeper evaluates their evidence. Three failed gate attempts freeze the work item. Release produces a sandbox-only Evidence Pack and cannot deploy.

## Consequences

- The team workflow, prompts, role boundaries and evidence chain are executable now.
- Registration in RuFlo proves coordination metadata, not agent reasoning quality.
- Work items touching RuFlo generative behavior remain frozen.
- Promotion outside the sandbox requires W9 quality/cost evidence and provider-backed certification.
