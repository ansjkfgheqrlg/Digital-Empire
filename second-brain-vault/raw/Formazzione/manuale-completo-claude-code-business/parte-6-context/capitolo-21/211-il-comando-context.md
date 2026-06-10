# 21.1 — Il Comando /context

Definizione del Concetto 
Il comando /context è lo strumento diagnostico primario per il Context Management in Claude Code. Digitando questo 
comando nel terminal, si ottiene un'analisi completa e granulare di come il contesto è attualmente distribuito tra le varie 
componenti. 
Spiegazione Approfondita 
Quando digitate /context nel terminal di Claude Code, il sistema produce un report che include: 
1.​
System Prompt: la percentuale occupata dalle istruzioni iniettate da Anthropic 
2.​
System Tools: la percentuale occupata dalle definizioni dei tool di sistema (bash, read, write, edit, etc.) 
3.​
MCP Tools: la percentuale occupata da ogni MCP installato, elencato individualmente 
4.​
Memory Files: la percentuale occupata dai file di memoria (memory.md, auto_memory.md, CLAUDE.md, 
rules, etc.) 
5.​
Skill: la percentuale occupata dalle skill del progetto 
6.​
Messages: la percentuale occupata dalla conversazione attuale 
7.​
Autocompact Buffer: lo spazio riservato per la compattazione automatica 
8.​
Spazio Libero: la percentuale ancora disponibile 
Come Leggere il Report 

--- PAGE 81 ---
Quando vedete il report del contesto, la prima cosa da fare è identificare eventuali anomalie. Un'anomalia è qualsiasi 
componente che occupa una percentuale inaspettatamente alta. Ad esempio: 
●​
Se gli MCP Tools occupano il 27%, avete un problema di contesto 
●​
Se i Messages occupano il 60%, probabilmente è ora di compattare o iniziare una nuova sessione 
●​
Se le Skill occupano più del 2-3%, potreste avere skill troppo verbose che necessitano di ottimizzazione 
Interpretazione Pratica — Workflow di Monitoraggio 
Il monitoraggio del contesto dovrebbe seguire questo workflow: 
 
┌──────────────────────────────────┐ 
│   INIZIO SESSIONE DI LAVORO      │ 
│   → Esegui /context              │ 
│   → Verifica stato iniziale      │ 
│   → Nota la % pre-occupata       │ 
└──────────────┬───────────────────┘ 
               │ 
               ▼ 
┌──────────────────────────────────┐ 
│   DURANTE IL LAVORO              │ 
│   → Ogni 15-20 messaggi, o       │ 
│     quando noti risposte         │ 
│     meno accurate, esegui        │ 
│     /context                     │ 
└──────────────┬───────────────────┘ 
               │ 
               ▼ 
┌──────────────────────────────────┐ 
│   CONTESTO > 60%?                │ 
│                                  │ 
│   SÌ → Compatta con /compact     │ 
│        oppure salva in memoria   │ 
│        e inizia nuova sessione   │ 
│                                  │ 
│   NO → Continua a lavorare       │ 
└──────────────────────────────────┘ 
Perché Monitorare Regolarmente 
Il monitoraggio regolare serve a tre scopi: 
1.​
Prevenzione: identificare problemi di contesto prima che impattino la qualità del lavoro 
2.​
Decisione informata: sapere se potete installare un nuovo MCP o se dovete prima liberare spazio 
3.​
Apprendimento: con il tempo, svilupperete un'intuizione su come le diverse azioni impattano il contesto 
Errori Comuni 
1.​
Monitorare solo quando qualcosa va storto: a quel punto il danno è fatto. Il contesto è già saturo e le risposte 
sono degradate. Monitorate proattivamente. 
2.​ Non sapere che il comando esiste: molti utenti di Claude Code non hanno mai digitato /context. È come 
guidare un'auto senza mai guardare il livello della benzina. 
3.​ Confondere la barra di stato con l'analisi reale: la barra di stato in basso al terminal mostra una percentuale 
approssimativa. Il comando /context è l'unica fonte accurata.

