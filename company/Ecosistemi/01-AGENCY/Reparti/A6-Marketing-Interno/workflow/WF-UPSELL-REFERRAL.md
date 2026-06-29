---
Type: WORKFLOW
Status: Active
Tags: #workflow #upsell #referral #nps #engine-room #A6
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-UPSELL-REFERRAL — Mappa Cliente verso Offerta Successiva

> **ID:** WF-A6-003 · **Owner:** `ag-a6-coord` + `ag-a6-upsell`
> **Reparto:** A6 Marketing Interno & Proof
> **Trigger:** segnale da A7-Account Mgmt — "90gg finiti + NPS ≥8"

---

## Scopo

Mappare ogni cliente soddisfatto verso l'offerta successiva (singolo prodotto → Engine Room
€8.000 → referral) e passare l'opportunità ad A3-Preventivi per la proposta commerciale. Il
fondamento della conversazione è il VALORE REALE già dimostrato (il case study del cliente),
non una tecnica di vendita. AG-A6-UPSELL segnala; non decide: la proposta va via umana (Max).

**Regola fondamentale:** mai upsell durante il supporto attivo (R3). Si attiva SOLO dopo Gate
Delivery + NPS ≥8. Se non c'è un next con fit reale → referral ask, mai un'offerta forzata.

---

## Attori

| Step | Agente A6 | Agente/Reparto esterno |
|---|---|---|
| Segnale NPS | — | A7-Account Mgmt |
| Verifica segnale | `ag-a6-coord` | — |
| Mappa upsell/referral | `ag-a6-upsell` (skill `upsell-mapper`) | — |
| Base proof | `ag-a6-case` (case study del cliente) | — |
| Proposta commerciale | — | A3-Preventivi (AG-A3-COORD) + Max (via umana) |

---

## Flusso passo-passo

```
[TRIGGER]
A7-Account Mgmt → segnale:
  {cliente, 90gg_finiti: true, nps: >=8, soddisfazione_qualitativa}
         │
         ▼
[STEP 1] AG-A6-COORD — verifica segnale
  → 90gg finiti AND NPS >=8? (entrambe obbligatorie)
  → GATE-1: segnale valido → prosegui; NPS <8 o supporto attivo → NON procede (R3)

         │
         ▼
[STEP 2] AG-A6-UPSELL — mappa prodotto attuale → next (skill upsell-mapper)
  → legge agency/clients/{cliente} + agency/a6/proof (risultato reale ottenuto)
  → matrice: prodotto attuale → next candidato
    - singolo servizio (CRO sprint / outreach) → Engine Room €8.000 (continuativo)
  → valuta il FIT: l'Engine Room ha senso per questo cliente (volume, bisogno)?

         │
   ┌─────┴──────────┐
 FIT upsell      NO fit
   │                 │
   ▼                 ▼
[STEP 3a]        [STEP 3b]
mappa upsell:    referral ask:
next = Engine    chi nella rete del cliente ha
Room €8.000      lo stesso problema risolto?
razionale basato  (solo dopo review positiva)
sul risultato reale
   │                 │
   └────────┬────────┘
            ▼
[STEP 4] AG-A6-UPSELL — prepara la mappa opportunità
  → razionale ancorato al case study del cliente (proof, non pressione)
  → registra in agency/a6/upsell/{cliente}

         │
         ▼
[STEP 5] Handoff ad AG-A3-COORD (Preventivi)
  → la mappa opportunità diventa input per il preventivo
  → la PROPOSTA viene emessa via umana (Max), MAI automaticamente
  → esito tracciato: proposto / contratto / declinato / in_attesa

         │
         ▼
[STEP 6] AG-A6-COORD — chiusura
  → aggiorna agency/a6/upsell con l'esito
  → se contratto → eventuale nuovo ciclo delivery → futuro WF-CASE-STUDY
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G1 — Segnale valido | 90gg finiti AND NPS ≥8 | AG-A6-COORD | Avvio mappatura (R3) |
| G2 — Fit verificato | Next con fit reale (upsell) O percorso referral | AG-A6-UPSELL | Handoff ad A3 |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "trigger": "nps_positivo",
  "cliente": "CLIENTE-X",
  "segnale": "90gg_finiti + nps>=8",
  "nps": 9,
  "prodotto_attuale": "CRO sprint singolo",
  "fonte_segnale": "A7-Account Mgmt"
}
```

**Output finale (upsell con fit):**
```json
{
  "cliente": "CLIENTE-X",
  "prodotto_attuale": "CRO sprint singolo",
  "next_mappato": "Engine Room €8.000",
  "tipo": "upsell",
  "razionale": "il risultato verificato dimostra il valore; il continuativo estende l'ottimizzazione",
  "handoff_a3": true,
  "esito": "in_attesa — proposta via Max",
  "namespace": "agency/a6/upsell/CLIENTE-X"
}
```

**Output finale (referral):**
```json
{
  "cliente": "CLIENTE-Y",
  "next_mappato": "referral_ask",
  "tipo": "referral",
  "razionale": "nessun upsell con fit; NPS alto → richiesta referral dopo review positiva",
  "handoff_a3": true,
  "esito": "referral_richiesto",
  "namespace": "agency/a6/upsell/CLIENTE-Y"
}
```

---

## State

File: `agency/a6/upsell/{cliente}.json`
- Creato allo STEP 1 (segnale valido).
- Campo `segnale` deve includere `nps>=8` e `90gg_finiti` (R3 — integrità).
- Campo `esito` OBBLIGATORIO alla chiusura: proposto / contratto / declinato / in_attesa.
- Nessun record con `tipo: upsell` senza segnale valido = anomalia di integrità.

---

## Connessioni

- [[ag-a6-upsell]] · `agenti/ag-a6-upsell.md` — mappa con `upsell-mapper`
- [[ag-a6-coord]] · `agenti/ag-a6-coord.md` — verifica segnale e coordinamento
- [[ag-a6-case]] · `agenti/ag-a6-case.md` — il case study è la base della conversazione
- [[WF-CASE-STUDY]] · `workflow/WF-CASE-STUDY.md` — fornisce il proof su cui si fonda l'upsell
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A6 WF-UPSELL-REFERRAL`
