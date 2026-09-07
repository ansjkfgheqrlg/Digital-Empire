# Estratto CSS — 12-claude-speedrun-v2

Solo cio' che insegna qualcosa: variabili, movimenti, effetti, gradienti, curve,
caratteri e **i commenti dell'autore**. Il resto e' utility generata e non si legge.

Generato da `scripts/analizza_css.py`.

---

## `src/37-player.css` — 232 KB

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

## `src/31-index-Cxg4z3Qv.css` — 94 KB

### Variabili — 34

**Misura, curva, tempo, carattere (34):**
```css
--background: 0 0% 7.5%;
--foreground: 0 0% 97.6%;
--card: 0 0% 10%;
--card-foreground: 0 0% 97.6%;
--popover: 0 0% 10%;
--popover-foreground: 0 0% 97.6%;
--primary: 16 97% 50%;
--primary-foreground: 0 0% 100%;
--secondary: 0 0% 15%;
--secondary-foreground: 0 0% 97.6%;
--muted: 0 0% 15%;
--muted-foreground: 0 0% 93.3%;
--muted-foreground-dim: 0 0% 55%;
--accent: 16 97% 50%;
--accent-foreground: 0 0% 100%;
--destructive: 0 84.2% 60.2%;
--destructive-foreground: 0 0% 100%;
--border: 0 0% 20%;
--input: 0 0% 20%;
--ring: 16 97% 50%;
--radius: .75rem;
--sidebar-background: 0 0% 7.5%;
--sidebar-foreground: 0 0% 97.6%;
--sidebar-primary: 16 97% 50%;
--sidebar-primary-foreground: 0 0% 100%;
--sidebar-accent: 0 0% 15%;
--sidebar-accent-foreground: 0 0% 97.6%;
--sidebar-border: 0 0% 20%;
--sidebar-ring: 16 97% 50%;
--brand-orange: 16 97% 50%;
--brand-black: 0 0% 7.5%;
--brand-dark-grey: 240 2% 23%;
--brand-grey: 0 0% 97.6%;
--brand-white: 0 0% 97.6%;
```

### Movimenti — 9 @keyframes

```css
@keyframes bounce {0%,to{transform:translateY(-25%);animation-timing-function:cubic-bezier(.8,0,1,1)}50%{transform:none;animation-timing-function:cubic-bezier(0,0,.2,1)}}
@keyframes pulse {50%{opacity:.5}}
@keyframes subtle-vibrate {0%,to{transform:rotate(0)}25%{transform:rotate(-2deg)}75%{transform:rotate(2deg)}}
@keyframes enter {0%{opacity:var(--tw-enter-opacity, 1);transform:translate3d(var(--tw-enter-translate-x, 0),var(--tw-enter-translate-y, 0),0) scale3d(var(--tw-enter-scale, 1),var(--tw-enter-scale, 1),var(--tw-enter-scale, 1)) rotate(var(--tw-enter-rotate, 0))}}
@keyframes exit {to{opacity:var(--tw-exit-opacity, 1);transform:translate3d(var(--tw-exit-translate-x, 0),var(--tw-exit-translate-y, 0),0) scale3d(var(--tw-exit-scale, 1),var(--tw-exit-scale, 1),var(--tw-exit-scale, 1)) rotate(var(--tw-exit-rotate, 0))}}
@keyframes highlighter-reveal {0%{background-size:0% 100%}to{background-size:100% 100%}}
@keyframes marquee-scroll {0%{transform:translate(0)}to{transform:translate(-50%)}}
@keyframes accordion-up {0%{height:var(--radix-accordion-content-height)}to{height:0}}
@keyframes accordion-down {0%{height:0}to{height:var(--radix-accordion-content-height)}}
```

### filtri — 1 valori distinti
```
var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)
```

### Gradienti non banali — 3
```css
linear-gradient(to bottom,var(--tw-gradient-stops))}.bg-gradient-to-t{background-image:linear-gradient(to top,var(--tw-gradient-stops)
linear-gradient(to right,hsl(var(--brand-orange) / 1),hsl(var(--brand-orange)
linear-gradient(to top right,var(--tw-gradient-stops))}.from-background{--tw-gradient-from: hsl(var(--background)
```

### Curve — 5
```
cubic-bezier(.22,1,.36,1)
cubic-bezier(.4,0,.2,1)
cubic-bezier(.4,0,.6,1)
cubic-bezier(.8,0,1,1)
cubic-bezier(0,0,.2,1)
```

### Commenti dell'autore — 1 (**lo strato 4**)

- fonte: https://claude-speedrun.com/assets/index-Cxg4z3Qv.css

---

## `src/40-css2.css` — 36 KB

### @font-face — 56
```css
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 100; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmS-HY6EQ.woff2) format('woff2'); unicode-range: U+0460-052F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 100; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmb-HY6EQ.woff2) format('woff2'); unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116; }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 100; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xnj-HY6EQ.woff2) format('woff2'); unicode-range: U+0302-0303, U+0305, U+0307-0308, U+0310, U+0312, U+0315, U+031A, U+032 }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 100; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xnx-HY6EQ.woff2) format('woff2'); unicode-range: U+0001-000C, U+000E-001F, U+007F-009F, U+20DD-20E0, U+20E2-20E4, U+2150 }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 100; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmQ-HY6EQ.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 100; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmR-HY6EQ.woff2) format('woff2'); unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304 }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 100; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmf-HY.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0 }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 200; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmS-HY6EQ.woff2) format('woff2'); unicode-range: U+0460-052F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 200; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmb-HY6EQ.woff2) format('woff2'); unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116; }
@font-face { font-family: 'Onest'; font-style: normal; font-weight: 200; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xnj-HY6EQ.woff2) format('woff2'); unicode-range: U+0302-0303, U+0305, U+0307-0308, U+0310, U+0312, U+0315, U+031A, U+032 }
```

### Commenti dell'autore — 24 (**lo strato 4**)

- fonte: https://fonts.googleapis.com/css2?family=Onest:wght@100;200;400;500;600;700;800;900&display=swap
- cyrillic-ext */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 100; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmS-HY6EQ.woff2) format('woff2'); unicode-range: U+0460-052F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F; } /* cyrillic
- vietnamese */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 100; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmQ-HY6EQ.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; } /* latin-ext
- latin */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 100; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmf-HY.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; } /* cyrillic-ext
- cyrillic */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 200; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmb-HY6EQ.woff2) format('woff2'); unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116; } /* math
- vietnamese */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 200; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmQ-HY6EQ.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; } /* latin-ext
- latin */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 200; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmf-HY.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; } /* cyrillic-ext
- cyrillic */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmb-HY6EQ.woff2) format('woff2'); unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116; } /* math
- vietnamese */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmQ-HY6EQ.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; } /* latin-ext
- latin */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 400; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmf-HY.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; } /* cyrillic-ext
- cyrillic */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmb-HY6EQ.woff2) format('woff2'); unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116; } /* math
- vietnamese */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmQ-HY6EQ.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; } /* latin-ext
- latin */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 500; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmf-HY.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; } /* cyrillic-ext
- cyrillic */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 600; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmb-HY6EQ.woff2) format('woff2'); unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116; } /* math
- vietnamese */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 600; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmQ-HY6EQ.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; } /* latin-ext
- latin */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 600; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmf-HY.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; } /* cyrillic-ext
- cyrillic */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 700; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmb-HY6EQ.woff2) format('woff2'); unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116; } /* math
- vietnamese */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 700; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmQ-HY6EQ.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; } /* latin-ext
- latin */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 700; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmf-HY.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; } /* cyrillic-ext
- cyrillic */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 800; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmb-HY6EQ.woff2) format('woff2'); unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116; } /* math
- vietnamese */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 800; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmQ-HY6EQ.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; } /* latin-ext
- latin */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 800; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmf-HY.woff2) format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; } /* cyrillic-ext
- cyrillic */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 900; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmb-HY6EQ.woff2) format('woff2'); unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116; } /* math
- vietnamese */ @font-face { font-family: 'Onest'; font-style: normal; font-weight: 900; font-display: swap; src: url(https://fonts.gstatic.com/s/onest/v11/gNMKW3F-SZuj7xmQ-HY6EQ.woff2) format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; } /* latin-ext
