#!/usr/bin/env python3
"""aura_prep.py — prepara le immagini del sito dal manifest (Dossier 37, F2).

Regola C2.2: le immagini con `sorgente: originale` NON entrano mai in `public/`. Vanno in
`cantiere/aura-preview/` (gitignored) e le vede solo il dev server locale, tramite la rewrite
`/aura-preview/*` di next.config (attiva solo in `next dev`). In `public/aura/` entrano soltanto
`sorgente in {generata, team, screenshot}`.

Per ogni immagine in pagina (posto != null):
  - ridimensiona a 1600 px sul lato lungo, WebP q80 (<= 250 KB, altrimenti scende di qualita')
  - il trattamento B (desaturazione, contrasto, vignetta) lo fa il CSS, non il file: il file resta
    neutro cosi' lo swap generata/originale non cambia la resa
  - scrive accanto un `.json` con alt e didascalia, letti dal componente <Aura/>

Composizione B (Dossier 37 v2, C3.1): il componente <Aura/> NON controlla il 404 a runtime, legge
`src/lib/aura-presenti.json` scritto qui. Un posto senza file sparisce dal layout (colonna chiusa),
gia' nell'HTML statico: niente cornice vuota, niente salto al mount.
  - default        : presenti = solo i file che stanno davvero in public/aura/ (quello che va online)
  - --pieno        : presenti += i file di preview (misura "manifest pieno" in locale, con
                     NEXT_PUBLIC_AURA_BASE=http://localhost:8787/ e `npx serve cantiere/aura-preview -l 8787`)

Uso:
  python scripts/aura_prep.py                      # tutte le immagini in pagina + presenti.json (produzione)
  python scripts/aura_prep.py --pieno              # idem, presenti.json include la preview
  python scripts/aura_prep.py --check              # solo il gate: originali in public/ = FAIL
"""
import json, sys, pathlib, argparse, io
from PIL import Image

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "public" / "aura" / "manifest.json"
SRC = pathlib.Path(r"C:\Users\Utente\Desktop\qui tutto\Digital Empire\Caroselli Style\immagini AURA")
PREVIEW = ROOT / "cantiere" / "aura-preview"
PUBLIC = ROOT / "public" / "aura"
PRESENTI = ROOT / "src" / "lib" / "aura-presenti.json"
MAX_KB = 250
LATO = 1600


def salva_webp(im: Image.Image, dest: pathlib.Path):
    im = im.convert("RGB")
    im.thumbnail((LATO, LATO), Image.LANCZOS)
    q = 82
    while True:
        buf = io.BytesIO()
        im.save(buf, "WEBP", quality=q, method=6)
        if buf.tell() <= MAX_KB * 1024 or q <= 50:
            break
        q -= 6
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(buf.getvalue())
    return buf.tell() // 1024, q, im.size


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--pieno", action="store_true", help="presenti.json include la preview locale")
    a = ap.parse_args()
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    in_pagina = [r for r in m["immagini"] if r.get("posto") and r.get("file_pubblico")]

    # GATE — nessun file originale in public/
    errori = []
    for r in in_pagina:
        if r["sorgente"] == "originale" and (PUBLIC / pathlib.Path(r["file_pubblico"]).name).exists():
            errori.append(f"ORIGINALE IN PUBLIC: {r['file_pubblico']} (id {r['id']})")
    if a.check:
        if errori:
            print("GATE IMMAGINI -- FAIL");  [print("  [X]", e) for e in errori]; sys.exit(1)
        print(f"GATE IMMAGINI -- PASS ({len(in_pagina)} in pagina, 0 originali in public/)"); sys.exit(0)

    for r in in_pagina:
        nome = pathlib.Path(r["file_pubblico"]).name
        if r["sorgente"] == "originale":
            src = SRC / r["file_originale"]
            if not src.exists():
                print(f"  [!] manca {src}"); continue
            kb, q, size = salva_webp(Image.open(src), PREVIEW / nome)
            dove = "preview"
        else:
            # generata/team/screenshot: il file lo mette Max o Higgsfield in public/aura/ con quel nome;
            # qui si controlla solo che esista e si normalizza se c'e'
            p = PUBLIC / nome
            if not p.exists():
                print(f"  [ ] {nome:32} {r['sorgente']:10} -- manca ancora (non blocca: il componente mostra il segnaposto)")
                continue
            kb, q, size = salva_webp(Image.open(p), p) if p.suffix == ".webp" else (p.stat().st_size // 1024, "-", Image.open(p).size)
            dove = "public"
        meta = {"id": r["id"], "alt": r["alt"], "didascalia": r.get("didascalia"), "sezione": r["sezione"],
                "posto": r["posto"], "sorgente": r["sorgente"], "trattamento": r.get("trattamento")}
        (PREVIEW if dove == "preview" else PUBLIC).joinpath(nome).with_suffix(".json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  [{dove:7}] {nome:32} {size[0]}x{size[1]}  {kb} KB  q{q}")

    # composizione B: la lista dei file che esistono davvero, letta dal componente a build time
    presenti = sorted(p.name for p in PUBLIC.glob("*.webp"))
    if a.pieno and PREVIEW.exists():
        presenti = sorted(set(presenti) | {p.name for p in PREVIEW.glob("*.webp")})
    PRESENTI.parent.mkdir(parents=True, exist_ok=True)
    PRESENTI.write_text(json.dumps({"pieno": bool(a.pieno), "file": presenti}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"  presenti.json: {len(presenti)} file ({'pieno: con preview' if a.pieno else 'produzione: solo public/'})")

    if errori:
        print("GATE IMMAGINI -- FAIL"); [print("  [X]", e) for e in errori]; sys.exit(1)
    print("GATE IMMAGINI -- PASS (0 originali in public/)")


if __name__ == "__main__":
    main()
