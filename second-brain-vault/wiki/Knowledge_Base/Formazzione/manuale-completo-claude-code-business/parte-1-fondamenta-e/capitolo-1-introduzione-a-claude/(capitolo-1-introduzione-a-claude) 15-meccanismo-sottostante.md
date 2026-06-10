# 1.5 — Meccanismo Sottostante
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-1-fondamenta-e > capitolo-1-introduzione-a-claude]]

## Content

Il funzionamento di Claude Code si basa su un modello di linguaggio (LLM) che ha accesso a una serie di "strumenti" 
(tools): 
[Utente] → scrive un prompt in linguaggio naturale 
     ↓ 
[Claude Code] → interpreta il prompt 
     ↓ 
[Strumenti] → esegue azioni reali (bash commands, file editing, web navigation) 
     ↓ 
[Output] → risultato visibile (codice modificato, file creato, sito costruito) 
Ogni volta che l'utente scrive qualcosa, Claude Code non si limita a generare testo. Può decidere di: 
●​
Leggere un file specifico nel progetto per capire il contesto 
●​
Eseguire un comando nel terminal 
●​
Modificare righe di codice 
●​
Creare nuovi file 
●​
Chiamare un sotto-agente per un compito specifico 
●​
Navigare nel web per fare ricerche 
●​
Fare uno screenshot per verificare il risultato visivo

## Collegamenti Correlati
- [[Map - Formazzione|Formazzione Area]]
