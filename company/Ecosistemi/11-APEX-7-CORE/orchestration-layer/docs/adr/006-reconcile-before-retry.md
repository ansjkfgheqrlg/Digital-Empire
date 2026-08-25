# ADR-006 — Reconcile unknown outcomes before retry

- **Status:** Accepted for W6
- **Date:** 2026-08-23

## Decision

A transient error is retryable only when the external outcome is known, the side-effect contract allows retry, attempts and budget remain, the deadline permits delay and the circuit is not open. Unknown outcomes always enter `RECONCILING` before retry or compensation.

Cancellation is a workflow: request, revoke task grants, cooperative stop, reconcile residual effects, then cancel or compensate. An artifact is automatically deleted only when path and SHA-256 match and it is not referenced.

The PostgreSQL claim query reclaims expired `LEASED` or `RUNNING` tasks only when attempts remain. Each claim increments the attempt counter. A stale execution token remains unable to commit.

## Consequences

- Duplicate side effects are less likely than with blind retries.
- Some ambiguous failures intentionally end in `MANUAL_INTERVENTION`.
- Compensation proves semantic cleanup; it does not erase audit history.
- Recovery paths require explicit catalog registration and tests.
