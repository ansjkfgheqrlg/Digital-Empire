# POLISH-LOOP-PROTOCOL
            
> Path: [[Map - Crea_Siti|Crea siti > skills > opus]]

## Content

# POLISH LOOP PROTOCOL — OPUS Anti-AI Refinement System
> Fase 9 del processo OPUS. Questa fase separa un sito da $500 da un sito da $50.000.
> **Minimum: 5 pass. Premium standard: 7 pass completi.**

---

## Filosofia del Polish Loop

Il Polish Loop non è "rivedere il codice" — è un **audit strutturato multi-pass** dove ogni iterazione ha un focus specifico e produce una lista di fix che vengono applicati prima del pass successivo.

La maggior parte dei siti AI-generated fallisce qui: vengono consegnati dopo 1 pass superficiale. OPUS esegue 7 pass dedicati, ciascuno con checklist precise e criteri di pass/fail chiari.

**Regola di base:**
- Ogni pass produce una lista di issue
- Tutte le issue vengono fixate prima di procedere al pass successivo
- Un issue Critical BLOCCA il pass — non si avanza finché non è risolto
- Il loop è completo solo quando tutti i 7 pass hanno ZERO Critical issue

---

## Setup del Polish Loop

Prima di iniziare qualsiasi pass:

```
9.0.1 Apri il sito in browser a 100% zoom (Chrome o Firefox)
9.0.2 Apri anche a 20% zoom (Ctrl/Cmd + − ripetuto) → test gerarchia visiva
9.0.3 Apri DevTools → Device emulation → iPhone 14 Pro (390px)
9.0.4 Tieni aperti SITE-DESIGN.md e ANTI-AI-BLACKLIST.md come riferimento
9.0.5 Crea lista issue per questo pass con 3 colonne: Elemento | Problema | Fix
```

---

## PASS 1 — ANTI-AI VERIFICATION
> Il pass più importante. Controlla ogni elemento contro la Blacklist OPUS.

**Obiettivo:** Eliminare tutto ciò che fa sembrare il sito "generato da AI".

### Checklist Pass 1

#### Font
- [ ] Font principale NON è Inter, Roboto, Arial, Helvetica o system-ui
- [ ] Font ha personalità riconoscibile (non "qualsiasi font di default")
- [ ] La coppia display + body crea tensione visiva interessante
- [ ] Font caricati correttamente — nessun fallback brutto visibile

#### Colori
- [ ] ZERO purple gradient su sfondo bianco (#8B5CF6, #6366F1, ecc.)
- [ ] ZERO pure black #000000 come colore principale
- [ ] ZERO pure white #FFFFFF come colore principale
- [ ] ZERO blue-to-purple o teal-to-blue gradient
- [ ] Accent color usato con parsimonia (<5% area visibile)
- [ ] Foundation layer occupa correttamente ~90% dello spazio
- [ ] Tutti i colori passano il test silver-mixed (nessuno completamente saturo)

#### Layout
- [ ] ZERO bottoni pill-shape (border-radius: 9999px) come unico stile
- [ ] Layout ha variazione — non 2-3 colonne simmetriche identiche su ogni sezione
- [ ] Grid ha asimmetria intenzionale in almeno 1-2 sezioni (7/5 o 8/4)
- [ ] ZERO "corporate anni 2010" (shadow su tutto, card ovunque, tutto boxed uguale)
- [ ] Almeno 1 sezione rompe il ritmo del layout per creare interesse

#### Il Test Finale Anti-AI
- [ ] **Sniff test:** il sito potrebbe essere stato generato da Wix, Framer AI, o qualsiasi AI template? Se SÌ → BLOCCANTE — torna alla Fase 4 e rifai il design system

### Esito Pass 1
- **PASS:** nessuna issue Critical → procedi a Pass 2
- **FAIL:** qualsiasi item critico fallisce → lista fix → applica → ripeti Pass 1

---

## PASS 2 — TYPOGRAPHY AUDIT
> Verifica che la tipografia comunichi lusso e gerarchia precisa.

**Obiettivo:** La tipografia deve essere leggibile a qualsiasi zoom, avere gerarchia cristallina, e comunicare qualità editoriale.

### Checklist Pass 2

#### Gerarchia Visiva
- [ ] Gerarchia a 5 livelli visibile al 20% zoom (display / heading / subhead / body / caption)
- [ ] Min 1.5x size difference tra livelli adiacenti — visibile a colpo d'occhio
- [ ] Display font (hero) è 3-5x il corpo — non meno
- [ ] Caption/label è riconoscibile come "metadata" (piccolo + uppercase + tracking)

#### Letter-Spacing
- [ ] Hero display (≥67px): letter-spacing negativo (-0.02em o meno) ✓
- [ ] H1-H2 (50-38px): letter-spacing leggermente negativo (-0.01em) ✓
- [ ] Label/nav (uppercase): letter-spacing largo (+0.12em a +0.20em) ✓
- [ ] Body text: neutro o leggermente positivo (+0.01em) ✓
- [ ] ZERO letter-spacing "default" su display — il tracking non è dettaglio, è qualità

#### Line-Height e Baseline Grid
- [ ] Display/hero: line-height 1.0–1.1 (tight leading = premium)
- [ ] Body: line-height 1.6–1.7 (lettura confortevole)
- [ ] Ogni line-height × font-size = numero divisibile per 4 (baseline grid)
  - Es: 16px × 1.5 = 24px ✓ | 16px × 1.45 = 23.2px ✗
- [ ] `text-wrap: balance` attivo su tutti gli heading (evita orphan words sull'ultima riga)

#### Bold Word System
- [ ] Bold word system presente nei paragrafi corpo (features, about, how it works)
- [ ] Font-weight bold usa 600 (semibold) — non 700 nei paragrafi corpo
- [ ] **Skeleton test:** leggendo SOLO le parole in grassetto si capisce il messaggio?
- [ ] Densità corretta: ~1 parola/frase boldata ogni 15-20 parole
- [ ] Nessuna intera frase in grassetto (distrugge il sistema)

#### Lowercase/Case Style
- [ ] H1, H2, H3 in sentence case (minuscolo, prima lettera maiuscola)
- [ ] ZERO Title Case sugli heading (troppo corporate)
- [ ] Label/nav in UPPERCASE con wide tracking (contrasto visivo con headings)
- [ ] Nomi propri e acronimi rispettano le eccezioni (maiuscola corretta)

#### Technical Font
- [ ] Font preload: `<link rel="preload" as="font">` per il display font principale
- [ ] `font-display: swap` su tutti i custom font
- [ ] Fluid typography: clamp() attivo su display e H1 (non solo breakpoint)
- [ ] Max 2 font families (eccezionalmente 3) — non di più

### Esito Pass 2
- **PASS:** gerarchia chiara a 20% zoom + skeleton test superato + tracking corretto
- **FAIL:** qualsiasi item tipografico critico → lista fix → applica → ripeti Pass 2

---

## PASS 3 — SPACING & RHYTHM AUDIT
> Verifica che il ritmo spaziale comunichi lusso attraverso il respiro.

**Obiettivo:** Ogni spazio deve venire dalla scala matematica. Il "vuoto" deve sembrare "costoso", non "mancante".

### Checklist Pass 3

#### Scala Matematica
- [ ] OGNI valore di margin/padding viene dalla spacing scale (4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 160, 192px)
- [ ] ZERO valori arbitrary (17px, 23px, 37px, 45px) — questi segnalano AI-generated
- [ ] Gap tra elementi di una grid: dalla scala
- [ ] Border-radius: coerente con il sistema (0px / 2px / 8px / 16px — non mix)

#### Section Padding
- [ ] Sezioni standard desktop: padding-block ≥ 128px (--space-16) — il minimum luxury
- [ ] Hero: padding-block ≥ 160px (--space-20)
- [ ] CTA finale: padding-block ≥ 128px — mai compresso
- [ ] `clamp()` attivo su section padding: `clamp(4rem, 8vw, 10rem)`

#### Negative Space
- [ ] Il negative space si "sente" come costoso (non come dimenticato)
- [ ] Hero ha abbastanza aria intorno all'headline — non soffocato
- [ ] Sezioni non sono troppo vicine — ogni sezione "respira"

#### Layout Ratios
- [ ] Almeno 1-2 sezioni usano ratio asimmetrico (7/5, 8/4, 3/7) — non sempre 6/6
- [ ] Full-bleed vs container usati con intenzione (non tutti uguali)
- [ ] Content max-width: 1200-1400px centrato (non full-width su desktop)

#### Heading → Body Gap
- [ ] Gap tra section heading e primo paragrafo: min 32px (--space-6)
- [ ] Gap tra H2 e H3: min 48px di margin superiore sull'H2
- [ ] Paragrafi corpo: max 68ch di larghezza (regola di leggibilità)
- [ ] Spaziatura tra paragrafi: 24-32px (--space-5/6) — mai uguale a line-height

### Esito Pass 3
- **PASS:** tutti gli spacing dalla scala + section padding ≥128px + negative space generoso
- **FAIL:** qualsiasi arbitrary value trovato → fix → ripeti Pass 3

---

## PASS 4 — COLOR, CONTRAST & GRAIN AUDIT
> Verifica palette, contrasto WCAG, grain texture e dark/light mode.

**Obiettivo:** Palette luxury (silver-mixed, accent parsimonioso), accessibilità WCAG AA, grain presente e corretta.

### Checklist Pass 4

#### Architettura Colore
- [ ] Foundation layer (~90% area): surface, surface-2, surface-3 distinte (3-4% lightness shift)
- [ ] Accent color: davvero <5% dell'area visibile? Non sovrausato?
- [ ] Borders sono rgba barely-visible — NON solid opachi dominanti
  - Dark: rgba(255,255,255,0.06-0.10)
  - Light: rgba(0,0,0,0.06-0.10)
- [ ] Colored shadows usate (non grigio neutro puro)
- [ ] Silver-mixed: nessun colore ha saturazione >65%

#### Contrasto WCAG AA
- [ ] Body text (16px): contrasto ≥ 4.5:1 su background
- [ ] Large text (≥18px o ≥14px bold): contrasto ≥ 3:1
- [ ] Interactive elements (button, link): contrasto ≥ 3:1 per indicatori UI
- [ ] Muted text: contrasto ≥ 4.5:1 (non troppo dimmed da essere illeggibile)

#### Grain Texture — QUALITY GATE OBBLIGATORIO
La grain è la firma finale del design premium. Verificare con cura.

- [ ] `body::before` con grain presente nel CSS
- [ ] Usa **SVG feTurbulence inline** (`data:image/svg+xml`) — **NON PNG/JPEG importato**
- [ ] `position: fixed` su body::before (non absolute — causerebbe salti allo scroll)
- [ ] `background-size ≤ 200px` dark / `≤ 150px` light — **MAI `auto` o `100%` o `400px+`**
- [ ] `opacity` nel range corretto: dark 4-6% | light 2.5-3.5% — **MAI sopra 8%**
- [ ] `mix-blend-mode: overlay` (dark) o `soft-light` (light)
- [ ] `pointer-events: none` attivo — la grain non intercetta click/touch
- [ ] `z-index: 9999` (sopra tutto il contenuto visivo, tranne modal/overlay UI)
- [ ] Adattamento dark/light con `[data-theme]` — opacity e background-size si adattano
- [ ] Mobile: `opacity: 0.03`, `background-size: 120px` (più fine e discreta)
- [ ] Verificato visivamente: la grain si **SENTE** come finitura, non si **VEDE** come elemento
- [ ] Verificato su Retina/HiDPI: grain nitida, zero pixelazione

**Se la grain sembra pixel → riduci background-size. NON aumentare baseFrequency come prima mossa.**

#### Dark/Light Mode
- [ ] Dark mode: 3 livelli surface distinti (ogni livello 3-4% più chiaro del precedente)
- [ ] Light mode: surface warm (non pure white) — es. #faf9f5
- [ ] Toggle visibile in navbar (sun/moon icon, 44×44px touch target)
- [ ] Preferenza salvata in localStorage (`opus-theme`)
- [ ] `prefers-color-scheme` come fallback se nessuna preferenza salvata
- [ ] Transizione smooth tra temi (300ms su background-color e color)

### Esito Pass 4
- [ ] **PASS:** contrasto WCAG ✓ + grain corretta ✓ + foundation layer 90% ✓
- [ ] **FAIL:** grain mancante o sbagliata = BLOCCANTE → fix → ripeti Pass 4

---

## PASS 5 — COMPONENT STATES AUDIT
> Verifica che ogni componente interattivo abbia tutti i suoi stati.

**Obiettivo:** Un sito premium ha stati ricchi e curati su ogni elemento interattivo. Ogni interaction è un'opportunità di mostrare qualità.

### Checklist Pass 5

#### Button (tutti i bottoni)
- [ ] 5 stati presenti: default / hover / focus / active / disabled
- [ ] **Hover:** background fill o cambiamento visivo evidente + letter-spacing expand (0.15em → 0.18em)
- [ ] **Focus:** outline visibile e STILIZZATO (non il browser default brutto blu)
  - Alternativa premium: outline offset + colore accent custom
- [ ] **Active:** leggermente pressed (scale 0.98 o background più scuro)
- [ ] **Disabled:** opacity 0.4 + cursor: not-allowed
- [ ] Transition duration corretta: 150-300ms con easing (ease-out-quart)
- [ ] Button padding: generoso (min 14px 32px) — non striminzito
- [ ] Border-radius coerente col sistema (NON 9999px pill su tutti)

#### Cards
- [ ] Hover: translateY(-4 a -6px) + shadow expansion
- [ ] Box-shadow su hover parte da shadow più piccola e si espande
- [ ] Immagine dentro card: scale 1.0 → 1.05 su hover (overflow:hidden sul container)
- [ ] Shimmer effect su card premium (::before gradient da sinistra a destra)
- [ ] Transition: 300ms ease-out-quart su tutto

#### Navigation
- [ ] Thin (56-64px height) — non chunky e pesante
- [ ] Sticky con backdrop-filter: blur(20px) attivo
- [ ] Dopo 80px scroll: background opacity aumenta + height shrink (64px → 48px)
- [ ] Nav items uppercase + letter-spacing 0.15-0.20em
- [ ] Current page: indicatore stilizzato (underline animato o punto sottile)
- [ ] Mobile drawer: off-canvas elegante (non hamburger brutto) con slide animation
- [ ] aria-expanded + aria-controls su hamburger button

#### Form Inputs
- [ ] Height: 48px (touch-friendly + premium)
- [ ] 4 stati: default / focus / error / disabled
- [ ] Focus: border colore accent (non solo outline browser default)
- [ ] Error: messaggio di errore visibile + colore semantic error
- [ ] Label: above input, uppercase tracking, non placeholder-as-label

#### Focus Management (Accessibility)
- [ ] Skip-to-content link presente e funzionante (first tab press visibile)
- [ ] Focus visible su TUTTI gli elementi interattivi
- [ ] Focus trap nei modal/drawer (Tab rimane dentro)
- [ ] Escape chiude modal/drawer/menu

### Esito Pass 5
- **PASS:** tutti i 5 stati button + hover cards + nav scroll behavior
- **FAIL:** qualsiasi stato mancante su elementi prominenti → fix → ripeti Pass 5

---

## PASS 6 — MOTION AUDIT
> Verifica che ogni animazione serva la UX e rispetti gli standard di timing.

**Obiettivo:** Le animazioni guidano l'attenzione e danno feedback. Nessuna animazione è puramente decorativa.

### Checklist Pass 6

#### Transizioni Base
- [ ] Ogni elemento interattivo ha transition eased — **ZERO transizioni istantanee**
- [ ] Hover states usano easing corretto: `ease-out-quart` o simile
- [ ] Nessuna transizione usa `linear` (appare meccanica) a meno che intenzionale
- [ ] `transition: all` evitato — preferire proprietà specifiche (transform, opacity, box-shadow)

#### Scroll Animations
- [ ] Scroll reveal (fade-up + stagger) su: card, feature, team, testimonial
  - translateY(20px → 0) + opacity(0 → 1)
  - duration: 500ms, easing: ease-out-expo
  - stagger: 60ms su grid items
  - `once: true` (non ri-anima su scroll up)
- [ ] IntersectionObserver threshold: 0.1 (parte appena entra nel viewport)

#### Hero Entrance Sequence
- [ ] Timeline orchestrata (non tutto appare insieme):
  - 0ms: badge/label → fadeIn + slideUp 20px, 400ms
  - 100ms: H1 headline → fadeIn + slideUp 30px, 600ms
  - 250ms: subheadline → fadeIn + slideUp 20px, 500ms
  - 400ms: CTA buttons → fadeIn + stagger 80ms, 400ms
  - 500ms: visual/image → fadeIn, 600ms

#### Counter Animations
- [ ] Counters numerici: animazione al viewport entry
- [ ] Duration: 1200ms ease-out-expo (rallenta verso il numero finale)
- [ ] Formato preservato durante animazione (1.234 o 98% — non "1234")

#### Performance & Accessibility
- [ ] `@media (prefers-reduced-motion: reduce)` → disabilita TUTTE le animazioni
- [ ] Mobile ≤768px: animazioni pesanti ridotte o disabilitate
- [ ] `passive: true` su tutti gli scroll event listener
- [ ] Animazioni usano SOLO `transform` e `opacity` — **VIETATO** animare width/height/top/left/margin
- [ ] Duration MAX: 1200ms per singola animazione — mai superare
- [ ] Fallback graceful se libreria CDN non carica (try/catch nell'init)

### Esito Pass 6
- **PASS:** zero transizioni istantanee + prefers-reduced-motion + hero sequence
- **FAIL:** transizioni istantanee su hover o mancanza prefers-reduced-motion → fix → ripeti

---

## PASS 7 — DETAIL SWEEP
> Il 1% che vale il 50% del valore percepito. I dettagli che separano l'artigianato dalla produzione.

**Obiettivo:** Perfezionare ogni dettaglio finale — footer, favicon, OG image, 404, tipografia fine.

### Checklist Pass 7

#### Pagine Speciali
- [ ] **404 page:** branded, coerente col design, non pagina default del browser/server
  - Testo: spiritoso o elegante, non generico "Page Not Found"
  - Link di ritorno alla home
  - Stessa navbar e footer
- [ ] **Thank You page** (PATH A): presente, di qualità, con prossimi passi chiari
- [ ] **Privacy Policy + Cookie Policy:** template GDPR compilato, link in footer

#### Footer
- [ ] Stessa cura del hero (non abbandonato o rushed)
- [ ] Anno copyright dinamico via JS (`new Date().getFullYear()`)
- [ ] Link legali: Privacy, Cookie, eventuali Termini
- [ ] Separato dal body con divider (gradient silver line o surface transition)
- [ ] Font size e spacing coerenti col design system (non dimenticati)

#### Favicon & Icons
- [ ] SVG favicon (scalabile, moderno)
- [ ] 192×192px PNG per Android/PWA
- [ ] 512×512px PNG per high-res
- [ ] Apple touch icon (180×180px)
- [ ] `<meta name="theme-color">` con colore brand

#### Social/SEO Details
- [ ] OG image (1200×630px) presente per ogni pagina — coerente col design
- [ ] OG image testata su social card preview tool
- [ ] `<meta name="viewport">` include `maximum-scale=1` (no zoom su input iOS)
- [ ] Theme color: `<meta name="theme-color" content="[colore surface dark]">`

#### Tipografia Fine
- [ ] `text-wrap: balance` su TUTTI gli headings — evita "lonely words" sull'ultima riga
- [ ] Orphan/widow check nei paragrafi lunghi (manually se necessario)
- [ ] Link nel corpo del testo: underline visibile + accent color (accessibility + design intent)
- [ ] Nessun "Lorem ipsum" o placeholder text rimasto

#### Loading & Performance
- [ ] Blur-up placeholder sulle immagini → full resolution (non spinner grezzo)
- [ ] `loading="lazy"` su immagini below-the-fold
- [ ] `fetchpriority="high"` sull'immagine hero (LCP element)
- [ ] Font preload: `<link rel="preload" as="font" type="font/woff2" crossorigin>`

#### Condizionali Premium
- [ ] Lenis smooth scroll: inizializzato e funzionante (se incluso)
- [ ] Scroll progress bar (solo pagine long-form — blog, case study, landing lunga)
- [ ] Custom cursor (SOLO brand lusso high-end — altrimenti ometti)

---

## Trigger Anti-Gravity — Fase 9 Pass 7

Dopo aver completato il Pass 7, questo è il **momento AG-7: Polish Review Finale**.

opus-director fornisce all'utente il contesto completo del progetto per costruire il prompt Anti-Gravity:
- Aesthetic axis scelto
- Font display + body + motivazione
- Palette principale + accent
- Tipo sito + audience
- Sezioni presenti
- Eventuali compromessi fatti durante il build

L'utente porta questo contesto in Anti-Gravity e chiede: **"Cosa ancora sembra AI? Dove posso spingere oltre?"**

---

## Polish Loop Summary — Tabella di Tracking

Tieni traccia dei pass completati nell'OPUS-STATUS.md:

| Pass | Focus | Issue trovate | Fix applicati | Status |
|------|-------|--------------|---------------|--------|
| 1 | Anti-AI Verification | — | — | ⏳ |
| 2 | Typography Audit | — | — | ⏳ |
| 3 | Spacing & Rhythm | — | — | ⏳ |
| 4 | Color, Contrast, Grain | — | — | ⏳ |
| 5 | Component States | — | — | ⏳ |
| 6 | Motion Audit | — | — | ⏳ |
| 7 | Detail Sweep | — | — | ⏳ |

**Stato finale:** Polish Loop COMPLETATO — standard $50.000 verificato ✅

---

## Regola dei Livelli di Severity

| Severity | Definizione | Azione |
|----------|-------------|--------|
| **CRITICAL** | Viola la blacklist / WCAG AA / funzionalità rotta | BLOCCA il pass — fix immediato obbligatorio |
| **HIGH** | Degrada qualità premium significativamente | Fix pre-deploy raccomandato |
| **MEDIUM** | Imperfezione visibile ma non bloccante | Documenta, fix next sprint |
| **LOW** | Micro-dettaglio migliorabile | Backlog |

**Regola:** ZERO Critical per completare il Polish Loop. ZERO Critical per approvare il deploy.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Crea_Siti|Crea Siti Area]]
