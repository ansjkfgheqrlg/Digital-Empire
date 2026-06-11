# BACKBONE — A1 RICERCA (Lead & Market Intelligence)

> Reparto L2 di 01-AGENCY. Schema canonico: coordinator, I/O, acceptance_criteria, failure_handling, shared_state.

## Coordinator

**AG-A1-COORD** (sonnet) — orchestratore reparto.
Responsabilita': alimentare il funnel con lead qualificati e fornire intelligence di nicchia.

## Team L3 / L4

| ID | Livello | Tipo | Flusso |
|---|---|---|---|
| WF-LEAD-SOURCING | L3 | workflow | scraping -> estrazione -> arricchimento -> qualifica -> leads.db |
| WF-MARKET-INTEL | L3 | workflow | nicchia/competitor/trend -> report per A2 e A3 |
| T-scraper | L4 | worker (haiku) | run scraper multi-fonte (maps, apify, outscraper, google) |
| T-extractor | L4 | worker (haiku) | estrazione contatti dal raw |
| T-qualifier | L4 | worker (sonnet) | scoring lead vs ICP (qualifier.py + regola 03_qualifica_lead.md) |
| T-icp-profiler | L4 | worker (sonnet) | definizione/aggiornamento ICP per nicchia (skill icp-radar) |
| T-competitor-profiler | L4 | worker (sonnet) | dossier competitor del prospect (competitor.py, cro_audit.py) |

## I/O

**Input:**
- Nuove nicchie target (da AG-DIR o 08-INTELLIGENCE via HC-IN-AG-01)
- Aggiornamento ICP (da A3 post-win/loss analysis)

**Output:**
- Lead qualificati in `leads.db` con score ICP >= soglia
- Report nicchia/competitor per A2 e A3
- Handoff -> A2 via `HC-A1-A2-leads`

## Acceptance Criteria

- qualifier_score >= soglia definita in ICP attivo
- Dati contatto completi: nome, email/canale, azienda, nicchia
- Deduplication verificata vs leads gia' in DB

## Failure Handling

| Failure | Azione |
|---|---|
| Scraper 0 risultati | log in agency/reasoning; retry con fonte alternativa; alert A2 di gap |
| Qualificatore sotto soglia batch | log; informa A2 del calo; notifica 07-FORGE se persiste 2+ cicli |
| Token/credenziali scraper scaduti | pre-flight check (job HC-AG-OP-01); alert dashboard; runbook rinnovo |

## Shared State (AgentDB)

Namespace: `agency/leads`

```json
{
  "lead_id": "string",
  "score_icp": 0,
  "nicchia": "string",
  "canali_disponibili": ["email", "linkedin", "instagram"],
  "stato": "new | qualified | outreach | responded | call_booked | won | lost",
  "source": "maps | apify | outscraper | manuale",
  "created_at": "ISO 8601"
}
```

## Asset esistenti (ADR-003 — non toccare)

| Path | Uso |
|---|---|
| `Outreach/Outreach Workflow/agents/` (scraper, qualifier, extractor) | T-scraper, T-extractor, T-qualifier |
| `Agenti/Agency/outreach/rules/01_ricerca_no_sito.md` ... `06_ricerca_ai_prospects.md` | knowledge layer |
| `Outreach/Outreach Workflow/leads.db` | storage primario lead |

## Connessioni

- `A2-ACQUISIZIONE/BACKBONE.md` — riceve lead da qui
- `A3-PREVENTIVI/BACKBONE.md` — riceve intelligence di nicchia
- `company/Backbone/Bus/contracts/` — HC-A1-A2-leads.json
- `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` sez. 2 (A1)
