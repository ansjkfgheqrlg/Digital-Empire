---
Type: SKILLS
Status: Active
Tags: #skills #agency #delivery #handover #support #A4
Created: 2026-06-23
Last updated: 2026-06-23
---

# Skill — A4 Delivery & Implementazione

> Mappa delle skill del reparto: skill operative esistenti (da wrappare, ADR-003) +
> eventuali skill proprie da forgiare via 07-FORGE.

---

## Skill operative del reparto (esistenti — wrap, non rewrite)

### `delivery-playbook` — operativa

**Funzione:** runbook 7gg per ciascuno dei 3 prodotti (Outreach, Content Factory, Second
Brain). Guida la delivery passo-passo G+0→G+7 con i check di ambiente, parametrizzazione e
training. Formalizza la logica di AG-A4-COORD + AG-A4-TRAIN.

**Quando invocarla:** all'apertura di ogni delivery, dopo l'handoff di A3 con scope congelato.

**Input:** `{delivery_id, prodotto, cliente, scope_congelato, prerequisiti_ambiente}`
**Output:** piano G+0→G+7 + materiale training kit + checklist per ogni step.

**Dipendenze:** scope congelato da A3; profilo ambiente da AG-A4-ENV.
**ADR-003:** la skill wrappa il motore esistente del prodotto, non lo riscrive.

---

### `client-handover` — operativa

**Funzione:** genera il pacchetto di handover: codice completo, README operativo, credenziali
(sul server cliente), licenza d'uso. Formalizza la logica di AG-A4-HAND.

**Quando invocarla:** al G+7, dopo UAT firmata e prima del Gate Delivery.

**Input:** `{delivery_id, prodotto, repo_cliente, runbook, licenza_template}`
**Output:** handover pack completo + manifest di consegna + verifica zero-dipendenza-DE.

**Dipendenze:** UAT firmata da AG-A4-UAT; setup completato da AG-A4-ENV/TENANT.
**ADR-003:** assembla artefatti esistenti, non genera nuovo motore.

---

### `support-90` — operativa

**Funzione:** gestione SLA dei ticket nei 90gg post-handover: triage (bug/domanda/fuori scope),
SLA, log, check proattivo settimanale. Formalizza la logica di AG-A4-SUPP.

**Quando invocarla:** all'ingresso di ogni ticket durante i 90gg + al check settimanale.

**Input:** `{delivery_id, ticket_text, data_ingresso, sla_contratto}`
**Output:** classe ticket + SLA target + stato + (se fuori scope) brief proposta upsell per A6.

**Dipendenze:** delivery chiusa con Gate Delivery PASS; SLA definito nel contratto.
**ADR-003:** wrappa il processo di triage; non sostituisce A7 Account Mgmt per la review 90gg.

---

## Skill candidate da forgiare (target V2, via 07-FORGE)

| Skill | Priorità | Funzione | Nota anti-contraddizione |
|---|---|---|---|
| `delivery-env-check` | P3 | Check conformità ambiente cliente automatizzato (G+0) | Estende `delivery-playbook`, non la ridefinisce |
| `uat-signoff-builder` | P3 | Generazione checklist UAT firmabile + verifica run autonoma | Ausiliaria del Gate Delivery; non sostituisce AG-A4-QA |

---

## Regola anti-contraddizione

Prima di forgiare nuove skill di reparto:
1. Eseguire `skill-contradiction-analyzer` contro `delivery-playbook`, `client-handover`, `support-90`.
2. Se sovrapposizione rilevata: la skill nuova IMPLEMENTA/ESTENDE quella esistente, non la ridefinisce (ADR-003).
3. Gerarchia: skill esistente = motore operativo; skill nuova = ausiliaria o automazione di uno step.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — dove le skill agiscono nei flussi di delivery
- [[WF-DELIVERY-OUTREACH-FACTORY]] · `workflow/WF-DELIVERY-OUTREACH-FACTORY.md` — usa `delivery-playbook` + `client-handover`
- [[WF-SUPPORTO-90GG]] · `workflow/WF-SUPPORTO-90GG.md` — usa `support-90`
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A4` — skill operative del reparto
