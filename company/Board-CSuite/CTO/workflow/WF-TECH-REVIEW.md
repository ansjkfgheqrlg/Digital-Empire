---
Type: CONCEPT
Status: Active
Tags: #workflow #cto #tech-review #architettura #security #quality #cf-grade
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-TECH-REVIEW — Workflow Revisione Tecnica

> **Tipo:** CF-grade · **Figura:** CTO
> **Blueprint:** `company/Board-CSuite/_BLUEPRINT/BP-CTO.md`
> **Connessioni:** [[WF-SECURITY-AUDIT]] · [[WF-STACK-UPGRADE]] · [[cto-conductor]] · [[14-DOSSIER-ARCHITETTURA]]

---

## Scopo

Portare qualsiasi proposta tecnica (nuova feature, nuovo sistema, modifica architetturale,
richiesta di integrazione) attraverso un ciclo strutturato: validazione architetturale →
gate di sicurezza → gate di qualità → decisione tecnica → dispatch deploy o handoff FORGE.
Questo è il workflow principale della figura CTO: ogni build significativa passa qui.

---

## Trigger

- Richiesta di deploy da qualsiasi ecosistema o figura Board.
- Nuovo blueprint prodotto dall'organo ARCHITETTURA.
- Richiesta di nuovo artefatto a FORGE da parte di un ecosistema.
- Nuova integrazione richiesta (backbone/Ruflo/MCP/API esterna).
- Modifica allo stack corrente proposta da qualsiasi sorgente.
- Alert da `cto-security-sentinel` su un sistema in staging.

---

## Agenti coinvolti

| Agente | Fase | Ruolo nel workflow |
|---|---|---|
| `cto-memoria` | 1, 10 | RECALL in apertura; write checkpoint in chiusura |
| `cto-conductor` | 1-10 | Orchestratore; produce la decisione tecnica finale |
| `cto-architecture-warden` | 2 | Valida allineamento con blueprints e ADR tecnici |
| `cto-integration-architect` | 3 | Valuta nuove integrazioni o impatti su integrazioni esistenti |
| `cto-stack-radar` | 3 | Verifica tecnologie richieste nel radar |
| `cto-forge-liaison` | 4 | Se la proposta richiede un nuovo artefatto FORGE |
| `cto-security-sentinel` | 5 | Gate sicurezza — BLOCCANTE (always-on) |
| `cto-quality-gate` | 6 | Gate qualità — BLOCCANTE (empire-verify + Lighthouse) |
| `cto-tech-debt-tracker` | 7 | Registra ogni problem non risolto come item debito |
| `cto-platform-liaison` | 8 | Dispatch del deploy a 06-PLATFORM se approvato |

---

## Flusso passo-passo

```
STEP 1 — RICEZIONE E RECALL
├─ cto-memoria carica: ADR tecnici attivi, debito tecnico corrente, stato ambienti
├─ cto-conductor riceve la proposta tecnica strutturata (JSON input)
├─ Dedup check: questa proposta è già coperta da un ADR? Sì → applica ADR, stop
└─ Output: brief di contesto + classificazione tipo (architettura / deploy / integrazione / forge)

STEP 2 — VALIDAZIONE ARCHITETTURALE
├─ cto-architecture-warden riceve la proposta
├─ Verifica: coerenza con ADR tecnici attivi
├─ Verifica: stack richiesto nel radar (altrimenti → alert a cto-stack-radar)
├─ Verifica: principio wrap-first (esiste già qualcosa che risolve il problema?)
├─ Esito: approvato | rimandato (con delta) | approvato_con_delta
└─ Output: esito architetturale con delta tecnici se necessari

STEP 3 — ANALISI INTEGRAZIONI E STACK (se applicabile, in parallelo)
├─ cto-integration-architect (se la proposta tocca un'integrazione):
│    Verifica contratti I/O esistenti, assenza dipendenze circolari, fallback
├─ cto-stack-radar (se la proposta usa tecnologie fuori dal radar):
│    Valuta l'aggiunta al radar o propone alternativa nel radar
└─ Output: integration-design (se nuova integrazione) + stack-assessment

STEP 4 — BRIEF A FORGE (se applicabile)
├─ Se la proposta richiede un nuovo artefatto (skill/agente/workflow):
│    cto-forge-liaison costruisce il brief tecnico per FORGE
│    Include: schema I/O atteso, dipendenze permesse, AC, standard da rispettare
└─ Output: brief FORGE (o n/a se non necessario)

STEP 5 — GATE SICUREZZA (BLOCCANTE)
├─ cto-security-sentinel esegue scan completo sul target
├─ Segreti, PII, CVE, injection → qualsiasi finding critico = BLOCCO
├─ BLOCCO → conductor notificato; nessuno step successivo eseguito
│   Sblocco: fix verificato + eventuale ADR per il pattern
└─ Output: security_gate: "pass | blocked | warning"

STEP 6 — GATE QUALITÀ (BLOCCANTE)
├─ cto-quality-gate esegue empire-verify completo:
│    lint → build → playwright E2E → Lighthouse ≥90 → brand gate → struttura → dry-run
├─ Uno qualsiasi BLOCKED → deploy non parte
│   cto-tech-debt-tracker registra ogni problema come item debito
└─ Output: quality_gate: "pass | blocked | warning" + report dettagliato

STEP 7 — DEBITO TECNICO (se applicablie)
├─ Ogni WARNING del gate qualità → registrato in cto-tech-debt-tracker
├─ Il conductor decide: il WARNING blocca il deploy? (Se sì → risolvi prima. Se no → schedule.)
└─ Output: lista item debito creati (se presenti)

STEP 8 — DECISIONE TECNICA FINALE
├─ cto-conductor integra: architettura + integrazione + stack + sicurezza + qualità
├─ Se tutti i gate sono PASS: decisione = approvato per il deploy / per il catalogo
├─ Se qualche gate è BLOCKED: decisione = bloccato; produce lista fix con owner e deadline
├─ Se qualche gate è WARNING: decisione rimessa al conductor (caso per caso)
└─ Output: decisione_tecnica JSON (vedi schema output conductor)

STEP 9 — DISPATCH
├─ Deploy approvato: cto-platform-liaison costruisce handoff HC-CTO-PLT con AC e deadline
├─ Artefatto FORGE approvato: cto-forge-liaison aggiorna catalogo e notifica FORGE
├─ Se decisione architetturale: cto-memoria redige ADR draft → firma conductor
└─ Output: handoff_id + adr_id (se prodotto)

STEP 10 — CHIUSURA E MEMORIA
├─ cto-memoria scrive checkpoint CP-YYYYMMDD-NNN
├─ Aggiorna STATO-EMPIRE sezione tecnica
└─ Output: checkpoint_id + confirm
```

---

## Gate del workflow

| Gate | Posizione | Tipo | Condizione per passare |
|---|---|---|---|
| Dedup gate | Step 1 | Bloccante | Proposta non già coperta da ADR esistente |
| Architettura gate | Step 2 | Bloccante | Warden approva (o approva con delta già risolti) |
| Security gate | Step 5 | Bloccante | Nessun finding critico o alto; nessun segreto nel codice |
| Quality gate | Step 6 | Bloccante | PASS su lint, build, playwright, Lighthouse ≥90, brand, struttura, dry-run |
| Conductor gate | Step 8 | Bloccante | Conductor integra e approva la decisione tecnica |

---

## Input del workflow

```json
{
  "tipo": "tech_review | deploy_request | architecture_change | forge_request | integration_change",
  "sorgente": "CEO | CMO | COO | ARCHITETTURA | FORGE | ecosistema-id",
  "sistemi_impattati": ["lista"],
  "contesto": "Descrizione tecnica della proposta",
  "vincoli": ["wrap_non_riscrittura", "zero_segreti_git", "dry_run_first"],
  "urgenza": "alta | media | bassa",
  "blueprint_riferimento": "ARCH-BP-NNN | null"
}
```

## Output del workflow

```json
{
  "esito": "approvato | bloccato | bloccato_con_fix",
  "decisione_tecnica": "string",
  "gate_results": {
    "architettura": "approvato | rimandato",
    "security": "pass | blocked",
    "quality": "pass | blocked"
  },
  "fix_richiesti": [{"chi": "FORGE | 06-PLATFORM", "cosa": "string", "deadline": "YYYY-MM-DD"}],
  "handoff_id": "HC-CTO-PLT-YYYYMMDD-NNN | null",
  "adr_prodotto": "ADR-NNN | null",
  "checkpoint": "CP-YYYYMMDD-NNN"
}
```

---

## State

Il workflow mantiene il suo stato in `state/tech-reviews-pending.json` durante l'esecuzione.
Ogni review ha un lifecycle: `ricevuta → architettura → security → quality → decisione → dispatched | bloccata`.
Le review bloccate rimangono nel registro finché non vengono risolte o ritirate esplicitamente.

---

## Connessioni

- [[cto-conductor]] · `agenti/cto-conductor.md`
- [[cto-architecture-warden]] · `agenti/cto-architecture-warden.md`
- [[cto-security-sentinel]] · `agenti/cto-security-sentinel.md`
- [[cto-quality-gate]] · `agenti/cto-quality-gate.md`
- [[cto-platform-liaison]] · `agenti/cto-platform-liaison.md`
- [[WF-SECURITY-AUDIT]] · `workflow/WF-SECURITY-AUDIT.md`
- [[PRINCIPI]] · `principi/PRINCIPI.md`
- [[14-DOSSIER-ARCHITETTURA]] · `PIANO-MAESTRO/14-DOSSIER-ARCHITETTURA.md`
