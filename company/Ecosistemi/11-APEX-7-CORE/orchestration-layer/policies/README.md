# OCP Policy Bundle

`authorization.rego` is default-deny and returns one of `ALLOW`, `DENY`, or `REQUIRE_APPROVAL`.

The control plane remains responsible for cryptographic verification, current time, nonce consumption and plan/policy hashes supplied to OPA. OPA evaluates policy; it does not issue capability tokens.

Test with a pinned OPA binary:

```bash
opa fmt --fail policies/
opa test policies/ -v
opa check --strict policies/
```
