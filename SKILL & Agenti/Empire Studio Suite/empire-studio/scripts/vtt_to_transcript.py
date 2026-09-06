# -*- coding: utf-8 -*-
"""Da .vtt a transcript.md, nel formato [hh:mm:ss] testo.

Nasce da un difetto misurato: senza `transcript.md` ogni sentinella riparsava
il VTT per conto proprio, e i sottotitoli a scorrimento di YouTube ripetono
la stessa riga decine di volte. Si fa una volta sola, qui.

Uso:  python scripts/vtt_to_transcript.py --run <run-id> [--tutti]
"""
import argparse
import io
import os
import re
import sys

NL = chr(10)
RUNS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "runs")
TEMPO = re.compile(r"^(\d\d):(\d\d):(\d\d)[.,]\d+\s*-->")


def pulisci(riga):
    riga = re.sub(r"<[^>]+>", "", riga)          # tag di karaoke <00:00:01.234>
    riga = riga.replace("&nbsp;", " ").strip()
    return riga


def converti(vtt_path):
    righe_out, viste, ultimo_ts = [], set(), None
    for riga in io.open(vtt_path, encoding="utf-8", errors="replace"):
        riga = riga.rstrip(NL).rstrip(chr(13))
        m = TEMPO.match(riga)
        if m:
            ultimo_ts = "%s:%s:%s" % m.groups()
            continue
        if not riga or riga.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        t = pulisci(riga)
        if not t or ultimo_ts is None:
            continue
        # i sottotitoli a scorrimento ripetono la stessa frase a ogni cue
        if t in viste:
            continue
        viste.add(t)
        righe_out.append("[%s] %s" % (ultimo_ts, t))
    return righe_out


def per_run(run):
    d = os.path.join(RUNS, run)
    dest = os.path.join(d, "transcript.md")
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return run, "gia' presente", 0
    vtt = sorted(f for f in os.listdir(d) if f.endswith(".vtt"))
    if not vtt:
        return run, "NESSUN VTT", 0
    # preferisci l'italiano se ce n'e' piu' d'uno
    scelto = next((f for f in vtt if ".it." in f), vtt[0])
    righe = converti(os.path.join(d, scelto))
    io.open(dest, "w", encoding="utf-8", newline=NL).write(NL + NL.join(righe) + NL)
    return run, "da " + scelto, len(righe)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run")
    ap.add_argument("--tutti", action="store_true")
    a = ap.parse_args()
    bersagli = sorted(os.listdir(RUNS)) if a.tutti else [a.run]
    for r in bersagli:
        if not os.path.isdir(os.path.join(RUNS, r)):
            continue
        try:
            nome, esito, n = per_run(r)
            print("%-32s %-24s %s righe" % (nome[:32], esito, n))
        except Exception as e:
            print("%-32s ERRORE: %s" % (r[:32], e))
    return 0


if __name__ == "__main__":
    sys.exit(main())
