---
Type: KPI
Status: Active
Tags: #kpi #content-factory #cf-r0 #director #metriche #ordini
Created: 2026-06-19
Last updated: 2026-06-19
---

# KPI — CF-R0 Director

> **Reparto:** CF-R0 · **Ecosistema:** 03-CONTENT-FACTORY · **Versione:** v2
> [DM] = Da Misurare — nessuna baseline storica disponibile; si stabilisce al primo ciclo operativo reale.
> Nessun numero inventato: i target numerici si fissano in M6 (milestone 6 dossier v2)
> dopo i primi cicli reali di produzione CF-DE.

---

## KPI primari: intake e dispatch ordini

| KPI | Owner | Definizione | Target | Baseline |
|---|---|---|---|---|
| Lead time ordine→dispatch (ore) | CF-D-DISPATCH | Ore dalla ricezione dell'ordine grezzo alla creazione di `orders/<id>/` e notifica capo area L1 | [DM] | [DM] |
| % ordini completi al primo giro | CF-D-QA | N. ordini con gate PASS senza risubmit / tot ordini ricevuti nel periodo | [DM] — obiettivo >80% in M6 | [DM] |
| % ordini dispatchati entro 2h dalla validazione QA | CF-D-LEAD | N. ordini con timestamp dispatch - timestamp QA PASS ≤ 2h / tot ordini dispatchati | [DM] | [DM] |

---

## KPI per area: distribuzione ordini

| KPI | Owner | Definizione | Target | Baseline |
|---|---|---|---|---|
| N. ordini attivi per area (Pre/Prod/Post) | CF-D-STATUS | Conteggio snapshot ordini per area ogni lunedì dal registry `cf/orders` | [DM] — indica distribuzione carico | [DM] |
| N. ordini per formato / settimana | CF-D-STATUS | Distribuzione ordini per tipo formato (carosello-ig, video-ugc, ecc.) | [DM] — indica formato dominante | [DM] |
| N. ordini per committente / settimana | CF-D-STATUS | Distribuzione ordini per committente | [DM] — indica dipendenza da singolo committente | [DM] |

---

## KPI qualità del gate

| KPI | Owner | Definizione | Target | Baseline |
|---|---|---|---|---|
| Fail rate gate QA (%) | CF-D-QA | N. ordini FAIL / tot ordini ricevuti nel periodo | [DM] — trend decrescente indica onboarding committenti migliorato | [DM] |
| Tipo errore FAIL più frequente | CF-D-QA | Campo con più FAIL nel periodo (brand_kit / icp / formato / budget) | Nessun tipo > 50% del totale FAIL | [DM] |
| % risubmit con PASS dopo FAIL | CF-D-QA | N. ordini corretti e risubmit con PASS / N. ordini con FAIL nel periodo | [DM] — indica utilità del messaggio di errore strutturato | [DM] |

---

## KPI delivery e SLA

| KPI | Owner | Definizione | Target | Baseline |
|---|---|---|---|---|
| % ordini rispettati nella deadline originale | CF-D-LEAD | N. ordini consegnati entro deadline / tot ordini chiusi nel periodo | [DM] — obiettivo >90% in M6 | [DM] |
| N. alert ritardo emessi per settimana | CF-D-STATUS | N. alert "70% tempo consumato, non ancora in QA" nel periodo | Trend decrescente (sistema migliora la stima) | [DM] |
| Delta deadline originale vs delivery effettiva (giorni) | CF-D-LEAD | Media |deadline_originale - data_consegna_effettiva| per ordini chiusi | [DM] | [DM] |

---

## KPI budget e accuratezza stime

| KPI | Owner | Definizione | Target | Baseline |
|---|---|---|---|---|
| % ordini con alert budget pre-dispatch | CF-D-BUDGET | N. ALERT_BUDGET / tot ordini nel periodo | [DM] — deve stabilizzarsi in M6 con stime mature | [DM] |
| Delta stima → consuntivo crediti engine (%) | CF-D-BUDGET | Media |(crediti_consuntivo - crediti_stimati) / crediti_stimati| per ordini chiusi | [DM] — <15% obiettivo in M6 | [DM] |
| Superamento envelope globale CF (deve essere 0) | CF-D-LEAD | N. cicli in cui l'envelope globale è stato superato | 0 (non negoziabile) | 0 (inizio) |

---

## KPI apprendimento e miglioramento sistemico

| KPI | Owner | Definizione | Target | Baseline |
|---|---|---|---|---|
| Pattern confermati in `cf/kpi` (cumulativo) | CF-D-LEARN | N. pattern con cicli_osservati ≥ 2 nel namespace | Crescita per ciclo — sistema impara | 0 (inizio) |
| Trigger 07-FORGE attivati per trimestre | CF-D-LEARN | N. richieste formali a 07-FORGE con spec del problema | [DM] — troppi indica instabilità; troppo pochi indica cecità sui problemi | [DM] |
| % raccomandazioni di cf-d-learn implementate entro 30gg | CF-D-LEAD | N. raccomandazioni con azione verificata / tot nel periodo | [DM] | [DM] |

---

## Note metodologiche

- **[DM] non è un gap:** la baseline si stabilisce al primo run reale. Un numero inventato
  è peggio di [DM]: inquina tutti i confronti futuri.
- **Trend > valore assoluto nelle fasi iniziali.** In M6, dopo i primi cicli reali, CF-D-LEARN
  fissa le baseline numeriche e i target per tutti i [DM].
- **Il KPI "superamento envelope globale = 0" è l'unico non negoziabile da subito.** Gli altri
  [DM] hanno target da definire con evidenza; questo ha già il target.
- **Il fail rate gate QA è un KPI di onboarding,** non solo di qualità interna. Un fail rate
  alto indica che i committenti non capiscono il contratto di ordine — il problema è a monte,
  non in CF-D-QA.

---

## Connessioni

- [[WF-DIRECTOR-REVIEW]] · `workflow/WF-DIRECTOR-REVIEW.md` — workflow che usa questi KPI
- [[cf-d-status]] · `agenti/cf-d-status.md` — produce i KPI grezzi
- [[cf-d-learn]] · `agenti/cf-d-learn.md` — elabora trend e pattern dai KPI
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §3 CF-R0`
