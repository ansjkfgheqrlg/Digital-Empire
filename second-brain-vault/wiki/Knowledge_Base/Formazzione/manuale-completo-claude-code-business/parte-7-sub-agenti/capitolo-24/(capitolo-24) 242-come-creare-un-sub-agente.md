# 24.2 — Come Creare un Sub-agente
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-7-sub-agenti > capitolo-24]]

## Content

--- PAGE 103 ---
Definizione del Concetto 
Un sub-agente è, nella sua essenza, un file di testo in formato Markdown posizionato nella cartella .claude/agents/ 
del progetto. Questo file contiene le istruzioni che definiscono il comportamento, le competenze e i limiti del sub-agente. 
Spiegazione Approfondita — La Struttura del File 
Quando create un sub-agente, il file Markdown contiene diverse sezioni delimitate da separatori (righe tratteggiate ---). 
La guida originale mostra che un file sub-agente tipico include: 
in Markdown 
--- 
model: haiku 
max_tokens: [limite di token per le risposte] 
--- 
 
# Nome del Sub-agente 
 
## Descrizione 
[Cosa fa questo sub-agente] 
 
## Istruzioni 
[Come deve comportarsi] 
 
## Vincoli 
[Cosa NON deve fare] 
 
## Formato di Output 
[Come deve presentare i risultati] 
Analisi della struttura: 
La sezione tra i tratteggi (---) è chiamata frontmatter e contiene metadati tecnici: 
●​
model: specifica quale modello LLM utilizzare per questo sub-agente. La guida indica che Haiku è il modello 
più utilizzato per i sub-agenti al momento della registrazione. Haiku è un modello più leggero e veloce di Opus 
o Sonnet, perfetto per task specializzate che non richiedono il modello più potente. 
●​
max_tokens: limita la quantità di token che il sub-agente può usare per le risposte. 
Il corpo del file contiene le istruzioni in linguaggio naturale che definiscono il comportamento del sub-agente. 
Procedura Pratica per Creare un Sub-agente 
Metodo 1 — Creazione Manuale: 
1.​ Navigate alla cartella .claude/agents/ nel vostro progetto 
2.​ Create un nuovo file con estensione .md (esempio: researcher.md) 
3.​
Scrivete le istruzioni seguendo la struttura mostrata sopra 
4.​
Salvate il file 
Metodo 2 — Creazione Assistita da Claude (raccomandato): 
Questo è il metodo utilizzato nella guida originale. Potete chiedere direttamente a Claude di creare il sub-agente per 
voi: 
"Per favore guarda la documentazione ufficiale di Claude  
e creami un sub-agente [nome]. Deve fare [descrizione].  
Popola il file con le best practice della documentazione ufficiale." 

--- PAGE 104 ---
Claude andrà a consultare la documentazione ufficiale di Anthropic, capirà la struttura corretta dei sub-agenti e creerà il 
file con le best practice aggiornate. 
Metodo 3 — Importazione da Template Globali: 
Se avete già sub-agenti configurati nella vostra cartella globale (~/.claude/agents/), potete chiedere a Claude di 
importarli nel progetto corrente: 
text 
"Per favore importa i tre sub-agenti che sono nella mia  
cartella globale .claude/agents/: il reviewer, il researcher e il QA." 
Dove Vivono i Sub-agenti 
I sub-agenti possono esistere a diversi livelli dell'architettura Claude Code: 
 
LIVELLO LOCAL (dentro il progetto): 
progetto/ 
└── .claude/ 
    └── agents/ 
        ├── researcher.md     ← Sub-agente di questo progetto 
        ├── reviewer.md       ← Sub-agente di questo progetto 
        └── qa.md             ← Sub-agente di questo progetto 
 
LIVELLO GLOBAL (nel computer dell'utente): 
~/.claude/ 
└── agents/ 
    ├── researcher.md     ← Disponibile per TUTTI i progetti 
    ├── reviewer.md       ← Disponibile per TUTTI i progetti 
    └── qa.md             ← Disponibile per TUTTI i progetti 
Il vantaggio di avere sub-agenti a livello globale è che non dovete ricrearli per ogni nuovo progetto. Potete importarli o 
Claude li troverà automaticamente. 
 
 
 
Come Chiamare un Sub-agente 
Una volta creato, chiamare un sub-agente è semplice come scrivere un prompt: 
 
"Per favore chiama il sub-agente reviewer e assicurati  
di rivedere tutto il codice." 
Oppure, in modo più diretto: 
 

--- PAGE 105 ---
"Chiama il researcher sub-agent per fare una ricerca  
sulle best practice per [argomento]." 
Claude riconosce il nome del sub-agente, lo attiva nel suo contesto separato, gli invia la task e raccoglie il risultato. 
Perché Usare Haiku per i Sub-agenti 
La scelta di Haiku come modello per i sub-agenti è strategica: 
Caratteristica 
Haiku 
Opus/Sonnet 
Velocità 
Molto veloce 
Più lento 
Costo per token 
Molto basso 
Più alto 
Capacità cognitiva 
Sufficiente per task specializzate 
Superiore per task complesse 
Ideale per 
Ricerche, review, test 
Ragionamento complesso, architettura 
Poiché i sub-agenti eseguono task specializzate e ben definite (non ragionamento generale complesso), non hanno 
bisogno del modello più potente. Haiku è sufficiente e molto più economico, il che è particolarmente importante 
considerando che i sub-agenti possono consumare molti token nel loro contesto interno. 
Errori Comuni nella Creazione 
1.​
Creare sub-agenti senza consultare la documentazione: la struttura dei sub-agenti evolve. Chiedete sempre a 
Claude di verificare le best practice aggiornate dalla documentazione ufficiale. 
2.​
Non specificare il modello nel frontmatter: se non specificate il modello, il sub-agente potrebbe usare lo stesso 
modello dell'agente principale (Opus/Sonnet), consumando inutilmente risorse più costose. 
3.​
Scrivere istruzioni troppo lunghe nel sub-agente: ricordate che anche le istruzioni del sub-agente occupano 
contesto (nel contesto del sub-agente). Istruzioni concise e precise producono risultati migliori. 
4.​
Non definire chiaramente il formato di output: se non dite al sub-agente COME presentare i risultati, potrebbe 
produrre output troppo lunghi che poi occuperanno troppo spazio nel contesto principale.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
- [[Map - General|General Area]]
