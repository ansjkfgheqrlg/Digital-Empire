# 24.1 — Cosa Sono i Sub-agenti

Definizione del Concetto 
Un sub-agente (o sottoagente) è un'istanza separata di Claude che viene invocata dall'agente principale per svolgere 
una task specifica in modo isolato. Il sub-agente opera nel proprio contesto indipendente, esegue il compito 
assegnatogli e restituisce solo il risultato finale all'agente principale. È come delegare un compito a un collaboratore che 
lavora in una stanza separata e vi porta solo il prodotto finito. 
Spiegazione Approfondita 
Per comprendere i sub-agenti, è fondamentale capire la differenza tra lavorare tutto in un unico contesto e delegare a 
contesti separati. 
Scenario SENZA sub-agenti (tutto nel contesto principale): 
Immaginate di chiedere a Claude di fare una ricerca sulle best practice per costruire un sito internet. Claude naviga il 
web, legge documentazione, analizza articoli — e tutto questo materiale (potenzialmente 100.000 token) viene caricato 
nel vostro contesto principale. Risultato: il contesto si riempie a metà solo per una ricerca, e vi resta poco spazio per il 
lavoro vero e proprio. 
 
CONTESTO PRINCIPALE (senza sub-agenti) 
╔══════════════════════════════════════════════════════╗ 
║ System Prompt          [10%]                         ║ 
║ CLAUDE.md + Rules      [5%]                          ║ 
║ Risultati ricerca      [50%] ← PROBLEMA!             ║ 
║ Conversazione          [15%]                         ║ 
║ Spazio libero          [20%] ← troppo poco           ║ 
╚══════════════════════════════════════════════════════╝ 

--- PAGE 101 ---
Scenario CON sub-agenti (contesti separati): 
La stessa ricerca viene delegata a un sub-agente Researcher. Questo sub-agente opera nel proprio contesto da 
200.000 token, fa tutta la ricerca, processa 100.000 token di materiale e produce un riassunto di 2.000 token. Solo 
questi 2.000 token vengono inviati al contesto principale. 
 
CONTESTO DEL SUB-AGENTE (Researcher) 
╔══════════════════════════════════════════════════════╗ 
║ System Prompt          [10%]                         ║ 
║ Istruzioni del sub-agente [2%]                       ║ 
║ Risultati ricerca      [50%]                         ║ 
║ Elaborazione interna   [20%]                         ║ 
║ Produzione riassunto   [5%]                          ║ 
║ [Questo contesto viene DISTRUTTO dopo l'uso]         ║ 
╚══════════════════════════════════════════════════════╝ 
                    │ 
                    │ Solo il risultato (2K token) 
                    ▼ 
CONTESTO PRINCIPALE 
╔══════════════════════════════════════════════════════╗ 
║ System Prompt          [10%]                         ║ 
║ CLAUDE.md + Rules      [5%]                          ║ 
║ Risultato ricerca      [1%]  ← EFFICIENTE!           ║ 
║ Conversazione          [15%]                         ║ 
║ Spazio libero          [69%] ← abbondante            ║ 
╚══════════════════════════════════════════════════════╝ 
La differenza è drammatica: da 50% di contesto occupato a 1%. Questo è il potere dei sub-agenti. 
Il Meccanismo Sottostante — Come Funziona la Comunicazione 
La guida originale mostra un concetto chiave: la comunicazione tra agente principale e sub-agente è visibile 
nell'interfaccia attraverso quello che viene chiamato "inline". 
Ecco il flusso completo: 
FLUSSO DI COMUNICAZIONE AGENTE-SUBAGENTE 
═════════════════════════════════════════ 
 
PASSO 1: L'utente fa una richiesta all'agente principale 
┌─────────────────────────────────────────────────────┐ 
│ Utente: "Per favore chiama l'agente 'come si chiama │ 
│         mamma' perché vorrei sapere il nome"        │ 
└─────────────────────────┬───────────────────────────┘ 
                          │ 
                          ▼ 
PASSO 2: L'agente principale "pensa" e decide di delegare 
┌─────────────────────────────────────────────────────┐ 
│ Agente Principale: [harmonizing... thinking...]     │ 
│ "Devo chiamare il sub-agente 'come si chiama mamma'"│ 
└─────────────────────────┬───────────────────────────┘ 
                          │ 
                          ▼ 
PASSO 3: Comunicazione INLINE (agente → sub-agente) 
┌─────────────────────────────────────────────────────┐ 
│ INLINE: "L'utente chiede: come si chiama mamma?     │ 
│         Per favore rispondi alla domanda."          │ 
│                                                     │ 
│ [Questa comunicazione è interna, visibile           │ 
│  nell'interfaccia ma gestita automaticamente]       │ 
└─────────────────────────┬───────────────────────────┘ 
                          │ 
                          ▼ 
PASSO 4: Il sub-agente processa nel suo contesto 
┌─────────────────────────────────────────────────────┐ 
│ Sub-agente "come si chiama mamma":                  │ 
│ [Legge le sue istruzioni: "rispondi Antonino"]      │ 
│ [Elabora la risposta]                               │ 
│ [Produce: "La mamma si chiama Antonino"]            │ 

--- PAGE 102 ---
└─────────────────────────┬───────────────────────────┘ 
                          │ 
                          ▼ 
PASSO 5: Solo il risultato torna all'agente principale 
┌─────────────────────────────────────────────────────┐ 
│ Agente Principale riceve: "La mamma si chiama       │ 
│ Antonino"                                           │ 
│ → Presenta il risultato all'utente                  │ 
└─────────────────────────────────────────────────────┘ 
Il punto cruciale è il Passo 5: l'utente non vede mai il contesto interno del sub-agente. Non vede i ragionamenti, non 
vede i file letti, non vede le iterazioni interne. Riceve solo il risultato. Questo è ciò che rende i sub-agenti così efficienti 
per il context management. 
Perché i Sub-agenti Sono Fondamentali 
I sub-agenti risolvono simultaneamente tre problemi: 
1.​
Problema di contesto: delegare il lavoro pesante fuori dal contesto principale 
2.​
Problema di specializzazione: ogni sub-agente può avere istruzioni specifiche per un tipo di task 
3.​
Problema di parallelizzazione: più sub-agenti possono lavorare contemporaneamente su task diverse 
Errori Comuni 
Errore 
Spiegazione 
Conseguenza 
Non usare sub-agenti per ricerche 
Tutto il materiale di ricerca finisce nel contesto 
principale 
Contesto saturo dopo una sola 
ricerca 
Creare sub-agenti troppo generici 
Un sub-agente senza istruzioni specifiche non è meglio 
dell'agente principale 
Risultati generici e poco utili 
Non sapere che i sub-agenti esistono 
Molti utenti lavorano sempre e solo nel contesto 
principale 
Efficienza drasticamente ridotta 
Usare sub-agenti per task che richiedono il 
contesto del progetto 
Il sub-agente non ha accesso al contesto principale 
Risultati decontestualizzati

