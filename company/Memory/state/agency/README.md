# State Schema — AGENCY (01)

## Scopo

Questa cartella contiene il project state dell'ecosistema AGENCY:
- `state.json` — snapshot corrente: cicli attivi, KPI per reparto, blockers
- `trace.jsonl` — log append-only di ogni evento nel ciclo revenue

Sono la fonte di verita' operativa per il Gate F4:
"un ciclo completo reale tracciato nel project state con handoff contract tra i reparti".

## state.json — schema

```json
{
  "_schema": "agency-state-v1",
  "updated_at": "ISO 8601",
  "cycles": {
    "active": [ "<cycle-object>" ],
    "completed": [ "<cycle-object>" ],
    "failed": [ "<cycle-object>" ]
  },
  "kpi": {
    "a1": { "leads_qualified_today": 0, "pct_qualifica": 0 },
    "a2": { "email_sent_today": 0, "li_sent_today": 0, "ig_sent_today": 0,
            "reply_rate": 0.0, "positive_reply_rate": 0.0, "calls_booked_week": 0 },
    "a3": { "avg_call_to_proposal_h": 0, "win_rate": 0.0, "avg_deal_value": 0 },
    "a4": { "avg_delivery_days": 0, "uat_first_pass_rate": 0.0,
            "tickets_resolved_in_sla_pct": 0.0 },
    "a5": { "copy_bibbia_pass_first_try_pct": 0.0 },
    "a6": { "case_studies_total": 0, "inbound_calls_month": 0, "testimonials_total": 0 }
  },
  "blockers": [
    { "id": "B-001", "desc": "Token FB scaduto -> outreach IG bloccato", "owner": "Max", "since": "2026-06-11" }
  ]
}
```

## Cycle object — schema

```json
{
  "id": "CY-YYYYMMDD-NNN",
  "lead_id": "string",
  "lead_nome_azienda": "string",
  "lead_nicchia": "string",
  "created_at": "ISO 8601",
  "status": "outreach | call_booked | proposal_sent | won | lost | in_delivery | delivered | in_support | closed",
  "prodotto": "outreach_factory | content_factory | second_brain | engine_room | null",
  "valore_eur": 0,
  "steps": {
    "outreach": { "started_at": null, "completed_at": null, "channel": null, "reply_type": null },
    "call":     { "scheduled_at": null, "completed_at": null, "brief_doc": null },
    "proposal": { "sent_at": null, "value_eur": null, "product": null, "gate_passed": null, "win_loss": null },
    "contratto":   { "signed_at": null, "payment_confirmed_at": null },
    "delivery":    { "started_at": null, "completed_at": null, "uat_signed_at": null, "gate_passed": null },
    "supporto_90gg": { "started_at": null, "ends_at": null, "tickets_open": 0 },
    "testimonianza": { "collected_at": null, "case_study_published_at": null, "upsell_sent_at": null }
  },
  "handoffs": [
    { "hc": "HC-A1-A2-leads", "sent_at": null, "accepted_at": null }
  ],
  "notes": ""
}
```

## trace.jsonl — schema per riga

Ogni riga = JSON su una riga (newline-delimited JSON):

```json
{
  "ts": "ISO 8601",
  "cycle_id": "CY-YYYYMMDD-NNN",
  "step": "A1.SOURCING | A2.OUTREACH | A2.REPLY | A3.PREVENTIVO | A4.DELIVERY | A4.SUPPORTO | A6.UPSELL",
  "event": "started | completed | failed | gate_passed | gate_failed | handoff_sent | handoff_received | blocker_added | blocker_resolved",
  "from_reparto": "A1 | A2 | A3 | A4 | A5 | A6 | HUMAN",
  "to_reparto": "A1 | A2 | A3 | A4 | A5 | A6 | HUMAN | null",
  "hc": "HC-xxx | null",
  "agent": "AG-xxx | null",
  "payload_summary": "string breve",
  "notes": ""
}
```

## Come aggiornare

- **Ogni handoff** tra reparti: aggiungi riga in trace.jsonl + aggiorna cycle.steps + cycle.handoffs in state.json
- **Ogni gate**: aggiungi evento gate_passed/gate_failed in trace.jsonl
- **Fine ciclo**: sposta cycle da active a completed/failed in state.json
- **KPI**: aggiorna state.json kpi ogni giorno (run giornaliera via 09-OPERATIONS)
