const puppeteer = require('puppeteer');
const fs = require('fs-extra');
const path = require('path');

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

// Applica gradiente per ogni singola parola (display:inline-block su ogni word)
function applyWordGradients(text, gradient, shadowCSS) {
  if (!text) return '';
  const shadow = shadowCSS ? `text-shadow: ${shadowCSS};` : '';
  return text
    .split('\n')
    .map(line =>
      line.split(' ')
        .filter(w => w.length > 0)
        .map(word =>
          `<span style="display: inline-block; background: ${gradient}; -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; ${shadow}">${word}</span>`
        )
        .join(' ')
    )
    .join('<br>');
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
    '{{FONT_PATH}}': path.join(__dirname, '..', 'brands', config.brand_name, 'assets', 'fonts').replace(/\\/g, '/'),
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
  let grandeHTML = '';
  if (slide.testo_grande) {
    if (useGradient) {
      // Splitta il testo intorno alla parola accent
      if (slide.testo_accent) {
        const regex = new RegExp(`(${slide.testo_accent.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'i');
        const parts = slide.testo_grande.split(regex);
        const before = parts[0] || '';
        const accentWord = parts[1] || '';
        const after = parts[2] || '';

        // Accent: usa il colore rosso sangue puro (non gradiente, per staccarsi)
        const accentSpan = accentWord
          ? `<span style="display: inline-block; -webkit-text-fill-color: ${accentColor}; color: ${accentColor}; text-shadow: ${config.effects.glow_accent};">${accentWord}</span>`
          : '';

        grandeHTML = applyWordGradients(before, gradient, shadowCSS)
          + accentSpan
          + applyWordGradients(after, gradient, shadowCSS);
      } else {
        grandeHTML = applyWordGradients(slide.testo_grande, gradient, shadowCSS);
      }
    } else {
      // Senza gradiente: testo normale con accent span
      let before = slide.testo_grande;
      let after = '';
      if (slide.testo_accent) {
        const regex = new RegExp(`(${slide.testo_accent.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'i');
        const parts = slide.testo_grande.split(regex);
        before = parts[0] || '';
        const accentWord = parts[1] || '';
        after = parts[2] || '';
        const accentSpan = `<span style="color: ${accentColor}; text-shadow: ${config.effects.glow_accent};">${accentWord}</span>`;
        grandeHTML = (before + accentSpan + after).replace(/\\n/g, '<br>');
      } else {
        grandeHTML = before.replace(/\\n/g, '<br>');
      }
    }
  }

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
