# Strategy Coordinator — Failure Modes

| Failure | Symptom | Prevention | Detection | Recovery |
|---------|---------|------------|-----------|----------|
| Scelta strategia generica | Manifest usa solo "default" | Sempre consulta specialisti + registry | Strategy Controller audit | Riscelta con specialisti + log in memory |
| Non salva in memory | Nessun entry in strategy-applications | Tool obbligatorio WriteToMemory | Memory Auditor | Recupero manuale + CP retroattivo |
| Ignora tipo contenuto | Design video trattato come marketing | Content-Type Strategist obbligatorio | Visual-Verifier + coverage basso | Re-run con manifest corretto |

**Trace**: Failure modes per il reparto strategie.