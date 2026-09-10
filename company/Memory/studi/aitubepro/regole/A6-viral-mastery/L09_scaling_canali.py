# -*- coding: utf-8 -*-
"""regole/A6-viral-mastery/L09_scaling_canali.py

Fonte: AI TUBE PRO / A6 Viral Mastery / L09 "Scaling dei canali e dei video YouTube" (07:38,
id a03af595-3999-4e57-a147-e9e20ca26898, docente Pietro Gangemi). Ultima lezione della categoria
in questo giro.

Caso reale con doppia dashboard Analytics a schermo (canale italiano vs canale spagnolo, stesso
script tradotto): risultati quasi identici in views/iscritti raggiunti in un terzo del tempo, a
costo di lavoro zero oltre la traduzione. I numeri del parlato sono garbugliati dalla trascrizione
automatica su questa lezione: presi dallo schermo (frame-005.png, frame-087.png), coerenti col
senso generale del parlato.
"""

FONTE = "AI TUBE PRO / A6 Viral Mastery / L09"
LEZIONE = "Scaling dei canali e dei video YouTube"

REGOLE = [
    {
        "id": "A6-L09-01",
        "tipo": "funzione",
        "regola": ("Manca una funzione che prenda uno script gia' scritto e approvato (passato "
                   "i gate di qualita') e lo traduca per generare un canale gemello in un'altra "
                   "lingua, invece di far ripartire la scrittura da zero per ogni nuova lingua. "
                   "Il caso reale della lezione mostra risultati quasi identici (views, "
                   "iscritti) raggiunti in un terzo del tempo (4 mesi contro 12), a costo di "
                   "lavoro pari a una sola chiamata di traduzione."),
        "prova": ("parlato @ 02:52-04:20 (\"l'impegno qui pero' e' stato zero [...] ho "
                  "semplicemente detto a ChatGPT [...] traducimi questo testo\"); schermo "
                  "frame-005.png @ 0:08 (canale IT: 2.767.607 views, +35.891 iscritti, "
                  "8.400,38 euro / 12 mesi) confrontato con frame-087.png @ 2:52 (canale ES: "
                  "2.220.649 views, +35.021 iscritti, 3.083,10 euro / 4 mesi)"),
        "fonte": "entrambi",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "medio",
        "misura": ("esiste una funzione replica_in_lingua(script_approvato, lingua_target) che "
                   "produce un secondo script pronto per un canale gemello; un canale replicato "
                   "in questo modo non richiede una nuova ricerca fonte ne' una nuova scrittura "
                   "da zero"),
    },
    {
        "id": "A6-L09-02",
        "tipo": "parametro",
        "regola": ("Il dizionario CANALI dovrebbe portare un campo lingua esplicito per ogni "
                   "canale — oggi e' implicitamente sempre italiano (voice_id/voice_gender sono "
                   "gia' per-canale, la lingua no) — prerequisito tecnico diretto per "
                   "A6-L09-01."),
        "prova": "codice: apex7_orchestrator.py:84-114 (dict CANALI, esempio dosementale) non ha nessun campo 'lingua'",
        "fonte": "schermo",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "basso",
        "misura": "ogni voce di CANALI ha un campo lingua valorizzato, usato per scegliere la voce Fliki e per orientare A6-L09-01",
    },
    {
        "id": "A6-L09-03",
        "tipo": "flusso",
        "regola": ("Manca un concetto di script 'richiudibile' nella coda di produzione: un "
                   "contenuto gia' diventato virale dovrebbe poter essere segnato come "
                   "candidato a ripubblicazione (con modifiche) dopo 1-1,5 mesi sullo stesso "
                   "canale, invece di restare un evento singolo mai piu' rivisitato."),
        "prova": "parlato @ 01:38-02:08 (\"puoi ripubblicare quel contenuto [...] avendo fatto delle modifiche\")",
        "fonte": "parlato",
        "tocca": "memory/coda_produzione.json",
        "azione": "costruisci",
        "binario": "A",
        "rischio": "basso",
        "misura": "coda_produzione.json ha un campo/flag richiudibile_dal con data, popolato per gli script gia' pubblicati con buoni risultati",
    },
]
