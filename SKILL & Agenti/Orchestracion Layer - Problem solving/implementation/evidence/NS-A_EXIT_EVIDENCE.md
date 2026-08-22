# NS-A — Constitutional Kernel local foundation exit evidence

**Initial gate date:** 2026-08-13  
**Post-hardening reconciliation:** 2026-08-14  
**Architecture baseline:** `b04ac7d7ae6ae05dc1770062f15dde2334fb927aa9cd1ec0d41c288d819ff781`  
**Execution state:** `E1 — LOCAL DISCOVERY / FOUNDATION AUTHORIZED`  
**Bounded result:** `LOCAL FOUNDATION EXIT GATE — PASS`  
**Production readiness/deployment:** `BLOCKED / NOT CLAIMED`

## 1. Scope closed

The bounded Component A implementation covers architecture functions `A01–A08`:

| Function | Implemented behavior | Evidence class |
|---|---|---|
| A01 | exact-version load; canonical SHA-256 then Ed25519 verification | positive and wrong hash/key/signature/version tests |
| A02 | immutable case binding over constitution, phase policy, scope, IDs and timestamp | valid binding and frozen-model tests |
| A03 | exact-version reload and complete binding-material verification | every material field tampered; replacement attack rejected |
| A04 | explicit precedence ranking; no hidden same-rank tie-break | winner, empty set, same-rank and unranked-domain tests |
| A05 | typed registered boundary; unknown capability fails closed to handoff | in-layer, Layer 2 and unresolved-capability tests |
| A06 | identity rendered only from a verified case binding | valid and tampered-binding tests |
| A07 | structural version diff without activation | changed principle and no-side-effect test |
| A08 | external authority check then repository-level atomic CAS plus audit | denial, stale CAS, concurrent CAS and success tests |

The implementation contains no domain reasoning and no private signing key or signing API.

## 2. Architectural correction made during validation

Initial A06 code accepted a constitution bundle directly. The definitive architecture requires `render_identity_anchor` to accept a binding. This was corrected to accept `ConstitutionBinding`, reload the exact signed version, verify all binding material and only then return the identity anchor. The change prevents identity use outside a case-bound constitutional context.

The Component A plan was also corrected to replace the obsolete independent `AuditSink` contract with the repository operation that atomically performs activation and audit append.

## 3. Verification environment

- CPython `3.13.14` (project target remains `>=3.11`);
- Pydantic `2.13.4`;
- Cryptography `46.0.7`;
- pytest `9.1.1`;
- pytest-asyncio `1.4.0`;
- mypy `1.20.2`;
- Ruff `0.16.2`;
- Coverage.py `7.15.4`.

`requirements.lock` and `requirements-dev.lock` preserve the exact locally tested versions. They are version locks, not yet hash-locked cross-platform supply-chain attestations.

## 4. Gate results

Executed in `implementation/` after the final A06 correction:

| Gate | Result |
|---|---|
| import/compile and public export check | `PASS` — 29 public exports after final A06 correction |
| Ruff | `PASS` — all checks passed |
| strict mypy on production source | `PASS` — no issues in 8 source files |
| pytest | `PASS` — 40 tests |
| statement coverage | `100%` — 342/342 |
| branch coverage | `100%` — 56/56, zero partial branches |
| coordinated trust-store + lock replacement regression | `PASS` — rejected by code-pinned public-key anchor; originals restored and reverified |
| locked candidate verification | `PASS` — signature, hashes, trust key and inactive status |
| architecture validator | `PASS` — 590 assertions |

Final gate command:

```text
ruff check .
mypy src
coverage erase
coverage run -m pytest -q
coverage report --fail-under=100 -m
python scripts/verify_constitution_candidate.py
```

Observed result on the final 2026-08-14 post-hardening run: compile/import passed with 29 exports; all static checks passed; `40 passed`; total `342` statements and `56` branches at `100%`; candidate verifier reported PASS while explicitly denying production activation. Full logs: `NS-A_POST_HARDENING_GATE.log` and `NS-A_COORDINATED_TAMPER_REGRESSION.log`.

Repository-root architecture result:

```text
PASS: 590 assertions
```

## 5. Locked local signed candidate

The constitution is a signed **local test candidate**, never an active production constitution.

| Artifact | SHA-256 |
|---|---|
| raw payload file | `fbd5d16597283a4dca48be7d55e559f73742da8276cd1a6cf0a85241851165c5` |
| canonical payload | `66a9a215c5af4f0ed3011b6f51489170c01fb4ba09e4af8a8fc0318b850642c4` |
| signed bundle file | `68539ec3b530dad524a279f758eea7a105e2aeb5a2dd4a03520295997e158ed7` |
| candidate lock file | `b1914b2aff9220075a0b86f599a34bf3eed6d95ca58679beffa8b99e4e471ab0` |
| local test trust store | `76bc80bf0b723af05955aee24ecbcb25a417fa1c59cbb786424a4709144ecba5` |

The one-time private test key was not persisted. The verifier pins the expected architecture hash, canonical payload hash, constitution version, key ID, public-key hash and artifact paths in code before checking the lock and Ed25519 signature. The trust record is explicitly `LOCAL_TEST_ONLY_NOT_PRODUCTION_TRUST`; the lock sets `production_activation_authorized` to `false`. This is verification evidence, not release-signing or production-activation authority.

## 6. RuFLO evidence boundary

RuFLO did not implement, test, sign, store or approve Component A. Its POC supplied only role-separation and coordination observations. It was stopped during the original Component A closure. On 2026-08-14 it was separately reactivated for bounded Component B coordination with direct pins for both `ruflo@3.38.8` and `@claude-flow/cli@3.38.8`. That later activation neither changes nor contributes to Component A evidence. Worker execution remains unproven, and RuFLO remains non-authoritative and outside the critical path. Current disposition: `../../poc/ruflo/ACTIVATION_REPORT_2026-08-14.md`.

## 7. Residual risks and exclusions

This local component gate does **not** establish production readiness:

1. only CPython 3.13 was executed; the declared 3.11/3.12 compatibility matrix has not run;
2. no PostgreSQL repository, migration, transaction/outbox or failover test exists yet;
3. the repository used in tests is an in-memory double, not durable authoritative state;
4. no KMS/HSM, production trust distribution, rotation, revocation or release-signing ceremony exists;
5. no case runtime yet enforces `ConstitutionBinding` at every entry/exit, so future bypass remains the strongest architectural objection;
6. no paused-safe behavior for already active cases can exist until the case/workflow runtime is built;
7. dependency locks are not artifact/hash locked and no SBOM/provenance pipeline exists;
8. performance, soak, fault-injection, restore and operational drills remain unrun;
9. Components B–T remain unimplemented.

## 8. Closure decision

Component A satisfies its **bounded local foundation** exit evidence with all current checks green. The final verifier hardening debt was reconciled on 2026-08-14: a coordinated trust-store/lock replacement was rejected by the independent code-pinned key hash, original artifacts were restored to their recorded hashes, and the complete sequential gate passed again. It may be used as the prerequisite contract for planning the next single component. It must not be described as production-ready, deployed, durably integrated or operationally proven.
