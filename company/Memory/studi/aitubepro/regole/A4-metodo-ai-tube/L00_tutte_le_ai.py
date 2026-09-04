# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L00.

«A.I Artificial Intelligence Tutte le AI + aggiornamenti + Opportunity Business»
Relatore: Pietro Gangemi (non Mirko Delfino, che e' l'autore del corso) · 10:59.

Lezione di apertura: come sorvegliare il mercato degli strumenti AI senza affogarci.
Non porta parametri per il motore — porta un criterio di scelta e una disciplina di
sorveglianza, due cose che nella fabbrica non esistevano affatto.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L00"
LEZIONE = "A.I Artificial Intelligence Tutte le AI + aggiornamenti + Opportunity Business"

REGOLE = [
    {
        "id": "A4-L00-01",
        "tipo": "vincolo",
        "regola": ("Uno strumento entra in produzione solo se ha uno storico dimostrabile e fa "
                   "cio' che dichiara: si scelgono i 'verificati' e i 'popolari', mai il piu' "
                   "nuovo. La novita' non e' un merito."),
        "prova": "frame-0141.png @ 04:48",
        "fonte": "entrambi",
        "tocca": "04-SKILLS-E-REFERENCE/references/scelta-strumenti.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "basso",
        "misura": ("esiste una scheda che dice PERCHE' usiamo Fliki e Arena e con che criterio "
                   "si valuta un sostituto: oggi non esiste, verificato con grep"),
    },
    {
        "id": "A4-L00-02",
        "tipo": "procedura",
        "regola": ("La sorveglianza del mercato strumenti si fa a tempo chiuso e cadenza fissa "
                   "(15-20 minuti, una volta a settimana), mai 'finche' si vuole': senza un "
                   "tetto, i cataloghi inducono un loop infinito dichiarato dal relatore stesso."),
        "prova": "solo parlato @ 03:15",
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/supporto/self-improver.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "basso",
        "misura": ("self-improver ha un compito periodico di sorveglianza con un tetto di tempo "
                   "scritto; oggi non ne ha nessuno"),
    },
    {
        "id": "A4-L00-03",
        "tipo": "euristica",
        "regola": ("I cataloghi di strumenti si interrogano anche per NICCHIA e non solo per "
                   "strumento: cercare 'finanza', 'avatar', 'chat' fa emergere idee di canale, "
                   "non solo software. Sono una fonte per WF1, non solo per WF3."),
        "prova": "solo parlato @ 07:57",
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/operatori/niche-scout.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "basso",
        "misura": "niche-scout elenca i cataloghi AI fra le sue fonti di ricerca nicchia",
    },
]


def verifica(fabbrica):
    """Dice se la fabbrica rispetta gia' queste regole. Nessun effetto collaterale.

    `fabbrica` e' il percorso della cartella YOUTUBE-AUTOMATION-FACTORY.
    """
    import os

    esiti = {}

    scheda = os.path.join(fabbrica, "04-SKILLS-E-REFERENCE", "references", "scelta-strumenti.md")
    esiti["A4-L00-01"] = os.path.exists(scheda)

    def contiene(percorso_relativo, aghi):
        p = os.path.join(fabbrica, percorso_relativo)
        if not os.path.exists(p):
            return False
        with open(p, encoding="utf-8", errors="replace") as f:
            testo = f.read().lower()
        return all(a.lower() in testo for a in aghi)

    esiti["A4-L00-02"] = contiene("03-AGENTI-E-RUOLI/supporto/self-improver.md",
                                  ["sorveglianza", "minuti"])
    esiti["A4-L00-03"] = contiene("03-AGENTI-E-RUOLI/operatori/niche-scout.md",
                                  ["futuretools"])
    return esiti
