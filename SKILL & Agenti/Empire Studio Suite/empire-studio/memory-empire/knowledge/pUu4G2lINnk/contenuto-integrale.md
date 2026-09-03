# Insane Claude Design Skills You Actually Need To Build Beautiful Sites — Analisi Integrale

- **ID video**: `pUu4G2lINnk`
- **Titolo**: Insane Claude Design Skills You Actually Need To Build Beautiful Sites
- **Canale**: Jack Roberts
- **Durata**: 1376s (22m56)
- **Pubblicato**: 2026-08-31 · 40.429 visualizzazioni · 518 like (al momento dell'ingestione)
- **URL**: https://www.youtube.com/watch?v=pUu4G2lINnk
- **Data ingestione**: 2026-09-03 (run `max17-v11-roberts-design`)
- **Copertura frame**: **182/270 frame unici guardati su 689 densi estratti** (1 ogni 2.0s), soglia di deduplicazione 3.0 — vedi `coverage.md`
- **Trascrizione**: `pUu4G2lINnk.en.vtt` ripulita in `transcript_clean.txt` (761 righe, deduplicazione caption a cascata), letta per intero
- **Risoluzione sorgente**: 640x360 (il video e' stato scaricato a 360p — vedi `coverage.md`, sezione limiti)

---

## AVVERTENZA DI METODO — la lettura dei pannelli di testo denso

Il video sorgente e' a **360p**. Molte schermate chiave (il pannello `DESIGN.md` di
refers.design, la tabella "Signs of AI writing", la tabella keyword di Glaido) sono
**pannelli di testo denso** che a quella risoluzione sono al limite della leggibilita'.
Per non violare NO-FINTO ho **ritagliato e ingrandito 4x-7x con Lanczos** le regioni
di interesse (script inline PIL, output in `_zoom/`) e letto quelle. Dove anche
l'ingrandimento non basta — tipicamente i valori esadecimali a 6 cifre — il valore e'
marcato `[illeggibile]` o `[incerto]`, **mai completato per invenzione**.

---

## WALKTHROUGH CRONOLOGICO (capitoli ufficiali YouTube)

### Intro (0:00-0:33)
Apertura su un montaggio rapido di siti di riferimento a schermo pieno: Apple Watch SE 3
(`frame-003.png @ 0:04`, banner "Now you can buy Apple Watch SE 3 with education savings"),
un sito **MORELAX** — "Creative technology studio building design + [mo]tion, mockups, and
interactive visuals", CTA `Explore Ecosystem` / `Open Studio` (`frame-011.png @ 0:20`), e
b-roll dell'autore all'estero (`frame-016.png @ 0:30`).

A voce (0:00-0:31): *"Claude is the world's number one design agent for building beautiful
websites. But just because your site looks pretty doesn't mean that it will sell or get
customers. For that, you need to use the correct skills. And in this video, I'll show you
the most important ones across seven levels so you can build beautiful websites that are
mobile optimized, sound like they've been written by a human, and have the correct
structure without the need to be a design expert."*

**La tesi del video, per intero**: bello != vendente. Le sette skill sono il ponte fra i due.

| Capitolo | Timestamp | Titolo |
|---|---|---|
| Intro | 0:00-0:33 | — |
| Level 1 | 0:33-1:46 | Finding the standard |
| Level 2 | 1:46-5:42 | The whole map |
| Level 3 | 5:42-12:41 | The scroll-stopper |
| Level 4 | 12:41-14:53 | Mobile |
| Level 5 | 14:53-18:30 | De-slopification |
| Level 6 | 18:30-20:30 | Icons + showstoppers (UI sniping) |
| Level 7 | 20:30-22:43 | SEO-ification + deploy |
| What's Next | 22:43-22:56 | — |

Ogni livello e' trattato per intero nelle sezioni dedicate sotto.

---

## IL MAZZO DI SLIDE — un deck HTML servito in locale

Trasversalmente a tutto il video, l'autore alterna screen-share degli strumenti a un
**mazzo di slide che ha costruito lui in HTML e serve in locale**: la barra indirizzi
mostra `127.0.0.1:5497/index.html` (`frame-018.png @ 0:34`, `frame-020/027`,
`frame-053`, `frame-059`, `frame-273`, `frame-380`, `frame-450`, `frame-557`,
`frame-619`). E' un dettaglio operativo non dichiarato a voce ma visibile a schermo:
**il deck e' esso stesso un artefatto Claude Design, non Keynote/Figma**. Sulla destra
di ogni slide c'e' un indicatore di scorrimento verticale a pallini (navigazione a
sezioni), tipico di un deck one-page.

Ogni slide ha la stessa grammatica visiva, ed e' la miglior sintesi del metodo:

```
[SKILL 0N · NOME-CATEGORIA]       <- eyebrow in maiuscoletto spaziato
0N                                 <- numerone in serif oro/rosa, enorme
Titolo in serif + parola in corsivo colorata
"Citazione-regola in corsivo grigio"
[chip] [chip] [chip]               <- gli oggetti concreti del livello
· LIVE DEMO · COSA SI VEDE, MAIUSCOLO ·   <- striscia inferiore
next: <la frase-ponte al livello successivo>
```

---

## I SETTE LIVELLI, UNO PER UNO

### LIVELLO 1 — FIND THE STANDARD (0:33-1:46)

**Slide** (`frame-018.png @ 0:34`): *SKILL 01 · REFERENCE* — **01** — **"Find the standard"**
— citazione: *"Pick the site you wish you'd built."*

**Muro di riferimento** (`frame-020.png @ 0:38`, `frame-027.png @ 0:52`): sotto la slide
scorre una **griglia di sei siti gold-standard** etichettati in maiuscoletto sotto ogni
tile — **APPLE**, **MINTLIFY**, **MODAL**, **MERCURY**, **LINEAR**, **SUPERHUMAN**.
Contenuti leggibili nelle tile:
- APPLE — "Hola, Neo." / MacBook Neo
- MINTLIFY — "The Intelligent Knowledge Platform" e "Built for the intelligence age"
- MODAL — "AI infrastructure that developers love", "Real-time, multi-node inference for
  AI Characters", "[ro]bot control running on Modal with [low late]ncy", loghi Lovable /
  Quora / "Powering AI ops"
- MERCURY — testimonianza: *"[Mercury] has completely changed my expectations of what to
  expect [from a bank]. The vision and craft is so far beyond what traditional banking
  can provide."* — Fred Fugglestone, Head of Ops
- LINEAR — "[The purpose-built shap]e of product tool. Purpose-built for m[odern product]
  workflows at its core, Linear sets a n[ew standard for] planning and building products."
  e "[Built for teams moving] forward [with age]nts and agents"
- SUPERHUMAN — "How it works"

**Lo strumento**: `refers.design` — a voce l'autore lo pronuncia "referral.design", ma la
barra indirizzi mostra **`refers.design`** (`frame-031.png @ 1:00`). Sottotitolo del sito:
**"Design Research for the AI Era"**. Sidebar: `+ New research`, `Web apps`, `iOS apps`,
`Styles (Beta)`. In alto un bottone **"Connect MCP"**.

Ricerca a tendina (`frame-033.png @ 1:04`), colonne:
- **Popular**: "Search results with filter sidebars" · "AI SaaS product landing pages" ·
  "Roadmap boards and product planning timelines"
- **Inspiration** · **Onboarding**
- **Workflows**: "Empty states with create-first CTA" · "AI chat with sources and citations" ·
  "Signup with email verification"

Loghi clienti: ATLASSIAN, PLAID, ramp, Retool, Spotify, Webflow — piu' un badge
**Product Hunt 5.0 ★★★★★ (15 reviews)**.

Tab "**Page Types**": Dashboard · Product Page & Landing · Paywall & Subscription · Log In ·
Product Details · Profile & Account · 404 Page · Catalog Page · Blog · About · Careers ·
Contacts · Developers Page · Integration Page · Media Kit.
Nella tab Dashboard (`frame-038.png @ 1:14`) sono catalogati e schermati: **Mercury**,
**Shopify**, **Runway**, **Cycle**, **GlossGenius** e altri.

**Sezione Styles** (`frame-042.png @ 1:22`, `styles.refers.design`): galleria di sistemi
visivi gia' smontati — **MindMarket**, **Monad**, "Your workspace has the answer. Just ask
Dala for it.", **Steep**, **ORYZO AI**, **Apple (España)**, **Shop**.

#### IL PEZZO PIU' IMPORTANTE DEL LIVELLO 1 — il file `DESIGN.md`

Aprendo `refers.design / Styles / Mintlify` (`frame-046.png @ 1:30`, `frame-049.png @ 1:36`,
`frame-051.png @ 1:40`, `frame-091.png @ 3:00`, `frame-178.png @ 5:54`) lo schermo si divide:
a sinistra lo screenshot navigabile del sito, **a destra un pannello di codice con quattro
tab: `DESIGN.md` | `Tokens.of` | `CSS Variables` | `Design Tokens`**, un toggle
**Compact / Extended** e due bottoni **Copy** / **.md**.

Il contenuto di `DESIGN.md` (trascritto dai ritagli ingranditi 4x di `frame-051.png`,
`_zoom/z051a.png` e `_zoom/z051b.png`):

```markdown
# Mintlify — Style Reference

> Cloud garden over a glass desk. A hand-illustrated sky and a documentation product
> share the same frame — the only place co[...tagliato a bordo pannello]

**Theme:** Light

Mintlify operates on a near-total monochrome discipline: white canvas, near-black text,
and a single vivid green as the only c[...tagliato]

## Tokens — Colors

| Name        | Value              | Token                 | Role |
|-------------|--------------------|-----------------------|------|
| Mint Green  | #0c8c5e [incerto]  | `--color-mint-green`  | Brand links, active nav state, feature icons, decorative dots in eyebrow lab[els...] |
| Ink Black   | #08090a [incerto]  | `--color-ink-black`   | Dark supporting neutral for text, icons, and strong contrast. Do not promote [...] |
| True Black  | #000000            | `--color-true-black`  | Body text, link defaults before hover, icon strokes, and footer rules — the [...] |
| Paper White | #ffffff            | `--color-paper-white` | Page canvas, card surfaces, button text on dark fills, input fields — the [...] |
| Mist Gray   | #f1f2f2 [incerto]  | `--color-mist-gray`   | Subtle dividers, hairline strokes on cards, low-emphasis backgrounds, and the [...] |
| Cloud Gray  | [illeggibile]      | `--color-cloud-gray`  | Input borders, card outlines on hover states, secondary divider lines that n[eed...] |

## Tokens — Typography

### Inter — Universal typeface — the only family in the system. Used for headlines,
### body, nav, buttons, inputs, and code. No s[econd family...]

- **Substitute:** Inter (Google Fonts) — also try IBM Plex Sans or General Sans as open
  alternatives if Inter is unavailable.
- **Weights:** 400, 500, 600
- **Sizes:** 13, 14, 15, 16, 18, 20, 24, 40, 57
- **Line height:** 1.18, 1.35, 1.38, 1.53, 1.50, 1.71
- **Letter spacing:** Tight at large sizes: -0.03em at 57px, -0.05em at 40px down through
  16px, neutral at 13-14px, +0.05em on [uppercase eyebrow labels...]
- **OpenType features:** `"ss01" on, "cv11" on`

### Type Scale

| Role         | Size | Line Height | Letter Spacing   | Token                |
|--------------|------|-------------|------------------|----------------------|
| caption      | 13px | 1.5         | 0.04px [incerto] | `--text-caption`     |
| body         | 16px | 1.5         | -0.16px          | `--text-body`        |
| subheading   | 20px | 1.3         | -0.2px           | `--text-subheading`  |
| heading-sm   | 24px | 1.35        | -0.24px          | `--text-heading-sm`  |
```

Nella vista **Color Palette** espansa (`frame-223.png @ 7:24`, `frame-243.png @ 8:04`,
ritaglio `_zoom/z223.png`) ogni colore ha una **descrizione di ruolo in prosa**, non un
semplice nome. I testi, verbatim:

> **Mint Green** — *"Brand links, active nav state, feature icons, decorative dots in
> eyebrow labels, the thin underline on inline code references — the only chromatic accent
> in a monochrome system, applied sparingly to make functional moments feel 'switched on'."*

> **Cloud Gray** — *"Input borders, card outlines on hover states, secondary divider lines
> that need a step more presence than Mist Gray."*

> **Mist Gray** — *"Subtle dividers, hairline strokes on cards, low-emphasis backgrounds,
> and the lightest fills that need to read as a surface."*

**Il concetto operativo del Livello 1** (a voce, 1:30-1:43): *"what this has done is given
us the design DNA, the design blueprint such that we can actually understand what makes this
design fantastic. And when we give that to Claude, we can build a version for ourselves."*

---

### LIVELLO 2 — THE WHOLE MAP (1:46-5:42)

**Slide** (`frame-053.png @ 1:44`, `frame-059.png @ 1:56`, `frame-201.png @ 6:40`):
**02** — **"The whole map"** — citazione: *"Everyone demos one landing page. The $10k site
is seven of them."* Sotto, un diagramma stile incisione ottocentesca su carta invecchiata
(sole nascente + rami) intitolato **"THE WHOLE MAP"**, con annotazioni di misura reali:
`HOME PAGE 72px`, `DEPTH 3 LEVELS`, e spaziature `120px` tra i rettangoli di pagina.

**Card Relume sulla stessa slide** (letta integralmente da `frame-268.png @ 8:54`, la
schermata piu' pulita):

```
Relume
✓ One brief in — sitemap, wireframes and page architecture out.
✓ Human-made components, assembled by AI — the system behind 2M websites.
✓ Stays consistent from the first section to the fiftieth — no drift by page three.
✓ Pulls into Claude via MCP — the code is yours, no lock-in.

THE RULE
Relume is the bones. Your design system is the skin.

next: the moment that stops the scroll
```

**Lo strumento: Relume** (`relume.ai`, `frame-064.png @ 2:06`, `frame-562.png @ 18:42`).
Headline del sito: *"Build a marketing site you'd actually publish — Start with a brief.
Relume builds the sitemap, wireframes, and a marketing site you'd actually publish. AI does
the work. You make the calls."* Badge: **"TRUSTED BY 2M+ FREELANCERS & AGENCIES"**.
Campo di input: *"Drop in your video, brief or a URL..."*; toggle **Publish** / **Export**;
bottone **Generate Website**; link **"Try an example"**. Nav: Products, Pricing, Contact
Sales, Component Voting, Learn, **Launch Builder**.
Loghi clienti (`frame-063.png @ 2:04`): Rakuten, Superside, headspace, DEPT., DARKTRACE, ROKT.
Progetto demo mostrato: **MAISONS** — hero *"We built around the neighbours"* con pellicano.

Sezione prodotto (`frame-574.png @ 19:06`):
> *"Build your site and take it to Figma, Webflow or React — Choose from 1,000+ responsive
> components to build a complete site, then export straight into Figma, Webflow or React, or
> pull them into your AI tools with the **Relume Library MCP**."*
> - **Webflow** — Clean, intent-free classes, ready with variables
> - **Figma** — Editable auto-layout with real variables and variants
> - **React** — Coded with Tailwind CSS and shadcn/ui components
>
> *"No hallucinated layouts. Relume assembles your site with human-built components on a
> shared system, so when something improves, every site improves. No rebuild. No effort
> from you."*

**Il flusso operativo mostrato** (2:36-5:41), passo per passo:

1. **Nuovo progetto** → campo **Description*** con placeholder *"Describe the company in a
   sentence or two, and generate a sitemap."*, bottone **Prompt ✦**, selettore
   **Number of pages: 2-5**, **Language: English (US)**, e opzione **Import sitemap**
   (`frame-084.png @ 2:46`). Il banner in cima avvisa: *"You've used 50% of your AI usage
   this cycle. Resets in 7 days. Upgrade to Pro"*.
2. Il brief dettato a voce dall'autore (2:47-2:53), verbatim:
   > *"hey that I want you to build for me a roofing company that is best-in-class using the
   > below design principles"*

   e sotto si incolla **l'URL preso da refers.design**, oppure l'intero `DESIGN.md`
   copiato con il bottone Copy.
3. **Sitemap generata** — le sezioni si trascinano su e giu'. Regola citata a voce (3:12):
   *"an ounce in print is worth a pound in post"*.
4. **Wireframe** (`frame-159.png @ 5:16`): sidebar **Site Structure** con `PAGES` (Home,
   Services, Our Work, About, Contact) e `LAYERS`. Sezioni wireframate visibili: *"Roofing
   services built to last"*, *"Every roofing service you need"*, *"Roof repair"*, *"Roof
   replacement"*, *"New installation"*, *"Maintenance & inspection"*, *"Work we're proud of"*,
   *"Recent projects"*, *"Roofing done right, since day one"*, *"A company built on doing the
   job right"*, *"By the numbers: 15+ / 2,000+ / 98% / 5-star"*, *"The people behind your
   roof"*, *"Ready to start your project?"*, *"Tell us about your project"*, *"Prefer to
   talk?"*, *"Not sure which service you need?"*.
5. **Editor di sezione** (`frame-118.png @ 3:54`): toggle **"Make a global section"**,
   **Name**: `Stats Section`, **Description**: *"Showcase key company metrics such as years
   in business, roofs completed, satisfied customers, and warranty coverage"*, campo
   **Prompt ✦**, **Stats 15**, **Columns 2**. In basso lo stato **"Generating designs..."**.
6. **Style Guide** (`frame-112.png @ 3:42`, `frame-113.png @ 3:44`): progetto "Mintlify
   Roofing", **Concept 1**, bottoni **Pitch Concepts** e **Shuffle**. Colori generati:
   scala **Neutrals** + **Salem `#0C8C5E`** (verde, con lucchetto = bloccato) +
   **Cello `#1D3557`** (blu notte) + **Burnt Sienna `#E76F51`** (arancio terracotta).
   Tipografia: **Body = Inter** (Google, Free), peso "Regular - medium".
   Sezione **Cards & Images** → "Outlined Card". Popup sull'anteprima: *"New schemes
   available — Pick a scheme to apply to your page, based on your new colors"*.
   Anteprima hero: **"Roofs built to outlast the weather"**, nav `About us · Services ·
   Projects · Roofing ∨ · Contact · [Quote]`, fascia sotto *"Certified by the names that set
   the standard"*.
7. **Export** (`frame-120.png @ 3:58`) — il menu, per intero:
   `Figma` · `Webflow` · `React` · **`HTML` ✓** · **`Export to Claude...` [New]** ·
   `Export to TXT` · `Export to CSV` · `Export to Excel`.
   L'autore sceglie **HTML** (zip) invece dell'export nativo a Claude, per mostrare il caso
   generale.
8. **Menu Edit del progetto** (`frame-080.png @ 2:38`): **Editor** `BETA` ("Take your project
   live and grow it") · **Export** ("Build an export to Figma, Webflow or React") ·
   **Library** ("Relume components") · "← Back to website". Sidebar: Webflow Library,
   React Library. Stato account: **"Relume Pro · 6 days remaining of Pro trial"**.
9. **Relume Publish** (funzione CMS, 4:49-5:41): `SITE SETTINGS` → General, Domains,
   Redirects, **CMS** (`CMS · SEO`), Forms, Custom code, Discoverability, Ownership &
   access, Hosting & billing. `PAGE SETTINGS` → per ogni pagina.
   - **General** (`frame-167.png @ 5:32`): Status `DRAFT`; URL `[...].relumesite.ai`;
     Owner: Jack Roberts; Project name: `Summit Roofing Co.`; Language: English (United
     States). **Meta title**: `Roofing Company | Summit Roofing Co.` — **Meta description**:
     *"Trusted residential and commercial roofing contractor. Roof repair, replacement,
     installation and maintenance with transparent pricing and a clear process. Get a free
     quote."*
   - **Page settings / Services** (`frame-169.png @ 5:36`): Page name `Services`, Slug
     `/services`, **Meta Title**: `Roofing Services | Repair, Replacement & Installation —
     Summit Roofing`, **Meta Description**: *"Explore our roofing services: roof repair, full
     replacement, new installation and maintenance for residential and commercial properties.
     See what each service involves."*, toggle **Search engine indexing** ON ("Show this page
     in Google search"), **Social preview** (*"Uses site default. Override for the page when
     shared on Facebook, LinkedIn, etc. 1200x630 pixels"*) con drop-zone "Drop image or
     upload".
   - **Custom code** (`frame-168.png @ 5:34`, marcato `Upgrade`): *"Add code from other tools.
     Only use them if they give you code to paste, do not include `<head>` or `<body>` tags."*
     Campo **Start of `</head>`** con placeholder `<!-- Paste your code here -->`.

#### IL PROMPT DI CONSEGNA A CLAUDE — trascritto parola per parola

`frame-123.png @ 4:04` (ritaglio ingrandito `_zoom/z123p.png`) — Claude Desktop, campo di
input, prompt digitato per intero:

> `hey there i want you to go ahead and build for me a beautiful website based on this
> particular link using the exact design systems and layouts that are included in this zip
> file that we built in relume`

Nello stesso frame, la schermata **"What's up next, Jack?"** con il pannello **Overview**
delle statistiche d'uso di Claude (`_zoom/z123s.png`):

| Metrica | Valore |
|---|---|
| Sessions | **540** |
| Messages | **132,025** |
| Total tokens | **97.2M** |
| Active days | **53** |
| Current streak | **21d** |
| Longest streak | **21d** |
| Peak hour | **7 PM** |
| Favorite model | **Fable 5** |

Nota sotto l'heatmap: *"You've used ~943x more tokens than Harry Potter and the
Philosopher's Stone"* [il moltiplicatore e' al limite della leggibilita' — cifra incerta,
l'ordine di grandezza (centinaia di volte) e' certo]. In una seconda ripresa
(`frame-632.png @ 21:02`) i contatori sono Sessions **532**, Messages **132,263**, Total
tokens **97.3M**, e la nota cita **Dune** invece di Harry Potter: **le due riprese sono di
sessioni diverse**, non un errore di lettura. Selettore modello: **Opus 5 / Extra** in una,
**Fable 5 / High** nell'altra.

---

### LIVELLO 3 — THE SCROLL-STOPPER (5:42-12:41)

**Slide** (`frame-273.png @ 9:04`, `frame-380.png @ 12:38`, ritaglio `_zoom/z273.png`):
*SKILL 03 · HERO* — **03** — **"The scroll-stopper"** — citazione: *"Generate the exact
image each section needs. Nothing generic."*
Sotto, una fila di mockup mobile generati. Due badge:
**`⚡ Higgsfield generates`** e **`◆ Claude places`**.
Striscia inferiore: **`· LIVE DEMO · HERO IMAGE + MOTION, GENERATED ON CAMERA ·`**
Frase-ponte: **`next: most visitors aren't on a monitor`**

#### 3a — Higgsfield come generatore di immagini/video

`higgsfield.ai` (`frame-179.png @ 5:56`): *"AI IMAGE GENERATOR BUILT FOR PROFESSIONALS —
Commercial-ready visuals in seconds. Perfect text, consistent characters, and every leading
model at your fingertips."* CTA **Create Image Now**. Barra prompt in basso: *"Describe any
visual idea. We will generate an image"* + **Generate**, modello selezionato
**Nano Banana Pro**, ratio **3:4**.
Nav laterale completa: Explore · Image · Video · Audio · Edit · Draw · **Cinema Studio (New)** ·
**Marketing Studio (New)** · Your Presets · **MCP & Apps (New)** · Competitor Intel · Academy ·
Community · **Onboard (New)** · Upgrade (50% OFF) · Enterprise · Assets.

**La pagina di connessione — `higgsfield.ai/mcp`** (`frame-183.png @ 6:04`,
`frame-199.png @ 6:36`, ritaglio `_zoom/z183.png`):

> **HIGGSFIELD MCP & CLI FOR ANY AI** — *"Create images and videos directly from your
> prompts in any AI tool"*
> Tab: `Claude` | `Grok Bot` | `ChatGPT` | `Cursor` | `Claude Code` | `OpenClaw` | `Hermes`
> Toggle: `MCP` | `CLI`
>
> **1. Copy the ✳ Higgsfield connector URL** — *"You'll paste this URL into Claude in the
> next step"* → campo con **`https://mcp.higgsfield.ai/mcp`** [+ icona copia]
>
> **2. Go to Claude → Customize** — *"In Claude desktop or claude.ai, go to Customize →
> Connectors, Name it Higgsfield and paste the URL."* → bottone **Open Claude Customize**
>
> **3. Connect, sign in and start** — *"Sign in, then ask Claude to generate an image or
> video."* → bottone **Start creating**
>
> Nota a pie': *"If you are using **Claude Code or Codex**, it's better to use the CLI ⇢
> GitHub"*
>
> Sotto: **HOW DOES MCP WORK?** con tab `Marketing` | `Faceless videos` | `Website building` |
> `Video generation` | `Image generation`

Il prompt di connessione dettato a voce (6:21-6:27), verbatim:
> *"hey I want you to connect to the Higgsfield CLI so we can create beautiful images and
> videos. Here's the link"*

#### 3b — Il sito costruito: RIDGELINE

Da `6:47` in poi il video mostra il risultato: un sito di copertura tetti chiamato
**Ridgeline**, servito come file locale — `file:///Users/jackroberts/Desktop/ridgeline-roofing/index.html`
(`frame-216.png @ 7:10`, `frame-255.png @ 8:28`, e decine di frame successivi).

**Hero, verbatim** (`frame-216/226/255`):
> Badge: `NEW · Same-day storm response across the country →`
>
> **H1: "The roof your house was supposed to have"**
>
> Sub: *"Inspection, repair and replacement for homes and businesses, with a written scope
> before anyone climbs a ladder."*
>
> Form: [Email address] [**Book my inspection**]
>
> Micro-copy sotto: *"Free, and you keep the report whether you hire us or not."*
>
> Nav: Home · Services · About us · Projects · Blog | Contact us | **Book an inspection**

**Il "report d'ispezione" interattivo** immediatamente sotto l'hero (`_zoom/z216.png`):
finto pannello software con sidebar `Overview · Findings · Photographs · Materials · Scope of
works · Enclosed · Warranty`, barra di ricerca "Search this report", bottone "+ Ask a roofer".
Intestazione: `Inspection · 14 May` — **"What we found up there"** — *"Single-storey hip roof ·
24 squares · architectural asphalt, 19 years old"*. Findings:
1. **"Flashing failed at the chimney saddle"** — *"Water is tracking behind the
   counter-flashing into the deck."* → tag "To plan"
2. **"Granule loss on the south slope"** — *"Sun-side wear consistent with age. Watch, do not
   replace yet."*
3. **"Decking is sound throughout"** — *"No soft spots. No sheathing replacement in this
   quote."* → tag "Not priced"

**Sezione "Built to outlast the mortgage"** (`frame-229.png @ 7:36`, `frame-486.png @ 16:10`):
> **"Built to outlast the mortgage"** — *"Four things decide whether a roof lasts, and not
> one of them is the shingle you picked off a board in a showroom."*
>
> `ALL SEVEN LAYERS` — **"Every layer priced, not just the shingle"** — *"Ask any quote which
> underlayment, how many nails, and whether the ice shield runs the valleys. Ours answers all
> three in writing before you sign."*
>
> `SAME-DAY MAKE-SAFE` — **"Someone is on the roof today"** — *"Active leaks get tarped before
> anything else happens. We stop the damage first and quote the repair once the weather lets
> us see properly."*
>
> `[COMMERCIAL / INDUSTRIAL]` — *"[Holdin]g the same standard [in a] building that cannot
> close — [Flat and low]-slope systems sequenced around your trading hours, with a
> [maintenance] record you can hand straight to an insurer."* → **Explore commercial →**

**Sezione "Loved by your favorite companies"** (`frame-240.png @ 7:58`, `frame-249.png @ 8:16`,
`frame-254.png @ 8:26`, `frame-488.png @ 16:14`) — il pezzo di design piu' citato dall'autore:
> **"Loved by your favorite companies"** — *"From head offices to trading floors, the region's
> best keep their roofs with Ridgeline."*
>
> Carosello di card, ognuna con logo su fondo scuro testurizzato + una frase + `Read story →`:
> - **OpenAI** — *"How [OpenAI] keeps its research [running] through a full storm."*
> - **Anthropic** — *"How Anthropic re-roofed its HQ without moving a single team off-site."*
> - **Slack** — *"How Slack's atrium skylights were re-kerbed over one quiet weekend."*
> - **PayPal** — *"How PayPal's data-centre roof passed its insurer audit first time."*
> - **Notion** — *"How Notion turned a leaking warehouse into its calmest office."*
> - **Spotify** — *"How Spotify's studio block was soundproofed from the roof down."*
> - **Stripe** — *"How Stripe's listed HQ kept its copper roof and its character."*
> - **Dropbox** — *"How Dropbox consolidated four roofs onto one maintenance plan."*

Cliccando un logo si apre la **customer story** collegata (`frame-488.png @ 16:14`):
> `CUSTOMER STORY` — **"84 squares re-roofed without losing a trading day"** — `Read story →`
> Metriche: **84** *"Squares of single-ply"* · **0** *"Trading days lost"*
>
> (in un'altra story: **120** *"Your design life on the copper"* · **2** *"Conservation
> sign-offs secured"*, titolo *"Copper detailed to last another century"*)

Piu' sotto: *"[A building that need]s to never shut — [...]ays, out of hours and across
weekends. Your staff arrive to a clean floor and your customers never see a barrier."* e
**"A record an insurer accepts"** — *"Dated photographs, measured scopes and a maintenance
log. When a claim comes, the evidence already exists."*

In basso a destra del sito c'e' una **barra a tab flottante**: `Website | System | Graphics |
Copy` (`frame-216`, `frame-479`, `frame-510`) — il sito e' anche il proprio making-of.

#### 3c — LA DESIGN LOOP SKILL (il pezzo di metodo piu' forte del video)

A `4:20-4:52` l'autore apre la sua guida Notion (`app.notion.com` — pagina **"The Design Loop:
Free Guide"**, `frame-131.png @ 4:20`, `frame-140.png @ 4:38`). Testo trascritto integralmente
dai ritagli `_zoom/z131.png` e `_zoom/z140a.png`:

> 🍎 **Claude Design has taste. It just can't judge its own work.**
>
> *The context that builds a piece is the context that grades it — a chef reviewing their own
> restaurant. Five stars, every time. The Design Loop fixes exactly that: it moves the judging
> into **fresh contexts** that never saw the work being made.*
>
> *Parallel agents buy you speed. **Fresh context buys you the result.***

> ## Source of the Gauntlet loop
>
> This method is an adaptation of the **Gauntlet Loop**, invented by **Matt Shumer**. He named
> it, defined it, and built the original — a Three.js FPS from a single prompt that did 3.8M
> views. Everything on this page is a variation on his idea.

Sotto, il tweet originale di **Matt Shumer** (@mattshumer_) incorporato:
> *"I'm officially calling this the Gauntlet Loop. The agent (not you!) breaks the goal into
> parts, gives each part a specialist builder and a ruthless blind critic sub-agent, with a
> mandate to only pass if the generated artifact is better than some real-world equivalent."*
>
> Prompt nella risposta: *"I want you to build a first-person shooter at the level of the most
> recent Call of Duty games. It should be utterly perfect, visually beautiful, with every
> single thing done at AAA quality—from textures to physics to [anything you would think of]."*
>
> 9:52 PM · Jul 27, 2026 — 787 [reazioni] / 63.4k views

**Il corpo della skill** — a `4:48` l'autore incolla la skill dentro Claude e nel messaggio si
legge la tabella dei suoi quattro meccanismi (`frame-145.png @ 4:48`, ritaglio
`_zoom/z145.png`), trascritta verbatim:

| Meccanismo | Perche' esiste |
|---|---|
| A **teardown pass** into `bar.md` | Converts a reference into checkable mechanisms *before* any building starts |
| **Three critics with distinct briefs** | Each can fail work the other two would pass — one "harsh critic" collapses into a single opinion |
| A **preflight** check | Verifies the critic can actually see before you waste a whole run |
| **Model tiering** across critics | Cheap where judgment is mechanical, strongest where it's taste |

> 🍎 **The one thing to remember**
>
> *A critic that shares memory with the builder is **grading its own homework**. Everything
> else here is detail.*

**Come si invoca**: a `10:22-10:24` l'autore dice, verbatim: *"you're going to do forward
slash. You type in **design loop**."* — cioe' e' una **slash-skill di Claude**, `/design loop`.
La guida gratuita si scarica dalla pagina risorse dell'autore (secondo link in descrizione).

#### 3d — UI sniping applicato: il widget preventivo tetto

Flusso completo, 9:23-11:56:
1. **Savee** (`savee.com`, pronunciato "save with two E", `frame-284.png @ 9:26`): sidebar
   `Pop | Store`, barra di ricerca *"What are you searching for?"*.
   **Popular searches**: Poster · Graphic Design · Logo · Photography · Portfolio · Typography.
   **Recents** dell'autore: `contact form design`, `contact form`, `form ui`.
   **Trending saves**: @rustan_ale, @nuecxdesigner, @fjfjcky.
   Cerca `dashboard ui` → suggerimenti: dashboard ui · dashboard ui clean · dashboard ui design ·
   dashboard ui floating cards · dashboard ui infographic showcase · dashboard ui minimal
   (`frame-287.png @ 9:32`, `frame-294.png @ 9:46`).
2. Cerca `signup form` (`frame-298.png @ 9:54`) e trova il riferimento
   (`frame-303/304.png @ 10:04-10:06`): una card con illustrazione ad acquerello e testo
   *"Welcome, you're starting your first journey here! Add your avatar and pick a nickname for
   quick start."* — campi `Your avatar` + `Upload`, `Display name`, bottone
   **"Create an account"**.
   Il problema dichiarato a voce (10:08-10:16): *"The problem with this is this is not a
   component. This is not a UI thing that we can just grab. We need to literally basically
   create this, but in the style for our own website."*
3. **Il prompt a Claude**, dettato a voce (10:26-10:44), verbatim:
   > *"Hey there, I want you to make a roofing version of this. And what I would like you to
   > do is enable them to upload an image of the roof, answer a few questions, and then I want
   > a beautiful **Siri-like animation** to play and then actually show what the price is for
   > them, and we can capture that information."*

   — piu' l'immagine di riferimento incollata.
4. **Il riferimento per l'animazione** (`frame-327.png @ 10:52`): torna su Savee e scarica un
   video — card scura con un'esplosione radiale di particelle bianche e la scritta
   **"Calculating."** — come *"video overview suggestion for Claude to use"*.
5. **Il risultato** (`frame-333.png @ 11:04`, `frame-341.png @ 11:20`): file locale
   `file:///Users/jackroberts/Desktop/roof-quote-section/welcome-card.html` — card verticale
   con illustrazione ad acquerello blu di tetti di case, titolo **"A free quote for your roof."**,
   campi: `Your roof` (*"A photo helps accuracy. PNG or JPG — optional"*) + **Upload**;
   `Postcode` [M1 4BT]; `The roof` [Full replacement ▾]; bottone nero **"Get my price"**.
   Stati dell'animazione narrati a voce (11:13-11:19): *"checking pitch and tiles"*, *"price of
   materials"*, *"almost there"*, *"having a look around"* → risultato: **£7,150**.
   Card finale (`frame-341.png @ 11:20`): **FULL REPLACEMENT · £7,150** — *"Fixed price
   confirmed by a free 20-minute survey."* + **Book free survey** + fila di avatar +
   **★★★★★ 4.9 from 812 roofs**.
6. **Integrato nel sito** (`frame-582.png @ 19:22`, `frame-588.png @ 19:34`):
   > `SIXTY SECONDS` — **"Get a number before anyone visits"** — *"Postcode, roof type, a
   > photograph if you have one. The free survey confirms the number. It does not move after
   > that."*

   con due prove sociali a hover: **"Booked in this week"** e **"4,800 roofs kept dry"**.
7. **Dettaglio di rifinitura dichiarato a voce** (11:39-11:51): *"at the bottom of the image
   you can see... it's got white. Now ideally these drops would have finished so it looks like
   a true blend in, but it's kind of phased out a little bit."* — ammette un difetto di
   fusione dell'immagine col fondo, non lo nasconde.

**Un secondo esempio di scroll-stopper** (`frame-276/277.png @ 9:10-9:12`): il sito
**PULP** su `pulp-cinema-[...].vercel.app` — hero video a pieno schermo di un vortice di
succo, capitolo `CH 03 — THE BLEND`, headline **"Drink the riot."** — *"Four flavors. Zero
manners. Straight from the orchard you just fell through."* CTA **"Find your flavor"**,
bottone **FLAVORS** in alto a destra.

---

### LIVELLO 4 — MOBILE (12:41-14:53)

**Slide** (`frame-448.png @ 14:54`, ritaglio `_zoom/z448.png`): *SKILL 04 · MOBILE* —
**04** — **"Where the traffic is"**. Striscia inferiore:
**`· LIVE DEMO · EVERY PAGE AUDITED AT 390PX ·`** — frase-ponte:
**`next: words that don't sound like AI.`**

`390px` e' la larghezza logica di un iPhone 14/15 in portrait: **il numero operativo del
livello 4**, dichiarato solo nella slide e mai a voce.

**Il dato**: *"60% of traffic at least actually is on our phones"* (12:55).

**Il prompt**, dettato a voce (13:21-13:35), verbatim:
> *"Hey, I want you to mobile optimize this website. Go out and find for me the most
> proficient, well-read repos that have been battle tested that will make sure that it
> follows all of the best mobile design principles."*

**Il metodo dell'autore, dichiarato** (14:22-14:35): *"we'd start off with the mobile first and
then work backwards to get to the actual full desktop version. And there is no substitute but
to actually going through the mobile yourself. Claude can do loads of checks using the
rea[dme/repo] that I'll share below in the skills section, but ultimately speaking you want to
go through the website yourself and check it out."*

**Mobile-first, poi a ritroso verso il desktop — e la verifica finale e' umana, sempre.**

**La verifica a schermo** (`frame-414.png @ 13:46`, `frame-418/419.png @ 13:54-13:56`,
`frame-425.png @ 14:08`): trascina il bordo della finestra restringendola progressivamente e
mostra il sito ricomporsi ad ogni frame rate. Cosa cambia davvero nella versione stretta:
- la nav si chiude in un **hamburger** (dichiarato a voce, 14:16)
- la fila di 5 loghi diventa **griglia 2 colonne** (OpenAI/Anthropic — Slack/PayPal — Stripe)
- il carosello "Loved by your favorite companies" diventa **swipe orizzontale con frecce**
- il report d'ispezione diventa **lista verticale con foto impilate**

Ammissione a voce (13:49-13:55): *"believe it or not, it did not look like this initially. I
had to do this... it's not perfect."*

Sullo sfondo di queste riprese, sulla meta' sinistra dello schermo, e' visibile il suo
**Claude Code OS** (vedi sezione "b-roll" sotto).

---

### LIVELLO 5 — DE-SLOPIFICATION (14:53-18:30)

**Slide** (`frame-450.png @ 14:58`, ritaglio `_zoom/z450.png`): *SKILL 05 · COPY* — **05** —
**"De-slopification"** — citazione: *"Readers smell AI copy in one line."*

**Le parole al bando, come chip barrati rossi** (trascritte una per una dall'ingrandimento 7x):
```
It's not just X, it's Y      seamless      unlock      elevate      robust      leverage
faster, smarter, better      Let's dive in
```

**La pipeline, come tre chip collegati da frecce**:
```
BENCHMARK  →  REWRITE  →  CLEANSE
```

Frase-ponte: **`next: the details that finish it`**

#### 5a — La tab "Copy" del sito Ridgeline

Il sito ha una quarta tab, `Copy`, che e' la **documentazione del proprio copy**
(`frame-479.png @ 15:56`, ritaglio `_zoom/z479.png`):

> `LEVEL 4 · COPY`
>
> **The copy system**
>
> *"The site arrived as a wireframe full of `Lorem ipsum` and `Medium length section heading
> goes here`. This tab is the record of what replaced it, the rules that decided each line, and
> a switch at the bottom that rewrites the live page in front of you."*
>
> ## Where it comes from
>
> *"Not from a brand workshop. Every line traces to one of four sources, and if a sentence
> cannot name its source it does not go on the page."*

Le **quattro fonti** (i titoli delle colonne sono **coperti dall'overlay webcam** in tutti i
frame disponibili — riporto i corpi, leggibili, e marco i titoli come non letti):
1. `[titolo coperto dalla webcam]` — *"['Six nails p]er shingle, every shingle' is a real
   specification with a real failure mode behind it. Nothing invented sounds like that, because
   invented copy does not [know the trade]."*
2. `[titolo coperto]` — *"[...that the ti]mber will move, that the yard will be wrecked, that
   they are being sold a whole roof for a flashing problem. The page answers those three in
   order."*
3. `[titolo coperto]` — *"[...goes one le]vel further than promises. 'We do not do overlays' and
   'we do not quote from the driveway' both position and disqualify in one line."*
4. `[titolo coperto]` — *"[...two lines] came in from the layout already written — the process
   steps and *From first call to final nail*. They were better than anything a rewrite would
   produce, [and were left] untouched."*

➕ **Inferenza dichiarata**: dalla struttura e dai corpi, le quattro fonti sono plausibilmente
*(1) cosa fa davvero il mestiere, (2) cosa il cliente gia' teme, (3) cosa la concorrenza non
dira', (4) le righe del layout che erano gia' buone*. **Non l'ho letto**: e' ricostruzione, non
osservazione.

**La sezione "WHERE IT COMES FROM" con le fonti tecniche** (`frame-479`, `frame-482.png @ 16:02`):
- icona GitHub — **"36,087 ★"** — *"Built on the leading open-source humanisers. All four MIT."*
- **"Signs of AI writing"** — *"Wikipedia's canonical catalogue of the tells. By the people who
  clean them up."*
- **"GPT-5.6 cleanse"** — *"A frontier model, sceptical — never trusted without the limiter on
  both sides."*
- **"World-class copy"** — *"Benchmarked live against the category's best. Headlines scored
  verbatim."*
- **"delve"** — *"65 words · 8 shapes"* [descrizione parzialmente illeggibile]
- **"3/5 → 5/5"** — *"This page, measured before and after — **not asserted**."*

Bottone gigante: **"ACTIVATE MAGIC COPY"** — *"Flips every line on the Website tab to its
rewritten version, live. Press it, then switch tabs and watch the page change under you."*

#### 5b — LA TABELLA "SIGNS OF AI WRITING" (il pezzo piu' riusabile del video)

`frame-510.png @ 16:58` (ritaglio 3x `_zoom/z510.png`) + `frame-514.png @ 17:06` +
`frame-520.png @ 17:18`, incrociati con la lettura a voce (16:47-17:56):

> **02 Signs of AI writing**
>
> *"These are the tells that get a line rewritten on sight. Every one of them showed up in a
> first draft of this page and was cut. Struck-through is what was written; green is what
> shipped."*

| # | Il tell | ~~Prima~~ | → Dopo | La regola |
|---|---|---|---|---|
| 1 | **The three-item flourish** | ~~Trusted, reliable and built to last.~~ | **Six nails per shingle, every shingle.** | *"Three adjectives is a rhythm, not an argument. One specification beats it every time."* |
| 2 | **"Not just X, but Y"** | ~~Not just a roof, but peace of mind.~~ | **A written scope and a fixed number before anyone climbs a ladder.** | *"The construction promises a reveal and then delivers an abstraction."* |
| 3 | **Elevated verbs** | ~~We leverage industry-leading materials to deliver unparalleled protection.~~ | **We source materials from manufacturers who test for wind, hail and sun.** | *"Leverage, deliver, unparalleled, seamless, robust, elevate. All of them mean nothing and cost a line."* |
| 4 | **Empty superlatives** | ~~The area's most trusted roofing experts.~~ | **Roofing, and only roofing, since 2001.** | *"'Most trusted' is unfalsifiable, so the reader discounts it entirely. A date cannot be argued with."* |
| 5 | **M-dash pileup** | ~~Our team — trained, certified and local — is ready to help.~~ | **Thirty-eight on the crew, factory-trained for every material we install.** | *"One dash in a paragraph is punctuation. Three is a tic."* |
| 6 | **Numeri inventati** | ~~Loved by 10,000+ happy homeowners.~~ | **Project names and photography are placeholders — swap in your own jobs before this ships.** | *"Inventing a number is the one unrecoverable mistake. Say the slot is empty instead."* |

Su questa ultima riga l'autore commenta a voce (17:55-18:00): *"that one's just telling me that
like I built placeholders, so that one's not a good idea, but you get the idea"* — **riconosce
lui stesso che la riga 6 e' una nota di cantiere finita in pagina, non un esempio di copy.**

#### 5c — Il "before → after" su un secondo prodotto (Neuro)

`frame-499.png @ 16:36` — stesso sistema applicato a **neuro-ai-[...].vercel.app**, un'app di
allenamento al prompting. Riquadro **"EVERY LINE, BEFORE → AFTER"**:

**THE HERO (4 LINES)**

| ~~Prima~~ | → Dopo |
|---|---|
| ~~Get started~~ | **Start free** |
| ~~A Fun Way to learn [AI]~~ | **Everyone uses AI. Almost nobody is good at it.** |
| [nuova riga] | **Neuro is five minutes a day of real prompting problems, marked the second you answer. You stop guessing at what works.** |
| ~~Get started~~ | **Start your first lesson** |

**THE HABIT**

| ~~Prima~~ | → Dopo |
|---|---|
| ~~the streak does the work~~ | **the hard part is day four** |
| ~~Miss a day and your streak resets — which turns out to be motivation enough. You get five hearts a day, a wrong ans[wer] costs one, and they refill overnight. Small stakes, daily [rely...]~~ | **Motivation gets you through day one. A strea[k gets] you through day four. Miss a day and it resets, which turns out to be all the pressure anyone needs. You get five hearts a day, one per wrong answer, refilled overnight.** |
| ~~Start a streak~~ | **Start day one** |

Sul sito Neuro (`frame-460.png @ 15:18`) la stessa disciplina applicata alle prove:
> `THE METHOD` — **"built on how people actually learn"** — *"Two techniques do the work.
> **Retrieval practice** means recalling a skill instead of rereading it. **Spaced repetition**
> brings a concept back just as you're about to forget it."*
>
> Riquadro grigio: *"Both are among the most-replicated findings in learning science. **Neuro is
> new, so this evidence is for the method, not for us.**"*
>
> CTA: **TRY A LESSON**

Quest'ultima frase e', da sola, una lezione di onesta' di copy: **si cita la prova per il
metodo e si dichiara di non averne ancora per se stessi.**

#### 5d — La psicologia sotto (16:50-17:24, solo a voce)

> *"it's underpinned by some core psychology. One of the best psychological principles in
> building anything is this idea of **don't make me think**. The idea essentially being that
> people don't read websites, they browse them. I need to be able to **glance** at it and
> understand what the website is about. Don't take anybody's time for granted... if I have to
> invest a minute to understand what your website is about, it's too much. So general idea, use
> the **system one cognition**. Just make it super easy. **You want to name the pain.**"*

*(L'autore si autocorregge a voce: dice "system two", poi si corregge in "system one".)*

**Repo citato in descrizione**: `👻 SlopMonster: https://github.com/ItsssssJack/SlopMonster` —
**mai aperto a schermo nel video**, solo linkato.

---

### LIVELLO 6 — ICONS + SHOWSTOPPERS / UI SNIPING (18:30-20:30)

**Slide** (`frame-557.png @ 18:32`, ritaglio `_zoom/z557.png`): *SKILL 06 · DETAILS* — **06** —
**"Icons + showstoppers"**. Sotto, una fila di **8 loghi di librerie di icone**. Numero
dichiarato: **`941 LICENSED ICONS`** — *"one subscription, in the repo, forever"*.
Striscia: **`· LIVE DEMO · ONE UI MOMENT SNIPED FROM SAVEE, REBUILT IN OUR BRAND ·`**
Frase-ponte: **`next: nobody can find it yet`**

**La definizione, a voce** (18:35-18:42): *"this is what I call **UI sniping**. UI sniping is
the idea that we can find any UI component that we like and bring it over."*

**Lo strumento: 21st.dev** (`frame-568.png @ 18:54`): sidebar
`Components` (Featured · Newest · Authors · **Libraries [Updated]**) e
`Marketing Blocks` (Announcements · **ASCII Art [New]** · Backgrounds · Borders ·
Calls to Action · Clients · Comparisons). In alto a destra: "Upgrade 2 free", "Feedback".
Sotto **Newest** e **Popular** si vedono: "Orbital Sphere", "Start Free Plan ✦",
"Scroll Animations (Container Scroll Animation)", "Interactive 3D", card stack.
Nella categoria **Borders** (`frame-571.png @ 19:00`, `21st.dev/s/community/components/border`):
tab `Recommended | Most downloaded | Most bookmarked | Newest`, componenti "Shine Border",
"Border Beam", "Click to upload or drop files", "Get 25% Annual Return", "Click me".

**Il flusso, a voce** (19:07-19:19): *"If you've got the Relume MCP you can just ask it, or if
you're grabbing it from a different website like 21st.dev you can come down and literally just
**copy the code**, head over to Claude and say: **'Hey, add this to my website.'**"*

**Le icone** (19:41-20:29): cita **Icons8**, **Flaticon**, **IconScout** — *"I think the one
I'm using right now is Flaticon. Not sponsored."* Costo dichiarato: **"$10 to 12"** al mese per
stare su una di queste piattaforme.
`flaticon.com` a schermo (`frame-596.png @ 19:50`): sezione **‹UICONS›** — *"The most wanted
free SVG user interface icons"* — con quattro stili e i conteggi reali:
**Bold 50,689 icons** · **Regular 10,899 icons** · **Solid 10,899 icons** · **Thin 10,899 icons**.
Consiglio di targeting (19:57-20:05): *"if you're doing a kind of new-age cool vibe, younger
demographic — millennial or Gen Z or below — you may want to use cool graphics."*

---

### LIVELLO 7 — SEO-IFICATION (20:30-22:43)

**Slide** (`frame-619.png @ 20:36`, ritaglio `_zoom/z619.png`): *SKILL 07 · SEO* — **07** —
**"SEO-ification"** — citazione: *"Grab a skill. Point Claude at the site. Approve the fixes."*
Tre chip con i nomi delle skill: **`claude-seo`** · **`amazing-seo-skill`** ·
**`seo-audit-skill`**.
Striscia: **`· LIVE DEMO · META, SCHEMA AND OG PATCHED ON CAMERA ·`**
Ultima frase-ponte: **`last: make it live.`**

#### 7a — La skill: `claude-seo` su GitHub

`frame-623.png @ 20:44`, `frame-628.png @ 20:54`, `frame-629.png @ 20:56` — repo GitHub
`claude-seo`. Testo **About** trascritto dall'ingrandimento (`_zoom/z623.png`):

> *"Universal SEO skill for Claude Code. **25 sub-skills + 18 sub-agents** covering technical
> SEO, E-E-A-T, schema, GEO/AEO, backlinks, local SEO, maps intelligence, semantic clustering,
> e-commerce SEO, international SEO, Google APIs, and PDF/Excel reporting. Optional
> **DataForSEO, Firecrawl, and Banana** extensions."*
>
> 🔗 `claude-seo.md`

Topics: `claude-seo-md` · `ai` · `ai-seo` · `claude-code` · `claude-code-skill` ·
`marketing-automation` · `open-source` · `seo`.
Rilascio in evidenza: **"Claude SEO v2.2.5 - Reliability and Google currency"** (Latest).
Repo: 9 Branches, 23 Tags, **23 Releases**, **17 Contributors**.
Linguaggi: **Python ~60%**, **PowerShell ~15%**, Shell, HTML ~1.7%, JavaScript.
File in root: `CHANGELOG.md`, `CITATION.cff`, **`CLAUDE.md`**, `CODE_OF_CONDUCT.md`,
`CONTRIBUTING.md`, `CONTRIBUTORS.md`, `LICENSE`, `PRIVACY.md`, `README.md`, `SECURITY.md`,
**`install.ps1`**, **`install.sh`**.

Banner README: `claude seo` + comando d'esempio **`/seo-backlinks rival.com`**.
Testo README: *"[Claude] SEO is an open-source SEO analysis plugin for **Claude Code**. It runs
25 sub-skills and 18 specialist agents across technical SEO, content quality (E-E-A-T),
Schema.org markup, AI search optimization (GEO), local [SEO], e-commerce, and international SEO.
Every audit produces a prioritized action plan with testable [recommen]dations grounded in
primary-source guidance from Google."*

Due versioni dichiarate:
- **Public open-source** → MIT, public releases, no membership. *"Use this if you want stable +
  downloadable."*
- **Community private mirror** → *"early access to upcoming features and direct collaboration
  with the AI Marketing Hub Pro community. (Requires membership)"*

#### 7b — IL PROMPT SEO (il piu' lungo e il piu' prezioso del video)

Dettato a voce, 21:00-21:39, trascritto verbatim:

> *"Hey, I want you to go ahead and **find for me the best SEO design strategies that exist on
> the internet**, and I want you to **take a look at this SEO repo**, and I want you to **build
> a checklist and a strategy for my website** — the things that I can rank for. Here are some
> of the keywords that I want to rank for, here's the kind of intent that I want to do, and **I
> want you to question me on my customer** so that we together can find out the **long-tail
> intention words**, the **short intention words**, and I want you to **rank those based on
> volume and also difficulty**. And from that we're going to build up an SEO strategy, a
> content roadmap, and we're going to find SEO suggestions for our own website."*

Cinque mosse dentro un solo prompt: (1) ricerca esterna sullo stato dell'arte, (2) lettura del
repo-skill, (3) checklist + strategia, (4) **intervista di ritorno sul cliente** — l'unico
prompt del video in cui si chiede all'AI di fare domande, (5) ranking volume x difficolta'.

#### 7c — L'output reale: la strategia SEO di Glaido

`frame-652.png @ 21:42`, `frame-655.png @ 21:48`, `frame-656.png @ 21:50` — l'autore apre un
**artifact pubblico di Claude** (`claude.ai/public/artifacts/...`) intitolato
**"Glaido SEO Strategy"**. Glaido e' la sua startup speech-to-text.

Copertina (ritaglio `_zoom/z652.png`):
> `Glaido` | `SEO STRATEGY / 19 AUGUST 2026`
>
> # **OWN VOICE CODING**
>
> *"The biggest undefended demand in this category is not dictation. It is people trying to code
> by talking — and almost nobody has written the pages for it. This is the plan for taking that
> lane, with every keyword sized, sorted and ready to copy."*
>
> **119,000** — *"US searches a month in the coding lane"* — *"Vibe coding, voice coding, Claude
> Code voice, Cursor voice. Estimated, ±50%."*
>
> **4** — *"Pages Whisp[e]r Flow has built there"* — *"Out of 306 pages in total. They have not
> noticed yet."*
>
> **0** — *"Pages Glaido has built there"* — *"The 351 keywords in this document close that gap."*

Indice: `01 Why voice coding, not dictation` — *"The demand data, and the three things it
changed about the plan."* · `02 The whole list, one click` · `03 Short tail — the head terms`.

Riga di posizionamento (`frame-655.png`): *"[...an] expensive product, so 'cheaper alternative'
is off the table. Our wedges are **zero data retention, speed, and the coding lane**."*

Sezione 02: **"Master list — 351 keywords as TSV"** + bottone **`COPY ALL`** — *"Columns:
keyword · est. vol · int. search/mo · demand index · difficulty · verdict. Paste straight into
Sheets or Excel."*

Sezione 03: **"Short tail — the head terms"** — *"Broad head terms. Big volume, slow to win, and
a few of them are traps. Sorted by volume."* Filtri a chip: `TAKE` · `EASY` · `LATER`
(*Month two or three*) · `SKIP` (*Wrong intent or unwinnable*) — e la nota di normalizzazione:
*"demand index relative to 'dictation app' = 100"*.

**La tabella, riga per riga** (`frame-656.png @ 21:50`):

| KEYWORD | EST. VOL/MO | DEMAND INDEX | DIFFICULTY | VERDICT | WHY |
|---|---|---|---|---|---|
| speech to text | ~280,000 | 2670 | HARD | **SKIP** | *"Video-editing intent — CapCut, Premiere, DaVinci. Wrong buyer."* |
| voice to text | ~155,000 | 1470 | HARD | **LATER** | *"Mostly mobile intent. Glaido is desktop-only."* |
| vibe coding | ~92,000 | 870 | HARD | **LATER** | *"Huge and adjacent. Our single biggest editorial head term."* |
| talk to type | ~39,000 | 370 | MEDIUM | **LATER** | *"Clean intent, no strong incumbent page."* |
| best voice to text | ~26,000 | 250 | HARD | **LATER** | *"[Lateral filter — buyers] see this first."* |
| whisper flow | ~25,000 | 240 | MEDIUM | **LATER** | *"Their brand is the biggest branded term in the category."* |
| voice typing | ~18,000 | 170 | HARD | **SKIP** | *"Google Docs and Windows built-ins own it."* |
| best voice to text app | ~14,000 | 137 | HARD | **SKIP** | *"App store intent, mostly mobile."* |
| voice coding | ~12,000 | 111 | MEDIUM | **EASY** | *"Barely defended. Closest head term to what we do."* |
| dictation app | ~10,000 | 100 | HARD | **LATER** | *"The obvious term, and the most contested."* |
| ai dictation | ~10,000 | 100 | MEDIUM | **EASY** | *"Right intent, beatable SERP."* |
| claude code voice | ~8,700 | 83 | EASY | **EASY** | *"Almost nobody has written this page. [Ship it] this week."* |

Numeri dichiarati a voce (21:56-22:02): **28 keyword** su cui posizionarsi e long-tail come
*"Whisper Flow alternative"* — **mentre il documento a schermo dice 351 keyword totali**.
I due numeri non coincidono: **28 e' plausibilmente il sottoinsieme "TAKE/EASY"**, ma il video
non lo dichiara ➕.

#### 7d — Deploy (22:14-22:33)

> *"to post it, you just need to basically tell Claude to **upload this to GitHub in a private
> repo**... And then you can run the entire thing from **Vercel**. Vercel hosts everything. It
> even hosts many of the websites that I show you on this channel. Super duper easy to set up.
> Explain to Claude and it will explain it to you step by step."*

`vercel.com` a schermo (`frame-668.png @ 22:14`, `frame-673.png @ 22:24`): headline
**"Agentic Infrastructure"** con tre righe *"For coding agents / To ship apps and agents /
Automated by agents"*, banner *"Vercel Agent works where you do → Add to Slack"*, e loghi
Charles Schwab, DoorDash, OpenAI, Supreme, The Weather Company, Polymarket.

---

### WHAT'S NEXT (22:43-22:56)

Chiusura in talking-head (`frame-679/683/686/688`), verbatim:
> *"these design skills are handy and they do help us build beautiful websites that sell. But
> the truth is, **if you don't have your own design operating system, you're leaving way too
> many hours and productivity and value on the table**. Which is why the next thing that we
> need to do is learn how to set one of these up, which we're going to do in this video right
> [here]."*

**Il cliffhanger e' esplicito: le 7 skill sono i pezzi; il video successivo promette il
sistema che li orchestra (design OS).**

---

## IL B-ROLL PROMOZIONALE — cosa mostra davvero (dichiarato)

Il video alterna al contenuto tre blocchi promozionali. Li elenco perche' contengono
informazione tecnica reale sull'assetto dell'autore, non solo pubblicita'.

### 1. La community Skool (11:56-12:34, `frame-133/134/136/137`)
`skool.com/ai-automation-vault` — **"AI Automation Vault"** — *"Free community to get started
with AI Automations (Claude Code, Cowork, AntiGravity etc..)"*.
**33.3k Members · 324 Online · 5 Admins**. Private · Free · By Jack Roberts.
Post visibili: *"Kimi K3 Builds $20,000 Websites in 19 Mins"* — corpo: *"Hey there, ✋ **Skill
attached to this post → Download ZIP and hand to Claude Code.**"* — e *"Claude Code just got 10X
Better (Codex + Gemini)"*.

### 2. Il corso "Claude Code FULL COURSE (Build & Sell)" (12:02-12:36, `frame-362/364/377`)
`claude-code-curriculum-deploy.vercel.app` — badge **"THE CURRICULUM · 10 PARTS · 46 LESSONS ·
40+ HOURS"**. Sezioni: 01 Foundation · 02 Website · 03 Power Features · 04 Memory ·
05 Hermes Agent · 06 Apps · 07 Build Anything · **08 Design** · 09 Compliance.
Stack in fondo: Vercel, Supabase, Stripe, GitHub, Pinecone, NotebookLM, Gmail, Notion.

**Sezione 08 Design, lezione per lezione** (`frame-377.png @ 12:32`) —
`5 LESSONS · CLAUDE CODE DESIGN · [PI]PE, SOUND · SPLINE · IMAGES · LOGOS`:
- **8.1 Claude Code Design (NEW)** — Use the workbook / Animations baked in / Export and share
- **8.2 HTML presentations** — Drop in for any website / CSS only / SVG patterns / Motion that
  converts
- **8.3 Animated graphics**
- **8.4 Spline 3D** — Turn 3D to worth it / prompt walkthrough
- **8.5 ElevenLabs + Higgsfield** — Voice generation / Video generation / Combining pipeline
- **8.6 Nano Banana images** — Best prompt patterns / Production workflow / Quality control
- **Auto-fetch brand assets** — *"Just enter your logo from any URL, with **Firecrawl**"*

**Sezione 01 Foundation** (`frame-364.png @ 12:06`), utile come mappa di cosa considera
"fondamenta" di Claude Code: 1.1 Install · 1.2 The interface tour (Terminal vs GUI, Antigravity
vs VS Code) · 1.3 Free vs Pro vs Max · **1.4 Permission modes** (Before edits / Edit
automatically / Bypass) · **1.5 The 5 Claude surfaces** (Chat · Cowork · Claude [Code] ·
Managed Agents · [SDK/API]) · **1.6 Daily slash commands** (`/context` `/compact` `/clear`
`/agent` `/init`) · 1.7 Organize your desktop · 1.8 Connect your tools (Dropbox, Gmail,
Firecrawl, YouTube, Notion, Drive) · **1.9 Folder structure** (dove vivono le Skills, dove va
`CLAUDE.md`) · 1.10 Git + GitHub backup · **1.11 CLAUDE.md + Plan Mode**.

**Sezione 07 Build Anything**: 7.1 *First principles system design* ("The Musk framework") ·
7.2 *Lead scraping + Instantly* (Apify + Firecrawl → arricchimento via Claude → push a
Instantly) · 7.3 *Marketing agency stack*.

### 3. Il "Claude Code OS" dell'autore (12:18-14:10, `frame-370/373/374/399/419/425`)
Applicazione web servita in locale su **`localhost:8081`**, sidebar: `Home · Dashboard · Memory ·
Knowledge Graph`, piu' due voci in evidenza **`HERMES-AGENT`** e **`OPEN CLAUDE`**.

- **`/memory`** — un knowledge graph a nodi colorati su fondo nero, con sotto una tabella
  file/stato: `[...]_daily_radar.md · telegram_debugging · HIGH ACC`, `[...]_case_playbook.md ·
  MEMORY · HIGH ACC`, `Welcome · 2026-04-08 · HIGH ACC`, `[...]_levels_overnight.md · README ·
  HIGH ACC`. Colonne: **Stale** / **Missing**.
- **`/dashboard`** — header `Operator | local | v0.2 | HEALTHY`. Card di consumo:
  **Claude Code / Claude Max 20x** → `5-HOUR LIMIT 69% (145)`, `WEEKLY - ALL MODELS 2,735
  (5,200)`, `[OPUS] ONLY 18 (2,220)`; **ChatGPT / ChatGPT Plus** → `6%`.
  Riga "Trends over time — TRACKING STARTED TODAY": `MESSAGES 2,735`, `WEEKLY WINDOW 80%`,
  `SKILL RUNS 196`.
- **Il "DREAM REVIEW"** (`frame-374.png @ 12:26`) — la parte piu' interessante:
  > **DREAM REVIEW — 4 improvements from 31 days ago**
  >
  > *"Pattern analysis across 7 days · generated 25 Jul, 11:41 · `claude-nightdream-cron.log`"*
  >
  > [**REPLAY THE DREAM**] · Engine: **CODEX**
  >
  > `WORKFLOW · [$14/m] · 145 min saved`
  >
  > **"Collapse the duplicate morning briefs before another 80-message run"**
  >
  > *"Keep one strategic morning brief schedule and make the Google Workspace check its
  > preflight. Two strategic brief schedules ran yesterday, while today's run consumed another
  > 87 messages. Fetch inbox and calendar once, fail last when either source is unavailable,
  > then perform one synthesis pass. Inspect the cron list before removing or changing
  > anything."*
  >
  > `▸ WHY WE'RE SUGGESTING THIS ⌄`
  >
  > **TRY IT NOW — COPY THIS AND PASTE INTO CLAUDE CODE** → `hermes cron list`
  >
  > [**RUN THIS FIX**] · [SKIP] · [APPLY & MARK DONE]
  >
  > Tile in basso: `Activity` · `Antigravity` · `Memory Files` · `Integrations` · `Automations`

Questo pannello **non e' spiegato a voce**: e' b-roll. Ma mostra un pattern architetturale
completo — **un cron notturno che analizza i log di 7 giorni, produce raccomandazioni con
risparmio stimato in minuti e in dollari, e le consegna come comando copiabile con tre esiti
(Run / Skip / Apply & mark done)**.

---

## TUTTI GLI STRUMENTI CITATI — tabella

| Strumento | URL | A cosa serve nel flusso | Costo dichiarato nel video |
|---|---|---|---|
| **refers.design** | `refers.design` / `styles.refers.design` | Livello 1 — trovare lo standard ed estrarre il `DESIGN.md` (design DNA) | non dichiarato · ha **Connect MCP** |
| **Relume** | `relume.ai` | Livello 2 — brief → sitemap → wireframe → style guide → export | Trial Pro; *"50% of your AI usage this cycle"* sul piano free |
| **Higgsfield** | `higgsfield.ai` · `mcp.higgsfield.ai/mcp` | Livello 3 — immagini e video generati per sezione; connettore MCP/CLI | non dichiarato (link affiliato in descrizione) |
| **Savee** | `savee.com` | Livelli 3 e 6 — UI sniping, riferimenti visivi e animazioni | non dichiarato |
| **21st.dev** | `21st.dev` | Livello 6 — componenti UI copiabili come codice | non dichiarato |
| **Flaticon** | `flaticon.com` | Livello 6 — icone (UICONS: Bold 50.689 / Regular 10.899 / Solid 10.899 / Thin 10.899) | **$10-12/mese** |
| **Icons8** | `icons8.com` | Livello 6 — icone | **$10-12/mese** |
| **IconScout** | `iconscout.com` | Livello 6 — icone | **$10-12/mese** |
| **claude-seo** | GitHub, repo `claude-seo` | Livello 7 — 25 sub-skill + 18 sub-agent SEO per Claude Code | MIT, gratis (mirror privato a pagamento) |
| **SlopMonster** | `github.com/ItsssssJack/SlopMonster` | Livello 5 — de-slopification (**solo linkato, mai mostrato**) | gratis |
| **Vercel** | `vercel.com` | Deploy | non dichiarato |
| **GitHub** | `github.com` | Repo privato prima del deploy | non dichiarato |
| **Design Loop** | guida Notion gratuita dell'autore | Livello 3 — la skill `/design loop` (critici a contesto fresco) | gratis, dietro pagina risorse |
| **Glaido** | (startup dell'autore) | Esempio SEO reale | codice **WHSAAKXO** per 1 mese gratis (descrizione) |
| **Notion** | `app.notion.com` | Ospita la guida Design Loop | — |
| **Skool** | `skool.com/ai-automation-vault` | Community gratuita (33.3k membri) | gratis |

---

## TUTTI I PROMPT DEL VIDEO — trascritti

1. **Brief a Relume** (2:47): *"hey that I want you to build for me a roofing company that is
   best-in-class using the below design principles"* + URL/DESIGN.md da refers.design
2. **Consegna a Claude** (digitato, `frame-123`): *"hey there i want you to go ahead and build
   for me a beautiful website based on this particular link using the exact design systems and
   layouts that are included in this zip file that we built in relume"*
3. **Connessione Higgsfield** (6:21): *"hey I want you to connect to the Higgsfield CLI so we
   can create beautiful images and videos. Here's the link"*
4. **Componente su misura** (10:26): *"Hey there, I want you to make a roofing version of this.
   And what I would like you to do is enable them to upload an image of the roof, answer a few
   questions, and then I want a beautiful Siri-like animation to play and then actually show
   what the price is for them, and we can capture that information."*
5. **Mobile** (13:21): *"Hey, I want you to mobile optimize this website. Go out and find for me
   the most proficient, well-read repos that have been battle tested that will make sure that it
   follows all of the best mobile design principles."*
6. **UI sniping** (19:17): *"Hey, add this to my website."* + codice incollato da 21st.dev
7. **SEO** (21:00): il prompt lungo in 5 mosse, trascritto per intero al §7b
8. **Deploy** (22:14): *"tell Claude to upload this to GitHub in a private repo"*
9. **Invocazione skill** (10:22): `/design loop` (slash command)

---

## I NUMERI REALI DEL VIDEO

| Numero | Cosa misura | Fonte |
|---|---|---|
| **7** | livelli/skill del metodo | struttura del video |
| **60%** | quota minima di traffico da mobile | voce @12:55 |
| **390px** | larghezza a cui va auditata ogni pagina | slide 04, `frame-448` |
| **2M+** | siti costruiti col sistema di componenti Relume | slide 02 + `relume.ai` |
| **1,000+** | componenti responsive nella libreria Relume | `relume.ai`, `frame-574` |
| **941** | icone licenziate "in the repo, forever" | slide 06, `frame-557` |
| **$10-12/mese** | costo di una piattaforma di icone | voce @20:09 |
| **351** | keyword nel master list SEO di Glaido | artifact, `frame-655` |
| **28** | keyword su cui posizionarsi (dichiarato a voce) | voce @21:57 — **non coincide con 351** |
| **119,000** | ricerche/mese US nella "coding lane" | artifact, `frame-652` |
| **4 / 0** | pagine del competitor / pagine di Glaido su quella lane | artifact, `frame-652` |
| **±50%** | margine d'errore dichiarato sulle stime di volume | artifact, `frame-652` |
| **306** | pagine totali del competitor Whisper Flow | artifact, `frame-652` |
| **25 + 18** | sub-skill + sub-agent di `claude-seo` | About del repo, `frame-623` |
| **36,087 ★** | stelle dei repo humaniser open source usati | tab Copy, `frame-479` |
| **3/5 → 5/5** | punteggio del copy misurato prima/dopo | tab Copy, `frame-479` |
| **£7,150** | preventivo restituito dal widget demo | voce @11:21 + `frame-341` |
| **4.9 / 812** | rating · numero recensioni sulla card finale | `frame-341` |
| **50,689 / 10,899 x3** | icone UICONS per stile su Flaticon | `frame-596` |
| **33.3k / 324 / 5** | membri / online / admin della community Skool | `frame-134` |
| **10 / 46 / 40+** | parti / lezioni / ore del corso a pagamento | `frame-362` |
| **97.2M / 132,025 / 540** | token / messaggi / sessioni Claude dell'autore | `frame-123` |
| **2,735 / 5,200** | messaggi settimanali usati / limite su Claude Max 20x | `frame-373` |
| **196** | skill runs registrate dal suo OS in un giorno | `frame-373` |
| **145 min / [$14/m]** | risparmio stimato da una singola raccomandazione notturna | `frame-374` |
| **3.8M** | views del video FPS originale di Matt Shumer | guida Notion, `frame-131` |

---

## CONFRONTO CON DIGITAL EMPIRE

### Dove l'Impero e' gia' avanti
- **Design system proprietario**: `.claude/agents/guild-design.md` (380 righe) codifica **due
  standard distinti** — A Empire Premium (schermo) e B AP Sales Minimal (documenti) — con la
  regola di scelta esplicita e 14 principi non negoziabili (stack obbligatorio Next.js 16 +
  Tailwind v4 + Lenis + Framer Motion + GSAP, token frozen, grana obbligatoria, sezioni
  alternate). Il video **non ha nulla di equivalente**: prende in prestito il design system di
  un altro sito ogni volta.
- **Sistema visivo generato per progetto**: `.claude/skills/site-design/SKILL.md` (509 righe)
  produce `SITE-DESIGN.md` + `design-tokens.css` + `style-guide.html` + `tailwind.config.js`,
  con filosofia visiva nominata e 3 principi. Il `DESIGN.md` di refers.design e' **lo stesso
  artefatto, ma estratto da un sito esistente invece che progettato** — sono complementari,
  non concorrenti.
- **Copy**: APSOC, `cro-copy-architect`, `guild-copy-apsoc` (688 righe), `sentinel-brandvoice`
  (che gia' vigila su claim senza prova e frasi Barnum) sono piu' strutturati del sistema del
  video sul lato *persuasione*.
- **Pipeline di sito**: `site-brief → site-plan → site-design → site-copy → site-build →
  site-qa` copre gia' cio' che il video ottiene con Relume.

### Dove il video e' davanti — i tre buchi veri
1. **Nessun critico a contesto fresco.** L'Impero ha sentinelle e gate (`sentinel-quality`,
   `guild-quality`, `apex-critic`), ma **nessuna regola scritta che imponga che il giudice non
   condivida la memoria del costruttore**. E' esattamente il principio del Design Loop:
   *"a critic that shares memory with the builder is grading its own homework"*. Verificato:
   `grep` su `.claude/agents` non trova nessuna formulazione di questo invariante.
2. **Nessuna lista operativa di tell dell'AI nel copy.** `copywriting/references/natural-
   transitions.md`, `cf-humanizer-agent`, `sentinel-brandvoice` toccano il tema, ma la tabella a
   6 tell con coppie prima/dopo e la regola dietro ognuno **non esiste in nessun file
   dell'Impero** — ed e' la cosa piu' immediatamente applicabile del video.
3. **Nessun numero di audit mobile.** `site-qa-mobile` esiste come agente, ma nel corpus non
   compare la larghezza operativa **390px** ne' la regola *mobile-first, poi a ritroso*.

### Dove il video non aggiunge nulla
- **SEO**: `claude-seo` e' un repo esterno; l'Impero ha gia' `seo-audit`, `ai-seo`,
  `programmatic-seo`, `site-seo`, `schema`, `market-seo`. Il prompt SEO in 5 mosse e' buono ma
  la sua parte nuova e' una sola: **"question me on my customer"**.
- **Deploy**: GitHub privato + Vercel e' gia' `site-deploy` / `deploy-cloud` / `vercel:deploy`.
- **Icone e componenti**: nomi di siti, non metodo.

---

## COSA IL VIDEO NON MOSTRA — avvertenze dichiarate

1. **Il corpo completo della skill Design Loop non e' mai a schermo.** Se ne vede la tabella dei
   4 meccanismi e l'aside finale. Il resto (come si scrive `bar.md`, quali sono i tre brief dei
   critici, come si configura il model tiering) e' dietro la pagina risorse dell'autore.
2. **SlopMonster non e' mai aperto.** E' il repo che darebbe la lista completa dei tell: solo
   linkato in descrizione.
3. **La generazione con Higgsfield non e' mai mostrata dal vivo**, malgrado la slide 03 dica
   *"MOTION, GENERATED ON CAMERA"*. Si vedono solo i risultati.
4. **La chiamata a Claude non e' mai mostrata mentre lavora.** Si vede il prompt digitato
   (`frame-123`) e si vede il sito finito. Il passaggio in mezzo — quanto tempo, quante
   iterazioni, quanti errori — non c'e'.
5. **Il "before" del sito non esiste a schermo.** L'autore dice *"it did not look like this
   initially. I had to do this"* ma non mostra la versione rotta.
6. **28 vs 351 keyword**: incoerenza tra voce e schermo, non spiegata.
7. **I titoli delle quattro fonti del copy sono coperti dalla webcam** in tutti i frame
   disponibili — ricostruiti solo per inferenza, marcati ➕.
8. **Il video e' a 360p.** Tutti i valori esadecimali dei token colore sono al limite
   della leggibilita' e alcuni sono marcati `[incerto]` o `[illeggibile]`.
9. **Contenuto misto educativo/promozionale**: circa 90 secondi su 1376 (~6.5%) sono promo di
   community gratuita e corso a pagamento, piu' tre link affiliati dichiarati in descrizione
   (Higgsfield, Relume, Glaido con codice sconto).

---

*Analisi prodotta da Empire Studio · run `max17-v11-roberts-design` · 2026-09-03 ·
NO-FINTO: ogni riga sopra e' letta da un frame reale o dalla trascrizione, le inferenze sono
marcate ➕ e le illeggibilita' sono dichiarate.*
