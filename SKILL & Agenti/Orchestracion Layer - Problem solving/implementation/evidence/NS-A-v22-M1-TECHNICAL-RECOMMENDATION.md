# NS-A v2.1 → v2.2 — M1 technical classification recommendation

**Date:** 2026-08-15  
**Scope:** Component A / Layer 1 only  
**Decision owner:** external constitutional authority, not the host implementer and not RuFLO  
**Technical recommendation:** classify the proposed delta as a **constitutional change**  
**Authority decision:** **UNRESOLVED**  
**M1 gate:** **OPEN / NOT PASSED**  
**Activation:** **UNAUTHORIZED**

## 1. Evidence examined

- immutable v2.1 payload: `config/constitutions/nerve-solve-2.1.0.payload.json`;
- unsigned v2.2 proposal: `proposals/constitution/nerve-solve-2.2.0.payload.proposed.json`;
- v2.2 architecture SHA-256: `d7862b9407ee38e469cfb0d1d1776dd1ee60223bc84eae405ae6546db28cad5b`;
- v2.2 prompt SHA-256: `214e4145dfa0cd2595a414ca58faca10ce5ef54eef5a9ebad88c86a77f9a05f2`;
- strict analysis transcript: `NS-A-v22-M1-STRICT-PAYLOAD-ANALYSIS.log`.

The proposal parses with `ConstitutionPayload.model_validate_json(..., strict=True)` under schema `1.0`. The canonical payload hashes are:

- v2.1: `66a9a215c5af4f0ed3011b6f51489170c01fb4ba09e4af8a8fc0318b850642c4`;
- proposed v2.2: `a7d3d32d41eb22ae2dd02ae5297be1660e8edb9a701cd5e6f641148b345ade4d`.

## 2. Semantic delta

The change is not merely wording in an operational runbook. It changes the constitutional payload itself:

1. five falsifiable principle definitions are strengthened (`0`, `2`, `4`, `6`, `7`);
2. `nerve.problem_structure` is added as an in-layer constitutional capability;
3. `nerve.execution_commitment` is added as an in-layer constitutional capability;
4. the constitution version and issue timestamp change;
5. identity, precedence ordering, the other five principles and the eight pre-existing boundary capabilities remain semantically unchanged.

The two added capabilities alter the authoritative boundary of Layer 1. The five changed falsifiers alter conditions under which the nervous principles are objectively violated. Both are governed by Component A’s constitution contracts, not only by operational policy.

## 3. Technical classification

**Recommendation: CONSTITUTIONAL_CHANGE.**

Reasons:

- the proposal directly modifies fields represented by `ConstitutionPayload`;
- principle falsifiers are constitutional invariants and cannot be downgraded to implementation guidance without weakening their enforcement meaning;
- adding in-layer capabilities changes the Layer 1 boundary and therefore the admissible action space;
- treating this as operational policy would permit a lower-authority policy mechanism to modify constitution-controlled behavior.

This recommendation is engineering evidence only. It does not impersonate or replace the required external constitutional authority.

## 4. Critical gaps and controls

1. Schema `1.0` has no architecture/prompt source-hash fields. The proposal hashes are independently verified, but the payload does not intrinsically bind those source documents. Any future authorized release lock must bind the exact source hashes externally, as the v2.1 local-test lock does.
2. The v2.2 proposal has no signature, trusted release key, bundle, active lock or activation command.
3. RuFLO contains coordination records only and has no constitutional authority or verified worker output.
4. M2 may produce tests and fail-closed runtime hardening only. It must not produce release artifacts or imply M1 approval.

## 5. Required authority response

An authorized decision record must explicitly choose one of:

- `APPROVE_AS_CONSTITUTIONAL_CHANGE` — permits later M3 release-authority work, but does not itself sign or activate;
- `RECLASSIFY_AS_OPERATIONAL_POLICY` — requires written rationale explaining why changed principle falsifiers and Layer 1 boundaries are not constitutional;
- `REJECT` — the proposal remains inactive and v2.1 remains controlling.

Until that record exists, **M1 remains open, M3–M7 remain blocked, v2.1 remains the only locally verified candidate, and v2.2 remains unsigned, untrusted, inactive and unauthorized.**
