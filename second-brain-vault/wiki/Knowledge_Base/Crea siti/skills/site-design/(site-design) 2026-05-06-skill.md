# SKILL
            
> Path: [[Map - Crea_Siti|Crea siti > skills > site-design]]

## Content

---
description: "Crea il sistema visivo completo del sito: filosofia estetica, palette colori, tipografia, spacing scale, componenti UI e atmosfera. Invoca frontend-design per le linee guida estetiche. Produce SITE-DESIGN.md (documentazione sistema di design), design-tokens.css (tutte le CSS custom properties) e style-guide.html (guida visiva autonoma apribile nel browser). Per Percorso B (Next.js) genera anche tailwind.config.js. Attiva su: /site design, crea sistema di design, genera palette colori sito, definisci tipografia progetto, design tokens CSS, style guide, visual system sito."
---

# Site Design — Sistema Visivo Completo

Sei il design director del progetto. Il tuo compito è costruire un **sistema di design coerente, distintivo e completamente documentato** che guiderà ogni scelta visiva del sito. Non palette generiche, non font di default: ogni progetto ha una sua identità visiva motivata dall'obiettivo e dal target.

---

## Prerequisiti

Prima di avviare, cerca e leggi nella CWD:

- `SITE-BRIEF.md` — **obbligatorio** (mood, colori, riferimenti estetici, tipo sito, target)
- `SITE-STACK.md` — **obbligatorio** (Percorso A/B/C determina il formato dei token)
- `SITE-PLAN.md` — se presente (per capire quanti componenti UI servono)
- `BRAND-VOICE.md` — opzionale (se presente, allinea la palette al tono del brand)

Se `SITE-BRIEF.md` non esiste: interrompi e comunica `"Esegui prima /site brief"`.
Se `SITE-STACK.md` non esiste: interrompi e comunica `"Esegui prima /site stack"`.

---

## Processo

### Step 1 — Leggi i Documenti di Input

Estrai da `SITE-BRIEF.md`:
- **Mood e atmosfera** richiesti (es. "professionale ma caldo", "tech minimalista", "lusso artigianale")
- **Colori di riferimento** eventualmente indicati dal cliente
- **Riferimenti estetici** (siti o brand citati come ispirazione)
- **Tipo di sito** (landing, agenzia, SaaS, portfolio, e-commerce, blog)
- **Target** (età, settore, livello di sofisticazione)

Da `SITE-STACK.md`:
- **Percorso A** → genera `design-tokens.css` come file CSS puro con custom properties
- **Percorso B** → genera `design-tokens.css` + `tailwind.config.js` con token integrati
- **Percorso C** → stessa logica del Percorso B, con eventuali adattamenti monorepo

---

### Step 2 — Filosofia Visiva

Definisci l'identità visiva con:

1. **Nome del movimento** — una frase che cattura l'essenza estetica (es. "Minimal Authority", "Organic Warmth", "Dark Precision", "Mediterranean Light", "Corporate Edge")
2. **3 principi visivi** che guidano ogni scelta successiva. Esempio:
   - *"Spazio come lusso"* — margini generosi comunicano sicurezza e qualità
   - *"Colore come segnale, non decorazione"* — ogni colore ha una funzione precisa
   - *"Tipografia che lavora"* — ogni testo ha un peso gerarchico chiaro

Documenta questo nella sezione iniziale di `SITE-DESIGN.md`.

---

### Step 3 — Palette Colori

Genera CSS custom properties complete. **Mai usare colori piatti senza varianti** — ogni primario ha la sua scala completa.

Struttura obbligatoria delle custom properties:

```css
/* === BRAND COLORS === */
--color-primary-50:  [valore];   /* tint più chiaro */
--color-primary-100: [valore];
--color-primary-200: [valore];
--color-primary-300: [valore];
--color-primary-400: [valore];
--color-primary-500: [valore];   /* colore base */
--color-primary-600: [valore];   /* hover */
--color-primary-700: [valore];   /* active / pressed */
--color-primary-800: [valore];
--color-primary-900: [valore];   /* shade più scuro */

--color-secondary-500: [valore];
--color-secondary-600: [valore];
--color-secondary-700: [valore];

--color-accent:      [valore];   /* colore di enfasi / CTA */

/* === SEMANTIC COLORS === */
--color-success:     [valore];
--color-success-bg:  [valore];
--color-warning:     [valore];
--color-warning-bg:  [valore];
--color-error:       [valore];
--color-error-bg:    [valore];

/* === SURFACE & BACKGROUND === */
--color-bg:          [valore];   /* sfondo principale */
--color-bg-secondary:[valore];   /* sfondo alternato sezioni */
--color-surface:     [valore];   /* card, modal, elevati */
--color-surface-alt: [valore];   /* superfici secondarie */

/* === TEXT === */
--color-text:        [valore];   /* testo primario */
--color-text-muted:  [valore];   /* testo secondario / label */
--color-text-faint:  [valore];   /* placeholder, note */
--color-text-inverse:[valore];   /* testo su sfondo scuro */

/* === BORDER === */
--color-border:      [valore];
--color-border-strong:[valore];
--color-border-focus:[valore];   /* anello focus accessibilità */
```

**Regola critica:** la palette deve essere motivata dal brief. Documenta il "perché" di ogni scelta cromatica in `SITE-DESIGN.md`.

---

### Step 4 — Tipografia

**Regola:** MAI usare Inter, Roboto o Arial come unico font display. Scegli font che costruiscono personalità.

Struttura di selezione:

| Ruolo | Fonte di scelta | Esempio |
|-------|----------------|---------|
| **Font Display** (headline H1–H3) | Google Fonts, variabile, carattere | Playfair Display, Syne, Clash Display, Cabinet Grotesk |
| **Font Body** (testo corrente) | Ottima leggibilità, 16–18px | Plus Jakarta Sans, DM Sans, Outfit, Source Serif 4 |
| **Font Mono** (solo SaaS/tech/code) | Chiarezza caratteri speciali | JetBrains Mono, Fira Code, IBM Plex Mono |

Genera la scala tipografica completa:

```css
/* === TYPOGRAPHY SCALE === */
--font-display: '[Font Display]', serif;
--font-body:    '[Font Body]', sans-serif;
--font-mono:    '[Font Mono]', monospace;     /* solo se SaaS/tech */

--text-xs:   0.75rem;    /* 12px — label, caption */
--text-sm:   0.875rem;   /* 14px — secondary text, badge */
--text-base: 1rem;       /* 16px — body default */
--text-lg:   1.125rem;   /* 18px — lead text, intro */
--text-xl:   1.25rem;    /* 20px — subheadline piccolo */
--text-2xl:  1.5rem;     /* 24px — H4 */
--text-3xl:  1.875rem;   /* 30px — H3 */
--text-4xl:  2.25rem;    /* 36px — H2 */
--text-5xl:  3rem;       /* 48px — H1 desktop */
--text-6xl:  3.75rem;    /* 60px — H1 hero large */

/* Line heights */
--leading-tight:  1.2;
--leading-snug:   1.35;
--leading-normal: 1.5;
--leading-relaxed:1.65;

/* Letter spacing */
--tracking-tight: -0.025em;
--tracking-normal: 0;
--tracking-wide:   0.025em;
--tracking-wider:  0.05em;
--tracking-widest: 0.1em;   /* caps label */
```

---

### Step 5 — Spacing, Layout e Breakpoints

```css
/* === SPACING SCALE (base 4px) === */
--space-1:  0.25rem;   /* 4px */
--space-2:  0.5rem;    /* 8px */
--space-3:  0.75rem;   /* 12px */
--space-4:  1rem;      /* 16px */
--space-5:  1.25rem;   /* 20px */
--space-6:  1.5rem;    /* 24px */
--space-8:  2rem;      /* 32px */
--space-10: 2.5rem;    /* 40px */
--space-12: 3rem;      /* 48px */
--space-16: 4rem;      /* 64px */
--space-20: 5rem;      /* 80px */
--space-24: 6rem;      /* 96px */
--space-32: 8rem;      /* 128px */

/* === LAYOUT === */
--container-sm:  640px;
--container-md:  768px;
--container-lg:  1024px;
--container-xl:  1280px;
--container-2xl: 1536px;
--container-max: 1200px;   /* max-width contenuto principale */
--container-px:  1.5rem;   /* padding laterale container */

/* === BORDER RADIUS === */
--radius-sm:   0.25rem;    /* 4px — input, badge */
--radius-md:   0.5rem;     /* 8px — card small */
--radius-lg:   0.75rem;    /* 12px — card standard */
--radius-xl:   1rem;       /* 16px — card large */
--radius-2xl:  1.5rem;     /* 24px — modale, panel */
--radius-full: 9999px;     /* pill — button, tag */

/* === SHADOWS === */
--shadow-sm:  0 1px 2px 0 rgb(0 0 0 / 0.05);
--shadow-md:  0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
--shadow-lg:  0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
--shadow-xl:  0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
--shadow-colored: 0 8px 30px -4px [color-primary-500-con-alpha]; /* colored shadow premium */
```

---

### Step 6 — Componenti Visual

Per ogni componente, specifica i **visual token** (non il CSS completo — quello va in build):

#### Button
| Variante | Background | Testo | Border | Hover |
|---------|-----------|-------|--------|-------|
| Primary | `--color-primary-600` | `--color-text-inverse` | nessuno | `--color-primary-700` |
| Secondary | `--color-surface` | `--color-primary-600` | `1px --color-primary-600` | `--color-primary-50` bg |
| Ghost | trasparente | `--color-text` | `1px --color-border` | `--color-bg-secondary` bg |
| Danger | `--color-error` | white | nessuno | `error` più scuro |

Sizes: `sm` (h:32px, px:12px, text-sm), `md` (h:40px, px:16px, text-base), `lg` (h:48px, px:24px, text-lg)

Stati: hover (150ms ease), focus (ring 2px `--color-border-focus`), disabled (opacity 0.5, cursor not-allowed)

#### Card
- Background: `--color-surface`
- Border: `1px solid --color-border`
- Border-radius: `--radius-lg`
- Shadow: `--shadow-md`
- Hover: `--shadow-lg` + `translateY(-2px)` (se cliccabile)
- Padding interno: `--space-6`

#### Badge / Tag
- Border-radius: `--radius-full`
- Padding: `--space-1` verticale, `--space-3` orizzontale
- Sizes: sm (`text-xs`), md (`text-sm`)
- Varianti colore: primary, secondary, success, warning, error, neutral

#### Form Input
- Height: 40px (md), 48px (lg)
- Border: `1px solid --color-border`
- Border-radius: `--radius-md`
- Focus: `border-color --color-border-focus` + ring 3px
- Error: `border-color --color-error`
- Background: `--color-bg`
- Placeholder: `--color-text-faint`

#### Divisori e Separatori
- `<hr>` standard: `1px solid --color-border`, opacity 60%
- Divisore sezione: `2px solid --color-primary-100` con gradient fade
- Spacing sezione: `--space-20` o `--space-24` tra sezioni principali

---

### Step 7 — Atmosfera e Effetti Premium

In base al mood estratto dal brief, specifica almeno 2-3 degli effetti seguenti:

**Gradient Mesh** (background organico):
```css
background: radial-gradient(ellipse at 20% 50%, [primary-100] 0%, transparent 60%),
            radial-gradient(ellipse at 80% 20%, [secondary-100] 0%, transparent 60%),
            radial-gradient(ellipse at 60% 80%, [accent-con-alpha] 0%, transparent 50%),
            [color-bg];
```

**Texture Noise** (profondità sottile):
```css
/* SVG noise filter inline — aggiunge texture organica */
background-image: url("data:image/svg+xml,...");
opacity: 0.03;   /* sempre subtle */
```

**Colored Shadows** (ombre di marca):
```css
box-shadow: 0 8px 30px -4px [color-primary-500-con-alpha-0.3];
```

**Hover Effect Premium** (card e button):
```css
transition: transform 150ms ease, box-shadow 150ms ease;
&:hover { transform: translateY(-3px); box-shadow: var(--shadow-xl); }
```

---

### Step 8 — Invoca `frontend-design`

Dopo aver definito il sistema visivo, invoca la skill `frontend-design` passando:
- La filosofia visiva e i 3 principi
- La palette colori selezionata (hex codes)
- La coppia tipografica scelta
- Il tipo di sito e il target

Usa il feedback di `frontend-design` per validare le scelte estetiche e affinare eventuali elementi deboli.

---

### Step 9 — Genera i File di Output

#### File 1: `SITE-DESIGN.md`

```markdown
# SITE-DESIGN.md — [Nome Progetto]

**Data:** [data]
**Stack:** [Percorso A/B/C]
**Basato su:** SITE-BRIEF.md

---

## Filosofia Visiva

**Movimento:** [Nome del movimento]

**3 Principi:**
1. [Principio 1] — [motivazione]
2. [Principio 2] — [motivazione]
3. [Principio 3] — [motivazione]

---

## Palette Colori

### Primario — [nome colore] ([hex base])
> Motivazione: [perché questo colore per questo progetto]

[tabella hex dei 10 step]

### Secondario — [nome] ([hex])
[descrizione uso]

### Accent — [hex]
[uso specifico: CTA, highlight, icone attive]

### Semantici
| Ruolo | Hex | Uso |
|-------|-----|-----|
| Success | | Form ok, conferme |
| Warning | | Alert, attenzione |
| Error | | Errori, campi invalidi |

### Surface & Text
[tabella completa con hex e uso]

---

## Tipografia

**Display:** [Font Name] — [motivazione]
**Body:** [Font Name] — [motivazione]
**Mono:** [Font Name] — [solo se presente]

**Import CDN:**
```html
<link href="https://fonts.googleapis.com/css2?family=..." rel="stylesheet">
```

[tabella scale tipografica con rem e uso]

---

## Spacing e Layout

[riepilogo scale principali]
**Container max-width:** [valore]
**Sezione padding verticale:** [valore]

---

## Componenti

[specifiche visual per ogni componente]

---

## Atmosfera e Effetti

[elenco effetti scelti con snippet CSS]

---

## File Generati

- `design-tokens.css` — tutte le CSS custom properties
- `style-guide.html` — guida visiva interattiva
[- `tailwind.config.js` — solo Percorso B/C]

---

*Generato da /site design — Digital Empire Site Creation System*
```

#### File 2: `design-tokens.css`

File CSS puro con **tutte** le custom properties definite negli step 3–6. Struttura con commenti sezione. Inizia con `:root { }`. Zero magic numbers — ogni valore ha una variabile.

```css
/* ==============================================
   DESIGN TOKENS — [Nome Progetto]
   Generato da /site design
   Digital Empire Site Creation System
   ============================================== */

:root {

  /* === BRAND COLORS === */
  /* Primario: [nome colore] — [motivazione] */
  --color-primary-50:  #...;
  /* ... tutti i token ... */

}
```

#### File 3: `style-guide.html`

Pagina HTML **autonoma** (nessuna dipendenza locale oltre ai font CDN) che mostra:

1. **Header** — nome progetto, data, stack
2. **Palette** — swatches per ogni colore con nome CSS var + hex + uso
3. **Tipografia** — ogni dimensione della scala con testo di esempio
4. **Spacing** — blocchi visuali della scale
5. **Componenti** — button (tutte le varianti e stati), card esempio, badge, input
6. **Atmosfera** — preview effetti gradient mesh, hover effects

Il file deve:
- Importare i font da Google Fonts CDN
- Includere `<style>` inline con i design tokens (copia di `design-tokens.css`)
- Funzionare aprendo il file direttamente nel browser
- Essere visivamente impressionante — è la "vetrina" del sistema di design

#### File 4: `tailwind.config.js` (solo Percorso B/C)

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50:  'var(--color-primary-50)',
          /* ... tutti gli step ... */
          900: 'var(--color-primary-900)',
        },
        secondary: { /* ... */ },
        accent:    'var(--color-accent)',
        success:   'var(--color-success)',
        warning:   'var(--color-warning)',
        error:     'var(--color-error)',
        surface:   'var(--color-surface)',
        border:    'var(--color-border)',
      },
      fontFamily: {
        display: ['[Font Display]', 'serif'],
        body:    ['[Font Body]', 'sans-serif'],
        mono:    ['[Font Mono]', 'monospace'],
      },
      fontSize: {
        'xs':   ['var(--text-xs)',   { lineHeight: 'var(--leading-normal)' }],
        'sm':   ['var(--text-sm)',   { lineHeight: 'var(--leading-normal)' }],
        'base': ['var(--text-base)', { lineHeight: 'var(--leading-relaxed)' }],
        /* ... tutta la scala ... */
      },
      spacing: {
        '1':  'var(--space-1)',
        '2':  'var(--space-2)',
        /* ... tutta la scala ... */
      },
      borderRadius: {
        'sm':   'var(--radius-sm)',
        'md':   'var(--radius-md)',
        'lg':   'var(--radius-lg)',
        'xl':   'var(--radius-xl)',
        '2xl':  'var(--radius-2xl)',
        'full': 'var(--radius-full)',
      },
      boxShadow: {
        'sm':      'var(--shadow-sm)',
        'md':      'var(--shadow-md)',
        'lg':      'var(--shadow-lg)',
        'xl':      'var(--shadow-xl)',
        'colored': 'var(--shadow-colored)',
      },
      maxWidth: {
        'container': 'var(--container-max)',
      },
    },
  },
  plugins: [],
}
```

---

### Step 10 — Aggiorna `SITE-STATUS.md`

Se esiste un file `SITE-STATUS.md` nella CWD, aggiorna la riga di `site-design` come completato. Indica il prossimo passo: `/site copy` (se non già fatto) o `/site build`.

---

## Regole Critiche

- **Mai palette generica** — ogni progetto ha colori distinti e motivati dal brief. Se il cliente non specifica colori, derivali dal settore + target + mood.
- **`style-guide.html` deve essere autonomo** — nessuna dipendenza locale tranne font CDN. Deve aprirsi nel browser con doppio click.
- **CSS custom properties sono la fonte di verità** — tutto il CSS successivo (in build) usa solo `var(--token)`, zero magic numbers.
- **La motivazione conta** — documenta sempre il "perché" di ogni scelta visiva in `SITE-DESIGN.md`. Il cliente deve capire il ragionamento.
- **Coerenza sistema > bellezza singolo elemento** — un componente mediocre che si integra bene vale più di un componente brillante che rompe il sistema.
- **Mobile-first nei token** — i valori base dei token sono pensati per mobile; usa i breakpoints per scalare verso desktop.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Crea_Siti|Crea Siti Area]]
- [[Map - Saas|Saas Area]]
