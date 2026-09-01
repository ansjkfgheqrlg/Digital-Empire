---
name: site-premium-stack
description: Stack obbligatorio per ogni landing page / sito ultra-premium. Next.js 15 + Tailwind + shadcn/ui + Radix + Headless UI + Chakra + Framer Motion + GSAP + Lenis + Three.js + Theatre.js + Anime.js + Playwright. Usa questo SEMPRE quando l'utente chiede un sito, landing page, o restyling ultra-premium.
---

# SITE PREMIUM STACK — Obbligatorio per ogni sito

## Regola ferrea
MAI più scrivere landing in HTML/CSS statico da zero. Ogni nuovo progetto sito/landing usa questo stack. L'utente e stato esplicito: il vecchio approccio "CSS custom + 6 round di polish" produce risultati scadenti. Le librerie qui sotto sono quelle che usano le agenzie premium e i vincitori Awwwards.

## Stack completo (installazione standard)

### 1. Base progetto
```bash
npx create-next-app@latest NOME --typescript --tailwind --app --eslint --src-dir --turbopack --import-alias "@/*" --use-npm --yes
cd NOME
echo 'legacy-peer-deps=true' > .npmrc
```

### 2. Install mega-pacchetto (un solo comando)
```bash
npm install --legacy-peer-deps \
  @chakra-ui/react @emotion/react @emotion/styled \
  framer-motion gsap @gsap/react \
  three @types/three animejs \
  evergreen-ui lenis \
  clsx tailwind-merge class-variance-authority lucide-react \
  @headlessui/react \
  @radix-ui/react-dropdown-menu @radix-ui/react-dialog @radix-ui/react-accordion \
  @radix-ui/react-tabs @radix-ui/react-tooltip @radix-ui/react-slot \
  @theatre/core @theatre/studio \
  material-components-web
npm install --save-dev --legacy-peer-deps @playwright/test
```

### 3. shadcn/ui init + componenti core
```bash
npx shadcn@latest init --yes --defaults --force
npx shadcn@latest add button card input label accordion dialog dropdown-menu tabs tooltip badge separator sheet form --yes --overwrite
```

## Quando usare cosa

| Bisogno | Libreria |
|---|---|
| Componenti base (Button, Card, Dialog) | **shadcn/ui** (copy-paste, Radix sotto) |
| Primitive accessibili custom | **Radix UI** primitives |
| Componenti non stilizzati + Tailwind | **Headless UI** |
| Design system completo rapido | **Chakra UI** |
| Componenti business pronti | **Evergreen** |
| Micro-interazioni React | **Framer Motion** |
| ScrollTrigger / timeline avanzate | **GSAP + @gsap/react** |
| Smooth scroll premium | **Lenis** (wrapper root) |
| 3D hero / canvas effects | **Three.js** |
| Motion design complesso | **Theatre.js** |
| Animazioni vanilla leggere | **anime.js** |
| Icone | **lucide-react** |
| Testing E2E | **Playwright** |

## Pattern Lenis + GSAP integrazione (obbligatorio nel layout root)
```tsx
'use client'
import { useEffect } from 'react'
import Lenis from 'lenis'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

export function SmoothScrollProvider({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    const lenis = new Lenis({ lerp: 0.1, smoothWheel: true })
    lenis.on('scroll', ScrollTrigger.update)
    gsap.ticker.add((time) => lenis.raf(time * 1000))
    gsap.ticker.lagSmoothing(0)
    return () => lenis.destroy()
  }, [])
  return <>{children}</>
}
```

## Template di riferimento (gia clonati)
- `Leanding Page CCM/templates/astrowind` — template Astro premium

## Reference ispirazione (da studiare, non installare)
- `basementstudio/basement.studio` — agency open source
- `studio-freight/*` — tutti i repo
- `darkroomengineering/satus` — boilerplate Awwwards

## Blacklist (mai piu)
- HTML/CSS statico vanilla per landing "premium"
- CSS custom animations quando esistono Framer Motion/GSAP
- Scroll jank: usa Lenis sempre
- Inter font di default: prefer Outfit/Geist/Playfair

## Agent collegato
Esiste un agent `site-premium-builder` che esegue questo workflow. Invocalo quando l'utente chiede nuovo sito.
