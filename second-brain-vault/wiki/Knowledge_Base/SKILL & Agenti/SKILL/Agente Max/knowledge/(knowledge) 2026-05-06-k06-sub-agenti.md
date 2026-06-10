# K06-sub-agenti
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Agente Max > knowledge]]

## Content

# MODULO KNOWLEDGE BASE

**K06-sub-agenti.md** — Capitoli 24-26 | Sub-agenti (Researcher/Reviewer/QA), Agent Teams, costi e ROI

## Riferimenti Correlati
- K05-context.md (ogni sub-agente ha contesto indipendente 200K)
- K07-skill-system.md (alternativa ai team costosi)

---

# **PARTE 7 — SUB-AGENTI E AGENT TEAMS**

*"Il motivo per cui utilizziamo questi agenti è perché possiamo tenere la task principale nel main agent ma poi andiamo ad utilizzare questi sub-agenti per riuscire ad efficientare l'utilizzo del contesto all'interno di Claude Code."*  
*— Dalla guida originale*

## **Introduzione alla Parte 7**

Se la Parte 6 vi ha insegnato a comprendere e gestire il contesto come risorsa finita, questa Parte vi insegna come moltiplicare la vostra capacità operativa senza saturare quella risorsa. I sub-agenti e gli Agent Teams rappresentano l'evoluzione dall'uso individuale di Claude Code all'uso orchestrato: passate da essere un singolo operatore che lavora con un singolo assistente a diventare un direttore d'orchestra che coordina un intero team di intelligenze specializzate.

Questa Parte è composta da tre capitoli:

| Capitolo | Titolo | Focus Principale |
| ----- | ----- | ----- |
| 24 | I Sub-agenti — Researcher, Reviewer, QA | Cosa sono, come crearli, perché usare questi tre |
| 25 | Agent Teams — Collaborazione Multi-Agente | Come funzionano i team, la comunicazione bidirezionale |
| 26 | Costi, ROI e Utilizzo Strategico | Quando conviene usarli e quando no |

# **CAPITOLO 24**

## **I Sub-agenti — Researcher, Reviewer, QA**

### **24.1 — Cosa Sono i Sub-agenti**

#### **Definizione del Concetto**

Un sub-agente (o sottoagente) è un'istanza separata di Claude che viene invocata dall'agente principale per svolgere una task specifica in modo isolato. Il sub-agente opera nel proprio contesto indipendente, esegue il compito assegnatogli e restituisce solo il risultato finale all'agente principale. È come delegare un compito a un collaboratore che lavora in una stanza separata e vi porta solo il prodotto finito.

#### **Spiegazione Approfondita**

Per comprendere i sub-agenti, è fondamentale capire la differenza tra lavorare tutto in un unico contesto e delegare a contesti separati.

Scenario SENZA sub-agenti (tutto nel contesto principale):

Immaginate di chiedere a Claude di fare una ricerca sulle best practice per costruire un sito internet. Claude naviga il web, legge documentazione, analizza articoli — e tutto questo materiale (potenzialmente 100.000 token) viene caricato nel vostro contesto principale. Risultato: il contesto si riempie a metà solo per una ricerca, e vi resta poco spazio per il lavoro vero e proprio.

CONTESTO PRINCIPALE (senza sub-agenti)  
╔══════════════════════════════════════════════════════╗  
║ System Prompt          \[10%\]                         ║  
║ CLAUDE.md \+ Rules      \[5%\]                          ║  
║ Risultati ricerca      \[50%\] ← PROBLEMA\!             ║  
║ Conversazione          \[15%\]                         ║  
║ Spazio libero          \[20%\] ← troppo poco           ║

╚══════════════════════════════════════════════════════╝

Scenario CON sub-agenti (contesti separati):

La stessa ricerca viene delegata a un sub-agente Researcher. Questo sub-agente opera nel proprio contesto da 200.000 token, fa tutta la ricerca, processa 100.000 token di materiale e produce un riassunto di 2.000 token. Solo questi 2.000 token vengono inviati al contesto principale.

CONTESTO DEL SUB-AGENTE (Researcher)  
╔══════════════════════════════════════════════════════╗  
║ System Prompt          \[10%\]                         ║  
║ Istruzioni del sub-agente \[2%\]                       ║  
║ Risultati ricerca      \[50%\]                         ║  
║ Elaborazione interna   \[20%\]                         ║  
║ Produzione riassunto   \[5%\]                          ║  
║ \[Questo contesto viene DISTRUTTO dopo l'uso\]         ║  
╚══════════════════════════════════════════════════════╝  
                    │  
                    │ Solo il risultato (2K token)  
                    ▼  
CONTESTO PRINCIPALE  
╔══════════════════════════════════════════════════════╗  
║ System Prompt          \[10%\]                         ║  
║ CLAUDE.md \+ Rules      \[5%\]                          ║  
║ Risultato ricerca      \[1%\]  ← EFFICIENTE\!           ║  
║ Conversazione          \[15%\]                         ║  
║ Spazio libero          \[69%\] ← abbondante            ║

╚══════════════════════════════════════════════════════╝

La differenza è drammatica: da 50% di contesto occupato a 1%. Questo è il potere dei sub-agenti.

#### **Il Meccanismo Sottostante — Come Funziona la Comunicazione**

La guida originale mostra un concetto chiave: la comunicazione tra agente principale e sub-agente è visibile nell'interfaccia attraverso quello che viene chiamato "inline".

Ecco il flusso completo:

FLUSSO DI COMUNICAZIONE AGENTE-SUBAGENTE  
═════════════════════════════════════════

PASSO 1: L'utente fa una richiesta all'agente principale  
┌─────────────────────────────────────────────────────┐  
│ Utente: "Per favore chiama l'agente 'come si chiama │  
│         mamma' perché vorrei sapere il nome"        │  
└─────────────────────────┬───────────────────────────┘  
                          │  
                          ▼  
PASSO 2: L'agente principale "pensa" e decide di delegare  
┌─────────────────────────────────────────────────────┐  
│ Agente Principale: \[harmonizing... thinking...\]     │  
│ "Devo chiamare il sub-agente 'come si chiama mamma'"│  
└─────────────────────────┬───────────────────────────┘  
                          │  
                          ▼  
PASSO 3: Comunicazione INLINE (agente → sub-agente)  
┌─────────────────────────────────────────────────────┐  
│ INLINE: "L'utente chiede: come si chiama mamma?     │  
│         Per favore rispondi alla domanda."          │  
│                                                     │  
│ \[Questa comunicazione è interna, visibile           │  
│  nell'interfaccia ma gestita automaticamente\]       │  
└─────────────────────────┬───────────────────────────┘  
                          │  
                          ▼  
PASSO 4: Il sub-agente processa nel suo contesto  
┌─────────────────────────────────────────────────────┐  
│ Sub-agente "come si chiama mamma":                  │  
│ \[Legge le sue istruzioni: "rispondi Antonino"\]      │  
│ \[Elabora la risposta\]                               │  
│ \[Produce: "La mamma si chiama Antonino"\]            │  
└─────────────────────────┬───────────────────────────┘  
                          │  
                          ▼  
PASSO 5: Solo il risultato torna all'agente principale  
┌─────────────────────────────────────────────────────┐  
│ Agente Principale riceve: "La mamma si chiama       │  
│ Antonino"                                           │  
│ → Presenta il risultato all'utente                  │

└─────────────────────────────────────────────────────┘

Il punto cruciale è il Passo 5: l'utente non vede mai il contesto interno del sub-agente. Non vede i ragionamenti, non vede i file letti, non vede le iterazioni interne. Riceve solo il risultato. Questo è ciò che rende i sub-agenti così efficienti per il context management.

#### **Perché i Sub-agenti Sono Fondamentali**

I sub-agenti risolvono simultaneamente tre problemi:

1. Problema di contesto: delegare il lavoro pesante fuori dal contesto principale  
2. Problema di specializzazione: ogni sub-agente può avere istruzioni specifiche per un tipo di task  
3. Problema di parallelizzazione: più sub-agenti possono lavorare contemporaneamente su task diverse

#### **Errori Comuni**

| Errore | Spiegazione | Conseguenza |
| ----- | ----- | ----- |
| Non usare sub-agenti per ricerche | Tutto il materiale di ricerca finisce nel contesto principale | Contesto saturo dopo una sola ricerca |
| Creare sub-agenti troppo generici | Un sub-agente senza istruzioni specifiche non è meglio dell'agente principale | Risultati generici e poco utili |
| Non sapere che i sub-agenti esistono | Molti utenti lavorano sempre e solo nel contesto principale | Efficienza drasticamente ridotta |
| Usare sub-agenti per task che richiedono il contesto del progetto | Il sub-agente non ha accesso al contesto principale | Risultati decontestualizzati |

### **24.2 — Come Creare un Sub-agente**

#### **Definizione del Concetto**

Un sub-agente è, nella sua essenza, un file di testo in formato Markdown posizionato nella cartella .claude/agents/ del progetto. Questo file contiene le istruzioni che definiscono il comportamento, le competenze e i limiti del sub-agente.

#### **Spiegazione Approfondita — La Struttura del File**

Quando create un sub-agente, il file Markdown contiene diverse sezioni delimitate da separatori (righe tratteggiate \---). La guida originale mostra che un file sub-agente tipico include:

in Markdown

\---  
model: haiku  
max\_tokens: \[limite di token per le risposte\]  
\---

**\# Nome del Sub-agente**

**\#\# Descrizione**  
\[Cosa fa questo sub-agente\]

**\#\# Istruzioni**  
\[Come deve comportarsi\]

**\#\# Vincoli**  
\[Cosa NON deve fare\]

**\#\# Formato di Output**

\[Come deve presentare i risultati\]

Analisi della struttura:

La sezione tra i tratteggi (\---) è chiamata frontmatter e contiene metadati tecnici:

* model: specifica quale modello LLM utilizzare per questo sub-agente. La guida indica che Haiku è il modello più utilizzato per i sub-agenti al momento della registrazione. Haiku è un modello più leggero e veloce di Opus o Sonnet, perfetto per task specializzate che non richiedono il modello più potente.  
* max\_tokens: limita la quantità di token che il sub-agente può usare per le risposte.

Il corpo del file contiene le istruzioni in linguaggio naturale che definiscono il comportamento del sub-agente.

#### **Procedura Pratica per Creare un Sub-agente**

Metodo 1 — Creazione Manuale:

1. Navigate alla cartella .claude/agents/ nel vostro progetto  
2. Create un nuovo file con estensione .md (esempio: researcher.md)  
3. Scrivete le istruzioni seguendo la struttura mostrata sopra  
4. Salvate il file

Metodo 2 — Creazione Assistita da Claude (raccomandato):

Questo è il metodo utilizzato nella guida originale. Potete chiedere direttamente a Claude di creare il sub-agente per voi:

"Per favore guarda la documentazione ufficiale di Claude   
e creami un sub-agente \[nome\]. Deve fare \[descrizione\]. 

Popola il file con le best practice della documentazione ufficiale."

Claude andrà a consultare la documentazione ufficiale di Anthropic, capirà la struttura corretta dei sub-agenti e creerà il file con le best practice aggiornate.

Metodo 3 — Importazione da Template Globali:

Se avete già sub-agenti configurati nella vostra cartella globale (\~/.claude/agents/), potete chiedere a Claude di importarli nel progetto corrente:

text

"Per favore importa i tre sub-agenti che sono nella mia 

cartella globale .claude/agents/: il reviewer, il researcher e il QA."

#### **Dove Vivono i Sub-agenti**

I sub-agenti possono esistere a diversi livelli dell'architettura Claude Code:

LIVELLO LOCAL (dentro il progetto):  
progetto/  
└── .claude/  
    └── agents/  
        ├── researcher.md     ← Sub-agente di questo progetto  
        ├── reviewer.md       ← Sub-agente di questo progetto  
        └── qa.md             ← Sub-agente di questo progetto

LIVELLO GLOBAL (nel computer dell'utente):  
\~/.claude/  
└── agents/  
    ├── researcher.md     ← Disponibile per TUTTI i progetti  
    ├── reviewer.md       ← Disponibile per TUTTI i progetti

    └── qa.md             ← Disponibile per TUTTI i progetti

Il vantaggio di avere sub-agenti a livello globale è che non dovete ricrearli per ogni nuovo progetto. Potete importarli o Claude li troverà automaticamente.

#### **Come Chiamare un Sub-agente**

Una volta creato, chiamare un sub-agente è semplice come scrivere un prompt:

"Per favore chiama il sub-agente reviewer e assicurati 

di rivedere tutto il codice."

Oppure, in modo più diretto:

"Chiama il researcher sub-agent per fare una ricerca 

sulle best practice per \[argomento\]."

Claude riconosce il nome del sub-agente, lo attiva nel suo contesto separato, gli invia la task e raccoglie il risultato.

#### **Perché Usare Haiku per i Sub-agenti**

La scelta di Haiku come modello per i sub-agenti è strategica:

| Caratteristica | Haiku | Opus/Sonnet |
| ----- | ----- | ----- |
| Velocità | Molto veloce | Più lento |
| Costo per token | Molto basso | Più alto |
| Capacità cognitiva | Sufficiente per task specializzate | Superiore per task complesse |
| Ideale per | Ricerche, review, test | Ragionamento complesso, architettura |

Poiché i sub-agenti eseguono task specializzate e ben definite (non ragionamento generale complesso), non hanno bisogno del modello più potente. Haiku è sufficiente e molto più economico, il che è particolarmente importante considerando che i sub-agenti possono consumare molti token nel loro contesto interno.

#### **Errori Comuni nella Creazione**

1. Creare sub-agenti senza consultare la documentazione: la struttura dei sub-agenti evolve. Chiedete sempre a Claude di verificare le best practice aggiornate dalla documentazione ufficiale.  
2. Non specificare il modello nel frontmatter: se non specificate il modello, il sub-agente potrebbe usare lo stesso modello dell'agente principale (Opus/Sonnet), consumando inutilmente risorse più costose.  
3. Scrivere istruzioni troppo lunghe nel sub-agente: ricordate che anche le istruzioni del sub-agente occupano contesto (nel contesto del sub-agente). Istruzioni concise e precise producono risultati migliori.  
4. Non definire chiaramente il formato di output: se non dite al sub-agente COME presentare i risultati, potrebbe produrre output troppo lunghi che poi occuperanno troppo spazio nel contesto principale.

### **24.3 — Il Researcher Sub-agent**

#### **Definizione del Concetto**

Il Researcher è un sub-agente specializzato nella ricerca di informazioni, best practice, documentazione e dati online. Il suo scopo è raccogliere grandi quantità di informazioni, processarle e restituire all'agente principale solo un riassunto sintetico e azionabile.

#### **Spiegazione Approfondita**

Il Researcher è il primo dei tre sub-agenti raccomandati dall'autore della guida, e il suo funzionamento illustra perfettamente il vantaggio dei sub-agenti per il context management.

Il Problema che il Researcher Risolve:

Quando chiedete a Claude di fare una ricerca (ad esempio: "Cerca le best practice per costruire un sito internet con Next.js"), il processo di ricerca genera una quantità enorme di dati:

* Pagine web visitate e scrappate  
* Documentazione tecnica letta  
* Articoli analizzati  
* Codice di esempio trovato  
* Discussioni su forum consultate

Tutto questo materiale può facilmente raggiungere i 100.000 token. Se questa ricerca avviene nel contesto principale, avete bruciato metà del vostro contesto solo per la fase di ricerca, prima ancora di iniziare a costruire qualcosa.

Come il Researcher Risolve il Problema:

FLUSSO DEL RESEARCHER SUB-AGENT  
════════════════════════════════

AGENTE PRINCIPALE                    RESEARCHER SUB-AGENT  
      │                                      │  
      │  "Cerca le best practice             │  
      │   per costruire un sito              │  
      │   con Next.js"                       │  
      │ ─────────────────────────────────►   │  
      │                                      │  
      │                              ┌───────┴───────┐  
      │                              │ Naviga il web  │  
      │                              │ Legge docs     │  
      │                              │ Analizza codice│  
      │                              │ Processa       │  
      │                              │ 100K token     │  
      │                              │ di materiale   │  
      │                              └───────┬───────┘  
      │                                      │  
      │                              ┌───────┴───────┐  
      │                              │ Sintetizza     │  
      │                              │ tutto in un    │  
      │                              │ riassunto di   │  
      │                              │ 2K token       │  
      │                              └───────┬───────┘  
      │                                      │  
      │  ◄───────────────────────────────────│  
      │  Risultato: 2K token                 │  
      │  "Le 10 best practice principali     │  
      │   sono: 1\) ... 2\) ... 3\) ..."        │  
      │                                      │  
      │  \[Il contesto del Researcher         │  
      │   viene distrutto\]                   │

      │                                      │

Il risultato netto è che nel contesto principale entrano solo 2.000 token di risultato altamente raffinato, invece di 100.000 token di materiale grezzo. Questo è un miglioramento del 98% nell'efficienza del contesto.

#### **Applicazione Pratica — Quando Usare il Researcher**

| Scenario | Usare il Researcher? | Motivo |
| ----- | ----- | ----- |
| Cercare best practice per un framework | ✅ Sì | Produce molti dati da sintetizzare |
| Analizzare documentazione di una libreria | ✅ Sì | Documentazioni sono tipicamente enormi |
| Confrontare diverse soluzioni tecniche | ✅ Sì | Richiede lettura di multiple fonti |
| Chiedere un parere su un errore specifico | ❌ No | Task troppo piccola, non serve delegare |
| Fare un semplice calcolo | ❌ No | Non c'è ricerca da fare |
| Esplorare un topic nuovo per il progetto | ✅ Sì | Esplorazione \= molti dati in input |

#### **L'Esempio Pratico dalla Guida**

L'autore della guida fornisce un esempio concreto: prima di costruire un sito internet, invece di chiedere all'agente principale di cercare le best practice (inquinando il contesto), fa questa sequenza:

1. Chiama il Researcher sub-agent: *"Cerca le best practice per costruire un sito internet"*  
2. Il Researcher fa la ricerca nel suo contesto separato  
3. Torna con un riassunto sintetico delle best practice  
4. L'agente principale usa queste best practice per costruire il sito

Questo approccio produce risultati superiori perché:

* Il contesto principale resta pulito per il lavoro di costruzione  
* Le best practice sono già sintetizzate e pronte all'uso  
* Non c'è rischio di "polluting the context" (inquinamento del contesto)

#### **Insight Avanzato — Il Concetto di "Polluting the Context"**

La guida introduce il termine "polluting the context" (inquinare il contesto) per descrivere ciò che accade quando si caricano nel contesto principale informazioni che non sono direttamente rilevanti per la task corrente. Ogni informazione irrilevante:

* Occupa spazio prezioso  
* Aumenta il rischio di "Lost in the Middle"  
* Può confondere il modello durante il ragionamento  
* Degrada la qualità complessiva delle risposte

Il Researcher sub-agent è la soluzione primaria a questo problema: tutta la "sporcizia" della ricerca resta nel suo contesto (che viene poi distrutto), e solo il "distillato" puro entra nel contesto principale.

---

### **24.4 — Il Reviewer Sub-agent**

#### **Definizione del Concetto**

Il Reviewer è un sub-agente specializzato nella revisione completa del codice. La sua caratteristica unica e fondamentale è che opera con zero contesto — non ha alcuna conoscenza pregressa del progetto, della conversazione o delle decisioni prese. Riceve semplicemente tutto il codice e lo rivede con occhi completamente freschi.

#### **Spiegazione Approfondita**

Il Reviewer rappresenta un concetto potentissimo: la revisione imparziale. Quando l'agente principale lavora su un progetto per ore, accumula bias e assunzioni. Ha preso decisioni, ha fatto scelte architetturali, ha risolto problemi in un certo modo. Il Reviewer non sa nulla di tutto questo. Vede solo il codice risultante e lo giudica per quello che è, non per come ci si è arrivati.

Il Meccanismo del Reviewer:

text

FLUSSO DEL REVIEWER SUB-AGENT  
═════════════════════════════

AGENTE PRINCIPALE                    REVIEWER SUB-AGENT  
      │                                      │  
      │  Invio di TUTTO il codice            │  
      │  del progetto                        │  
      │  (es. 200K token di codice)          │  
      │ ─────────────────────────────────►   │  
      │                                      │  
      │                              ┌───────┴───────┐  
      │                              │               │  
      │                              │  ZERO         │  
      │                              │  CONTESTO     │  
      │                              │  PRECEDENTE   │  
      │                              │               │  
      │                              │  Legge TUTTO  │  
      │                              │  il codice    │  
      │                              │  senza bias   │  
      │                              │               │  
      │                              └───────┬───────┘  
      │                                      │  
      │                              ┌───────┴───────┐  
      │                              │ Produce:      │  
      │                              │ • Bug trovati │  
      │                              │ • Migliorie   │  
      │                              │ • Ristruttura │  
      │                              │   zioni       │  
      │                              │ • Soluzioni   │  
      │                              │   alternative │  
      │                              └───────┬───────┘  
      │                                      │  
      │  ◄───────────────────────────────────│  
      │  Risultato: \~2K token                │  
      │  "8 fix applicati:                   │  
      │   Critical: 2, High: 3, Medium: 3   │  
      │   CLAUDE.md ristrutturato"           │

      │                                      │

#### **Perché "Zero Contesto" è un Vantaggio**

A prima vista, potrebbe sembrare uno svantaggio che il Reviewer non conosca il contesto del progetto. In realtà è il suo punto di forza più grande:

1\. Nessun bias di conferma:  
L'agente principale potrebbe aver scritto codice in un certo modo perché "funzionava al momento" o perché era la soluzione più rapida. Il Reviewer non ha questo bias — valuta il codice oggettivamente.

2\. Prospettiva fresca:  
Spesso in programmazione (e nella vita), quando si lavora troppo a lungo su qualcosa, si perdono di vista soluzioni migliori. Il Reviewer può dire: *"Perché l'hai fatto così? Ci sono soluzioni molto più semplici."*

3\. Scoperta di pattern nascosti:  
Senza contesto, il Reviewer analizza il codice basandosi solo sulla sua qualità intrinseca. Può identificare pattern architetturali problematici che l'agente principale non notava perché li aveva costruiti gradualmente.

#### **Cosa Fa il Reviewer in Pratica**

Dalla guida originale, quando il Reviewer viene chiamato su un progetto reale, produce:

* Fix critici: problemi di sicurezza, bug che causano crash  
* Fix ad alta priorità: problemi di performance, logica errata  
* Fix a media priorità: miglioramenti di codice, refactoring  
* Ristrutturazione del CLAUDE.md: lo rende più conciso e ben organizzato  
* Creazione di regole: genera file di regole per la cartella .claude/rules/  
* Creazione di skill: se identifica pattern ripetitivi, può suggerire di creare skill

Nell'esempio della guida, il Reviewer applicava 8 fix categorizzati per priorità (Critical, High, Medium) e ristrutturava il CLAUDE.md rendendolo più pulito e modulare.

#### **Applicazione Pratica — Quando Usare il Reviewer**

| Scenario | Usare il Reviewer? | Motivo |
| ----- | ----- | ----- |
| Dopo aver completato un MVP | ✅ Sì | Revisione completa prima di procedere |
| Dopo ogni fase significativa del progetto | ✅ Sì | Catch errori accumulati |
| Prima del deployment in produzione | ✅ Assolutamente sì | Ultima verifica critica |
| Dopo ogni singolo piccolo cambiamento | ❌ No | Spreco di risorse per task troppo piccola |
| Quando il codice "funziona ma non mi convince" | ✅ Sì | Validazione oggettiva |

#### **L'Impatto sul CLAUDE.md**

Un aspetto particolarmente prezioso del Reviewer, evidenziato nella guida, è la sua capacità di ristrutturare il CLAUDE.md. Dopo la revisione, il Reviewer produce un CLAUDE.md che:

*"È pulitissimo, non c'è praticamente nulla, quattro regole in croce, do/don't, what/how. Un gioiello per quando cominceremo ad usarlo seriamente."*

Questo è l'ideale: un CLAUDE.md conciso che contiene solo le informazioni essenziali, con tutto il resto scaricato nelle regole modulari. Il Reviewer riesce a fare questo perché, non avendo contesto, non ha "attaccamento emotivo" alle regole ridondanti e le elimina senza esitazione.

---

### **24.5 — Il QA Sub-agent**

#### **Definizione del Concetto**

Il QA (Quality Assurance) è un sub-agente specializzato nell'esecuzione di test e nella verifica che il codice funzioni correttamente. È la componente che si assicura che tutto ciò che è stato costruito funzioni come previsto, senza bug e senza regressioni.

#### **Spiegazione Approfondita**

Il QA sub-agent rappresenta la fase finale del ciclo di qualità. Se il Researcher trova le informazioni giuste per costruire qualcosa, e il Reviewer verifica che il codice sia ben scritto, il QA verifica che il codice funzioni effettivamente.

Le Attività del QA Sub-agent:

text

AMBITI DI TEST DEL QA SUB-AGENT  
════════════════════════════════

1\. TEST FUNZIONALI  
   └── Verifica che ogni funzione faccia ciò che deve fare  
   └── Testa i percorsi principali dell'applicazione  
   └── Verifica che input/output siano corretti

2\. TEST DI REGRESSIONE  
   └── Verifica che le modifiche recenti non abbiano rotto  
       funzionalità precedenti  
   └── Confronta il comportamento attuale con quello atteso

3\. TEST DI INTEGRAZIONE  
   └── Verifica che i diversi componenti lavorino insieme  
   └── Testa le connessioni con servizi esterni  
       (Supabase, Stripe, etc.)

4\. TEST DI EDGE CASE  
   └── Testa scenari limite (input vuoti, valori estremi)  
   └── Verifica la gestione degli errori

5\. FIX AUTOMATICI  
   └── Se trova bug, li corregge automaticamente

   └── Verifica che il fix non introduca nuovi problemi

#### **Come Funziona in Pratica**

Nell'esempio della guida, quando il QA sub-agent viene chiamato sull'applicazione Trello:

1. Riceve tutto il codice del progetto  
2. Esegue una batteria di test  
3. Identifica eventuali problemi  
4. Applica fix automaticamente (se gli è stato dato il permesso)  
5. Verifica che i fix funzionino  
6. Produce un report: *"Risultati QA: costruito, passato dopo il fix"*

Il dettaglio importante è che il QA può applicare fix direttamente, senza chiedere all'utente. Questo è particolarmente utile quando si lavora in modalità bypass permission e si vuole che il sistema si auto-corregga.

#### **La Sinergia tra i Tre Sub-agenti**

I tre sub-agenti raccomandati formano un sistema completo di garanzia della qualità:

text

FLUSSO IDEALE DI UN PROGETTO CON TUTTI E TRE I SUB-AGENTI  
══════════════════════════════════════════════════════════

FASE 1: RICERCA  
    Researcher → "Ecco le best practice per \[argomento\]"  
         │  
         ▼  
FASE 2: COSTRUZIONE  
    Agente Principale → costruisce il progetto usando  
                        le best practice del Researcher  
         │  
         ▼  
FASE 3: REVISIONE  
    Reviewer → "Ho trovato 8 problemi, ecco i fix.  
                Ho ristrutturato il CLAUDE.md.  
                Ho creato regole e skill."  
         │  
         ▼  
FASE 4: TESTING  
    QA → "Ho testato tutto, trovati 3 bug,  
          fixati automaticamente.   
          Tutti i test passano ora."  
         │  
         ▼  
FASE 5: RISULTATO FINALE  
    Progetto completo, testato, ottimizzato,

    con CLAUDE.md pulito e regole modulari

Questa sequenza può essere eseguita dando pochi prompt:

text

Prompt 1: "Chiama il researcher sub-agent per cercare   
           le best practice per \[progetto\]"

Prompt 2: "Usando le best practice trovate, costruisci   
           \[progetto\]" 

Prompt 3: "Chiama il reviewer sub-agent per rivedere   
           tutto il codice"

Prompt 4: "Chiama il QA sub-agent per verificare che 

           tutto funzioni"

Quattro prompt per un ciclo completo di sviluppo professionale.

#### **Il Vantaggio Economico dei Sub-agenti vs Lavoro nel Contesto Principale**

L'autore della guida sottolinea un punto fondamentale: utilizzare sub-agenti è un investimento che si ripaga. Anche se i sub-agenti consumano token nei loro contesti separati, il risparmio nel contesto principale è tale che:

* Potete lavorare per sessioni molto più lunghe senza degrado di qualità  
* Evitate di dovere ricominciare da zero perché il contesto si è saturato  
* Ogni iterazione è più efficiente perché il contesto principale è pulito  
* La qualità finale è superiore perché ogni fase è gestita da uno specialista

#### **Errori Comuni nell'Uso dei Sub-agenti**

1. Non usarli perché "tanto Claude può fare tutto": Claude può fare tutto, ma la qualità è drasticamente superiore con sub-agenti specializzati.  
2. Usare i sub-agenti per task banali: chiamare un sub-agente per rinominare un file è spreco. I sub-agenti eccellono su task complesse che generano molti token.  
3. Non parallelizzare i sub-agenti: Reviewer e QA possono lavorare contemporaneamente (in terminal separati). Non c'è motivo di aspettare che uno finisca per lanciare l'altro.  
4. Dimenticare di importare i risultati: dopo che un sub-agente ha finito, assicuratevi che i fix e le modifiche siano effettivamente applicati nel progetto principale.

---

### **24.6 — Parallelizzazione dei Sub-agenti**

#### **Definizione del Concetto**

La parallelizzazione dei sub-agenti consiste nell'eseguire più sub-agenti contemporaneamente in terminal separati, in modo che lavorino in parallelo su task diverse anziché in sequenza.

#### **Spiegazione Approfondita**

Nella guida originale, l'autore mostra come parallelizzare i sub-agenti aprendo più istanze di Claude Code:

text

TERMINAL 1 (Agente Principale)  
┌─────────────────────────────────┐  
│ $ claude \--dangerously-skip-    │  
│   permissions                    │  
│                                  │  
│ \> "Per favore chiama il         │  
│    reviewer sub-agent..."       │  
└─────────────────────────────────┘

TERMINAL 2 (Parallelo)  
┌─────────────────────────────────┐  
│ $ claude \--dangerously-skip-    │  
│   permissions                    │  
│                                  │  
│ \> "Per favore chiama il         │  
│    QA sub-agent..."             │  
└─────────────────────────────────┘

TERMINAL 3 (Parallelo)  
┌─────────────────────────────────┐  
│ $ claude \--dangerously-skip-    │  
│   permissions                    │  
│                                  │  
│ \> "Per favore fai una ricerca   │  
│    sulla pasta con il           │  
│    researcher sub-agent..."     │

└─────────────────────────────────┘

Ogni istanza ha il proprio contesto indipendente. Non si influenzano a vicenda. Tutte hanno accesso allo stesso file system (stessa cartella del progetto), quindi le modifiche fatte da un sub-agente sono visibili agli altri.

#### **L'Importanza del Flusso Monodirezionale**

Un punto critico sottolineato nella guida è che con i sub-agenti tradizionali, il flusso di informazioni è monodirezionale: dai sub-agenti all'agente principale.

text

FLUSSO MONODIREZIONALE DEI SUB-AGENTI  
═══════════════════════════════════════

     Sub-agente 1 ──────────►  
                              \\  
     Sub-agente 2 ────────────►  Agente Principale  
                              /  
     Sub-agente 3 ──────────►

OGNI FRECCIA \= solo risultato (2K token circa)

NESSUNA COMUNICAZIONE TRA SUB-AGENTI

I sub-agenti non si parlano tra loro. Sub-agente 1 non sa cosa sta facendo Sub-agente 2, e viceversa. Questo è un vantaggio per il context management (nessun overhead di comunicazione) ma un limite per task che richiedono collaborazione. Per superare questo limite, Anthropic ha introdotto gli Agent Teams, che vedremo nel capitolo successivo.

---

# **CAPITOLO 25**

## **Agent Teams — Collaborazione Multi-Agente**

---

### **25.1 — Cosa Sono gli Agent Teams**

#### **Definizione del Concetto**

Gli Agent Teams sono una funzionalità relativamente recente introdotta da Anthropic che permette di creare un team di agenti collaborativi che possono comunicare tra loro in modo bidirezionale. A differenza dei sub-agenti tradizionali (dove la comunicazione è solo dal sub-agente verso l'agente principale), negli Agent Teams ogni agente può parlare con ogni altro agente del team.

#### **Spiegazione Approfondita**

La differenza fondamentale tra sub-agenti e Agent Teams si capisce meglio con un diagramma comparativo:

SUB-AGENTI (comunicazione monodirezionale):

text

    Researcher ──────►   
                         \\  
     Reviewer  ──────────► Main Agent  
                         /  
     QA ────────────────►

• Ogni sub-agente lavora isolato  
• Nessuna comunicazione tra sub-agenti  
• Solo il risultato va all'agente principale

• Costo: BASE (1x)

AGENT TEAMS (comunicazione bidirezionale):

text

    Code Quality ◄────────► Security  
          │    \\              /    │  
          │     \\            /     │  
          │      ▼          ▼      │  
          │     Team Leader        │  
          │      ▲          ▲      │  
          │     /            \\     │  
          │    /              \\    │  
     Architect ◄──────────► Content

• Ogni agente può parlare con ogni altro agente  
• Condivisione di informazioni reciproca  
• Coordinamento automatico dei lavori

• Costo: ELEVATO (3-5x rispetto ai sub-agenti)

#### **Il Meccanismo della Comunicazione Bidirezionale**

Negli Agent Teams, quando un agente scopre qualcosa di rilevante per un altro agente, può comunicarglielo direttamente. Questo elimina il collo di bottiglia dell'agente principale come unico punto di comunicazione.

Esempio pratico dalla guida:

L'autore analizza una repository GitHub con un Agent Team di 4 teammate:

* Code Quality: analizza la qualità del codice  
* Security: analizza la sicurezza  
* Architect: analizza l'architettura  
* Content: analizza la documentazione

Durante l'analisi, il teammate Security potrebbe trovare una vulnerabilità che impatta l'architettura. In un sistema con sub-agenti tradizionali, dovrebbe:

1. Comunicare il problema all'agente principale  
2. L'agente principale dovrebbe poi comunicarlo al sub-agente Architect  
3. L'Architect dovrebbe poi proporre una soluzione  
4. La soluzione tornerebbe all'agente principale

Con un Agent Team, il processo è diretto:

1. Security comunica direttamente ad Architect: *"Ho trovato una vulnerabilità nella struttura X. Devi ristrutturare Y."*  
2. Architect modifica l'architettura  
3. Entrambi aggiornano il Team Leader

Questo è molto più veloce e produce risultati più coerenti.

#### **La Struttura del Team**

text

STRUTTURA DI UN AGENT TEAM  
═══════════════════════════

                ┌──────────────────┐  
                │   TEAM LEADER    │  
                │   (Main Agent)   │  
                │                  │  
                │ Responsabilità:  │  
                │ • Coordinamento  │  
                │ • Assegnazione   │  
                │   task           │  
                │ • Raccolta       │  
                │   risultati      │  
                │ • Decisioni      │  
                │   finali         │  
                └────────┬─────────┘  
                         │  
            ┌────────────┼────────────┐  
            │            │            │  
    ┌───────┴──────┐ ┌───┴───┐ ┌─────┴────────┐  
    │  Teammate 1  │ │ T. 2  │ │  Teammate 3  │  
    │  (es. Code   │ │(Sec.) │ │  (es. Arch.) │  
    │   Quality)   │ │       │ │              │  
    └──────┬───────┘ └───┬───┘ └──────┬───────┘  
           │             │            │  
           └─────────────┼────────────┘  
                         │  
              Comunicazione bidirezionale  
              tra tutti i teammate

#### **Come il Team Leader "Spawna" i Teammate**

Quando date un comando per creare un Agent Team, il Team Leader (l'agente principale) analizza la task e decide:

1. Quanti teammate servono (potete specificarlo voi o lasciarlo decidere a lui)  
2. Quali ruoli assegnare a ciascun teammate  
3. Quali responsabilità specifiche dare a ciascuno  
4. Come suddividere il lavoro per evitare duplicazioni

Nell'esempio della guida, l'autore chiede:

*"Crea un agent team con un massimo di quattro compagni di squadra per analizzare questa repository."*

Il Team Leader decide autonomamente di creare:

* Code Quality teammate  
* Security teammate  
* Architect teammate  
* Content teammate

Ciascuno con responsabilità specifiche e complementari.

#### **L'Interfaccia di Monitoraggio**

La guida mostra che è possibile monitorare i teammate in tempo reale. Premendo Shift \+ freccia giù nel terminal, si accede a una visualizzazione live che mostra:

text

VISUALIZZAZIONE LIVE AGENT TEAMS  
════════════════════════════════

┌─── Main (Team Leader) ──────────────────────────┐  
│ Contesto: 45.000/200.000 tokens                 │  
│ Tools chiamati: 12                               │  
│ Stato: coordinamento                             │  
└─────────────────────────────────────────────────┘

┌─── Code Quality ────────────────────────────────┐  
│ Contesto: 171.000/200.000 tokens                │ ← QUASI PIENO  
│ Tools chiamati: 47                               │  
│ Stato: analisi in corso                          │  
└─────────────────────────────────────────────────┘

┌─── Security ────────────────────────────────────┐  
│ Contesto: 89.000/200.000 tokens                 │  
│ Tools chiamati: 63                               │  
│ Stato: scan vulnerabilità                        │  
└─────────────────────────────────────────────────┘

┌─── Architect ───────────────────────────────────┐  
│ Contesto: 120.000/200.000 tokens                │  
│ Tools chiamati: 35                               │  
│ Stato: revisione struttura                       │

└─────────────────────────────────────────────────┘

Dalla guida emerge un dato importante: il teammate Code Quality ha raggiunto i 171.000 token nel suo contesto. Successivamente fa un reset del context e scende a 59.000, dimostrando che anche i teammate hanno la capacità di fare context management automatico.

#### **Le Shared Task — Coordinamento Automatico**

Una caratteristica specifica degli Agent Teams è la gestione delle shared task (task condivise). Anthropic ha implementato un meccanismo che impedisce a due agenti di lavorare sulla stessa identica cosa:

*"Loro sanno in automatico che cosa uno sta facendo e quindi Anthropic in automatico ha fatto sì che noi non avessimo mai il problema di avere due agent che lavorano sulla stessa identica cosa."*

Questo significa che se il teammate Code Quality sta analizzando il file auth.js, il teammate Security sa che quel file è "occupato" e analizzerà prima altri file, per poi tornare su auth.js quando sarà libero (con eventuali note del teammate precedente).

---

### **25.2 — Come Abilitare e Utilizzare gli Agent Teams**

#### **Definizione del Concetto**

Gli Agent Teams funzionano attualmente solo nel terminal e richiedono un processo di abilitazione specifico. Non sono disponibili nella GUI degli IDE (VS Code o Antigravity).

#### **Procedura di Abilitazione**

La guida mostra il processo pratico:

Passo 1 — Consultare la documentazione:

text

"Per favore, utilizzando questa documentazione   
\[link alla documentazione ufficiale\], 

potresti abilitarmi gli Agent Teams?"

Passo 2 — Claude configura il sistema:  
Claude legge la documentazione e configura automaticamente gli Agent Teams nel vostro ambiente.

Passo 3 — Verificare l'abilitazione:  
Dopo la configurazione, Claude conferma che gli Agent Teams sono abilitati e vi spiega come usarli.

#### **Come Creare un Team per una Task Specifica**

Una volta abilitati, potete creare un team con un singolo prompt:

text

"Crea un agent team con un massimo di \[N\] compagni   
di squadra per \[descrizione della task\]. 

Vorrei che ogni teammate avesse un ruolo specifico   
e che analizzassero \[cosa\] in parallelo.

Alla fine, portami \[tipo di risultato desiderato\]."

Esempio concreto dalla guida:

text

"Ho una repository \[link\]. Vorrei che tu la analizzassi   
creando un agent team con un massimo di quattro compagni   
di squadra. Vorrei che poi tu mi portassi delle migliorie   
che possiamo fare a tutto tondo, non solo in ambito sicurezza 

ma anche a livello di codice."

#### **Navigazione e Monitoraggio durante l'Esecuzione**

Durante l'esecuzione di un Agent Team:

| Azione | Tasto/Comando | Risultato |
| ----- | ----- | ----- |
| Vedere i teammate attivi | Guarda la barra in basso | Mostra: main, architect, code quality, etc. |
| Navigare tra i teammate | Shift \+ freccia giù | Visualizzazione live con dettagli |
| Vedere il consumo di contesto | Visualizzazione live | Token e % per ogni teammate |
| Vedere i tool chiamati | Visualizzazione live | Numero di tool call per teammate |
| Vedere il costo in tempo reale | Status line | Costo cumulativo aggiornato |

---

### **25.3 — Casi d'Uso Avanzati per gli Agent Teams**

#### **Analisi di Repository**

Il caso d'uso principale mostrato nella guida è l'analisi di repository GitHub. Questo è un uso ideale degli Agent Teams perché:

* La repository è grande (centinaia di file)  
* Serve analizzarla da prospettive diverse (sicurezza, qualità, architettura, documentazione)  
* I teammate possono lavorare in parallelo su file diversi  
* Le scoperte di un teammate possono informare il lavoro degli altri

Il risultato finale è un report completo con migliorie prioritizzate: *"Ha trovato tutte le migliorie, fixare bug critici, aggiungere un capitolo, etc."*

#### **Creazione di Contenuti Multipli in Parallelo**

Un secondo caso d'uso potente illustrato nella guida è la creazione di contenuti multipli:

text

FLUSSO DI CREAZIONE ADS CON AGENT TEAMS  
════════════════════════════════════════

ROUND 1: Generazione iniziale  
──────────────────────────────  
Prompt: "Fammi 5 proposte di ads totalmente diverse"

    Team Leader  
        │  
        ├── Teammate 1 → Ad creativa \#1  
        ├── Teammate 2 → Ad creativa \#2  
        ├── Teammate 3 → Ad creativa \#3  
        ├── Teammate 4 → Ad creativa \#4  
        └── Teammate 5 → Ad creativa \#5

    Tutto in PARALLELO → risultato in minuti

ROUND 2: Selezione e iterazione  
────────────────────────────────  
Utente: "Mi piacciono la \#2 e la \#4.   
         Fammi 5 copie diverse di ciascuna."

    Team Leader  
        │  
        ├── Sotto-team per Ad \#2  
        │   ├── Copia A  
        │   ├── Copia B  
        │   ├── Copia C  
        │   ├── Copia D  
        │   └── Copia E  
        │  
        └── Sotto-team per Ad \#4  
            ├── Copia A  
            ├── Copia B  
            ├── Copia C  
            ├── Copia D  
            └── Copia E

ROUND 3: Targeting  
──────────────────  
Utente: "Bellissima la versione visiva\!   
         Fammine 5 uguali ma targetizzate per:  
         elettricisti, imprenditori, meccanici,   
         medici, avvocati"

    Team Leader  
        │  
        ├── Versione per elettricisti  
        ├── Versione per imprenditori  
        ├── Versione per meccanici  
        ├── Versione per medici

        └── Versione per avvocati

In un'ora, con questo processo iterativo, si possono produrre 50-60 ads complete, ciascuna targetizzata per un segmento specifico. L'equivalente umano richiederebbe giorni di lavoro di un team creativo.

#### **Il Calcolo del ROI**

L'autore della guida fornisce un calcolo ROI concreto per l'uso degli Agent Teams nel contesto business:

text

CALCOLO ROI PER AGENT TEAMS (Ads)  
═════════════════════════════════

COSTO:  
• Agent Teams per 1 ora: \~€500 (scenario pessimistico)

RICAVO:  
• 50-60 ads prodotte in 1 giorno  
• Se il ticket medio cliente \= €1.000  
• Se un lead costa €50 (costo acquisizione)  
• Se le ads convertono 1 lead/giorno per 30 giorni  
• Ricavo mensile: €1.000 × 30 \= €30.000

ROI \= (€30.000 \- €500) / €500 \= 5.900%

CONFRONTO UMANO:  
• Team creativo umano: 2 settimane per 50 ads  
• Costo team umano: €5.000-€10.000  
• Agent Teams: 1 ora, €500

• Risparmio: 10-20x

Questo calcolo è ovviamente semplificato, ma illustra il principio: per un business con budget adeguato, gli Agent Teams possono avere un ROI devastante.

---

# **CAPITOLO 26**

## **Costi, ROI e Utilizzo Strategico**

---

### **26.1 — Il Costo Reale degli Agent Teams**

#### **Definizione del Concetto**

Gli Agent Teams consumano token a una velocità significativamente superiore rispetto ai sub-agenti tradizionali o al lavoro nel contesto singolo. L'autore della guida stima che il consumo sia 3-5 volte superiore rispetto all'uso di sub-agenti per la stessa task.

#### **Spiegazione Approfondita — Perché Costano di Più**

Il costo elevato degli Agent Teams deriva da tre fattori:

1\. Comunicazione bidirezionale:  
Ogni comunicazione tra teammate genera token sia in uscita (dal mittente) che in ingresso (nel destinatario). Con 4 teammate che comunicano tutti con tutti, il numero di comunicazioni possibili cresce in modo combinatorio.

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

Formula: N × (N-1) comunicazioni bidirezionali

Ogni comunicazione consuma token. Più teammate avete, più comunicazioni avvengono, più token vengono consumati.

2\. Contesti multipli simultanei:  
Ogni teammate ha il proprio contesto completo. Con 4 teammate più il Team Leader, avete 5 contesti attivi contemporaneamente, ciascuno con il proprio system prompt, i propri tool e la propria conversazione.

3\. Context Management interno:  
Come mostrato nella guida, i teammate possono raggiungere i 171.000 token nel loro contesto e poi fare reset a 59.000. Questo processo di compattazione e reset consuma ulteriori risorse computazionali.

#### **I Numeri Reali dalla Guida**

L'autore condivide dati concreti durante la sessione di Agent Teams:

| Tempo trascorso | Costo accumulato | Osservazione |
| ----- | ----- | ----- |
| \~5 minuti | €3 | "Solo l'inizio" |
| \~7 minuti | €5 | "Ogni volta che fa bip ho speso €5" |
| Fine sessione | €10-20 (stimato) | Analisi completa di una repository |

Per confronto, una sessione di lavoro normale con un singolo agente su un piano abbonamento da €17/mese costa effettivamente... €17/mese per uso illimitato. La differenza è abissale.

#### **L'Avvertimento dell'Autore**

*"Per favore non dimenticatevi mai che siate consapevoli di quello che state facendo perché se non avete i soldi da buttare tipo €10-€20 beh evitate perché nel senso non ha poi tutto questo senso."*

E ancora:

*"Nonostante sembri sexy a dirlo, facendogli andare 15 minuti spendete €80."*

Questi avvertimenti sono fondamentali. L'hype online intorno agli Agent Teams è enorme, ma l'autore (che spende circa €400/mese in Claude Code) è molto pragmatico: non li usa regolarmente perché il costo è troppo elevato per la maggior parte dei casi d'uso quotidiani.

---

### **26.2 — Quando Usare gli Agent Teams vs i Sub-agenti**

#### **Definizione del Concetto**

La scelta tra Agent Teams e sub-agenti non è una questione di "quale è migliore" ma di quale è appropriato per la task specifica, considerando il rapporto costo-beneficio.

#### **Framework Decisionale Completo**

text

ALBERO DECISIONALE: AGENT TEAMS vs SUB-AGENTI  
══════════════════════════════════════════════

La task richiede COLLABORAZIONE tra agenti?  
│  
├── NO → Usa SUB-AGENTI  
│   │  
│   ├── Task indipendenti (ricerca, review, test)  
│   ├── Risultato di un agente non dipende dagli altri  
│   └── Costo: BASSO  
│  
└── SÌ → La task genera un ROI significativo?  
    │  
    ├── NO → Usa SUB-AGENTI in sequenza  
    │   │  
    │   ├── Fai prima il Researcher  
    │   ├── Poi il Reviewer  
    │   ├── Poi il QA  
    │   └── Comunica i risultati manualmente  
    │  
    └── SÌ → Usa AGENT TEAMS  
        │  
        ├── Analisi complesse multi-dimensionali  
        ├── Creazione massiva di contenuti  
        ├── Task che richiedono coordinamento  
        └── Budget disponibile per il costo

#### **Tabella Comparativa Dettagliata**

| Caratteristica | Sub-agenti | Agent Teams |
| ----- | ----- | ----- |
| Comunicazione | Mono-direzionale (→ principale) | Bidirezionale (tutti ↔ tutti) |
| Costo | Basso (1x) | Alto (3-5x) |
| Velocità | Veloce per task singole | Velocissimo per task parallele |
| Coordinamento | Manuale (tramite utente) | Automatico (tramite Team Leader) |
| Context overhead | Minimo | Significativo |
| Ideale per | Task indipendenti e specializzate | Task complesse che richiedono collaborazione |
| Disponibilità | GUI e Terminal | Solo Terminal |
| Rischio di costo | Basso e prevedibile | Alto e potenzialmente imprevedibile |
| Esempi ideali | Ricerca, review, test | Analisi repository, creazione ads, audit |

#### **Gli Use Case Ideali per Ciascuno**

Sub-agenti — Use Case Ideali:

1. Ricerca di best practice (Researcher)  
2. Revisione del codice dopo una fase di sviluppo (Reviewer)  
3. Test e quality assurance (QA)  
4. Qualsiasi task che un singolo specialista può fare indipendentemente

Agent Teams — Use Case Ideali:

1. Analisi completa di repository grandi (multi-prospettiva)  
2. Creazione massiva di contenuti con variazioni (ads, post, email)  
3. Refactoring completo di un'applicazione (serve coordinamento tra frontend, backend, test)  
4. Audit aziendale completo (sicurezza \+ codice \+ architettura \+ documentazione)  
5. Qualsiasi task che in un'azienda richiederebbe un team di persone che si parlano

#### **La Regola Pratica**

*Se la task può essere fatta da una singola persona competente → Sub-agente*  
*Se la task richiede un team di persone che collaborano → Agent Team*

---

### **26.3 — Strategia di Utilizzo Pragmatica**

#### **Definizione del Concetto**

L'approccio pragmatico all'utilizzo di Agent Teams e sub-agenti si basa sul principio del ROI consapevole: ogni decisione di spesa deve essere giustificata da un ritorno misurabile.

#### **Il Framework ROI per la Decisione**

Prima di lanciare un Agent Team, fatevi queste domande:

text

CHECKLIST PRE-LANCIO AGENT TEAM  
═══════════════════════════════

□ 1\. VALORE: Quanto vale il risultato di questa task?  
     → Se la task produce un asset che genera ricavo: PROCEDERE  
     → Se la task è esplorativa o personale: USARE SUB-AGENTI

□ 2\. ALTERNATIVA UMANA: Quanto costerebbe farlo manualmente?  
     → Se il team umano costerebbe 10x+ il costo dell'Agent Team: PROCEDERE  
     → Se il costo è comparabile: VALUTARE caso per caso

□ 3\. TEMPO: Quanto tempo risparmiamo?  
     → Se risparmiamo giorni/settimane: PROCEDERE  
     → Se risparmiamo minuti: NON GIUSTIFICATO

□ 4\. QUALITÀ: L'Agent Team produce risultati migliori?  
     → Se la parallelizzazione migliora la qualità: PROCEDERE  
     → Se la qualità è equivalente ai sub-agenti: USARE SUB-AGENTI

□ 5\. BUDGET: Posso permettermi il costo?  
     → Se €10-80 per sessione sono sostenibili: PROCEDERE

     → Se ogni euro conta: USARE SUB-AGENTI

#### **Esempi di ROI dal Mondo Reale (dalla Guida)**

Esempio 1: Analisi Repository per un Cliente

text

Costo Agent Team:  €20 (una sessione di \~15 minuti)  
Costo alternativo: 3 developer × 2 settimane \= €6.000+  
Valore deliverable: Report completo con priorità di intervento  
ROI: Estremo (300x)

Verdetto: USARE AGENT TEAMS ✅

Esempio 2: Creazione Ads per Campagna

text

Costo Agent Team:  €500 (sessione intensiva di 1 ora)  
Costo alternativo: Team creativo × 2 settimane \= €5.000-10.000  
Valore deliverable: 50-60 ads targetizzate  
ROI: 10-20x

Verdetto: USARE AGENT TEAMS ✅

Esempio 3: Rinominare file e fare piccole modifiche

text

Costo Agent Team:  €10  
Costo alternativo: 5 minuti di lavoro manuale \= €0  
Valore deliverable: File rinominati (valore quasi nullo)  
ROI: Negativo

Verdetto: NON USARE AGENT TEAMS ❌ (usare singolo agente)

#### **Il Pubblico Target per gli Agent Teams**

L'autore è molto chiaro su chi dovrebbe usare gli Agent Teams:

* Business con budget per AI: aziende che hanno allocato budget per strumenti AI e possono assorbire costi di €100-500 per sessione  
* Consulenti AI che vendono servizi: il costo dell'Agent Team viene ribaltato sul cliente con markup  
* Progetti ad alto valore: dove il risultato dell'Agent Team vale migliaia di euro

Chi NON dovrebbe usare gli Agent Teams:

* Hobbisti e curiosi: il costo è troppo alto per l'esplorazione  
* Progetti personali a basso budget: i sub-agenti fanno il 90% del lavoro a una frazione del costo  
* Task semplici: sprecare €20 per qualcosa che un singolo agente può fare in 2 minuti

#### **Insight Avanzato — Il Pattern "Agent Team come MVP → Skill"**

Un pattern avanzato che emerge dalla guida è usare gli Agent Teams come strumento di prototipazione rapida per poi convertire il risultato in skill riutilizzabili:

text

PATTERN: AGENT TEAM → SKILL CONVERSION  
═══════════════════════════════════════

FASE 1: Usa un Agent Team per fare qualcosa di complesso  
        (costo: €50)

FASE 2: Analizza come i teammate hanno lavorato

FASE 3: Estrai i pattern e le procedure usate

FASE 4: Converti queste procedure in SKILL

FASE 5: D'ora in poi, usa le SKILL invece dell'Agent Team  
        (costo: \~€0.01 per chiamata)

RISULTATO: Investimento una tantum → risparmio perpetuo

Questo è simile al pattern MCP → Skill discusso nella guida: usate lo strumento costoso (Agent Team/MCP) per capire COME fare qualcosa, poi codificate quel "come" in una skill che costa quasi nulla da eseguire.

---

## **Riepilogo della Parte 7**

In questa Parte avete appreso:

1. Cosa sono i sub-agenti: istanze separate di Claude con contesto indipendente che restituiscono solo il risultato all'agente principale  
2. Come creare sub-agenti: file Markdown nella cartella .claude/agents/ con frontmatter (modello, limiti) e istruzioni in linguaggio naturale  
3. I tre sub-agenti raccomandati:  
   * Researcher: ricerca informazioni, restituisce sintesi (100K → 2K token)  
   * Reviewer: revisione a zero contesto, ristruttura codice e CLAUDE.md  
   * QA: test funzionali, di regressione e di integrazione con fix automatici  
4. La comunicazione monodirezionale: i sub-agenti non si parlano tra loro, tutto passa attraverso l'agente principale  
5. Gli Agent Teams: team collaborativi con comunicazione bidirezionale tra tutti i teammate  
6. Come abilitare e usare gli Agent Teams: solo via terminal, con Team Leader che spawna teammate  
7. I costi reali: Agent Teams costano 3-5x più dei sub-agenti, €10-80+ per sessione  
8. Quando usare cosa: sub-agenti per task indipendenti, Agent Teams per task che richiedono collaborazione  
9. La strategia ROI: ogni decisione di utilizzo deve essere giustificata da un ritorno misurabile  
10. Il pattern di conversione: usare strumenti costosi (Agent Teams) per prototipare, poi convertire in skill economiche

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - General|General Area]]
