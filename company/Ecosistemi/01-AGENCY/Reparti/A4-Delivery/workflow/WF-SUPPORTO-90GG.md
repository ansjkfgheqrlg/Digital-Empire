---
Type: WORKFLOW
Status: Active
Tags: #workflow #agency #delivery #support #sla #A4
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-SUPPORTO-90GG — Supporto Post-Handover 90 Giorni

> **ID:** WF-A4-004 · **Owner:** `ag-a4-supp` (triage) + `ag-a4-coord` (escalation)
> **Trigger:** delivery chiusa (Gate Delivery PASS) → ticket in ingresso o check settimanale
> **Topologia:** `star` (triage centrale) · **Standard:** CF-grade (ADR-007)

---

## Scopo

Fornire supporto per 90 giorni dopo l'handover, con un **obiettivo decrescente di ticket**:
ogni intervento deve rendere il cliente più autonomo, non più dipendente. Triage di ogni
ticket (bug/domanda/fuori scope), SLA rispettata (≤24h bug, ≤48h domanda), check proattivo
settimanale, chiusura a 90gg con review A7 e proposta upsell da A6. Nessun ticket chiuso senza
conferma cliente (R5).

---

## Attori

| Step | Agente A4 | Esterno |
|---|---|---|
| Intake + triage | `ag-a4-supp` | cliente |
| Fix bug | `ag-a4-supp` (o handoff motore) | reparto proprietario motore |
| Risposta domanda | `ag-a4-supp` | cliente |
| Fuori scope → upsell | `ag-a4-supp` → A6 | A6 Marketing-Interno |
| Check settimanale | `ag-a4-supp` | 09 OPERATIONS (scheduling) |
| Pattern | `ag-a4-learn` | — |
| Review 90gg | `ag-a4-coord` | A7 Account Mgmt + A6 (upsell) |

---

## Flusso passo-passo

```
[TRIGGER A] Ticket in ingresso durante i 90gg
[TRIGGER B] Check proattivo settimanale (pianificato da 09 OPERATIONS, HC-OP-AG-01)
         │
         ▼
[STEP 1] AG-A4-SUPP — intake + triage (support-90)
  → classifica: BUG (non funziona come da scope) | DOMANDA (uso) | FUORI SCOPE (nuova feature)
  → assegna SLA: ≤24h bug · ≤48h domanda
  → logga in agency/a4/support/{ticket_id}.json (classe, sla_target, giorno_dei_90)

         │
         ├─ BUG ────────────────────────────────────────────────┐
         │   → fix se di config/runbook                          │
         │   → modifica STRUTTURALE del motore? handoff al        │
         │     reparto proprietario via AG-A4-COORD (ADR-003)     │
         │                                                        │
         ├─ DOMANDA ─────────────────────────────────────────────┤
         │   → risposta dal runbook/FAQ; se ricorrente → integra  │
         │     la FAQ per ridurre ticket futuri (P7)              │
         │                                                        │
         └─ FUORI SCOPE ─────────────────────────────────────────┤
             → risposta standard "fuori scope"                   │
             → brief proposta estensione a pagamento → A6         │
                                                                  │
         ▼ ◄──────────────────────────────────────────────────────┘
[STEP 2] AG-A4-SUPP — risoluzione entro SLA
  → registra risolto_entro_sla (true/false)
  → GATE-SLA: risposta entro SLA contrattuale? (≤24h bug, ≤48h domanda)

         │
         ▼
[STEP 3] AG-A4-SUPP — conferma cliente (R5)
  → chiede al cliente conferma che il problema è risolto
  → conferma ricevuta → stato=chiuso, conferma_cliente=true
  → NESSUN ticket chiuso senza conferma cliente (chiusura unilaterale vietata)

         │
         ▼
[STEP 4] AG-A4-SUPP — check proattivo settimanale
  → verifica stato cliente, anticipa problemi; aggiorna il trend ticket/settimana
  → trend crescente → segnala ad AG-A4-COORD (handover forse incompleto, P7)

         │
         ▼
[STEP 5] AG-A4-LEARN — distillazione pattern
  → ticket ricorrenti → pattern in agency/a4/reasoning (causa + azione su training/handover)

         │
         ▼
[STEP 6 · giorno 90] AG-A4-COORD — review chiusura 90gg
  → review con A7 Account Mgmt: trend ticket, SLA rispettata, NPS misurato (non inventato)
  → proposta upsell da A6 (se opportuna)
  → cliente più autonomo di quando ha firmato? (test P7)
  → GATE-90: SLA rispettato globalmente · nessun ticket aperto senza conferma · NPS raccolto
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| GATE-SLA | Risposta entro SLA (≤24h bug, ≤48h domanda) | AG-A4-SUPP | KPI ticket in SLA |
| GATE-CONFERMA | Conferma cliente prima della chiusura | AG-A4-SUPP | Chiusura ticket (R5) |
| GATE-90 | SLA globale rispettato · nessun ticket aperto senza conferma · NPS raccolto | AG-A4-COORD + A7 | Chiusura finestra 90gg |

---

## Input / Output del workflow

**Input trigger (ticket):**
```json
{
  "delivery_id": "DEL-001",
  "ticket_text": "l'invio email si è fermato",
  "data_ingresso": "2026-08-01T09:00:00Z",
  "sla_contratto": "≤24h bug, ≤48h domanda",
  "giorno_dei_90": 12
}
```

**Output (ticket chiuso):**
```json
{
  "ticket_id": "TKT-001",
  "delivery_id": "DEL-001",
  "classe": "bug",
  "sla_target_h": 24,
  "risolto_entro_sla": true,
  "stato": "chiuso",
  "conferma_cliente": true
}
```

**Output (review 90gg):**
```json
{
  "delivery_id": "DEL-001",
  "trend_ticket": "decrescente",
  "sla_rispettata_pct": "[DM]",
  "nps_fine_90gg": "[DM] — misurato a chiusura",
  "upsell_proposto_a6": true,
  "review_a7": "completata"
}
```

---

## State

File: `agency/a4/support/{ticket_id}.json` (per ticket) + report di review a 90gg.
- Ogni ticket ha `classe`, `sla_target_h`, `risolto_entro_sla`, `stato`, `conferma_cliente`, `giorno_dei_90`.
- Trend ticket/settimana tracciato per il test P7 (cliente sempre più autonomo).
- NPS resta [DM] finché non misurato a chiusura (Mandato Art.2, R6 reparto: prove non promesse).

---

## Connessioni

- [[ag-a4-supp]] · `agenti/ag-a4-supp.md` — esegue triage e SLA
- [[ag-a4-coord]] · `agenti/ag-a4-coord.md` — review 90gg + escalation
- [[ag-a4-learn]] · `agenti/ag-a4-learn.md` — distilla pattern da ticket ricorrenti
- [[A6-Marketing-Interno]] · riceve i fuori scope come proposta upsell
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A4`
