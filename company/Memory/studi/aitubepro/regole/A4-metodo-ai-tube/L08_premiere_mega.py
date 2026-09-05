# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L08.

«Premiere Pro Mega Tutorial Completo» · 54:42 · 9.586 parole · profondita' BRONZO dichiarata.

54 minuti d'interfaccia di Adobe Premiere Pro: quali tasti premere, come installare un font, come
navigare un menu. Il docente stesso la presenta come opzionale per chi usa editor AI, e cita Fliki
(07:16). Letta integralmente da uno scagnozzo, dichiarato.

In 54 minuti di «mega tutorial completo» non c'e' una riga su PERCHE' un video trattiene lo
spettatore: niente sul gancio iniziale, niente sulla durata delle scene, niente sui sottotitoli
come leva di ritenzione (ci sono, ma solo come funzione del software). Sopravvivono tre principi
al netto dello strumento, e una quarta affermazione da segnare.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L08"
LEZIONE = "Premiere Pro Mega Tutorial Completo"

REGOLE = [
    {
        "id": "A4-L08-01",
        "tipo": "euristica",
        "regola": ("Gli elementi ricorrenti di un canale (richiami all'iscrizione, stacchi, "
                   "chiusure) si tengono in un ventaglio piccolo e SI RUOTANO: tre o quattro, "
                   "diversi fra loro, mai gli stessi due video di fila. Un timbro identico su "
                   "ogni video e' quello che fa sembrare un canale una catena di montaggio."),
        "prova": "solo parlato @ 09:35 ('ne prendete 3-4 che vi piacciono, diversi anche tra di loro; per ogni video ne utilizzate qualcuno diverso, non sempre gli stessi')",
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/operatori/script-writer.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "basso",
        "misura": ("script-writer tiene un ventaglio di chiusure/richiami e ne ruota l'uso; oggi "
                   "non esiste alcuna regola di rotazione e nulla impedisce la stessa CTA "
                   "identica su ogni video"),
    },
    {
        "id": "A4-L08-02",
        "tipo": "parametro",
        "regola": ("La musica sta SOTTO la voce, e il livello giusto e' molto piu' basso di quanto "
                   "sembri: nella lezione, -25 dB e' ancora troppo alto e il valore buono e' "
                   "-35 dB. Vale come riferimento il giorno in cui accerteremo se i nostri video "
                   "hanno una traccia musicale (verifica aperta di A4-L04-04)."),
        "prova": "solo parlato @ 44:39 -> 45:06 (da 0 dB a -25 dB, 'ancora troppo alta', poi -35 dB)",
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/controllo/qa-audio-video.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "basso",
        "misura": ("qa-audio-video §9 porta il riferimento numerico (-35 dB) accanto alla verifica "
                   "sospesa sulla musica, cosi' che quando si accertera' ci sia gia' un metro"),
    },
    {
        "id": "A4-L08-03",
        "tipo": "vincolo",
        "regola": ("Coprire il logo con un rettangolo, ritagliare, zoomare o tradurre il testo "
                   "sovraimpresso NON evita i problemi di diritto d'autore: il diritto protegge "
                   "il contenuto audiovisivo, non il marchio che ci sta sopra. Coprire la "
                   "provenienza non trasferisce i diritti. Quarto dei quattro miti del "
                   "camuffamento."),
        "prova": "solo parlato @ 48:49 ('cambiare le carte in tavola serve per evitare problemi di copyright'), ribadito @ 39:56 e @ 40:37",
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "alto",
        "misura": ("monetizzazione-compliance §5 elenca questo mito con la sua confutazione e la "
                   "regola di casa in una riga; oggi la scheda non lo nominava"),
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

    return {
        "A4-L08-01": contiene("03-AGENTI-E-RUOLI/operatori/script-writer.md",
                              ["ventaglio", "ruota"]),
        # "35 db" senza segno: nel testo il meno e' quello tipografico (U+2212), non il trattino
        # ASCII — cercare "-35 db" darebbe un falso negativo.
        "A4-L08-02": contiene("03-AGENTI-E-RUOLI/controllo/qa-audio-video.md", ["35 db"]),
        "A4-L08-03": contiene("04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
                              ["miti del camuffamento", "logo"]),
    }
