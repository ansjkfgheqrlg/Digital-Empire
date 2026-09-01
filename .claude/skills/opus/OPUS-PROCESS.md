# OPUS PROCESS — Il Cervello Completo
> Tutte le 21 fasi del sistema OPUS con ogni sub-step, quality gate, e momento Anti-Gravity.
> Questo file è il knowledge base primario di opus-director.

---

## PRINCIPI FONDATIVI (mai dimenticare)

1. **Restraint is luxury** — rimuovi fino a quando rimane solo l'essenziale
2. **One focal point per viewport** — mai 4-5 CTA che competono per l'attenzione
3. **Commit to an aesthetic axis** — non indecisione, esecuzione totale di una direzione precisa
4. **Anti-AI by design** — Inter fonts, purple gradients, pill buttons = VIETATI (vedi ANTI-AI-BLACKLIST.md)
5. **Polish loop is the difference-maker** — 7 pass iterativi, non 1 (vedi POLISH-LOOP-PROTOCOL.md)
6. **Desktop-first** — progetta l'esperienza desktop completa prima, poi ottimizza mobile
7. **Silver-mixed mandatory** — ogni colore (incluso brand primary) ha saturazione ridotta 20-35% + silver undertones
8. **Grain mandatory** — SVG feTurbulence su ogni sfondo, position:fixed, background-size ≤200px
9. **Dual-theme always** — dark/light toggle incluso in ogni sito OPUS

---

## ARCHITETTURA GLOBALE — 21 Fasi

```
/opus new <project>
     │
     ▼
opus-director (model: Opus — conosce tutto questo file a memoria)
     │
     ├─── FASE 0:   INITIALIZATION
     ├─── FASE 1:   DISCOVERY                    → /site brief
     ├─── FASE 2:   TECHNICAL ARCHITECTURE       → /site stack + CMS decision
     ├─── FASE 2.5: VISUAL ASSETS STRATEGY       → ASSET-STRATEGY.md
     ├─── FASE 3:   INFORMATION ARCHITECTURE     → /site plan + PATH A/B/C
     ├─── FASE 4:   DESIGN SYSTEM               → /site design + frontend-design
     ├─── FASE 4A:  SILVER-METALLIC COLORS       → design-tokens.css aggiornato
     ├─── FASE 4B:  SECTION DIVIDERS             → pattern divider nel CSS
     ├─── FASE 4C:  BLOCK & CARD DESIGN          → components in style-guide.html
     ├─── FASE 4D:  GRAIN TEXTURE SYSTEM         → body::before in styles.css
     ├─── FASE 5:   TYPOGRAPHY MASTERY           → design-tokens.css tipo + TYPOGRAPHY-SYSTEM.md
     ├─── FASE 5A:  TEXT VISUAL DESIGN           → SITE-COPY.md annotazioni
     ├─── FASE 6:   CONTENT & COPY               → /site copy (3 agenti paralleli)
     ├─── FASE 7:   BUILD                        → /site build (3-step shell→pages+interactions)
     ├─── FASE 7.5: CONVERSION ENGINEERING       → js/conversion.js + thank-you.html
     ├─── FASE 8:   MOTION ENGINEERING           → /site animate
     ├─── FASE 9:   ANTI-AI POLISH LOOP          → 7 pass iterativi (POLISH-LOOP-PROTOCOL.md)
     ├─── FASE 10:  TECHNICAL SEO                → /site seo
     ├─── FASE 11:  QUALITY ASSURANCE            → /site qa (4 agenti paralleli)
     ├─── FASE 12:  DEPLOYMENT + GDPR + GA4      → /site deploy
     └─── FASE 13:  DELIVERY                     → /site report
```

**Anti-Gravity moments:** Fasi 4.1, 4.5, 4.7, 5.2, 6.2, 8.1, 9.7, 12.2 (8 totali)

---

## CONTESTO D'USO — 2 Modalità

**MODALITÀ 1 — USO PERSONALE (primario):**
L'utente crea siti per **se stesso** — info business: lanci prodotti digitali (corsi, coaching, membership), acquisizione lead, vendita diretta.
- Copy: direct response, convince, vende, supera obiezioni
- Design: premium + conversion-driven (bello E che converte)
- Voice: brand personale dell'utente, non corporate
- Urgenza: **reale** (launch windows, posti limitati) — mai fake
- Sezioni: ottimizzate per PATH A (info business)

**MODALITÀ 2 — CLIENTI AGENZIA:**
L'utente gestisce un'agenzia che crea siti per attività locali e business.
- Copy: brand del cliente, tono del settore
- Design: adattato all'identità del cliente
- Deliverable: sito + report cliente + guida modifiche post-lancio

**opus-director chiede in Phase 0:** "Questo sito è per te o per un cliente?"

---

## PATH — 3 Percorsi di Struttura

### PATH A — INFO BUSINESS LAUNCH PAGE [PRIMARIO]
Per: lanci prodotti digitali (corso, coaching, membership, consulenza)
Obiettivo: massimizzare conversioni su un'offerta specifica.

**Struttura ottimizzata (ordine validato da direct response):**
1. HERO: Headline trasformazione + subheadline obiezione + CTA primario
2. SOCIAL PROOF IMMEDIATA: mini-testimonianze above fold (2-3 righe)
3. PROBLEM/AGITATION: il dolore che il prodotto risolve
4. PROMISE: cosa ottieni + trasformazione promessa
5. WHO FOR: per chi è (e chi NON è) — filtraggio e identificazione
6. WHAT YOU GET (Offer Stack): ogni elemento con valore percepito
7. HOW IT WORKS: processo in 3 step — semplicità percepita
8. RESULTS/PROOF: case study, screenshot, trasformazioni specifiche
9. ABOUT (autorità): storia del creator — credibilità senza arroganza
10. BONUSES: bonus stack con valore percepito totale
11. PRICING: anchor (prezzo pieno → prezzo offerta)
12. GUARANTEE: riduzione del rischio percepito
13. FAQ: le 7 obiezioni reali del target
14. URGENCY/SCARCITY: **reale** (chiude il [data], solo N posti)
15. FINAL CTA: riepilogo offerta + CTA forte

### PATH B — SALES PAGE / LANDING PAGE SEMPLICE
Per: lead generation, iscrizione lista, webinar, product page singola.
Max 6-8 sezioni: Hero → Problem → Solution → Proof → CTA.
Focus su un'unica azione.

### PATH C — SAAS / PRODOTTO DIGITALE
Per: tool, app, software. Struttura per spiegare + far provare.
Sezioni: Hero (demo CTA) → Social Proof (loghi) → Features Grid → How It Works →
Pricing toggle → Integrations → Testimonials → FAQ → CTA finale.
Specifiche SaaS: dashboard preview animated, integration logos, security badges.

---

## FASE 0 — INITIALIZATION

```
0.1 Project Setup
    0.1.1 Crea cartella: projects/<project-name>/
    0.1.2 Inizializza OPUS-STATUS.md (template da OPUS-STATUS-template.md)
          con tutte le fasi a ⏳
    0.1.3 Crea PROJECT-CONTEXT.md con dati cliente
          (persiste tra sessioni — viene riletto ad ogni resume)
    0.1.4 Determina entry point:
          ├─ FULL: da zero, tutte le fasi
          ├─ RESUME: ripresa da fase X (legge deliverable esistenti)
          └─ PATCH: fix issue specifico (/opus fix <issue>)

0.2 Pre-Flight Check
    0.2.1 Verifica che le skill site-* siano attive (site brief/stack/plan/design/copy/build/animate/seo/qa/deploy/report)
    0.2.2 Controlla deliverable già esistenti per evitare ridondanza
    0.2.3 Identifica tipo di sito:
          landing | vetrina | portfolio | SaaS | e-commerce |
          corporate | blog | booking | directory | app
    0.2.4 Chiede: "Questo sito è per te o per un cliente?"
          → risposta determina voice, copy style, e urgency approach

OUTPUT → OPUS-STATUS.md + PROJECT-CONTEXT.md
```

---

## FASE 1 — DISCOVERY (→ /site brief)

```
1.1 Business Foundation
    1.1.1 Nome progetto + settore
    1.1.2 Obiettivi primari (3 max, ordinati per priorità)
    1.1.3 Obiettivi secondari (massimo 2)
    1.1.4 Metriche di successo quantitative
          Es: "100 lead/mese", "5% conversion", "€50k revenue dal lancio"
    1.1.5 Timeline: hard deadline vs soft deadline
    1.1.6 Vincoli: budget, tech, legale, brand

1.2 Audience Definition
    1.2.1 Persona primaria: nome fittizio, età, professione, dolori, desideri
    1.2.2 Persona secondaria (solo se davvero distinta)
    1.2.3 User journey: arriva al sito → cosa fa → cosa porta via
    1.2.4 5 obiezioni reali del target (usate in copy e FAQ)
    1.2.5 Linguaggio del target: parole che usa, parole che evita

1.3 Brand Foundation
    1.3.1 5 aggettivi che descrivono il brand (non le feature)
    1.3.2 Tono di voce su 4 assi:
          - Formale ←→ Informale
          - Serio ←→ Giocoso
          - Tecnico ←→ Umano
          - Riservato ←→ Audace
    1.3.3 3 siti di ispirazione con note specifiche
          (es. "voglio questa navigazione")
    1.3.4 3 siti da NON imitare con note specifiche
    1.3.5 Asset esistenti: logo (formati), colori brand, font ufficiali, foto

1.4 Content Inventory
    1.4.1 Lista pagine necessarie (ordinata per priorità)
    1.4.2 Sezioni speciali con logica (blog, shop, booking, portfolio)
    1.4.3 Lingue richieste + lingua principale
    1.4.4 Integrazioni: CRM, analytics, chat, newsletter, payment, API

OUTPUT → SITE-BRIEF.md
```

---

## FASE 2 — TECHNICAL ARCHITECTURE (→ /site stack)

```
2.1 Stack Decision Matrix
    2.1.1 Complessità 1-5: features speciali, dynamic content, auth
    2.1.2 Capacità tecnica per mantenimento post-lancio
    2.1.3 Performance target (LCP < 2.5s)
    2.1.4 Vincoli hosting e deployment
    2.1.5 Budget per dipendenze premium
    2.1.6 DECISIONE → Percorso:
          A: HTML + Tailwind CDN + GSAP    (landing, vetrina, portfolio)
          B: Next.js 15 + React 19 + Tailwind + Motion (SaaS, e-commerce)
          C: Turborepo + Next.js + Storybook (agency, design system)

2.2 Animation Library Decision
    React → Motion (ex Framer Motion) per UI + GSAP per scene complesse
    HTML  → GSAP primary, Anime.js micro-animazioni, Lenis smooth scroll
    Regola: non installare entrambi se uno è sufficiente
    Performance budget: max 50KB di libreria JS animazione

2.2b CMS Decision
    GATE: il cliente deve modificare contenuti in autonomia?
    ├─ NO → sito statico puro. Performance massima.
    ├─ Testi solo → Decap CMS o Tina.io (markdown-based, zero database)
    └─ Contenuti strutturati → Sanity.io (headless) + Next.js (Percorso B)

2.2c CMS Setup (condizionale)
    2.2c.1 Configura schema contenuti
    2.2c.2 Installa e configura CMS
    2.2c.3 Documentazione editing per cliente (1 pagina)
    2.2c.4 Testa flusso: login → edit → save → preview

2.3 Premium Toolstack
    Smooth scroll: Lenis (0.9KB, zero dipendenze)
    Page transitions: Barba.js (HTML) / AnimatePresence (React)
    3D: Three.js (HTML) / React Three Fiber (React) — solo se giustificato
    Design system: Radix UI + shadcn/ui (React) / DaisyUI (HTML)

2.4 Environment Setup
    2.4.1 Struttura cartelle stabilita prima del codice
    2.4.2 File configurazione: tailwind.config, tsconfig, .env.example
    2.4.3 CSS custom properties come layer zero
    2.4.4 Variabili d'ambiente documentate

OUTPUT → SITE-STACK.md
```

---

## FASE 2.5 — VISUAL ASSETS STRATEGY

```
Obiettivo: definire la strategia per ogni immagine/visual PRIMA di design e build.
Evita problema #1 dei siti premium: design curato + immagini mediocri.

2.5.1 Asset Inventory (da cliente)
    Logo (SVG + PNG), foto prodotto/team/ufficio, brand images,
    video, icone custom, illustrazioni.
    Per ogni asset: nome → formato → risoluzione → utilizzo → qualità OK?

2.5.2 Decision per ogni sezione visiva:
    TIPO A: "Client asset" → cliente fornisce immagine specifica
            Nota: [CLIENTE FORNISCE: hero image 1440×900]
    TIPO B: "Quality placeholder" → semanticamente preciso
            [IMMAGINE: descrizione precisa — contesto, soggetto, lighting, ratio]
            Es: [IMMAGINE HERO: professionista 30-40 anni su laptop in
            ambiente minimal moderno, luce naturale soffusa, 1440×900]
    TIPO C: "AI generation" → prompt per Midjourney/SDXL
            Template: "[Soggetto], [stile fotografico], [lighting],
            [colori coerenti con palette], [composizione], [ratio],
            [qualità: ultra-detailed, professional photography], [no text]"

2.5.3 Image Quality Standards
    Risoluzione minima: 2x del size display (800px display → 1600px file)
    Formato: JPEG (photo) o PNG (logo/illustration)
    OPUS converte a WebP/AVIF durante build
    srcset: 400w, 800w, 1200w, 1600w
    ZERO compression artifacts

OUTPUT → ASSET-STRATEGY.md
```

---

## FASE 3 — INFORMATION ARCHITECTURE (→ /site plan)

```
3.1 Sitemap Design
    3.1.1 Gerarchia pagine (max 3 livelli di profondità)
    3.1.2 URL scheme: lowercase, hyphens, keyword-informed
    3.1.3 Navigazione principale: max 6 voci
    3.1.4 Navigazione secondaria: footer, breadcrumb, sidebar
    3.1.5 Internal linking: ogni pagina ha 2-3 link contestuali

3.2 Page-Level Architecture (per OGNI pagina)
    3.2.1 Obiettivo primario in 1 frase
    3.2.2 CTA primario (1 solo per pagina)
    3.2.3 Sequenza sezioni per conversion:
          Hero → Proof → Value → How → Proof → CTA
    3.2.4 Zone: attention zone (hero) / consideration / decision
    3.2.5 One focal point per viewport: cosa vede l'occhio per PRIMO

3.3 Component Library Inventory
    Globali: navbar (scroll/mobile variants), footer
    Sezione-level: hero, features, testimonials, pricing, FAQ, CTA, about
    Micro-componenti: button (varianti), card (varianti), badge, input, divider
    Interattivi: accordion, tabs, carousel, modal, tooltip, dropdown
    Premium-only: timeline, comparison table, progress steps, map, video player

OUTPUT → SITE-PLAN.md
```

---

## FASE 4 — DESIGN SYSTEM (→ /site design + frontend-design)

```
4.1 Aesthetic Axis Declaration — IMPEGNO TOTALE
    Scegli UN SOLO asse: brutalism raffinato | minimalismo organico |
    retro-futurismo | lusso editoriale | maximalism curato | brutalism raw |
    natura-distillata | art deco geometrico | soft/pastel premium |
    industrial/utilitario | editorial/magazine | tech/cyberpunk

    4.1.1 Nomina il movimento visivo (es. "Modernismo Caldo", "Lusso Sereno")
    4.1.2 3 principi di design non negoziabili
    4.1.3 Risposta emotiva target: cosa SENTE il visitatore dopo 3 secondi
    4.1.4 Mood board testuale: 5 riferimenti visivi descritti con parole precise
    4.1.5 VERIFICA: questo asse è OPPOSTO all'aesthetic AI-generica? Se no, riparti.

    ⬇️ MOMENTO ANTI-GRAVITY #1 — Design Manifesto
       Fornire contesto: nome movimento + 3 principi + risposta emotiva + tipo sito
       AG espande il manifesto e offre 5 direzioni alternative non ovvie

4.2 Color Engineering
    Architettura palette (regola dei 3 layer):
    FOUNDATION (~90% area):
      --color-surface:    dark: ~#0c0c0c | light: ~#faf9f5 (MAI puro)
      --color-surface-2:  3-4% lightness shift
      --color-surface-3:  ulteriore 3-4% shift
    CONTENT:
      --color-text:       warm off-white o warm near-black (MAI puro)
      --color-text-muted: 50-60% opacity del text principale
    ACCENT (<5% area):
      --color-accent:       colore brand — uno solo
      --color-accent-hover: +10% lightness

    4.2.1 Scala primaria 10 step (50→900) per colore brand
    4.2.2 Colori semantici: success / warning / error / info
    4.2.3 Border tokens: rgba(255,255,255, 0.06-0.10) dark — mai solid
    4.2.4 Gradient: ultra-sottili se necessari (2-3° hue shift max)
    4.2.5 Colored shadows: basate sull'accent (non grigio neutro)

    GATE: La palette supera il test "restraint"? L'accent è davvero <5%?

4.3 Spatial System — Mathematical Rhythm (Desktop-First)
    Base: 8px
    --space-1:  4px  | --space-2:  8px  | --space-3: 12px  | --space-4: 16px
    --space-5: 24px  | --space-6: 32px  | --space-8: 48px  | --space-10: 64px
    --space-12: 96px | --space-16: 128px | --space-20: 160px | --space-24: 192px

    Luxury sites RADDOPPIANO lo spacing standard — vai largo
    Section padding: clamp(4rem, 8vw, 10rem) — mai fixed pixel
    Layout grid: ratio asimmetrici (7/5, 8/4, 3/7) — non solo 6/6
    Border-radius: luxury 0-2px | modern 8px | organico 16-24px

4.4 Component Visual Language
    BUTTON anatomy premium:
      padding: 14px 32px | border-radius: 2px (NON 9999px)
      font-size: 13px | font-weight: 400 | letter-spacing: 0.15em
      text-transform: uppercase | background: transparent (outlined default)
      hover: fill + letter-spacing 0.18em | 5 stati obbligatori

    CARD sistema elevazione:
      flat | elevated | bordered | glass
      hover: translateY(-4 a -6px) + shadow expansion + image scale 1.05

    NAVIGATION premium:
      height: 56-64px | sticky + backdrop-filter: blur(20px)
      Nav items: uppercase, 12px, letter-spacing 0.20em
      Scroll: shrinks 64px→48px dopo 100px
      Mobile: off-canvas drawer (NO hamburger brutto)

4.5 Atmosphere & Premium Details
    Scegli UN background technique dominante (oltre alla grana obbligatoria):
    gradient mesh | pattern geometrico sottile | layered transparency | texture fotografica

    Glass morphism (tech/premium moderno):
      backdrop-filter: blur(20px)
      background: rgba(255,255,255,0.05)
      border: 1px solid rgba(255,255,255,0.10)

    Colored shadows: basate sull'accent
    Accent decorativi: max 1-2 per sezione

    ⬇️ MOMENTO ANTI-GRAVITY #2 — Atmosphere Expansion
       Fornire contesto: aesthetic axis + palette + tipo sito + audience + settore
       AG espande con micro-dettagli premium non ovvi per quel specifico settore

4.6 Visual Hierarchy — 5 Livelli (vedi TYPOGRAPHY-SYSTEM.md per dettagli)
    Min 1.5x size difference tra livelli adiacenti
    Leggibile al 20% zoom

4.6b Dark Mode / Light Mode — SEMPRE entrambi
    CSS custom properties + data-theme attribute + JS toggle
    Dark: surface #0c0c0c→#161616→#1f1f1f | text warm off-white
    Light: surface #faf9f5→#f0ede8→#e8e3dc | text warm near-black
    Toggle: sun/moon in navbar, 44×44px touch target, localStorage

4.7 Design Tokens Lock — FREEZE
    Tutti i token congelati PRIMA di scrivere codice:
    ├─ Color tokens (surface, text, accent, semantic, border, shadow, silver-mixed)
    ├─ Type scale completo (ogni livello in rem + clamp())
    ├─ Spacing scale (space-1 → space-24)
    ├─ Component tokens (button, card, input, nav)
    ├─ Motion tokens (durations, easings, stagger)
    ├─ Border radius tokens
    ├─ Divider tokens
    └─ Block tokens
    Tutto in design-tokens.css PRIMA di qualsiasi HTML.
    ZERO hex hardcoded nel codice — SOLO custom properties.

    ⬇️ MOMENTO ANTI-GRAVITY #3 — Token Review
       Fornire contesto: design-tokens.css completo
       AG fa review critica e identifica token che sembrano ancora AI-generic

OUTPUT → SITE-DESIGN.md + design-tokens.css + style-guide.html
```

---

## FASE 4A — SILVER-METALLIC COLOR ARCHITECTURE

```
Ogni colore del sito è "silver-mixed" — la firma visiva del lusso moderno.

PROCESSO SILVER-MIXING:
  STEP 1: Riduci saturazione del 20-35%
          Es: Blue hsl(210, 80%, 50%) → hsl(210, 45%, 55%)
  STEP 2: Aumenta luminosità 5-10%
          Risultato: il colore "guadagna aria" e sembra metallico
  STEP 3: Aggiungi overlay silver rgba(192,192,192, 0.05-0.10) nei blocchi
  STEP 4: Verifica: sembra "stampato su carta patinata di lusso"? Se no → riduci ancora

BRAND PRIMARY silver-mixed obbligatorio:
  Oro:     hsl(45, 60%, 65%)  — "champagne gold"
  Blu:     hsl(210, 35%, 60%) — "steel blue"
  Verde:   hsl(150, 25%, 58%) — "sage silver-green"
  Rosso:   hsl(5, 35%, 62%)   — "dusty rose-silver"
  Viola:   hsl(265, 25%, 65%) — "silver lavender"
  Nero:    hsl(0, 0%, 12%)    — "charcoal silver"
  Bianco:  hsl(45, 15%, 97%)  — "warm silver-white"

TOKEN SILVER aggiuntivi:
  --surface-silver-light: rgba(192,192,192, 0.04)
  --surface-silver-dark:  rgba(192,192,192, 0.06)
  --border-silver:        rgba(192,192,192, 0.15)
  --shimmer-silver:       rgba(255,255,255, 0.08)

SHIMMER EFFECT su componenti premium:
  .premium-card::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg,
      transparent 0%, rgba(192,192,192,0.08) 50%, transparent 100%);
    transition: left 600ms var(--ease-out-expo);
  }
  .premium-card:hover::before { left: 100%; }

OUTPUT → design-tokens.css aggiornato con token silver-mixed
```

---

## FASE 4B — SECTION DIVIDERS & VISUAL TRANSITIONS

```
Tra sezioni il passaggio è PROGETTATO — non accidentale.

STRATEGIA DEFAULT OPUS:
  Gradient silver line: tra sezioni normali (discreto, sempre)
  Geometric/diagonal: solo 3-4 macro-transizioni principali

TIPO 1 — GRADIENT SILVER LINE (default):
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(192,192,192,0.4) 50%, transparent);

TIPO 2 — SURFACE TRANSITION:
  Cambio background con gradient — sezioni "fluiscono"

TIPO 3 — GEOMETRIC DIVIDER (macro-sezioni):
  SVG inline con forma geometrica (diagonale, onda 2°, chevron sottile)

TIPO 4 — DECORATIVE RULE (brand editoriali/lusso):
  Elemento centrato: · linea · oppure SVG ornament

TIPO 5 — SECTION NUMBER (How It Works, Steps):
  Numero oversize (80-120px, opacity 0.06-0.10) dietro il contenuto

REGOLE APPLICAZIONE:
  □ MAI sezione che finisce e altra inizia senza transizione
  □ Max 2 tipi di divider per sito (coerenza)
  □ Stesso background → TIPO 1 | Background diverso → TIPO 2
  □ Hero → prima sezione: TIPO 3 o TIPO 2
  □ Footer: TIPO 1 o TIPO 2

PADDING SEZIONI:
  Standard desktop: clamp(5rem, 8vw, 10rem)
  Hero + CTA finale: clamp(7rem, 12vw, 14rem)

OUTPUT → design-tokens.css + HTML pattern divider
```

---

## FASE 4C — BLOCK & CARD PREMIUM DESIGN

```
I blocchi non sono box con testo — sono elementi visivi che "incorniciano" informazioni preziose.

ANATOMIA BLOCCO PREMIUM:
  background: --surface-silver (silver-tinted, semi-trasparente)
  border: 1px solid --border-silver
  border-radius: coerente col design system
  padding: --space-5 (24px) minimo
  shadow: 0 4px 24px rgba(0,0,0,0.08) +
          0 1px 0 rgba(192,192,192,0.10) (top highlight 3D)
  hover: shadow expansion + shimmer border

VARIANTI:
  FEATURED BLOCK: border gradient silver-to-accent + accent bg opacity 5-8%
  NUMBERED STEP: number oversize (opacity 0.06) + connecting line silver
  LIST BLOCK: custom markers (→ ✓ —) invece di bullet (•)
  HIGHLIGHT BLOCK: border-left 3px accent + pull quote style

BULLET LIST PREMIUM:
  list-style: none + ::before con → o ✓ o — in accent color
  Spacing tra items: --space-3 (12px)
  line-height: 1.7

OUTPUT → CSS block variants + style-guide.html aggiornato
```

---

## FASE 4D — GRAIN TEXTURE SYSTEM (OBBLIGATORIO ASSOLUTO)

La grain è la firma finale di un design premium. OGNI sezione, OGNI sfondo.

```css
/* IMPLEMENTAZIONE STANDARD — usare sempre questa */
body::before {
  content: '';
  position: fixed;        /* FISSO: non scrolla */
  inset: 0;
  z-index: 9999;
  pointer-events: none;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='grain'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23grain)'/%3E%3C/svg%3E");
  background-repeat: repeat;
  background-size: 180px 180px;  /* CRITICO: piccolo = grana fine */
  opacity: 0.045;
  mix-blend-mode: overlay;
}

/* DARK/LIGHT ADAPTATION */
[data-theme="dark"]  body::before { opacity: 0.05; mix-blend-mode: overlay; }
[data-theme="light"] body::before { background-size: 140px 140px; opacity: 0.03; mix-blend-mode: soft-light; }

/* MOBILE */
@media (max-width: 768px) {
  body::before { opacity: 0.03; background-size: 120px; }
}
```

**Parametri critici:**
- baseFrequency 0.75 (dark) / 0.85 (light)
- background-size ≤200px dark / ≤150px light — **MAI auto o 100%**
- opacity: dark 4-6% / light 2.5-3.5% — **MAI sopra 8%**
- **Se la grana sembra pixel → RIDUCI background-size (non aumentare baseFrequency)**

**4 errori comuni:**
- background-size troppo grande → grain pixelato
- opacity troppo alta → grain artificiale
- mix-blend-mode sbagliato → grain "incollato"
- PNG importato → sempre pixelato su Retina

```css
/* TOKEN GRAIN in design-tokens.css */
--grain-base-freq-dark:  0.75;
--grain-base-freq-light: 0.85;
--grain-size-dark:  180px;
--grain-size-light: 140px;
--grain-opacity-dark:  0.05;
--grain-opacity-light: 0.03;
```

OUTPUT → body::before in styles.css + grain tokens in design-tokens.css

---

## FASE 5 — TYPOGRAPHY MASTERY (→ vedi TYPOGRAPHY-SYSTEM.md)

```
5.1 Font Selection (vedi tabella in TYPOGRAPHY-SYSTEM.md)
    VIETATI: Inter, Roboto, Arial, Helvetica, system-ui
    APPROVATI: Satoshi, Cabinet Grotesk, DM Sans, Cormorant Garamond, ecc.
    Coppia tipografica: SEMPRE 2 font (display + body) con tensione visiva

5.2 Type Scale — Perfect Fourth 1.333 (vedi TYPOGRAPHY-SYSTEM.md)
    --text-xs: 0.75rem → --text-5xl: 5.61rem
    Fluid con clamp() su ogni livello — mai solo breakpoint

    ⬇️ MOMENTO ANTI-GRAVITY #4 — Typography Deep Dive
       Fornire contesto: aesthetic axis + brand personality + settore + 2 font candidati
       AG suggerisce combinazioni insolite e sorprendenti per quell'aesthetic

5.3-5.8 (vedi dettagli in TYPOGRAPHY-SYSTEM.md):
    Line height, letter-spacing, font weight strategy,
    bold word system, fluid typography, font loading

OUTPUT → design-tokens.css tipo aggiornato + style-guide.html
```

---

## FASE 5A — TEXT VISUAL DESIGN SYSTEM

```
5A.1 Lowercase Style (sentence case per H1/H2/H3)
    "il metodo che ha cambiato tutto" NON "Il Metodo Che Ha Cambiato Tutto"
    ECCEZIONI: nomi propri, acronimi, brand name

5A.2 Bold Word System (vedi TYPOGRAPHY-SYSTEM.md — sezione dedicata)
    1-3 parole per frase | font-weight 600 | skeleton test obbligatorio

5A.3 Paragrafo Perfetto
    max-width: 68ch | line-height 1.6-1.7 | max 3-4 righe
    margin-bottom: --space-5 o --space-6

5A.4 Heading Treatment
    H1 display: leading 1.0-1.05, tracking negativo, weight 300-400
    H2 section: leading 1.1, tracking -0.01em, weight 400
    H3 sub: leading 1.3, tracking 0em, weight 500-600

5A.5 Label & Tag Style
    font-size: 11-12px | uppercase | letter-spacing 0.15em+ | muted color

5A.7 Numeri e Statistiche
    font-size: 3-5x corpo | font-weight: 300 (light!) | accent color
    Label sotto: xs, uppercase, muted, tracking 0.15em

5A.8 Quote / Testimonial
    font-size: --text-xl | italic | weight 300 (light)
    border-left: 3px solid accent

OUTPUT → SITE-COPY.md annotazioni di stile + styles.css regole testo
```

---

## FASE 6 — CONTENT & COPY (→ /site copy)

```
6.1 Lancio Parallelo 3 Agenti
    site-copy-hero: H1 (max 8 parole), H2 seconda persona, CTA verbo attivo
    site-copy-body: features con bold word system, about, how it works, FAQ, pricing
    site-copy-meta: title tag 50-60ch, meta description 150-160ch, OG, alt text

6.1b Stile Copy — Modalità Uso Personale
    TONE: diretto, autorevole, senza giri di parole
    VOCE: prima persona dove appropriato
    STANCE: esperto che sa già la risposta
    VIETATE: "Potrebbe aiutarti", "Scopri come", "Forse stai cercando"
    APPROVATE: "Questo è per te se...", "Ecco cosa otterrai:", "Il risultato? [specifico]."

6.2 Copy Quality Gate
    □ Ogni headline: "Cosa ci guadagno io in 3 secondi?"
    □ Ogni CTA: verbo attivo, non generico ("Scopri di più" = VIETATO)
    □ Features: PRIMA il beneficio, POI la feature tecnica
    □ Zero placeholder text
    □ Bold word system applicato + skeleton test superato
    □ Lunghezza righe corpo: 45-68 caratteri

    ⬇️ MOMENTO ANTI-GRAVITY #5 — Copy Refinement
       Fornire: headline principale + problema che risolve + audience + tono
       AG produce varianti headline A/B + versione emozionale profonda

OUTPUT → SITE-COPY.md
```

---

## FASE 7 — BUILD (→ /site build)

```
7.1 Foundation — AGENTE site-build-shell (SEQUENZIALE — eseguito PRIMA)
    design-tokens.css: TUTTI i token (colore, tipo, spacing, componenti, motion)
    css/styles.css: CSS reset moderno + base typography + utility classes
    template.html: shell con head ottimizzato (meta, preconnect, preload, JSON-LD)
    components/navbar.html: sticky + backdrop-filter + mobile drawer + skip-link
    components/footer.html: copyright anno dinamico via JS
    js/main.js: init + theme toggle + globals

    GATE: verifica shell completa prima di procedere

7.2 Build Parallelo
    AGENTE site-build-pages: index.html + ogni pagina da SITE-PLAN.md
      REGOLE QUALITÀ:
      - Copy ESATTO da SITE-COPY.md
      - TUTTI i colori da design-tokens.css (ZERO hex hardcoded)
      - Bold word system applicato
      - One focal point per sezione
      - Spacing da tokens (ZERO arbitrary)
      - Image width + height espliciti (previene CLS)
      - id="" su ogni sezione per anchor navigation

    AGENTE site-build-interactions: js/interactions.js (IIFE, zero dipendenze)
      Mobile menu, smooth scroll, FAQ accordion, pricing toggle,
      tabs keyboard, form validation, counter animation, back-to-top,
      navbar shrink, lazy load fallback

7.3 3D (condizionale — solo portfolio creativo / product showcase)
    Three.js (HTML) o React Three Fiber (React)
    FALLBACK obbligatorio se WebGL non supportato
    Pixel ratio max: 2x | Disable su mobile hardware limitato

7.4 Build Verification
    ✅ ZERO hex hardcoded | ✅ ZERO placeholder text
    ✅ Bold word system presente | ✅ Spacing da scale
    ✅ Image width/height dichiarate | ✅ ARIA baseline
    ✅ Grain texture: body::before presente + position:fixed + SVG inline
    ✅ background-size ≤200px + opacity nel range

OUTPUT → Sito funzionante in browser
```

---

## FASE 7.5 — CONVERSION ENGINEERING (PATH A only)

```
7.5.1 COUNTDOWN TIMER — Urgenza Reale
    Solo se c'è una scadenza reale (launch window, early bird)
    Vanilla JS, data-deadline attribute in HTML
    Varianti: hero timer | sticky bar | section timer
    Alla scadenza: pricing cambia, CTA diventa "lista d'attesa"
    Performance: interval 1000ms + requestAnimationFrame per display

7.5.2 SOCIAL PROOF NOTIFICATIONS
    Appare dopo 3 secondi, bottom-left, max 280px
    Dati statici (array JSON) o da API
    Frequenza: 1 ogni 25-40s | Max: 3 per sessione
    Animazione: slide-in 300ms → pausa 4-5s → slide-out 200ms
    prefers-reduced-motion: disabilita

7.5.3 EXIT-INTENT POPUP
    Trigger: cursore sopra il 10% viewport height (solo desktop)
    Appare max 1 volta per sessione (sessionStorage)
    Contenuto: offerta last-minute | lead capture | obiezione handler
    Focus-trap + Escape chiude | aria-modal

7.5.4 PAYMENT INTEGRATION
    Stripe Payment Links o Gumroad redirect (zero codice server-side)
    Design button: stesso stile del sito (non il verde PayPal)

7.5.5 THANK YOU PAGE
    /grazie — stessa qualità visiva del sito
    Conferma acquisto + prossimi passi (3 step) + link accesso
    Meta: noindex, nofollow | GA4: evento purchase con valore

7.5.6 WEBINAR / ZOOM (solo coaching/webinar live)
    Form → webhook → email con link Zoom
    Reminder page: /webinar-conferma con .ics download

OUTPUT → js/conversion.js + thank-you.html
```

---

## FASE 8 — MOTION ENGINEERING (→ /site animate)

```
8.1 Strategy
    Identifica 3 "wow moments" MAX — dove animazione ha impatto REALE
    Checklist: "cambierebbe l'experience senza di essa? Se no → eliminala"
    Performance budget: max 50KB libreria JS

    ⬇️ MOMENTO ANTI-GRAVITY #6 — Motion Concepts
       Fornire: tipo sito + aesthetic axis + tech stack + 3 wow moments candidati
       AG propone concetti motion innovativi per quell'aesthetic specifico

8.2 Motion Token System (in design-tokens.css):
    --ease-out-expo:   cubic-bezier(0.16, 1, 0.3, 1)    ← entrances
    --ease-out-quart:  cubic-bezier(0.25, 1, 0.5, 1)    ← hover, UI
    --ease-in-out:     cubic-bezier(0.65, 0, 0.35, 1)   ← page transitions
    --ease-spring:     cubic-bezier(0.34, 1.56, 0.64, 1) ← bouncy micro

    --dur-fast:   150ms | --dur-normal: 300ms | --dur-slow: 500ms
    --dur-slower: 800ms | --dur-slowest: 1200ms (MAX ASSOLUTO)

    --stagger-tight: 40ms | --stagger-normal: 60ms | --stagger-wide: 100ms

8.3 Core Animations — SEMPRE incluse
    SCROLL REVEAL: translateY(20px→0) + opacity(0→1), 500ms ease-out-expo
                   stagger 60ms su grid | once:true | threshold 0.1
    NAVBAR SCROLL: backdrop-filter aumenta + height 64→48px dopo 80px
    HERO ENTRANCE: timeline orchestrata:
                   0ms: badge fadeIn+slideUp20, 400ms
                   100ms: H1 fadeIn+slideUp30, 600ms
                   250ms: subhead fadeIn+slideUp20, 500ms
                   400ms: CTA fadeIn, stagger 80ms, 400ms
                   500ms: visual/image fadeIn, 600ms
    COUNTER: IntersectionObserver + 1200ms ease-out-expo

8.4 Premium Interactions (condizionali)
    MAGNETIC BUTTON: solo portfolio creativo (max 10px displacement)
    CUSTOM CURSOR: solo brand lusso high-end
    PARALLAX SOTTILE: transform:translateY only, max 2 layer
    HOVER LIFT CARDS: translateY(-6px) + shadow + image scale 1.05
    LENIS SMOOTH SCROLL: lerp 0.1, smooth 1
    PAGE TRANSITIONS: cross-fade 300ms o slide 20px
    SCROLL PROGRESS BAR: solo long-form pages

8.5 Safety
    prefers-reduced-motion: reduce → disabilita TUTTO
    Mobile ≤768px: riduce animazioni pesanti
    passive:true su tutti gli scroll listener
    SOLO transform e opacity (GPU-accelerated — VIETATO width/height/top/left)
    Duration MAX: 1200ms — mai superare

OUTPUT → js/animations.js
```

---

## FASE 9 — ANTI-AI POLISH LOOP (vedi POLISH-LOOP-PROTOCOL.md)

```
7 pass iterativi di audit e rifinitura.
Minimum: 5 pass. Premium standard: 7 pass.

PASS 1: Anti-AI Verification (blacklist check)
PASS 2: Typography Audit (gerarchia, tracking, bold word, lowercase)
PASS 3: Spacing & Rhythm (scala matematica, section padding, negative space)
PASS 4: Color, Contrast & Grain (WCAG, grain quality gate, dark/light)
PASS 5: Component States (button 5 stati, card hover, nav scroll, form)
PASS 6: Motion Audit (no instantaneous, prefers-reduced-motion, hero sequence)
PASS 7: Detail Sweep (404, footer, favicon, OG image, text-wrap:balance)

Setup: browser 100% zoom + 20% zoom + DevTools mobile 375px

⬇️ MOMENTO ANTI-GRAVITY #7 — Polish Review Finale (dopo Pass 7)
   Fornire: tutto il contesto del progetto
   AG risponde: "Cosa ancora sembra AI? Dove spingere oltre?"

GATE: ZERO Critical issue in tutti i 7 pass → procedi a Fase 10

OUTPUT → Sito standard "$50.000 quality", anti-AI verificato
```

---

## FASE 10 — TECHNICAL SEO (→ /site seo)

```
10.1 On-Page (per ogni pagina)
    Meta: title (50-60ch), description (150-160ch), robots, canonical
    OG: og:title, og:description, og:image (1200×630), og:type
    Twitter Card
    Heading hierarchy: esattamente 1 H1, nessun salto H2→H3→...
    Alt text: descrittivo + keyword su tutte le immagini

10.2 Structured Data JSON-LD
    Organization (ogni pagina) | WebSite + SearchAction (homepage)
    Schema specifico: LocalBusiness / Person / Product / Article / Event
    FAQPage (se FAQ presente) | BreadcrumbList (pagine interne)

10.3 Technical Files
    sitemap.xml: homepage 1.0 | main 0.8 | secondary 0.6 | detail 0.5
    robots.txt: disallow admin/checkout/staging | include sitemap URL

10.4 Performance Tags
    Preconnect: Google Fonts, CDN, analytics
    font-display: swap | fetchpriority="high" su hero image (LCP)
    loading="lazy" su immagini below-fold | preload display font .woff2

OUTPUT → HTML aggiornati + sitemap.xml + robots.txt + SEO-AUDIT.md
```

---

## FASE 11 — QUALITY ASSURANCE (→ /site qa)

```
4 agenti paralleli:
  site-qa-html: HTML5 validity, heading hierarchy, landmark regions, form labels
  site-qa-accessibility: WCAG 2.1 AA (4.5:1/3:1), ARIA, keyboard, focus, skip link
  site-qa-performance: LCP <2.5s, CLS, render-blocking, image/WebP, bundle size
  site-qa-mobile: viewport meta, touch targets 44×44px, no overflow-x, breakpoints

Score formula: HTML(25%) + Accessibility(30%) + Performance(25%) + Mobile(20%)
Soglia deploy: ≥ 75/100 | Gate assoluto: ZERO Critical

Critical → BLOCCA → fix → re-QA
High     → Fix raccomandato pre-deploy
Medium   → Documenta → fix next sprint

OUTPUT → QA-REPORT.md
```

---

## FASE 12 — DEPLOYMENT + GDPR + GA4 (→ /site deploy)

```
12.1 Pre-Deploy Checklist
    QA Score ≥75 + ZERO Critical | Polish Loop completo (7 pass)
    ZERO placeholder text | Form testati | Favicon + OG image | SSL/HTTPS

12.2 Platform Config
    Vercel: vercel.json (security headers, cache, redirects)
    Netlify: netlify.toml (build + headers + redirects)
    GitHub Pages: deploy.yml (Actions)

12.2b GDPR (mercato italiano/europeo — obbligatorio)
    Cookie consent banner: vanilla JS, 3 livelli (necessari/analytics/marketing)
    Design: coerente col sito (stessa palette e tipografia)
    Privacy Policy: template GDPR + campi specifici del cliente
    Cookie Policy: lista cookie per categoria
    Footer: link legali (Privacy + Cookie + Termini)

12.2c GA4 Configuration
    gtag.js con G-XXXXXXXXXX placeholder
    Consenso condizionale GDPR: default 'denied' → 'granted' su consenso
    Tracking eventi: scroll_depth, CTA click, form_submit, countdown_expired
    IP anonymization sempre attiva
    data-attributes per tracking senza modificare JS core:
    <button data-ga-event="cta_click" data-ga-label="hero_cta">

12.3 Post-Deploy
    Test su dispositivi reali (iOS Safari, Android Chrome)
    Google Search Console: sitemap submission
    PageSpeed Insights (real performance check)
    Form test in produzione

    ⬇️ MOMENTO ANTI-GRAVITY #8 — Launch Announcement
       Fornire: nome prodotto/sito + benefit principale + audience + URL
       AG produce social posts + email di annuncio brandizzata

OUTPUT → Config files + DEPLOY-CHECKLIST.md
```

---

## FASE 13 — DELIVERY (→ /site report)

```
13.1 Report Cliente
    Cover: nome, tipo, stack, pagine, URL, data
    Executive summary: 5 bullet di valore consegnato
    Aesthetic direction + motivazione
    Typography system: font scelti + scale + motivazione
    Color architecture: palette con restraint rationale
    Polish Loop results: issue trovate e risolte per pass
    QA Score breakdown
    SEO implementation summary
    Deploy guide (comandi pronti da copiare)
    Post-lancio recommendations: settimana 1, mese 1, trimestre 1
    File manifest completo

13.2 OPUS Completion
    OPUS-STATUS.md → COMPLETED con tutti i pass ✅
    Archivia PROJECT-CONTEXT.md per future iterazioni

OUTPUT → SITE-REPORT.md
```

---

## ANTI-GRAVITY INTEGRATION SUMMARY

| # | Fase | Quando | Contesto da fornire ad AG |
|---|------|--------|--------------------------|
| AG-1 | 4.1 | Dopo nome movimento visivo | aesthetic axis + 3 principi + risposta emotiva + tipo sito |
| AG-2 | 4.5 | Dopo atmosphere design | palette + aesthetic + settore + audience |
| AG-3 | 4.7 | Dopo design token lock | design-tokens.css completo |
| AG-4 | 5.2 | Dopo type scale | aesthetic + brand personality + settore + font candidati |
| AG-5 | 6.2 | Dopo copy quality gate | headline principale + problema + audience + tono |
| AG-6 | 8.1 | Prima di animazioni | tipo sito + aesthetic + stack + wow moments |
| AG-7 | 9.7 | Dopo Pass 7 polish | tutto il contesto del progetto |
| AG-8 | 12.2 | Dopo deploy config | nome prodotto + benefit + audience + URL |

opus-director dice: **"Questo è il momento di consultare Anti-Gravity."**
Poi fornisce TUTTO il contesto per costruire il prompt.
Non dice "usa questo prompt" — l'utente costruisce il suo prompt con il contesto fornito.

---

## ERRORI COMUNI DA EVITARE

**Design:**
- Accordion dove non serve — la semplicità è lusso
- Card ovunque — non tutto deve essere in una card
- Ombre uguali su tutto — le ombre hanno gerarchia
- Dark mode "invertita" — non è solo cambiare i colori

**Typography:**
- Usare Inter "perché è leggibile" — segnala template AI
- Bold word system su headings (troppo brevi, inutile)
- Letterspacing di default sugli headings display
- max-width mancante sui paragrafi

**Build:**
- Hex hardcoded nel CSS — rompe il sistema token
- Inline style per quick fix — accumula debito tecnico
- Placeholder text dimenticato nella consegna
- body::before grain con position:absolute invece di fixed

**Polish:**
- Saltare il pass Anti-AI perché "sembra già buono"
- Non fare il skeleton test sul bold word system
- Dimenticare il 20% zoom test per la gerarchia
- Grain con background-size > 200px (sembra pixelata)
