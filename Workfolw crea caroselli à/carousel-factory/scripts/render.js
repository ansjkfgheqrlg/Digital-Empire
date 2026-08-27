const puppeteer = require('puppeteer');
const fs = require('fs-extra');
const path = require('path');
const { pathToFileURL } = require('url');

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
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
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
      let imgUrl = slide.sfondo_img;
      if (!imgUrl.startsWith('http') && !imgUrl.startsWith('file://')) {
        const absPath = path.resolve(slide.sfondo_img).replace(/\\/g, '/');
        imgUrl = `file:///${absPath}`;
      }
      finalHTML = finalHTML.replace('{{BG_IMAGE_BLOCK}}', `
        <div class="bg-image" style="background-image: url('${imgUrl}');"></div>
        <div class="bg-overlay"></div>
      `);
    } else {
      finalHTML = finalHTML.replace('{{BG_IMAGE_BLOCK}}', '');
    }

    // Renderizza con Puppeteer
    const page = await browser.newPage();
    await page.setViewport({ width: 1080, height: 1080 });
    await page.setContent(finalHTML, { waitUntil: 'networkidle0' });

    // BUG REALE (2026-08-25): `networkidle0` NON aspetta i webfont. Lo
    // screenshot partiva prima che @font-face avesse applicato Anton, quindi
    // ogni slide usciva col sans di ripiego. Anche qui: zero errori nel log,
    // difetto visibile solo aprendo il PNG.
    //
    // document.fonts.ready si risolve quando il font e' davvero applicabile.
    // Verifichiamo anche che sia stato caricato per davvero e lo diciamo, invece
    // di lasciare che un font mancante passi in silenzio: `Inter-Regular.ttf` in
    // questo repo NON e' un font (e' una pagina HTML salvata con estensione
    // .ttf, verificato dai magic bytes) ed era stato notato da nessuno.
    await page.evaluate(() => document.fonts.ready);
    const fontiCaricate = await page.evaluate(() =>
      [...document.fonts].map(f => `${f.family}:${f.status}`)
    );
    // Solo `error` e' un difetto: `unloaded` significa che quella famiglia non
    // e' usata da nessun elemento di QUESTA slide, e il browser non la carica
    // apposta. Segnalarlo sarebbe un falso allarme a ogni singola slide.
    const inErrore = fontiCaricate.filter(f => f.endsWith(':error'));
    if (inErrore.length) {
      console.warn(`   [!] font in errore: ${inErrore.join(', ')} — la slide uscira' con un font di ripiego`);
    }

    // Screenshot
    const fileName = `slide-${String(slide.numero).padStart(2, '0')}.png`;
    await page.screenshot({
      path: path.join(outputDir, fileName),
      type: 'png',
      clip: { x: 0, y: 0, width: 1080, height: 1080 }
    });

    // Salva HTML per debug
    await fs.writeFile(
      path.join(outputDir, `slide-${String(slide.numero).padStart(2, '0')}.html`),
      finalHTML
    );

    await page.close();
  }

  // 7. Salva caption
  await fs.writeFile(path.join(outputDir, 'caption.txt'), carouselData.caption);

  await browser.close();
  console.log(`\n✅ Carosello generato in: ${outputDir}`);
  console.log(`📊 ${carouselData.slides.length} slide create`);
}

// Applica gradiente per ogni singola parola (display:inline-block su ogni word).
//
// BUG REALE (2026-08-25): prima la parola accent veniva gestita FUORI di qui,
// spezzando `testo_grande` con una regex e riconcatenando
// `before + accentSpan + after`. Ma questa funzione fa
// `split(' ').filter(w => w.length > 0).join(' ')`, che butta via gli spazi di
// bordo: con testo_grande "funziona il render" e accent "funziona" usciva
// **"funzionail render"**, parole incollate. Visibile solo guardando il PNG,
// nessun errore nel log.
//
// Adesso l'accent e' una decisione presa DENTRO il ciclo delle parole: lo
// spazio fra le parole lo mette sempre e solo il `join(' ')` finale, quindi la
// classe di bug non puo' ripresentarsi.
function applyWordGradients(text, gradient, shadowCSS, opts = {}) {
  if (!text) return '';
  const { accent = '', accentColor = '', glow = '' } = opts;
  const shadow = shadowCSS ? `text-shadow: ${shadowCSS};` : '';
  const accentWords = accent
    ? accent.toLowerCase().split(/\s+/).filter(Boolean)
    : [];
  const spoglia = (w) => w.toLowerCase().replace(/[.,;:!?"'()«»]/g, '');

  return text
    .replace(/\\n/g, '\n')   // "\n" letterale nel JSON = a capo voluto
    .split('\n')
    .map(line =>
      line.split(' ')
        .filter(w => w.length > 0)
        .map(word => {
          if (accentWords.length && accentWords.includes(spoglia(word))) {
            return `<span style="display: inline-block; -webkit-text-fill-color: ${accentColor}; color: ${accentColor}; text-shadow: ${glow};">${word}</span>`;
          }
          if (!gradient) {
            return `<span style="display: inline-block; ${shadow}">${word}</span>`;
          }
          return `<span style="display: inline-block; background: ${gradient}; -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; ${shadow}">${word}</span>`;
        })
        .join(' ')
    )
    .join('<br>');
}

// Legge un font dal brand e lo restituisce come `src:` CSS gia' pronto,
// incorporato in base64.
//
// Perche' incorporato e non un url() su disco: la pagina nasce da
// page.setContent(), quindi ha origine about:blank e Chrome rifiuta le
// sottorisorse file:// richieste da li'. Con l'url su disco il font non si
// caricava MAI e nessuno se ne accorgeva, perche' il fallback e' silenzioso.
//
// Controlla anche che il file sia davvero un font guardando i magic bytes:
// `Inter-Regular.ttf` in questo repo e' una pagina HTML salvata con estensione
// .ttf (verificato), e incorporarla come base64 produrrebbe lo stesso identico
// fallback silenzioso che stiamo togliendo di mezzo. Meglio dirlo e ripiegare
// su un font di sistema dichiarato.
function fontSrc(brandName, fontFile, ruolo) {
  const ripiego = "local('Arial'), local('Helvetica'), sans-serif";
  if (!fontFile) return ripiego;

  const file = path.join(__dirname, '..', 'brands', brandName, 'assets', 'fonts', `${fontFile}.ttf`);
  if (!fs.existsSync(file)) {
    console.warn(`   [!] font ${ruolo}: ${fontFile}.ttf non esiste — uso un font di sistema`);
    return ripiego;
  }

  const buf = fs.readFileSync(file);
  // TrueType: 00 01 00 00 oppure "true"/"ttcf". OpenType/CFF: "OTTO". WOFF: "wOFF"/"wOF2".
  const firma = buf.subarray(0, 4);
  const firmeValide = [
    Buffer.from([0x00, 0x01, 0x00, 0x00]),
    Buffer.from('true'), Buffer.from('ttcf'), Buffer.from('OTTO'),
    Buffer.from('wOFF'), Buffer.from('wOF2'),
  ];
  if (!firmeValide.some(f => firma.equals(f))) {
    console.warn(`   [!] font ${ruolo}: ${fontFile}.ttf NON e' un font (primi byte: ${firma.toString('hex')}) — uso un font di sistema`);
    return ripiego;
  }

  return `url(data:font/ttf;base64,${buf.toString('base64')}) format('truetype')`;
}

function replaceBrandVars(html, config) {
  // .text-hero non ha più colore proprio: sarà gestito parola per parola inline
  const heroFontCSS = `font-family: 'Hero', sans-serif;`;

  // --- Image overlay ---
  const bgOverlayGradient = config.effects.image_overlay ||
    'linear-gradient(180deg, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.85) 100%)';

  // --- Image filter ---
  const imageFilter = config.effects.image_filter || 'none';

  // --- Logo block ---
  let logoBlock = '';
  if (config.logo && config.logo.show) {
    const logoPath = path.join(__dirname, '..', 'brands', config.brand_name, 'assets', 'logo.png');
    logoBlock = `<div class="logo-watermark"><img src="file://${logoPath.replace(/\\/g, '/')}" /></div>`;
  }

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
    '{{GRAIN_OPACITY}}': String(config.effects.grain_opacity),
    '{{VIGNETTE_INTENSITY}}': String(config.effects.vignette_intensity),
    '{{PADDING}}': config.layout.padding,
    '{{FONT_HERO_SRC}}': fontSrc(config.brand_name, config.typography.font_hero, 'Hero'),
    '{{FONT_BOLD_SRC}}': fontSrc(config.brand_name, config.typography.font_bold, 'Bold'),
    '{{FONT_REGULAR_SRC}}': fontSrc(config.brand_name, config.typography.font_regular, 'Regular'),
    '{{FONT_HERO_FILE}}': config.typography.font_hero,
    '{{FONT_BOLD_FILE}}': config.typography.font_bold,
    '{{FONT_REGULAR_FILE}}': config.typography.font_regular,
    '{{HERO_FONT_CSS}}': heroFontCSS,
    '{{BG_OVERLAY_GRADIENT}}': bgOverlayGradient,
    '{{IMAGE_FILTER}}': imageFilter,
    '{{LOGO_OPACITY}}': String(config.logo ? config.logo.opacity : 0),
    '{{LOGO_SIZE}}': config.logo ? config.logo.size : '0px',
    '{{LOGO_BLOCK}}': logoBlock,
  };

  for (const [key, value] of Object.entries(replacements)) {
    html = html.replaceAll(key, value);
  }
  return html;
}

function populateSlide(template, slide, config) {
  const accentColor = slide.colore_override || config.colors.accent_1;
  const useGradient = config.gradient && config.gradient.use_gradient_text;
  const gradient = useGradient ? config.gradient.hero_text : null;
  const shadowCSS = config.effects.text_shadow;

  // --- Costruisce TESTO_GRANDE_HTML con gradiente per-parola ---
  // Un solo percorso, con o senza gradiente e con o senza accent: la parola
  // accent e' un caso dentro il ciclo delle parole, non una concatenazione
  // fatta fuori (vedi il commento su applyWordGradients per il bug che
  // quella concatenazione produceva).
  const grandeHTML = slide.testo_grande
    ? applyWordGradients(slide.testo_grande, gradient, shadowCSS, {
        accent: slide.testo_accent || '',
        accentColor,
        glow: config.effects.glow_accent,
      })
    : '';

  // --- Sostituzioni base ---
  template = template
    .replaceAll('{{TESTO_PICCOLO}}', slide.testo_piccolo || '')
    .replaceAll('{{TESTO_GRANDE_HTML}}', grandeHTML)
    .replaceAll('{{TESTO_GRANDE}}', slide.testo_grande || '')
    .replaceAll('{{ACCENT_1}}', accentColor)
    .replaceAll('{{ACCENT_2}}', config.colors.accent_2 || '#C0C0C0')
    .replaceAll('{{SIZE_MEDIUM}}', config.typography.size_medium)
    .replaceAll('{{SIZE_LARGE}}', config.typography.size_large)
    .replaceAll('{{TEXT_PRIMARY}}', config.colors.text_primary)
    .replaceAll('{{TEXT_SECONDARY}}', config.colors.text_secondary)
    .replaceAll('{{INSTAGRAM_HANDLE}}', config.instagram || '')
    .replaceAll('{{TEXT_MUTED}}', config.colors.text_muted);

  // --- Nodi diagramma ---
  const nodi = slide.nodi || [];
  template = template
    .replaceAll('{{NODO_1}}', nodi[0] || '')
    .replaceAll('{{NODO_2}}', nodi[1] || '')
    .replaceAll('{{NODO_3}}', nodi[2] || '');
  if (nodi[3]) {
    const nodo4Block = `
      <div style="padding: 6px 0 6px 48px; color: ${accentColor}; font-size: 36px; opacity: 0.7;">↓</div>
      <div style="padding: 22px 32px; background: rgba(139,0,0,0.20); border: 2px solid ${config.colors.accent_2}; border-radius: 12px; font-family: 'Bold', sans-serif; font-size: ${config.typography.size_medium}; color: ${config.colors.accent_2};">${nodi[3]}</div>`;
    template = template.replaceAll('{{NODO_4_BLOCK}}', nodo4Block);
  } else {
    template = template.replaceAll('{{NODO_4_BLOCK}}', '');
  }

  // --- Items lista ---
  const items = slide.items || [];
  const defColors = [accentColor, config.colors.accent_2 || '#C0C0C0', '#EEEEEE'];
  const itemsHTML = items.map((item, i) => {
    const color = item.colore || defColors[i % defColors.length];
    const icon = item.icona || '▸';
    const text = typeof item === 'string' ? item : (item.testo || '');
    return `<div style="display: flex; align-items: center; gap: 16px; padding: 18px 32px; border: 2px solid ${color}; border-radius: 50px; width: fit-content; background: rgba(0,0,0,0.25);">
      <span style="font-size: 22px; color: ${color};">${icon}</span>
      <span style="font-family: 'Bold', sans-serif; font-size: 30px; color: ${color}; letter-spacing: -0.5px;">${text}</span>
    </div>`;
  }).join('\n');
  template = template.replaceAll('{{ITEMS_HTML}}', itemsHTML);

  // Newline rimasti
  template = template.replace(/\\n/g, '<br>');

  return template;
}

module.exports = { renderCarousel };
