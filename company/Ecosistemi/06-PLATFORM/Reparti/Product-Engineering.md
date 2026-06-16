> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. PLATFORM

# L2 PRODUCT-ENGINEERING — SaaS & App

> Reparto L2 · Ecosistema: 06-PLATFORM
> Riferimento: `company/Ecosistemi/06-PLATFORM/ECOSISTEMA.md` · `company/Ecosistemi/06-PLATFORM/BACKBONE.md`

---

## Missione

Costruire, iterare e mantenere i prodotti software propri di Digital Empire: SaaS, App, automazioni di prodotto (es. book-factory). Mentre WEB-ENGINEERING serve i clienti Agency, PRODUCT-ENGINEERING serve la holding stessa come editore/produttore di tool proprietari.

Ogni progetto parte da un PRD generato da `prd-architect-os` (via FORGE) e segue il ciclo MVP → iterazioni cadenzate.

---

## Workflow L3

| Workflow | Descrizione | Gate |
|---|---|---|
| **WF-SAAS-BUILD** | PRD (da FORGE/prd-architect-os) → MVP → iterazioni rilasciate | PRD quality score ≥ 75 prima del build |
| **WF-APP-MAINTAIN** | Manutenzione `App/` e book-factory automation; patch, aggiornamenti dipendenze | verify verde dopo ogni modifica |

---

## Funzioni L4

PRODUCT-ENGINEERING eredita le funzioni L4 tecniche di WEB-ENGINEERING per il codice (build, QA, deploy), con in più:

| ID Funzione | Descrizione |
|---|---|
| T-prd-intake | Ricezione PRD da FORGE, verifica quality score ≥ 75 |
| T-mvp-build | Build MVP con scope minimo (build-implementation) |
| T-iteration-cycle | Sprint di iterazione su feedback utenti/Board |
| T-app-patch | Patch e aggiornamenti su App/ (manutenzione continua) |
| T-book-factory-op | Operatività book-factory automation (KDP pipeline) |

---

## Agenti L5 del reparto

| ID Agente | Ruolo | Tier |
|---|---|---|
| `plt-director` | Direttore PLATFORM — approva architetture prodotto | Opus |
| `plt-cc-master` | Orchestratore build SaaS/App | Sonnet |
| `plt-site-architect` | Architettura tecnica prodotto (API, schema dati, stack) | Sonnet |
| `plt-site-builder` | Implementazione codebase prodotto | Sonnet |
| `plt-qa-runner` | Test e QA prodotto | Haiku |
| `plt-sec-sentinel` | Security review su ogni rilascio | Sonnet |
| `plt-deploy-op` | Deploy Vercel + CI/CD per SaaS | Haiku |

---

## Asset esistenti

| Path | Stato |
|---|---|
| `Digital Empire/SaaS/` | EVOLVI — censire, owner e pipeline |
| `Digital Empire/App/` | EVOLVI — censire, owner e pipeline |
| skill `prd-architect-os` (via FORGE) | USA — PRD obbligatorio pre-build |
| skill `build-implementation` | USA — standard build |
| skill `playwright-dev` | USA — test end-to-end |

---

## Handoff contract

**Riceve da FORGE:** `{PRD_type, quality_score, scope, tech_stack, budget}` → MVP consegnato con codice in custodia  
**Emette verso OPERATIONS:** `{commessa, costo_build, durata, esito}` per cost attribution  
**Emette verso INTELLIGENCE:** post-mortem tecnico + decisioni architetturali → wiki `tools/`

---

## KPI

| KPI | Target |
|---|---|
| PRD quality score pre-build | ≥ 75/100 |
| Build senza regressioni alla delivery | ≥ 90% |
| Repo SaaS/App censiti con owner | 100% |
| Incidenti security post-deploy | 0 |

## Connessioni

- [[06-PLATFORM/ECOSISTEMA.md]] — panoramica PLATFORM
- [[06-PLATFORM/BACKBONE.md]] — namespace AgentDB `platform/build-status`
- [[06-PLATFORM/Reparti/Security-Quality.md]] — G-SEC obbligatorio
- [[06-PLATFORM/Reparti/Deploy-CICD.md]] — deploy finale
- [[PIANO-MAESTRO/06-ECOSISTEMI-CORE.md]] — dossier completo
