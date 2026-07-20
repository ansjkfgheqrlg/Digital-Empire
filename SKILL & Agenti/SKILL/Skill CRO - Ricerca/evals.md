# EVALS — skill-cro-ricerca / Client Research Engine (retrofit MIR-5 sprint 2)

Casi di attivazione/uso atteso (criterio skill-creator: attiva corretta? output al livello DE? deleghe rispettate?).

| # | Scenario (input utente) | Atteso | Tipo |
|---|---|---|---|
| E1 | "Nuovo cliente: studio dentistico a Milano, inizia la ricerca" | STEP 0: chiede briefing/dati minimi; poi piano piattaforme B2C-locale (YouTube+Google+FB Groups IT) con query personalizzate e tempi | happy |
| E2 | "Ho incollato 8 commenti YouTube, proseguiamo" | Riconosce R1; estrae frasi esatte; **verifica completezza: <20 → chiede ricerca aggiuntiva con query specifiche**; NON procede inventando | gate |
| E3 | "Analizzami il competitor principale, ecco l'URL" | R2: scheda completa campo per campo (headline/CTA/pricing/obiezioni/gap); confronta con schede già fatte se presenti | happy |
| E4 | "Questi pain point sono buoni? 'vogliono più clienti'" | R4 + knowledge PAIN: segnala superficie → scava ai 3 livelli; categorizza in 4 categorie; scoring I×F×A; NON accetta "più clienti" come pain azionabile | quality |
| E5 | "Rispondi pure tu alle obiezioni nel copy" | **RIFIUTA il compito gestione**: R5 raccoglie e scora, la gestione è del CRO Copy Architect (confine esplicito del master) | boundary (anti-sconfinamento) |
| E6 | "Il report è finito, mandiamolo" | Gate qualità: verifica le 13 voci (o dichiara modalità minimum 2.5h con impatti); sezioni senza fonte → blocco con richiesta fonti | gate |
| E7 | "Ho dati solo da Instagram. Basta così?" | CROSS-PLATFORM: pattern da 1 sola piattaforma ≠ pattern di mercato; chiede almeno una seconda fonte prima del top-5; segnala limite nel report | quality |

**Esito atteso al retrofit (gate):** un operatore nuovo trova in ≤2 minuti: cosa fa il motore, l'ordine dei
7 knowledge, dov'è il gate qualità, cosa NON fa (non scrive copy, non gestisce obiezioni, non inventa dati),
e sa che i 5 template del manifest sono inline nel master — senza cercare file che non esistono (anti-F1).
