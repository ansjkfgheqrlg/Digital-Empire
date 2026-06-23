---
Type: KPI
Status: Active
Tags: #kpi #content-factory #CF-R7 #pubblicazione #metriche #performance
Created: 2026-06-23
Last updated: 2026-06-23
---

# KPI — CF-R7 Pubblicazione & Distribuzione

> **Reparto:** CF-R7 · **Area:** Post-Produzione
> **[DM] = Da Misurare** — baseline da costruire nelle prime 4 settimane operative

---

## 1. KPI di processo (efficienza pipeline)

| KPI | Definizione | Owner | Cadenza | Target |
|---|---|---|---|---|
| % slot calendario rispettati | N. publish avvenuti negli slot previsti da WF-CALENDAR / tot slot assegnati | CF-R7-COORD | Settimanale | ≥90% — [DM] baseline |
| Latenza gate verdi → pubblicazione live | Ore tra `state.json 05-qa: PASS` (CF-R6) e post live sul canale | CF-R7-QA / CF-R7-COORD | Per ordine | [DM] — dipende da review umana; obiettivo <24h |
| % ordini bloccati pre-publish | N. ordini bloccati da CF-R7-QA (gate verdi mancanti / review umana / token) / tot ordini | CF-R7-QA | Settimanale | Monitorare ↓; ogni blocco = diagnosi |
| % token scaduti al check | N. ordini con token scaduto al momento del check / tot ordini | CF-R7-QA | Mensile | Obiettivo 0% con rinnovo proattivo; [DM] baseline |

---

## 2. KPI di qualità pubblicazione

| KPI | Definizione | Owner | Cadenza | Target |
|---|---|---|---|---|
| Post-check green rate | % URL verificati live con HTTP 200 al primo controllo (no retry) / tot URL | CF-R7-CHECK | Per ordine | ≥98% — [DM] baseline |
| % publish riusciti al primo tentativo | N. publish OK senza retry / tot invocazioni orchestratore | CF-R7-PUBLISH | Settimanale | ≥95% — [DM] baseline |
| % consegne con conferma ricezione entro 48h | N. conferme committente entro 48h / tot consegne non-social | CF-R7-DELIVER | Settimanale | ≥85% — [DM] baseline |

---

## 3. KPI di feedback e apprendimento

| KPI | Definizione | Owner | Cadenza | Target |
|---|---|---|---|---|
| % ordini con entrambe le misurazioni feedback | N. ordini con metriche 48h + 7gg completate / tot ordini chiusi | CF-R7-FEEDBACK | Mensile | ≥90% — [DM] baseline |
| N. entry cf/patterns per brand/formato per ciclo | Conteggio entry complete (48h + 7gg) per brand e formato | CF-R7-FEEDBACK | Mensile | Cresce nel tempo; primo target: ≥5 per brand attivo |
| Latenza raccolta metriche 48h | Ore tra ts_48h previsto e metriche effettivamente raccolte | CF-R7-FEEDBACK | Per ordine | [DM] — dipende da API piattaforme |

---

## 4. KPI metriche engagement per formato / brand

> Le metriche di engagement non sono KPI interni di CF-R7 ma dati raccolti e trasferiti
> a `cf/patterns` e a 04-MARKETING Analytics. CF-R7 non è responsabile dei risultati
> di engagement: è responsabile della raccolta puntuale e affidabile.

| Metrica raccolta | Canale | Cosa misura |
|---|---|---|
| Reach, impression, salvataggi | Instagram | Portata e retention del contenuto |
| Views, like, condivisioni | TikTok | Viralità e interesse |
| Impression, click, like | LinkedIn | Interesse professionale e click-through |
| Views, like, commenti, retention | YouTube | Qualità e completamento video |

**Regola:** [DM] per tutti i valori di engagement — baseline da costruire con dati reali.
Nessun benchmark inventato. I dati si leggono dalle API delle piattaforme.

---

## 5. KPI adattamento per canale

| KPI | Definizione | Owner | Target |
|---|---|---|---|
| % caption entro limite canale | N. caption conformi al limite char / tot caption prodotte | CF-R7-ADAPT | 100% |
| % pack senza flag resize | N. pack prodotti senza segnalare asset mancanti / tot pack | CF-R7-ADAPT | ≥95% — [DM] baseline |

---

## Revisione KPI

I KPI vengono rivisti a cadenza mensile da CF-R7-COORD con report a L1-POST.
Baseline da costruire nelle prime 4 settimane operative (≥20 pubblicazioni) per ogni canale.
Fino al raggiungimento della baseline: si raccolgono dati ma non si giudicano le performance.

---

## Connessioni

- [[CF-R7-Pubblicazione/README]] · `README.md` — roster e handoff
- [[WF-FEEDBACK-LOOP]] · `workflow/WF-FEEDBACK-LOOP.md` — raccolta dati che alimenta questi KPI
- [[CF-R8-Apprendimento]] · destinatario pattern per analisi che impatta calibrazione KPI
