# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L07.

«Editing facile con Filmora» · ~43 min · 5.843 parole · profondita' BRONZO dichiarata.

Tutorial d'interfaccia di Wondershare Filmora dal primo minuto all'ultimo. La nostra fabbrica
genera via API e non apre mai un editor: **questa lezione non porta nessun metodo trasferibile**,
e il rapporto dello scagnozzo che l'ha letta integralmente lo dice in chiaro. Non si finge un
raccolto (piano §9).

Resta UNA cosa, e non e' un insegnamento: un'affermazione da segnare, la seconda di quattro
trovate nella stessa categoria sullo stesso errore.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L07"
LEZIONE = "Editing facile con Filmora"

REGOLE = [
    {
        "id": "A4-L07-01",
        "tipo": "vincolo",
        "regola": ("Filtri, overlay ed effetti applicati a un video altrui NON lo rendono "
                   "originale: rendono piu' difficile riconoscerlo. Irriconoscibilita' e "
                   "titolarita' sono due cose diverse, e chi le confonde costruisce un canale su "
                   "un equivoco. Secondo dei quattro miti del camuffamento."),
        "prova": "solo parlato @ 24:57 e @ 33:04 ('il video e' diventato un video originale e non e' piu' riconoscibile')",
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "alto",
        "misura": ("monetizzazione-compliance §5 raccoglie i quattro miti del camuffamento con la "
                   "confutazione di ciascuno; oggi la scheda non ne nominava nessuno"),
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

    return {
        "A4-L07-01": contiene("04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
                              ["miti del camuffamento", "riconoscibile"]),
    }
