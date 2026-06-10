# 22.2 — Il Comando /compact
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-6-context > capitolo-22]]

## Content

Definizione del Concetto 
Il comando /compact è lo strumento manuale per attivare la compattazione del contesto. A differenza dell'Autocompact 
(che si attiva automaticamente a una certa soglia), /compact può essere eseguito in qualsiasi momento per forzare una 
compressione della conversazione. 
Spiegazione Approfondita 
Quando digitate /compact nel terminal: 
1.​
Claude analizza tutta la conversazione presente nel contesto 
2.​
Identifica le informazioni essenziali: decisioni prese, azioni completate, stato attuale, istruzioni pendenti 
3.​
Riscrive tutto in formato bullet point ad alta densità 
4.​
Sostituisce la conversazione originale con la versione compressa 
5.​
Il contesto si riduce significativamente 
Quando Usare /compact Manualmente 
Situazione 
Azione Raccomandata 
Contesto sopra il 60% e dovete continuare a lavorare 
Eseguite /compact 
State per dare un prompt complesso che richiede molto contesto 
Eseguite /compact prima 
Claude inizia a "dimenticare" cose dette in precedenza 
Probabilmente il contesto è saturo, eseguite /compact 

--- PAGE 89 ---
State per chiamare un sub-agente che produrrà molto output 
Liberate spazio prima con /compact 
Volete iniziare una fase nuova del progetto nella stessa sessione 
Eseguite /compact per "pulire" la fase precedente 
Differenza tra /compact e Nuova Sessione 
Una domanda che molti utenti si pongono è: "È meglio compattare o iniziare una nuova sessione?" La risposta dipende 
dalla situazione: 
Usate /compact quando: 
●​
Il lavoro è continuo e avete bisogno del contesto precedente 
●​
Siete a metà di un'implementazione 
●​
Le informazioni accumulate sono ancora rilevanti 
Iniziate una nuova sessione quando: 
●​
Passate a un argomento o task completamente diverso 
●​
Il contesto è oltre l'80% anche dopo compattazione 
●​
Volete un "foglio bianco" per una nuova fase 
Strategia combinata (raccomandata dall'autore della guida): 
1.​
Quando il contesto supera il 65-70% 
2.​
Dite a Claude: "Salva in memoria le informazioni importanti per la prossima sessione" 
3.​
Claude scrive le informazioni nel memory.md 
4.​
Iniziate una nuova sessione 
5.​
Nella nuova sessione, Claude recupera automaticamente le informazioni salvate in memoria 
6.​
Continuate il lavoro con un contesto fresco 
Questo è esattamente ciò che l'autore della guida fa nel video quando è al 66% di contesto e deve ancora integrare 
Stripe nell'applicazione Trello. 
Errori Comuni 
1.​ Usare /compact troppo frequentemente: ogni compattazione perde una piccola quantità di sfumature e 
dettagli. Se compattate ogni 5 messaggi, state perdendo troppe informazioni. 
2.​ Non usare /compact mai: l'estremo opposto. Se lasciate che il contesto si saturi senza mai intervenire, la 
qualità degraderà inesorabilmente. 
3.​ Compattare e poi ripetere le stesse informazioni: se dopo /compact riscrivete tutto quello che avevate detto 
prima, avete annullato il vantaggio della compattazione. 
4.​
Aspettarsi che la compattazione preservi tutto: la compattazione è una lossy compression — una 
compressione con perdita. Le informazioni principali vengono preservate, ma i dettagli minori potrebbero 
andare persi. Per questo è importante salvare informazioni critiche nel memory.md prima di compattare. 
Insight Avanzato 
La qualità della compattazione dipende dalla qualità della vostra conversazione. Se avete scritto prompt chiari, 
strutturati e con informazioni ben organizzate, la compattazione produrrà un riassunto eccellente. Se la vostra 

--- PAGE 90 ---
conversazione è caotica, piena di ripensamenti e deviazioni, la compattazione potrebbe perdere informazioni importanti 
perché non riesce a distinguerle dal rumore. 
Questo crea un circolo virtuoso: scrivere prompt migliori → compattazione più efficace → più contesto disponibile → 
risposte migliori → workflow più efficiente.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
