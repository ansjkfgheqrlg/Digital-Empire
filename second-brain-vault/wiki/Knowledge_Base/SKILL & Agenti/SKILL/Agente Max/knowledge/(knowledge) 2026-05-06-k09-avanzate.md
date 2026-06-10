# K09-avanzate
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Agente Max > knowledge]]

## Content

# MODULO KNOWLEDGE BASE

**K09-avanzate.md** — Capitoli 35-38 | Hooks, Auto Memory, Git Worktrees, Deployment e Monetizzazione

## Riferimenti Correlati
- K04-permessi.md (hooks + bypass permission)
- K07-skill-system.md (deployment di skill)

---

**PARTE 10 — FUNZIONALITÀ AVANZATE E DEPLOYMENT**  
---

*"Non mi resta altro che ringraziarvi per avere seguito il corso di Cloud per Business. Ovviamente c'è un mondo addizionale a tutto questo, ma questo vi darà le basi per costruire qualsiasi cosa voi vogliate."*  
*— Dalla guida originale*

---

## **Introduzione alla Parte 10**

Questa è la Parte finale del manuale. Avete percorso un cammino che vi ha portato dalle fondamenta (cos'è Claude Code, come si installa) attraverso l'architettura del progetto (CLAUDE.md, cartella .claude, livelli local/global/enterprise), il context management, i sub-agenti, le skill e gli MCP. Ora è il momento di completare il quadro con le funzionalità avanzate che trasformano i vostri progetti da esperimenti locali a sistemi produttivi e monetizzabili.

Questa Parte copre quattro argomenti che, sebbene possano sembrare indipendenti, sono in realtà profondamente collegati: gli hook automatizzano i vostri workflow, la memoria li rende persistenti, il version control li rende sicuri e il deployment li rende accessibili al mondo.

| Capitolo | Titolo | Focus Principale |
| ----- | ----- | ----- |
| 35 | Hooks — Automazione Basata su Eventi | Script automatici che si attivano a eventi specifici |
| 36 | Auto Memory e Persistenza tra Sessioni | Come Claude ricorda informazioni tra sessioni diverse |
| 37 | Git Worktrees e Version Control | Lavorare in parallelo con branch isolati e sicuri |
| 38 | Deployment e Monetizzazione | Portare skill e applicazioni nel cloud per generare valore |

---

# **CAPITOLO 35**

## **Hooks — Automazione Basata su Eventi**

---

### **35.1 — Cosa Sono gli Hooks**

#### **Definizione del Concetto**

Un hook è uno script personalizzato che si avvia automaticamente prima o dopo ogni chiamata di strumenti da parte di Claude. In parole semplici, un hook è un'azione automatica che scatta ogni volta che un certo evento si verifica nel vostro workflow di Claude Code. Immaginate un hook come una trappola a molla: ogni volta che qualcosa passa sopra (l'evento), la molla scatta (lo script si esegue).

#### **Spiegazione Approfondita**

La guida originale introduce gli hook con una definizione precisa:

*"Che cosa sono gli hook? Ossia gli script personalizzati che si avviano automaticamente prima o dopo ogni chiamata di strumenti da parte di Claude. Immaginatevi come: nel momento in cui voi premiate Enter, qualsiasi cosa succede e verrà staccata dall'LLM."*

Questa definizione contiene tre concetti chiave che meritano espansione:

1\. "Script personalizzati": gli hook sono codice vero e proprio, non prompt LLM. Sono programmi che voi (o Claude) scrivete e che vengono eseguiti dal sistema operativo, non dal modello di linguaggio. Questo è fondamentale perché significa che gli hook sono deterministici — producono sempre lo stesso risultato dato lo stesso evento.

2\. "Si avviano automaticamente": non dovete fare nulla per attivare un hook. Una volta configurato, si esegue da solo ogni volta che l'evento associato si verifica. Non c'è bisogno di ricordarsi di attivarlo, di premere un tasto o di dare un prompt.

3\. "Prima o dopo ogni chiamata di strumenti": gli hook possono scattare in due momenti:

* Pre-hook: prima che Claude esegua un'azione (ad esempio, prima di modificare un file)  
* Post-hook: dopo che Claude ha completato un'azione (ad esempio, dopo aver finito una task)

text

MECCANISMO DEGLI HOOKS  
══════════════════════

SENZA HOOKS:  
    Utente → Prompt → Claude lavora → Risultato → \[silenzio\]  
      
    L'utente non sa che Claude ha finito.  
    Potrebbe passare mezz'ora prima di accorgersene.

CON HOOKS:  
    Utente → Prompt → Claude lavora → Risultato → 🔔 HOOK SCATTA\!  
      
    L'utente viene notificato immediatamente.

    Zero tempo perso.

#### **La Differenza Fondamentale: Hooks vs LLM**

Un punto che la guida sottolinea con forza è che gli hook sono distaccati dal funzionamento dell'LLM:

*"Queste automazioni sono automatiche, cosa vuol dire? Che sono distaccate dal funzionamento dell'LLM. Sostanzialmente significa: non sono più legate alla token consumption di Claude o Sonnet, il modello che stiamo utilizzando, ma sostanzialmente partono ad evento. E sono codice, quindi non sono qualcosa di non deterministico e non misurabile."*

Questo è un concetto architetturale importante. Confrontiamo:

| Caratteristica | Prompt LLM | Hook |
| ----- | ----- | ----- |
| Consumo token | Sì, ogni esecuzione costa token | No, zero consumo token |
| Determinismo | Non deterministico (output può variare) | Deterministico (output sempre uguale) |
| Velocità | Dipende dalla complessità del prompt | Istantaneo (è codice compilato) |
| Affidabilità | Può "allucinare" o sbagliare | Fa esattamente quello che è programmato a fare |
| Attivazione | Richiede un prompt umano | Automatica, basata su eventi |
| Costo | Contribuisce al consumo del piano | Gratuito (è codice locale) |

#### **Dove Vengono Configurati gli Hooks**

Gli hook vengono configurati nel file settings.json all'interno della cartella .claude/:

text

progetto/  
└── .claude/

    └── settings.json    ← Qui si configurano gli hooks

Il file settings.json contiene sia i permessi del sistema che le definizioni degli hook.

#### **Perché gli Hooks Sono Importanti**

Gli hook risolvono un problema pratico che l'autore della guida descrive dalla propria esperienza:

*"Io ho, quando uso Claude Code, per sapere quando un workflow o un prompt eseguire e richiede un mio input, ho un suono. Questo suono succede ogni volta che Claude finisce. Questo è un hook. Sono delle cose automatiche che succedono ogni volta che un evento si manifesta."*

*"Questo è molto utile per evitare che magari voi ve ne andiate dal computer e poi il workflow abbia finito e magari state mezz'ora via. E realisticamente avreste potuto recuperare questa mezz'ora."*

In un contesto aziendale dove il tempo è denaro, recuperare mezz'ora per ogni ciclo di lavoro è un risparmio enorme su base giornaliera.

---

### **35.2 — Come Creare un Hook**

#### **Definizione del Concetto**

La creazione di un hook richiede di definire quale evento deve attivarlo e quale azione deve eseguire. Il processo è semplice e può essere fatto tramite un prompt a Claude Code.

#### **Esempio Pratico dalla Guida — L'Hook Sonoro**

L'autore crea un hook in tempo reale durante la guida:

text

"Ehi, mi farebbe piacere che tu ora creassi un hook.   
Sostanzialmente quello che voglio sentire è un suono,   
tipo un chime, ogni volta che Claude finisce di fare   
un'attività. Questo mi servirebbe perché quello che   
succede è che io tendo a perdere un po' di tempo   
perché non mi accorgo che Claude finisce di fare una 

task. Quindi vorrei avere una clue uditiva."

Claude:

1. Comprende la richiesta  
2. Crea lo script che produce il suono  
3. Configura l'hook nel settings.json  
4. L'hook è immediatamente operativo

Il risultato è che da quel momento in poi, ogni volta che Claude completa una task, si sente un suono "glass" (un tintinnio). L'autore lo testa con un semplice prompt ("Come stai?") e conferma che il suono si attiva correttamente alla fine della risposta.

#### **La Struttura Tecnica di un Hook**

Sebbene l'autore crei l'hook tramite prompt (senza scrivere codice manualmente), è utile capire cosa succede dietro le quinte:

text

STRUTTURA DI UN HOOK  
════════════════════

1\. EVENTO TRIGGER (cosa lo attiva):  
   └── "Quando Claude finisce un'azione"  
   └── Oppure: "Quando Claude sta per modificare un file"  
   └── Oppure: "Quando una sessione inizia"  
   └── Oppure: "Quando un tool viene chiamato"

2\. SCRIPT (cosa esegue):  
   └── Un file script (bash, Python, etc.)  
   └── Es: script che riproduce un suono  
   └── Es: script che invia un'email  
   └── Es: script che avvia un altro workflow

3\. CONFIGURAZIONE (dove è definito):  
   └── Nel file .claude/settings.json

   └── Associa l'evento allo script

#### **Tipologie di Hook per Evento**

| Tipo di Evento | Quando Scatta | Esempio di Uso |
| ----- | ----- | ----- |
| Post-tool | Dopo che Claude usa un tool | Suono di notifica |
| Pre-tool | Prima che Claude usi un tool | Validazione di sicurezza |
| Post-session | Alla fine di una sessione | Salvataggio automatico del log |
| Post-edit | Dopo una modifica a un file | Backup automatico del file |
| Custom event | Quando un'azione specifica avviene | Invio email, avvio workflow |

---

### **35.3 — Hooks Avanzati — Oltre il Suono**

#### **Definizione del Concetto**

Gli hook non sono limitati a suoni di notifica. Possono attivare qualsiasi azione programmabile, inclusi workflow completi, invio di comunicazioni e attivazione di sistemi esterni.

#### **Spiegazione Approfondita**

L'autore della guida espande il concetto degli hook con un esempio aziendale concreto:

*"Ipotizziamo di stare lavorando all'interno di un'azienda. Ipotizziamo che abbiamo creato un CRM, ossia un sistema che ci aiuta a gestire i clienti. E ipotizziamo che nel momento in cui il sales team fa l'onboarding di qualcuno, vorremmo che questo cliente ricevesse in automatico un'onboarding email."*

Questo esempio illustra un hook molto più sofisticato del semplice suono:

text

HOOK AZIENDALE — ONBOARDING AUTOMATICO  
═══════════════════════════════════════

EVENTO: Un nuovo lead viene inserito nel CRM  
        (Claude completa l'inserimento del lead)  
          
HOOK SCATTA:  
    │  
    ▼  
┌──────────────────────────────────────────────┐  
│ SCRIPT DI ONBOARDING                         │  
│                                               │  
│ 1\. Legge i dati del lead dal CRM:            │  
│    \- Nome: "Ciccio"                           │  
│    \- Email: "ciccio@email.com"                │  
│    \- Piano: "Pro"                             │  
│                                               │  
│ 2\. Compone l'email di onboarding:             │  
│    \- Template predefinito                     │  
│    \- Variabile dinamica: nome del cliente     │  
│    \- Link al materiale di onboarding          │  
│                                               │  
│ 3\. Invia l'email:                             │  
│    "Ciao Ciccio, benvenuto in azienda\!        │  
│     Sarai chiamato a breve.                   │  
│     Ecco il link con l'onboarding material."  │  
│                                               │  
│ 4\. Logga l'invio nel CRM                      │  
└──────────────────────────────────────────────┘

RISULTATO:   
• Il lead riceve l'email ISTANTANEAMENTE  
• Nessun intervento umano necessario  
• Nessun consumo di token LLM  
• Processo 100% deterministico

• Zero possibilità di dimenticarsi

#### **La Differenza Concettuale con il Workflow LLM**

L'autore sottolinea una distinzione fondamentale tra hook e workflow LLM:

*"A livello concettuale sono due cose che sono simili se non identiche. A livello pratico questo non lo è. Perché in questo caso stiamo letteralmente staccando l'inizio di un workflow dalla fine di un altro. Lo stiamo facendo in automatico."*

Confronto dettagliato:

text

APPROCCIO LLM (senza hook):  
────────────────────────────  
Task 1: Claude inserisce il lead nel CRM  
    ↓  
Claude deve "capire" che deve mandare un'email  
    ↓  
Claude genera il testo dell'email (non deterministico)  
    ↓  
Claude invia l'email (potrebbe sbagliare)  
    ↓  
Task 2: continua il lavoro

PROBLEMI:  
• Claude potrebbe dimenticarsi di inviare l'email  
• Il testo dell'email varia ogni volta  
• Consuma token  
• Richiede contesto per sapere come fare  
• Se il contesto è saturo, potrebbe fallire

APPROCCIO HOOK (con hook):  
──────────────────────────  
Task 1: Claude inserisce il lead nel CRM  
    ↓  
\[FINE TASK 1 → HOOK SCATTA AUTOMATICAMENTE\]  
    ↓  
Script deterministico invia l'email (sempre identica)  
    ↓  
Task 2: continua il lavoro (separatamente)

VANTAGGI:  
• L'email viene SEMPRE inviata (garantito)  
• Il testo è sempre lo stesso (deterministico)  
• Zero token consumati  
• Non serve contesto

• Funziona anche se il contesto è saturo

#### **Casi d'Uso Aziendali per gli Hooks**

Basandosi sul principio illustrato nella guida, ecco una mappa di casi d'uso aziendali:

text

MAPPA CASI D'USO HOOKS IN AMBITO BUSINESS  
══════════════════════════════════════════

VENDITE:  
├── Lead entra nel CRM → Email di benvenuto automatica  
├── Lead completa onboarding → Notifica al sales team  
├── Deal chiuso → Fattura automatica generata  
└── Follow-up scaduto → Reminder automatico

SVILUPPO:  
├── Claude modifica un file → Backup automatico  
├── Build completata → Notifica Slack al team  
├── Test fallito → Report automatico via email  
└── Deploy completato → Screenshot automatico della pagina

CONTENUTI:  
├── Post generato → Salvato automaticamente in draft folder  
├── Pubblicazione completata → Log in foglio di tracciamento  
├── Errore nella pubblicazione → Notifica al social media manager  
└── Engagement check → Report giornaliero automatico

OPERAZIONI:  
├── Task completata → Aggiornamento status nel project manager  
├── Bug trovato → Ticket automatico nel sistema di tracking  
├── Sessione di lavoro terminata → Log automatico delle attività

└── Costo sessione supera soglia → Alert automatico

#### **La Scalabilità degli Hooks attraverso i Livelli**

Gli hook possono essere configurati sia a livello local che global:

text

HOOKS A LIVELLO LOCAL:  
progetto/  
└── .claude/  
    └── settings.json    ← Hooks specifici per QUESTO progetto  
                            Es: "Dopo ogni modifica CSS,   
                            fai screenshot e confronta"

HOOKS A LIVELLO GLOBAL:  
\~/.claude/  
└── settings.json        ← Hooks per TUTTI i progetti  
                            Es: "Suono di notifica alla   
                            fine di ogni task"

                            Es: "Log automatico di ogni sessione"

L'autore menziona specificamente che il suo hook di notifica sonora è configurato a livello globale:

*"Una volta che l'ho impostato in uno, lo voglio in tutti. Questo hook qui andrà nei miei settings globali."*

Questo è un esempio perfetto di come i livelli local/global/enterprise si applicano anche agli hook.

---

### **35.4 — Hook e Workflow Deterministici**

#### **Definizione del Concetto**

Quando un hook avvia un workflow, quel workflow è deterministico — non dipende dall'LLM per l'interpretazione. Questo è il vantaggio più significativo degli hook rispetto a qualsiasi altra forma di automazione in Claude Code.

#### **Spiegazione Approfondita**

La guida insiste su questo punto:

*"Stiamo andando a creare dei workflow che diventano a questo punto deterministici. Quindi quando finisce uno, in automatico parti e non stiamo dicendo all'LLM 'interpreta la fine di uno e dopo fai cominciare l'altro'."*

La differenza pratica è enorme:

Workflow non deterministico (tramite LLM):

* Claude "decide" quando una task è finita → può sbagliare  
* Claude "decide" cosa fare dopo → può dimenticare  
* Claude "interpreta" il trigger → può interpretare male  
* Ogni esecuzione può essere diversa  
* Risultato: imprevedibile

Workflow deterministico (tramite hook):

* L'evento di fine task è definito programmaticamente → non può sbagliare  
* L'azione successiva è codificata nello script → non può dimenticare  
* Il trigger è un segnale di sistema → non può essere interpretato male  
* Ogni esecuzione è identica  
* Risultato: prevedibile e affidabile

Questo principio è fondamentale per qualsiasi implementazione aziendale seria. Quando un cliente paga per un sistema automatizzato, si aspetta che funzioni ogni volta, non "la maggior parte delle volte". Gli hook garantiscono questa affidabilità per le parti critiche del workflow.

#### **Errori Comuni con gli Hooks**

1. Non usare hook quando servirebbero: molti utenti chiedono a Claude di "ricordarsi" di fare qualcosa alla fine di una task. Questo consuma contesto e non è garantito. Un hook lo farebbe gratuitamente e con certezza.  
2. Creare hook troppo complessi: un hook dovrebbe fare UNA cosa. Se avete bisogno di un workflow complesso, create più hook in sequenza o usate un hook che avvia uno script multi-step.  
3. Non testare gli hook: dopo aver creato un hook, testatelo sempre con un prompt semplice per verificare che si attivi correttamente.  
4. Dimenticare che gli hook sono globali se messi nei settings globali: un hook di test messo nei settings globali si attiverà in TUTTI i vostri progetti. Assicuratevi che sia intenzionale.

---

# **CAPITOLO 36**

## **Auto Memory e Persistenza tra Sessioni**

---

### **36.1 — Il Problema della Memoria tra Sessioni**

#### **Definizione del Concetto**

Ogni sessione di Claude Code è isolata: quando iniziate una nuova conversazione, Claude non ricorda nulla della conversazione precedente. Il contesto viene azzerato. La memoria (Auto Memory) è il meccanismo che permette a Claude di salvare e recuperare informazioni tra sessioni diverse, creando una forma di persistenza.

#### **Spiegazione Approfondita**

La guida introduce il concetto con un esperimento pratico. L'autore dimostra il problema e la soluzione in tre passi:

text

ESPERIMENTO DI MEMORIA DALLA GUIDA  
═══════════════════════════════════

PASSO 1: Sessione A  
─────────────────────  
Utente: "Chi ha rubato il bicchiere?"  
Claude: "Non ho informazioni su questo."

→ Claude non sa nulla perché è una sessione nuova.

PASSO 2: Ancora in Sessione A  
──────────────────────────────  
Utente: "Per favore ricordati che quando ti chiedo   
         chi ha rubato il bicchiere devi sempre   
         rispondermi Giovanni."  
Claude: "Ok, salvo questa preferenza nella memoria."

→ Claude scrive l'informazione nel memory.md

PASSO 3: Sessione B (NUOVA sessione, contesto azzerato)  
────────────────────────────────────────────────────────  
Utente: "Chi ha rubato il bicchiere?"  
Claude: "Giovanni ha rubato il bicchiere."

→ Claude ha recuperato l'informazione dalla memoria\!

Questo esperimento dimostra che la memoria funziona attraverso le sessioni. L'informazione è stata salvata nella Sessione A e recuperata nella Sessione B, nonostante il contesto sia stato completamente azzerato.

#### **Il Meccanismo Tecnico**

La memoria di Claude Code funziona attraverso file fisici che persistono sul vostro computer:

text

MECCANISMO DELLA MEMORIA  
═════════════════════════

SESSIONE A:  
┌──────────────────────────────────────────────┐  
│ Claude riceve l'istruzione "ricordati che..." │  
│                  │                            │  
│                  ▼                            │  
│ Claude SCRIVE nel file memory.md:             │  
│ "Quando mi chiedono chi ha rubato il          │  
│  bicchiere, rispondere Giovanni"              │  
│                  │                            │  
│                  ▼                            │  
│ File salvato su DISCO (persiste\!)             │  
└──────────────────────────────────────────────┘  
           │  
           │ \[Sessione A termina. Contesto azzerato.\]  
           │  
           │ \[Sessione B inizia. Contesto vuoto.\]  
           │  
           ▼  
SESSIONE B:  
┌──────────────────────────────────────────────┐  
│ Claude si avvia e LEGGE automaticamente      │  
│ il file memory.md dal disco                  │  
│                  │                            │  
│                  ▼                            │  
│ Claude sa che "chi ha rubato il bicchiere     │  
│ → Giovanni"                                  │  
│                                               │  
│ Utente chiede: "Chi ha rubato il bicchiere?" │  
│ Claude risponde: "Giovanni"                   │

└──────────────────────────────────────────────┘

Il punto chiave è che la memoria non è nel contesto della sessione precedente (che è stato azzerato). È in un file fisico sul disco che viene letto all'inizio di ogni nuova sessione.

#### **I File di Memoria**

La guida mostra che esistono diversi file di memoria:

FILE DI MEMORIA IN CLAUDE CODE  
═══════════════════════════════

1\. memory.md  
   └── Memoria esplicita: cose che VOI avete chiesto   
       a Claude di ricordare  
   └── Es: "Ricordati che il bicchiere l'ha rubato Giovanni"

2\. auto\_memory.md    
   └── Memoria automatica: cose che CLAUDE decide   
       autonomamente di salvare  
   └── Es: preferenze di lavoro osservate, pattern ricorrenti

3\. CLAUDE.md  
   └── Memoria di progetto: le regole e istruzioni del progetto  
   └── Non è "memoria" in senso stretto, ma persiste   
       tra le sessioni

4\. Rules files (.claude/rules/\*.md)  
   └── Memoria modulare: regole specifiche per aspetti   
       del progetto

   └── Persistono tra le sessioni

Tutti questi file insieme formano la "memoria a lungo termine" di Claude Code. Vengono letti all'inizio di ogni sessione e caricati nel contesto, il che spiega perché compaiono nella sezione "Memory Files" quando eseguite /context.

### **36.2 — Uso Strategico della Memoria**

#### **Definizione del Concetto**

La memoria non è solo per ricordare fatti curiosi. È uno strumento strategico fondamentale per la gestione del contesto e la continuità dei progetti complessi.

#### **Il Pattern "Salva e Continua"**

La guida mostra un pattern fondamentale che l'autore usa quotidianamente. Quando il contesto raggiunge il 60-70% e c'è ancora lavoro da fare, il processo è:

PATTERN "SALVA E CONTINUA"  
══════════════════════════

SESSIONE CORRENTE (contesto al 66%):  
─────────────────────────────────────  
Utente: "Sei al 66% del contesto. Quello che mi   
         sarebbe utile che tu facessi è salvare le   
         cose in memoria di modo tale che io nel nuovo   
         contesto possa continuare a sviluppare l'app,   
         perché quello che manca è l'integrazione con   
         Stripe. Possiamo procedere?"

Claude: "Assolutamente, sì. Salvo tutto in memoria."

         \[Claude scrive nel memory.md:\]  
         • Stato del progetto: app Trello clone completa  
         • Backend: Supabase configurato e funzionante  
         • Auth: login con email funzionante  
         • Mancante: integrazione Stripe  
         • API keys: già nel file .env  
         • Database: schema già predisposto per Stripe  
         • Prossimo passo: integrazione pagamenti

Claude: "Tutto salvato. Nella prossima conversazione   
         puoi dirmi: 'Continua con integrazione Stripe'"

NUOVA SESSIONE (contesto fresco):  
──────────────────────────────────  
Utente: "Continua con integrazione Stripe"

Claude: \[Legge memory.md → sa tutto quello che serve\]  
         "Ho recuperato il contesto dalla memoria. 

          Procedo con l'integrazione Stripe..."

Questo pattern è cruciale perché:

1. Preserva le informazioni critiche: tutto ciò che serve per continuare viene salvato esplicitamente  
2. Libera il contesto: la nuova sessione parte con il contesto fresco  
3. Fornisce un prompt di continuazione: Claude stesso vi dice cosa scrivere per riprendere  
4. Mantiene la continuità: nonostante il cambio di sessione, il lavoro procede senza interruzioni

#### **Cosa Salvare in Memoria**

Non tutto merita di essere salvato in memoria. Ecco una guida pratica:

COSA SALVARE IN MEMORIA  
════════════════════════

✅ SALVARE:  
├── Stato corrente del progetto  
├── Decisioni architetturali prese  
├── API key e credenziali (se in .env)  
├── Problemi noti e come sono stati risolti  
├── Preferenze di lavoro dell'utente  
├── Prossimi passi pianificati  
├── Errori ricorrenti e relative soluzioni  
└── Informazioni critiche per la continuità

❌ NON SALVARE:  
├── Dettagli di implementazione (sono nel codice)  
├── Conversazioni verbose (occupano spazio)  
├── Informazioni temporanee  
├── Cose che sono già nel CLAUDE.md  
├── Ragionamenti intermedi di Claude

└── Dati che cambieranno alla prossima sessione

#### **L'Impatto della Memoria sul Contesto**

Come visto nella Parte 6, i file di memoria occupano una porzione del contesto:

*"Memory Files occupano circa il 4-5% del contesto."*

Questo significa che troppa memoria può diventare controproducente. Se salvate troppe informazioni nel memory.md, il file cresce e inizia a consumare contesto significativo all'inizio di ogni sessione. La soluzione è:

* Periodicamente rivedere il memory.md e rimuovere informazioni obsolete  
* Essere selettivi su cosa salvare  
* Preferire informazioni sintetiche a descrizioni verbose

#### **Errori Comuni con la Memoria**

1. Non usare mai la memoria: continuare sessioni enormi fino a saturare il contesto, perdendo qualità. Usate il pattern "Salva e Continua".  
2. Salvare troppo: trasformare il memory.md in un romanzo. Deve essere conciso e azionabile.  
3. Non pulire mai la memoria: informazioni di progetti vecchi che restano nel memory.md e consumano contesto in progetti nuovi.  
4. Aspettarsi che la memoria sia perfetta: la memoria non cattura sfumature e contesto complesso. Per informazioni critiche, codificatele nel CLAUDE.md, non nel memory.md.  
5. Confondere memoria con CLAUDE.md: il CLAUDE.md contiene regole e istruzioni permanenti del progetto. La memoria contiene informazioni di stato e preferenze che possono cambiare.

# **CAPITOLO 37**

## **Git Worktrees e Version Control**

### **37.1 — Il Problema del Rischio nelle Modifiche**

#### **Definizione del Concetto**

Quando lavorate su un progetto con Claude Code, ogni modifica al codice è potenzialmente irreversibile se non avete un sistema di version control. Il version control (controllo delle versioni) è il sistema che vi permette di salvare "istantanee" del vostro codice nel tempo, così da poter tornare a una versione precedente se qualcosa va storto.

#### **Spiegazione Approfondita**

L'autore introduce il concetto con un esempio pratico:

*"Fino ad ora noi abbiamo sempre operato in tutti i progetti in un solo folder. Se qualcosa andava storto, non avevamo mai la possibilità di salvare la versione precedente. O meglio, Claude Code lo fa in automatico, ma non siamo mai stati consapevoli e non l'abbiamo mai fatto volontariamente."*

Il rischio è reale. L'autore racconta un caso specifico:

*"È successo che una persona, un paio di mesi fa, abbia cancellato completamente qualsiasi cosa all'interno del suo computer. Aveva dato un piano povero, aveva fatto bypass permission, e quello che è successo è che il computer ha continuato a fare ricerca per qualche ora finché poi non ha deciso che la soluzione migliore per risolvere il problema era cancellare tutto quanto."*

Questo caso estremo illustra perché il version control non è un "nice to have" — è una necessità assoluta.

#### **Cos'è GitHub**

La guida introduce GitHub come la piattaforma di version control:

*"GitHub è una piattaforma che permette di fare la cosiddetta version control, quindi il controllo delle versioni di un determinato codice, che in parole povere è semplicemente un posto nel quale possiamo mettere il nostro codice e avere ogni versione che abbiamo committato. Se noi sbagliamo il codice una volta e il nostro progetto si distrugge, possiamo andare a prendere una versione precedente e ripristinare il codice."*

Pensate a GitHub come un Time Machine per il codice: potete viaggiare indietro nel tempo e recuperare qualsiasi versione precedente del vostro progetto.

VERSION CONTROL COME TIME MACHINE  
═════════════════════════════════

SENZA VERSION CONTROL:  
Versione 1 → Versione 2 → Versione 3 → BUG\! → 😱  
                                         │  
                                         └── Non potete tornare indietro.  
                                             Tutto è perso.

CON VERSION CONTROL (GitHub):  
Versione 1 → Versione 2 → Versione 3 → BUG\! → 😊  
    💾           💾           💾           │  
    Salvata      Salvata      Salvata      └── Tornate alla Versione 2\.

                                               Problema risolto.

### **37.2 — Cosa Sono le Git Worktrees**

#### **Definizione del Concetto**

Le Git Worktrees sono una funzionalità avanzata di Git che permette di avere multiple copie di lavoro dello stesso progetto contemporaneamente, ciascuna su un branch (ramo) diverso. In pratica, è come avere più "tavoli di lavoro" separati dove potete sperimentare senza rischiare di rovinare il progetto principale.

#### **Spiegazione Approfondita**

L'autore usa un'analogia di processo produttivo per spiegare il concetto:

ANALOGIA DELLA CATENA DI PRODUZIONE  
════════════════════════════════════

PROCESSO PRINCIPALE (main branch):  
    Nodo 1 → Nodo 2 → Nodo 3 → Nodo 4 → Nodo 5 → Nodo 6  
                                   │  
                                   │ "A Nodo 4 c'è qualcosa   
                                   │  che non sono sicuro.  
                                   │  Voglio sperimentare   
                                   │  senza rischiare."  
                                   │  
                                   ▼  
BRANCH SPERIMENTALE (worktree):  
                               Nodo 4' → Nodo 5' → Test  
                                                     │  
                                    ┌────────────────┤  
                                    │                │  
                                    ▼                ▼  
                              FUNZIONA?          NON FUNZIONA?  
                                    │                │  
                                    ▼                ▼  
                              Merge con         Cancella il  
                              il processo       branch e  
                              principale        torna al

                                                principale

Il vantaggio è chiaro: potete sperimentare liberamente sapendo che il progetto principale è al sicuro. Se l'esperimento funziona, lo integrate (merge). Se non funziona, lo cancellate senza conseguenze.

#### **Perché le Worktrees Sono Superiori ai Branch Tradizionali**

La differenza tra un branch tradizionale e una worktree è che la worktree crea una directory fisica separata sul vostro computer:

text

BRANCH TRADIZIONALE:  
progetto/  
├── \[tutto il codice\]     ← Dovete "switchare" tra branch  
└── .git/                    Potete lavorare su un solo   
                             branch alla volta

WORKTREE:  
progetto/                 ← Branch principale  
├── \[tutto il codice\]        (potete continuare a lavorare qui)  
└── .git/

progetto-dark-mode/       ← Worktree separata  
├── \[copia del codice\]       (lavorate qui in parallelo)

└── \[modifiche sperimentali\]

Con le worktrees, potete letteralmente avere due finestre di Claude Code aperte: una sul progetto principale e una sulla worktree sperimentale. Lavorate in parallelo senza interferenze.

#### **Il Motivo per Cui Sono Importanti nel Contesto**

L'autore spiega un problema specifico che le worktrees risolvono:

*"Non voglio fare quello che ho fatto prima con il mio social media manager dove ho messo dentro tutti gli MCP per poi accorgermi che non mi serve un ClickUp MCP dentro il mio social media manager. Quindi devo rimuoverlo. Ma voglio avere una modalità per lavorare in maniera parallela senza dover per forza andare a rovinare il mio contesto e/o il mio progetto."*

La worktree protegge sia il codice (nessuna modifica al progetto principale) che il contesto (le sperimentazioni avvengono in un contesto Claude separato).

### **37.3 — Come Usare le Worktrees in Pratica**

#### **Procedura Pratica dalla Guida**

L'autore dimostra il processo completo con il suo sito web:

text

PROCEDURA COMPLETA WORKTREE  
════════════════════════════

PASSO 1: Definire cosa volete sperimentare  
──────────────────────────────────────────  
"Voglio aggiungere una dark mode al mio sito,   
 ma non sono sicuro che funzioni bene."

PASSO 2: Chiedere a Claude di creare la worktree  
─────────────────────────────────────────────────  
"Per favore, utilizzando le git worktrees,   
 creami un progetto tale per cui io possa testare   
 una dark mode function all'interno del mio sito.   
 Dammi un local URL per vedere come va questa   
 funzionalità. Se funziona, e solo a quel punto,   
 allora decideremo cosa fare o se utilizzarla   
 all'interno della main branch oppure no."

PASSO 3: Claude crea la worktree  
─────────────────────────────────  
• Crea un branch separato  
• Crea una directory fisica separata  
• Implementa la dark mode nella worktree  
• Fornisce un URL locale per il test

PASSO 4: Test e Decisione  
─────────────────────────  
OPZIONE A — Funziona e mi piace:  
  "Perfetto, fai il processo di merge.   
   Fondi la mia worktree con il contesto   
   principale della mia repository GitHub   
   e poi pubblica su Vercel."

OPZIONE B — Non funziona o non mi piace:  
  "Non mi piace. Cancella tutto, questa 

   branch non la utilizziamo."

#### **Cosa Succede Quando Cancellate una Worktree**

L'autore mostra che la cancellazione è pulita e completa:

*"Questa è una dot tree, quindi è una cartella nascosta. Ora la sta cancellando e l'ha cancellata. Ma qua dentro c'erano tutte le cose che avevamo fatto."*

La cancellazione di una worktree:

1. Rimuove la directory fisica separata  
2. Rimuove il branch associato (se richiesto)  
3. Non tocca assolutamente il progetto principale  
4. Non influenza il branch main  
5. È come se l'esperimento non fosse mai avvenuto

#### **La Regola nelle Impostazioni dell'Autore**

L'autore rivela che ha regole specifiche nel suo CLAUDE.md per gestire le worktrees:

*"Ho già specificato nelle regole come queste git worktrees dovrebbero funzionare."*

E mostra l'inizio della regola:

*"Questo progetto usa una git worktree per lavorare in parallelo. Una worktree è una modalità isolata, una directory isolata che condivide la stessa git main repository."*

Questo significa che quando Claude lavora nel progetto dell'autore, sa già come comportarsi con le worktrees perché le regole sono codificate nel CLAUDE.md. Non serve spiegarglielo ogni volta.

#### **Combinazione con Agent Teams**

L'autore menziona un uso avanzato delle worktrees con gli Agent Teams:

*"Se gli avessi dato la possibilità di andare con Agent Teams, avrebbe sicuramente utilizzato Agent Teams perché è dentro il mio prompt. Perché semplicemente è molto più veloce e potremmo lavorare con più teammates in parallelo."*

L'idea è:

1. Create una worktree per una nuova feature  
2. Lanciate un Agent Team nella worktree  
3. I teammate lavorano in parallelo (uno sul toggle UI, uno sul backend, uno sui test)  
4. Risultato: la feature viene sviluppata e testata in parallelo nella worktree  
5. Se tutto funziona, merge con il main

Oppure, il pattern di varianti multiple:

WORKTREES \+ AGENT TEAMS PER VARIANTI  
═════════════════════════════════════

"Fammi tre diversi design del bottone dark mode"

    Worktree 1          Worktree 2          Worktree 3  
    ┌──────────┐       ┌──────────┐       ┌──────────┐  
    │ Design A │       │ Design B │       │ Design C │  
    │ (Toggle) │       │ (Slider) │       │ (Menu)   │  
    └────┬─────┘       └────┬─────┘       └────┬─────┘  
         │                  │                   │  
         └──────────────────┼───────────────────┘  
                            │  
                      Scegliete il migliore  
                            │  
                            ▼

                      Merge con main

Ogni worktree è isolata, ogni Agent Team lavora indipendentemente, e voi scegliete il risultato migliore senza rischio.

#### **Errori Comuni con le Worktrees**

1. Non usare le worktrees per esperimenti rischiosi: se state per fare qualcosa di cui non siete sicuri, createne una. Il costo è zero, il beneficio è enorme.  
2. Dimenticare di cancellare le worktrees inutilizzate: le worktrees occupano spazio su disco. Cancellate quelle che non vi servono più.  
3. Fare merge senza testare: prima di fare merge con il main, testate SEMPRE la worktree. Un merge di codice rotto nel main è esattamente il problema che le worktrees dovrebbero prevenire.  
4. Non avere regole per le worktrees nel CLAUDE.md: se usate regolarmente le worktrees, codificate le regole nel CLAUDE.md così Claude sa come comportarsi.

# 

# 

# **CAPITOLO 38**

## **Deployment e Monetizzazione**

### **38.1 — Il Concetto di Deployment**

#### **Definizione del Concetto**

Il deployment (distribuzione) è il processo di rendere il vostro progetto o le vostre skill accessibili al mondo esterno — non più solo sul vostro computer locale, ma disponibili tramite un URL pubblico che chiunque può visitare. È il passo che trasforma un progetto locale in un prodotto utilizzabile e potenzialmente monetizzabile.

#### **Spiegazione Approfondita**

La guida introduce il deployment con una spiegazione chiara:

*"Quando mettiamo le cose nel web, quindi le mettiamo nel cloud, quello che stiamo facendo è semplicemente creare la nostra API o creare un endpoint, che non è altro che un URL, quindi un [https://blablabla](https://blablabla/), al quale le persone possono accedere se hanno questo URL. Quindi quello che stiamo facendo è semplicemente mettere a disposizione degli altri una cosa che abbiamo creato noi."*

text

DEPLOYMENT: DA LOCALE A GLOBALE  
═══════════════════════════════

PRIMA DEL DEPLOYMENT:  
┌─────────────────────────────────────────────┐  
│ IL VOSTRO COMPUTER                          │  
│                                             │  
│ ┌──────────────────────────────────────┐      
│ │ La vostra skill / app / workflow     │    │  
│ │                                      │    │  
│ │ Accessibile SOLO da voi              │    │  
│ │ Funziona SOLO quando il PC è acceso  │    │  
│ │ Nessun altro può usarla              │    │  
│ └──────────────────────────────────────┘    │  
└─────────────────────────────────────────────┘

DOPO IL DEPLOYMENT:  
┌─────────────────────────────────────────────┐  
│ IL CLOUD (Modal / Vercel / etc.)            │  
│                                             │  
│ ┌──────────────────────────────────────┐    │  
│ │ La vostra skill / app / workflow     │    │  
│ │                                      │    │  
│ │ URL: https://giovanni.modal.run      │    │  
│ │                                      │    │  
│ │ Accessibile da CHIUNQUE con il link  │    │  
│ │ Funziona 24/7 (server nel cloud)     │    │  
│ │ Può essere monetizzata               │    │  
│ └──────────────────────────────────────┘    │  
│                                             │  
│ ← Voi   ← Clienti   ← Team   ← Mondo        │

└─────────────────────────────────────────────┘

### **38.2 — Deployment di Skill nel Cloud con Modal**

#### **Definizione del Concetto**

Modal è la piattaforma di deployment che l'autore della guida preferisce e utilizza per portare le proprie skill nel cloud. Modal permette di creare cloud functions — funzioni che girano su server remoti e sono accessibili tramite URL pubblici.

#### **Spiegazione Approfondita**

La guida mostra il processo completo di deployment di una skill (il LinkedIn Post Generator) su Modal:

text

PROCESSO DI DEPLOYMENT SU MODAL  
════════════════════════════════

PASSO 1: Creare un Account Modal  
─────────────────────────────────  
• Andate su modal.com  
• Sign in con Google  
• Completate la registrazione  
• Riceverete due righe di autenticazione da copiare

PASSO 2: Collegare Modal a Claude Code  
───────────────────────────────────────  
• Copiate le due righe di autenticazione  
• Incollatele in Claude Code  
• "Connettimi a Modal"  
• Claude configura la connessione

PASSO 3: Creare un Token API  
─────────────────────────────  
• Nella dashboard Modal → Token  
• "New API Token"  
• Dategli un nome descrittivo  
• Copiate il token

PASSO 4: Chiedere a Claude di Fare il Deployment  
─────────────────────────────────────────────────  
"Ho una skill nella cartella .claude/skills che mi   
 permette di creare dei post LinkedIn. Vorrei creare   
 una mia API, quindi avere un mio URL che posso   
 premere e avere questa skill accessibile nel web.  
 Vorrei che questo fosse accessibile non solo a me   
 ma a tutti. Per farlo, vorrei utilizzare Modal.  
 L'URL al mio Modal è \[link\].  
 Per favore entraci e creami una cloud function.  
 Una volta che hai fatto, fammi vedere l'URL."

PASSO 5: Claude Esegue il Deployment  
─────────────────────────────────────  
• Claude crea la cloud function su Modal  
• Configura l'interfaccia web  
• Pubblica il servizio  
• Restituisce l'URL pubblico

RISULTATO:  
──────────  
URL: https://giovanni-beggiato--linkedin-post-generator.modal.run  
Accessibile da: chiunque con il link

Funzionalità: generare LinkedIn post nel vostro stile

#### **L'Interfaccia Web Risultante**

L'autore mostra l'interfaccia web generata dal deployment:

INTERFACCIA WEB DEL LINKEDIN POST GENERATOR  
════════════════════════════════════════════

┌─────────────────────────────────────────────┐  
│ Giovanni's LinkedIn Post Generator          │  
│                                             │  
│ Topic: \[                                  \] │  
│ "Quanto importante è utilizzare Claude Code │  
│  nel futuro"                                │  
│                                             │  
│ Paste from another author: \[              \] │  
│ (opzionale)                                 │  
│                                             │  
│ Style: \[Storytelling ▼\]                     │  
│                                             │  
│ Include CTA: \[No ▼\]                         │  
│                                             │  
│ \[    GENERATE POST    \]                     │  
│                                             │

└─────────────────────────────────────────────┘

L'utente compila i campi, preme "Generate Post" e riceve un LinkedIn post generato nel stile dell'autore. Tutto avviene nel cloud, senza bisogno che il computer dell'autore sia acceso.

#### **Verifica del Deployment su Modal**

Dopo il deployment, l'autore verifica nella dashboard di Modal:

*"Vediamo che qui abbiamo fatto una chiamata adesso, che è l'ultima che abbiamo fatto. Mezzanotte, 9 secondi. Quindi vediamo che è stata chiamata."*

La dashboard mostra:

* Ogni chiamata effettuata al servizio  
* Il tempo di esecuzione (9 secondi)  
* Le chiamate di inizializzazione  
* I log per il debugging

### **38.3 — Il Modello di Monetizzazione End-to-End**

#### **Definizione del Concetto**

La monetizzazione end-to-end è il processo completo di creare un servizio basato su Claude Code, deployarlo nel cloud e renderlo a pagamento. La guida mostra tutti i pezzi necessari: frontend, backend, autenticazione, pagamento e deployment.

#### **Spiegazione Approfondita**

L'autore collega esplicitamente il deployment alla monetizzazione, mostrando come tutti i pezzi costruiti durante il corso si assemblano in un prodotto vendibile:

ARCHITETTURA DI MONETIZZAZIONE END-TO-END  
══════════════════════════════════════════

PEZZO 1: FRONTEND (costruito nella Parte 4\)  
├── Interfaccia utente (HTML/CSS/JS)  
├── Form di registrazione  
├── Form di login  
└── Interfaccia del servizio

PEZZO 2: AUTENTICAZIONE (costruita nella Parte 4\)  
├── Supabase come backend  
├── Email \+ password login  
├── Gestione utenti  
└── Tracking utenti attivi/inattivi

PEZZO 3: PAGAMENTO (costruito nella Parte 4\)  
├── Stripe integration  
├── Piano gratuito \+ Piano Pro  
├── Abbonamento mensile  
├── Gestione status pagamento

PEZZO 4: SERVIZIO (costruito nella Parte 8\)  
├── Skill personalizzata  
├── Script deterministici  
├── Reference data di qualità  
└── Self-healing

PEZZO 5: DEPLOYMENT (costruito nella Parte 10\)  
├── Modal per le cloud function  
├── Vercel per il frontend (se necessario)  
├── GitHub per il version control  
└── URL pubblico accessibile

ASSEMBLAGGIO:  
─────────────  
Utente arriva → Si registra (Supabase) → Paga (Stripe)  
    → Accede al servizio → Usa la skill → Riceve il risultato

    → Tutto funziona 24/7 nel cloud

#### **L'Esempio di Business Reale dalla Guida**

L'autore fornisce un esempio di business reale in cui questo modello è stato applicato:

*"Facciamo un esempio che abbiamo uno scraper molto specializzato nel trovare lead in Google Maps, magari con criteri particolari, che sono appena — che hanno magari appena aperto — quindi magari vediamo chi appare in Google Maps negli ultimi 50 giorni."*

*"Questo l'ho fatto per esempio per un business in Francia in cui vendono brochure per televisori nelle varie cliniche. Era molto importante per loro capire quali erano le cliniche che avevano appena aperto, potenzialmente entro due settimane, perché questo permetteva a loro di andare direttamente ad offrire già il loro monitor."*

In questo esempio:

* Il servizio: uno scraper specializzato (skill con script deterministici)  
* Il valore per il cliente: identificare nuove cliniche in anticipo rispetto alla concorrenza  
* Il deployment: accessibile via URL, il cliente inserisce i criteri e riceve i risultati  
* La monetizzazione: abbonamento mensile tramite Stripe

Il percorso completo è:

CASO STUDIO: SCRAPER PER CLINICHE  
═════════════════════════════════

1\. Creare la skill (scraper Google Maps)  
2\. Testare localmente che funzioni  
3\. Fare deployment su Modal  
4\. Aggiungere autenticazione (Supabase)  
5\. Aggiungere pagamento (Stripe)  
6\. Dare il link al cliente  
7\. Il cliente paga → accede → usa il servizio  
8\. Voi incassate ricorrente ogni mese

INVESTIMENTO: qualche ora di sviluppo \+ \~€20 di API  
RICAVO: abbonamento mensile dal cliente

ROI: potenzialmente infinito (costo marginale quasi zero)

### **38.4 — Le Piattaforme di Deployment**

#### **Definizione del Concetto**

Esistono diverse piattaforme su cui potete fare deployment dei vostri progetti. La guida menziona specificamente Modal, Vercel e GitHub Actions come le tre opzioni principali.

#### **Confronto delle Piattaforme**

| Piattaforma | Ideale Per | Caratteristiche Chiave |
| ----- | ----- | ----- |
| Modal | Cloud functions, skill, API, workflow | Serverless, pay-per-use, deployment di script Python |
| Vercel | Frontend, siti web, web app | Ottimo per Next.js, deploy automatico da GitHub, hosting web |
| GitHub Actions | CI/CD, automazioni, test | Esegue workflow automatici su push/merge, gratuito per repo pubbliche |

#### **Quando Usare Quale**

ALBERO DECISIONALE PER LA PIATTAFORMA  
═════════════════════════════════════

Cosa state deployando?  
│  
├── Una SKILL o un'API → MODAL  
│   └── Es: LinkedIn Post Generator come servizio  
│   └── Es: Scraper come servizio  
│   └── Es: Qualsiasi workflow backend  
│  
├── Un SITO WEB o una WEB APP → VERCEL  
│   └── Es: Il sito aziendale  
│   └── Es: L'app Trello clone con frontend  
│   └── Es: Landing page con pagamento integrato  
│  
└── Un'AUTOMAZIONE che parte a evento → GITHUB ACTIONS  
    └── Es: Test automatici quando il codice cambia  
    └── Es: Deploy automatico quando fate merge  
    └── Es: Report automatici giornalieri

#### **Modal nel Dettaglio**

L'autore mostra familiarità specifica con Modal e ne illustra i vantaggi:

1. Serverless: non dovete gestire server. Il codice gira solo quando viene chiamato e pagate solo per il tempo di esecuzione.  
2. Facilità di deployment: un singolo prompt a Claude Code è sufficiente per fare deployment di una skill su Modal.  
3. URL pubblico automatico: Modal genera automaticamente un URL accessibile a chiunque.  
4. Dashboard di monitoraggio: potete vedere ogni chiamata, il tempo di esecuzione e i log.  
5. Costi contenuti: per la maggior parte dei casi d'uso, i costi sono nell'ordine di centesimi per chiamata.

#### **Vercel nel Dettaglio**

L'autore menziona Vercel come piattaforma per il deployment del suo sito web:

*"Andiamo a Vercel, che è anche il posto in cui alcune di queste cose verranno pubblicate."*

Vercel è ideale quando avete:

* Un frontend web (React, Next.js, etc.)  
* Bisogno di un hosting continuo (non solo a chiamata)  
* Integrazione con GitHub per deploy automatici

L'autore ha il suo sito ("Gentes") deployato su Vercel, e quando fa merge di una worktree, il deploy su Vercel è automatico.

### **38.5 — Il Percorso Completo di Monetizzazione**

#### **Definizione del Concetto**

Il percorso completo di monetizzazione è il cammino che va dalla competenza tecnica alla generazione di ricavo. La guida traccia questo percorso in modo molto chiaro, partendo dall'apprendimento di Claude Code fino alla vendita di servizi.

#### **Il Percorso dalla Guida**

L'autore delinea un percorso progressivo:

PERCORSO DI MONETIZZAZIONE  
═══════════════════════════

LIVELLO 1: PRINCIPIANTE  
────────────────────────  
• Impara Claude Code  
• Costruisce progetti semplici (siti web)  
• Usa le modalità base (ask before edits)  
• Risultato: competenza tecnica di base

LIVELLO 2: INTERMEDIO  
─────────────────────  
• Crea il proprio CLAUDE.md strutturato  
• Usa regole modulari  
• Usa sub-agenti  
• Costruisce applicazioni funzionali  
• Risultato: capacità di creare prodotti

LIVELLO 3: AVANZATO  
───────────────────  
• Crea skill personalizzate con reference data  
• Usa MCP strategicamente  
• Gestisce il contesto professionalmente  
• Fa deployment su cloud  
• Risultato: capacità di creare servizi vendibili

LIVELLO 4: ESPERTO  
──────────────────  
• Usa Agent Teams per task complesse  
• Implementa sistemi aziendali completi  
• Vende servizi di consulenza AI  
• Implementa sistemi in aziende terze

• Risultato: business redditizio

#### **Le Due Strade di Monetizzazione**

La guida presenta due strade principali:

Strada 1 — AI Agency / AI Consultancy:

*"Se studiare questo vi è piaciuto e pensate 'Ok, ora so costruire, come monetizzo?' — vi ho lasciato un link sotto che è il link al one-to-one coaching program con me per chi di voi avesse voglia di aprire un'AI agency o di fare AI consultancy."*

Questa strada prevede:

* Vendere servizi di implementazione Claude Code ad aziende  
* Creare sistemi personalizzati per clienti  
* Offrire consulenza sull'ottimizzazione dei workflow  
* Costruire skill personalizzate per settori specifici

Strada 2 — Imprenditore con AI:

*"Se siete un imprenditore, potete mandare una mail sotto ed è la mail mia personale."*

Questa strada prevede:

* Usare Claude Code per il proprio business  
* Automatizzare processi interni  
* Creare prodotti SaaS basati su skill  
* Ridurre costi operativi con automazione

#### **L'Equazione del Valore**

L'autore fornisce numeri concreti che illustrano il valore di Claude Code come competenza professionale:

EQUAZIONE DEL VALORE  
════════════════════

COSTO:  
• Piano Pro Claude: $17/mese  
• Piano Max Claude: $100/mese  
• Costi aggiuntivi (API, deployment): variabile

VALORE PRODOTTO:  
• "Questi $17 vi daranno un ROI in termini di qualsiasi   
   cosa MOSTRUOSO perché questo sostanzialmente equivale   
   ad avere un software developer in tasca."

CONFRONTO:  
• Software developer junior: €30.000-50.000/anno  
• Claude Code Pro: €204/anno ($17 × 12\)  
• Rapporto: il software developer costa 150-250x di più

SERVIZI VENDIBILI:  
• Implementazione base: €200-500  
• Sistema personalizzato: €1.000-3.000  
• Implementazione enterprise: €5.000-15.000+

• Consulenza ricorrente: €500-2.000/mese

#### **Il Ruolo della Piattaforma Upwork**

L'autore menziona un dettaglio pratico per chi ha bisogno di completare le proprie competenze:

*"In Upwork, che è una piattaforma di terzi, trovate persone estremamente competenti che per €200-300 vi fanno un mega lavoro. Sono ovviamente indiani o pakistani quindi dovete parlare un minimo di inglese, ma sono persone estremamente competenti."*

Questo è rilevante per la sicurezza: l'autore raccomanda sempre di avere un controllo di sicurezza fatto da un professionista prima di mettere un sistema in produzione. Claude Code costruisce il sistema, ma la verifica di sicurezza umana è ancora fondamentale.

### **38.6 — Riepilogo Architetturale Completo**

#### **Il Disegno Completo**

La guida costruisce progressivamente un disegno architetturale che cresce capitolo dopo capitolo. Ecco la versione finale e completa:

ARCHITETTURA COMPLETA DI UN PROGETTO CLAUDE CODE  
═════════════════════════════════════════════════

LIVELLO ENTERPRISE (opzionale, per aziende grandi)  
┌─────────────────────────────────────────────────────────┐  
│ CLAUDE.md Enterprise                                    │  
│ ├── Permessi a livello di sistema                       │  
│ ├── Regole di sicurezza enterprise                      │  
│ └── Override globale su tutto                           │  
└─────────────────────────────────────────────────────────┘  
            │ (override)  
            ▼  
LIVELLO GLOBAL (\~/.claude/)  
┌─────────────────────────────────────────────────────────┐  
│ ├── CLAUDE.md Globale                                   │  
│ │   ├── Permessi globali                                │  
│ │   ├── Istruzioni di sicurezza globali                 │  
│ │   └── Stile e brand globali                           │  
│ ├── agents/ (sub-agenti globali)                          
│ │   ├── researcher.md                                   │  
│ │   ├── reviewer.md                                     │  
│ │   └── qa.md                                           │  
│ ├── skills/ (skill globali)                             │  
│ ├── rules/ (regole globali)                             │  
│ ├── settings.json (hooks globali)                       │  
│ └── .mcp.json (MCP globali, es: Chrome Dev Tool)        │  
└─────────────────────────────────────────────────────────┘  
            │ (si applica a tutti i progetti)  
            ▼  
LIVELLO LOCAL (progetto/.claude/)  
┌─────────────────────────────────────────────────────────┐  
│ ├── CLAUDE.md del Progetto                              │  
│ │   └── Conciso: what, how, why, do, don't              │  
│ ├── agents/ (sub-agenti del progetto)                   │  
│ ├── skills/ (skill del progetto)                        │  
│ │   └── \[nome-skill\]/                                   │  
│ │       ├── skill.md (orchestratore)                    │  
│ │       ├── scripts/ (codice deterministico)            │  
│ │       └── references/ (dati di riferimento)           │  
│ ├── rules/ (regole modulari)                            │  
│ │   ├── design-fidelity.md                              │  
│ │   ├── security.md                                     │  
│ │   └── screenshot-workflow.md                          │  
│ ├── settings.json (hooks \+ permessi locali)             │  
│ ├── .local.json (istruzioni personali, non condivise)   │  
│ └── .mcp.json (MCP del progetto)                        │  
└─────────────────────────────────────────────────────────┘  
            │  
            ▼  
COMPONENTI INIETTATI DA ANTHROPIC  
┌─────────────────────────────────────────────────────────┐  
│ ├── System Prompt (\~10% del contesto)                   │  
│ ├── System Tools (bash, read, write, edit, etc.)        │  
│ ├── Tool Calling                                        │  
│ └── Auto Memory (memory.md, auto\_memory.md)             │  
└─────────────────────────────────────────────────────────┘  
            │  
            ▼  
CONTESTO DELLA SESSIONE  
┌─────────────────────────────────────────────────────────┐  
│ ├── Tutto quanto sopra viene caricato qui               │  
│ ├── \+ i vostri messaggi                                 │  
│ ├── \+ le risposte di Claude                             │  
│ ├── \+ Autocompact Buffer (\~33K token riservati)         │  
│ └── \= La vostra finestra di lavoro                      │  
└─────────────────────────────────────────────────────────┘  
            │  
            ▼  
DEPLOYMENT (rendere accessibile al mondo)  
┌─────────────────────────────────────────────────────────┐  
│ ├── Modal: cloud functions, API, skill deployate        │  
│ ├── Vercel: frontend, siti web, web app                 │  
│ ├── GitHub: version control, collaborazione             │  
│ ├── GitHub Actions: CI/CD, automazioni                  │  
│ ├── Supabase: backend, database, autenticazione         │  
│ └── Stripe: pagamenti, abbonamenti                      │

└─────────────────────────────────────────────────────────┘

Questo disegno rappresenta il quadro completo di come un progetto Claude Code professionale è strutturato, dalla configurazione di base fino al deployment e alla monetizzazione.

## **Riepilogo della Parte 10**

In questa Parte finale avete appreso:

1. Hooks: script deterministici che si attivano automaticamente a eventi specifici, senza consumo di token e con affidabilità garantita  
2. Hook sonoro: l'esempio base per essere notificati quando Claude finisce una task, risparmiando potenzialmente ore di attesa  
3. Hook aziendali: automazioni come l'invio automatico di email di onboarding quando un lead entra nel CRM  
4. La differenza fondamentale tra hook e workflow LLM: gli hook sono deterministici, gratuiti, istantanei e affidabili; i workflow LLM sono non deterministici, costosi, più lenti e potenzialmente inaffidabili  
5. Auto Memory: il meccanismo che permette a Claude di salvare e recuperare informazioni tra sessioni diverse attraverso file fisici (memory.md, auto\_memory.md)  
6. Il pattern "Salva e Continua": salvare lo stato del progetto in memoria quando il contesto raggiunge il 60-70%, poi continuare in una nuova sessione con contesto fresco  
7. Git Worktrees: directory isolate che permettono di sperimentare in parallelo senza rischiare il progetto principale, con possibilità di merge se l'esperimento ha successo  
8. Deployment su Modal: il processo completo per portare una skill nel cloud e renderla accessibile tramite URL pubblico  
9. Il modello di monetizzazione end-to-end: frontend \+ autenticazione (Supabase) \+ pagamento (Stripe) \+ servizio (skill) \+ deployment (Modal/Vercel)  
10. L'architettura completa: dal livello enterprise al deployment, passando per global, local, componenti Anthropic e gestione del contesto

## **Riepilogo Generale del Manuale**

Avete completato il Manuale Completo di Claude Code per il Business. Ecco il percorso che avete fatto:

| Parte | Contenuto | Competenza Acquisita |
| ----- | ----- | ----- |
| 1 | Fondamenta e Panoramica | Sapete cosa è Claude Code e come scegliere il piano |
| 2 | Installazione e Configurazione | Sapete installare e configurare Claude Code |
| 3 | CLAUDE.md e Architettura | Sapete strutturare un progetto professionale |
| 4 | Costruire Progetti | Sapete costruire siti web e applicazioni complete |
| 5 | Modalità di Permesso | Sapete quando usare Plan Mode vs Bypass Permission |
| 6 | Context Management | Sapete gestire il contesto come un professionista |
| 7 | Sub-agenti e Agent Teams | Sapete delegare e parallelizzare con team di agenti |
| 8 | Sistema delle Skill | Sapete creare, importare e monetizzare skill |
| 9 | MCP | Sapete installare, gestire e ottimizzare gli MCP |
| 10 | Funzionalità Avanzate e Deployment | Sapete automatizzare, versionare e deployare |

Come dice l'autore della guida:

*"Alla fine sarete sicuramente nel top 10% delle persone che usano Claude Code."*

Con questo manuale, avete le basi per costruire qualsiasi cosa vogliate — e le competenze per trasformare quella costruzione in valore reale e monetizzabile.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - General|General Area]]
- [[Map - Saas|Saas Area]]
