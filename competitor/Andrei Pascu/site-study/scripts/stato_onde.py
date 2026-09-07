# -*- coding: utf-8 -*-
"""
stato_onde.py — lo stato dello studio totale, contato sul disco.

Nasce dal PRE-MORTEM del 2026-09-07: la tabella STATO di ECOSISTEMA.md dichiarava
"Onda A: 0 su 9" mentre sul disco c'erano 6 catture complete. Uno stato scritto a
mano mente, e questo studio dura giorni attraversando chat che muoiono.

Una pagina e' CHIUSA solo con tutti e quattro:
    scheda.json  ·  rapporto  ·  ATLANTE  ·  COPY
(il Passo 3 del dossier 33 pretende i tre rapporti; il COPY e' quello che l'esecuzione
sta saltando, ed e' il prodotto che il concorrente vende davvero).

Uso:
    python stato_onde.py              stampa la tabella
    python stato_onde.py --scrivi     riscrive la sezione STATO di ECOSISTEMA.md
"""
import argparse
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAPTURE = os.path.join(BASE, "capture")
REPORTS = os.path.join(BASE, "reports")
ECOSISTEMA = os.path.join(BASE, "ECOSISTEMA.md")

ONDE = [
    ("A", "T1 artigianali (speedrun, apsales + 3, le 4 figlie di armageddon)", 9, [
        "12-claude-speedrun-v2", "13-apsales-v2",
        "14-arma-outemail", "15-arma-outfunnel", "16-arma-outheadline", "17-arma-outviral",
        "18-apsales-servizi", "19-apsales-landing-page", "20-apsales-consulenza",
    ]),
    ("B", "T2 mai viste su andrei-copy.com", 8, [
        "21-outemail", "22-outviral", "23-vendita", "24-asa",
        "25-define", "26-mpo2", "27-armadeggon-strp", "28-outfunnel-1",
    ]),
    ("C", "T2 gia' catturate: integrazione delle vecchie", 7, [
        "01-andrei-copy-home", "02-funnel-operator", "03-outheadline",
        "04-outfunnel", "05-copy", "06-manuale-del-copywriter",
    ]),
    ("D", "T3 la macchina del funnel (le pagine -pre)", 14, []),
    ("E", "T4 campioni di prova e negozio", 9, []),
    ("F", "T5 corpus del blog", 1, []),
    ("G", "le tre sintesi + fusione empire-premium-style", 4, []),
]


def prefissi_report():
    """Mappa numero -> tipi di rapporto presenti. Gestisce i rapporti di gruppo (14-17-...)."""
    mappa = {}
    if not os.path.isdir(REPORTS):
        return mappa
    for nome in os.listdir(REPORTS):
        if not nome.endswith(".md"):
            continue
        m = re.match(r"^(\d{2})(?:-(\d{2}))?-", nome)
        if not m:
            continue
        da = int(m.group(1))
        a = int(m.group(2)) if m.group(2) else da
        up = nome.upper()
        tipo = "atlante" if "ATLANTE" in up else ("copy" if "-COPY" in up else "rapporto")
        for n in range(da, a + 1):
            mappa.setdefault(n, set()).add(tipo)
    return mappa


def stato_pagina(slug, rep):
    num = int(slug[:2]) if slug[:2].isdigit() else -1
    tipi = rep.get(num, set())
    scheda = os.path.isfile(os.path.join(CAPTURE, slug, "scheda.json"))
    return {
        "slug": slug,
        "scheda": scheda,
        "rapporto": "rapporto" in tipi,
        "atlante": "atlante" in tipi,
        "copy": "copy" in tipi,
    }


def righe_tabella():
    rep = prefissi_report()
    fuori = []
    righe = []
    for lettera, cosa, atteso, slugs in ONDE:
        pagine = [stato_pagina(s, rep) for s in slugs]
        catturate = sum(1 for p in pagine if p["scheda"])
        chiuse = sum(1 for p in pagine if all((p["scheda"], p["rapporto"], p["atlante"], p["copy"])))
        senza_copy = [p["slug"] for p in pagine if p["scheda"] and not p["copy"]]
        righe.append({
            "onda": lettera, "cosa": cosa, "atteso": atteso, "mappate": len(slugs),
            "catturate": catturate, "chiuse": chiuse, "senza_copy": senza_copy,
            "pagine": pagine,
        })
        fuori.extend(s for s in slugs)
    orfane = []
    if os.path.isdir(CAPTURE):
        for d in sorted(os.listdir(CAPTURE)):
            if d not in fuori and os.path.isdir(os.path.join(CAPTURE, d)):
                orfane.append(d)
    return righe, orfane


def stampa(righe, orfane):
    print("STATO DELLO STUDIO TOTALE - contato sul disco, non dichiarato")
    print("=" * 78)
    print(f"{'Onda':<5}{'catturate':>11}{'chiuse':>9}{'attese':>9}   {'cosa'}")
    print("-" * 78)
    tot_c = tot_ch = tot_att = 0
    for r in righe:
        mapp = "" if r["mappate"] == r["atteso"] else f" ({r['mappate']} mappate)"
        print(f"{r['onda']:<5}{r['catturate']:>11}{r['chiuse']:>9}{r['atteso']:>9}   {r['cosa']}{mapp}")
        tot_c += r["catturate"]; tot_ch += r["chiuse"]; tot_att += r["atteso"]
    print("-" * 78)
    print(f"{'TOT':<5}{tot_c:>11}{tot_ch:>9}{tot_att:>9}")
    print()
    debiti = [(r["onda"], r["senza_copy"]) for r in righe if r["senza_copy"]]
    if debiti:
        print("DEBITO DI COPY - catturate senza teardown -COPY.md (causa 1 del pre-mortem):")
        for onda, slugs in debiti:
            print(f"  onda {onda}: {len(slugs)} - " + ", ".join(slugs))
        print()
    if orfane:
        print("CATTURE FUORI DALLE ONDE MAPPATE: " + ", ".join(orfane))
        print()
    return tot_c, tot_ch, tot_att


def scrivi(righe):
    if not os.path.isfile(ECOSISTEMA):
        print("[X] ECOSISTEMA.md non trovato", file=sys.stderr)
        return 1
    with open(ECOSISTEMA, encoding="utf-8") as f:
        testo = f.read()

    corpo = ["| Onda | Catturate | Chiuse (4 file) | Attese |", "|---|---|---|---|"]
    for r in righe:
        corpo.append(f"| Onda {r['onda']} | {r['catturate']} | {r['chiuse']} | {r['atteso']} |")
    blocco = (
        "## STATO — contato sul disco da `scripts/stato_onde.py`\n\n"
        "> Non si scrive a mano. Una pagina e' **chiusa** solo con `scheda.json` + rapporto + "
        "ATLANTE + COPY.\n\n"
        + "\n".join(corpo) + "\n"
    )

    m = re.search(r"^## STATO.*?(?=^## |\Z)", testo, re.M | re.S)
    if m:
        testo = testo[:m.start()] + blocco + "\n" + testo[m.end():]
    else:
        testo += "\n" + blocco
    with open(ECOSISTEMA, "w", encoding="utf-8", newline="\n") as f:
        f.write(testo)
    print("[OK] sezione STATO di ECOSISTEMA.md riscritta dai numeri del disco")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scrivi", action="store_true", help="riscrive la sezione STATO di ECOSISTEMA.md")
    ap.add_argument("--json", action="store_true", help="stampa i dati grezzi")
    a = ap.parse_args()
    righe, orfane = righe_tabella()
    if a.json:
        print(json.dumps(righe, indent=2, ensure_ascii=False))
        return 0
    stampa(righe, orfane)
    return scrivi(righe) if a.scrivi else 0


if __name__ == "__main__":
    sys.exit(main())
