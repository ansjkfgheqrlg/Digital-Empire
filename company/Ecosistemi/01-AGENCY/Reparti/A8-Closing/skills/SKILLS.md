---
Type: TOOL
Status: Active
Tags: #skill #agency #closing #sales-call #A8
Created: 2026-07-11
Last updated: 2026-07-11
---

# SKILLS — A8 Closing / Sales-Call

> Skill usate dal reparto, con contratto I/O esplicito.
> **Regola di confine:** A8 **non invoca** le skill possedute da altri reparti (es. `beast-preventivi`
> è di A3). Ne **legge l'output** via handoff (ADR-003 wrap-non-riscrittura).

---

## `discovery-call-brief` — esistente, mappata

**Owner d'uso:** AG-A8-PREP · **Ruolo:** motore del dossier pre-call.

```json
{
  "input": {
    "lead_id": "LEAD-001",
    "dossier_lead": "agency/a1/dossier/LEAD-001",
    "preventivo_ref": "agency/a3/PREV-001",
    "call_type": "discovery | closing",
    "awareness_level": "unaware | problem-aware | solution-aware | product-aware"
  },
  "output": {
    "brief": {
      "chi_e": "...", "problema_quantificato": "... [DM] se stimato",
      "cosa_abbiamo_proposto": "verbatim da A3",
      "prove_disponibili": ["..."], "prove_mancanti": ["... → [DM]"]
    }
  }
}
```

---

## `sales-enablement` — esistente, mappata

**Owner d'uso:** AG-A8-PREP, AG-A8-OBJ, AG-A8-SCRIPT · **Ruolo:** battle card, struttura
risposta-obiezione, materiale di supporto alla call.

```json
{
  "input": {
    "icp": "PMI servizi",
    "prodotto": "Outreach Factory",
    "obiezioni_target": ["prezzo", "timing", "fiducia", "decisore multiplo"],
    "prove": ["case study", "numeri misurati", "clausole contrattuali", "demo"]
  },
  "output": {
    "battle_card": [
      {"obiezione": "...", "risposta_a_prova": "...", "prova": "rif verificabile"}
    ],
    "claim_vietati": ["promesse senza prova → blocco 7 del dossier"]
  }
}
```

**Vincolo:** l'output non può contenere leve di scarsità artificiale o pressione (R4).

---

## `beast-preventivi` — esistente (A3), **handoff, non invocata**

**Owner:** A3 Preventivi (`ag-a3-prop`). A8 **non la chiama**: legge il preventivo già prodotto.

```json
{
  "input_ad_A8": {
    "preventivo_id": "PREV-001",
    "prodotto": "...", "scope": "...",
    "prezzo": "da catalogo fisso B-003",
    "prove_allegate": ["..."]
  },
  "uso_in_A8": "citazione verbatim nel blocco 3 del dossier; mai riscrittura"
}
```

---

## `outreach-reply-triage` — esistente, mappata

**Owner d'uso:** AG-A8-DEBRIEF · **Ruolo:** classificare l'esito e il segnale nel testo libero /
vocale che Max invia dopo la call.

```json
{
  "input": {"call_id": "CALL-001", "note_max": "testo libero o vocale trascritto"},
  "output": {
    "esito": "win | loss | da-ricontattare",
    "motivo_parole_prospect": "citazione, non parafrasi",
    "ipotesi_di_max": "registrata separatamente — NON è il motivo",
    "next_step": {"azione": "...", "data": "YYYY-MM-DD", "owner": "A4 | A3 | Max"}
  }
}
```

---

## `closing-call-prep` — **P3, da forgiare via 07-FORGE**

**Owner d'uso previsto:** AG-A8-PREP + AG-A8-OBJ + AG-A8-SCRIPT (formalizza il trio in un'unica
skill). Oggi la logica vive nei tre agenti; la skill la renderà riusabile e testabile.

```json
{
  "input": {
    "call_id": "CALL-001", "lead_id": "LEAD-001", "preventivo_id": "PREV-001",
    "fonti": {"a1_dossier": "...", "a3_preventivo": "...", "a5_obiezioni": "...", "a5_script": "..."},
    "call_datetime": "YYYY-MM-DDTHH:MM:SSZ"
  },
  "output": {
    "dossier": {"blocchi_1_8": "..."},
    "obiezioni": [{"id": "OBJ-01", "risposta_a_prova": "...", "prova_presente": true}],
    "script": {"apertura": "...", "chiusura": "...", "uscita_no": "..."},
    "gate_ready": true,
    "prove_mancanti": ["... → [DM]"]
  }
}
```

**Criteri di accettazione per la forgiatura (07-FORGE):**
- Rifiuta di produrre un claim senza prova (R3) — non lo "ammorbidisce": lo rimuove.
- Filtro anti-pressione/scarsità artificiale nativo (R4).
- Prezzi letti dal catalogo fisso, mai generati (R5).
- Nessun PII nell'output strutturato (R7).

---

## Connessioni

- [[ag-a8-prep]] · `agenti/ag-a8-prep.md` — principale consumatore delle skill
- [[README]] · `README.md` — mappa skill del reparto
- [[REGOLE]] · `regole/REGOLE.md` — i vincoli che ogni skill deve rispettare
