# 🖥️ 06a — ECOSISTEMA PLATFORM V2 (Dossier EMPIRE OS)

> Dossier v2 (V2-2, ADR-007) — nasce dallo **SPLIT** del v1 `06-ECOSISTEMI-CORE.md` (che
> impacchettava insieme PLATFORM, FORGE, INTELLIGENCE, OPERATIONS) in **4 dossier V2
> indipendenti**, uno per ecosistema core (decisione registrata in `V2-INDEX.md` §"Proposta
> split 06-CORE"). Questo file amplia a scala CF-grade la sezione "06 · PLATFORM" del v1
> (righe 31-145). La **matrice di dipendenza tra i 4 core** — INTELLIGENCE → FORGE → PLATFORM,
> con OPERATIONS trasversale (v1 §Chiusura, righe 497-536) — resta il riferimento condiviso
> valido per tutti e 4 i dossier e NON viene riscritta qui: si cita, non si duplica.
>
> **Ecosistema L1 #06 della holding Digital Empire Group — uno dei 4 core trasversali** (gli
> altri: [[06b-ECOSISTEMA-FORGE-V2]], [[06c-ECOSISTEMA-INTELLIGENCE-V2]],
> [[06d-ECOSISTEMA-OPERATIONS-V2]]). PLATFORM è il "kernel + driver" di EMPIRE OS: produce e
> custodisce TUTTO il codice della holding. È l'unico ecosistema autorizzato a scrivere
> codice di produzione.
>
> Versione: 2.0 · Creato: 2026-07-19 · Fase roadmap: V2-2
> Supera il v1 `06-ECOSISTEMI-CORE.md` §PLATFORM per profondità e scala. Il v1 resta
> riferimento intatto, non toccato da questo dossier. Standard: CF-grade
> (§0 piano V2 `11-PIANO-V2-DIRETTIVA-SCALA.md`).

---

## 0. Missione + DONE WHEN

**MISSIONE (ereditata dal v1, invariata):** essere il reparto engineering della holding:
produrre e mantenere TUTTO il codice di Digital Empire — siti premium (DE e clienti), SaaS/App,
tooling interno — con custodia del codice, sicurezza, CI/CD e deploy. PLATFORM è l'unico
ecosistema autorizzato a scrivere codice di produzione.

In v1 PLATFORM era 5 reparti con **11 agenti totali** in tutto l'ecosistema — sotto lo standard
minimo di un solo reparto v2 (6-10 agenti). In v2, applicando §2 della direttiva di scala,
PLATFORM diventa un **ecosistema a 5 reparti**, di cui uno — **WEB-ENGINEERING** (il reparto
"Crea Siti", già operativo, già il più grande e maturo dell'intera holding) — è un
**MEGA-REPARTO**: gerarchia interna propria (leader di reparto → capi area → coordinatori →
verificatori → worker, §2 direttiva: "mega-reparti = aziende dentro l'azienda"). Gli altri 4
reparti (PRODUCT-ENGINEERING, TOOLING & AUTOMATION, SECURITY & QUALITY, DEPLOY & CI/CD) sono
portati allo standard 6-10 agenti + 1-5 workflow CF-grade ciascuno.

**DONE WHEN:**

| # | Criterio | Origine |
|---|---|---|
| 1 | Crea Siti formalizzato come L2 WEB-ENGINEERING con team L3 documentati; produce un sito cliente end-to-end senza intervento manuale fuori dai gate | v1, confermato |
| 2 | Ogni repo/progetto (`agency-empire-landing`, `SaaS/`, `App/`, siti clienti) ha owner, pipeline di verify e procedura di deploy Vercel documentata | v1, confermato |
| 3 | `verify.sh` Empire gira verde su ogni deliverable prima del deploy | v1, confermato |
| 4 | Zero codice orfano: ogni script attivo (incl. quelli di Outreach) è censito nel registry PLATFORM con owner e stato | v1, confermato |
| 5 | I 5 reparti L2 hanno org L3/L4 documentata, team a schede millimetriche (standard §0 piano V2), e almeno un workflow CF-grade eseguito end-to-end ciascuno | v2 NUOVO |
| 6 | WEB-ENGINEERING ha gerarchia interna documentata (aree, capi area, coordinatori) — non è più un elenco piatto di 8 agenti come nel v1 | v2 NUOVO |
| 7 | Namespace memoria `platform/...` inizializzato; ogni workflow produce state ripartibile a freddo (test amnesia §6 piano V2) | v2 NUOVO |
| 8 | Skill proprie dell'ecosistema forgiate (≥3, vedi §6) via 06b-FORGE con PRD+architettura (standard §8 piano V2) | v2 NUOVO |

**OUT OF SCOPE (ora):** scrittura di copy (→ 04-MARKETING, PLATFORM monta il copy, non lo
scrive — v1 §2); ricerca tecnica autonoma su stack/librerie senza passare da 06c-INTELLIGENCE;
spesa infrastrutturale (hosting, servizi a pagamento, licenze SaaS terze) senza ok esplicito
di Max (vincolo globale, pattern #9 Piano Maestro).

---

## 1. Posizione nella holding — PLATFORM è l'engineering di tutti

```
                    👑 LX — Mandato Empire (custodia del codice, dry-run default, security-first)
                              |
L0  C-Suite ────── CTO ───────┤  (CTO = figura Board v2, workflow CF-grade — vedi 12-DOSSIER-MAXIMILIAN)
                              |
L1  06a-PLATFORM  ◄────── handoff contract ──────► tutti gli altri ecosistemi
        │
        ├── DIPENDE DA: 06b-FORGE (nuovi agenti/skill engineering, es. nuova skill site-*),
        │              06c-INTELLIGENCE (ricerca tecnica: stack, librerie, competitor tecnici),
        │              06d-OPERATIONS (runtime swarm, cost attribution, scheduling deploy)
        └── SERVE:    01-AGENCY        — siti clienti, implementazioni, code custody
                      02-INFO-BUSINESS  — sales page tecniche, piattaforma corsi
                      03-CONTENT-FACTORY — tooling pubblicazione, embed/ottimizzazione asset
                      04-MARKETING      — landing/funnel tecnici (implementa L2.6 Conversion Architecture)
                      05-MULTI-BUSINESS — SaaS/App, automazioni KDP/YT (book-factory)
```

### 1.1 Handoff espliciti — chi chiede cosa a PLATFORM

| Committente | Cosa richiede | Formato tipico | Reparto / Workflow destinazione |
|---|---|---|---|
| **01 AGENCY** | Sito cliente completo, implementazione tecnica, code custody a fine commessa | `sito-completo`, `implementazione`, `handover-codice` | L2.1 WEB-ENGINEERING / WF-SITE-FULL + L2.3 TOOLING / WF-CODE-CUSTODY |
| **02 INFO-BUSINESS** | Sales page tecnica, piattaforma corsi/membership | `sales-page-tech`, `piattaforma` | L2.1 WEB-ENGINEERING / WF-SITE-FULL o WF-LANDING-RAPIDA |
| **03 CONTENT-FACTORY** | Tooling di pubblicazione; embed e ottimizzazione performance di asset visual/video | `embed`, `perf-opt` | L2.1 WEB-ENGINEERING (T-site-qa) + L2.3 TOOLING & AUTOMATION |
| **04 MARKETING** | Implementazione tecnica di landing/funnel disegnati da L2.6 Conversion Architecture | `landing`, `funnel-tecnico` | L2.1 WEB-ENGINEERING / WF-LANDING-RAPIDA |
| **05 MULTI-BUSINESS** | MVP SaaS/App, automazioni KDP/YT (book-factory automation) | `mvp`, `automazione` | L2.2 PRODUCT-ENGINEERING / WF-SAAS-BUILD, WF-APP-MAINTAIN |
| **06b FORGE** | Installazione nuovi agenti/skill engineering consegnati (es. nuova skill site-*) | `skill-nuova`, `agente-nuovo` | Reparto destinatario secondo competenza della skill |
| **06c INTELLIGENCE** | Fornisce ricerca tecnica (in ingresso, non su richiesta) prima di ogni scelta d'architettura | — | L2.1/L2.2 consultano PRIMA di ogni scelta stack |

**Regola non negoziabile:** nessun ecosistema business scrive o modifica codice di produzione
in autonomia. Può fornire brief e contenuti (copy, asset), ma l'implementazione e il deploy
vivono in PLATFORM.

### 1.2 Contratto di handoff standard

```json
{
  "committente": "01-AGENCY | 02-INFO | 03-CF | 04-MKT | 05-MB | 06b-FORGE",
  "formato": "sito-completo | landing | sales-page-tech | mvp | automazione | implementazione | handover-codice | embed | skill-nuova",
  "brand_kit": "riferimento brand kit cliente o empire-premium-style (default DE)",
  "scope": "descrizione funzionale + vincoli tecnici (stack, integrazioni, performance target)",
  "deadline": "YYYY-MM-DD",
  "budget_max": "obbligatorio se il deliverable prevede spesa infrastrutturale (hosting, licenze) — cost guard 06d-OPERATIONS"
}
```

Risposta di PLATFORM: `{deliverable, url_staging_prod, verify_report, security_report,
costo_evento, workflow_eseguito}`.

**Regole del contratto (non negoziabili):**
- Richiesta senza `brand_kit` → si applica `empire-premium-style` di default.
- Scelta di stack/libreria mai usata in DE → consultazione obbligatoria 06c-INTELLIGENCE prima
  del build (v1 §2, riga "INTELLIGENCE → PLATFORM").
- Ogni build/deploy emette un evento `{commessa, costo, durata, esito}` verso 06d-OPERATIONS
  (v1 §2, riga "PLATFORM → OPERATIONS") — nessun deliverable esce senza evento costo.

---

## 2. Reparti L2 v2 — 5 reparti, uno mega

Il v1 aveva già 5 reparti nominati ma con **11 agenti totali in tutto l'ecosistema** — un
sesto della soglia minima di un singolo reparto v2. In v2 nessun reparto nuovo si aggiunge
(i 5 del v1 coprono già lo scope reale), ma ognuno viene portato a scala:

```
06a-PLATFORM (L1) — coordinatore: PLT-Director
 ├── L2.1 WEB-ENGINEERING          ← MEGA-REPARTO ("Crea Siti"), gerarchia propria (§2.1)
 ├── L2.2 PRODUCT-ENGINEERING      ← SaaS & App
 ├── L2.3 TOOLING & AUTOMATION     ← codice interno, script, dashboard
 ├── L2.4 SECURITY & QUALITY       ← aidefence, security-review, verify, playwright
 └── L2.5 DEPLOY & CI/CD           ← Vercel, rollback, smoke test, cost event
```

---

### L2.1 — WEB-ENGINEERING (MEGA-REPARTO — "Crea Siti", azienda dentro l'azienda)

**Missione:** produrre siti premium (DE e clienti) end-to-end — dal brief al deploy — con lo
stile empire-premium-style, senza intervento manuale fuori dai gate. **Ingloba il sistema
Crea Siti esistente come motore: non si riscrive, si formalizza sopra con nomi L2/L3/L4 e
gerarchia interna** (ADR-003).

**Dove il v1 era carente:** il v1 elencava 8 agenti (`plt-site-architect` → `plt-custodian`)
come lista piatta, senza gerarchia interna né aree. Per un reparto che è già il più grande e
il più operativo della holding (20+ skill site-*, orchestrators, sistema Crea Siti maturo),
un elenco piatto sottostima la complessità reale. In v2 il reparto ha **gerarchia interna
esplicita** (§2 direttiva: "mega-reparti = aziende dentro l'azienda") con un capo reparto,
un verificatore capo, e 4 aree specializzate.

```
WEB-ENGINEERING (mega-reparto)
 ├─ Leadership:              plt-web-lead (capo reparto) · plt-web-qa-lead (verificatore capo)
 ├─ AREA STRATEGY & ARCH.:   plt-site-architect · plt-brief-analyst · plt-stack-selector
 ├─ AREA BUILD:              plt-site-builder · plt-site-designer · plt-component-builder · plt-site-copy-merger
 ├─ AREA MOTION & 3D:        plt-motion-eng · plt-3d-eng
 ├─ AREA QUALITY & PERF.:    plt-qa-runner · plt-seo-tech · plt-perf-auditor
 └─ AREA RESTYLE & RAPID:    plt-restyle-specialist · plt-landing-rapid-builder
```

#### Team L2.1 (16 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `plt-web-lead` | Web-Engineering Lead | coordinator | opus | **NUOVO v2** (era `plt-cc-master`, promosso a capo mega-reparto): coordina le 4 aree, arbitra scope, risponde dei KPI dell'intero reparto |
| `plt-web-qa-lead` | Web-Engineering QA Lead | verifier | opus | **NUOVO v2:** supervisore del gate G-QA/G-BRAND; decide fix mirato vs rifacimento; traccia first-pass rate del mega-reparto |
| `plt-site-architect` | Site Architect | worker | sonnet | (esistente) Architettura informativa + stack (site-architecture, site-stack) |
| `plt-brief-analyst` | Brief Analyst | worker | sonnet | **NUOVO v2:** raccoglie e valida il brief cliente (T-site-brief) prima che l'architettura parta |
| `plt-stack-selector` | Stack Selector | worker | haiku | **NUOVO v2:** sceglie lo stack per progetto (Next.js 15/16, Tailwind v4) da matrice validata; escalation a 06c-INTELLIGENCE se stack nuovo |
| `plt-site-builder` | Site Builder | worker | sonnet | (esistente) Implementazione Next.js 15/16 + Tailwind v4 (agente site-build) |
| `plt-site-designer` | Site Designer | worker | sonnet | **NUOVO v2:** design visivo (site-design) — palette, layout, componenti prima del build |
| `plt-component-builder` | Component Builder | worker | sonnet | **NUOVO v2:** libreria componenti riusabili (site-components), owner di WF-COMPONENT-LIBRARY |
| `plt-site-copy-merger` | Site Copy Merger | worker | haiku | (esistente) Integra il copy di MARKETING nei componenti (agente site-copy) |
| `plt-motion-eng` | Motion Engineer | worker | sonnet | (esistente) Animazioni Lenis/Framer/GSAP (site-animate) |
| `plt-3d-eng` | 3D Engineer | worker | sonnet | **NUOVO v2:** split da motion — elementi 3D (site-3d), WebGL/Three.js dove richiesto |
| `plt-qa-runner` | QA Runner | worker | haiku | (esistente) QA browser con playwright-dev + verify (agente site-qa) |
| `plt-seo-tech` | SEO Tech | worker | haiku | (esistente) SEO tecnico on-build (site-seo, schema) |
| `plt-perf-auditor` | Performance Auditor | worker | haiku | **NUOVO v2:** audit Lighthouse dedicato, owner del KPI performance ≥90 |
| `plt-restyle-specialist` | Restyle Specialist | worker | sonnet | **NUOVO v2:** owner di WF-EMPIRE-RESTYLE (sito esistente → stile premium DE) |
| `plt-landing-rapid-builder` | Landing Rapid Builder | worker | haiku | **NUOVO v2:** owner di WF-LANDING-RAPIDA (< 48h, market-landing + site-premium-stack) |

#### Workflow L3 di L2.1 (5 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-SITE-FULL** | Pipeline completa: brief → plan → design → copy-merge → build → qa → deploy | G-SEC + G-QA + G-BRAND + G-DEPLOY tutti verdi (v1 §7) |
| **WF-EMPIRE-RESTYLE** | Sito esistente → stile premium DE (empire-premium-style): audit sorgente, rebuild Next.js 15, token design, motion | G-BRAND (stile conforme a empire-premium-style); G-QA su regressioni |
| **WF-LANDING-RAPIDA** | Landing singola < 48h (market-landing + site-premium-stack) | G-QA + G-BRAND; SLA 48h come parte del gate |
| **WF-SITE-QA-SPRINT** | **NUOVO v2:** sprint dedicato QA+SEO+performance su un sito già live (non solo pre-deploy) | Lighthouse ≥90 confermato; SEO tech verde; nessuna regressione vs baseline |
| **WF-COMPONENT-LIBRARY** | **NUOVO v2:** costruzione/manutenzione della libreria componenti condivisa tra progetti (riduce tempo build ripetuto) | plt-web-qa-lead approva; componente pubblicato in `platform/sites/patterns` |

#### Funzioni L4 di L2.1

`T-site-brief` · `T-site-architecture` · `T-site-design` · `T-site-components` ·
`T-site-animate` · `T-site-3d` · `T-site-seo` · `T-site-qa` · `T-site-report` · `T-audit-sorgente` ·
`T-rebuild-next15` · `T-token-design` (palette ink/orange/silver) · `T-motion` (Lenis/GSAP) ·
`T-stack-select` **[NUOVO v2]** · `T-component-publish` **[NUOVO v2]**.

---

### L2.2 — PRODUCT-ENGINEERING (SaaS & App)

**Missione:** costruire e mantenere i prodotti software propri della holding (SaaS/, App/,
book-factory automation) — dal PRD (fornito da 06b-FORGE via prd-architect-os) all'MVP, fino
alle iterazioni.

**Dove il v1 era carente:** il v1 non aveva nemmeno un agente nominato per questo reparto —
solo 2 workflow (WF-SAAS-BUILD, WF-APP-MAINTAIN) senza team. In v2 il reparto ha 8 agenti con
lead, QA e specialisti dedicati.

#### Team L2.2 (8 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `plt-product-lead` | Product Engineering Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; riceve PRD, assegna build/manutenzione, risponde dei KPI prodotto |
| `plt-prd-intake` | PRD Intake Specialist | worker | sonnet | **NUOVO v2:** riceve il PRD da `frg-prd-architect` (06b-FORGE), lo traduce in task di build |
| `plt-app-builder` | App Builder | worker | sonnet | **NUOVO v2:** build/iterazione di `Digital Empire/App/` |
| `plt-saas-builder` | SaaS Builder | worker | sonnet | **NUOVO v2:** build/iterazione di `Digital Empire/SaaS/` |
| `plt-app-maintainer` | App Maintainer | worker | haiku | **NUOVO v2:** owner di WF-APP-MAINTAIN, incl. book-factory automation |
| `plt-product-qa` | Product QA Verifier | verifier | haiku | **NUOVO v2:** verifica funzionale + verify.sh prima di ogni rilascio prodotto |
| `plt-release-manager` | Release Manager | worker | sonnet | **NUOVO v2:** gestisce iterazioni, changelog, versioning |
| `plt-product-registrar` | Product Registrar | worker | haiku | **NUOVO v2:** censisce SaaS/App con owner e pipeline (DONE WHEN #2 v1) |

#### Workflow L3 di L2.2 (4 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-SAAS-BUILD** | PRD (da 06b-FORGE/prd-architect-os) → MVP → iterazioni | `plt-product-qa` verde; PRD quality score ≥75 rispettato a build |
| **WF-APP-MAINTAIN** | Manutenzione `App/` e book-factory automation | Nessuna regressione; verify.sh verde |
| **WF-PRODUCT-ITERATION** | **NUOVO v2:** ciclo iterazione post-lancio (feedback → priorità → build → release) | Release note + changelog aggiornato; regressione zero |
| **WF-PRODUCT-REGISTRY** | **NUOVO v2:** censimento SaaS/App con owner, pipeline, stato — colma DONE WHEN #2 v1 | 100% prodotti censiti in `platform/product/registry` |

---

### L2.3 — TOOLING & AUTOMATION (codice interno)

**Missione:** costruire e mantenere script/CLI interni (pipeline outreach, dashboard) e
custodire il codice attivo con registry e ownership — **senza mai toccare i flussi attivi**
(rischio #4 Piano Maestro: gli script Outreach sono operativi e non vanno rotti).

**Dove il v1 era carente:** 2 workflow senza team dedicato; `plt-custodian` (v1) era l'unico
agente per l'intero code custody. In v2 il reparto ha 7 agenti, con la funzione custody
sdoppiata in censimento registry + gestione handover.

#### Team L2.3 (7 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `plt-tooling-lead` | Tooling & Automation Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; arbitra priorità tra script interni |
| `plt-script-builder` | Script Builder | worker | sonnet | **NUOVO v2:** build script/CLI interni (build-implementation) |
| `plt-dashboard-dev` | Dashboard Developer | worker | sonnet | **NUOVO v2:** codice della dashboard holding (supporta 06d-OPERATIONS che la usa) |
| `plt-outreach-code-custodian` | Outreach Code Custodian | worker | haiku | (evoluzione di `plt-custodian`) **WRAPPA** `Outreach/*.py`, `*.bat` — registry + verify, NON tocca i flussi attivi |
| `plt-repo-registrar` | Repo Registrar | worker | haiku | (evoluzione di `plt-custodian`) Registry di tutti i repo/script con owner e stato |
| `plt-code-custody-lead` | Code Custody Lead | worker | sonnet | **NUOVO v2:** procedura di handover codice cliente (repo transfer, env, docs, 90gg supporto) |
| `plt-tooling-qa` | Tooling QA Verifier | verifier | haiku | **NUOVO v2:** verify.sh su ogni script interno prima del merge |

#### Workflow L3 di L2.3 (3 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-TOOL-BUILD** | Script/CLI interni (es. pipeline outreach, dashboard) — build-implementation | `plt-tooling-qa` verde; nessuna modifica a flussi Outreach attivi senza approvazione esplicita |
| **WF-CODE-CUSTODY** | Repo hygiene, ownership, handover codice ai clienti (€0 canoni = codice loro) | Checklist `code-custody` completa; cliente conferma ricezione |
| **WF-REPO-CENSUS** | **NUOVO v2:** censimento periodico di tutti i repo/script con owner e stato | 100% repo in `platform/registry/repos` — colma DONE WHEN #4 v1 |

---

### L2.4 — SECURITY & QUALITY

**Missione:** garantire che nessun deliverable esca senza sicurezza e qualità verificate:
aidefence scan, security-review, verify.sh, test browser reali (playwright-dev).

**Dove il v1 era carente:** 1 agente (`plt-sec-sentinel`) per l'intero reparto, senza QA
dedicata oltre a `plt-qa-runner` (che in v2 resta in WEB-ENGINEERING, focalizzato sul sito).
In v2 SECURITY & QUALITY ha un reparto autonomo con 7 agenti che copre sicurezza trasversale
a TUTTI i deliverable PLATFORM, non solo i siti.

#### Team L2.4 (7 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `plt-sec-lead` | Security & Quality Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; risponde del KPI "incidenti security post-deploy = 0" |
| `plt-sec-sentinel` | Security Sentinel | worker | sonnet | (esistente) Security always-on: aidefence, security-review, has_pii |
| `plt-security-reviewer` | Security Reviewer | worker | sonnet | **NUOVO v2:** operatore dedicato security-review su ogni deliverable non-sito (script, SaaS/App) |
| `plt-verify-runner` | Verify Runner | worker | haiku | **NUOVO v2:** esegue `verify.sh` Empire su ogni deliverable prima del deploy (DONE WHEN #3 v1) |
| `plt-playwright-tester` | Playwright Tester | worker | haiku | **NUOVO v2:** test browser reali (playwright-dev) su prodotti oltre ai siti |
| `plt-quality-auditor` | Quality Auditor | verifier | sonnet | **NUOVO v2:** traccia first-pass QA rate; decide iterazione mirata vs rework totale |
| `plt-pii-guard` | PII Guard | verifier | haiku | **NUOVO v2:** verifica `has_pii` su codice/config che tocca dati cliente (Art.7 Mandato) |

#### Workflow L3 di L2.4 (3 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-SEC-SCAN** | aidefence scan + security-review su ogni deliverable | Zero vulnerabilità critiche; `has_pii` gestito |
| **WF-VERIFY** | verify.sh Empire + playwright-dev (test browser reali) | Verify verde; test browser passati |
| **WF-EMPIRE-VERIFY-PIPELINE** | **NUOVO v2:** orchestrazione della skill `empire-verify` (lint+build+playwright+brand gate in un comando) su tutti i deliverable, non solo siti | Pipeline unica verde prima di ogni handoff a L2.5 |

---

### L2.5 — DEPLOY & CI/CD

**Missione:** deploy sicuro e tracciato di ogni deliverable — Vercel per i siti, pipeline
dedicate per SaaS/App — con rollback pronto e smoke test post-deploy.

**Dove il v1 era carente:** 1 agente (`plt-deploy-op`) per l'intero reparto, un solo workflow.
In v2 il reparto ha 6 agenti con CI pipeline dedicata e cost reporting verso OPERATIONS.

#### Team L2.5 (6 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `plt-deploy-lead` | Deploy & CI/CD Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; owner del KPI lead time deploy |
| `plt-deploy-op` | Deploy Operator | worker | haiku | (esistente) Deploy Vercel + logs + rollback |
| `plt-ci-pipeline-eng` | CI Pipeline Engineer | worker | sonnet | **NUOVO v2:** costruisce/mantiene pipeline CI per repo non-Vercel (SaaS/App) |
| `plt-rollback-op` | Rollback Operator | worker | haiku | **NUOVO v2:** procedura di rollback testata, runbook per ogni deploy |
| `plt-smoke-tester` | Smoke Tester | worker | haiku | **NUOVO v2:** smoke test post-deploy (owner esplicito, prima era implicito in WF-DEPLOY) |
| `plt-deploy-cost-reporter` | Deploy Cost Reporter | worker | haiku | **NUOVO v2:** emette evento costi a fine build/deploy (skill `site-cost-report`) verso 06d-OPERATIONS |

#### Workflow L3 di L2.5 (3 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-DEPLOY** | vercel:deploy + vercel:logs + rollback + post-deploy smoke | G-DEPLOY (verify + smoke post-deploy verdi) |
| **WF-CI-PIPELINE** | **NUOVO v2:** pipeline CI dedicata per SaaS/App (build → test → deploy) | Pipeline verde end-to-end senza intervento manuale |
| **WF-ROLLBACK** | **NUOVO v2:** rollback testato periodicamente (non solo in emergenza) | Rollback eseguito con successo in ambiente di staging, 1/mese |

---

## 3. Roster agenti completo (tutti i reparti)

### PLT-Director (L1)

| ID | Agente | Tipo | Tier | Ruolo |
|---|---|---|---|---|
| `plt-director` | PLT-Director | coordinator | opus | Coordinatore ecosistema L1 (era "opus-director" di Crea Siti): riceve handoff dal BUS, valida contratto, smista ai reparti, arbitra scope, approva architetture, escalation a CTO/C-Suite |

### Conteggio roster v2

| Reparto | Agenti esistenti (dal v1) | Agenti nuovi v2 | Totale |
|---|---|---|---|
| L1 PLT-Director | 1 (`plt-director`) | 0 | 1 |
| L2.1 Web-Engineering (mega) | 7 (era `plt-cc-master` + 6 worker) | 9 | 16 |
| L2.2 Product-Engineering | 0 | 8 | 8 |
| L2.3 Tooling & Automation | 1 (`plt-custodian`, evoluto in 2 ruoli) | 6 | 7 |
| L2.4 Security & Quality | 1 (`plt-sec-sentinel`) | 6 | 7 |
| L2.5 Deploy & CI/CD | 1 (`plt-deploy-op`) | 5 | 6 |
| **TOTALE** | **11** | **34** | **45** |

*(Il v1 aveva 11 agenti in tutto l'ecosistema. In v2 se ne aggiungono 34 per portare ogni
reparto allo standard 6-10 con lead + QA + specialisti, e WEB-ENGINEERING a gerarchia da
mega-reparto. Nota: `plt-cc-master` → `plt-web-lead`; `plt-custodian` → `plt-outreach-code-custodian`
+ `plt-repo-registrar`, come riportato nelle tabelle team.)*

---

## 4. Workflow chiave CF-grade

### (a) Routing cross-ecosistema — flusso di ingresso principale

```
[Ecosistema committente]
   │  handoff contract {committente, formato, brand_kit, scope, deadline, budget_max}
   ▼
PLT-Director ──► valida contratto (formato riconosciuto? budget dichiarato se serve spesa?)
   │               ├─ stack nuovo per DE → consulta 06c-INTELLIGENCE PRIMA di procedere
   │               └─ budget mancante e serve spesa → blocco, richiesta ok Max
   ▼  ROUTING PER FORMATO
   ├─ sito-completo / landing / sales-page-tech  → L2.1 WEB-ENGINEERING (WF-SITE-FULL / WF-LANDING-RAPIDA)
   ├─ mvp / automazione                          → L2.2 PRODUCT-ENGINEERING (WF-SAAS-BUILD / WF-APP-MAINTAIN)
   ├─ implementazione (script interni)           → L2.3 TOOLING & AUTOMATION (WF-TOOL-BUILD)
   ├─ handover-codice                            → L2.3 TOOLING & AUTOMATION (WF-CODE-CUSTODY)
   └─ skill-nuova / agente-nuovo (da 06b-FORGE)  → reparto destinatario secondo competenza
   ▼
L2.4 SECURITY & QUALITY ──► WF-SEC-SCAN + WF-VERIFY (obbligatorio per ogni deliverable)
   ▼
L2.5 DEPLOY & CI/CD ──► WF-DEPLOY (solo se G-SEC + G-QA + G-BRAND verdi)
   ▼
Risposta handoff: {deliverable, url_staging_prod, verify_report, security_report, costo_evento, workflow_eseguito}
   └─► hooks post-task: evento costo a 06d-OPERATIONS + post-mortem tecnico a 06c-INTELLIGENCE (wiki/log.md)
```

### (b) WF-SITE-FULL — pipeline dettagliata del mega-reparto

```
plt-brief-analyst ── T-site-brief: raccolta requisiti cliente
   ▼
plt-site-architect + plt-stack-selector ── architettura + scelta stack (escalation 06c-INTELLIGENCE se nuovo)
   ▼
plt-site-designer ── T-site-design: palette, layout, componenti chiave
   ▼
plt-site-builder + plt-component-builder ── build Next.js 15/16 + Tailwind v4 (component library riusata)
   ▼
plt-site-copy-merger ── integra copy APSOC validato da 04-MARKETING (PLATFORM non scrive copy)
   ▼
plt-motion-eng / plt-3d-eng ── animazioni e interattività (se richiesto dal brief)
   ▼
plt-qa-runner + plt-seo-tech + plt-perf-auditor ── QA browser + SEO tecnico + Lighthouse ≥90
   ▼
plt-web-qa-lead ──► score sotto soglia → iterazione mirata (max 3, poi escalation umana)
   ▼
L2.4 SECURITY & QUALITY ──► WF-SEC-SCAN + WF-VERIFY
   ▼
L2.5 DEPLOY & CI/CD ──► WF-DEPLOY (dry-run poi deploy reale)
   └─► plt-deploy-cost-reporter emette evento costo a 06d-OPERATIONS
```

### (c) Deploy con cost attribution

```
Deliverable pronto (G-SEC + G-QA + G-BRAND verdi)
   ▼
plt-deploy-lead ── verifica pipeline CI/CD pronta
   ▼
plt-deploy-op ── vercel:deploy (o plt-ci-pipeline-eng per SaaS/App)
   ▼
plt-smoke-tester ── smoke test post-deploy
   ▼
plt-rollback-op ── rollback pronto se smoke fallisce (mai deploy senza rollback testato)
   ▼
plt-deploy-cost-reporter ── evento {commessa, costo, durata, esito} → 06d-OPERATIONS
   └─► successo → post-mortem tecnico a 06c-INTELLIGENCE (ADR se decisione architetturale)
```

---

## 5. Asset esistenti wrappati (ADR-003: mappatura + wrapper, MAI riscrittura)

| Path | Reparto L2 | Azione v2 |
|---|---|---|
| `Digital Empire/Crea siti/` (agents/orchestrators, site-build, site-copy, site-qa; system/SOP-SITE, SOP-OPUS, ARCHITETTURA-SISTEMA-SITE) | WEB-ENGINEERING | **INGLOBA come motore mega-reparto.** Wrapper handoff sopra la gerarchia esistente; registrazione agenti in Identity-HR; formalizzare nomi L3/L4, non riscrivere |
| `Crea siti/skills/site-*` (20+ skill) + `theme-factory`, `frontend-design`, `canvas-design` | WEB-ENGINEERING | **USA** — motore reale, distribuito tra le 4 aree del mega-reparto |
| Skill `empire-premium-style` / `empire-style` (`SKILL & Agenti/empire-style`) | WEB-ENGINEERING / WF-EMPIRE-RESTYLE | **USA** — motore del restyle premium, owner `plt-restyle-specialist` |
| `Digital Empire/agency-empire-landing/` | WEB-ENGINEERING | **USA** (vetrina viva) + **EVOLVI** (CI verify pre-deploy via L2.4/L2.5) |
| `Digital Empire/Crea siti/Siti CCM/` | WEB-ENGINEERING | **USA** come reference design system (ccm-premium) |
| `Digital Empire/SaaS/` | PRODUCT-ENGINEERING | **EVOLVI** — censire (`plt-product-registrar`), dare owner e pipeline |
| `Digital Empire/App/` | PRODUCT-ENGINEERING | **EVOLVI** — idem, owner `plt-app-maintainer` |
| `Digital Empire/Outreach/*.py`, `*.bat` (codice, non i run) | TOOLING & AUTOMATION | **WRAPPA** — registry + verify (`plt-outreach-code-custodian`), NON toccare i flussi attivi (rischio #4 Piano Maestro) |
| Skill `playwright-dev`, `verify`, `build-implementation`, `review-and-heal` | SECURITY & QUALITY | **USA** — distribuite tra `plt-verify-runner`, `plt-playwright-tester`, `plt-tooling-qa` |
| Skill `vercel:deploy/logs/setup` | DEPLOY & CI/CD | **USA** — motore di `plt-deploy-op` |

---

## 6. Skill NUOVE da forgiare (via 06b-FORGE, standard §8 piano V2: PRD → architettura → build)

| Skill nuova | Reparto | Cosa fa | Priorità |
|---|---|---|---|
| `empire-verify` | SECURITY & QUALITY | verify.sh versione DE: lint+build+playwright+brand gate in un comando (WF-EMPIRE-VERIFY-PIPELINE) | **ALTA** |
| `code-custody` | TOOLING & AUTOMATION | Checklist handover codice cliente (repo transfer, env, docs, 90gg supporto) | **ALTA** |
| `site-cost-report` | DEPLOY & CI/CD | Emette evento costi per 06d-OPERATIONS a fine build | MEDIA |
| `stack-radar` | WEB-ENGINEERING | Watch trimestrale su stack (Next, Tailwind, Vercel) con proposta upgrade (`plt-stack-selector`) | BASSA |
| `product-registry` | PRODUCT-ENGINEERING | Registro strutturato SaaS/App con owner, pipeline, stato — motore di `plt-product-registrar` | MEDIA |
| `ci-pipeline-template` | DEPLOY & CI/CD | Template CI riusabile per repo non-Vercel (SaaS/App) — motore di `plt-ci-pipeline-eng` | MEDIA |

**Regola anti-contraddizione:** prima di creare ogni skill nuova → `skill-contradiction-analyzer`
(motore 06b-FORGE) contro le skill site-* esistenti. Rischio concreto: `empire-verify` deve
COMPORRE le skill esistenti (verify, playwright-dev, security-review), non ridefinirle.

---

## 7. KPI + Quality Gates

### 7.1 Quality gates (bloccanti, in serie)

| Gate | Chi | Soglia | Esito fail |
|---|---|---|---|
| **G-SEC** | `plt-sec-sentinel` + `plt-security-reviewer` | aidefence + security-review verde; `has_pii` gestito | Blocco fino a fix; escalation se violazione Art.7 Mandato |
| **G-QA** | `plt-qa-runner` + `plt-playwright-tester` + `plt-web-qa-lead` | site-qa + playwright verde | Iterazione mirata (max 3 cicli) → escalation umana |
| **G-BRAND** | `plt-web-qa-lead` | Stile conforme a empire-premium-style / brand kit cliente | Blocco, richiesta rework a `plt-site-designer` |
| **G-DEPLOY** | `plt-deploy-lead` | verify + smoke post-deploy verdi | Rollback automatico via `plt-rollback-op` |

Nessun deploy salta un gate (v1, confermato).

### 7.2 KPI

| KPI | Reparto | Target |
|---|---|---|
| Lead time sito cliente (brief→deploy) | L2.1 | ≤ 10 giorni lavorativi (v1) |
| First-pass QA (deliverable passa site-qa al primo giro) | L2.1 | ≥ 80% (v1) |
| Lighthouse performance siti consegnati | L2.1 | ≥ 90 (v1) |
| Incidenti security post-deploy | L2.4 | 0 (v1) |
| Repo censiti nel registry / repo totali | L2.3 | 100% (v1) |
| Copertura registry prodotti SaaS/App | L2.2 | 100% — nessuna baseline storica: si misura al primo censimento (v2, niente numeri inventati) |
| Tempo di build MVP (PRD → primo deploy staging) | L2.2 | da misurare al primo ciclo reale (v2) |
| Rollback testati / mese | L2.5 | 1/mese verde (v2, coerente con OPERATIONS §7) |
| Copertura evento costo / deploy totali | L2.5 | 100% (v2, prerequisito per 06d-OPERATIONS) |
| Gate bypass rate | trasversale | 0 (Art.4.1 Mandato) |

---

## 8. Integrazione Ruflo (TopologyOrchestration)

**Topologia:** `hierarchical` (default holding) — PLT-Director coordinatore di ecosistema;
`plt-web-lead` coordinatore del mega-reparto L2.1 con 4 capi area impliciti nelle aree; lead
di reparto (`plt-product-lead`, `plt-tooling-lead`, `plt-sec-lead`, `plt-deploy-lead`)
coordinatori L2. Fan-out `mesh` SOLO dentro batch paralleli (es. build componenti multipli,
test su più browser).

| Funzione | Tool Ruflo | Uso in PLATFORM |
|---|---|---|
| Spawn pipeline brief→deploy | `agent_spawn` sequenziale | Ogni agente riceve output del precedente (handoff interno WF-SITE-FULL) |
| Fan-out componenti/varianti | `swarm_init` + `task_orchestrate` | Build parallelo di componenti multipli, test multi-browser |
| Pattern pre-build | `memory_search` | `plt-site-architect` interroga `platform/sites/patterns` prima di progettare |
| Salvataggio esiti | `memory_store` + hooks post-task | Report verify/security/deploy dopo ogni run |
| Sicurezza input | `aidefence_scan` / `aidefence_has_pii` | Brief cliente e config prima dell'elaborazione |
| State per workflow | state.json per esecuzione | Ogni workflow CF-grade produce record ripartibile a freddo (test amnesia §6 piano V2) |

---

## 9. Namespace memoria — `platform/...` (AgentDB/HNSW)

| Namespace | Contenuto | Owner |
|---|---|---|
| `platform/registry/repos` | Registry di tutti i repo/script con owner e stato (DONE WHEN #4) | `plt-repo-registrar` scrive |
| `platform/sites/builds/{project}` | Stato build sito (state.json per WF-SITE-FULL) | `plt-web-lead` scrive |
| `platform/sites/patterns` | Pattern di design/build riusabili, libreria componenti pubblicata | `plt-component-builder` scrive |
| `platform/security/scans` | Storico scan aidefence/security-review | `plt-sec-sentinel` scrive |
| `platform/deploy/log` | Storico deploy, rollback, smoke test | `plt-deploy-op` scrive |
| `platform/cost/events` | Eventi costo emessi verso 06d-OPERATIONS (site-cost-report) | `plt-deploy-cost-reporter` scrive |
| `platform/product/registry` | SaaS/App con owner, pipeline, stato | `plt-product-registrar` scrive |
| `platform/handoffs/log` | Registro richieste/risposte cross-ecosistema | `plt-director` scrive |

**Wiki-first (pattern #12 Piano Maestro):** decisioni d'architettura (ADR tecnici) e
post-mortem vanno ANCHE in pagina wiki `tools/` + entry `wiki/log.md` (v1 §2: "PLATFORM →
INTELLIGENCE"). In conflitto wiki ↔ AgentDB: vince la wiki.

---

## 10. Build plan v2 (dentro V2-2, poi V2-6 per la build strutturale completa)

### Sequenza milestone (ordine non negoziabile: censimento prima di formalizzare, formalizzazione prima di scalare)

| Fase | Cosa si costruisce | Gate di uscita |
|---|---|---|
| **P1 — Censimento** | Registry di tutti i repo/script con owner e stato (`plt-repo-registrar`) | Inventario 100% |
| **P2 — Formalizzazione mega-reparto** | Crea Siti formalizzato come L2.1 WEB-ENGINEERING (gerarchia 4 aree, ruoli rinominati, L3/L4 documentati) | Un sito demo prodotto col flusso formale |
| **P3 — empire-verify + pipeline gates** | Skill `empire-verify` forgiata; pipeline G-SEC/G-QA/G-BRAND/G-DEPLOY su `agency-empire-landing` | verify verde su landing live |
| **P4 — Code custody** | Procedura handover cliente testata su una commessa reale (`plt-code-custody-lead`) | Handover completato |
| **P5 — Reparti minori a scala** | PRODUCT-ENGINEERING, TOOLING, SECURITY, DEPLOY portati a team completi (agenti reali via Ruflo) | Ogni reparto ha eseguito almeno un workflow CF-grade end-to-end |

---

## 11. Pre-mortem — rischi v2

| Rischio | Probabilità | Mitigazione |
|---|---|---|
| **Riscrittura accidentale di Crea Siti** durante la formalizzazione a mega-reparto | Alta | ADR-003 ferma: formalizzazione = wrapper + gerarchia sopra il sistema esistente, mai modifica ai file del motore; `Crea siti/system/SOP-SITE` resta fonte di verità finché il wrapper non è validato (P2) |
| **WEB-ENGINEERING diventa un collo di bottiglia** (tutti gli ecosistemi in coda su un solo mega-reparto) | Media | Fan-out swarm su build paralleli; priorità nel contratto via `deadline`; escalation a C-Suite se due committenti confliggono |
| **Reparti minori (PRODUCT/TOOLING/SECURITY/DEPLOY) restano sulla carta** (schede v2 senza agenti reali) | Alta senza presidio | Standard §0 piano V2 obbligatorio; build plan P5 dedicato; `plt-director` traccia quali reparti hanno eseguito almeno un workflow reale |
| **Deploy senza evento costo** (rompe l'attribution di 06d-OPERATIONS) | Media | G-DEPLOY include verifica evento costo emesso; `plt-deploy-cost-reporter` come owner esplicito, non implicito |
| **Stack nuovo adottato senza consultare INTELLIGENCE** | Media | Regola esplicita nel contratto §1.2; `plt-stack-selector` come gate obbligatorio prima di ogni scelta non standard |
| **Outreach code rotto durante il wrapping** (rischio #4 Piano Maestro) | Alta se non presidiato | `plt-outreach-code-custodian` opera SOLO in lettura/registry sui flussi attivi; nessuna modifica senza approvazione esplicita e testing separato |
| **Schede agenti v2 non millimetriche** ("è un file markdown? INACCETTABILE" — principio Maximilian) | Alta senza presidio | Standard §0 piano V2 obbligatorio per ogni agente nuovo; `plt-web-qa-lead` e `plt-quality-auditor` tracciano conformità |
| **Duplicazione tra plt-qa-runner (L2.1) e plt-verify-runner/plt-playwright-tester (L2.4)** | Media | Confine esplicito: L2.1 QA è specifica del sito nel flusso WF-SITE-FULL; L2.4 è trasversale a TUTTI i deliverable (incl. SaaS/App, script) |

---

## 12. Connessioni

- [[00-PIANO-MAESTRO]] — gerarchia LX→L5, backbone, pattern non negoziabili, roadmap
- [[11-PIANO-V2-DIRETTIVA-SCALA]] §0-2 — direttiva suprema che governa questo dossier (ADR-007)
- [[06-ECOSISTEMI-CORE]] — il v1 da cui si parte (§PLATFORM, righe 31-145); resta riferimento intatto
- [[06b-ECOSISTEMA-FORGE-V2]] — fornitore di agenti/skill/team nuovi per PLATFORM; secondo core nella catena di dipendenza
- [[06c-ECOSISTEMA-INTELLIGENCE-V2]] — fornitore di ricerca tecnica pre-scelta architetturale
- [[06d-ECOSISTEMA-OPERATIONS-V2]] — destinatario degli eventi costo; runtime swarm per build/deploy paralleli
- [[04-ECOSISTEMA-MARKETING-V2]] — fornitore di copy APSOC (PLATFORM monta, non scrive); committente di L2.6 Conversion Architecture
- [[01-ECOSISTEMA-AGENCY-V2]] — primo committente reale (siti clienti, code custody)
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] — fornitore asset visual/video da integrare
- [[07-BACKBONE-RUFLO-SKILLS]] — registro skill e integrazione Ruflo; tutte le skill §5-§6 registrate qui
- [[12-DOSSIER-MAXIMILIAN]] — revisione 5-bis da V2-3: "Max approverebbe questa gerarchia?"
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] — enforcement; custodia del codice come invariante cardinale
- ADR-003 (wrap, non riscrittura) · ADR-007 (V2, CF-grade) · ADR-005 (minuzie → BACKLOG) · ADR-002 (memory-first)
