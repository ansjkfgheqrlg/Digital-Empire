---
Type: SKILLS
Status: Active
Tags: #skills #agency #copywriting #apsoc #cro-copy-architect #market-copy #A5
Created: 2026-06-23
Last updated: 2026-06-23
---

# Skill — A5 Copywriting Interno

> Mappa delle skill del reparto: skill esistenti mappate (A5 NON forgia skill nuove —
> riusa quelle del knowledge layer). Il Gate Bibbia è un motore condiviso, non una skill di A5.

---

## Skill esistenti mappate a A5

| Skill | Stato | Ruolo in A5 | Note |
|---|---|---|---|
| `cro-copy-architect` | Esistente, mappata | Motore APSOC primario di AG-A5-WRITE e AG-A5-SCRIPT | Framework Attenzione-Problema-Soluzione-Obiezioni-CTA; cuore della scrittura |
| `market-copy` | Esistente, mappata | Ausiliaria di AG-A5-WRITE per template e micro-copy | Suite `market-*`; fornisce pattern e variazioni |
| `cold-email` | Esistente, mappata | Ausiliaria per i template email cold di outreach | Knowledge layer outreach; AG-A5-WRITE la usa per il canale email |
| `agency-scalping` | Esistente, mappata | Contesto agenzia per script call e posizionamento | Brand voice "agenzia progettata per essere licenziata" |
| `copywriting` / `copy-editing` | Esistenti, mappate | Rifinitura e coerenza del copy operativo | Ausiliarie; non sostituiscono APSOC |

---

## Riuso del Gate Bibbia (NON è una skill da forgiare)

Il **Gate Bibbia** (`bibbia_team.py`) è il motore di qualità CONDIVISO con A2-Acquisizione
(pattern 6: una skill, molti reparti). A5 NON lo riscrive e NON lo forgia come skill nuova:

1. AG-A5-QA invoca lo stesso gate di A2 via il wrapper `../A2-Acquisizione/agenti/ag-a2-qa.md`.
2. I criteri di PASS/FAIL sono identici a quelli di A2 — nessun criterio locale (REGOLE R7).
3. Se il gate evolve, evolve in un posto solo (ADR-003 wrap-not-rewrite).

Questo è l'esempio applicato di pattern 6: la qualità del copy operativo dell'agency passa per
un unico gate, indipendentemente dal reparto che produce il messaggio.

---

## Regola anti-contraddizione

A5 non forgia skill proprie: i pezzi grandi (che richiederebbero skill nuove tipo
`sales-page-builder`) sono di 04-MARKETING. Se emerge il bisogno di una skill nuova per copy
operativo:
1. Eseguire `skill-contradiction-analyzer` contro `cro-copy-architect`, `market-copy`, `cold-email`.
2. Se sovrapposizione rilevata: NON si forgia — si usa l'esistente (A5 è adattatore, non factory).
3. Se davvero nuova e operativa → si propone via 07-FORGE con PRD; se è "grande" → va a 04-MARKETING.

---

## Connessioni

- [[ag-a5-write]] · `agenti/ag-a5-write.md` — usa `cro-copy-architect` + `market-copy`
- [[ag-a5-script]] · `agenti/ag-a5-script.md` — usa `cro-copy-architect` per gli script call
- [[ag-a2-qa]] · `../A2-Acquisizione/agenti/ag-a2-qa.md` — Gate Bibbia condiviso (pattern 6)
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A5` — knowledge layer
