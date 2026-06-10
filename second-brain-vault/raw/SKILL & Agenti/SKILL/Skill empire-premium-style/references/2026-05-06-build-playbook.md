# build-playbook

> Source: File system (`SKILL & Agenti\SKILL\Skill empire-premium-style\references\build-playbook.md`)
> Collected: 2026-05-06
> Published: Unknown

# Build Playbook & Troubleshooting

## Procedura post-generazione

```bash
cd <dest-project>
npm install --silent
npm run build
```

Se build OK → `npm run dev` → verifica http://localhost:3000 visivamente.

## Errori comuni e fix

### `Cannot find module 'shadcn/tailwind.css'`
`design-tokens.css` ha `@import "shadcn/tailwind.css";` in alto. Rimuovilo — non abbiamo shadcn nelle deps.

### `Cannot find module 'tw-animate-css'`
Tieni la riga `@import "tw-animate-css";` SOLO se il CSS usa classi tw-animate (es. `animate-*` custom). Altrimenti rimuovila e rimuovi `tw-animate-css` da package.json.

### `Module not found: '@/lib/utils'`
Assicurati che `src/lib/utils.ts` esista con l'helper `cn`. Verifica anche che `tsconfig.json` abbia `"paths": { "@/*": ["./src/*"] }`.

### Font Onest non carica
Verifica che `layout.tsx` importi `import { Onest } from "next/font/google"` e che la classe `${onest.variable}` sia sull'`<html>`.

### Grain non visibile
La classe `grain-fine` DEVE essere sul `<body>`, non su altri elementi. Se stai debuggando, verifica che `z-index: 100` e `position: fixed` del ::before siano presenti.

### Lenis error SSR
`smooth-scroll-provider.tsx` DEVE iniziare con `"use client";`. Se non c'è, aggiungilo.

### `border-border` / `outline-ring/50` unknown utility
Tailwind v4 con `@theme inline` → la mappatura `--color-border` → `border-border` richiede `@theme inline` correttamente impostato. Se la build fallisce su `@apply border-border`, sostituisci con:
```css
* { border-color: var(--border); outline-color: color-mix(in oklch, var(--ring) 50%, transparent); }
```

### `next/font` build error su Windows
Se il build si blocca sul download Google Fonts, assicurati che la macchina abbia connessione. In alternativa fallback a `"system-ui, -apple-system, sans-serif"` nel CSS e rimuovi `Onest` da layout (ultima risorsa, perde eleganza).

## Verifica qualità finale

Prima di consegnare, controlla che in DevTools:

- [ ] Body ha class `grain-fine` → sul ::before c'è l'SVG noise
- [ ] HTML ha class `dark` + `antialiased`
- [ ] Font-family computato è "Onest", fallback system
- [ ] Scroll è smooth (Lenis attivo)
- [ ] Hero marquee anima (30s linear infinite)
- [ ] silver-chip hanno animazione chip-float (solo desktop ≥1024px)
- [ ] H1 hero ha gradient silver-white + silver-orange visibile
- [ ] Almeno una `hl-block` arancione visibile nel subtitle
- [ ] CTA `btn-orange` ha box-shadow glow arancione
- [ ] Card-paper su paper sezioni hanno shadow profondo + hover translateY
- [ ] Sezioni alternate bg (ink → paper → ink → paper…)

Se anche solo UNA di queste fallisce, la trasformazione NON è completa.

## Avvio dev server (finale)

```bash
cd <dest> && npm run dev
```

Comunica all'utente: "Progetto pronto su http://localhost:3000. Apri e confronta con ccm-premium per verificare che lo stile sia identico. Per modifiche ai colori chiedi `modifica palette`, per aggiungere sezioni chiedi `aggiungi sezione <tipo>`."
