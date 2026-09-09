# -*- coding: utf-8 -*-
"""
sintesi_visiva.py — le misure del sistema visivo, calcolate sulle 52 schede.

Il Passo 4 del dossier 33 impone che le sintesi si costruiscano DAI dati
(`scheda.json`), non rileggendo le prose. Questo script produce i numeri; la
lettura sta in SINTESI-SISTEMA-VISIVO.md.

Console Windows in cp1252: niente caratteri fuori ASCII in stampa.

Uso:  python sintesi_visiva.py
"""
import glob
import json
import os
import sys
from collections import Counter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# I prezzi noti, per rispondere alla domanda "come cambia col prezzo".
PREZZI = {
    "04-outfunnel": 98, "28-outfunnel-1": 98, "03-outheadline": 98,
    "21-outemail": 139, "23-vendita": 400, "35-vendita101-pre": 400,
    "12-claude-speedrun-v2": 249, "02-funnel-operator": 434, "05-copy": 999,
    "11-armageddon": 199,
}


def carica():
    fuori = []
    for p in sorted(glob.glob(os.path.join(BASE, "capture", "*", "scheda.json"))):
        with open(p, encoding="utf-8") as f:
            d = json.load(f)
        d["_slug"] = os.path.basename(os.path.dirname(p))
        fuori.append(d)
    return fuori


def n(d, campo):
    v = d.get(campo)
    return len(v) if isinstance(v, (list, dict)) else (v or 0)


def densita(d):
    """Media per 1.000 px: la misura che dice se una pagina e' carica o ariosa."""
    h = d.get("altezza") or 1
    return 1000.0 * n(d, "media") / h


def blocco(titolo):
    print("\n" + titolo)
    print("-" * 74)


def main():
    schede = carica()
    print("SISTEMA VISIVO - misure su {} schede".format(len(schede)))
    print("=" * 74)

    blocco("1. COSTRUZIONE")
    c = Counter(d["costruzione"] for d in schede)
    for k, v in c.most_common():
        sub = [d for d in schede if d["costruzione"] == k]
        print("  {:<14} {:>3} pagine | altezza media {:>6.0f}px | keyframes medi {:>4.1f} | "
              "media/1000px {:>4.1f}".format(
                  k, v,
                  sum(d["altezza"] for d in sub) / v,
                  sum(n(d, "keyframes") for d in sub) / v,
                  sum(densita(d) for d in sub) / v))

    blocco("2. COSA FA SEMPRE - i valori piu' ricorrenti")
    for campo in ("body_bg", "body_font"):
        cc = Counter(str(d.get(campo)) for d in schede)
        top = cc.most_common(3)
        print("  {:<10} ".format(campo) + " | ".join(
            "{} ({}/{})".format(k[:34], v, len(schede)) for k, v in top))
    colori = Counter()
    for d in schede:
        for voce in (d.get("palette_testo") or []):
            if isinstance(voce, list) and voce:
                colori[voce[0]] += 1
    print("  colori di testo piu' diffusi: " + ", ".join(
        "{} su {} pagine".format(k, v) for k, v in colori.most_common(6)))

    blocco("3. COME CAMBIA COL PREZZO")
    print("  {:<26}{:>7}{:>10}{:>8}{:>9}{:>8}".format(
        "pagina", "prezzo", "altezza", "sez", "blocchi", "med/1k"))
    for slug, prezzo in sorted(PREZZI.items(), key=lambda x: x[1]):
        d = next((x for x in schede if x["_slug"] == slug), None)
        if not d:
            continue
        print("  {:<26}{:>7}{:>10}{:>8}{:>9}{:>8.1f}".format(
            slug[:26], str(prezzo) + "E", d["altezza"], d.get("sezioni_totali", 0),
            n(d, "blocchi_testo"), densita(d)))

    blocco("4. TEMPERATURA DEL TRAFFICO - gradini contro pagine di vendita")
    grad = [d for d in schede if d["altezza"] <= 2200]
    vend = [d for d in schede if d["altezza"] >= 9000]
    for nome, gruppo in (("gradini  ", grad), ("vendita  ", vend)):
        if not gruppo:
            continue
        print("  {} {:>3} pagine | altezza media {:>6.0f}px | blocchi medi {:>5.0f} | "
              "cta medie {:>4.1f}".format(
                  nome, len(gruppo),
                  sum(d["altezza"] for d in gruppo) / len(gruppo),
                  sum(n(d, "blocchi_testo") for d in gruppo) / len(gruppo),
                  sum(n(d, "cta") for d in gruppo) / len(gruppo)))

    blocco("5. LA REGOLA DELL'ACCENTO - un colore speso una volta sola")
    uno, piu_di_uno, senza = [], [], []
    for d in schede:
        acc = [(k, v) for k, v in (d.get("palette_testo") or [])
               if isinstance(v, int) and k not in ("#fafafa", "#ebe9e0", "#ffffff", "#1c1c1e")]
        rari = [k for k, v in acc if v == 1]
        if not acc:
            senza.append(d["_slug"])
        elif rari:
            uno.append(d["_slug"])
        else:
            piu_di_uno.append(d["_slug"])
    print("  pagine con almeno un colore usato UNA volta sola : {}".format(len(uno)))
    print("  pagine senza accenti oltre i neutri              : {}".format(len(senza)))
    print("  pagine dove ogni accento e' usato piu' volte     : {}".format(len(piu_di_uno)))
    if piu_di_uno:
        print("    eccezioni: " + ", ".join(piu_di_uno[:8]))

    blocco("6. GLI ESTREMI")
    piu_alta = max(schede, key=lambda d: d["altezza"])
    piu_densa = max(schede, key=densita)
    piu_cta = max(schede, key=lambda d: n(d, "cta"))
    print("  pagina piu' alta  : {} ({}px)".format(piu_alta["_slug"], piu_alta["altezza"]))
    print("  pagina piu' densa : {} ({:.1f} media/1000px)".format(piu_densa["_slug"], densita(piu_densa)))
    print("  piu' CTA          : {} ({})".format(piu_cta["_slug"], n(piu_cta, "cta")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
