---
Type: KPI
Status: Active
Tags: #kpi #marketing-interno #proof #case-study #agency #A6
Created: 2026-06-23
Last updated: 2026-06-23
---

# KPI — A6 Marketing Interno & Proof

> Metriche del reparto. Baseline storica: [DM] — da misurare al primo case study e al primo
> periodo di tracking inbound. Nessun numero inventato (Mandato Art.2 + principio P3 del reparto).

---

## KPI operativi

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| Case study per cliente chiuso | AG-A6-COORD | N. case study pubblicati / N. delivery chiuse (con metriche o qualitativo documentato) | [DM] | 1 per delivery chiusa |
| Testimonianze raccolte | AG-A6-PROOF | % clienti che forniscono testimonianza a fine 90gg | [DM] | progressivo — migliora col volume |
| Tasso consenso pubblicazione | AG-A6-PROOF | % clienti che acconsentono a nome/metriche pubblici | [DM] | [DM] |
| Call da inbound | AG-A6-INBOUND | N. call prenotate da chi ha visto landing/case study (non da outreach) | [DM] — primo periodo tracking | [DM] |
| Tasso conversione vetrina | AG-A6-INBOUND | % visita → call prenotata sugli asset della vetrina | [DM] — primo periodo reale | [DM] — si stabilisce dopo M1-M2 |
| Referral generati | AG-A6-UPSELL | N. referral ottenuti da clienti con NPS ≥8 | [DM] | progressivo |
| Upsell convertiti | AG-A6-UPSELL | % proposte upsell mappate che diventano contratto (via A3) | [DM] | [DM] |

---

## KPI di qualità del sistema (trasversali al reparto)

| KPI | Owner | Definizione | Target |
|---|---|---|---|
| Brand Gate bypass rate | AG-A6-QA | N. asset pubblici consegnati senza gate AG-A6-QA / tot output | 0 (Mandato Art.4 + R4) |
| Claim senza fonte in produzione | AG-A6-QA | N. claim numerici pubblicati senza fonte verificata | 0 (R1 — prove non promesse) |
| Upsell durante supporto attivo | AG-A6-UPSELL | N. upsell avviati prima dei 90gg / tot upsell | 0 (R3) |
| Metriche fabbricate rilevate | AG-A6-QA | N. numeri non verificabili rilevati in gate | 0 (R1 — violazione automatica) |
| Brand Gate PASS al primo tentativo | AG-A6-QA | % asset che passano il gate senza cicli di rework | progressivo — migliora col volume |

---

## Come si misurano

- **Case study e testimonianze:** da `agency/a6/case-studies/` e `agency/a6/proof/` —
  conteggio dei file con stato `pubblicato` e `proof_status` popolato.
- **Call da inbound e tasso conversione:** da tracking 06-PLATFORM/04-MARKETING; AG-A6-INBOUND
  attribuisce la fonte (inbound vs outreach). Baseline [DM] finché il tracking non produce dati.
- **Referral e upsell:** da `agency/a6/upsell/` — esito di ogni proposta mappata (via A3).
- **Gate KPI:** AG-A6-QA registra ogni gate (PASS/FAIL + motivo) nello `state.json` del case
  study o della modifica landing corrispondente.

---

## Cadenza di revisione

- Case study KPI: ad ogni delivery chiusa (un case study per cliente).
- Tasso conversione vetrina: mensile, dal primo mese di tracking attivo.
- Upsell/referral: ad ogni segnale NPS ≥8 processato.
- Report di sintesi ad AG-CONDUCTOR (01-AGENCY): ogni ciclo di reparto completato.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace memoria dove i KPI vengono scritti
- [[ag-a6-qa]] · `agenti/ag-a6-qa.md` — presidia i gate di qualità (claim senza fonte, bypass)
- [[ag-a6-inbound]] · `agenti/ag-a6-inbound.md` — fornitore dei dati di conversione vetrina
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A6` — KPI di reparto
