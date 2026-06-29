---
Type: KPI
Status: Active
Tags: #kpi #agency #delivery #handover #uat #A4
Created: 2026-06-23
Last updated: 2026-06-23
---

# KPI — A4 Delivery & Implementazione

> Metriche del reparto. Baseline storica: [DM] — da misurare alla prima delivery reale.
> Nessun numero inventato (Mandato Art.2 + principio P6 del reparto).

---

## KPI operativi

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| Giorni delivery | AG-A4-COORD | Giorni da ambiente conforme (G+0) a Gate Delivery PASS | [DM] — prima delivery | ≤7 dall'ambiente conforme |
| UAT pass al primo giro | AG-A4-UAT | % delivery con UAT firmata senza cicli di rework | [DM] | [DM] — si stabilisce dopo M1-M2 |
| Run autonoma cliente in UAT | AG-A4-QA | % delivery in cui il cliente ha eseguito ≥1 run da solo prima del handover | [DM] | 100% (condizione Gate Delivery) |
| Ticket risolti in SLA | AG-A4-SUPP | % ticket 90gg risolti entro SLA (≤24h bug, ≤48h domanda) | [DM] | [DM] — SLA da contratto |
| NPS fine 90gg | AG-A4-COORD | NPS misurato a chiusura dei 90gg di supporto | [DM] | misurato, non inventato |
| Ticket per settimana (trend) | AG-A4-SUPP | Numero ticket/settimana nei 90gg; atteso decrescente (cliente più autonomo) | [DM] | trend decrescente |
| Delivery riusate da pattern | AG-A4-LEARN | % delivery che riusano runbook/pattern da `agency/a4/reasoning` vs ex novo | [DM] | cresce col volume |

---

## KPI di qualità del sistema (trasversali al reparto)

| KPI | Owner | Definizione | Target |
|---|---|---|---|
| Gate Delivery bypass rate | AG-A4-QA | N. handover chiusi senza Gate Delivery / tot handover | 0 (Regola R1) |
| Dipendenza residua DE post-handover | AG-A4-QA | N. delivery dove serve ancora DE per girare / tot delivery | 0 (R2 — identità DE) |
| Countdown partito su ambiente non conforme | AG-A4-ENV | N. delivery con countdown avviato senza conformità ambiente | 0 (R3) |
| Secrets/PII cliente nel namespace DE | AG-A4-COORD | N. file di stato con secrets o PII cliente | 0 (R6) |
| Ticket chiusi senza conferma cliente | AG-A4-SUPP | N. ticket 90gg chiusi senza conferma esplicita del cliente | 0 (R5) |

---

## Come si misurano

- **Giorni delivery e UAT pass:** da `agency/a4/delivery/` — ogni delivery ha `countdown_start`,
  `gate_delivery`, `uat_firmata`. Conteggio da AG-A4-COORD a chiusura.
- **Run autonoma cliente:** AG-A4-QA registra il flag `run_autonoma_cliente` nel Gate Delivery.
- **Ticket SLA e trend:** da `agency/a4/support/` — ogni ticket ha `classe`, `sla_target`,
  `risolto_entro_sla`, `data`. Conteggio settimanale da AG-A4-SUPP.
- **NPS fine 90gg:** survey a chiusura supporto; valore reale, [DM] finché non raccolto.
  Letto e aggregato in review con A7 Account Mgmt.

---

## Cadenza di revisione

- Giorni delivery / UAT pass: ad ogni delivery chiusa.
- Ticket SLA + trend settimanale: check proattivo settimanale (09 OPERATIONS schedula).
- NPS + review supporto: a chiusura dei 90gg, con A7 e proposta upsell da A6.
- Report di sintesi ad AG-DIR: ogni delivery chiusa + ogni chiusura 90gg.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §4` — namespace memoria dove i KPI vengono scritti
- [[ag-a4-qa]] · `agenti/ag-a4-qa.md` — presidia il Gate Delivery e i KPI di qualità
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A4` — KPI di reparto
- [[A6-Marketing-Interno]] · riceve segnale delivery chiusa per case study
