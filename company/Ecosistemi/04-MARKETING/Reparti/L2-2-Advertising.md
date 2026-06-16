> Fonte: PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md sez. 2 (L2.2 — ADVERTISING)

# L2.2 — ADVERTISING

> Reparto L2 · Ecosistema: 04-MARKETING
> Ecosistema: `company/Ecosistemi/04-MARKETING/ECOSISTEMA.md`
> Backbone: `company/Ecosistemi/04-MARKETING/BACKBONE.md`

---

## Missione

Campagne paid end-to-end (strategia → creative → setup → monitoraggio → iterazione) su **Meta, Google, LinkedIn, TikTok**. Il copy delle ads viene SEMPRE da L2.1 (WF-COPY-AD); Advertising possiede targeting, budget, struttura campagna e testing creativo.

**Vincolo non negoziabile:** nessuna spesa reale senza approvazione umana esplicita. Dry-run di default (pattern #3 del Piano Maestro). AD3 non può lanciare autonomamente.

---

## Struttura interna

| Livello | ID | Contenuto |
|---|---|---|
| Workflow L3 | WF-ADS-CAMPAIGN | Campagna end-to-end: brief → strategia (S3) → creative → setup → launch |
| Workflow L3 | WF-ADS-CREATIVE-TEST | Batch testing creativo: fan-out varianti → matrice test → winner |
| Funzione L4 | T-AUDIENCE | Ricerca e definizione audience/segmenti per piattaforma |
| Funzione L4 | T-CREATIVE-BATCH | Generazione varianti a scala (skill ad-creative) + brief visual a 03-CONTENT-FACTORY |
| Funzione L4 | T-BUDGET-BID | Allocazione budget, strategia bid, pacing (sotto Cost-Sentinel) |
| Funzione L4 | T-AD-COMPLIANCE | Check policy piattaforma pre-pubblicazione |

---

## Agenti L5

| Codice | Agente | Ruolo | Stato |
|---|---|---|---|
| S3 | Campaign Strategist | Strategia campagna multi-canale (prestato da L2.1) | ESISTENTE |
| AD1 | Audience Analyst | Ricerca audience, segmenti, lookalike per piattaforma | NUOVO |
| AD2 | Creative Iterator | Varianti creative a scala da winner (skill ad-creative) | NUOVO |
| AD3 | Media Buyer | Struttura campagna, budget, bid, pacing | NUOVO |
| AD4 | Ad Compliance Checker | Policy Meta/Google/LinkedIn/TikTok pre-flight | NUOVO |

---

## Flusso campagna ads (sintesi §4b)

```
Brief campagna (budget OK esplicito utente — MAI spesa autonoma)
  ▼
S3 Campaign Strategist — obiettivo, canali, struttura, KPI target
  ▼
AD1 Audience Analyst — segmenti per piattaforma ─────────────────┐
  ▼                                                               │ fan-out swarm
WF-COPY-AD (L2.1) — 3+ varianti copy APSOC ─────────────────────┤
  ▼                                                               │
handoff a 03-CONTENT-FACTORY — visual/creative ──────────────────┘
  ▼
AD2 Creative Iterator — matrice copy × visual × audience
  ▼
AD4 Compliance check → AD3 Media Buyer — setup campagna (dry-run)
  ▼
LAUNCH (previa approvazione umana) → monitoraggio AN2 → WF-OPTIMIZATION-LOOP
```

---

## KPI principali

| KPI | Definizione |
|---|---|
| CTR / CPC / CPA per campagna | Per piattaforma; confronto solo variante-vs-variante |
| Esperimenti chiusi con verdetto | Velocità di apprendimento (→ L2.4 loop) |
| Costo per run | Cost-attribution per agente (Cost-Sentinel) |

---

## Connessioni

- `company/Ecosistemi/04-MARKETING/ECOSISTEMA.md` — ecosistema padre
- `company/Ecosistemi/04-MARKETING/Reparti/L2-1-Copywriting.md` — fornitore copy ads
- `company/Ecosistemi/04-MARKETING/Reparti/L2-4-Analytics.md` — monitoraggio e loop
- `company/Ecosistemi/04-MARKETING/Agenti/MKT-AD1-audience-analyst.md`
- `company/Ecosistemi/04-MARKETING/Agenti/MKT-AD3-media-buyer.md`
- `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md` §2 (L2.2), §4b

*Fonte: dossier 04 §2 (L2.2), §4b · Aggiornato: 2026-06-12*
