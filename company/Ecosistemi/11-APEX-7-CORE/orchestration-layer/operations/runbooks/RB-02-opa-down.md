# RB-02 OPA unavailable

1. Confirm policy adapter returns DENY.
2. Block new writes and high-risk actions; no stale ALLOW.
3. Verify signed bundle hash and OPA process health.
4. Restore OPA and execute known ALLOW/DENY probes.
5. Reopen only after default-deny and bundle integrity pass.
