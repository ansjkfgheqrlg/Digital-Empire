# K05-context
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Agente Max > knowledge]]

## Content

# MODULO KNOWLEDGE BASE

**K05-context.md** — Capitoli 20-23 | Token e contesto, monitoraggio, autocompact, bias cognitivi

## Riferimenti Correlati
- K06-sub-agenti.md (i sub-agenti gestiscono il contesto autonomamente)
- K08-mcp.md (gli MCP consumano contesto)

---

# **PARTE 6 — CONTEXT MANAGEMENT**

*"Il Context Management è una delle cose più importanti che ci sia per ottenere prompt efficaci e un elevato ROI da Claude Code."*  
*— Dalla guida originale*

## **Introduzione alla Parte 6**

Il Context Management — ovvero la gestione del contesto — rappresenta il cuore pulsante dell'efficienza operativa in Claude Code. Se le Parti precedenti di questo manuale vi hanno insegnato *cosa* sia Claude Code e *come* si configuri un progetto, questa Parte vi insegna *come pensare* quando interagite con il sistema.

Ogni singola parola che inviate a Claude, ogni file che viene letto, ogni MCP installato, ogni sub-agente chiamato — tutto questo occupa spazio all'interno di una risorsa finita chiamata finestra di contesto. Chi comprende questa risorsa e la gestisce con intelligenza ottiene risultati straordinariamente migliori. Chi la ignora si ritrova con un sistema che "allucinà", dimentica istruzioni, perde coerenza e brucia tempo e denaro.

Questa Parte è composta da quattro capitoli:

| Capitolo | Titolo | Focus Principale |
| ----- | ----- | ----- |
| 20 | Comprendere Contesto e Token | Cosa sono, come funzionano, perché contano |
| 21 | Analisi e Monitoraggio del Contesto | Strumenti pratici per vedere dove va il contesto |
| 22 | Autocompact e Densità Informativa | Come Claude comprime e riusa lo spazio |
| 23 | Primacy Bias, Recency Bias e Lost in the Middle | Come l'LLM "ricorda" e come sfruttarlo |

# **CAPITOLO 20**

## **Comprendere Contesto e Token**

### **20.1 — Introduzione al Concetto di Contesto**

#### **Definizione del Concetto**

Quando si parla di contesto in Claude Code, ci si riferisce alla quantità totale di informazioni che il modello di linguaggio (LLM) è in grado di "tenere in mente" durante una singola sessione di lavoro. Immaginate il contesto come la memoria di lavoro di Claude: tutto ciò che il sistema sa, vede, ricorda e può utilizzare per rispondere ai vostri prompt in un dato momento.

Questa memoria di lavoro non è infinita. Ha una dimensione massima fissa, misurata in unità chiamate token. Una volta che questa memoria si riempie, il sistema deve fare delle scelte: comprimere informazioni precedenti, dimenticarne alcune o degradare nella qualità delle risposte.

#### **Spiegazione Approfondita**

Il contesto funziona esattamente come una scrivania fisica. Immaginate di avere una scrivania di dimensioni fisse:

* Potete appoggiarci sopra documenti, foto, appunti, strumenti  
* Più cose ci mettete, meno spazio avete per lavorare  
* Se la scrivania si riempie completamente, dovete togliere qualcosa per fare spazio a qualcosa di nuovo  
* Se ammassate troppa roba, non riuscite più a trovare quello che vi serve

In Claude Code, questa "scrivania" contiene:

* Le istruzioni di sistema iniettate da Anthropic (il system prompt)  
* Il vostro file CLAUDE.md e tutte le regole del progetto  
* I file di memoria (memory.md)  
* Le definizioni dei tool di sistema  
* Le definizioni degli MCP installati  
* Le skill caricate  
* Tutta la vostra conversazione (ogni messaggio che avete scritto e ogni risposta di Claude)

#### **Perché Questo Concetto è Fondamentale**

Comprendere il contesto è la differenza tra usare Claude Code come un chatbot qualsiasi e usarlo come uno strumento professionale che genera valore reale. Senza questa comprensione:

* Non capirete perché Claude "dimentica" cose che gli avete detto  
* Non capirete perché le risposte diventano meno accurate dopo conversazioni lunghe  
* Non saprete come organizzare le informazioni per ottenere risultati migliori  
* Sprecherete contesto prezioso con informazioni irrilevanti  
* Non potrete fare scelte informate su cosa installare (MCP, skill, sub-agenti)

#### **Interpretazione Pratica**

A livello pratico, gestire il contesto significa:

1. Sapere quanto contesto è stato usato in ogni momento  
2. Sapere da cosa è occupato (conversazione? MCP? system prompt?)  
3. Decidere consapevolmente cosa aggiungere e cosa togliere  
4. Scrivere prompt concisi che non sprechino spazio  
5. Strutturare il progetto in modo da minimizzare l'occupazione di contesto inutile

#### **Errori Comuni**

| Errore | Conseguenza | Soluzione |
| ----- | ----- | ----- |
| Ignorare completamente il contesto | L'LLM perde coerenza dopo pochi messaggi | Monitorare regolarmente con /context |
| Installare troppi MCP contemporaneamente | Il contesto si riempie prima ancora di iniziare a lavorare | Installare solo ciò che serve, convertire in skill |
| Scrivere prompt lunghissimi e ridondanti | Spreco di token preziosi | Aumentare la densità informativa dei prompt |
| Non fare mai compattazione | Il contesto si satura rapidamente | Usare autocompact o /compact manualmente |
| Mettere tutto nel CLAUDE.md principale | File monolitico che occupa troppo contesto | Spezzare in regole modulari nella cartella .claude |

#### **Insight Avanzato**

Il contesto non è solo una questione di "capienza". È una questione di qualità cognitiva. Anche quando il contesto non è completamente pieno, la qualità delle risposte di Claude degrada in modo proporzionale alla quantità di informazioni presenti. Questo avviene perché il modello deve "distribuire la sua attenzione" su tutti gli elementi presenti nel contesto. Meno rumore c'è, più nitida è la risposta.

Pensate a questo come ascoltare una persona in una stanza silenziosa versus ascoltarla in un mercato affollato. In entrambi i casi "sentite", ma la qualità dell'ascolto è radicalmente diversa.

### **20.2 — Cosa Sono i Token**

#### **Definizione del Concetto**

Un token è l'unità fondamentale con cui gli LLM misurano e processano il testo. In termini semplificati — come suggerisce la guida originale — potete pensare a un token come una parola. In realtà tecnicamente un token corrisponde a circa 3-4 lettere, ma per finalità pratiche e per questo corso, l'approssimazione "un token ≈ una parola" è sufficiente.

#### **Spiegazione Approfondita**

Quando voi scrivete un messaggio a Claude, quel messaggio viene scomposto in token prima di essere processato. Ad esempio:

* La frase "Ciao come stai" potrebbe essere scomposta in 3-4 token  
* La frase "Per favore analizza il codice del mio progetto e trova i bug" potrebbe essere 10-12 token  
* Un intero file di codice di 500 righe potrebbe essere migliaia di token

Il modello Claude ha un limite massimo di token per il contesto. A seconda del modello utilizzato, questo limite può essere:

* 200.000 token (200K) per le configurazioni standard  
* 1.000.000 token (1M) per configurazioni specifiche

Questo numero rappresenta il totale di tutto ciò che può stare nella "scrivania" del modello: input vostro, output di Claude, istruzioni di sistema, MCP, skill, memoria — tutto insieme.

#### **Il Meccanismo Sottostante**

I token non corrispondono esattamente alle parole perché il sistema di tokenizzazione (il processo con cui il testo viene convertito in token) funziona diversamente dalla divisione per parole che facciamo noi umani:

Esempio di tokenizzazione approssimativa:

Testo: "Costruiamo un'applicazione web"  
Token: \["Costru", "iamo", " un", "'", "applic", "azione", " web"\]  
Risultato: \~7 token per 3 parole

Testo: "Hello world"  
Token: \["Hello", " world"\]

Risultato: \~2 token per 2 parole

Notate come le parole italiane tendono a consumare più token rispetto a quelle inglesi. Questo accade perché i modelli LLM sono stati addestrati prevalentemente su testo inglese, quindi il tokenizzatore è più "efficiente" con l'inglese.

#### **Perché i Token Contano**

I token sono la valuta di Claude Code. Ogni azione ha un costo in token:

| Azione | Consumo Token Approssimativo |
| ----- | ----- |
| Un messaggio breve dell'utente | 50-200 token |
| Una risposta breve di Claude | 200-500 token |
| Lettura di un file di codice medio | 1.000-5.000 token |
| System prompt di Anthropic | \~10.000-20.000 token |
| Un MCP leggero (Chrome Dev Tool) | \~200 token (0,1% del contesto) |
| Un MCP pesante (ClickUp) | \~54.000 token (27% del contesto) |
| Le skill del progetto | \~600 token (0,3% del contesto) |

#### **Interpretazione Pratica**

Nella barra di stato di Claude Code (quella che avete configurato seguendo le istruzioni nella Parte 2 del manuale), vedrete due informazioni relative ai token:

1. Percentuale di contesto utilizzato: ad esempio "14% used" — questo indica quanto della finestra totale è occupato  
2. Token totali disponibili: ad esempio "200K" — questo è il limite massimo  
3. Costo API equivalente: se usaste il piano API al posto dell'abbonamento, questo sarebbe il costo effettivo della chiamata

Queste informazioni sono fondamentali per prendere decisioni in tempo reale durante il lavoro.

#### **Nota Importante sui Piani**

Se utilizzate il piano Pro ($17/mese) o il piano Max ($100/mese o superiore), il costo dei token è incluso nell'abbonamento. Il costo visualizzato nella barra di stato è puramente informativo — vi mostra quanto avreste speso se foste sul piano API. Tuttavia, anche con un piano in abbonamento, la gestione del contesto resta fondamentale perché la qualità delle risposte dipende da quanto efficientemente usate il contesto disponibile, non solo da quanto ne avete.

#### **Errori Comuni**

1. Pensare che "tanto ho token illimitati con l'abbonamento": l'abbonamento vi dà accesso illimitato alle chiamate, ma ogni singola sessione ha un limite di contesto fisso. Se lo riempite, le prestazioni degradano indipendentemente dal piano.  
2. Non distinguere tra token di input e token di output: i token che voi scrivete (input) e quelli che Claude produce (output) occupano entrambi spazio nel contesto. Una risposta molto lunga di Claude consuma contesto esattamente come un prompt lungo vostro.  
3. Ignorare il consumo "invisibile": prima ancora che voi scriviate il primo messaggio, una percentuale significativa del contesto è già occupata dal system prompt di Anthropic, dagli MCP e dalle configurazioni del progetto.

#### **Insight Avanzato**

Esiste una relazione diretta tra il numero di token nel contesto e la latenza (tempo di risposta) di Claude. Più token ci sono nel contesto, più tempo impiega Claude per elaborare una risposta, perché deve "leggere" e "considerare" tutto ciò che è presente. Questo significa che un contesto snello non solo produce risposte migliori, ma anche risposte più veloci. L'ottimizzazione del contesto è quindi un'ottimizzazione sia qualitativa che temporale.

### **20.3 — La Composizione del Contesto in Claude Code**

#### **Definizione del Concetto**

Il contesto in Claude Code non è composto solo dalla vostra conversazione. È un aggregato di molteplici fonti che vengono tutte caricate nella finestra di contesto prima e durante la sessione di lavoro. Comprendere questa composizione è essenziale per gestire il contesto in modo professionale.

#### **Spiegazione Approfondita — Mappa Completa del Contesto**

Dalla guida originale e dall'analisi pratica del comando /context, sappiamo che il contesto è composto dalle seguenti componenti, elencate nell'ordine in cui vengono caricate:

╔══════════════════════════════════════════════════════════════╗  
║                    FINESTRA DI CONTESTO                      ║  
║                     (es. 200.000 token)                      ║  
╠══════════════════════════════════════════════════════════════╣  
║                                                              ║  
║  ┌─────────────────────────────────────────────────────┐     ║  
║  │  1\. SYSTEM PROMPT (iniettato da Anthropic)          │     ║  
║  │     → Non modificabile dall'utente                  │     ║  
║  │     → Circa 10-12% del contesto                     │     ║  
║  └─────────────────────────────────────────────────────┘     ║  
║                                                              ║  
║  ┌─────────────────────────────────────────────────────┐     ║  
║  │  2\. SYSTEM TOOLS                                    │     ║  
║  │     → Comandi bash, read, write, edit, etc.         │     ║  
║  │     → Definizioni dei tool disponibili              │     ║  
║  └─────────────────────────────────────────────────────┘     ║  
║                                                              ║  
║  ┌─────────────────────────────────────────────────────┐    ║  
║  │  3\. MCP TOOLS                                       │    ║  
║  │     → Chrome Dev Tool, ClickUp, etc.                │    ║  
║  │     → VARIABILE: da 0,1% a 27%+ del contesto       │     ║  
║  └─────────────────────────────────────────────────────┘    ║  
║                                                             ║  
║  ┌─────────────────────────────────────────────────────┐    ║  
║  │  4\. MEMORY FILES                                    │    ║  
║  │     → memory.md                                     │    ║  
║  │     → auto\_memory.md                                │    ║  
║  │     → CLAUDE.md del progetto                        │    ║  
║  │     → Rules del workspace                           │    ║  
║  └─────────────────────────────────────────────────────┘    ║  
║                                                             ║  
║  ┌─────────────────────────────────────────────────────┐    ║  
║  │  5\. SKILL                                           │    ║  
║  │     → Generalmente molto leggere (\~0,3%)            │    ║  
║  └─────────────────────────────────────────────────────┘    ║  
║                                                             ║  
║  ┌─────────────────────────────────────────────────────┐    ║  
║  │  6\. MESSAGGI (la vostra conversazione)              │    ║  
║  │     → Input dell'utente \+ Output di Claude          │    ║  
║  │     → Cresce con ogni scambio                       │    ║  
║  └─────────────────────────────────────────────────────┘    ║  
║                                                             ║  
║  ┌─────────────────────────────────────────────────────┐    ║  
║  │  7\. AUTOCOMPACT BUFFER                              │    ║  
║  │     → \~33.000 token riservati                       │    ║  
║  │     → Spazio per la compattazione automatica        │    ║  
║  └─────────────────────────────────────────────────────┘    ║  
║                                                             ║  
║  ┌─────────────────────────────────────────────────────┐    ║  
║  │  8\. SPAZIO LIBERO                                   │    ║  
║  │     → Disponibile per nuovi messaggi e operazioni   │    ║  
║  └─────────────────────────────────────────────────────┘    ║  
║                                                             ║

╚══════════════════════════════════════════════════════════════╝

#### **Il Problema del Contesto "Pre-Occupato"**

Un dato fondamentale emerso dalla guida originale è questo: prima ancora di scrivere il vostro primo messaggio, una percentuale significativa del contesto è già occupata.

Nell'esempio pratico mostrato nella guida:

| Componente | % del Contesto |
| ----- | ----- |
| System Prompt (Anthropic) | \~10% |
| System Tools | \~0,7% |
| MCP Tools (solo Chrome Dev Tool) | \~0,1% |
| Memory Files | \~4-5% |
| Skill | \~0,3% |
| Totale pre-occupato (configurazione leggera) | \~15-16% |

Ma quando vengono installati MCP pesanti:

| Componente | % del Contesto |
| ----- | ----- |
| System Prompt (Anthropic) | \~10% |
| System Tools | \~0,7% |
| MCP Tools (Chrome Dev Tool \+ ClickUp \+ Canva) | \~28% |
| Memory Files | \~4-5% |
| Skill | \~0,3% |
| Totale pre-occupato (configurazione pesante) | \~43% |

Questo significa che nel secondo caso, quasi metà del contesto è già occupata prima ancora di cominciare a lavorare. Restate con solo il 57% per la vostra effettiva conversazione e il lavoro produttivo.

#### **Perché Questo è Critico**

Immaginate di avere un serbatoio da 100 litri per un viaggio. Se prima di partire qualcuno ci mette dentro 43 litri di sabbia, vi restano solo 57 litri per la benzina. Arriverete molto meno lontano.

Lo stesso vale per il contesto. Se il 43% è occupato da MCP che forse non vi servono, avrete:

* Meno spazio per conversazioni complesse  
* Compattazioni più frequenti (con perdita potenziale di informazioni)  
* Qualità delle risposte degradata più rapidamente  
* Sessioni di lavoro più corte prima di dover resettare

#### **Interpretazione Pratica — Come Verificare**

Per vedere la composizione esatta del vostro contesto in qualsiasi momento, utilizzate il comando:

/context

Questo comando produce un'analisi dettagliata che mostra:

* Ogni componente del contesto  
* La percentuale occupata da ciascuno  
* Il totale utilizzato  
* Lo spazio libero rimanente

Questo è il vostro cruscotto di guida. Consultarlo regolarmente è un'abitudine che distingue l'utente esperto dal principiante.

#### **Errori Comuni**

1. Non controllare mai il contesto: molti utenti non sanno nemmeno che il comando /context esiste. Volano alla cieca.  
2. Attribuire errori di Claude alla "stupidità del modello" quando in realtà il contesto è saturo: se Claude inizia a dimenticare istruzioni o a dare risposte incoerenti, la prima cosa da verificare è la percentuale di contesto utilizzata.  
3. Non considerare il costo degli MCP: come visto, un singolo MCP come ClickUp può occupare il 27% del contesto. È un prezzo enorme da pagare se non lo state effettivamente usando.

#### **Insight Avanzato**

La percentuale di contesto utilizzato e la percentuale di contesto nella barra di stato non sono necessariamente uguali. La guida originale nota specificamente questa discrepanza. Il motivo è che la barra di stato mostra una stima semplificata, mentre il comando /context fornisce l'analisi granulare reale. Usate sempre /context per le decisioni importanti.

### **20.4 — La Relazione tra Contesto e Prestazioni**

#### **Definizione del Concetto**

Esiste una relazione inversamente proporzionale tra la quantità di contesto occupato e la qualità delle prestazioni di Claude. Questa relazione non è lineare: le prestazioni non degradano in modo uniforme, ma seguono un pattern specifico legato ai bias cognitivi del modello.

#### **Spiegazione Approfondita**

La guida originale introduce un grafico concettuale che possiamo rappresentare così:

Qualità delle Prestazioni  
        │  
   100% ┤ ████  
        │ ████████  
    75% ┤ ████████████  
        │ ████████████████  
    50% ┤ ████████████████████  
        │ ████████████████████████  
    25% ┤ ████████████████████████████  
        │ ████████████████████████████████  
     0% ┤─────────────────────────────────────  
        0%   20%   40%   60%   80%   100%

                 Contesto Utilizzato

Le prestazioni diminuiscono man mano che il contesto si riempie, e la diminuzione accelera nella seconda metà. Questo significa che:

* Da 0% a 30% di contesto: prestazioni eccellenti  
* Da 30% a 60% di contesto: prestazioni buone, leggero calo  
* Da 60% a 80% di contesto: prestazioni in calo visibile  
* Da 80% a 100% di contesto: prestazioni significativamente degradate

#### **Implicazione Pratica Diretta**

Quando nella guida l'autore vede che il contesto è al 66%, dice immediatamente a Claude: *"Sei al 66% del contesto, cosa che significa che comincerai a perdermi a livello di performance."* E chiede di salvare le informazioni importanti in memoria per poter iniziare una nuova sessione pulita.

Questa è la strategia corretta: non aspettare che il contesto sia al 90% per reagire. Già al 60-70% è il momento di:

1. Compattare il contesto (/compact)  
2. Salvare informazioni critiche nella memoria  
3. Considerare di iniziare una nuova sessione  
4. Fornire a Claude un prompt di continuazione per la sessione successiva

#### **Perché le Prestazioni Degradano**

Le prestazioni degradano per diverse ragioni tecniche che è utile comprendere almeno a livello intuitivo:

1. Dispersione dell'attenzione: il modello deve distribuire la sua "attenzione computazionale" su tutti i token presenti. Più token ci sono, meno attenzione viene data a ciascuno.  
2. Conflitto di istruzioni: con più contesto, aumenta la probabilità che ci siano istruzioni contraddittorie o ambigue, causando incertezza nel modello.  
3. Allucinazioni: quando il contesto è saturo, il modello è più propenso a "inventare" informazioni anziché ammettere di non sapere, perché ha troppi pattern tra cui scegliere.  
4. Perdita di focus: le istruzioni iniziali (il CLAUDE.md, le regole) vengono "diluite" dalla massa di conversazione successiva.

# **CAPITOLO 21**

## **Analisi e Monitoraggio del Contesto**

### **21.1 — Il Comando /context**

#### **Definizione del Concetto**

Il comando /context è lo strumento diagnostico primario per il Context Management in Claude Code. Digitando questo comando nel terminal, si ottiene un'analisi completa e granulare di come il contesto è attualmente distribuito tra le varie componenti.

#### **Spiegazione Approfondita**

Quando digitate /context nel terminal di Claude Code, il sistema produce un report che include:

1. System Prompt: la percentuale occupata dalle istruzioni iniettate da Anthropic  
2. System Tools: la percentuale occupata dalle definizioni dei tool di sistema (bash, read, write, edit, etc.)  
3. MCP Tools: la percentuale occupata da ogni MCP installato, elencato individualmente  
4. Memory Files: la percentuale occupata dai file di memoria (memory.md, auto\_memory.md, CLAUDE.md, rules, etc.)  
5. Skill: la percentuale occupata dalle skill del progetto  
6. Messages: la percentuale occupata dalla conversazione attuale  
7. Autocompact Buffer: lo spazio riservato per la compattazione automatica  
8. Spazio Libero: la percentuale ancora disponibile

#### **Come Leggere il Report**

Quando vedete il report del contesto, la prima cosa da fare è identificare eventuali anomalie. Un'anomalia è qualsiasi componente che occupa una percentuale inaspettatamente alta. Ad esempio:

* Se gli MCP Tools occupano il 27%, avete un problema di contesto  
* Se i Messages occupano il 60%, probabilmente è ora di compattare o iniziare una nuova sessione  
* Se le Skill occupano più del 2-3%, potreste avere skill troppo verbose che necessitano di ottimizzazione

#### **Interpretazione Pratica — Workflow di Monitoraggio**

Il monitoraggio del contesto dovrebbe seguire questo workflow:

┌──────────────────────────────────┐  
│   INIZIO SESSIONE DI LAVORO      │  
│   → Esegui /context              │  
│   → Verifica stato iniziale      │  
│   → Nota la % pre-occupata       │  
└──────────────┬───────────────────┘  
               │  
               ▼  
┌──────────────────────────────────┐  
│   DURANTE IL LAVORO              │  
│   → Ogni 15-20 messaggi, o       │  
│     quando noti risposte         │  
│     meno accurate, esegui        │  
│     /context                     │  
└──────────────┬───────────────────┘  
               │  
               ▼  
┌──────────────────────────────────┐  
│   CONTESTO \> 60%?                │  
│                                  │  
│   SÌ → Compatta con /compact     │  
│        oppure salva in memoria   │  
│        e inizia nuova sessione   │  
│                                  │  
│   NO → Continua a lavorare       │

└──────────────────────────────────┘

#### **Perché Monitorare Regolarmente**

Il monitoraggio regolare serve a tre scopi:

1. Prevenzione: identificare problemi di contesto prima che impattino la qualità del lavoro  
2. Decisione informata: sapere se potete installare un nuovo MCP o se dovete prima liberare spazio  
3. Apprendimento: con il tempo, svilupperete un'intuizione su come le diverse azioni impattano il contesto

#### **Errori Comuni**

1. Monitorare solo quando qualcosa va storto: a quel punto il danno è fatto. Il contesto è già saturo e le risposte sono degradate. Monitorate proattivamente.  
2. Non sapere che il comando esiste: molti utenti di Claude Code non hanno mai digitato /context. È come guidare un'auto senza mai guardare il livello della benzina.  
3. Confondere la barra di stato con l'analisi reale: la barra di stato in basso al terminal mostra una percentuale approssimativa. Il comando /context è l'unica fonte accurata.

### **21.2 — La Barra di Stato (Status Line)**

#### **Definizione del Concetto**

La Status Line è una barra informativa posizionata nella parte inferiore del terminal di Claude Code che mostra in tempo reale informazioni chiave sulla sessione corrente: percentuale di contesto utilizzato, costo equivalente API, token totali disponibili e durata della sessione.

#### **Spiegazione Approfondita**

La Status Line mostra le seguenti informazioni:

| Elemento | Significato | Esempio |
| ----- | ----- | ----- |
| % used | Percentuale del contesto utilizzata | 14% used |
| Cost | Costo equivalente se si usasse il piano API | $0.03 |
| Token totali | Dimensione totale della finestra di contesto | 200K |
| Durata sessione | Da quanto tempo è attiva la sessione | 5m |

#### **Come Configurare la Status Line**

Per ottenere la Status Line, esistono due metodi:

Metodo 1 — Comando diretto:

/status line

Premete Enter e la barra verrà configurata automaticamente.

Metodo 2 — Prompt a Claude Code:  
Nel caso in cui il Metodo 1 non funzionasse, l'autore della guida suggerisce un approccio ingegnoso:

1. Fate uno screenshot della barra di stato che volete replicare (ad esempio dalla guida o da un video)  
2. Incollatelo nel terminal  
3. Dite a Claude: *"Per favore fai sì che io abbia sotto al terminal queste cose qui"*  
4. Claude configurerà automaticamente la Status Line

Questa è un'applicazione pratica di un principio fondamentale: la vostra vita con Claude Code sarà sempre alla distanza di un buon prompt dal risolvere i vostri problemi.

#### **Interpretazione Pratica**

La Status Line è il vostro indicatore di carburante durante la guida. Non è precisa come il comando /context (che è il vostro cruscotto diagnostico completo), ma è sempre visibile e vi dà un'indicazione rapida di dove siete.

Abitudini corrette con la Status Line:

* Guardarla dopo ogni scambio significativo con Claude  
* Preoccuparvi quando supera il 50-60%: è il momento di iniziare a pensare alla gestione del contesto  
* Non ignorarla mai quando supera il 70%: a questo punto le azioni di gestione del contesto diventano urgenti

#### **La Discrepanza tra Percentuale e Token**

La guida originale nota che la percentuale mostrata nella Status Line e il numero di token "non sono uguali". Questo avviene perché:

* La percentuale è calcolata sul contesto totale disponibile  
* Il numero di token potrebbe riferirsi al totale di token processati (input \+ output cumulativi), che può superare il contesto disponibile grazie alla compattazione  
* La durata della sessione influenza questa discrepanza perché la compattazione ridistribuisce i token

La regola pratica è: fidatevi della percentuale per le decisioni operative. Se dice 60%, agite di conseguenza, indipendentemente dal numero assoluto di token mostrato.

### **21.3 — Il Comando /config e le Informazioni di Sistema**

#### **Definizione del Concetto**

Il comando /config apre un pannello di configurazione completo che mostra tutte le impostazioni attive di Claude Code. Tra le informazioni disponibili in questo pannello, ci sono anche dati relativi alla gestione del contesto.

#### **Spiegazione Approfondita**

Quando digitate /config nel terminal, potete navigare tra diverse sezioni usando le frecce su/giù e il tasto Tab. Le sezioni principali sono:

Sezione Config:

* Autocompact: mostra se la compattazione automatica è attiva (on/off)  
* Thinking Mode: mostra se la modalità di pensiero estensivo è attiva  
* Rewind Checkpoint: mostra se i checkpoint di ripristino sono attivi  
* Tema e personalizzazione visiva  
* Teammate Mode e altre impostazioni avanzate

Sezione Usage (raggiungibile premendo Tab):

* Mostra quanto del modello è stato utilizzato nella sessione corrente  
* Nell'esempio della guida: "28% utilizzato al momento"

Sezione Status (raggiungibile premendo Tab di nuovo):

* Mostra un riepilogo delle informazioni della Status Line

#### **Autocompact nel Config**

L'impostazione più rilevante per il Context Management nel pannello /config è Autocompact. Quando questa è impostata su "on":

* Claude compatta automaticamente il contesto quando raggiunge una certa soglia  
* Non dovete fare nulla manualmente per attivare la compattazione  
* Il sistema gestisce autonomamente la densità delle informazioni

Quando è su "off":

* Il contesto si riempie linearmente senza compressione  
* Dovete usare manualmente /compact per liberare spazio  
* Avete più controllo ma più responsabilità

Raccomandazione: tenete Autocompact su on. La gestione automatica è generalmente superiore a quella manuale per la maggior parte degli utenti. Potrete sempre usare /compact manualmente in aggiunta quando necessario.

#### **Rewind Checkpoint nel Config**

Questa funzione è rilevante per il Context Management perché i checkpoint occupano spazio. Quando è su "on":

* Claude salva dei punti di ripristino a cui potete tornare  
* Potete dire "torna alla versione precedente" e Claude lo farà  
* Questi checkpoint consumano una piccola quantità di contesto aggiuntiva

Quando è su "off":

* Non ci sono checkpoint  
* Non potete fare rollback delle azioni  
* Risparmiate una piccola quantità di contesto

Raccomandazione: tenete i checkpoint su on. Lo spazio che consumano è minimo rispetto al vantaggio di poter tornare indietro in caso di errore.

#  **CAPITOLO 22**

## **Auto Compact e Densità Informativa**

**22.1 — Il Concetto di Densità Informativa**

#### **Definizione del Concetto**

La densità informativa è il rapporto tra la quantità di informazione utile contenuta in un testo e il numero di token utilizzati per esprimerla. Un testo ad alta densità informativa comunica molta informazione con pochi token. Un testo a bassa densità informativa spreca token con parole inutili, ripetizioni e informazioni irrilevanti.

#### **Spiegazione Approfondita**

La guida originale fornisce un esempio perfetto per comprendere questo concetto. Immaginate di scrivere questo prompt a Claude:

Prompt a bassa densità informativa:

*"Ciao sono Giovanni ho 30 anni il mio compleanno il 27 di febbraio quindi qualche giorno fa mi piacciono le pentole ah no le pentole non c'entrano vivo a Lussemburgo e bla bla bla"*

In questo prompt ci sono informazioni rilevanti e informazioni irrilevanti mescolate insieme:

| Informazione | Rilevante? | Motivo |
| ----- | ----- | ----- |
| "Ciao" | No | Convenevole inutile per il contesto |
| "sono Giovanni" | Sì | Identità dell'utente |
| "ho 30 anni" | Sì | Dato anagrafico potenzialmente utile |
| "il mio compleanno il 27 di febbraio" | Sì | Dato specifico |
| "qualche giorno fa" | No | Deduzione inutile, spreca token |
| "mi piacciono le pentole" | No | Totalmente irrilevante |
| "ah no le pentole non c'entrano" | No | Correzione di un errore proprio, doppio spreco |
| "vivo a Lussemburgo" | Sì | Dato geografico |
| "bla bla bla" | No | Riempitivo |

Prompt ad alta densità informativa (equivalente):

*"Giovanni, 30 anni, Lussemburgo, compleanno 27 febbraio"*

Stesse informazioni utili, un quinto dei token. Questo è il principio della densità informativa.

#### **Il Meccanismo dell'Autocompact**

L'Autocompact è la funzione di Claude Code che automatizza questo processo di aumento della densità informativa. Ecco come funziona:

PROCESSO DI AUTOCOMPACT  
═══════════════════════

PRIMA della compattazione:  
┌────────────────────────────────────────────────┐  
│ Utente: Ciao, mi chiamo Giovanni, vivo a       │  
│ Lussemburgo, ho 30 anni, il mio compleanno     │  
│ è il 27 febbraio, mi piacciono le pentole      │  
│ ah no le pentole non c'entrano...              │  
│                                                │  
│ Claude: Ciao Giovanni\! Piacere di conoscerti\!  │  
│ Come posso aiutarti oggi? Vedo che vivi a      │  
│ Lussemburgo, bellissimo posto\! E auguri in     │  
│ ritardo per il tuo compleanno\!                 │  
│                                                │  
│ Utente: Grazie, allora vorrei...               │  
│ \[... altri 50 messaggi di conversazione ...\]   │  
│                                                │  
│ CONSUMO: 85% del contesto                      │  
└────────────────────────────────────────────────┘

DOPO la compattazione:  
┌────────────────────────────────────────────────┐  
│ • User: Giovanni, 30 anni, Lussemburgo,        │  
│   compleanno 27 febbraio                        │  
│ • Richiesta principale: \[sintesi della task\]    │  
│ • Azioni completate: \[lista bullet point\]       │  
│ • Stato attuale: \[sintesi dello stato\]          │  
│ • Decisioni prese: \[lista decisioni\]            │  
│                                                 │  
│ CONSUMO: 25% del contesto                       │

└────────────────────────────────────────────────┘

Come potete vedere, il processo di compattazione:

1. Elimina tutte le parole ridondanti e i convenevoli  
2. Sintetizza le conversazioni in bullet point ad alta densità  
3. Preserva le informazioni chiave e le decisioni prese  
4. Riduce drasticamente il consumo di contesto

#### **Perché l'Autocompact è Fondamentale**

Senza Autocompact, ogni sessione di lavoro con Claude Code avrebbe una durata massima limitata dalla dimensione del contesto. Con conversazioni intensive, potreste esaurire il contesto in 20-30 messaggi. L'Autocompact vi permette di estendere le sessioni molto oltre questo limite, comprimendo periodicamente le informazioni accumulate.

#### **Il Buffer di Autocompact**

L'Autocompact utilizza un buffer riservato di circa 33.000 token. Questo buffer funziona come una zona di transito:

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

Quando il contesto raggiunge la soglia del buffer, Claude si prende un momento (noterete che "pensa" più a lungo del solito) e riscrive tutta la conversazione in formato compresso. Dopo questa operazione, il contesto torna a un livello più basso e potete continuare a lavorare.

#### **Interpretazione Pratica — Il Formato Compattato**

Dopo una compattazione, se esaminate il contesto compattato (visibile con il comando /compact), vedrete qualcosa del genere:

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

Questo è ciò che la guida chiama formato "ad alta densità" — tutta la conversazione precedente condensata in bullet point essenziali.

### **22.2 — Il Comando /compact**

#### **Definizione del Concetto**

Il comando /compact è lo strumento manuale per attivare la compattazione del contesto. A differenza dell'Autocompact (che si attiva automaticamente a una certa soglia), /compact può essere eseguito in qualsiasi momento per forzare una compressione della conversazione.

#### **Spiegazione Approfondita**

Quando digitate /compact nel terminal:

1. Claude analizza tutta la conversazione presente nel contesto  
2. Identifica le informazioni essenziali: decisioni prese, azioni completate, stato attuale, istruzioni pendenti  
3. Riscrive tutto in formato bullet point ad alta densità  
4. Sostituisce la conversazione originale con la versione compressa  
5. Il contesto si riduce significativamente

#### **Quando Usare /compact Manualmente**

| Situazione | Azione Raccomandata |
| ----- | ----- |
| Contesto sopra il 60% e dovete continuare a lavorare | Eseguite /compact |
| State per dare un prompt complesso che richiede molto contesto | Eseguite /compact prima |
| Claude inizia a "dimenticare" cose dette in precedenza | Probabilmente il contesto è saturo, eseguite /compact |
| State per chiamare un sub-agente che produrrà molto output | Liberate spazio prima con /compact |
| Volete iniziare una fase nuova del progetto nella stessa sessione | Eseguite /compact per "pulire" la fase precedente |

#### **Differenza tra /compact e Nuova Sessione**

Una domanda che molti utenti si pongono è: "È meglio compattare o iniziare una nuova sessione?" La risposta dipende dalla situazione:

Usate /compact quando:

* Il lavoro è continuo e avete bisogno del contesto precedente  
* Siete a metà di un'implementazione  
* Le informazioni accumulate sono ancora rilevanti

Iniziate una nuova sessione quando:

* Passate a un argomento o task completamente diverso  
* Il contesto è oltre l'80% anche dopo compattazione  
* Volete un "foglio bianco" per una nuova fase

Strategia combinata (raccomandata dall'autore della guida):

1. Quando il contesto supera il 65-70%  
2. Dite a Claude: *"Salva in memoria le informazioni importanti per la prossima sessione"*  
3. Claude scrive le informazioni nel memory.md  
4. Iniziate una nuova sessione  
5. Nella nuova sessione, Claude recupera automaticamente le informazioni salvate in memoria  
6. Continuate il lavoro con un contesto fresco

Questo è esattamente ciò che l'autore della guida fa nel video quando è al 66% di contesto e deve ancora integrare Stripe nell'applicazione Trello.

#### **Errori Comuni**

1. Usare /compact troppo frequentemente: ogni compattazione perde una piccola quantità di sfumature e dettagli. Se compattate ogni 5 messaggi, state perdendo troppe informazioni.  
2. Non usare /compact mai: l'estremo opposto. Se lasciate che il contesto si saturi senza mai intervenire, la qualità degraderà inesorabilmente.  
3. Compattare e poi ripetere le stesse informazioni: se dopo /compact riscrivete tutto quello che avevate detto prima, avete annullato il vantaggio della compattazione.  
4. Aspettarsi che la compattazione preservi tutto: la compattazione è una lossy compression — una compressione con perdita. Le informazioni principali vengono preservate, ma i dettagli minori potrebbero andare persi. Per questo è importante salvare informazioni critiche nel memory.md prima di compattare.

#### **Insight Avanzato**

La qualità della compattazione dipende dalla qualità della vostra conversazione. Se avete scritto prompt chiari, strutturati e con informazioni ben organizzate, la compattazione produrrà un riassunto eccellente. Se la vostra conversazione è caotica, piena di ripensamenti e deviazioni, la compattazione potrebbe perdere informazioni importanti perché non riesce a distinguerle dal rumore.

Questo crea un circolo virtuoso: scrivere prompt migliori → compattazione più efficace → più contesto disponibile → risposte migliori → workflow più efficiente.

### **22.3 — Strategie Pratiche per l'Efficienza del Contesto**

#### **La Lista delle Cose da Fare e Non Fare**

La guida originale fornisce un "80/20" delle best practice per il Context Management. Espandiamo ciascuna:

✅ COSE DA FARE:

1\. Lanciare /init quando si inizia un nuovo progetto

Il comando /init crea automaticamente un CLAUDE.md strutturato secondo le best practice. Questo assicura che il contesto iniziale sia organizzato in modo efficiente. Un CLAUDE.md ben strutturato consuma meno contesto di uno caotico per la stessa quantità di informazioni.

2\. Mettere le regole più importanti in cima al CLAUDE.md

Questo è legato direttamente al fenomeno del Primacy Bias che tratteremo nel Capitolo 23\. Le regole posizionate all'inizio del CLAUDE.md vengono "ricordate" meglio dall'LLM. Esempi di regole critiche da mettere in cima:

* "Non cancellare mai il file X"  
* "Non rimuovere le API key"  
* "Non modificare il database di produzione"  
* "Chiedi sempre conferma prima di cancellare file"

3\. Tenere sotto controllo il file CLAUDE.md e sfoltirlo regolarmente

Il CLAUDE.md tende a crescere nel tempo man mano che aggiungete regole e istruzioni. Periodicamente:

* Rimuovete regole che non sono più rilevanti  
* Consolidate regole simili  
* Spostate regole specifiche nelle sotto-cartelle (rules/)  
* Verificate che non ci siano ripetizioni

4\. Spezzare il CLAUDE.md in regole modulari

Come spiegato nelle Parti precedenti del manuale, invece di avere un unico CLAUDE.md monolitico, è molto più efficiente spezzare le regole in file separati nella cartella .claude/rules/:

Prima (inefficiente):  
CLAUDE.md → un unico file enorme che viene caricato per intero

Dopo (efficiente):  
CLAUDE.md → piccolo, solo regole essenziali  
.claude/rules/design-fidelity.md → regole di design  
.claude/rules/security.md → regole di sicurezza

.claude/rules/screenshot-workflow.md → regole per gli screenshot

Il vantaggio è che Claude carica solo le regole rilevanti per la task corrente, non tutte le regole di tutti gli aspetti del progetto.

5\. Inserire errori ricorrenti direttamente nel CLAUDE.md

Quando Claude continua a fare lo stesso errore nonostante le vostre correzioni, la soluzione è codificarlo nel CLAUDE.md:

*"Se Claude te lo fa due-tre volte, inseriscilo nel CLAUDE.md. Lo fai hard code dentro e hai risolto i tuoi problemi."*

Questo trasforma un problema ricorrente (che consuma contesto ogni volta che dovete correggerlo) in una regola permanente (che previene il problema alla fonte).

6\. Raccogliere regolarmente le best practice aggiornate

L'autore della guida condivide la sua strategia personale per rimanere aggiornato:

* Va su X (Twitter)  
* Segue Boris (il fondatore di Claude Code) e altri power user  
* Usa Grok per sintetizzare le novità: *"Per favore raccoglimi tutto quello che è successo nell'ultimo mese in termini di best practice di Claude e riassumile così che io possa inglobarle dentro al mio progetto"*  
* Incorpora le nuove best practice nel proprio CLAUDE.md

❌ COSE DA NON FARE:

1\. Non buttate dentro guide inutili o documentazioni API

*"Le API sono legate al vostro conto in banca."*

Caricare documentazioni API complete, guide di terze parti o blocchi enormi di testo nel contesto è uno spreco catastrofico. Questi documenti possono consumare decine di migliaia di token senza fornire valore proporzionale. Se avete bisogno di informazioni da una documentazione, chiedete a Claude di cercarle specificamente (usando il Dev Tool MCP o un sub-agente researcher) invece di caricare tutto il documento.

2\. Non scrivete regole vaghe o aspirazionali

Regole come:

* ❌ *"Non fare errori"* — è inutile e vaga  
* ❌ *"Fammi diventare ricco"* — non è un'istruzione operativa  
* ❌ *"Scrivi codice perfetto"* — non definisce cosa significhi "perfetto"

Regole efficaci sono:

* ✅ *"Quando modifichi un file, crea sempre un backup prima"*  
* ✅ *"Ogni funzione deve avere una documentazione inline"*  
* ✅ *"Dopo ogni modifica CSS, fai uno screenshot e confronta con il design di riferimento"*

Le regole vaghe non solo non aiutano Claude, ma consumano contesto senza produrre valore.

3\. Non sprecate contesto con il ciclo di verifica umano quando potete automatizzarlo

Il pattern inefficiente è:

Utente: "Fai X"  
Claude: \[fa X\]  
Utente: "Hai fatto bene?"  
Claude: "Sì"  
Utente: "Sei sicuro?"

Claude: "Sì, sono sicuro"

Ogni messaggio "Hai fatto bene?" e "Sei sicuro?" è uno spreco di contesto. Invece, codificate la verifica nel CLAUDE.md: *"Dopo ogni modifica, verifica automaticamente il risultato confrontandolo con il riferimento. Se ci sono differenze, correggi e ripeti."*

# **CAPITOLO 23**

## **Primacy Bias, Recency Bias e Lost in the Middle**

### **23.1 — Introduzione ai Bias Cognitivi degli LLM**

#### **Definizione del Concetto**

I bias cognitivi degli LLM sono pattern sistematici nel modo in cui i modelli di linguaggio processano e "ricordano" le informazioni all'interno del contesto. Esattamente come gli esseri umani hanno bias cognitivi che influenzano la memoria e il giudizio, anche gli LLM presentano pattern prevedibili che dobbiamo conoscere e sfruttare.

#### **Spiegazione Approfondita**

La guida originale introduce tre concetti fondamentali che rappresentano il cuore del Context Management avanzato:

1. Primacy Bias (Bias di Primato): il modello ricorda molto bene le informazioni posizionate all'inizio del contesto  
2. Recency Bias (Bias di Recenza): il modello ricorda molto bene le informazioni posizionate alla fine del contesto  
3. Lost in the Middle (Perso nel Mezzo): il modello ha difficoltà significative a ricordare e utilizzare le informazioni posizionate nel mezzo del contesto

Questi tre fenomeni insieme creano una curva di "attenzione" del modello che ha una forma caratteristica a U:

Performance / Capacità di Ricordo  
        │  
   Alta ┤ ████                              ████  
        │ ████████                      ████████  
        │ ████████████            ████████████  
        │ ████████████████  ████████████████  
  Bassa ┤ ████████████████████████████████████  
        │  
        └──────────────────────────────────────  
          INIZIO       MEZZO          FINE  
                del contesto  
            
          ◄─────►                   ◄─────►  
          Primacy                   Recency  
           Bias                     Bias  
            
                    ◄───────►  
                   Lost in the

                     Middle

### **23.2 — Il Primacy Bias (Bias di Primato)**

#### **Definizione del Concetto**

Il Primacy Bias è la tendenza degli LLM a dare maggiore peso e attenzione alle informazioni che appaiono all'inizio del contesto. Proprio come gli esseri umani tendono a ricordare meglio le prime informazioni ricevute (il "primo impatto"), gli LLM processano le istruzioni iniziali con maggiore fedeltà.

#### **Spiegazione Approfondita**

Questo bias ha implicazioni enormi per come strutturate il vostro CLAUDE.md e i vostri prompt. Le istruzioni posizionate all'inizio del contesto:

* Vengono seguite con maggiore coerenza  
* Vengono rispettate anche quando il contesto si riempie  
* Hanno un effetto più duraturo sulla sessione di lavoro  
* Resistono meglio alla "diluizione" causata da messaggi successivi

#### **Applicazione Pratica Diretta**

Regola d'oro del Primacy Bias:

*Mettete le regole più importanti PER PRIME nel CLAUDE.md.*

Esempi concreti:

in Markdown

**\# CLAUDE.md — Struttura Ottimizzata per Primacy Bias**

**\#\# REGOLE CRITICHE (INIZIO \= massima attenzione)**  
\- NON cancellare MAI il file .env  
\- NON rimuovere MAI le API key dal codice  
\- NON modificare MAI il database di produzione  
\- Chiedi SEMPRE conferma prima di eliminare file

**\#\# Regole Operative (mezzo \= attenzione moderata)**  
\- Usa TypeScript per tutti i nuovi file  
\- Segui le convenzioni ESLint del progetto  
\- Scrivi commenti in italiano

**\#\# Preferenze Stilistiche (fine \= attenzione elevata grazie al Recency)**  
\- Preferisci componenti funzionali a classi

\- Usa Tailwind CSS per lo styling

Notate come le regole critiche per la sicurezza sono posizionate all'inizio, dove il Primacy Bias garantisce la massima attenzione. Le regole operative sono nel mezzo (dove saranno meno "ricordate" ma non sono critiche se occasionalmente ignorate). Le preferenze stilistiche sono alla fine, dove il Recency Bias le mantiene presenti.

#### **L'Analogia della Lista della Spesa**

L'autore della guida usa un'analogia perfetta. Dice di avere "una memoria personale di un pesce rosso" e racconta:

*Immaginate che qualcuno vi dica: "Per favore vai al supermercato alle 6 e compra: biscotti, latte, pane, uova, burro, farina, zucchero, sale, olio, aceto."*

La maggior parte delle persone ricorderà:

* Biscotti (primo elemento — Primacy Bias) ✅  
* Aceto (ultimo elemento — Recency Bias) ✅  
* Pochi o nessuno degli elementi nel mezzo ❌

Lo stesso identico pattern si applica agli LLM.

#### **Errori Comuni**

1. Mettere regole critiche nel mezzo del CLAUDE.md: è il peggior posto possibile. Saranno le prime a essere "dimenticate" quando il contesto si riempie.  
2. Mettere disclaimer o introduzioni lunghe all'inizio: se iniziate il CLAUDE.md con tre paragrafi di spiegazione generale del progetto, state "sprecando" la posizione più pregiata (l'inizio) per informazioni a basso impatto.  
3. Non ordinare le regole per importanza: molti utenti scrivono le regole nell'ordine in cui le pensano, non nell'ordine di importanza. Ristrutturate il CLAUDE.md mettendo le regole più critiche prima.

### **23.3 — Il Recency Bias (Bias di Recenza)**

#### **Definizione del Concetto**

Il Recency Bias è la tendenza degli LLM a dare maggiore peso alle informazioni che appaiono alla fine del contesto — cioè le informazioni più recenti nella conversazione. L'ultimo messaggio che inviate, le ultime istruzioni che date, le ultime informazioni che condividete avranno un impatto sproporzionatamente elevato sulla risposta di Claude.

#### **Spiegazione Approfondita**

Il Recency Bias funziona a vostro vantaggio in diversi modi:

1. Correzioni immediate funzionano bene: se Claude fa un errore e lo correggete immediatamente, la correzione (essendo l'informazione più recente) viene rispettata con alta fedeltà.  
2. L'ultimo prompt è il più influente: se dovete dare un'istruzione critica, fatelo nell'ultimo messaggio prima che Claude inizi a lavorare.  
3. Le decisioni recenti prevalgono: se all'inizio della conversazione avete detto "usa il colore blu" e alla fine dite "usa il colore rosso", Claude userà il rosso (Recency Bias) a meno che la regola del blu non sia nel CLAUDE.md (Primacy Bias del system prompt).

#### **Applicazione Pratica**

Potete sfruttare il Recency Bias in modo strategico:

Strategia "Rinforzo Finale":  
Prima di dare un comando complesso a Claude, ripetete le istruzioni più importanti nell'ultimo messaggio:

Utente: "Costruisci il componente di autenticazione.   
RICORDA:   
\- usa Supabase come backend  
\- email \+ password, NO magic link  
\- salva nome e email nel database

Procedi."

Le tre istruzioni dopo "RICORDA" sono posizionate alla fine del prompt (Recency Bias), quindi Claude le seguirà con maggiore fedeltà.

Strategia "Prompt di Continuazione":  
Quando salvate informazioni in memoria per continuare in una nuova sessione, l'autore della guida mostra che Claude produce un "prompt di continuazione" — un messaggio predefinito da usare nella sessione successiva. Questo prompt, essendo il primo messaggio della nuova sessione, beneficerà del Primacy Bias nella nuova sessione E del Recency Bias (perché è l'ultimo contesto significativo salvato).

### **23.4 — Lost in the Middle — Il Fenomeno della Zona Cieca**

#### **Definizione del Concetto**

Lost in the Middle è un fenomeno documentato nella ricerca accademica sugli LLM secondo il quale le informazioni posizionate nella parte centrale del contesto vengono processate con minore attenzione e fedeltà rispetto a quelle posizionate all'inizio o alla fine. È la "zona cieca" del modello.

#### **Spiegazione Approfondita**

L'autore della guida fa riferimento a un documento di ricerca specifico chiamato "Lost in the Middle" che ha studiato questo fenomeno in modo rigoroso. Il risultato chiave è:

MODELLO DI ATTENZIONE DELL'LLM  
═══════════════════════════════

Posizione nel contesto:    INIZIO ←───────────────→ FINE  
                             
Livello di attenzione:     ██████░░░░░░░░░░░░██████  
                           ALTO  BASSO BASSO  ALTO  
                             
Qualità delle risposte:   ██████░░░░░░░░░░░░██████  
basate su info in questa   ALTA  BASSA BASSA  ALTA

posizione:

Questo fenomeno spiega perché:

* Le istruzioni nel CLAUDE.md (inizio del contesto) vengono generalmente rispettate bene  
* I vostri ultimi messaggi (fine del contesto) ricevono risposte accurate  
* Le istruzioni date a metà di una lunga conversazione vengono spesso "dimenticate" o ignorate

#### **Implicazioni per il Context Management**

La comprensione del Lost in the Middle ha implicazioni profonde per come strutturate il vostro lavoro:

1\. Struttura del CLAUDE.md:

INIZIO (Primacy Bias — massima attenzione)  
├── Regole di sicurezza critiche  
├── Vincoli inviolabili  
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

2\. Strategia di conversazione:  
Se dovete dare un'istruzione importante nel mezzo di una conversazione lunga, ripetetela. Ditela una volta quando la pensate (sarà nel mezzo), e poi ripetetela prima del prompt operativo (sarà alla fine). In questo modo, coprite sia la posizione originale che la posizione di Recency.

3\. Importanza delle regole modulari:  
Questo fenomeno è un'altra ragione per cui è fondamentale spezzare il CLAUDE.md in regole modulari. Quando Claude deve seguire una regola specifica (ad esempio design-fidelity.md), carica solo quel file. Quel file, essendo piccolo, non soffre del Lost in the Middle perché non c'è abbastanza "mezzo" da perdersi.

Confronto:

* CLAUDE.md monolitico (5.000 token): le regole nel mezzo (token 1.500-3.500) saranno nella zona cieca  
* Regola modulare (300 token): l'intero file è abbastanza corto che Claude lo processa interamente con alta attenzione

4\. L'effetto amplificato dalla distanza:  
L'autore della guida usa l'analogia dell'arco e del bersaglio per illustrare un concetto correlato: man mano che il progetto diventa più grande (la distanza dal bersaglio aumenta), l'intervallo di incertezza si amplifica. Lo stesso vale per il Lost in the Middle: man mano che il contesto si riempie, la "zona cieca" nel mezzo diventa proporzionalmente più grande e più problematica.

CONTESTO PICCOLO (20% pieno):  
███░███          Zona cieca piccola e gestibile

CONTESTO MEDIO (50% pieno):  
█████░░░░░█████  Zona cieca più grande

CONTESTO GRANDE (80% pieno):

███████░░░░░░░░░░░░░░░░███████  Zona cieca estesa e pericolosa

#### **Errori Comuni**

1. Dare istruzioni critiche una sola volta a metà conversazione: se date un'istruzione importante al messaggio \#15 di una conversazione di 40 messaggi, al messaggio \#30 Claude potrebbe averla completamente "dimenticata".  
2. Pensare che Claude "faccia apposta" a ignorare istruzioni: non è malizia, è un bias cognitivo del modello. La soluzione non è arrabbiarsi, ma posizionare strategicamente le informazioni.  
3. Non ripetere mai le istruzioni importanti: la ripetizione strategica è uno strumento legittimo e importante nel prompt engineering. Non è ridondanza — è resilienza informativa.  
4. Caricare documenti enormi nel contesto: un documento di 50.000 token avrà una zona cieca enorme nel mezzo. Claude "vedrà" bene l'inizio e la fine del documento, ma perderà dettagli cruciali nel mezzo. Meglio spezzare il documento in sezioni più piccole e caricarle una alla volta.

#### **Insight Avanzato**

Il Lost in the Middle è uno dei motivi principali per cui i sub-agenti sono così preziosi per il Context Management. Quando un sub-agente (ad esempio il Researcher) fa una ricerca che produce 100.000 token di risultati, quei token vivono nel contesto del sub-agente, non nel contesto principale. Il sub-agente, avendo processato tutto quel materiale, produce un riassunto di 2.000 token che viene inviato all'agente principale.

Questo elimina il problema del Lost in the Middle perché:

* Nel sub-agente: il documento lungo soffre del Lost in the Middle, ma il sub-agente ha come unico compito processarlo, quindi può iterare e verificare  
* Nell'agente principale: arrivano solo 2.000 token di risultato, che non creano alcuna zona cieca

È come avere un assistente che legge un libro di 500 pagine e vi fa un riassunto di 5 pagine. Voi leggete 5 pagine (nessuna zona cieca), non 500 (zona cieca enorme).

### **23.5 — Strategia Integrata di Context Management**

#### **Definizione del Concetto**

La Strategia Integrata di Context Management è l'applicazione combinata di tutti i principi discussi in questa Parte del manuale per massimizzare l'efficienza e la qualità del lavoro con Claude Code.

#### **Il Framework Completo**

Combinando tutti i concetti appresi, ecco il framework completo per la gestione del contesto:

FRAMEWORK DI CONTEXT MANAGEMENT  
════════════════════════════════

FASE 1: PRIMA DI INIZIARE  
─────────────────────────  
□ Verificare gli MCP installati → rimuovere quelli non necessari  
□ Verificare che il CLAUDE.md sia conciso e ben strutturato  
□ Verificare che le regole siano spezzate in file modulari  
□ Eseguire /context per vedere lo stato iniziale  
□ Obiettivo: tenere il contesto pre-occupato sotto il 20%

FASE 2: STRUTTURA DEL CLAUDE.MD  
────────────────────────────────  
□ Regole critiche (sicurezza, vincoli) → INIZIO  
□ Dettagli operativi → MEZZO  
□ Standard di qualità e formato → FINE  
□ Tutto il resto → file modulari in .claude/rules/

FASE 3: DURANTE IL LAVORO  
─────────────────────────  
□ Scrivere prompt concisi ad alta densità informativa  
□ Monitorare il contesto con /context ogni 15-20 messaggi  
□ Compattare con /compact quando si supera il 60%  
□ Ripetere istruzioni importanti prima dei comandi critici  
□ Non caricare documenti enormi → usare sub-agenti

FASE 4: GESTIONE DELLE TRANSIZIONI  
───────────────────────────────────  
□ Al 65-70% di contesto → salvare in memoria  
□ Chiedere a Claude il prompt di continuazione  
□ Iniziare nuova sessione con contesto fresco  
□ Nella nuova sessione: "Continua con \[task\]"

FASE 5: OTTIMIZZAZIONE CONTINUA  
────────────────────────────────  
□ Errori ricorrenti → codificarli nel CLAUDE.md  
□ MCP pesanti usati una volta → convertire in skill  
□ Regole obsolete → rimuovere dal CLAUDE.md

□ Raccogliere nuove best practice mensilmente

#### **Riepilogo delle Metriche Chiave**

| Metrica | Soglia Verde | Soglia Gialla | Soglia Rossa |
| ----- | ----- | ----- | ----- |
| Contesto pre-occupato | \< 20% | 20-35% | \> 35% |
| Contesto durante il lavoro | \< 50% | 50-70% | \> 70% |
| Skill nel contesto | \< 1% | 1-3% | \> 3% |
| MCP nel contesto | \< 5% | 5-15% | \> 15% |
| Messaggi nel contesto | \< 40% | 40-60% | \> 60% |

#### **Il Principio Fondamentale**

Se dovessimo riassumere l'intero Context Management in una singola frase, sarebbe questa:

*Ogni token nel contesto deve guadagnarsi il suo posto. Se un'informazione non contribuisce direttamente alla qualità del risultato, non dovrebbe essere nel contesto.*

Questo principio guida ogni decisione: cosa installare, cosa scrivere nel CLAUDE.md, come strutturare i prompt, quando compattare, quando iniziare una nuova sessione. È il metro con cui misurare ogni azione che impatta il contesto.

## **Riepilogo della Parte 6**

In questa Parte avete appreso:

1. Cosa sono i token e come funzionano come unità di misura del contesto  
2. Come è composto il contesto in Claude Code (system prompt, tools, MCP, memoria, skill, messaggi, buffer)  
3. Come monitorare il contesto con /context, /config e la Status Line  
4. Come funziona l'Autocompact e come usare /compact manualmente  
5. Il concetto di densità informativa e come scrivere prompt efficienti  
6. Il Primacy Bias e perché le regole importanti vanno all'inizio  
7. Il Recency Bias e come sfruttare la posizione finale per istruzioni critiche  
8. Il Lost in the Middle e perché le informazioni nel mezzo del contesto vengono "dimenticate"  
9. La strategia integrata che combina tutti questi principi in un framework operativo

Questa conoscenza è la base su cui si costruisce l'uso professionale di Claude Code. Senza Context Management, state usando Claude Code come un chatbot. Con il Context Management, lo state usando come uno strumento di produttività professionale.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - General|General Area]]
