# 27.2 — La Struttura Interna di una Skill

Definizione del Concetto 
Ogni skill è composta da due componenti fondamentali contenuti in una cartella dedicata: 
1.​
Il file skill.md — l'orchestratore (la checklist) 
2.​
La cartella scripts/ — il codice eseguibile 
Questi due componenti lavorano insieme ma hanno ruoli molto diversi. 
Spiegazione Approfondita — Il File skill.md (L'Orchestratore) 
L'autore della guida usa una metafora potente per spiegare il ruolo del file skill.md: 
"Dovete pensare a questa skill.md come un orchestrator. Immaginatevi un'orchestra: c'è il direttore d'orchestra — il tizio 
con le bacchette — e poi ci sono quelli che suonano l'orchestra." 
text 
ANATOMIA DEL FILE SKILL.MD 
═══════════════════════════ 
 
┌─────────────────────────────────────────────────────┐ 
│                    SKILL.MD                          │ 
│              (Il Direttore d'Orchestra)              │ 
│                                                      │ 
│  ┌───────────────────────────────────────────────┐  │ 
│  │ DESCRIZIONE DELLA SKILL                       │  │ 
│  │ "Pubblica Real Short Video e posta su          │  │ 

--- PAGE 130 ---
│  │  YouTube, Instagram o Facebook in maniera      │  │ 
│  │  automatica"                                   │  │ 
│  └───────────────────────────────────────────────┘  │ 
│                                                      │ 
│  ┌───────────────────────────────────────────────┐  │ 
│  │ PIATTAFORME E STRUMENTI                       │  │ 
│  │ • YouTube: Python API                         │  │ 
│  │ • Instagram: tramite Chrome Dev Tool MCP      │  │ 
│  │ • Facebook: tramite Chrome Dev Tool MCP       │  │ 
│  └───────────────────────────────────────────────┘  │ 
│                                                      │ 
│  ┌───────────────────────────────────────────────┐  │ 
│  │ CHECKLIST DI VALIDAZIONE INPUT                │  │ 
│  │ □ Gather input: which platform?               │  │ 
│  │ □ Gather input: which content?                │  │ 
│  │ □ If valid → procedi                          │  │ 
│  │ □ If invalid → richiedi correzione            │  │ 
│  └───────────────────────────────────────────────┘  │ 
│                                                      │ 
│  ┌───────────────────────────────────────────────┐  │ 
│  │ SEQUENZA DI ESECUZIONE                        │  │ 
│  │ 1. Chiama build_schedule.py                   │  │ 
│  │ 2. Chiama check_meta.py                       │  │ 
│  │ 3. Chiama check_youtube.py                    │  │ 
│  │ 4. Chiama upload_youtube.py                   │  │ 
│  └───────────────────────────────────────────────┘  │ 
│                                                      │ 
│  ┌───────────────────────────────────────────────┐  │ 
│  │ GESTIONE ERRORI                               │  │ 
│  │ • Se uno step fallisce → log errore           │  │ 
│  │ • Tenta auto-correzione                       │  │ 
│  │ • Se non risolvibile → notifica utente        │  │ 
│  └───────────────────────────────────────────────┘  │ 
│                                                      │ 
└─────────────────────────────────────────────────────┘ 
Il file skill.md è essenzialmente la mappa di navigazione della skill. Dice a Claude: 
●​
Che cosa deve fare questa skill 
●​
Quali input raccogliere dall'utente 
●​
Come validare gli input 
●​
In quale ordine eseguire le operazioni 
●​
Quali script chiamare 
●​
Come gestire gli errori 
La Cartella scripts/ (I Musicisti dell'Orchestra) 
Se il file skill.md è il direttore d'orchestra, gli script sono i musicisti. Sono loro che effettivamente "suonano" — 
eseguono il codice reale che compie le operazioni. 
text 
ANATOMIA DELLA CARTELLA SCRIPTS/ 
════════════════════════════════ 
 
scripts/ 
├── build_schedule.py 
│   └── Costruisce la mappatura di quando pubblicare 
│       Input: preferenze utente (giorno, ora, piattaforma) 
│       Output: schedule strutturato 
│ 
├── check_meta.py 
│   └── Verifica se su Meta (Facebook/Instagram)  
│       c'è già un post programmato 
│       Input: schedule, credenziali Meta 
│       Output: stato (libero/occupato) 
│ 
├── check_youtube.py 
│   └── Verifica lo stato del canale YouTube 
│       Input: credenziali YouTube API 
│       Output: stato canale, video recenti 

--- PAGE 131 ---
│ 
└── upload_youtube.py 
    └── Carica il video su YouTube 
        Input: file video, titolo, descrizione, tag 
        Output: URL del video pubblicato 
Gli script sono codice deterministico — non sono prompt LLM. Sono programmi Python (o altro linguaggio) che 
eseguono operazioni specifiche e prevedibili. Questo è un punto cruciale che vedremo in dettaglio. 
La Relazione tra skill.md e scripts/ 
La guida originale chiarisce un malinteso molto comune: 
"Molte persone fanno una skill.md dicendo che è semplicemente un markdown, ma questo è un po' forviante." 
La skill non è il file markdown. La skill è l'insieme di skill.md + scripts/. Il markdown è il direttore d'orchestra, ma senza i 
musicisti (gli script) non c'è concerto. 
text 
INTERAZIONE TRA SKILL.MD E SCRIPTS 
═══════════════════════════════════ 
 
    L'utente dice: "Pubblica il mio video su YouTube" 
                │ 
                ▼ 
    ┌──────────────────────────┐ 
    │      SKILL.MD            │ 
    │   (Direttore)            │ 
    │                          │ 
    │   "OK, devo:             │ 
    │    1. Validare l'input   │ 
    │    2. Chiamare gli       │ 
    │       script giusti      │ 
    │    3. Verificare i       │ 
    │       risultati"         │ 
    └────────────┬─────────────┘ 
                 │ 
    ┌────────────┼────────────────────┐ 
    │            │                    │ 
    ▼            ▼                    ▼ 
┌─────────┐ ┌─────────────┐ ┌──────────────┐ 
│ build_  │ │ check_      │ │ upload_      │ 
│schedule │ │ youtube     │ │ youtube      │ 
│  .py    │ │  .py        │ │  .py         │ 
│         │ │             │ │              │ 
│ [CODICE]│ │ [CODICE]    │ │ [CODICE]     │ 
│ [DETER- │ │ [DETER-     │ │ [DETER-      │ 
│ MINISTI-│ │ MINISTICO]  │ │ MINISTICO]   │ 
│ CO]     │ │             │ │              │ 
└────┬────┘ └──────┬──────┘ └──────┬───────┘ 
     │             │               │ 
     └─────────────┼───────────────┘ 
                   │ 
                   ▼ 
    ┌──────────────────────────┐ 
    │      SKILL.MD            │ 
    │   (Verifica risultati)   │ 
    │                          │ 
    │   "Tutto OK? → Report    │ 
    │    Errore? → Self-heal"  │ 
    └──────────────────────────┘ 
 

--- PAGE 132 ---

