# NS-A v2.1 → v2.2 — M1 external authority decision request

**Request date:** 2026-08-16  
**Request status:** `AWAITING_EXTERNAL_CONSTITUTIONAL_AUTHORITY`  
**Requested decision:** classification of the proposed v2.2 delta  
**Requesting boundary:** host-controlled engineering evidence only  
**RuFLO authority:** none  
**Current constitution:** local-test candidate `2.1.0`  
**Proposed constitution:** unsigned/untrusted/inactive `2.2.0`  
**Production activation:** `UNAUTHORIZED`

## 1. Decision requested

An identified external constitutional authority must select exactly one disposition:

1. `APPROVE_AS_CONSTITUTIONAL_CHANGE`;
2. `RECLASSIFY_AS_OPERATIONAL_POLICY`;
3. `REJECT`.

Silence, “continue”, technical test success, RuFLO registry state and host implementation activity do **not** constitute this decision.

## 2. Bound evidence set

| Artifact | SHA-256 / canonical digest |
|---|---|
| v2.2 architecture | `d7862b9407ee38e469cfb0d1d1776dd1ee60223bc84eae405ae6546db28cad5b` |
| v2.2 system prompt | `214e4145dfa0cd2595a414ca58faca10ce5ef54eef5a9ebad88c86a77f9a05f2` |
| proposed payload file | `9dd23985e37961cefcb08fa11ac84cd4d84775f9358856692a869bc2323415d1` |
| proposed payload canonical content | `a7d3d32d41eb22ae2dd02ae5297be1660e8edb9a701cd5e6f641148b345ade4d` |
| migration plan | `1821abb59faf4ed9a6a566e9d884ec21f5f3d61d2e589b891b940eba1c8f3c42` |
| M1 technical recommendation | `6c490e2c5c38fb69408a8e4a3ea2c392ea3f5963ef33b0108ca9d3065568077b` |
| M2 preparatory report | `a4bf3ae624606617985e442bc54b0922eb42cc309b3c0e2f6049b56be0248e9c` |
| M2 comprehensive gate transcript | `a93df192bc1c9573dfcf9dd2a08c761ef9b94fa07f6d4bbbde6cabcd5998e70b` |

The architecture validator returned `PASS: 707 assertions`. Component A’s preparatory gate returned 48 tests with 100% statement and branch coverage. These facts establish technical evidence only.

## 3. Delta requiring classification

The unsigned proposed payload changes constitution-controlled fields:

- principle `0` falsifier: requires triage, frame and minimum structure while preserving urgent containment;
- principle `2` falsifier: adds the decomposition actually used;
- principle `4` falsifier: rejects a universal depth quota;
- principle `6` falsifier: rejects false exhaustiveness in addition to invented causes and cosmetic alternatives;
- principle `7` falsifier: adds proposed owner and standard to visible decision conditions;
- adds `nerve.problem_structure` as `IN_LAYER`;
- adds `nerve.execution_commitment` as `IN_LAYER`.

Identity and precedence remain unchanged. Existing Layer 2, Layer 3, Builder, release and irreversible-action handoffs remain out of layer.

## 4. Engineering recommendation

The engineering recommendation is `APPROVE_AS_CONSTITUTIONAL_CHANGE`, because the proposal modifies falsifiable nervous principles and the authoritative Layer 1 capability boundary. Treating these fields as lower-authority operational policy would permit policy to alter constitution-controlled behavior.

This recommendation is non-authoritative and may be rejected by the decision owner.

## 5. Minimum valid decision record

A valid external response must contain all of:

- decision owner identity or governed role;
- evidence that the owner is authorized for constitutional classification;
- decision timestamp;
- exactly one disposition from section 1;
- this request path and the bound hashes from section 2;
- explicit rationale;
- scope: Component A / Layer 1 / v2.1→v2.2 only;
- explicit statement that classification approval is **not** a production signature, trust-root approval, activation command or deployment authorization;
- durable decision reference suitable for later audit.

A message lacking authority identity, scope or bound hashes is advisory feedback, not an M1 exit record.

## 6. Consequences of each disposition

### `APPROVE_AS_CONSTITUTIONAL_CHANGE`

- permits M1 to close after the decision record is independently checked;
- permits the already-green M2 preparatory checks to be reconciled as the M2 stage gate;
- permits a separate M3 signer/trust-root request;
- does not authorize signing, lock creation, activation, Component B or production.

### `RECLASSIFY_AS_OPERATIONAL_POLICY`

- requires written rationale explaining why principle falsifiers and capability boundaries are not constitutional;
- forbids activating the current v2.2 payload as a constitutional successor;
- requires extracting the accepted rules into a separately governed operational-policy artifact and rerunning compatibility analysis.

### `REJECT`

- leaves v2.1 controlling;
- quarantines the v2.2 proposal;
- keeps M2 as preparatory evidence only and blocks M3–M7.

## 7. Current stop condition

Until a valid decision record exists:

- M1 remains `OPEN`;
- M2 remains `PREPARATORY CHECKS PASS — GATE BLOCKED BY M1`;
- M3–M7 remain `BLOCKED`;
- no v2.2 private key, production signature, bundle, trust root, release lock or activation command may be created;
- Component B remains `HOLD`;
- Layer 2 and Layer 3 remain out of scope.
