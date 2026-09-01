# verification-integrity / change-auditor

**Ruolo:** Logga ogni modifica eseguita. Gestisce il rollback.
Ogni operazione di enrich ha un record in memory/audit/.

## Rollback
```bash
python scripts/audit_log.py --rollback PROP-001
```
