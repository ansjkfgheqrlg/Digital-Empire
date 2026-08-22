# NS-A v2.2 — M2 sequential gate closure report

**Date:** 2026-08-20  
**Scope:** NERVE-SOLVE Layer 1 / Component A / constitution 2.1.0→2.2.0  
**M1:** `PASS_LOCAL_AUTHORITY_ATTESTATION`  
**M2:** `PASS`  
**M3:** `OPEN — SEPARATE SIGNER AND TRUST APPROVAL REQUIRED`  
**v2.2:** `UNSIGNED_UNTRUSTED_INACTIVE`

## Authority basis

The user explicitly selected:

- authority attestation: `YES_OWNER`, as Project Owner / Constitutional Authority;
- disposition: `APPROVE_AS_CONSTITUTIONAL_CHANGE`.

The durable decision record is `../decisions/NS-A-v22-M1-AUTHORITY-DECISION-2026-08-20.json`, decision reference `NS-A-v22-M1-DECISION-2026-08-20-001`.

The decision is accepted for local governance classification. Identity assurance is self-attested conversation context, not independently verified production identity. It is not a cryptographic signature, signer appointment, trust-root approval, activation command or deployment authorization.

## Independent decision-record verification

`scripts/verify_m1_authority_decision.py` verified:

- exact record shape and disposition;
- authority role, assurance limitation and scope;
- request packet hash;
- all seven bound evidence file hashes;
- proposed payload file and canonical-content hashes;
- all explicit non-authorizations;
- mandatory separation of M3 signer/trust approval.

Result: `PASS: M1 authority decision record shape and all bound hashes verified`.

## M2 closure evidence

The post-decision sequential gate reran under CPython 3.13.14 with the exact versions in `requirements-dev.lock`:

- strict v2.2 payload parse: PASS;
- canonical payload SHA-256: `a7d3d32d41eb22ae2dd02ae5297be1660e8edb9a701cd5e6f641148b345ade4d`;
- compile: PASS;
- 29 unique public exports: PASS;
- Ruff: PASS;
- strict mypy over eight production source files: PASS;
- pytest: 48 passed;
- statement coverage: 350/350, 100%;
- branch coverage: 62/62, 100%;
- locked v2.1 candidate verifier: PASS;
- all immutable v2.1 hashes: PASS;
- v2.2 architecture validator: `PASS: 707 assertions`;
- prohibited v2.2 release/authority artifacts: zero.

Authoritative transcript: `NS-A-v22-M2-GATE-CLOSURE-2026-08-20.log`.

An initial closure run correctly stopped on two Ruff defects in the newly added decision verifier (import ordering and line length). That red transcript is preserved as `NS-A-v22-M2-GATE-CLOSURE-TEST-FIRST-RED-2026-08-20.log`; both defects were corrected before the authoritative green rerun.

## M2 disposition

M2 now passes sequentially because:

1. M0 is already green;
2. M1 has an explicit bounded authority classification;
3. M2 technical checks have been rerun after that decision;
4. no active lock, trust root, bundle or case binding changed;
5. v2.1 remains immutable and controlling.

## Next gate

M3 cannot be self-issued by the implementation agent. It requires:

- a signer separate from implementation and classification authority;
- externally protected private-key custody;
- an approved public trust-root record;
- an Ed25519 signature over the exact canonical payload;
- provenance and revocation metadata;
- independent verification before any M4 lock is considered.

The request packet is `../proposals/authority/NS-A-v22-M3-SIGNER-TRUST-REQUEST.md`. No private key, production signature, bundle, trust root or v2.2 lock has been generated.
