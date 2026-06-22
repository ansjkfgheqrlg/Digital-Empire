---
Type: SKILLS
Status: Active
Tags: #skills #ricerca #icp #market-audit #competitor #A1
Created: 2026-06-22
Last updated: 2026-06-22
---

# Skill — A1 Ricerca & Market Intelligence

> Mappa delle skill del reparto: skill esistenti mappate (wrappate) + regola anti-contraddizione.
> A1 wrappa skill esistenti (ADR-003): non ne forgia di nuove se una esistente già copre il caso.

---

## Skill esistenti mappate ad A1

### `icp-radar` — ICP Profiler [WRAPPA-ESISTENTE]

**Funzione:** crea/aggiorna profili ICP per nicchia. Definisce target, fonti, criteri di qualifica.
**Owner agente:** AG-A1-ICP.
**Quando invocarla:** nicchia nuova (prima dello scraping — R2) o aggiornamento ICP nicchia attiva.
**Input:** `{nicchia, segnali_mercato, fonti}` · **Output:** profilo ICP in `agency/a1/icp` con fonti citate.
**Confine:** alimenta AG-A1-QUAL (soglia di qualifica) e A9/08-INTELLIGENCE.

---

### `market-audit` — Marketing Audit Orchestrator [WRAPPA-ESISTENTE]

**Funzione:** audit marketing del prospect/competitor (presenza, funnel, ads, copy).
**Owner agente:** AG-A1-COMP.
**Quando invocarla:** dossier competitor per prospect specifico (WF-MARKET-INTEL, WF-BRIEF-PRE-CALL).
**Input:** `{url_prospect, url_competitor[]}` · **Output:** audit problema strutturato con fonti.
**Confine:** affianca `competitor.py` + `cro_audit.py`; ogni claim cita la fonte (R4).

---

### `competitor-profiling` — Competitor Dossier [WRAPPA-ESISTENTE]

**Funzione:** profila competitor da URL → dossier strutturato (posizionamento, offerta, prezzi, gap).
**Owner agente:** AG-A1-COMP.
**Quando invocarla:** quando serve un dossier competitor per il brief pre-call o il report nicchia.
**Input:** lista URL competitor · **Output:** profili competitor MD con fonti citate.
**Confine:** input per AG-A1-BRIEF (3 competitor nel dossier) e AG-A1-INTEL (competitor_top3).

---

## Skill esistenti ausiliarie

| Skill | Stato | Ruolo in A1 | Note |
|---|---|---|---|
| `market-competitors` | Esistente | Ausiliaria di AG-A1-COMP per il confronto competitor | Knowledge base; non sostituisce il workflow |
| `competitors` | Esistente | Generazione pagine comparison da profili (downstream) | Owner primario in 04-MARKETING |
| `customer-research` | Esistente | Ausiliaria di AG-A1-ICP per la ricerca avatar/nicchia | Affianca `icp-radar` |

---

## Regola anti-contraddizione

A1 NON forgia skill nuove se una skill esistente già copre il caso (ADR-003, no doppio standard).
Se emerge un bisogno non coperto:
1. Eseguire `skill-contradiction-analyzer` contro `icp-radar`, `market-audit`, `competitor-profiling`.
2. Se sovrapposizione: la nuova IMPLEMENTA/ESTENDE l'esistente, non la ridefinisce.
3. Forgiatura solo via 07-FORGE con PRD esplicito.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §1` — ADR-003 WRAP-not-rewrite
- [[ag-a1-icp]] · `agenti/ag-a1-icp.md` — owner di `icp-radar`
- [[ag-a1-comp]] · `agenti/ag-a1-comp.md` — owner di `market-audit` e `competitor-profiling`
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A1`
