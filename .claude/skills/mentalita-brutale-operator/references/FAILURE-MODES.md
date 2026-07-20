# Failure Modes

| Failure | Symptom | Prevention | Detection | Recovery |
|---|---|---|---|---|
| Secret in Git | literal password/token assignment | env-only + secret scan | `secret_scan.py` | revoke/rotate, remove current file; history remains compromised |
| Token expiry | 401/OAuth error | refresh cadence | doctor online | pause, refresh/reauth |
| Wrong account | username differs | health before side effect | account gate | pause, correct token/id |
| Private/invalid media URL | container ERROR | HTTPS mirror + preflight | container status | restage and retry |
| PNG sent live | Meta rejects image | convert to JPEG | live format gate | Pillow conversion |
| Duplicate publish | same content twice | canonical hash | publication unique key | pause/audit retry path |
| Browser UI drift | selector missing | API-first | legacy test fails | do not promote legacy fallback |
| Quality drift | pass rate drops | independent CF-R6 | batch report | rework/rollback pattern |
| Pattern overfit | one post drives rule | n≥3 + median | CF-R8 gate | demote to observation |
| Missing insights represented as 0 | false failure | preserve null | response parser | recollect after delay |
| Harmful “brutal” copy | humiliation/unsafe claim | safety gate | forbidden claims + review | reject/rewrite |
| Fake video study | no frame/timestamp | video forensics | evidence coverage | ingest original via Empire Studio |
| Auto without certification | scheduler side effect | mode+env+kill switch | LiveGuardError | complete evidence gate |
