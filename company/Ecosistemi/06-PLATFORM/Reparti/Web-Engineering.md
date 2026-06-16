> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. PLATFORM

# L2 WEB-ENGINEERING — Il Reparto "Crea Siti"

> Reparto L2 · Ecosistema: 06-PLATFORM
> Riferimento: `company/Ecosistemi/06-PLATFORM/ECOSISTEMA.md` · `company/Ecosistemi/06-PLATFORM/BACKBONE.md`

---

## Missione

Produrre e mantenere TUTTI i siti di Digital Empire e dei suoi clienti — dalla landing singola al sito premium multisezione — con standard design `empire-premium-style`, stack Next.js 15/16 + Tailwind v4, deploy Vercel. È il cuore operativo di PLATFORM per la delivery AGENCY.

WEB-ENGINEERING **wrappa Crea Siti così com'è** (ADR-003): formalizza nomi L3/L4 e pipeline gate senza riscrivere il sistema esistente.

---

## Workflow L3

| Workflow | Descrizione | Lead time |
|---|---|---|
| **WF-SITE-FULL** | brief → plan → design → copy-merge → build → QA → deploy (flusso completo) | ≤ 10 gg lavorativi |
| **WF-EMPIRE-RESTYLE** | sito esistente → stile premium DE (`empire-premium-style`) | ≤ 5 gg |
| **WF-LANDING-RAPIDA** | landing singola < 48h (`market-landing` + `site-premium-stack`) | < 48h |

---

## Funzioni L4

| ID Funzione | Team | Workflow padre |
|---|---|---|
| T-site-brief | Brief strutturato dal mandato Agency | WF-SITE-FULL |
| T-site-architecture | Stack + architettura informativa (site-architecture, site-stack) | WF-SITE-FULL |
| T-site-design | Design system, palette, componenti (frontend-design, theme-factory) | WF-SITE-FULL |
| T-site-components | Sviluppo componenti Next.js/Tailwind | WF-SITE-FULL |
| T-site-animate | Animazioni Lenis/Framer/GSAP | WF-SITE-FULL |
| T-site-3d | Elementi 3D (Three.js/R3F) | WF-SITE-FULL |
| T-site-seo | SEO tecnico on-build (meta, schema, sitemap) | WF-SITE-FULL |
| T-site-qa | QA browser con playwright-dev + verify | WF-SITE-FULL |
| T-site-report | Report post-build consegnato ad OPERATIONS | WF-SITE-FULL |
| T-audit-sorgente | Audit sito sorgente esistente | WF-EMPIRE-RESTYLE |
| T-rebuild-next15 | Rebuild su stack Next.js 15 | WF-EMPIRE-RESTYLE |
| T-token-design | Aggiornamento token design (palette ink/orange/silver) | WF-EMPIRE-RESTYLE |
| T-motion | Lenis/GSAP su sito restyle | WF-EMPIRE-RESTYLE |

---

## Agenti L5 del reparto

| ID Agente | Ruolo | Tier |
|---|---|---|
| `plt-director` | Direttore PLATFORM — arbitra scope e architetture | Opus |
| `plt-cc-master` | Orchestratore esecutivo build | Sonnet |
| `plt-site-architect` | Architettura + stack | Sonnet |
| `plt-site-builder` | Implementazione Next.js/Tailwind | Sonnet |
| `plt-site-copy-merger` | Integra copy MARKETING nei componenti | Haiku |
| `plt-motion-eng` | Animazioni Lenis/Framer/GSAP + 3D | Sonnet |
| `plt-qa-runner` | QA browser + verify | Haiku |
| `plt-seo-tech` | SEO tecnico on-build | Haiku |

---

## Gate qualità

**G-QA** (site-qa + playwright verde) → **G-BRAND** (stile conforme a empire-premium-style / brand kit cliente) → **G-DEPLOY** (verify + smoke post-deploy). Nessuna consegna salta un gate.

---

## Asset esistenti

| Path | Stato |
|---|---|
| `Crea siti/agents/orchestrators/` | USA — orchestratori reali |
| `Crea siti/skills/site-*` (20+ skill) | USA — motore del reparto |
| `empire-style/` · `SKILL & Agenti/empire-style` | USA — design system premium |
| `agency-empire-landing/` | USA + EVOLVI (CI verify pre-deploy) |
| `Crea siti/Siti CCM/` | USA come reference design system |

---

## KPI

| KPI | Target |
|---|---|
| Lead time sito cliente (brief→deploy) | ≤ 10 giorni lavorativi |
| First-pass QA (deliverable passa site-qa al primo giro) | ≥ 80% |
| Lighthouse performance siti consegnati | ≥ 90 |

## Connessioni

- [[06-PLATFORM/ECOSISTEMA.md]] — panoramica reparto nel contesto holding
- [[06-PLATFORM/BACKBONE.md]] — come PLATFORM si connette al Backbone
- [[06-PLATFORM/Reparti/Security-Quality.md]] — gate G-SEC obbligatorio prima di ogni build
- [[06-PLATFORM/Reparti/Deploy-CICD.md]] — deploy finale (WF-DEPLOY)
- [[PIANO-MAESTRO/06-ECOSISTEMI-CORE.md]] — dossier completo
