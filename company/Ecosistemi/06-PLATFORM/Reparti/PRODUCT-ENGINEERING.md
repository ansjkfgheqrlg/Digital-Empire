# PRODUCT-ENGINEERING — 06-PLATFORM

> Reparto responsabile di SaaS e App di Digital Empire: costruzione, mantenimento e iterazione dei prodotti software.

## Missione
Costruire e mantenere i prodotti software di Digital Empire: SaaS (applicazioni web con modello abbonamento), App (tool interni e automatizzazioni come book-factory), e qualsiasi nuovo prodotto digitale che richieda un ciclo PRD → MVP → iterazioni. Differisce da WEB-ENGINEERING per il focus sul prodotto ricorrente (non sul sito one-shot): ha stato, database, autenticazione, billing.

**Principio:** ogni prodotto nasce da un PRD approvato (prd-architect-os, quality score ≥75). Nessun MVP senza PRD.

## Team Agenti
| ID | Agente | Tier | Ruolo |
|---|---|---|---|
| `plt-director` | Direttore PLATFORM | Opus | Approva PRD e architettura prodotto |
| `plt-cc-master` | Orchestratore Esecutivo | Sonnet | Coordina la pipeline PRD→MVP |
| `plt-site-architect` | Architetto | Sonnet | Architettura tecnica (db, auth, API) |
| `plt-site-builder` | Builder | Sonnet | Implementazione MVP (Next.js + Supabase/Prisma) |
| `plt-sec-sentinel` | Security Sentinel | Sonnet | Security + PII su prodotti con dati utente |
| `plt-qa-runner` | QA Runner | Haiku | Test flussi utente con playwright-dev |
| `plt-deploy-op` | Deploy Operator | Haiku | Deploy + monitoring produzione |
| `plt-custodian` | Custodian | Haiku | Registry repo, versioning, changelog |

## Workflow L3
| ID | Workflow | Descrizione |
|---|---|---|
| WF-SAAS-BUILD | Build SaaS | PRD approvato → MVP → iterazioni con feedback loop |
| WF-APP-MAINTAIN | Manutenzione App | manutenzione App/ e book-factory automation |

## Funzioni L4
- **T-prd-review** — review PRD (quality score ≥75) prima di qualsiasi sviluppo
- **T-db-schema** — design database (Supabase / Prisma) con migration plan
- **T-auth-setup** — autenticazione e authorization (NextAuth / Clerk / Supabase Auth)
- **T-api-layer** — API routes Next.js + validazione Zod
- **T-ui-product** — UI prodotto (differisce dai siti: dashboard, forms, tabelle, stati)
- **T-billing** — integrazione Stripe/Lemon Squeezy per SaaS
- **T-mvp-test** — test smoke + E2E flussi critici (onboarding, pagamento, core feature)

## Asset Esistenti Usati
| Path | Utilizzo |
|---|---|
| `Digital Empire/SaaS/` | Codebase SaaS attivi — censire, dare owner, pipeline verify |
| `Digital Empire/App/` | App interni — book-factory automation e altri tool |
| `prd-architect-os` | Skill PRD obbligatoria prima di ogni build prodotto |
| `playwright-dev` | Test E2E flussi utente critici |
| `vercel:deploy` | Deploy + preview environments |
| `security-review` | Obbligatorio su prodotti con dati utente (G-SEC più stringente) |

## Gate di Qualità
```
G-PRD (PRD quality score ≥75, approvato plt-director)
  → G-SEC (aidefence + security-review: più stringente per prodotti con auth/dati)
    → G-QA (playwright E2E su flussi critici: onboarding, core feature, billing)
      → G-DEPLOY (verify + smoke + monitoring 24h post-deploy)
```

**Nota security:** prodotti con autenticazione o dati utente subiscono G-SEC esteso (OWASP Top 10 completo + PII review).

## KPI
| KPI | Target |
|---|---|
| PRD quality score prima dell'approvazione | ≥ 75/100 |
| Uptime SaaS in produzione | ≥ 99.5% |
| Tempo medio risoluzione bug P1 (bloccante) | ≤ 4 ore |
| Repo SaaS/App censiti nel registry PLATFORM | 100% |

## Connessioni
- [[06-ECOSISTEMI-CORE]] — dossier padre
- [[WEB-ENGINEERING]] — reparto fratello (siti vs prodotti)
- [[SECURITY-QUALITY]] — gate G-SEC più stringente per prodotti
- [[DEPLOY-CICD]] — pipeline deploy e monitoring
- [[BACKBONE]] — registro agenti
