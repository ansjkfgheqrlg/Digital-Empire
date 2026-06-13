# WF-EMPIRE-RESTYLE — Sito Esistente → Stile Premium DE

> **Trasforma un sito esistente in un sito premium Digital Empire.** Usa `empire-premium-style` come motore del restyle. Più veloce di WF-SITE-FULL perché la struttura esiste già — il focus è sul design system e sul motion layer.

## Trigger
- DE vuole portare un proprio sito al visual standard premium
- Cliente Agency ha sito esistente funzionante ma non allineato al brand DE
- Post-audit visivo che rivela gap con empire-premium-style

## Input
```json
{
  "url_sito_sorgente": "sito esistente da restyle",
  "repo_sorgente": "path repo o accesso codebase",
  "brand_kit": "token cliente o DE (colori ink/orange/silver se DE)",
  "obiettivo_restyle": "visual only / motion + visual / full rebuild struttura",
  "note_brand": "vincoli specifici (font approvati, elementi da preservare)"
}
```

## Pipeline (Passi)

### Fase 1 — AUDIT SORGENTE (Giorno 1)
```
plt-site-architect: T-audit-sorgente
  → analizza stack attuale (compatibilità Next.js 15/16 + Tailwind v4)
  → identifica componenti da riscrivere vs da restyling CSS only
  → produce: RESTYLE-PLAN.md (delta tra stato attuale e target premium)
  → stima: visual-only (< 3gg) / motion + visual (< 5gg) / full rebuild (→ WF-SITE-FULL)
plt-director: approva scope e piano
```

### Fase 2 — REBUILD / RESTYLE (Giorno 1-3)
```
plt-site-builder: T-rebuild-next15
  → migra (se necessario) a Next.js 15/16 con App Router
  → applica Tailwind v4 con token design DE:
      - Palette: ink (#1a1a2e), orange (#ff6b35), silver (#c0c0c0)
      - Typography: font DE approvati
      - Spacing e border-radius token
      - Glass card effect, grain texture background
  → empire-premium-style come spec visiva obbligatoria

plt-site-builder: T-token-design
  → crea o aggiorna design token file (tailwind.config.ts)
  → garantisce consistenza token in tutto il codebase
```

### Fase 3 — MOTION LAYER (Giorno 3-4)
```
plt-motion-eng: T-motion
  → configura Lenis smooth scroll provider root
  → aggiunge scroll reveal (Framer Motion FadeInView, SlideUp)
  → hero section: animazione entry GSAP o Framer
  → (opzionale) Three.js particle background se brief lo richiede
  → verifica: Lighthouse performance ≥ 90 con motion
```

### Fase 4 — GATE G-SEC + G-QA (Giorno 4-5)
```
plt-sec-sentinel: G-SEC scan
  → focus su modifiche introdotte dal restyle (nuove dipendenze, env vars)
  → se verde → plt-qa-runner: G-QA
plt-qa-runner: playwright-dev + verify + Lighthouse
  → confronto before/after Lighthouse (nessuna regressione performance)
  → verifica che il copy esistente sia integro (nessun placeholder introdotto)
plt-director: G-BRAND (stile conforme empire-premium-style)
```

### Fase 5 — DEPLOY (Giorno 5)
```
plt-deploy-op: vercel:deploy + smoke test
plt-custodian: aggiorna registry con versione restyle
INTELLIGENCE: log post-mortem restyle (pattern riusabili in wiki)
OPERATIONS: evento costo
```

## Gate
| Gate | Owner | Criterio |
|---|---|---|
| G-AUDIT | plt-director | RESTYLE-PLAN approvato, scope definito |
| G-SEC | plt-sec-sentinel | 0 CRITICAL/HIGH, 0 nuovi secret |
| G-QA | plt-qa-runner | Lighthouse ≥ 90, nessuna regressione vs sito sorgente |
| G-BRAND | plt-director | Token design DE applicati correttamente, grain + glass presenti |
| G-DEPLOY | plt-deploy-op | Smoke test verde, URL produzione live |

## Output
- Sito restyled live su Vercel con visual premium DE
- Token design aggiornati nel repo
- Report before/after Lighthouse
- Componenti motion riutilizzabili aggiunti alla codebase

## Owner Agente
`plt-cc-master` con delega a `plt-site-builder` per la parte tecnica

## Skill Usate
`empire-premium-style` · `empire-style` · `site-design` · `site-animate` · `site-3d` (opzionale) · `site-build` · `frontend-design` · `playwright-dev` · `verify` · `security-review` · `vercel:deploy`
