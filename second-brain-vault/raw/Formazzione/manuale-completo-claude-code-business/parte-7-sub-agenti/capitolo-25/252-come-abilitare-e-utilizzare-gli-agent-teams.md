# 25.2 — Come Abilitare e Utilizzare gli Agent Teams

Definizione del Concetto 
Gli Agent Teams funzionano attualmente solo nel terminal e richiedono un processo di abilitazione specifico. Non sono 
disponibili nella GUI degli IDE (VS Code o Antigravity). 
Procedura di Abilitazione 
La guida mostra il processo pratico: 
Passo 1 — Consultare la documentazione: 
text 
"Per favore, utilizzando questa documentazione  
[link alla documentazione ufficiale],  
potresti abilitarmi gli Agent Teams?" 
Passo 2 — Claude configura il sistema:​
Claude legge la documentazione e configura automaticamente gli Agent Teams nel vostro ambiente. 
Passo 3 — Verificare l'abilitazione:​
Dopo la configurazione, Claude conferma che gli Agent Teams sono abilitati e vi spiega come usarli. 
Come Creare un Team per una Task Specifica 
Una volta abilitati, potete creare un team con un singolo prompt: 
text 
"Crea un agent team con un massimo di [N] compagni  
di squadra per [descrizione della task].  
 
Vorrei che ogni teammate avesse un ruolo specifico  
e che analizzassero [cosa] in parallelo. 
 
Alla fine, portami [tipo di risultato desiderato]." 
Esempio concreto dalla guida: 
text 
"Ho una repository [link]. Vorrei che tu la analizzassi  
creando un agent team con un massimo di quattro compagni  
di squadra. Vorrei che poi tu mi portassi delle migliorie  
che possiamo fare a tutto tondo, non solo in ambito sicurezza  
ma anche a livello di codice." 

--- PAGE 118 ---
Navigazione e Monitoraggio durante l'Esecuzione 
Durante l'esecuzione di un Agent Team: 
Azione 
Tasto/Comando 
Risultato 
Vedere i teammate attivi 
Guarda la barra in basso 
Mostra: main, architect, code quality, etc. 
Navigare tra i teammate 
Shift + freccia giù 
Visualizzazione live con dettagli 
Vedere il consumo di contesto 
Visualizzazione live 
Token e % per ogni teammate 
Vedere i tool chiamati 
Visualizzazione live 
Numero di tool call per teammate 
Vedere il costo in tempo reale 
Status line 
Costo cumulativo aggiornato

