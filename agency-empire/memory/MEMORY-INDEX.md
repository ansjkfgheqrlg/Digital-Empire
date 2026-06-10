# MEMORY INDEX — Agency Empire Landing

> Aggiornato: 2026-05-30 | Regola: leggi questo file PRIMA di ogni task

## Progetto Attivo
**agency-empire-landing** — Landing page Digital Empire (AI Automation Agency)
- Path: `C:\Users\Utente\Desktop\qui tutto\Digital Empire\agency-empire-landing\`
- Stack: Next.js 16.2.3 · TypeScript · Tailwind CSS v4 · Framer Motion · Lucide
- Dev: `npm run dev --prefix "...agency-empire-landing"` → localhost:3000
- Sections dir: `src/components/sections/`

## Sezioni Landing Page
| File | Sezione | Copy Status | Visual Status |
|------|---------|-------------|---------------|
| hero.tsx | Hero + headline 3 righe | ✅ Audit 2026-05-30 | ✅ Stabile |
| science-stats.tsx | 3 stat (7gg / 300+ / €0) | ✅ Audit 2026-05-30 | ✅ Stabile |
| audience.tsx | YES/NO cards ICP | ✅ Audit 2026-05-30 | ✅ Silver border |
| hierarchy.tsx | 3 livelli operatività | ✅ Audit 2026-05-30 | ✅ Pill status labels |
| no-fluff.tsx | Asset vs SaaS | ✅ Audit 2026-05-30 | ✅ Stabile |
| mastery-map.tsx | 3 servizi in dettaglio | ✅ Audit 2026-05-30 | ✅ Stabile |
| roadmap.tsx | 4 step processo | ✅ Audit 2026-05-30 | ✅ Colored step cards |
| builder-not-trainer.tsx | Storia + 3 stat cards | ✅ Stabile | ✅ Unified bg fixed |
| pricing-roi.tsx | Prezzi + Engine Room | ✅ Audit 2026-05-30 | ✅ 3 cards + combo |
| about-story.tsx | Storia team (5 sub-section) | ✅ Audit 2026-05-30 | ✅ Stabile |

## Checkpoints
- [2026-05-30_copy-audit.md](checkpoints/2026-05-30_copy-audit.md) — 20 modifiche copy su 9 file
- [2026-05-30_ui-fixes.md](checkpoints/2026-05-30_ui-fixes.md) — Visual fixes hero + cards + pricing

## Decisions
- [typography-system.md](decisions/typography-system.md) — Clamp sizing, 3-line hero variable sizes
- [color-palette.md](decisions/color-palette.md) — ink/paper/grey/orange + silver border constant
- [pricing-structure.md](decisions/pricing-structure.md) — 3 servizi singoli + Engine Room combo

## Sessions
- [session_2026-05-30.md](sessions/session_2026-05-30.md) — UI fixes batch + copy audit

## Regole di utilizzo
1. **PRIMA di ogni task** → leggi le sezioni rilevanti di questo file
2. **DOPO ogni task completato** → aggiorna la tabella + crea/aggiorna checkpoint
3. **Nuove decisioni architetturali** → aggiungi in `decisions/`
4. **Fine sessione** → aggiorna `sessions/` con recap

## Costanti tecniche da ricordare
- Silver border: `2px solid rgba(210,218,232,0.65)`
- Font serif: `var(--font-serif), Georgia, serif`
- Orange: `#fb4604` | Ink: `#1c1c1c` | Paper: `#fafafa` | Grey: `#e8e8e6`
- Hero clamp: line1 `clamp(22px,3.2vw,42px)` · line2 `clamp(82px,13.5vw,148px)` · line3 `clamp(44px,7vw,88px)`
- Supporto post-setup: **90 giorni** (non 30 — inconsistenza fixata 2026-05-30)
