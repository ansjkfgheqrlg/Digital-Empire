# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L09.

«18 Tecniche Avanzate del Metodo Copia e Incolla» · ~18 min · 3.167 parole · BRONZO dichiarata.

Tutorial di Adobe Premiere Pro applicato a clip scaricate da video altrui. Il titolo promette
18 tecniche, contandole se ne trovano 9-12. Per una fabbrica che genera via API e non parte mai
da materiale di terzi il valore didattico e' ZERO, e si dice invece di fingere un raccolto
(piano §9).

Resta UNA cosa, e non e' un insegnamento: il CATALOGO delle manovre di camuffamento, che serve a
riconoscerle quando arrivano. Due di esse — flip a specchio e distorsione — non hanno nessuna
funzione se non ingannare un sistema di riconoscimento, e sono il caso limite che rende visibile
l'errore comune ai sei miti del §5.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L09"
LEZIONE = "18 Tecniche Avanzate del Metodo Copia e Incolla"

REGOLE = [
    {
        "id": "A4-L09-01",
        "tipo": "vincolo",
        "regola": ("Le manovre di camuffamento su materiale altrui (zoom, color grading, green "
                   "screen, overlay e soprattutto flip a specchio e distorsione) sono ELUSIONE "
                   "del riconoscimento automatico, non lavorazione creativa: non entrano in "
                   "fabbrica. Una manovra che non migliora il video di un fotogramma e serve solo "
                   "a non farsi riconoscere dichiara da sola che c'e' qualcosa da riconoscere."),
        "prova": ("solo parlato @ 09:10-09:41 (flip orizzontale) e @ 09:53-10:17 (distorsione), "
                  "con la giustificazione dichiarata @ 03:05 ('evitare potenzialmente reclami')"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "alto",
        "misura": ("monetizzazione-compliance §6 elenca le dodici manovre col loro scopo reale e "
                   "marca le due di pura elusione; oggi la scheda raccoglieva le FRASI (§5) ma "
                   "non le MANOVRE, e chi ne vedesse proporre una non l'avrebbe riconosciuta"),
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
        "A4-L09-01": contiene("04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
                              ["manovre di camuffamento", "specchio", "elusione"]),
    }
