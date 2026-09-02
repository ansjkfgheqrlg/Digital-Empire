#!/usr/bin/env python3
"""
scene_detector.py — Empire Studio

Riduce una sequenza di frame densi (estratti con --interval 2) ai soli frame
in cui lo schermo CAMBIA davvero.

Perche' esiste
--------------
Un video di 13 minuti a 1 frame ogni 2 secondi produce ~400 immagini. In un
video con screen recording lo schermo resta identico per decine di secondi:
15-20 frame consecutivi sono la stessa schermata. Guardarli tutti costa 10 volte
tanto e non aggiunge una sola informazione.

Questo script confronta ogni frame con l'ultimo frame TENUTO (non col precedente,
per non perdere le derive lente) e tiene solo quelli sopra una soglia di
differenza percettiva.

Metodo (deterministico, nessuna dipendenza esterna oltre Pillow)
---------------------------------------------------------------
1. Ogni frame -> miniatura in scala di grigi 64x64 (via Pillow).
2. Differenza = media dei valori assoluti pixel-per-pixel, normalizzata 0..100.
3. Se differenza >= soglia -> il frame e' una schermata NUOVA: si tiene.
4. Il primo e l'ultimo frame si tengono SEMPRE (apertura e chiusura del video).

Onesta' della copertura (regola NO-FINTO)
-----------------------------------------
Lo script NON cancella nulla: tutti i frame densi restano su disco. Produce un
manifest che dichiara quanti frame esistono, quanti sono unici, la soglia usata
e, per ogni frame tenuto, quanti duplicati rappresenta e per quanti secondi
quella schermata resta a video. Chi legge l'analisi puo' sempre risalire.

Uso
---
    python scripts/scene_detector.py --run max17-v01-artem
    python scripts/scene_detector.py --run max17-v01-artem --threshold 3.5
    python scripts/scene_detector.py --run max17-v01-artem --interval 2

Output
------
    runs/<run>/scenes.json      manifest completo (macchina)
    runs/<run>/scenes.md        elenco leggibile dei frame da guardare (umano)
"""

import argparse
import json
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("[scene] ERRORE: manca Pillow. Installa con: pip install --user Pillow")

THUMB = (64, 64)


def firma(path: Path):
    """Miniatura 64x64 in scala di grigi, come lista di 4096 interi 0-255."""
    with Image.open(path) as im:
        return list(im.convert("L").resize(THUMB, Image.BILINEAR).getdata())


def differenza(a, b) -> float:
    """Differenza media assoluta tra due firme, normalizzata 0..100."""
    if not a or not b:
        return 100.0
    tot = sum(abs(x - y) for x, y in zip(a, b))
    return (tot / len(a)) / 255.0 * 100.0


def mmss(secondi: float) -> str:
    s = int(secondi)
    return f"{s // 60}:{s % 60:02d}"


def main():
    ap = argparse.ArgumentParser(
        description="Tiene solo i frame in cui lo schermo cambia davvero"
    )
    ap.add_argument("--run", required=True, help="run-id sotto runs/")
    ap.add_argument(
        "--threshold",
        type=float,
        default=3.0,
        help="soglia di differenza 0-100 (default 3.0; alza per tenerne meno)",
    )
    ap.add_argument(
        "--interval",
        type=float,
        default=2.0,
        help="secondi tra un frame denso e il successivo (default 2.0)",
    )
    args = ap.parse_args()

    base = Path(__file__).resolve().parent.parent
    run_dir = base / "runs" / args.run
    frames_dir = run_dir / "frames"
    if not frames_dir.is_dir():
        sys.exit(f"[scene] ERRORE: non trovo {frames_dir}")

    frames = sorted(frames_dir.glob("frame-*.png"))
    if not frames:
        sys.exit(f"[scene] ERRORE: nessun frame in {frames_dir}")

    print(f"[scene] run={args.run} · {len(frames)} frame densi · soglia={args.threshold}")

    tenuti = []
    rif = None  # firma dell'ultimo frame TENUTO
    for i, f in enumerate(frames):
        try:
            sig = firma(f)
        except Exception as e:
            # NO-FINTO: un frame illeggibile si dichiara, non si finge
            tenuti.append(
                {
                    "frame": f.name,
                    "indice": i,
                    "secondi": round(i * args.interval, 1),
                    "timestamp": mmss(i * args.interval),
                    "delta": None,
                    "errore": f"illeggibile: {e}",
                }
            )
            continue

        d = 100.0 if rif is None else differenza(rif, sig)
        ultimo = i == len(frames) - 1
        if rif is None or d >= args.threshold or ultimo:
            tenuti.append(
                {
                    "frame": f.name,
                    "indice": i,
                    "secondi": round(i * args.interval, 1),
                    "timestamp": mmss(i * args.interval),
                    "delta": round(d, 2),
                }
            )
            rif = sig

    # quanti duplicati rappresenta ogni frame tenuto, e per quanti secondi resta
    for n, t in enumerate(tenuti):
        fine = tenuti[n + 1]["indice"] if n + 1 < len(tenuti) else len(frames)
        t["rappresenta_frame"] = fine - t["indice"]
        t["durata_schermata_s"] = round((fine - t["indice"]) * args.interval, 1)

    riduzione = 100.0 * (1 - len(tenuti) / len(frames))
    manifest = {
        "run": args.run,
        "frame_densi_totali": len(frames),
        "frame_unici_da_guardare": len(tenuti),
        "riduzione_percentuale": round(riduzione, 1),
        "soglia": args.threshold,
        "intervallo_s": args.interval,
        "metodo": "grayscale 64x64, differenza media assoluta vs ultimo frame tenuto",
        "nota_copertura": (
            "Nessun frame cancellato: tutti restano in frames/. I frame non elencati "
            "sono sotto soglia rispetto al precedente tenuto, cioe' schermate gia' viste."
        ),
        "frames": tenuti,
    }

    (run_dir / "scenes.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    righe = [
        f"# Frame da guardare — {args.run}",
        "",
        f"- Frame densi estratti (1 ogni {args.interval}s): **{len(frames)}**",
        f"- Frame unici da guardare: **{len(tenuti)}**",
        f"- Riduzione: **{riduzione:.1f}%** · soglia {args.threshold}",
        "",
        "> Nessun frame e' stato cancellato: tutti restano in `frames/`.",
        "> I frame non elencati qui sono identici (sotto soglia) a un frame gia' elencato.",
        "",
        "| # | frame | ts | delta | schermata dura |",
        "|---|---|---|---|---|",
    ]
    for n, t in enumerate(tenuti, 1):
        d = "ERR" if t.get("delta") is None else f"{t['delta']:.1f}"
        righe.append(
            f"| {n} | `{t['frame']}` | {t['timestamp']} | {d} | {t['durata_schermata_s']}s |"
        )
    (run_dir / "scenes.md").write_text("\n".join(righe) + "\n", encoding="utf-8")

    print(f"[scene] OK: {len(tenuti)}/{len(frames)} frame unici (-{riduzione:.1f}%)")
    print(f"[scene] -> {run_dir / 'scenes.json'}")
    print(f"[scene] -> {run_dir / 'scenes.md'}")


if __name__ == "__main__":
    main()
