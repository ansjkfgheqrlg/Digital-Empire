# Failure Modes

| Failure | Detection | Recovery |
|---|---|---|
| Stale context | Check handover/ADR dates | Reload canonical memory |
| Unsupported claim | Missing source or command | Mark unverified and investigate |
| Scope drift | Output lacks WF-0/RF link | Return to ORCH for scope decision |
| Missing handoff | No owner or next step | Create a structured handoff |
