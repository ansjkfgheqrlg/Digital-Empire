# MODULO KNOWLEDGE BASE

**K08-mcp.md** — Capitoli 31-34 | MCP: cos'è, installazione, MCP vs Skill, Chrome Dev Tool

## Riferimenti Correlati
- K07-skill-system.md (alternativa leggera agli MCP pesanti)
- K05-context.md (impatto MCP sul contesto)

---

# **PARTE 9 — MCP (MODEL CONTEXT PROTOCOL)**

---

*"L'MCP non è altro che un insieme di skill che sono state scritte da qualcun altro. Potete vederlo semplicemente come una chiavetta USB universale che se connettete ad un altro sistema vi permette di ereditare tutte le funzioni di questa applicazione."*  
*— Dalla guida originale*

---

## **Introduzione alla Parte 9**

Se le skill sono ricette che voi create per il vostro chef (Claude), gli MCP sono interi ricettari scritti da qualcun altro che potete collegare al vostro progetto con un solo comando. Sembrano una soluzione magica — e in parte lo sono — ma come ogni strumento potente, hanno un costo nascosto che bisogna comprendere prima di usarli.

Questa Parte vi insegnerà non solo cosa sono gli MCP e come installarli, ma soprattutto quando usarli e quando non usarli. La guida originale contiene una delle lezioni più importanti dell'intero corso proprio in questa sezione: l'impatto devastante che un MCP mal scelto può avere sul contesto e, di conseguenza, sulla qualità del vostro lavoro.

Questa Parte è composta da quattro capitoli:

| Capitolo | Titolo | Focus Principale |
| ----- | ----- | ----- |
| 31 | Comprendere l'MCP | Cos'è, come funziona, l'analogia della chiavetta USB |
| 32 | Installare e Gestire gli MCP | Procedura pratica e formati di configurazione |
| 33 | MCP vs Skill — Impatto sul Contesto | Il confronto critico e la strategia ottimale |
| 34 | Chrome Dev Tool MCP | L'unico MCP raccomandato per uso pratico |

---

# **CAPITOLO 31**

## **Comprendere l'MCP**

---

### **31.1 — Cos'è il Model Context Protocol**

#### **Definizione del Concetto**

L'MCP (Model Context Protocol) è un protocollo standardizzato che permette di collegare servizi e applicazioni di terze parti direttamente a Claude Code. Quando installate un MCP, Claude acquisisce automaticamente la capacità di interagire con quel servizio esterno — leggere dati, scrivere dati, eseguire operazioni — senza che dobbiate scrivere codice o creare skill manualmente.

#### **Spiegazione Approfondita**

L'analogia usata nella guida originale è perfetta per comprendere il concetto:

*"Potete vederlo semplicemente come una chiavetta USB universale che se voi avete e connettete ad un altro sistema di terze parti, sviluppato da qualcun altro, vi permette di ereditare tutte le funzioni di questa applicazione."*

Espandiamo questa analogia per renderla completamente chiara:

text

ANALOGIA: MCP COME CHIAVETTA USB UNIVERSALE  
════════════════════════════════════════════

SENZA MCP:  
┌─────────────────┐          ┌─────────────────┐  
│   CLAUDE CODE   │    ✗     │    CLICKUP      │  
│                 │◄─────────│                 │  
│  "Non so come   │  Nessuna │  "Ho tutte le   │  
│   interagire    │  connes- │   funzionalità  │  
│   con ClickUp"  │  sione   │   ma Claude non │  
│                 │          │   può usarmi"   │  
└─────────────────┘          └─────────────────┘

CON MCP:  
┌─────────────────┐          ┌─────────────────┐  
│   CLAUDE CODE   │          │    CLICKUP      │  
│                 │◄════╗    │                 │  
│  "Ora so fare   │  ║MCP║   │  "Claude ora    │  
│   tutto quello  │  ║   ║   │   può usare     │  
│   che ClickUp   │  ╚═══╝   │   tutte le mie  │  
│   sa fare\!"     │  chiavetta│   funzionalità" │  
│                 │  USB      │                 │

└─────────────────┘          └─────────────────┘

Quando collegate la "chiavetta USB" (l'MCP), Claude eredita automaticamente tutte le capacità dell'applicazione collegata. Se collegate l'MCP di ClickUp, Claude sa:

* Creare task in ClickUp  
* Leggere le board  
* Assegnare compiti  
* Aggiornare stati  
* Cercare nel workspace  
* E tutte le altre funzionalità che ClickUp espone tramite il suo MCP

#### **Il Meccanismo Sottostante**

Per comprendere perché gli MCP funzionano, bisogna capire che un MCP è essenzialmente un pacchetto di skill pre-costruite dal fornitore del servizio:

text

STRUTTURA CONCETTUALE DI UN MCP  
═══════════════════════════════

MCP di ClickUp \= insieme di skill pre-costruite:

    ┌────────────────────────────────────────────┐  
    │              MCP CLICKUP                    │  
    │                                             │  
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐ │  
    │  │ Skill 1  │  │ Skill 2  │  │ Skill 3  │ │  
    │  │ "Crea    │  │ "Leggi   │  │ "Assegna │ │  
    │  │  task"   │  │  board"  │  │  task"   │ │  
    │  └──────────┘  └──────────┘  └──────────┘ │  
    │                                             │  
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐ │  
    │  │ Skill 4  │  │ Skill 5  │  │ Skill 6  │ │  
    │  │ "Aggiorna│  │ "Cerca   │  │ "Crea    │ │  
    │  │  stato"  │  │  task"   │  │  progetto│ │  
    │  └──────────┘  └──────────┘  └──────────┘ │  
    │                                             │  
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐ │  
    │  │ Skill 7  │  │ Skill 8  │  │  ...     │ │  
    │  │ "Elimina │  │ "Commenta│  │          │ │  
    │  │  task"   │  │  task"   │  │          │ │  
    │  └──────────┘  └──────────┘  └──────────┘ │  
    │                                             │

    └────────────────────────────────────────────┘

Ognuna di queste "skill interne" all'MCP ha:

* Una descrizione di cosa fa  
* I parametri che accetta  
* Il formato della risposta  
* Le istruzioni per Claude su come utilizzarla

Tutte queste descrizioni vengono caricate nel contesto di Claude quando l'MCP è installato. Ed è esattamente qui che nasce il problema principale degli MCP, che vedremo in dettaglio nel Capitolo 33\.

#### **Perché l'MCP è Diventato Comune Solo Recentemente**

La guida menziona un dettaglio temporale importante:

*"Solo ultimamente è diventato molto più comune e molto più utilizzato."*

Questo accade perché il protocollo MCP è relativamente nuovo e la sua adozione è stata graduale. All'inizio, pochi servizi offrivano MCP compatibili con Claude Code. Man mano che Claude Code è cresciuto in popolarità e che Anthropic ha standardizzato il protocollo, sempre più aziende hanno iniziato a creare i propri MCP.

L'effetto è stato una rapida espansione dell'ecosistema: oggi esistono centinaia di MCP per servizi diversi — da ClickUp a GitHub, da Slack a database, da servizi email a strumenti di analytics.

---

### **31.2 — Tipologie di MCP**

#### **Definizione del Concetto**

Non tutti gli MCP sono uguali. Esistono differenze significative tra gli MCP in termini di peso (consumo di contesto), modalità di funzionamento e origine (chi li ha sviluppati). Comprendere queste differenze è essenziale per prendere decisioni informate su quali installare.

#### **MCP Leggeri vs MCP Pesanti**

La guida originale dimostra questa distinzione con dati concreti:

text

CONFRONTO: MCP LEGGERO vs MCP PESANTE  
══════════════════════════════════════

MCP LEGGERO — Chrome Dev Tool:  
┌──────────────────────────────────┐  
│ Consumo contesto: \~0,1%         │  
│ Funzionalità: navigazione web,  │  
│ screenshot, scraping             │  
│ Numero di "skill interne": poche│  
│ Descrizioni: concise             │  
│ IMPATTO: trascurabile            │  
└──────────────────────────────────┘

MCP PESANTE — ClickUp:  
┌──────────────────────────────────┐  
│ Consumo contesto: \~27%          │  
│ Funzionalità: gestione completa │  
│ dei progetti e task              │  
│ Numero di "skill interne": molte│  
│ Descrizioni: dettagliate        │  
│ IMPATTO: devastante             │  
└──────────────────────────────────┘

DIFFERENZA: 270 volte più pesante\!

Un MCP leggero come Chrome Dev Tool occupa lo 0,1% del contesto. Un MCP pesante come ClickUp occupa il 27%. Questo significa che ClickUp è 270 volte più pesante di Chrome Dev Tool in termini di impatto sul contesto.

#### **MCP Built-in vs MCP di Terze Parti**

La guida menziona che Claude Code ha già degli MCP built-in (integrati):

text

TIPOLOGIE DI MCP PER ORIGINE  
═════════════════════════════

1\. BUILT-IN (integrati in Claude Code):  
   └── Già presenti, non richiedono installazione  
   └── Fanno parte del system prompt  
   └── Consumo incluso nel 10% base del system prompt

2\. DI TERZE PARTI (installati dall'utente):  
   └── Richiedono installazione manuale  
   └── Aggiungono consumo di contesto AGGIUNTIVO  
   └── Qualità e sicurezza variabili  
   └── Possono contenere malware → ATTENZIONE

3\. CUSTOM (creati dall'utente):  
   └── Configurati nel file .mcp.json del progetto  
   └── Completamente sotto il vostro controllo

   └── Consumo dipende dalla complessità

#### **MCP "On-Demand" vs MCP "Always-On"**

Un concetto importante che emerge dalla guida è la distinzione tra MCP che vengono caricati sempre e MCP che vengono chiamati solo quando necessario:

*"Non tutti gli MCP sono i cosiddetti MCP di third, che vengono chiamati solamente a chiamata o a bisogno."*

Questo è un punto tecnico cruciale:

| Tipo | Comportamento | Impatto Contesto |
| ----- | ----- | ----- |
| Always-On | Le descrizioni di tutte le funzionalità sono caricate SEMPRE nel contesto | PERMANENTE — occupa contesto anche quando non lo usate |
| On-Demand | Le descrizioni vengono caricate solo quando l'MCP viene effettivamente chiamato | TEMPORANEO — occupa contesto solo durante l'uso |

Il problema principale è che la maggior parte degli MCP di terze parti sono Always-On: le loro descrizioni vengono caricate nel contesto all'avvio della sessione e ci restano per tutta la durata, consumando spazio anche quando non state usando quel servizio.

#### **Implicazione Pratica**

Questa distinzione ha un'implicazione enorme per la strategia di utilizzo:

* Se installate 3 MCP pesanti (tutti Always-On), potreste trovarvi con il 60-80% del contesto occupato prima ancora di scrivere il primo messaggio  
* È come salire in macchina con il bagagliaio pieno di attrezzi che non userete mai durante quel viaggio: occupano spazio e rendono la macchina più lenta

---

### **31.3 — Dove Trovare gli MCP**

#### **Definizione del Concetto**

Gli MCP sono distribuiti attraverso vari canali: repository GitHub, marketplace dedicati e documentazione ufficiale dei servizi che li offrono.

#### **Il Marketplace Principale**

La guida indica Awesome MCP Servers come risorsa principale:

*"MCP Server find — troveremo Awesome MCP Servers. Questa è un'ottima piattaforma."*

Questo repository contiene un elenco curato di MCP organizzati per categoria e verificati dalla community.

#### **Come Navigare e Scegliere**

Quando cercate un MCP, valutate:

text

CHECKLIST DI VALUTAZIONE MCP  
════════════════════════════

□ FUNZIONALITÀ: Fa quello che mi serve?  
  → Leggete la lista delle funzionalità esposte

□ PESO: Quanto contesto consuma?  
  → Se possibile, verificate prima di installare  
  → Installate, fate /context, verificate il consumo

□ SICUREZZA: È sviluppato da una fonte affidabile?  
  → Preferite MCP ufficiali (sviluppati dal servizio stesso)  
  → Es: MCP di ClickUp sviluppato da ClickUp \= più sicuro  
  → MCP di ClickUp sviluppato da "random\_user\_123" \= rischio

□ MANUTENZIONE: È aggiornato regolarmente?  
  → Controllate la data dell'ultimo commit su GitHub  
  → MCP non aggiornati possono avere bug o incompatibilità

□ NECESSITÀ: Mi serve DAVVERO come MCP?  
  → Posso ottenere lo stesso risultato con una skill?  
  → Lo userò abbastanza spesso da giustificare 

    il consumo permanente di contesto?

---

# **CAPITOLO 32**

## **Installare e Gestire gli MCP**

---

### **32.1 — Il Formato JSON di Configurazione**

#### **Definizione del Concetto**

Ogni MCP ha un file di configurazione in formato JSON che contiene le informazioni necessarie per il collegamento. Questo JSON definisce come Claude Code deve comunicare con il servizio esterno.

#### **Spiegazione Approfondita**

La guida spiega il formato JSON:

*"Questo non è altro che un formato JSON che io ora ho copiato. Il formato JSON lo vediamo perché è contenuto in parentesi graffe, ha la prima parte che si chiamano key (chiavi), la seconda parte che si chiamano value (valori), e sono divisi da questi due punti."*

Un file di configurazione MCP ha tipicamente questa struttura:

JSON

{  
  "mcpServers": {  
    "nome-del-servizio": {  
      "command": "npx",  
      "args": \[  
        "-y",  
        "@nome-pacchetto/mcp-server"  
      \],  
      "env": {  
        "API\_KEY": "la-vostra-chiave-api",  
        "WORKSPACE\_ID": "il-vostro-workspace"  
      }  
    }  
  }

}

Analisi della struttura:

| Elemento | Significato |
| ----- | ----- |
| mcpServers | Contenitore di tutti gli MCP configurati |
| nome-del-servizio | Identificativo dell'MCP (es: "clickup", "chrome-devtools") |
| command | Il comando per avviare il server MCP |
| args | Gli argomenti passati al comando |
| env | Le variabili d'ambiente (API key, credenziali, etc.) |

#### **Dove Va il File di Configurazione**

Il file di configurazione MCP si chiama .mcp.json e può essere posizionato a diversi livelli:

text

POSIZIONAMENTO DEL FILE .mcp.json  
═════════════════════════════════

LIVELLO LOCAL (dentro il progetto):  
progetto/  
└── .mcp.json          ← MCP disponibili solo in questo progetto

LIVELLO GLOBAL (nel computer dell'utente):  
\~/.claude/

└── .mcp.json          ← MCP disponibili in TUTTI i progetti

La scelta del posizionamento segue la stessa logica delle regole e dei sub-agenti:

* Local: quando l'MCP serve solo per un progetto specifico  
* Global: quando l'MCP è utile in tutti i progetti (come Chrome Dev Tool)

---

### **32.2 — Procedura di Installazione**

#### **Definizione del Concetto**

L'installazione di un MCP può avvenire in diversi modi, dal più semplice (prompt a Claude) al più manuale (editing diretto del file JSON).

#### **Metodo 1 — Installazione Tramite Prompt (Raccomandato)**

Il metodo più semplice, mostrato nella guida:

text

"Per favore installa il \[nome\] MCP da questo link: 

\[link alla pagina del MCP o al JSON di configurazione\]"

Claude:

1. Legge il link o il JSON fornito  
2. Identifica il tipo di MCP  
3. Scarica e configura automaticamente  
4. Aggiorna il file .mcp.json  
5. Conferma l'installazione

Esempio concreto dalla guida per Chrome Dev Tool:

text

"Per favore installa Dev Tool MCP"

Claude cerca la documentazione, trova il JSON di configurazione e lo installa automaticamente.

#### **Metodo 2 — Installazione Tramite Dev Tool MCP**

Un metodo particolarmente elegante mostrato nella guida: usare il Chrome Dev Tool MCP (già installato) per navigare alla pagina di un altro MCP e installarlo:

text

"Per favore, usando il Dev Tool MCP, guarda questo   
link \[pagina del MCP su GitHub\] e collegami l'MCP 

di ClickUp a questo progetto."

In questo caso, Claude:

1. Usa il Dev Tool MCP per navigare alla pagina GitHub del MCP  
2. Legge le istruzioni di installazione dalla pagina  
3. Identifica il JSON di configurazione  
4. Installa l'MCP seguendo le istruzioni trovate

#### **Metodo 3 — Installazione con Comando Specifico**

Alcuni MCP hanno comandi di installazione specifici. Dalla guida, l'esempio di ClickUp:

*"Cloud Code, use the following command. Once you open Claude Code session, run \[comando\] to go through the authentication flow."*

In questo caso:

1. Copiate il comando dalla documentazione del MCP  
2. Incollatelo nel terminal di Claude Code  
3. Seguite il processo di autenticazione (se richiesto)  
4. Riavviate la sessione di Claude Code  
5. Verificate con /mcp che l'MCP sia attivo

#### **Il Processo di Autenticazione**

Molti MCP richiedono un processo di autenticazione per accedere al servizio esterno. La guida mostra questo processo con l'esempio di ClickUp:

PROCESSO DI AUTENTICAZIONE MCP  
══════════════════════════════

Passo 1: Installazione dell'MCP  
    → Claude configura il server MCP locale

Passo 2: Riavvio della sessione  
    → "Chiudi e riavvia Claude Code"

Passo 3: Verifica connessione  
    → Eseguire /mcp per verificare lo stato

Passo 4: Autenticazione  
    → "ClickUp ha bisogno di un'autenticazione"  
    → "Enter to confirm"  
    → Si apre il browser  
    → Login nel servizio (es: ClickUp)  
    → Autorizzazione dell'accesso

Passo 5: Conferma  
    → Il terminale conferma la connessione

    → L'MCP è ora operativo

### **32.3 — Verificare e Gestire gli MCP Installati**

#### **Definizione del Concetto**

Dopo l'installazione, è fondamentale verificare che l'MCP funzioni correttamente e monitorare il suo impatto sul contesto.

#### **Il Comando /mcp**

Per verificare quali MCP sono installati e il loro stato:

/mcp

Questo comando mostra:

* L'elenco degli MCP installati  
* Lo stato di ciascuno (connesso, disconnesso, errore)  
* Eventuali problemi di autenticazione

#### **Verificare l'Impatto sul Contesto**

Immediatamente dopo l'installazione di un nuovo MCP, eseguite:

/context

E confrontate i numeri con quelli precedenti all'installazione. Se l'impatto è eccessivo (più del 5-10% per un singolo MCP), valutate se ne vale la pena.

#### **Come Rimuovere un MCP**

La rimozione è altrettanto semplice dell'installazione:

"Per favore rimuovi l'MCP \[nome\]"

L'autore della guida lo dimostra con l'esempio di Canva:

*"Per favore puoi rimuovere il mio Cloud AI Canva MCP? Non mi serve."*

Claude rimuove la configurazione dal file .mcp.json e libera il contesto corrispondente.

#### **La Gestione come Routine**

L'installazione e la rimozione degli MCP dovrebbe essere una routine consapevole, non un'azione casuale:

ROUTINE DI GESTIONE MCP  
═══════════════════════

PRIMA DI INIZIARE UN PROGETTO:  
□ Verificare quali MCP sono installati (/mcp)  
□ Verificare il loro impatto sul contesto (/context)  
□ Rimuovere MCP non necessari per questo progetto  
□ Installare MCP specifici necessari per questo progetto

DURANTE IL LAVORO:  
□ Monitorare il contesto regolarmente  
□ Se un MCP non viene più usato → rimuoverlo

ALLA FINE DEL PROGETTO:  
□ Rimuovere MCP project-specific

□ Mantenere solo MCP globali (es: Chrome Dev Tool)

# **CAPITOLO 33**

## **MCP vs Skill — Impatto sul Contesto**

### **33.1 — L'Esperimento Cruciale della Guida**

#### **Definizione del Concetto**

La guida originale contiene quello che è forse l'esperimento più illuminante dell'intero corso: il confronto diretto tra l'impatto sul contesto degli MCP e delle skill. Questo confronto rivela una verità fondamentale che cambia radicalmente il modo in cui si dovrebbero usare gli MCP.

#### **Spiegazione Approfondita — I Numeri**

L'autore esegue un test sistematico. Prima verifica il contesto con solo Chrome Dev Tool installato:

CONFIGURAZIONE LEGGERA (solo Chrome Dev Tool):  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
System Prompt:        \~10%  
System Tools:          \~0,7%  
MCP Tools:             \~0,1%  (Chrome Dev Tool)  
Memory Files:          \~4-5%  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
TOTALE PRE-MESSAGGIO:  \~15-16%

SPAZIO LIBERO:         \~84-85%

Poi installa ClickUp e Canva e verifica di nuovo:

CONFIGURAZIONE PESANTE (Chrome Dev Tool \+ ClickUp \+ Canva):  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
System Prompt:        \~10%  
System Tools:          \~0,7%  
MCP Tools:             \~28%   (Chrome \+ ClickUp \+ Canva)  
Memory Files:          \~4-5%  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
TOTALE PRE-MESSAGGIO:  \~43%

SPAZIO LIBERO:         \~57%

E poi confronta con il consumo delle skill:

SKILL DEL PROGETTO:  
━━━━━━━━━━━━━━━━━━  
Tutte le skill combinate:  \~0,3%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### **Il Confronto Visivo**

CONFRONTO IMPATTO SUL CONTESTO  
══════════════════════════════

MCP ClickUp:     ████████████████████████████████████  27%  
MCP Canva:       █████████  \~8% (stimato)  
MCP Chrome Dev:  ▏  0,1%  
TUTTE le Skill:  ▏  0,3%

Le skill sono circa 90x più efficienti del MCP pesante  
per fornire funzionalità a Claude.

#### **La Conclusione dell'Autore**

*"Quando e come usate gli MCP? Beh sostanzialmente gli MCP sono una chiavetta universale che ti permette di avere tutte le varie skill e che ti permette di chiamare tutti i servizi. Vi consiglio di utilizzarle soprattutto per fare quello che noi definiremo un MVP, quindi per assicurarci che la cosa che vogliamo fare funzioni. Poi quello che faremo è chiedere a Claude: 'Ora che sai cercarmi le cose dentro al workspace, creami una skill adatta a quello che vuoi fare.' E dopo una volta fatta la skill, toglieremo l'MCP."*

Questa è la strategia ottimale. Ripetiamola perché è fondamentale.

à

**33.2 — La Strategia MCP → Skill Conversion**

#### **Definizione del Concetto**

La MCP → Skill Conversion è il processo strategico di usare un MCP come strumento di prototipazione rapida per poi convertire le funzionalità necessarie in skill native, rimuovendo l'MCP e liberando il contesto.

#### **Il Processo in Dettaglio**

PROCESSO MCP → SKILL CONVERSION  
════════════════════════════════

FASE 1: INSTALLAZIONE MCP (temporanea)  
────────────────────────────────────────  
□ Installate l'MCP del servizio che vi interessa  
□ Verificate l'impatto sul contesto (/context)  
□ Annotate mentalmente: "Questo è temporaneo"

FASE 2: PROTOTIPAZIONE CON MCP  
────────────────────────────────  
□ Usate l'MCP per fare quello che vi serve  
□ Testate tutte le funzionalità necessarie  
□ Verificate che il collegamento funzioni  
□ Identificate QUALI funzionalità vi servono davvero  
  (probabilmente solo 2-3 su 20+ disponibili)

FASE 3: CONVERSIONE IN SKILL  
─────────────────────────────  
□ Chiedete a Claude:  
  "Ora che sai come funziona \[servizio\],   
   creami una skill che faccia \[operazione specifica\].  
   La skill deve usare l'API di \[servizio\] direttamente  
   senza bisogno dell'MCP."  
□ Claude crea la skill con gli script necessari  
□ La skill fa chiamate API dirette al servizio

FASE 4: RIMOZIONE MCP  
──────────────────────  
□ Testate che la skill funzioni indipendentemente  
□ Rimuovete l'MCP: "Rimuovi l'MCP \[nome\]"  
□ Verificate con /context che il contesto sia libero  
□ Verificate che la skill continui a funzionare

RISULTATO:  
──────────  
PRIMA:  MCP ClickUp \= 27% del contesto per TUTTE le funzionalità  
DOPO:   Skill custom \= 0,1% del contesto per LE funzionalità che servono  
RISPARMIO: 26,9% di contesto → enorme miglioramento

#### **Perché Funziona**

La ragione per cui questa strategia è così efficace è che un MCP carica le descrizioni di TUTTE le funzionalità del servizio nel contesto, anche quelle che non userete mai. Se ClickUp ha 50 funzionalità e voi ne usate solo 3, state pagando il "peso" di 47 funzionalità inutili.

Con una skill personalizzata, caricate nel contesto solo le istruzioni per le 3 funzionalità che vi servono. Il risparmio è proporzionale al rapporto tra funzionalità totali e funzionalità necessarie.

ESEMPIO NUMERICO  
════════════════

MCP ClickUp: 50 funzionalità × \~5.400 token ciascuna \= 270.000 token  
Voi usate: 3 funzionalità

CON MCP:     270.000 token nel contesto (27% su 1M)  
CON SKILL:   \~3.000 token nel contesto (0,3% su 1M)

EFFICIENZA: 90x migliore con la skill

#### **Quando NON Convertire (Eccezioni)**

Ci sono situazioni in cui ha senso mantenere l'MCP invece di convertire in skill:

| Situazione | Motivo per Mantenere l'MCP |
| ----- | ----- |
| Usate molte funzionalità del servizio (\>10) | Creare 10+ skill separate sarebbe più dispendioso |
| Il servizio cambia API frequentemente | Le skill diventerebbero obsolete rapidamente, l'MCP viene aggiornato dal fornitore |
| Siete in fase esplorativa | Non sapete ancora quali funzionalità vi servono |
| L'MCP è leggero (\<1% contesto) | Il costo di mantenimento è trascurabile |

### **33.3 — Il Collegamento con il Lost in the Middle**

#### **Definizione del Concetto**

L'impatto degli MCP sul contesto non è solo quantitativo (occupano spazio) ma anche qualitativo: gli MCP pesanti spostano le vostre informazioni utili nella zona "Lost in the Middle", degradando la qualità delle risposte.

#### **Spiegazione Approfondita**

La guida collega esplicitamente l'impatto degli MCP al fenomeno del Lost in the Middle:

*"Vi ricordate il Lost in the Middle di cui abbiamo discusso all'inizio? Vuol dire che noi siamo arrivati già qua. Abbiamo fatto una cosa orribile per caricare queste tipologie di MCP."*

Ecco cosa succede visivamente:

IMPATTO MCP SUL LOST IN THE MIDDLE  
═══════════════════════════════════

SENZA MCP PESANTI:  
┌────────────────────────────────────────────┐  
│ System Prompt \[INIZIO \- alta attenzione\]   │ 10%  
│ CLAUDE.md     \[INIZIO \- alta attenzione\]   │ 5%  
│ ───────────────────────────────────────    │  
│ Messaggi      \[MEZZO → FINE\]               │ 20%  
│ ───────────────────────────────────────    │  
│ Ultimo prompt \[FINE \- alta attenzione\]     │ 1%  
│ SPAZIO LIBERO                              │ 64%  
└────────────────────────────────────────────┘  
→ Le vostre informazioni sono nelle zone di ALTA attenzione  
→ Risultato: risposte eccellenti

CON MCP PESANTI (27% occupato):  
┌────────────────────────────────────────────┐  
│ System Prompt \[INIZIO \- alta attenzione\]   │ 10%  
│ MCP PESANTE   \[INIZIO→MEZZO\]              │ 27%  
│ ───────────────────────────────────────    │  
│ CLAUDE.md     \[MEZZO \- BASSA attenzione\]   │ 5%  ← PROBLEMA\!  
│ Messaggi      \[MEZZO \- BASSA attenzione\]   │ 20% ← PROBLEMA\!  
│ ───────────────────────────────────────    │  
│ Ultimo prompt \[FINE \- alta attenzione\]     │ 1%  
│ SPAZIO LIBERO                              │ 37%  
└────────────────────────────────────────────┘  
→ Il CLAUDE.md e i messaggi sono nella zona di BASSA attenzione  
→ Risultato: Claude "dimentica" le vostre regole e istruzioni

→ Risposte degradate significativamente

L'MCP pesante non solo occupa spazio, ma spinge le vostre informazioni importanti (CLAUDE.md, regole, messaggi) nella zona cieca del Lost in the Middle. Questo è il doppio danno degli MCP pesanti.

#### **La Regola Pratica**

*"Quello che noi vogliamo fare è andare a costruire qualcosa che ci permetta di essere efficienti. Ci permetta di agire nelle fasi qui \[inizio e fine\] con le cose più importanti. Non vogliamo mai che il nostro prompt iniziale sia nell'intervallo in cui sostanzialmente l'LLM perde qualsiasi cosa."*

Tradotto in regola pratica:

Se un MCP occupa più del 5% del contesto, valutate seriamente la conversione in skill.

Sopra il 5%, l'MCP inizia a spingere le vostre informazioni nella zona Lost in the Middle. Sopra il 15%, l'impatto è significativo. Sopra il 25%, è devastante.

# **CAPITOLO 34**

## **Chrome Dev Tool MCP**

### **34.1 — L'Unico MCP Raccomandato**

#### **Definizione del Concetto**

Il Chrome Dev Tool MCP è l'unica integrazione MCP che l'autore della guida raccomanda esplicitamente per uso pratico e aziendale. È un MCP leggero che permette a Claude di navigare il web, fare screenshot, leggere contenuti di pagine e interagire con i browser.

#### **Spiegazione Approfondita**

*"La Chrome Dev Tool Integration è l'unica integrazione di Claude Code che io raccomando a livello pratico e aziendale. Non ho trovato nessun'altra che abbia valore per quanto mi riguarda."*

Questa affermazione è forte e deliberata. L'autore, che implementa Claude Code in aziende che generano fino a 70 milioni di euro di fatturato, dice che tra tutti gli MCP disponibili, solo uno vale la pena di mantenere installato permanentemente.

Le ragioni sono:

1. Peso trascurabile: solo 0,1% del contesto  
2. Utilità universale: la navigazione web è utile in praticamente ogni progetto  
3. Complementarità con le skill: permette di navigare a siti e fare screenshot che le skill da sole non potrebbero fare  
4. Nessun equivalente in skill: la navigazione web interattiva è difficile da replicare come skill  
5. Strumento di verifica: essenziale per il ciclo Task-Do-Verify nella costruzione di siti web

### **34.2 — Funzionalità del Chrome Dev Tool MCP**

#### **Definizione del Concetto**

Il Chrome Dev Tool MCP fornisce a Claude la capacità di controllare un browser Chrome come se fosse un utente umano. Può navigare pagine, leggere contenuti, fare screenshot, cliccare elementi e interagire con interfacce web.

#### **Le Capacità Specifiche**

FUNZIONALITÀ DEL CHROME DEV TOOL MCP  
═════════════════════════════════════

1\. NAVIGAZIONE WEB  
   └── Aprire URL specifici  
   └── Navigare tra pagine  
   └── Seguire link  
   └── Es: "Vai alla documentazione ufficiale di Anthropic"

2\. SCREENSHOT  
   └── Catturare screenshot di pagine web  
   └── Screenshot full-page  
   └── Screenshot di elementi specifici  
   └── Es: "Fai uno screenshot del sito e confrontalo   
            con l'immagine di riferimento"

3\. LETTURA CONTENUTI  
   └── Leggere il testo di una pagina web  
   └── Estrarre informazioni strutturate  
   └── Fare summary di pagine  
   └── Es: "Leggi questa pagina e fammene un riassunto"

4\. INTERAZIONE  
   └── Cliccare bottoni  
   └── Compilare form  
   └── Scrollare pagine  
   └── Es: "Vai su Google e cerca \[query\]"

5\. SCRAPING  
   └── Estrarre dati da pagine web  
   └── Raccogliere informazioni strutturate  
   └── Es: "Raccogli tutti i prezzi da questa pagina"

#### **Applicazioni Pratiche dalla Guida**

1\. Verifica di siti web costruiti:  
Il Chrome Dev Tool MCP è fondamentale per il ciclo di verifica screenshot nella costruzione di siti. Claude può:

* Fare screenshot del sito in costruzione  
* Confrontarlo con l'immagine di riferimento  
* Identificare le differenze  
* Correggerle  
* Ripetere il ciclo

2\. Ricerca senza API:

*"Quando non ci sono API, potrete usare questo tool qui e vi permette di girare nel web."*

Questo è un caso d'uso cruciale: molti servizi non offrono API pubbliche. Con il Chrome Dev Tool MCP, Claude può comunque interagire con questi servizi navigando la loro interfaccia web come farebbe un umano.

3\. Pubblicazione su piattaforme:

Nella skill "publish" dell'autore, Instagram viene gestito tramite Chrome Dev Tool MCP perché non è pratico usare l'API di Instagram:

*"YouTube: Python API. Instagram: tramite Chrome Dev Tool MCP."*

Questo mostra come l'MCP può essere integrato nelle skill come strumento complementare.

4\. Installazione di altri MCP:

Come visto nel Capitolo 32, il Chrome Dev Tool MCP può essere usato per navigare alle pagine GitHub di altri MCP, leggere le istruzioni di installazione e aiutare a installarli.

### **34.3 — Come Installare Chrome Dev Tool MCP**

#### **Procedura di Installazione**

La guida mostra il processo:

Passo 1: Trovare la pagina dell'MCP  
    → Cercate "Chrome Dev Tool MCP" su Google  
    → Trovate la repository GitHub ufficiale

Passo 2: Copiare il JSON di configurazione  
    → Sulla pagina GitHub, trovate il JSON  
    → Copiate il blocco di configurazione

Passo 3: Installare tramite Claude Code  
    → "Per favore installa Dev Tool MCP"  
    → Oppure: incollate il JSON e chiedete di installarlo

Passo 4: Autenticazione  
    → Al primo uso, Claude vi chiederà di autenticare  
    → Si aprirà Chrome  
    → Confermate l'accesso

Passo 5: Verifica  
    → "Per favore accedi a google.com usando il Dev Tool MCP"

    → Se funziona, l'installazione è completa

#### **Consumo di Token**

*"Consumando una quantità anche ragionevole di token perché non è eccessivamente costoso."*

Il Chrome Dev Tool MCP è progettato per essere efficiente:

* Le navigazioni semplici consumano pochi token  
* Gli screenshot sono compressi automaticamente  
* La lettura di pagine è ottimizzata per estrarre solo il testo rilevante  
* L'impatto permanente sul contesto è solo dello 0,1%

Questo lo rende ideale per un uso frequente senza preoccupazioni di costo.

### **34.4 — Il Pattern Strategico Completo per gli MCP**

#### **Riepilogo della Strategia Ottimale**

Combinando tutti i concetti appresi in questa Parte, ecco la strategia completa per la gestione degli MCP:

STRATEGIA COMPLETA DI GESTIONE MCP  
═══════════════════════════════════

LIVELLO BASE (per tutti):  
─────────────────────────  
✅ Installate Chrome Dev Tool MCP → tenetelo SEMPRE  
✅ Non installate nient'altro a meno che non serva  
✅ Consumo contesto base: \~0,1%

QUANDO SERVE UN SERVIZIO ESTERNO:  
─────────────────────────────────  
1\. Installate l'MCP del servizio  
2\. Verificate il consumo con /context  
3\. Usate l'MCP per capire COME funziona il servizio  
4\. Identificate le 2-3 funzionalità che vi servono  
5\. Chiedete a Claude di creare skill per quelle funzionalità  
6\. Testate le skill indipendentemente  
7\. Rimuovete l'MCP  
8\. Verificate con /context che il contesto sia libero

ECCEZIONI (mantenete l'MCP):  
────────────────────────────  
• MCP con consumo \< 1% del contesto  
• MCP che usate quotidianamente con molte funzionalità  
• MCP in fase di esplorazione attiva

MAI:  
────  
• Non installate più di 2-3 MCP contemporaneamente  
• Non lasciate MCP installati che non state usando  
• Non ignorate l'impatto sul contesto

• Non assumete che "più MCP \= migliore"

## **Riepilogo della Parte 9**

In questa Parte avete appreso:

1. Cos'è un MCP: un protocollo che collega servizi esterni a Claude Code, come una "chiavetta USB universale" che eredita tutte le funzionalità del servizio  
2. Le tipologie di MCP: leggeri vs pesanti, built-in vs terze parti, always-on vs on-demand  
3. Il formato JSON di configurazione: struttura con key-value che definisce come Claude comunica con il servizio  
4. Come installare un MCP: tramite prompt, tramite Dev Tool MCP o tramite comando specifico  
5. L'impatto devastante degli MCP pesanti sul contesto: ClickUp occupa il 27% del contesto, 270 volte più del Chrome Dev Tool  
6. La strategia MCP → Skill Conversion: usare l'MCP per prototipare, poi convertire in skill e rimuovere l'MCP  
7. Il collegamento con il Lost in the Middle: gli MCP pesanti spingono le vostre informazioni nella zona cieca del contesto  
8. Il Chrome Dev Tool MCP: l'unico MCP raccomandato, con 0,1% di consumo e funzionalità universali  
9. La regola del 5%: se un MCP occupa più del 5% del contesto, valutate la conversione in skill  
10. La strategia completa: Chrome Dev Tool sempre, tutto il resto temporaneo e convertito in skill

