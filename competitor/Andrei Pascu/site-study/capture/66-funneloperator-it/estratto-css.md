# Estratto CSS — 66-funneloperator-it

Solo cio' che insegna qualcosa: variabili, movimenti, effetti, gradienti, curve,
caratteri e **i commenti dell'autore**. Il resto e' utility generata e non si legge.

Generato da `scripts/analizza_css.py`.

---

## `src/38-styles-Cm6i-gBj.css` — 144 KB

### Variabili — 102

**Colore (59):**
```css
--background: oklch(100% 0 0);
--foreground: oklch(12.9% .042 264.695);
--card: oklch(100% 0 0);
--card-foreground: oklch(12.9% .042 264.695);
--popover: oklch(100% 0 0);
--popover-foreground: oklch(12.9% .042 264.695);
--primary: oklch(20.8% .042 265.755);
--primary-foreground: oklch(98.4% .003 247.858);
--secondary: oklch(96.8% .007 247.896);
--secondary-foreground: oklch(20.8% .042 265.755);
--muted: oklch(96.8% .007 247.896);
--muted-foreground: oklch(55.4% .046 257.417);
--accent: oklch(96.8% .007 247.896);
--accent-foreground: oklch(20.8% .042 265.755);
--destructive: oklch(57.7% .245 27.325);
--destructive-foreground: oklch(98.4% .003 247.858);
--border: oklch(92.9% .013 255.508);
--input: oklch(92.9% .013 255.508);
--chart-1: oklch(64.6% .222 41.116);
--chart-2: oklch(60% .118 184.704);
--chart-3: oklch(39.8% .07 227.392);
--chart-4: oklch(82.8% .189 84.429);
--chart-5: oklch(76.9% .188 70.08);
--fo-bg: oklch(17.8% 0 89.9);
--fo-surface: oklch(22% 0 89.9);
--fo-elevated: oklch(25.1% 0 89.9);
--fo-line: oklch(29.3% 0 89.9);
--fo-line-forte: oklch(39.1% 0 89.9);
--fo-text: oklch(93.4% 0 89.9);
--fo-muted: oklch(63.3% 0 89.9);
--fo-blue: oklch(65.6% .134 235.9);
--fo-blue-hover: oklch(54.6% .143 246.7);
--fo-blue-deep: oklch(45.9% .121 247.3);
--fo-blue-light: oklch(80.8% .09 238.3);
--fo-chiaro-fondo: oklch(94.6% 0 89.9);
--fo-chiaro-testo: oklch(17.8% 0 89.9);
--fo-chiaro-muto: oklch(47.3% 0 89.9);
--fo-chiaro-riga: oklch(87% 0 89.9);
--fo-chiaro-superficie: oklch(100% 0 89.9);
--fo-chiaro-verde: oklch(59.8% .199 143.2);
--fo-chiaro-blu: oklch(61% .14 240.1);
--fo-chiaro-riga-foto: oklch(80.6% 0 89.9);
--fo-chiaro-nero: oklch(0% 0 0);
--fo-chiaro-testo-alzato: oklch(22% 0 89.9);
--fo-chiaro-riga-scura: oklch(51.4% 0 89.9);
--fo-velo: oklch(17.8% 0 89.9/.72);
--fo-success-text: oklch(78% .15 155);
--fo-success-line: oklch(60% .13 155);
--fo-success-surface: oklch(24.5% .045 155);
--fo-warning-text: oklch(84% .145 85);
--fo-warning-line: oklch(66% .13 85);
--fo-warning-surface: oklch(25% .045 85);
--fo-error-text: oklch(72% .16 25);
--fo-error-line: oklch(58% .19 25);
--fo-error-surface: oklch(24.5% .06 25);
--fo-error-solid: oklch(52% .21 27);
--fo-error-solid-hover: oklch(46% .21 27);
--fo-info-surface: oklch(25% .05 240);
--sagoma-luce: oklch(28.8% 0 89.9);
```

**Misura, curva, tempo, carattere (43):**
```css
--radius: .5rem;
--ring: var(--fo-focus);
--sidebar: var(--fo-surface);
--sidebar-foreground: var(--fo-text);
--sidebar-primary: var(--fo-selected);
--sidebar-primary-foreground: var(--fo-text);
--sidebar-accent: var(--fo-elevated);
--sidebar-accent-foreground: var(--fo-text);
--sidebar-border: var(--fo-line);
--sidebar-ring: var(--fo-focus);
--spazio-blocchi: clamp(32px, 7.5vw, 48px);
--spazio-sezioni: clamp(40px, 10vw, 64px);
--spazio-vendita: clamp(56px, 15vw, 96px);
--spazio-area: clamp(64px, 17.5vw, 112px);
--scheda-dentro: 16px;
--scheda-riga: 8px;
--colonna: 832px;
--modulo: 400px;
--finestra: 520px;
--barra: 256px;
--margine-pagina: 24px;
--griglia-colonne: 12;
--griglia-colonna: 40px;
--griglia-canale: 32px;
--fo-action: var(--fo-blue);
--fo-action-hover: var(--fo-blue-light);
--fo-action-press: var(--fo-blue-hover);
--fo-on-action: var(--fo-bg);
--fo-link: var(--fo-blue);
--fo-link-hover: var(--fo-blue-light);
--fo-focus: var(--fo-blue-light);
--fo-selected: var(--fo-blue-deep);
--fo-info-text: var(--fo-blue-light);
--fo-info-line: var(--fo-blue-hover);
--spento-fondo: var(--fo-surface);
--spento-testo: var(--fo-muted);
--riga-passaggio: var(--fo-elevated);
--bottone-minimo: 7.5rem;
--piede-campo: 1.125rem;
--moto-stato: .12s;
--moto-comparsa: .16s;
--moto-momento: .32s;
--moto-battuta: 90ms;
```

### Movimenti — 13 @keyframes

```css
@keyframes fo-comparsa {0%{opacity:0;transform:translateY(4px)}}
@keyframes fo-momento {0%{opacity:0;transform:translateY(8px)}}
@keyframes fo-foglio-su {0%{transform:translateY(0)}10%{transform:translateY(-2.2px)}20%{transform:translateY(-4.1px)}30%{transform:translateY(-5.6px)}40%{transform:translateY(-6.6px)}50%{transform:translateY(-7px)}60%{transform:translateY(-6.9px)}70%{transform:translateY(-6.4px)}80%{transform:translateY(-5.8px)}90%{transform:translateY(-5.3px)}to{transform:translateY(-5px)}}
@keyframes fo-gira {to{transform:rotate(360deg)}}
@keyframes fo-luccichio {to{background-position:-200% 0}}
@keyframes fo-rail {0%{transform:translate(0)}to{transform:translate(-50%)}}
@keyframes fo-dissolvenza {0%{opacity:0}}
@keyframes pulse {50%{opacity:.5}}
@keyframes enter {0%{opacity:var(--tw-enter-opacity,1);transform:translate3d(var(--tw-enter-translate-x,0),var(--tw-enter-translate-y,0),0)scale3d(var(--tw-enter-scale,1),var(--tw-enter-scale,1),var(--tw-enter-scale,1))rotate(var(--tw-enter-rotate,0));filter:blur(var(--tw-enter-blur,0))}}
@keyframes exit {to{opacity:var(--tw-exit-opacity,1);transform:translate3d(var(--tw-exit-translate-x,0),var(--tw-exit-translate-y,0),0)scale3d(var(--tw-exit-scale,1),var(--tw-exit-scale,1),var(--tw-exit-scale,1))rotate(var(--tw-exit-rotate,0));filter:blur(var(--tw-exit-blur,0))}}
@keyframes accordion-down {0%{height:0}to{height:var(--radix-accordion-content-height,var(--bits-accordion-content-height,var(--reka-accordion-content-height,var(--kb-accordion-content-height,var(--ngp-accordion-content-height,auto)))))}}
@keyframes accordion-up {0%{height:var(--radix-accordion-content-height,var(--bits-accordion-content-height,var(--reka-accordion-content-height,var(--kb-accordion-content-height,var(--ngp-accordion-content-height,auto)))))}to{height:0}}
@keyframes caret-blink {0%,70%,to{opacity:1}20%,50%{opacity:0}}
```

### filtri — 3 valori distinti
```
blur(var(--tw-enter-blur,0))
blur(var(--tw-exit-blur,0))
var(--tw-blur,) var(--tw-brightness,) var(--tw-contrast,) var(--tw-grayscale,) var(--tw-hue-rotate,) var(--tw-invert,) var(--tw-saturate,) var(--tw-sepia,) var(--tw-drop-shadow,)
```

### blend — 7 valori distinti
```
color-dodge
darken
difference
exclusion
hard-light
lighten
screen
```

### clip/mask — 5 valori distinti
```
inset(50%)
linear-gradient(90deg,#0000,#000 13% 87%,#0000)
linear-gradient(90deg,#0000,#000 22% 78%,#0000)
linear-gradient(90deg,#0000,#000 28% 72%,#0000)
linear-gradient(90deg,#0000,#000 6% 94%,#0000)
```

### scroll — 1 valori distinti
```
smooth
```

### container — 1 valori distinti
```
inline-size
```

### Gradienti non banali — 10
```css
linear-gradient(#88c9f4 0%,#1e9cd7 33%,#0075be 66%,#005b97 100%)
linear-gradient(90deg, var(--fo-elevated) 0%, var(--sagoma-luce)
linear-gradient(90deg,#0000,#000 13% 87%,#0000)}.\[mask-image\:linear-gradient\(to_right\,transparent\,black_22\%\,black_78\%\,transparent\)
linear-gradient(90deg,#0000,#000 22% 78%,#0000)}.\[mask-image\:linear-gradient\(to_right\,transparent\,black_28\%\,black_72\%\,transparent\)
linear-gradient(90deg,#0000,#000 6% 94%,#0000)}.\[mask-image\:linear-gradient\(to_right\,transparent\,black_13\%\,black_87\%\,transparent\)
linear-gradient(90deg,#88c9f4 0%,#1e9cd7 33%,#0075be 66%,#005b97 100%)
linear-gradient(currentColor,currentColor)}.bg-\[url\(\'\/vendita\/offerta-roccia\.webp\'\)
linear-gradient(in lab, red, red)){.bg-linear-to-l{--tw-gradient-position:to left in oklab}}.bg-linear-to-l{background-image:linear-gradient(var(--tw-gradient-stops)
linear-gradient(in lab, red, red)){.bg-linear-to-r{--tw-gradient-position:to right in oklab}}.bg-linear-to-r{background-image:linear-gradient(var(--tw-gradient-stops)
linear-gradient(var(--tw-gradient-stops))}.bg-\[linear-gradient\(90deg\,\#88C9F4_0\%\,\#1E9CD7_33\%\,\#0075BE_66\%\,\#005B97_100\%\)
```

### Curve — 3
```
cubic-bezier(.2, 0, 0, 1)
cubic-bezier(.4, 0, .2, 1)
cubic-bezier(.4, 0, .6, 1)
```

### @font-face — 13
```css
@font-face { font-family:Curseyt;src:url(/caratteri/curseyt.woff2)format("woff2");font-weight:400;font-style:normal;font-display:block }
@font-face { font-family:DM Mono;font-style:normal;font-weight:400;font-display:swap;src:url(/caratteri/dm-mono-400-normal-latin-ext.woff2)format("woff2");unicode-range:U+100-2BA,U+2BD-2C5,U+2C7-2CC,U+2CE-2D7,U+2DD-2FF,U+304,U+308,U+329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF, }
@font-face { font-family:DM Mono;font-style:normal;font-weight:400;font-display:swap;src:url(/caratteri/dm-mono-400-normal-latin.woff2)format("woff2");unicode-range:U+??,U+131,U+152-153,U+2BB-2BC,U+2C6,U+2DA,U+2DC,U+304,U+308,U+329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U }
@font-face { font-family:DM Mono;font-style:normal;font-weight:500;font-display:swap;src:url(/caratteri/dm-mono-500-normal-latin-ext.woff2)format("woff2");unicode-range:U+100-2BA,U+2BD-2C5,U+2C7-2CC,U+2CE-2D7,U+2DD-2FF,U+304,U+308,U+329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF, }
@font-face { font-family:DM Mono;font-style:normal;font-weight:500;font-display:swap;src:url(/caratteri/dm-mono-500-normal-latin.woff2)format("woff2");unicode-range:U+??,U+131,U+152-153,U+2BB-2BC,U+2C6,U+2DA,U+2DC,U+304,U+308,U+329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U }
@font-face { font-family:Inter Tight;font-style:italic;font-weight:400 700;font-display:swap;src:url(/caratteri/inter-tight-400-700-italic-latin-ext.woff2)format("woff2");unicode-range:U+100-2BA,U+2BD-2C5,U+2C7-2CC,U+2CE-2D7,U+2DD-2FF,U+304,U+308,U+329,U+1D00-1DBF,U+1E00-1 }
@font-face { font-family:Inter Tight;font-style:italic;font-weight:400 700;font-display:swap;src:url(/caratteri/inter-tight-400-700-italic-latin.woff2)format("woff2");unicode-range:U+??,U+131,U+152-153,U+2BB-2BC,U+2C6,U+2DA,U+2DC,U+304,U+308,U+329,U+2000-206F,U+20AC,U+2122 }
@font-face { font-family:Inter Tight;font-style:normal;font-weight:400 700;font-display:swap;src:url(/caratteri/inter-tight-400-700-normal-latin-ext.woff2)format("woff2");unicode-range:U+100-2BA,U+2BD-2C5,U+2C7-2CC,U+2CE-2D7,U+2DD-2FF,U+304,U+308,U+329,U+1D00-1DBF,U+1E00-1 }
@font-face { font-family:Inter Tight;font-style:normal;font-weight:400 700;font-display:swap;src:url(/caratteri/inter-tight-400-700-normal-latin.woff2)format("woff2");unicode-range:U+??,U+131,U+152-153,U+2BB-2BC,U+2C6,U+2DA,U+2DC,U+304,U+308,U+329,U+2000-206F,U+20AC,U+2122 }
@font-face { font-family:Plus Jakarta Sans;font-style:italic;font-weight:200 800;font-display:swap;src:url(/caratteri/plus-jakarta-sans-200-800-italic-latin-ext.woff2)format("woff2");unicode-range:U+100-2BA,U+2BD-2C5,U+2C7-2CC,U+2CE-2D7,U+2DD-2FF,U+304,U+308,U+329,U+1D00-1 }
```

### Commenti dell'autore — 1 (**lo strato 4**)

- fonte: https://www.funneloperator.it/assets/styles-Cm6i-gBj.css
