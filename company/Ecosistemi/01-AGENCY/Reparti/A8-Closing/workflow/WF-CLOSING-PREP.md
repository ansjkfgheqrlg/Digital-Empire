---
Type: PROJECT
Status: Active
Tags: #workflow #agency #closing #sales-call #prep #A8
Created: 2026-07-11
Last updated: 2026-07-11
---

# WF-CLOSING-PREP — Preparazione call di chiusura

> **Reparto:** A8 Closing / Sales-Call · **Owner:** AG-A8-COORD · **Gate:** AG-A8-QA (bloccante)
> **Scopo:** consegnare a Max, **≥2h prima** di ogni call, un dossier pre-call completo e a-prova.
> **Standard:** CF-grade (ADR-007) · **Namespace:** `agency/a8/prep/{call_id}/`

---

## 1. Trigger

| Condizione | Sorgente | Handoff |
|---|---|---|
| Call prenotata (discovery o closing) | A2 Acquisizione — `ag-a2-book` | `HC-AG-CL-01` |
| Preventivo inviato disponibile | A3 Preventivi — `ag-a3-prop` | Lettura `agency/a3/{preventivo_id}` |
| Dossier lead disponibile | A1 Ricerca — `ag-a1-brief`, `ag-a1-icp` | Lettura `agency/a1/dossier/{lead_id}` |

**Precondizione bloccante (R1):** per una call di tipo `closing`, senza `preventivo_id` valido il
workflow **non parte**. Una call di chiusura senza preventivo non ha oggetto → AG-A8-COORD escala ad
AG-DIR. Per una `discovery` il preventivo non è richiesto (non esiste ancora).

**Precondizione temporale (R6):** il workflow deve poter completare **≥2h prima** di
`call_datetime`. Se al momento del trigger mancano già meno di 2h, non si "corre di più": si dichiara
la call **scoperta** (KPI K9), si informa Max e si escala.

---

## 2. Step

### Step 0 — Validazione trigger e recall (AG-A8-COORD)

- Verifica: `call_id`, `lead_id`, `call_datetime`, `preventivo_id` (se closing), fonti A1/A3 leggibili.
- `memory_search("agency/a8/patterns")` → obiezioni ricorrenti su questo ICP/prodotto.
- `memory_search("agency/a8/calls")` → esiti su lead simili; leve che hanno chiuso.
- `memory_search("agency/a8/scripts")` → varianti di script con win su questo ICP.
- **Crea** `agency/a8/prep/{call_id}/state.json` con `qa_gate: pending`.

**Uscita:** state creato, contesto storico caricato. **Se una fonte obbligatoria manca → escalation, stop.**

---

### Step 1 — Aggregazione dossier (AG-A8-PREP)

Costruisce `dossier.md` a **8 blocchi**, nessuno vuoto:

| # | Blocco | Fonte |
|---|---|---|
| 1 | Chi è il prospect (profilo + ICP) | A1 `ag-a1-brief`, `ag-a1-icp` |
| 2 | Problema quantificato (numeri; `[DM]` se stimati) | A1 audit + A3 |
| 3 | Cosa abbiamo proposto (prodotto, scope, **prezzo a catalogo**) | A3 `ag-a3-prop` — **verbatim** |
| 4 | Prove disponibili (1 prova per ogni promessa) | A3 + A1 |
| 5 | Obiezioni attese + risposta a-prova | AG-A8-OBJ (Step 2a) |
| 6 | Script call (apertura → discovery → scope → chiusura → uscita NO) | AG-A8-SCRIPT (Step 2b) |
| 7 | **Cosa NON promettere** (claim senza prova, marcati `[DM]`) | AG-A8-PREP |
| 8 | Prossimo passo (se win → A4; se loss → A3 follow-up) | AG-A8-PREP |

**Vincoli:** preventivo citato verbatim (ADR-003); ogni promessa mappata su una prova, altrimenti
`[DM]` + blocco 7; prezzo **identico** al catalogo fisso (B-003) o stop.

---

### Step 2 — PARALLELO

#### 2a — Obiezioni attese (AG-A8-OBJ)

- Recall obiezioni **realmente emerse** (`agency/a8/patterns/obiezioni/`) prima di simularne di nuove.
- Carica la libreria obiezioni di **A5** (`ag-a5-obj`) filtrata su ICP + prodotto + awareness.
- Copre almeno: **prezzo, timing, fiducia/rischio, attrito interno (decisore multiplo)**.
- Per ogni obiezione: **risposta a-prova** con prova citata. Senza prova → `[DM]`, **nessuna risposta
  scritta**, gap ad AG-A8-LEARN.
- **Filtro anti-pressione:** nessuna scarsità artificiale, urgenza fabbricata, sconto (R4, R5).

**Output:** `obiezioni.json` → blocco 5 + input al blocco 7.

#### 2b — Script personalizzato (AG-A8-SCRIPT)

- Wrappa lo **script standard di A5** (`ag-a5-script`); dichiara il `delta_vs_standard`.
- Calibra sull'**awareness level**: basso → diagnosi lunga, soluzione tardi; alto → scope e prove subito.
- Ogni promessa nello script punta a una prova del blocco 4, o **esce dallo script**.
- **Chiusura senza pressione** + **uscita NO** obbligatoria (un no pulito vale più di un sì strappato).
- `brand_voice_check` → `conforme` o il gate blocca.

**Output:** `script.md` → blocco 6.

---

### Step 3 — Gate (AG-A8-QA) — BLOCCANTE

Checklist Gate Prep, deterministica (motore: `scripts/gate_precall.py`):

| # | Check | Regola |
|---|---|---|
| 1 | 8 blocchi presenti e non vuoti | R2 |
| 2 | Ogni promessa ha prova citata **o** `[DM]` | R3 |
| 3 | Zero scarsità artificiale / pressione | **R4 — bloccante assoluta** |
| 4 | Prezzi solo da catalogo fisso; zero sconti | R5 |
| 5 | Script conforme Brand Voice | R2 |
| 6 | Dossier pronto **≥2h** prima della call | R6 |
| 7 | Blocco "uscita NO" presente | R2 |
| 8 | Zero PII nello `state.json` | R7 |

- **FAIL** → `qa_cicli++`, note di rework (regola + posizione esatta) ad AG-A8-COORD → ritorno allo
  Step 1/2 per il blocco in errore. **La SLA 2h continua a correre.**
- **2 FAIL consecutivi** → escalation strutturale ad AG-DIR (il problema è a monte: A1/A3).
- **PASS** → `qa_gate: PASS`, via libera allo Step 4.

**Il gate non si negozia con il calendario.** Call fra un'ora + dossier FAIL = call **scoperta**
(escalation + Max informato), **non** consegna forzata.

---

### Step 4 — Consegna a Max (AG-A8-COORD)

- Consegna `dossier.md` a Max con timestamp `consegnato_a_max_at`.
- Registra `sla_2h_rispettata` (true/false) — alimenta K3.
- Da qui in poi **la call è di Max**. A8 non partecipa, non suggerisce in tempo reale, non ascolta.

---

## 3. Gate di uscita

**AG-A8-QA — PASS obbligatorio.** Nessuna eccezione, nessun "PASS con riserva", nessun bypass da
parte di AG-A8-COORD. Il gate è motivato: ogni FAIL cita la regola (R1–R8) e la posizione esatta.

---

## 4. Input / Output

**Input:**
```json
{
  "call_id": "CALL-001",
  "lead_id": "LEAD-001",
  "preventivo_id": "PREV-001",
  "call_type": "discovery | closing",
  "call_datetime": "YYYY-MM-DDTHH:MM:SSZ",
  "fonti": {"a1": "agency/a1/dossier/LEAD-001", "a3": "agency/a3/PREV-001",
             "a5_obiezioni": "ag-a5-obj", "a5_script": "ag-a5-script"}
}
```

**Output:**
```json
{
  "dossier_path": "agency/a8/prep/CALL-001/dossier.md",
  "qa_gate": "PASS",
  "consegnato_a_max_at": "YYYY-MM-DDTHH:MM:SSZ",
  "sla_2h_rispettata": true,
  "prove_mancanti": ["promesse senza prova → [DM], nel blocco 7"]
}
```

---

## 5. Handoff

| Direzione | Controparte | Cosa transita |
|---|---|---|
| ← in | `ag-a2-book` (A2) | Call prenotata + thread (`HC-AG-CL-01`) |
| ← in | `ag-a1-brief`, `ag-a1-icp` (A1) | Dossier lead, problema quantificato, ICP |
| ← in | `ag-a3-prop` (A3) | Preventivo: scope, pricing a catalogo, prove |
| ← in | `ag-a5-obj`, `ag-a5-script` (A5) | Libreria obiezioni + script standard |
| → out | **UMANO (Max)** | Dossier pre-call gated, ≥2h prima della call |
| → out | AG-A8-LEARN | `prove_mancanti` + obiezioni fuori libreria (gap) |
| → out | `WF-CLOSING-DEBRIEF` | `call_id` in attesa di esito |

---

## 6. DONE-WHEN

Il workflow è **DONE** quando **tutte** queste condizioni sono vere:

- [ ] `agency/a8/prep/{call_id}/state.json` esiste con `qa_gate = PASS`.
- [ ] `dossier.md` ha **8 blocchi** compilati, incluso il blocco 7 "cosa NON promettere".
- [ ] Ogni promessa nel dossier ha una **prova citata** oppure è marcata `[DM]` (R3).
- [ ] Zero occorrenze di scarsità artificiale o pressione in obiezioni e script (R4).
- [ ] Ogni prezzo citato corrisponde al **catalogo fisso** B-003 (R5).
- [ ] `script.md` ha `brand_voice_check = conforme` e contiene l'**uscita NO**.
- [ ] `consegnato_a_max_at` ≤ `call_datetime - 2h` → `sla_2h_rispettata = true` (R6).
- [ ] Zero PII in `state.json` e negli artefatti di prep (R7).
- [ ] `prove_mancanti` inoltrate ad AG-A8-LEARN (anche se vuoto: il campo esiste).
- [ ] `call_id` registrato in attesa di debrief (`WF-CLOSING-DEBRIEF` armato).

**NON è DONE se:** il dossier è stato consegnato con gate FAIL, oppure a meno di 2h dalla call,
oppure con un blocco vuoto "tanto Max lo sa". Questi tre casi sono **incidenti**, non varianti.

---

## Connessioni

- [[WF-CLOSING-DEBRIEF]] · `workflow/WF-CLOSING-DEBRIEF.md` — workflow gemello, post-call
- [[ag-a8-qa]] · `agenti/ag-a8-qa.md` — gate di uscita bloccante
- [[REGOLE]] · `regole/REGOLE.md` — R1–R7 applicate in questo workflow
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — §2.1 flusso di preparazione
