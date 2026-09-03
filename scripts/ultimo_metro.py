# -*- coding: utf-8 -*-
"""
ULTIMO METRO - l'occhio che vede il lavoro finito e fermo.

Digital Empire produce e non pubblica. Non per mancanza di strumenti: i pubblicatori
esistono gia' (social-publisher, workflow-pubblicazione-auto). Manca l'organo che
GUARDA e dice cosa e' pronto e da quanti giorni marcisce.

Questo script apre i depositi noti, riconosce cosa e' finito, incrocia col registro
di cio' che e' gia' uscito, e produce la lista di cosa caricare OGGI, dal piu' vecchio.

Non pubblica niente. Vede, e riferisce.

Uso:
    python scripts/ultimo_metro.py                 rapporto a schermo
    python scripts/ultimo_metro.py --scrivi        scrive anche il rapporto su file
    python scripts/ultimo_metro.py --segna <id>    segna un pezzo come pubblicato

Console Windows: solo ASCII in output, cp1252 non regge gli emoji.
"""

import os
import sys
import json
import time
import argparse
from datetime import datetime

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRO = os.path.join(RADICE, "company", "Memory", "pubblicati.json")
RAPPORTO = os.path.join(RADICE, "company", "Memory", "ULTIMO-METRO.md")

# --------------------------------------------------------------------------
# I DEPOSITI - dove si accumula il lavoro finito.
# Aggiungerne uno = aggiungere una voce qui. Nient'altro da toccare.
# --------------------------------------------------------------------------
DEPOSITI = [
    {
        "percorso": "company/Ecosistemi/02-INFO-BUSINESS/Workflow/"
                    "libri-performanti-multiagente/LIBRI/libri_pronti",
        "tipo": "LIBRO",
        "granularita": "cartella",
        "canale": "Amazon KDP",
        "richiesti": [".pdf", ".epub"],
        "copertina": [".png", ".jpg", ".jpeg"],
    },
    {
        "percorso": "YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI",
        "tipo": "VIDEO",
        "granularita": "cartella",
        "canale": "YouTube",
        "richiesti": [".mp4"],
        "copertina": [".png", ".jpg", ".jpeg"],
    },
    {
        "percorso": "Lancio corso skill beast/Page/Leo/da pubblicare",
        "tipo": "VIDEO",
        "granularita": "file",
        "canale": "YouTube / Social",
        "richiesti": [".mp4"],
        "copertina": [],
    },
]

# soglie di allarme, in giorni di fermo
SOGLIA_ROSSA = 60
SOGLIA_GIALLA = 14


def carica_registro():
    """Cio' che e' gia' uscito. Registro assente = non e' mai uscito niente."""
    if not os.path.exists(REGISTRO):
        return {"pubblicati": {}, "creato": datetime.now().strftime("%Y-%m-%d")}
    try:
        with open(REGISTRO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (ValueError, IOError):
        # un registro illeggibile non deve fermare l'occhio: si riparte da vuoto
        return {"pubblicati": {}, "creato": None, "errore_lettura": True}


def salva_registro(reg):
    os.makedirs(os.path.dirname(REGISTRO), exist_ok=True)
    # newline="\n" obbligatorio: su Windows la scrittura di testo tradurrebbe in
    # CRLF, e il guardiano pre-commit blocca i CRLF dentro company/Memory perche'
    # rendono illeggibili le fusioni col lavoro dell'altro socio.
    with open(REGISTRO, "w", encoding="utf-8", newline="\n") as f:
        json.dump(reg, f, indent=2, ensure_ascii=False)


def giorni_fermo(percorso):
    """Da quanti giorni non si tocca. Su una cartella guarda il file piu' recente:
    e' quello che dice quando il lavoro e' stato davvero finito."""
    piu_recente = 0
    if os.path.isfile(percorso):
        try:
            piu_recente = os.path.getmtime(percorso)
        except OSError:
            return None
    else:
        for radice, _dirs, files in os.walk(percorso):
            for nome in files:
                try:
                    m = os.path.getmtime(os.path.join(radice, nome))
                    if m > piu_recente:
                        piu_recente = m
                except OSError:
                    continue
    if piu_recente == 0:
        return None
    return int((time.time() - piu_recente) / 86400)


def peso_mb(percorso):
    tot = 0
    if os.path.isfile(percorso):
        try:
            return os.path.getsize(percorso) / (1024.0 * 1024.0)
        except OSError:
            return 0.0
    for radice, _dirs, files in os.walk(percorso):
        for nome in files:
            try:
                tot += os.path.getsize(os.path.join(radice, nome))
            except OSError:
                continue
    return tot / (1024.0 * 1024.0)


def estensioni_presenti(percorso):
    est = set()
    if os.path.isfile(percorso):
        est.add(os.path.splitext(percorso)[1].lower())
        return est
    for radice, _dirs, files in os.walk(percorso):
        for nome in files:
            est.add(os.path.splitext(nome)[1].lower())
    return est


def valuta_completezza(deposito, percorso):
    """Quanto e' finito questo pezzo e cosa gli manca.
    Ritorna (percentuale, elenco delle cose mancanti)."""
    est = estensioni_presenti(percorso)
    mancanti = []
    punti = 0
    totale = 0

    for r in deposito["richiesti"]:
        totale += 1
        if r in est:
            punti += 1
        else:
            mancanti.append("manca il file %s" % r)

    if deposito["copertina"]:
        totale += 1
        if any(c in est for c in deposito["copertina"]):
            punti += 1
        else:
            mancanti.append("manca la copertina")

    # i dati per il negozio (titolo, descrizione, parole chiave): senza, non si carica
    if deposito["tipo"] == "LIBRO":
        totale += 1
        ha_meta = False
        if os.path.isdir(percorso):
            for nome in os.listdir(percorso):
                basso = nome.lower()
                if "metadata" in basso or "kdp" in basso:
                    ha_meta = True
                    break
        if ha_meta:
            punti += 1
        else:
            mancanti.append("mancano i dati per il negozio")

    perc = int(100.0 * punti / totale) if totale else 0
    return perc, mancanti


def scandaglia():
    """Apre i depositi e conta cosa c'e' dentro che non e' mai uscito."""
    reg = carica_registro()
    gia_usciti = reg.get("pubblicati", {})
    trovati = []
    depositi_assenti = []

    for dep in DEPOSITI:
        base = os.path.join(RADICE, dep["percorso"])
        if not os.path.isdir(base):
            depositi_assenti.append(dep["percorso"])
            continue

        if dep["granularita"] == "cartella":
            voci = [v for v in sorted(os.listdir(base))
                    if os.path.isdir(os.path.join(base, v))]
        else:
            voci = [v for v in sorted(os.listdir(base))
                    if os.path.isfile(os.path.join(base, v))
                    and os.path.splitext(v)[1].lower() in dep["richiesti"]]

        for voce in voci:
            pieno = os.path.join(base, voce)
            ident = "%s/%s" % (dep["percorso"], voce)
            if ident in gia_usciti:
                continue  # gia' uscito, non e' piu' affar nostro

            perc, mancanti = valuta_completezza(dep, pieno)
            trovati.append({
                "id": ident,
                "nome": voce,
                "tipo": dep["tipo"],
                "canale": dep["canale"],
                "giorni": giorni_fermo(pieno) or 0,
                "mb": peso_mb(pieno),
                "completezza": perc,
                "mancanti": mancanti,
                "percorso": pieno,
            })

    # il piu' vecchio per primo: e' quello che ci sta costando di piu'
    trovati.sort(key=lambda x: (-x["giorni"], -x["completezza"]))
    return trovati, depositi_assenti, reg


def semaforo(giorni):
    if giorni >= SOGLIA_ROSSA:
        return "[ROSSO] "
    if giorni >= SOGLIA_GIALLA:
        return "[GIALLO]"
    return "[VERDE] "


def stampa(trovati, assenti):
    print("")
    print("=" * 78)
    print("  ULTIMO METRO - il lavoro finito che non e' mai uscito")
    print("  " + datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("=" * 78)

    if not trovati:
        print("")
        print("  Nessun pezzo finito in attesa. I depositi sono vuoti.")
        print("  Se non te lo aspettavi: controlla che i depositi elencati in")
        print("  DEPOSITI puntino ancora alle cartelle giuste.")
        print("")
        return

    pronti = [t for t in trovati if t["completezza"] == 100]
    quasi = [t for t in trovati if t["completezza"] < 100]
    mb_tot = sum(t["mb"] for t in trovati)
    piu_vecchio = max(t["giorni"] for t in trovati)

    print("")
    print("  IL CONTO:")
    print("    %d pezzi finiti e mai usciti, %.0f MB di lavoro fermo"
          % (len(trovati), mb_tot))
    print("    %d caricabili subito, senza toccare niente" % len(pronti))
    print("    %d a cui manca un pezzo" % len(quasi))
    print("    il piu' vecchio e' fermo da %d giorni" % piu_vecchio)
    print("")
    print("-" * 78)
    print("")

    if pronti:
        print("  CARICABILI ADESSO - non manca niente")
        print("")
        for t in pronti:
            print("  %s %4d gg  %-7s %-30s %7.0f MB  -> %s"
                  % (semaforo(t["giorni"]), t["giorni"], t["tipo"],
                     t["nome"][:30], t["mb"], t["canale"]))
        print("")

    if quasi:
        print("  MANCA UN PEZZO - poco lavoro e sono fuori")
        print("")
        for t in quasi:
            print("  %s %4d gg  %-7s %-30s  %d%% pronto"
                  % (semaforo(t["giorni"]), t["giorni"], t["tipo"],
                     t["nome"][:30], t["completezza"]))
            for m in t["mancanti"]:
                print("                     - %s" % m)
        print("")

    if assenti:
        print("-" * 78)
        print("")
        print("  DEPOSITI NON TROVATI - puntatore vecchio o cartella spostata:")
        for a in assenti:
            print("    %s" % a)
        print("")

    print("=" * 78)
    print("  Quando ne carichi uno, segnalo:")
    print('    python scripts/ultimo_metro.py --segna "ID-DEL-PEZZO"')
    print("  Cosi' sparisce dalla lista e non te lo ripropongo piu'.")
    print("=" * 78)
    print("")


def scrivi_rapporto(trovati, assenti):
    """Il rapporto su file: serve a chi non ha una console davanti."""
    os.makedirs(os.path.dirname(RAPPORTO), exist_ok=True)
    r = []
    r.append("# ULTIMO METRO - il lavoro finito che non e' mai uscito")
    r.append("")
    r.append("> Rigenerato da `scripts/ultimo_metro.py` il %s"
             % datetime.now().strftime("%Y-%m-%d %H:%M"))
    r.append("> Non modificare a mano: si riscrive a ogni esecuzione.")
    r.append("")

    if not trovati:
        r.append("Nessun pezzo finito in attesa.")
        with open(RAPPORTO, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(r) + "\n")
        return

    mb_tot = sum(t["mb"] for t in trovati)
    piu_vecchio = max(t["giorni"] for t in trovati)
    pronti = [t for t in trovati if t["completezza"] == 100]

    r.append("## Il conto")
    r.append("")
    r.append("| | |")
    r.append("|---|---|")
    r.append("| Pezzi finiti e mai usciti | **%d** |" % len(trovati))
    r.append("| Lavoro fermo | **%.0f MB** |" % mb_tot)
    r.append("| Caricabili subito | **%d** |" % len(pronti))
    r.append("| Il piu' vecchio e' fermo da | **%d giorni** |" % piu_vecchio)
    r.append("")
    r.append("## La lista, dal piu' vecchio")
    r.append("")
    r.append("| | Fermo da | Tipo | Nome | Peso | Dove va | Pronto |")
    r.append("|---|---|---|---|---|---|---|")
    for t in trovati:
        r.append("| %s | %d gg | %s | %s | %.0f MB | %s | %d%% |"
                 % (semaforo(t["giorni"]).strip(), t["giorni"], t["tipo"],
                    t["nome"], t["mb"], t["canale"], t["completezza"]))
    r.append("")

    manca = [t for t in trovati if t["mancanti"]]
    if manca:
        r.append("## Cosa manca, pezzo per pezzo")
        r.append("")
        for t in manca:
            r.append("- **%s** (%s, fermo da %d gg): %s"
                     % (t["nome"], t["tipo"], t["giorni"], "; ".join(t["mancanti"])))
        r.append("")

    if assenti:
        r.append("## Depositi non trovati")
        r.append("")
        r.append("Puntatore vecchio o cartella spostata - vanno corretti in `DEPOSITI`:")
        r.append("")
        for a in assenti:
            r.append("- `%s`" % a)
        r.append("")

    with open(RAPPORTO, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(r) + "\n")


def segna(ident):
    reg = carica_registro()
    reg.setdefault("pubblicati", {})[ident] = {
        "data": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    salva_registro(reg)
    print("Segnato come pubblicato: %s" % ident)
    print("Non comparira' piu' nella lista.")


def main():
    ap = argparse.ArgumentParser(
        description="Ultimo Metro - vede il lavoro finito e fermo")
    ap.add_argument("--scrivi", action="store_true",
                    help="scrive anche il rapporto in company/Memory/ULTIMO-METRO.md")
    ap.add_argument("--segna", metavar="ID",
                    help="segna un pezzo come pubblicato, cosi' esce dalla lista")
    args = ap.parse_args()

    if args.segna:
        segna(args.segna)
        return 0

    trovati, assenti, _reg = scandaglia()
    stampa(trovati, assenti)
    if args.scrivi:
        scrivi_rapporto(trovati, assenti)
        print("Rapporto scritto in: company/Memory/ULTIMO-METRO.md")
        print("")
    return 0


if __name__ == "__main__":
    sys.exit(main())
