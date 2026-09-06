# -*- coding: utf-8 -*-
"""Unisce gli atoms-p*.json di un run in atoms.json rinumerato KA-nnn.

Idempotente. Misura cio' che conta e non si fida: archi rotti, orfani,
ancore che nell'analisi non esistono, componenti connesse del grafo.

Uso:  python scripts/unisci_atomi.py --run <run-id>
"""
import argparse, glob, io, json, os, re, sys

NL = chr(10)
RUNS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "runs")


def piano(t):
    """Toglie i marcatori markdown e schiaccia gli spazi: il confronto cade sul
    testo, non sul grassetto. Un validatore che grida al falso non lo si crede piu'."""
    return re.sub(r"\s+", " ", re.sub(r"[*`_]", "", t)).strip()


def componenti(atomi):
    adj = {a["id"]: set() for a in atomi}
    for a in atomi:
        for r in a["relazioni"]:
            adj[a["id"]].add(r["verso"]); adj[r["verso"]].add(a["id"])
    vis, comp = set(), []
    for n in sorted(adj):
        if n in vis:
            continue
        pila, c = [n], []
        while pila:
            x = pila.pop()
            if x in vis:
                continue
            vis.add(x); c.append(x); pila.extend(adj[x] - vis)
        comp.append(len(c))
    return sorted(comp, reverse=True), [i for i in adj if not adj[i]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    d = os.path.join(RUNS, a.run)

    pezzi = []
    for f in sorted(glob.glob(os.path.join(d, "atoms-p*.json"))):
        try:
            pezzi.append((os.path.basename(f), json.load(io.open(f, encoding="utf-8"))))
        except Exception as e:
            print("JSON ROTTO in %s: %s" % (f, e)); return 2
    if not pezzi:
        print("nessun atoms-p*.json in", d); return 1

    mappa, uniti = {}, []
    for nome, lista in pezzi:
        for at in lista:
            nuovo = "KA-%03d" % (len(uniti) + 1)
            mappa[at["id"]] = nuovo
            b = dict(at); b["id"] = nuovo; b["_origine"] = nome
            uniti.append(b)

    rotti = []
    for at in uniti:
        rel = []
        for r in at.get("relazioni", []):
            v = r.get("verso")
            if v in mappa:
                r2 = {"verso": mappa[v], "tipo": r.get("tipo", "collegato-a")}
                if r.get("perche"):
                    r2["perche"] = r["perche"]
                rel.append(r2)
            else:
                rotti.append((at["id"], v))
        at["relazioni"] = rel

    base = os.path.join(d, "video-analysis.md")
    testo = piano(io.open(base, encoding="utf-8").read()) if os.path.exists(base) else ""
    finte = []
    for at in uniti:
        anc = piano(at.get("ancora") or "")
        if len(anc) > 25 and anc[:60] not in testo and anc[-45:] not in testo:
            finte.append(at["id"])

    io.open(os.path.join(d, "atoms.json"), "w", encoding="utf-8", newline=NL).write(
        json.dumps(uniti, ensure_ascii=False, indent=1) + NL)

    comp, orfani = componenti(uniti)
    print("atomi        :", len(uniti))
    print("archi        :", sum(len(x["relazioni"]) for x in uniti))
    print("archi rotti  :", len(rotti), rotti[:5] if rotti else "")
    print("orfani       :", len(orfani), orfani[:10] if orfani else "")
    print("ancore non trovate:", len(finte), finte[:10] if finte else "")
    print("componenti   :", len(comp), comp)
    return 0


if __name__ == "__main__":
    sys.exit(main())
