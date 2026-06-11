# L2 — MONITORING-DASHBOARD (Osservabilità della Holding)

> **Ecosistema:** 09-OPERATIONS · **Coordinator:** `ops-watchdog` (health) + `ops-dashboard-builder` (vista)
> **Direttore:** `ops-director` · **Workflow L3:** `Workflow/WF-WATCH/` · `Workflow/WF-DASHBOARD/`

## Cosa fa

MONITORING-DASHBOARD rende EMPIRE OS **osservabile**: nessun processo gira al buio,
nessun guasto resta invisibile più di 15 minuti, e la Board legge lo stato della
holding **in 30 secondi** (DONE WHEN #4).

Due workflow:
1. **WF-WATCH** — health check continuo: run attive, daemon Ruflo (rischio #5 su
   Windows), token in scadenza (es. token FB outreach — blocco noto), processi zombie,
   esito sync Max↔Gael, spazio disco.
2. **WF-DASHBOARD** — la dashboard unica della holding: stato run, costi per
   ecosistema (dal ledger COST-GUARD), alert sentinels, fase roadmap. Si costruisce
   per **evoluzione di `outreach-dashboard-premium`** (Next.js, già esistente), non
   da zero — il codice lo scrive PLATFORM, i requisiti e i dati li dà questo reparto.

## Come si collega

| Con chi | Direzione | Cosa passa |
|---|---|---|
| TUTTI i reparti OPERATIONS | inbound | heartbeat, esiti run, eventi ledger, esiti backup |
| TUTTI gli ecosistemi | inbound/outbound | health dei loro processi; alert quando qualcosa muore |
| Board (L0) | outbound | dashboard + report settimanale (costi, run, incidenti) |
| PLATFORM | outbound | richieste di implementazione dashboard (OPERATIONS specifica, PLATFORM codifica) |
| INTELLIGENCE | outbound | incidenti e post-mortem → wiki + ReasoningBank (si impara dai guasti) |
| Sentinels LX | bidirezionale | gli alert delle 5 sentinelle confluiscono nella dashboard |
| 10-MEMORY | outbound | incidenti rilevanti → CP; cambi di soglie/SLA → ADR |

## 🧠 Come si ATTIVA e RAGIONA

**Attivazione.** WF-WATCH è **always-on a polling** (cron fitto via SCHEDULING, es.
ogni 10-15 min) + ricezione passiva di heartbeat in mesh. WF-DASHBOARD si aggiorna a
ogni evento e genera il report Board su cron settimanale.

**Ragionamento del watchdog (`ops-watchdog`):**
1. Per ogni processo censito nel runbook registry: atteso vivo? → verifica reale
   (processo, file di log recente, esito ultimo run). **Lo stato si legge dal
   filesystem/processi, mai dichiarato** (pattern catalog_status di Empire Studio).
2. Anomalia → classifica: (a) run fallita → retry policy del runbook; (b) daemon giù
   → bootstrap auto-riparante, se fallisce → fallback bash + alert; (c) token in
   scadenza/scaduto → alert al proprietario PRIMA che il flusso fallisca (lezione
   imparata: il token FB è scaduto silenziosamente); (d) zombie → kill + log.
3. Ogni rilevazione ha SLA: run fallita scoperta entro ≤15 min (KPI di ecosistema).
4. Tre guasti uguali in 7 giorni → non è più un incidente, è un pattern: handoff a
   INTELLIGENCE (ReasoningBank) + proposta di fix strutturale a ops-director.

**Ragionamento del dashboard-builder (`ops-dashboard-builder`):**
1. Una sola domanda guida ogni widget: "la Board capisce in 30 secondi?" — semaforo
   per ecosistema, costi vs budget, ultime run, alert aperti. Niente vanity metrics.
2. Dati SOLO da fonti canoniche: ledger (`operations/cost`), schedule
   (`operations/schedule`), health (`operations/health`). Mai numeri calcolati a mano.
3. Nuovo widget = nuova spec a PLATFORM via handoff (con acceptance criteria),
   non codice scritto qui.

**Principio:** ciò che non si vede non si gestisce; ciò che si vede male si gestisce peggio.

*Fonte: dossier 06 §09 L2 MONITORING & DASHBOARD · Aggiornato: 2026-06-11*
