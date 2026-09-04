# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L02.

«Scrivere e (ri)scrivere testi originali con A.I» · 15:35 · relatore Pietro Gangemi ·
registrata il 20 aprile 2023 (data visibile nel testo generato, frame-022).

E' la lezione piu' vicina al cuore della fabbrica: quattro comandi di riscrittura e una
leva (la sorgente in un'altra lingua). Ha scoperto il buco piu' grave trovato finora in
questo studio: sappiamo misurare se un testo e' COPIATO (regolatori.py:153, n-grammi) e
non abbiamo niente che dica se e' ancora VERO. Cercato su tutta la fabbrica
("verifica dei fatti", "fact-check", "controllo dei fatti"): zero risultati.

NOTA DI PROVENIENZA: questa lezione era arrivata a casa col video sbagliato due volte
(119 s e 1.595 s contro i 935 dichiarati). Le prove qui sotto vengono dal video giusto,
riscaricato dopo la riparazione dell'ingestione.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L02"
LEZIONE = "Scrivere e (ri)scrivere testi originali con A.I"

REGOLE = [
    {
        "id": "A4-L02-01",
        "tipo": "vincolo",
        "regola": ("Mai impersonare una testata, un ente o un giornalista reale: ne' nel testo "
                   "pubblicato, ne' nel comando dato al modello. L'autorevolezza di un nome che "
                   "non e' nostro non si prende in prestito."),
        "prova": "solo parlato @ 10:22 e @ 12:01 ('tolgo queste RAI, perche' non lo siamo')",
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/regolatori/regolatore-copy.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "alto",
        "misura": ("regolatore-copy elenca il divieto fra le cause di BLOCCO; oggi i divieti "
                   "riguardano solo lo stile (anglicismi, emoji, promesse mediche)"),
    },
    {
        "id": "A4-L02-02",
        "tipo": "procedura",
        "regola": ("I fatti presi dalla sorgente — nomi, date, cifre, citazioni fra virgolette, "
                   "luoghi — si rileggono uno per uno contro la fonte DOPO la riscrittura. Si "
                   "controlla che sia ancora vero, non solo che non sia copiato."),
        "prova": "frame-043.png @ 02:48 (testo riscritto con eta', data, causa, citazioni)",
        "fonte": "schermo",
        "tocca": "03-AGENTI-E-RUOLI/operatori/script-writer.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "alto",
        "misura": ("script-writer ha una lista dei fatti da riverificare; oggi in tutta la "
                   "fabbrica non esiste nessun controllo dei fatti (grep: zero risultati)"),
    },
    {
        "id": "A4-L02-03",
        "tipo": "strumento",
        "regola": ("Esiste un catalogo dei comandi di riscrittura, con la clausola "
                   "anti-ripetizione obbligatoria e il divieto di allungare con 'continua': si "
                   "allunga con le fonti, mai col serbatoio del modello."),
        "prova": "solo parlato @ 02:43 ('aggiungi questa parte senza essere ripetitivo') e @ 08:07",
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/comandi-riscrittura.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "medio",
        "misura": ("esiste la scheda dei comandi; oggi in script-writer.md la parola 'prompt' "
                   "compare una volta sola, ed e' l'intestazione di una sezione"),
    },
    {
        "id": "A4-L02-04",
        "tipo": "vincolo",
        "regola": ("Una sorgente in un'altra lingua e' ammessa e va cercata, ma allora il "
                   "controllo a n-grammi e' cieco per costruzione: serve un controllo semantico "
                   "dichiarato, altrimenti 'zero sovrapposizione' viene scambiato per prova di "
                   "originalita' quando non lo e'."),
        "prova": "frame-215.png @ 14:16 (sottotitoli francesi -> testo italiano) + parlato @ 13:48",
        "fonte": "entrambi",
        "tocca": "03-AGENTI-E-RUOLI/capi/capo-ricerca.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "medio",
        "misura": ("capo-ricerca dice cosa fare con una sorgente non italiana e impone il "
                   "controllo semantico; il punto cieco e' gia' dichiarato in regolatori.py:156"),
    },
]


def verifica(fabbrica):
    """Dice se la fabbrica rispetta gia' queste regole. Nessun effetto collaterale."""
    import os

    def contiene(percorso_relativo, aghi):
        p = os.path.join(fabbrica, percorso_relativo)
        if not os.path.exists(p):
            return False
        with open(p, encoding="utf-8", errors="replace") as f:
            testo = f.read().lower()
        return all(a.lower() in testo for a in aghi)

    esiti = {}
    esiti["A4-L02-01"] = contiene("03-AGENTI-E-RUOLI/regolatori/regolatore-copy.md",
                                  ["impersonare"])
    esiti["A4-L02-02"] = contiene("03-AGENTI-E-RUOLI/operatori/script-writer.md",
                                  ["fatti presi dalla sorgente"])
    esiti["A4-L02-03"] = os.path.exists(os.path.join(
        fabbrica, "04-SKILLS-E-REFERENCE", "references", "comandi-riscrittura.md"))
    esiti["A4-L02-04"] = contiene("03-AGENTI-E-RUOLI/capi/capo-ricerca.md",
                                  ["altra lingua"])
    return esiti
