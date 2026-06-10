# 32.2 — Procedura di Installazione

Definizione del Concetto 
L'installazione di un MCP può avvenire in diversi modi, dal più semplice (prompt a Claude) al più manuale (editing 
diretto del file JSON). 
Metodo 1 — Installazione Tramite Prompt (Raccomandato) 
Il metodo più semplice, mostrato nella guida: 
text 
"Per favore installa il [nome] MCP da questo link:  
[link alla pagina del MCP o al JSON di configurazione]" 
Claude: 
1.​
Legge il link o il JSON fornito 
2.​
Identifica il tipo di MCP 
3.​
Scarica e configura automaticamente 
4.​ Aggiorna il file .mcp.json 
5.​
Conferma l'installazione 
Esempio concreto dalla guida per Chrome Dev Tool: 
text 
"Per favore installa Dev Tool MCP" 
Claude cerca la documentazione, trova il JSON di configurazione e lo installa automaticamente. 
Metodo 2 — Installazione Tramite Dev Tool MCP 

--- PAGE 158 ---
Un metodo particolarmente elegante mostrato nella guida: usare il Chrome Dev Tool MCP (già installato) per navigare 
alla pagina di un altro MCP e installarlo: 
text 
"Per favore, usando il Dev Tool MCP, guarda questo  
link [pagina del MCP su GitHub] e collegami l'MCP  
di ClickUp a questo progetto." 
In questo caso, Claude: 
1.​
Usa il Dev Tool MCP per navigare alla pagina GitHub del MCP 
2.​
Legge le istruzioni di installazione dalla pagina 
3.​
Identifica il JSON di configurazione 
4.​
Installa l'MCP seguendo le istruzioni trovate 
Metodo 3 — Installazione con Comando Specifico 
Alcuni MCP hanno comandi di installazione specifici. Dalla guida, l'esempio di ClickUp: 
"Cloud Code, use the following command. Once you open Claude Code session, run [comando] to go through the 
authentication flow." 
In questo caso: 
1.​
Copiate il comando dalla documentazione del MCP 
2.​
Incollatelo nel terminal di Claude Code 
3.​
Seguite il processo di autenticazione (se richiesto) 
4.​
Riavviate la sessione di Claude Code 
5.​ Verificate con /mcp che l'MCP sia attivo 
Il Processo di Autenticazione 
Molti MCP richiedono un processo di autenticazione per accedere al servizio esterno. La guida mostra questo processo 
con l'esempio di ClickUp: 
 
PROCESSO DI AUTENTICAZIONE MCP 
══════════════════════════════ 
 
Passo 1: Installazione dell'MCP 
    → Claude configura il server MCP locale 
 
Passo 2: Riavvio della sessione 
    → "Chiudi e riavvia Claude Code" 
 
Passo 3: Verifica connessione 
    → Eseguire /mcp per verificare lo stato 
 
Passo 4: Autenticazione 
    → "ClickUp ha bisogno di un'autenticazione" 
    → "Enter to confirm" 
    → Si apre il browser 
    → Login nel servizio (es: ClickUp) 
    → Autorizzazione dell'accesso 
 
Passo 5: Conferma 
    → Il terminale conferma la connessione 

--- PAGE 159 ---
    → L'MCP è ora operativo

