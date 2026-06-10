# paino da fare
            
> Path: [[Map - Workfolw_Crea_Caroselli_À|Workfolw crea caroselli à]]

## Content

SISTEMA COMPLETO: Carousel Factory
Panoramica dell'architettura
text

🧠 CONTEXT ENGINE          🎨 DESIGN ENGINE         ⚡ AUTOMATION
(Claude + files .md)       (Templates HTML/CSS)      (Node.js + Puppeteer)
                           (oppure Figma)
        │                        │                         │
   Genera JSON ──────────► Popola template ──────────► Esporta PNG
   strutturato               con dati                   1080x1080
FASE 0 — Struttura cartelle
Crea questa struttura esatta sul tuo computer:

text

📁 carousel-factory/
│
├── 📁 brands/
│   ├── 📁 brand-personal/
│   │   ├── config.json
│   │   ├── style.css
│   │   └── 📁 assets/
│   │       ├── grain-overlay.png
│   │       ├── logo.png
│   │       └── 📁 fonts/
│   │           ├── Montserrat-Black.ttf
│   │           ├── Montserrat-Bold.ttf
│   │           └── Montserrat-Regular.ttf
│   │
│   ├── 📁 brand-agency/
│   │   ├── config.json
│   │   ├── style.css
│   │   └── 📁 assets/
│   │       └── ...
│   │
│   └── 📁 brand-education/
│       ├── config.json
│       ├── style.css
│       └── 📁 assets/
│           └── ...
│
├── 📁 context/
│   ├── SYSTEM.md
│   ├── copywriting-rules.md
│   ├── slide-types.md
│   ├── hook-formulas.md
│   ├── cta-formulas.md
│   └── 📁 examples/
│       ├── example-carousel-1.json
│       └── example-carousel-2.json
│
├── 📁 templates/
│   ├── base.html
│   ├── hook-cover.html
│   ├── text-statement.html
│   ├── quote-block.html
│   ├── list-items.html
│   ├── diagram.html
│   └── cta-finale.html
│
├── 📁 scripts/
│   ├── generate.js
│   ├── render.js
│   └── export-all.js
│
├── 📁 output/
│   └── 📁 [data]-[titolo]/
│       ├── slide-01.png
│       ├── slide-02.png
│       └── ...
│
└── package.json
FASE 1 — Context Engineering (il cervello)
File 1: context/SYSTEM.md
Markdown

# SISTEMA GENERATORE CAROSELLI

## Chi sei
Sei un sistema di generazione caroselli per social media.
Il tuo output è SEMPRE un JSON strutturato, MAI testo libero.

## Regole assolute
1. Ogni carosello ha tra 7 e 10 slide
2. Slide 1 = SEMPRE hook/cover (ferma lo scroll)
3. Slide finale = SEMPRE CTA
4. Ogni slide ha MAX 20 parole
5. Il testo grande ha MAX 3-5 parole (impatto visivo)
6. Il testo piccolo introduce/contestualizza
7. Alterna slide "pesanti" (testo enorme) a slide "ariose"
8. Ogni slide deve far venire voglia di swipare

## Formato output obbligatorio
Rispondi SEMPRE con questo JSON:

{
  "brand": "nome-brand",
  "titolo": "titolo del carosello",
  "caption": "caption per il post Instagram con hashtag",
  "slides": [
    {
      "numero": 1,
      "tipo": "hook-cover | text-statement | quote-block | 
              list-items | diagram | cta-finale",
      "testo_piccolo": "testo introduttivo sopra",
      "testo_grande": "PAROLE\nIMPATTO",
      "testo_accent": "parola evidenziata nel colore accent",
      "colore_override": null,
      "sfondo_img": "keyword per immagine sfondo (opzionale)",
      "note_design": "indicazioni specifiche per il design"
    }
  ]
}

## Regole per tipo di slide

### hook-cover
- Deve fermare lo scroll in 0.5 secondi
- Testo grande: provocatorio, controverso o numerico
- Può avere immagine di sfondo scurata

### text-statement
- Una frase forte, grande, centrata
- Testo piccolo sopra che introduce
- Massimo impatto tipografico

### quote-block
- Virgolette grandi decorative
- Citazione o frase chiave
- Stile cinematografico

### list-items
- 3-4 elementi con icone
- Testo chiaro e gerarchico
- Ogni item: max 5 parole

### diagram
- Frecce, connessioni, flussi semplici
- Max 4 elementi collegati
- Visuale > testuale

### cta-finale
- Call to action chiara
- "Segui per...", "Salva questo post", "Link in bio"
- Urgenza o beneficio
File 2: context/copywriting-rules.md
Markdown

# REGOLE DI COPYWRITING

## Tono di voce per brand
- brand-personal: diretto, crudo, zero fuffa, 
  parla come un amico esperto che non ha paura di dire la verità
- brand-agency: professionale ma non noioso, 
  dati + provocazione
- brand-education: didattico, step-by-step, 
  "ti spiego come funziona davvero"

## Pattern che funzionano per l'hook (Slide 1)
1. NUMERO + PROVOCAZIONE: "5 cose che nessuno ti dice su..."
2. ERRORE COMUNE: "Stai facendo [cosa] nel modo sbagliato"
3. CONTRASTO: "Tutti fanno X. I pro fanno Y."
4. DOMANDA: "Perché il tuo [cosa] non funziona?"
5. SHOCK: "Ho smesso di fare [cosa]. Ecco perché."
6. RISULTATO: "[Risultato specifico] in [tempo]"

## Pattern per le slide centrali
- Una idea per slide, MAI di più
- Inizia con il problema, poi la soluzione
- Usa "tu" non "voi"
- Frasi spezzate su più righe per impatto
- Le parole chiave vanno nel testo_accent

## Pattern per la CTA (Slide finale)
1. "Segui @nome per [beneficio specifico]"
2. "Salva questo post, ti servirà"
3. "Commenta [parola] se vuoi [cosa]"
4. "Link in bio per [cosa specifica]"
File 3: context/slide-types.md
Markdown

# STRUTTURE CAROSELLO COLLAUDATE

## Struttura 1: PROBLEMA → SOLUZIONE
1. Hook: il problema comune
2. Amplifica il dolore
3. Perché succede
4. La soluzione (intro)
5. Step 1
6. Step 2
7. Step 3
8. Risultato/prova
9. CTA

## Struttura 2: LISTA ERRORI
1. Hook: "X errori che fai con..."
2. Errore 1
3. Errore 2
4. Errore 3
5. Errore 4
6. Errore 5
7. Cosa fare invece (riassunto)
8. CTA

## Struttura 3: CONTROINTUITIVO
1. Hook: affermazione shock
2. "Tutti pensano che..."
3. "Ma in realtà..."
4. Prova/esempio 1
5. Prova/esempio 2
6. "Quindi cosa fare?"
7. La strategia
8. CTA

## Struttura 4: CASE STUDY / STORIA
1. Hook: risultato ottenuto
2. "La situazione di partenza"
3. "Il problema principale"
4. "Ho provato X (non ha funzionato)"
5. "Poi ho scoperto Y"
6. "Come l'ho applicato"
7. "Il risultato"
8. "La lezione"
9. CTA

## Struttura 5: FRAMEWORK / METODO
1. Hook: "Il metodo [nome] per [risultato]"
2. Overview del framework
3. Pillar 1
4. Pillar 2
5. Pillar 3
6. Come si collegano
7. Primo step per iniziare
8. CTA
File 4: context/examples/example-carousel-1.json
JSON

{
  "brand": "brand-personal",
  "titolo": "Il portfolio è inutile",
  "caption": "Il portfolio non serve a niente se lavori in...",
  "slides": [
    {
      "numero": 1,
      "tipo": "hook-cover",
      "testo_piccolo": "dura verità per freelance:",
      "testo_grande": "IL PORTFOLIO\nÈ MORTO",
      "testo_accent": "MORTO",
      "colore_override": null,
      "sfondo_img": "laptop-dark-office",
      "note_design": "Immagine sfondo scurata al 80%, testo grande centrato"
    },
    {
      "numero": 2,
      "tipo": "text-statement",
      "testo_piccolo": "ho pensato...",
      "testo_grande": "le aziende\nvogliono\nvendere",
      "testo_accent": "vendere",
      "colore_override": null,
      "sfondo_img": null,
      "note_design": "Sfondo scuro puro, virgolette decorative rosse"
    },
    {
      "numero": 3,
      "tipo": "text-statement",
      "testo_piccolo": "e lo vogliono più di",
      "testo_grande": "ogni\naltra\ncosa",
      "testo_accent": null,
      "colore_override": "#FFD700",
      "sfondo_img": "businessman-leaning",
      "note_design": "Foto sfondo con persona, testo oro grande"
    },
    {
      "numero": 4,
      "tipo": "diagram",
      "testo_piccolo": "esempio: sei un copywriter. col portfolio:",
      "testo_grande": "",
      "testo_accent": null,
      "colore_override": null,
      "sfondo_img": null,
      "note_design": "3 frecce che partono da portfolio: non capiscono strategia, si concentrano sul testo, pensano non funziona per me"
    },
    {
      "numero": 5,
      "tipo": "list-items",
      "testo_piccolo": "ma per:",
      "testo_grande": "il portfolio è\n(quasi) inutile",
      "testo_accent": "inutile",
      "colore_override": null,
      "sfondo_img": null,
      "note_design": "3 pill/badge: copywriting (oro), developer (azzurro), SMM (arancione)"
    }
  ]
}
FASE 2 — Brand Configuration
File: brands/brand-personal/config.json
JSON

{
  "brand_name": "brand-personal",
  "display_name": "Il tuo nome",
  "instagram": "@tuohandle",
  
  "colors": {
    "background": "#1A1A1A",
    "background_alt": "#111111",
    "text_primary": "#FFFFFF",
    "text_secondary": "#CCCCCC",
    "text_muted": "#888888",
    "accent_1": "#FF3B3B",
    "accent_2": "#FFD700",
    "accent_3": "#4A9EFF"
  },
  
  "typography": {
    "font_hero": "Montserrat-Black",
    "font_bold": "Montserrat-Bold",
    "font_regular": "Montserrat-Regular",
    "size_hero": "90px",
    "size_large": "64px",
    "size_medium": "36px",
    "size_small": "24px",
    "line_height_hero": "0.95",
    "line_height_body": "1.3",
    "letter_spacing_hero": "-2px",
    "text_transform_hero": "lowercase"
  },
  
  "effects": {
    "grain_opacity": 0.15,
    "grain_intensity": "medium",
    "text_shadow": "0 4px 30px rgba(0,0,0,0.8)",
    "glow_accent": "0 0 40px rgba(255,59,59,0.3)",
    "background_blur": "8px",
    "vignette": true,
    "vignette_intensity": 0.4
  },
  
  "layout": {
    "canvas_width": 1080,
    "canvas_height": 1080,
    "padding": "60px",
    "text_align": "left"
  }
}
Crea un file simile per ogni brand, cambiando colori, font e stile.

FASE 3 — Template HTML/CSS (il design engine)
File: templates/base.html
HTML

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  @font-face {
    font-family: 'Hero';
    src: url('{{FONT_PATH}}/Montserrat-Black.ttf');
  }
  @font-face {
    font-family: 'Bold';
    src: url('{{FONT_PATH}}/Montserrat-Bold.ttf');
  }
  @font-face {
    font-family: 'Regular';
    src: url('{{FONT_PATH}}/Montserrat-Regular.ttf');
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    width: 1080px;
    height: 1080px;
    overflow: hidden;
    position: relative;
    background: {{BG_COLOR}};
  }

  /* === GRANA CINEMATOGRAFICA === */
  .grain {
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.4'/%3E%3C/svg%3E");
    opacity: {{GRAIN_OPACITY}};
    pointer-events: none;
    z-index: 100;
    mix-blend-mode: overlay;
  }

  /* === VIGNETTATURA === */
  .vignette {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: radial-gradient(
      ellipse at center,
      transparent 40%,
      rgba(0,0,0,{{VIGNETTE_INTENSITY}}) 100%
    );
    pointer-events: none;
    z-index: 99;
  }

  /* === CONTENUTO === */
  .content {
    position: relative;
    width: 100%;
    height: 100%;
    padding: {{PADDING}};
    display: flex;
    flex-direction: column;
    justify-content: center;
    z-index: 10;
  }

  /* === TIPOGRAFIA === */
  .text-small {
    font-family: 'Regular', sans-serif;
    font-size: {{SIZE_SMALL}};
    color: {{TEXT_SECONDARY}};
    margin-bottom: 16px;
    line-height: {{LINE_HEIGHT_BODY}};
  }

  .text-hero {
    font-family: 'Hero', sans-serif;
    font-size: {{SIZE_HERO}};
    color: {{TEXT_PRIMARY}};
    line-height: {{LINE_HEIGHT_HERO}};
    letter-spacing: {{LETTER_SPACING_HERO}};
    text-shadow: {{TEXT_SHADOW}};
  }

  .text-hero .accent {
    color: {{ACCENT_1}};
    text-shadow: {{GLOW_ACCENT}};
  }

  /* === SFONDO IMMAGINE === */
  .bg-image {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background-size: cover;
    background-position: center;
    z-index: 1;
  }

  .bg-overlay {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: linear-gradient(
      180deg,
      rgba(0,0,0,0.6) 0%,
      rgba(0,0,0,0.85) 100%
    );
    z-index: 2;
  }
</style>
</head>
<body>

  <!-- Sfondo immagine (opzionale) -->
  {{BG_IMAGE_BLOCK}}

  <!-- Contenuto slide -->
  <div class="content">
    {{SLIDE_CONTENT}}
  </div>

  <!-- Effetti -->
  <div class="vignette"></div>
  <div class="grain"></div>

</body>
</html>
File: templates/hook-cover.html
HTML

<!-- Si inserisce dentro {{SLIDE_CONTENT}} di base.html -->

<div class="text-small">{{TESTO_PICCOLO}}</div>
<div class="text-hero">
  {{TESTO_GRANDE_BEFORE_ACCENT}}
  <span class="accent">{{TESTO_ACCENT}}</span>
  {{TESTO_GRANDE_AFTER_ACCENT}}
</div>
File: templates/text-statement.html
HTML

<div style="position: relative;">
  <!-- Virgolette decorative -->
  <div style="
    position: absolute;
    top: -40px; left: -20px;
    font-size: 200px;
    color: {{ACCENT_1}};
    opacity: 0.15;
    font-family: 'Hero';
    line-height: 1;
  ">"</div>
  
  <div class="text-small">{{TESTO_PICCOLO}}</div>
  <div class="text-hero">
    {{TESTO_GRANDE_BEFORE_ACCENT}}
    <span class="accent">{{TESTO_ACCENT}}</span>
    {{TESTO_GRANDE_AFTER_ACCENT}}
  </div>

  <div style="
    position: absolute;
    bottom: -120px; right: 20px;
    font-size: 200px;
    color: {{ACCENT_1}};
    opacity: 0.15;
    font-family: 'Hero';
    line-height: 1;
  ">"</div>
</div>
File: templates/list-items.html
HTML

<div class="text-small">{{TESTO_PICCOLO}}</div>

<div style="
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin: 40px 0;
">
  {{#each ITEMS}}
  <div style="
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 18px 28px;
    border: 2px solid {{ITEM_COLOR}};
    border-radius: 50px;
    width: fit-content;
  ">
    <span style="font-size: 24px;">{{ITEM_ICON}}</span>
    <span style="
      font-family: 'Bold';
      font-size: 32px;
      color: {{ITEM_COLOR}};
    ">{{ITEM_TEXT}}</span>
  </div>
  {{/each}}
</div>

<div class="text-hero" style="margin-top: 30px;">
  {{TESTO_GRANDE_BEFORE_ACCENT}}
  <span class="accent">{{TESTO_ACCENT}}</span>
</div>
File: templates/cta-finale.html
HTML

<div style="
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  height: 100%;
">
  <div class="text-hero" style="
    text-align: center;
    margin-bottom: 40px;
  ">{{TESTO_GRANDE}}</div>
  
  <div style="
    padding: 20px 48px;
    background: {{ACCENT_1}};
    border-radius: 60px;
    font-family: 'Bold';
    font-size: 28px;
    color: white;
  ">{{CTA_BUTTON}}</div>
  
  <div style="
    margin-top: 30px;
    font-family: 'Regular';
    font-size: 22px;
    color: {{TEXT_MUTED}};
  ">{{INSTAGRAM_HANDLE}}</div>
</div>
FASE 4 — Script di Rendering
Installa dipendenze
Bash

cd carousel-factory
npm init -y
npm install puppeteer fs-extra handlebars
File: scripts/render.js
JavaScript

const puppeteer = require('puppeteer');
const fs = require('fs-extra');
const path = require('path');
const Handlebars = require('handlebars');

async function renderCarousel(carouselData) {
  const brand = carouselData.brand;
  
  // 1. Carica config brand
  const config = await fs.readJson(
    path.join(__dirname, '..', 'brands', brand, 'config.json')
  );
  
  // 2. Carica template base
  let baseHTML = await fs.readFile(
    path.join(__dirname, '..', 'templates', 'base.html'), 'utf8'
  );
  
  // 3. Sostituisci variabili brand nel base
  baseHTML = replaceBrandVars(baseHTML, config);
  
  // 4. Crea cartella output
  const date = new Date().toISOString().split('T')[0];
  const slug = carouselData.titolo
    .toLowerCase()
    .replace(/\s+/g, '-')
    .replace(/[^a-z0-9-]/g, '');
  const outputDir = path.join(
    __dirname, '..', 'output', `${date}-${slug}`
  );
  await fs.ensureDir(outputDir);
  
  // 5. Avvia browser
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox']
  });
  
  // 6. Genera ogni slide
  for (const slide of carouselData.slides) {
    console.log(`Rendering slide ${slide.numero}...`);
    
    // Carica template specifico per tipo
    const templatePath = path.join(
      __dirname, '..', 'templates', `${slide.tipo}.html`
    );
    let slideContent = await fs.readFile(templatePath, 'utf8');
    
    // Popola il template con i dati della slide
    slideContent = populateSlide(slideContent, slide, config);
    
    // Inserisci nel base
    let finalHTML = baseHTML.replace('{{SLIDE_CONTENT}}', slideContent);
    
    // Gestisci sfondo immagine
    if (slide.sfondo_img) {
      finalHTML = finalHTML.replace('{{BG_IMAGE_BLOCK}}', `
        <div class="bg-image" style="
          background-image: url('${slide.sfondo_img}');
        "></div>
        <div class="bg-overlay"></div>
      `);
    } else {
      finalHTML = finalHTML.replace('{{BG_IMAGE_BLOCK}}', '');
    }
    
    // Renderizza con Puppeteer
    const page = await browser.newPage();
    await page.setViewport({ width: 1080, height: 1080 });
    await page.setContent(finalHTML, { 
      waitUntil: 'networkidle0' 
    });
    
    // Screenshot
    const fileName = `slide-${String(slide.numero).padStart(2, '0')}.png`;
    await page.screenshot({
      path: path.join(outputDir, fileName),
      type: 'png',
      clip: { x: 0, y: 0, width: 1080, height: 1080 }
    });
    
    // Salva anche l'HTML (per debug)
    await fs.writeFile(
      path.join(outputDir, `slide-${String(slide.numero).padStart(2, '0')}.html`),
      finalHTML
    );
    
    await page.close();
  }
  
  // 7. Salva caption
  await fs.writeFile(
    path.join(outputDir, 'caption.txt'),
    carouselData.caption
  );
  
  await browser.close();
  console.log(`\n✅ Carosello generato in: ${outputDir}`);
  console.log(`📊 ${carouselData.slides.length} slide create`);
}

function replaceBrandVars(html, config) {
  const replacements = {
    '{{BG_COLOR}}': config.colors.background,
    '{{TEXT_PRIMARY}}': config.colors.text_primary,
    '{{TEXT_SECONDARY}}': config.colors.text_secondary,
    '{{TEXT_MUTED}}': config.colors.text_muted,
    '{{ACCENT_1}}': config.colors.accent_1,
    '{{ACCENT_2}}': config.colors.accent_2,
    '{{ACCENT_3}}': config.colors.accent_3,
    '{{SIZE_HERO}}': config.typography.size_hero,
    '{{SIZE_LARGE}}': config.typography.size_large,
    '{{SIZE_MEDIUM}}': config.typography.size_medium,
    '{{SIZE_SMALL}}': config.typography.size_small,
    '{{LINE_HEIGHT_HERO}}': config.typography.line_height_hero,
    '{{LINE_HEIGHT_BODY}}': config.typography.line_height_body,
    '{{LETTER_SPACING_HERO}}': config.typography.letter_spacing_hero,
    '{{TEXT_SHADOW}}': config.effects.text_shadow,
    '{{GLOW_ACCENT}}': config.effects.glow_accent,
    '{{GRAIN_OPACITY}}': config.effects.grain_opacity,
    '{{VIGNETTE_INTENSITY}}': config.effects.vignette_intensity,
    '{{PADDING}}': config.layout.padding,
    '{{FONT_PATH}}': `../brands/${config.brand_name}/assets/fonts`,
  };
  
  for (const [key, value] of Object.entries(replacements)) {
    html = html.replaceAll(key, value);
  }
  return html;
}

function populateSlide(template, slide, config) {
  // Splitta testo grande intorno all'accent
  let beforeAccent = slide.testo_grande || '';
  let afterAccent = '';
  
  if (slide.testo_accent && slide.testo_grande) {
    const parts = slide.testo_grande.split(
      new RegExp(`(${slide.testo_accent})`, 'i')
    );
    if (parts.length >= 2) {
      beforeAccent = parts[0] || '';
      afterAccent = parts[2] || '';
    }
  }
  
  const accentColor = slide.colore_override || config.colors.accent_1;
  
  template = template
    .replaceAll('{{TESTO_PICCOLO}}', slide.testo_piccolo || '')
    .replaceAll('{{TESTO_GRANDE}}', slide.testo_grande || '')
    .replaceAll('{{TESTO_GRANDE_BEFORE_ACCENT}}', beforeAccent)
    .replaceAll('{{TESTO_ACCENT}}', slide.testo_accent || '')
    .replaceAll('{{TESTO_GRANDE_AFTER_ACCENT}}', afterAccent)
    .replaceAll('{{ACCENT_1}}', accentColor)
    .replaceAll('{{INSTAGRAM_HANDLE}}', config.instagram || '')
    .replaceAll('{{TEXT_MUTED}}', config.colors.text_muted);
  
  // Sostituisci \n con <br>
  template = template.replace(
    /(?<=<[^>]*>)([^<]*?)\\n/g, 
    '$1<br>'
  );
  
  return template;
}

// Esporta
module.exports = { renderCarousel };
File: scripts/generate.js (il main)
JavaScript

const fs = require('fs-extra');
const path = require('path');
const { renderCarousel } = require('./render');

async function main() {
  // Leggi il JSON del carosello (generato da Claude)
  const inputFile = process.argv[2];
  
  if (!inputFile) {
    console.log('Uso: node generate.js <file-carousel.json>');
    console.log('Es:  node generate.js ./input.json');
    process.exit(1);
  }
  
  const carouselData = await fs.readJson(inputFile);
  
  console.log(`🎨 Brand: ${carouselData.brand}`);
  console.log(`📝 Titolo: ${carouselData.titolo}`);
  console.log(`📊 Slide: ${carouselData.slides.length}`);
  console.log('');
  
  await renderCarousel(carouselData);
}

main().catch(console.error);
FASE 5 — Il Workflow completo
Come usi il sistema ogni giorno:
text

STEP 1                    STEP 2                    STEP 3
   │                         │                         │
Apri Claude              Salva il JSON             Esegui script
con i file               come input.json
di contesto
   │                         │                         │
   ▼                         ▼                         ▼

"Genera carosello        Copi il JSON          node generate.js
brand-personal           nell'editor            input.json
su: come trovare         e salvi
clienti high-ticket"         │                      │
   │                         │                      ▼
   ▼                         │              📁 output/
Claude ti dà             input.json         ├── slide-01.png
il JSON completo                            ├── slide-02.png
                                            ├── ...
                                            └── caption.txt




FASE 6 — Setup con Claude Code (automazione totale)
Se usi Claude Code, puoi fare tutto in un comando:

File: CLAUDE.md (nella root del progetto)
Markdown

# ISTRUZIONI PER CLAUDE CODE

## Questo progetto
Sistema di generazione caroselli automatizzato.

## Quando ti chiedo di creare un carosello:
1. Leggi il brand richiesto da brands/[nome]/config.json
2. Usa le regole in context/SYSTEM.md
3. Usa le regole copy in context/copywriting-rules.md
4. Genera il JSON strutturato
5. Salvalo in /tmp/carousel-input.json
6. Esegui: node scripts/generate.js /tmp/carousel-input.json
7. Mostrami il path dell'output

## Comandi utili
- Generare: node scripts/generate.js <file.json>
- Preview: open output/<cartella>/slide-01.png

## Non fare mai
- Non cambiare i template senza chiedere
- Non modificare i config brand
- Non usare font diversi da quelli nel brand
Poi in Claude Code scrivi semplicemente:

text

> Crea un carosello per brand-personal sul tema 
  "5 motivi per cui il tuo funnel non converte". 
  Stile provocatorio. 8 slide.
E Claude Code fa tutto da solo: genera il JSON, esegue lo script, crea le PNG.

FASE 7 — Grana di alta qualità
Per la grana cinematografica che hai nelle tue slide, crea un overlay reale:

Opzione A: Scarica grain overlay pro (consigliato)
Cerca su Google: "film grain overlay PNG free 1080x1080"
Salvalo come brands/brand-personal/assets/grain-overlay.png

Poi nel base.html sostituisci il blocco .grain con:

CSS

.grain {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background-image: url('{{GRAIN_OVERLAY_PATH}}');
  background-size: cover;
  opacity: {{GRAIN_OPACITY}};
  mix-blend-mode: overlay;
  pointer-events: none;
  z-index: 100;
}
Opzione B: Grain generato via CSS (più controllabile)
CSS

.grain {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  pointer-events: none;
  z-index: 100;
  mix-blend-mode: overlay;
  opacity: 0.18;
}

.grain::before {
  content: '';
  position: absolute;
  top: -200%; left: -200%;
  width: 500%; height: 500%;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' seed='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/%3E%3C/svg%3E");
  background-size: 300px 300px;
}
FASE 8 — Aggiungere nuovi brand
Per ogni nuovo brand:

Bash

# 1. Crea cartella
mkdir -p brands/brand-nuovo/assets/fonts

# 2. Copia template config
cp brands/brand-personal/config.json brands/brand-nuovo/config.json

# 3. Modifica config con i tuoi colori/font

# 4. Aggiungi le regole di copy in copywriting-rules.md
CHECKLIST FINALE
text

□ FASE 0 — Crea struttura cartelle
□ FASE 1 — Scrivi tutti i file context/*.md
□ FASE 2 — Configura brands/*/config.json per ogni brand
□ FASE 3 — Crea i template HTML (base + tipi slide)
□ FASE 4 — Installa Node.js + dipendenze + scripts
□ FASE 5 — Testa: genera un JSON e renderizza
□ FASE 6 — (Opzionale) Setup Claude Code con CLAUDE.md
□ FASE 7 — Aggiungi grain overlay professionale
□ FASE 8 — Duplica per ogni brand
Risultato finale
text

Tu: "Crea carosello su [tema] per [brand]"

↓ 15 secondi ↓

📁 output/2025-01-15-come-trovare-clienti/
├── slide-01.png    ← Hook con grana, ombre, effetti
├── slide-02.png    ← Statement tipografico
├── slide-03.png    ← Quote con virgolette
├── slide-04.png    ← Lista con badge colorati
├── ...
├── slide-08.png    ← CTA finale
└── caption.txt     ← Caption pronta da copiare

## Collegamenti Correlati
- [[Knowledge_Base/Formazzione/manuale-completo-claude-code-business/parte-delle-volte-gli-hook-garantiscono-questa-affidabilità-per-le-parti-critiche-del-workflow/capitolo-38/(capitolo-38) overview|overview]]
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
