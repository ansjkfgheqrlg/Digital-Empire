# -*- coding: utf-8 -*-
"""Unisce atoms-p*.json in un solo atoms.json rinumerato KA-nnn.

Idempotente. Verifica: archi rotti, orfani, ancore realmente presenti
nell'analisi. I numeri si contano, non si dichiarano.
"""
import io, json, glob, os, sys, re

NL = chr(10)
ORDINE = ["atoms-p1.json", "atoms-p1b.json", "atoms-p2a.json",
          "atoms-p2b.json", "atoms-p3.json", "atoms-p3b.json"]


def main():
    pezzi, mancanti = [], []
    for f in ORDINE:
        if os.path.exists(f):
            try:
                d = json.load(io.open(f, encoding="utf-8"))
                pezzi.append((f, d))
            except Exception as e:
                print("JSON ROTTO in %s: %s" % (f, e)); return 2
        else:
            mancanti.append(f)
    if mancanti:
        print("pezzi non ancora presenti:", mancanti)

    # rinumerazione stabile nell'ordine di lettura
    mappa, uniti = {}, []
    for f, d in pezzi:
        for a in d:
            nuovo = "KA-%03d" % (len(uniti) + 1)
            mappa[a["id"]] = nuovo
            b = dict(a); b["id"] = nuovo; b["_origine"] = f
            uniti.append(b)

    rotti = []
    for a in uniti:
        rel = []
        for r in a.get("relazioni", []):
            v = r.get("verso")
            if v in mappa:
                rel.append({"verso": mappa[v], "tipo": r.get("tipo", "collegato-a")})
            else:
                rotti.append((a["id"], v))
        a["relazioni"] = rel

    ids = set(a["id"] for a in uniti)
    puntati = set(r["verso"] for a in uniti for r in a["relazioni"])
    orfani = [a["id"] for a in uniti if not a["relazioni"] and a["id"] not in puntati]

    # verifica che le ancore esistano davvero nell'analisi
    def piano(t):
        """Toglie i marcatori markdown e schiaccia gli spazi: il confronto deve
        cadere sul testo, non sul grassetto. Senza questo il controllo grida al
        falso e chi lo legge smette di credergli."""
        t = re.sub(r"[*`_]", "", t)
        return re.sub(r"\s+", " ", t).strip()

    testo = piano(io.open("video-analysis.md", encoding="utf-8").read()) if os.path.exists("video-analysis.md") else ""
    ancore_finte = []
    for a in uniti:
        anc = piano(a.get("ancora") or "")
        if len(anc) > 25 and anc[:60] not in testo and anc[-45:] not in testo:
            ancore_finte.append(a["id"])

    io.open("atoms.json", "w", encoding="utf-8", newline=NL).write(
        json.dumps(uniti, ensure_ascii=False, indent=1) + NL)

    archi = sum(len(a["relazioni"]) for a in uniti)
    print("atomi        :", len(uniti))
    print("archi        :", archi)
    print("archi rotti  :", len(rotti), rotti[:5] if rotti else "")
    print("orfani       :", len(orfani), orfani[:10] if orfani else "")
    print("ancore non trovate nell'analisi:", len(ancore_finte), ancore_finte[:10] if ancore_finte else "")
    tipi = {}
    for a in uniti:
        tipi[a.get("tipo", "?")] = tipi.get(a.get("tipo", "?"), 0) + 1
    print("per tipo     :", dict(sorted(tipi.items(), key=lambda x: -x[1])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
