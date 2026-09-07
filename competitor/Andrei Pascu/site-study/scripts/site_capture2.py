# -*- coding: utf-8 -*-
"""
site_capture2.py — cattura forense v2, per lo STUDIO TOTALE (dossier 33).

Cosa fa in piu' della v1 (`site_capture.py`), e perche' ognuna:

  1. FIX B-057   il testo di un <p> si ricompone dai figli: la v1 bucava i
                 paragrafi con <strong> dentro, e quel file e' la base di ogni
                 teardown di copy.
  2. src/        scarica CSS e JS SERVITI. E' lo strato 4: su armageddon i
                 commenti del CSS hanno rivelato il metodo di costruzione.
  3. costruzione riconosce Squarespace / Framer / Webflow / Wix / Next / WordPress
                 / artigianale. La profondita' dello studio si decide per MISURA,
                 non per giudizio.
  4. sezioni/    segmenta la pagina in sezioni reali e fa lo screenshot di
                 OGNUNA. E' cio' che serve per l'atlante visivo.
  5. firma       ogni sezione ha una firma strutturale, e le sezioni uguali
                 finiscono nello stesso gruppo: la visione ne guarda UNA per
                 gruppo, non tutte. E' cio' che rende il lavoro sostenibile.
  6. effetti     inventario di @keyframes, transizioni, filtri, blend, clip-path,
                 backdrop, trasformazioni.
  7. schema      albero delle sezioni con altezza, ruolo, media, CTA, densita'.
  8. scheda.json schema FISSO, uguale per ogni sito: e' cio' che rende possibile
                 la sintesi trasversale dai dati invece che dalle prose.

Uso:
  python site_capture2.py <url> [--slug nome] [--out DIR] [--max-slices N]
                          [--no-src] [--max-sezioni N]

Idempotente: se `scheda.json` esiste e non si passa --force, non rifa' nulla.
"""
import argparse
import json
import os
import re
import sys
import urllib.parse

from playwright.sync_api import sync_playwright

# --------------------------------------------------------------------------- #
# 1. ESTRAZIONE — token, blocchi di testo, CTA, media
# --------------------------------------------------------------------------- #
JS_TOKENS = r"""
() => {
  const rgbToHex = (c) => {
    if (!c) return null;
    if (c === 'transparent' || c === 'rgba(0, 0, 0, 0)') return 'transparent';
    const m = c.match(/rgba?\(([^)]+)\)/);
    if (!m) return c;
    const p = m[1].split(',').map(s => parseFloat(s.trim()));
    const hex = '#' + p.slice(0,3).map(v => Math.round(v).toString(16).padStart(2,'0')).join('');
    return (p.length > 3 && p[3] < 1) ? hex + ' @' + p[3] : hex;
  };
  const bump = (o,k) => { if(!k) return; o[k] = (o[k]||0)+1; };
  const sortDesc = (o) => Object.entries(o).sort((a,b)=>b[1]-a[1]).slice(0,40);

  const colorCount={}, bgCount={}, fontCount={}, sizeCount={}, weightCount={},
        radiusCount={}, shadowCount={}, transCount={}, animCount={}, filterCount={},
        blendCount={}, clipCount={}, transformCount={};

  for (const el of document.querySelectorAll('*')) {
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
    if (s.boxShadow && s.boxShadow !== 'none') bump(shadowCount, s.boxShadow.slice(0,120));

    /* --- gli EFFETTI, misurati dal DOM renderizzato --- */
    if (s.transition && s.transition !== 'all 0s ease 0s') bump(transCount, s.transition.slice(0,120));
    if (s.animationName && s.animationName !== 'none')
      bump(animCount, s.animationName + ' ' + s.animationDuration + ' ' + s.animationTimingFunction);
    if (s.filter && s.filter !== 'none') bump(filterCount, s.filter.slice(0,120));
    if (s.backdropFilter && s.backdropFilter !== 'none') bump(filterCount, 'backdrop: ' + s.backdropFilter.slice(0,100));
    if (s.mixBlendMode && s.mixBlendMode !== 'normal') bump(blendCount, s.mixBlendMode);
    if (s.clipPath && s.clipPath !== 'none') bump(clipCount, s.clipPath.slice(0,120));
    if (s.transform && s.transform !== 'none') bump(transformCount, s.transform.slice(0,80));
  }

  /* --- BLOCCHI DI TESTO — con il FIX B-057 -----------------------------
     La v1 prendeva solo i nodi di testo DIRETTI, quindi un <p> con dentro
     <strong> usciva bucato ("Quattro corsi completi — , , e —").
     Qui: se l'elemento non contiene altri elementi di blocco, si prende tutto
     il suo innerText. I figli inline (strong/em/a/span) restano dentro la
     frase, e vengono anche elencati a parte. */
  const BLOCKISH = 'h1,h2,h3,h4,h5,h6,p,li,div,section,ul,ol,table,blockquote,figure,header,footer,nav,article,details';
  const SEL = 'h1,h2,h3,h4,h5,h6,p,li,a,button,span,div,label,strong,em,blockquote,figcaption,td,th,summary';
  const blocks = [];
  for (const el of document.querySelectorAll(SEL)) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    const s = getComputedStyle(el);
    if (s.visibility === 'hidden' || s.display === 'none') continue;

    const haBlocchi = !!el.querySelector(BLOCKISH);
    let testo = '';
    if (!haBlocchi) {
      testo = (el.innerText || '').replace(/\s+/g, ' ').trim();
    } else {
      testo = Array.from(el.childNodes).filter(n => n.nodeType === 3)
                   .map(n => n.textContent).join(' ').replace(/\s+/g, ' ').trim();
    }
    if (!testo) continue;

    const inline = Array.from(el.querySelectorAll('strong,b,em,i,a,mark,u'))
                        .map(x => (x.innerText||'').replace(/\s+/g,' ').trim())
                        .filter(t => t && t.length < 200).slice(0, 12);

    blocks.push({
      tag: el.tagName.toLowerCase(),
      y: Math.round(r.top + window.scrollY),
      x: Math.round(r.left + window.scrollX),
      w: Math.round(r.width),
      text: testo.slice(0, 3000),
      inline: inline,
      color: rgbToHex(s.color),
      size: parseFloat(s.fontSize),
      weight: s.fontWeight,
      transform: s.textTransform,
      align: s.textAlign,
      href: el.tagName === 'A' ? el.getAttribute('href') : null
    });
  }

  /* --- CTA --- */
  const ctas = [];
  for (const el of document.querySelectorAll('a,button,[role="button"],input[type="submit"]')) {
    const r = el.getBoundingClientRect();
    if (r.width < 60 || r.height < 24) continue;
    const s = getComputedStyle(el);
    const t = (el.innerText || el.value || '').replace(/\s+/g,' ').trim();
    if (!t || t.length > 80) continue;
    ctas.push({ text: t, href: el.getAttribute('href') || null,
                y: Math.round(r.top + window.scrollY), x: Math.round(r.left),
                w: Math.round(r.width), h: Math.round(r.height),
                bg: rgbToHex(s.backgroundColor), color: rgbToHex(s.color),
                radius: s.borderRadius, border: s.border.slice(0,60),
                shadow: s.boxShadow === 'none' ? 'none' : s.boxShadow.slice(0,80),
                size: parseFloat(s.fontSize), weight: s.fontWeight,
                transform: s.textTransform, padding: s.padding });
  }

  /* --- media --- */
  const media = [];
  for (const el of document.querySelectorAll('img,video,svg,iframe,picture')) {
    const r = el.getBoundingClientRect();
    if (r.width < 24 || r.height < 24) continue;
    media.push({ tag: el.tagName.toLowerCase(),
                 src: el.getAttribute('src') || el.getAttribute('data-src') || '',
                 alt: el.getAttribute('alt') || '',
                 y: Math.round(r.top + window.scrollY), x: Math.round(r.left),
                 w: Math.round(r.width), h: Math.round(r.height) });
  }

  const bs = getComputedStyle(document.body);
  return {
    title: document.title,
    meta_description: (document.querySelector('meta[name="description"]')||{}).content || null,
    og_title: (document.querySelector('meta[property="og:title"]')||{}).content || null,
    og_image: (document.querySelector('meta[property="og:image"]')||{}).content || null,
    canonical: (document.querySelector('link[rel="canonical"]')||{}).href || null,
    jsonld: Array.from(document.querySelectorAll('script[type="application/ld+json"]'))
                 .map(s => (s.textContent||'').slice(0,400)),
    lang: document.documentElement.lang || null,
    page_height: document.body.scrollHeight,
    page_width: document.body.scrollWidth,
    body_bg: rgbToHex(bs.backgroundColor),
    body_font: bs.fontFamily,
    palette_text: sortDesc(colorCount),
    palette_bg: sortDesc(bgCount),
    fonts: sortDesc(fontCount),
    type_scale: sortDesc(sizeCount),
    weights: sortDesc(weightCount),
    radii: sortDesc(radiusCount),
    shadows: sortDesc(shadowCount),
    effetti: {
      transizioni: sortDesc(transCount),
      animazioni: sortDesc(animCount),
      filtri: sortDesc(filterCount),
      blend: sortDesc(blendCount),
      clip: sortDesc(clipCount),
      trasformazioni: sortDesc(transformCount)
    },
    headings: Array.from(document.querySelectorAll('h1,h2,h3'))
                   .map(h => ({ tag: h.tagName.toLowerCase(), y: Math.round(h.getBoundingClientRect().top + window.scrollY),
                                text: (h.innerText||'').replace(/\s+/g,' ').trim().slice(0,300) }))
                   .filter(h => h.text),
    ctas, media, blocks
  };
}
"""

# --------------------------------------------------------------------------- #
# 2. SEGMENTAZIONE IN SEZIONI
# --------------------------------------------------------------------------- #
JS_SEZIONI = r"""
(minH) => {
  const vw = window.innerWidth;
  const H = document.body.scrollHeight;
  /* Un CONTENITORE non e' una sezione. Su una pagina costruita a mano il nodo
     piu' alto (.page, main, un wrapper) copre tutto e, se lo si prende, blocca
     ogni altra scelta: e' esattamente cosi' che il primo giro su armageddon ha
     trovato "1 sezione". Quindi si squalifica chi copre piu' del 60% della
     pagina, e si scende. */
  const TETTO = Math.max(H * 0.6, 2000);
  const candidati = [];
  for (const el of document.querySelectorAll('body *')) {
    const r = el.getBoundingClientRect();
    if (r.height < minH) continue;
    if (r.height > TETTO) continue;
    if (r.width < vw * 0.55) continue;
    const s = getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden') continue;
    if (s.position === 'fixed') continue;          /* barre appiccicate, non sezioni */
    let prof = 0; let p = el;
    while (p && p !== document.body) { prof++; p = p.parentElement; }
    candidati.push({ el, top: Math.round(r.top + window.scrollY),
                     h: Math.round(r.height), prof });
  }
  /* i piu' alti nell'albero vincono: si vuole la partizione, non le scatole dentro */
  candidati.sort((a,b) => a.top - b.top || a.prof - b.prof);

  const scelte = [];
  for (const c of candidati) {
    const sovrappone = scelte.some(s => !(c.top >= s.top + s.h - 8 || c.top + c.h <= s.top + 8));
    if (!sovrappone) scelte.push(c);
  }
  scelte.sort((a,b) => a.top - b.top);

  const rgbToHex = (c) => {
    if (!c || c === 'transparent' || c === 'rgba(0, 0, 0, 0)') return 'transparent';
    const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return c;
    const p = m[1].split(',').map(s => parseFloat(s.trim()));
    return '#' + p.slice(0,3).map(v => Math.round(v).toString(16).padStart(2,'0')).join('');
  };

  return scelte.map((c, i) => {
    const el = c.el;
    const s = getComputedStyle(el);
    const testi = el.querySelectorAll('h1,h2,h3,h4,p,li,span,a,button');
    const heads = Array.from(el.querySelectorAll('h1,h2,h3,h4'))
                       .map(h => (h.innerText||'').replace(/\s+/g,' ').trim()).filter(Boolean);
    const mediaN = el.querySelectorAll('img,video,svg,iframe,picture').length;
    const ctaN = Array.from(el.querySelectorAll('a,button')).filter(b => {
      const r = b.getBoundingClientRect(); return r.width >= 60 && r.height >= 24; }).length;
    const parole = (el.innerText || '').split(/\s+/).filter(Boolean).length;

    /* firma strutturale: due sezioni con la stessa firma sono lo stesso pattern
       ripetuto, e ne basta guardare una. */
    const cls = (el.className && typeof el.className === 'string')
                ? el.className.split(/\s+/).filter(Boolean).slice(0,3).join('.') : '';
    const bucketH = Math.round(c.h / 200);
    const bucketFigli = Math.min(9, el.children.length);
    const firma = [el.tagName.toLowerCase(), cls, bucketFigli, mediaN > 0 ? 'M' : '-',
                   ctaN > 0 ? 'C' : '-', bucketH].join('|');

    return {
      i: i + 1,
      y: c.top, h: c.h, prof: c.prof,
      tag: el.tagName.toLowerCase(),
      id: el.id || null,
      classi: cls,
      bg: rgbToHex(s.backgroundColor),
      bg_img: s.backgroundImage !== 'none',
      heading: heads[0] || null,
      headings: heads.slice(0, 6),
      blocchi_testo: testi.length,
      parole: parole,
      densita: c.h ? Math.round(parole / (c.h / 100)) : 0,
      media: mediaN,
      cta: ctaN,
      firma: firma
    };
  });
}
"""

FIRME_COSTRUZIONE = [
    ("squarespace", ["squarespace-cdn", "static1.squarespace.com", "sqspcdn", "Squarespace"]),
    ("framer", ["framerusercontent.com", "framer.com/m/", "data-framer"]),
    ("webflow", ["webflow.com", "wf-", "data-wf-page"]),
    ("wix", ["wixstatic.com", "parastorage.com"]),
    ("shopify", ["cdn.shopify.com", "shopify"]),
    ("wordpress", ["wp-content", "wp-includes"]),
    ("next", ["/_next/static", "__NEXT_DATA__"]),
    ("react", ["react-dom", "data-reactroot"]),
]


def riconosci_costruzione(html, risorse):
    testo = html + " " + " ".join(risorse)
    trovate = [nome for nome, chiavi in FIRME_COSTRUZIONE if any(k in testo for k in chiavi)]
    return trovate[0] if trovate else "artigianale"


def slugify(u):
    s = re.sub(r"^https?://(www\.)?", "", u).rstrip("/")
    return re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower() or "home"


def nome_file(u, i):
    p = urllib.parse.urlparse(u).path.rsplit("/", 1)[-1] or ("risorsa-%02d" % i)
    p = re.sub(r"[^a-zA-Z0-9._-]+", "-", p)[:80]
    return "%02d-%s" % (i, p)


def capture(url, outdir, slug, max_slices, scarica_src=True, max_sezioni=60, force=False):
    d = os.path.join(outdir, slug)
    os.makedirs(d, exist_ok=True)
    scheda_path = os.path.join(d, "scheda.json")
    if os.path.isfile(scheda_path) and not force:
        print("[SALTO] %s: scheda.json esiste gia' (usa --force per rifare)" % slug)
        return d

    dir_sez = os.path.join(d, "sezioni")
    dir_src = os.path.join(d, "src")
    os.makedirs(dir_sez, exist_ok=True)
    if scarica_src:
        os.makedirs(dir_src, exist_ok=True)

    risorse = []          # URL di css/js visti passare
    corpi = {}            # url -> testo

    with sync_playwright() as p:
        br = p.chromium.launch()
        dati = {}
        sezioni = []
        html_sorgente = ""

        for etichetta, vw, vh in [("desktop", 1440, 900), ("mobile", 390, 844)]:
            ctx = br.new_context(viewport={"width": vw, "height": vh},
                                 device_scale_factor=1,
                                 user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                                             "Chrome/124.0 Safari/537.36"))
            pg = ctx.new_page()

            if etichetta == "desktop" and scarica_src:
                def su_risposta(resp):
                    try:
                        tipo = (resp.headers or {}).get("content-type", "")
                        u = resp.url
                        if ("css" in tipo or "javascript" in tipo
                                or u.endswith(".css") or u.endswith(".js")):
                            if len(corpi) < 40:
                                risorse.append(u)
                                corpi[u] = resp.text()
                    except Exception:
                        pass
                pg.on("response", su_risposta)

            try:
                pg.goto(url, wait_until="networkidle", timeout=45000)
            except Exception:
                pg.goto(url, wait_until="domcontentloaded", timeout=45000)
            pg.wait_for_timeout(2500)

            for etichetta_cookie in ["Accetta", "Accept", "Solo essenziali", "Accetta tutti", "Ho capito"]:
                try:
                    btn = pg.get_by_text(etichetta_cookie, exact=True).first
                    if btn.is_visible(timeout=1000):
                        btn.click(timeout=2000)
                        pg.wait_for_timeout(700)
                        break
                except Exception:
                    pass

            pg.evaluate("async () => { const H=document.body.scrollHeight; "
                        "for (let y=0; y<H; y+=600){ window.scrollTo(0,y); "
                        "await new Promise(r=>setTimeout(r,110)); } window.scrollTo(0,0); }")
            pg.wait_for_timeout(1200)

            altezza = pg.evaluate("document.body.scrollHeight")
            n = min(max_slices, max(1, -(-altezza // vh)))
            for i in range(n):
                pg.evaluate("window.scrollTo(0, %d)" % (i * vh))
                pg.wait_for_timeout(350)
                pg.screenshot(path=os.path.join(d, "%s-%02d.png" % (etichetta, i + 1)))

            if etichetta == "desktop":
                pg.evaluate("window.scrollTo(0,0)")
                pg.wait_for_timeout(300)
                dati = pg.evaluate(JS_TOKENS)
                dati["slices_desktop"] = n
                html_sorgente = pg.content()

                # ---- SEZIONI + screenshot per sezione ------------------------
                sezioni = pg.evaluate(JS_SEZIONI, 180)
                if len(sezioni) < 3:
                    # ripiego dichiarato (dossier 33, tabella dei modi di rottura):
                    # soglia piu' bassa prima di arrendersi alle fette cieche
                    sezioni = pg.evaluate(JS_SEZIONI, 90)
                sezioni = sezioni[:max_sezioni]
                visti = {}
                for s in sezioni:
                    g = visti.setdefault(s["firma"], s["i"])
                    s["gruppo"] = g
                    s["rappresentante"] = (g == s["i"])
                largh = pg.evaluate("document.body.scrollWidth")
                for s in sezioni:
                    nome = "%02d-%s.png" % (s["i"], re.sub(r"[^a-z0-9]+", "-",
                                                           (s["heading"] or s["tag"]).lower())[:34].strip("-") or "sezione")
                    try:
                        pg.screenshot(path=os.path.join(dir_sez, nome), full_page=True,
                                      clip={"x": 0, "y": s["y"], "width": min(largh, 1440),
                                            "height": min(s["h"], 4000)})
                        s["screenshot"] = "sezioni/" + nome
                    except Exception as e:
                        s["screenshot"] = None
                        s["errore_screenshot"] = type(e).__name__
            else:
                dati["slices_mobile"] = n
                dati["mobile_page_height"] = altezza

            ctx.close()
        br.close()

    # ---- src/ ---------------------------------------------------------------
    salvati = []
    if scarica_src:
        for i, u in enumerate(sorted(corpi), 1):
            testo = corpi[u] or ""
            if len(testo) < 40:
                continue
            fn = nome_file(u, i)
            if not fn.endswith((".css", ".js")):
                fn += ".css" if "css" in u else ".js"
            with open(os.path.join(dir_src, fn), "w", encoding="utf-8", newline="") as f:
                f.write("/* fonte: %s */\n" % u + testo)
            salvati.append({"file": "src/" + fn, "url": u, "bytes": len(testo)})
        with open(os.path.join(dir_src, "_INDICE.json"), "w", encoding="utf-8", newline="") as f:
            json.dump(salvati, f, ensure_ascii=False, indent=1)

    costruzione = riconosci_costruzione(html_sorgente, risorse)

    # ---- keyframes dai CSS scaricati ---------------------------------------
    keyframes = []
    for r in salvati:
        if not r["file"].endswith(".css"):
            continue
        try:
            with open(os.path.join(d, r["file"]), encoding="utf-8") as f:
                keyframes += re.findall(r"@(?:-webkit-)?keyframes\s+([A-Za-z0-9_-]+)", f.read())
        except Exception:
            pass
    keyframes = sorted(set(keyframes))

    # ---- file di uscita -----------------------------------------------------
    leggeri = {k: v for k, v in dati.items() if k != "blocks"}
    with open(os.path.join(d, "design-tokens.json"), "w", encoding="utf-8", newline="") as f:
        json.dump(leggeri, f, ensure_ascii=False, indent=1)
    with open(os.path.join(d, "dom-blocks.json"), "w", encoding="utf-8", newline="") as f:
        json.dump(dati.get("blocks", []), f, ensure_ascii=False, indent=1)

    gruppi = len({s["firma"] for s in sezioni})
    scheda = {
        "url": url, "slug": slug, "catturata": __import__("datetime").date.today().isoformat(),
        "dominio": urllib.parse.urlparse(url).netloc,
        "titolo": dati.get("title"), "lang": dati.get("lang"),
        "costruzione": costruzione,
        "altezza": dati.get("page_height"), "larghezza": dati.get("page_width"),
        "altezza_mobile": dati.get("mobile_page_height"),
        "body_bg": dati.get("body_bg"), "body_font": dati.get("body_font"),
        "palette_testo": dati.get("palette_text"), "palette_sfondi": dati.get("palette_bg"),
        "caratteri": dati.get("fonts"), "scala_tipografica": dati.get("type_scale"),
        "pesi": dati.get("weights"), "raggi": dati.get("radii"), "ombre": dati.get("shadows"),
        "effetti": dati.get("effetti", {}),
        "keyframes": keyframes,
        "headings": dati.get("headings"),
        "cta": dati.get("ctas"), "media": dati.get("media"),
        "blocchi_testo": len(dati.get("blocks", [])),
        "meta": {"description": dati.get("meta_description"), "og_title": dati.get("og_title"),
                 "og_image": dati.get("og_image"), "canonical": dati.get("canonical"),
                 "jsonld": dati.get("jsonld", [])},
        "sezioni": sezioni,
        "sezioni_totali": len(sezioni),
        "sezioni_distinte": gruppi,
        "src": salvati,
        "segmentazione": "ok" if len(sezioni) >= 2 else "fallita",
    }
    with open(scheda_path, "w", encoding="utf-8", newline="") as f:
        json.dump(scheda, f, ensure_ascii=False, indent=1)

    # ---- copy integrale (col fix B-057) ------------------------------------
    righe = ["# Copy integrale — %s" % (dati.get("title") or ""),
             "**URL:** %s  ·  **Catturato:** %s  ·  **Costruzione:** %s" % (url, scheda["catturata"], costruzione),
             "**Altezza:** %spx  ·  **Blocchi:** %d  ·  **Sezioni:** %d (%d distinte)"
             % (dati.get("page_height"), len(dati.get("blocks", [])), len(sezioni), gruppi),
             "", "> Ogni riga: `[y] <tag> (colore / corpo / peso)` poi il testo esatto.",
             "> Il testo dei paragrafi e' RICOMPOSTO coi figli in linea (fix B-057): niente buchi.",
             "", "---", ""]
    visti = set()
    for b in dati.get("blocks", []):
        chiave = (b["text"], b["y"])
        if chiave in visti:
            continue
        visti.add(chiave)
        riga = "**[y=%s] `%s`** — %s / %spx / w%s" % (b["y"], b["tag"], b["color"], b["size"], b["weight"])
        if b.get("transform") not in (None, "none"):
            riga += " / %s" % b["transform"]
        if b.get("href"):
            riga += " → `%s`" % b["href"]
        righe += [riga, "", b["text"], ""]
        if b.get("inline"):
            righe += ["  *in grassetto/link dentro:* " + " · ".join(b["inline"]), ""]
    with open(os.path.join(d, "copy-integrale.md"), "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(righe))

    print("[OK] %s | costruzione: %s | %spx | %d sezioni (%d distinte) | %d blocchi | %d CTA | %d media | %d file src | %d keyframes"
          % (slug, costruzione, dati.get("page_height"), len(sezioni), gruppi,
             len(dati.get("blocks", [])), len(dati.get("ctas", [])), len(dati.get("media", [])),
             len(salvati), len(keyframes)))
    return d


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--slug", default=None)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "capture"))
    ap.add_argument("--max-slices", type=int, default=32)
    ap.add_argument("--max-sezioni", type=int, default=60)
    ap.add_argument("--no-src", action="store_true")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    try:
        capture(a.url, a.out, a.slug or slugify(a.url), a.max_slices,
                scarica_src=not a.no_src, max_sezioni=a.max_sezioni, force=a.force)
    except Exception as e:
        print("[ERRORE]", type(e).__name__, str(e)[:300])
        sys.exit(1)
