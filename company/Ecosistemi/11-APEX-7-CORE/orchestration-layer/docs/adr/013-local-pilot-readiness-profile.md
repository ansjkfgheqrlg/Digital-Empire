# ADR-013 — Separate local secure pilot readiness from production readiness

- **Status:** Accepted for W11 remediation
- **Date:** 2026-08-23

## Context

The selected deployment target is local-only, with one temporary owner and local tests. Those choices cannot prove production KMS, managed failover/PITR, cloud residency, external penetration or 24x7 on-call.

Anonymous identity was requested but rejected because a token-management control plane must authenticate the principal requesting or approving tokens.

## Decision

Create a `LOCAL_SECURE_PILOT` profile using Ed25519 challenge-response operator identity. It is loopback-only, R0/R1-only, LocalRuntime-only, without external side effects. R2, R3 and RuFlo generative execution remain disabled.

Run two independent reviews:

- local pilot: `GO_LOCAL_PILOT` when local evidence passes;
- production: remains `NO_GO` until external and human production controls exist.

## Consequences

- All solvable local-pilot blockers are closed.
- No false production claim is made.
- Single-owner operation has no separation of duties and therefore cannot enable R2/R3.
- Production blockers require real people and infrastructure, not more code generation.
