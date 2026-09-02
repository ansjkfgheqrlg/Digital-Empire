# -*- coding: utf-8 -*-
"""
site_capture.py — cattura forense di una pagina web per lo studio competitor.

Produce, per ogni URL:
  capture/<slug>/desktop-NN.png      screenshot a fette verticali (1440x900)
  capture/<slug>/mobile-NN.png       screenshot a fette verticali (390x844)
  capture/<slug>/design-tokens.json  palette con conteggi, font, dimensioni, CTA, immagini
  capture/<slug>/copy-integrale.md   ogni testo della pagina in ordine DOM, con stile e posizione
  capture/<slug>/dom-blocks.json     blocchi testuali con bbox + stile computato

Uso:
  python site_capture.py <url> [--slug nome] [--out DIR] [--max-slices N]
"""
import argparse, json, os, re, sys
from playwright.sync_api import sync_playwright

JS_EXTRACT = r"""
() => {
  const px = v => { const n = parseFloat(v); return isNaN(n) ? null : Math.round(n); };
  const rgbToHex = (c) => {
    if (!c) return null;
    if (c === 'transparent' || c === 'rgba(0, 0, 0, 0)') return 'transparent';
    const m = c.match(/rgba?\(([^)]+)\)/);
    if (!m) return c;
    const p = m[1].split(',').map(s => parseFloat(s.trim()));
    const hex = '#' + p.slice(0,3).map(v => Math.round(v).toString(16).padStart(2,'0')).join('');
    return (p.length > 3 && p[3] < 1) ? hex + ' @' + p[3] : hex;
  };

  const colorCount = {}, bgCount = {}, fontCount = {}, sizeCount = {}, weightCount = {}, radiusCount = {};
  const bump = (o,k) => { if(!k) return; o[k] = (o[k]||0)+1; };

  const all = Array.from(document.querySelectorAll('*'));
  for (const el of all) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    const s = getComputedStyle(el);
    if (s.visibility === 'hidden' || s.display === 'none' || s.opacity === '0') continue;
    const hasText = Array.from(el.childNodes).some(n => n.nodeType === 3 && n.textContent.trim());
    if (hasText) {
      bump(colorCount, rgbToHex(s.color));
      bump(fontCount, s.fontFamily);
      bump(sizeCount, s.fontSize + ' / lh ' + s.lineHeight + ' / w' + s.fontWeight);
      bump(weightCount, s.fontWeight);
    }
    const bg = rgbToHex(s.backgroundColor);
    if (bg && bg !== 'transparent') bump(bgCount, bg + (s.backgroundImage !== 'none' ? ' (+img)' : ''));
    if (s.borderRadius && s.borderRadius !== '0px') bump(radiusCount, s.borderRadius);
  }

  // blocchi testuali in ordine DOM
  const blocks = [];
  const SEL = 'h1,h2,h3,h4,h5,h6,p,li,a,button,span,div,label,strong,em,blockquote,figcaption,td,th';
  const BLOCKISH = 'h1,h2,h3,h4,h5,h6,p,li,div,section,ul,ol,table,blockquote,figure,header,footer,nav,article';
  for (const el of document.querySelectorAll(SEL)) {
    // testo proprio (solo nodi di testo diretti)
    const own = Array.from(el.childNodes).filter(n => n.nodeType === 3)
                     .map(n => n.textContent).join(' ').replace(/\s+/g,' ').trim();
    // frase completa: se l'elemento non contiene altri blocchi, prendi tutto innerText
    // (recupera le parole dentro <strong>/<em>/<a> inline che altrimenti si perdono)
    const isLeafBlock = !el.querySelector(BLOCKISH);
    const full = isLeafBlock ? (el.innerText || '').replace(/\s+/g,' ').trim() : own;
    if (!own || own.length < 2) continue;
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    const s = getComputedStyle(el);
    if (s.visibility === 'hidden' || s.display === 'none') continue;
    blocks.push({
      tag: el.tagName.toLowerCase(),
      cls: (el.className && typeof el.className === 'string') ? el.className.slice(0,120) : '',
      text: own.slice(0, 1200),
      full: (full && full !== own) ? full.slice(0, 2000) : null,
      y: Math.round(r.top + window.scrollY),
      x: Math.round(r.left),
      w: Math.round(r.width),
      h: Math.round(r.height),
      color: rgbToHex(s.color),
      bg: rgbToHex(s.backgroundColor),
      font: s.fontFamily,
      size: s.fontSize,
      weight: s.fontWeight,
      lh: s.lineHeight,
      ls: s.letterSpacing,
      transform: s.textTransform,
      align: s.textAlign,
      href: el.tagName === 'A' ? el.getAttribute('href') : null
    });
  }
  blocks.sort((a,b) => a.y - b.y || a.x - b.x);

  // CTA: link e bottoni con aspetto da pulsante
  const ctas = [];
  for (const el of document.querySelectorAll('a,button,input[type=submit]')) {
    const r = el.getBoundingClientRect();
    if (r.width < 40 || r.height < 20) continue;
    const s = getComputedStyle(el);
    const bg = rgbToHex(s.backgroundColor);
    const bordered = s.borderWidth && s.borderWidth !== '0px';
    if (bg === 'transparent' && !bordered) continue;
    ctas.push({
      text: (el.innerText || el.value || '').replace(/\s+/g,' ').trim().slice(0,120),
      href: el.getAttribute('href'),
      y: Math.round(r.top + window.scrollY), x: Math.round(r.left),
      w: Math.round(r.width), h: Math.round(r.height),
      bg, color: rgbToHex(s.color), radius: s.borderRadius,
      border: s.border, shadow: s.boxShadow, font: s.fontFamily,
      size: s.fontSize, weight: s.fontWeight, transform: s.textTransform,
      padding: s.padding
    });
  }
  ctas.sort((a,b) => a.y - b.y);

  const images = Array.from(document.querySelectorAll('img,svg,video')).map(el => {
    const r = el.getBoundingClientRect();
    return { tag: el.tagName.toLowerCase(),
             src: (el.getAttribute('src')||'').slice(0,200),
             alt: el.getAttribute('alt') || '',
             y: Math.round(r.top + window.scrollY), x: Math.round(r.left),
             w: Math.round(r.width), h: Math.round(r.height) };
  }).filter(i => i.w > 8 && i.h > 8).sort((a,b)=>a.y-b.y);

  const sortDesc = o => Object.entries(o).sort((a,b)=>b[1]-a[1]);
  const bodyStyle = getComputedStyle(document.body);

  return {
    url: location.href,
    title: document.title,
    meta_description: (document.querySelector('meta[name=description]')||{}).content || null,
    og_title: (document.querySelector('meta[property="og:title"]')||{}).content || null,
    lang: document.documentElement.lang || null,
    page_height: document.body.scrollHeight,
    page_width: document.body.scrollWidth,
    body_bg: rgbToHex(bodyStyle.backgroundColor),
    body_font: bodyStyle.fontFamily,
    palette_text: sortDesc(colorCount),
    palette_bg: sortDesc(bgCount),
    fonts: sortDesc(fontCount),
    type_scale: sortDesc(sizeCount),
    weights: sortDesc(weightCount),
    radii: sortDesc(radiusCount),
    headings: Array.from(document.querySelectorAll('h1,h2,h3'))
                   .map(h => ({ tag: h.tagName.toLowerCase(),
                                text: (h.innerText||'').replace(/\s+/g,' ').trim().slice(0,300) }))
                   .filter(h => h.text),
    ctas, images, blocks
  };
}
"""


def slugify(u):
    s = re.sub(r"^https?://(www\.)?", "", u).rstrip("/")
    return re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower() or "home"


def capture(url, outdir, slug, max_slices):
    d = os.path.join(outdir, slug)
    os.makedirs(d, exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch()
        data = {}
        for label, vw, vh in [("desktop", 1440, 900), ("mobile", 390, 844)]:
            ctx = br.new_context(viewport={"width": vw, "height": vh},
                                 device_scale_factor=1,
                                 user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                                             "Chrome/124.0 Safari/537.36"))
            pg = ctx.new_page()
            try:
                pg.goto(url, wait_until="networkidle", timeout=45000)
            except Exception:
                pg.goto(url, wait_until="domcontentloaded", timeout=45000)
            pg.wait_for_timeout(2500)
            # chiudi il banner cookie: occlude stabilmente l'angolo in basso su ogni fetta
            for cookie_label in ["Accetta", "Accept", "Solo essenziali", "Accetta tutti"]:
                try:
                    btn = pg.get_by_text(cookie_label, exact=True).first
                    if btn.is_visible(timeout=1200):
                        btn.click(timeout=2000)
                        pg.wait_for_timeout(800)
                        break
                except Exception:
                    pass
            # forza il lazy-load scorrendo tutta la pagina
            pg.evaluate("async () => { const H=document.body.scrollHeight; "
                        "for (let y=0; y<H; y+=600){ window.scrollTo(0,y); "
                        "await new Promise(r=>setTimeout(r,120)); } window.scrollTo(0,0); }")
            pg.wait_for_timeout(1200)
            height = pg.evaluate("document.body.scrollHeight")
            n = min(max_slices, max(1, -(-height // vh)))
            for i in range(n):
                pg.evaluate(f"window.scrollTo(0, {i * vh})")
                pg.wait_for_timeout(400)
                pg.screenshot(path=os.path.join(d, f"{label}-{i+1:02d}.png"))
            if label == "desktop":
                pg.evaluate("window.scrollTo(0,0)")
                pg.wait_for_timeout(300)
                data = pg.evaluate(JS_EXTRACT)
                data["slices_desktop"] = n
            else:
                data["slices_mobile"] = n
                data["mobile_page_height"] = height
            ctx.close()
        br.close()

    with open(os.path.join(d, "design-tokens.json"), "w", encoding="utf-8") as f:
        light = {k: v for k, v in data.items() if k != "blocks"}
        json.dump(light, f, ensure_ascii=False, indent=1)
    with open(os.path.join(d, "dom-blocks.json"), "w", encoding="utf-8") as f:
        json.dump(data.get("blocks", []), f, ensure_ascii=False, indent=1)

    # copy integrale in ordine di lettura
    lines = [f"# Copy integrale — {data.get('title','')}", f"**URL:** {url}",
             f"**Altezza pagina:** {data.get('page_height')}px  ·  **Blocchi testuali:** {len(data.get('blocks',[]))}",
             "", "> Ogni riga: `[y=posizione verticale px] <tag> (colore / dimensione / peso)` poi il testo esatto.",
             "> Estratto dal DOM renderizzato, nessuna parola riscritta.", "", "---", ""]
    seen = set()
    for b in data.get("blocks", []):
        key = (b.get("full") or b["text"], b["y"])
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"**[y={b['y']}] `{b['tag']}`** — {b['color']} / {b['size']} / w{b['weight']}"
                     + (f" / {b['transform']}" if b.get("transform") not in (None, "none") else "")
                     + (f" → `{b['href']}`" if b.get("href") else ""))
        lines.append("")
        lines.append(b.get("full") or b["text"])
        lines.append("")
    with open(os.path.join(d, "copy-integrale.md"), "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(lines))

    print(f"[OK] {slug}: {data.get('slices_desktop')} slice desktop, {data.get('slices_mobile')} mobile, "
          f"{len(data.get('blocks',[]))} blocchi, {len(data.get('ctas',[]))} CTA, "
          f"{len(data.get('images',[]))} media, altezza {data.get('page_height')}px")
    return d


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--slug", default=None)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "capture"))
    ap.add_argument("--max-slices", type=int, default=32)
    a = ap.parse_args()
    try:
        capture(a.url, a.out, a.slug or slugify(a.url), a.max_slices)
    except Exception as e:
        print("[ERRORE]", type(e).__name__, str(e)[:300])
        sys.exit(1)
