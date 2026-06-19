# 8.6 — Errori Comuni
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-2-installazione-e > capitolo-8-configurazione]]

## Content

Errore 1: Non abilitare l'Autocompact​
Senza Autocompact, il contesto si riempie progressivamente e non viene mai liberato. Questo porta a una 
degradazione graduale delle performance fino al punto in cui Claude Code non riesce più a operare efficacemente. 
L'Autocompact è la prima impostazione da verificare. 
Errore 2: Disabilitare il Thinking Mode per "velocizzare"​
Il Thinking Mode permette a Claude di ragionare in modo estensivo prima di rispondere. Disabilitarlo rende le risposte 
più rapide ma significativamente meno accurate, specialmente su task complesse. È come chiedere a qualcuno di 
risolvere un problema complesso vietandogli di pensare. 
Errore 3: Non monitorare /context regolarmente​
Molti utenti non sanno nemmeno che il comando /context esiste. Questo li rende "ciechi" rispetto a come il contesto 
viene distribuito. Come vedremo nei capitoli sugli MCP, un singolo MCP può consumare il 27% del contesto senza che 
l'utente se ne renda conto. 
Errore 4: Cambiare configurazioni senza capirne l'impatto​
Ogni impostazione in /config ha implicazioni a cascata. Per esempio, disabilitare i checkpoint in un progetto dove si 
usa bypass permission è una ricetta per il disastro. Ogni modifica di configurazione dovrebbe essere fatta con 
consapevolezza delle conseguenze.

## Collegamenti Correlati
- [[Map - Formazzione|Formazzione Area]]
