---
Type: SKILLS
Status: Active
Tags: #skills #strategia #intelligence #backlog #scoring #IB-L2-STRA
Created: 2026-06-21
Last updated: 2026-06-21
---

# Skill — IB-L2-STRA Strategia & Intelligence

> Mappa delle skill del reparto: skill proprie da forgiare + skill esistenti mappate.

---

## Skill proprie del reparto (da forgiare via 07-FORGE — standard §8 V2)

### `product-idea-scorer` — Priorità P0

**Funzione:** scoring deterministico di un'idea prodotto sui 5 criteri /100 (domanda, gap competitor,
fit ICP, fattibilità produzione, potenziale revenue). Rende il gate idea ripetibile: a parità di dati,
lo stesso punteggio. Formalizza la logica di IB-STRA-BACKLOG e dello script `idea-scorer.py`.

**Quando invocarla:** ogni volta che IB-STRA-BACKLOG integra trend + gap + pain ICP in una bozza idea,
o quando si ri-prioritizza il backlog dopo nuova evidenza.

**Input:** `{idea_id, titolo, criteri: {domanda, gap, fit_icp, fattibilita, revenue}, fonti_per_criterio[]}`
**Output:** `{idea_id, score, score_breakdown[5], soglia, flag_fonte_mancante[], candidabile: bool}`

**Dipendenze:** richiede ICP corrente + gap analysis competitor in namespace prima dell'invocazione.
**PRD da produrre prima della build:** via 07-FORGE, contradiction-analyzer contro
`marketing-ideas` (skill ausiliaria esistente mappata qui — genera angoli, non assegna score).

---

### `intel-source-verifier` — Priorità P2

**Funzione:** verifica che ogni claim di un output STRA abbia fonte reale dichiarata e che nessuna
metrica stimata sia presentata come reale. Formalizza il gate G-FONTI/G-METRICHE di IB-STRA-QA e lo
script `fonti-checker.py`.

**Quando invocarla:** prima di ogni handoff in uscita (idea a PROD, roadmap a Director, dossier).

**Input:** `{output_id, claims[], metriche[], registro_fonti: "intelligence/fonti.json"}`
**Output:** `{verdetto: PASS|FAIL, claim_senza_fonte[], metriche_non_etichettate[], note}`

**Dipendenze:** richiede registro `fonti.json` popolato dagli step INTEL/COMP.
**PRD da produrre prima della build:** via 07-FORGE, contradiction-analyzer contro
`competitor-profiling` (non sostituisce il profiling, ne verifica la tracciabilità delle fonti).

---

## Skill esistenti mappate a IB-L2-STRA

| Skill | Stato | Ruolo in IB-L2-STRA | Note |
|---|---|---|---|
| `marketing-ideas` | Esistente, mappata | Generazione angoli/idee prodotto per IB-STRA-BACKLOG | Ausiliaria: genera candidati; lo score lo assegna `product-idea-scorer` |
| `competitor-profiling` | Esistente, mappata | Profili competitor estesi per IB-STRA-COMP | Ausiliaria: produce il dossier; le fonti le verifica `intel-source-verifier` |
| `icp-radar` | Esistente, mappata | Profilazione e aggiornamento ICP per IB-STRA-ICP | Owner uso in IB-STRA-ICP; alimenta criterio 3 dello score |
| `customer-research` | Esistente, mappata | Voice-of-customer (domande, obiezioni) per ICP e backlog | Input ai segnali community via HC-COMM-STRA-01 |
| `market` | Esistente, mappata | Intelligence di mercato per IB-STRA-INTEL | Ausiliaria: scan trend; ricerca pesante delegata a 08-INTELLIGENCE |

---

## Regola anti-contraddizione

Prima di forgiare `product-idea-scorer` e `intel-source-verifier`:
1. Eseguire `skill-contradiction-analyzer` contro `marketing-ideas`, `competitor-profiling`, `icp-radar`.
2. Se sovrapposizione rilevata: la skill nuova IMPLEMENTA/ESTENDE quella esistente, non la ridefinisce.
3. Gerarchia: skill nuova = motore deterministico (score/gate); skill esistente = generatore o knowledge base.

---

## Connessioni

- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md §IB-L2-STRA` — skill area
- [[WF-PRODUCT-INTELLIGENCE]] · `workflow/WF-PRODUCT-INTELLIGENCE.md` — usa `product-idea-scorer` + `intel-source-verifier`
- [[scripts/README]] · `scripts/README.md` — `idea-scorer.py` e `fonti-checker.py` implementano queste skill
- [[ARCHITETTURA]] · `ARCHITETTURA.md §Skill del reparto` — mapping skill esistenti
