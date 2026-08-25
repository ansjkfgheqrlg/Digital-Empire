# ADR-010 — Security hardening, governed deletion and restore evidence

- **Status:** Accepted for W10
- **Date:** 2026-08-23

## Decision

Security release evidence includes Bandit, dependency audit, secret scan, signed policy-bundle verification, real RLS tests and an environment SBOM. Zero findings in these tools does not replace an independent penetration test.

Privacy deletion is an explicit state machine. Subject references are hashed; every transition requires actor and evidence; legal hold blocks deletion; all systems and derived indexes must prove deletion/purge; backup expiry is recorded before a receipt can close.

Database recovery uses a dedicated read-only backup role with `BYPASSRLS` and a separate DR operator role. Application and migration roles are not reused for routine backup. Restore validation sets a known drill tenant because forced RLS correctly hides rows without tenant context.

## Consequences

- Backup credentials are high-impact and require vaulting, monitoring and no application access.
- The W10 signing key is ephemeral and test-only; production requires KMS/HSM-backed signing.
- PostgreSQL schema, state, audit and outbox were restored together in the sandbox.
- Managed failover, PITR and external penetration testing remain pre-production blockers.
