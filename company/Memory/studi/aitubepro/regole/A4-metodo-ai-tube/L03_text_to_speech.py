# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L03.

«Text to speech: cosa e', e come funziona» · 16:34 · strumento mostrato: Genny by LOVO
(la trascrizione automatica lo storpia in «l'obo»; verificato a schermo, frame-079).

Lezione introduttiva su uno strumento che non usiamo. Il suo valore per noi e' di specchio:
ci ha fatto trovare una contraddizione fra cio' che il nostro agente `voice-caster` ordina
(«una voce calma, di qualita', non la prima disponibile») e cio' che il nostro codice fa
(`candidates[0]`, la prima della lista, ri-risolta ad ogni generazione). E ci ha ricordato
che il giro di miglioramento sulla pronuncia esiste sulla carta e non ha mai prodotto una
riga: 125 decisioni registrate, zero sulla pronuncia.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L03"
LEZIONE = "Text to speech: cosa e', e come funziona"

REGOLE = [
    {
        "id": "A4-L03-01",
        "tipo": "procedura",
        "regola": ("La voce di un canale si sceglie UNA volta con criteri dichiarati — genere, "
                   "eta' percepita, uso previsto, ritmo — e poi si fissa. Un cambio di voce e' "
                   "una decisione scritta, mai l'effetto dell'ordine di una lista."),
        "prova": "frame-160.png @ 10:36 (tre blocchi con tre voci diverse) + parlato @ 07:30",
        "fonte": "entrambi",
        "tocca": "03-AGENTI-E-RUOLI/operatori/voice-caster.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "alto",
        "misura": ("voice-caster elenca i criteri e impone di fissare la voce; oggi chiede una "
                   "voce 'calma e di qualita'' mentre il codice prende candidates[0] "
                   "(fliki_client.py:113)"),
    },
    {
        "id": "A4-L03-02",
        "tipo": "parametro",
        "regola": ("Il voice_id sta fisso nella configurazione del canale: find_italian_voice "
                   "serve a risolverlo la prima volta, non a riscegliere la voce ad ogni "
                   "generazione. Un canale che cambia voce da solo perde la sua faccia."),
        "prova": "solo parlato @ 09:25 (sceglie a mano 'questa che ci e' piaciuta di piu'')",
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py",
        "azione": "modifica",
        "binario": "B",
        "rischio": "alto",
        "misura": ("CANALI contiene voice_id per ogni canale; oggi contiene solo voice_gender "
                   "(apex7_orchestrator.py:100 e 119) e la voce si ri-risolve ogni volta"),
    },
    {
        "id": "A4-L03-03",
        "tipo": "procedura",
        "regola": ("Il lessico di pronuncia e' un file vivo: ogni parola letta male trovata in "
                   "QA ci finisce dentro con la grafia che la fa leggere bene, e chi scrive lo "
                   "applica PRIMA di generare. Una correzione che resta in un rapporto e non in "
                   "un elenco si ripete identica al video dopo."),
        "prova": "solo parlato @ 13:17 ('ve le salvate su un file')",
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/lessico-pronuncia.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "medio",
        "misura": ("esiste il file del lessico e qa-audio-video ha l'ordine di scriverci dentro; "
                   "oggi in memory/decisions ci sono 125 decisioni e nessuna sulla pronuncia"),
    },
    {
        "id": "A4-L03-04",
        "tipo": "euristica",
        "regola": ("Davanti a decine di strumenti equivalenti si sceglie per realismo, costo, "
                   "lingua e controllo fine (pause, velocita', pronuncia), mai per novita': e' "
                   "la regola A4-L00-01 vista su un caso concreto, 52 sintetizzatori vocali."),
        "prova": "frame-046.png @ 03:00 (schede con etichette di costo) + parlato @ 02:26",
        "fonte": "entrambi",
        "tocca": "04-SKILLS-E-REFERENCE/references/scelta-strumenti.md",
        "azione": "conferma",
        "binario": "A",
        "rischio": "basso",
        "misura": ("la scheda di scelta strumenti cita il caso TTS e i quattro criteri di "
                   "controllo fine"),
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

    esiti = {}
    esiti["A4-L03-01"] = contiene("03-AGENTI-E-RUOLI/operatori/voice-caster.md",
                                  ["si sceglie una volta e si fissa", "à percepita"])
    esiti["A4-L03-02"] = contiene("02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py",
                                  ["voice_id"])
    esiti["A4-L03-03"] = (os.path.exists(os.path.join(
        fabbrica, "04-SKILLS-E-REFERENCE", "references", "lessico-pronuncia.md"))
        and contiene("03-AGENTI-E-RUOLI/controllo/qa-audio-video.md", ["lessico-pronuncia"]))
    esiti["A4-L03-04"] = contiene("04-SKILLS-E-REFERENCE/references/scelta-strumenti.md",
                                  ["text to speech"])
    return esiti
