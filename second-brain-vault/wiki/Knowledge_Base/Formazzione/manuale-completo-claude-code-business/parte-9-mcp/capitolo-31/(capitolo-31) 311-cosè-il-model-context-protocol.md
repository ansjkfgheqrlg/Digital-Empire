# 31.1 — Cos'è il Model Context Protocol
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-9-mcp > capitolo-31]]

## Content

Definizione del Concetto 
L'MCP (Model Context Protocol) è un protocollo standardizzato che permette di collegare servizi e applicazioni di terze 
parti direttamente a Claude Code. Quando installate un MCP, Claude acquisisce automaticamente la capacità di 
interagire con quel servizio esterno — leggere dati, scrivere dati, eseguire operazioni — senza che dobbiate scrivere 
codice o creare skill manualmente. 
Spiegazione Approfondita 
L'analogia usata nella guida originale è perfetta per comprendere il concetto: 
"Potete vederlo semplicemente come una chiavetta USB universale che se voi avete e connettete ad un altro sistema di 
terze parti, sviluppato da qualcun altro, vi permette di ereditare tutte le funzioni di questa applicazione." 
Espandiamo questa analogia per renderla completamente chiara: 
text 
ANALOGIA: MCP COME CHIAVETTA USB UNIVERSALE 
════════════════════════════════════════════ 
 
SENZA MCP: 
┌─────────────────┐          ┌─────────────────┐ 
│   CLAUDE CODE   │    ✗     │    CLICKUP      │ 
│                 │◄─────────│                 │ 
│  "Non so come   │  Nessuna │  "Ho tutte le   │ 
│   interagire    │  connes- │   funzionalità  │ 
│   con ClickUp"  │  sione   │   ma Claude non │ 
│                 │          │   può usarmi"   │ 
└─────────────────┘          └─────────────────┘ 
 
CON MCP: 
┌─────────────────┐          ┌─────────────────┐ 
│   CLAUDE CODE   │          │    CLICKUP      │ 
│                 │◄════╗    │                 │ 
│  "Ora so fare   │  ║MCP║   │  "Claude ora    │ 
│   tutto quello  │  ║   ║   │   può usare     │ 
│   che ClickUp   │  ╚═══╝   │   tutte le mie  │ 
│   sa fare!"     │  chiavetta│   funzionalità" │ 
│                 │  USB      │                 │ 
└─────────────────┘          └─────────────────┘ 
Quando collegate la "chiavetta USB" (l'MCP), Claude eredita automaticamente tutte le capacità dell'applicazione 
collegata. Se collegate l'MCP di ClickUp, Claude sa: 
●​
Creare task in ClickUp 
●​
Leggere le board 
●​
Assegnare compiti 
●​
Aggiornare stati 
●​
Cercare nel workspace 
●​
E tutte le altre funzionalità che ClickUp espone tramite il suo MCP 
Il Meccanismo Sottostante 
Per comprendere perché gli MCP funzionano, bisogna capire che un MCP è essenzialmente un pacchetto di skill 
pre-costruite dal fornitore del servizio: 

--- PAGE 152 ---
text 
STRUTTURA CONCETTUALE DI UN MCP 
═══════════════════════════════ 
 
MCP di ClickUp = insieme di skill pre-costruite: 
 
    ┌────────────────────────────────────────────┐ 
    │              MCP CLICKUP                    │ 
    │                                             │ 
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐ │ 
    │  │ Skill 1  │  │ Skill 2  │  │ Skill 3  │ │ 
    │  │ "Crea    │  │ "Leggi   │  │ "Assegna │ │ 
    │  │  task"   │  │  board"  │  │  task"   │ │ 
    │  └──────────┘  └──────────┘  └──────────┘ │ 
    │                                             │ 
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐ │ 
    │  │ Skill 4  │  │ Skill 5  │  │ Skill 6  │ │ 
    │  │ "Aggiorna│  │ "Cerca   │  │ "Crea    │ │ 
    │  │  stato"  │  │  task"   │  │  progetto│ │ 
    │  └──────────┘  └──────────┘  └──────────┘ │ 
    │                                             │ 
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐ │ 
    │  │ Skill 7  │  │ Skill 8  │  │  ...     │ │ 
    │  │ "Elimina │  │ "Commenta│  │          │ │ 
    │  │  task"   │  │  task"   │  │          │ │ 
    │  └──────────┘  └──────────┘  └──────────┘ │ 
    │                                             │ 
    └────────────────────────────────────────────┘ 
Ognuna di queste "skill interne" all'MCP ha: 
●​
Una descrizione di cosa fa 
●​
I parametri che accetta 
●​
Il formato della risposta 
●​
Le istruzioni per Claude su come utilizzarla 
Tutte queste descrizioni vengono caricate nel contesto di Claude quando l'MCP è installato. Ed è esattamente qui che 
nasce il problema principale degli MCP, che vedremo in dettaglio nel Capitolo 33. 
Perché l'MCP è Diventato Comune Solo Recentemente 
La guida menziona un dettaglio temporale importante: 
"Solo ultimamente è diventato molto più comune e molto più utilizzato." 
Questo accade perché il protocollo MCP è relativamente nuovo e la sua adozione è stata graduale. All'inizio, pochi 
servizi offrivano MCP compatibili con Claude Code. Man mano che Claude Code è cresciuto in popolarità e che 
Anthropic ha standardizzato il protocollo, sempre più aziende hanno iniziato a creare i propri MCP. 
L'effetto è stato una rapida espansione dell'ecosistema: oggi esistono centinaia di MCP per servizi diversi — da ClickUp 
a GitHub, da Slack a database, da servizi email a strumenti di analytics.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
