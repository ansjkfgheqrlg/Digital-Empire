#!/usr/bin/env python3
"""og_stampo.py — stampo dell'immagine di anteprima (Open Graph, 1200×630) per i siti della Fabbrica.

Perché uno stampo: l'anteprima che esce su WhatsApp/LinkedIn/Telegram quando si condivide il link è sempre la
stessa cosa (eyebrow, titolo con UN accento, sottotitolo, dominio, invito) — e ciò che si ripete diventa uno
stampo (CLAUDE-SITI §11, SINTESI-METODO §4). Canone: fondo ink, grana PNG (mai SVG), argento, accento su una
sola parola (§12), font del canone (Onest + Instrument Serif) caricati da Google al momento del render.

Uso:
  python og_stampo.py --titolo "Sistemi AI che girano|sul tuo server." --accento "Zero canoni." \
    --sotto "Outreach Factory · Content Factory · Second Brain." --sotto2 "Installati in 7 giorni. Codice tuo per sempre." \
    --eyebrow "Digital Empire|Agenzia · Sistemi AI proprietari" --dominio agency-empire-landing.vercel.app \
    --invito "Prenota la chiamata → /prenota/" --out agency-empire-landing/public/og.jpg

`|` nel titolo = a capo; `|` nell'eyebrow separa la parte chiara (brand) da quella attenuata.
I numeri nel testo devono stare in FATTI.md come per il copy (gate_fatti.py): l'immagine è copy.
Poi in layout.tsx: metadataBase + openGraph.images [{url:"/og.jpg",width:1200,height:630}] + twitter summary_large_image.
"""
import argparse, base64, html, io, os, random, sys

from PIL import Image
from playwright.sync_api import sync_playwright

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def grana_png_b64(lato: int = 400, seed: int = 7) -> str:
    rnd = random.Random(seed)
    g = Image.new("L", (lato, lato))
    g.putdata([rnd.randint(0, 255) for _ in range(lato * lato)])
    buf = io.BytesIO(); g.save(buf, "PNG")
    return base64.b64encode(buf.getvalue()).decode()


def pagina(a) -> str:
    grana = grana_png_b64()
    e = html.escape
    brand, _, resto = a.eyebrow.partition("|")
    titolo = "<br>".join(e(r) for r in a.titolo.split("|"))
    return f"""<!doctype html><html lang="it"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;700;800&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<style>
html,body{{margin:0;width:1200px;height:630px;overflow:hidden;background:#0a0a0a;font-family:Onest,system-ui,sans-serif;color:#d9d4e1}}
.bg{{position:absolute;inset:0;background:radial-gradient(120% 90% at 20% 0%,#202021 0%,#0a0a0a 60%,#050505 100%)}}
.grana{{position:absolute;inset:0;background-image:url(data:image/png;base64,{grana});background-size:200px 200px;opacity:.16;mix-blend-mode:overlay}}
.grana2{{position:absolute;inset:0;background-image:url(data:image/png;base64,{grana});background-size:333px 333px;opacity:.08}}
.vign{{position:absolute;inset:0;background:radial-gradient(85% 85% at 50% 45%,transparent 60%,rgba(0,0,0,.55) 100%)}}
.linea{{position:absolute;left:72px;right:72px;top:78px;height:1px;background:rgba(217,212,225,.16)}}
.eyebrow{{position:absolute;left:72px;top:96px;font:700 15px/1 'Onest';letter-spacing:.32em;text-transform:uppercase;color:#8f8a99}}
.eyebrow b{{color:#d9d4e1}}
h1{{position:absolute;left:72px;top:190px;margin:0;width:1000px;font:800 {a.corpo}px/1.02 'Onest';letter-spacing:-.025em;color:#f3ede0}}
h1 i{{font:italic 400 {int(a.corpo*1.1)}px/1 'Instrument Serif',Georgia,serif;color:{a.colore}}}
.sub{{position:absolute;left:72px;top:434px;width:900px;font:400 27px/1.35 'Onest';color:#8f8a99}}
.sub b{{color:#d9d4e1;font-weight:400}}
.piede{{position:absolute;left:72px;right:72px;bottom:56px;display:flex;justify-content:space-between;font:700 14px/1 'Onest';letter-spacing:.28em;text-transform:uppercase;color:#8f8a99}}
.piede span:last-child{{color:#d9d4e1}}
</style></head><body>
<div class="bg"></div><div class="grana"></div><div class="grana2"></div><div class="vign"></div><div class="linea"></div>
<div class="eyebrow"><b>{e(brand.strip())}</b>{(' &nbsp;·&nbsp; ' + e(resto.strip())) if resto.strip() else ''}</div>
<h1>{titolo} <i>{e(a.accento)}</i></h1>
<div class="sub">{e(a.sotto)}{('<br><b>' + e(a.sotto2) + '</b>') if a.sotto2 else ''}</div>
<div class="piede"><span>{e(a.dominio)}</span><span>{e(a.invito)}</span></div>
</body></html>"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--titolo", required=True, help="titolo; `|` = a capo")
    ap.add_argument("--accento", required=True, help="la parola/frase accesa (una sola, §12) — corsivo serif")
    ap.add_argument("--sotto", required=True)
    ap.add_argument("--sotto2", default="")
    ap.add_argument("--eyebrow", default="Digital Empire|", help="brand|resto attenuato")
    ap.add_argument("--dominio", required=True)
    ap.add_argument("--invito", default="")
    ap.add_argument("--colore", default="#fb4604", help="colore dell'accento (default arancione DE)")
    ap.add_argument("--corpo", type=int, default=84, help="corpo del titolo in px (84 regge 2 righe da ~22 caratteri)")
    ap.add_argument("--out", required=True, help="file .jpg di uscita (1200×630)")
    ap.add_argument("--qualita", type=int, default=86)
    a = ap.parse_args()

    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
        pg.set_content(pagina(a), wait_until="networkidle")
        pg.wait_for_timeout(1200)
        pg.evaluate("document.fonts.ready.then(()=>1)")
        pg.wait_for_timeout(400)
        png = pg.screenshot(type="png")
        b.close()
    im = Image.open(io.BytesIO(png)).convert("RGB")
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    im.save(a.out, "JPEG", quality=a.qualita, optimize=True, progressive=True)
    print(f"{a.out}  {im.size[0]}×{im.size[1]}  {os.path.getsize(a.out):,} B".replace(",", "."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
