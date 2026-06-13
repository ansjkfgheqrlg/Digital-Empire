# WF-SITE-FULL — Build Sito Completo

> **Pipeline ufficiale Crea Siti DE:** brief → plan → design → copy-merge → build → qa → deploy.
> Lead time target: ≤ 10 giorni lavorativi. Nessun gate saltabile.

## Trigger
- AGENCY chiude contratto con cliente sito → handoff `{brief cliente, brand_kit, icp, scope, deadline}` a PLATFORM
- DE decide di costruire un nuovo sito proprio
- INFO-BUSINESS richiede nuova sales page o piattaforma corsi

## Input
```json
{
  "brief_cliente": "obiettivo sito, pagine richieste, funzionalità, tono",
  "brand_kit": "logo, colori, font, asset visivi",
  "icp": "target audience, pain points (da INTELLIGENCE se disponibile)",
  "scope": "numero pagine, integrazioni, deadline",
  "copy_apsoc": "da MARKETING — opzionale in ingresso, obbligatorio a T-copy-merge",
  "budget_token": "token budget massimo per la build"
}
```

## Pipeline (Passi)

### Fase 1 — BRIEF & ARCHITECTURE (Giorno 1-2)
```
plt-director approva brief
  → plt-site-architect: SITE-PLAN.md + SITE-ARCHITECTURE.md
  → plt-director: approva architettura (ADR micro se stack non standard)
  → shared_state: {fase: "architecture", gate: {spec: "verde"}}
```

### Fase 2 — DESIGN & SETUP (Giorno 2-3)
```
plt-cc-master lancia in PARALLELO:
  [A] plt-site-builder: setup repo Next.js 15/16 + Tailwind v4 + token design
  [B] MARKETING: produzione copy APSOC (fuori PLATFORM — handoff bidirezionale)
  → shared_state: {fase: "design-setup"}
```

### Fase 3 — BUILD (Giorno 3-6)
```
plt-cc-master lancia in PARALLELO:
  [A] plt-site-builder: costruzione componenti e pagine (attende setup completo)
  [B] plt-seo-tech: struttura heading + meta tags + JSON-LD (su draft builder)
  → npm run build verde → shared_state: {fase: "build", build_status: "verde"}
```

### Fase 4 — COPY-MERGE & MOTION (Giorno 6-7)
```
plt-cc-master lancia in SEQUENZA:
  1. plt-site-copy-merger: integra copy APSOC finale nei componenti
  2. plt-motion-eng: aggiunge Lenis + Framer Motion + GSAP (parallelo possibile)
  3. plt-seo-tech: completa SEO tecnico (sitemap, canonical, OG definitivi)
  → shared_state: {fase: "copy-motion"}
```

### Fase 5 — GATE G-SEC (Giorno 7-8)
```
plt-sec-sentinel: aidefence scan + security-review + PII check
  → se CRITICAL/HIGH trovati → blocco → fix plt-site-builder → re-scan
  → se verde → shared_state: {gate: {g_sec: "verde"}}
```

### Fase 6 — GATE G-QA (Giorno 8-9)
```
plt-qa-runner: playwright-dev (tutte le pagine) + verify + Lighthouse
  → se failures → lista bug a plt-site-builder → fix → re-test
  → se verde (Lighthouse ≥ 90, 0 broken links, 0 console errors)
  → plt-director: G-BRAND check (stile conforme empire-premium-style)
  → shared_state: {gate: {g_qa: "verde", g_brand: "verde"}}
```

### Fase 7 — GATE G-DEPLOY (Giorno 9-10)
```
plt-deploy-op: vercel:deploy + smoke test + log watch 10 min
  → se rollback necessario → fix → retry
  → se verde → evento costo OPERATIONS
  → plt-custodian: censisce repo nel registry
  → shared_state: {gate: {g_deploy: "verde"}, url_produzione: "https://..."}
```

### Fase 8 — CHIUSURA
```
plt-cc-master: report finale {durata, costo, url, gate_stati, artefatti}
plt-director: approva consegna → notifica AGENCY
plt-custodian: (se cliente) prepara pacchetto handover
INTELLIGENCE: archivia post-mortem tecnico in wiki tools/
OPERATIONS: riceve evento costo → ledger aggiornato
```

## Gate
| Gate | Owner | Criterio |
|---|---|---|
| G-SPEC | plt-director | Architettura approvata prima del build |
| G-SEC | plt-sec-sentinel | 0 CRITICAL/HIGH, 0 secret, 0 PII |
| G-QA | plt-qa-runner | Lighthouse ≥ 90, 0 broken links, 0 console errors |
| G-BRAND | plt-director | Stile conforme empire-premium-style / brand kit |
| G-DEPLOY | plt-deploy-op | Smoke test verde, 0 5xx in 10 min |

## Output
- URL sito in produzione su Vercel
- Repo censite nel registry PLATFORM
- Report qualità (gate stati, Lighthouse scores, screenshot QA)
- Evento costo per OPERATIONS
- Pacchetto handover (se cliente Agency)

## Owner Agente
`plt-cc-master` — coordinator di tutta la pipeline

## Skill Usate
`site-brief` · `site-architecture` · `site-plan` · `site-premium-stack` · `site-build` · `site-components` · `site-design` · `site-copy` · `site-animate` · `site-3d` (opzionale) · `site-seo` · `site-qa` · `site-report` · `empire-premium-style` · `playwright-dev` · `verify` · `security-review` · `vercel:deploy` · `vercel:logs`
