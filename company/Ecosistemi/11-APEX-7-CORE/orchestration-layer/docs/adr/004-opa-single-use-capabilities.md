# ADR-004 — OPA default deny and single-use capability grants

- **Status:** Accepted for W4
- **Date:** 2026-08-23

## Decision

OPA evaluates authorization and returns `ALLOW`, `DENY`, or `REQUIRE_APPROVAL`. OPA does not issue credentials. Unavailable, malformed or unexpected OPA responses fail closed.

The pilot uses opaque capability tokens stored only as SHA-256 hashes. A grant is bound to tenant, workflow, task, execution-token hash and `tool-gateway` audience; TTL is capped at five minutes. A grant authorizes one capability scope and is consumed atomically before tool execution. Retry requires a fresh grant.

The Tool Gateway is the only component that turns a grant into a tool action. Initial tools are repository text read and immutable ADR artifact write. There is no shell executor or unrestricted network tool.

## Consequences

- A failed tool call still consumes the token, reducing replay risk.
- Unknown tools and capabilities are denied.
- R2/R3 require valid, non-stale approval; R3 additionally requires step-up MFA.
- PostgreSQL is the production grant store; the in-memory store exists only for isolated tests.
- OPA bundle distribution/signing and constrained decision caching remain pre-production work.
