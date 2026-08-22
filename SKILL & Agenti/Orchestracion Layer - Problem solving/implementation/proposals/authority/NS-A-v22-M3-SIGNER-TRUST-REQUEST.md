# NS-A v2.2 — M3 separate signer and trust-approval request

**Request date:** 2026-08-20  
**Request status:** `AWAITING_SEPARATE_SIGNER_AND_TRUST_AUTHORITY`  
**Scope:** NERVE-SOLVE Layer 1 / Component A / proposed constitution 2.2.0  
**M1 decision:** `NS-A-v22-M1-DECISION-2026-08-20-001`  
**M2:** `PASS`  
**Current v2.2 status:** `UNSIGNED_UNTRUSTED_INACTIVE`

## 1. Separation requirement

The implementation agent and Project Owner classification attestation cannot substitute for a separate signer and trust-root approval. The signer must not send, persist or expose a private key in this workspace. Existing local-test trust material must not be promoted or represented as production trust.

RuFLO has no signing, trust, release, deployment or constitutional activation authority.

## 2. Exact object proposed for signing

| Object | Digest |
|---|---|
| payload file | `9dd23985e37961cefcb08fa11ac84cd4d84775f9358856692a869bc2323415d1` |
| canonical payload bytes | `a7d3d32d41eb22ae2dd02ae5297be1660e8edb9a701cd5e6f641148b345ade4d` |
| architecture v2.2 | `d7862b9407ee38e469cfb0d1d1776dd1ee60223bc84eae405ae6546db28cad5b` |
| system prompt v2.2 | `214e4145dfa0cd2595a414ca58faca10ce5ef54eef5a9ebad88c86a77f9a05f2` |
| M1 decision record | to be verified from `decisions/NS-A-v22-M1-AUTHORITY-DECISION-2026-08-20.json` and its evidence manifest |
| M2 closure transcript | to be verified from `evidence/NS-A-v22-M2-GATE-CLOSURE-2026-08-20.log` and its evidence manifest |

Only the canonical JSON bytes produced with UTF-8, sorted keys, compact separators, Unicode preserved and non-finite numbers forbidden are eligible for signing.

## 3. Required external deliverables

The separate signer/trust process must return all of:

1. signer identity and governed signing role;
2. proof of authorization for this exact scope;
3. signing timestamp and immutable ceremony/reference ID;
4. Ed25519 `key_id` and public key — never the private key;
5. Ed25519 signature over the exact canonical payload bytes;
6. approved trust-root record binding `key_id`, algorithm and public key;
7. provenance binding signer, canonical digest, architecture digest, prompt digest and M1/M2 references;
8. revocation status and a defined revocation authority/process;
9. explicit statement that M3 signing does not itself activate, deploy or migrate cases;
10. independent verification receipt.

Deliverables must first enter a quarantine/incoming area. They must not overwrite v2.1 files or active trust configuration.

## 4. Rejection conditions

M3 fails closed if any of these occurs:

- private key material enters the workspace;
- signer and implementation identity are not separated;
- key identity or authorization is ambiguous;
- signature algorithm differs from approved Ed25519;
- any bound digest differs;
- signature verification fails;
- key is revoked or revocation state is unavailable where required;
- trust approval is missing or merely self-declared by the implementation agent;
- provenance is incomplete;
- a bundle, trust record or lock claims activation authority.

## 5. Effects of valid M3 evidence

A valid M3 response permits only:

- independent verification of signature and trust metadata;
- construction of a distinct candidate bundle in M3 evidence scope;
- consideration of a separate M4 candidate lock.

It does not authorize lock activation, case migration, deployment, Component B, Layer 2 or Layer 3.

## 6. Current stop condition

Until the complete separate M3 response is supplied and verified:

- M3 remains `OPEN`;
- M4–M7 remain `BLOCKED`;
- v2.1 remains controlling;
- v2.2 remains unsigned, untrusted and inactive;
- no production-readiness claim is permitted.
