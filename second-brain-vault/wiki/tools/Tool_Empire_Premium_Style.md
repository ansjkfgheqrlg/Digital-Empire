---
Type: TOOL
Status: Active
Tags: #design-system #skill #nextjs #landing-page #ccm
Created: 2026-08-25
Last updated: 2026-08-25
---

# Tool: empire-premium-style — Trasformatore di Stile Empire

## Overview
Skill Claude Code che prende un sito esistente in **qualsiasi formato** (HTML statico, Next.js,
React, Vue, export WordPress) e lo **ricostruisce** nel design system ultra-premium di Digital
Empire — lo stesso di `ccm-premium`. Non adatta e non "si ispira": rifà ogni sezione con i
pattern Empire, mantenendo però la **struttura delle sezioni e il copy originali**.
Sorgente nel monorepo: `Skill empire-premium-style/` (10 file: `SKILL.md`, slash command,
8 file `references/`).

## Dettagli

**Invocazione**: `/empire-style <path-sito-sorgente>` oppure "trasforma questo sito in stile
empire: `<path>`". Se il target ha già un `package.json` Next.js, chiede conferma prima di
sovrascrivere (default: nuova cartella `<nome>-empire/`).

**Design system (token congelati — `references/design-tokens.css`)**
- Palette ink / paper / grey + arancione `#fb4604` + gradient silver-mixed
- Tipografia **Onest** variabile
- Grana fine fissa a doppio layer
- Componenti: `card-dark` / `card-paper` / `card-silver-orange`, bubble orange/silver/ink,
  silver-chip flottanti, pre-headline tag, corner brackets, `btn-orange` con glow, marquee,
  `step-num`, `hl-block` highlight

**Stack obbligatorio (non negoziabile)**: Next.js 16 App Router + Tailwind v4 + Lenis smooth
scroll + Framer Motion (reveal) + GSAP ScrollTrigger + lucide-react + font Onest.
Mai HTML/CSS statico, mai Pages Router, mai componenti shadcn inline (solo le classi CSS raw
di `design-tokens.css`).

**Struttura `references/`**
| File | Ruolo |
|---|---|
| `design-tokens.css` | STEP 2 del playbook: si copia **integrale** come `globals.css` |
| `build-playbook.md` | Procedura di build passo-passo |
| `section-patterns.md` | Pattern visivi per tipo di sezione |
| `components.md` + `components/` | Catalogo componenti |
| `layout-template.md` / `reference-layout.tsx` | Layout di riferimento |
| `reference-page-full.tsx` | Pagina completa di riferimento (48K) |
| `package.json.md` | Dipendenze attese |

**Nota di build ricorrente**: se `design-tokens.css` contiene `@import "shadcn/tailwind.css"`,
va rimossa — shadcn non è nelle dipendenze.

## Dove è già stata applicata
Le build CCM committate il 2026-08-25 nascono da questo design system:
`Crea siti/Siti CCM/ccm-sale-page-empire/`, `ccm-elite-ultimate/`, `ccm-full-empire/` (parziale)
e `Landing Page/ccm-empire/` (home + masterclass + thank-you, deploy Netlify).

## Connessioni
- [[tools/Tool_Copy_Workflow_Orchestration]] — il copy che riempie le sezioni resta APSOC:
  la skill preserva il copy originale, non lo riscrive
- [[sources/Source_Claude_Design_Beggiato]] — metodo "Design System → Template → Skills",
  stesso principio anti-"vibe design": token fissi, non improvvisazione a ogni pagina
- [[concepts/Concept_Conversion_Rate_Moltiplicatore]] — la resa visiva di una sale page agisce
  sul CR, non sul traffico: è lì che questa skill lavora
- [[01 - Projects/Agency_Empire_Landing]] — landing di agenzia, candidata naturale alla stessa
  trasformazione
