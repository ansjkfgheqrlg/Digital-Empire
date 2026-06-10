# 31.2 — Tipologie di MCP

Definizione del Concetto 
Non tutti gli MCP sono uguali. Esistono differenze significative tra gli MCP in termini di peso (consumo di contesto), 
modalità di funzionamento e origine (chi li ha sviluppati). Comprendere queste differenze è essenziale per prendere 
decisioni informate su quali installare. 

--- PAGE 153 ---
MCP Leggeri vs MCP Pesanti 
La guida originale dimostra questa distinzione con dati concreti: 
text 
CONFRONTO: MCP LEGGERO vs MCP PESANTE 
══════════════════════════════════════ 
 
MCP LEGGERO — Chrome Dev Tool: 
┌──────────────────────────────────┐ 
│ Consumo contesto: ~0,1%         │ 
│ Funzionalità: navigazione web,  │ 
│ screenshot, scraping             │ 
│ Numero di "skill interne": poche│ 
│ Descrizioni: concise             │ 
│ IMPATTO: trascurabile            │ 
└──────────────────────────────────┘ 
 
MCP PESANTE — ClickUp: 
┌──────────────────────────────────┐ 
│ Consumo contesto: ~27%          │ 
│ Funzionalità: gestione completa │ 
│ dei progetti e task              │ 
│ Numero di "skill interne": molte│ 
│ Descrizioni: dettagliate        │ 
│ IMPATTO: devastante             │ 
└──────────────────────────────────┘ 
 
DIFFERENZA: 270 volte più pesante! 
Un MCP leggero come Chrome Dev Tool occupa lo 0,1% del contesto. Un MCP pesante come ClickUp occupa il 27%. 
Questo significa che ClickUp è 270 volte più pesante di Chrome Dev Tool in termini di impatto sul contesto. 
MCP Built-in vs MCP di Terze Parti 
La guida menziona che Claude Code ha già degli MCP built-in (integrati): 
text 
TIPOLOGIE DI MCP PER ORIGINE 
═════════════════════════════ 
 
1. BUILT-IN (integrati in Claude Code): 
   └── Già presenti, non richiedono installazione 
   └── Fanno parte del system prompt 
   └── Consumo incluso nel 10% base del system prompt 
 
2. DI TERZE PARTI (installati dall'utente): 
   └── Richiedono installazione manuale 
   └── Aggiungono consumo di contesto AGGIUNTIVO 
   └── Qualità e sicurezza variabili 
   └── Possono contenere malware → ATTENZIONE 
 
3. CUSTOM (creati dall'utente): 
   └── Configurati nel file .mcp.json del progetto 
   └── Completamente sotto il vostro controllo 
   └── Consumo dipende dalla complessità 
MCP "On-Demand" vs MCP "Always-On" 
Un concetto importante che emerge dalla guida è la distinzione tra MCP che vengono caricati sempre e MCP che 
vengono chiamati solo quando necessario: 

--- PAGE 154 ---
"Non tutti gli MCP sono i cosiddetti MCP di third, che vengono chiamati solamente a chiamata o a bisogno." 
Questo è un punto tecnico cruciale: 
Tipo 
Comportamento 
Impatto Contesto 
Always-On 
Le descrizioni di tutte le funzionalità sono caricate SEMPRE nel 
contesto 
PERMANENTE — occupa contesto anche quando 
non lo usate 
On-Demand 
Le descrizioni vengono caricate solo quando l'MCP viene 
effettivamente chiamato 
TEMPORANEO — occupa contesto solo durante 
l'uso 
Il problema principale è che la maggior parte degli MCP di terze parti sono Always-On: le loro descrizioni vengono 
caricate nel contesto all'avvio della sessione e ci restano per tutta la durata, consumando spazio anche quando non 
state usando quel servizio. 
Implicazione Pratica 
Questa distinzione ha un'implicazione enorme per la strategia di utilizzo: 
●​
Se installate 3 MCP pesanti (tutti Always-On), potreste trovarvi con il 60-80% del contesto occupato prima 
ancora di scrivere il primo messaggio 
●​
È come salire in macchina con il bagagliaio pieno di attrezzi che non userete mai durante quel viaggio: 
occupano spazio e rendono la macchina più lenta

