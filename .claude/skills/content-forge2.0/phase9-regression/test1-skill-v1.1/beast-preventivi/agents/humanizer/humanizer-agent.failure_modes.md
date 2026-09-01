# Failure Modes — humanizer-agent

| ID | Failure | Sintomo | Prevenzione | Rilevamento | Recupero |
|----|---------|---------|-------------|-------------|----------|
| fm-001 | Output schema validation fail | C3 ritorna FAIL | Hardcoded check pre-handoff | Schema validator | Re-run con feedback |
| fm-002 | LLM-speak nel output | Utente segnala tono AI | TOV vincoli nel SP | no_summary_lint | Pass at O4 humanizer |
| fm-003 | Tempo eccessivo (>10 min) | Pipeline lenta | Hard timeout 600s | Monitoring task duration | Skip ottimizzazioni opzionali |
| fm-004 | Tool failure | Tool ritorna error | Try/catch + fallback | Tool error log | Default fallback behavior |
| fm-005 | Out of scope creep | Agent fa lavoro di altro agente | Vincoli espliciti in SP | Eval case 'out of scope request' | Reject + suggest right agent |
| fm-006 | Aderenza sorgente persa | Output contiene best practice generica non da manuale | Force quote/cite per ogni claim | Eval cross-check vs KG | Re-run con context KG enforced |
| fm-007 | Handoff malformato | Next agent non capisce output | Schema handoff hardcoded | Validation handoff JSON | Re-format + retry |
| fm-008 | Token overflow | Context troppo grande | Truncation strategy | Token counting pre-call | Splitting input |
