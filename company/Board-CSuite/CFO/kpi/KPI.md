---
Type: CONCEPT
Status: Active
Tags: #cfo #kpi #cost-guard #budget #misure
Created: 2026-06-18
Last updated: 2026-06-18
---

# KPI — Indicatori Presidiati dalla Figura CFO

> Fonte: `company/Board-CSuite/_BLUEPRINT/BP-CFO.md` §KPI
> Principio: KPI "da misurare" — nessun numero inventato (Mandato / MAXIMILIAN standard "prove non promesse")
> Connessioni: [[cfo-cost-sentinel]] · [[cfo-cost-accountant]] · [[WF-COST-REPORT]]

---

## Nota metodologica

I KPI elencati sono quelli che la figura CFO è responsabile di presidiare. I target sono dichiarati
"da misurare" [DM] finché non esistono dati reali nel ledger. Ogni KPI dichiara la fonte del dato
(dove si trova lo stato da leggere). Il CFO predica col proprio esempio: è la figura più Haiku-heavy
e a costo più basso della holding.

---

## KPI 1 — Sforamenti budget (blocco pre-sforo funziona)

**Cosa misura:** quante volte un workflow/ecosistema ha superato il budget dichiarato. L'obiettivo è
sempre 0: il blocco di `cfo-budget-guard` deve fermare la spesa PRIMA dello sforo, mai dopo.

**Come si misura:** conteggio eventi `esito = "sforo"` vs `esito = "bloccato_pre_sforo"` nel ledger
`state/ledger/eventi_YYYYMMDD.json`.

**Target:** 0 sforamenti. Ogni sforo è un'anomalia (il guard ha fallito) → post-mortem immediato.

**Frequenza:** per run; report in WF-COST-REPORT.

---

## KPI 2 — Copertura ledger (cost attribution)

**Cosa misura:** la percentuale di run/operazioni della holding che hanno un evento di costo
attribuito (agente/run/commessa/ecosistema). Una run senza evento costo è una run "invisibile".

**Come si misura:** n. run con evento nel ledger / n. run totali (da log OPERATIONS + 09-OPERATIONS).

**Target:** ≥ 98% — sotto questa soglia il controllo costi è cieco (regola G-ATTRIBUTION).

**Frequenza:** settimanale (`cost_report.py`).

---

## KPI 3 — Quota task su tier economico (WASM/Haiku)

**Cosa misura:** la percentuale di task instradati da `cfo-tier-router` sul tier economico
(WASM/Haiku) invece di Sonnet/Opus. Misura la disciplina di costo: il modello giusto per il task giusto.

**Come si misura:** n. task tier economico / n. task totali, da `state/tier-decisions/*.json`.

**Target:** ≥ 70% — la maggioranza del lavoro ripetitivo deve costare poco.

**Frequenza:** settimanale.

---

## KPI 4 — Tempestività alert 80% budget

**Cosa misura:** quanto tempestivamente `cfo-cost-sentinel` emette l'alert all'80% del budget,
prima che si arrivi al limite. Misura la prevenzione (vs reazione).

**Come si misura:** delta tra il momento del raggiungimento dell'80% e l'emissione dell'alert
(`state/alerts/*.json`). Aggregato: mediana.

**Target:** alert entro pochi minuti dall'80%; 0 sforamenti raggiunti senza alert precedente.

**Frequenza:** per evento; report settimanale.

---

## KPI 5 — Accuratezza forecast costi

**Cosa misura:** lo scostamento tra il forecast costi di `cfo-forecast-finance` e il costo reale
consuntivato. Misura quanto il CFO sa prevedere la spesa.

**Come si misura:** `|forecast - reale| / reale` per periodo, da `state/forecast/*.json` vs ledger.

**Target:** [DM] — da misurare sui primi 3 cicli; obiettivo iniziale scostamento < 20%.

**Frequenza:** per ciclo di forecast (trimestrale + revisione mensile).

---

## KPI 6 — % spese reali con ok esplicito (pattern #3)

**Cosa misura:** la percentuale di spese API/crediti reali che sono passate da `cfo-spend-approver`
con ok esplicito (mai spesa autonoma). Pattern #3 (dry-run di default).

**Come si misura:** n. spese con `approvazione = "ok_esplicito"` / n. spese reali totali.

**Target:** 100% — nessuna spesa reale autonoma. Non negoziabile.

**Frequenza:** per spesa; report settimanale.

---

## KPI 7 — ROI per ecosistema

**Cosa misura:** il rapporto tra valore prodotto e costo per ogni ecosistema (lettura di
`cfo-roi-analyst`). Indica dove la spesa rende e dove no.

**Come si misura:** valore attribuito (da CRO/output) / costo attribuito (da ledger) per ecosistema.

**Target:** [DM] — nessuna baseline storica; si stabilisce dopo 1 trimestre di ledger reale.

**Frequenza:** trimestrale (WF-COST-REPORT esteso).

---

## KPI 8 — Budget-guard 20% rispettato (ADR-006)

**Cosa misura:** quante volte una sessione di build ha aperto un nuovo lavoro sotto il 20% di
risorse residue (violazione del budget-guard). Owner: `cfo-runway-tracker`.

**Come si misura:** conteggio eventi `runway < 20% AND nuovo_build_aperto = true` nei log di sessione.

**Target:** 0 — sotto il 20% si chiude col COMMIT, non si apre nuovo (lezione CP-005).

**Frequenza:** per sessione; alert immediato se violato.

---

## Connessioni

- [[cfo-cost-sentinel]] · `agenti/cfo-cost-sentinel.md`
- [[cfo-cost-accountant]] · `agenti/cfo-cost-accountant.md`
- [[cfo-runway-tracker]] · `agenti/cfo-runway-tracker.md`
- [[WF-COST-REPORT]] · `workflow/WF-COST-REPORT.md`
- [[STATE]] · `state/README.md`
- [[SKILLS]] · `skills/SKILLS.md`
