---
Type: CONCEPT
Status: Active
Tags: #workflow #cto #security #audit #aidefence #dipendenze #cf-grade
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-SECURITY-AUDIT — Workflow Audit di Sicurezza Periodico

> **Tipo:** CF-grade · **Figura:** CTO
> **Blueprint:** `company/Board-CSuite/_BLUEPRINT/BP-CTO.md`
> **Connessioni:** [[WF-TECH-REVIEW]] · [[cto-security-sentinel]] · [[cto-conductor]] · [[KPI]]

---

## Scopo

Eseguire una scansione sistematica e periodica di tutta l'infrastruttura della holding per
identificare: segreti nel repo, vulnerabilità nelle dipendenze, PII non protette nei log/export,
pattern di injection nei prompt degli agenti. Il risultato è un report rischi strutturato con
priorità di remediation. Questo workflow è distinto dal gate security del WF-TECH-REVIEW (che
è pre-deploy): l'audit è una scansione a tappeto dell'intera holding, non limitata a un sistema
specifico in fase di deploy.

---

## Trigger

- **Periodico:** ogni lunedì mattina (o inizio settimana lavorativa). Frequenza minima: settimanale.
- **On-demand:** richiesta del conductor o del CEO dopo un incidente o una comunicazione di
  vulnerabilità da parte di un fornitore di stack (es. advisory Vercel, Next.js, Ruflo).
- **Post-deploy critico:** dopo ogni deploy di un sistema classificato "alto impatto" (più di
  3 ecosistemi impattati o sistema con accesso a dati utente).
- **Auto-trigger:** `cto-security-sentinel` può avviare autonomamente una scansione parziale
  se rileva un pattern sospetto durante un'operazione routinaria.

---

## Agenti coinvolti

| Agente | Fase | Ruolo nel workflow |
|---|---|---|
| `cto-memoria` | 1, 7 | RECALL audit precedente; write report e checkpoint |
| `cto-conductor` | 1-7 | Orchestratore; decide le priorità di remediation |
| `cto-security-sentinel` | 2, 3, 4 | Esegue le scansioni (segreti, dipendenze, PII, injection) |
| `cto-stack-radar` | 3 | Fornisce la lista aggiornata delle dipendenze nel radar |
| `cto-integration-architect` | 4 | Verifica la sicurezza dei contratti di integrazione |
| `cto-tech-debt-tracker` | 6 | Registra ogni finding non-critico come item debito |
| `cto-platform-liaison` | 6 | Se il remediation richiede azioni su 06-PLATFORM |
| `cto-forge-liaison` | 6 | Se il remediation richiede fix in artefatti FORGE |

---

## Flusso passo-passo

```
STEP 1 — RICEZIONE E RECALL
├─ cto-memoria carica: report audit precedente, incidenti aperti, ADR di sicurezza attivi
├─ cto-conductor determina lo scope dell'audit (full | parziale | focus-area)
│    full: tutta la holding (periodico settimanale)
│    parziale: solo sistemi modificati dall'ultimo audit
│    focus-area: solo un dominio specifico (es. solo dipendenze, solo segreti)
└─ Output: scope audit + contesto da audit precedente

STEP 2 — SCAN SEGRETI (repo e staging)
├─ cto-security-sentinel scansiona:
│    - Tutto il repo company/ per pattern di segreti (API key, token, password, IBAN)
│    - File di configurazione (*.env*, *.json config, *.yml)
│    - Script e workflow scripts/
│    - Artefatti FORGE nel catalogo
├─ Findings classificati: critico (in prod) | alto (in staging) | medio (non deployato) | info
└─ Output: lista segreti trovati con path + gravità

STEP 3 — SCAN DIPENDENZE (CVE)
├─ cto-stack-radar fornisce la lista completa delle dipendenze censite nel radar
├─ cto-security-sentinel verifica CVE per ogni dipendenza:
│    CVSS ≥9.0: critico → alert immediato al conductor
│    CVSS 7.0-8.9: alto → da risolvere entro 48h
│    CVSS 4.0-6.9: medio → da risolvere entro il prossimo sprint
│    CVSS <4.0: info → registrato come debito tecnico basso
└─ Output: lista CVE con CVSS score, dipendenza impattata, versione vulnerabile, fix disponibile

STEP 4 — SCAN PII E INTEGRATION SECURITY
├─ cto-security-sentinel scansiona output/log/export recenti per PII non anonimizzate
│    (email, nomi, CF, telefoni, IBAN in file che potrebbero essere esposti)
├─ cto-integration-architect verifica i contratti di integrazione:
│    - Nessun segreto nei contratti I/O (devono usare riferimenti a .env, mai valori)
│    - I webhook hanno autenticazione (HMAC o API key via header sicuro)
│    - Le API esterne hanno timeout e retry configurati
└─ Output: PII findings + integration security assessment

STEP 5 — SCAN PROMPT INJECTION (agenti attivi)
├─ cto-security-sentinel scansiona tutti gli agenti nel catalogo per:
│    - Mancanza di input sanitization nei campi utente
│    - System prompt leak risk (prompt che espone informazioni interne)
│    - Agenti con accesso a tool critici senza validazione dell'input
└─ Output: lista agenti con potential injection risk + severity

STEP 6 — PRIORITIZZAZIONE E REMEDIATION BRIEF
├─ cto-conductor raccoglie tutti i findings e li prioritizza:
│    Critico: blocco immediato del sistema impattato + remediation entro 2h
│    Alto: remediation entro 48h con handoff a FORGE/Platform
│    Medio: entra nel register debito tecnico con scheduling
│    Info/Basso: entra nel register debito tecnico come bassa priorità
├─ cto-tech-debt-tracker registra tutti i findings non-critici come item debito
├─ cto-platform-liaison: brief di remediation per sistemi Platform se richiesto
├─ cto-forge-liaison: brief di remediation per artefatti FORGE se richiesto
└─ Output: remediation-plan strutturato con owner, deadline, acceptance criteria

STEP 7 — REPORT E MEMORIA
├─ cto-conductor produce il security-report strutturato (vedi output)
├─ cto-memoria scrive: checkpoint CP-YYYYMMDD-NNN + aggiorna STATO-EMPIRE
├─ Se findings critici: cto-conductor scala al CEO con il report
└─ Output: security-report + checkpoint
```

---

## Gate del workflow

| Gate | Posizione | Tipo | Condizione per passare |
|---|---|---|---|
| Scope gate | Step 1 | Bloccante | Scope definito prima di avviare le scansioni |
| Critico immediato | Step 2-5 | Bloccante | Qualsiasi finding critico → blocca il sistema impattato + escalation |
| Remediation owner | Step 6 | Bloccante | Ogni finding ha un owner e una deadline prima di chiudere il workflow |

---

## Input del workflow

```json
{
  "tipo": "audit_full | audit_parziale | audit_focus",
  "trigger": "periodico | on_demand | post_deploy | auto_trigger",
  "scope": {
    "segreti": true,
    "dipendenze_cve": true,
    "pii_log": true,
    "injection_agenti": true,
    "integration_security": true
  },
  "sistemi_focus": ["tutti | lista-sistemi-specifici"],
  "audit_precedente_id": "AUDIT-YYYYMMDD-NNN | null"
}
```

## Output del workflow

```json
{
  "audit_id": "AUDIT-YYYYMMDD-NNN",
  "data": "YYYY-MM-DD",
  "scope": "full | parziale | focus",
  "findings_totali": 0,
  "findings_per_gravita": {
    "critico": 0,
    "alto": 0,
    "medio": 0,
    "info": 0
  },
  "findings_detail": [
    {
      "id": "FIND-NNN",
      "tipo": "segreto | cve | pii | injection | integration",
      "gravita": "critico | alto | medio | info",
      "sistema": "string",
      "descrizione": "string",
      "fix": "string",
      "owner": "FORGE | 06-PLATFORM | CTO",
      "deadline": "YYYY-MM-DD"
    }
  ],
  "remediation_plan_id": "REM-YYYYMMDD-NNN",
  "escalazione_ceo": false,
  "checkpoint": "CP-YYYYMMDD-NNN"
}
```

---

## State

Lo stato dell'audit è mantenuto in `state/security-audit-log.json`. Ogni audit ha un ID
univoco e un lifecycle: `avviato → in_scan → prioritizzato → remediation_dispatched | chiuso`.
I findings critici rimangono nello stato "aperti" finché la remediation non è verificata.

---

## Connessioni

- [[cto-security-sentinel]] · `agenti/cto-security-sentinel.md`
- [[cto-conductor]] · `agenti/cto-conductor.md`
- [[cto-memoria]] · `agenti/cto-memoria.md`
- [[cto-tech-debt-tracker]] · `agenti/cto-tech-debt-tracker.md`
- [[WF-TECH-REVIEW]] · `workflow/WF-TECH-REVIEW.md`
- [[REGOLE]] · `regole/REGOLE.md`
- [[KPI]] · `kpi/KPI.md`
- [[BP-CTO]] · `company/Board-CSuite/_BLUEPRINT/BP-CTO.md`
