---
Type: KPI
Status: Active
Tags: #kpi #agency #copywriting #apsoc #reply-rate #gate #A5
Created: 2026-06-23
Last updated: 2026-06-23
---

# KPI — A5 Copywriting Interno

> Metriche del reparto. Baseline storica: [DM] — da misurare al primo ciclo reale.
> Nessun numero inventato (Mandato Art.2 + principio P3 del reparto).

---

## KPI operativi

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| % copy passato Gate Bibbia al primo giro | AG-A5-QA | output PASS senza rework / tot output verificati | [DM] | progressivo — migliora col volume |
| Tempo brief → copy | AG-A5-WRITE | ore dalla ricezione brief alla consegna gated, per tipo standard (email, DM, preventivo) | [DM] | si stabilisce dopo M1-M2 |
| Reply rate medio varianti | AG-A5-LEARN | reply rate per variante post-rollout, letto da `agency/outreach` | [DM] — primo ciclo | [DM] — stabilito su dati reali |
| Refresh con winner adottato | AG-A5-COORD | N. refresh con winner A/B adottato / tot refresh avviati | [DM] | cresce col volume |
| Copertura obiezioni validate | AG-A5-OBJ | % obiezioni ricorrenti con almeno 1 risposta `validata` | [DM] | 100% obiezioni ricorrenti coperte |
| Script gated consegnati ad A8 | AG-A5-SCRIPT | N. script PASS consegnati / tot richiesti da A8 | [DM] | 100% consegnati gated |

---

## KPI di qualità del sistema (trasversali al reparto)

| KPI | Owner | Definizione | Target |
|---|---|---|---|
| Gate bypass rate | AG-A5-QA | N. output rilasciati senza Gate Bibbia verde / tot output | 0 (R1) |
| Claim non provabili in produzione | AG-A5-QA | N. copy/script rilasciati con claim senza prova reale | 0 (R4 — Mandato Art.2) |
| Risposte obiezioni non validate usate | AG-A5-OBJ | N. risposte `non_validata` finite in copy rilasciato | 0 (R4) |
| Rollout universali senza dati A/B | AG-A5-COORD | N. adozioni di variante senza verdetto A/B su campione valido | 0 (R3) |
| P prima di S violazioni | AG-A5-QA | N. output con S prima di P rilevati in gate | 0 (R5 — FAIL automatico) |
| Pezzi grandi prodotti internamente per errore | AG-A5-COORD | N. sales page/sequenze lunghe fatte in A5 invece di delegate a 04-MKT | 0 (R2) |

---

## Come si misurano

- **Gate KPI:** AG-A5-QA registra ogni esito (PASS/FAIL + check fallito) in `agency/a5/templates/`
  (refresh) o `agency/a5/script/` (script). Allineato allo schema del gate di A2.
- **Reply rate e refresh KPI:** letti da `agency/outreach` (dati reali di invio di A2). AG-A5-LEARN
  consolida in `agency/a5/performance`. A5 legge, non produce i dati grezzi di invio.
- **Obiezioni KPI:** da `agency/a5/obiezioni` — conteggio coppie `validata` vs `non_validata`.
- **Tempo brief → copy:** AG-A5-COORD registra il timestamp di ricezione e di consegna gated.

---

## Cadenza di revisione

- Gate KPI: ad ogni output verificato.
- Reply rate / refresh KPI: ad ogni ciclo di outreach di A2 (mensile o per batch).
- Report di sintesi ad AG-DIR: ogni ciclo di reparto completato (almeno 1 refresh chiuso).

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §4` — namespace memoria dove i KPI vengono scritti
- [[ag-a5-qa]] · `agenti/ag-a5-qa.md` — presidia i gate KPI (riuso Gate Bibbia A2)
- [[ag-a5-learn]] · `agenti/ag-a5-learn.md` — fornisce i dati di reply rate e refresh
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A5` — KPI dossier
