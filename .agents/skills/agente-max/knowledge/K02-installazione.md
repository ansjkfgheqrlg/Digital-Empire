# MODULO KNOWLEDGE BASE

**K02-installazione.md** — Capitoli 5-8 | Installazione, IDE (VS Code/Antigravity), terminal, configurazione

## Riferimenti Correlati
- K01-fondamenta.md (per contesto generale)
- K05-permessi.md (per modalità permesso)

---

# **PARTE 2 — INSTALLAZIONE E CONFIGURAZIONE**

## **CAPITOLO 5: INSTALLAZIONE DI CLAUDE CODE VIA TERMINAL**

### **5.1 — Definizione del Concetto**

L'installazione di Claude Code è il processo attraverso il quale il software viene scaricato e integrato all'interno del sistema operativo del computer. Una volta installato, Claude Code ha accesso diretto a cartelle, file, documenti e a qualsiasi risorsa presente nel computer dell'utente.

### **5.2 — Spiegazione Espansa**

Il processo di installazione è sorprendentemente semplice e si compone di pochi passaggi sequenziali. Nonostante il Terminal possa sembrare intimidatorio per chi non ha esperienza tecnica, l'operazione è meccanica: si copia un comando, si incolla, si preme Enter.

Passaggio 1: Trovare il comando di installazione

* Andare su docs.anthropic.com (la documentazione ufficiale)  
* Cercare la sezione "Get Started"  
* Nella pagina troverete una serie di comandi per diversi sistemi operativi (Mac, Linux, Windows)  
* Il comando corretto per il vostro sistema operativo va copiato premendo il pulsante di copia accanto ad esso

Passaggio 2: Aprire il Terminal

* Su Mac: premere Command \+ Barra Spaziatrice (si apre Spotlight)  
* Digitare "terminal"  
* Premere Enter  
* Si apre la finestra del Terminal

Passaggio 3: Incollare ed eseguire il comando

* Nel Terminal, premere Command \+ V per incollare il comando copiato  
* Premere Enter  
* Attendere che l'installazione si completi

### **5.3 — Perché Questo Concetto È Importante**

L'installazione non è un semplice "download". Quando installate Claude Code nel vostro sistema, state dando al software accesso reale al vostro computer. Questo è un punto fondamentale da comprendere:

COSA SUCCEDE DOPO L'INSTALLAZIONE:

Claude Code ottiene accesso a:  
├── Cartelle del computer  
├── Documenti  
├── File condivisi  
├── Terminal (per eseguire comandi)  
├── Capacità di leggere qualsiasi file  
├── Capacità di modificare qualsiasi file  
├── Capacità di creare nuovi file

└── Capacità di cancellare file (in Bypass Permission)

Questo è esattamente ciò che rende Claude Code così potente — e anche il motivo per cui le modalità di permesso (che vedremo nel Capitolo 17\) sono così importanti. Claude Code non è un'applicazione isolata in una sandbox: opera nel vostro ambiente reale.

### **5.4 — Interpretazione Pratica**

Il comando non è immediato. L'autore avverte esplicitamente: *"Come vedete anche il comando non è immediato. Cosa vuol dire? Che ci metterà un po' prima di installarlo, e quindi non preoccupatevi se dopo avere premuto Enter magari avete 3-4 secondi, 10 di awkward silence, perché non ci interessa."*

Questo è un dettaglio importante perché molte persone, soprattutto i principianti, premono Enter e vedendo che non succede nulla immediatamente, pensano di aver sbagliato qualcosa. Non è così. L'installazione richiede tempo perché sta scaricando e configurando diversi componenti nel sistema.

Dopo l'installazione — prima esecuzione:

1. Pulire il Terminal digitando clear e premendo Enter  
2. Digitare claude e premere Enter  
3. Comparirà un messaggio di sicurezza: "Quick safety check" — rispondere Sì  
4. A questo punto appare il logo di Claude Code (che l'autore descrive come un granchio o una medusa)  
5. Vengono mostrate le informazioni di sessione

### **5.5 — Meccanismo Sottostante**

Quando Claude Code viene avviato per la prima volta, vengono visualizzate diverse informazioni nella schermata iniziale:

╔════════════════════════════════════════╗  
║         \[Logo Claude Code\]             ║  
║                                        ║  
║  Modello: Opus / Sonnet (a seconda     ║  
║           del piano)                   ║  
║                                        ║  
║  Piano: Free / Pro / Max               ║  
║                                        ║  
║  Path: /percorso/della/cartella/       ║  
║        corrente                        ║  
║                                        ║  
╚════════════════════════════════════════╝

\> \[barra del prompt \- qui si scrive\]

Modello: Indica quale modello di linguaggio è in uso (Opus è il più potente, Sonnet è più veloce ma meno capace per task complesse).

Piano: Conferma il tipo di abbonamento attivo.

Path: Mostra in quale cartella del computer vi trovate. Questo è critico perché Claude Code lavora nella cartella in cui viene avviato. Se lo avviate dalla cartella Desktop, avrà accesso ai file del Desktop. Se lo avviate dalla cartella di un progetto specifico, lavorerà su quel progetto.

### **5.6 — Errori Comuni**

Errore 1: Avviare Claude Code dalla cartella sbagliata  
Se avviate Claude Code dal Desktop ma il vostro progetto è in Documents/MioProgetto, Claude Code non vedrà automaticamente i file del progetto. Dovete prima navigare nella cartella corretta usando il comando cd (change directory) nel Terminal, oppure aprire il Terminal direttamente dalla cartella del progetto.

Errore 2: Non completare il safety check  
Il messaggio "Quick safety check" richiede una conferma esplicita. Se lo ignorate o chiudete il Terminal a questo punto, l'inizializzazione non si completa.

Errore 3: Panico durante l'attesa dell'installazione  
L'installazione richiede tempo. Non chiudete il Terminal, non premete Ctrl+C, non fate nulla. Aspettate che il processo si completi da solo.

Errore 4: Usare il comando di installazione sbagliato per il proprio sistema operativo  
La documentazione fornisce comandi diversi per Mac, Linux e Windows. Assicuratevi di copiare quello corretto per il vostro sistema operativo.

### **5.7 — Insight Avanzato**

Quando interagite con Claude Code nel Terminal, noterete diversi elementi visivi:

Indicatori di pensiero: Quando Claude sta elaborando una risposta, vedrete parole come "harmonizing", "thinking", "cogitating", "looping", "noodling". Queste sono etichette casuali (e personalizzabili) che indicano semplicemente che il modello sta processando la richiesta. Non hanno significato specifico — servono solo a comunicare "sto pensando, attendi".

Distinzione input/output: Il vostro input (ciò che scrivete) è preceduto da un rettangolino/indicatore visivo. La risposta di Claude non ha questo indicatore. Questo vi permette di distinguere immediatamente chi ha scritto cosa nella conversazione.

Informazioni di sessione nella barra inferiore (Status Line):

┌─────────────────────────────────────────────────────┐  
│ Context: 14% used │ Cost: $0.03 │ Tokens: 28K/200K │ Session: 5m │

└─────────────────────────────────────────────────────┘

* Context % used: La percentuale di contesto totale utilizzata. Questa è una delle metriche più importanti da monitorare (approfondita nel Capitolo 20-22)  
* Cost: Il costo stimato dell'interazione se si fosse sul piano API. Per chi usa un piano subscription, è solo informativo  
* Tokens: Il totale di token utilizzati rispetto al massimo disponibile  
* Session duration: Da quanto tempo è attiva la sessione corrente

Nota importante dell'autore: Il numero di token totali e il contesto utilizzato non sono la stessa cosa. La ragione sarà spiegata nei capitoli dedicati al context management, ma per ora è sufficiente sapere che sono due metriche correlate ma distinte.

### **5.8 — Contesto Applicato: Cos'è un Token?**

L'autore fornisce una definizione semplificata ma pratica: *"Per questo corso, dato che non voglio andare troppo nei tecnicismi, pensate ad un token come una parola. In realtà non lo è — sarebbero tre-quattro lettere — ma per semplicità potete pensarlo così."*

Per essere più precisi (senza eccedere nei tecnicismi):

APPROSSIMAZIONE PRATICA:

1 token ≈ 3-4 caratteri in inglese  
1 token ≈ 0.75 parole in inglese  
1 token ≈ 0.5-0.6 parole in italiano (l'italiano è più "costoso" in token)

Esempi:  
"Ciao" \= 1-2 token  
"Buongiorno, come stai oggi?" \= \~8-10 token  
Un prompt di 200 parole ≈ 300-400 token

Un file di codice di 500 righe ≈ 5.000-15.000 token

I token sono l'unità di misura fondamentale perché:

* Il contesto disponibile è misurato in token (es. 200.000 token)  
* Il costo del piano API è calcolato per token  
* La qualità delle risposte degrada quando il contesto si riempie di token  
* Ogni file letto, ogni prompt scritto, ogni risposta generata consuma token

## **CAPITOLO 6: GLI IDE — VS CODE E ANTIGRAVITY**

### **6.1 — Definizione del Concetto**

Un IDE (Integrated Development Environment), in italiano "Ambiente di Sviluppo Integrato", è un software che fornisce un'interfaccia visiva completa per lavorare su progetti. Un IDE tipicamente include: un esploratore di file (per navigare la struttura del progetto), un editor di testo (per modificare i file), un terminal integrato, e — nel nostro caso — l'integrazione con Claude Code.

### **6.2 — Spiegazione Espansa**

Per utilizzare Claude Code con un'interfaccia visiva (anziché solo dal Terminal), servono questi IDE. Il mercato attualmente si concentra su due opzioni principali.

#### **6.2.1 — VS Code (Visual Studio Code)**

Produttore: Microsoft  
Download: Cercare "Visual Studio Code Download" su Google, primo risultato  
Status: L'IDE storico, consolidato, utilizzatissimo. L'autore lo definisce "l'OG" (Original Gangster — il primo, quello storico)  
Interfaccia: Più rigida e meno pulita rispetto ad Antigravity

Struttura dell'interfaccia VS Code:

┌──────────────────────────────────────────────────┐  
│  \[Barra superiore \- Menu\]                        │  
├────────────┬─────────────────────────────────────┤  
│            │                                     │  
│  EXPLORER  │     AREA EDITOR                     │  
│            │     (visualizzazione/modifica file) │  
│  📁 src    │                                     │  
│  📁 public │                                     │  
│  📄 index  │                                     │  
│  📄 cloud  │                                     │  
│            │                                     │  
│            │                                     │  
├────────────┴─────────────────────────────────────┤  
│  \[Terminal integrato / Claude Code panel\]        │

└──────────────────────────────────────────────────┘

L'Explorer (pannello sinistro) è semplicemente una rappresentazione visiva della cartella del progetto. Tutto ciò che vedete nell'Explorer corrisponde esattamente ai file e cartelle presenti fisicamente nel vostro computer. L'autore lo dimostra aprendo la stessa cartella nel Finder del Mac e mostrando che il contenuto è identico.

Come aprire un progetto in VS Code:

1. Avviare VS Code  
2. Premere l'icona in alto a sinistra  
3. Selezionare "Open Folder"  
4. Navigare fino alla cartella del progetto  
5. Premere "Open"

Come installare Claude Code in VS Code:

1. Premere l'icona delle estensioni (nella barra laterale sinistra — sembra un gruppo di blocchi/quadrati)  
2. Nella barra di ricerca digitare "Claude Code"  
3. Premere "Install"  
4. Una volta installato, appare un'icona a stella nella barra laterale  
5. Premere l'icona stella per aprire il pannello Claude Code

#### **6.2.2 — Antigravity**

Produttore: Google  
Data di lancio: Circa novembre 2025  
Download: Cercare "Antigravity Google Download" su Google  
Interfaccia: Più pulita, moderna, con animazioni che seguono il mouse  
Preferenza dell'autore: Preferito rispetto a VS Code

Struttura dell'interfaccia Antigravity:

┌──────────────────────────────────────────────────────────────┐  
│  \[Barra superiore \- Menu \+ Impostazioni ⚙️\]                  │  
├────────────┬──────────────────────────┬──────────────────────┤  
│            │                          │                      │  
│  EXPLORER  │    AREA EDITOR           │  PANNELLO AGENTE     │  
│            │    (visualizzazione/     │  (Chat con AI)       │  
│  📁 src    │     modifica file)       │                      │  
│  📁 .cloud │                          │  Modelli disponibili:│  
│  📄 index  │                          │  • Google (Gemini)   │  
│  📄 CLAUDE │                          │  • Claude Code       │  
│            │                          │  • GPT               │  
│            │                          │                      │  
├────────────┴──────────────────────────┴──────────────────────┤  
│  \[Terminal integrato\]                                        │

└──────────────────────────────────────────────────────────────┘

Differenza chiave: Antigravity ha un pannello agente sulla destra che permette di chattare con diversi modelli AI — non solo Claude Code, ma anche i modelli di Google (Gemini) e GPT. Questo è perché Google, avendo sviluppato Antigravity, spinge naturalmente i propri modelli rendendoli disponibili di default.

Come installare Claude Code in Antigravity:

1. Premere l'icona delle estensioni  
2. Cercare "Claude Code"  
3. Premere "Install"  
4. Accesso rapido: Command \+ Shift \+ ESC (apre Claude Code direttamente)  
5. Alternativa: premere l'icona stella nella barra laterale

### **6.3 — Perché Questo Concetto È Importante**

La scelta dell'IDE determina il vostro workflow quotidiano. Entrambi gli IDE funzionano allo stesso modo con Claude Code, ma ci sono sfumature pratiche:

Antigravity è preferibile quando:

* Lavorate molto sul frontend (design, interfaccia visiva)  
* Volete avere accesso a più modelli AI nella stessa interfaccia  
* Preferite un'interfaccia più moderna e pulita  
* Volete sfruttare i modelli Google per compiti specifici

VS Code è preferibile quando:

* Avete già familiarità con esso  
* Avete estensioni specifiche installate che non esistono su Antigravity  
* Lavorate in un team che usa VS Code come standard

La strategia dell'autore:  
L'autore utilizza una divisione specifica del lavoro tra i modelli disponibili:

* Codice backend (logica, server, database) → Claude Code  
* Codice frontend (design, interfaccia utente) → Modelli Google in Antigravity

Questa strategia può essere codificata nel CLAUDE.md in modo che il sistema scelga automaticamente il modello appropriato per il tipo di task.

### **6.4 — Meccanismo Sottostante: Il Concetto di Workspace/Cartella**

Un punto fondamentale che l'autore sottolinea con forza è che la cartella è ciò che conta, non l'IDE:

STESSO PROGETTO, VISUALIZZATO IN MODI DIVERSI:

Cartella fisica sul computer:  
📁 company-website/  
├── 📁 src/  
├── 📁 public/  
├── 📄 index.html  
├── 📄 CLAUDE.md  
├── 📁 .claude/  
└── 📄 package.json

Questa STESSA cartella appare identica in:  
• VS Code (Explorer panel a sinistra)  
• Antigravity (Explorer panel a sinistra)  
• Terminal (comando 'ls' per listare i file)

• Finder/File Manager del computer

Se modificate un file tramite Claude Code in VS Code, la modifica è visibile anche in Antigravity se aprite la stessa cartella, e viceversa. L'IDE è solo una "finestra" attraverso la quale guardate e lavorate sulla stessa cartella.

### **6.5 — Dettaglio Pratico: Il File in Contesto**

Quando Claude Code è aperto in un IDE, nella parte superiore del pannello chat viene mostrato il nome del file attualmente visualizzato nell'editor. Per esempio, se state guardando il file package.json, vedrete un'indicazione come package.json accanto ai vari pulsanti.

L'autore spiega che questo è il file che Claude Code sta attualmente "guardando". Se chiedete *"Che tipo di file stai guardando in questo momento?"*, Claude risponderà con il nome di quel file.

Implicazione pratica: Quando scrivete un prompt che si riferisce a "questo file" o "il file corrente", Claude Code interpreta la richiesta nel contesto del file mostrato. Se volete modificare un file specifico, assicuratevi di averlo aperto nell'editor prima di dare l'istruzione.

### **6.6 — Errori Comuni**

Errore 1: Non accettare le modifiche proposte da Claude Code  
Quando Claude Code propone una modifica a un file, questa viene mostrata come una "diff" (differenza tra la versione originale e quella proposta). Se salvate il file senza accettare esplicitamente le modifiche, il file viene duplicato anziché modificato. L'autore ha mostrato questo accidentalmente durante il corso: *"Se poi io ora lo salvassi senza accettare questi cambiamenti, vedete che me l'ha semplicemente duplicato."*

La regola è: sempre accettare o rifiutare esplicitamente le modifiche proposte prima di procedere.

Errore 2: Non configurare il Dangerously Skip Permission  
La modalità bypass permission (che verrà approfondita nel Capitolo 19\) non è attiva di default. Per abilitarla:

In VS Code:

1. Premere l'icona ingranaggio (⚙️)  
2. Selezionare "Settings"  
3. Cercare "Claude"  
4. Abilitare "Allow Dangerously Skip Permission"

In Antigravity:

1. Premere la rotellina/ingranaggio in alto a destra (posizione diversa da VS Code)  
2. Selezionare "Settings"  
3. Cercare "Claude Code"  
4. Abilitare "Dangerously Skip Permission"

Nota: la posizione dell'ingranaggio è diversa nei due IDE. In VS Code è nella barra laterale, in Antigravity è in alto a destra.

Errore 3: Confondere le modalità di interazione  
In entrambi gli IDE, Claude Code offre diverse modalità nella parte superiore del pannello:

| Modalità | Comportamento |
| ----- | ----- |
| Ask before edits | Claude propone le modifiche e chiede approvazione prima di applicarle |
| Edit automatically | Claude applica le modifiche automaticamente (tranne creazione/cancellazione file) |
| Plan mode | Claude crea un piano strutturato e chiede approvazione prima di eseguirlo |
| Bypass permission | Claude fa tutto in autonomia: crea, modifica, cancella file senza chiedere |

La confusione tra queste modalità è molto comune e può portare a risultati inattesi (Claude che modifica file senza il vostro consenso, o al contrario Claude che si ferma continuamente a chiedere permessi rallentando il workflow).

### **6.7 — Insight Avanzato**

Indicatore "U" (Updated):  
Quando un file viene modificato da Claude Code, nell'Explorer dell'IDE appare una lettera "U" accanto al nome del file. Questa indica che il file è stato aggiornato rispetto alla sua versione precedente. È un indicatore visivo utile per sapere immediatamente quali file sono stati toccati durante una sessione di lavoro.

La portabilità del progetto:  
Poiché il progetto vive nella cartella e non nell'IDE, potete:

* Iniziare un progetto in VS Code e continuarlo in Antigravity  
* Lavorare dal Terminal e poi visualizzare i risultati nell'IDE  
* Condividere la cartella del progetto con un collaboratore che usa un IDE diverso  
* Caricare la cartella su GitHub e scaricarla su un altro computer

Tutto funzionerà perché le configurazioni di Claude Code (CLAUDE.md, cartella .claude, regole, skill) sono tutte contenute nella cartella del progetto stessa.

## **CAPITOLO 7: IL TERMINAL COME INTERFACCIA AVANZATA**

### **7.1 — Definizione del Concetto**

Il Terminal è un'interfaccia a riga di comando che permette di interagire con il computer digitando comandi testuali anziché cliccando su bottoni e icone. Nel contesto di Claude Code, il Terminal è l'interfaccia più potente e completa, quella che sblocca tutte le funzionalità avanzate.

### **7.2 — Spiegazione Espansa**

L'autore è molto chiaro su questo punto: nonostante il Terminal possa sembrare intimidatorio, è l'interfaccia raccomandata per chi vuole sfruttare Claude Code al massimo delle sue capacità. Le ragioni sono concrete:

Funzionalità esclusive del Terminal:

1. Agent Teams — La funzionalità multi-agente collaborativo è disponibile solo da Terminal  
2. Analisi completa del contesto (/context) — Visione dettagliata di come il contesto è distribuito  
3. Configurazione avanzata (/config) — Accesso a tutte le impostazioni  
4. Gestione permessi granulare — Allow, Ask, Deny per tool specifici  
5. Status Line completa — Barra informativa con contesto, costi, token, durata sessione  
6. Navigazione tra modalità con shortcut — Shift+Tab per passare tra le modalità

Come avviare Claude Code dal Terminal:

Avvio standard:  
$ claude

Avvio con bypass permission (YOLO mode):  
$ claude \--dangerously-skip-permissions

Nota: l'autore usa l'alias "YOLO" (You Only Live Once)

per abbreviare questo comando nel suo setup personale

### **7.3 — Perché Questo Concetto È Importante**

Il Terminal è dove si effettua la transizione da "utente base" a "utente avanzato" di Claude Code. Molte delle operazioni più potenti e produttive — Agent Teams, analisi del contesto, gestione MCP — richiedono il Terminal.

L'autore lo esprime con una frase importante: *"Il motivo per cui vi dico, magari se ce la fate, prendete familiarità piano alla volta con il terminal: sembra difficile all'inizio ma veramente non lo è."*

La parola chiave è "piano alla volta". Non serve imparare tutto il Terminal in un giorno. I comandi fondamentali sono pochissimi:

text

COMANDI TERMINAL ESSENZIALI PER CLAUDE CODE:

claude                              → Avvia Claude Code  
claude \--dangerously-skip-permissions → Avvia con bypass permission  
clear                               → Pulisce la schermata  
cd /percorso/cartella               → Cambia directory

ls                                  → Lista i file nella cartella corrente

Con questi cinque comandi potete fare il 90% di tutto ciò che serve nel Terminal per lavorare con Claude Code.

### **7.4 — Meccanismo Sottostante: Navigazione nel Terminal**

Quando Claude Code è attivo nel Terminal, avete accesso a due livelli di navigazione:

Livello 1: Comandi Slash  
Digitando / seguito da un comando, accedete a funzionalità specifiche di Claude Code:

text

/config    → Visualizza e modifica la configurazione  
/context   → Analizza la distribuzione del contesto  
/compact   → Compatta il contesto per liberare spazio  
/init      → Inizializza un nuovo progetto (crea CLAUDE.md)  
/mcp       → Gestisce i Model Context Protocol

/status    → Mostra lo stato della sessione corrente

Livello 2: Navigazione con tasti

* Shift \+ Freccia su \+ Tab: Visualizza le modalità di Claude Code (Accept edits, Plan mode, Bypass permission)  
* Frecce su/giù: Navigano tra le opzioni nella vista configurazione  
* Tab: Passa tra le sezioni (Config → Usage → Status)  
* ESC: Esce dalla vista corrente e torna al prompt

### **7.5 — Interpretazione Pratica: Il Comando /config**

Il comando /config è il primo comando avanzato che l'autore mostra. Quando lo eseguite, vedete tutte le impostazioni interne di Claude Code:

CONTENUTO DI /config:

Autocompact: \[ON/OFF\]  
  → Compatta automaticamente il contesto quando si riempie  
  → Fondamentale per il context management

Thinking Mode: \[ON/OFF\]  
  → Permette a Claude di "pensare" in modo estensivo  
  → Migliora la qualità delle risposte su task complesse

Rewind/Checkpoint: \[ON/OFF\]  
  → Salva checkpoint automatici del progetto  
  → Permette di tornare a versioni precedenti  
  → Se OFF, non potete fare rollback

Theme: \[personalizzabile\]  
  → Personalizzazione visiva del terminal

Status Line: \[ON/OFF\]  
  → La barra informativa in basso al terminal  
  → Mostra contesto, costi, token, durata

Teammate Mode: \[ON/OFF\]

  → Abilita la funzionalità Agent Teams

### **7.6 — Approfondimento: La Status Line**

La Status Line è la barra informativa che appare nella parte inferiore del Terminal quando Claude Code è attivo. L'autore la considera essenziale e mostra come attivarla.

Come attivare la Status Line:

Metodo 1: Comando diretto  
Nel prompt di Claude Code, digitare il comando specifico per la status line (disponibile nella configurazione) e premere Enter.

Metodo 2: Chiedere a Claude Code  
Se non riuscite a configurarla manualmente, l'autore suggerisce un approccio pragmatico e potente: fare uno screenshot della Status Line come appare nel video/tutorial, incollarlo nel Terminal, e chiedere a Claude: *"Ehi, per favore fa sì che io abbia sotto al terminal queste cose qui."* Claude Code configurerà tutto automaticamente.

Questa è una perla filosofica dell'autore: *"D'ora in poi la vostra vita sarà sempre alla distanza di un buon prompt da risolvere gran parte dei vostri problemi."*

Cosa mostra la Status Line:

┌────────────────────────────────────────────────────────────────┐  
│ 📊 14% used │ 💰 $0.03 │ 🔢 28,000/200,000 tokens │ ⏱ 5m 32s    
└────────────────────────────────────────────────────────────────┘

📊 Contesto utilizzato (%)  
   → La metrica più importante da monitorare  
   → Quando si avvicina al 100%, le performance degradano  
   → L'autocompact interviene automaticamente prima del 100%

💰 Costo stimato (API pricing)  
   → Quanto costerebbe l'interazione nel piano API  
   → Solo informativo per utenti con piano subscription  
   → Utile per capire il "peso" di ogni operazione

🔢 Token utilizzati / Token totali  
   → Quanti token sono stati consumati nella sessione  
   → Il totale dipende dal modello (es. 200K per alcuni, 1M per altri)

⏱ Durata sessione  
   → Da quanto tempo la sessione è attiva

   → Utile per gestire il tempo e pianificare i compact

### **7.7 — Errori Comuni**

Errore 1: Chiudere il Terminal durante un'operazione  
Se Claude Code sta eseguendo un'operazione (installazione, modifica file, ricerca), chiudere il Terminal interrompe bruscamente il processo. Questo può lasciare file in uno stato inconsistente.

Errore 2: Non usare /config per verificare le impostazioni  
Molti problemi (autocompact non attivo, checkpoint disabilitati, thinking mode spento) derivano da impostazioni non verificate. Eseguire /config come prima operazione in ogni nuova installazione è una best practice fondamentale.

Errore 3: Ignorare la Status Line  
Senza la Status Line, non avete visibilità sul consumo di contesto. Questo è come guidare senza il cruscotto: non sapete a che velocità andate, quanto carburante avete, o da quanto tempo state guidando. La Status Line è il vostro cruscotto di Claude Code.

### **7.8 — Insight Avanzato**

Il comando /config è navigabile:  
Quando eseguite /config, potete:

* Usare le frecce su/giù per scorrere le opzioni  
* Premere Tab per passare alla vista "Usage" (quanto avete utilizzato del modello, es. 28%)  
* Premere Tab ancora per passare alla vista "Status"  
* Premere ESC per uscire

Questo crea un flusso di navigazione:

/config → \[Configurazione\] \--Tab--\> \[Usage\] \--Tab--\> \[Status\] \--ESC--\> \[Prompt\]

Il concetto di Autocompact:  
L'Autocompact è una delle funzionalità più importanti di Claude Code e merita una spiegazione dettagliata qui perché si configura tramite /config.

L'autore spiega il concetto con un esempio vivido. Immaginate di aver scritto un prompt come questo:

*"Ciao, sono Giovanni, ho 30 anni, il mio compleanno è il 27 febbraio, quindi qualche giorno fa, mi piacciono le pentole, vivo a Lussemburgo..."*

In questo prompt, "mi piacciono le pentole" è informazione irrilevante che occupa contesto inutilmente. L'Autocompact fa esattamente questo: prende il contesto e ne aumenta la densità informativa, eliminando ciò che non è rilevante.

Il risultato dopo Autocompact sarebbe qualcosa come:

*"Giovanni, Lussemburgo, 30 anni, compleanno 27 febbraio"*

Stesse informazioni utili, frazione dello spazio. Questo processo avviene automaticamente quando il contesto si avvicina alla soglia critica (circa 33.000 token nel buffer di Autocompact, come verrà spiegato nel Capitolo 22).

## **CAPITOLO 8: CONFIGURAZIONE, STATUS LINE E COMANDI FONDAMENTALI**

### **8.1 — Definizione del Concetto**

La configurazione di Claude Code comprende tutti i parametri, le impostazioni e i comandi che determinano come il sistema si comporta, cosa monitora, e quali funzionalità sono attive. Una configurazione corretta è il prerequisito per un utilizzo efficiente e produttivo.

### **8.2 — Spiegazione Espansa: Mappa Completa dei Comandi**

L'autore introduce i comandi nel corso della guida in modo progressivo. Qui li raccogliamo tutti in una mappa organizzata per funzione:

#### **Comandi di Inizializzazione e Gestione Progetto**

/init  
├── Funzione: Inizializza un nuovo progetto Claude Code  
├── Cosa fa: Analizza i file presenti nella cartella,  
│           legge il codice esistente, comprende la struttura,  
│           e genera un CLAUDE.md strutturato secondo le best practice  
├── Quando usarlo: Sempre all'inizio di un nuovo progetto  
├── Quando è particolarmente utile:  
│   • Quando importate un progetto da qualcun altro  
│   • Quando il team vi manda script e risorse  
│   • Quando volete ricreare il CLAUDE.md dopo modifiche importanti  
└── Nota importante: Se avete impostazioni globali (\~/.claude),  
    il /init le incorpora automaticamente nel nuovo CLAUDE.md

L'autore sottolinea un vantaggio sottile ma potente di /init: se esiste un comando che rimanda a "come si crea un CLAUDE.md" per tutti i processi, quel file verrà strutturato in modo identico ogni volta. Questo crea standardizzazione: *"Tutti runnando quel comando abbiano lo stesso, e questo crea un'efficienza non da ridere."*

#### **Comandi di Context Management**

/context  
├── Funzione: Mostra un'analisi dettagliata della distribuzione del contesto  
├── Cosa mostra:  
│   • System prompt (injection di Anthropic) → \~10-12%  
│   • System tools → %  
│   • MCP tools → % (può essere molto alto\!)  
│   • Memory files → %  
│   • Skills → %  
│   • Custom agents → %  
│   • Messages (la conversazione) → %  
│   • Spazio libero → %  
└── Perché è critico: Permette di capire dove il contesto viene consumato  
    e identificare sprechi

/compact  
├── Funzione: Compatta manualmente il contesto della conversazione  
├── Cosa fa: Riscrive l'intera conversazione in formato ad alta densità  
│           (bullet point, eliminazione ridondanze, compressione)  
├── Esempio di compattazione:  
│   PRIMA: "Ho chiesto a Claude di importare i tre sub-agenti che sono  
│           il reviewer, il researcher e il QA. Poi ho chiesto di fare  
│           un review completo del codice..."  
│   DOPO:  "• Importati 3 sub-agenti: reviewer, researcher, QA  
│           • Review codice completato"  
├── Quando usarlo: Quando il contesto supera il 60-70%  
│                  o quando notate degradazione delle performance  
└── Nota: L'Autocompact fa la stessa cosa ma automaticamente  
         quando si raggiunge la soglia del buffer (\~33K token)

#### **Comandi di Gestione Sessione**

clear (nel prompt Claude)  
├── Funzione: Pulisce la conversazione corrente  
└── Nota: Non cancella la memoria o le configurazioni

clear context  
├── Funzione: Pulisce il contesto della conversazione  
└── Quando usarlo: Quando volete iniziare una nuova conversazione  
    mantenendo le configurazioni del progetto

#### **Comandi di Gestione MCP e Permessi**

/mcp  
├── Funzione: Gestisce i Model Context Protocol installati  
├── Cosa mostra: Lista degli MCP attivi e il loro stato  
└── Quando usarlo: Per verificare connessioni, autenticarsi,  
    o risolvere problemi con MCP

permissions (nel prompt di configurazione)  
├── Funzione: Gestisce i permessi dei tool  
├── Opzioni:  
│   • Allow: Il tool è sempre permesso (nessuna richiesta)  
│   • Ask: Chiede sempre permesso prima di usare il tool  
│   • Deny: Il tool non viene mai usato  
│   • Workspace: Permessi specifici per il workspace corrente  
└── Nota critica: I permessi dell'agente principale si replicano  
    a TUTTI i sotto-agenti (downstream)

### **8.3 — Perché Questo Concetto È Importante**

La configurazione non è un'operazione "una tantum". È un processo continuo di ottimizzazione che impatta direttamente sulla qualità del lavoro e sull'efficienza del sistema. Una configurazione subottimale porta a:

* Spreco di contesto (meno spazio per le informazioni utili)  
* Mancanza di visibilità sullo stato del sistema (senza Status Line)  
* Impossibilità di tornare a versioni precedenti (senza checkpoint)  
* Performance degradate (senza Autocompact o thinking mode)  
* Rischi di sicurezza (senza gestione appropriata dei permessi)

### **8.4 — Interpretazione Pratica: Checklist di Configurazione Iniziale**

Ogni volta che installate Claude Code o iniziate un nuovo progetto, questa è la sequenza di configurazione raccomandata:

CHECKLIST DI CONFIGURAZIONE INIZIALE:

□ 1\. Avviare Claude Code ($ claude)  
□ 2\. Eseguire /config e verificare:  
     □ Autocompact: ON  
     □ Thinking Mode: ON  
     □ Rewind/Checkpoint: ON  
□ 3\. Attivare la Status Line  
□ 4\. Eseguire /init per generare il CLAUDE.md  
□ 5\. Verificare i permessi con /permissions  
□ 6\. Controllare gli MCP con /mcp

□ 7\. Eseguire /context per avere una baseline del contesto

### **8.5 — Meccanismo Sottostante: La Funzione Rewind/Checkpoint**

Il Rewind/Checkpoint è una funzionalità che salva automaticamente "istantanee" del progetto durante il lavoro. L'autore la spiega così:

*"Rewind checkpoint vuol dire che ipotizziamo che eravamo contenti con una roba che abbiamo fatto ma ci siamo fregati e abbiamo scritto una cosa che ha mandato a monte tutto il resto. Per tornare indietro semplicemente diciamo: 'Ehi torna alla versione precedente.' Se fosse OFF non potremmo farlo."*

Questa funzionalità è particolarmente importante quando si lavora in bypass permission, dove Claude Code ha la libertà di creare e cancellare file autonomamente. Senza checkpoint, un errore potrebbe essere irreversibile (o almeno molto costoso da recuperare).

ESEMPIO DI FLUSSO CON CHECKPOINT:

Checkpoint 1: Progetto funzionante ✅  
     ↓  
Modifica A: Aggiunta feature X → tutto ok  
     ↓  
Checkpoint 2: Progetto con feature X ✅  
     ↓  
Modifica B: Tentativo feature Y → ERRORE\! Progetto rotto 💥  
     ↓  
"Ehi, torna alla versione precedente"  
     ↓

Ripristinato Checkpoint 2: Progetto con feature X ✅

### **8.6 — Errori Comuni**

Errore 1: Non abilitare l'Autocompact  
Senza Autocompact, il contesto si riempie progressivamente e non viene mai liberato. Questo porta a una degradazione graduale delle performance fino al punto in cui Claude Code non riesce più a operare efficacemente. L'Autocompact è la prima impostazione da verificare.

Errore 2: Disabilitare il Thinking Mode per "velocizzare"  
Il Thinking Mode permette a Claude di ragionare in modo estensivo prima di rispondere. Disabilitarlo rende le risposte più rapide ma significativamente meno accurate, specialmente su task complesse. È come chiedere a qualcuno di risolvere un problema complesso vietandogli di pensare.

Errore 3: Non monitorare /context regolarmente  
Molti utenti non sanno nemmeno che il comando /context esiste. Questo li rende "ciechi" rispetto a come il contesto viene distribuito. Come vedremo nei capitoli sugli MCP, un singolo MCP può consumare il 27% del contesto senza che l'utente se ne renda conto.

Errore 4: Cambiare configurazioni senza capirne l'impatto  
Ogni impostazione in /config ha implicazioni a cascata. Per esempio, disabilitare i checkpoint in un progetto dove si usa bypass permission è una ricetta per il disastro. Ogni modifica di configurazione dovrebbe essere fatta con consapevolezza delle conseguenze.

### **8.7 — Insight Avanzato**

Il Tab cycling in /config:  
Il sistema di navigazione con Tab in /config rivela tre livelli di informazione che servono a scopi diversi:

Tab 1: CONFIG (Configurazione)  
→ Per impostare il comportamento del sistema  
→ Usare all'inizio di un progetto o quando serve cambiare qualcosa

Tab 2: USAGE (Utilizzo)  
→ Per monitorare quanto del modello avete usato  
→ Mostra la percentuale di utilizzo rispetto al limite del piano  
→ Es: "Ho utilizzato il 28% del mio modello questo mese"  
→ Utile per gestire i limiti del piano subscription

Tab 3: STATUS (Stato)  
→ Per verificare lo stato corrente della sessione

→ Mostra informazioni tecniche sulla connessione e il funzionamento

Questi tre livelli corrispondono a tre domande diverse:

* Config: "Come è impostato il mio sistema?" (passato/futuro)  
* Usage: "Quanto ho usato il mio sistema?" (storico)  
* Status: "Come sta andando il mio sistema adesso?" (presente)

Personalizzazione della Status Line:  
La Status Line non è un'entità fissa. L'autore menziona che contiene "informazioni addizionali che utilizzo per controllare meglio il mio terminal" e che è possibile personalizzarla. Se volete replicare la configurazione dell'autore, il metodo più efficace è fare uno screenshot della Status Line mostrata nel video, incollarlo in Claude Code, e chiedere di replicarla. Claude Code configurerà automaticamente il Terminal per mostrare le stesse informazioni.

