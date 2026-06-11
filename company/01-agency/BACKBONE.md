# BACKBONE — 01-AGENCY (Ecosistema Revenue)
# ADR-003: wrap, mai riscrittura. Sistemi outreach ATTIVI: invariati.

> Fonte verita': `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md`
> Stato live: `company/Memory/state/agency/state.json`
> Trace cicli: `company/Memory/state/agency/trace.jsonl`

## 1. Struttura reparti L2

| Cartella | Reparto | Coordinator | Topologia swarm |
|---|---|---|---|
| `A1-RICERCA/` | Lead & Market Intelligence | AG-A1-COORD (sonnet) | star |
| `A2-ACQUISIZIONE/` | Outreach multicanale | AG-A2-COORD (sonnet) | pipeline + star canali |
| `A3-PREVENTIVI/` | Preventivi problem-first | AG-A3-COORD (opus) | pipeline |
| `A4-DELIVERY/` | Delivery <=7gg + supporto 90gg | AG-A4-COORD (opus) | hierarchical / star ticket |
| `A5-COPY-INTERNO/` | Copy operativo quotidiano | AG-A5-COORD (sonnet) | mesh |
| `A6-MARKETING-INTERNO/` | Vetrina + case study + upsell | AG-A6-COORD (sonnet) | star |

Direttore ecosistema: **AG-DIR** (opus) — riporta a C-Suite.

## 2. Pipeline revenue end-to-end

```
[A1] LEAD --> [A2] OUTREACH --> [A2] REPLY/FOLLOWUP --> CALL (umano: Max)
                                                          |
[A3] PREVENTIVO --> CONTRATTO --> [A4] DELIVERY <=7gg --> [A4] SUPPORTO 90GG
                                                                    |
                                          [A6] TESTIMONIANZA / UPSELL
```

Ogni freccia = handoff contract HC-v1 su BUS.
Ogni step = evento in `trace.jsonl` con: ts, cycle_id, step, event, from, to, hc, agent.

## 3. Handoff contracts inter-reparto (intra-AGENCY)

| ID | Da | A | Payload chiave | Gate |
|---|---|---|---|---|
| `HC-A1-A2-leads` | A1-RICERCA | A2-ACQUISIZIONE | lead_id, score_icp, dati_contatto | qualifier_score >= soglia |
| `HC-A2-A3-call` | A2-ACQUISIZIONE | A3-PREVENTIVI | call_booked, lead_id, thread_conversazione | triage=interessato; call confermata |
| `HC-A3-A4-contratto` | A3-PREVENTIVI | A4-DELIVERY | client_id, prodotto, brief_tecnico, pagamento_confermato | gate_preventivo=PASS; pagamento=verificato |
| `HC-A4-A6-testimonianza` | A4-DELIVERY | A6-MARKETING-INTERNO | client_id, metriche_reali, uat_firmata | delivery_days<=7; UAT firmata; gate_delivery=PASS |

Contracts fisici: `A*/handoffs/HC-*.json`

## 4. Namespace AgentDB (prefisso agency/)

| Namespace | Contenuto | PII |
|---|---|---|
| `agency/leads` | score, stato funnel (specchio semantico leads.db) | no |
| `agency/outreach` | template attivi, performance variante, esiti Bibbia | no |
| `agency/conversations` | thread risposta, obiezioni, esiti triage | YES -> aidefence_has_pii prima dello store |
| `agency/proposals` | preventivi: stato, win/loss, motivi | no |
| `agency/clients` | anagrafica, prodotto, brand_kit, icp, milestone delivery | YES |
| `agency/delivery` | checklist UAT, ambienti, ticket 90gg | no |
| `agency/kpi` | metriche per reparto per ciclo | no |
| `agency/reasoning` | pattern distillati da fallimenti -> ReasoningBank corporate | no |

## 5. Offerta + pricing (catalogo fisso — mai sconti improvvisati)

| Prodotto | Prezzo | Delivery | Supporto |
|---|---|---|---|
| Outreach Factory | EUR 4.000 | 7gg | 90gg |
| Content Factory | EUR 3.500 | 7gg | 90gg |
| Second Brain | EUR 2.500 | 7gg | 90gg |
| Engine Room (bundle) | EUR 8.000 | 7gg | 90gg |

One-time. EUR 0 canoni mensili. Codice di proprieta' del cliente.

## 6. Quality gates

1. **Gate Bibbia** (ESISTENTE — bibbia_team.py, 3 checker): blocca ogni messaggio outreach pre-invio.
2. **Gate Preventivo** (skill proposal-gate): problem-first, pricing catalogo, promesse=prove.
3. **Gate Delivery** (skill delivery-playbook): UAT firmata, workflow sul server cliente, training erogato.
4. **Brand gate corporate** (Sentinel Brand-Voice, Mandato Empire): trasversale.

## 7. KPI target (baseline — misurare dal giorno 1)

| Reparto | KPI principali | Cap/vincolo |
|---|---|---|
| A1 | lead qualificati/gg | — |
| A2 | inviati/gg per canale; reply rate; call/sett | email <=500/gg 100/h; LI 20+20+30; IG 30 DM/gg |
| A3 | call->preventivo <=48h; win rate | pricing fisso |
| A4 | delivery <=7gg; UAT first-pass; NPS | promessa commerciale |
| A5 | % copy passa Bibbia al 1o giro | — |
| A6 | case study per cliente chiuso | — |

## 8. Connessioni

- `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` — dossier completo
- `company/Backbone/Bus/contracts/HC-template.json` — schema HC-v1
- `company/Backbone/Identity-HR/registro-agenti.yaml` — roster agenti AG-*
- `company/Ecosistemi/01-AGENCY/Workflow/outreach-wrapper.md` — wrap L3 pipeline outreach
- `company/Memory/state/agency/` — state.json + trace.jsonl
