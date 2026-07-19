---
Type: CONCEPT
Status: Active
Tags: #kpi #account-management #customer-success #retention #nps #A7
Created: 2026-07-11
Last updated: 2026-07-11
---

# KPI — A7 Account Management & Customer Success

> Tutte le baseline sono **[DM]** (da misurare). Nessun numero è inventato: A7 è un reparto NUOVO
> in v2, non ha storico. La prima misurazione reale sostituisce il [DM] e diventa la baseline.

---

## Tabella KPI

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| **NPS medio fine 90gg** | AG-A7-CLOSE | Media dell'NPS raccolto a G+90 sui clienti chiusi nel periodo. Solo NPS effettivamente dichiarati dal cliente; i `[DM]` sono esclusi dalla media e contati a parte | [DM] | ≥8 |
| **% clienti con KAM assegnato** | AG-A7-QA | Clienti con campo `kam` popolato in `agency/a7/clients` / totale clienti attivi | [DM] | **100%** (R1, non negoziabile) |
| **% clienti con upsell/referral attivato** | AG-A7-COORD | Clienti con almeno un handoff emesso verso A3-Preventivi, A6-Marketing-Interno o 02-INFO-BUSINESS / totale clienti chiusi nel periodo | [DM] | [DM] → definito dopo 5 cicli chiusi |
| **SLA ticket rispettato** | AG-A7-QA | % ticket chiusi entro l'SLA contrattuale. **Dato prodotto da A4-Delivery**, letto da A7 in sola lettura | [DM] | ≥ soglia contrattuale del cliente |
| **Alert churn risolti entro 24h** | AG-A7-HEALTH | Alert con azione correttiva registrata in `agency/a7/alerts` entro 24h dal segnale / totale alert alzati | [DM] | 100% (R2) |
| **NPS raccolto a G+90** | AG-A7-CLOSE | Clienti con `nps ≠ [DM]` a closure / totale clienti arrivati a G+90 | [DM] | 100% (R5) |
| **Tasso di churn nel ciclo** | AG-A7-COORD | Clienti persi prima del G+90 / totale clienti entrati nel ciclo | [DM] | [DM] → definito dopo 5 cicli |
| **Touchpoint loggati** | AG-A7-QA | Touchpoint registrati in `agency/a7/touchpoints` / touchpoint pianificati dalla cadenza | [DM] | 100% (R3) |

---

## Come si misurano

Tutti i KPI si calcolano **leggendo lo state**, mai da stime o ricordi di sessione:

- **NPS medio** e **NPS raccolto** → campo `nps` in `agency/a7/clients/{client_id}`. Un `[DM]`
  non è uno zero e non entra nella media: entra nel denominatore di "NPS raccolto".
- **% clienti con KAM** → conteggio del campo `kam` su `agency/a7/clients/*`. Un cliente senza KAM
  è un'anomalia bloccante, non un punto percentuale.
- **% upsell/referral** → campo `upsell_referral` in `agency/a7/clients/{client_id}`; conta un
  handoff **emesso**, non un'opportunità solo "vista".
- **SLA ticket** → `agency/a4/sla/{client_id}`. **A7 non produce questo dato**: lo legge da
  A4-Delivery. Se A4 non lo produce, il KPI è `[DM]` e AG-A7-QA lo segnala come gate cieco.
- **Alert entro 24h** → differenza tra `timestamp_alert` (`agency/a7/health`) e il timestamp
  dell'azione registrata (`agency/a7/alerts`).
- **Touchpoint loggati** → conteggio su `agency/a7/touchpoints/{client_id}` contro la cadenza
  fissata al kickoff da AG-A7-ONBOARD.

**Regola:** un KPI che non si può calcolare dallo state **non è un KPI di A7** — è un'illusione.

---

## Cadenza

| Cadenza | KPI | Chi produce |
|---|---|---|
| **Settimanale** | Alert churn risolti entro 24h · Touchpoint loggati · % clienti con KAM | AG-A7-HEALTH + AG-A7-QA |
| **A ogni closure** | NPS · NPS raccolto · upsell/referral attivato · SLA ticket finale | AG-A7-CLOSE + AG-A7-QA |
| **Mensile** | NPS medio · tasso di churn nel ciclo · % upsell/referral aggregata | AG-A7-COORD → AG-DIR |
| **Su richiesta** | Aggregati NPS e churn rate per report di ecosistema (sola lettura, no nominativi) | 08-INTELLIGENCE |

I KPI mensili vanno in `agency/a7/gates/` come snapshot datato e sono l'unica fonte per il report
verso AG-DIR. Nessun KPI viene riportato "a memoria".

---

## Connessioni

- [[ag-a7-qa]] · `agenti/ag-a7-qa.md` — owner della verifica dei KPI di gate
- [[ag-a7-health]] · `agenti/ag-a7-health.md` — owner degli alert e del monitoraggio settimanale
- [[REGOLE]] · `regole/REGOLE.md` — R1, R2, R3, R5 rendono bloccanti i target al 100%
- [[A4-Delivery]] · `../A4-Delivery/` — produttore del dato SLA ticket
