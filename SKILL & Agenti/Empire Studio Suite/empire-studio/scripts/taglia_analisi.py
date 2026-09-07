# -*- coding: utf-8 -*-
"""taglia_analisi.py — taglia da video-analysis.md il solo blocco di scene di un atomizzatore.

PERCHE' ESISTE. Un `video-analysis.md` chiuso pesa mezzo megabyte (v06: 457 KB, 1.919 righe).
Farlo aprire intero a un atomizzatore e' lo stesso errore gia' pagato col transcript: la testa
si riempie di roba che non le serve e muore prima di scrivere. Qui il taglio si fa una volta,
fuori dagli agenti, e ognuno riceve solo le scene che deve trasformare in atomi.

USO
    python scripts/taglia_analisi.py --run <run-id> --da 1 --a 126
Scrive: runs/<run-id>/_analisi-<da>-<a>.md e stampa percorso, scene e peso.
"""
import argparse, os, re, sys

NL = chr(10)
RUNS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "runs")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--da", type=int, required=True)
    ap.add_argument("--a", type=int, required=True)
    x = ap.parse_args()

    base = os.path.join(RUNS, x.run)
    src = os.path.join(base, "video-analysis.md")
    if not os.path.exists(src):
        sys.exit("manca %s: prima si unisce con unisci_parti.py" % src)

    testo = open(src, encoding="utf-8").read()
    blocchi, corrente, buf = {}, None, []
    for riga in testo.split(NL):
        m = re.match(r"^### Scena\s+(\d+)\s*[·.]", riga)
        if m:
            if corrente is not None:
                blocchi[corrente] = NL.join(buf).rstrip()
            corrente, buf = int(m.group(1)), [riga]
        elif corrente is not None:
            buf.append(riga)
    if corrente is not None:
        blocchi[corrente] = NL.join(buf).rstrip()

    presi = [n for n in range(x.da, x.a + 1) if n in blocchi]
    mancanti = [n for n in range(x.da, x.a + 1) if n not in blocchi]
    out = os.path.join(base, "_analisi-%03d-%03d.md" % (x.da, x.a))
    testa = "# analisi scene %d-%d del run %s%s%s" % (x.da, x.a, x.run, NL, NL)
    with open(out, "w", encoding="utf-8") as f:
        f.write(testa + (NL + NL).join(blocchi[n] for n in presi) + NL)

    print("%s  scene:%d/%d  peso:%d KB%s" % (
        out, len(presi), x.a - x.da + 1, os.path.getsize(out) // 1024,
        ("  MANCANTI:%s" % mancanti[:8]) if mancanti else ""))


if __name__ == "__main__":
    main()
