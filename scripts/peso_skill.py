# -*- coding: utf-8 -*-
"""
PESO SKILL - quanto ci costa davvero ogni strumento, a ogni accensione.

Il problema
-----------
Una skill si carica INTERA quando si attiva. Se ne servono tre righe, si paga
tutto il file. 115 delle 170 skill superano le 150 righe; le peggiori superano
le 5.000. Nessuno aveva mai misurato quanto costa: senza la misura, "sono troppo
lunghe" resta un'opinione e non si decide niente (voce B-039).

Cosa fa
-------
Misura ogni skill in righe, byte e gettoni stimati, la confronta con la soglia,
e dice quali vanno spezzate per prime - ordinate per costo, non per lunghezza.
Distingue chi e' lungo perche' contiene conoscenza vera (accettabile, ma va
spostata in file a parte) da chi e' lungo per disordine.

Non modifica niente. Misura e riferisce.

Uso:
    python scripts/peso_skill.py
    python scripts/peso_skill.py --tutte        anche quelle sotto soglia
    python scripts/peso_skill.py --scrivi       scrive il rapporto su file

Console Windows: solo ASCII in output.
"""

import os
import io
import sys
import argparse
from datetime import datetime

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(RADICE, ".claude", "skills")
RAPPORTO = os.path.join(RADICE, "company", "Memory", "PESO-SKILL.md")

# soglia oltre la quale una skill andrebbe spezzata in indice + file a parte.
# Origine: prompt "Skills Level 3" di Jay E (video 8NSyI-npJCU) - NON e' uno
# standard ufficiale Anthropic, e va detto: e' una soglia presa da una fonte
# esterna e adottata da noi, non una legge di natura.
SOGLIA_RIGHE = 150

# quattro caratteri per gettone: stima grossolana e dichiarata tale, buona per
# confrontare le skill fra loro, non per fatturare.
CARATTERI_PER_GETTONE = 4.0


def gettoni(caratteri):
    return int(caratteri / CARATTERI_PER_GETTONE)


def analizza_una(percorso):
    try:
        with io.open(percorso, encoding="utf-8", errors="ignore") as f:
            testo = f.read()
    except IOError:
        return None

    righe = testo.count("\n") + 1
    caratteri = len(testo)

    # quanto di questo file e' conoscenza vera (esempi, tabelle, blocchi di
    # codice) e quanto e' istruzione? La conoscenza va spostata in file a parte,
    # non buttata: e' la differenza fra spezzare e amputare.
    in_blocco = False
    righe_codice = 0
    righe_tabella = 0
    for r in testo.split("\n"):
        se = r.strip()
        if se.startswith("```"):
            in_blocco = not in_blocco
            righe_codice += 1
            continue
        if in_blocco:
            righe_codice += 1
        elif se.startswith("|"):
            righe_tabella += 1

    quota_materiale = (righe_codice + righe_tabella) / float(max(righe, 1))

    return {
        "righe": righe,
        "caratteri": caratteri,
        "gettoni": gettoni(caratteri),
        "righe_codice": righe_codice,
        "righe_tabella": righe_tabella,
        "quota_materiale": quota_materiale,
    }


def diagnosi(d):
    """Perche' e' lunga - e quindi cosa farne."""
    if d["righe"] <= SOGLIA_RIGHE:
        return "sotto soglia", "niente da fare"
    if d["quota_materiale"] > 0.45:
        return ("piena di materiale",
                "spostare esempi e tabelle in file a parte, lasciare l'indice")
    if d["righe"] > 1500:
        return ("enorme",
                "spezzare in indice + file per argomento: si carica solo cio' che serve")
    return ("lunga", "accorciare le istruzioni, spostare i dettagli in file a parte")


def raccogli():
    fuori = []
    if not os.path.isdir(SKILLS):
        print("Cartella skill non trovata: %s" % SKILLS)
        return fuori

    for radice_dir, dirs, files in os.walk(SKILLS):
        dirs[:] = [x for x in dirs if not x.startswith(".")]
        for nome in files:
            if nome != "SKILL.md":
                continue
            pieno = os.path.join(radice_dir, nome)
            rel = os.path.relpath(pieno, RADICE).replace("\\", "/")
            d = analizza_una(pieno)
            if d is None:
                continue
            # il nome della skill e' la cartella che la contiene
            d["nome"] = os.path.basename(os.path.dirname(pieno))
            d["percorso"] = rel
            d["causa"], d["rimedio"] = diagnosi(d)
            fuori.append(d)

    fuori.sort(key=lambda x: -x["gettoni"])
    return fuori


def stampa(tutte, mostra_tutte):
    sopra = [t for t in tutte if t["righe"] > SOGLIA_RIGHE]
    da_mostrare = tutte if mostra_tutte else sopra

    tot_gettoni = sum(t["gettoni"] for t in tutte)
    gettoni_sopra = sum(t["gettoni"] for t in sopra)

    print("")
    print("=" * 78)
    print("  PESO SKILL - quanto costa ogni strumento a ogni accensione")
    print("  " + datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("=" * 78)
    print("")
    print("  IL CONTO:")
    print("    %d skill in tutto" % len(tutte))
    print("    %d sopra le %d righe (%d%%)"
          % (len(sopra), SOGLIA_RIGHE, int(100.0 * len(sopra) / max(len(tutte), 1))))
    print("    %s gettoni stimati in tutto, di cui %s nelle skill sopra soglia (%d%%)"
          % ("{:,}".format(tot_gettoni).replace(",", "."),
             "{:,}".format(gettoni_sopra).replace(",", "."),
             int(100.0 * gettoni_sopra / max(tot_gettoni, 1))))
    print("")
    print("-" * 78)
    print("")
    print("  %-38s %6s %9s  %s" % ("SKILL", "RIGHE", "GETTONI", "PERCHE'"))
    print("  " + "-" * 74)

    for t in da_mostrare[:40]:
        print("  %-38s %6d %9s  %s"
              % (t["nome"][:38], t["righe"],
                 "{:,}".format(t["gettoni"]).replace(",", "."), t["causa"]))

    if len(da_mostrare) > 40:
        print("  ... e altre %d" % (len(da_mostrare) - 40))

    print("")
    print("-" * 78)
    print("")
    print("  LE PRIME CINQUE - qui sta il grosso del costo:")
    print("")
    for t in da_mostrare[:5]:
        print("  %s (%d righe, %s gettoni)"
              % (t["nome"], t["righe"],
                 "{:,}".format(t["gettoni"]).replace(",", ".")))
        print("     %d%% del file e' materiale (esempi, tabelle, codice)"
              % int(100 * t["quota_materiale"]))
        print("     -> %s" % t["rimedio"])
        print("")

    print("=" * 78)
    print("  NOTA ONESTA: i gettoni sono stimati a 4 caratteri l'uno. Serve a")
    print("  confrontare le skill fra loro, non a fatturare. La soglia di 150")
    print("  righe viene da una fonte esterna adottata da noi, non da uno")
    print("  standard ufficiale.")
    print("=" * 78)
    print("")


def scrivi_rapporto(tutte):
    os.makedirs(os.path.dirname(RAPPORTO), exist_ok=True)
    sopra = [t for t in tutte if t["righe"] > SOGLIA_RIGHE]
    tot = sum(t["gettoni"] for t in tutte)
    tot_sopra = sum(t["gettoni"] for t in sopra)

    r = []
    r.append("# PESO SKILL - quanto costa ogni strumento a ogni accensione")
    r.append("")
    r.append("> Rigenerato da `scripts/peso_skill.py` il %s"
             % datetime.now().strftime("%Y-%m-%d %H:%M"))
    r.append("> Non modificare a mano: si riscrive a ogni esecuzione.")
    r.append("")
    r.append("## Il conto")
    r.append("")
    r.append("| | |")
    r.append("|---|---|")
    r.append("| Skill in tutto | **%d** |" % len(tutte))
    r.append("| Sopra le %d righe | **%d** (%d%%) |"
             % (SOGLIA_RIGHE, len(sopra),
                int(100.0 * len(sopra) / max(len(tutte), 1))))
    r.append("| Gettoni stimati in tutto | **%s** |"
             % "{:,}".format(tot).replace(",", "."))
    r.append("| Di cui nelle skill sopra soglia | **%s** (%d%%) |"
             % ("{:,}".format(tot_sopra).replace(",", "."),
                int(100.0 * tot_sopra / max(tot, 1))))
    r.append("")
    r.append("## Le piu' pesanti")
    r.append("")
    r.append("| Skill | Righe | Gettoni | Materiale | Perche' | Rimedio |")
    r.append("|---|---|---|---|---|---|")
    for t in sopra[:30]:
        r.append("| `%s` | %d | %s | %d%% | %s | %s |"
                 % (t["nome"], t["righe"],
                    "{:,}".format(t["gettoni"]).replace(",", "."),
                    int(100 * t["quota_materiale"]), t["causa"], t["rimedio"]))
    r.append("")
    r.append("## Nota onesta sui numeri")
    r.append("")
    r.append("- I gettoni sono **stimati** a 4 caratteri l'uno: servono a confrontare le")
    r.append("  skill fra loro, non a fatturare.")
    r.append("- La soglia di 150 righe viene da una **fonte esterna** adottata da noi")
    r.append("  (prompt \"Skills Level 3\", video `8NSyI-npJCU`), non da uno standard ufficiale.")
    r.append("- \"Materiale\" = righe di codice e di tabella. Una skill piena di materiale non")
    r.append("  e' disordinata: contiene conoscenza vera, che va **spostata** in file a parte,")
    r.append("  non buttata.")
    r.append("")

    # newline="\n" obbligatorio: su Windows la scrittura di testo tradurrebbe in
    # CRLF, e il guardiano pre-commit blocca i CRLF dentro company/Memory perche'
    # rendono illeggibili le fusioni col lavoro dell'altro socio.
    with io.open(RAPPORTO, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(r) + "\n")


def main():
    ap = argparse.ArgumentParser(description="Peso Skill - misura il costo delle skill")
    ap.add_argument("--tutte", action="store_true",
                    help="mostra anche le skill sotto soglia")
    ap.add_argument("--scrivi", action="store_true",
                    help="scrive il rapporto in company/Memory/PESO-SKILL.md")
    args = ap.parse_args()

    tutte = raccogli()
    if not tutte:
        return 1
    stampa(tutte, args.tutte)
    if args.scrivi:
        scrivi_rapporto(tutte)
        print("Rapporto scritto in: company/Memory/PESO-SKILL.md")
        print("")
    return 0


if __name__ == "__main__":
    sys.exit(main())
