# WF-SEC-SCAN — Security Scan Completo

> **Scansione di sicurezza standalone:** può essere eseguita come gate G-SEC nella pipeline principale o come audit indipendente su codebase esistenti. Owner: plt-sec-sentinel.

## Trigger
- Attivato da plt-cc-master come Fase 5 di WF-SITE-FULL
- Audit periodico su siti DE in produzione (mensile)
- Prima di ogni merge su branch produzione
- Richiesta esplicita da plt-director o Board
- Aggiornamento dipendenze major version su repo in produzione

## Input
```json
{
  "repo_path": "path o URL repo da scansionare",
  "tipo_progetto": "sito | SaaS | tool-interno | landing",
  "contesto": "dati utente gestiti, autenticazione presente, integrazioni terze parti",
  "scope_scan": "full | dipendenze-only | secrets-only | diff-commit",
  "commit_range": "solo per scope diff-commit: da sha a sha"
}
```

## Pipeline (Passi)

### Step 1 — SECRET & PII DETECTION (5 min)
```
plt-sec-sentinel:
  → scansione regex su tutto il codebase:
    - API keys (pattern: sk-, pk-, AIza, AKIA...)
    - Password/token hardcoded
    - Email reali nei file di codice
    - Indirizzi IP interni
  → verifica .gitignore: .env, .env.local, .env.production esclusi
  → output: lista file:line con ogni match trovato
```

### Step 2 — DEPENDENCY AUDIT (5 min)
```
plt-sec-sentinel:
  → npm audit --json → estrae CVE CRITICAL e HIGH
  → confronta con NIST NVD se necessario per contesto
  → output: lista dipendenze vulnerabili con versione fix disponibile
```

### Step 3 — OWASP TOP 10 REVIEW (15 min)
```
plt-sec-sentinel: security-review focalizzata su:
  → A01 Broken Access Control: routes protette, middleware auth
  → A02 Cryptographic Failures: HTTPS obbligatorio, no HTTP interno
  → A03 Injection: input non sanitizzati, SQL/template injection
  → A05 Security Misconfiguration: headers HTTP (CSP, HSTS, X-Frame)
  → A07 Auth Failures: sessioni, JWT handling, password policy
  → A09 Logging: no log di dati sensibili

Per siti/landing semplici (no auth, no db): solo A03 + A05
Per SaaS con auth: OWASP completo
```

### Step 4 — ENVIRONMENT VARIABLES AUDIT (5 min)
```
plt-sec-sentinel:
  → verifica naming convention NEXT_PUBLIC_* (mai segreti con prefisso PUBLIC)
  → controlla che le env vars Vercel dichiarate non siano esposte lato client
  → verifica presenza di .env.example aggiornato (senza valori reali)
```

### Step 5 — REPORT G-SEC (5 min)
```
plt-sec-sentinel produce report:
{
  "verdetto": "VERDE | ROSSO",
  "findings": [
    { "tipo": "SECRET | CVE | OWASP | ENV", "severity": "CRITICAL | HIGH | MEDIUM | LOW",
      "file": "path:line", "descrizione": "...", "fix": "..." }
  ],
  "azioni_bloccanti": [...],  // CRITICAL + HIGH → bloccano
  "backlog": [...]            // MEDIUM + LOW → non bloccano
}
```

## Gate
| Criterio | Risultato |
|---|---|
| 0 finding CRITICAL | Obbligatorio per VERDE |
| 0 finding HIGH | Obbligatorio per VERDE |
| 0 secret/PII hardcoded | Obbligatorio per VERDE |
| Finding MEDIUM/LOW presenti | Non bloccano — vanno in backlog |

## Output
- Report G-SEC con severity tagging
- Verdetto VERDE/ROSSO per la pipeline
- Lista finding bloccanti con fix specifici per plt-site-builder
- Backlog MEDIUM/LOW per OPERATIONS (gestione iterativa)

## Owner Agente
`plt-sec-sentinel`

## Skill Usate
`security-review` · `verify` · `github-automation` (per .gitignore check)
