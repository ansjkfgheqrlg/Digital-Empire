---
Type: WORKFLOW
Status: Active
Tags: #workflow #agency #copywriting #script #call #closing #apsoc #A5
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-SCRIPT-CALL — Script Discovery e Chiusura per A8-Closing

> **ID:** WF-A5-002 · **Owner:** `ag-a5-coord` + `ag-a5-script`
> **Reparto:** A5 Copywriting Interno (01-AGENCY)
> **Trigger:** richiesta di A8-Closing (script discovery o chiusura per una nicchia)
> **Consegna a:** A8-Closing (le call le fa Max) · [TARGET-V2]

---

## Scopo

Produrre gli **script per le call** dell'agency — discovery e chiusura — su misura della nicchia,
strutturati con il framework APSOC adattato al parlato, con le obiezioni attese gestite tramite
**risposte provate** (da AG-A5-OBJ). Lo script passa dal Gate Bibbia (AG-A5-QA) prima di essere
consegnato ad A8-Closing.

**Regola fondamentale:** "prove non promesse" (Mandato Art.2) vale anche nel parlato. Nessuno
script contiene un claim di risultato non provabile o dependency-language. Il gate verifica:
no claim senza proof, no dependency-language, brand voice conforme, P prima di S.

---

## Attori

| Step | Agente A5 | Esterno |
|---|---|---|
| Richiesta script | `ag-a5-coord` | A8-Closing (committente) |
| Obiezioni nicchia | `ag-a5-obj` | libreria `agency/a5/obiezioni` |
| Struttura script | `ag-a5-script` | skill `cro-copy-architect` (APSOC) |
| Gate Bibbia | `ag-a5-qa` | gate riusato da A2 (`../A2-Acquisizione/agenti/ag-a2-qa.md`) |
| Consegna | `ag-a5-coord` | A8-Closing (Max conduce le call) |

---

## Flusso passo-passo

```
[TRIGGER]
A8-Closing → richiesta script
  {tipo: discovery | chiusura, nicchia, offerta, next_step}
         │
         ▼
[STEP 1] AG-A5-COORD — validazione richiesta
  → tipo, nicchia, offerta, next-step presenti?
  → GATE-1: richiesta completa → prosegui; incompleta → richiede dettaglio ad A8

         │
         ▼
[STEP 2] AG-A5-OBJ — obiezioni attese per la nicchia
  → estrae da agency/a5/obiezioni SOLO coppie validate (con prova reale) per la nicchia
  → se la nicchia ha poche obiezioni validate → nota il gap (no obiezioni inventate)
  → GATE-2: obiezioni della nicchia disponibili e validate → prosegui

         │
         ▼
[STEP 3] AG-A5-SCRIPT — struttura script APSOC parlato
  → apertura sul problema condiviso (A)
  → amplificazione del costo del problema (P)
  → offerta ancorata, SEMPRE dopo P (S)
  → blocco obiezioni con risposte provate, in forma parlata naturale (O)
  → CTA di chiusura = next-step concordato con A8 (CTA)

         │
         ▼
[STEP 4] AG-A5-QA — Gate Bibbia (riuso A2, pattern 6)
  → check 1 APSOC: A→P→S→O→CTA, P prima di S
  → check 2 CTA: next-step singolo e chiaro
  → check 3 no dependency + prove: nessun claim di risultato senza prova reale
  → FAIL: torna ad AG-A5-SCRIPT con note (es. rimuovi claim assoluto)
  → GATE-3: PASS → autorizzato alla consegna

         │
         ▼
[STEP 5] AG-A5-COORD — consegna ad A8-Closing
  → script gated + obiezioni provate referenziate + note d'uso
  → scrive state in agency/a5/script/{script_id}
  → A8 usa lo script come guida (non copione rigido); Max conduce la call

         │
         ▼
[FEEDBACK LOOP]
A8 segnala esiti reali (obiezione nuova emersa in call, risposta che ha chiuso)
  → AG-A5-OBJ aggiorna la libreria con la nuova prova (promuove non_validata → validata)
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G1 — Richiesta completa | tipo + nicchia + offerta + next-step presenti | AG-A5-COORD | Avvio script |
| G2 — Obiezioni validate disponibili | la nicchia ha obiezioni con prova reale | AG-A5-OBJ | Struttura script |
| G3 — Gate Bibbia PASS | APSOC (P prima di S) + CTA singola + no claim senza proof | AG-A5-QA | Consegna ad A8 |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "tipo_script": "chiusura",
  "nicchia": "e-commerce",
  "offerta": "sprint CRO 2-4 settimane pay-on-performance",
  "next_step": "invio_preventivo"
}
```

**Output finale:**
```json
{
  "script_id": "SCRIPT-A5-001",
  "tipo": "chiusura",
  "nicchia": "e-commerce",
  "struttura_apsoc": ["A", "P", "S", "O", "CTA"],
  "obiezioni_provate": ["OBJ-A5-001 (prezzo)", "OBJ-A5-004 (timing)", "OBJ-A5-009 (fiducia)"],
  "gate_bibbia": "PASS",
  "consegna": "A8-Closing",
  "namespace": "agency/a5/script/SCRIPT-A5-001"
}
```

---

## State

File: `agency/a5/script/{script_id}.json`
- Creato alla consegna (STEP 5).
- Campo `gate_bibbia` OBBLIGATORIO = PASS prima della consegna ad A8.
- Campo `obiezioni_provate` referenzia solo obiezioni validate.
- Aggiornato dal feedback loop quando A8 riporta esiti reali (nuove prove → AG-A5-OBJ).
- Ripartibilità a freddo: `last_updated` permette di riprendere dallo step esatto.

---

## Connessioni

- [[ag-a5-script]] · `agenti/ag-a5-script.md` — struttura lo script APSOC parlato
- [[ag-a5-obj]] · `agenti/ag-a5-obj.md` — fornisce le obiezioni provate della nicchia
- [[ag-a5-qa]] · `agenti/ag-a5-qa.md` — Gate Bibbia (riuso A2, pattern 6)
- [[ARCHITETTURA]] · `ARCHITETTURA.md §2.2` — flusso script call
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A5 WF-SCRIPT-CALL`
