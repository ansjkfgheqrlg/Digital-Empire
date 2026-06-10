---
decision: Color Palette & Design Tokens
date: 2026-05-30
status: active
---

# Decisione: Palette e Token

## Colori base
| Token | Hex | Uso |
|-------|-----|-----|
| ink | #1c1c1c | Background dark sections, testo su paper |
| paper | #fafafa | Background light sections |
| grey | #e8e8e6 | Background medium sections |
| orange | #fb4604 | Accent, CTA, highlights |

## Classi Tailwind custom
- `bg-ink`, `bg-paper`, `bg-grey`, `bg-ink-2`
- `text-silver-white` — testo chiaro su bg dark
- `text-silver-orange` — accent orange su bg dark
- `text-silver-black` — testo scuro su bg light
- `text-orange-pure` — orange puro #fb4604
- `bubble-orange` — pill badge arancione
- `card-glass` — card trasparente bordata
- `card-silver-orange` — card con accent orange
- `card-dark` — card su bg dark

## Silver Border (costante usata ovunque)
```
2px solid rgba(210,218,232,0.65)
```
Usata su: audience cards, pricing cards, builder cards, engine room

## Font
- Sans: font di sistema / Next.js default
- Serif: `var(--font-serif), Georgia, serif` — usato per parole italic accent
