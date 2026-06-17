---
Type: CONCEPT
Status: Active
Tags: #cto #architettura #gerarchia #flusso #platform #forge #sicurezza
Created: 2026-06-17
Last updated: 2026-06-17
---

# ARCHITETTURA — CTO / Chief Technology Officer

> Blueprint espanso: gerarchia interna, flusso decisionale tecnico, relazioni con Platform / Forge / ARCHITETTURA / sicurezza.
> Fonte: `company/Board-CSuite/_BLUEPRINT/BP-CTO.md` + v1 `CTO.md`
> Connessioni: [[README]] · [[14-DOSSIER-ARCHITETTURA]] · [[BP-CTO]]

---

## 1. Posizione nella gerarchia

```
LX (Mandato)
  └── Board C-Suite (L0)
        └── CTO ← questa figura
              ├── cto-conductor           [Opus]   ← decisore / orchestratore
              ├── cto-architecture-warden [Opus]   ← presidia ARCHITETTURA
              ├── cto-platform-liaison    [Sonnet] ← interfaccia 06-PLATFORM
              ├── cto-forge-liaison       [Sonnet] ← interfaccia FORGE
              ├── cto-security-sentinel   [Sonnet] ← always-on security
              ├── cto-stack-radar         [Haiku]  ← watch stack
              ├── cto-tech-debt-tracker   [Haiku]  ← debito tecnico
              ├── cto-integration-architect [Sonnet] ← backbone/Ruflo/MCP
              ├── cto-quality-gate        [Sonnet] ← gate pre-deploy
              └── cto-memoria             [Haiku]  ← ADR tecnici e memoria
```

Il `cto-conductor` è il baricentro interno: riceve input tecnici da qualsiasi sorgente,
distribuisce l'analisi agli agenti specializzati, integra i risultati e produce la decisione finale.
Non scala mai a CEO senza aver eseguito il ciclo interno completo (security + quality + ADR).

---

## 2. Gerarchia interna — chi coordina chi

**cto-conductor** (Opus) coordina tutti. Ogni agente riporta solo al conductor:
- Non ci sono sub-coordinatori.
- `cto-memoria` gira sempre in apertura (RECALL) e in chiusura (write ADR/checkpoint).
- `cto-security-sentinel` è always-on: può fermare qualsiasi flusso se rileva un rischio critico.
- `cto-architecture-warden` e `cto-quality-gate` sono i due gate bloccanti nel WF-TECH-REVIEW.

---

## 3. Flusso decisionale tecnico (logica principale)

```
Input tecnico (da: ecosistema, figura Board, organo ARCHITETTURA, scan periodico)
  │
  ▼
[STEP 0] cto-memoria: RECALL — carica ADR tecnici attivi, stato repo, debito corrente
  │
  ▼
[STEP 1] cto-conductor: classifica l'input
  ├── "architettura" → cto-architecture-warden (valida allineamento blueprints)
  ├── "sicurezza"    → cto-security-sentinel (scan immediato)
  ├── "deploy"       → cto-platform-liaison (check ambiente staging)
  ├── "build forge"  → cto-forge-liaison (brief artefatto)
  ├── "integrazione" → cto-integration-architect (analisi backbone/Ruflo)
  └── "stack watch"  → cto-stack-radar (valutazione upgrade)
  │
  ▼
[STEP 2] Agente specializzato produce analisi/proposta
  │
  ▼
[STEP 3] Gate SECURITY: cto-security-sentinel verifica assenza segreti, vulnerabilità, PII
  │       ↳ KO → blocca e produce security-report → conductor decide se escalare a CEO
  ▼
[STEP 4] Gate QUALITY: cto-quality-gate esegue empire-verify (lint + build + playwright + brand)
  │       ↳ KO → blocca, cto-tech-debt-tracker registra l'item, conductor prioritizza
  ▼
[STEP 5] cto-conductor: integra analisi + gate + eventuali ADR
          produce decisione tecnica finale
  │
  ▼
[STEP 6] cto-memoria: write — ADR tecnico se decisione architetturale, checkpoint CP-YYYYMMDD-NNN
  │
  ▼
[STEP 7] Handoff → 06-PLATFORM (deploy) | ARCHITETTURA (feedback blueprints) | CEO (se escalation)
```

---

## 4. Relazione con l'organo ARCHITETTURA

L'organo ARCHITETTURA produce i **blueprint tecnici** della holding (design di sistema, struttura
cartelle, schemi I/O, diagrammi di flusso). Il CTO è il **cliente primario** dei blueprint e il
loro **gate di approvazione**:

- `cto-architecture-warden` legge ogni nuovo blueprint prodotto dall'organo ARCHITETTURA.
- Verifica la coerenza con lo stack attuale, gli ADR tecnici, e le capacità di 06-PLATFORM.
- Se il blueprint introduce una tecnologia non nel radar → `cto-stack-radar` viene interpellato.
- Se il blueprint richiede una nuova integrazione → `cto-integration-architect` valida la fattibilità.
- Approvazione CTO = blueprint pronto per essere forgiato da FORGE.

**Flusso bidirezionale:** ARCHITETTURA progetta, CTO approva o rimanda con delta tecnici.
Il CTO non ridisegna i blueprint: delega il redesign all'organo ARCHITETTURA con brief preciso.

---

## 5. Relazione con 06-PLATFORM

06-PLATFORM esegue il build e il deploy (siti, SaaS, landing pages, sistemi). Il CTO:

- Definisce gli **standard tecnici** che 06-PLATFORM deve rispettare (struttura cartelle,
  naming, CI/CD, dry-run obbligatorio, zero segreti nel repo).
- Non esegue direttamente il deploy: dispatcha direttive a `cto-platform-liaison` che traduce
  le decisioni tecnica in handoff contract verso 06-PLATFORM.
- `cto-quality-gate` verifica il gate pre-deploy prima di ogni push in produzione.
- Ogni incidente in produzione risale a CTO per il post-mortem tecnico.

---

## 6. Relazione con l'organo FORGE

FORGE costruisce le skill, gli agenti e i workflow della holding. Il CTO supervisiona FORGE
**lato tecnico** (non lato creativo/strategico, che è del Chief-Forge):

- `cto-forge-liaison` è il punto di contatto: riceve brief tecnici da FORGE, verifica che
  gli artefatti rispettino gli standard (schema I/O, naming, dry-run mode, acceptance criteria).
- Nuova skill proposta da FORGE → CTO verifica: introduce dipendenze nuove? Rischi di sicurezza?
  Conflitti con ADR tecnici esistenti?
- `cto-security-sentinel` scansiona ogni nuovo artefatto prima che sia pubblicato nel catalogo.

---

## 7. Presidio della sicurezza (always-on)

`cto-security-sentinel` è l'unico agente a operare **fuori dal ciclo normale**: può fermare
qualsiasi workflow in qualsiasi momento se rileva:
- Segreti (API key, password, token) nel codice o nel repo.
- Vulnerabilità critiche nelle dipendenze.
- PII non anonimizzate in output/log.
- Pattern injection nei prompt degli agenti.

Quando scatta il blocco di sicurezza, il conductor NON può overridarlo senza un ADR esplicito
e senza l'escalation al CEO. La sicurezza è il vincolo invariante di questa figura.

---

## 8. Invarianti tecnici (da v1 CTO.md — ampliati)

| Invariante | Regola | Fonte |
|---|---|---|
| Struttura cartelle | `company/` rispecchia `PIANO-MAESTRO/` — mai divergere | ADR-002 |
| Schema agenti | ogni agente: input/output JSON esplicito + acceptance criteria | standard CF-grade |
| Dry-run obbligatorio | ogni workflow: dry-run mode prima di qualsiasi spesa reale | pattern #3 |
| Segreti | mai nel repo; `.env` locale + `.gitignore` blindato | ADR-004 |
| Repo annidati | `.git.bak` — non ripristinare senza ADR | ADR-004 |
| Wrap-first | prima di modificare: esiste già qualcosa? Wrappa, non riscrivere | principio P3 |
| ADR tecnici | ogni decisione architetturale produce un ADR in `Memory/decisions/` | ADR-002 |

---

## Connessioni

- [[README]] · `company/Board-CSuite/CTO/README.md`
- [[BP-CTO]] · `company/Board-CSuite/_BLUEPRINT/BP-CTO.md`
- [[cto-conductor]] · `agenti/cto-conductor.md`
- [[cto-architecture-warden]] · `agenti/cto-architecture-warden.md`
- [[cto-security-sentinel]] · `agenti/cto-security-sentinel.md`
- [[WF-TECH-REVIEW]] · `workflow/WF-TECH-REVIEW.md`
- [[14-DOSSIER-ARCHITETTURA]] · `PIANO-MAESTRO/14-DOSSIER-ARCHITETTURA.md`
- [[12-DOSSIER-MAXIMILIAN]] · `PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`
