# 7.8 — Insight Avanzato
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-2-installazione-e > capitolo-7-il-terminal-come]]

## Content

Il comando /config è navigabile:​
Quando eseguite /config, potete: 
●​
Usare le frecce su/giù per scorrere le opzioni 
●​
Premere Tab per passare alla vista "Usage" (quanto avete utilizzato del modello, es. 28%) 
●​
Premere Tab ancora per passare alla vista "Status" 
●​
Premere ESC per uscire 
Questo crea un flusso di navigazione: 
/config → [Configurazione] --Tab--> [Usage] --Tab--> [Status] --ESC--> [Prompt] 
Il concetto di Autocompact:​
L'Autocompact è una delle funzionalità più importanti di Claude Code e merita una spiegazione dettagliata qui perché si 
configura tramite /config. 
L'autore spiega il concetto con un esempio vivido. Immaginate di aver scritto un prompt come questo: 
"Ciao, sono Giovanni, ho 30 anni, il mio compleanno è il 27 febbraio, quindi qualche giorno fa, mi piacciono le pentole, 
vivo a Lussemburgo..." 
In questo prompt, "mi piacciono le pentole" è informazione irrilevante che occupa contesto inutilmente. L'Autocompact 
fa esattamente questo: prende il contesto e ne aumenta la densità informativa, eliminando ciò che non è rilevante. 
Il risultato dopo Autocompact sarebbe qualcosa come: 
"Giovanni, Lussemburgo, 30 anni, compleanno 27 febbraio" 
Stesse informazioni utili, frazione dello spazio. Questo processo avviene automaticamente quando il contesto si 
avvicina alla soglia critica (circa 33.000 token nel buffer di Autocompact, come verrà spiegato nel Capitolo 22).

## Collegamenti Correlati
- [[Map - Formazzione|Formazzione Area]]
