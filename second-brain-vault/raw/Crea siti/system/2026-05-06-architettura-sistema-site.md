# ARCHITETTURA-SISTEMA-SITE

> Source: File system (`Crea siti\system\ARCHITETTURA-SISTEMA-SITE.md`)
> Collected: 2026-05-06
> Published: Unknown

# Architettura Sistema `site` — Blueprint Completo

**Data:** 28 Marzo 2026
**Autore:** Piano strategico Digital Empire
**Scopo:** Documento di riferimento per la creazione di tutte le skill, agenti e flussi mancanti del sistema di creazione siti web.

---

## Stato Attuale (Già Creati)

| Elemento | Tipo | File | Stato |
|---------|------|------|-------|
| `site` | Skill orchestratore | `skills/site/SKILL.md` | ✅ Creato |
| `site-brief` | Skill | `skills/site-brief/SKILL.md` | ✅ Creato |
| `site-stack` | Skill | `skills/site-stack/SKILL.md` | ✅ Creato |
| `site-plan` | Skill | `skills/site-plan/SKILL.md` | ✅ Creato |
| `site-copy` | Skill | `skills/site-copy/SKILL.md` | ✅ Creato |
| `site-build` | Skill | `skills/site-build/SKILL.md` | ✅ Creato |

---

## Elementi Da Creare

---

# PARTE A — SKILL (8 rimanenti)

---

## SKILL: `site-design`

**File da creare:** `C:\Users\Utente\.claude\skills\site-design\SKILL.md`
**Comando:** `/site design`
**Wave:** 2

### Descrizione (frontmatter)
> "Crea il sistema visivo completo del sito: filosofia estetica, palette colori, tipografia, spacing scale, componenti UI e atmosfera. Invoca frontend-design per le linee guida estetiche. Produce SITE-DESIGN.md (documentazione), design-tokens.css (variabili CSS) e style-guide.html (guida visiva)."

### Input Necessari
- `SITE-BRIEF.md` — obbligatorio (mood, colori, riferimenti estetici)
- `SITE-STACK.md` — obbligatorio (Percorso A/B/C determina formato token)
- `BRAND-VOICE.md` — opzionale (se presente, allinea estetica alla voce brand)

### Processo (step by step)
1. **FILOSOFIA VISIVA** — definisci un "nome del movimento" (es. "Minimal Authority", "Organic Warmth") e 3 principi visivi che guidano ogni scelta
2. **PALETTE COLORI** — genera custom properties CSS: primario (con varianti 50–900), secondario, accent, semantici (success/warning/error), surface (bg, bg-secondary, surface), testo (text, text-muted, text-inverse), bordo (border, border-focus)
3. **TIPOGRAFIA** — seleziona font caratterizzanti (MAI Inter/Roboto/Arial come unico font display): font display per headline, font body per testo, font mono se SaaS/tech. Genera scale da `--text-xs` a `--text-6xl` con size, line-height, letter-spacing
4. **SPACING E LAYOUT** — scale 4px base × moltiplicatori standard, grid system, breakpoints (sm/md/lg/xl/2xl), border-radius scale
5. **COMPONENTI VISUAL** — specifica visual di: button (varianti primary/secondary/ghost, sizes sm/md/lg, stati hover/focus/disabled), card, badge, form input, divisori
6. **ATMOSFERA** — gradient mesh, texture noise, pattern, colored shadows, hover effects premium
7. **INVOCA `frontend-design`** — per validazione aesthetics e allineamento al mood
8. **GENERA 3 FILE:** `SITE-DESIGN.md`, `design-tokens.css`, `style-guide.html`
9. Per Percorso B (Next.js) — genera anche `tailwind.config.js` con token integrati

### Output Files
- `SITE-DESIGN.md` — documentazione sistema di design (filosofia, palette, tipografia, componenti)
- `design-tokens.css` — tutte le CSS custom properties in un file
- `style-guide.html` — pagina HTML autonoma con swatches colori, scale tipografica, componenti visualizzati (no server richiesto)
- `tailwind.config.js` — solo Percorso B

### Regole Critiche
- Mai palette generica — ogni progetto ha colori distinti e motivati
- Il `style-guide.html` funziona aprendo il file nel browser (no dipendenze locali tranne font CDN)
- I CSS custom properties sono la fonte di verità — zero magic numbers nel CSS successivo

---

## SKILL: `site-animate`

**File da creare:** `C:\Users\Utente\.claude\skills\site-animate\SKILL.md`
**Comando:** `/site animate`
**Wave:** 2 (dopo `/site build`)

### Descrizione (frontmatter)
> "Aggiunge animazioni e motion design al sito già costruito. Seleziona la libreria ottimale in base allo stack (Motion per React, GSAP per HTML puro, Anime.js per micro-animazioni, Lottie per animazioni JSON). Implementa scroll triggers, page transitions, micro-interactions e counter animations."

### Input Necessari
- `SITE-STACK.md` — obbligatorio (determina quale libreria animation usare)
- `SITE-BUILD.md` — obbligatorio (manifest dei file esistenti)
- `index.html` e altri file HTML/JSX — da modificare con le animazioni
- `SITE-BRIEF.md` — per capire intensità animazioni (portfolio creativo vs corporate sobrio)

### Decisione Libreria (albero)

```
Stack è React/Next.js?
  └── Sì → usa Motion (ex Framer Motion)
      └── Portfolio creativo premium? → aggiungi GSAP ScrollTrigger
  └── No (HTML puro) →
      └── Animazioni complesse/timeline? → GSAP
      └── Micro-animazioni/SVG? → Anime.js
      └── Hai file .json Lottie? → lottie-web
      └── Sito corporate sobrio? → CSS transitions pure (no JS library)
```

### Animazioni Standard da Implementare
1. **Scroll reveal** — elementi che appaiono entrando nel viewport (fade-up, fade-in, scale-in)
2. **Navbar scroll** — header che cambia sfondo/ombra dopo X pixel di scroll
3. **Hero entrance** — animazione di ingresso elementi hero al caricamento pagina
4. **Counter animations** — numeri che contano fino al valore finale quando entrano in viewport
5. **Hover effects JS** — card tilt, magnetic buttons, cursor personalizzato (solo portfolio premium)
6. **Page transitions** — dissolvenza tra pagine (solo Percorso B/React)
7. **Parallax sottile** — elementi hero con movimento parallax leggero (non esagerato)
8. **Stagger animations** — liste, card, feature grid che appaiono in sequenza

### Intensità per Tipo di Sito
- **Landing page / SaaS:** scroll reveals + counter animations + hero entrance
- **Portfolio creativo:** tutto incluso magnetic buttons, cursor custom, page transitions
- **Sito business/corporate:** solo scroll reveals sobri + navbar scroll (niente di aggressivo)
- **E-commerce:** add-to-cart feedback, image zoom, loading skeleton states
- **Blog:** solo scroll reveals leggeri

### Output Files
- `js/animations.js` — file dedicato alle animazioni (non mischiare con interactions.js)
- File HTML/JSX aggiornati con classi/attributi per trigger animazioni
- Per GSAP: include CDN link nell'head HTML
- Per Motion: import nel layout.tsx o nelle pagine

### Aggiorna SITE-STATUS.md
Segna Animate come completato.

---

## SKILL: `site-seo`

**File da creare:** `C:\Users\Utente\.claude\skills\site-seo\SKILL.md`
**Comando:** `/site seo`
**Wave:** 2 (dopo `/site build`)

### Descrizione (frontmatter)
> "Ottimizza il sito per i motori di ricerca a livello tecnico e on-page. Inietta meta tag completi, Open Graph, JSON-LD schema markup, genera sitemap.xml e robots.txt. Produce SEO-AUDIT.md con checklist completa e priorità di intervento."

### Input Necessari
- Tutti i file `*.html` o `*.tsx` nella CWD — da analizzare e aggiornare
- `SITE-PLAN.md` — per URL structure e pagine
- `SITE-COPY.md` — per keyword e meta descriptions già scritte
- `SITE-BRIEF.md` — per keyword focus, tipo sito, nome brand
- `SEO-AUDIT.md` da `/market seo` — se presente, incrociare con findings esistenti

### Processo
1. **AUDIT ESISTENTE** — analizza ogni file HTML: title tag presenti? meta description? heading hierarchy corretta? alt text sulle immagini?
2. **INIETTA META TAG** — per ogni pagina, aggiungi/correggi: `<title>`, `<meta name="description">`, `<meta property="og:*">`, `<meta name="twitter:*">`, `<link rel="canonical">`
3. **SCHEMA JSON-LD** — seleziona schema appropriato per tipo sito:
   - Tutti: `Organization`, `WebSite`, `WebPage`
   - Business: `LocalBusiness`, `ContactPage`
   - Portfolio: `Person`, `CreativeWork`
   - E-commerce: `Product`, `BreadcrumbList`, `AggregateRating`, `Offer`
   - SaaS: `SoftwareApplication`, `FAQ`
   - Blog: `Article`, `BlogPosting`, `Author`
4. **GENERA sitemap.xml** — tutte le URL del sito con `<lastmod>` e `<priority>`
5. **GENERA robots.txt** — Disallow per pagine private (admin, staging, grazie), Allow tutto il resto
6. **HEADING HIERARCHY** — verifica che ogni pagina abbia esattamente un H1 e gerarchia corretta H2→H3
7. **PERFORMANCE SEO** — immagini senza alt text, link senza testo descrittivo, meta description duplicate

### Schema JSON-LD da Includere Sempre
```json
// Organization (in ogni pagina, di solito nel footer o head)
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[nome brand]",
  "url": "[url sito]",
  "logo": "[url logo]",
  "sameAs": ["[social URL 1]", "[social URL 2]"]
}

// BreadcrumbList (in pagine interne)
// FAQPage (se presente sezione FAQ)
// ecc. in base al tipo sito
```

### Output Files
- `sitemap.xml` — generato nella root del progetto
- `robots.txt` — generato nella root
- File HTML aggiornati con meta tag + JSON-LD iniettati
- `SEO-AUDIT.md` — checklist con: ✅ elementi OK, ❌ elementi mancanti/errati, priorità fix

### Aggiorna SITE-STATUS.md
Segna SEO come completato.

---

## SKILL: `site-qa`

**File da creare:** `C:\Users\Utente\.claude\skills\site-qa\SKILL.md`
**Comando:** `/site qa`
**Wave:** 2 (in parallelo con `/site seo`)

### Descrizione (frontmatter)
> "Quality assurance completo del sito web. Lancia 4 agenti in parallelo: site-qa-html (validità e struttura), site-qa-accessibility (WCAG 2.1 AA), site-qa-performance (Core Web Vitals), site-qa-mobile (responsive e cross-browser). Produce QA-REPORT.md con severity rating e fix instructions."

### Input Necessari
- Tutti i file `*.html`, `*.css`, `*.js` nella CWD
- `SITE-BUILD.md` — per il manifest dei file
- `SITE-PLAN.md` — per verificare che tutte le pagine siano state costruite

### Processo
1. **Leggi tutti i file** del progetto per avere il contesto completo
2. **Lancia 4 agenti in parallelo:**
   - `site-qa-html` — validità HTML, struttura semantica
   - `site-qa-accessibility` — WCAG 2.1 AA compliance
   - `site-qa-performance` — performance e Core Web Vitals
   - `site-qa-mobile` — responsive e cross-browser
3. **Raccogli i risultati** dai 4 agenti
4. **Calcola il Site Quality Score** — media pesata delle 4 dimensioni
5. **Aggrega e prioritizza** — Critical (blocca deploy), High, Medium, Low
6. **Genera QA-REPORT.md**

### Scoring
| Dimensione | Peso | Range |
|-----------|------|-------|
| HTML Quality | 25% | 0-100 |
| Accessibility | 30% | 0-100 |
| Performance | 25% | 0-100 |
| Mobile/Responsive | 20% | 0-100 |
| **TOTALE** | 100% | 0-100 |

### Gate di Deploy
Se il QA-REPORT contiene issue con severity "Critical" → il comando `/site deploy` deve mostrare un warning e chiedere conferma esplicita prima di procedere.

### Output Files
- `QA-REPORT.md` — report completo con sezioni per ogni agente, scoring, fix instructions

### Aggiorna SITE-STATUS.md
Segna QA come completato. Se ci sono critical issues, aggiungili ai Blockers.

---

## SKILL: `site-deploy`

**File da creare:** `C:\Users\Utente\.claude\skills\site-deploy\SKILL.md`
**Comando:** `/site deploy [platform]`
**Wave:** 3 (ultima fase prima del report)

### Descrizione (frontmatter)
> "Prepara il sito per il deploy su Vercel, Netlify, GitHub Pages o hosting generico. Verifica che QA non abbia blockers critici, genera i file di configurazione specifici per la piattaforma, e produce DEPLOY-CHECKLIST.md con tutti i passaggi pre-lancio."

### Argomenti Supportati
- `/site deploy vercel` — genera `vercel.json`
- `/site deploy netlify` — genera `netlify.toml`
- `/site deploy github` — genera `.github/workflows/deploy.yml`
- `/site deploy generic` — genera guide per FTP/hosting condiviso
- `/site deploy` senza argomenti — chiede quale piattaforma scegliere basandosi su SITE-STACK.md

### Prerequisiti (verifica prima di procedere)
1. Leggi `QA-REPORT.md` — se ci sono issue "Critical" non risolte, mostra warning
2. Verifica che `sitemap.xml` esista (da `/site seo`)
3. Verifica che `robots.txt` esista
4. Verifica che `index.html` o app Next.js esista

### Configurazioni da Generare

**Vercel (`vercel.json`):**
```json
{
  "cleanUrls": true,
  "trailingSlash": false,
  "headers": [
    { "source": "/(.*)", "headers": [
      { "key": "X-Content-Type-Options", "value": "nosniff" },
      { "key": "X-Frame-Options", "value": "DENY" },
      { "key": "X-XSS-Protection", "value": "1; mode=block" }
    ]}
  ],
  "redirects": [{ "source": "/index.html", "destination": "/", "permanent": true }]
}
```

**Netlify (`netlify.toml`):**
```toml
[build]
  publish = "."
  command = ""

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    X-Frame-Options = "DENY"

[[redirects]]
  from = "/index.html"
  to = "/"
  status = 301
```

**GitHub Actions (`deploy.yml`):**
```yaml
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v4
      - uses: actions/upload-pages-artifact@v3
        with:
          path: '.'
      - uses: actions/deploy-pages@v4
```

### Checklist Pre-Lancio (`DEPLOY-CHECKLIST.md`)
Include sezioni:
- [ ] Verifica tecnica (file presenti, link funzionanti, form backend configurato)
- [ ] SEO check (sitemap.xml, robots.txt, meta tag su ogni pagina)
- [ ] Performance check (immagini ottimizzate, nessun file enorme)
- [ ] Accessibility check (nessun critical issue da QA)
- [ ] Analytics (GA4 o altro tracker configurato)
- [ ] Dominio (DNS configurato, SSL attivo)
- [ ] Form backend (endpoint configurato, email di notifica testata)
- [ ] Cookie banner (se raccoglie dati utente)
- [ ] Privacy policy e Cookie policy presenti
- [ ] Test cross-browser (Chrome, Firefox, Safari, Edge)
- [ ] Test mobile (iOS Safari, Chrome Android)
- [ ] 404 page personalizzata presente

### Output Files
- `vercel.json` / `netlify.toml` / `.github/workflows/deploy.yml` (in base alla piattaforma)
- `DEPLOY-CHECKLIST.md` con tutti gli item

### Aggiorna SITE-STATUS.md
Segna Deploy come completato.

---

## SKILL: `site-components`

**File da creare:** `C:\Users\Utente\.claude\skills\site-components\SKILL.md`
**Comando:** `/site components [nome-componente]`
**Wave:** 3 (tool di iterazione post-build)

### Descrizione (frontmatter)
> "Genera o rigenera componenti UI isolati. Utile per iterazione post-lancio senza ricostruire l'intero sito. Ogni componente è un file HTML standalone con CSS e JS inline, completamente funzionante nel browser."

### Componenti Standard Riconosciuti
| Argomento | Componente Generato |
|---------|-------------------|
| `navbar` | Navbar responsive con hamburger menu e dropdown |
| `hero` | Sezione hero con headline, subheadline, CTA, immagine |
| `features` | Griglia feature card con icone |
| `pricing` | Tabella prezzi con toggle mensile/annuale |
| `testimonials` | Sezione testimonial con carousel o grid |
| `faq` | Accordion FAQ con animazione apertura/chiusura |
| `contact` | Form di contatto con validazione |
| `footer` | Footer con colonne link e social |
| `cta-banner` | Sezione CTA con background colorato |
| `team` | Griglia team card con foto e bio |
| `gallery` | Portfolio/gallery con lightbox |
| `stats` | Sezione statistiche con counter animation |

### Processo
1. Leggi `SITE-DESIGN.md` e `design-tokens.css` — applica il design system esistente
2. Leggi la sezione rilevante di `SITE-COPY.md` — usa i testi già scritti
3. Genera il componente come file HTML standalone: CSS inline o in `<style>`, JS in `<script>`
4. Il file deve funzionare aprendo nel browser in isolamento
5. Aggiorna `SITE-BUILD.md` aggiungendo il componente al registro

### Output Files
- `components/[nome-componente].html` — componente standalone
- `SITE-BUILD.md` aggiornato

---

## SKILL: `site-report`

**File da creare:** `C:\Users\Utente\.claude\skills\site-report\SKILL.md`
**Comando:** `/site report`
**Wave:** 3 (ultimo step)

### Descrizione (frontmatter)
> "Genera il report finale da consegnare al cliente. Aggrega tutti gli output del progetto in un documento completo che mostra le decisioni prese, il design system, i risultati del QA, la checklist di deploy e i prossimi passi consigliati post-lancio."

### Input
Legge tutto ciò che esiste nella CWD: SITE-BRIEF.md, SITE-STACK.md, SITE-PLAN.md, SITE-DESIGN.md, SITE-BUILD.md, SEO-AUDIT.md, QA-REPORT.md, DEPLOY-CHECKLIST.md, e — se presenti — MARKETING-AUDIT.md e LANDING-CRO.md da sessioni `/market`.

### Struttura del Report (SITE-REPORT.md)
1. **Cover** — nome progetto, data, tipo sito, URL finale
2. **Executive Summary** — 3-5 bullet punti su cosa è stato costruito e perché
3. **Brief e Obiettivi** — sintesi dei requisiti e come sono stati soddisfatti
4. **Decisioni di Stack** — perché è stato scelto quel percorso tecnico + repo usati
5. **Architettura Informativa** — sitemap e struttura pagine con motivazioni
6. **Sistema di Design** — filosofia visiva, palette, tipografia con screenshot/esempi
7. **Copywriting** — approccio al tono, headline chiave adottate
8. **Build Summary** — pagine create, componenti, file manifest
9. **Quality Assurance** — Site Quality Score con breakdown 4 dimensioni
10. **SEO Implementation** — schema markup usati, sitemap, meta highlights
11. **Deploy Guide** — piattaforma scelta, comandi, prossimi passi tecnici
12. **Post-Launch Recommendations** — azioni consigliate dopo il go-live:
    - `/market audit <url>` — analisi sito live dopo indicizzazione
    - `/market seo <url>` — SEO audit live
    - Content plan per blog (se presente)
    - A/B testing suggeriti
13. **Appendice** — file completo prodotti

### Output Files
- `SITE-REPORT.md` — documento finale completo, consegnabile al cliente

### Aggiorna SITE-STATUS.md
Segna Report come completato. Fase: "PROGETTO COMPLETATO ✅"

---

## SKILL: `site-3d`

**File da creare:** `C:\Users\Utente\.claude\skills\site-3d\SKILL.md`
**Comando:** `/site 3d`
**Wave:** 3 (solo per progetti premium)

### Descrizione (frontmatter)
> "Integra esperienze 3D nel sito usando Three.js (Percorso A HTML puro) o React Three Fiber + Drei (Percorso B React). Solo per portfolio creativi, SaaS premium, o product showcase dove l'esperienza 3D ha valore reale. Genera scene 3D per hero sections, product viewer o background interattivi."

### Quando Usarlo (NON sempre)
Usare SOLO se il brief menziona esplicitamente:
- Portfolio creativo / design / 3D artist
- Product showcase con oggetti fisici (gioielli, electronics, auto)
- SaaS con esperienza wow per differenziarsi
- Agency creativa / studio di design
NON usare per siti business normali, landing page semplici, blog.

### Tipologie di Scene 3D
1. **Hero 3D** — oggetto 3D rotante o interattivo nella hero section (es. logo 3D, prodotto, sfera astratta)
2. **Particle background** — campo di particelle 3D come sfondo della hero
3. **Product viewer** — visualizzatore 3D di prodotto con drag-to-rotate
4. **Abstract art** — geometria generativa come elemento decorativo
5. **Globe/Earth** — globo interattivo per aziende globali

### Implementazione per Percorso A (HTML + Three.js)
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<canvas id="hero-canvas"></canvas>
<script src="js/scene-3d.js"></script>
```

File `js/scene-3d.js`:
- Setup Scene, Camera, Renderer
- Oggetti geometrici con materiali (MeshStandardMaterial, ShaderMaterial)
- AmbientLight + DirectionalLight
- Resize handler (responsive)
- RequestAnimationFrame loop
- Mouse/touch interaction se rilevante

### Implementazione per Percorso B (React Three Fiber)
```bash
bun add @react-three/fiber @react-three/drei three
```
Componente React:
- `<Canvas>` come wrapper
- `useFrame` per animazioni
- `<OrbitControls>` per interazione drag
- `<Environment>` da Drei per illuminazione preset
- `<Suspense>` con fallback durante il caricamento

### Regole di Performance
- La scena 3D NON deve bloccare il caricamento del contenuto testuale
- Usa `Suspense` e lazy loading
- Fornisci sempre un fallback statico (immagine o gradiente) se WebGL non è supportato
- Targetizza 60fps su desktop, 30fps accettabile su mobile
- Disabilita la scena 3D su mobile se troppo pesante (usa CSS media query o `navigator.hardwareConcurrency < 4`)

### Output Files
- `js/scene-3d.js` (Percorso A) o `components/Scene3D.tsx` (Percorso B)
- File HTML/JSX aggiornati con canvas + import

---

# PARTE B — AGENTI (10 totali)

---

## AGENTE: `site-copy-hero`

**File da creare:** `C:\Users\Utente\.claude\agents\site-copy-hero.md`
**Lanciato da:** skill `site-copy` (in parallelo con site-copy-body e site-copy-meta)

### Frontmatter YAML
```yaml
name: site-copy-hero
description: >
  Use this agent when site-copy needs headline and above-the-fold copy for all pages.
  Specializes in H1/H2 pairs, subheadlines, primary CTAs, and brand taglines.
  Receives SITE-BRIEF.md and SITE-PLAN.md as context.
model: sonnet
color: yellow
tools:
  - Read
  - Write
```

### Identità e Missione
Sei un copywriter specializzato in above-the-fold copy. Scrivi le parole che un visitatore legge nei primi 3 secondi su ogni pagina — le più importanti, le più difficili, quelle che decidono se resta o se scappa.

### Processo
1. Leggi `SITE-BRIEF.md` — estrai: target, proposta di valore, tono, competitor
2. Leggi `SITE-PLAN.md` — identifica ogni pagina e il suo obiettivo primario
3. Per ogni pagina, scrivi:
   - **3 varianti di H1** — pain-point / outcome / curiosità
   - **H2 (subheadline)** — espande l'H1, specifica il target, anticipa il beneficio
   - **CTA primario** — verbo + beneficio (max 4 parole)
   - **CTA secondario** — opzione alternativa meno impegnativa
4. Per la homepage, scrivi anche la **tagline brand** (max 7 parole, 3 varianti)
5. Applica framework: AIDA per SaaS, PAS per problema-soluzione, 4U per urgenza

### Output Contract
Produce una sezione "HERO COPY" in `SITE-COPY.md` con headline, varianti, subheadline e CTA per ogni pagina.

### Regole
- Mai "Benvenuti nel nostro sito" o simili
- Sempre beneficio specifico, mai generico "miglioreremo il tuo business"
- H1 max 10 parole
- CTA con verbo attivo ("Inizia", "Ottieni", "Prenota", "Scopri") mai "Clicca qui" o "Invia"
- 3 varianti headline OBBLIGATORIE per ogni pagina principale

---

## AGENTE: `site-copy-body`

**File da creare:** `C:\Users\Utente\.claude\agents\site-copy-body.md`
**Lanciato da:** skill `site-copy` (in parallelo)

### Frontmatter YAML
```yaml
name: site-copy-body
description: >
  Use this agent when site-copy needs body copy for all non-hero sections.
  Specializes in features-to-benefits translation, social proof framing,
  about page narrative, FAQ, and all mid-page content.
model: sonnet
color: orange
tools:
  - Read
  - Write
```

### Identità e Missione
Sei il copywriter delle sezioni body. Scrivi il testo che converte dopo che l'headline ha catturato l'attenzione: features tradotte in benefits, storie di clienti, spiegazioni chiare del prodotto, sezioni about che creano connessione umana.

### Processo
1. Leggi `SITE-BRIEF.md` e `SITE-PLAN.md`
2. Leggi la sezione HERO di `SITE-COPY.md` per coerenza tono
3. Per ogni sezione non-hero identificata nel piano, scrivi:
   - **Features/Benefits:** per ogni feature, trascrivi in "Cosa significa per te: [beneficio concreto]"
   - **Social Proof:** framing dei testimonial, statistiche, loghi clienti
   - **About/Chi Siamo:** narrazione umana, origine del brand, perché esiste
   - **How It Works:** 3-5 step chiari, linguaggio di azione
   - **FAQ:** 5-8 domande reali con risposte oneste (includi obiezioni di acquisto)
   - **Pricing descriptions:** testo delle tier/piani, cosa include, per chi è
4. Mantieni il tono coerente con il HERO copy

### Output Contract
Produce sezione "BODY COPY" per ogni pagina in `SITE-COPY.md`.

### Regole
- Mai jargon tecnico senza spiegazione
- Paragrafi max 3 frasi
- Sezione FAQ: includi almeno 2 obiezioni di acquisto ("È sicuro?" "Posso disdire?")
- About page: includi un elemento umano/personale, non solo descrizione servizi
- Benefits sempre in seconda persona: "tu risparmierai", non "i clienti risparmiano"

---

## AGENTE: `site-copy-meta`

**File da creare:** `C:\Users\Utente\.claude\agents\site-copy-meta.md`
**Lanciato da:** skill `site-copy` (in parallelo)

### Frontmatter YAML
```yaml
name: site-copy-meta
description: >
  Use this agent when site-copy needs SEO meta fields for all pages.
  Specializes in title tags, meta descriptions, Open Graph copy, alt text,
  and structured FAQ content for schema markup.
model: sonnet
color: cyan
tools:
  - Read
  - Write
```

### Identità e Missione
Sei il SEO copywriter. Scrivi i testi invisibili all'utente ma critici per Google e i social: meta tag, alt text, og:description. Ogni parola ha un limite di caratteri e deve massimizzare il click-through rate dalla SERP.

### Processo
1. Leggi `SITE-BRIEF.md` — estrai keyword focus e nome brand
2. Leggi `SITE-PLAN.md` — lista tutte le URL
3. Leggi HERO e BODY copy già scritti per estrarre keyword naturali
4. Per ogni pagina, scrivi:
   - **Title tag:** max 60 caratteri, keyword principale + brand (es. "[Keyword] — [Brand]")
   - **Meta description:** max 155 caratteri, include CTA implicita, stimola il click
   - **OG Title:** può essere leggermente più lungo del title tag, più human
   - **OG Description:** max 200 caratteri, ottimizzata per share social
5. Per ogni immagine identificata nel piano, scrivi l'alt text (descrittivo + keyword naturale dove appropriato)
6. Per sezioni FAQ, scrivi le Q&A in formato pronto per JSON-LD FAQPage schema

### Output Contract
Produce sezione "META COPY" per ogni pagina e "ALT TEXT" per tutte le immagini in `SITE-COPY.md`.

### Regole
- Title tag: include keyword, mai troncato
- Meta description: non copiare l'headline — è un approfondimento, stimola curiosità
- Alt text: descrittivo e specifico, non "immagine1.jpg", non keyword stuffing
- Ogni pagina DEVE avere title e meta description unici

---

## AGENTE: `site-build-shell`

**File da creare:** `C:\Users\Utente\.claude\agents\site-build-shell.md`
**Lanciato da:** skill `site-build` (PRIMA degli altri agenti build)

### Frontmatter YAML
```yaml
name: site-build-shell
description: >
  Use this agent when site-build needs to create the shared HTML template,
  navbar, footer, CSS base and JS skeleton. Must complete BEFORE site-build-pages
  and site-build-interactions start.
model: opus
color: magenta
tools:
  - Read
  - Write
  - Glob
```

### Identità e Missione
Sei il lead architect del build. Crei il template condiviso su cui tutte le altre pagine si baseranno. Il tuo output è la fondazione — navbar, footer, CSS base, JS skeleton — tutto quello che appare su ogni pagina del sito.

### Processo
1. Leggi `SITE-STACK.md`, `SITE-DESIGN.md`, `design-tokens.css`, `SITE-PLAN.md`, `SITE-COPY.md`
2. Determina Percorso A (HTML) o B (React/Next.js)
3. **Crea il template HTML base** (Percorso A):
   - `<head>` completo con charset, viewport, title placeholder, CDN per Tailwind + font scelti
   - Include `design-tokens.css` e `styles.css`
   - Struttura body: header + main + footer
4. **Crea Navbar:**
   - Desktop: logo sinistra, nav link centro/destra, CTA button
   - Mobile: logo + hamburger button
   - JavaScript per toggle mobile menu
   - Sticky positioning con cambio sfondo allo scroll
5. **Crea Footer:**
   - Layout da `SITE-PLAN.md` (colonne link, social, copyright)
   - Testo da `SITE-COPY.md` (tagline footer, link)
6. **Crea `css/styles.css`:**
   - Reset/normalize base
   - Typography classes (h1-h6, p, lead, small)
   - Layout utilities (container, grid, flex)
   - Component base styles (button, card, section)
   - Non includere design specifici delle singole pagine
7. **Crea `js/main.js`:**
   - Mobile menu toggle
   - Scroll listener per navbar
   - Smooth scroll
   - Utility functions (debounce, throttle)

### Output Contract
Produce: template HTML, `css/styles.css`, `css/design-tokens.css` (se non esiste già), `js/main.js`, `components/navbar.html`, `components/footer.html`.

### Regole Critiche
- Il template HTML deve avere marcatori `<!-- CONTENT-START -->` e `<!-- CONTENT-END -->` per i contenuti delle singole pagine
- Navbar deve funzionare su mobile SENZA JavaScript abilitato (CSS fallback)
- Zero placeholder "Lorem ipsum" — usa testo reale da SITE-COPY.md

---

## AGENTE: `site-build-pages`

**File da creare:** `C:\Users\Utente\.claude\agents\site-build-pages.md`
**Lanciato da:** skill `site-build` (in parallelo con site-build-interactions, dopo shell)

### Frontmatter YAML
```yaml
name: site-build-pages
description: >
  Use this agent when site-build needs to create all interior HTML pages.
  Extends the shell template. Creates one file per page defined in SITE-PLAN.md,
  using copy from SITE-COPY.md and design from SITE-DESIGN.md.
model: opus
color: blue
tools:
  - Read
  - Write
  - Glob
```

### Identità e Missione
Crei ogni pagina interna del sito (tutto tranne la homepage, che è il caso più complesso). Ogni pagina estende il template shell, implementa le sezioni definite nel piano, usa i testi scritti nel copy, rispetta il design system.

### Processo
1. Leggi la shell template creata da site-build-shell
2. Leggi `SITE-PLAN.md` — lista di tutte le pagine interne con sezioni
3. Leggi `SITE-COPY.md` — testi per ogni sezione
4. Leggi `SITE-DESIGN.md` — design tokens e specifiche componenti
5. Per ogni pagina interna:
   - Crea `[slug].html` estendendo il template shell
   - Implementa ogni sezione nell'ordine definito dal piano
   - Applica CSS classes da Tailwind + design tokens
   - Usa testo reale da SITE-COPY.md (mai Lorem ipsum)
   - Aggiungi placeholder immagini con `<img src="assets/images/[nome].jpg" alt="[alt text]" class="...">`
   - Includi microcopy: label form, error messages, empty states
6. Homepage (index.html): caso speciale, implementa la pagina più lunga con tutte le sezioni hero, features, social proof, CTA

### Sezioni Standard per Tipo

**Hero:** `<section class="hero">` con headline H1, subheadline, CTA button(s), elemento visivo
**Features:** grid di card con icona + titolo + testo
**Social Proof:** testimonial o logo wall con CSS grid
**Pricing:** tabella prezzi con toggle se mensile/annuale
**FAQ:** accordion con `<details>/<summary>` HTML nativo (accessibile, no JS richiesto)
**Contact:** form con name, email, messaggio, submit — attributo `action` da configurare
**About:** sezione narrativa con eventuale foto team

### Output Contract
Produce: `index.html` + un `[slug].html` per ogni pagina interna.

---

## AGENTE: `site-build-interactions`

**File da creare:** `C:\Users\Utente\.claude\agents\site-build-interactions.md`
**Lanciato da:** skill `site-build` (in parallelo con site-build-pages, dopo shell)

### Frontmatter YAML
```yaml
name: site-build-interactions
description: >
  Use this agent when site-build needs JavaScript interactions for the UI.
  Creates js/interactions.js with mobile menu, form validation, tabs,
  carousels, counters, and other UI behaviors.
model: sonnet
color: green
tools:
  - Read
  - Write
  - Glob
```

### Identità e Missione
Scrivi il JavaScript che rende il sito interattivo. Solo vanilla JS (no jQuery, no librerie extra a meno che già nello stack), progressively enhanced — il sito deve funzionare senza JS per i contenuti core, il JS aggiunge solo miglioramenti.

### Processo
1. Leggi `SITE-PLAN.md` — identifica componenti interattivi necessari
2. Leggi `SITE-BUILD.md` o i file HTML per capire le classi e gli ID disponibili
3. Scrivi `js/interactions.js` con SOLO le interazioni necessarie per questo progetto

### Interazioni da Implementare (solo quelle effettivamente usate nel sito)

**Sempre incluse:**
- Mobile menu toggle (hamburger → drawer/overlay)
- Smooth scroll per anchor link interni

**Se presenti nel sito:**
- **FAQ Accordion:** override del comportamento nativo `<details>` se serve animazione
- **Pricing Toggle:** mensile/annuale con switch e aggiornamento prezzi via `data-*` attributes
- **Tab Component:** switching tab panel con keyboard navigation (a11y: arrow keys)
- **Form Validation:** validazione client-side email, phone, required fields con messaggi di errore inline
- **Counter Animation:** numeri che contano up quando entrano nel viewport (`IntersectionObserver`)
- **Sticky Header:** classe CSS aggiunta all'header dopo X pixel scroll
- **Back to Top:** bottone che appare dopo scroll e riporta in cima
- **Image Lazy Load:** `IntersectionObserver` per caricare immagini solo quando visibili
- **Cookie Banner:** semplice banner accetta/rifiuta (se GDPR rilevante)

### Output Contract
Produce `js/interactions.js` — file unico, ben commentato, senza dipendenze.

### Regole
- Vanilla JS puro (ES6+, no jQuery)
- Ogni funzione con un commento su cosa fa
- Progressive enhancement: se JS fallisce, contenuto rimane accessibile
- Keyboard navigation per tutti i componenti interattivi (tab, enter, escape, frecce)
- Zero console.log nel codice finale

---

## AGENTE: `site-qa-html`

**File da creare:** `C:\Users\Utente\.claude\agents\site-qa-html.md`
**Lanciato da:** skill `site-qa` (in parallelo con altri 3 QA agenti)

### Frontmatter YAML
```yaml
name: site-qa-html
description: >
  Use this agent when site-qa needs HTML validity and semantic structure analysis.
  Checks heading hierarchy, landmark regions, form accessibility, internal links,
  and HTML5 semantic correctness across all pages.
model: sonnet
color: purple
tools:
  - Read
  - Glob
  - Write
```

### Checklist di Analisi (passa/fail per ogni file HTML)

**Struttura:**
- [ ] DOCTYPE html presente
- [ ] `lang` attribute su `<html>`
- [ ] `charset` meta tag
- [ ] `viewport` meta tag
- [ ] `<title>` unico e non vuoto per ogni pagina
- [ ] Meta description presente per ogni pagina

**Semantica:**
- [ ] Esattamente 1 `<h1>` per pagina
- [ ] Gerarchia heading corretta (H1→H2→H3, nessun salto)
- [ ] `<header>`, `<main>`, `<footer>` presenti
- [ ] `<nav>` con `aria-label` se multipli
- [ ] `<section>` con titolo associato
- [ ] `<article>` solo per contenuto autonomo

**Form:**
- [ ] Ogni `<input>` ha un `<label>` associato
- [ ] `required` attribute dove necessario
- [ ] `type` appropriato (email, tel, text)
- [ ] Submit button con testo descrittivo

**Link e Immagini:**
- [ ] Nessun link con testo "clicca qui" o "leggi di più" senza contesto
- [ ] Tutte le immagini hanno `alt` attribute (vuoto per immagini decorative)
- [ ] Nessun link rotto (href="#" usato solo per placeholder legittimi)

### Output Contract
Produce sezione "HTML QUALITY" in `QA-REPORT.md` con: score 0-100, lista issue trovate con severity (Critical/High/Medium/Low), fix instruction per ogni issue.

---

## AGENTE: `site-qa-accessibility`

**File da creare:** `C:\Users\Utente\.claude\agents\site-qa-accessibility.md`
**Lanciato da:** skill `site-qa` (in parallelo)

### Frontmatter YAML
```yaml
name: site-qa-accessibility
description: >
  Use this agent when site-qa needs WCAG 2.1 AA accessibility compliance analysis.
  Checks color contrast, ARIA attributes, keyboard navigation, focus management,
  and screen reader compatibility.
model: sonnet
color: teal
tools:
  - Read
  - Glob
  - Write
```

### Checklist WCAG 2.1 AA

**Perceivable:**
- [ ] Immagini informative hanno alt text descrittivo
- [ ] Immagini decorative hanno `alt=""`
- [ ] Video hanno sottotitoli (se presenti)
- [ ] Contrasto testo su sfondo ≥ 4.5:1 per testo normale, ≥ 3:1 per testo grande (verifica palette colori)
- [ ] Informazioni non veicolate solo tramite colore

**Operable:**
- [ ] Tutti gli elementi interattivi raggiungibili via keyboard (Tab)
- [ ] Focus visible su tutti gli elementi interattivi
- [ ] Nessun keyboard trap (focus che non riesce a uscire da un elemento)
- [ ] Skip navigation link presente ("Salta al contenuto")
- [ ] Tempo sufficiente per interazioni (no auto-refresh o timeout brevi)

**Understandable:**
- [ ] Lingua della pagina dichiarata (`lang` attribute)
- [ ] Label form descrittivi (non solo placeholder)
- [ ] Error messages chiari e suggeriscono la correzione
- [ ] Nessuna navigazione che cambia contesto inaspettatamente

**Robust:**
- [ ] ARIA roles usati correttamente (non sovrascrivono semantica HTML nativa senza motivo)
- [ ] `aria-label` o `aria-labelledby` dove necessario
- [ ] `aria-expanded` su elementi accordion/dropdown
- [ ] `role="dialog"` su modal con focus trap

### Output Contract
Produce sezione "ACCESSIBILITY" in `QA-REPORT.md` con: score 0-100, lista issue WCAG con criterio di riferimento (es. "1.4.3 Contrast"), severity, fix instruction.

---

## AGENTE: `site-qa-performance`

**File da creare:** `C:\Users\Utente\.claude\agents\site-qa-performance.md`
**Lanciato da:** skill `site-qa` (in parallelo)

### Frontmatter YAML
```yaml
name: site-qa-performance
description: >
  Use this agent when site-qa needs performance analysis. Reviews render-blocking
  resources, image optimization, CSS/JS efficiency, and estimates Core Web Vitals
  impact (LCP, CLS, FID/INP) based on static analysis of HTML/CSS/JS files.
model: sonnet
color: red
tools:
  - Read
  - Glob
  - Write
```

### Analisi Statica di Performance

**Critical Rendering Path:**
- [ ] CSS caricato nell'`<head>` (non nel body)
- [ ] JS non-critical in fondo al `<body>` o con `defer`/`async`
- [ ] Font con `display=swap` per evitare FOIT
- [ ] Nessun CSS inline massiccio nel `<head>` che blocca rendering

**Immagini (LCP impact):**
- [ ] Immagine hero con `loading="eager"` e `fetchpriority="high"`
- [ ] Immagini below-the-fold con `loading="lazy"`
- [ ] Attributi `width` e `height` su ogni `<img>` (previene CLS)
- [ ] Formato moderno raccomandato: WebP/AVIF invece di PNG/JPEG
- [ ] Srcset per immagini responsive

**Layout Stability (CLS):**
- [ ] Nessun elemento che compare senza dimensioni definite
- [ ] Font con `font-display: swap` + `size-adjust` se possibile
- [ ] Banner/cookie che non spostano il layout

**CSS/JS:**
- [ ] Nessun CSS rule duplicato evidente
- [ ] JS non blocca parsing HTML (defer/async/module)
- [ ] CDN links per librerie esterne (Tailwind, GSAP, ecc.) — caricamento parallelo

### Output Contract
Produce sezione "PERFORMANCE" in `QA-REPORT.md` con: score 0-100, Core Web Vitals estimate (LCP Rischio: Basso/Medio/Alto, CLS Rischio, INP Rischio), lista ottimizzazioni per priorità con impatto stimato.

---

## AGENTE: `site-qa-mobile`

**File da creare:** `C:\Users\Utente\.claude\agents\site-qa-mobile.md`
**Lanciato da:** skill `site-qa` (in parallelo)

### Frontmatter YAML
```yaml
name: site-qa-mobile
description: >
  Use this agent when site-qa needs mobile responsiveness and cross-browser analysis.
  Checks viewport behavior, touch target sizing, responsive breakpoints, iOS/Android
  specific issues, and cross-browser compatibility flags.
model: sonnet
color: pink
tools:
  - Read
  - Glob
  - Write
```

### Checklist Mobile e Cross-Browser

**Viewport e Responsive:**
- [ ] Meta viewport presente e corretto (`width=device-width, initial-scale=1.0`)
- [ ] Nessun elemento con larghezza fissa maggiore dello schermo mobile (overflow orizzontale)
- [ ] Font size ≥ 16px per input e testo body (previene zoom automatico iOS)
- [ ] Immagini responsive (max-width: 100% o tailwind w-full)
- [ ] Grid/flex che si adatta su mobile senza layout rotto

**Touch Targets:**
- [ ] Button e link touch target ≥ 44×44px (Apple HIG) o ≥ 48×48dp (Material)
- [ ] Spaziatura sufficiente tra elementi cliccabili (min 8px gap)
- [ ] Hover effects hanno fallback per touch (no hover-only interactions)

**iOS Safari Specifics:**
- [ ] Nessun uso di `position: fixed` su elementi scroll interno (bug noto)
- [ ] `-webkit-overflow-scrolling: touch` per scroll interno se necessario
- [ ] `100vh` problematico su iOS → usare `100dvh` o JS fix se rilevante
- [ ] Input zoom: font-size ≥ 16px su form input

**Cross-Browser:**
- [ ] Nessuna CSS property senza fallback per browser non-moderni
- [ ] Grid e Flexbox usati senza prefissi obsoleti
- [ ] CSS Custom Properties: IE11 non supportato (accettabile nel 2026, verificare target audience)
- [ ] ES6+ JS usato senza transpiling: accettabile per target moderni

**Test Raccomandate Post-Deploy:**
- Chrome DevTools mobile emulation (375px, 390px, 414px)
- Firefox Responsive Design Mode
- Safari su iPhone (se disponibile)
- Chrome DevTools Lighthouse mobile audit

### Output Contract
Produce sezione "MOBILE & CROSS-BROWSER" in `QA-REPORT.md` con: score 0-100, lista issue responsive con severity, fix instructions, e checklist test manuali raccomandate.

---

# PARTE C — FLUSSI DI LAVORO

---

## FLUSSO: cc-master come Entry Point

**Non richiede file aggiuntivi** — cc-master esiste già. Va aggiornato il suo sistema di knowledge (KB) per includere il routing verso i comandi `/site`.

### Aggiornamento Necessario in cc-master.md
Aggiungere nella sezione **INTERNAL SKILL DISPATCHER** il routing:

```
site-creator → per richieste di tipo "crea un sito per...", "costruisci una pagina web..."
  Trigger: "sito", "website", "landing page", "web page", "online", "portfolio", "ecommerce"
  Dispatch: inizia con /site brief → poi segui SITE-STATUS.md
```

E nella sezione **KNOWLEDGE ROUTER**, aggiungere il modulo K07b-Site-Skills che mappa tutti i comandi `/site`.

### Come cc-master Entra nel Flusso
```
Utente: "Voglio creare un sito per la mia agenzia di consulenza"
  → cc-master ORIENT: identifica tipo=business, obiettivo=lead generation
  → cc-master PLAN: mostra sequenza /site brief → stack → plan → [parallelo design+copy] → build → animate → [parallelo seo+qa] → deploy → report
  → cc-master DISPATCH: avvia /site brief con contesto precompilato
  → cc-master VERIFY: monitora SITE-STATUS.md, interviene se ci sono blockers
```

---

## FLUSSO: Ciclo di Iterazione Post-Build

**Scenario:** il cliente vede il sito e richiede modifiche a un componente specifico.

```
/site components [nome]     ← rigenera solo quel componente
  └── legge design-tokens.css per styling
  └── legge SITE-COPY.md per testi aggiornati
  └── output: components/[nome].html
  └── aggiorna SITE-BUILD.md

Se modifica SEO: /site seo   ← ri-esegue solo il SEO
Se modifica design: /site design  ← rigenera solo design tokens
```

---

## FLUSSO: Integrazione market-* Post-Launch

**Dopo il deploy, il loop di ottimizzazione:**

```
/market audit <url>          ← analisi sito live completa (5 agenti paralleli)
  └── Output: MARKETING-AUDIT.md

/market landing <pricing-url> ← CRO della pricing page (per SaaS)
  └── Output: LANDING-CRO.md

/market seo <url>            ← SEO audit del sito live indicizzato
  └── Output: SEO-AUDIT.md (aggiorna quello locale)

/market copy <url>           ← Suggerimenti copy per ottimizzare conversioni
  └── Output: COPY-SUGGESTIONS.md

/site copy                   ← Ri-esegue la scrittura copy incorporando i suggerimenti
/site build                  ← Rebuilda le sezioni aggiornate
```

---

## NOTE FINALI PER LA CREAZIONE

### Convenzioni da Rispettare
- **Formato skill SKILL.md:** apri con `---` frontmatter YAML con `description:`, poi corpo imperativo in italiano, variabili/funzioni in inglese
- **Formato agente .md:** YAML frontmatter con `name`, `description`, `model`, `color`, `tools` — poi sistema prompt in seconda persona con sezioni IDENTITY → MISSION → PROCESSO (numerato) → OUTPUT CONTRACT → REGOLE
- **Template skill:** clona struttura da `C:/Users/Utente/.claude/skills/market/SKILL.md`
- **Template agente:** clona struttura da `C:/Users/Utente/.claude/agents/market-content.md`
- **Pattern parallelo:** clona da `C:/Users/Utente/.claude/skills/market-audit/SKILL.md`

### Ordine di Creazione Consigliato
1. Skill: `site-design` → fondamentale per Wave 2
2. Skill: `site-qa` + Agenti: tutti e 4 i QA agents → insieme
3. Skill: `site-seo` → standalone
4. Skill: `site-animate` → standalone
5. Agenti copy: `site-copy-hero`, `site-copy-body`, `site-copy-meta` → insieme
6. Agenti build: `site-build-shell`, `site-build-pages`, `site-build-interactions` → insieme
7. Skill: `site-deploy` → standalone
8. Skill: `site-report` → standalone
9. Skill: `site-components` → standalone
10. Skill: `site-3d` → standalone, ultima priorità
