# ADR-014 — Complete the local orchestration layer with API, worker and outbox

- **Status:** Accepted for W13
- **Date:** 2026-08-23

## Decision

Complete the local secure pilot with a loopback-only FastAPI service, Ed25519 operator authentication, opaque sessions, PostgreSQL command/query service, durable worker, event-stream persistence and outbox publisher.

Workflow creation is idempotent by tenant/key. The worker claims a durable task, executes the existing LocalRuntime R1 slice, commits seven transitions plus task result, and the outbox publisher marks all eight events delivered. Cancelled workflows cannot be claimed.

R2, R3, anonymous access and RuFlo generative execution remain disabled.

## Consequences

- The local pilot has a real API/worker execution surface rather than CLI-only composition.
- The local outbox sink writes JSON to stdout; production requires a durable broker.
- The Compose profile remains local and uses simplified database credentials.
- Production readiness still requires the external/human controls listed by the production PRR.
