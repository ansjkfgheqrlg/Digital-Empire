---
Type: KPI
Status: Active
Tags: #kpi #CF-R5 #visual #carosello #thumbnail #design #metriche
Created: 2026-06-23
Last updated: 2026-06-23
---

# KPI — CF-R5 Visual & Design / Caroselli

> Tutti i valori target sono `[DM]` (da misurare) fino a baseline reale di 4 settimane.
> Nessun numero inventato (Mandato Art.2 — "prove non promesse").
> La baseline si misura a partire dalla prima produzione reale con pipeline CF-grade completa.

---

## KPI operativi — produzione

| KPI | Owner | Definizione | Direzione | Baseline |
|---|---|---|---|---|
| Caroselli prodotti / ciclo per brand | CF-R5-COORD | N. caroselli con gate verde (GATE-FORMATO + GATE-BRAND PASS) consegnati per brand nel periodo (settimanale) | ↑ | [DM] |
| Thumbnail prodotte / ciclo | CF-R5-COORD | N. thumbnail con gate verde consegnate nel periodo | ↑ | [DM] |
| Grafiche statiche prodotte / ciclo | CF-R5-COORD | N. grafiche one-shot con gate verde consegnate nel periodo | ↑ | [DM] |
| Costo per carosello — Ramo A (AI image) | CF-R5-COORD | Crediti engine AI consumati / n. caroselli prodotti via Ramo A | ↓ | [DM] |
| Costo per carosello — Ramo B (Canva) | CF-R5-COORD | Sempre 0 crediti engine; monitora tempo operatore Canva MCP | — | 0 crediti |
| Costo per carosello — Ramo C (render.mjs) | CF-R5-COORD | Sempre 0 crediti engine; monitora tempo render locale (s) | — | 0 crediti |
| Lead time brief→deliverable (min) | CF-R5-COORD | Ore dalla ricezione brief.json al GATE-BRAND PASS; per ramo | ↓ | [DM] |
| Varianti multi-formato per ordine | CF-R5-RESIZE | N. medio formati prodotti per ordine; target: tutti i formati dichiarati nell'ordine | → target ordine | [DM] |

---

## KPI qualità — gate

| KPI | Owner | Definizione | Soglia tecnica | Baseline |
|---|---|---|---|---|
| GATE-FORMATO first-pass rate | CF-R5-QA | % ordini che superano GATE-FORMATO al primo tentativo (senza rework) | ↑ | [DM] |
| GATE-BRAND first-pass rate | CF-R5-QA | % ordini che superano GATE-BRAND al primo tentativo | ↑ | [DM] |
| Dimensioni conformità | CF-R5-QA | % PNG con dimensioni nei ±2px tolleranza; target 100% | 100% | — |
| Peso conformità | CF-R5-QA | % PNG sotto soglia peso (< 8MB carosello; < 2MB thumbnail YT) | 100% | — |
| Contrasto testo conformità | CF-R5-QA | % PNG con rapporto contrasto ≥ 4.5:1 su tutti gli elementi testuali | 100% | — |
| Safe-area conformità | CF-R5-QA | % PNG senza elementi testuali/logo nei 72px di margine | 100% | — |
| N. rework per ordine (media) | CF-R5-QA | Media rework per ordine nel periodo; 0 è il target | ↓ | [DM] |
| % ordini con secondo FAIL (entry cf/failures) | CF-R5-QA | N. ordini con ≥2 rework falliti / tot ordini; ogni entry indica un pattern da risolvere | ↓ | [DM] |

---

## KPI asset library

| KPI | Owner | Definizione | Baseline |
|---|---|---|---|
| Asset brand caricati su Canva per brand | CF-R5-ASSET | N. asset_id attivi in `canva-asset-index.json` per brand | [DM] |
| % template Canva attivi per brand | CF-R5-COORD | N. brand con tutti e 4 i template Canva / tot brand attivi; target 100% | [DM] |
| Indice desincronizzato (spot-check mensile) | CF-R5-ASSET | N. asset_id in indice non trovati in Canva; target 0 | [DM] |

---

## KPI apprendimento (CF-R5-LEARN)

| KPI | Owner | Definizione |
|---|---|---|
| Pattern visual validati / mese | CF-R5-LEARN | N. pattern con ≥5 casi in `cf/patterns` per il reparto visual |
| % asset con dati feedback a 7gg | CF-R5-LEARN | N. asset con metriche engagement a 7gg / tot asset pubblicati |
| CTR medio thumbnail per brand (evoluzione) | CF-R5-LEARN | Media `ctr_thumbnail_7gg` per brand_slug per mese; [DM] baseline |
| Engagement rate medio carosello per brand | CF-R5-LEARN | Media `engagement_rate_7gg` per brand_slug per mese; [DM] baseline |
| % Concept A scelto vs B vs C | CF-R5-LEARN | Distribuzione scelte committente nei thumbnail; usato per calibrare default |

---

## Dashboard (alimentazione)

Namespace sorgenti per dashboard CF-Director:
- `cf/design` → stato ordini design: fase corrente, ramo attivo, gate risultati
- `cf/thumbnails` → stato ordini thumbnail: concept scelto, variante A/B selezionata, CTR 7gg
- `cf/graphics` → stato ordini grafiche statiche: formato, canale, delivery
- `cf/patterns` → pattern engagement visual per brand/formato (da CF-R5-LEARN via CF-R7-FEEDBACK)

Dashboard aggiornata dopo ogni ordine CF-R5 chiuso (CF-R5-COORD aggiorna `cf/kpi`).

---

## Connessioni

- [[cf-r5-coord]] · `agenti/cf-r5-coord.md` — owner KPI operativi e produzione
- [[cf-r5-qa]] · `agenti/cf-r5-qa.md` — owner KPI gate qualità
- [[cf-r5-asset]] · `agenti/cf-r5-asset.md` — owner KPI asset library
- [[cf-r5-learn]] · `agenti/cf-r5-learn.md` — owner KPI apprendimento e feedback
