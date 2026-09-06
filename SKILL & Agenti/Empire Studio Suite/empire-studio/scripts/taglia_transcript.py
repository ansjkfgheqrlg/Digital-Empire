# -*- coding: utf-8 -*-
"""Taglia da transcript.md la sola finestra temporale di un blocco di scene.

Nasce da una trappola vera (EMP-W4K7 §6): aprire il transcript intero da 117 KB
faceva morire le sentinelle al watchdog dei 600s. Qui il taglio si fa una volta
sola, fuori dalla sentinella, e ognuna riceve solo le righe che le servono.

Uso:  python scripts/taglia_transcript.py --run <run-id> --da 274 --a 294 [--margine 30]
Scrive: runs/<run-id>/_slice-<da>-<a>.md  e stampa il percorso.
"""
import argparse, json, os, re, sys

NL = chr(10)
RUNS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "runs")


def secondi(ts):
    """Accetta MM:SS o HH:MM:SS e restituisce secondi interi."""
    p = [int(x) for x in ts.strip().split(":")]
    if len(p) == 2:
        return p[0] * 60 + p[1]
    return p[0] * 3600 + p[1] * 60 + p[2]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--da", type=int, required=True)
    ap.add_argument("--a", type=int, required=True)
    ap.add_argument("--margine", type=int, default=30, help="secondi di respiro ai due estremi")
    a = ap.parse_args()

    base = os.path.join(RUNS, a.run)
    idx = {x["n"]: x for x in json.load(open(os.path.join(base, "_scene_index.json"), encoding="utf-8"))}
    if a.da not in idx or a.a not in idx:
        sys.exit("scene fuori indice: %d-%d" % (a.da, a.a))

    t0 = secondi(idx[a.da]["ts"]) - a.margine
    # la finestra arriva fino all'inizio della scena successiva all'ultima, se esiste
    fine = idx.get(a.a + 1, idx[a.a])["ts"]
    t1 = secondi(fine) + a.margine

    righe = []
    with open(os.path.join(base, "transcript.md"), encoding="utf-8") as f:
        for riga in f:
            m = re.match(r"^\[(\d+:\d+:\d+)\]", riga)
            if not m:
                continue
            s = secondi(m.group(1))
            if t0 <= s <= t1:
                righe.append(riga.rstrip())

    out = os.path.join(base, "_slice-%03d-%03d.md" % (a.da, a.a))
    testa = "# transcript scene %d-%d (%s -> %s, margine %ds)%s%s" % (
        a.da, a.a, idx[a.da]["ts"], fine, a.margine, NL, NL)
    with open(out, "w", encoding="utf-8") as f:
        f.write(testa + NL.join(righe) + NL)
    print("%s  righe:%d" % (out, len(righe)))


if __name__ == "__main__":
    main()
