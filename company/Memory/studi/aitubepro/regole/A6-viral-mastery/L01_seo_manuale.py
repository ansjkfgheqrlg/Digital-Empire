# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / YouTube Viral Mastery / L01.

«SEO YouTube manuale operativo» · 17:54 · ~2.477 parole.

Il raccolto migliore non viene dal metodo insegnato (che riconosciamo quasi per intero: keyword
research su YouTube nativo, vidIQ per leggere i competitor, riscrittura non copia, ChatGPT per
titolo/descrizione) ma dal confronto fra una frase della lezione ("i sottotitoli sono indicizzati
da YouTube") e il nostro `seo_score.py`, che pesa esattamente quello — 15/100 punti — leggendo un
campo che il nostro orchestratore scrive sempre `True` senza mai verificarlo.
"""

FONTE = "AI TUBE PRO / A6 YouTube Viral Mastery / L01"
LEZIONE = "SEO YouTube manuale operativo"

REGOLE = [
    {
        "id": "A6-L01-01",
        "tipo": "vincolo",
        "regola": ("`seo_score.py` pesa 'subtitles' 15/100 punti definendoli 'indicizzati da "
                   "YouTube' (traccia CC nativa, non il karaoke bruciato di Fliki — gia' "
                   "trovato assente come automazione in A6-L00-01). `apex7_orchestrator.py:1515` "
                   "scrive 'subtitles': True SEMPRE, senza verifica: ogni video riceve 15 punti "
                   "fissi su un elemento mai creato, e questo sposta pass_soglia_70 su video "
                   "borderline. Va reso condizionale (False finche' non esiste una vera "
                   "automazione dei sottotitoli nativi) o rimosso dal punteggio finche' non lo "
                   "e'."),
        "prova": "solo parlato @ 17:07-17:18 (il pannello punteggio del wizard, citato ma non fotografato) + verifica sul codice: seo_score.py:26-31 e apex7_orchestrator.py:1515",
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py",
        "azione": "modifica",
        "binario": "B",
        "rischio": "alto",
        "misura": ("apex7_orchestrator.py non scrive piu' 'subtitles': True incondizionato; "
                   "seo_score.py continua a passare 62/65+ regole a norma, ma i punteggi SEO "
                   "storici vanno riletti sapendo che erano gonfiati di 15 punti fissi"),
    },
    {
        "id": "A6-L01-02",
        "tipo": "parametro",
        "regola": ("Aggiorna A6-L00-02: la raccomandazione citata dal corso come 'consigliata da "
                   "YouTube stesso' e' ALMENO DUE playlist per video, non una generica. Non "
                   "sostituisce A6-L00-02 (stesso gap, playlist mai assegnata), lo precisa con "
                   "un numero."),
        "prova": "solo parlato @ 13:18-13:23 ('almeno due playlist, e' consigliato da parte di youtube') + frame-407.png @ 13:32 (due playlist selezionate nel pannello)",
        "fonte": "entrambi",
        "tocca": "04-SKILLS-E-REFERENCE/references/youtube-pubblicazione.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "basso",
        "misura": "youtube-pubblicazione.md cita il numero 'almeno due' invece di 'una playlist' generica",
    },
    {
        "id": "A6-L01-03",
        "tipo": "vincolo",
        "regola": ("I tag dovrebbero includere il nome del canale (chi cerca il canale per nome "
                   "trova tutti i video). Verificato ASSENTE nel nostro codice: tag_candidates "
                   "(apex7_orchestrator.py righe 1494-1495) somma high_performing_tags + "
                   "tag_tema + idea_tokens + keyword — mai il nome del canale."),
        "prova": "solo parlato @ 16:32-17:04 (spiega il motivo) — riscontrato falso/assente dal codice reale, non da un frame",
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py",
        "azione": "nuovo",
        "binario": "B",
        "rischio": "basso",
        "misura": ("tag_candidates include il nome del canale (dosementale/legamidiamore o un "
                   "nome pubblico, da decidere a gate) fra le fonti sommate"),
    },
    {
        "id": "A6-L01-04",
        "tipo": "strumento",
        "regola": ("vidIQ (mistrascritto 'BDQ' dal parlato) è lo strumento reale usato dal corso "
                   "per leggere punteggio SEO e tag dei video competitor via overlay browser. "
                   "Non è nel nostro catalogo strumenti (A4-L00-01): candidato da valutare con "
                   "le 5 domande del criterio (storico, piano B, costo, CLI, licenza)."),
        "prova": "frame-057.png @ 1:52 (overlay vidIQ con punteggio) e frame-071.png @ 2:20 (tag suggeriti)",
        "fonte": "schermo",
        "tocca": "04-SKILLS-E-REFERENCE/references/scelta-strumenti.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "basso",
        "misura": "scelta-strumenti.md elenca vidIQ come candidato non ancora valutato, non ancora adottato",
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
    ST = "04-SKILLS-E-REFERENCE/references/scelta-strumenti.md"
    return {
        # binario B: non applicate al motore oggi, per costruzione false finche' il gate A6
        # non le applica davvero (ADR-024) — dichiarato qui, non nascosto in un True comodo.
        "A6-L01-01": False,
        "A6-L01-02": contiene(YP, ["almeno due playlist"]),
        "A6-L01-03": False,
        "A6-L01-04": contiene(ST, ["vidiq"]),
    }
