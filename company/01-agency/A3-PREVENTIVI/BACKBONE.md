# BACKBONE — A3 PREVENTIVI

> Reparto L2 di 01-AGENCY. Schema canonico: coordinator, I/O, acceptance_criteria, failure_handling, shared_state.

## Coordinator

**AG-A3-COORD** (opus) — orchestratore reparto.
Responsabilita': trasformare ogni discovery call in proposta problem-first inviata entro 48h.

## Team L3 / L4

| ID | Livello | Tipo | Flusso |
|---|---|---|---|
| WF-PREVENTIVO | L3 | workflow | trascrizione/appunti -> brief -> audit -> outline -> documento -> gate -> invio -> followup |
| T-discovery-brief | L4 | worker (sonnet) | da call a brief strutturato (skill discovery-call-brief) |
| T-problem-audit | L4 | worker (sonnet) | quantifica il problema (skill market-audit, cro_audit.py) |
| T-proposal-writer | L4 | worker (opus) | costruisce il preventivo (skill beast-preventivi + market-proposal) |
| T-pricing-config | L4 | worker (haiku) | seleziona prodotto/bundle dal catalogo fisso |
| T-proposal-qa | L4 | worker (opus) | Gate Preventivo (skill proposal-gate) |

## I/O

**Input:**
- Call prenotata + thread conversazione da A2 via `HC-A2-A3-call`
- Dossier pre-call: lead score, audit competitor, nicchia (da A1/08-INTELLIGENCE)

**Output:**
- Preventivo problem-first inviato entro 48h dalla call
- Esito win/loss -> agency/proposals
- Lead perso/non pronto -> 02-INFO-BUSINESS via `HC-AG-IB-01`
- Contratto firmato -> A4 via `HC-A3-A4-contratto`

## Acceptance Criteria (Gate Preventivo)

1. Il PROBLEMA del cliente apre il documento (problem-first verificato)
2. Awareness level corretto (aware/unaware rispetto al prodotto)
3. Pricing SOLO dal catalogo: EUR 4.000 / 3.500 / 2.500 / 8.000 — nessuno sconto improvvisato
4. Promesse = SOLO prove verificabili (Mandato Empire: "prove non promesse")
5. Scope delivery 7gg esplicito
6. Clausola proprieta' codice + EUR 0 canoni presente
7. Supporto 90gg definito
8. Brand voice conforme (Gate Bibbia corporate)
9. Inviato entro 48h dalla discovery call

## Failure Handling

| Failure | Azione |
|---|---|
| Gate Preventivo FAIL | Blocca invio; log motivo in agency/proposals; rework da passo fallito |
| Preventivo perso (loss) | Log motivo in agency/reasoning (pattern per ReasoningBank); considera lead -> 02-INFO-BIZ |
| 48h scadute senza invio | Alert AG-A3-COORD; escalation a AG-DIR; log ritardo |
| Pricing non a catalogo (tentativo) | T-pricing-config rifiuta; escalation a AG-DIR |

## Shared State (AgentDB)

Namespace: `agency/proposals`

```json
{
  "proposal_id": "string",
  "cycle_id": "CY-YYYYMMDD-NNN",
  "client_id": "string",
  "prodotto": "outreach_factory | content_factory | second_brain | engine_room",
  "valore_eur": 0,
  "sent_at": "ISO 8601",
  "gate_passed": true,
  "stato": "sent | win | loss | ghost",
  "motivo_loss": "string | null"
}
```

## Asset esistenti (da usare as-is)

| Path | Team |
|---|---|
| Skill globale `beast-preventivi` | T-proposal-writer (cuore) |
| Skill globale `market-proposal` | T-proposal-writer (supporto) |
| Skill globale `market-audit` | T-problem-audit |
| `Agenti/Agency/outreach/script_chiamata_freddo.md` | T-discovery-brief |
| `Agenti/Agency/sub-agents/` (ai-implementation, cro-funnel, no-website) | T-icp-profiler + T-problem-audit |

## Connessioni

- `A2-ACQUISIZIONE/BACKBONE.md` — call in ingresso
- `A4-DELIVERY/BACKBONE.md` — contratto in uscita
- `company/Backbone/Bus/contracts/` — HC-A2-A3-call.json, HC-A3-A4-contratto.json
- `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` sez. 2 (A3) + sez. 8 (Gate Preventivo)
