---
Type: TOOL
Status: Active
Tags: #state #memoria #agency #closing #namespace #A8
Created: 2026-07-11
Last updated: 2026-07-11
---

# State — A8 Closing / Sales-Call

> Namespace di memoria del reparto: **`agency/a8`**.
> Fonte unica di verità per KPI, gate e ripartibilità a freddo (test amnesia §6 V2).
> **Nessun PII in nessuno schema.** Solo identificatori: `lead_id`, `call_id`, `preventivo_id`.

---

## 1. Namespace

| Namespace | Contenuto | Owner scrittura | Lettori |
|---|---|---|---|
| `agency/a8/prep` | Dossier pre-call, state, esito gate, SLA | **AG-A8-PREP** (+ AG-A8-QA sul campo gate) | COORD, OBJ, SCRIPT, QA, DEBRIEF |
| `agency/a8/calls` | Esiti call: win/loss, motivo, obiezioni emerse, tempi | **AG-A8-DEBRIEF** | COORD, LEARN, QA |
| `agency/a8/scripts` | Libreria script personalizzati per ICP/prodotto + varianti | **AG-A8-SCRIPT** | PREP, LEARN |
| `agency/a8/patterns` | Pattern win/loss, gap di prova, obiezioni fuori libreria | **AG-A8-LEARN** (+ OBJ/DEBRIEF su `gaps/` in append) | COORD, OBJ, SCRIPT, QA |

**Regola di scrittura unica:** ogni chiave ha **un solo owner in scrittura**. Gli altri agenti
leggono. Le eccezioni sono esplicite e append-only (`patterns/gaps/`).

---

## 2. Schema file system

```
agency/a8/
├── prep/
│   └── {call_id}/
│       ├── state.json          # stato macchina del workflow (schema §3)
│       ├── dossier.md          # dossier pre-call, 8 blocchi (owner: AG-A8-PREP)
│       ├── obiezioni.json      # top obiezioni + risposte a-prova (owner: AG-A8-OBJ)
│       └── script.md           # script personalizzato (owner: AG-A8-SCRIPT)
├── calls/
│   └── {call_id}.json          # esito + motivo (OBBLIGATORIO) — owner: AG-A8-DEBRIEF
├── scripts/
│   └── {icp}-{prodotto}/
│       ├── variante-01.md      # variante di script
│       └── esiti.json          # variante → win/loss (correlazione, non causalità)
└── patterns/
    ├── {pattern_id}.json       # pattern consolidato (≥3 evidenze — R8)
    ├── gaps/                   # append-only: prove mancanti, obiezioni fuori libreria A5
    └── obiezioni/              # storico obiezioni realmente emerse per ICP/prodotto
```

---

## 3. Schema `prep/{call_id}/state.json`

```json
{
  "call_id": "CALL-001",
  "lead_id": "LEAD-001",
  "preventivo_id": "PREV-001",
  "call_type": "discovery | closing",
  "call_datetime": "YYYY-MM-DDTHH:MM:SSZ",
  "dossier_status": "in_progress | completo",
  "obiezioni_status": "assente | prodotto",
  "script_status": "assente | personalizzato | conforme_brand_voice",
  "qa_gate": "pending | PASS | FAIL",
  "qa_gate_motivo": "regola violata + posizione esatta (vuoto se PASS)",
  "qa_cicli": 1,
  "sla_2h_rispettata": true,
  "consegnato_a_max_at": "YYYY-MM-DDTHH:MM:SSZ | null",
  "prove_mancanti": ["promessa senza prova → [DM]"],
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

## 4. Schema `calls/{call_id}.json`

```json
{
  "call_id": "CALL-001",
  "lead_id": "LEAD-001",
  "preventivo_id": "PREV-001",
  "esito": "win | loss | da-ricontattare",
  "motivo": "OBBLIGATORIO — parole del prospect, mai l'interpretazione",
  "ipotesi_interna": "opinione di chi ha condotto — campo separato, NON è il motivo",
  "obiezioni_emerse": [{"id": "OBJ-01", "prevista": true, "risposta_ha_funzionato": true}],
  "obiezione_nuova_non_in_libreria": ["testo → gap per A5"],
  "prove_richieste_e_mancanti": ["prova chiesta e non disponibile"],
  "giorni_preventivo_to_decisione": 6,
  "next_step": {"azione": "...", "data": "YYYY-MM-DD", "owner": "A4 | A3 | Max"},
  "entro_2h": true,
  "debrief_chiuso_at": "YYYY-MM-DDTHH:MM:SSZ"
}
```

---

## 5. Lifecycle di una call

```
[A2 HC-AG-CL-01: call prenotata]
        ▼
1. CREATE   AG-A8-COORD → prep/{call_id}/state.json   (qa_gate: pending)
        ▼
2. FILL     AG-A8-PREP → dossier.md                   (dossier_status: in_progress → completo)
            AG-A8-OBJ  → obiezioni.json               (obiezioni_status: prodotto)      ┐ parallelo
            AG-A8-SCRIPT → script.md                  (script_status: personalizzato)   ┘
        ▼
3. GATE     AG-A8-QA → state.json.qa_gate = PASS | FAIL
            FAIL → qa_cicli++ → ritorno allo step 2 (SLA 2h continua a correre)
            2 FAIL consecutivi → escalation AG-DIR
        ▼
4. DELIVER  AG-A8-COORD → consegnato_a_max_at (≥2h prima della call — R6)
        ▼
        ⟨ CALL — umana, condotta da Max. A8 non partecipa. ⟩
        ▼
5. DEBRIEF  AG-A8-DEBRIEF → calls/{call_id}.json      (esito + motivo — entro 2h)
        ▼
6. GATE     AG-A8-QA → motivo popolato? data se da-ricontattare? entro_2h?
            FAIL → la call resta APERTA (R7). Mai chiusa a stima.
        ▼
7. ROUTE    WIN  → A4 Delivery (via A7, HC-AG-AM-01) — solo se calls/{call_id} esiste
            LOSS → A3 (ag-a3-fup + ag-a3-learn) + AG-A8-LEARN → patterns/
        ▼
8. LEARN    AG-A8-LEARN → patterns/ (≥3 evidenze → consolidato; sotto → [DM])
```

**Ripartibilità a freddo:** un agente che rientra a metà legge `state.json` e riprende dallo step
esatto (`dossier_status`, `obiezioni_status`, `script_status`, `qa_gate`) — non ri-aggrega il
dossier da zero. Questo è ciò che rende A8 superabile dal test amnesia.

---

## 6. Regole di accesso

| # | Regola |
|---|---|
| **A1** | **Un solo owner in scrittura per chiave.** Gli altri agenti leggono. Eccezione append-only: `patterns/gaps/`. |
| **A2** | **A8 non scrive fuori da `agency/a8`.** Mai in `agency/a1`, `a2`, `a3`, `a5` (ADR-003 wrap-non-riscrittura). I miglioramenti agli artefatti altrui viaggiano come **proposte** via handoff. |
| **A3** | **Zero PII.** Nessun nome, email, telefono, indirizzo in nessuno schema. Solo `lead_id`, `call_id`, `preventivo_id`, ICP, prodotto. Il campo `motivo` cita le parole del prospect **senza** identificarlo. Un PII rilevato è un FAIL di gate (R7). |
| **A4** | **Integrità `calls`:** nessun record senza `esito` **e** `motivo`. Una call senza motivo non è chiusa, qualunque cosa dica il calendario. |
| **A5** | **`[DM]` obbligatorio** su ogni numero non misurato: baseline, impatti stimati, quantificazioni riportate dal lead. Un numero senza `[DM]` è una promessa: ricade sotto R3. |
| **A6** | **Idempotenza:** rieseguire uno step non duplica record. `call_id` è la chiave; una seconda scrittura aggiorna, non appende. |
| **A7** | **Solo dati verificabili nei pattern:** un pattern pubblicato cita gli `call_id` che lo sostengono. Nessuna evidenza → nessun pattern (R8). |

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — §4 namespace, §6 state e ripartibilità
- [[ag-a8-qa]] · `agenti/ag-a8-qa.md` — verifica l'integrità del namespace a ogni gate
- [[scripts/README]] · `scripts/README.md` — script che operano su questo namespace
