# Decision Trees — 6 Alberi Decisionali

> **Fonte:** Knowledge Pack 05-decision-trees + estrazioni da Ruflo, Content-Forge, Context-Engineering-Advisor.

## DT01 — Topology Selection
**Domanda:** Quale topologia di swarm usare?

```
Tipo di coordinamento necessario?
├── Gerarchico (comando centrale) → Hierarchical
│   └── Esempio: conductor + sub-agents (PT01)
├── Collaborativo (parità tra agenti) → Mesh
│   └── Esempio: peer-to-peer builders
└── Sequenziale (pipeline) → Pipeline
    └── Esempio: Content-Forge 9-stage (PT02)
```

**Fattori:**
- Complexità task: alta → hierarchical, bassa → mesh
- Dipendenze tra agenti: forti → pipeline, deboli → mesh
- Scalabilità necessaria: alta → hierarchical, bassa → mesh

---

## DT02 — Agent Count
**Domanda:** Quanti agenti creare?

```
Scope del progetto?
├── Piccolo (1-3 task) → Minimal (≤10 agenti)
│   └── Conductor + 3-5 builders + 1-2 QA
├── Medio (4-10 task) → Standard (10-25 agenti)
│   └── Conductor + 8-15 builders + 3-5 QA + 2-3 domain
└── Grande (10+ task) → Large (25+ agenti)
    └── Full swarm: conductor + pipeline + builders + domain + QA + optimizers + SI
```

**Fattori:**
- Budget token: limitato → minimal, ampio → large
- Tempo disponibile: poco → minimal, tanto → large
- Complessità dominio: bassa → minimal, alta → large

---

## DT03 — Memory Strategy
**Domanda:** Quale strategia di memoria adottare?

```
Durata sessione e necessità di persistenza?
├── Single-session, no persistenza → Short-term only
│   └── Solo conversazione, niente memory/
├── Multi-session, persistenza base → Two-layer
│   └── Short-term (session) + Long-term (file system)
└── Multi-session, ricerca avanzata → Full (AgentDB)
    └── Two-layer + AgentDB HNSW + SONA (Ruflo)
```

**Fattori:**
- Numero sessioni: 1 → short-term, 2+ → two-layer/full
- Necessità ricerca semantica: no → two-layer, sì → full
- Disponibilità Ruflo: no → two-layer, sì → full

---

## DT04 — Depth vs Breadth
**Domanda:** Prioritizzare profondità o ampiezza?

```
Stadio del progetto?
├── Iniziale (fondamenta) → Depth-first (P08)
│   └── Costruire profondità prima di espandere
├── Intermedio (base solida) → Breadth-first
│   └── Espandere copertura
└── Avanzato (copertura ampia) → Depth-first again
    └── Approfondire dove necessario
```

**Fattori:**
- Stadio progetto: iniziale/avanzato → depth, intermedio → breadth
- Requisiti utente: profondità richiesta → depth, copertura richiesta → breadth
- Risorse: limitate → depth, abbondanti → breadth

---

## DT05 — Meta-Recursive Need
**Domanda:** La skill deve produrre altre skill (PT08)?

```
La skill deve auto-migliorarsi o produrre varianti?
├── Sì, auto-miglioramento → Meta-recursive (PT08)
│   └── Includere meta-recursive-builder, self-ref in playbook
├── Sì, produrre varianti → Meta-recursive + skill-builder
│   └── Includere skill-builder + meta-recursive-builder
└── No, skill statica → No meta-recursive
    └── Omettere meta-recursive-builder
```

**Fattori:**
- Necessità auto-miglioramento: sì → PT08, no → no PT08
- Necessità produrre altre skill: sì → skill-builder + PT08, no → no
- Complessità accettabile: alta → PT08, bassa → no PT08

---

## DT06 — Release Readiness
**Domanda:** La skill è pronta per il rilascio?

```
Tutti i validation gate sono PASS?
├── Sì → Pronto per release
│   └── Procedere con PR07 (packaging)
└── No → Non pronto
    ├── Gap critici (agenti incompleti, validation FAIL) → Fix required
    │   └── Tornare a PR03/PR04, fix, re-validate
    └── Gap minori (coverage <100%, FM entries <5) → Fix optional
        └── Documentare gap, procedere con release (con disclaimer)
```

**Fattori:**
- Validation status: all PASS → ready, any FAIL → not ready
- Gap severity: critici → fix required, minori → fix optional
- Deadline: stretta → release con gap, ampia → fix before release

---

## Connessioni
- **Principi correlati:** P01 (iterative planning), P04 (interactive), P06 (shapes), P08 (depth)
- **Pattern correlati:** PT01 (conductor), PT02 (pipeline), PT05 (canonical files), PT08 (meta-recursive)
- **Processi correlati:** PR01 (plan creation), PR03 (agent construction), PR04 (validation), PR07 (packaging)
- **Agenti:** plan-builder (DT01/DT02), conductor (DT03), target-schema-validator (DT06)
