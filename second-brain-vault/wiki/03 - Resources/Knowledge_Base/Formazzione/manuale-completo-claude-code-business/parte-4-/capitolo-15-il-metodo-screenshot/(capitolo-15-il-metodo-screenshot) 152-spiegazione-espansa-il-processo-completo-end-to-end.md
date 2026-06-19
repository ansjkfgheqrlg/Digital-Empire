# 15.2 — Spiegazione Espansa: Il Processo Completo End-to-End
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-4- > capitolo-15-il-metodo-screenshot]]

## Content

L'autore dimostra l'intero processo dal vivo, replicando il sito "Hyper" trovato su Godly Website. Qui documentiamo ogni 
passaggio in dettaglio. 
Fase di Preparazione 
Step 1: Selezionare il sito di riferimento 
●​
L'autore sceglie un sito chiamato "Hyper" da Godly Website 
●​
L'obiettivo è ricostruirlo usando Claude Code 

--- PAGE 41 ---
Step 2: Catturare il full-page screenshot 
text 
1. Aprire il sito in Chrome 
2. Tasto destro → Inspect 
3. Impostare dimensioni: 1920x1080 
4. Command + Shift + P → "screenshot" → "Capture full size screenshot" 
5. Il file viene scaricato automaticamente 
Step 3: Ridimensionare l'immagine 
text 
1. Andare su iloveimg.com 
2. Caricare lo screenshot 
3. Resize al 50% (NON 75%) 
4. Scaricare 
5. Rinominare in "image-reference.png" 
6. Posizionare nella cartella del progetto 
Step 4: Copiare gli stili CSS 
text 
1. Sul sito originale: tasto destro → Inspect 
2. Selezionare <body> nell'albero DOM 
3. Tasto destro → Copy → Copy styles 
4. Tenere negli appunti per il prompt 
Fase di Esecuzione 
Step 5: Formulare il prompt​
Combinare tre elementi: 
●​
Riferimento al CLAUDE.md (che contiene le regole del screenshot loop) 
●​
Riferimento all'immagine di riferimento nella cartella 
●​
Gli stili CSS copiati incollati direttamente nel prompt 
Step 6: Scegliere la modalità​
L'autore sceglie Bypass Permission anziché Plan Mode. La ragione: 
"In questo caso, siccome il piano è già altamente dettagliato — perché ho un image reference e ho tutti i dettagli di stile 
— se anche salto [il planning] va benissimo." 

--- PAGE 42 ---
La logica è: se le informazioni nel prompt sono sufficientemente dettagliate (immagine + stili + CLAUDE.md), il piano è 
implicito nei materiali forniti. La pianificazione formale è meno necessaria. 
Avvertenza dell'autore: Questa scelta è basata sull'esperienza. Per chi inizia, il Plan Mode è sempre raccomandato. 
Step 7: Claude Code esegue il ciclo autonomamente 
text 
CICLO OSSERVATO DALL'AUTORE: 
 
Iterazione 1 ("Round 1"): 
├── Claude costruisce la prima versione del sito 
├── Fa il primo screenshot 
├── Confronta con l'immagine di riferimento 
├── Identifica le differenze 
└── Corregge (font, dimensioni, spaziature, colori) 
 
Iterazione 2 ("Round 2"): 
├── Fa un nuovo screenshot 
├── Confronta di nuovo 
├── Identifica differenze residue 
└── Corregge 
 
[Continua fino a convergenza o fino a quando Claude 
 dichiara di aver raggiunto il massimo livello di fedeltà possibile] 
L'autore osserva: "Io non sto toccando letteralmente nulla. L'AI sta già cercando di ripensare a cosa deve fare per 
replicare questo sito." 
Fase di Risultato 
Step 8: Valutazione del risultato 
Il risultato prodotto dopo il ciclo di screenshot loop presenta: 
●​
✅ Struttura generale corretta 
●​
✅ Bottoni corretti ("Solution Personalized Aviation" con i due bottoni) 
●​
✅ Sezione con quattro componenti correttamente replicata 
●​
✅ Sezione "Flexible Services" con tre screenshot 
●​
⚠️ Immagine principale in un rettangolo anziché a schermo intero 
●​
⚠️ Placeholder al posto delle immagini originali (lazy images) 
●​
⚠️ Font potenzialmente diverso (se non installato nel sistema) 

--- PAGE 43 ---
Perché mancano le immagini:​
Claude Code ha identificato che le immagini del sito originale sono "lazy" (si caricano on-demand) e non erano incluse 
nello screenshot. Ha quindi inserito placeholder. Per risolvere questo serve accesso agli asset originali del sito. 
Perché il font potrebbe essere diverso:​
Claude Code segnala: "Il font vertical now display potrebbe non essere installato sul sistema." I font custom devono 
essere disponibili nel sistema per essere replicati correttamente.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
- [[Map - General|General Area]]
