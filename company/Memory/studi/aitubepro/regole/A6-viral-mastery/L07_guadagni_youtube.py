# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / YouTube Viral Mastery / L07.

«Come Aumentare i GUADAGNI su YouTube» · 14:34 · ~2.017 parole.

Il raccolto vero e' duplice: (1) la soglia "8 minuti per i mid-roll" del corso coincide
esattamente con regolatori.py:270 DURATA_MINIMA_S = 480, chiudendo con un numero motivato
l'ambiguita' segnalata dal piano di studio fra questa soglia e il target 12 minuti di
apex7_orchestrator.py; (2) la Tesoreria ha gia' "youtube" come motore valido ma nessun ricavo
YouTube reale e' mai stato registrato -- lo stesso accesso Studio richiesto da A6-L04 (CTR)
serve anche per leggere le entrate.
"""

FONTE = "AI TUBE PRO / A6 YouTube Viral Mastery / L07"
LEZIONE = "Come Aumentare i GUADAGNI su YouTube"

REGOLE = [
    {
        "id": "A6-L07-01",
        "tipo": "script",
        "regola": ("Costruire un pull delle 'Entrate stimate' da YouTube Studio (tab "
                   "Panoramica video e canale) verso scripts/tesoreria.py, usando il motore "
                   "'youtube' gia' presente nel ledger (tesoreria.py:57) ma mai popolato da un "
                   "ricavo reale. Condivide l'accesso Studio con A6-L04-01."),
        "prova": ("frame-346.png @ 11:30 (canale con campo email business, contesto ricavi da "
                  "collaborazione) · parlato @ 00:40-01:07 (YouTube paga in base alla "
                  "pubblicita' nel video) -- entrambi mostrano dati di guadagno leggibili solo "
                  "da dentro YouTube Studio, mai dal fetch pubblico"),
        "fonte": "entrambi",
        "tocca": "scripts/tesoreria.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "alto",
        "misura": ("scripts/tesoreria.py ha almeno una voce con motore='youtube' e importo "
                   "diverso da zero derivata da un pull reale, non inserita a mano; "
                   "tesoreria-entrate puo' rispondere 'quanto ha reso YouTube questo mese' con "
                   "un numero vero"),
    },
    {
        "id": "A6-L07-02",
        "tipo": "vincolo",
        "regola": ("La soglia di durata 480s (8 minuti) in regolatori.py e' confermata come il "
                   "minimo tecnico reale per sbloccare le interruzioni pubblicitarie (mid-roll): "
                   "non va alzata al target di apex7_orchestrator.py (12 minuti), che serve la "
                   "retention/algoritmo, non la monetizzazione. Le due soglie sono compatibili, "
                   "non in conflitto."),
        "prova": "parlato @ 00:52-01:07 ('nei video che durano meno di 8 minuti non abbiamo la possibilita' di inserire altri annunci') · frame-057.png @ 1:52 (pannello Interruzioni pubblicitarie attivo su video di 14 minuti)",
        "fonte": "entrambi",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/regolatori.py",
        "azione": "conferma",
        "binario": "B",
        "rischio": "basso",
        "misura": ("nessuna modifica al valore di DURATA_MINIMA_S; la nota nel piano di studio "
                   "§2 sull'incoerenza fra le due soglie viene chiusa in CONFLITTI.md come "
                   "'non e' un conflitto'"),
    },
    {
        "id": "A6-L07-03",
        "tipo": "funzione",
        "regola": ("Aggiungere il campo email business nel checklist di lancio canale (sezione "
                   "Informazioni di base), oggi assente in tutti gli agenti di setup canale: e' "
                   "il canale che genera proposte di collaborazione/sponsorizzazione."),
        "prova": "frame-346.png @ 11:30 (tab Informazioni canale con campo email visualizzabile) · parlato @ 10:43-11:55",
        "fonte": "entrambi",
        "tocca": "03-AGENTI-E-RUOLI/operatori/ytl-channel-architect.md",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "medio",
        "misura": ("ogni canale lanciato da ytl-channel-architect ha il campo email business "
                   "compilato nella sezione Informazioni di base, verificabile a schermo come "
                   "in frame-346.png"),
    },
    {
        "id": "A6-L07-04",
        "tipo": "flusso",
        "regola": ("Il posizionamento delle interruzioni pubblicitarie mid-roll non e' mai "
                   "configurato dal nostro uploader: ads_on_after_upload() attiva solo "
                   "l'interruttore generale ads on/off, mai il pannello 'Interruzioni "
                   "pubblicitarie'. Valutare se automatizzare una cadenza (es. ogni 2 minuti) "
                   "per i video sopra 480s."),
        "prova": "frame-057.png @ 1:52 (pannello mai toccato dal nostro codice) · parlato @ 03:11-04:18 (strategia ogni 2 minuti, anche per intercettare chi salta avanti nel video)",
        "fonte": "entrambi",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py",
        "azione": "ridisegna",
        "binario": "B",
        "rischio": "medio",
        "misura": ("grep su youtube_uploader_playwright.py trova una funzione dedicata al "
                   "mid-roll (sul modello di _gestisci_step_monetization); un video di prova "
                   "sopra 480s pubblicato dopo l'applicazione ha interruzioni pubblicitarie "
                   "verificabili nel pannello Monetizzazione"),
    },
    {
        "id": "A6-L07-05",
        "tipo": "euristica",
        "regola": ("Gli Shorts monetizzano pochissimo salvo scala enorme (centinaia di milioni "
                   "di view): non deviare risorse di produzione dal formato lungo gia' scelto "
                   "dalla fabbrica per inseguire gli Shorts."),
        "prova": "solo parlato @ 04:47-05:07 (non ripreso in un frame dedicato nel campione, la tab Guadagna resta ferma per tutto il segmento)",
        "fonte": "parlato",
        "tocca": "-",
        "azione": "conferma",
        "binario": "A",
        "rischio": "basso",
        "misura": ("nessuna, e' una conferma della scelta di formato gia' presa: nessun cambio "
                   "misurabile atteso"),
    },
    {
        "id": "A6-L07-06",
        "tipo": "funzione",
        "regola": ("Le affiliazioni in descrizione/commento fissato sono una fonte di ricavo "
                   "indipendente dalle view pubblicitarie: oggi nessuno slot esiste nella "
                   "generazione automatica della descrizione."),
        "prova": "frame-402.png @ 13:22 (video con link Ledger in descrizione, 227k+ views) · frame-412.png @ 13:42 (destinazione del link) · parlato @ 13:32-13:53",
        "fonte": "entrambi",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "medio",
        "misura": ("apex7_orchestrator.py genera un campo description con uno slot opzionale "
                   "per link di affiliazione, popolato solo quando la nicchia ha un programma "
                   "attivo configurato; almeno un video pubblicato con link di affiliazione "
                   "tracciabile in tesoreria (dipende da A6-L07-01 per la registrazione ricavi)"),
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

    return {
        "A6-L07-01": contiene("scripts/tesoreria.py", ["youtube"]) and False,  # motore esiste, pull no: verificare a mano finche' A6-L04-01 non esiste
        "A6-L07-02": contiene("02-AUTOMAZIONI-E-SCRIPTS/regolatori.py", ["480"]),
        "A6-L07-03": contiene(
            "03-AGENTI-E-RUOLI/operatori/ytl-channel-architect.md", ["email"]
        ),
        "A6-L07-04": contiene(
            "02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py",
            ["midroll", "mid-roll", "interruzione pubblicitaria"],
        ),
        "A6-L07-05": True,  # conferma, nessun file bersaglio da verificare
        "A6-L07-06": contiene(
            "02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py", ["affiliat"]
        ),
    }
