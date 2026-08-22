# NS-A v2.1 → v2.2 — M2 preparatory implementation report

**Date:** 2026-08-15  
**Scope:** Component A / Layer 1 only  
**M0:** `PASS`  
**M1:** `OPEN — EXTERNAL AUTHORITY UNRESOLVED`  
**M2 technical checks:** `PASS`  
**M2 migration stage:** `BLOCKED_BY_M1`  
**M3–M7:** `BLOCKED`  
**v2.2 activation:** `UNAUTHORIZED`

## 1. Bounded change sets

### Change set 1 — exact environment and untouched baseline

- recreated `implementation/.venv` with CPython `3.13.14`;
- installed only `requirements-dev.lock` exact versions;
- preserved an environment freeze in `NS-A-v22-python-environment-freeze.txt`;
- reran the untouched v2.1 production gate: 29 exports, Ruff pass, strict mypy pass on eight production files, 40 tests, 342/342 statements and 56/56 branches at 100%;
- reverified the locked local-test v2.1 candidate.

Two invocation errors were corrected without changing product code: an expanded `mypy src tests` run did not match the historical production-source gate and exposed pre-existing test annotation debt; a subsequent src-layout coverage run initially omitted `PYTHONPATH=src`. The authoritative passing baseline is `NS-A-v22-M0-BASELINE-PASS.log`.

### Change set 2 — M1 technical recommendation

Strict schema validation passed for the unsigned proposed payload. The semantic delta is five principle-falsifier changes plus two new in-layer capabilities. The technical recommendation is `CONSTITUTIONAL_CHANGE`, but no host or RuFLO action was treated as constitutional authority. See `NS-A-v22-M1-TECHNICAL-RECOMMENDATION.md`.

### Change set 3 — monotonic activation guard, test first

The new migration tests first demonstrated that A08 accepted both a `2.2.0 → 2.1.0` downgrade and a `2.1.0 → 2.1.0` same-version activation. Red evidence: `NS-A-v22-M2-TEST-FIRST-RED.log`.

A08 now rejects `target_version <= expected_current_version` after exact target verification and before authority/repository side effects. Tests prove:

- downgrade rejection;
- same-version collision/no-op rejection;
- forward version reaches the independent authority boundary;
- authority denial leaves active version, repository version and audit unchanged.

The migration plan’s rollback wording was corrected accordingly: rollback of constitutional semantics must use a new forward version rather than reactivate a lower version. Existing case bindings are never rewritten.

### Change set 4 — explicit key revocation, test first

A corrected red test proved the verifier lacked an explicit revocation input: `NS-A-v22-M2-REVOCATION-TEST-FIRST-RED-2.log`.

`Ed25519TrustStoreVerifier` now accepts a read-only `revoked_key_ids` collection and excludes those keys even when their public key remains provisioned. The positive/negative test uses the public RFC 8032 §7.1 vector; no private key was generated, reconstructed or persisted.

## 2. Added migration coverage

`tests/unit/constitutional/test_v22_migration.py` adds eight tests covering:

1. strict v2.2 payload validation and rejection of extra fields;
2. exact semantic 2.1→2.2 diff with no activation/audit/authority side effect;
3. simultaneous v2.1/v2.2 repository visibility with isolated immutable case bindings;
4. explicit cryptographic-verifier revocation overriding an otherwise valid public test vector;
5. proposed-candidate rejection for revoked verifier identity, signature-byte tamper and payload/hash tamper;
6. downgrade rejection before authority or persistence;
7. a forward candidate reaching authority but remaining inactive when denied;
8. same-version activation/collision rejection before authority.

The unsigned payload is exercised through in-memory port-test objects using a deterministic no-key verifier. No v2.2 signed bundle is written or represented as release evidence.

## 3. Final technical gate

Authoritative transcript: `NS-A-v22-M2-PREPARATORY-COMPREHENSIVE-GATE.log`.

| Gate | Result |
|---|---|
| CPython | `3.13.14` |
| compile | pass |
| public exports | 29, unchanged |
| Ruff | pass |
| strict mypy, production source | pass, 8 files |
| pytest | `48 passed` |
| statements | `350/350`, 100% |
| branches | `62/62`, 100% |
| locked v2.1 verifier | pass; production activation unauthorized |
| immutable v2.1 artifact hashes | all pass |
| v2.2 architecture validator | `PASS: 707 assertions` |
| persisted forbidden v2.2 release artifacts | zero |

## 4. Public critical register

| Type | Record |
|---|---|
| Assumption | Semantic version strings remain constrained by the existing strict `X.Y.Z` schema. |
| Objection | Starting M2 before M1 could imply sequencing bypass. |
| Decision | Only preparatory, version-agnostic tests/hardening were executed; the M2 migration stage is explicitly not passed. |
| Gap found | A08 previously allowed downgrade and same-version activation. |
| Modification | Reject all non-forward target versions before authority/repository side effects. |
| Contradiction found | The migration rollback paragraph allowed returning to `2.1`, conflicting with mandatory downgrade rejection. |
| Architecture-level correction | The component migration plan now requires a new forward corrective version; old bindings remain immutable. |
| Gap found | Revocation was implicit only through trust-store key removal. |
| Modification | Add explicit read-only revoked-key exclusion to the verifier adapter. |
| Evidence limit | The in-memory repository is a test double; no PostgreSQL adapter or restart-retention proof exists in Component A. |
| Evidence limit | No real v2.2 signer, release trust root, release bundle, separate v2.2 lock or authority decision exists. |
| RuFLO limit | Registry metadata supplied no worker output and made no code, trust or authority decision. |

## 5. Current disposition

The bounded implementation is technically green, but the migration is not authorized to advance to release stages. M1 still requires an external authority decision. Therefore:

- v2.1 artifacts and case-binding semantics remain authoritative and immutable;
- v2.2 remains an unsigned proposal;
- no M3 signer request, M4 lock, M5 shadow activation, M6 activation or M7 Component B authorization may be claimed;
- Component B remains `HOLD`; Layer 2 and Layer 3 remain out of scope.
