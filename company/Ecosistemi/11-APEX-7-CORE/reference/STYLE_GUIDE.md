# DIGITAL EMPIRE - REFERENCE STYLE GUIDE - CAROUSEL PREMIUM
Estratto dalle 8 slide reference fornite - analisi pixel-perfect

## Palette Colori Esatta
- Background: #000000 puro con overlay grain texture 35% opacity (film grain, non flat)
- Glow primario: #FF3B1F / #FF4D2E / #E94E1B - radial gradient angoli top-right e bottom-left, 400-600px radius, blur 120px, opacity 40-60%
- Testo headline: #F5F5F0 (bianco sporco con grain, non #FFFFFF puro) - texture leggera 5%
- Accent italic: #FF3B1F (stesso del glow) - parole chiave in serif italic
- Grigio body: #9CA3AF / #A1A1AA
- Pill border: rgba(255,255,255,0.25) - 1px stroke
- Card dark: rgba(15,15,15,0.9) con border rgba(255,255,255,0.08) - 1px, radius 20-24px
- Card light (slide soluzione): gradient #F5F5F2 -> #FFB088 / #FF8A5B peach, 135deg

## Tipografia Esatta
- Headline BIG: Sans-serif extrabold 800-900, font simile a General Sans / Satoshi / Inter Tight, 110-140pt su 1080x1350, tight line-height 0.9, letter-spacing -0.03em
- Accent words: Serif italic elegante (Instrument Serif Italic / Playfair Display Italic / Editorial New Italic) 110-140pt, italic 12deg, colore #FF3B1F
- Pill label top: Monospace JetBrains Mono / Space Mono, uppercase, 13-15pt, tracking 0.12em, colore #E5E5E5 su sfondo pill trasparente con border
- Body: Inter / Satoshi regular 22-26pt, line-height 1.4, colore #9CA3AF
- Numeri 01 02 03: Serif italic #FF3B1F, 80-100pt
- Metrics (97%, 120+): Sans bold 64-72pt white + accent red per 120+
- Footer page: Mono 14pt #6B7280 "3/8"
- Logo E: Quadrato rounded 12px con gradient #FF8A5B -> #FFFFFF, lettera E bold bianca

## Layout Griglia 1080x1350
- Margin: 64px left/right/top/bottom
- Top pill: 64px from top, height 36px, padding 12px 20px, gap icon 8px
- Headline: inizia a 180px from top, width 952px (1080-128), max 3-4 righe
- Body: sotto headline 24px gap
- Card: se presente, 64px margin, radius 20px, padding 32px
- Footer: 64px from bottom, flex space-between page number left, logo right 48x48px + text 18pt
- Thin line divider: 1px rgba(255,255,255,0.15) full width quando presente

## Effetti Obbligatori (questo fa la differenza premium)
1. FILM GRAIN: overlay noise texture su TUTTA immagine, 35% opacity, size 1-2px grain, NON pulito digitale
2. GLOW ANGOLARE: 2 radial gradient - uno top (0% top, 100% right) orange-red #FF3B1F 60% opacity 500px, uno bottom-left #FF3B1F 40% 600px - blur heavy
3. VIGNETTE: subtle dark vignette 15%
4. TEXTURE su testo: headline white non flat, ha leggero grain/bump 3% per effetto stampa premium
5. Card border inner glow: per dark cards, inner highlight 1px top con rgba(255,255,255,0.15)
6. Icon pill: emoji/icona rossa #FF3B1F dentro pill (occhio, ingranaggi, stella, grafico, domanda, fulmine, orologio)

## Composizione per tipo slide
- SLIDE HOOK (Ogni post ti ruba 3 ore): Grande headline 60% canvas, sotto lista con freccia rossa →
- SLIDE VERITÀ: Headline con 2-3 parole rosse italic, sotto body 2 righe, divider line, footer frase italic mono piccola
- SLIDE CONTENT FACTORY: Domanda grande, sotto sottotitolo gray, swipe indicator mono in basso
- SLIDE SOLUZIONE: Headline + card light con 3 check + footer tags mono
- SLIDE COME FUNZIONA: Titolo + 3 card dark numerate 01/02/03 con linea verticale sinistra
- SLIDE RISULTATO: Titolo + 3 cards metrics affiancate (ratio 1:1:1, gap 16px)
- SLIDE DOMANDA VERA: Titolo con virgolette red «» + card dark grande con lista check rossi
- SLIDE CTA: Titolo + card offer con prezzo barrato + prezzo grande + pill -50% + bottone gradient white->orange con freccia + sottotitolo mono

## Prompt engineering per replicare
Devi descrivere ESATTAMENTE: "black background #000000 with heavy film grain noise texture 35%, subtle red-orange #FF3B1F radial glow top-right and bottom corners blurred, premium editorial Instagram carousel 1080x1350, typography mix bold white sans-serif Satoshi extra-bold with textured grain + elegant red #FF3B1F serif italic Instrument Serif for accent words, top pill label with thin white border rgba(255,255,255,0.25) and red icon, monospaced JetBrains Mono uppercase, bottom page number 3/8 mono gray and Digital Empire E logo orange gradient square, layout with 64px margins, ultra-premium noise grain, no flat vector, no 3D cheesy, photoreal grain, high-end agency style"
