# L2 — SCHEDULING (Run Ricorrenti e Loop)

> **Ecosistema:** 09-OPERATIONS · **Coordinator:** `ops-scheduler` · **Direttore:** `ops-director`
> **Workflow L3:** `Workflow/WF-CRON/` · `Workflow/WF-LOOP/`

## Cosa fa

SCHEDULING elimina il "lancio a mano": ogni flusso ricorrente della holding diventa
una **run schedulata, monitorata e con runbook**. È il reparto che porta a casa il
DONE WHEN #3 di OPERATIONS: le run outreach giornaliere (`avvia-email`, `avvia-ig`,
`avvia-parallel`) girano da sole.

Due modalità:
1. **WF-CRON** — trigger temporali: outreach giornaliero, wiki-garden settimanale
   (per INTELLIGENCE), trend-radar mensile, backup, report costi Board.
2. **WF-LOOP** — loop self-paced su condizione (skill `loop`/`schedule`): "ripeti
   finché la coda non è vuota", "controlla il deploy ogni 5 minuti".

**Vincolo ADR-003 (wrap, mai riscrittura):** gli script outreach attivi
(`run_parallel.py`, `run_ig_email.py`, `AVVIA-*.bat` — 6 team Nemotron $0/giorno)
NON si toccano. SCHEDULING li **invoca tramite le skill avvia-*** esistenti e ne
osserva l'esito. Il giorno che falliscono, l'escalation va all'umano, non si patcha.

## Come si collega

| Con chi | Direzione | Cosa passa |
|---|---|---|
| Qualsiasi ecosistema | inbound | richiesta schedule: `{workflow, cron_expr|condizione, budget_max, runbook}` |
| COST-GUARD | bidirezionale | ogni schedule ha budget per-run e mensile; sforo previsto → run sospesa |
| RUNTIME | outbound | job ricorrenti pesanti vengono delegati come batch swarm |
| MONITORING-DASHBOARD | outbound | calendario run, esiti, run saltate; il watchdog verifica che il cron VIVA |
| 01-AGENCY | servizio | è il cliente n.1: outreach 3 canali sotto WF-CRON (fase O3) |
| 10-MEMORY | outbound | esito di ogni run schedulata → CP (post-task obbligatorio) |

## 🧠 Come si ATTIVA e RAGIONA

**Attivazione.** (a) handoff di registrazione schedule (una tantum, gate G-RUNBOOK:
senza runbook+rollback non si schedula nulla); (b) trigger temporale del cron stesso;
(c) condizione di loop verificata.

**Ragionamento del coordinator (`ops-scheduler`):**
1. Al momento del trigger: verifica pre-condizioni dal runbook (token validi? daemon
   su? disco libero? — chiede a `ops-watchdog`). Pre-condizione rossa → NON lancia,
   alert al proprietario del workflow (es. token FB scaduto → run scraper sospesa).
2. Verifica budget residuo con `ops-cost-sentinel`: il budget mensile del workflow
   coprirebbe questa run? No → sospende e alert (mai "lancia e spera").
3. Lancia tramite il trigger ufficiale (skill avvia-*, script censito, o handoff a
   RUNTIME) — mai invocando internals dei sistemi wrappati.
4. Registra esito + durata + costo in `operations/schedule`; run fallita → 1 retry
   se il runbook lo permette, poi escalation.
5. Run saltata o in ritardo > finestra → segnala al watchdog (che ha il suo SLA di
   rilevazione ≤ 15 min).

**Principio:** una run che non può pagare se stessa o non sa come tornare indietro
(rollback) non parte. Lo scheduler è un portiere, non un passacarte.

*Fonte: dossier 06 §09 L2 SCHEDULING · Aggiornato: 2026-06-11*
