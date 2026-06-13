# WEB-ENGINEERING — 06-PLATFORM

> **"Crea Siti"**: reparto responsabile di tutti i siti premium di Digital Empire e dei siti clienti Agency. Formalizzazione L2 dell'esistente sistema Crea Siti.

## Missione
Produrre siti web premium — per Digital Empire stessa e per i clienti Agency — dallo zero al deploy Vercel, con stile conforme a `empire-premium-style` (ink/orange/silver, grain texture, glass card, animazioni Lenis/Framer/GSAP). Custodisce il design system DE e garantisce che ogni sito rispetti i 4 gate di qualità prima della consegna.

**Principio cardine:** PLATFORM non scrive copy — lo integra. Il copy arriva da MARKETING (APSOC validato) e viene montato nei componenti da plt-site-copy-merger.

## Team Agenti
| ID | Agente | Tier | Ruolo |
|---|---|---|---|
| `plt-director` | Direttore PLATFORM | Opus | Approva architetture, arbitra scope |
| `plt-cc-master` | Orchestratore Esecutivo | Sonnet | Coordina i worker, gestisce la pipeline |
| `plt-site-architect` | Architetto | Sonnet | SITE-PLAN + SITE-ARCHITECTURE |
| `plt-site-builder` | Builder | Sonnet | Next.js 15/16 + Tailwind v4 |
| `plt-site-copy-merger` | Copy Merger | Haiku | Integra copy MARKETING nei componenti |
| `plt-motion-eng` | Motion Engineer | Sonnet | Lenis + Framer Motion + GSAP + Three.js |
| `plt-seo-tech` | SEO Tecnico | Haiku | Meta tags, JSON-LD, sitemap on-build |
| `plt-qa-runner` | QA Runner | Haiku | playwright-dev + verify (gate G-QA) |
| `plt-sec-sentinel` | Security Sentinel | Sonnet | aidefence + security-review (gate G-SEC) |
| `plt-deploy-op` | Deploy Operator | Haiku | vercel:deploy + logs + rollback |

## Workflow L3
| ID | Workflow | Descrizione |
|---|---|---|
| WF-SITE-FULL | Build Completo | brief → plan → design → copy-merge → build → qa → deploy |
| WF-EMPIRE-RESTYLE | Restyle Premium | sito esistente → stile premium DE (empire-premium-style) |
| WF-LANDING-RAPIDA | Landing < 48h | landing singola con market-landing + site-premium-stack |

## Funzioni L4
- **T-site-brief** — ricezione e strutturazione del brief cliente
- **T-site-architecture** — architettura informativa + stack decision
- **T-site-design** — design system, token colore, tipografia
- **T-site-components** — costruzione componenti atomici riutilizzabili
- **T-site-animate** — layer motion (Lenis scroll, Framer reveal, GSAP timeline)
- **T-site-3d** — Three.js / WebGL scene quando richiesto
- **T-site-seo** — SEO tecnico on-build (meta, JSON-LD, sitemap)
- **T-site-qa** — QA browser con playwright-dev
- **T-site-report** — report deliverable finale

## Asset Esistenti Usati
| Path | Utilizzo |
|---|---|
| `Digital Empire/Crea siti/` | Base del reparto — orchestrators, skill site-*, SOP-SITE, SOP-OPUS, ARCHITETTURA-SISTEMA-SITE |
| `Crea siti/skills/site-*` (20+ skill) | Skill operative del reparto |
| `theme-factory`, `frontend-design`, `canvas-design` | Skill ausiliarie design |
| `empire-premium-style` / `empire-style` | Motore stile brand DE — obbligatorio su ogni sito DE |
| `agency-empire-landing/` | Vetrina viva + reference per CI verify pre-deploy |
| `Crea siti/Siti CCM/` | Reference design system (ccm-premium) |

## Gate di Qualità
```
G-SEC (plt-sec-sentinel: aidefence + security-review verde)
  → G-QA (plt-qa-runner: site-qa + playwright verde, Lighthouse ≥ 90)
    → G-BRAND (stile conforme empire-premium-style / brand kit cliente)
      → G-DEPLOY (plt-deploy-op: verify + smoke post-deploy verde)
```
**Nessun deploy salta un gate.** Ogni gate fallito blocca la pipeline e richiede fix prima di procedere.

## KPI
| KPI | Target |
|---|---|
| Lead time sito cliente (brief→deploy) | ≤ 10 giorni lavorativi |
| First-pass QA | ≥ 80% |
| Lighthouse performance siti consegnati | ≥ 90 |
| Incidenti security post-deploy | 0 |

## Connessioni
- [[06-ECOSISTEMI-CORE]] — dossier padre
- [[BACKBONE]] — registro agenti
- [[WF-SITE-FULL]] — workflow principale
- [[WF-EMPIRE-RESTYLE]] — workflow restyle
- [[SECURITY-QUALITY]] — reparto gate G-SEC e G-QA
- [[DEPLOY-CICD]] — reparto gate G-DEPLOY
