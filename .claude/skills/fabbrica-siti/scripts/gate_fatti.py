#!/usr/bin/env python3
"""gate_fatti.py — ogni numero del copy deve stare in FATTI.md (Dossier 37 v2, C2.4).

Deterministico: estrae ogni cifra da COPY.md (fuori dalle righe di struttura) e fallisce se non
compare, come numero, in FATTI.md. Un numero senza fonte non entra in pagina.

Uso:
  python gate_fatti.py COPY.md FATTI.md            # exit 0 = PASS, 1 = FAIL
  python gate_fatti.py COPY.md FATTI.md --mostra   # elenca anche i numeri ammessi

Cosa NON conta come numero del copy:
  - righe di struttura: `## N1 —`, `**id**`, `[ruolo]` (il tag fra parentesi quadre), `data-fonte=`
  - riferimenti a posti/sezioni del manifest (`posto 3`, `N12`, `?da=N2`)
  - i numeri romani (I, II, III) non sono cifre
"""
import io, re, sys, pathlib

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

NUM = re.compile(r"(?<![\w/.-])(\d+(?:[.,]\d+)*)(?![\w/-])")


def numeri(testo: str):
    out = set()
    for m in NUM.finditer(testo):
        n = m.group(1)
        out.add(n)
        # 2.400 e 2400, 2,5 e 2.5 contano uguali
        out.add(n.replace(".", "").replace(",", "."))
        out.add(n.replace(".", ""))
    return out


def righe_copy(path: pathlib.Path):
    for i, riga in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        r = riga.strip()
        if not r or r.startswith("#") or r.startswith("**id**") or r.startswith("---") or r.startswith(">"):
            continue
        if r.startswith("[") and "]" in r:
            tag, _, resto = r.partition("]")
            if "fonte" in tag:  # [caso-1-fonte] data-fonte=...
                continue
            r = resto
        r = re.sub(r"\?da=N\d+", "", r)
        r = re.sub(r"\bN\d+\b", "", r)
        r = re.sub(r"\bposto\s+\d+", "", r)
        r = re.sub(r"\bposti\s+[\d, e]+", "", r)
        yield i, r


def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    copy, fatti = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    mostra = "--mostra" in sys.argv
    ammessi = numeri(fatti.read_text(encoding="utf-8"))
    if mostra:
        print("ammessi:", ", ".join(sorted(ammessi, key=lambda x: (len(x), x))))
    errori = []
    tot = 0
    for i, r in righe_copy(copy):
        for m in NUM.finditer(r):
            tot += 1
            n = m.group(1)
            if n in ammessi or n.replace(".", "") in ammessi:
                continue
            errori.append((i, n, r.strip()[:90]))
    print(f"GATE FATTI — {copy.name} contro {fatti.name}: {tot} numeri letti, {len(errori)} senza fonte")
    for i, n, r in errori:
        print(f"  riga {i}: «{n}» — {r}")
    print("PASS" if not errori else "FAIL")
    sys.exit(0 if not errori else 1)


if __name__ == "__main__":
    main()
