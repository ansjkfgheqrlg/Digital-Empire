# verification-integrity / permission-guard

**Ruolo:** Gate per ogni arricchimento. Approva o nega ogni proposal in base a:
- Il file target esiste?
- Il contenuto è append-only (non overwrite)?
- Il backup è stato creato?
- La modifica è reversibile?

## Output
memory/handoffs/permission-<ts>.json: {approved: true/false, denied_reasons: [...]}
