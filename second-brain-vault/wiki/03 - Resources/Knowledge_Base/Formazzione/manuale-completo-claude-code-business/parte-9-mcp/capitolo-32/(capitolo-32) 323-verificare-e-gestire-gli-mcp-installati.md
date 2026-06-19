# 32.3 — Verificare e Gestire gli MCP Installati
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-9-mcp > capitolo-32]]

## Content

Definizione del Concetto 
Dopo l'installazione, è fondamentale verificare che l'MCP funzioni correttamente e monitorare il suo impatto sul 
contesto. 
Il Comando /mcp 
Per verificare quali MCP sono installati e il loro stato: 
 
/mcp 
Questo comando mostra: 
●​
L'elenco degli MCP installati 
●​
Lo stato di ciascuno (connesso, disconnesso, errore) 
●​
Eventuali problemi di autenticazione 
Verificare l'Impatto sul Contesto 
Immediatamente dopo l'installazione di un nuovo MCP, eseguite: 
 
/context 
E confrontate i numeri con quelli precedenti all'installazione. Se l'impatto è eccessivo (più del 5-10% per un singolo 
MCP), valutate se ne vale la pena. 
Come Rimuovere un MCP 
La rimozione è altrettanto semplice dell'installazione: 
 
"Per favore rimuovi l'MCP [nome]" 
L'autore della guida lo dimostra con l'esempio di Canva: 
"Per favore puoi rimuovere il mio Cloud AI Canva MCP? Non mi serve." 
Claude rimuove la configurazione dal file .mcp.json e libera il contesto corrispondente. 
La Gestione come Routine 

--- PAGE 160 ---
L'installazione e la rimozione degli MCP dovrebbe essere una routine consapevole, non un'azione casuale: 
 
ROUTINE DI GESTIONE MCP 
═══════════════════════ 
 
PRIMA DI INIZIARE UN PROGETTO: 
□ Verificare quali MCP sono installati (/mcp) 
□ Verificare il loro impatto sul contesto (/context) 
□ Rimuovere MCP non necessari per questo progetto 
□ Installare MCP specifici necessari per questo progetto 
 
DURANTE IL LAVORO: 
□ Monitorare il contesto regolarmente 
□ Se un MCP non viene più usato → rimuoverlo 
 
ALLA FINE DEL PROGETTO: 
□ Rimuovere MCP project-specific 
□ Mantenere solo MCP globali (es: Chrome Dev Tool)

## Collegamenti Correlati
- [[Map - Formazzione|Formazzione Area]]
