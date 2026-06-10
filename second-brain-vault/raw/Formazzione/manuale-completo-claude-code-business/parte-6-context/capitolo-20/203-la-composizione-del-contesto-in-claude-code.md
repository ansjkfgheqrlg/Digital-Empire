# 20.3 — La Composizione del Contesto in Claude Code

Definizione del Concetto 
Il contesto in Claude Code non è composto solo dalla vostra conversazione. È un aggregato di molteplici fonti che 
vengono tutte caricate nella finestra di contesto prima e durante la sessione di lavoro. Comprendere questa 
composizione è essenziale per gestire il contesto in modo professionale. 
Spiegazione Approfondita — Mappa Completa del Contesto 
Dalla guida originale e dall'analisi pratica del comando /context, sappiamo che il contesto è composto dalle seguenti 
componenti, elencate nell'ordine in cui vengono caricate: 
 
╔══════════════════════════════════════════════════════════════╗ 

--- PAGE 76 ---
║                    FINESTRA DI CONTESTO                      ║ 
║                     (es. 200.000 token)                      ║ 
╠══════════════════════════════════════════════════════════════╣ 
║                                                              ║ 
║  ┌─────────────────────────────────────────────────────┐     ║ 
║  │  1. SYSTEM PROMPT (iniettato da Anthropic)          │     ║ 
║  │     → Non modificabile dall'utente                  │     ║ 
║  │     → Circa 10-12% del contesto                     │     ║ 
║  └─────────────────────────────────────────────────────┘     ║ 
║                                                              ║ 
║  ┌─────────────────────────────────────────────────────┐     ║ 
║  │  2. SYSTEM TOOLS                                    │     ║ 
║  │     → Comandi bash, read, write, edit, etc.         │     ║ 
║  │     → Definizioni dei tool disponibili              │     ║ 
║  └─────────────────────────────────────────────────────┘     ║ 
║                                                              ║ 
║  ┌─────────────────────────────────────────────────────┐    ║ 
║  │  3. MCP TOOLS                                       │    ║ 
║  │     → Chrome Dev Tool, ClickUp, etc.                │    ║ 
║  │     → VARIABILE: da 0,1% a 27%+ del contesto       │     ║ 
║  └─────────────────────────────────────────────────────┘    ║ 
║                                                             ║ 
║  ┌─────────────────────────────────────────────────────┐    ║ 
║  │  4. MEMORY FILES                                    │    ║ 
║  │     → memory.md                                     │    ║ 
║  │     → auto_memory.md                                │    ║ 
║  │     → CLAUDE.md del progetto                        │    ║ 
║  │     → Rules del workspace                           │    ║ 
║  └─────────────────────────────────────────────────────┘    ║ 
║                                                             ║ 
║  ┌─────────────────────────────────────────────────────┐    ║ 
║  │  5. SKILL                                           │    ║ 
║  │     → Generalmente molto leggere (~0,3%)            │    ║ 
║  └─────────────────────────────────────────────────────┘    ║ 
║                                                             ║ 
║  ┌─────────────────────────────────────────────────────┐    ║ 
║  │  6. MESSAGGI (la vostra conversazione)              │    ║ 
║  │     → Input dell'utente + Output di Claude          │    ║ 
║  │     → Cresce con ogni scambio                       │    ║ 
║  └─────────────────────────────────────────────────────┘    ║ 
║                                                             ║ 
║  ┌─────────────────────────────────────────────────────┐    ║ 
║  │  7. AUTOCOMPACT BUFFER                              │    ║ 
║  │     → ~33.000 token riservati                       │    ║ 
║  │     → Spazio per la compattazione automatica        │    ║ 
║  └─────────────────────────────────────────────────────┘    ║ 
║                                                             ║ 
║  ┌─────────────────────────────────────────────────────┐    ║ 
║  │  8. SPAZIO LIBERO                                   │    ║ 
║  │     → Disponibile per nuovi messaggi e operazioni   │    ║ 
║  └─────────────────────────────────────────────────────┘    ║ 
║                                                             ║ 
╚══════════════════════════════════════════════════════════════╝ 
Il Problema del Contesto "Pre-Occupato" 
Un dato fondamentale emerso dalla guida originale è questo: prima ancora di scrivere il vostro primo messaggio, una 
percentuale significativa del contesto è già occupata. 
Nell'esempio pratico mostrato nella guida: 
Componente 
% del Contesto 

--- PAGE 77 ---
System Prompt (Anthropic) 
~10% 
System Tools 
~0,7% 
MCP Tools (solo Chrome Dev Tool) 
~0,1% 
Memory Files 
~4-5% 
Skill 
~0,3% 
Totale pre-occupato (configurazione leggera) 
~15-16% 
Ma quando vengono installati MCP pesanti: 
Componente 
% del Contesto 
System Prompt (Anthropic) 
~10% 
System Tools 
~0,7% 
MCP Tools (Chrome Dev Tool + ClickUp + Canva) 
~28% 

--- PAGE 78 ---
Memory Files 
~4-5% 
Skill 
~0,3% 
Totale pre-occupato (configurazione pesante) 
~43% 
Questo significa che nel secondo caso, quasi metà del contesto è già occupata prima ancora di cominciare a lavorare. 
Restate con solo il 57% per la vostra effettiva conversazione e il lavoro produttivo. 
Perché Questo è Critico 
Immaginate di avere un serbatoio da 100 litri per un viaggio. Se prima di partire qualcuno ci mette dentro 43 litri di 
sabbia, vi restano solo 57 litri per la benzina. Arriverete molto meno lontano. 
Lo stesso vale per il contesto. Se il 43% è occupato da MCP che forse non vi servono, avrete: 
●​
Meno spazio per conversazioni complesse 
●​
Compattazioni più frequenti (con perdita potenziale di informazioni) 
●​
Qualità delle risposte degradata più rapidamente 
●​
Sessioni di lavoro più corte prima di dover resettare 
Interpretazione Pratica — Come Verificare 
Per vedere la composizione esatta del vostro contesto in qualsiasi momento, utilizzate il comando: 
 
/context 
Questo comando produce un'analisi dettagliata che mostra: 
●​
Ogni componente del contesto 
●​
La percentuale occupata da ciascuno 
●​
Il totale utilizzato 
●​
Lo spazio libero rimanente 
Questo è il vostro cruscotto di guida. Consultarlo regolarmente è un'abitudine che distingue l'utente esperto dal 
principiante. 
Errori Comuni 
1.​ Non controllare mai il contesto: molti utenti non sanno nemmeno che il comando /context esiste. Volano alla 
cieca. 

--- PAGE 79 ---
2.​
Attribuire errori di Claude alla "stupidità del modello" quando in realtà il contesto è saturo: se Claude inizia a 
dimenticare istruzioni o a dare risposte incoerenti, la prima cosa da verificare è la percentuale di contesto 
utilizzata. 
3.​
Non considerare il costo degli MCP: come visto, un singolo MCP come ClickUp può occupare il 27% del 
contesto. È un prezzo enorme da pagare se non lo state effettivamente usando. 
Insight Avanzato 
La percentuale di contesto utilizzato e la percentuale di contesto nella barra di stato non sono necessariamente uguali. 
La guida originale nota specificamente questa discrepanza. Il motivo è che la barra di stato mostra una stima 
semplificata, mentre il comando /context fornisce l'analisi granulare reale. Usate sempre /context per le decisioni 
importanti.

