---
Type: WORKFLOW
Status: Active
Tags: #workflow #advertising #creative #testing #ab-test #L2-2
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-CREATIVE-TEST — Testing Creativo a Matrice

> **Reparto:** L2.2 Advertising · **Owner:** ADS-LEAD
> **Trigger:** richiesta test su matrice copy × visual × audience
> **Output:** verdetto statistico con winner identificato e pattern salvati

---

## Precondizioni obbligatorie

Prima che il workflow parta:
- [ ] Budget test approvato (campo `budget_test_ok_max: true` nel brief)
- [ ] Dimensione campione validata da AN3 (L2.4) prima del lancio
- [ ] Criterio di verdetto predefinito dichiarato (CTR per proxy, CPA come definitivo)
- [ ] Copy varianti già gated da L2.1 (score ≥80 ciascuna)

---

## Passi del workflow

### PASSO 1 — Design della matrice (ADS-LEAD + AD2)

**Agenti:** ADS-LEAD (decisione struttura) + AD2 (assemblaggio)

ADS-LEAD decide la dimensione della matrice in funzione del budget:
- Budget limitato → testa prima il copy (copy × 1 visual × 1 audience), poi visual sul copy winner
- Budget ampio → matrice completa N copy × M visual × K audience

**Regola anti-explosion:** non testare >12 varianti contemporaneamente — il segnale diventa
rumoroso e il budget per variante insufficiente. AD2 propone la matrice; ADS-LEAD approva.

**Output:** matrice pianificata con numero varianti, budget per variante, durata test.

---

### PASSO 2 — Validazione dimensione campione (AN3, L2.4)

**Agente:** AN3 Experiment Designer (L2.4 — prestato)

AN3 verifica: con il budget per variante e la durata pianificata, si raggiungerà la dimensione
campione minima per un verdetto statisticamente valido?

**Soglia minima:** per test CTR: ≥1.000 impressioni per variante; per test conversione:
≥50 conversioni per variante (o budget che le produca).

**Gate AN3:** se la dimensione è insufficiente per il numero di varianti → ADS-LEAD riduce
la matrice o aumenta il budget. Il test non parte senza questo gate.

---

### PASSO 3 — Assemblaggio creative (AD2, fan-out swarm)

**Agente:** AD2 Creative Iterator
**Fan-out:** se N×M > 4 varianti → swarm parallelo, 1 agente per creative (idempotente)

AD2 assembla le creative dalla matrice pianificata.
AD4 (compliance) + AD-QA verificano le varianti prima del lancio test.

---

### PASSO 4 — Setup test in dry-run (AD3)

**Agente:** AD3 Media Buyer

AD3 produce il piano test: N ad set con budget uguale per variante (split uguale per test puro).
`dry_run: true` di default. Budget per variante = budget_test_totale / N varianti.
Regola equità: stesso budget per ogni variante — test invalido se il budget è asimmetrico.

---

### PASSO 5 — Lancio e monitoraggio (approvazione Max → AN2, L2.4)

**Trigger:** approvazione Max (Art.4.3 — obbligatoria anche per test)

Dopo approvazione: test lanciato. AN2 (L2.4) traccia i dati per creative_id in tempo reale.
AD6 monitora i dati in ingresso: segnala se una variante performa insolitamente male
nelle prime 24h (eventuale stop early per proteggere il budget).

---

### PASSO 6 — Verdetto statistico (AN3 + AD6)

**Agenti:** AN3 Experiment Designer (L2.4) + AD6 Creative Analyst

AN3 verifica che il campione predefinito sia stato raggiunto.
AD6 calcola: CTR/CPA per variante, delta percentuale, identifica winner con criterio predefinito.

**Regola anti-rumore:** se la dimensione campione non è ancora raggiunta → verdetto "inconclusivo",
non si dichiara un winner. Mai forzare il verdetto prima del campione minimo.

**Output:** `test_results.json` con winner_id, metriche per variante, pattern identificati.

---

### PASSO 7 — Salvataggio pattern e iterazione (AD6 → AD2)

**Agenti:** AD6 → ReasoningBank → AD2

AD6 scrive i pattern vincenti in `marketing/ads/experiments` e in `marketing/ads/patterns/{icp}`.
AD2 riceve il brief per la prossima iterazione (basata sul winner, con una sola variabile modificata).

---

## Gates di uscita

| Gate | Agente | Soglia | Esito fail |
|---|---|---|---|
| **AN3 dimensione campione** | AN3 (L2.4) | Campione minimo predefinito raggiunto | Dichiarazione "inconclusivo"; test continua o stop |
| **Verdetto con criterio predefinito** | AD6 | Winner dichiarato solo con criterio pre-impostato (no cherry-picking post-hoc) | Inconclusivo se criterio non soddisfatto |
| **Approvazione Max per lancio** | Max (umano) | ok esplicito in state.json | Test non parte |

---

## Handoff contract

**Input:**
```json
{
  "campaign_id": "campo popolato a runtime",
  "copy_varianti": "array copy gated (score ≥80)",
  "visual_asset": "array visual da 03-CF",
  "segmenti_audience": "array da AD1",
  "budget_test_EUR": "campo popolato a runtime",
  "budget_test_ok_max": true,
  "criterio_verdetto": "CTR | CPA | conversioni",
  "durata_giorni": "campo popolato a runtime"
}
```

**Output:**
```json
{
  "test_id": "campo popolato a runtime",
  "winner_id": "creative_id vincitore",
  "criterio_applicato": "CPA | CTR",
  "delta_winner_vs_media": "% di miglioramento",
  "campione_sufficiente": true,
  "pattern_salvati": "array pattern scritti in namespace",
  "raccomandazione_iterazione": "prossima variabile da testare"
}
```

---

## Esempio operativo

**Scenario:** test su Meta. 3 hook copy (da L2.1), 2 visual (da 03-CF), 1 audience. Budget test: 600 EUR.

**Strategia matrice:** primo ciclo testa solo il copy (3 copy × 1 visual × 1 audience = 3 varianti).
Budget per variante: 200 EUR. AN3 valida: 200 EUR su Meta produce ~1.200 impressioni/variante a
CPM tipico — sufficiente per CTR proxy. Test dura 5-7 giorni.

Winner: COPY-V2 CTR 1.49% vs COPY-V1 0.87% vs COPY-V3 0.92%.
Secondo ciclo: 1 copy winner × 2 visual × 1 audience = 2 varianti. Budget: 400 EUR.

---

## Connessioni

- [[WF-ADS-CAMPAIGN]] · `workflow/WF-ADS-CAMPAIGN.md`
- [[WF-ADS-PERFORMANCE]] · `workflow/WF-ADS-PERFORMANCE.md`
- [[ad2-creative-iterator]] · `agenti/ad2-creative-iterator.md`
- [[ad6-creative-analyst]] · `agenti/ad6-creative-analyst.md`
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.2`
