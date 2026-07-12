---
Type: KPI
Status: Active
Tags: #kpi #agency #acquisizione #outreach #A2
Created: 2026-06-22
Last updated: 2026-06-22
---

# KPI — A2 Acquisizione / Outreach

> Metriche del reparto. Baseline storica: `[DM]` — da misurare dal primo ciclo reale.
> Nessun numero inventato (Mandato Art.2 + REGOLE R4). I cap NON sono KPI: sono vincoli
> non negoziabili che proteggono deliverability e account.

---

## KPI operativi

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| Inviati/gg email | AG-A2-SEND | N. email inviate al giorno entro il cap | `[DM]` | ≤500/gg, cap 100/h (vincolo, non da superare) |
| Inviati/gg LinkedIn | AG-A2-LI | Connessioni + messaggi + commenti al giorno | `[DM]` | 20 conn + 20 msg + 30 commenti/gg (vincolo) |
| Inviati/gg Instagram | AG-A2-IG | DM inviati al giorno | `[DM]` | ≤30 DM/gg (vincolo) |
| Reply rate per canale | AG-A2-TRIAGE | Risposte ricevute / messaggi inviati, per canale | `[DM]` — dal giorno 1 | progressivo, mai inventato |
| Positive reply rate | AG-A2-TRIAGE | Risposte "interessato" / risposte totali | `[DM]` | progressivo |
| Call prenotate/settimana | AG-A2-BOOK | Slot discovery confermati passati ad A8 | `[DM]` | output finale del reparto |
| Gate Bibbia pass al primo tentativo | AG-A2-QA | % messaggi che passano i 3 check senza rework | `[DM]` | progressivo, migliora col volume |

---

## KPI di qualità del sistema (trasversali al reparto)

| KPI | Owner | Definizione | Target |
|---|---|---|---|
| Gate Bibbia bypassati | AG-A2-QA | N. messaggi inviati senza gate Bibbia verde / tot inviati | 0 (REGOLE R1) |
| Cap superati | AG-A2-SEND / LI / IG | N. volte che un cap reale è stato superato in una run | 0 (REGOLE R2) |
| Risposte a un "no" definitivo | AG-A2-TRIAGE / AG-A2-FUP | N. follow-up inviati a lead con "no" definitivo | 0 (REGOLE R5) |
| Store con PII nello schema state | AG-A2-TRIAGE | N. record di state contenenti PII non scansionata | 0 (REGOLE R3) |
| Handoff ad A8 senza slot confermato | AG-A2-BOOK | N. passaggi ad A8 senza slot call confermato | 0 (REGOLE R6) |

---

## Come si misurano

- **Inviati/gg e cap:** letti dai contatori in `agency/a2/{canale}/state.json`,
  scritti dal sender / operatore canale a ogni run. Il cap residuo è la fonte di verità.
- **Reply / positive reply rate:** AG-A2-TRIAGE classifica ogni risposta (reply_monitor.py +
  skill `outreach-reply-triage`) e aggiorna i contatori in `agency/a2/reply/`.
- **Call prenotate:** AG-A2-BOOK registra ogni slot confermato prima dell'handoff `HC-AG-CL-01`.
- **Gate Bibbia pass/fail:** AG-A2-QA registra ogni esito (PASS / FAIL + check fallito) nel
  namespace email/canale. Il rapporto pass/totale è il first-pass rate.
- **KPI di qualità:** sono soglie a zero. Ogni occorrenza > 0 è un incidente da escalare ad AG-DIR.

---

## Cadenza di revisione

- Contatori cap e invii: a ogni run giornaliera (battito cardiaco del reparto).
- Reply rate / positive reply rate: settimanale (per canale e per variante template).
- Call prenotate/settimana: settimanale, è l'output che AG-A2-COORD riporta ad AG-DIR.
- Template in calo (reply rate sotto baseline per 2 cicli) → richiesta refresh ad A5 Copy-interno / 04-MARKETING.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §5` — namespace dove i KPI vengono scritti
- [[ag-a2-qa]] · `agenti/ag-a2-qa.md` — presidia il gate Bibbia e i KPI di qualità
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A2` — KPI e cap reali
