# NS-A — Component plan: Constitutional Kernel

**Architecture functions:** `A01–A08`  
**Baseline:** `b04ac7d7ae6ae05dc1770062f15dde2334fb927aa9cd1ec0d41c288d819ff781`  
**Status:** `LOCAL FOUNDATION EXIT GATE — PASS; POST-HARDENING RECONCILED 2026-08-14`  
**Production status:** `BLOCKED / NOT CLAIMED`  
**Evidence:** `../evidence/NS-A_EXIT_EVIDENCE.md`  
**Scope:** one component only

## Purpose

Make identity, ten principles, precedence and Layer 1 boundaries immutable, verifiable and bindable to each case before cognitive work starts.

## In scope

- strict Pydantic contracts;
- canonical serialization and SHA-256;
- Ed25519 verification through a trust-store port;
- fail-closed load and case binding;
- precedence and boundary decisions;
- structural diff between versions;
- activation command guarded by independent authority verification and atomic compare-and-swap repository semantics;
- audit event emission through a port;
- unit, property-like and adversarial tests.

## Out of scope

- authoring or privately signing a production constitution;
- policy decision point implementation;
- PostgreSQL adapter and migrations;
- case intake, triage or any later `B–T` component;
- RuFLO integration with the runtime;
- production activation.

## Invariants

1. exactly ten principles, IDs `0–9`, each with a falsifier;
2. canonical payload hash must match before signature verification;
3. unknown key, invalid signature or malformed payload fails closed;
4. a binding includes constitution, phase-policy and scope hashes;
5. a binding never follows a later active constitution automatically;
6. unknown capabilities route `OUT_OF_LAYER` and require handoff;
7. safety/authority/integrity precedence cannot be lowered by content;
8. activation requires an independently verified authority decision and migration plan;
9. activation is compare-and-swap against the expected current version;
10. activation emits an audit record but grants no case action authority.

## Public contracts

- `ConstitutionPayload`
- `SignedConstitutionBundle`
- `ConstitutionBinding`
- `RuleCandidate` / `PrecedenceDecision`
- `BoundaryDecision`
- `ConstitutionDiff`
- `ActivationCommand` / `ActivationReceipt` / `ConstitutionAuditEvent`
- `ConstitutionRepository` (atomic activation plus audit append)
- `SignatureVerifier` / `Ed25519TrustStoreVerifier`
- `ActivationAuthorityVerifier`
- `Clock`

## Test-first exit evidence

- malformed, unsigned, wrong-hash and wrong-key bundles rejected;
- valid Ed25519 bundle loaded;
- binding verify/pass and every material mismatch/fail;
- precedence deterministic and hierarchy preserved;
- known/unknown boundary decisions conservative;
- diff has no activation side effect;
- activation rejects missing plan, unauthorized decision and stale expected version;
- successful activation is atomic and audited;
- `ruff`, `mypy --strict`, `pytest` and coverage gate green.

## Strongest objection

A correct constitutional model can still be bypassed by a future intake or delivery path that never calls it.

**Decision:** this component only establishes the fail-closed kernel. Later state-machine and delivery components must make a verified `ConstitutionBinding` an entry/exit invariant; until then no runtime completeness claim is allowed.
