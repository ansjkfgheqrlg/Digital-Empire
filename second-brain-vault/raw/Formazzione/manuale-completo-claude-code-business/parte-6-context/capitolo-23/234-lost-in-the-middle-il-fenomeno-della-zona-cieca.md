# 23.4 — Lost in the Middle — Il Fenomeno della Zona Cieca

Definizione del Concetto 
Lost in the Middle è un fenomeno documentato nella ricerca accademica sugli LLM secondo il quale le informazioni 
posizionate nella parte centrale del contesto vengono processate con minore attenzione e fedeltà rispetto a quelle 
posizionate all'inizio o alla fine. È la "zona cieca" del modello. 
Spiegazione Approfondita 
L'autore della guida fa riferimento a un documento di ricerca specifico chiamato "Lost in the Middle" che ha studiato 
questo fenomeno in modo rigoroso. Il risultato chiave è: 
MODELLO DI ATTENZIONE DELL'LLM 
═══════════════════════════════ 
 
Posizione nel contesto:    INIZIO ←───────────────→ FINE 
                            
Livello di attenzione:     ██████░░░░░░░░░░░░██████ 
                           ALTO  BASSO BASSO  ALTO 
                            
Qualità delle risposte:   ██████░░░░░░░░░░░░██████ 
basate su info in questa   ALTA  BASSA BASSA  ALTA 
posizione: 
Questo fenomeno spiega perché: 
●​
Le istruzioni nel CLAUDE.md (inizio del contesto) vengono generalmente rispettate bene 
●​
I vostri ultimi messaggi (fine del contesto) ricevono risposte accurate 
●​
Le istruzioni date a metà di una lunga conversazione vengono spesso "dimenticate" o ignorate 
Implicazioni per il Context Management 
La comprensione del Lost in the Middle ha implicazioni profonde per come strutturate il vostro lavoro: 
1. Struttura del CLAUDE.md: 
INIZIO (Primacy Bias — massima attenzione) 
├── Regole di sicurezza critiche 
├── Vincoli inviolabili 

--- PAGE 96 ---
├── Istruzioni fondamentali del progetto 
│ 
MEZZO (Lost in the Middle — minima attenzione) 
├── Dettagli operativi secondari 
├── Preferenze minori 
├── Informazioni di contesto generiche 
│ 
FINE (Recency Bias — alta attenzione) 
├── Istruzioni operative correnti 
├── Standard di qualità 
├── Formato di output desiderato 
2. Strategia di conversazione:​
Se dovete dare un'istruzione importante nel mezzo di una conversazione lunga, ripetetela. Ditela una volta quando la 
pensate (sarà nel mezzo), e poi ripetetela prima del prompt operativo (sarà alla fine). In questo modo, coprite sia la 
posizione originale che la posizione di Recency. 
3. Importanza delle regole modulari:​
Questo fenomeno è un'altra ragione per cui è fondamentale spezzare il CLAUDE.md in regole modulari. Quando 
Claude deve seguire una regola specifica (ad esempio design-fidelity.md), carica solo quel file. Quel file, essendo 
piccolo, non soffre del Lost in the Middle perché non c'è abbastanza "mezzo" da perdersi. 
Confronto: 
●​
CLAUDE.md monolitico (5.000 token): le regole nel mezzo (token 1.500-3.500) saranno nella zona cieca 
●​
Regola modulare (300 token): l'intero file è abbastanza corto che Claude lo processa interamente con alta 
attenzione 
4. L'effetto amplificato dalla distanza:​
L'autore della guida usa l'analogia dell'arco e del bersaglio per illustrare un concetto correlato: man mano che il progetto 
diventa più grande (la distanza dal bersaglio aumenta), l'intervallo di incertezza si amplifica. Lo stesso vale per il Lost in 
the Middle: man mano che il contesto si riempie, la "zona cieca" nel mezzo diventa proporzionalmente più grande e più 
problematica. 
CONTESTO PICCOLO (20% pieno): 
███░███          Zona cieca piccola e gestibile 
 
CONTESTO MEDIO (50% pieno): 
█████░░░░░█████  Zona cieca più grande 
 
CONTESTO GRANDE (80% pieno): 
███████░░░░░░░░░░░░░░░░███████  Zona cieca estesa e pericolosa 
Errori Comuni 
1.​
Dare istruzioni critiche una sola volta a metà conversazione: se date un'istruzione importante al messaggio 
#15 di una conversazione di 40 messaggi, al messaggio #30 Claude potrebbe averla completamente 
"dimenticata". 
2.​
Pensare che Claude "faccia apposta" a ignorare istruzioni: non è malizia, è un bias cognitivo del modello. La 
soluzione non è arrabbiarsi, ma posizionare strategicamente le informazioni. 
3.​
Non ripetere mai le istruzioni importanti: la ripetizione strategica è uno strumento legittimo e importante nel 
prompt engineering. Non è ridondanza — è resilienza informativa. 
4.​
Caricare documenti enormi nel contesto: un documento di 50.000 token avrà una zona cieca enorme nel 
mezzo. Claude "vedrà" bene l'inizio e la fine del documento, ma perderà dettagli cruciali nel mezzo. Meglio 
spezzare il documento in sezioni più piccole e caricarle una alla volta. 
Insight Avanzato 
Il Lost in the Middle è uno dei motivi principali per cui i sub-agenti sono così preziosi per il Context Management. 
Quando un sub-agente (ad esempio il Researcher) fa una ricerca che produce 100.000 token di risultati, quei token 

--- PAGE 97 ---
vivono nel contesto del sub-agente, non nel contesto principale. Il sub-agente, avendo processato tutto quel materiale, 
produce un riassunto di 2.000 token che viene inviato all'agente principale. 
Questo elimina il problema del Lost in the Middle perché: 
●​
Nel sub-agente: il documento lungo soffre del Lost in the Middle, ma il sub-agente ha come unico compito 
processarlo, quindi può iterare e verificare 
●​
Nell'agente principale: arrivano solo 2.000 token di risultato, che non creano alcuna zona cieca 
È come avere un assistente che legge un libro di 500 pagine e vi fa un riassunto di 5 pagine. Voi leggete 5 pagine 
(nessuna zona cieca), non 500 (zona cieca enorme).

