# -*- coding: utf-8 -*-
"""Regole COSTRUTTIVE del ripasso all'indietro — categoria A6, 2026-09-10.

Stessa origine e stessa ragione del file gemello in A4-metodo-ai-tube/: le due lezioni A6
gia' chiuse (L00 caricamento video, L01 SEO manuale) erano state lette col contratto
vecchio, che ammetteva una sola domanda — «quale documento cambio?».

Le otto lezioni A6 ancora da leggere partiranno direttamente col contratto nuovo: per loro
non ci sara' debito da ripassare.

Origine integrale: ../../ripasso-costruttivo/_blocco-3-fliki-A6-trasversali.md
"""

FONTE = "AI TUBE PRO / A6 Viral Mastery / ripasso costruttivo 2026-09-10"
LEZIONE = "ripasso all'indietro di A6/L00 e A6/L01 con le quattro domande costruttive"

REGOLE = [
    {
        "id": "A6-RC-01",
        "tipo": "flusso",
        "regola": ("La pubblicazione deve comprendere il tab «Elementi video» e l'assegnazione a "
                   "playlist, oggi saltati per intero: sottotitoli nativi, schermata finale, "
                   "schede e playlist non vengono mai toccati. Sono leve gratuite, e la playlist "
                   "e' raccomandata da YouTube stesso secondo la lezione."),
        "prova": ("A6/L01/appunti.md @ 13:18-13:23 «inserire il video in almeno due playlist, e' "
                  "consigliato da parte di YouTube», con due playlist selezionate nel wizard "
                  "(frame-407.png @ 13:32); A6/L00 @ 09:00 «faccio fine, e in automatico youtube "
                  "adesso trascrive tutto». Riverificato 2026-09-10 con grep su "
                  "youtube_uploader_playwright.py: zero occorrenze di playlist, scheda, card, "
                  "endscreen, subtitle, caption"),
        "fonte": "entrambi",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py",
        "azione": "ridisegna",
        "binario": "B",
        "rischio": "medio",
        "misura": ("l'uploader ha una funzione dedicata sul modello di "
                   "_gestisci_step_monetization gia' esistente, e un video pubblicato dopo "
                   "l'applicazione ha almeno 2 playlist verificabili e una traccia CC nativa "
                   "attiva"),
    },
    {
        "id": "A6-RC-02",
        "tipo": "funzione",
        "regola": ("Il punteggio SEO deve dire il vero sui sottotitoli: la voce vale 15 punti su "
                   "100 e viene dichiarata sempre presente, per un elemento che non abbiamo mai "
                   "creato. Finche' i sottotitoli nativi non vengono davvero generati, la "
                   "funzione deve restituire False — l'onesta' del punteggio viene prima della "
                   "comodita' di non toccare il numero."),
        "prova": ("A6/L01/appunti.md — apex7_orchestrator.py:1515 scrive «\"subtitles\": True» "
                  "incondizionatamente, a fianco di «\"thumbnail\": not skip_thumbnail» che "
                  "invece e' condizionale; seo_score.py:30 «\"subtitles\": 15, # presenti = "
                  "indicizzati da YouTube». Riverificato 2026-09-10: il difetto e' ancora aperto"),
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "alto",
        "misura": ("grep su apex7_orchestrator.py non trova piu' «\"subtitles\": True» "
                   "incondizionato; un video senza sottotitoli nativi riceve 0/15 su quella voce, "
                   "uno con sottotitoli reali riceve 15/15. Dipende da A6-RC-01 per poter valere "
                   "True in qualche caso"),
    },
]
