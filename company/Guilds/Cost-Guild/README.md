# 💰 Cost Guild — Guild

> Fonte: PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md sez. 4.2
> **Expertise:** cost-attribution per agente/task/brand, routing table 3-tier, envelope per reparto, ROI calc, dry-run policy
> **Serve:** OPERATIONS (usa la Guild come team di supporto), CFO (supervisione policy)
> **Sponsor C-level:** CFO (empire-cfo)
> Collegato a: [[GRUPPO.md]] · [[company/Backbone/Coordination/README.md]]

---

## Identità

| Campo | Valore |
|---|---|
| **Guild Master** | `cost-guild-master` (= CFO + T1 routing agent) |
| **Tipo** | Guild trasversale — expertise su richiesta, non gerarchia verticale |
| **Deliverable principale** | Routing policy YAML + envelope per reparto + soglie Cost Sentinel |
| **Ingaggio** | Passivo (`memory_search "routing policy"`) o attivo (guild_request) |

---

## Cosa standardizza

### 1. Routing Policy 3-Tier (la policy di sistema — Pattern #9 cost guard)

La Cost Guild mantiene la tabella di routing che ogni coordinator DEVE applicare prima di scegliere il modello:

| Tier | Modello | Task DE tipici | Regola |
|---|---|---|---|
| **0** | WASM (gratis) | validazione JSON/YAML, routing bus, aggregazione metriche, file ops, rename | tutto ciò che è deterministico NON tocca un LLM |
| **1** | Haiku | qualifica lead, tagging, estrazione dati, meta description, alt-text, QA checklist semplici, classificazione messaggi bus | default per classificazione/estrazione |
| **2** | Sonnet | copy standard (email, post, caroselli), codice, ricerca, report, qualifica complessa, draft preventivi | default produzione |
| **3** | Opus | sales page APSOC, preventivi finali (beast-preventivi), architettura sistemi, decisioni Board, debugging difficile | SOLO con giustificazione; Cost Sentinel segnala Opus su Tier ≤1 |

Thompson Sampling di Ruflo ottimizza nel tempo dentro questi vincoli; la tabella è il prior e il limite. Ogni run logga `tier_usato` per la cost-attribution.

### 2. Envelope per Reparto

La Guild definisce e aggiorna i budget envelope mensili per ecosistema (base: stima dalle prime run reali F4+):

| Ecosistema | Envelope mensile indicativo | Note |
|---|---|---|
| 01-AGENCY | da misurare F4 | varia con volume outreach |
| 02-INFO-BUSINESS | da misurare F6 | picchi in fase lancio |
| 03-CONTENT-FACTORY | da misurare F5 | scala con volume contenuti |
| 04-MARKETING | da misurare F5 | dipende da volume copy |
| 05-MULTI-BUSINESS | da misurare F7 | picchi per video e KDP |
| 06-PLATFORM | fisso basso | engineering < produzione |
| 07-FORGE | fisso basso | skill creation raramente necessaria |
| 08-INTELLIGENCE | fisso medio | ingestione Empire Studio |
| 09-OPERATIONS | fisso basso | orchestrazione efficiente |
| 10-MEMORY | quasi zero | prevalentemente WASM/Haiku |

Gli envelope vengono fissati dopo le prime 4 settimane di run reale e approvati dal CFO (non si improvvisano — Mandato Art.3.3).

### 3. Soglie Cost Sentinel

La Guild propone le soglie al CFO per approvazione (60/80/95/100% envelope, Opus su Tier ≤1, loop >20 chiamate/min); il CFO le approva; il Cost Sentinel le applica. Variazioni soglie → ADR.

### 4. Dry-run Policy (Pattern #3)

- Ogni workflow con costo stimato > €0.10 per run deve avere dry-run eseguito e documentato prima del run reale
- Il dry-run produce: `{task, tier_usato, n_run_stimati, costo_stimato_totale, envelope_rimanente_post_run}`
- Se il dry-run non è stato fatto → Cost Sentinel blocca il run

### 5. ROI Tracking

La Guild definisce le metriche di ROI per tipo di output:
- **Outreach email**: costo per email generata · costo per reply · costo per lead
- **Contenuto social**: costo per post · engagement rate (se disponibile)
- **Preventivo**: costo di produzione vs revenue potenziale (conversion rate × prezzo)
- **Lancio info-product**: costo totale ecosistema 02 per lancio vs revenue lancio

---

## Deliverable

- **Routing policy YAML** — `company/runtime/cost/routing-policy.yaml` (aggiornato dalla Guild, approvato CFO)
- **Envelope registry** — `company/runtime/cost/envelopes.yaml` (per ecosistema, per brand_kit)
- **Soglie Cost Sentinel** — `company/runtime/cost/sentinel-thresholds.yaml`
- **ROI templates** — metriche standard per tipo di operazione

---

## Come si richiede supporto alla Guild

```json
{
  "from": "<ecosistema_richiedente>",
  "to": "Cost-Guild",
  "tipo": "guild_request",
  "sottotipo": "routing_advice | envelope_request | dry_run_review | roi_calc",
  "brief": "workflow WF-OUTREACH-EMAIL su 500 email/giorno — quale tier e quale stima costo?",
  "task_tipo": "email_generation",
  "volume_stimato": 500,
  "brand_kit": "DE | <cliente>",
  "formato_atteso": "stima dry-run + tier raccomandato + costo/unità",
  "deadline": "YYYY-MM-DD"
}
```

---

## KPI

| Metrica | Target |
|---|---|
| Run con tier errato non segnalati | 0 |
| Envelope overrun non previsti | 0 |
| Dry-run saltati non rilevati | 0 |
| Cost attribution completa (agente + ecosistema + brand_kit) | ≥ 95% delle spese |
| Quota task su tier corretto vs policy | ≥ 90% (KPI Backbone §6.1) |

---

## Stato

Struttura creata (F1). Agenti L5 da assegnare in F3 (migrazione asset + registro Identity-HR).
Guild Master disponibile in consultazione manuale (F1-F3): applica routing table §1 a ogni scelta di modello prima del run.
