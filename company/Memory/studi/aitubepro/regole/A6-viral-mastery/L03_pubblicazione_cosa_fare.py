# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / YouTube Viral Mastery / L03.

«Pubblicazione Video + cosa da fare» · 4:04 · ~510 parole.

Lezione breve ma con un buco diverso da quello gia' a registro (A6-RC-01, che riguarda i tab
del wizard): qui il video E' GIA' pubblico, e il docente mostra quattro azioni immediate di
engagement (like, commento pinnato, like al commento, condivisione social) che il nostro
uploader non fa mai -- si ferma alla pubblicazione, non tocca mai la pagina pubblica dopo.
"""

FONTE = "AI TUBE PRO / A6 YouTube Viral Mastery / L03"
LEZIONE = "Pubblicazione Video + cosa da fare"

REGOLE = [
    {
        "id": "A6-L03-01",
        "tipo": "funzione",
        "regola": ("Aggiungere un passo post-pubblicazione all'uploader: mettere like al video "
                   "appena pubblicato, pubblicare e mettere in evidenza (pin) un commento con "
                   "una call-to-action a rispondere (calibrata sul tono del contenuto), mettere "
                   "like al proprio commento. Leva gratuita, nessun costo di crediti."),
        "prova": ("frame-045.png @ 1:28 (like attivo sulla pagina pubblica) · frame-080.png @ "
                  "2:38 (commento pinnato pubblicato, con metriche del video a fianco) · "
                  "parlato @ 01:24-02:37"),
        "fonte": "entrambi",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "medio",
        "misura": ("grep su youtube_uploader_playwright.py trova una funzione dedicata "
                   "(es. _azioni_post_pubblicazione, sul modello di ads_on_after_upload); un "
                   "video pubblicato dopo l'applicazione ha un like proprio e un commento "
                   "pinnato verificabili sulla pagina pubblica"),
    },
    {
        "id": "A6-L03-02",
        "tipo": "funzione",
        "regola": ("Aggiungere alla manutenzione periodica del canale (non per-video) "
                   "l'aggiornamento del trailer canale (per i non iscritti) e del video in "
                   "primo piano per gli iscritti, dopo ogni pubblicazione rilevante."),
        "prova": "frame-098.png @ 3:14 (modale scelta video specifico nel pannello Personalizzazione) · frame-106.png @ 3:30 (homepage canale con video in evidenza) · parlato @ 02:57-03:26",
        "fonte": "entrambi",
        "tocca": "03-AGENTI-E-RUOLI/operatori/ytl-channel-architect.md",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "basso",
        "misura": ("ytl-channel-architect.md include un passo periodico (non per ogni video) "
                   "di revisione trailer/video in primo piano; verificabile a schermo come in "
                   "frame-106.png su un canale reale della fabbrica"),
    },
    {
        "id": "A6-L03-03",
        "tipo": "procedura",
        "regola": ("Conferma: assegnare almeno due playlist a ogni video prima della "
                   "pubblicazione, coerente con la regola gia' registrata A6-L01-02."),
        "prova": "frame-025.png @ 0:48 (tab Elementi video, sezione Playlist con 2 playlist assegnate)",
        "fonte": "schermo",
        "tocca": "04-SKILLS-E-REFERENCE/references/youtube-pubblicazione.md",
        "azione": "conferma",
        "binario": "A",
        "rischio": "basso",
        "misura": ("nessuna nuova azione: rafforza A6-L01-02 con un secondo frame di prova "
                   "indipendente"),
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

    YP = "04-SKILLS-E-REFERENCE/references/youtube-pubblicazione.md"
    return {
        "A6-L03-01": contiene(
            "02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py",
            ["pin", "commento"],
        ),
        "A6-L03-02": contiene(
            "03-AGENTI-E-RUOLI/operatori/ytl-channel-architect.md",
            ["trailer"],
        ),
        "A6-L03-03": contiene(YP, ["playlist"]),
    }
