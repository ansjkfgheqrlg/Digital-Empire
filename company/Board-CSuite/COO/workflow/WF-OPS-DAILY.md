---
Type: CONCEPT
Status: Active
Tags: #workflow #coo #daily #health-check #report #backbone #runtime
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-OPS-DAILY — Health Check Operativo Giornaliero

> **ID workflow:** WF-COO-01 · **Owner:** coo-conductor
> **Trigger:** apertura sessione (giornaliero) + on-demand
> **Durata attesa:** ≤5 minuti per il ciclo completo; report CEO in ≤30 secondi di lettura
> **Blueprint di riferimento:** `company/Board-CSuite/_BLUEPRINT/BP-COO.md`

---

## Scopo

Garantire che ogni sessione di lavoro parta con una fotografia accurata dello stato operativo
della holding: backbone sano? Sync Max↔Gael ok? Run schedulate partite? SLA a rischio?
Il workflow produce un report strutturato per il CEO (HC-COO-CEO-01) e aggiorna lo stato
operativo in AgentDB `board/coo/stato-operativo`. È il "pulse check" della macchina.

---

## Agenti coinvolti

| Agente | Ruolo nel workflow | Parallelo / Sequenziale |
|---|---|---|
| `coo-memoria` | carica contesto: STATO-EMPIRE + incidenti aperti + checkpoint | primo (sequenziale) |
| `coo-backbone-health` | verifica BUS/BRAIN/Governance/Observability/Coordination/Identity-HR | parallelo (passo 2) |
| `coo-sync-keeper` | check sync Max↔Gael, flag COORDINAMENTO, conflitti | parallelo (passo 2) |
| `coo-runtime-marshal` | swarm attivi, cron schedulati, zombie scan, budget-guard | parallelo (passo 2) |
| `coo-sla-tracker` | SLA in scadenza 24h, breach, trend ritardi | parallelo (passo 2) |
| `coo-cadence-keeper` | standup di oggi completata? Review settimanale/mensile in scadenza? | parallelo (passo 2) |
| `coo-incident-handler` | triage se ci sono anomalie (si attiva solo se stato ≠ verde) | condizionale (passo 3) |
| `coo-conductor` | aggrega, decide, produce report CEO, scrive checkpoint | finale (passo 4-5) |

---

## Flusso passo-passo

### Passo 1 — Carica contesto (sequenziale, pre-requisito)
**Agente:** `coo-memoria`

Legge `company/Memory/STATO-EMPIRE.md` e il namespace `board/coo/incidenti-aperti`.
Verifica se esiste un flag `⚠️ COORDINAMENTO` attivo (ADR-004 — se sì, area bloccata comunicata al conductor).
Carica il contesto per tutti gli agenti: incidenti aperti, pattern noti, false positive.

**Output:** `contesto_sessione` (incidenti aperti, flag coordinamento, pattern bank rilevanti)

**Gate:** se BRAIN (AgentDB) non è disponibile → coo-backbone-health parte da analisi BRAIN offline;
il conductor nota il gap e procede con dati parziali (non si blocca).

---

### Passo 2 — Monitor paralleli (5 agenti in parallelo)
**Agenti:** `coo-backbone-health` · `coo-sync-keeper` · `coo-runtime-marshal` · `coo-sla-tracker` · `coo-cadence-keeper`

Tutti i monitor partono simultaneamente con il contesto caricato al passo 1.
Ogni monitor produce il suo report strutturato in formato JSON (vedere schede agente).
Timeout per ciascun monitor: 90 secondi. Se un monitor non risponde entro il timeout →
il conductor lo marca come "timeout" e continua con dati parziali (il timeout è esso stesso
un'anomalia che va nel report).

**Output (per ogni monitor):**
- `coo-backbone-health` → stato per componente + anomalie rilevate
- `coo-sync-keeper` → sync status + conflitti + flag coordinamento
- `coo-runtime-marshal` → swarm attivi + cron + zombie + budget status
- `coo-sla-tracker` → SLA in scadenza + breach + trend
- `coo-cadence-keeper` → cadenza completata? Milestone in scadenza?

---

### Passo 3 — Triage condizionale (solo se stato ≠ verde)
**Agente:** `coo-incident-handler`

**Condizione:** almeno un monitor ha restituito stato giallo o rosso.
Se tutti i monitor sono verdi → passo 3 saltato, si va direttamente al passo 4.

Il conductor passa a coo-incident-handler le anomalie rilevate. L'incident-handler:
- Verifica se le anomalie già hanno un INC aperto (in tal caso: aggiorna lo stato).
- Per le nuove anomalie: apre INC, esegue il triage (impatto / causa / contromisura).
- Propone: risolvo in autonomia (e stima ETA) OPPURE escalation (a chi, con quale motivazione).

**Output:** lista INC (nuovi + aggiornati), azioni immediate avviate, decisioni di escalation

---

### Passo 4 — Aggregazione e report CEO (sequenziale)
**Agente:** `coo-conductor`

Aggrega tutti i report del passo 2 e l'esito del passo 3. Produce:
1. **Semaforo aggregato** (verde/giallo/rosso): la regola è il colore più critico tra tutti i monitor.
2. **Report CEO** (HC-COO-CEO-01): ≤5 righe di testo + JSON strutturato. Contiene: colore, dettaglio
   per area, blocchi attivi con owner e ETA, azioni avviate, escalation eventuale.
3. **Agenda standup** (se coo-cadence-keeper ha confermato che è il momento): template con
   i dati già popolati dai monitor.

**Format report CEO:**
```
STATO: GIALLO
BACKBONE: verde | SYNC: ok | RUNTIME: 3 run attive 0 zombie | SLA: 1 a rischio (01-AGENCY) | CADENZA: ok

BLOCCHI ATTIVI:
- SLA-AGENCY-CF-001: delivery cliente X scade tra 33h. Owner: coo-sla-tracker. ETA: verifica con 01-AGENCY entro sessione.

AZIONI AVVIATE: [1] coo-sla-tracker notifica 01-AGENCY per status update.
ESCALATION: nessuna richiesta.
```

---

### Passo 5 — Checkpoint e aggiornamento stato (sequenziale, finale)
**Agente:** `coo-conductor` (triggera `coo-memoria`)

Indipendentemente dal colore dello stato:
- `coo-memoria` scrive checkpoint in `company/Memory/checkpoints/CP-YYYYMMDD-NNN.md`.
- `coo-memoria` aggiorna `company/Memory/STATO-EMPIRE.md` sezione "Lavori in corso".
- `coo-conductor` aggiorna `board/coo/stato-operativo` in AgentDB.
- `coo-cadence-keeper` registra la standup come completata nel cadence log.

---

## State del workflow

| Campo | Valore atteso |
|---|---|
| `stato` | `running | completed | paused` |
| `passo_corrente` | `1-contesto | 2-monitor | 3-triage | 4-report | 5-checkpoint` |
| `stato_aggregato` | `verde | giallo | rosso | parziale` |
| `report_ceo_inviato` | `true | false` |
| `checkpoint_scritto` | `true | false` |
| `escalation_attive` | `[]` o lista con `{destinatario, motivo}` |

---

## Gate di completamento

Il workflow è **COMPLETATO** quando:
- [ ] Tutti i monitor hanno restituito output (o sono stati marcati timeout).
- [ ] Triage completato se stato ≠ verde.
- [ ] Report CEO compilato e pronto per invio (HC-COO-CEO-01).
- [ ] Checkpoint scritto in Memory/.
- [ ] STATO-EMPIRE aggiornato.

Il workflow è **FALLITO** (anomalia nel workflow stesso) quando:
- Il conductor non riesce ad aggregare i report dopo 3 minuti.
- Il checkpoint non può essere scritto (BRAIN down o Memory/ non accessibile).
→ In entrambi i casi: alert manuale a Max/Gael.

---

## Connessioni

- [[coo-conductor]] · `agenti/coo-conductor.md`
- [[coo-backbone-health]] · `agenti/coo-backbone-health.md`
- [[coo-sync-keeper]] · `agenti/coo-sync-keeper.md`
- [[coo-runtime-marshal]] · `agenti/coo-runtime-marshal.md`
- [[coo-sla-tracker]] · `agenti/coo-sla-tracker.md`
- [[coo-cadence-keeper]] · `agenti/coo-cadence-keeper.md`
- [[coo-incident-handler]] · `agenti/coo-incident-handler.md`
- [[coo-memoria]] · `agenti/coo-memoria.md`
- [[WF-INCIDENT]] · `workflow/WF-INCIDENT.md`
- [[BP-COO]] · `company/Board-CSuite/_BLUEPRINT/BP-COO.md`
- [[STATO-EMPIRE]] · `company/Memory/STATO-EMPIRE.md`
