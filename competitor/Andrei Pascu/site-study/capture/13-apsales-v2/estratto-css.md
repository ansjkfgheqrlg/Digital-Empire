# Estratto CSS — 13-apsales-v2

Solo cio' che insegna qualcosa: variabili, movimenti, effetti, gradienti, curve,
caratteri e **i commenti dell'autore**. Il resto e' utility generata e non si legge.

Generato da `scripts/analizza_css.py`.

---

## `src/11-styles-CHG2jDaU.css` — 124 KB

### Variabili — 38

**Colore (27):**
```css
--brand-ink: oklch(22.73% .0038 286.09);
--brand-bone: oklch(93.01% .0122 96.43);
--brand-blue: oklch(55.6% .2453 261.33);
--brand-paper: oklch(98.21% 0 0);
--brand-pitch: oklch(17.76% 0 0);
--brand-void: oklch(14.48% .002 285);
--card: oklch(100% 0 0);
--popover: oklch(100% 0 0);
--primary-foreground: oklch(100% 0 0);
--muted: oklch(95.5% .0061 96.43);
--muted-foreground: oklch(52% .0055 286);
--destructive: oklch(57.7% .245 27.325);
--destructive-foreground: oklch(98.4% .003 247.858);
--border: oklch(90% .004 286);
--input: oklch(90% .004 286);
--chart-1: oklch(64.6% .222 41.116);
--chart-2: oklch(60% .118 184.704);
--chart-3: oklch(39.8% .07 227.392);
--chart-4: oklch(82.8% .189 84.429);
--chart-5: oklch(76.9% .188 70.08);
--sidebar: oklch(98.4% .003 247.858);
--sidebar-foreground: oklch(12.9% .042 264.695);
--sidebar-primary: oklch(20.8% .042 265.755);
--sidebar-primary-foreground: oklch(98.4% .003 247.858);
--sidebar-accent: oklch(96.8% .007 247.896);
--sidebar-accent-foreground: oklch(20.8% .042 265.755);
--sidebar-border: oklch(92.9% .013 255.508);
```

**Misura, curva, tempo, carattere (11):**
```css
--radius: .5rem;
--background: var(--brand-paper);
--foreground: var(--brand-ink);
--card-foreground: var(--brand-ink);
--popover-foreground: var(--brand-ink);
--primary: var(--brand-blue);
--secondary: var(--brand-bone);
--secondary-foreground: var(--brand-ink);
--accent: var(--brand-bone);
--accent-foreground: var(--brand-ink);
--ring: var(--brand-blue);
```

### Movimenti — 9 @keyframes

```css
@keyframes node-in {0%{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
@keyframes rail-marquee {0%{transform:translate(0)}to{transform:translate(-50%)}}
@keyframes logo-marquee {0%{transform:translate(0)}to{transform:translate(-50%)}}
@keyframes pulse {50%{opacity:.5}}
@keyframes enter {0%{opacity:var(--tw-enter-opacity,1);transform:translate3d(var(--tw-enter-translate-x,0),var(--tw-enter-translate-y,0),0)scale3d(var(--tw-enter-scale,1),var(--tw-enter-scale,1),var(--tw-enter-scale,1))rotate(var(--tw-enter-rotate,0));filter:blur(var(--tw-enter-blur,0))}}
@keyframes exit {to{opacity:var(--tw-exit-opacity,1);transform:translate3d(var(--tw-exit-translate-x,0),var(--tw-exit-translate-y,0),0)scale3d(var(--tw-exit-scale,1),var(--tw-exit-scale,1),var(--tw-exit-scale,1))rotate(var(--tw-exit-rotate,0));filter:blur(var(--tw-exit-blur,0))}}
@keyframes accordion-down {0%{height:0}to{height:var(--radix-accordion-content-height,var(--bits-accordion-content-height,var(--reka-accordion-content-height,var(--kb-accordion-content-height,var(--ngp-accordion-content-height,auto)))))}}
@keyframes accordion-up {0%{height:var(--radix-accordion-content-height,var(--bits-accordion-content-height,var(--reka-accordion-content-height,var(--kb-accordion-content-height,var(--ngp-accordion-content-height,auto)))))}to{height:0}}
@keyframes caret-blink {0%,70%,to{opacity:1}20%,50%{opacity:0}}
```

### filtri — 8 valori distinti
```
blur(var(--tw-enter-blur,0))
blur(var(--tw-exit-blur,0))
contrast(1.15)brightness(1.3)
contrast(1.3)brightness(1.45)
contrast(1.35)brightness(1.5)
url(#luma-alpha)
url(#luma-alpha-band)
var(--tw-blur,) var(--tw-brightness,) var(--tw-contrast,) var(--tw-grayscale,) var(--tw-hue-rotate,) var(--tw-invert,) var(--tw-saturate,) var(--tw-sepia,) var(--tw-drop-shadow,)
```

### blend — 1 valori distinti
```
screen
```

### clip/mask — 13 valori distinti
```
inset(50%)
linear-gradient(#000 78%,#0000 97%)
linear-gradient(#000,#0000 80%)
linear-gradient(#000,#0000 82%)
linear-gradient(#000,#0000 85%)
linear-gradient(#0000 22%,#000)
linear-gradient(#0000,#000 18% 82%,#0000)
linear-gradient(115deg,#000 55%,#0000)
linear-gradient(245deg,#000 55%,#0000)
linear-gradient(90deg,#0000,#000 10% 90%,#0000)
linear-gradient(90deg,#0000,#000 9% 91%,#0000)
radial-gradient(circle,#000 52%,#0000 72%)
radial-gradient(closest-side,#000,#0000)
```

### scroll — 1 valori distinti
```
smooth
```

### container — 1 valori distinti
```
inline-size
```

### Gradienti non banali — 14
```css
linear-gradient(#000 78%,#0000 97%)}.\[mask-image\:linear-gradient\(to_bottom\,transparent\,black_18\%\,black_82\%\,transparent\)
linear-gradient(#000,#0000 80%)}.\[mask-image\:linear-gradient\(to_bottom\,black\,transparent_82\%\)
linear-gradient(#000,#0000 82%)}.\[mask-image\:linear-gradient\(to_bottom\,black\,transparent_85\%\)
linear-gradient(#000,#0000 85%)}.\[mask-image\:linear-gradient\(to_bottom\,black_78\%\,transparent_97\%\)
linear-gradient(#0000 22%,#000)}.\[mask-image\:radial-gradient\(circle_at_center\,black_52\%\,transparent_72\%\)
linear-gradient(#0000,#000 18% 82%,#0000)}.\[mask-image\:linear-gradient\(to_right\,transparent\,black_9\%\,black_91\%\,transparent\)
linear-gradient(115deg,#000 55%,#0000)}.\[mask-image\:linear-gradient\(245deg\,black_55\%\,transparent\)
linear-gradient(245deg,#000 55%,#0000)}.\[mask-image\:linear-gradient\(to_bottom\,black\,transparent_80\%\)
linear-gradient(90deg,#0000,#000 10% 90%,#0000)}.\[mask-image\:linear-gradient\(to_top\,black\,transparent_78\%\)
linear-gradient(90deg,#0000,#000 9% 91%,#0000)}.\[mask-image\:linear-gradient\(to_right\,transparent\,black_10\%\,black_90\%\,transparent\)
linear-gradient(90deg,#f9f9f90b 1px,#0000 1px),linear-gradient(#f9f9f90b 1px,#0000 1px)
linear-gradient(var(--tw-gradient-stops))}.bg-dotfield{background-image:radial-gradient(circle,#f9f9f921 .5px,#0000 .5px)
radial-gradient(circle,#000 52%,#0000 72%)}.\[mask-image\:radial-gradient\(closest-side\,black\,transparent\)
radial-gradient(closest-side,#000,#0000)}.fill-current{fill:currentColor}.fill-primary{fill:var(--primary)
```

### Curve — 5
```
cubic-bezier(.16,1,.3,1)
cubic-bezier(.4, 0, .2, 1)
cubic-bezier(.4, 0, .6, 1)
cubic-bezier(.4,0,.2,1)
cubic-bezier(0, 0, .2, 1)
```

### Commenti dell'autore — 1 (**lo strato 4**)

- fonte: https://apsales.eu/assets/styles-CHG2jDaU.css

---

## `src/13-css2.css` — 14 KB

### @font-face — 39
```css
@font-face { font-family: 'DM Mono'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/dmmono/v16/aFTU7PB1QTsUX8KYthSQBLyM.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U }
@font-face { font-family: 'DM Mono'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/dmmono/v16/aFTU7PB1QTsUX8KYthqQBA.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02D }
@font-face { font-family: 'DM Mono'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/dmmono/v16/aFTR7PB1QTsUX8KYvumzEY2tbZX9.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02F }
@font-face { font-family: 'DM Mono'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/dmmono/v16/aFTR7PB1QTsUX8KYvumzEYOtbQ.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U }
@font-face { font-family: 'DM Sans'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/dmsans/v17/rP2Yp2ywxg089UriI5-g4vlH9VoD8Cmcqbu6-K6h9Q.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02 }
@font-face { font-family: 'DM Sans'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/dmsans/v17/rP2Yp2ywxg089UriI5-g4vlH9VoD8Cmcqbu0-K4.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02 }
@font-face { font-family: 'DM Sans'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/dmsans/v17/rP2Yp2ywxg089UriI5-g4vlH9VoD8Cmcqbu6-K6h9Q.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02 }
@font-face { font-family: 'DM Sans'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/dmsans/v17/rP2Yp2ywxg089UriI5-g4vlH9VoD8Cmcqbu0-K4.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02 }
@font-face { font-family: 'DM Sans'; font-style: normal; font-weight: 700; font-display: swap; src: url(https://fonts.gstatic.com/s/dmsans/v17/rP2Yp2ywxg089UriI5-g4vlH9VoD8Cmcqbu6-K6h9Q.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02 }
@font-face { font-family: 'DM Sans'; font-style: normal; font-weight: 700; font-display: swap; src: url(https://fonts.gstatic.com/s/dmsans/v17/rP2Yp2ywxg089UriI5-g4vlH9VoD8Cmcqbu0-K4.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02 }
```

### Commenti dell'autore — 20 (**lo strato 4**)

- fonte: https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&family=Inter:wght@400;500;600&family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400;500&display=swap
- latin-ext */ @font-face { font-family: 'DM Mono'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/dmmono/v16/aFTU7PB1QTsUX8KYthSQBLyM.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7
- latin-ext */ @font-face { font-family: 'DM Mono'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/dmmono/v16/aFTR7PB1QTsUX8KYvumzEY2tbZX9.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60
- latin-ext */ @font-face { font-family: 'DM Sans'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/dmsans/v17/rP2Yp2ywxg089UriI5-g4vlH9VoD8Cmcqbu6-K6h9Q.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, 
- latin-ext */ @font-face { font-family: 'DM Sans'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/dmsans/v17/rP2Yp2ywxg089UriI5-g4vlH9VoD8Cmcqbu6-K6h9Q.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, 
- latin-ext */ @font-face { font-family: 'DM Sans'; font-style: normal; font-weight: 700; font-display: swap; src: url(https://fonts.gstatic.com/s/dmsans/v17/rP2Yp2ywxg089UriI5-g4vlH9VoD8Cmcqbu6-K6h9Q.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, 
- cyrillic-ext */ @font-face { font-family: 'Inter'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa2JL7SUc.woff2) format('woff2'); unicode-range: U+0460-052F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F; } /* cyrillic
- greek-ext */ @font-face { font-family: 'Inter'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa2ZL7SUc.woff2) format('woff2'); unicode-range: U+1F00-1FFF; } /* greek
- vietnamese */ @font-face { font-family: 'Inter'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa2pL7SUc.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; } /* latin-ex
- latin */ @font-face { font-family: 'Inter'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; } /
- cyrillic */ @font-face { font-family: 'Inter'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa0ZL7SUc.woff2) format('woff2'); unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116; } /* greek-ext
- greek */ @font-face { font-family: 'Inter'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1pL7SUc.woff2) format('woff2'); unicode-range: U+0370-0377, U+037A-037F, U+0384-038A, U+038C, U+038E-03A1, U+03A3-03FF; } /* vietnamese
- latin-ext */ @font-face { font-family: 'Inter'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa25L7SUc.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113
- cyrillic-ext */ @font-face { font-family: 'Inter'; font-style: normal; font-weight: 600; font-display: swap; src: url(https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa2JL7SUc.woff2) format('woff2'); unicode-range: U+0460-052F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F; } /* cyrillic
- greek-ext */ @font-face { font-family: 'Inter'; font-style: normal; font-weight: 600; font-display: swap; src: url(https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa2ZL7SUc.woff2) format('woff2'); unicode-range: U+1F00-1FFF; } /* greek
- vietnamese */ @font-face { font-family: 'Inter'; font-style: normal; font-weight: 600; font-display: swap; src: url(https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa2pL7SUc.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; } /* latin-ex
- latin */ @font-face { font-family: 'Inter'; font-style: normal; font-weight: 600; font-display: swap; src: url(https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; } /
- vietnamese */ @font-face { font-family: 'Plus Jakarta Sans'; font-style: italic; font-weight: 200 800; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIuaomQNQcsA88c7O9yZ4KMCoOg4Koz4yGqhMva.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-
- latin */ @font-face { font-family: 'Plus Jakarta Sans'; font-style: italic; font-weight: 200 800; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIuaomQNQcsA88c7O9yZ4KMCoOg4Koz4y6qhA.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212,
- vietnamese */ @font-face { font-family: 'Plus Jakarta Sans'; font-style: normal; font-weight: 200 800; font-display: swap; src: url(https://fonts.gstatic.com/s/plusjakartasans/v12/LDIoaomQNQcsA88c7O9yZ4KMCoOg4Ko50yyygA.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1E
