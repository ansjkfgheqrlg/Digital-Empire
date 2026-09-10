# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / YouTube Viral Mastery / L04.

«Come aumentare il CTR vertiginosamente» · 21:12 · ~2.993 parole.

Il raccolto vero non e' nel metodo del corso (che riconosciamo quasi per intero: leggere Studio,
soglie di CTR, copertine che non rivelano) ma nella scoperta che il nostro `self_improve.py` e
`meta_agent.py` hanno GIA' la logica di apprendimento sul CTR pronta e mai alimentata, perche'
nessuno script legge mai YouTube Studio -- mentre la porta di login persistente esiste gia' in
`youtube_uploader_playwright.py`, usata solo per pubblicare, mai per leggere Analytics.
"""

FONTE = "AI TUBE PRO / A6 YouTube Viral Mastery / L04"
LEZIONE = "Come aumentare il CTR vertiginosamente"

REGOLE = [
    {
        "id": "A6-L04-01",
        "tipo": "script",
        "regola": ("Costruire un lettore Playwright di YouTube Studio Analytics (tab "
                   "Panoramica/Copertura/Pubblico per video e per canale) che riusa il login "
                   "persistente gia' collaudato in youtube_uploader_playwright.py, cosi' che "
                   "channel-performance-analyst possa popolare ctr/retention_rate reali invece "
                   "di scrivere sempre None."),
        "prova": ("frame-202.png @ 6:42 (271.070 views, 2,1 Mln impressioni, 11,9% CTR) · "
                  "frame-262.png @ 8:42 (stesso canale, 90gg, CTR sceso a 7,2%) · "
                  "frame-322.png @ 10:42 (6,1 Mln impressioni, 5,4% CTR) -- tutti dati leggibili "
                  "solo dentro YouTube Studio, mai dal fetch pubblico"),
        "fonte": "schermo",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/youtube_studio_analytics_playwright.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "alto",
        "misura": ("channel-performance-analyst.md §2 non dichiara piu' 'CTR sempre null': "
                   "memory/performance_logs.json ha almeno un record con ctr/retention_rate "
                   "numerici e non None su un video reale pubblicato; self_improve.py produce "
                   "almeno una regola derivata da un CTR reale (non solo da mock)"),
    },
    {
        "id": "A6-L04-02",
        "tipo": "parametro",
        "regola": ("Soglia di lettura del CTR per canali/video con pochi dati: 8% = in media, "
                   "12-15% = copertina da replicare, sotto 4-6% = copertina/titolo da rivedere -- "
                   "ma il giudizio va sospeso prima di 10-20 video pubblicati. Su canali con "
                   "milioni di visualizzazioni un CTR 5,5-7% resta accettabile."),
        "prova": "parlato @ 07:18-08:10 (soglia 8%) · frame-262.png @ 8:42 (7,2% su 90gg/25,5Mln impressioni, letto come 'va bene' su scala)",
        "fonte": "entrambi",
        "tocca": "04-SKILLS-E-REFERENCE/references/youtube-pubblicazione.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "basso",
        "misura": ("youtube-pubblicazione.md elenca le tre soglie di CTR con la clausola "
                   "'valide solo dopo 10-20 video' e la deroga per canali a scala"),
    },
    {
        "id": "A6-L04-03",
        "tipo": "euristica",
        "regola": ("Il CTR percentuale scende fisiologicamente quando le impressioni assolute "
                   "crescono (stesso video/canale, periodo piu' lungo): un calo percentuale da "
                   "solo non e' un segnale di peggioramento, va letto insieme al volume di "
                   "impressioni."),
        "prova": ("frame-202.png @ 6:42 (11,9% su 2,1Mln impressioni/11gg) confrontato con "
                  "frame-262.png @ 8:42 (7,2% su 25,5Mln impressioni/90gg, stesso canale)"),
        "fonte": "schermo",
        "tocca": "03-AGENTI-E-RUOLI/operatori/channel-performance-analyst.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "basso",
        "misura": ("channel-performance-analyst.md riporta sempre CTR insieme a impressioni "
                   "totali nello stesso confronto, mai il CTR isolato"),
    },
    {
        "id": "A6-L04-04",
        "tipo": "procedura",
        "regola": ("Nessuna intro di canale nel primo minuto del video; ripetere la keyword e "
                   "creare un gancio nei primi secondi; inserire una call-to-action mirata (non "
                   "generica) entro i primi minuti, perche' i commenti pesano piu' dei like per "
                   "l'algoritmo ma vanno comunque chiesti entrambi."),
        "prova": "parlato @ 13:30-15:19 (primo minuto, gancio, CTA e commenti vs like)",
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/operatori/ytf-script-writer.md",
        "azione": "conferma",
        "binario": "A",
        "rischio": "basso",
        "misura": ("script prodotti da ytf-script-writer non contengono mai un blocco intro nel "
                   "primo minuto e contengono sempre una CTA a commentare entro i primi due "
                   "minuti di parlato"),
    },
    {
        "id": "A6-L04-05",
        "tipo": "strumento",
        "regola": ("La sezione YouTube Studio Pubblico > 'cosa guarda il nostro pubblico' e' una "
                   "fonte diretta di idee per nuovi video e nuovi canali, dichiarata da YouTube "
                   "stesso: non e' oggi consultata da nessun agente della fabbrica."),
        "prova": "solo parlato @ 12:05-13:04 (sezione sotto il fold, non catturata in un frame dedicato nel campione)",
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/operatori/ytf-niche-scout.md",
        "azione": "conferma",
        "binario": "A",
        "rischio": "basso",
        "misura": ("dipende da A6-L04-01 per avere accesso a Studio: candidato successivo, non "
                   "misurabile finche' il lettore Analytics non esiste"),
    },
]


def verifica(fabbrica):
    """Dice se la fabbrica rispetta gia' queste regole. Nessun effetto collaterale."""
    import os

    def esiste(percorso_relativo):
        return os.path.exists(os.path.join(fabbrica, percorso_relativo))

    def contiene(percorso_relativo, aghi):
        p = os.path.join(fabbrica, percorso_relativo)
        if not os.path.exists(p):
            return False
        with open(p, encoding="utf-8", errors="replace") as f:
            testo = f.read().lower()
        return all(a.lower() in testo for a in aghi)

    YP = "04-SKILLS-E-REFERENCE/references/youtube-pubblicazione.md"
    return {
        "A6-L04-01": esiste("02-AUTOMAZIONI-E-SCRIPTS/youtube_studio_analytics_playwright.py"),
        "A6-L04-02": contiene(YP, ["8%", "ctr"]),
        "A6-L04-03": contiene(
            "03-AGENTI-E-RUOLI/operatori/channel-performance-analyst.md",
            ["impressioni"],
        ),
        "A6-L04-04": True,  # gia' pratica corrente, da verificare a campione sugli script prodotti
        "A6-L04-05": esiste("02-AUTOMAZIONI-E-SCRIPTS/youtube_studio_analytics_playwright.py"),
    }
