---
Type: CONCEPT
Status: Active
Tags: #scripts #cro #automazione #pipeline
Created: 2026-06-17
Last updated: 2026-06-17
---

# SCRIPTS — CRO (Chief Revenue Officer)

> Directory degli script di supporto al team CRO. La maggior parte degli script del CRO
> sono wrapper attorno agli script operativi di 01-AGENCY (che NON vengono modificati).
> Blueprint: `company/Board-CSuite/_BLUEPRINT/BP-CRO.md`.

---

## Stato attuale: V2-2 (progettato, non ancora implementato)

Gli script elencati qui sono il target architetturale. Vengono implementati nella fase di
build V2-6 (AGENCY + CRO operativo). Quelli marcati [WRAPPA-ESISTENTE] si appoggiano a
script Agency già esistenti; quelli marcati [TARGET-V2] sono nuovi.

---

## script-pipeline-snapshot.py [TARGET-V2]

**Scopo:** raccoglie lo snapshot pipeline Agency per stadio e lo struttura in JSON per
`cro-pipeline-health` e `cro-agency-pipeline`.

**Input:** lettura da `agency/leads/`, `agency/03-preventivi/state.json`, log outreach.
**Output:** `board/cro/pipeline/snapshot-YYYYMMDD.json` con n. deal per stadio.
**Cadenza:** settimanale (trigger manuale o schedulato).
**Owner:** `cro-pipeline-health`

```python
# Struttura target (non implementato)
# pipeline_snapshot = {
#   "data": "YYYY-MM-DD",
#   "lead_qualificati": 0,
#   "outreach_attivo": 0,
#   "risposta_positiva": 0,
#   "preventivo_inviato": 0,
#   "in_chiusura": 0,
#   "contratto_firmato_mese": 0
# }
```

---

## script-deal-archiver.py [TARGET-V2]

**Scopo:** archivia ogni deal chiuso (win o loss) in `board/cro/deals/` con tutti i metadati
richiesti da `cro-memoria`. Garantisce integrità (nessun duplicato, nessun PII grezzo).

**Input:** notifica di chiusura deal da A3 o A8-Agency (JSON strutturato).
**Output:** record in `board/cro/deals/DEAL-NNN.json` + aggiornamento indice.
**Trigger:** ogni chiusura deal (win o loss).
**Owner:** `cro-memoria`

---

## script-forecast-builder.py [TARGET-V2]

**Scopo:** aggrega i dati di input dalle 3 fonti (pipeline, lanci IB, retention) e applica
il modello 3 scenari per produrre il documento forecast JSON.

**Input:** JSON da `cro-pipeline-health`, `cro-infobusiness-launches`, `cro-retention-revenue`.
**Output:** `board/cro/forecast/forecast-QN-YYYY.json`.
**Cadenza:** trimestrale (avviato da `cro-conductor` nel WF-FORECAST).
**Owner:** `cro-forecast-analyst`

---

## script-catalogo-versioner.py [TARGET-V2]

**Scopo:** gestisce le versioni del catalogo prezzi. Ogni modifica approvata dal lotto crea
una nuova versione; la precedente viene marcata "superseded". Garantisce atomicità: mai
due versioni "attive" contemporaneamente.

**Input:** dossier B-003 approvato (JSON con nuovi prezzi + metadati approvazione).
**Output:** `board/cro/pricing/catalogo-corrente.json` (aggiornato) + archivio versione precedente.
**Trigger:** solo dopo ok lotto nel WF-PRICING.
**Owner:** `cro-pricing-arbiter`

---

## script-cross-sell-scanner.py [TARGET-V2]

**Scopo:** scansiona la lista acquirenti di un lancio IB e applica il modello di scoring
compatibilità ICP Agency. Produce la lista ordinata per `cro-cross-sell-mapper`.

**Input:** lista acquirenti lancio (da 02-IB), lista clienti Agency attivi (da A7), storico
outreach 90gg (da `cro-memoria`).
**Output:** `board/cro/cross-sell/LANCIO-NNN-candidates.json` ordinato per score.
**Cadenza:** entro 48h da ogni lancio IB chiuso.
**Owner:** `cro-cross-sell-mapper`

---

## Dipendenze (script Agency — [WRAPPA-ESISTENTE, NON MODIFICARE])

Il CRO usa i dati prodotti da questi script Agency senza modificarli:

| Script Agency | Uso nel CRO | Owner Agency |
|---|---|---|
| `agency/03-preventivi/state.json` | Input per pipeline snapshot | A3-Agency |
| `agency/02-acquisizione/*/state.json` | Dati outreach per pipeline | A2-Agency |
| `agency/04-delivery/state.json` | Clienti in delivery (retention) | A4-Agency |
| `leads.db` | Pool lead qualificati (count per cross-sell) | A1-Agency |

**REGOLA FERREA:** gli script CRO leggono i file Agency, MAI scrivono in directory Agency.
Ogni modifica all'ecosistema Agency passa dai handoff contract definiti in `ARCHITETTURA.md`.

---

## Connessioni

- [[ARCHITETTURA]] · `company/Board-CSuite/CRO/ARCHITETTURA.md`
- [[cro-pipeline-health]] · `agenti/cro-pipeline-health.md`
- [[cro-forecast-analyst]] · `agenti/cro-forecast-analyst.md`
- [[cro-pricing-arbiter]] · `agenti/cro-pricing-arbiter.md`
- [[cro-memoria]] · `agenti/cro-memoria.md`
- [[cro-cross-sell-mapper]] · `agenti/cro-cross-sell-mapper.md`
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md`
