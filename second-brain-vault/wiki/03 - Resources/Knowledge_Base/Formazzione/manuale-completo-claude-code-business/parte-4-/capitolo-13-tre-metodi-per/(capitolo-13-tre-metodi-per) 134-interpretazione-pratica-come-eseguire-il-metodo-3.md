# 13.4 — Interpretazione Pratica: Come Eseguire il Metodo 3
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-4- > capitolo-13-tre-metodi-per]]

## Content

L'autore mostra il processo completo passo dopo passo: 
Step 1: Catturare lo screenshot full-page del sito di riferimento 
Non si usa un normale screenshot (che cattura solo la parte visibile). Si usa una funzionalità specifica del browser: 
text 
PROCESSO PER FULL-PAGE SCREENSHOT: 
 
1. Aprire il sito di riferimento nel browser 
2. Tasto destro → "Inspect" (apre i DevTools) 
3. Assicurarsi che la dimensione sia 1920x1080: 
   → Nel pannello DevTools, cercare le dimensioni 

--- PAGE 33 ---
   → Cambiare a 1920x1080 se necessario 
4. Premere Command + Shift + P (apre il command menu dei DevTools) 
5. Digitare "screenshot" 
6. Selezionare "Capture full size screenshot" 
7. L'immagine viene scaricata automaticamente 
L'autore ha scoperto questo metodo dopo "aver fatto 8 miliardi di siti" — il che implica che molti developer non 
conoscono questa funzionalità e fanno screenshot manuali sezione per sezione, il che è enormemente meno efficiente. 
Vantaggio aggiuntivo del full-page screenshot:​
Oltre ad avere tutto il sito in un'unica immagine, permette di identificare le lazy images — immagini che non appaiono 
subito perché si caricano solo quando l'utente scorre fino alla loro posizione. Nel full-page screenshot queste appaiono 
come placeholder o spazi vuoti, il che è un'informazione diagnostica utile. 
Step 2: Ridimensionare l'immagine 
Il full-page screenshot di un sito complesso può pesare 10-15 MB. Inserire un'immagine di questa dimensione nel 
contesto di Claude Code causerebbe problemi. L'autore lo dice chiaramente: "Questo sito è troppo grosso — se lo 
mettessimo nell'LLM, questa immagine è 12.5 mega, esploderebbe tutto." 
text 
PROCESSO DI RIDIMENSIONAMENTO: 
 
1. Andare su iloveimg.com (o servizio equivalente) 
2. Caricare l'immagine 
3. Selezionare "Resize" al 50% 
   (NON 75% — l'autore specifica: "non farei il 75% perché non ha molto senso") 
4. Scaricare l'immagine ridimensionata 
5. Rinominarla in qualcosa di significativo (es. "image-reference.png") 
6. Posizionarla nella cartella del progetto 
Step 3: Copiare gli stili CSS dal sito di riferimento 
Questo passaggio riduce enormemente lo spazio di manovra per errori da parte di Claude Code: 
text 
PROCESSO PER COPIARE GLI STILI: 
 
1. Sul sito di riferimento, tasto destro → Inspect 
2. Selezionare l'elemento <body> nell'albero DOM 
3. Tasto destro sull'elemento body 
4. Selezionare "Copy" → "Copy styles" 

--- PAGE 34 ---
5. Questi stili verranno incollati nel prompt a Claude Code 
Perché copiare gli stili è cruciale:​
L'autore spiega: "Non vogliamo che l'LLM abbia molto spazio di manovra per sbagliarsi." Gli stili CSS contengono 
informazioni precise su: 
●​
Font utilizzati (famiglia, dimensione, peso) 
●​
Colori esatti (codici esadecimali) 
●​
Spaziature (margini, padding) 
●​
Layout (flexbox, grid) 
●​
Ombre, bordi, effetti 
Senza questi stili, Claude Code dovrebbe "indovinare" tutti questi parametri dall'immagine, con un margine di errore 
molto alto. Con gli stili, ha informazioni precise per gran parte delle decisioni estetiche. 
Step 4: Formulare il prompt e avviare 
Il prompt combina tre elementi: 
1.​
Il CLAUDE.md (già presente nel progetto con le regole del ciclo di verifica) 
2.​
L'immagine di riferimento (posizionata nella cartella del progetto) 
3.​
Gli stili CSS copiati dal sito originale 
text 
ESEMPIO DI PROMPT: 
 
"Utilizzando il CLAUDE.md, per favore costruiscimi un sito. 
Per farlo ti ho messo un'immagine di riferimento nella cartella. 
Qua sotto ti incollerò lo stile che c'è all'interno del sito: 
 
[INCOLLARE QUI GLI STILI CSS COPIATI]" 
Step 5: Claude Code esegue il ciclo iterativo automaticamente 
Grazie alle istruzioni nel CLAUDE.md (che contengono il workflow di verifica tramite screenshot), Claude Code: 
1.​
Costruisce la prima versione del sito 
2.​
Fa uno screenshot del risultato 
3.​
Confronta con l'immagine di riferimento 
4.​
Identifica le differenze (spaziature, dimensioni, colori) 
5.​
Corregge le differenze 
6.​
Fa un nuovo screenshot 
7.​
Ripete fino a quando le differenze sono minime 
L'autore osserva il processo in tempo reale: "Vedete che ora sta facendo questo — prende gli screenshot, naviga, 
prende, capisce, fa briga. Io non sto toccando letteralmente nulla. L'AI sta già cercando di ripensare a cosa deve fare 
per replicare questo sito."

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
