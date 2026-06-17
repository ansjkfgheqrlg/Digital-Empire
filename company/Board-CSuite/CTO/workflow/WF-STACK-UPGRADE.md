---
Type: CONCEPT
Status: Active
Tags: #workflow #cto #stack #upgrade #dry-run #rollout #cf-grade
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-STACK-UPGRADE — Workflow Upgrade dello Stack Tecnologico

> **Tipo:** CF-grade · **Figura:** CTO
> **Blueprint:** `company/Board-CSuite/_BLUEPRINT/BP-CTO.md`
> **Connessioni:** [[WF-TECH-REVIEW]] · [[cto-stack-radar]] · [[cto-platform-liaison]] · [[KPI]]

---

## Scopo

Portare un aggiornamento dello stack tecnologico (Next.js, Tailwind, Vercel, Ruflo, o qualsiasi
dipendenza censita nel radar) attraverso un ciclo controllato: valutazione → proposta → dry-run
in staging → gate di qualità → rollout in produzione. Garantisce che nessun upgrade entri in
produzione senza aver superato un ciclo completo di test, evitando regressioni e downtime.

---

## Trigger

- `cto-stack-radar` rileva una nuova versione major o una patch di sicurezza.
- `cto-architecture-warden` segnala che un blueprint richiede una versione più recente di
  una tecnologia attualmente nel radar.
- CEO o altro membro Board segnala che un competitor usa una capacità tecnica non disponibile
  nello stack corrente (via escalation al CTO).
- CVE critica identificata nel WF-SECURITY-AUDIT che richiede un upgrade di dipendenza.

---

## Agenti coinvolti

| Agente | Fase | Ruolo nel workflow |
|---|---|---|
| `cto-memoria` | 1, 8 | RECALL stato stack corrente; write ADR upgrade e checkpoint |
| `cto-conductor` | 1-8 | Orchestratore; approva l'upgrade; decide il go/no-go rollout |
| `cto-stack-radar` | 2 | Analisi upgrade: breaking changes, impatto sistemi, proposta |
| `cto-architecture-warden` | 3 | Verifica impatto architetturale: il blueprint regge con la nuova versione? |
| `cto-integration-architect` | 3 | Verifica impatto sulle integrazioni esistenti (API changes, breaking) |
| `cto-security-sentinel` | 4 | Security gate sull'upgrade: la nuova versione non introduce CVE? |
| `cto-quality-gate` | 5, 6 | Verifica in staging; verifica in produzione post-rollout |
| `cto-tech-debt-tracker` | 5 | Registra eventuali breaking changes non risolti come debito tecnico |
| `cto-platform-liaison` | 6, 7 | Esegue l'upgrade in staging e poi in produzione via 06-PLATFORM |
| `cto-forge-liaison` | 3 | Verifica impatto su artefatti FORGE che usano la tecnologia |

---

## Flusso passo-passo

```
STEP 1 — RICEZIONE E RECALL
├─ cto-memoria carica: versione corrente dello stack, ADR tecnici relativi alla tecnologia,
│   deploy in corso (un upgrade non parte se c'è un deploy critico in staging)
├─ cto-conductor riceve la proposta di upgrade dal radar
├─ Verifica prerequisiti: nessun deploy critico in corso; ambiente staging disponibile
└─ Output: brief contesto stack + go/no-go per avvio del ciclo

STEP 2 — ANALISI RADAR (cto-stack-radar)
├─ Produce il documento di valutazione upgrade:
│    Versione attuale → versione candidata: tipo (major/minor/patch)
│    Breaking changes: lista completa con sistemi impattati
│    Deprecazioni rilevanti: cosa smette di funzionare e quando
│    Nuove funzionalità: cosa si guadagna
│    Stima tempo migrazione: per i breaking changes identificati
│    Proposta: upgrade_si | upgrade_no | rimanda (con motivazione)
└─ Output: upgrade-assessment JSON (vedi schema stack-radar)

STEP 3 — IMPATTO ARCHITETTURALE E INTEGRAZIONI (in parallelo)
├─ cto-architecture-warden: i blueprint approvati reggono con la nuova versione?
│    Se no → produce delta tecnici; l'upgrade è condizionato alla risoluzione dei delta
├─ cto-integration-architect: le integrazioni esistenti (Ruflo, MCP, API esterne) reggono?
│    Se no → produce piano di aggiornamento contratti I/O
├─ cto-forge-liaison: gli artefatti FORGE che usano la tecnologia reggono?
│    Lista artefatti impattati con stima di aggiornamento
└─ Output: impact-assessment combinato (architettura + integrazioni + forge)

STEP 4 — GATE SICUREZZA UPGRADE
├─ cto-security-sentinel verifica che la versione candidata:
│    Non introduca CVE nuove (o che le CVE risolte > CVE introdotte)
│    Non cambi il comportamento di sicurezza in modo non previsto
│    Non richieda nuove dipendenze con licenze incompatibili
└─ Output: security_gate upgrade: "pass | blocked | warning"

STEP 5 — DRY-RUN IN STAGING
├─ cto-platform-liaison coordina con 06-PLATFORM: upgrade in ambiente staging
├─ cto-quality-gate esegue empire-verify completo in staging con la nuova versione:
│    lint → build → playwright E2E → Lighthouse → brand gate → struttura → dry-run
├─ Se quality gate BLOCKED: cto-tech-debt-tracker registra i breaking changes come debito
│   Il conductor decide: risolvi subito (bloccante) o schedula (non bloccante)
├─ Se quality gate PASS: si procede al go/no-go rollout
└─ Output: staging-test-results + lista item debito tecnico generati dall'upgrade

STEP 6 — DECISIONE ROLLOUT (conductor)
├─ cto-conductor integra: radar assessment + impact architetturale + security gate + staging test
├─ Decisione: go_rollout | no_rollout | go_rollout_condizionato (fix prima del rollout)
├─ Se go_rollout_condizionato: identifica fix bloccanti con owner e deadline
│   Il rollout non parte finché i fix bloccanti non sono risolti e verificati
└─ Output: decisione rollout + rationale + eventuali fix bloccanti

STEP 7 — ROLLOUT IN PRODUZIONE
├─ cto-platform-liaison dispatcha handoff a 06-PLATFORM per upgrade in produzione
├─ HC contiene: versione da deployare, sistemi impattati, window di manutenzione, rollback plan
├─ Rollback plan OBBLIGATORIO: se il rollout fallisce, come si torna alla versione precedente?
├─ Post-rollout: cto-quality-gate esegue spot-check (Lighthouse, E2E subset) in produzione
└─ Output: deploy_status + post-rollout spot-check results

STEP 8 — CHIUSURA E MEMORIA
├─ cto-stack-radar aggiorna state/stack-current.json con la nuova versione
├─ cto-memoria scrive ADR tecnico: "ADR-NNN — [tecnologia] aggiornata da vX a vY"
├─ cto-memoria scrive checkpoint CP-YYYYMMDD-NNN
├─ Se debito tecnico generato: cto-tech-debt-tracker aggiorna il registro
└─ Output: ADR prodotto + checkpoint + stack-current.json aggiornato
```

---

## Gate del workflow

| Gate | Posizione | Tipo | Condizione per passare |
|---|---|---|---|
| Prerequisiti gate | Step 1 | Bloccante | Nessun deploy critico in corso; staging disponibile |
| Radar proposta gate | Step 2 | Bloccante | stack-radar produce proposta (upgrade_si / no / rimanda) |
| Architettura gate | Step 3 | Bloccante | Warden + integration-architect approvano l'impatto |
| Security upgrade gate | Step 4 | Bloccante | Versione candidata non introduce CVE critiche |
| Staging quality gate | Step 5 | Bloccante | empire-verify PASS in staging |
| Conductor go/no-go | Step 6 | Bloccante | Conductor approva il rollout (con o senza condizioni) |
| Rollback plan gate | Step 7 | Bloccante | Rollback plan documentato prima del deploy in produzione |

---

## Input del workflow

```json
{
  "tecnologia": "Next.js | Tailwind | Vercel | Ruflo | dipendenza-specifica",
  "versione_attuale": "semver",
  "versione_candidata": "semver",
  "trigger": "radar | blueprint | security_patch | ceo_request",
  "urgenza": "critica (CVE) | alta | media | bassa",
  "sistemi_potenzialmente_impattati": ["lista"]
}
```

## Output del workflow

```json
{
  "upgrade_id": "UPGRADE-YYYYMMDD-NNN",
  "tecnologia": "Next.js",
  "da_versione": "14.2.5",
  "a_versione": "15.0.0",
  "esito": "rollout_completato | bloccato | rimandato",
  "security_gate": "pass | blocked",
  "staging_quality_gate": "pass | blocked",
  "breaking_changes_risolti": 0,
  "debito_tecnico_generato": 0,
  "rollback_plan": "Revert a Next.js 14.2.5 via Vercel deployment history",
  "adr_prodotto": "ADR-NNN",
  "checkpoint": "CP-YYYYMMDD-NNN",
  "stack_current_aggiornato": true
}
```

---

## State

Lo stato dell'upgrade è mantenuto in `state/stack-upgrades-log.json`. Lifecycle:
`proposto → analisi → staging → go/no-go → rollout → completato | bloccato`.
Gli upgrade bloccati rimangono nel log con il motivo del blocco fino a risoluzione o ritiro.

---

## Connessioni

- [[cto-stack-radar]] · `agenti/cto-stack-radar.md`
- [[cto-conductor]] · `agenti/cto-conductor.md`
- [[cto-quality-gate]] · `agenti/cto-quality-gate.md`
- [[cto-security-sentinel]] · `agenti/cto-security-sentinel.md`
- [[cto-platform-liaison]] · `agenti/cto-platform-liaison.md`
- [[cto-architecture-warden]] · `agenti/cto-architecture-warden.md`
- [[cto-memoria]] · `agenti/cto-memoria.md`
- [[WF-TECH-REVIEW]] · `workflow/WF-TECH-REVIEW.md`
- [[WF-SECURITY-AUDIT]] · `workflow/WF-SECURITY-AUDIT.md`
- [[KPI]] · `kpi/KPI.md`
- [[BP-CTO]] · `company/Board-CSuite/_BLUEPRINT/BP-CTO.md`
