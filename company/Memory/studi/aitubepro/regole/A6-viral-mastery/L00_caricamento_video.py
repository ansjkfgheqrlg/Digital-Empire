# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / YouTube Viral Mastery / L00.

«Caricamento video su YouTube» · 12:05 · ~1.801 parole.

Il wizard di pubblicazione Studio per intero, confrontato riga per riga col nostro
`youtube_uploader_playwright.py`. Il rischio maggiore trovato non era nella lezione: era in un
primo controllo mio, un grep in una sola lingua che ha dichiarato assente un passo (il
questionario di autocertificazione) che invece e' gia' automatizzato, in inglese. Corretto prima
di essere scritto nel report finale.
"""

FONTE = "AI TUBE PRO / A6 YouTube Viral Mastery / L00"
LEZIONE = "Caricamento video su YouTube"

REGOLE = [
    {
        "id": "A6-L00-01",
        "tipo": "vincolo",
        "regola": ("Tre elementi del wizard di pubblicazione non hanno MAI automazione nel "
                   "nostro uploader: sottotitoli nativi (traccia CC, distinta dal karaoke "
                   "bruciato di Fliki), schermata finale, schede (video/playlist/canale/link). "
                   "Verificato assente in italiano e in inglese, non solo per una stringa "
                   "mancata."),
        "prova": "frame-264.png @ 8:46 (sottotitoli) · frame-280.png @ 9:18 (schermata finale) · frame-285.png @ 9:28 (schede)",
        "fonte": "entrambi",
        "tocca": "04-SKILLS-E-REFERENCE/references/youtube-pubblicazione.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "medio",
        "misura": ("youtube-pubblicazione.md elenca i tre elementi come leve di crescita non "
                   "ancora sfruttate, con priorita' da assegnare a fine categoria A6 (dopo L04 "
                   "CTR e L08 community, che dicono se vale la pena costruirli)"),
    },
    {
        "id": "A6-L00-02",
        "tipo": "vincolo",
        "regola": ("Nessun video prodotto viene mai assegnato a una playlist. Le playlist "
                   "raggruppano sessioni di visione (un video finito porta al successivo dello "
                   "stesso argomento) e YouTube le premia in watch-time complessivo del canale: "
                   "vanno create/gestite una volta per canale, non ripetute per ogni video."),
        "prova": "frame-305.png @ 10:08 (modale creazione playlist nel wizard)",
        "fonte": "schermo",
        "tocca": "04-SKILLS-E-REFERENCE/references/youtube-pubblicazione.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "basso",
        "misura": ("stesso file, sezione playlist: elenca le playlist mancanti per canale e "
                   "il criterio per raggrupparle (tema, non data)"),
    },
    {
        "id": "A6-L00-03",
        "tipo": "procedura",
        "regola": ("Prima di dichiarare un passo del wizard 'non gestito' dal nostro codice, "
                   "verificare SEMPRE in due lingue: il corso e' in italiano, la UI Studio "
                   "automatizzata (Playwright) e' in inglese. Un grep in una lingua sola ha "
                   "prodotto oggi un falso negativo sul questionario di autocertificazione, gia' "
                   "gestito in inglese (righe 129-138 di youtube_uploader_playwright.py) ma "
                   "invisibile a un grep solo su 'idoneit'."),
        "prova": "solo parlato @ 08:06 (autocertificazione) — riscontrato falso dal codice reale, non da un frame",
        "fonte": "parlato",
        "tocca": "-",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "basso",
        "misura": ("procedura interna allo studio, non tocca la fabbrica: ogni prossima "
                   "affermazione 'non e' gestito' in questo studio va accompagnata da un grep "
                   "bilingue, non uno solo"),
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
        "A6-L00-01": contiene(YP, ["schermata finale", "schede", "sottotitoli nativi"]),
        "A6-L00-02": contiene(YP, ["playlist"]),
        "A6-L00-03": True,  # procedura interna, non ha un file bersaglio da verificare
    }
