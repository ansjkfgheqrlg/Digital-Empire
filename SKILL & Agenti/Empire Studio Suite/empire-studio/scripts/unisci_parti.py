# -*- coding: utf-8 -*-
"""Unisce i _parte-*.md di un run in video-analysis.md, in ordine di scena.

Idempotente. Conta la copertura vera e denuncia buchi e doppioni: i numeri
si contano, non si dichiarano.

Uso:  python scripts/unisci_parti.py --run <run-id> --scene <totale>
"""
import argparse, glob, io, os, re, sys

NL = chr(10)
RUNS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "runs")


def blocchi(testo):
    testa, out, corrente, buf = [], {}, None, []
    for riga in testo.split(NL):
        m = re.match(r"^### Scena\s+(\d+)\s*[·.]", riga)
        if m:
            if corrente is not None:
                out[corrente] = NL.join(buf).rstrip()
            corrente, buf = int(m.group(1)), [riga]
        elif corrente is None:
            testa.append(riga)
        else:
            buf.append(riga)
    if corrente is not None:
        out[corrente] = NL.join(buf).rstrip()
    return NL.join(testa).rstrip(), out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--scene", type=int, required=True)
    a = ap.parse_args()
    d = os.path.join(RUNS, a.run)
    base = os.path.join(d, "video-analysis.md")

    testa, scene, origine = "", {}, {}
    if os.path.exists(base):
        testa, scene = blocchi(io.open(base, encoding="utf-8").read())
        origine = {n: "video-analysis.md" for n in scene}
    for f in sorted(glob.glob(os.path.join(d, "_parte-*.md"))):
        t2, s2 = blocchi(io.open(f, encoding="utf-8").read())
        if not testa and t2.strip():
            testa = t2
        for n, txt in s2.items():
            if n in scene and origine.get(n) != os.path.basename(f):
                print("DOPPIONE scena %d: %s e %s -> tengo il piu' lungo"
                      % (n, origine[n], os.path.basename(f)))
                if len(txt) <= len(scene[n]):
                    continue
            scene[n] = txt
            origine[n] = os.path.basename(f)

    numeri = sorted(scene)
    pezzi = [testa, ""]
    for n in numeri:
        pezzi.append(scene[n]); pezzi.append("")
    io.open(base, "w", encoding="utf-8", newline=NL).write(NL.join(pezzi).rstrip() + NL)

    manca = [n for n in range(1, a.scene + 1) if n not in scene]
    print("scene unite     :", len(numeri))
    print("copertura reale : %d/%d = %d%%" % (len(numeri), a.scene, len(numeri) * 100 // a.scene))
    print("MANCANTI (%d): %s" % (len(manca), manca[:30]) if manca else "NESSUNA SCENA MANCANTE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
