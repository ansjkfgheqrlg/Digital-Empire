> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 09 §3 L3 WF-DASHBOARD

# L3 — WF-DASHBOARD (Dashboard Unica della Holding per la Board)

**Ecosistema:** 09-OPERATIONS · **Reparto L2:** MONITORING-DASHBOARD
**Coordinator:** `ops-dashboard-builder` · **Direttore:** `ops-director`
**Connessione:** [[ECOSISTEMA.md]] · [[BACKBONE.md]]

## Missione

WF-DASHBOARD è la vista unica della holding: la Board legge lo stato di EMPIRE OS
in 30 secondi (DONE WHEN #4). Si costruisce per evoluzione di `outreach-dashboard-premium`
(Next.js, già esistente in `Outreach/outreach-dashboard-premium/`) — non da zero.
OPERATIONS specifica i requisiti e i dati; PLATFORM scrive il codice.

## Principio guida

Una sola domanda guida ogni widget: "la Board capisce in 30 secondi?"
- Semaforo per ecosistema (verde/giallo/rosso)
- Costi vs budget (barra progresso)
- Ultime run (stato, esito, costo)
- Alert aperti (numero + gravità)

**Nessuna vanity metric.** Dati SOLO da fonti canoniche: ledger (`operations/cost`),
schedule (`operations/schedule`), health (`operations/health`). Mai numeri calcolati
a mano o dichiarati senza fonte.

## Widget della dashboard (spec per PLATFORM)

| Widget | Dati sorgente | Refresh |
|---|---|---|
| Semaforo ecosistemi (10 bollini) | `operations/health` | ogni 15 min |
| Costo settimana per ecosistema | `operations/ledger` | ogni ora |
| Budget residuo mese | `operations/ledger` | ogni ora |
| Ultime 10 run (stato, durata, costo) | `operations/schedule` | ogni 15 min |
| Alert aperti (gravità, processo) | `operations/health` | real-time |
| Fase roadmap corrente | `company/Memory/STATO-EMPIRE.md` | manuale (cambio fase) |
| Quota Haiku/Sonnet/Opus settimana | `operations/tier-stats` | ogni ora |

## Processo decisionale (`ops-dashboard-builder`)

1. Non scrive codice: specifica ogni nuovo widget con handoff a PLATFORM
   (`{acceptance_criteria, sorgente dati, refresh rate, mockup}`) e attende implementazione.
2. Valida ogni widget: "i dati vengono da fonte canonica?" Sì → ok. No → corregge
   la sorgente, non abbandona la regola.
3. Nuovo widget proposto senza spec: viene rifiutato (no widget senza acceptance_criteria).
4. Ogni settimana: genera il report Board come documento testuale (PDF o MD) da
   ops-cost-accountant + invia via Bus al CFO.

## Evoluzione da outreach-dashboard-premium

**Fase attuale:** la dashboard monitora solo l'outreach (3 canali, run status, token).
**Target OPERATIONS O5:** dashboard monitoring holding intera con tutti i widget sopra.

**Piano di evoluzione (non rompe mai il funzionamento attuale):**
1. Mantiene le sezioni outreach esistenti intatte (ADR-003: wrap, mai riscrittura).
2. Aggiunge nuove sezioni in tab separati (costi ecosistema, roadmap, alert generali).
3. Ogni tab = una spec a PLATFORM = un handoff.

## Gate di qualità

- `G-CANONICAL-SOURCE` — tutti i widget attingono da fonti canoniche in AgentDB
- `G-30S-READ` — review mensile: la Board capisce in 30s? Se no → semplifica
- `G-SPEC-FIRST` — nessun widget senza spec scritta e handoff formale a PLATFORM

## KPI

| Metrica | Target |
|---|---|
| Uptime dashboard | ≥ 99% ore lavoro |
| Report Board settimanale inviato | 100% lunedì mattina |
| Widget con dati da fonte non canonica | 0 |
| Tempo "stato holding in 30s" (test con Board) | ≤ 30s |
