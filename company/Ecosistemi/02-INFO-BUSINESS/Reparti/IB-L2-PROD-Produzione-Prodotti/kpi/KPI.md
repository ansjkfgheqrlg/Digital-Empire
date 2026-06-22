---
Type: KPI
Status: Active
Tags: #kpi #infobusiness #prodotto #produzione #IB-L2-PROD
Created: 2026-06-21
Last updated: 2026-06-21
---

# KPI — IB-L2-PROD Produzione Prodotti

> Metriche del reparto. Baseline storica: [DM] — da misurare al primo prodotto live.
> Nessun numero inventato (Mandato Art.2 + principio P5 del reparto).

---

## KPI operativi

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| Lead time corso | IB-COORD-PRODOTTO | Giorni da brief validato (WF-VALIDAZIONE PASS) → corso live su piattaforma con smoke test verde | [DM] — primo corso live (Vendi la Skill) | [DM] — si stabilisce dopo i primi 2-3 corsi |
| % idee oltre gate validazione | IB-PROD-VALID | n. idee con score ≥60/100 + MVP test PASS / tot idee valutate nel periodo | [DM] | [DM] — cresce con qualità del brief in ingresso |
| Rapporto espansione MKD | IB-PROD-MKD + IB-PROD-QA | lunghezza MKD / lunghezza fonte; deve essere ≥1 (mai sintesi — sempre espansione) | [DM] | ≥1.0 su ogni MKD (vincolo, non target) |
| % gate QA al primo giro | IB-PROD-QA | n. gate QA PASS alla prima iterazione / tot gate del periodo (qualità a monte) | [DM] | progressivo — migliora col volume |
| Difetti smoke test per corso | IB-PROD-QA | n. difetti trovati nello smoke test "studente fantasma" per corso prima del PASS | [DM] | tendente a 0 — i difetti si chiudono a monte |
| Copertura atomi fonte | IB-PROD-QA | % atomi informativi della fonte presenti nel MKD (checklist quantitativa: n. atomi MKD / n. atomi fonte) | [DM] | 100% (R2 — sotto soglia = FAIL automatico) |
| Outcome verificabili per lezione | IB-PROD-CURRIC | % lezioni con 1 outcome misurabile dichiarato + esercizio pratico | [DM] | 100% lezioni con outcome + esercizio |

---

## KPI di qualità del sistema (trasversali al reparto)

| KPI | Owner | Definizione | Target |
|---|---|---|---|
| Gate QA bypass rate | IB-PROD-QA | n. output IB-L2-PROD consegnati senza gate QA / tot output | 0 (gate bloccante R4) |
| Prodotti avviati senza validazione | IB-PROD-VALID | n. prodotti entrati in WF-CORSO/WF-EBOOK senza WF-VALIDAZIONE PASS / tot | 0 (R1 — violazione automatica) |
| Asset con placeholder in produzione | IB-PROD-QA | n. asset (copertina, workbook, ebook) consegnati con placeholder / tot asset | 0 (R6) |
| Claim senza prova in produzione | IB-PROD-QA | n. claim "prove non promesse" non motivati rilevati in gate / tot claim | 0 (Mandato Art.2) |

---

## Come si misurano

- **Lead time corso e % idee oltre gate:** da `infobusiness/prod/validazione/state.json` e
  `infobusiness/prod/corso/state.json` — date `data_avvio`, `data_live`, esito MVP.
- **Rapporto espansione MKD e copertura atomi:** da `idea_scorer.py` / `content_forge_runner.py`
  (quando disponibili) o manuale da IB-PROD-QA sulla checklist quantitativa atomi.
- **Gate QA KPI:** IB-PROD-QA registra ogni gate (PASS/FAIL) nello `state.json` del prodotto.
- **Difetti smoke test:** da `smoke-test-{prodotto}.json` in `infobusiness/prod/corso/`.

---

## Cadenza di revisione

- Gate QA KPI: ad ogni gate chiuso.
- Lead time e % idee: ad ogni prodotto chiuso (corso live o ebook esportato).
- Report di sintesi a IB-0-conductor: settimanale (KPI di area) + a fine ciclo di reparto.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace `infobusiness/prod` dove i KPI vengono scritti
- [[ib-prod-qa]] · `agenti/ib-prod-qa.md` — presidia i gate QA bloccanti
- [[ib-coord-prodotto]] · `agenti/ib-coord-prodotto.md` — aggrega e riporta KPI settimanale a L1
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md §IB-L2-PROD` — KPI area
