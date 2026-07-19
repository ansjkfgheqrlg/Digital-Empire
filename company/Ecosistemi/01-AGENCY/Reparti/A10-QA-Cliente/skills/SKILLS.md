---
Type: TOOL
Status: Active
Tags: #skills #agency #qa #audit #gate #A10
Created: 2026-07-11
Last updated: 2026-07-11
---

# SKILLS — A10 QA-Cliente & Audit Qualità

> Skill **reali** già presenti nell'ecosistema. A10 non ne inventa di nuove: le compone.
> Metodo di gate di riferimento: `company/MAXIMILIAN/Skill/maximilian-standard-gate`
> (criteri espliciti prima del test · verdetto binario · evidenza citata · nessun verdetto senza prova).

---

## 1. Skill in uso

| Skill | Chi la usa | A cosa serve in A10 |
|---|---|---|
| `verification-quality` | REVIEW · UAT · BRAND · LEARN | Verifica del **comportamento reale**: si esegue e si osserva, non si legge e si spera (P4) |
| `impeccable` | HANDOVER · BRAND · UAT | Completezza: nessuna voce del pacchetto, nessun campo del `brand_kit`, nessuno step UAT saltato |
| `agent-reviewer` | REVIEW · COORD · LEARN | Review sistematica di codice, config e artefatti consegnati |
| `client-handover` (lettura) | HANDOVER · UAT | Definizione di riferimento del pacchetto che A4 doveva consegnare |
| `memory-empire` | LEARN | Scrittura dei pattern distillati in `agency/reasoning` |

---

## 2. Contratto I/O — check di gate

Ogni check A10 produce lo stesso oggetto, qualunque sia la skill usata. Uniformità = report aggregabile.

```json
{
  "delivery_id": "DLV-2026-0042",
  "cliente_ref": "CLI-017",
  "check": "G2",
  "check_label": "Zero dipendenza DE",
  "owner": "AG-A10-REVIEW",
  "skill": "verification-quality",
  "esito": "FAIL",
  "severita": "blocker",
  "evidenza": {
    "comando": "grep -rn 'digitalempire' /srv/cliente/runtime/",
    "osservato": "config/mailer.yml:12 → smtp.digitalempire.internal",
    "atteso": "nessun endpoint DE nel runtime cliente"
  },
  "ts": "2026-07-11T14:22:00Z"
}
```

**Vincoli**: `esito ∈ {PASS, FAIL}` — nessun terzo valore (R3). `evidenza` obbligatoria, anche
sui PASS (R2). Nessun PII e nessun segreto nei campi (R6).

---

## 3. Contratto I/O — verdetto di review

```json
{
  "delivery_id": "DLV-2026-0042",
  "review_index": 1,
  "verdetto": "FAIL",
  "checks": ["G1:PASS", "G2:FAIL", "G3:PASS", "G4:PASS", "G5:SKIP", "G6:SKIP", "G7:PASS"],
  "difetti": [
    { "id": "DEF-0113", "categoria": "dipendenza-DE", "severita": "blocker", "step_origine": "G+1 setup secrets" }
  ],
  "handoff_out": "HC-QC-AG-01",
  "ts_handoff_in": "2026-07-11T09:00:00Z",
  "ts_verdetto": "2026-07-11T15:40:00Z"
}
```

`SKIP` è ammesso **solo** su G5/G6 quando l'UAT non si è aperta per R5 (delivery già rossa sui
check tecnici). Un `SKIP` non è mai un PASS: il verdetto complessivo resta FAIL.

---

## 4. Contratto I/O — report mensile

```json
{
  "periodo": "2026-07",
  "campione": { "delivery_reviewate": 6, "delivery_totali": 6 },
  "pass_primo_review_pct": "[DM]",
  "tempo_qa_mediano_h": "[DM]",
  "difetti_per_categoria": { "dipendenza-DE": 3, "brand": 2, "handover": 1, "uat": 0 },
  "difetti_sfuggiti_al_gate": 0,
  "pattern_ricorrenti": [
    { "categoria": "dipendenza-DE", "occorrenze": 3, "clienti_distinti": 2, "step_origine": "G+1 setup secrets", "destinatario": "07-FORGE" }
  ],
  "ts_report": "2026-08-04T10:00:00Z"
}
```

Baseline non ancora misurata → **`"[DM]"`**, mai un numero plausibile (R7).

---

## Connessioni

- [[REGOLE]] · `../regole/REGOLE.md` — R2, R3, R6, R7: i vincoli su questi contratti
- [[ARCHITETTURA]] · `../ARCHITETTURA.md §4` — i check G1..G7 che questi JSON descrivono
- [[state]] · `../state/README.md` — dove atterrano questi oggetti
