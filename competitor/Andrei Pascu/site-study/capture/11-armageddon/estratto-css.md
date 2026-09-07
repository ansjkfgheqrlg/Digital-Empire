# Estratto CSS — 11-armageddon

Solo cio' che insegna qualcosa: variabili, movimenti, effetti, gradienti, curve,
caratteri e **i commenti dell'autore**. Il resto e' utility generata e non si legge.

Generato da `scripts/analizza_css.py`.

---

## `src/02-player.css` — 232 KB

### Movimenti — 31 @keyframes

```css
@keyframes buffer {100%{transform:translateX(-10px)}}
@keyframes throb {0%,100%{background-color:#555}50%{background-color:#444}}
@keyframes wiggle {0%{transform:translateY(10px)}20%{transform:translateY(0)}40%,80%{transform:translateX(8px)}60%{transform:translateX(-8px)}100%{transform:translateX(0)}}
@keyframes pulse {50%{transform:scale(.9)}}
@keyframes dash {0%{stroke-dasharray:1,200;stroke-dashoffset:0}50%{stroke-dasharray:89,200;stroke-dashoffset:-35px}100%{stroke-dasharray:89,200;stroke-dashoffset:-135px}}
@keyframes rotate {100%{transform:rotate(360deg)}}
@keyframes scaleAnimation {0%{transform:scale(.9,.9)}100%{transform:scale(1,1)}}
@keyframes LikeButton_module_heartbeat__3908feee {0%{transform:scale(1)}10%{transform:scale(1)}20%{transform:scale(1.3)}30%{transform:scale(1.1)}40%{transform:scale(1.3)}100%{transform:scale(1)}}
@keyframes ShareButton_module_takeoff__26260904 {0%{transform:translate(0,0)}20%{transform:translate(-3px,3px)}40%{transform:translate(2px,-2px)}60%{transform:translate(-1px,1px)}80%{transform:translate(.5px,-.5px)}100%{transform:translate(0,0)}}
@keyframes EmbedButton_module_embedPop__dece8678 {0%{transform:scale(1)}40%{transform:scale(1.15)}100%{transform:scale(1)}}
@keyframes WatchLaterButton_module_pop__238c6c3b {0%{transform:scale(1)}10%{transform:scale(1.15)}100%{transform:scale(1)}}
@keyframes TinyProgressBar_module_buffer__c04d36b1 {100%{transform:translateX(-10px)}}
@keyframes ShareSheet_module_backdropFadeIn__5ab8a323 {from{opacity:0}to{opacity:1}}
@keyframes ShareSheet_module_backdropFadeOut__5ab8a323 {from{opacity:1}to{opacity:0}}
@keyframes ShareSheet_module_modalSlideIn__5ab8a323 {from{opacity:0;transform:translateY(12px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}
@keyframes ShareSheet_module_modalSlideOut__5ab8a323 {from{opacity:1;transform:translateY(0) scale(1)}to{opacity:0;transform:translateY(12px) scale(.97)}}
@keyframes AiCreditsEnrollmentModal_module_backdropFadeIn__6d3d95f8 {from{opacity:0}to{opacity:1}}
@keyframes AiCreditsEnrollmentModal_module_backdropFadeOut__6d3d95f8 {from{opacity:1}to{opacity:0}}
@keyframes AiCreditsEnrollmentModal_module_modalSlideIn__6d3d95f8 {from{opacity:0;transform:translateY(12px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}
@keyframes AiCreditsEnrollmentModal_module_modalSlideOut__6d3d95f8 {from{opacity:1;transform:translateY(0) scale(1)}to{opacity:0;transform:translateY(12px) scale(.97)}}
@keyframes OutroContentWrapper_module_fadeIn__06afa88b {0%{opacity:0}100%{opacity:1}}
@keyframes LinkOutro_module_slideDown__0f1c39e6 {to{transform:translate(0,0);opacity:1}}
@keyframes Spinner_module_buffer__795e5e53 {100%{transform:translateX(-10px)}}
@keyframes Spinner_module_throb__795e5e53 {0%,100%{background-color:#555}50%{background-color:#444}}
@keyframes Spinner_module_wiggle__795e5e53 {0%{transform:translateY(10px)}20%{transform:translateY(0)}40%,80%{transform:translateX(8px)}60%{transform:translateX(-8px)}100%{transform:translateX(0)}}
@keyframes Spinner_module_pulse__795e5e53 {50%{transform:scale(.9)}}
```

### filtri — 11 valori distinti
```
blur(10px)
blur(40px)
blur(8px)
brightness(.9) contrast(1.5) grayscale(0) hue-rotate(0) saturate(1) sepia(0)
brightness(0)
brightness(1) contrast(.9) grayscale(0) hue-rotate(0) saturate(1) sepia(.2)
brightness(1) contrast(1.1) grayscale(0) hue-rotate(0) saturate(1.1) sepia(0)
brightness(1) contrast(2) grayscale(0) hue-rotate(0) saturate(1) sepia(0)
brightness(1.1) contrast(1.1) grayscale(1) hue-rotate(0) saturate(1) sepia(0)
brightness(1.2) contrast(.9) grayscale(0) hue-rotate(-20deg) saturate(.85) sepia(0)
brightness(1.2) contrast(.9) grayscale(0) hue-rotate(0) saturate(1.1) sepia(0)
```

### blend — 4 valori distinti
```
darken
multiply
overlay
screen
```

### clip/mask — 3 valori distinti
```
inset(50%)
linear-gradient(to right,transparent 0%,#000 16px,#000 calc(100% - 16px),transparent 100%)
no-clip
```

### container — 1 valori distinti
```
scroll-state
```

### Gradienti non banali — 10
```css
linear-gradient(45deg,#414141 25%,transparent 25%),linear-gradient(-45deg,#414141 25%,transparent 25%)
linear-gradient(45deg,transparent 75%,#414141 75%),linear-gradient(-45deg,transparent 75%,#414141 75%)
linear-gradient(to right,rgba(66,10,14,.2),transparent),radial-gradient(circle,transparent,transparent)
linear-gradient(to right,transparent 0%,#000 16px,#000 calc(100% - 16px)
linear-gradient(to right,transparent,transparent),radial-gradient(circle at 40% 40%,rgba(255,255,255,.8)
linear-gradient(to right,transparent,transparent),radial-gradient(circle,#804e0f,#3b003b)
linear-gradient(to right,transparent,transparent),radial-gradient(circle,#a6b1ff 50%,#342134)
linear-gradient(to right,transparent,transparent),radial-gradient(circle,#d0ba8e 20%,#360309 85%,#1d0210 100%)
linear-gradient(to right,transparent,transparent),radial-gradient(circle,transparent,transparent)
radial-gradient(#82ffeb 0,#17d5ff 30%,#0ba1ff 45%,#9e00ff 75%,rgba(157,0,255,0)
```

### Curve — 9
```
cubic-bezier(.08, .82, .17, 1)
cubic-bezier(.17, .88, .32, 1.28)
cubic-bezier(.18, .89, .32, 1.2)
cubic-bezier(.18, 0, .07, 1)
cubic-bezier(.34,1.2,.64,1)
cubic-bezier(0.17,0,0.2,1)
cubic-bezier(0.18,0.89,0.32,1.2)
cubic-bezier(0.2,0.9,1,1)
cubic-bezier(0.5,0,0.83,1)
```

### Commenti dell'autore — 2 (**lo strato 4**)

- fonte: https://f.vimeocdn.com/p/4.46.106/css/player.css
- VimeoPlayer - v4.46.106 - 2026-09-04

---

## `src/01-armageddon.css` — 24 KB

### Variabili — 4

**Colore (2):**
```css
--red: #bc0807;
--ink: #fff;
```

**Misura, curva, tempo, carattere (2):**
```css
--ease-heavy: cubic-bezier(0.65, 0, 0.25, 1);
--ease-land: cubic-bezier(0.16, 0.86, 0.3, 1);
```

### Movimenti — 3 @keyframes

```css
@keyframes ag-rise { from { opacity: 0; transform: translateY(var(--rise)); } to { opacity: 1; transform: none; } }
@keyframes ag-zoom { from { transform: scale(1.055); } to { transform: none; } }
@keyframes ag-fade { from { opacity: 0; } to { opacity: 1; } }
```

### filtri — 4 valori distinti
```
blur(4px)
drop-shadow(0 0 10px rgba(188, 8, 7, 0.75))
drop-shadow(0 0 calc(var(--u) * 0.014) rgba(0, 0, 0, 0.9))
drop-shadow(0 calc(var(--u) * 0.012) calc(var(--u) * 0.03) rgba(0, 0, 0, 0.55)) drop-shadow(0 calc(var(--u) * 0.032) calc(var(--u) * 0.078) rgba(0, 0, 0, 0.45))
```

### ombre-testo — 1 valori distinti
```
0 0 calc(var(--u) * 0.028) rgba(0, 0, 0, 0.95), 0 calc(var(--u) * 0.003) 0 rgba(0, 0, 0, 0.6)
```

### contorno-testo — 1 valori distinti
```
max(1px, calc(var(--u) * 0.0013)) var(--red)
```

### container — 1 valori distinti
```
inline-size
```

### Gradienti non banali — 7
```css
linear-gradient( to bottom, #000 0, rgba(0, 0, 0, 0)
linear-gradient( to bottom, rgba(0, 0, 0, 0.71)
linear-gradient(90deg, rgba(188, 8, 7, 0.85), transparent)
linear-gradient(90deg, transparent, rgba(188, 8, 7, 0.85)
linear-gradient(to bottom, rgba(0, 0, 0, 0) 0, rgba(0, 0, 0, 0.992)
linear-gradient(to bottom, rgba(0, 0, 0, 0.992) 0, rgba(0, 0, 0, 0.71)
radial-gradient(120% 72% at 50% 0%, rgba(188, 8, 7, 0.22)
```

### Curve — 2
```
cubic-bezier(0.16, 0.86, 0.3, 1)
cubic-bezier(0.65, 0, 0.25, 1)
```

### @font-face — 1
```css
@font-face { font-family: "Curseyt"; src: url("/assets/fonts/curseyt.woff") format("woff"); font-weight: 400; font-style: normal; font-display: block; /* the blackletter IS the design — no swap flash */ }
```

### Commenti dell'autore — 39 (**lo strato 4**)

- fonte: https://armageddon.bsns.it/assets/armageddon.css
- the blackletter IS the design — no swap flash
- his, sampled out of the mockup
- slow off the mark, slow into place
- No default scroller. Styling it turns off macOS overlay scrollbars, so the gutter is reserved up front and nothing shifts when it appears. The page measures itself in container units, which already exclude it.
- clip, not hidden: hidden would make body a scroller
- The design column. Everything on the page is a fraction of it, so the whole composition scales as one. Container units so a desktop scrollbar cannot push the page sideways; vw is the fallback. The dialog is a sibling of `.page`, so it is given the same tokens.
- left edge of the design column
- Andrei's note on AP-138: the type scale is his rough pass, fix it. At his exact ratios the buy button lands at 117x29px on a phone with a 10px label. These floors keep each element's own proportions and only stop it shrinking past the point where it can be read and tapped.
- --- the masthead -------------------------------------------------------- Not in the mockup; his brief asks for a way back to bsns.it. Built as a plate between two rules that dissolve into the black, so it reads as part of the same object rather than a website nav bolted on top.
- --- the hero ------------------------------------------------------------ A square at column width: black, the splatter, then the portrait cut to his silhouette on top of it, then the two words.
- stops where ::after starts, at 0.8785
- deliberately no z-index: the words have to sort individually against the portrait, one below it and two above
- "Armageddon" is drawn twice in the mockup: solid *behind* him, and again in front as an outline only. So the word reads solid against the black and turns into a red etching where it crosses his hair. The two move together as one parallax group.
- The landing move. It sits on the children so it never fights the parallax transforms the script writes onto the layers themselves.
- --- the video, over the red sky ----------------------------------------
- The fades are the mockup's own, in absolute distance from the top of the section so they land in the same place whatever the section measures. The first stop picks up at exactly the opacity `.hero::after` hands over at, so the two halves of his one gradient meet without a step.
- Andrei asked on 5 September for a line and an arrow over the player, big enough that nobody misses it. The room comes from the video's own top, which moves down by 6.5% of the column — the empty black between the player and "Sei pronto?" absorbs it, so nothing else in the section moves.
- it sits over the sky, never over a control
- Off-white, not the red: the sky behind this band is red, and his red on it is the one thing that would not read. The shadow is what carries it over the bright patches of that photograph.
- His own thumbnail is 16:9, and so is the video that will replace it, so the slot is 16:9 rather than the mockup grey box's rough 1.67. Same top edge, same width — it ends 2.7% of the column higher.
- On a phone his desktop inset leaves the player at 76% of the screen with uneven margins either side. Andrei asked on 5 September for the full width of the screen and square corners: the video is the page's whole job here, so it gets the whole width. `--u` is the design column, which on a phone is the viewport, and `--col` is its left edge — so this is edge to edge without a `100vw` that a scrollba
- A phone's column is the screen, so the same fractions come out small in absolute terms: the line and the arrow are set larger against it. The player is full width here, which makes it 56% of the column tall instead of 43%, so the section has to grow — otherwise the callout above and "Sei pronto?" below both land on top of the player. Every number here is measured at 390px: callout ends 9px above t
- This override has to sit after the rule above, not with the other phone rules further up: same specificity, so source order decides. On a phone the player is full width and therefore taller, and it would otherwise run under the question.
- --- the offer, over the fire ------------------------------------------- This one flows rather than sitting on fixed coordinates: the buttons and the counter carry a size floor on small screens, so the section has to be free to grow under them.
- The box is exactly the two tickets' footprint, so hovering means hovering them and not half the section.
- The mockup places these through Canva's own copies of the artwork, which carry more transparent margin than the source PNGs in docs/. These rects are re-derived so the *printed* ticket lands exactly where the mockup puts it — do not "simplify" them back to the PDF's own numbers.
- Separated: both the state they arrive in and the state they take under the mouse. `is-locked` is on while they arrive, which is what keeps the hover from firing mid-flight.
- the ticket overlaps it, as drawn
- --- the counter ---------------------------------------------------------

---

## `src/06-css2.css` — 4 KB

### @font-face — 12
```css
@font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko70yyygA.woff2) format('woff2'); unicode-range: U+0460-052F, U+1C80-1C8A, U+20B4, }
@font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko50yyygA.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128- }
@font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko40yyygA.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7- }
@font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko20yw.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+ }
@font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 700; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko70yyygA.woff2) format('woff2'); unicode-range: U+0460-052F, U+1C80-1C8A, U+20B4, }
@font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 700; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko50yyygA.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128- }
@font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 700; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko40yyygA.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7- }
@font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 700; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko20yw.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+ }
@font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 800; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko70yyygA.woff2) format('woff2'); unicode-range: U+0460-052F, U+1C80-1C8A, U+20B4, }
@font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 800; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko50yyygA.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128- }
```

### Commenti dell'autore — 7 (**lo strato 4**)

- fonte: https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700;800&display=swap
- cyrillic-ext */ @font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko70yyygA.woff2) format('woff2'); unicode-range: U+0460-052F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F; } /* vietnamese
- latin-ext */ @font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko40yyygA.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB
- cyrillic-ext */ @font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 700; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko70yyygA.woff2) format('woff2'); unicode-range: U+0460-052F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F; } /* vietnamese
- latin-ext */ @font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 700; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko40yyygA.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB
- cyrillic-ext */ @font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 800; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko70yyygA.woff2) format('woff2'); unicode-range: U+0460-052F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F; } /* vietnamese
- latin-ext */ @font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 800; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko40yyygA.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB
