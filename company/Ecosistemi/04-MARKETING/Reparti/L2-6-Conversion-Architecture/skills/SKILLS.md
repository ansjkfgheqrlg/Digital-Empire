---
Type: SKILLS
Status: Active
Tags: #skills #conversion #funnel #cro #marketing #L2.6
Created: 2026-06-18
Last updated: 2026-06-18
---

# Skill — L2.6 Conversion Architecture

> Mappa delle skill del reparto: skill proprie da forgiare + skill esistenti mappate.

---

## Skill proprie del reparto (da forgiare via 07-FORGE — standard §8 V2)

### `conversion-funnel-designer` — Priorità P2

**Funzione:** architettura funnel multi-step con mapping APSOC per stage e brief tecnico
per 06-PLATFORM. Formalizza la logica di CA1+CA2.

**Quando invocarla:** quando un committente richiede un funnel completo nuovo o una
revisione strutturale di un funnel esistente.

**Input:** `{committente, prodotto, obiettivo, icp, awareness_level, canali, deadline}`
**Output:** stage map completa con brief copy per ogni stage + brief tecnico landing per 06-PLATFORM.

**Dipendenze:** richiede avatar ICP in namespace prima dell'invocazione.
**PRD da produrre prima della build:** via 07-FORGE, contradiction-analyzer contro
`market-funnel` (skill ausiliaria esistente mappata qui).

---

### `cro-sprint-runner` — Priorità P3

**Funzione:** esecuzione sprint CRO data-driven: diagnosi collo di bottiglia → variante →
coordinamento test → misurazione. Formalizza la logica di CA4.

**Quando invocarla:** quando AN5 ha prodotto un drop report su funnel live con traffico
sufficiente per un test statistico.

**Input:** `{funnel_id, landing_id, drop_report da AN5, micro_conversion_schema da CA3}`
**Output:** sprint_id + variante disegnata + brief per L2.1 (se copy) + brief per 06-PLATFORM
(se struttura) + coordinamento WF-AB-TEST.

**Dipendenze:** richiede drop report AN5 come input; non si invoca su opinione.
**PRD da produrre prima della build:** via 07-FORGE, contradiction-analyzer contro
`cro` (skill esistente mappata qui).

---

## Skill esistenti mappate a L2.6

| Skill | Stato | Ruolo in L2.6 | Note |
|---|---|---|---|
| `cro` | Esistente, mappata | Motore di ottimizzazione page-level per WF-CRO-SPRINT | La skill `cro-sprint-runner` implementa/estende questa skill; no doppio standard |
| `market-funnel` | Esistente, mappata | Ausiliaria di CA1 Funnel Strategist | Ausiliaria: non sostituisce il workflow CA1, fornisce pattern storici |
| `market-landing` | Esistente, mappata | Strategia landing (Marketing) + implementazione (06-PLATFORM) | La skill copre entrambi i lati; L2.6 usa la parte strategia |
| `ab-testing` | Esistente (L2.4) | Invocata da CA4 via WF-AB-TEST per il disegno statistico del test | Owner primario in L2.4/AN3; L2.6 la usa come servizio |
| `analytics` | Esistente (L2.4) | Invocata da AN5 per l'analisi drop rate | Owner primario in L2.4; L2.6 legge i report come input |

---

## Regola anti-contraddizione

Prima di forgiare `conversion-funnel-designer` e `cro-sprint-runner`:
1. Eseguire `skill-contradiction-analyzer` contro `market-funnel`, `market-landing`, `cro`.
2. Se sovrapposizione rilevata: la skill nuova IMPLEMENTA/ESTENDE quella esistente, non la ridefinisce.
3. Gerarchia: skill nuova = motore; skill esistente = ausiliaria o knowledge base.

---

## Connessioni

- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §6` — skill P2/P3
- [[WF-CRO-SPRINT]] · `workflow/WF-CRO-SPRINT.md` — workflow che usa `cro-sprint-runner`
- [[WF-FUNNEL-DESIGN]] · `workflow/WF-FUNNEL-DESIGN.md` — workflow che usa `conversion-funnel-designer`
- [[07-BACKBONE-RUFLO-SKILLS]] · registro skill globale EMPIRE OS
