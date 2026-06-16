> Fonte: PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md sez. 2 (L2.1 — COPYWRITING)

# L2.1 — COPYWRITING

> Reparto L2 · Priorità: MASSIMA · Ecosistema: 04-MARKETING
> Ecosistema: `company/Ecosistemi/04-MARKETING/ECOSISTEMA.md`
> Backbone: `company/Ecosistemi/04-MARKETING/BACKBONE.md`

---

## Missione

Produrre ogni copy di conversione della holding via framework **APSOC** (Attenzione → Problema → Soluzione/Promessa → Obiezioni → CTA) + **CPB** (Claim → Proof → Benefit), con QA a 100 punti. Servizio trasversale: risponde a richieste da tutti gli ecosistemi committenti tramite handoff contract.

**PRIORITÀ ASSOLUTA:** nessun altro reparto di Marketing diventa operativo prima che questo reparto abbia eseguito almeno un workflow end-to-end gated.

---

## Motore: Copy Workflow Orchestration Layer

Il reparto **ingloba** il sistema esistente in `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/` senza modifiche. La migrazione è un **wrapper di handoff**, non una riscrittura. I file del motore restano fonte di verità finché il wrapper non è validato (fase M1).

Entry point invariato: `/copywriting full|ad|sales-page|email|vsl|social|headline|objections|avatar|funnel|review`

---

## Struttura interna

| Livello | ID | Contenuto |
|---|---|---|
| Coordinatore L2 | `copy-master` | Orchestratore/router: riceve contratto, sceglie workflow L3, spawna A1-A8 |
| Workflow L3 | WF-COPY-FULL | Pipeline completo A1→A8 (motore: `full-copy-workflow.md`) |
| Workflow L3 | WF-COPY-AD | Ad copy 3 varianti (motore: `quick-ad-workflow.md`) |
| Workflow L3 | WF-COPY-SALES-PAGE | Sales page, gate ≥85 (motore: `sales-page-workflow.md`) |
| Workflow L3 | WF-COPY-EMAIL | Sequenze email, in coordinamento con L2.3 (motore: `email-sequence-workflow.md`) |
| Workflow L3 | WF-COPY-VSL | Script VSL 8-20 min (motore: `vsl-workflow.md`) |
| Workflow L3 | WF-COPY-SOCIAL | 5 post in sequenza strategica (motore: `social-post-workflow.md`) |
| Funzione L4 | T-HEADLINE | headline-forge: 10+ headline con formule |
| Funzione L4 | T-OBJECTIONS | objections-forge: CPB per obiezione |
| Funzione L4 | T-AVATAR | target-avatar: buyer persona completa |
| Funzione L4 | T-FUNNEL | funnel-designer: architettura funnel |
| Funzione L4 | T-REVIEW | copy-review: score 100pt su copy esistente |
| Funzione L4 | T-APSOC | apsoc-builder: costruzione APSOC interattiva |

---

## Agenti L5

| Codice | Agente | Ruolo | Stato |
|---|---|---|---|
| — | copy-master | Orchestratore/router L2.1 | ESISTENTE |
| A1 | Briefing Analyst | Raccolta requisiti → briefing-completo.md | ESISTENTE |
| A2 | Target Analyst | Avatar + pain points + language map | ESISTENTE |
| A3 | Attention Writer | Headline + hook (9 strategie) | ESISTENTE |
| A4 | Problem Writer | Problema amplificato (regola: no prodotto) | ESISTENTE |
| A5 | Solution Writer | USP + benefits + post-acquisto | ESISTENTE |
| A6 | Objections Handler | CPB per obiezione (10 tipi) | ESISTENTE |
| A7 | CTA Writer | CTA profondo + urgenza | ESISTENTE |
| A8 | Copy Reviewer | Score APSOC 100pt — gate QA G1 | ESISTENTE |
| S1 | Funnel Strategist | Architettura funnel multi-step | ESISTENTE |
| S2 | Positioning Strategist | Posizionamento, USP, angolo di mercato | ESISTENTE |
| S3 | Campaign Strategist | Strategia campagna multi-canale (prestato a L2.2) | ESISTENTE |

---

## Quality Gates

| Gate | Soglia | Esito fail |
|---|---|---|
| G1 — Score APSOC (A8) | ≥80/100 standard | Iterazione mirata (max 3), poi escalation umana |
| G1b — Score APSOC sales page | ≥85/100 | Iterazione mirata, poi escalation umana |
| G2 — Brand gate Mandato Empire | Checklist binaria | Blocco non derogabile, solo LX può sbloccare |

Regola struttura: **P (Problema) prima di S (Soluzione)** — violazione = −15 automatico.

---

## KPI principali

| KPI | Definizione |
|---|---|
| First-pass rate G1 | % copy che passa A8 ≥80 alla prima iterazione |
| Time-to-copy per formato | Dalla richiesta valida alla consegna gated (ad: 15-20 min; sales page: 90-120 min) |
| Handoff acceptance rate | % consegne accettate dal committente senza rework |

---

## Connessioni

- `company/Ecosistemi/04-MARKETING/ECOSISTEMA.md` — ecosistema padre
- `company/Ecosistemi/04-MARKETING/BACKBONE.md` — infrastruttura
- `company/Ecosistemi/04-MARKETING/Agenti/MKT-0-conductor.md` — coordinatore L1
- `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md` §2, §3, §4a
- `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/` — motore (non modificare)

*Fonte: dossier 04 §2 (L2.1), §3, §4a · Aggiornato: 2026-06-12*
