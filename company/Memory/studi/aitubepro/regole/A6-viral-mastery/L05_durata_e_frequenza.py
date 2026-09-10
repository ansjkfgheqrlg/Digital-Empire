# -*- coding: utf-8 -*-
"""regole/A6-viral-mastery/L05_durata_e_frequenza.py

Fonte: AI TUBE PRO / A6 Viral Mastery / L05 "Quanti video pubblicare, quanto devono durare e
proporzione trend evergreen" (14:22, id 7648b298-badd-4709-bcaf-f6e47b416a2c).

QUESTA E' LA LEZIONE ATTESA DA BASELINE.md PER CHIUDERE D-1.
Letta integralmente (parlato + schermo). Conclusione onesta: la lezione NON da un numero unico di
"durata ottimale" che sostituisca DURATA_MASSIMA_S/PAROLE_MINIME_SCRIPT — anzi insegna
esplicitamente che una durata fissa e sbagliata nell'impianto, perche' la durata dipende dalla
nicchia. Prova decisiva: nel documento Word che il docente scrive in diretta durante la lezione,
la voce "Quanto devono durare i video?" resta senza risposta scritta per tutti i 14:22, mentre le
altre tre domande della lezione ricevono tutte un numero (vedi frame-350.png @ 11:38,
frame-410.png @ 13:38 — la lavagna finale completa).

D-1 non si chiude con un numero magico: si chiude sostituendo il tetto fisso con una funzione
per-nicchia (A6-L05-02/03), usando i due numeri reali che la lezione DA (floor 4 min, soglia
opzionale 8 min) come ingredienti di quella funzione, non come sostituti diretti delle costanti.
"""

FONTE = "AI TUBE PRO / A6 Viral Mastery / L05"
LEZIONE = "Quanti video pubblicare, quanto devono durare e proporzione trend evergreen"

REGOLE = [
    {
        "id": "A6-L05-01",
        "tipo": "parametro",
        "regola": ("Pubblicare almeno 3 video a settimana (12-15 al mese) come pavimento minimo "
                   "per ogni canale; salire fino alla cadenza dei migliori competitor della "
                   "propria nicchia se si vuole competere davvero."),
        "prova": "parlato @ 01:04-01:28, confermato a schermo frame-125.png @ 4:08 (\"3 volte a settimana / 12-15 video al mese e il minimo\")",
        "fonte": "entrambi",
        "tocca": "-",
        "azione": "costruisci",
        "binario": "A",
        "rischio": "basso",
        "misura": ("esiste una costante FREQUENZA_MINIMA_SETTIMANALE_VIDEO consultabile da "
                   "un agente/reference; oggi non esiste nessun valore, quindi qualunque numero "
                   "scritto e' un miglioramento verificabile a colpo d'occhio"),
    },
    {
        "id": "A6-L05-02",
        "tipo": "vincolo",
        "regola": ("DURATA_MASSIMA_S e DURATA_MINIMA_S fissi e identici per ogni nicchia/canale "
                   "contraddicono l'insegnamento esplicito della lezione: la durata deve essere "
                   "decisa dal contenuto necessario alla nicchia, non da un tetto universale. "
                   "Il vincolo attuale e' l'origine strutturale di D-1, non solo il sintomo "
                   "numerico (600s vs ~720s)."),
        "prova": ("parlato @ 03:37-03:57 \"non c'e' una durata prestabilita che noi dobbiamo "
                  "fare\"; prova a schermo decisiva: frame-350.png @ 11:38 e frame-410.png @ "
                  "13:38 mostrano la voce \"Quanto devono durare i video?\" ancora senza "
                  "risposta scritta a fine lezione, mentre le altre tre domande hanno tutte un "
                  "numero"),
        "fonte": "entrambi",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/regolatori.py",
        "azione": "ridisegna",
        "binario": "B",
        "rischio": "alto",
        "misura": ("DURATA_MASSIMA_S/DURATA_MINIMA_S smettono di essere costanti globali fisse; "
                   "un video prodotto per una nicchia flash/news e uno per una nicchia evergreen "
                   "passano entrambi verifica_qualita() con range diversi, e nessuno script che "
                   "rispetta PAROLE_MINIME_SCRIPT viene piu' automaticamente bocciato"),
    },
    {
        "id": "A6-L05-03",
        "tipo": "funzione",
        "regola": ("Costruire range_durata_per_nicchia(tipo_nicchia) in regolatori.py: per "
                   "nicchie 'flash/news' ammette 60-240s (coerente con l'esempio del corso, "
                   "notizia flash da 1-2 minuti); per nicchie 'standard' richiede minimo 4 "
                   "minuti (240s) senza tetto rigido superiore, coerente col floor di retention "
                   "citato dal corso. PAROLE_MINIME_SCRIPT deve derivare dal range scelto, non "
                   "restare fisso a 2220 indipendentemente dalla nicchia."),
        "prova": "parlato @ 03:37-05:14 (esempi vecchioni 1-2min, oroscopo 5-12min, telegiornale 40min)",
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/regolatori.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "alto",
        "misura": ("funzione nuova con test che copre almeno 2 tipi di nicchia; "
                   "apex7_orchestrator.py chiama la funzione invece di usare PAROLE_MINIME_SCRIPT "
                   "fisso; dipende da A6-L05-02"),
    },
    {
        "id": "A6-L05-04",
        "tipo": "parametro",
        "regola": ("Floor raccomandato di 4 minuti per video 'corti per natura': sotto questa "
                   "soglia la lezione segnala meno probabilita' di essere spinti dall'algoritmo "
                   "dei video consigliati (retention insufficiente)."),
        "prova": "parlato @ 04:21-04:48 \"resto sempre in media, minimo nei video [...] che durano almeno 4 minuti\"",
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/regolatori.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "medio",
        "misura": "il floor di 4 minuti e' un parametro nominato in range_durata_per_nicchia, non un numero perso in un commento",
    },
    {
        "id": "A6-L05-05",
        "tipo": "parametro",
        "regola": ("Soglia di 8 minuti = sblocco di piu' inserzioni mid-roll: esplicitamente "
                   "dichiarata OPZIONALE dal docente, non un obbligo di durata. Va esposta come "
                   "informazione per chi decide la strategia di monetizzazione, mai imposta come "
                   "vincolo di durata minima universale (sarebbe un fraintendimento del corso)."),
        "prova": "parlato @ 05:39-06:07 \"questo non vuol dire che noi dobbiamo far durare il video per forza piu' di 8 minuti\"",
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references",
        "azione": "costruisci",
        "binario": "A",
        "rischio": "basso",
        "misura": "esiste una nota in reference che spiega la soglia 8min come leva di monetizzazione opzionale, non come regola di durata",
    },
    {
        "id": "A6-L05-06",
        "tipo": "parametro",
        "regola": ("Proporzione editoriale trend/evergreen: 70/30 in condizioni normali, fino a "
                   "85 trend / 15 evergreen se si vuole spingere aggressivamente; i primi 15 "
                   "video di un canale nuovo vanno dedicati all'evergreen."),
        "prova": "parlato @ 08:41-09:02, confermato a schermo frame-290.png @ 9:38 (\"70/30\", \"85/trend 15 ever green\")",
        "fonte": "entrambi",
        "tocca": "-",
        "azione": "costruisci",
        "binario": "A",
        "rischio": "basso",
        "misura": "esiste una costante/reference con la proporzione, consultabile dal niche-scout o dal piano editoriale; oggi zero",
    },
    {
        "id": "A6-L05-07",
        "tipo": "script",
        "regola": ("Manca uno script/contatore che segnali quando un canale raggiunge i tre "
                   "checkpoint di volume citati dal corso (33, 100, 500 video) e apra "
                   "esplicitamente una fase di analisi/revisione a quel punto. Oggi nessun "
                   "contatore per canale esiste, e con 8 video totali prodotti in tutta la "
                   "fabbrica (BASELINE.md §4) siamo lontanissimi dal primo checkpoint — motivo "
                   "in piu' per costruirlo ora, prima che serva davvero."),
        "prova": ("parlato @ 09:16-11:53 (33 = dati sufficienti su Analytics, 100 = atteso 10% "
                  "vincenti, 500 = canale avviato), confermato a schermo frame-410.png @ 13:38 "
                  "(\"1 step 33 video / 2 step 100 video / 3 step 500 video\")"),
        "fonte": "entrambi",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/milestone_tracker.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "basso",
        "misura": ("nuovo script milestone_tracker.py esiste, legge memory/video_prodotti.json "
                   "per canale, e stampa un avviso quando un canale attraversa 33/100/500 video "
                   "pubblicati"),
    },
]
