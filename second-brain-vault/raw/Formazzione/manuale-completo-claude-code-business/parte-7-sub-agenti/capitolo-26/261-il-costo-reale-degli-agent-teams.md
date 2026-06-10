# 26.1 — Il Costo Reale degli Agent Teams

Definizione del Concetto 
Gli Agent Teams consumano token a una velocità significativamente superiore rispetto ai sub-agenti tradizionali o al 
lavoro nel contesto singolo. L'autore della guida stima che il consumo sia 3-5 volte superiore rispetto all'uso di 
sub-agenti per la stessa task. 
Spiegazione Approfondita — Perché Costano di Più 
Il costo elevato degli Agent Teams deriva da tre fattori: 
1. Comunicazione bidirezionale:​
Ogni comunicazione tra teammate genera token sia in uscita (dal mittente) che in ingresso (nel destinatario). Con 4 
teammate che comunicano tutti con tutti, il numero di comunicazioni possibili cresce in modo combinatorio. 
text 
COMUNICAZIONI POSSIBILI CON N TEAMMATE 
═══════════════════════════════════════ 
 
Con 2 teammate: 2 comunicazioni possibili 
    A ↔ B 
 
Con 3 teammate: 6 comunicazioni possibili   
    A ↔ B, A ↔ C, B ↔ C 
 
Con 4 teammate: 12 comunicazioni possibili 
    A ↔ B, A ↔ C, A ↔ D, B ↔ C, B ↔ D, C ↔ D 
 
Con 5 teammate: 20 comunicazioni possibili 
 

--- PAGE 121 ---
Formula: N × (N-1) comunicazioni bidirezionali 
Ogni comunicazione consuma token. Più teammate avete, più comunicazioni avvengono, più token vengono consumati. 
2. Contesti multipli simultanei:​
Ogni teammate ha il proprio contesto completo. Con 4 teammate più il Team Leader, avete 5 contesti attivi 
contemporaneamente, ciascuno con il proprio system prompt, i propri tool e la propria conversazione. 
3. Context Management interno:​
Come mostrato nella guida, i teammate possono raggiungere i 171.000 token nel loro contesto e poi fare reset a 
59.000. Questo processo di compattazione e reset consuma ulteriori risorse computazionali. 
I Numeri Reali dalla Guida 
L'autore condivide dati concreti durante la sessione di Agent Teams: 
Tempo trascorso 
Costo accumulato 
Osservazione 
~5 minuti 
€3 
"Solo l'inizio" 
~7 minuti 
€5 
"Ogni volta che fa bip ho speso €5" 
Fine sessione 
€10-20 (stimato) 
Analisi completa di una repository 
Per confronto, una sessione di lavoro normale con un singolo agente su un piano abbonamento da €17/mese costa 
effettivamente... €17/mese per uso illimitato. La differenza è abissale. 
L'Avvertimento dell'Autore 
"Per favore non dimenticatevi mai che siate consapevoli di quello che state facendo perché se non avete i soldi da 
buttare tipo €10-€20 beh evitate perché nel senso non ha poi tutto questo senso." 
E ancora: 
"Nonostante sembri sexy a dirlo, facendogli andare 15 minuti spendete €80." 
Questi avvertimenti sono fondamentali. L'hype online intorno agli Agent Teams è enorme, ma l'autore (che spende circa 
€400/mese in Claude Code) è molto pragmatico: non li usa regolarmente perché il costo è troppo elevato per la maggior

