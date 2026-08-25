# ADR-001 — Bootstrap the Builder Swarm before the runtime

- **Status:** Accepted for W0
- **Date:** 2026-08-23

## Context

The orchestration layer requires code, contracts, policy, tests and RuFlo integration. Activating an unrestricted swarm before governance exists would let the construction mechanism bypass the architecture it is supposed to build.

## Decision

Create a deterministic Builder Team registry and work-item planner first. The team is configuration-driven, least-privilege and non-executing at W0. It creates governed plans and checkpoints but cannot call production tools or RuFlo.

Eight specialized roles are registered: Build Lead, Architect, RuFlo Scout, Implementer, Tester, Security, Gatekeeper and Release.

## Consequences

- Construction begins with explicit ownership and separation of duties.
- RuFlo remains disabled until certification.
- Human approval is required before activation.
- The initial team manager is intentionally simple and standard-library only.
- Agent execution adapters will be added after deterministic contracts and security gates exist.
