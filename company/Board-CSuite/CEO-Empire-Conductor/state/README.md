---
Type: CONCEPT
Status: Active
Tags: #ceo #state #namespace #memoria #agentdb
Created: 2026-06-17
Last updated: 2026-06-17
---

# STATE — Schema dello Stato della Figura CEO / Empire-Conductor

> Namespace AgentDB: `board/ceo`
> Connessioni: [[ceo-memoria]] · [[ceo-okr-tracker]] · [[ceo-verificatore]] · [[SCRIPTS]]

---

## Panoramica

Lo stato della figura CEO è mantenuto in due livelli:

1. **AgentDB namespace `board/ceo`** — stato in-memory per le sessioni attive. Accessibile
   da tutti gli agenti del team CEO in lettura; solo `ceo-memoria` scrive le chiavi di storico.
2. **File system `state/`** — stato persistente tra sessioni. I file JSON in questa cartella
   sono la fonte di verità per gli script e per il `ceo-verificatore`.

---

## Schema namespace `board/ceo` (AgentDB)

| Chiave | Tipo | Owner (chi scrive) | Chi legge | Cosa contiene |
|---|---|---|---|---|
| `board/ceo/stato-holding` | JSON snapshot | `ceo-memoria` | tutti gli agenti CEO | Snapshot STATO-EMPIRE al momento del load |
| `board/ceo/adr-attivi` | array of string | `ceo-memoria` | `ceo-conductor`, `ceo-analista-strategico`, `ceo-advisor-rischi` | Lista ADR attivi con sintesi |
| `board/ceo/sessione-corrente` | JSON | `ceo-conductor` | tutti | Input della sessione Board corrente, fase, agenti attivati |
| `board/ceo/decisioni-pendenti` | array of JSON | `ceo-conductor` | `ceo-analista-strategico`, `ceo-priorita-arbiter` | Decisioni aperte non ancora votate |
| `board/ceo/voti-raft` | JSON | `board-consensus` skill | `ceo-conductor`, `ceo-memoria` | Registro voti della sessione corrente |
| `board/ceo/direttive-dispatch` | array of JSON | `ceo-comunicatore` | `ceo-verificatore` | Handoff dispatched con stato (inviato/confermato/completato/scaduto) |
| `board/ceo/okr-trimestre` | JSON | `ceo-okr-tracker` | `ceo-conductor`, `ceo-analista-strategico` | OKR correnti + progress + stato |
| `board/ceo/budget-envelope` | JSON | `ceo-budget-allocator` | `ceo-conductor`, `ceo-budget-allocator` | Envelope di spesa approvati per ecosistema |
| `board/ceo/alerts` | array of JSON | `ceo-verificatore` | `ceo-conductor` | Alert aperti (non-esecuzione, scaduti, pattern) |

---

## Schema file system `state/` (persistente)

```
state/
├── direttive-dispatch/
│   ├── HC-CEO-CMO-YYYYMMDD-001.json   ← un file per handoff
│   ├── HC-CEO-COO-YYYYMMDD-001.json
│   └── ...
├── okr-trimestre/
│   ├── okr_correnti.json              ← OKR attivi del trimestre in corso
│   ├── aggregato_YYYYMMDD.json        ← ultimo aggregato progress
│   ├── mancanti_YYYYMMDD.json         ← ecosistemi senza risposta
│   └── archivio/
│       ├── Q1-2026_okr.json           ← OKR storico trimestri passati
│       └── Q2-2026_okr.json
├── alerts/
│   ├── YYYYMMDD_HHMM_alert.json       ← un file per alert prodotto da verify_execution.ps1
│   └── ...
├── sessioni/
│   ├── sessione_YYYYMMDD_001.json     ← input/output di ogni sessione Board
│   └── ...
└── budget-envelope/
    ├── envelope_Q2-2026.json          ← envelope trimestre corrente per ecosistema
    └── archivio/
        └── envelope_Q1-2026.json
```

---

## Schema dei file chiave

### `state/direttive-dispatch/<handoff_id>.json`
```json
{
  "handoff_id": "HC-CEO-CMO-20260617-001",
  "da": "CEO / Empire-Conductor",
  "a": "CMO",
  "tipo": "directive",
  "payload": {
    "decisione_sintetica": "string",
    "istruzione_operativa": "string",
    "acceptance_criteria": ["string"],
    "deadline": "YYYY-MM-DD"
  },
  "stato": "inviato | confermato | in_esecuzione | completato_verificato | scaduto | ac_non_soddisfatti",
  "timestamp_dispatch": "ISO8601",
  "timestamp_conferma": "ISO8601 | null",
  "timestamp_completamento": "ISO8601 | null",
  "verifica_ac": "pass | fail | pending"
}
```

### `state/okr-trimestre/okr_correnti.json`
```json
{
  "trimestre": "Q2-2026",
  "okr": [
    {
      "id": "OKR-Q2-01",
      "descrizione": "string",
      "owner_ecosistema": "01-AGENCY",
      "target": "string (misurabile o stimato con nota)",
      "priorita": 1,
      "stato": "on-track | at-risk | off-track | completato",
      "progress_ultimo": "string",
      "data_ultimo_aggiornamento": "YYYY-MM-DD"
    }
  ]
}
```

### `state/alerts/<timestamp>_alert.json`
```json
{
  "alert_id": "ALERT-YYYYMMDD-NNN",
  "tipo": "non_conferma | scaduto | ac_non_soddisfatti | pattern_sistemico | okr_off_track",
  "handoff_id": "HC-CEO-CMO-20260617-001 | null",
  "okr_id": "OKR-Q2-03 | null",
  "destinatario": "CMO | 04-MARKETING",
  "priorita": "critica | alta | media",
  "stato_alert": "aperto | preso_in_carico | risolto",
  "timestamp_creazione": "ISO8601",
  "nota": "string"
}
```

---

## Lifecycle degli stati

```
HANDOFF: inviato → confermato → in_esecuzione → completato_verificato
                                              └→ scaduto (se deadline superata)
                                              └→ ac_non_soddisfatti (se AC mancano)

OKR: on-track → at-risk → off-track → completato (se target raggiunto)
                        └→ on-track (se il blocco viene risolto)

ALERT: aperto → preso_in_carico → risolto
```

---

## Regole di accesso

- **Scrittura cross-agente:** solo `ceo-memoria` scrive le chiavi di storico (`adr-attivi`,
  `stato-holding`). Gli altri agenti scrivono solo nelle loro chiavi di ownership.
- **Lettura aperta:** tutti gli agenti del team CEO leggono qualsiasi chiave del namespace.
- **Aggiornamento atomico:** ogni aggiornamento di stato (es. da "inviato" a "confermato")
  include il timestamp. Nessun aggiornamento retroattivo.
- **Nessuna cancellazione:** i record di handoff e alert non vengono eliminati, solo archiviati.

---

## Connessioni

- [[ceo-memoria]] · `agenti/ceo-memoria.md`
- [[ceo-verificatore]] · `agenti/ceo-verificatore.md`
- [[ceo-okr-tracker]] · `agenti/ceo-okr-tracker.md`
- [[SCRIPTS]] · `scripts/README.md`
- [[KPI]] · `kpi/KPI.md`
- [[ARCHITETTURA]] · `ARCHITETTURA.md`
