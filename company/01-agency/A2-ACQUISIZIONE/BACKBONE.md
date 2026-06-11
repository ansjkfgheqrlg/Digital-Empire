# BACKBONE — A2 ACQUISIZIONE / OUTREACH

> Reparto L2 di 01-AGENCY. Schema canonico: coordinator, I/O, acceptance_criteria, failure_handling, shared_state.
> ATTENZIONE ADR-003: pipeline outreach ATTIVA — nessuna modifica al runtime; solo wrapper.

## Coordinator

**AG-A2-COORD** (sonnet) — orchestratore reparto.
Oggi mappa a `orchestrator.py` nella pipeline esistente.
Responsabilita': convertire lead qualificati in discovery call prenotate su 3 canali.

## Team L3 / L4

| ID | Livello | Tipo | Flusso / Note |
|---|---|---|---|
| WF-OUTREACH-EMAIL | L3 | workflow ATTIVO | scraper->qualifier->strategist->writer(APSOC)->Bibbia-QA->sender. <=500/gg cap 100/h. NON TOCCARE |
| WF-OUTREACH-LINKEDIN | L3 | workflow | 20 connessioni + 20 messaggi + 30 commenti/gg |
| WF-OUTREACH-INSTAGRAM | L3 | workflow | 30 DM/gg, 2 messaggi (corpo + link), follow-up. BLOCCATO: token FB scaduto |
| WF-REPLY-FOLLOWUP | L3 | workflow | reply_monitor -> triage -> conversation_manager -> followup_writer -> booking |
| T-strategist | L4 | worker (sonnet) | angolo di attacco per lead (strategist.py, insight.py) |
| T-writer-apsoc | L4 | worker (sonnet) | scrittura messaggio (writer.py, humanizer.py, copy_knowledge.py) |
| T-bibbia-qa | L4 | worker x3 (sonnet) | gate Bibbia 3-checker (bibbia_team.py) — BLOCCA, non suggerisce |
| T-sender | L4 | worker (haiku) | invio + rate limiting + log (sender.py) |
| T-reply-triage | L4 | worker (haiku) | classificazione: interessato / obiezione / no / out-of-office |
| T-followup | L4 | worker (sonnet) | sequenze follow-up multi-touch (skill cold-email) |
| T-li-engage | L4 | worker (haiku) | commenti + connessioni LinkedIn |
| T-ig-dm | L4 | worker (haiku) | DM Instagram + follow-up 2-step |

## I/O

**Input:**
- Lead qualificati da A1 via `HC-A1-A2-leads`
- Template refresh da A5-COPY-INTERNO (WF-COPY-OUTREACH)

**Output:**
- Messaggi inviati (loggati in agency/outreach)
- Call prenotate -> A3 via `HC-A2-A3-call`
- Obiezioni/dati campo -> 08-INTELLIGENCE via `HC-AG-IN-01`

## Acceptance Criteria

- Ogni messaggio DEVE passare Gate Bibbia (3 checker) prima dell'invio
- Cap rispettati: email <=500/gg 100/h; LI 20+20+30; IG 30 DM/gg
- CTA standard: presentazione-empire.vercel.app
- Triage risposta: no invio a "no" definitivo

## Failure Handling

| Failure | Azione |
|---|---|
| Gate Bibbia FAIL | Messaggio bloccato; log in agency/outreach; ritorna a T-writer-apsoc |
| Bounce rate > 5% | Stop batch; alert A2-COORD; log pattern in agency/reasoning |
| Token FB scaduto | WF-OUTREACH-INSTAGRAM sospeso; alert dashboard; ticket a Max (runbook rinnovo) |
| LinkedIn rate limit | Stop; attendi 24h; log evento in agency/outreach |
| Reply classificata erroneamente | Feedback a T-reply-triage; aggiorna modello |

## Shared State (AgentDB)

Namespace: `agency/outreach`

```json
{
  "template_id": "string",
  "canale": "email | linkedin | instagram",
  "versione": "string",
  "bibbia_pass_rate": 0.0,
  "reply_rate": 0.0,
  "positive_reply_rate": 0.0,
  "attivo": true,
  "ultimo_invio": "ISO 8601"
}
```

## Asset esistenti (ADR-003 — runtime INVARIATO)

| Path | Team |
|---|---|
| `Outreach/Outreach Workflow/` (run.py, orchestrator.py, agents/) | WF-OUTREACH-EMAIL completo |
| `Outreach/LinkedIn Automation/` (01-05 + comment_posts.py) | WF-OUTREACH-LINKEDIN |
| `Outreach/Instagram Automation/` | WF-OUTREACH-INSTAGRAM (bloccato token) |
| `Agenti/Agency/orchestrator/` (AGENT.md, run.py, run_500.py, batch_send.py) | AG-A2-COORD |

## Connessioni

- `A1-RICERCA/BACKBONE.md` — lead in ingresso
- `A3-PREVENTIVI/BACKBONE.md` — call booked in uscita
- `company/Backbone/Bus/contracts/` — HC-A1-A2-leads.json, HC-A2-A3-call.json
- `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` sez. 2 (A2)
