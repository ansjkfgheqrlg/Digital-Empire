---
Type: WORKFLOW
Status: Active
Tags: #workflow #advertising #performance #monitoraggio #iterazione #L2-2
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-ADS-PERFORMANCE — Loop Monitoraggio e Ottimizzazione

> **Reparto:** L2.2 Advertising · **Owner:** ADS-LEAD
> **Trigger:** campagna live (post-lancio) o richiesta diagnosi su campagna esistente
> **Output:** diagnosi + iterazione dal winner + pattern aggiornati in `marketing/ads/experiments`

---

## Premessa: regola anti-rumore

Questo workflow opera su campagne live con dati reali. La regola più importante:
**nessuna decisione di ottimizzazione viene presa senza evidenza sufficiente.**
Modifiche premature su campagne che non hanno ancora raggiunto la fase di apprendimento
(di solito 48-72h post-lancio su Meta) distruggono il segnale. AD6 e AN3 sono i guardiani
di questa regola. ADS-LEAD non modifica una campagna in apprendimento.

---

## Ciclo del workflow (loop continuo)

### CICLO A — Monitoraggio attivo

**Frequenza:** quotidiana nelle prime 2 settimane; poi ogni 3-5 giorni per campagne stabili.

**Agente:** AD6 Creative Analyst (monitoraggio) + AN2 (L2.4, tracciamento dati per copy_id)

AN2 raccoglie: CTR, CPC, CPA, impressioni per creative_id.
AD6 analizza: la performance è nel range atteso? Ci sono segnali di ad fatigue?

**Soglie di allerta automatica:**
- CTR cala >30% rispetto alla media delle prime 48h → alert ad ADS-LEAD
- CPA supera 2× il target per un ad set → alert ad ADS-LEAD (verifica regola stop di AD3)
- Impressioni calano >50% senza cambiamenti (possibile ad fatigue) → alert ad ADS-LEAD

---

### CICLO B — Diagnosi (su alert)

**Agente:** ADS-LEAD + AD6

ADS-LEAD e AD6 diagnosticano la causa del calo:

| Sintomo | Diagnosi probabile | Azione |
|---|---|---|
| CTR in calo + CPA stabile | Ad fatigue — creative vista troppe volte | AD2: nuova variante creative (copy o visual) |
| CTR stabile + CPA in aumento | Qualità audience in calo o bid competition | AD1: nuovo segmento; AD3: aggiusta bid |
| CTR in calo + CPA in aumento | Creative esaurita + mercato sauro | AD2: iterazione dal winner con nuova angolo |
| Performance piattaforma generale giù | Algoritmo cambiato o stagionalità | AD5: aggiornamento note piattaforma |

---

### CICLO C — Iterazione dal winner (AD2)

**Agente:** AD2 Creative Iterator

AD2 riceve dal winner corrente il brief per la prossima variante.
**Regola iterazione:** una sola variabile modificata per ciclo — non si cambia copy + visual
insieme (perde segnale). AD2 propone, ADS-LEAD approva la variabile da modificare.

Se la modifica richiede nuovo copy → richiesta a L2.1/WF-COPY-AD.
Se richiede nuovo visual → richiesta a 03-CF via BR3.

**Gate:** nuova variante passa AD4 (G3 compliance) + AD-QA prima del lancio.
Approvazione Max richiesta anche per varianti in sostituzione (Art.4.3).

---

### CICLO D — Aggiornamento pattern (AD6 → ReasoningBank)

**Agente:** AD6 Creative Analyst

Dopo ogni ciclo con verdetto:
- Pattern vincenti → `marketing/ads/patterns/{icp_piattaforma}`
- Anti-pattern (cosa NON ha funzionato) → `marketing/ads/experiments` con campo `esito: perdente`
- Segnale di ad fatigue → entry separata: "creative X ha esaurito in N giorni su ICP Y"

Questi pattern alimentano il ciclo successivo: AD2 non ripete varianti già testate perdenti.

---

## Gates di uscita del loop

Il loop non ha un gate di uscita fisso: è continuo finché la campagna è attiva.
Si chiude quando: (a) budget esaurito; (b) obiettivo raggiunto; (c) campagna dismessa da ADS-LEAD.

| Condizione | Azione |
|---|---|
| Budget esaurito | ADS-LEAD produce report finale; pattern salvati; stato campagna = `chiusa` |
| CPA stabile e accettabile | Campagna entra in fase di "scaling" (aumento budget con approvazione Max) |
| Campagna non ottimizzabile (2+ cicli senza miglioramento) | ADS-LEAD escalation a MKT-Conductor: prodotto/offerta/ICP da rivedere |

---

## State e tracciamento

Ogni ciclo del workflow aggiorna `marketing/ads/campaigns/{campaign_id}/state.json` con:
- `ciclo_ottimizzazione_n` — numero del ciclo corrente
- `ultimo_alert` — tipo e timestamp dell'ultimo alert
- `diagnosi_corrente` — risultato del ciclo B
- `iterazione_in_corso` — ID della variante in test
- `pattern_consolidati` — n. pattern scritti finora per questa campagna

---

## Handoff contract

**Input (trigger da AN2 o da ADS-LEAD):**
```json
{
  "campaign_id": "campo popolato a runtime",
  "tipo_trigger": "alert_automatico | review_periodica | richiesta_ADS-LEAD",
  "dati_performance": {
    "creative_id": "campo popolato a runtime",
    "ctr_corrente": "campo popolato a runtime",
    "cpa_corrente": "campo popolato a runtime",
    "cpa_target": "campo popolato a runtime",
    "giorni_live": "campo popolato a runtime"
  }
}
```

**Output (per ciclo):**
```json
{
  "campaign_id": "campo popolato a runtime",
  "ciclo_n": "campo popolato a runtime",
  "diagnosi": "ad_fatigue | audience_esaurita | bid_competition | algoritmo_variato",
  "azione_intrapresa": "nuova_variante | aggiustamento_bid | nessuna_azione",
  "variante_iterata": "creative_id nuova variante se lanciata",
  "pattern_aggiornati": true,
  "prossima_review": "YYYY-MM-DD"
}
```

---

## Esempio operativo

**Scenario:** campagna Meta live da 10 giorni. Winner CRE-002. CTR passa da 1.49% (giorni 1-5)
a 0.92% (giorni 6-10).

**AD6 diagnosi:** calo CTR 38% in 5 giorni → segnale di ad fatigue (creative vista troppe volte
dall'audience fredda; frequenza media 3.2 volte per utente nelle ultime 72h).

**Ciclo C:** AD2 itera dal winner CRE-002. Modifica: nuovo visual (foto vs grafica — testate
rispettivamente). Copy invariato. Richiesta a 03-CF per 1 nuovo asset. AD4 + AD-QA verificano.
Approvazione Max. Lancio nuova variante.

**AD6 scrive pattern:** "ad fatigue su Info-Producer Meta: creative si esaurisce in ~7 giorni
a frequenza 3+. Ruotare creative ogni 5-7 giorni per questo ICP."

---

## Connessioni

- [[WF-ADS-CAMPAIGN]] · `workflow/WF-ADS-CAMPAIGN.md`
- [[WF-CREATIVE-TEST]] · `workflow/WF-CREATIVE-TEST.md`
- [[ad6-creative-analyst]] · `agenti/ad6-creative-analyst.md`
- [[ad2-creative-iterator]] · `agenti/ad2-creative-iterator.md`
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.2`
