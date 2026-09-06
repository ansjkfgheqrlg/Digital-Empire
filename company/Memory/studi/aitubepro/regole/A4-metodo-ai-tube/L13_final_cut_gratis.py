# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L13.

«Come avere Final Cut Pro X Gratis per Sempre» · ~8 min · 1.368 parole · BRONZO dichiarata.

Meta' lezione legittima (la prova ufficiale Apple di 90 giorni), meta' aggiramento: una stringa
da Terminale che azzera il contatore della prova, ripetibile all'infinito. Manomissione del
meccanismo di licenza di un software da 350 EUR, contro EULA.

Non usiamo Final Cut e non lo useremo mai. La regola che ne nasce non riguarda quel software:
riguarda il BUCO che la lezione ha reso visibile — il criterio di scelta degli strumenti faceva
quattro domande e nessuna era «con che titolo lo stiamo usando».
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L13"
LEZIONE = "Come avere Final Cut Pro X Gratis per Sempre"

REGOLE = [
    {
        "id": "A4-L13-01",
        "tipo": "vincolo",
        "regola": ("Uno strumento entra in produzione solo per la porta d'ingresso: licenza "
                   "pagata, piano gratuito dichiarato dal fornitore, o prova ufficiale entro la "
                   "sua durata. Mai per aggiramento del meccanismo di licenza (reset del "
                   "contatore, crack, chiave condivisa) — nemmeno per una prova. E' la quinta "
                   "domanda del criterio di scelta, che prima non c'era."),
        "prova": ("solo parlato @ 05:31 ('riazzerare questi 78 giorni ... avere per sempre attivo "
                  "Final Cut Pro') e @ 08:01 ('non so quanto durera' questo metodo')"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/scelta-strumenti.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "alto",
        "misura": ("scelta-strumenti.md porta cinque domande invece di quattro e la quinta e' il "
                   "titolo d'uso, con le tre risposte ammesse e il caso EULA per esteso; oggi il "
                   "criterio non nominava la licenza in nessun punto"),
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
        "A4-L13-01": contiene("04-SKILLS-E-REFERENCE/references/scelta-strumenti.md",
                              ["vaglio della licenza", "eula", "con che titolo"]),
    }
