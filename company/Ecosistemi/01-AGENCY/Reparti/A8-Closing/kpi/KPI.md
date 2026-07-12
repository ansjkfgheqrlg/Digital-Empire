---
Type: CONCEPT
Status: Active
Tags: #kpi #agency #closing #sales-call #A8
Created: 2026-07-11
Last updated: 2026-07-11
---

# KPI — A8 Closing / Sales-Call

> Metriche del reparto che presidia il gap preventivo→contratto.
> Tutte le baseline sono **[DM]** (da misurare): il reparto è greenfield v2, nessuno storico v1.
> **Regola:** una baseline non si inventa. Si dichiara `[DM]` finché non ci sono ≥10 call chiuse.

---

## Tabella KPI

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| **K1 — Tasso conversione preventivo→contratto** | AG-A8-COORD | N. contratti firmati / N. preventivi arrivati a call di chiusura, nel periodo | [DM] | [DM] dopo 10 call; poi +10% sul misurato |
| **K2 — Tempo preventivo→firma** | AG-A8-COORD | Giorni medi tra invio preventivo (A3) e contratto firmato | [DM] | ≤14 giorni |
| **K3 — Dossier pre-call con gate PASS ≥2h** | AG-A8-QA | % dossier consegnati a Max in SLA (≥2h prima) **e** con `qa_gate = PASS` | [DM] | 100% (SLA non negoziabile) |
| **K4 — Gate PASS al primo tentativo** | AG-A8-QA | % dossier che passano AG-A8-QA senza rework | [DM] | ≥80% |
| **K5 — Debrief chiusi entro 2h con motivo** | AG-A8-DEBRIEF | % call con `esito` **e** `motivo` popolati entro 2h dalla fine | [DM] | 100% (integrità namespace) |
| **K6 — Pattern obiezioni ricorrenti** | AG-A8-LEARN | N. obiezioni distinte catalogate **con risposta a-prova**; % copertura vs. libreria A5 | [DM] | Copertura ≥90% delle obiezioni emerse |
| **K7 — Obiezioni emerse non previste** | AG-A8-LEARN | % obiezioni emerse in call che **non** erano nel dossier pre-call | [DM] | ≤20% (misura la qualità della prep) |
| **K8 — Prove mancanti richieste in call** | AG-A8-OBJ | N. prove che il prospect ha chiesto e che non avevamo | [DM] | Trend decrescente; ogni gap → A5/A3 |
| **K9 — Call scoperte (senza dossier gated)** | AG-A8-COORD | N. call condotte da Max **senza** dossier con gate PASS | [DM] | 0 |

---

## Come si misurano

**Fonte unica di verità:** il namespace `agency/a8`. Nessun KPI si calcola da stime o da memoria.

| KPI | Fonte dati | Calcolo |
|---|---|---|
| K1 | `agency/a8/calls/*.json` (`esito`) | `count(esito=win) / count(call_type=closing)` |
| K2 | `agency/a8/calls/*.json` (`giorni_preventivo_to_decisione`) | Media sui record con `esito=win` |
| K3 | `agency/a8/prep/*/state.json` (`qa_gate`, `sla_2h_rispettata`) | `count(PASS AND sla=true) / count(prep)` |
| K4 | `agency/a8/prep/*/state.json` (contatore rework del gate) | `count(PASS al ciclo 1) / count(prep)` |
| K5 | `agency/a8/calls/*.json` (`motivo`, `entro_2h`) | `count(motivo≠null AND entro_2h) / count(calls)` |
| K6 | `agency/a8/patterns/obiezioni/` + libreria `ag-a5-obj` | Confronto insiemi: emerse ∩ catalogate |
| K7 | `agency/a8/calls/*.json` (`obiezione_nuova_non_in_libreria`) | `count(nuove) / count(obiezioni_emerse)` |
| K8 | `agency/a8/patterns/gaps/` (`prove_richieste_e_mancanti`) | Conteggio + trend mensile |
| K9 | `agency/a8/prep/*/state.json` vs. `agency/a8/calls/*.json` | Call con record ma senza prep gated |

**Regola anti-vanity:** K1 e K2 sono i KPI di **risultato** (revenue). K3–K9 sono KPI di **processo**:
servono a spiegare K1/K2, non a sostituirli. Un reparto con K3 al 100% e K1 in caduta non sta bene:
sta preparando bene call che perde, e il problema è a monte (A3 o A1) o nell'ICP.

---

## Cadenza

| Cadenza | Cosa | Owner | Destinatario |
|---|---|---|---|
| **Per call** | K3, K4, K5 registrati nello state alla chiusura del gate | AG-A8-QA | `agency/a8/prep`, `agency/a8/calls` |
| **Settimanale** | K3, K4, K5, K9 — igiene di processo; ogni K9 > 0 è un incidente | AG-A8-COORD | AG-DIR |
| **Mensile** | K1, K2, K6, K7, K8 — risultato + apprendimento; pattern consolidati (≥3 evidenze) | AG-A8-LEARN | AG-DIR + 08-INTELLIGENCE |
| **Trimestrale** | Revisione baseline: i `[DM]` con ≥10 osservazioni diventano numeri; i target si ricalibrano | AG-A8-COORD | Board |

**Soglie di allarme (escalation automatica ad AG-DIR):**
- K9 > 0 in una settimana → una call è andata scoperta: incidente di processo.
- K5 < 100% → esiste una call chiusa senza motivo: il namespace è compromesso (R7).
- K4 < 50% su 2 settimane → il problema non è la singola prep, è l'input da A1/A3.
- 2 loss consecutive con lo stesso motivo → `WF-LOSS-ANALYSIS` in A3 + `HC-AG-IN-01`.

---

## Connessioni

- [[README]] · `README.md` — KPI di reparto in sintesi
- [[ag-a8-qa]] · `agenti/ag-a8-qa.md` — owner dei KPI di gate (K3, K4)
- [[ag-a8-learn]] · `agenti/ag-a8-learn.md` — owner dei KPI di apprendimento (K6, K7, K8)
- [[REGOLE]] · `regole/REGOLE.md` — le regole che i KPI di processo misurano
