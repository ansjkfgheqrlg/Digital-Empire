# 22.1 — Il Concetto di Densità Informativa
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-6-context > capitolo-22]]

## Content

Definizione del Concetto 
La densità informativa è il rapporto tra la quantità di informazione utile contenuta in un testo e il numero di token 
utilizzati per esprimerla. Un testo ad alta densità informativa comunica molta informazione con pochi token. Un testo a 
bassa densità informativa spreca token con parole inutili, ripetizioni e informazioni irrilevanti. 

--- PAGE 85 ---
Spiegazione Approfondita 
La guida originale fornisce un esempio perfetto per comprendere questo concetto. Immaginate di scrivere questo 
prompt a Claude: 
Prompt a bassa densità informativa: 
"Ciao sono Giovanni ho 30 anni il mio compleanno il 27 di febbraio quindi qualche giorno fa mi piacciono le pentole ah 
no le pentole non c'entrano vivo a Lussemburgo e bla bla bla" 
In questo prompt ci sono informazioni rilevanti e informazioni irrilevanti mescolate insieme: 
Informazione 
Rilevante? 
Motivo 
"Ciao" 
No 
Convenevole inutile per il contesto 
"sono Giovanni" 
Sì 
Identità dell'utente 
"ho 30 anni" 
Sì 
Dato anagrafico potenzialmente utile 
"il mio compleanno il 27 di febbraio" 
Sì 
Dato specifico 
"qualche giorno fa" 
No 
Deduzione inutile, spreca token 
"mi piacciono le pentole" 
No 
Totalmente irrilevante 
"ah no le pentole non c'entrano" 
No 
Correzione di un errore proprio, doppio spreco 

--- PAGE 86 ---
"vivo a Lussemburgo" 
Sì 
Dato geografico 
"bla bla bla" 
No 
Riempitivo 
Prompt ad alta densità informativa (equivalente): 
"Giovanni, 30 anni, Lussemburgo, compleanno 27 febbraio" 
Stesse informazioni utili, un quinto dei token. Questo è il principio della densità informativa. 
Il Meccanismo dell'Autocompact 
L'Autocompact è la funzione di Claude Code che automatizza questo processo di aumento della densità informativa. 
Ecco come funziona: 
​
​
​
 
PROCESSO DI AUTOCOMPACT 
═══════════════════════ 
 
PRIMA della compattazione: 
┌────────────────────────────────────────────────┐ 
│ Utente: Ciao, mi chiamo Giovanni, vivo a       │ 
│ Lussemburgo, ho 30 anni, il mio compleanno     │ 
│ è il 27 febbraio, mi piacciono le pentole      │ 
│ ah no le pentole non c'entrano...              │ 
│                                                │ 
│ Claude: Ciao Giovanni! Piacere di conoscerti!  │ 
│ Come posso aiutarti oggi? Vedo che vivi a      │ 
│ Lussemburgo, bellissimo posto! E auguri in     │ 
│ ritardo per il tuo compleanno!                 │ 
│                                                │ 
│ Utente: Grazie, allora vorrei...               │ 
│ [... altri 50 messaggi di conversazione ...]   │ 
│                                                │ 
│ CONSUMO: 85% del contesto                      │ 
└────────────────────────────────────────────────┘ 
 
DOPO la compattazione: 
┌────────────────────────────────────────────────┐ 
│ • User: Giovanni, 30 anni, Lussemburgo,        │ 
│   compleanno 27 febbraio                        │ 
│ • Richiesta principale: [sintesi della task]    │ 
│ • Azioni completate: [lista bullet point]       │ 
│ • Stato attuale: [sintesi dello stato]          │ 
│ • Decisioni prese: [lista decisioni]            │ 
│                                                 │ 
│ CONSUMO: 25% del contesto                       │ 
└────────────────────────────────────────────────┘ 

--- PAGE 87 ---
Come potete vedere, il processo di compattazione: 
1.​
Elimina tutte le parole ridondanti e i convenevoli 
2.​
Sintetizza le conversazioni in bullet point ad alta densità 
3.​
Preserva le informazioni chiave e le decisioni prese 
4.​
Riduce drasticamente il consumo di contesto 
Perché l'Autocompact è Fondamentale 
Senza Autocompact, ogni sessione di lavoro con Claude Code avrebbe una durata massima limitata dalla dimensione 
del contesto. Con conversazioni intensive, potreste esaurire il contesto in 20-30 messaggi. L'Autocompact vi permette di 
estendere le sessioni molto oltre questo limite, comprimendo periodicamente le informazioni accumulate. 
Il Buffer di Autocompact 
L'Autocompact utilizza un buffer riservato di circa 33.000 token. Questo buffer funziona come una zona di transito: 
​
​
​
 
MECCANISMO DEL BUFFER 
═════════════════════ 
 
CONTESTO PIENO (soglia raggiunta) 
         │ 
         ▼ 
┌─────────────────────────────┐ 
│  Il contesto raggiunge la   │ 
│  soglia dei 33.000 token    │ 
│  riservati al buffer        │ 
└──────────────┬──────────────┘ 
               │ 
               ▼ 
┌─────────────────────────────┐ 
│  ATTIVAZIONE AUTOCOMPACT    │ 
│  Claude "ripensa" tutta la  │ 
│  conversazione e la         │ 
│  riscrive in forma          │ 
│  compressa                  │ 
└──────────────┬──────────────┘ 
               │ 
               ▼ 
┌─────────────────────────────┐ 
│  CONTESTO RIDOTTO           │ 
│  La conversazione compressa │ 
│  occupa molto meno spazio   │ 
│  Il contesto torna a un     │ 
│  livello gestibile          │ 
└─────────────────────────────┘ 
Quando il contesto raggiunge la soglia del buffer, Claude si prende un momento (noterete che "pensa" più a lungo del 
solito) e riscrive tutta la conversazione in formato compresso. Dopo questa operazione, il contesto torna a un livello più 
basso e potete continuare a lavorare. 
Interpretazione Pratica — Il Formato Compattato 
Dopo una compattazione, se esaminate il contesto compattato (visibile con il comando /compact), vedrete qualcosa del 
genere: 
 

--- PAGE 88 ---
Esempio di contesto compattato: 
──────────────────────────────── 
• User message: importa i tre subagenti 
• My action: creati reviewer, researcher, QA 
• User message: chiama il reviewer subagent 
• My action: review del codice, 8 fix applicati 
• User message: chiama il QA subagent 
• My action: test eseguiti, tutti passati 
• Stato corrente: app funzionante, deploy pendente 
──────────────────────────────── 
Questo è ciò che la guida chiama formato "ad alta densità" — tutta la conversazione precedente condensata in bullet 
point essenziali.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
