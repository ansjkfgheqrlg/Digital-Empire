---
Type: SKILLS
Status: Active
Tags: #skills #infobusiness #prodotto #mkd #curriculum #IB-L2-PROD
Created: 2026-06-21
Last updated: 2026-06-21
---

# Skill — IB-L2-PROD Produzione Prodotti

> Mappa delle skill del reparto: skill proprie da forgiare + skill esistenti mappate.

---

## Skill proprie del reparto (da forgiare via 07-FORGE — standard §8 V2)

### `course-architect` — Priorità P1

**Funzione:** trasforma un MKD in curriculum standardizzato con outcome verificabili per lezione,
prerequisiti, durata stimata ed esercizio pratico per ogni lezione. Formalizza la logica di IB-PROD-CURRIC.

**Quando invocarla:** quando IB-PROD-MKD ha consegnato un MKD gated (100% atomi) e serve la struttura
moduli/lezioni prima della scrittura degli script.

**Input:**
```json
{"prodotto_id": "...", "mkd_path": "infobusiness/prod/corso/MKD-{prodotto}.md",
 "formato": "corso | ebook", "icp": "...", "durata_target_h": 0}
```
**Output:**
```json
{"curriculum_path": "infobusiness/prod/corso/CURRIC-{prodotto}.md",
 "moduli": [{"id": "M1", "lezioni": [{"id": "L1", "outcome": "...", "esercizio": "...", "durata_min": 0}]}],
 "durata_totale_stimata_h": 0, "outcome_map_completa": true}
```
**Dipendenze:** richiede MKD gated da IB-PROD-MKD prima dell'invocazione.
**PRD da produrre prima della build:** via 07-FORGE, contradiction-analyzer contro
`prd-architect-os` e `book-to-skill` (skill ausiliarie esistenti mappate qui).

---

### `mvp-validator` — Priorità P3

**Funzione:** struttura e traccia l'MVP test 7gg di WF-VALIDAZIONE: genera il template del test
(domanda, ICP target, canale, soglia 5 "sì lo comprerei") e registra le risposte reali. Formalizza
la parte MVP della logica di IB-PROD-VALID.

**Quando invocarla:** quando un'idea ha superato Gate 1 (score ≥60) e serve eseguire il test reale.

**Input:**
```json
{"idea_id": "...", "score": 0, "icp_target": "...", "canale_test": "...", "data_inizio": "YYYY-MM-DD"}
```
**Output:**
```json
{"mvp_id": "...", "risposte_raccolte": 0, "si_comprerei": 0, "soglia": 5,
 "gate_2": "PASS | FAIL | in_corso", "data_chiusura": "YYYY-MM-DD"}
```
**Dipendenze:** richiede score Gate 1 ≥60 come precondizione; non si invoca su idea sotto soglia.
**PRD da produrre prima della build:** via 07-FORGE, contradiction-analyzer contro `customer-research`.

---

## Skill esistenti mappate a IB-L2-PROD

| Skill | Stato | Ruolo in IB-L2-PROD | Note |
|---|---|---|---|
| `content-forge` | Esistente, mappata | Motore primario raw → MKD per IB-PROD-MKD (WF-CORSO + WF-EBOOK) | Espande, non sintetizza; copertura 100% atomi è il vincolo |
| `book-to-skill` | Esistente, mappata | Strutturazione di PDF lunghi (Manuale Claude Code 203pp) per IB-PROD-EBOOK | Ausiliaria di `course-architect`; non sostituisce IB-PROD-CURRIC |
| `prd-architect-os` | Esistente, mappata | Strutturazione gerarchica contenuti per IB-PROD-CURRIC | Ausiliaria: fornisce pattern di struttura, non l'outcome map |
| `customer-research` | Esistente, mappata | Definizione ICP e MVP test per IB-PROD-VALID (WF-VALIDAZIONE) | Owner ICP a monte in IB-L2-STRA; qui usata per il test |
| `printing-press` | Esistente | Impaginazione/export ebook per IB-PROD-EBOOK + IB-PROD-DESIGN | Usata come servizio nella fase impaginazione PDF/ePub |

---

## Regola anti-contraddizione

Prima di forgiare `course-architect` e `mvp-validator`:
1. Eseguire `skill-contradiction-analyzer` contro `prd-architect-os`, `book-to-skill`, `customer-research`.
2. Se sovrapposizione rilevata: la skill nuova IMPLEMENTA/ESTENDE quella esistente, non la ridefinisce.
3. Gerarchia: skill nuova = motore di area; skill esistente = ausiliaria o knowledge base.

---

## Connessioni

- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md §IB-L2-PROD` — skill area
- [[WF-CORSO]] · `workflow/WF-CORSO.md` — usa `course-architect` + `content-forge`
- [[WF-VALIDAZIONE]] · `workflow/WF-VALIDAZIONE.md` — usa `mvp-validator`
- [[07-BACKBONE-RUFLO-SKILLS]] · registro skill globale EMPIRE OS
