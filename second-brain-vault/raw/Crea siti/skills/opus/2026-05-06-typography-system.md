# TYPOGRAPHY-SYSTEM

> Source: File system (`Crea siti\skills\opus\TYPOGRAPHY-SYSTEM.md`)
> Collected: 2026-05-06
> Published: Unknown

# TYPOGRAPHY SYSTEM — OPUS Premium Type Architecture
> Fasi 5 e 5A del processo OPUS. Il sistema tipografico completo con Bold Word System.
> La tipografia è il 60% del design. Tutto il resto è dettaglio.

---

## Filosofia Tipografica OPUS

La tipografia premium non è semplicemente scegliere un bel font. È costruire un **sistema** dove ogni livello della gerarchia ha dimensione, peso, spaziatura e case deliberatamente calcolati per creare un ritmo visivo percepibile.

**Tre principi fondativi:**
1. **Gerarchia cristallina** — 5 livelli visivamente distinti a qualsiasi zoom
2. **Tensione tipografica** — la coppia font crea tensione interessante (non armonia banale)
3. **Il testo è architettura** — prima di leggere una parola, l'occhio vede struttura

---

## FONT SELECTION GUIDE

### Categoria per Aesthetic Axis

| Aesthetic Axis | Font Display (heading) | Font Body (paragrafi) |
|----------------|------------------------|----------------------|
| Luxury editoriale | Cormorant Garamond, Playfair Display, DM Serif Display | DM Sans, Satoshi |
| Minimalismo organico | Fraunces, Lora | Cabinet Grotesk, Outfit |
| Modern premium | Satoshi, Cabinet Grotesk | DM Sans, Plus Jakarta Sans |
| Tech / SaaS | Space Grotesk, Geist | Plus Jakarta Sans, Sora |
| Avant-garde | Neue Haas Grotesk, Aktiv Grotesk | DM Sans, Epilogue |
| Editorial bold | Barlow Condensed, Oswald | DM Sans, Satoshi |
| Retro-futurismo | Syne, Space Grotesk | Cabinet Grotesk |
| Art deco geometrico | Cormorant, DM Serif Display | Satoshi, Outfit |

### Regola della Coppia Tipografica

**SEMPRE 2 font families (eccezionalmente 3 con mono per tech):**

```
PATTERN 1 — Serif Display + Sans Body (più sicuro, sempre premium)
Esempio: Cormorant Garamond (display) + DM Sans (body)
Tensione: eleganza classica vs modernità pulita

PATTERN 2 — Sans Display + Serif Body (più insolito, quando si osa)
Esempio: Satoshi (display) + Lora (body)
Tensione: contemporaneità vs calore letterario

PATTERN 3 — Sans Display + Sans Body (modern premium)
Esempio: Cabinet Grotesk (display) + DM Sans (body)
Tensione: personalità forte vs neutralità funzionale

PATTERN 4 — Condensed Display + Regular Body (editorial)
Esempio: Barlow Condensed (display) + Plus Jakarta Sans (body)
Tensione: impatto visivo vs leggibilità
```

### Font APPROVATI (carattere, non generici)

**Sans-serif con personalità:**
- Satoshi — geometric, carattere moderno preciso
- Cabinet Grotesk — organic curves, premium feel
- DM Sans — pulito, leggermente distintivo
- Plus Jakarta Sans — versatile, tech-friendly
- Space Grotesk — angular, tech personality
- Outfit — friendly premium
- Sora — rounded, approachable luxury
- Epilogue — editorial, strong personality

**Serif/Display con carattere:**
- Cormorant Garamond — ultra-luxury, fashion
- Playfair Display — editorial luxury
- DM Serif Display — modern serif, impactful
- Fraunces — organic, warm optical serif
- Lora — readable, warm
- Libre Baskerville — classic, authoritative

**Mono (solo SaaS/tech):**
- Geist Mono
- JetBrains Mono
- Fira Code

### Font VIETATI come font principale
- **Inter** — il segnale più forte di "AI-generated, generic SaaS"
- **Roboto** — Google-default, zero personalità
- **Arial** — sistema default, invisibile
- **Helvetica** — troppo neutro senza contesto forte
- **system-ui** — fallback del sistema, non un font di design

---

## TYPE SCALE — Perfect Fourth (ratio 1.333)

La scala è basata su un rapporto matematico preciso. Questo crea armonia subliminale percepita dall'occhio senza che il visitatore sappia perché il layout "sembra giusto".

```css
/* design-tokens.css — Type Scale */
--text-xs:   0.75rem;   /* 12px — metadata, caption, footer note */
--text-sm:   0.875rem;  /* 14px — secondary body, form label */
--text-base: 1rem;      /* 16px — body principale */
--text-lg:   1.333rem;  /* 21px — lead paragraph, intro text */
--text-xl:   1.777rem;  /* 28px — H3, card heading */
--text-2xl:  2.369rem;  /* 38px — H2, section heading */
--text-3xl:  3.157rem;  /* 50px — H1 standard */
--text-4xl:  4.209rem;  /* 67px — H1 grande / display */
--text-5xl:  5.61rem;   /* 90px — hero display (desktop) */
```

### Fluid Typography — clamp() per ogni livello

MAI cambiare font-size solo ai breakpoint. Usa clamp() per scaling fluido:

```css
/* Fluid scale obbligatoria */
.text-hero   { font-size: clamp(3rem, 8vw + 1rem, 5.625rem); }
.text-h1     { font-size: clamp(2.5rem, 5vw + 1rem, 5.625rem); }
.text-h2     { font-size: clamp(1.75rem, 3vw + 0.5rem, 3rem); }
.text-h3     { font-size: clamp(1.25rem, 2vw + 0.25rem, 1.75rem); }
.text-body   { font-size: clamp(1rem, 0.5vw + 0.875rem, 1.125rem); }
```

---

## LINE HEIGHT — 4px Baseline Grid

```css
/* design-tokens.css — Line Heights */
--leading-none:    1.0;  /* display/hero tight — premium look */
--leading-tight:   1.1;  /* H1-H2 headings */
--leading-snug:    1.2;  /* H2 larger */
--leading-normal:  1.35; /* subheadings */
--leading-relaxed: 1.6;  /* body minimum — mai scendere sotto */
--leading-loose:   1.7;  /* body premium — ideale per lettura comfort */
--leading-caption: 1.45; /* small/caption */
```

**Regola baseline grid:**
line-height × font-size = numero divisibile per 4
- 16px × 1.5 = 24px ✅
- 16px × 1.75 = 28px ✅
- 16px × 1.45 = 23.2px ❌ → usa 1.5

---

## LETTER-SPACING — Regole di Raffinatezza

```css
/* design-tokens.css — Letter Spacing */
--tracking-tightest: -0.04em; /* hero display ultra-large (≥90px) */
--tracking-tighter:  -0.02em; /* hero (67-90px) */
--tracking-tight:    -0.01em; /* H1-H2 (38-67px) */
--tracking-normal:    0em;    /* H3 (28px) — neutro */
--tracking-body:     +0.01em; /* body (lieve apertura → leggibilità) */
--tracking-wide:     +0.05em; /* H3 minuscolo */
--tracking-wider:    +0.12em; /* label/tag uppercase */
--tracking-widest:   +0.20em; /* nav items uppercase — premium navigation */
```

**Regole di applicazione:**
- Al crescere della dimensione → tracking più **negativo** (lusso, condensed)
- Al decrescere o UPPERCASE → tracking più **positivo** (leggibilità, eleganza)
- NAV ITEMS: sempre 0.15-0.20em — definisce navigazione premium
- HERO: sempre tracking negativo — il display senza tracking sembra amatoriale

---

## FONT WEIGHT STRATEGY

```css
/* design-tokens.css — Font Weights */
--weight-thin:       100;
--weight-extralight: 200;
--weight-light:      300; /* display luxury/fashion */
--weight-regular:    400; /* body, H2 section heading */
--weight-medium:     500; /* subheadings, H3 */
--weight-semibold:   600; /* bold words in body, H3 enfatico */
--weight-bold:       700; /* solo CTA, headline breve, accent */
--weight-extrabold:  800; /* rarissimo — uso editoriale intenzionale */
--weight-black:      900; /* quasi mai — solo display specifici */
```

**Strategia per aesthetic axis:**

| Aesthetic | Display Weight | Body Weight |
|-----------|---------------|-------------|
| Luxury/fashion | 300 (light) | 400 (regular) |
| Modern premium | 400-500 (regular-medium) | 400 |
| Editorial bold | 600-700 (semibold-bold) | 400 |
| Tech/SaaS | 500-600 | 400 |

**Regola:** MAI heavy (800-900) come stile dominante → segnala commercialismo.
Il weight leggero su display grande = paradossalmente più impattante.

---

## VISUAL HIERARCHY — 5 Livelli Obbligatori

Deve essere **LEGGIBILE AL 20% DI ZOOM**. Ogni livello ha size + weight + color + case distinti.

```
LIVELLO 1 — DISPLAY (hero):
  font-size:      clamp(3rem, 8vw + 1rem, 5.625rem)
  font-weight:    300-400 (light/regular per serif)
  line-height:    1.0-1.1
  letter-spacing: -0.02em a -0.04em
  color:          var(--color-text) [pieno]
  text-transform: lowercase (sentence case)

LIVELLO 2 — HEADING (sezioni):
  font-size:      clamp(1.75rem, 3vw + 0.5rem, 3rem)
  font-weight:    400 (regular) — leggerezza = eleganza
  line-height:    1.1-1.2
  letter-spacing: -0.01em
  color:          var(--color-text) [pieno]
  text-transform: lowercase (sentence case)

LIVELLO 3 — SUBHEAD / H3:
  font-size:      clamp(1.25rem, 2vw + 0.25rem, 1.75rem)
  font-weight:    500-600 (medium/semibold)
  line-height:    1.3-1.4
  letter-spacing: 0em (neutro)
  color:          var(--color-text) [pieno o leggermente muted]

LIVELLO 4 — BODY:
  font-size:      clamp(1rem, 0.5vw + 0.875rem, 1.125rem)
  font-weight:    400 (regular)
  line-height:    1.6-1.7
  letter-spacing: +0.01em
  color:          var(--color-text)
  max-width:      68ch (regola di leggibilità)

LIVELLO 5 — CAPTION/LABEL:
  font-size:      0.75-0.875rem (12-14px)
  font-weight:    500-600
  line-height:    1.4-1.5
  letter-spacing: +0.12em a +0.20em
  text-transform: UPPERCASE
  color:          var(--color-text-muted)
```

**Contrasto estremo tra Livello 1 e Livello 5:**
- Size: 5.625rem vs 0.75rem = 7.5x
- Weight: 300 vs 500-600 = inversione (display più leggero di label)
- Case: minuscolo vs UPPERCASE
- Color: pieno vs muted
Questa combinazione produce la gerarchia percepita come "pubblicazione premium".

---

## BOLD WORD SYSTEM — Eleganza Editoriale nel Corpo del Testo

Il Bold Word System trasforma blocchi di testo ordinari in elementi visivi dinamici che guidano la lettura e segnalano qualità editoriale. È la differenza tra "testo" e "architettura di testo".

### Regola Base

**1-3 parole in grassetto per frase. MAI di più.**

### Quali Parole Boldare

**DA BOLDARE ✅**
- Sostantivi chiave che portano il messaggio principale
- Verbi d'azione forti: *ottieni*, *crei*, *trasforma*, *lancia*, *costruisci*
- Numeri e dati: *3x*, *48 ore*, *100%*, *€12.000*
- Benefici specifici (non le feature, il **beneficio**)
- Nomi propri di brand o prodotti rilevanti

**MAI BOLDARE ❌**
- Aggettivi generici: "veloce", "facile", "ottimo", "incredibile"
- Articoli, preposizioni, congiunzioni: "il", "di", "e", "ma"
- Intere frasi o più di 3 parole consecutive — distrugge il sistema
- Parole che non aggiungono enfasi semantica

### Skeleton Test (OBBLIGATORIO)

Prima di approvare il body copy:

> **Leggi SOLO le parole in grassetto**. Formano un messaggio comprensibile?

Se sì → il Bold Word System è corretto.
Se no → cambia le parole boldate.

**Esempio corretto:**
> Il metodo che ha **trasformato** il modo in cui **3.000 professionisti** costruiscono il loro business online. Non un corso generico — un **sistema** testato con **risultati misurabili**.

*Skeleton: "trasformato" → "3.000 professionisti" → "sistema" → "risultati misurabili"*
*Il messaggio si capisce? Sì. ✅*

### Stile Visivo del Bold

```css
/* Nel body text */
strong, b {
  font-weight: 600; /* semibold — MAI 700 o 800 nei paragrafi corpo */
  /* Il semibold è elegante; il bold pieno è "urlato" */
}

/* Solo per headline brevi o CTA */
.headline-bold {
  font-weight: 700;
}
```

**Perché 600 e non 700:**
- 600 crea contrasto visivo sufficiente
- 700 nei paragrafi crea dissonanza — "rumore" invece di "enfasi"
- L'eleganza editoriale usa il contrasto minimo necessario

### Densità del Bold Word System

**Formula:** ~1 parola boldata ogni 15-20 parole di corpo

| Lunghezza paragrafo | Parole in grassetto |
|--------------------|---------------------|
| 30 parole | 1-2 |
| 60 parole | 3-4 |
| 90 parole | 4-5 |

**Ritmo non uniforme (obbligatorio):**
- Alcune frasi SENZA grassetto = "respiro"
- Alcune frasi CON 2-3 parole = "picco di enfasi"
- Il ritmo varia: intro (meno bold) → benefici (più bold) → CTA (massimo bold)

### Dove Applicare il Bold Word System

**APPLICARE ✅**
- Sezione features/benefits — ogni bullet o paragrafo
- Sezione about/story — punti emotivi chiave
- Paragrafi introduttivi delle sezioni
- How It Works — ogni step
- Pricing — descrizione dei piani

**NON APPLICARE ❌**
- Hero headline (troppo breve — inutile)
- CTA buttons (già enfatizzati dal contesto)
- Testimonial (rompe l'autenticità della voce del cliente)
- Footer, nav, label (non sono corpo narrativo)

---

## LOWERCASE / CASE STYLE

### Regola Principale

**H1, H2, H3 → sentence case (minuscolo)**

```
✅ CORRETTO: "il metodo che ha cambiato tutto"
✅ CORRETTO: "perché 3.000 professionisti scelgono questo sistema"
❌ SBAGLIATO: "Il Metodo Che Ha Cambiato Tutto" (Title Case — troppo corporate)
❌ SBAGLIATO: "IL METODO CHE HA CAMBIATO TUTTO" (ALL CAPS — aggressivo)
```

**Perché lowercase:**
- Usato da: Supreme, Acne Studios, arte contemporanea, media indie, brand lusso moderni
- Comunica: autenticità, personalità, rifiuto del corporate, modernità
- Crea contrasto forte con label/nav in UPPERCASE — gerarchia visiva più ricca

**Eccezioni al lowercase:**
- Nomi propri: "Marco Rossi", "Milano", "Apple"
- Acronimi: "SEO", "CTA", "AI", "GDPR"
- Brand name: rispetta le maiuscole del brand

### Quando NON usare lowercase
- Siti istituzionali/corporate per clienti agenzia → Title Case standard
- Professionisti formali (avvocati, medici, finanza) → Sentence Case normale
- **opus-director chiede in Phase 0 Discovery** — non decidere senza aver capito il tono del brand

### UPPERCASE: Solo per Label e Metadata

```css
/* Label / nav / tag / caption */
.label, .nav-item, .tag, .caption {
  text-transform: uppercase;
  letter-spacing: var(--tracking-wider); /* +0.15em a +0.20em */
  font-size: var(--text-xs); /* 12px o 14px */
  font-weight: 500;
  color: var(--color-text-muted);
}
```

---

## PARAGRAFO PERFETTO — Struttura Visiva

### Larghezza del Paragrafo

```css
/* REGOLA CRITICA — applicare sempre al container del testo */
.body-text, p, .prose {
  max-width: 68ch; /* 68 caratteri per riga — ottima leggibilità */
  /* NON applicare all'intera sezione — solo al container del testo */
}
```

**Perché 68ch:**
- Sotto 45ch → righe troppo corte, eye-track discontinuo
- Sopra 75ch → difficoltà nel trovare la riga successiva
- 55-68ch → zona ottimale per lettura comfort

### Spaziatura tra Paragrafi

```css
p {
  margin-bottom: var(--space-5); /* 24px tra paragrafi normali */
}

.section-text p:last-child {
  margin-bottom: 0;
}

/* Sezioni di testo importanti */
.major-text-block p {
  margin-bottom: var(--space-6); /* 32px per testi lunghi */
}
```

**MAI:** margin-bottom uguale a line-height (troppo compresso)

### Paragrafo Lunghezza

- Desktop: max 3-4 righe (50-70 parole)
- Paragrafi più lunghi → dividere in 2 paragrafi con linea bianca visibile
- Single-sentence paragraphs: usare per enfasi (stile copywriting diretto)

---

## TIPOGRAFIA SPECIALE — Numeri e Statistiche

```css
/* Stat number — trattamento speciale premium */
.stat-number {
  font-size: clamp(3rem, 6vw, 5rem); /* molto grande */
  font-weight: 300; /* light — paradossalmente elegante */
  letter-spacing: -0.02em;
  line-height: 1.0;
  color: var(--color-accent); /* silver-mixed accent */
}

.stat-label {
  font-size: var(--text-xs);
  text-transform: uppercase;
  letter-spacing: var(--tracking-wider);
  color: var(--color-text-muted);
  margin-top: var(--space-2);
}
```

**Esempio HTML:**
```html
<div class="stat">
  <span class="stat-number">3.247</span>
  <span class="stat-label">clienti soddisfatti</span>
</div>
```

---

## TIPOGRAFIA SPECIALE — Quote e Testimonial

```css
.testimonial-text {
  font-size: var(--text-xl); /* 28px */
  font-style: italic;
  font-weight: 300; /* light — eleganza editoriale */
  line-height: var(--leading-relaxed);
  color: var(--color-text);
  border-left: 3px solid var(--color-accent);
  padding-left: var(--space-6);
  margin: 0;
}

.testimonial-attribution {
  font-size: var(--text-xs);
  text-transform: uppercase;
  letter-spacing: var(--tracking-wider);
  color: var(--color-text-muted);
  margin-top: var(--space-4);
}
```

---

## FONT LOADING — Ottimizzazione Performance

```html
<!-- In <head> — OBBLIGATORIO -->

<!-- 1. Preconnect per Google Fonts (se usato) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- 2. Preload display font (primo .woff2 del font principale) -->
<link rel="preload" as="font" type="font/woff2"
      href="[URL del font display principale]" crossorigin>

<!-- 3. CSS con font-display: swap -->
<link href="[Google Fonts URL]&display=swap" rel="stylesheet">
```

```css
/* In design-tokens.css / styles.css */
@font-face {
  font-family: '[Font Name]';
  src: url('[font].woff2') format('woff2');
  font-display: swap; /* evita FOUT bloccante */
  font-weight: 100 900; /* per variable fonts */
}
```

**Regole di performance:**
- Max 2 font families per pagina (eccezionalmente 3)
- Preferire variable fonts (1 file per tutti i pesi — riduce richieste HTTP)
- Subset per lingua (solo caratteri usati — riduce peso file)
- Preload solo il display font — non tutti i font

---

## DESIGN TOKENS COMPLETI — Typography

```css
/* ================================================
   TYPOGRAPHY TOKENS — design-tokens.css
   ================================================ */

/* Famiglie font */
--font-display: 'Cormorant Garamond', Georgia, serif;   /* ESEMPIO */
--font-body:    'DM Sans', system-ui, sans-serif;         /* ESEMPIO */
--font-mono:    'Geist Mono', 'Fira Code', monospace;    /* solo SaaS */

/* Type scale — Perfect Fourth 1.333 */
--text-xs:   0.75rem;
--text-sm:   0.875rem;
--text-base: 1rem;
--text-lg:   1.333rem;
--text-xl:   1.777rem;
--text-2xl:  2.369rem;
--text-3xl:  3.157rem;
--text-4xl:  4.209rem;
--text-5xl:  5.61rem;

/* Line heights */
--leading-none:    1.0;
--leading-tight:   1.1;
--leading-snug:    1.2;
--leading-normal:  1.35;
--leading-relaxed: 1.6;
--leading-loose:   1.7;
--leading-caption: 1.45;

/* Letter spacing */
--tracking-tightest: -0.04em;
--tracking-tighter:  -0.02em;
--tracking-tight:    -0.01em;
--tracking-normal:    0em;
--tracking-body:     +0.01em;
--tracking-wide:     +0.05em;
--tracking-wider:    +0.12em;
--tracking-widest:   +0.20em;

/* Font weights */
--weight-thin:       100;
--weight-extralight: 200;
--weight-light:      300;
--weight-regular:    400;
--weight-medium:     500;
--weight-semibold:   600;
--weight-bold:       700;
--weight-extrabold:  800;
--weight-black:      900;
```

---

## TYPOGRAPHY QUALITY GATE

Prima di procedere dalla Fase 5 alla Fase 6, verificare ogni elemento:

```
□ Font display: NON è Inter/Roboto/Arial/Helvetica/system-ui
□ Coppia tipografica: 2 font con tensione visiva (non 2 font simili)
□ Type scale: basata su Perfect Fourth (1.333) — verificare i valori
□ Hero/Display: tracking negativo (-0.02em o meno)
□ Label/Nav: tracking positivo (+0.12em o più) + UPPERCASE
□ Body: max-width 68ch applicato al container del testo
□ Line-height body: 1.6 minimo (mai scendere sotto)
□ Baseline grid: ogni line-height × font-size = divisibile per 4
□ Fluid typography: clamp() su H1 e display — verificare in browser a varie larghezze
□ Bold word system: presenti nei paragrafi corpo
□ Skeleton test: superato per ogni sezione di testo
□ Font loading: preload display font + font-display:swap
□ text-wrap: balance su tutti gli headings (verifica visivamente)
□ Lowercase: headings tutti in sentence case
```

**Trigger Anti-Gravity #4:** dopo aver completato la type scale e selezionato la coppia di font, questo è il momento di consultare Anti-Gravity per esplorare combinazioni tipografiche insolite e sorprendenti per l'aesthetic axis scelto.
