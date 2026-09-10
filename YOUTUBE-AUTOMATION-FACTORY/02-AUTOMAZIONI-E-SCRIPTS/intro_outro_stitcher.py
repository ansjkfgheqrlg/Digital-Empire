#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regola che ordina questo script: A4-RC-14
(company/Memory/studi/aitubepro/regole/A4-metodo-ai-tube/RIPASSO_COSTRUTTIVO.py).

Buco che chiude, misurato sulla fabbrica: fliki_client.py:252 non ha nessun campo per una
clip di apertura o chiusura fissa, e nessuno script della fabbrica concatena asset fissi a un
video generato. Lo strumento tecnico si costruisce ORA; la decisione se USARLO (intro/outro
di canale) resta a Max, aperta in company/Memory/BACKLOG.md — ADR-028: l'attesa di una
decisione ferma solo se stessa, mai il lavoro intorno. Il giorno del si', il costo scende da
"scrivere uno script" ad "attivare un flag".

STATO: SPENTO. Nessun file esistente lo importa o lo chiama (apex7_orchestrator.py,
fliki_client.py, build_candidate_pool.py, youtube_uploader_playwright.py restano invariati).

COME FUNZIONA: concatena intro.mp4 + video principale + outro.mp4 con il concat demuxer di
ffmpeg. Se i tre file hanno lo stesso codec/risoluzione/sample-rate usa `-c copy` (nessuna
ricodifica, istantaneo); altrimenti ripiega automaticamente su una ricodifica con
filter_complex concat (piu' lento ma sempre corretto).

Uso da riga di comando:
  python intro_outro_stitcher.py --aiuto
  python intro_outro_stitcher.py --intro intro.mp4 --main video.mp4 --outro outro.mp4 --output finale.mp4

Uso come libreria:
  from intro_outro_stitcher import concatena
  risultato = concatena("intro.mp4", "video.mp4", "outro.mp4", "finale.mp4")
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)


def verifica_dipendenze() -> None:
    """Controlla che ffmpeg e ffprobe siano nel PATH. Si ferma con un messaggio chiaro se mancano."""
    mancanti = []
    if shutil.which("ffmpeg") is None:
        mancanti.append("ffmpeg")
    if shutil.which("ffprobe") is None:
        mancanti.append("ffprobe")
    if mancanti:
        raise SystemExit(
            "[STOP] Dipendenze mancanti per intro_outro_stitcher.py: " + ", ".join(mancanti) +
            ". Installa FFmpeg (include entrambi gli eseguibili) e rilancia: senza, nessuna "
            "concatenazione puo' essere prodotta."
        )


def _sonda(path: str) -> dict:
    """Legge codec/risoluzione video e codec/sample-rate audio di un file con ffprobe."""
    comando = [
        "ffprobe", "-v", "error", "-print_format", "json",
        "-show_entries", "stream=codec_type,codec_name,width,height,sample_rate,channels",
        path,
    ]
    risultato = subprocess.run(comando, capture_output=True, text=True)
    if risultato.returncode != 0:
        raise RuntimeError(f"ffprobe ha fallito su {path}: {risultato.stderr.strip()}")
    dati = json.loads(risultato.stdout)
    info = {"video": None, "audio": None}
    for stream in dati.get("streams", []):
        if stream.get("codec_type") == "video" and info["video"] is None:
            info["video"] = {
                "codec": stream.get("codec_name"),
                "width": stream.get("width"),
                "height": stream.get("height"),
            }
        elif stream.get("codec_type") == "audio" and info["audio"] is None:
            info["audio"] = {
                "codec": stream.get("codec_name"),
                "sample_rate": stream.get("sample_rate"),
                "channels": stream.get("channels"),
            }
    return info


def _combaciano(info_a: dict, info_b: dict) -> bool:
    """True se due file hanno codec/risoluzione video e codec/sample-rate audio compatibili per -c copy."""
    if (info_a["video"] is None) != (info_b["video"] is None):
        return False
    if info_a["video"] and info_b["video"]:
        va, vb = info_a["video"], info_b["video"]
        if (va["codec"], va["width"], va["height"]) != (vb["codec"], vb["width"], vb["height"]):
            return False
    if (info_a["audio"] is None) != (info_b["audio"] is None):
        return False
    if info_a["audio"] and info_b["audio"]:
        aa, ab = info_a["audio"], info_b["audio"]
        if (aa["codec"], aa["sample_rate"]) != (ab["codec"], ab["sample_rate"]):
            return False
    return True


def _durata_secondi(path: str) -> float | None:
    comando = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", path]
    risultato = subprocess.run(comando, capture_output=True, text=True)
    if risultato.returncode != 0:
        return None
    try:
        return float(json.loads(risultato.stdout)["format"]["duration"])
    except (KeyError, TypeError, ValueError):
        return None


def concatena(
    intro_path: str,
    main_path: str,
    outro_path: str,
    output_path: str,
    forza_ricodifica: bool = False,
    log=print,
) -> dict:
    """
    Concatena intro + video principale + outro in output_path. Usa il concat demuxer con
    `-c copy` quando i tre file combaciano per codec/risoluzione, altrimenti ricodifica.

    Ritorna {"output", "metodo" ("copy" o "ricodifica"), "durata_secondi"}.
    """
    verifica_dipendenze()
    for p in (intro_path, main_path, outro_path):
        if not os.path.isfile(p):
            raise FileNotFoundError(f"File non trovato: {p}")

    info_intro = _sonda(intro_path)
    info_main = _sonda(main_path)
    info_outro = _sonda(outro_path)
    tutti_combaciano = _combaciano(info_intro, info_main) and _combaciano(info_main, info_outro)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)) or ".", exist_ok=True)

    metodo = None
    if tutti_combaciano and not forza_ricodifica:
        lista_path = None
        try:
            with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
                for p in (intro_path, main_path, outro_path):
                    percorso_assoluto = os.path.abspath(p).replace("\\", "/")
                    f.write(f"file '{percorso_assoluto}'\n")
                lista_path = f.name
            comando = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lista_path, "-c", "copy", output_path]
            risultato = subprocess.run(comando, capture_output=True, text=True)
            if risultato.returncode == 0:
                metodo = "copy"
            else:
                log("[AVVISO] concat -c copy fallito nonostante codec compatibili, ripiego su ricodifica.")
                tutti_combaciano = False
        finally:
            if lista_path and os.path.exists(lista_path):
                os.unlink(lista_path)

    if metodo is None:
        filtro_parti = "".join(f"[{i}:v:0][{i}:a:0]" for i in range(3))
        comando = [
            "ffmpeg", "-y",
            "-i", intro_path, "-i", main_path, "-i", outro_path,
            "-filter_complex", f"{filtro_parti}concat=n=3:v=1:a=1[v][a]",
            "-map", "[v]", "-map", "[a]",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20",
            "-c:a", "aac", "-b:a", "128k",
            output_path,
        ]
        risultato = subprocess.run(comando, capture_output=True, text=True)
        if risultato.returncode != 0:
            raise RuntimeError(f"ffmpeg ha fallito (codice {risultato.returncode}):\n{risultato.stderr[-2000:]}")
        metodo = "ricodifica"

    durata = _durata_secondi(output_path)
    log(f"[OK] {output_path} — metodo={metodo}, durata={durata}")
    return {"output": output_path, "metodo": metodo, "durata_secondi": durata}


def main():
    parser = argparse.ArgumentParser(
        prog="intro_outro_stitcher.py",
        description=(
            "Concatena intro.mp4 + video + outro.mp4 di canale, senza ricodifica quando i "
            "codec combaciano (A4-RC-14). SPENTO: nessuna fase della fabbrica lo chiama, in "
            "attesa della decisione di Max in BACKLOG.md."
        ),
        add_help=False,
    )
    parser.add_argument("-h", "--help", "--aiuto", action="help", help="mostra questo messaggio ed esce")
    parser.add_argument("--intro", required=True)
    parser.add_argument("--main", required=True, dest="principale")
    parser.add_argument("--outro", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--canale", default=None, help="etichetta informativa, non incide sulla logica")
    parser.add_argument("--forza-ricodifica", action="store_true", dest="forza_ricodifica")
    args = parser.parse_args()

    try:
        risultato = concatena(
            args.intro, args.principale, args.outro, args.output,
            forza_ricodifica=args.forza_ricodifica,
        )
    except SystemExit:
        raise
    except Exception as e:
        print(f"[STOP] {e}")
        sys.exit(1)

    print(json.dumps(risultato, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
