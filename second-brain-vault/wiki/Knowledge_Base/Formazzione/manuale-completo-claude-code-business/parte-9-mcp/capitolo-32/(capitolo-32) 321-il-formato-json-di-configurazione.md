# 32.1 — Il Formato JSON di Configurazione
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-9-mcp > capitolo-32]]

## Content

Definizione del Concetto 
Ogni MCP ha un file di configurazione in formato JSON che contiene le informazioni necessarie per il collegamento. 
Questo JSON definisce come Claude Code deve comunicare con il servizio esterno. 
Spiegazione Approfondita 
La guida spiega il formato JSON: 
"Questo non è altro che un formato JSON che io ora ho copiato. Il formato JSON lo vediamo perché è contenuto in 
parentesi graffe, ha la prima parte che si chiamano key (chiavi), la seconda parte che si chiamano value (valori), e sono 
divisi da questi due punti." 

--- PAGE 156 ---
Un file di configurazione MCP ha tipicamente questa struttura: 
JSON 
{ 
  "mcpServers": { 
    "nome-del-servizio": { 
      "command": "npx", 
      "args": [ 
        "-y", 
        "@nome-pacchetto/mcp-server" 
      ], 
      "env": { 
        "API_KEY": "la-vostra-chiave-api", 
        "WORKSPACE_ID": "il-vostro-workspace" 
      } 
    } 
  } 
} 
Analisi della struttura: 
Elemento 
Significato 
mcpServers 
Contenitore di tutti gli MCP configurati 
nome-del-servizio 
Identificativo dell'MCP (es: "clickup", "chrome-devtools") 
command 
Il comando per avviare il server MCP 
args 
Gli argomenti passati al comando 
env 
Le variabili d'ambiente (API key, credenziali, etc.) 
Dove Va il File di Configurazione 
Il file di configurazione MCP si chiama .mcp.json e può essere posizionato a diversi livelli: 

--- PAGE 157 ---
text 
POSIZIONAMENTO DEL FILE .mcp.json 
═════════════════════════════════ 
 
LIVELLO LOCAL (dentro il progetto): 
progetto/ 
└── .mcp.json          ← MCP disponibili solo in questo progetto 
 
LIVELLO GLOBAL (nel computer dell'utente): 
~/.claude/ 
└── .mcp.json          ← MCP disponibili in TUTTI i progetti 
La scelta del posizionamento segue la stessa logica delle regole e dei sub-agenti: 
●​
Local: quando l'MCP serve solo per un progetto specifico 
●​
Global: quando l'MCP è utile in tutti i progetti (come Chrome Dev Tool)

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
