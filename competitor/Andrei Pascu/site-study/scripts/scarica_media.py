# -*- coding: utf-8 -*-
"""scarica_media.py — scarica in originale ogni immagine di una cattura (scheda.json → media[]) e ne misura
formato, dimensioni in pixel, peso e rapporto. Serve allo studio della QUALITA' GRAFICA: un'immagine si
giudica sull'originale, non sullo screenshot. Scrive <cattura>/media/ e <cattura>/media-inventario.md.

Uso: python scarica_media.py capture/66-funneloperator-it
"""
import io, json, os, sys, urllib.parse, urllib.request
from PIL import Image

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
cart = sys.argv[1]
s = json.load(open(os.path.join(cart, "scheda.json"), encoding="utf-8"))
base = s["url"]
out = os.path.join(cart, "media"); os.makedirs(out, exist_ok=True)
righe, visti = [], set()
for m in s["media"]:
    src = m.get("src") or ""
    if not src or src.startswith("data:") or src in visti:
        continue
    visti.add(src)
    url = urllib.parse.urljoin(base, src)
    nome = urllib.parse.unquote(os.path.basename(urllib.parse.urlparse(url).path)) or "senza-nome"
    dest = os.path.join(out, nome)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=30).read()
        open(dest, "wb").write(data)
        try:
            im = Image.open(io.BytesIO(data)); w, h = im.size; fmt = im.format
        except Exception:
            w = h = 0; fmt = os.path.splitext(nome)[1].upper().strip(".") or "?"
        righe.append((nome, fmt, w, h, len(data), m.get("w"), m.get("h"), m.get("alt", ""), src))
    except Exception as e:
        righe.append((nome, "ERR", 0, 0, 0, m.get("w"), m.get("h"), str(e)[:60], src))

righe.sort(key=lambda r: -r[4])
tot = sum(r[4] for r in righe)
L = [f"# Inventario media — {s['slug']} ({len(righe)} file unici, {tot/1024:.0f} KB)\n",
     "| file | formato | px originali | reso in pagina (w×h) | peso | alt | src |", "|---|---|---|---|---|---|---|"]
for n, f, w, h, peso, rw, rh, alt, src in righe:
    L.append(f"| `{n}` | {f} | {w}×{h} | {rw}×{rh} | {peso/1024:.0f} KB | {alt[:60]} | `{src[:70]}` |")
open(os.path.join(cart, "media-inventario.md"), "w", encoding="utf-8").write("\n".join(L))
print(f"[OK] {len(righe)} media, {tot/1024:.0f} KB -> {cart}/media-inventario.md")
