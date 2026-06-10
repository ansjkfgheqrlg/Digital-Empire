# 24.5 — Il QA Sub-agent

Definizione del Concetto 
Il QA (Quality Assurance) è un sub-agente specializzato nell'esecuzione di test e nella verifica che il codice funzioni 
correttamente. È la componente che si assicura che tutto ciò che è stato costruito funzioni come previsto, senza bug e 
senza regressioni. 
Spiegazione Approfondita 
Il QA sub-agent rappresenta la fase finale del ciclo di qualità. Se il Researcher trova le informazioni giuste per costruire 
qualcosa, e il Reviewer verifica che il codice sia ben scritto, il QA verifica che il codice funzioni effettivamente. 
Le Attività del QA Sub-agent: 
text 
AMBITI DI TEST DEL QA SUB-AGENT 
════════════════════════════════ 
 
1. TEST FUNZIONALI 
   └── Verifica che ogni funzione faccia ciò che deve fare 
   └── Testa i percorsi principali dell'applicazione 
   └── Verifica che input/output siano corretti 
 
2. TEST DI REGRESSIONE 
   └── Verifica che le modifiche recenti non abbiano rotto 

--- PAGE 111 ---
       funzionalità precedenti 
   └── Confronta il comportamento attuale con quello atteso 
 
3. TEST DI INTEGRAZIONE 
   └── Verifica che i diversi componenti lavorino insieme 
   └── Testa le connessioni con servizi esterni 
       (Supabase, Stripe, etc.) 
 
4. TEST DI EDGE CASE 
   └── Testa scenari limite (input vuoti, valori estremi) 
   └── Verifica la gestione degli errori 
 
5. FIX AUTOMATICI 
   └── Se trova bug, li corregge automaticamente 
   └── Verifica che il fix non introduca nuovi problemi 
Come Funziona in Pratica 
Nell'esempio della guida, quando il QA sub-agent viene chiamato sull'applicazione Trello: 
1.​
Riceve tutto il codice del progetto 
2.​
Esegue una batteria di test 
3.​
Identifica eventuali problemi 
4.​
Applica fix automaticamente (se gli è stato dato il permesso) 
5.​
Verifica che i fix funzionino 
6.​
Produce un report: "Risultati QA: costruito, passato dopo il fix" 
Il dettaglio importante è che il QA può applicare fix direttamente, senza chiedere all'utente. Questo è particolarmente 
utile quando si lavora in modalità bypass permission e si vuole che il sistema si auto-corregga. 
La Sinergia tra i Tre Sub-agenti 
I tre sub-agenti raccomandati formano un sistema completo di garanzia della qualità: 
text 
FLUSSO IDEALE DI UN PROGETTO CON TUTTI E TRE I SUB-AGENTI 
══════════════════════════════════════════════════════════ 
 
FASE 1: RICERCA 
    Researcher → "Ecco le best practice per [argomento]" 
         │ 
         ▼ 
FASE 2: COSTRUZIONE 
    Agente Principale → costruisce il progetto usando 
                        le best practice del Researcher 
         │ 
         ▼ 
FASE 3: REVISIONE 
    Reviewer → "Ho trovato 8 problemi, ecco i fix. 
                Ho ristrutturato il CLAUDE.md. 
                Ho creato regole e skill." 
         │ 
         ▼ 
FASE 4: TESTING 
    QA → "Ho testato tutto, trovati 3 bug, 
          fixati automaticamente.  
          Tutti i test passano ora." 
         │ 
         ▼ 
FASE 5: RISULTATO FINALE 
    Progetto completo, testato, ottimizzato, 
    con CLAUDE.md pulito e regole modulari 
Questa sequenza può essere eseguita dando pochi prompt: 

--- PAGE 112 ---
text 
Prompt 1: "Chiama il researcher sub-agent per cercare  
           le best practice per [progetto]" 
 
Prompt 2: "Usando le best practice trovate, costruisci  
           [progetto]"  
 
Prompt 3: "Chiama il reviewer sub-agent per rivedere  
           tutto il codice" 
 
Prompt 4: "Chiama il QA sub-agent per verificare che  
           tutto funzioni" 
Quattro prompt per un ciclo completo di sviluppo professionale. 
Il Vantaggio Economico dei Sub-agenti vs Lavoro nel Contesto Principale 
L'autore della guida sottolinea un punto fondamentale: utilizzare sub-agenti è un investimento che si ripaga. Anche se i 
sub-agenti consumano token nei loro contesti separati, il risparmio nel contesto principale è tale che: 
●​
Potete lavorare per sessioni molto più lunghe senza degrado di qualità 
●​
Evitate di dovere ricominciare da zero perché il contesto si è saturato 
●​
Ogni iterazione è più efficiente perché il contesto principale è pulito 
●​
La qualità finale è superiore perché ogni fase è gestita da uno specialista 
Errori Comuni nell'Uso dei Sub-agenti 
1.​
Non usarli perché "tanto Claude può fare tutto": Claude può fare tutto, ma la qualità è drasticamente superiore 
con sub-agenti specializzati. 
2.​
Usare i sub-agenti per task banali: chiamare un sub-agente per rinominare un file è spreco. I sub-agenti 
eccellono su task complesse che generano molti token. 
3.​
Non parallelizzare i sub-agenti: Reviewer e QA possono lavorare contemporaneamente (in terminal separati). 
Non c'è motivo di aspettare che uno finisca per lanciare l'altro. 
4.​
Dimenticare di importare i risultati: dopo che un sub-agente ha finito, assicuratevi che i fix e le modifiche siano 
effettivamente applicati nel progetto principale.

