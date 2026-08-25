# ADR-003 — PostgreSQL canonical state, transactional audit and outbox

- **Status:** Accepted for W3 implementation; runtime certification pending
- **Date:** 2026-08-23

## Decision

PostgreSQL 16 is the canonical state store. Every domain mutation is performed through an async Unit of Work that installs tenant context, applies optimistic version checks, and writes state, audit and outbox records in one transaction.

The pilot work queue uses `FOR UPDATE SKIP LOCKED`, 30-second leases and execution-token hashes. A stale heartbeat or result cannot mutate a task. Outbox delivery is at-least-once; consumers must deduplicate by event ID.

All tenant-owned tables force Row Level Security. The runtime role must not own tables or possess `BYPASSRLS`.

## Consequences

- A real PostgreSQL integration environment is required before W3 receives production certification.
- Unit tests validate SQL intent and transaction ordering but cannot prove PostgreSQL lock, RLS or failover semantics.
- NATS is deferred until measured queue triggers are crossed.
- Destructive down migration is prohibited; recovery uses forward fixes or restore.
