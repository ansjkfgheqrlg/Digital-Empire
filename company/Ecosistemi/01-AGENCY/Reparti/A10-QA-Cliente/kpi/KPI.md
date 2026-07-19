---
Type: CONCEPT
Status: Active
Tags: #kpi #agency #qa #audit #A10
Created: 2026-07-11
Last updated: 2026-07-11
---

# KPI — A10 QA-Cliente & Audit Qualità

> **[DM] = Da Misurare.** Il reparto è nuovo: nessuna baseline è nota. Zero numeri inventati —
> una baseline falsa è peggio di una baseline assente, perché sembra vera (R7).

---

## 1. KPI del reparto

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| **% delivery PASS al primo review** | AG-A10-COORD | Delivery con verdetto PASS alla prima review A10 / delivery totali reviewate, per mese | [DM] | ≥ 80% a regime |
| **Difetti per categoria** | AG-A10-REVIEW | Conteggio difetti per categoria (ambiente, brand, handover, UAT, dipendenza-DE), per mese | [DM] | Trend decrescente m/m |
| **Tempo QA** | AG-A10-COORD | Ore dal `HC-AG-QC-01` all'emissione del verdetto (`HC-QC-AG-01`) | [DM] | ≤ 48h |
| **Difetti sfuggiti al gate** | AG-A10-LEARN | Difetti emersi come ticket 90gg (A4) ma non rilevati in review — il KPI che giudica A10 stesso | [DM] | → 0 |
| **% run autonome del cliente** | AG-A10-UAT | Delivery in cui il cliente esegue 1 run da solo **e** sa spiegarla / delivery reviewate | [DM] | 100% (è G6: è un gate, non un obiettivo) |
| **Puntualità audit mensile** | AG-A10-LEARN | Report condiviso entro 5gg da fine mese (sì/no), per mese | [DM] | 100% |
| **Indipendenza del verdetto** | AG-A10-COORD | Verdetti emessi senza scritture A4 in `agency/a10/*` e senza override da A4 | [DM] | 100% (è G7) |

---

## 2. Come si misurano

| KPI | Fonte dato | Metodo |
|---|---|---|
| % PASS al primo review | `agency/a10/reviews/*` | Conta `verdetto == PASS` su `review_index == 1` / totale review aperte nel mese |
| Difetti per categoria | `agency/a10/defects/*` | Group-by `categoria` + `severita` sul mese |
| Tempo QA | `agency/a10/reviews/*` | `ts_verdetto − ts_handoff_in` per review; mediana mensile |
| Difetti sfuggiti | `agency/a4/support` ∩ `agency/a10/defects` | Ticket 90gg classificati come difetto di delivery e **assenti** dalla review corrispondente |
| % run autonome | `agency/a10/uat/*` | `run_autonoma == true AND comprensione_verificata == true` / totale UAT |
| Puntualità audit | `agency/a10/patterns/monthly/*` | `ts_report ≤ fine_mese + 5gg` |
| Indipendenza verdetto | `agency/a10/reviews/*` (audit scritture) | Nessun `author` fuori dal roster A10 sulle chiavi `agency/a10/*` |

**Regola di misura:** ogni numero pubblicato cita la chiave di stato da cui proviene.
Un KPI senza fonte è un KPI cancellato (R7).

---

## 3. Cadenza

| Cadenza | Cosa | Owner |
|---|---|---|
| Per delivery | Tempo QA, esito primo review, run autonoma | AG-A10-COORD |
| Settimanale | Difetti aperti per categoria, review in coda | AG-A10-COORD |
| Mensile (entro 5gg da fine mese) | Report completo: tutti i KPI + pattern + azioni → AG-DIR, 07-FORGE | AG-A10-LEARN |
| Trimestrale | Revisione delle **soglie target** alla luce delle baseline finalmente misurate | AG-DIR |

---

## 4. Anti-gaming

Un reparto di audit ha un incentivo perverso: alzare la % di PASS abbassando l'asticella.
Tre contromisure strutturali:

1. **Difetti sfuggiti al gate** è il KPI dominante su A10: se A10 fa passare tutto, i difetti
   riemergono come ticket 90gg e il numero esplode. Non si può barare a lungo.
2. **% PASS al primo review** è un KPI **di A4**, non di A10: misura la qualità della costruzione.
   A10 non è premiata per farlo salire — è premiata per misurarlo bene.
3. La linea di riporto è **AG-DIR**, non A4: nessuno dentro la delivery ha leva sul verdetto.

---

## Connessioni

- [[ARCHITETTURA]] · `../ARCHITETTURA.md §4` — i gate che generano questi numeri
- [[ag-a10-learn]] · `../agenti/ag-a10-learn.md` — owner del report mensile
- [[WF-QUALITY-AUDIT]] · `../workflow/WF-QUALITY-AUDIT.md`
