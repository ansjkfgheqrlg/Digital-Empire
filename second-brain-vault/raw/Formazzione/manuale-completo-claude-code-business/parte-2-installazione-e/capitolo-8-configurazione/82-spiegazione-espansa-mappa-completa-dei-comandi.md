# 8.2 — Spiegazione Espansa: Mappa Completa dei Comandi

L'autore introduce i comandi nel corso della guida in modo progressivo. Qui li raccogliamo tutti in una mappa 
organizzata per funzione: 
Comandi di Inizializzazione e Gestione Progetto 
/init 
├── Funzione: Inizializza un nuovo progetto Claude Code 
├── Cosa fa: Analizza i file presenti nella cartella, 
│           legge il codice esistente, comprende la struttura, 
│           e genera un CLAUDE.md strutturato secondo le best practice 
├── Quando usarlo: Sempre all'inizio di un nuovo progetto 
├── Quando è particolarmente utile: 
│   • Quando importate un progetto da qualcun altro 
│   • Quando il team vi manda script e risorse 
│   • Quando volete ricreare il CLAUDE.md dopo modifiche importanti 
└── Nota importante: Se avete impostazioni globali (~/.claude), 
    il /init le incorpora automaticamente nel nuovo CLAUDE.md 
L'autore sottolinea un vantaggio sottile ma potente di /init: se esiste un comando che rimanda a "come si crea un 
CLAUDE.md" per tutti i processi, quel file verrà strutturato in modo identico ogni volta. Questo crea standardizzazione: 
"Tutti runnando quel comando abbiano lo stesso, e questo crea un'efficienza non da ridere." 
Comandi di Context Management 
/context 
├── Funzione: Mostra un'analisi dettagliata della distribuzione del contesto 
├── Cosa mostra: 
│   • System prompt (injection di Anthropic) → ~10-12% 
│   • System tools → % 
│   • MCP tools → % (può essere molto alto!) 
│   • Memory files → % 
│   • Skills → % 
│   • Custom agents → % 
│   • Messages (la conversazione) → % 
│   • Spazio libero → % 
└── Perché è critico: Permette di capire dove il contesto viene consumato 
    e identificare sprechi 
 
/compact 
├── Funzione: Compatta manualmente il contesto della conversazione 
├── Cosa fa: Riscrive l'intera conversazione in formato ad alta densità 
│           (bullet point, eliminazione ridondanze, compressione) 
├── Esempio di compattazione: 
│   PRIMA: "Ho chiesto a Claude di importare i tre sub-agenti che sono 
│           il reviewer, il researcher e il QA. Poi ho chiesto di fare 
│           un review completo del codice..." 
│   DOPO:  "• Importati 3 sub-agenti: reviewer, researcher, QA 
│           • Review codice completato" 
├── Quando usarlo: Quando il contesto supera il 60-70% 
│                  o quando notate degradazione delle performance 
└── Nota: L'Autocompact fa la stessa cosa ma automaticamente 
         quando si raggiunge la soglia del buffer (~33K token) 
Comandi di Gestione Sessione 
clear (nel prompt Claude) 
├── Funzione: Pulisce la conversazione corrente 
└── Nota: Non cancella la memoria o le configurazioni 
 
clear context 
├── Funzione: Pulisce il contesto della conversazione 
└── Quando usarlo: Quando volete iniziare una nuova conversazione 

--- PAGE 26 ---
    mantenendo le configurazioni del progetto 
Comandi di Gestione MCP e Permessi 
/mcp 
├── Funzione: Gestisce i Model Context Protocol installati 
├── Cosa mostra: Lista degli MCP attivi e il loro stato 
└── Quando usarlo: Per verificare connessioni, autenticarsi, 
    o risolvere problemi con MCP 
 
permissions (nel prompt di configurazione) 
├── Funzione: Gestisce i permessi dei tool 
├── Opzioni: 
│   • Allow: Il tool è sempre permesso (nessuna richiesta) 
│   • Ask: Chiede sempre permesso prima di usare il tool 
│   • Deny: Il tool non viene mai usato 
│   • Workspace: Permessi specifici per il workspace corrente 
└── Nota critica: I permessi dell'agente principale si replicano 
    a TUTTI i sotto-agenti (downstream)

