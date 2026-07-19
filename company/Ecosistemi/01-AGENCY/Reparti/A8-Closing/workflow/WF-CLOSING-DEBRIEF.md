---
Type: PROJECT
Status: Active
Tags: #workflow #agency #closing #sales-call #debrief #learning #A8
Created: 2026-07-11
Last updated: 2026-07-11
---

# WF-CLOSING-DEBRIEF — Debrief e apprendimento post-call

> **Reparto:** A8 Closing / Sales-Call · **Owner:** AG-A8-COORD · **Gate:** AG-A8-QA (bloccante)
> **Scopo:** trasformare ogni call (win o loss) in un record con **motivo**, instradare l'esito e
> restituire il pattern a chi possiede lo strumento (A5, A3, 08-INTELLIGENCE).
> **Standard:** CF-grade (ADR-007) · **Namespace:** `agency/a8/calls/`, `agency/a8/patterns/`

---

## 1. Trigger

| Condizione | Sorgente |
|---|---|
| Max ha concluso la call e comunica l'esito | **UMANO (Max)** → AG-A8-COORD |
| Timer: 2h dalla fine della call senza comunicazione | `scripts/check_sla.py` → sollecito automatico |

**Precondizione:** esiste `agency/a8/prep/{call_id}/` con `qa_gate = PASS` (la call era coperta).
Se la call è stata condotta **senza** dossier gated → è un **incidente K9**: il debrief si fa
comunque, ma la call viene marcata `scoperta: true` e va in escalation ad AG-DIR.

**Finestra (R6):** il debrief si apre e si chiude **entro 2h** dalla fine della call. Oltre le 2h la
memoria dell'esito si riscrive in una storia coerente — e le storie coerenti sono quasi sempre false.

---

## 2. Step

### Step 0 — Raccolta esito (AG-A8-COORD → AG-A8-DEBRIEF)

- AG-A8-COORD riceve la comunicazione di Max (testo libero o vocale trascritto).
- Se non arriva entro 2h → **sollecito**. La call resta **aperta**: non si chiude a stima (R7).
- Assegna AG-A8-DEBRIEF.

---

### Step 1 — Debrief strutturato (AG-A8-DEBRIEF)

Estrae dal testo libero (skill `outreach-reply-triage` + `customer-research`):

| Campo | Regola di estrazione |
|---|---|
| `esito` | `win` \| `loss` \| `da-ricontattare`. **Nessun quarto valore.** "Forse" non è un esito. |
| `motivo` | **OBBLIGATORIO** — con le **parole del prospect**, non la parafrasi. |
| `ipotesi_interna` | L'opinione di Max ("secondo me è il prezzo") va in un campo **separato**: non è il motivo. |
| `obiezioni_emerse` | Quali obiezioni sono uscite davvero; per ognuna: era **prevista**? la risposta a-prova **ha funzionato**? |
| `obiezione_nuova_non_in_libreria` | Obiezioni fuori dalla libreria A5 → gap prezioso. |
| `prove_richieste_e_mancanti` | Prove chieste dal prospect che **non avevamo**: il dato più prezioso della call. |
| `giorni_preventivo_to_decisione` | Alimenta K2 (tempo preventivo→firma). |
| `next_step` | Azione + **data** + owner. Un next step senza data non esiste. |

**Vincolo `da-ricontattare` (R7):** ammesso **solo con una data**. Senza data è un `loss` mascherato
e va registrato come `loss` — altrimenti la pipeline si riempie di zombie che gonfiano K1.

**Output:** `agency/a8/calls/{call_id}.json`.

---

### Step 2 — Gate debrief (AG-A8-QA) — BLOCCANTE

| # | Check | Regola | FAIL se |
|---|---|---|---|
| 1 | `esito` popolato | R7 | Vuoto |
| 2 | **`motivo` popolato** (win **o** loss) | **R7 — bloccante assoluta** | Vuoto → **call NON chiusa** |
| 3 | `da-ricontattare` ha una data nel `next_step` | R7 | Data assente |
| 4 | Debrief chiuso entro 2h (`entro_2h`) | R6 | Oltre → flag K5 + escalation |
| 5 | Zero PII nel record (incluso il campo `motivo`) | R7 | Nome/email/telefono presente |
| 6 | Se `esito = win`: il record esiste **prima** dell'handoff a A4 | R1 | Handoff senza record |

**FAIL** → la call **resta aperta** in `agency/a8/calls`, AG-A8-COORD sollecita l'informazione
mancante. Non esiste chiusura per decorrenza dei termini.
Motore dei check meccanici: `scripts/debrief_integrity.py` (return code `1` = blocco).

---

### Step 3 — Instradamento esito (AG-A8-COORD)

#### 3a — WIN

- Attiva `HC-AG-AM-01` verso **A7** (account management).
- Handoff a **A4 Delivery** (`ag-a4-coord`, `ag-a4-hand`): contratto firmato + **scope congelato**
  (verbatim dal preventivo A3 — A8 non lo riscrive, ADR-003).
- **Precondizione (R1):** l'handoff parte **solo** se `agency/a8/calls/{call_id}.json` esiste con
  `esito = win`. Nessun onboarding fantasma.
- Passa la variante di script usata ad AG-A8-LEARN: **cosa ha chiuso** vale quanto cosa ha perso.

#### 3b — LOSS

- **A3 Preventivi** — `ag-a3-fup`: follow-up commerciale (con il motivo, non "a freddo").
- **A3 Preventivi** — `ag-a3-learn`: `WF-LOSS-ANALYSIS` con il motivo nelle parole del prospect.
- **AG-A8-LEARN**: registra il pattern di perdita.

#### 3c — DA-RICONTATTARE

- Next step con data + owner. Il `call_id` resta **aperto** in `agency/a8/calls` con la data di
  ripresa. Alla data: nuova call → nuovo ciclo `WF-CLOSING-PREP`.

---

### Step 4 — Pattern learning (AG-A8-LEARN)

- Clusterizza i motivi con le **parole reali** dei prospect ("devo sentire il socio" ≠ "troppo caro":
  due cause, due rimedi).
- **Soglia 3 (R8):** cluster con ≥3 osservazioni → `consolidato: true`. Sotto → **aneddoto `[DM]`**,
  resta in osservazione, **non si propaga**. Motore: `scripts/pattern_threshold.py`.
- Collega ogni pattern all'**artefatto che lo genera**: libreria obiezioni incompleta (A5), script che
  chiude male (A5), scope ambiguo nel preventivo (A3), prova inesistente (A3/A1).
- **Propone** (non modifica — ADR-003): `ag-a5-obj`, `ag-a5-script`, `ag-a3-learn`, `ag-a3-prop`.
- Aggrega verso **08-INTELLIGENCE** (`HC-AG-IN-01`) i pattern consolidati, **senza `lead_id`**.

**Trigger di escalation:** 2 loss consecutive con lo **stesso motivo** → `WF-LOSS-ANALYSIS` in A3 +
`HC-AG-IN-01`. Non è più sfortuna: è un difetto di artefatto.

---

## 3. Gate di uscita

**AG-A8-QA — PASS obbligatorio.** Il debrief è chiuso solo con `esito` **e** `motivo` popolati,
entro 2h, senza PII. Un pattern è pubblicabile solo con ≥3 evidenze citate (R8).

---

## 4. Input / Output

**Input:**
```json
{
  "call_id": "CALL-001",
  "dossier_precall": "agency/a8/prep/CALL-001/dossier.md",
  "esito_dichiarato_da_max": "win | loss | da-ricontattare",
  "note_max": "testo libero / vocale trascritto (obbligatorio)",
  "call_end_at": "YYYY-MM-DDTHH:MM:SSZ"
}
```

**Output:**
```json
{
  "call_record": "agency/a8/calls/CALL-001.json",
  "esito": "win",
  "motivo": "parole del prospect",
  "entro_2h": true,
  "handoff": {"win": "A4 Delivery via HC-AG-AM-01 (A7)", "loss": "A3 ag-a3-fup + ag-a3-learn"},
  "pattern": {"pattern_id": "PAT-A8-001", "consolidato": false, "nota": "[DM] — 2 evidenze su 3"}
}
```

---

## 5. Handoff

| Direzione | Controparte | Cosa transita |
|---|---|---|
| ← in | **UMANO (Max)** | Esito call + note (obbligatorie per chiudere) |
| ← in | `WF-CLOSING-PREP` | Dossier pre-call (confronto previsto vs. emerso) |
| → WIN | A7 (`HC-AG-AM-01`) + `ag-a4-coord`, `ag-a4-hand` (A4) | Contratto firmato + scope congelato |
| → LOSS | `ag-a3-fup` (A3) | Follow-up commerciale con il motivo reale |
| → LOSS | `ag-a3-learn` (A3) | `WF-LOSS-ANALYSIS` |
| → out | `ag-a5-obj`, `ag-a5-script` (A5) | **Proposte** di libreria/script (mai modifiche dirette) |
| → out | 08-INTELLIGENCE (`HC-AG-IN-01`) | Pattern consolidati, senza `lead_id` |

---

## 6. DONE-WHEN

Il workflow è **DONE** quando **tutte** queste condizioni sono vere:

- [ ] `agency/a8/calls/{call_id}.json` esiste con `esito` **e** `motivo` popolati (R7).
- [ ] Il `motivo` riporta le **parole del prospect**; l'`ipotesi_interna` è in un campo separato.
- [ ] `da-ricontattare` (se presente) ha una **data** e un **owner** nel `next_step`.
- [ ] `entro_2h = true`, oppure il ritardo è registrato ed escalato (R6, K5).
- [ ] Zero PII nel record, incluso il campo `motivo` (R7).
- [ ] **WIN:** `HC-AG-AM-01` attivato + scope congelato passato ad A4 — **dopo** la scrittura del record (R1).
- [ ] **LOSS:** motivo consegnato ad `ag-a3-fup` e `ag-a3-learn`; pattern registrato in `agency/a8/patterns/`.
- [ ] Obiezioni emerse confrontate con quelle previste (alimenta K7); prove mancanti registrate (K8).
- [ ] Pattern pubblicati **solo** con ≥3 evidenze citate; sotto soglia → `[DM]`, non propagati (R8).
- [ ] Nessuna proposta ad A5/A3 è stata applicata come modifica diretta (ADR-003).

**NON è DONE se:** l'esito è registrato ma il motivo è vuoto ("si capiva"), oppure il motivo è
l'interpretazione di chi ha condotto invece delle parole del prospect, oppure un pattern con 2
evidenze è già stato spedito ad A5. Sono i tre modi in cui un reparto smette di imparare.

---

## Connessioni

- [[WF-CLOSING-PREP]] · `workflow/WF-CLOSING-PREP.md` — workflow gemello, pre-call
- [[ag-a8-debrief]] · `agenti/ag-a8-debrief.md` — owner del record di call
- [[ag-a8-learn]] · `agenti/ag-a8-learn.md` — owner dei pattern win/loss
- [[REGOLE]] · `regole/REGOLE.md` — R1, R6, R7, R8 applicate in questo workflow
