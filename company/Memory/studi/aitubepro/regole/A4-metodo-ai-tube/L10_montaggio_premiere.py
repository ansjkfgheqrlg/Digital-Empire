# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L10.

«Montaggio Video Pro con Premiere Pro» · ~13 min · 2.000 parole · profondita' BRONZO dichiarata.

Tutorial di montaggio manuale applicato al metodo copia-incolla. Provenienza dichiarata dal
docente stesso (00:48): e' un video preso da un altro percorso a pagamento della stessa casa,
regalato dentro AI TUBE PRO.

Nonostante sia un tutorial di software, porta due cose vere — una che ci manca (intro e outro
come firma del canale) e una che ci fa capire un vantaggio che non sapevamo di avere (la
sincronia voce/immagini, che nel nostro flusso e' gratis) — piu' il terzo mito del camuffamento.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L10"
LEZIONE = "Montaggio Video Pro con Premiere Pro"

REGOLE = [
    {
        "id": "A4-L10-01",
        "tipo": "procedura",
        "regola": ("Un canale ha una INTRO e un OUTRO propri, ricorrenti: sono la firma che rende "
                   "il video riconoscibile come nostro e non come uno dei tanti. La nostra "
                   "fabbrica oggi non ne ha nessuno dei due — i video cominciano e finiscono "
                   "nudi, e nulla dice a chi guarda di che canale sono."),
        "prova": "solo parlato @ 04:01 ('ecco perche' vi consiglio di creare un'intro e anche un outro') e @ 07:27 (l'intro allunga il video e lo rende unico)",
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/operatori/video-producer.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "medio",
        "misura": ("video-producer dichiara intro e outro fra gli elementi del canale e segnala "
                   "che oggi la catena non li produce; oggi ne' l'agente ne' il payload li "
                   "nominano"),
    },
    {
        "id": "A4-L10-02",
        "tipo": "vincolo",
        "regola": ("NESSUNA soglia di durata rende lecito l'uso di una clip protetta: ne' 5, ne' "
                   "7, ne' 30 secondi. La porzione usata e' UNO dei fattori valutati, non una "
                   "franchigia, e il Content ID riconosce anche frammenti brevi. Terzo dei quattro "
                   "miti del camuffamento."),
        "prova": "solo parlato @ 09:02 ('possiamo anche utilizzare clip con il copyright, magari di un film, della serie Narcos, che dura non meno di 5 secondi')",
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "alto",
        "misura": ("monetizzazione-compliance §5 elenca il mito dei 5 secondi con la sua "
                   "confutazione; oggi la scheda non lo nominava"),
    },
    {
        "id": "A4-L10-03",
        "tipo": "euristica",
        "regola": ("Generare le immagini DAL nostro testo ci regala la sincronia voce/immagini, "
                   "che chi monta a mano deve inseguire: con clip altrui il voiceover nuovo e' "
                   "sempre piu' veloce o piu' lento dell'originale, e va compensato togliendo o "
                   "aggiungendo clip a mano. E' un vantaggio strutturale del nostro flusso, e va "
                   "scritto: chi non sa di averlo lo baratta alla prima scorciatoia."),
        "prova": "solo parlato @ 05:25 -> 05:56 ('il voiceover americano va troppo veloce o piu' lento rispetto al vostro: se e' piu' lento dovete rimuovere clip, se e' piu' veloce dovete aggiungerne')",
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/operatori/video-producer.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "basso",
        "misura": ("video-producer scrive perche' la sincronia e' gratis nel nostro flusso e cosa "
                   "si perderebbe passando a clip altrui"),
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

    VP = "03-AGENTI-E-RUOLI/operatori/video-producer.md"
    return {
        "A4-L10-01": contiene(VP, ["intro", "outro"]),
        "A4-L10-02": contiene("04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
                              ["miti del camuffamento", "5 secondi"]),
        "A4-L10-03": contiene(VP, ["sincronia"]),
    }
