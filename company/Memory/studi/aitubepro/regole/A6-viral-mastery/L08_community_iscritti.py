# -*- coding: utf-8 -*-
"""regole/A6-viral-mastery/L08_community_iscritti.py

Fonte: AI TUBE PRO / A6 Viral Mastery / L08 "Fai crescere la Community e gli iscritti" (10:34,
id e9e519a2-0a9f-4b79-ab21-6658b3db83f5, docente Pietro Gangemi).

Nessun bug da correggere qui: la scheda Community di YouTube (post-video, sondaggi,
cross-promotion, gestione commenti, Telegram) e' un intero canale di crescita che la fabbrica non
tocca mai. Quattro regole, tutte costruttive.
"""

FONTE = "AI TUBE PRO / A6 Viral Mastery / L08"
LEZIONE = "Fai crescere la Community e gli iscritti"

REGOLE = [
    {
        "id": "A6-L08-01",
        "tipo": "flusso",
        "regola": ("Ogni video pubblicato dovrebbe generare anche un post nella scheda "
                   "Community (non solo il video stesso): messaggio di richiamo, video "
                   "allegato, like proprio e un commento fissato che inviti a commentare. "
                   "YouTube distribuisce questi post anche a non iscritti interessati "
                   "all'argomento, non solo agli iscritti."),
        "prova": ("parlato @ 00:58-02:15 (dimostrazione pratica) e @ 02:50-03:00 (\"YouTube non "
                  "mostra questo contenuto solo alle persone che sono iscritte\"); schermo "
                  "frame-032.png @ 1:02 (selezione video), frame-096.png @ 3:10 (post "
                  "pubblicato con like e commento fissato)"),
        "fonte": "entrambi",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "basso",
        "misura": ("un video pubblicato dalla fabbrica genera anche un post Community "
                   "verificabile sul canale entro pochi minuti dalla pubblicazione"),
    },
    {
        "id": "A6-L08-02",
        "tipo": "agente",
        "regola": ("Manca un operatore che presidi i commenti (sui video e sulla scheda "
                   "Community) e risponda a TUTTI, non a campione, seguendo un copione fisso: "
                   "ringraziare sempre (anche ai commenti negativi, chiedendo il motivo), e ai "
                   "commenti positivi invitare esplicitamente a iscriversi e attivare la "
                   "campanella. E' la regola piu' ripetuta e piu' enfatica di tutta la lezione."),
        "prova": ("parlato @ 08:26-09:21 \"rispondere singolarmente ad ogni commento che "
                  "riceverete [...] che io faccio su tutti i canali [...] e' fondamentale che "
                  "risponderete a tutti i commenti\""),
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/operatori/comment-responder.md",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "medio",
        "misura": ("nuovo agente comment-responder documentato con il copione (ringrazia, "
                   "chiedi motivo se negativo, invita a iscriversi se positivo); nessuna "
                   "risposta generata liberamente senza il copione, per non danneggiare la "
                   "voce pubblica del canale (rischio reputazionale, non tecnico)"),
    },
    {
        "id": "A6-L08-03",
        "tipo": "funzione",
        "regola": ("Manca una funzione di cross-promotion via Community fra i canali propri "
                   "della fabbrica: un canale con piu' iscritti/views (es. una nicchia news) "
                   "puo' pubblicare un post che rimanda a un canale verticale correlato (es. "
                   "viaggi, cucina), invece di disperdersi aprendo troppe nicchie scollegate. "
                   "La fabbrica ha gia' una lista CANALI multi-canale su cui innestare questa "
                   "funzione."),
        "prova": ("parlato @ 05:12-06:42 \"noi abbiamo la possibilita' da un canale stesso di "
                  "farci pubblicita' su un altro canale [...] specializzarsi [...] in una "
                  "nicchia specifica\"; schermo frame-200.png @ 6:38, post reale \"Interessato/a "
                  "in cucine del mondo? Fate seguire questo canale\" con thumbnail di un video "
                  "di viaggio"),
        "fonte": "entrambi",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "basso",
        "misura": ("funzione nuova che, dato l'elenco CANALI, propone almeno un abbinamento "
                   "canale-sorgente/canale-destinazione per la cross-promotion"),
    },
    {
        "id": "A6-L08-04",
        "tipo": "strumento",
        "regola": ("Aprire un canale Telegram di notifica per ogni canale YouTube, linkato nel "
                   "primo commento dei video: bypassa il problema delle notifiche YouTube "
                   "disattivate di default e dà una spinta di visualizzazioni immediate a ogni "
                   "nuova pubblicazione."),
        "prova": "parlato @ 09:21-09:44",
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/youtube-pubblicazione.md",
        "azione": "costruisci",
        "binario": "A",
        "rischio": "basso",
        "misura": ("reference aggiornata con la procedura Telegram; non tocca il motore in "
                   "produzione, quindi binario A anche se lo strumento stesso (bot Telegram) "
                   "sara' costruito solo quando un canale reale lo richiede"),
    },
]
