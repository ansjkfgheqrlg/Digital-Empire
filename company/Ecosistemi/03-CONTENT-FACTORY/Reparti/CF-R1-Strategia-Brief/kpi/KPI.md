---
Type: KPI
Status: Active
Tags: #kpi #content-factory #CF-R1 #misurazione #performance
Created: 2026-06-19
Last updated: 2026-06-19
---

# KPI — CF-R1 Strategia & Brief

> **Reparto:** CF-R1 Strategia & Brief · **Ecosistema:** 03-CONTENT-FACTORY
> Owner KPI: `cf-r1-coord` · Report a: L1-PRE · Cadenza: settimanale

---

## KPI primari del reparto

| KPI | Formula | Owner | Fonte dati | [DM] |
|---|---|---|---|---|
| **Lead time ordine→brief** | (timestamp gate PASS) − (timestamp ricezione ordine) in minuti | CF-R1-COORD | `orders/<id>/state.json` | [DM] — baseline da raccogliere al primo ciclo produttivo |
| **% brief completi al primo giro** | N. brief con `n_rework = 0` / N. tot brief prodotti nel periodo | CF-R1-QA | `orders/<id>/state.json` | [DM] — target atteso >70% dopo 4 settimane |
| **Angle usati vs scartati per brand** | N. angle selezionati dal committente (o da COORD) / N. angle prodotti (tot per periodo) | CF-R1-ANGLE | Log selezione in context.json | [DM] — segnale di qualità libreria formule |
| **Lead time WF-TREND-BRIEF** | (timestamp brief PASS) − (timestamp avvio workflow) in minuti | CF-R1-COORD | `orders/CF-TREND-*/state.json` | Target: ≤60 min per definizione workflow |
| **% trend processati entro SLA** | N. WF-TREND-BRIEF con lead_time ≤60 min / N. tot WF-TREND-BRIEF avviati | CF-R1-TREND | `orders/CF-TREND-*/state.json` | Target: ≥90% |
| **% trend scartati per età** | N. trend scartati (età >48h) / N. tot trend ricevuti | CF-R1-TREND | `cf/briefs/trend/scartati/` | Segnale latenza 08-INTELLIGENCE; target: <20% |

---

## KPI secondari (qualità libreria)

| KPI | Formula | Owner | Fonte dati | [DM] |
|---|---|---|---|---|
| Pattern consolidati in `cf/patterns` | N. pattern con `scritto_in_libreria: true` (cumulativo) | CF-R1-LEARN | `cf/patterns/*` | [DM] — cresce con il tempo; 0 alla prima settimana |
| Antipattern identificati | N. antipattern in libreria (cumulativo) | CF-R1-LEARN | `cf/patterns/*` | [DM] |
| Lacune pipeline segnalate | N. segnalazioni campo mancante sistematico / periodo | CF-R1-LEARN | Log CF-R1-QA | Target: 0 lacune sistemiche ricorrenti |
| Slot calendario con brand_kit validato | N. slot con brand_kit validato / tot slot nel piano | CF-R1-CAL | `cf/calendars/*/settimana-*.json` | Target: 100% (zero slot orfani) |

---

## KPI di sistema (salute del reparto)

| KPI | Soglia | Azione se sotto soglia |
|---|---|---|
| % brief PASS al primo giro | <50% per 2 settimane consecutive | Escalation L1-PRE: analisi bottleneck pipeline |
| Lead time ordine→brief | >120 min per 3 ordini consecutivi | CF-R1-COORD identifica agente bottleneck; segnala a L1-PRE |
| SLA WF-TREND-BRIEF | <80% rispettato | CF-R1-COORD analizza cause; segnala a L1-PRE |
| Trend scartati per età | >30% in una settimana | Segnalazione a 08-INTELLIGENCE: aumentare frequenza invio brief |

---

## Note su [DM]

I valori marcati [DM] (Da Misurare) richiedono dati reali provenienti dai primi cicli
produttivi. Non vengono stimati o inventati: i target si definiscono dopo almeno
4 settimane di operatività del reparto, in accordo con L1-PRE e CF-Director.

Il Mandato Empire Art.2 ("prove non promesse") si applica anche ai KPI interni:
nessun target viene dichiarato senza almeno un ciclo di dati reali a supporto.

---

## Connessioni

- [[cf-r1-coord]] · `agenti/cf-r1-coord.md` — owner KPI e report a L1-PRE
- [[cf-r1-learn]] · `agenti/cf-r1-learn.md` — produce i dati per KPI libreria
- [[WF-BRIEF]] · `workflow/WF-BRIEF.md`
- [[WF-TREND-BRIEF]] · `workflow/WF-TREND-BRIEF.md`
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R1`
