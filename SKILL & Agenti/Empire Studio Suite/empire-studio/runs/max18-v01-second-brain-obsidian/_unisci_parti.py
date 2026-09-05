# -*- coding: utf-8 -*-
"""Unisce i pezzi delle sentinelle dentro video-analysis.md.

Idempotente: si puo' rilanciare. Le scene si contano, non si dichiarano.
"""
import io, os, re, sys, glob

NL = chr(10)
BASE = "video-analysis.md"


def blocchi(testo):
    """Spezza un testo in blocchi di scena: {numero: testo}."""
    fuori = []
    out = {}
    corrente = None
    buf = []
    for riga in testo.split(NL):
        m = re.match(r"^### Scena\s+(\d+)\s*·", riga)
        if m:
            if corrente is not None:
                out[corrente] = NL.join(buf).rstrip()
            corrente = int(m.group(1))
            buf = [riga]
        elif corrente is None:
            fuori.append(riga)
        else:
            buf.append(riga)
    if corrente is not None:
        out[corrente] = NL.join(buf).rstrip()
    return NL.join(fuori).rstrip(), out


def main():
    if not os.path.exists(BASE):
        print("ERRORE: manca", BASE); return 2
    testata, scene = blocchi(io.open(BASE, encoding="utf-8").read())
    origine = {n: BASE for n in scene}
    for f in sorted(glob.glob("_parte-*.md")):
        _, s2 = blocchi(io.open(f, encoding="utf-8").read())
        for n, t in s2.items():
            if n in scene and origine[n] != f:
                print("DOPPIONE scena %d: %s e %s -> tengo il piu' lungo" % (n, origine[n], f))
                if len(t) <= len(scene[n]):
                    continue
            scene[n] = t
            origine[n] = f

    numeri = sorted(scene)
    attese = set(range(1, 353))
    mancanti = sorted(attese - set(numeri))
    pezzi = [testata, ""]
    for n in numeri:
        pezzi.append(scene[n]); pezzi.append("")
    io.open(BASE, "w", encoding="utf-8", newline=NL).write(NL.join(pezzi).rstrip() + NL)

    print("scene unite     :", len(numeri))
    print("copertura reale : %d/352 = %d%%" % (len(numeri), len(numeri) * 100 // 352))
    if mancanti:
        print("MANCANTI (%d):" % len(mancanti), mancanti[:25], "..." if len(mancanti) > 25 else "")
    else:
        print("NESSUNA SCENA MANCANTE - copertura totale")
    return 0


if __name__ == "__main__":
    sys.exit(main())
