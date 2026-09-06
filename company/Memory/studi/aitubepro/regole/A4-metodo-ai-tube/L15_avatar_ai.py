# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L15.

«Crea il tuo AVATAR con A.I» · ~14 min · profondita' BRONZO dichiarata.

Tutorial d'interfaccia di uno strumento di avatar parlanti (nel parlato «studio di ID»,
verosimilmente D-ID Studio): diciassette passaggi, tutti dentro un browser, mai un endpoint.
Del metodo non si prende nulla.

Si prende la CONDOTTA, e non perche' usiamo avatar: perche' la lezione mostra due manovre come
esercizi tecnici normali — un deepfake di una persona reale con una finta notizia di lutto, e un
personaggio protetto generato e fatto parlare — senza una parola di avvertimento. E' la stessa
struttura d'errore dei sei miti del camuffamento, spostata dal video riusato al contenuto
generato: la' si credeva che modificare creasse un diritto, qui si crede che generare lo crei.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L15"
LEZIONE = "Crea il tuo AVATAR con A.I"

REGOLE = [
    {
        "id": "A4-L15-01",
        "tipo": "vincolo",
        "regola": ("La fabbrica non genera volto, voce o sembianze riconoscibili di una PERSONA "
                   "REALE — nota o sconosciuta, viva o morta — e non le attribuisce dichiarazioni "
                   "che non ha fatto. Non e' diritto d'autore: e' diritto all'immagine e identita' "
                   "personale, e non si estingue perche' l'immagine e' sintetica. L'unica "
                   "eccezione sarebbe il consenso scritto della persona, che per una fabbrica che "
                   "pubblica in automatico vuol dire mai."),
        "prova": ("solo parlato @ 11:36-11:48 (l'avatar legge una finta notizia di lutto su un "
                  "cantante italiano reale, poi: 'abbiamo dato anche un volto all'intelligenza "
                  "artificiale'), senza una parola su consenso o diritto all'immagine"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "alto",
        "misura": ("monetizzazione-compliance §8.1 vieta il volto e la voce di persone reali e "
                   "nomina il caso peggiore (notizia falsa attribuita a persona vera); oggi la "
                   "scheda copriva solo il materiale altrui RIUSATO, non quello GENERATO"),
    },
    {
        "id": "A4-L15-02",
        "tipo": "vincolo",
        "regola": ("Un personaggio protetto generato da un modello resta di chi e': non "
                   "generiamo, non pubblichiamo e non mettiamo in miniatura personaggi, "
                   "mascotte, loghi o stili identificabili di terzi. Il metro: se un umano "
                   "guardando l'immagine sa dire di chi e' il personaggio, quel diritto e' di "
                   "qualcun altro, e averlo generato una macchina non cambia nulla."),
        "prova": ("solo parlato @ 09:08-09:21 (prompt 'qualcosa che ha a che fare con Dragon "
                  "Ball ... e Goku') e @ 10:03-10:52 (il ritratto generato parla: 'sono un "
                  "personaggio di Dragon Ball'), senza alcuna menzione del copyright"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "alto",
        "misura": ("monetizzazione-compliance §8.2 dichiara che la generazione non trasferisce "
                   "diritti sui personaggi protetti e da' il metro della riconoscibilita'; oggi "
                   "nessun documento diceva cosa NON si puo' chiedere a un modello generativo"),
    },
    {
        "id": "A4-L15-03",
        "tipo": "strumento",
        "regola": ("Gli strumenti di avatar parlante mostrati nel corso si comandano SOLO a "
                   "click: nessun endpoint, nessuna chiave, nessun payload in quattordici minuti "
                   "di dimostrazione. Non sono adottabili dalla nostra catena — e' il caso piu' "
                   "netto della domanda 4 del criterio di scelta. I prezzi restano come metro di "
                   "mercato, mai come istruzione operativa."),
        "prova": ("solo parlato @ 02:25-08:20 (i diciassette passaggi, tutti nel browser) e "
                  "@ 12:44-13:09 (piani: 5 $/mese per 10 minuti, intermedio 'un'ora', Enterprise)"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/scelta-strumenti.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "basso",
        "misura": ("scelta-strumenti.md porta il caso degli avatar parlanti come esempio della "
                   "domanda 4, col metro di mercato dei prezzi; oggi la domanda 4 era una regola "
                   "senza un caso che la rendesse concreta"),
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

    MC = "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md"
    return {
        "A4-L15-01": contiene(MC, ["persona reale", "diritto all'immagine"]),
        "A4-L15-02": contiene(MC, ["personaggi protetti", "toei"]),
        "A4-L15-03": contiene("04-SKILLS-E-REFERENCE/references/scelta-strumenti.md",
                              ["avatar parlanti", "domanda 4"]),
    }
