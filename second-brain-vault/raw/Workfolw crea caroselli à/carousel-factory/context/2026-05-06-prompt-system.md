# PROMPT-SYSTEM

> Source: File system (`Workfolw crea caroselli à\carousel-factory\context\PROMPT-SYSTEM.md`)
> Collected: 2026-05-06
> Published: Unknown

# SISTEMA PROMPT — MENTALITÀ BRUTALE
# Per generazione immagini AI (Gemini / Imagen)

## COME FUNZIONA

Per ogni carosello genero:
1. La struttura del carosello (copy di ogni slide)
2. Un prompt ultra-specifico per ogni slide
3. L'utente incolla ogni prompt in Gemini e genera l'immagine

Il prompt genera la SLIDE COMPLETA: foto di sfondo + testo overlay + effetti.

---

## LINGUA DEI PROMPT

**SEMPRE IN INGLESE** — i modelli di image generation performano meglio in inglese.
Il TESTO che deve apparire nella slide è in italiano (tra virgolette nel prompt).

---

## STRUTTURA STANDARD DEL PROMPT

```
[TECHNICAL SPECS]
[BACKGROUND PHOTO]
[PHOTO TREATMENT]
[TYPOGRAPHY — small text]
[TYPOGRAPHY — hero text]
[EFFECTS & MOOD]
[BRAND DETAILS]
```

---

## TEMPLATE PROMPT — HOOK COVER (slide con foto soggetto)

```
Instagram carousel slide, 1080x1080px square format.

BACKGROUND PHOTO: [descrizione soggetto ed ambiente — uomo, donna, ambiente specifico]
Full bleed photo, subject [posizione: left/center/right], [espressione: intense gaze / looking away / dramatic]

PHOTO TREATMENT:
- Severely darkened: brightness reduced to 40%
- Deep blood-red color grade: add crimson/dark red tint (hue shift toward #8B0000)
- Heavy cinematic film grain texture overlaid (35mm film look)
- Intense vignette: edges darkened heavily, center slightly brighter
- Mood: brutal, dark, raw, cinematic

TEXT OVERLAY — exact placement:
1. SMALL TEXT (top-left, 60px from edges):
   "[testo piccolo qui]"
   Font: Inter Regular, size 26px, color #EEEEEE, opacity 85%

2. HERO TEXT (left-aligned, lower third of image):
   "[riga 1]"
   "[riga 2]"
   "[riga 3 — questa è la parola accent]"
   Font: Anton Bold, lowercase, size 110px, line-height 0.9
   Each word on its own line
   Color treatment: vertical gradient per word — blood red (#8B0000) at top of each letter → silver (#C0C0C0) at bottom
   EXCEPTION: "[parola accent]" = solid blood red (#8B0000) with subtle red glow (text-shadow: 0 0 40px rgba(139,0,0,0.8))

BRAND WATERMARK:
Small circular logo, bottom-right corner, 70px diameter, 65% opacity
Logo: dark warrior king silhouette raising crown, blood-red background

OVERALL MOOD: brutal, intense, premium dark Italian brand, cinematic quality, high contrast
NO: clean/bright aesthetics, soft colors, motivational poster look
```

---

## TEMPLATE PROMPT — TEXT STATEMENT (slide solo testo / foto sfondo)

```
Instagram carousel slide, 1080x1080px square format.

BACKGROUND PHOTO: [descrizione ambiente/soggetto]
Full bleed, [composizione specifica]

PHOTO TREATMENT:
- Darkness level: 85% darkened (almost black but with texture visible)
- Blood-red color cast throughout
- Heavy film grain (35mm analog)
- Deep vignette edges

DECORATIVE ELEMENT:
Large oversized quotation mark ("), top-left corner, font size 260px
Color: blood red (#8B0000), opacity 10%, font Anton

TEXT OVERLAY:
1. SMALL TEXT: "[testo piccolo]"
   Inter Regular, 26px, #EEEEEE, top-left area

2. HERO TEXT: "[parola 1]" / "[parola 2]" / "[parola 3]"
   Anton Bold, lowercase, 110px, left-aligned, line-height 0.9
   Per-word gradient: blood red → silver (top to bottom of each letter)
   Accent word "[parola]": solid #8B0000 + red glow

BRAND WATERMARK: circular logo bottom-right, 70px, 65% opacity

MOOD: cinematic, dark, raw truth, no-filter honesty
```

---

## TEMPLATE PROMPT — LIST ITEMS (slide con lista badge)

```
Instagram carousel slide, 1080x1080px square format.

BACKGROUND PHOTO: [soggetto/ambiente]

PHOTO TREATMENT:
- 80% darkened, strong blood-red tint
- Film grain, vignette

TEXT LAYOUT (top to bottom, left-aligned):
1. SMALL TEXT: "[testo piccolo]"
   Inter Regular, 26px, #EEEEEE

2. BADGE LIST (3 items, pill/capsule shape):
   Each badge: horizontal pill shape, border 2px solid [colore], border-radius 50px, dark semi-transparent fill

   Badge 1: icon "[icona]" + text "[testo item 1]"
             border color: [colore 1], text color: [colore 1], font: Anton 30px
   Badge 2: icon "[icona]" + text "[testo item 2]"
             border color: [colore 2], text color: [colore 2], font: Anton 30px
   Badge 3: icon "[icona]" + text "[testo item 3]"
             border color: [colore 3], text color: [colore 3], font: Anton 30px

3. HERO TEXT (bottom): "[parola 1]" "[parola accent]"
   Anton Bold, lowercase, 90px, per-word gradient red→silver
   Accent: solid #8B0000

BRAND WATERMARK: bottom-right, 70px, 65% opacity

MOOD: dark, list-style, informative but brutal
```

---

## TEMPLATE PROMPT — QUOTE BLOCK (citazione)

```
Instagram carousel slide, 1080x1080px square format.

BACKGROUND PHOTO: [soggetto]

PHOTO TREATMENT: 85% dark, blood-red tint, heavy grain, heavy vignette

LEFT BORDER ACCENT:
Vertical line, 5px wide, blood red (#8B0000), left side of text area (60px from left edge)

TEXT:
1. SMALL TEXT: "[testo piccolo]"
   Inter Regular, 24px, #EEEEEE, above the border

2. QUOTE TEXT (left of border line, 28px padding-left from border):
   "[riga 1]"
   "[riga 2]"
   "[parola accent]"
   Anton Bold, lowercase, 90px, per-word gradient blood-red→silver
   Accent: solid #8B0000

Large decorative quote mark top-left, 260px, #8B0000 at 10% opacity

BRAND WATERMARK: bottom-right, 70px, 65% opacity
```

---

## TEMPLATE PROMPT — CTA FINALE

```
Instagram carousel slide, 1080x1080px square format.

BACKGROUND PHOTO: [ambiente business / team / community]

PHOTO TREATMENT: 75% darkened, blood-red tint, film grain, vignette

ALL TEXT CENTERED:

1. HERO TEXT (upper-center):
   "[riga 1]"
   "[riga 2]"
   "[riga 3 — parola accent]"
   Anton Bold, lowercase, 110px, centered
   Per-word gradient: blood red (#8B0000) top → silver (#C0C0C0) bottom
   Accent word: solid #8B0000

2. CTA BUTTON (center):
   Pill-shaped button, background #8B0000, border-radius 60px
   Text: "segui ora" — white, Anton Bold, uppercase, 30px, letter-spacing 1px
   Padding: 22px 56px

3. INSTAGRAM HANDLE (below button):
   "@mentalita.brutale"
   Inter Regular, 22px, #777777

BRAND WATERMARK: bottom-right, 70px, 65% opacity

MOOD: call to action, urgent but premium, dark and intense
```

---

## COLORI DI RIFERIMENTO

| Elemento | Colore | Hex |
|----------|--------|-----|
| Accent / rosso sangue | Blood red | `#8B0000` |
| Argento | Silver | `#C0C0C0` |
| Background | Near black | `#0A0A0A` |
| Testo piccolo | Off-white | `#EEEEEE` |
| Testo muted | Gray | `#777777` |
| Gradiente testo grande | `#8B0000` (top) → `#C0C0C0` (bottom) per ogni parola |

---

## COME USO QUESTO FILE

Quando l'utente chiede un carosello:
1. Genero la struttura (copy di ogni slide)
2. Per ogni slide compilo il template prompt corrispondente
3. Output: documento con tutti i prompt numerati, pronti da copiare uno ad uno in Gemini
