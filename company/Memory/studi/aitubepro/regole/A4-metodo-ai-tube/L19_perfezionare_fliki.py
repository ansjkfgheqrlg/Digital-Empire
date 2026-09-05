# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L19.

«Perfezionare un video con l'AI All In One» · ~11 min · 1.630 parole · profondita' ORO.

Approfondimento su FLIKI, il nostro strumento di produzione: i pannelli che L04 non aveva
toccato. E' la lezione col miglior rapporto valore/durata di tutto lo studio finora, e tre delle
quattro regole qui sotto nascono da una SCHERMATA, non dal parlato.

La piu' importante e' A4-L19-01: Fliki espone nel profilo un campo «YouTube channel ID(s)» il cui
scopo dichiarato e' prevenire i reclami di copyright sui contenuti generati. In tutta la fabbrica
non e' mai stato nominato: cercati channel id / channelid / whitelist / licenza fliki in
02-AUTOMAZIONI-E-SCRIPTS, 03-AGENTI-E-RUOLI e 04-SKILLS-E-REFERENCE il 2026-09-06 -> zero
occorrenze pertinenti. E' una casella da compilare a mano, gratuita, mai compilata.

La piu' istruttiva e' A4-L19-02: il docente dice che le pronunce «rimangono salvate su Fliki», il
pannello dice «to apply while generating audio FOR THIS VIDEO». Schermo batte parlato (piano
§6.4). Chiude una speranza aperta da L03 dichiarandola non percorribile — che e' un risultato,
non un fallimento.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L19"
LEZIONE = "Perfezionare un video con l'AI All In One"

REGOLE = [
    {
        "id": "A4-L19-01",
        "tipo": "procedura",
        "regola": ("Ogni canale che pubblica video generati con Fliki ha il proprio ID YouTube "
                   "registrato nel profilo Fliki (Profile -> YouTube channel ID(s)): serve a "
                   "opporre la licenza Fliki in caso di reclamo sulle clip e sulle musiche che "
                   "la piattaforma ci fornisce. Copre cio' che Fliki ci da', NON cio' che "
                   "carichiamo noi ne' materiale di terzi."),
        "prova": "frame-040.png @ 02:40 e frame-047.png @ 03:08 (il campo 'YouTube channel ID(s)' con due caselle e il pulsante Update)",
        "fonte": "schermo",
        "tocca": "04-SKILLS-E-REFERENCE/references/fliki-produzione.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "alto",
        "misura": ("fliki-produzione.md descrive il campo, come si trova l'ID del canale e cosa "
                   "copre davvero, e la compilazione per dosementale e legamidiamore e' "
                   "assegnata al gate A4; oggi in tutta la fabbrica il campo non e' mai nominato"),
    },
    {
        "id": "A4-L19-02",
        "tipo": "vincolo",
        "regola": ("La mappa delle pronunce di Fliki vale PER UN VIDEO SOLO: non e' una "
                   "configurazione di account, non si eredita fra progetti e una generazione via "
                   "API non la vede. Le pronunce si correggono nel TESTO dello script, con il "
                   "lessico, prima di generare. E' anche case-sensitive."),
        "prova": "frame-123.png @ 08:12 ('Manage pronunciation of words ... to apply while generating audio for this video' + 'This pronunciation map is case-sensitive')",
        "fonte": "schermo",
        "tocca": "04-SKILLS-E-REFERENCE/references/lessico-pronuncia.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "medio",
        "misura": ("lessico-pronuncia.md dichiara che la mappa di Fliki e' per-video e che percio' "
                   "la correzione si fa nel testo; oggi la scheda non dice perche' quella via non "
                   "e' percorribile, e qualcuno potrebbe riproporla"),
    },
    {
        "id": "A4-L19-03",
        "tipo": "parametro",
        "regola": ("Il volume della musica in Fliki e' una PERCENTUALE, e il riferimento visto a "
                   "schermo e' 10%. Conferma su prova la prescrizione che avevamo gia' in casa "
                   "('musica al 10-15%'), che fino a oggi era senza fonte."),
        "prova": "frame-088.png @ 05:52 (pannello Background music con lo slider 'Volume (10%)')",
        "fonte": "schermo",
        "tocca": "04-SKILLS-E-REFERENCE/references/fliki-avanzato.md",
        "azione": "conferma",
        "binario": "A",
        "rischio": "basso",
        "misura": ("fliki-avanzato.md porta la fonte del 10% accanto alla prescrizione; oggi il "
                   "numero c'e' ma non si sa da dove venga"),
    },
    {
        "id": "A4-L19-04",
        "tipo": "vincolo",
        "regola": ("I minuti del piano Fliki sono un plafond MENSILE, e il tetto non e' rigido: si "
                   "puo' chiedere un piano su misura all'assistenza. Il tetto dei minuti e' il "
                   "vincolo fisico della capacita' produttiva della fabbrica, e va trattato come "
                   "un numero negoziabile, non come una legge di natura."),
        "prova": "solo parlato @ 00:50 ('potete chiedere un piano aggiuntivo direttamente a Fliki ... ditegli quanti minuti vorreste e loro vi fanno un'offerta')",
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/fliki-produzione.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "basso",
        "misura": ("fliki-produzione.md dichiara che i minuti sono un plafond mensile e che il "
                   "piano e' negoziabile; oggi la capacita' produttiva non e' descritta da "
                   "nessuna parte"),
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

    FP = "04-SKILLS-E-REFERENCE/references/fliki-produzione.md"
    return {
        "A4-L19-01": contiene(FP, ["youtube channel id", "reclamo"]),
        "A4-L19-02": contiene("04-SKILLS-E-REFERENCE/references/lessico-pronuncia.md",
                              ["for this video"]),
        "A4-L19-03": contiene("04-SKILLS-E-REFERENCE/references/fliki-avanzato.md",
                              ["frame-088"]),
        "A4-L19-04": contiene(FP, ["plafond"]),
    }
