# 20.1 — Introduzione al Concetto di Contesto
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-6-context > capitolo-20]]

## Content

Definizione del Concetto 
Quando si parla di contesto in Claude Code, ci si riferisce alla quantità totale di informazioni che il modello di linguaggio 
(LLM) è in grado di "tenere in mente" durante una singola sessione di lavoro. Immaginate il contesto come la memoria 
di lavoro di Claude: tutto ciò che il sistema sa, vede, ricorda e può utilizzare per rispondere ai vostri prompt in un dato 
momento. 
Questa memoria di lavoro non è infinita. Ha una dimensione massima fissa, misurata in unità chiamate token. Una volta 
che questa memoria si riempie, il sistema deve fare delle scelte: comprimere informazioni precedenti, dimenticarne 
alcune o degradare nella qualità delle risposte. 
Spiegazione Approfondita 
Il contesto funziona esattamente come una scrivania fisica. Immaginate di avere una scrivania di dimensioni fisse: 
●​
Potete appoggiarci sopra documenti, foto, appunti, strumenti 
●​
Più cose ci mettete, meno spazio avete per lavorare 
●​
Se la scrivania si riempie completamente, dovete togliere qualcosa per fare spazio a qualcosa di nuovo 
●​
Se ammassate troppa roba, non riuscite più a trovare quello che vi serve 
In Claude Code, questa "scrivania" contiene: 
●​
Le istruzioni di sistema iniettate da Anthropic (il system prompt) 
●​
Il vostro file CLAUDE.md e tutte le regole del progetto 
●​
I file di memoria (memory.md) 
●​
Le definizioni dei tool di sistema 
●​
Le definizioni degli MCP installati 
●​
Le skill caricate 
●​
Tutta la vostra conversazione (ogni messaggio che avete scritto e ogni risposta di Claude) 

--- PAGE 72 ---
Perché Questo Concetto è Fondamentale 
Comprendere il contesto è la differenza tra usare Claude Code come un chatbot qualsiasi e usarlo come uno strumento 
professionale che genera valore reale. Senza questa comprensione: 
●​
Non capirete perché Claude "dimentica" cose che gli avete detto 
●​
Non capirete perché le risposte diventano meno accurate dopo conversazioni lunghe 
●​
Non saprete come organizzare le informazioni per ottenere risultati migliori 
●​
Sprecherete contesto prezioso con informazioni irrilevanti 
●​
Non potrete fare scelte informate su cosa installare (MCP, skill, sub-agenti) 
Interpretazione Pratica 
A livello pratico, gestire il contesto significa: 
1.​
Sapere quanto contesto è stato usato in ogni momento 
2.​
Sapere da cosa è occupato (conversazione? MCP? system prompt?) 
3.​
Decidere consapevolmente cosa aggiungere e cosa togliere 
4.​
Scrivere prompt concisi che non sprechino spazio 
5.​
Strutturare il progetto in modo da minimizzare l'occupazione di contesto inutile 
Errori Comuni 
Errore 
Conseguenza 
Soluzione 
Ignorare completamente il contesto 
L'LLM perde coerenza dopo pochi messaggi 
Monitorare regolarmente con /context 
Installare troppi MCP 
contemporaneamente 
Il contesto si riempie prima ancora di iniziare a 
lavorare 
Installare solo ciò che serve, convertire in 
skill 
Scrivere prompt lunghissimi e ridondanti 
Spreco di token preziosi 
Aumentare la densità informativa dei prompt 
Non fare mai compattazione 
Il contesto si satura rapidamente 
Usare autocompact o /compact 
manualmente 

--- PAGE 73 ---
Mettere tutto nel CLAUDE.md principale 
File monolitico che occupa troppo contesto 
Spezzare in regole modulari nella cartella 
.claude 
Insight Avanzato 
Il contesto non è solo una questione di "capienza". È una questione di qualità cognitiva. Anche quando il contesto non è 
completamente pieno, la qualità delle risposte di Claude degrada in modo proporzionale alla quantità di informazioni 
presenti. Questo avviene perché il modello deve "distribuire la sua attenzione" su tutti gli elementi presenti nel contesto. 
Meno rumore c'è, più nitida è la risposta. 
Pensate a questo come ascoltare una persona in una stanza silenziosa versus ascoltarla in un mercato affollato. In 
entrambi i casi "sentite", ma la qualità dell'ascolto è radicalmente diversa.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
