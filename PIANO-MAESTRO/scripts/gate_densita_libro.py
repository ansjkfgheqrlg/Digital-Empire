"""
gate_densita_libro.py — il giudice della densita'. FASE 2 del piano 35, §8.4.

L'errore madre che ha prodotto un libro da 11 pagine non e' stato la fretta: e' stato
che NESSUNA macchina rifiutava il capitolo corto. Un documento non esce denso perche'
me lo ricordo. Esce denso perche' un programma conta gli atomi e blocca la consegna.

Questo script e' lo stesso mestiere di `verifica_recap.py` per il battito: non ricorda,
BLOCCA. Ed e' scritto per essere generale (piano 35 §8.7): vale per il libro e per
qualunque documento di conoscenza che dichiari quali atomi deve coprire.

COME UN CAPITOLO CITA UN ATOMO
    Nel markdown si scrive il marcatore  [[<uid>]]  dove l'atomo entra davvero.
    Esempio:  [[max18-v09-NmoOZVTrTXA::KA-045]]
    Il costruttore del PDF lo trasforma in una nota di fonte; il gate lo conta.

LE CINQUE MISURE (una sola che manca = RIFIUTATO)
    1. copertura         100% degli atomi assegnati al capitolo compare
    2. densita'          >= 150 parole attorno a ogni atomo PORTANTE
    3. ancora verbatim   >= 90% dei portanti CHE HANNO un'ancora la riportano davvero
                         (il 62% degli atomi non ce l'ha: su quelli non si puo' pretendere,
                          e il gate lo dichiara invece di fingere)
    4. blocco di confine "Cosa fa Digital Empire su questo punto" presente
    5. nessun marcatore di lavoro non finito (NO-STUB)

USO
    python gate_densita_libro.py                        # tutti i capitoli scritti
    python gate_densita_libro.py --capitolo V.16        # uno solo
    python gate_densita_libro.py --elenco V.16          # stampa gli atomi che mancano

Console Windows cp1252: nessuna emoji nei print.
"""

from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "36-LIBRO-AGENCY-INTEGRALE")
CAP_DIR = os.path.join(OUT_DIR, "capitoli")

PAROLE_MINIME_PORTANTE = 150
QUOTA_ANCORE = 0.90
BLOCCO_DE = "Cosa fa Digital Empire su questo punto"
STUB = re.compile(r"\bTODO\b|\bTBD\b|\bFIXME\b|da completare|lorem ipsum|\.\.\.\]|"
                  r"\[da scrivere\]|XXX", re.IGNORECASE)
MARCATORE = re.compile(r"\[\[([^\]\[]+?)\]\]")

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


# --------------------------------------------------------------------------- aiuti

def normalizza(t: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", (t or "").lower())


def parole(t: str) -> int:
    return len(re.sub(r"\[\[[^\]]+\]\]", " ", t or "").split())


def blocchi(testo: str) -> list[str]:
    """Il testo spezzato in blocchi (paragrafo, elenco, tabella, citazione)."""
    return [b for b in re.split(r"\n\s*\n", testo) if b.strip()]


def ancora_presente(ancora: str, testo_norm: str, minimo: int = 6) -> bool:
    """Vera se una sequenza di almeno `minimo` parole dell'ancora ricompare nel capitolo.
    Non si pretende la citazione intera: le trascrizioni contengono refusi e a capo."""
    par = normalizza(ancora).split()
    if len(par) < minimo:
        return bool(par) and " ".join(par) in testo_norm
    for i in range(len(par) - minimo + 1):
        if " ".join(par[i:i + minimo]) in testo_norm:
            return True
    return False


def carica_indice() -> dict:
    with open(os.path.join(OUT_DIR, "atomi-index.json"), encoding="utf-8") as fh:
        return json.load(fh)


# --------------------------------------------------------------------------- il giudizio

def giudica(codice: str, testo: str, atomi: list[dict], elenco: bool = False) -> tuple[bool, list[str]]:
    guai: list[str] = []
    testo_norm = normalizza(testo)
    citati = set()
    for m in MARCATORE.finditer(testo):
        citati.add(m.group(1).strip())

    attesi_corpo = [a for a in atomi if a["peso"] in ("portante", "supporto")]
    di_contesto = [a for a in atomi if a["peso"] == "contesto"]

    # --- 1. copertura ---------------------------------------------------------
    mancanti = [a for a in attesi_corpo if a["uid"] not in citati]
    if mancanti:
        guai.append("copertura: %d atomi su %d non compaiono nel capitolo"
                    % (len(mancanti), len(attesi_corpo)))
        if elenco:
            for a in mancanti:
                guai.append("    MANCA %s [%s] %s"
                            % (a["uid"], a["peso"], a["contenuto"][:90].replace("\n", " ")))

    fantasmi = citati - {a["uid"] for a in atomi}
    if fantasmi:
        guai.append("citati %d atomi che non appartengono a questo capitolo (es. %s)"
                    % (len(fantasmi), sorted(fantasmi)[0]))

    # --- 2. densita' attorno ai portanti --------------------------------------
    portanti = [a for a in atomi if a["peso"] == "portante"]
    magri = []
    for a in portanti:
        contorno = sum(parole(b) for b in blocchi(testo) if "[[%s]]" % a["uid"] in b)
        if contorno < PAROLE_MINIME_PORTANTE:
            magri.append((a["uid"], contorno))
    if magri:
        guai.append("densita': %d atomi portanti su %d hanno meno di %d parole attorno"
                    % (len(magri), len(portanti), PAROLE_MINIME_PORTANTE))
        for uid, n in magri[:12]:
            guai.append("    MAGRO %s — %d parole" % (uid, n))

    # --- 3. ancora verbatim ---------------------------------------------------
    con_ancora = [a for a in portanti if a["ancora"] and a["uid"] in citati]
    if con_ancora:
        rese = [a for a in con_ancora if ancora_presente(a["ancora"], testo_norm)]
        quota = len(rese) / len(con_ancora)
        if quota < QUOTA_ANCORE:
            guai.append("ancore: solo %d su %d atomi portanti riportano davvero la "
                        "citazione della fonte (%.0f%%, serve %.0f%%)"
                        % (len(rese), len(con_ancora), quota * 100, QUOTA_ANCORE * 100))
            for a in con_ancora:
                if a not in rese and len(guai) < 40:
                    guai.append("    SENZA ANCORA %s — attesa: \"%s\""
                                % (a["uid"], a["ancora"][:70]))

    # --- 4. blocco di confine -------------------------------------------------
    if BLOCCO_DE.lower() not in testo.lower():
        guai.append("manca il blocco \"%s\"" % BLOCCO_DE)

    # --- 5. NO-STUB -----------------------------------------------------------
    for m in STUB.finditer(testo):
        guai.append("marcatore di lavoro non finito: \"%s\"" % m.group(0))
        break

    return (not guai), guai


def rapporto_capitolo(codice: str, atomi: list[dict], testo: str, elenco: bool) -> bool:
    ok, guai = giudica(codice, testo, atomi, elenco)
    portanti = sum(1 for a in atomi if a["peso"] == "portante")
    senza_ancora = sum(1 for a in atomi if a["peso"] == "portante" and not a["ancora"])
    print("%-7s %-8s %5d parole  %3d atomi (%d portanti, %d senza ancora in origine)"
          % (codice, "PASSA" if ok else "RIFIUTATO", parole(testo), len(atomi),
             portanti, senza_ancora))
    for g in guai:
        print("        %s" % g)
    return ok


def main() -> int:
    solo = None
    elenco = "--elenco" in sys.argv
    for bandiera in ("--capitolo", "--elenco"):
        if bandiera in sys.argv:
            i = sys.argv.index(bandiera)
            if i + 1 < len(sys.argv) and not sys.argv[i + 1].startswith("--"):
                solo = sys.argv[i + 1]

    indice = carica_indice()
    if not indice["atomi"] or indice["atomi"][0].get("capitolo") is None:
        print("La classificazione non e' ancora dentro l'indice: prima "
              "`valida_assegnazioni.py`. Niente da giudicare.")
        return 1

    per_capitolo: dict[str, list[dict]] = {}
    for a in indice["atomi"]:
        if a["capitolo"] and a["capitolo"] != "FUORI":
            per_capitolo.setdefault(a["capitolo"], []).append(a)

    if not os.path.isdir(CAP_DIR):
        print("Nessun capitolo scritto: manca %s" % CAP_DIR)
        print("Capitoli previsti dalla classificazione: %d" % len(per_capitolo))
        return 1

    passati, rifiutati, non_scritti = 0, 0, []
    for codice in sorted(per_capitolo, key=lambda c: (c.split(".")[0], int(c.split(".")[1]))):
        if solo and codice != solo:
            continue
        path = os.path.join(CAP_DIR, "%s.md" % codice)
        if not os.path.exists(path):
            non_scritti.append(codice)
            continue
        with open(path, encoding="utf-8") as fh:
            testo = fh.read()
        if rapporto_capitolo(codice, per_capitolo[codice], testo, elenco):
            passati += 1
        else:
            rifiutati += 1

    print("")
    print("capitoli passati: %d   rifiutati: %d   non ancora scritti: %d"
          % (passati, rifiutati, len(non_scritti)))
    if non_scritti and not solo:
        print("non scritti: %s" % ", ".join(non_scritti[:25]))
    return 0 if rifiutati == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
