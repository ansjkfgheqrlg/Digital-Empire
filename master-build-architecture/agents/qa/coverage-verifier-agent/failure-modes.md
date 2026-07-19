# Failure Modes

| Failure | Detection | Recovery |
|---|---|---|
| Reviewing stale context | Compare timestamps and ADRs | Reload canonical memory |
| Accepting an unverified claim | Require command/file evidence | Downgrade to unverified and re-test |
| Validating own critical work | Check assignment ownership | Assign independent reviewer |
| Ignoring workflow traceability | Inspect WF-0 links | Block and restore trace links |
