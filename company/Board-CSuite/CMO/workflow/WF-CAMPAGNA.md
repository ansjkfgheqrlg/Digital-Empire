---
Type: WORKFLOW
Status: Active
Tags: #workflow #cmo #campagna #apsoc #multi-canale #brand-gate
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-CAMPAGNA — Workflow Campagna Multi-Canale

> **ID:** WF-CMO-001 · **Owner:** cmo-conductor · **Trigger:** richiesta campagna da CEO o Board
> **Blueprint:** `company/Board-CSuite/_BLUEPRINT/BP-CMO.md`
> **Standard:** CF-grade — ogni nodo ha owner, I/O, gate, state.

---

## Scopo

Portare un obiettivo di business (lead, vendita, awareness) a un lancio di campagna verificato,
con gate APSOC+brand integrato e approvazione umana obbligatoria su ogni spesa. Nessun output
di campagna esce dalla holding senza aver attraversato questo workflow o WF-BRAND-GATE.

---

## Pre-condizioni (INPUT obbligatori)

Prima che WF-CAMPAGNA possa partire, devono essere dichiarati:
- `obiettivo` — lead | vendita | awareness | retention
- `prodotto` — quale prodotto DE è il focus
- `brand_kit` — DE | cliente-X (obbligatorio, Mandato Art.6.1)
- `icp_id` — profilo ICP attivo o ID da `cmo-memoria`
- `budget_envelope` — budget approvato o [DM]
- `deadline` — data target di lancio campagna

Un brief senza questi 6 campi viene rimandato al richiedente prima di avviare il workflow.

---

## Flusso

```
[STEP 1 — INTAKE]
  Owner: cmo-conductor
  Input: brief da CEO/Board
  Action: valida pre-condizioni, classifica (campagna nuova | ottimizzazione | lancio)
  Output: task_id + assegnazioni agenti
  Gate: pre-condizioni complete? NO → rimanda al richiedente

[STEP 2 — ICP + AWARENESS]
  Owner: cmo-audience-intel
  Input: icp_id, prodotto, segnali da 08-INTELLIGENCE
  Action: profila l'ICP per questa campagna specifica; identifica awareness level predominante
  Output: ICP brief (pain points, awareness level, obiezioni, trigger conversione)
  Gate: ICP ha awareness level dichiarato? NO → [DM] esplicito + segnalazione gap intelligence

[STEP 3 — STRATEGIA]
  Owner: cmo-campaign-strategist
  Input: obiettivo, ICP brief, budget_envelope, canali disponibili
  Action: produce strategia multi-canale (canali, timing, struttura APSOC per canale, KPI)
  Output: strategia_id + dry-run budget (stima, non spesa)
  Gate: dry-run budget presentato al conductor → OK UMANO su spesa prima di procedere

[STEP 4 — ARCHITETTURA FUNNEL]
  Owner: cmo-funnel-architect
  Input: strategia_id, ICP brief
  Action: progetta/aggiorna il funnel per questa campagna (fasi, touch-point, metriche per nodo)
  Output: funnel_id con APSOC mapping per nodo
  Gate: ogni nodo ha owner e metrica dichiarata? (o [DM] esplicito)

[STEP 5 — BRIEF AI LIAISON]
  Owner: cmo-conductor (coordina)
  Sub-step A — cmo-marketing-liaison: brief copy a 04-MARKETING
  Sub-step B — cmo-content-liaison: brief asset a 03-CONTENT-FACTORY
  Action: handoff simultaneo con SLA dichiarata per ogni deliverable
  Gate: brief completo (brand_kit, icp, awareness, formato, deadline)?

[STEP 6 — PRODUZIONE]
  Owner: 04-MARKETING (copy) + 03-CONTENT-FACTORY (asset)
  Timing: entro SLA dichiarata nel brief
  Monitoring: liaison check al 50% del tempo (non aspettare la scadenza)

[STEP 7 — GATE BRAND+APSOC]
  Owner: cmo-brand-voice-warden (ALWAYS-ON)
  Input: ogni output di copy/asset dal passo 6
  Action: score APSOC + Brand Gate G2 (voce, prove, pricing, anti-slop)
  Output: PASS (score ≥80 standard, ≥85 sales page) | FAIL con feedback granulare
  Gate BLOCCANTE: FAIL → torna a STEP 6 con brief di fix specifico. Nessun bypass.

[STEP 8 — LAUNCH]
  Owner: cmo-conductor
  Pre-condition: tutti gli output a PASS, dry-run completato, ok umano su spesa
  Action: attiva i canali nella sequenza definita dalla strategia
  Output: campagna live + timestamp di attivazione per ogni canale

[STEP 9 — MONITORAGGIO]
  Owner: cmo-performance-analyst
  Timing: real-time prime 48h, poi report settimanale
  Action: raccoglie metriche, diagnostica APSOC, segnala anomalie
  Output: report performance + brief ottimizzazione se necessario
  Trigger: se metrica critica sotto target → alert al conductor → ottimizzazione (ritorna a STEP 6)
```

---

## State (namespace AgentDB)

```
board/cmo/campagne/<campaign-id>/
  ├── brief.json            — input iniziale
  ├── strategia.json        — output STEP 3
  ├── funnel.json           — output STEP 4
  ├── brief-liaison/        — brief per 04-MARKETING e 03-CONTENT-FACTORY
  ├── assets/               — asset prodotti e gate log per ogni asset
  ├── gate-log.json         — ogni check APSOC con score e esito
  ├── launch-log.json       — timestamp attivazione canali
  └── performance/          — report periodici
```

---

## Gate non bypassabili

1. **Dry-run budget** (STEP 3) — nessuna spesa senza stima preventiva e ok umano.
2. **Brand Gate APSOC** (STEP 7) — nessun output di conversione esce con score <80 (o <85 su sales page).
3. **Pre-condizioni brief** (STEP 1) — brand_kit + icp obbligatori, nessuna eccezione.

---

## Connessioni

- [[cmo-conductor]] · `agenti/cmo-conductor.md`
- [[cmo-brand-voice-warden]] · `agenti/cmo-brand-voice-warden.md`
- [[cmo-campaign-strategist]] · `agenti/cmo-campaign-strategist.md`
- [[cmo-audience-intel]] · `agenti/cmo-audience-intel.md`
- [[cmo-funnel-architect]] · `agenti/cmo-funnel-architect.md`
- [[cmo-marketing-liaison]] · `agenti/cmo-marketing-liaison.md`
- [[cmo-content-liaison]] · `agenti/cmo-content-liaison.md`
- [[cmo-performance-analyst]] · `agenti/cmo-performance-analyst.md`
- [[WF-BRAND-GATE]] · `workflow/WF-BRAND-GATE.md`
- [[MANDATO-EMPIRE]] Art.2 + Art.4 + Art.6
