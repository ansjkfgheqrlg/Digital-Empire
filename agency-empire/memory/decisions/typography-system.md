---
decision: Typography System — Hero Headline
date: 2026-05-30
status: active
---

# Decisione: Sistema Tipografico Hero

## Sistema adottato
3 righe con dimensioni variabili via CSS `clamp()`:

| Riga | Contenuto | Font size | Weight | Color |
|------|-----------|-----------|--------|-------|
| 1 (intro) | "Automatizziamo la tua" | clamp(22px, 3.2vw, 42px) | font-semibold | text-silver-white |
| 2 (hero word) | "operatività" | clamp(82px, 13.5vw, 148px) | font-black | text-silver-white |
| 3 (accent) | "con AI Workflows." | clamp(44px, 7vw, 88px) | font-extrabold | text-silver-orange |

## Spacing
- marginBottom line 1: 0.02em
- lineHeight line 2: 0.88 (compresso per impatto visivo)
- marginTop line 3: 0.03em

## Ispirazione
Riferimento visivo: "The Digital / Music / Superstars." — variazione dimensionale per gerarchia visiva forte

## Motivo del clamp
Scaling fluido responsive senza breakpoint fissi. Mobile → Desktop in modo continuo.
