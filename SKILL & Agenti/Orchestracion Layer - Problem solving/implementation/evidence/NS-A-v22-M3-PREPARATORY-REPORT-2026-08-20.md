# NS-A v2.2 — M3 preparatory verifier report

**Date:** 2026-08-20  
**Scope:** public signer/trust evidence intake only  
**M3 preparatory implementation:** `PASS`  
**M3 sequential gate:** `OPEN — EXTERNAL SIGNER/TRUST RESPONSE REQUIRED`  
**v2.2:** `UNSIGNED_UNTRUSTED_INACTIVE`

## Implemented

1. Strict public-evidence contract: `contracts/release/NS-A-v22-M3-RESPONSE.schema.json`.
2. Fail-closed verifier: `scripts/verify_m3_response.py`.
3. Quarantine boundary: `incoming/README.md` and expected response path `incoming/NS-A-v22-M3-signer-trust-response.json`.
4. Three targeted tests in `tests/unit/constitutional/test_m3_response_verifier.py`.

The verifier is pinned to the exact v2.2 payload, canonical digest, architecture, system prompt, M1 decision and M2 gate transcript. It requires distinct signer, trust approver and independent-verifier identities; Ed25519; approved/non-revoked public trust metadata; provenance; timezone-bearing timestamps; strict base64 lengths; public-key hash binding; and a valid signature over the canonical payload bytes.

It recursively rejects private-key/secret-shaped fields and PEM private-key markers before interpreting the response. It never creates a key or signature.

## Test-first evidence

The initial targeted run failed because `verify_m3_response.py` did not yet exist: three tests failed as expected. The authoritative red is `NS-A-v22-M3-VERIFIER-TEST-FIRST-RED-2026-08-20.log`.

A separate precondition log records that workspace materialization had removed `.venv`; it is not treated as the test-first red. The environment was restored from exact `requirements-dev.lock` before the authoritative red and green runs.

After implementation and static corrections:

- targeted M3 verifier tests: `3 passed`;
- RFC 8032 public-vector verification: PASS;
- tampered-message rejection: PASS;
- private-key material used: none;
- missing external response: clean `BLOCKED`, exit code 2;
- unsafe private-key-shaped response field: rejected, exit code 1.

## Comprehensive gate

The final gate returned:

- CPython 3.13.14 and exact development-lock versions: PASS;
- JSON decision/contract parsing: PASS;
- compileall: PASS;
- Ruff: PASS;
- strict mypy over eight production source files: PASS;
- M1 decision evidence: PASS;
- pytest: 51 passed;
- statement coverage: 350/350, 100%;
- branch coverage: 62/62, 100%;
- immutable v2.1 verification and hashes: PASS;
- architecture v2.2: `PASS: 707 assertions`;
- prohibited v2.2 release/secret artifact count: zero.

Authoritative transcript: `NS-A-v22-M3-PREPARATORY-COMPREHENSIVE-GATE-2026-08-20.log`.

A prior comprehensive run reached the final scanner but stopped because the quarantine directory did not yet exist. The scanner red is preserved; `incoming/README.md` now makes the quarantine boundary explicit, and the entire gate was rerun green.

## Disposition and percentage

The M3 verifier preparation is complete, but preparatory work is not the M3 gate itself. M0–M2 remain the only passed sequential gates.

**Migration progress remains 3/8 = 37.5%.**

M3 can pass only after a real external response supplies public signer/trust evidence and an Ed25519 signature over the exact canonical v2.2 payload. No implementation-agent action can truthfully manufacture that separation.
