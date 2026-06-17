---
Type: CONCEPT
Status: Active
Tags: #cto #state #namespace #memoria #agentdb
Created: 2026-06-17
Last updated: 2026-06-17
---

# STATE — Schema Stato della Figura CTO

> Connessioni: [[cto-memoria]] · [[cto-tech-debt-tracker]] · [[cto-security-sentinel]] · [[KPI]]

---

## Namespace AgentDB

Il namespace AgentDB per la figura CTO è `board/cto`. Ogni agente della figura scrive e
legge da questo namespace. La gerarchia interna del namespace rispecchia i domini tecnici.

```
board/cto/
├── sessioni/          ← log sessioni CTO con timestamp, agenti attivati, decisioni
├── adr-tecnici/       ← indice ADR tecnici attivi (mirror di Memory/decisions/ con tag #cto)
├── debito-tecnico/    ← stato corrente del register debito (sync con state/tech-debt-register.json)
├── security-log/      ← log scan security con findings e stati di remediation
├── quality-gate-log/  ← log run quality gate con esiti per sistema
├── platform-status/   ← stato ambienti (staging/prod) per ogni sistema gestito
└── stack-radar/       ← versioni correnti stack e storia upgrade
```

---

## File di Stato Locali

I file di stato locali (in `company/Board-CSuite/CTO/state/`) sono il fallback quando
AgentDB non è disponibile e la fonte primaria per la lettura rapida senza invocare MCP.

### `tech-debt-register.json`
Registro del debito tecnico. Struttura:
```json
{
  "metadata": {"ultimo_aggiornamento": "YYYY-MM-DD", "totale_aperti": 0},
  "items": [
    {
      "id": "TD-NNN",
      "descrizione": "string",
      "sistema_impattato": "string",
      "sorgente": "cto-quality-gate | cto-security-sentinel | manuale",
      "gravita": "alta | media | bassa",
      "priorita": 1,
      "blocca_deploy": false,
      "data_rilevazione": "YYYY-MM-DD",
      "stato": "aperto | in_lavorazione | risolto",
      "data_risoluzione": null,
      "riferimento_fix": null
    }
  ]
}
```

### `stack-current.json`
Versioni correnti dello stack tecnologico:
```json
{
  "metadata": {"ultimo_aggiornamento": "YYYY-MM-DD"},
  "tecnologie": [
    {
      "nome": "Next.js",
      "versione_corrente": "15.0.0",
      "versione_latest": "15.0.0",
      "ultima_verifica": "YYYY-MM-DD",
      "sistemi_che_usano": ["06-PLATFORM/siti", "06-PLATFORM/landing-pages"],
      "adr_riferimento": "ADR-012"
    },
    {
      "nome": "Tailwind",
      "versione_corrente": "4.0",
      "versione_latest": "4.0",
      "ultima_verifica": "YYYY-MM-DD",
      "sistemi_che_usano": ["06-PLATFORM/siti"],
      "adr_riferimento": null
    },
    {
      "nome": "Vercel",
      "versione_corrente": "managed",
      "versione_latest": "managed",
      "ultima_verifica": "YYYY-MM-DD",
      "sistemi_che_usano": ["06-PLATFORM"],
      "adr_riferimento": null
    },
    {
      "nome": "Ruflo (claude-flow)",
      "versione_corrente": "current",
      "versione_latest": "current",
      "ultima_verifica": "YYYY-MM-DD",
      "sistemi_che_usano": ["board/cto", "hive-mind", "agentdb"],
      "adr_riferimento": null
    }
  ]
}
```

### `architecture-registry.json`
Registro dei blueprint architetturali approvati:
```json
{
  "metadata": {"ultimo_aggiornamento": "YYYY-MM-DD"},
  "blueprints": [
    {
      "blueprint_id": "ARCH-BP-NNN",
      "titolo": "string",
      "versione": "v1.0",
      "stato": "approvato | rimandato | superato",
      "data_approvazione": "YYYY-MM-DD",
      "adr_riferimento": ["ADR-NNN"],
      "sistemi_impattati": ["lista"]
    }
  ]
}
```

### `security-audit-log.json`
Log degli audit di sicurezza:
```json
{
  "audit_recenti": [
    {
      "audit_id": "AUDIT-YYYYMMDD-NNN",
      "data": "YYYY-MM-DD",
      "tipo": "full | parziale | focus",
      "findings_critici": 0,
      "findings_alti": 0,
      "stato": "chiuso | remediation_in_corso"
    }
  ]
}
```

### `platform-status.json`
Stato degli ambienti e dei sistemi gestiti da 06-PLATFORM:
```json
{
  "sistemi": [
    {
      "id": "landing-manuale-claude-code",
      "url_staging": "https://staging.xxx.vercel.app",
      "url_prod": "https://manuale.digitalempire.io",
      "ultimo_deploy": "YYYY-MM-DD",
      "lighthouse_score_prod": 94,
      "dry_run_verified": true,
      "stato": "up | down | in_deploy"
    }
  ]
}
```

### `integration-map.json`
Mappa delle integrazioni attive tra sistemi:
```json
{
  "integrazioni": [
    {
      "id": "INT-CTO-NNN",
      "da": "board/cto",
      "a": "Ruflo-AgentDB",
      "protocollo": "MCP",
      "tool": "mcp__claude-flow__agentdb_hierarchical-store",
      "stato": "attiva | disattiva | in_build",
      "gestione_errori": "retry 3x + fallback locale",
      "adr_riferimento": null
    }
  ]
}
```

---

## Ciclo di Vita dello Stato

**Apertura sessione:** `cto-memoria` legge tutti i file di stato + AgentDB se disponibile.
Produce un brief di contesto per il conductor (5 campi chiave: debito-summary, security-status,
stack-version, ultimo-deploy, ripresa-da).

**Durante la sessione:** gli agenti aggiornano i loro file di stato in modo incrementale
(append, non overwrite). Il conductor tiene traccia delle modifiche per il checkpoint finale.

**Chiusura sessione:** `cto-memoria` scrive il checkpoint CP-YYYYMMDD-NNN, aggiorna
STATO-EMPIRE.md nella sezione tecnica, sincronizza AgentDB se disponibile.

**Amnesia test (ADR-002):** da un record in `board/cto/sessioni/<session-id>` deve essere
possibile ricostruire cosa è stato deciso e perché, senza accesso alla sessione originale.

---

## Connessioni

- [[cto-memoria]] · `agenti/cto-memoria.md`
- [[cto-tech-debt-tracker]] · `agenti/cto-tech-debt-tracker.md`
- [[cto-security-sentinel]] · `agenti/cto-security-sentinel.md`
- [[cto-stack-radar]] · `agenti/cto-stack-radar.md`
- [[KPI]] · `kpi/KPI.md`
- `company/Memory/INDEX.md`
- `company/Memory/STATO-EMPIRE.md`
- [[BP-CTO]] · `company/Board-CSuite/_BLUEPRINT/BP-CTO.md`
