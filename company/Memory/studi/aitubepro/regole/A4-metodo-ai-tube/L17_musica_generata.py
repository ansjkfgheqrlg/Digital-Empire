# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L17.

«Componi Musica Originale Con AI in pochi click» · ~14 min · profondita' BRONZO dichiarata.

Dimostrazione di AIVA. E' la lezione mandata a leggere con una domanda precisa: dopo L16, che
proponeva la via sporca (separare voce e base da brani altrui), esiste una via per avere musica
con diritti puliti? La risposta c'e', ed e' condizionata al piano che si paga.

Il merito della lezione: dice che i diritti dipendono dall'abbonamento (free = nessun diritto,
Standard = solo quattro piattaforme, Pro = proprieta'). Il suo difetto: lo dice DOPO aver
promesso in apertura la proprieta' piena senza condizioni — contraddizione interna alla stessa
lezione, arbitrata in C-007.

Il buco che nessuno copre: Content ID non e' mai nominato. Un contratto col fornitore dice cosa
hai il diritto di fare; non impedisce a un sistema automatico di segnalarti.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L17"
LEZIONE = "Componi Musica Originale Con AI in pochi click"

REGOLE = [
    {
        "id": "A4-L17-01",
        "tipo": "vincolo",
        "regola": ("La musica dei nostri video puo' venire da tre vie e una e' chiusa: (1) quella "
                   "fornita da Fliki, coperta dalla sua licenza — ed e' la via che abbiamo gia' "
                   "in casa; (2) musica generata da AI, percorribile solo se il piano pagato "
                   "dichiara i diritti d'uso e senza brani altrui come riferimento; (3) voce e "
                   "base separate da brani altrui, vietata. Il titolo d'uso si verifica SUI "
                   "TERMINI DEL FORNITORE, mai su una lezione o su un video."),
        "prova": ("solo parlato @ 08:50 (free: 'non abbiamo i diritti'), @ 08:57 (Standard: "
                  "'solamente su YouTube, Twitch, TikTok e Instagram'), @ 09:16 (Pro: 'siamo noi "
                  "i proprietari'), contro l'apertura @ 00:46-01:03 che prometteva proprieta' "
                  "piena senza condizioni"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "alto",
        "misura": ("monetizzazione-compliance §9 elenca le tre vie con lo stato di ciascuna e "
                   "dichiara che il titolo si legge sui termini del fornitore; oggi la fabbrica "
                   "non aveva UNA riga su da dove possa venire la musica, pur avendo un criterio "
                   "di qualita' sul suo volume"),
    },
    {
        "id": "A4-L17-02",
        "tipo": "vincolo",
        "regola": ("Non si carica un brano altrui come riferimento di stile in uno strumento "
                   "generativo: il materiale in ingresso torna a essere di terzi, ed e' lo stesso "
                   "schema della porta chiusa sulla separazione audio. La musica si genera da "
                   "zero — genere, umore, durata — e nessun file di riferimento che non sia "
                   "nostro."),
        "prova": ("solo parlato @ 11:03-11:23 (carica in 'Influencers' 'una canzone abbastanza "
                  "conosciuta e abbastanza famosa' per generarne una simile, senza una parola "
                  "sulla licenza o sul rischio di somiglianza)"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "alto",
        "misura": ("monetizzazione-compliance §9 pone la seconda condizione (nessun brano altrui "
                   "come riferimento) e la lega allo schema del §7; oggi nulla vietava di "
                   "alimentare un generatore con materiale di terzi"),
    },
    {
        "id": "A4-L17-03",
        "tipo": "strumento",
        "regola": ("Quando serve una capacita' nuova (un volto, una musica, una voce) la prima "
                   "domanda non e' 'qual e' il migliore' ma 'quale si comanda da programma': in "
                   "una fabbrica che produce a nastro uno strumento migliore ma solo a click e' "
                   "uno strumento peggiore, perche' il suo costo vero non e' l'abbonamento ma il "
                   "tempo umano che reintroduce su ogni video."),
        "prova": ("solo parlato @ 01:38-13:30 (ventisei passaggi tutti a click: account, genere, "
                  "nota, durata, varianti, editor, download; mai un endpoint, una chiave o un "
                  "formato di richiesta in quattordici minuti)"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/scelta-strumenti.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "basso",
        "misura": ("scelta-strumenti.md porta il caso della musica accanto a quello degli avatar "
                   "e ne ricava la domanda da fare per prima; oggi la domanda 4 c'era ma non "
                   "aveva la sua conseguenza scritta"),
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
        "A4-L17-01": contiene(MC, ["da dove", "musica dei nostri video", "termini del fornitore"]),
        "A4-L17-02": contiene(MC, ["riferimento di stile", "influencers"]),
        "A4-L17-03": contiene("04-SKILLS-E-REFERENCE/references/scelta-strumenti.md",
                              ["si comanda da", "aiva"]),
    }
