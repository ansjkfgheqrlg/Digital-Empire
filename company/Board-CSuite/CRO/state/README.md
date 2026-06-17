---
Type: CONCEPT
Status: Active
Tags: #state #cro #namespace #memoria #pipeline
Created: 2026-06-17
Last updated: 2026-06-17
---

# STATE — CRO (Chief Revenue Officer)

> Namespace memoria e struttura state del team CRO. Documenta dove vive ogni dato,
> chi è il owner, la cadenza di aggiornamento e le regole di integrità.
> Blueprint: `company/Board-CSuite/_BLUEPRINT/BP-CRO.md`.

---

## Namespace AgentDB: `board/cro/`

```
board/cro/
├── pipeline/
│   ├── deals-active.json        → deal in corso (id, stadio, agente, data ingresso stadio)
│   ├── snapshot-YYYYMMDD.json   → snapshot settimanale per stadio (prodotto da script-pipeline-snapshot)
│   └── index.json               → indice di tutti gli snapshot
│
├── deals/
│   ├── DEAL-NNN.json            → scheda deal chiuso (win o loss, tutti i metadati)
│   ├── index.json               → indice per prodotto, esito, canale, data
│   └── patterns/
│       └── loss-patterns-QN.md  → analisi motivi loss per trimestre
│
├── pricing/
│   ├── catalogo-corrente.json   → versione attiva del catalogo prezzi
│   ├── changelog.md             → storico ogni modifica (data, approvatore, vecchio→nuovo prezzo)
│   └── istruttorie/
│       └── B003-YYYY-NNN.json   → dossier istruttoria per ogni variazione richiesta
│
├── forecast/
│   ├── forecast-QN-YYYY.json    → forecast trimestrale con 3 scenari
│   ├── retro-QN-YYYY.md         → retrospettiva forecast vs reale a fine trimestre
│   └── changelog.md             → motivi di ritardo consegna (se presenti)
│
├── launches/
│   ├── LANCIO-NNN.json          → scheda lancio IB (pianificato/attivo/chiuso, metriche)
│   └── index.json               → indice per prodotto, data, stato
│
├── cross-sell/
│   ├── LANCIO-NNN-candidates.json → lista lead caldi da lancio, ordinata per score
│   └── conversions.json           → track: cross-sell attivati → esito deal
│
└── retention/
    ├── ltv-registro.json          → LTV per cliente (tutti gli acquisti, Agency + IB)
    ├── churn-alerts.json          → alert churn attivi (client_id, rischio, azione, data)
    └── win-back-pipeline.json     → candidati win-back (inattivi >180gg, score)
```

---

## Regole di integrità state

### Atomicità catalogo
Il file `catalogo-corrente.json` ha sempre esattamente 1 versione "attiva". Ogni modifica
crea una nuova versione; quella precedente viene spostata in `pricing/archivio/v-N.json`
con campo `status: "superseded"` e `data_superseded`. MAI sovrascrivere senza archiviare.

### Nessun PII grezzo
Nessun file in `board/cro/` contiene nome, email, telefono o indirizzo del prospect/cliente
in chiaro. Si usa sempre `client_id` o `lead_id` pseudonimizzato. Il mapping id → dati reali
è in 01-AGENCY (`agency/clients/`) — il CRO legge gli id, non i dati personali.

### Integrità deals
Ogni deal chiuso deve avere campo `motivo` popolato prima di essere archiviato. Il script
`script-deal-archiver.py` rigetta record senza motivo. Il conductor verifica settimanalmente
che `n(deals in pipeline CHIUSI) = n(record in board/cro/deals/)`.

### Forecast immutabile dopo consegna
Una volta che il documento forecast è stato consegnato al CEO (HC-CRO-CEO-01), non viene
modificato retroattivamente. Il confronto vs reale produce un documento `retro-QN-YYYY.md`
separato, non una modifica del forecast originale.

---

## Stato corrente (2026-06-17 — fase V2-2)

| Namespace | Stato | Note |
|---|---|---|
| `board/cro/pipeline/` | DA INIZIALIZZARE | script-pipeline-snapshot.py non ancora implementato |
| `board/cro/deals/` | DA INIZIALIZZARE | Deal precedenti da catalogare retroattivamente |
| `board/cro/pricing/` | DA INIZIALIZZARE | Catalogo corrente da formalizzare in JSON |
| `board/cro/forecast/` | DA INIZIALIZZARE | Primo forecast: Q3-2026 (luglio) |
| `board/cro/launches/` | DA INIZIALIZZARE | Lancio "Manuale Claude Code": bloccato (prezzo TBD) |
| `board/cro/cross-sell/` | DA INIZIALIZZARE | Nessun lancio chiuso ancora |
| `board/cro/retention/` | DA INIZIALIZZARE | Base clienti da popolare dopo prime delivery |

---

## Catalogo prezzi corrente (da formalizzare)

```json
{
  "versione": "v1.0",
  "data_attivazione": "2026-06-17",
  "status": "attivo",
  "approvato_da": "Mandato Art.3",
  "prezzi": {
    "Outreach_Factory": 4000,
    "Content_Factory": 3500,
    "Second_Brain": 2500,
    "Engine_Room": 8000
  },
  "valuta": "EUR",
  "modello": "one-time",
  "canoni_ricorrenti": false
}
```

---

## Connessioni

- [[README]] · `company/Board-CSuite/CRO/README.md`
- [[ARCHITETTURA]] · `company/Board-CSuite/CRO/ARCHITETTURA.md`
- [[cro-memoria]] · `agenti/cro-memoria.md`
- [[cro-pipeline-health]] · `agenti/cro-pipeline-health.md`
- [[cro-pricing-arbiter]] · `agenti/cro-pricing-arbiter.md`
- [[kpi/KPI]] · `company/Board-CSuite/CRO/kpi/KPI.md`
- [[scripts/README]] · `company/Board-CSuite/CRO/scripts/README.md`
