---
Type: SCRIPTS
Status: Planned (target V2)
Tags: #scripts #strategia #intelligence #backlog #scoring #IB-L2-STRA
Created: 2026-06-21
Last updated: 2026-06-21
---

# Script — IB-L2-STRA Strategia & Intelligence

> Script di supporto del reparto. Target V2 — deterministici, nessuna spesa API autonoma.
> Standard: ogni script accetta input strutturato, produce output JSON o MD, nessun side-effect
> senza input esplicito, eseguibile da IB-COORD-STRATEGIA senza approvazione aggiuntiva.

---

## Script pianificati (build in V2)

### `idea-scorer.py`

**Scopo:** calcola lo score deterministico /100 di un'idea sui 5 criteri (20 punti ciascuno:
domanda, gap, fit ICP, fattibilità, revenue). Ogni punteggio richiede un riferimento a fonte;
se un criterio è privo di fonte lo score per quel criterio è 0 + flag `fonte_mancante`.

**Input:** `{idea_id, criteri: {domanda, gap, fit_icp, fattibilita, revenue}, fonti_per_criterio[]}`
**Output:** aggiorna l'idea in `backlog/idee.json` con `score`, `score_breakdown[5]`, `soglia` (scartata|parcheggiata|candidabile|priorita_alta) e `flag[]`.
**Prerequisiti:** nessuno — non inventa dati; segnala i criteri senza fonte invece di assegnare punti.

---

### `fonti-checker.py`

**Scopo:** scansiona un output (idea, dossier, trend report) e verifica che ogni claim di mercato/
competitor abbia una fonte associata in `fonti.json` (URL + data rilevazione). Supporto a IB-STRA-QA
nel gate G-FONTI: produce la lista dei claim privi di fonte da bloccare.

**Input:** `{output_id, claims[], registro_fonti: "intelligence/fonti.json"}`
**Output:** `qa_report_{output_id}.json` con `claim_con_fonte[]`, `claim_senza_fonte[]`,
`metriche_non_etichettate[]` e verdetto `PASS|FAIL` (FAIL se almeno un claim/metrica scoperto).
**Prerequisiti:** registro `fonti.json` popolato dagli step INTEL/COMP.

---

### `roadmap-buffer-validator.py`

**Scopo:** legge la roadmap candidata e verifica i due requisiti del gate WF-ROADMAP-PRODOTTI:
ogni prodotto ha `lead_time_stimato` e ogni coppia di lanci consecutivi ha gap ≥30gg (recovery list).
Produce input strutturato per IB-STRA-QA prima della presentazione al Director.

**Input:** `{roadmap_candidata: [{prodotto, lead_time, data_lancio_pianificata}], buffer_min_gg: 30}`
**Output:** `roadmap_check.json` con `prodotti_senza_lead_time[]`, `coppie_buffer_violato[]` e
verdetto `PASS|FAIL`; se PASS, candidata pronta per `roadmap/roadmap_corrente.md`.
**Prerequisiti:** lead time per prodotto da IB-L2-PROD (capacità reale); calendario lanci da IB-L2-LANC.

---

## Convenzioni

- Tutti gli script producono file in `infobusiness/strategia/` (namespace corretto) — mai fuori.
- Nessuno script fa chiamate API esterne autonome; la ricerca pesante si delega a 08-INTELLIGENCE.
- Nessuno script inventa dati: un dato mancante diventa flag/`[DM]`, mai un valore di comodo (R2).
- Output JSON segue lo schema del namespace corrispondente (vedi `state/README.md`).
- Versione: i file output hanno suffisso `_v{N}`; le idee in `idee.json` si aggiornano, non si duplicano.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace memoria su cui gli script scrivono
- [[WF-PRODUCT-INTELLIGENCE]] · `workflow/WF-PRODUCT-INTELLIGENCE.md` — usa `idea-scorer.py` e `fonti-checker.py`
- [[WF-ROADMAP-PRODOTTI]] · `workflow/WF-ROADMAP-PRODOTTI.md` — usa `roadmap-buffer-validator.py`
- [[SKILLS]] · `skills/SKILLS.md` — `product-idea-scorer` formalizza `idea-scorer.py`
