# BLUEPRINT — CTO (figura C-level = workflow CF-grade)

> Prodotto da ARCHITETTURA (WF-ARCH-DESIGN, ARCH-BOARD-20260616). Per FORGE. Forma: cartella-workflow (PESANTE).

## Forma scelta + perché
La tecnologia della holding (codice, architettura, sicurezza, integrazione Ruflo) è un dominio
ampio con gate di qualità → cartella-workflow ≥10 agenti, non un ruolo singolo.

## Missione della figura
Custode dell'architettura tecnica e del codice: presidia l'output dell'organo ARCHITETTURA, governa
06-PLATFORM (engineering) e l'organo FORGE lato tecnico, la sicurezza, lo stack, il debito tecnico e
l'integrazione backbone/Ruflo. NON scrive copy né decide revenue: garantisce che la macchina tecnica regga.

## Struttura cartella (FORGE)
```
Board-CSuite/CTO/  ├── README.md ARCHITETTURA.md ├── agenti/(10) principi/ regole/ skills/ scripts/ workflow/(≥2) kpi/ state/
```

## Roster agenti (10)
| Agente | Ruolo | Tier |
|---|---|---|
| cto-conductor | coordina la tecnologia, riporta al CEO | opus |
| cto-architecture-warden | presidia i blueprint dell'organo ARCHITETTURA | opus |
| cto-platform-liaison | punto di contatto con 06-PLATFORM (siti, SaaS, deploy) | sonnet |
| cto-forge-liaison | punto di contatto con l'organo FORGE (build artefatti) | sonnet |
| cto-security-sentinel | aidefence, security-review, has_pii (always-on) | sonnet |
| cto-stack-radar | watch su stack (Next, Tailwind, Vercel, Ruflo) | haiku |
| cto-tech-debt-tracker | inventario e priorità del debito tecnico | haiku |
| cto-integration-architect | integrazione backbone/Ruflo/MCP | sonnet |
| cto-quality-gate | verify Empire + playwright gate pre-deploy | sonnet |
| cto-memoria | ADR tecnici, decisioni d'architettura | haiku |

## Workflow CF-grade (≥2)
- `WF-TECH-REVIEW` — proposta tecnica → architettura (via ARCHITETTURA) → security gate → quality gate → ok/deploy.
- `WF-SECURITY-AUDIT` — scan periodico aidefence + dipendenze + segreti → report rischi.
- `WF-STACK-UPGRADE` — radar stack → proposta upgrade in dry-run → rollout.

## Skill proprie (FORGE)
`empire-verify` (lint+build+playwright+brand gate) · `tech-adr` · `security-preflight`.

## Handoff
→ **06-PLATFORM** (esecuzione build/deploy), ↔ **ARCHITETTURA** (blueprint tecnici), ↔ **FORGE** (nuovi tool/agenti), → **CEO** (rischi tecnici), → **CFO** (costi infra).

## KPI presidiati
0 incidenti security post-deploy · first-pass QA ≥80% · Lighthouse ≥90 · debito tecnico in calo · 100% repo censiti.

## Struct-gate checklist
- [ ] ≥10 agenti · [ ] ≥2 workflow · [ ] principi/regole · [ ] ≥3 skill · [ ] scripts · [ ] kpi/state · [ ] 0 magri/0 vuote

## Note per la FORGE
Base dal v1 `CTO.md`. Collegare cto-architecture-warden all'organo ARCHITETTURA e cto-platform-liaison a 06-PLATFORM (Crea Siti).

## Connessioni
- [[BP-INDEX]] · [[BP-CEO]] · [[14-DOSSIER-ARCHITETTURA]] · Genesi-Core/FORGE
