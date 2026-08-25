# Threat Model — W10 checkpoint

## Critical assets

Canonical state, approval hashes, capability grants, tenant data, artifact evidence, policy bundles, provider credentials and audit history.

## Priority threats

| Threat | Control | Verification |
|---|---|---|
| Prompt injection grants tools | LLM cannot issue grants; OPA + Tool Gateway | negative capability tests |
| Cross-tenant access | forced PostgreSQL RLS | real integration test |
| Token replay | opaque single-use task-bound grant | PostgreSQL replay test |
| Approval replay | plan/policy hash and SoD | OPA tests |
| Path escape | resolved-root checks, no shell | traversal tests |
| Dependency compromise | pin, audit, SBOM/signature roadmap | pip/npm audit, RuFlo provenance |
| Policy tampering | deterministic bundle + signature verification | W10 signed test bundle |
| Worker crash | lease expiry and stale-token rejection | exit-137 chaos test |
| Unknown side effect | reconciliation before retry | W6 tests |
| Data-removal false claim | deletion state machine and backup expiry | W10 privacy tests |

## Residual risk

The policy signing key used in W10 is ephemeral and test-only. Production requires a KMS/HSM-backed identity. Provider-backed RuFlo execution, object-store KMS, external penetration testing, managed failover and full PITR remain blocked.
