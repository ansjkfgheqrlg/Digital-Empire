# 14.4 — Interpretazione Pratica: Implementare il Ciclo nel

CLAUDE.md 
Per attivare il ciclo Task-Do-Verify, le istruzioni devono essere codificate nel CLAUDE.md o nelle rules del progetto. 
L'autore mostra che nel suo CLAUDE.md per siti web è presente: 
text 
ESEMPIO DI REGOLA DI VERIFICA NEL CLAUDE.MD: 
 
## Workflow di Verifica 
 
Dopo ogni implementazione: 
1. Confronta il tuo screenshot con l'immagine di riferimento 
2. Confronta le differenze in spaziatura, dimensioni, colori 

--- PAGE 39 ---
3. Correggi le differenze trovate 
4. Rifai lo screenshot 
5. Ripeti fino a quando le differenze sono minime 
Per applicazioni (non siti web), il ciclo potrebbe essere: 
text 
ESEMPIO DI REGOLA DI VERIFICA PER APPLICAZIONI: 
 
## Workflow di Verifica 
 
Dopo ogni implementazione: 
1. Esegui il codice per verificare che compili senza errori 
2. Esegui i test automatici 
3. Se un test fallisce, identifica la causa e correggi 
4. Ri-esegui i test 
5. Ripeti fino a quando tutti i test passano 
6. Presenta il risultato finale con il riepilogo dei test

