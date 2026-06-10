# 34.2 — Funzionalità del Chrome Dev Tool MCP
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-9-mcp > capitolo-34]]

## Content

Definizione del Concetto 
Il Chrome Dev Tool MCP fornisce a Claude la capacità di controllare un browser Chrome come se fosse un utente 
umano. Può navigare pagine, leggere contenuti, fare screenshot, cliccare elementi e interagire con interfacce web. 
Le Capacità Specifiche 
 
FUNZIONALITÀ DEL CHROME DEV TOOL MCP 
═════════════════════════════════════ 
 
1. NAVIGAZIONE WEB 
   └── Aprire URL specifici 
   └── Navigare tra pagine 
   └── Seguire link 
   └── Es: "Vai alla documentazione ufficiale di Anthropic" 
 
2. SCREENSHOT 
   └── Catturare screenshot di pagine web 
   └── Screenshot full-page 
   └── Screenshot di elementi specifici 
   └── Es: "Fai uno screenshot del sito e confrontalo  
            con l'immagine di riferimento" 
 
3. LETTURA CONTENUTI 
   └── Leggere il testo di una pagina web 
   └── Estrarre informazioni strutturate 
   └── Fare summary di pagine 
   └── Es: "Leggi questa pagina e fammene un riassunto" 
 
4. INTERAZIONE 
   └── Cliccare bottoni 
   └── Compilare form 
   └── Scrollare pagine 
   └── Es: "Vai su Google e cerca [query]" 
 
5. SCRAPING 
   └── Estrarre dati da pagine web 
   └── Raccogliere informazioni strutturate 

--- PAGE 166 ---
   └── Es: "Raccogli tutti i prezzi da questa pagina" 
Applicazioni Pratiche dalla Guida 
1. Verifica di siti web costruiti:​
Il Chrome Dev Tool MCP è fondamentale per il ciclo di verifica screenshot nella costruzione di siti. Claude può: 
●​
Fare screenshot del sito in costruzione 
●​
Confrontarlo con l'immagine di riferimento 
●​
Identificare le differenze 
●​
Correggerle 
●​
Ripetere il ciclo 
2. Ricerca senza API: 
"Quando non ci sono API, potrete usare questo tool qui e vi permette di girare nel web." 
Questo è un caso d'uso cruciale: molti servizi non offrono API pubbliche. Con il Chrome Dev Tool MCP, Claude può 
comunque interagire con questi servizi navigando la loro interfaccia web come farebbe un umano. 
3. Pubblicazione su piattaforme: 
Nella skill "publish" dell'autore, Instagram viene gestito tramite Chrome Dev Tool MCP perché non è pratico usare l'API 
di Instagram: 
"YouTube: Python API. Instagram: tramite Chrome Dev Tool MCP." 
Questo mostra come l'MCP può essere integrato nelle skill come strumento complementare. 
4. Installazione di altri MCP: 
Come visto nel Capitolo 32, il Chrome Dev Tool MCP può essere usato per navigare alle pagine GitHub di altri MCP, 
leggere le istruzioni di installazione e aiutare a installarli.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
