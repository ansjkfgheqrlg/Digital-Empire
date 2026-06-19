---
Type: KPI
Status: Active
Tags: #kpi #analytics #ottimizzazione #metriche #L2.4
Created: 2026-06-18
Last updated: 2026-06-18
---

# KPI — L2.4 Analytics & Ottimizzazione

> **Reparto:** L2.4 · **Ecosistema:** 04-MARKETING · **Versione:** v2
> [DM] = Da Misurare — nessuna baseline storica disponibile; si stabilisce al primo run reale.
> Nessun numero inventato: i target numerici si fissano in M6 (milestone 6 dossier v2)
> dopo i primi cicli reali di ottimizzazione.

---

## KPI primari del reparto

| KPI | Owner | Definizione | Target | Baseline |
|---|---|---|---|---|
| Esperimenti chiusi con verdetto / mese | AN3 | N. WF-AB-TEST con verdetto statisticamente valido (PASS o INCONCLUSIVO documentato) nel periodo | [DM] | [DM] |
| Pattern ICP consolidati (cumulativo) | AN4 | N. record totali in `marketing/copy/patterns/*` con n_run ≥ 2 | Cresce a ogni ciclo | 0 (inizio) |
| Antipattern ICP consolidati (cumulativo) | AN4 | N. record in `marketing/copy/antipatterns/*` con n_run ≥ 2 | Cresce a ogni ciclo | 0 (inizio) |
| Cicli WF-OPTIMIZATION-LOOP completati / mese | AN-LEAD | N. cicli con tutti i 6 passi tracciati in state.json | [DM] | [DM] |

---

## KPI tracking e copertura

| KPI | Owner | Definizione | Target | Baseline |
|---|---|---|---|---|
| % campagne con tracking plan (0 eventi fantasma) | AN1 | N. campagne con TP validato PASS / tot campagne lanciate nel periodo | 100% | [DM] |
| Tempo brief → TP consegnato a 06-PLATFORM | AN1 | Ore dalla ricezione brief alla consegna specifica tecnica | [DM] | [DM] |
| Copertura eventi micro-conversione (% landing con schema CA3) | AN5 | N. landing con schema micro-conversioni definito / tot landing attive | [DM] | [DM] |

---

## KPI qualità del sistema

| KPI | Owner | Definizione | Target | Baseline |
|---|---|---|---|---|
| % verdetti A/B statisticamente validi | AN3 | N. PASS / tot test chiusi (PASS + INCONCLUSIVO) | [DM] — atteso >60% | [DM] |
| % pattern con n_run ≥ 2 (anti-rumore) | AN4 | N. pattern con n_run ≥ 2 / tot pattern nel namespace | 100% (non negoziabile) | 100% al primo write |
| Anomalie AN-OBSERVER risolte entro 48h | AN-OBSERVER | N. anomalie con diagnosi in corso entro 48h / tot anomalie segnalate | [DM] | [DM] |
| Gate bypass rate | AN-OBSERVER | N. copy consegnati senza score A8 + brand gate / tot copy consegnati | 0 (Art.4.1 Mandato) | 0 |

---

## KPI di connessione con altri reparti

| KPI | Owner | Definizione | Reparto collegato |
|---|---|---|---|
| Drop rate per sezione APSOC per landing attiva | AN5 | % utenti che abbandonano in ogni sezione APSOC su ogni landing con ≥200 sessioni | L2.6 (CA4 per sprint CRO) |
| Pattern usati da COPY-MASTER nell'ultimo ciclo | AN4 | N. pattern ReasoningBank citati nel contratto copy inviato da COPY-MASTER | L2.1 (misura riuso) |
| Sprint CRO avviati da input AN5 | AN5 | N. WF-CRO-SPRINT avviati su colli di bottiglia segnalati da AN5 | L2.6 CA4 |

---

## Note metodologiche

- **[DM] non è un gap:** significa che la baseline si stabilisce al primo run reale.
  Un numero inventato è peggio di un [DM]: inquina il confronto futuro.
- **Trend > valore assoluto** nelle fasi iniziali: importa che i pattern aumentino
  (sistema impara), non che raggiungano un numero specifico.
- **Revisione KPI in M6** (milestone 6 dossier v2): al completamento del primo ciclo
  WF-OPTIMIZATION-LOOP reale, AN-LEAD fissa le baseline numeriche per tutti i [DM].

---

## Connessioni

- [[WF-OPTIMIZATION-LOOP]] · `workflow/WF-OPTIMIZATION-LOOP.md`
- [[WF-AB-TEST]] · `workflow/WF-AB-TEST.md`
- [[an-observer-observability-lead]] · `agenti/an-observer-observability-lead.md`
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §7.2`
