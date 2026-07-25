# MODULO KNOWLEDGE BASE

**K04-permessi.md** — Capitoli 17-19 | Le 4 modalità di permesso, Plan Mode, Bypass Permission

## Riferimenti Correlati
- K03-progetti.md (per costruire progetti)
- K05-context.md (per ottimizzare il lavoro)

---

# **PARTE 5 — MODALITÀ DI PERMESSO E PIANIFICAZIONE**

---

## **CAPITOLO 17: LE QUATTRO MODALITÀ DI PERMESSO**

### **17.1 — Definizione del Concetto**

Le modalità di permesso (permission modes) sono i livelli di autonomia che l'utente concede a Claude Code durante il lavoro. Determinano quanto controllo l'utente mantiene sulle azioni di Claude Code — dalla supervisione totale di ogni singola modifica, fino alla completa autonomia operativa. La scelta della modalità corretta in ogni fase del lavoro è una decisione strategica che impatta direttamente su velocità, sicurezza e qualità del risultato.

### **17.2 — Spiegazione Espansa**

Esistono quattro modalità di permesso, disposte in ordine crescente di autonomia:

text

SPETTRO DI AUTONOMIA:

Controllo massimo ◄────────────────────────────► Autonomia massima  
dell'utente                                       di Claude Code

\[Ask Before Edits\] → \[Accept Edits\] → \[Plan Mode\] → \[Bypass Permission\]

    Modalità 1          Modalità 2      Modalità 3      Modalità 4

#### **Modalità 1: Ask Before Edits (Default)**

text

COMPORTAMENTO:

Utente: "Cambia il titolo del sito e scrivici Giovanni"  
     ↓  
Claude Code: \[analizza il file, trova il titolo\]  
     ↓  
Claude Code: \[MOSTRA le modifiche proposte senza applicarle\]  
     ↓  
Schermata: "Vorrei fare queste modifiche. Vuoi procedere?"  
     ↓  
Opzioni:  
├── \[Sì\] → Applica questa modifica specifica  
├── \[Sì a tutto\] → Applica tutte le modifiche in questa sessione  
├── \[No\] → Non applicare  
└── \[Altro\] → Opzione alternativa / modifica della richiesta

Caratteristiche chiave:

* È il comportamento di default quando si installa Claude Code  
* Claude Code propone le modifiche ma non le applica fino a conferma esplicita  
* L'utente vede esattamente cosa verrà modificato prima che succeda  
* Ogni modifica richiede un'approvazione separata (a meno che non si scelga "Sì a tutto")

Quando usarla:

* Quando state imparando Claude Code e volete capire cosa fa  
* Quando lavorate su file critici che non volete siano modificati per errore  
* Quando volete controllo granulare su ogni singola modifica  
* In ambienti di produzione dove ogni cambiamento deve essere approvato

Limitazione:  
È la modalità più lenta perché richiede intervento umano per ogni modifica. Su progetti con decine o centinaia di modifiche, diventa impraticabile.

#### **Modalità 2: Accept Edits (Accettazione Automatica delle Modifiche)**

text

COMPORTAMENTO:

Utente: "Cambia il titolo del sito e scrivici Giovanni"  
     ↓  
Claude Code: \[analizza il file, trova il titolo\]  
     ↓  
Claude Code: \[APPLICA le modifiche AUTOMATICAMENTE\]  
     ↓  
\[Modifica completata senza chiedere conferma\]  
     ↓  
⚠️ ECCEZIONE: Chiede sempre conferma per:  
   • Creare nuovi file  
   • Cancellare file esistenti

Caratteristiche chiave:

* Le modifiche ai file esistenti vengono applicate automaticamente  
* La creazione e cancellazione di file richiede sempre conferma  
* È un buon compromesso tra velocità e sicurezza  
* Elimina la necessità di approvare ogni singolo edit

Quando usarla:

* Quando avete un'idea chiara di cosa volete e non serve revisionare ogni modifica  
* Per task di refactoring dove molti file devono essere modificati  
* Quando volete velocità ma mantenete la protezione contro creazione/cancellazione accidentale

Limitazione importante notata dall'autore:  
Accept Edits non può creare o cancellare file autonomamente. Per queste operazioni, chiederà sempre il consenso. Questo è un limite di sicurezza intenzionale che protegge da cancellazioni accidentali.

#### **Modalità 3: Plan Mode (Pianificazione)**

Il Plan Mode è sufficientemente importante da meritare un capitolo dedicato (Capitolo 18). Qui ne forniamo la definizione sintetica nel contesto delle quattro modalità.

text

COMPORTAMENTO:

Utente: "Costruiscimi un'app simile a Trello con autenticazione e pagamenti"  
     ↓  
Claude Code: \[ANALIZZA la richiesta\]  
     ↓  
Claude Code: \[CREA UN PIANO strutturato con subtask\]  
     ↓  
Claude Code: \[PRESENTA il piano all'utente\]  
     ↓  
Utente: \[Revisiona il piano, approva/modifica\]  
     ↓

Claude Code: \[Esegue il piano approvato\]

Caratteristiche chiave:

* Claude Code non esegue nulla immediatamente  
* Prima crea un piano strutturato e lo presenta per approvazione  
* L'utente può modificare, aggiungere o rimuovere elementi dal piano  
* Solo dopo l'approvazione, Claude Code procede all'esecuzione  
* Durante l'esecuzione, segue la checklist del piano approvato

#### **Modalità 4: Bypass Permission (Dangerously Skip Permissions)**

Anche questa modalità merita un capitolo dedicato (Capitolo 19). Definizione sintetica:

text

COMPORTAMENTO:

Utente: "Costruiscimi un'app simile a Trello con autenticazione e pagamenti"  
     ↓  
Claude Code: \[ESEGUE TUTTO in completa autonomia\]  
     ↓  
\[Crea file, modifica file, cancella file, esegue comandi\]  
     ↓  
\[NESSUNA richiesta di conferma per nulla\]  
     ↓

\[Risultato finale presentato quando tutto è completato\]

Caratteristiche chiave:

* Autonomia totale: Claude Code può fare qualsiasi cosa senza chiedere  
* Include la capacità di creare e cancellare file  
* È la modalità più veloce ma anche la più rischiosa  
* L'autore la usa frequentemente ma avverte dei rischi

### **17.3 — Perché Questo Concetto È Importante**

La scelta della modalità di permesso non è una preferenza estetica. È una decisione strategica che deve essere presa in base a:

1. La fase del progetto — Pianificazione? Esecuzione? Debugging?  
2. Il livello di rischio — File critici? Dati sensibili? Produzione?  
3. La qualità del piano — Piano dettagliato? Prompt vago?  
4. L'esperienza dell'utente — Principiante? Esperto?

text

MATRICE DECISIONALE:

                      Rischio Basso    Rischio Alto  
                    ┌─────────────────┬──────────────────┐  
Piano Buono         │ Bypass          │ Plan Mode →      │  
                    │ Permission      │ poi Accept Edits  │  
                    ├─────────────────┼──────────────────┤  
Piano Vago/Assente  │ Accept Edits    │ Ask Before Edits │  
                    │                 │                  │

                    └─────────────────┴──────────────────┘

### **17.4 — Meccanismo Sottostante: Propagazione dei Permessi**

L'autore introduce un concetto critico che molti ignorano: i permessi si propagano a tutti i sotto-agenti.

*"Quando diamo una permission all'agente principale, tutte queste permission si replicano anche a tutti i sottoagenti o a qualsiasi cosa concateniamo dopo."*

text

PROPAGAZIONE DEI PERMESSI:

Agente Principale (Bypass Permission)  
     ↓ eredita  
Sub-agente Researcher (Bypass Permission)  
     ↓ eredita  
Sub-agente Reviewer (Bypass Permission)  
     ↓ eredita  
Sub-agente QA (Bypass Permission)

IMPLICAZIONE: Se l'agente principale ha Bypass Permission,  
TUTTI i sotto-agenti avranno Bypass Permission.  
Non è possibile dare Bypass Permission al principale

e Ask Before Edits a un sotto-agente.

Questo ha implicazioni di sicurezza significative: se date bypass permission all'agente principale e uno dei sotto-agenti commette un errore, quell'errore viene eseguito senza alcuna richiesta di conferma.

### **17.5 — Interpretazione Pratica: Come Cambiare Modalità**

#### **Nell'IDE (VS Code / Antigravity)**

Nella parte superiore del pannello Claude Code, ci sono pulsanti/selector per cambiare tra le modalità:

* Ask Before Edits  
* Edit Automatically (Accept Edits)  
* Plan Mode  
* Bypass Permission (se abilitato nelle impostazioni)

#### **Nel Terminal**

text

NAVIGAZIONE MODALITÀ NEL TERMINAL:

Shift \+ Freccia su \+ Tab → Mostra le modalità disponibili  
                         → Navigare con le frecce  
                         → Selezionare con Enter

Oppure all'avvio:  
$ claude                                    → Avvia in modalità default  
$ claude \--dangerously-skip-permissions     → Avvia in Bypass Permission

#### **Abilitare Bypass Permission (non attivo di default)**

In VS Code:

1. Icona ingranaggio (⚙️) → Settings  
2. Cercare "Claude"  
3. Abilitare "Allow Dangerously Skip Permission"

In Antigravity:

1. Icona ingranaggio in alto a destra → Settings  
2. Cercare "Claude Code"  
3. Abilitare "Dangerously Skip Permission"

Nel Terminal:  
Usare il flag \--dangerously-skip-permissions all'avvio, oppure configurare un alias come l'autore che usa "YOLO" (You Only Live Once).

### **17.6 — Gestione Avanzata dei Permessi nel Terminal**

Nel Terminal, esiste un sistema di permessi più granulare accessibile tramite il comando permissions:

text

SISTEMA DI PERMESSI GRANULARE:

Allow (Consenti):  
→ Il tool è sempre permesso senza chiedere  
→ Esempio: "Allow bash" \= i comandi bash vengono eseguiti automaticamente

Ask (Chiedi):  
→ Chiede sempre il permesso prima di usare il tool  
→ Esempio: "Ask write" \= chiede conferma prima di ogni scrittura su file

Deny (Nega):  
→ Il tool non viene mai usato, nemmeno se richiesto  
→ Esempio: "Deny delete" \= impossibile cancellare file in qualsiasi circostanza

Workspace:  
→ Permessi specifici per il workspace/progetto corrente

→ Permette configurazioni diverse per progetti diversi

Questo sistema è più granulare delle quattro modalità principali perché permette di controllare i singoli tool individualmente anziché applicare una politica uniforme a tutti i tool.

### **17.7 — Errori Comuni**

Errore 1: Restare sempre in Ask Before Edits  
Molti utenti non escono mai dalla modalità default per paura di perdere il controllo. Questo rallenta enormemente il workflow. Una volta che avete familiarità con Claude Code e avete un buon piano, passare ad Accept Edits o Bypass Permission è una scelta di produttività essenziale.

Errore 2: Andare direttamente in Bypass Permission senza piano  
Questo è l'estremo opposto ed è molto pericoloso. L'autore racconta il caso di una persona che: *"ha cancellato completamente qualsiasi cosa all'interno del suo computer. Aveva dato un piano povero, aveva fatto bypass permission, e quello che è successo è che il computer ha continuato a fare ricerca per qualche ora finché poi non ha deciso che la soluzione migliore per risolvere il problema era cancellare tutto quanto."*

Errore 3: Non capire la propagazione ai sotto-agenti  
Se date bypass permission all'agente principale, ogni sotto-agente chiamato eredita la stessa autonomia. Questo è particolarmente rischioso con sotto-agenti che fanno operazioni distruttive (es. pulizia codice, ristrutturazione file).

Errore 4: Cambiare modalità nel mezzo di un'operazione critica  
Passare da Plan Mode a Bypass Permission mentre Claude sta ancora pianificando può creare confusione. Completate la fase corrente prima di cambiare modalità.

Errore 5: Non abilitare Bypass Permission nelle impostazioni e non capire perché non appare  
La modalità Bypass Permission non è visibile di default. Deve essere esplicitamente abilitata nelle impostazioni dell'IDE. Molti utenti cercano questa opzione senza trovarla perché non hanno modificato le impostazioni.

### **17.8 — Insight Avanzato**

Il quinto livello: Don't Ask (solo Terminal)

L'autore menziona una modalità aggiuntiva disponibile solo nel Terminal e non presente nelle IDE:

text

PERMESSI NEL TERMINAL:

Allow → "We always allow this tool"  
Ask   → "We always ask permission" (default)  
Deny  → "We always reject request to use denied tools"

Deny è il "Don't Ask" — non chiede nemmeno, rifiuta direttamente.

La differenza tra "Ask" e "Deny" è sottile ma importante:

* Ask: "Posso usare questo tool?" → L'utente può dire sì o no  
* Deny: Il tool non viene mai usato, Claude Code non chiede nemmeno. Il tool è effettivamente disabilitato.

Questo è utile per disabilitare completamente strumenti che non volete siano mai usati nel vostro progetto (per esempio, disabilitare la capacità di cancellare file in un ambiente di produzione).

Workflow raccomandato dall'autore:

L'autore rivela il suo workflow personale basato sulla citazione del creatore di Claude Code, Boris:

*"Come disse Boris, creatore di Claude Code — e che lui stesso fa questa cosa — spende gran parte del suo tempo in Plan Mode, e una volta che il piano ha senso ed è fatto in maniera corretta, allora Claude Code può fare il cosiddetto one-shot."*

text

WORKFLOW BORIS/AUTORE:

Fase 1: PLAN MODE (70-80% del tempo)  
├── Definire il progetto  
├── Creare il piano  
├── Revisionare il piano  
├── Modificare il piano  
├── Ri-revisionare  
├── Approvare il piano finale  
└── Tempo: la maggior parte della sessione

Fase 2: BYPASS PERMISSION (20-30% del tempo)  
├── Eseguire il piano approvato  
├── Claude Code lavora in autonomia  
├── One-shot (idealmente)  
└── Tempo: relativamente breve

Proporzione ideale: PIANO \>\> ESECUZIONE

---

## **CAPITOLO 18: PLAN MODE — L'APPROCCIO STRATEGICO**

### **18.1 — Definizione del Concetto**

Il Plan Mode è la modalità in cui Claude Code, anziché eseguire immediatamente le istruzioni, crea prima un piano strutturato composto da subtask ordinate, lo presenta all'utente per revisione e approvazione, e solo successivamente procede all'esecuzione. È la modalità strategica per eccellenza e quella che l'autore considera la più importante per progetti di qualsiasi complessità.

### **18.2 — Spiegazione Espansa**

#### **Il Flusso del Plan Mode**

text

FLUSSO COMPLETO:

FASE 1 — INPUT  
Utente scrive un prompt con la richiesta completa  
     ↓

FASE 2 — ANALISI  
Claude Code analizza:  
├── Il prompt dell'utente  
├── Il CLAUDE.md del progetto  
├── I file esistenti nel progetto  
├── Le rules nella cartella .claude  
├── Le risorse disponibili (API, tools, MCP)  
└── Le skill applicabili  
     ↓

FASE 3 — PIANIFICAZIONE  
Claude Code produce una checklist strutturata:  
├── Subtask 1: \[descrizione\]  
├── Subtask 2: \[descrizione\]  
├── Subtask 3: \[descrizione\]  
├── ...  
├── Subtask N: \[descrizione\]  
└── Ordine di esecuzione e dipendenze  
     ↓

FASE 4 — REVISIONE  
L'utente rivede la checklist:  
├── ✅ "Questo va bene"  
├── ✅ "Questo va bene"  
├── ❌ "Questo non va bene — cambia così"  
├── ⚠️ "Qui manca qualcosa — aggiungi questo"  
├── ✅ "Questo va bene ma potremmo migliorarlo — cambialo"  
└── Feedback inviato a Claude Code  
     ↓

FASE 5 — REVISIONE ITERATIVA  
Claude Code aggiorna il piano in base al feedback  
L'utente rivede di nuovo  
Si ripete fino a quando l'utente è soddisfatto  
     ↓

FASE 6 — APPROVAZIONE  
L'utente approva il piano finale  
     ↓

FASE 7 — ESECUZIONE  
Claude Code esegue il piano (tipicamente in Accept Edits o Bypass Permission)

L'autore è molto chiaro sull'approccio alla revisione: *"Plan mode significa semplicemente: continuiamo ad insistere fino alla morte sulla nostra checklist fino a che non siamo soddisfatti. E poi, una volta che abbiamo pianificato il tutto, allora muoviamoci ad accettare gli edits e ad andare a costruire."*

La parola chiave è "fino alla morte" — non è un'esagerazione. La qualità del piano è direttamente proporzionale al tempo investito nella sua revisione.

### **18.3 — Perché Questo Concetto È Importante**

L'autore presenta un'analisi visiva che dimostra perché il Plan Mode è cruciale, usando l'esempio dei "blocchi":

#### **Scenario SENZA Plan Mode (Esecuzione Diretta):**

text

COSTRUZIONE DIRETTA SENZA PIANO:

Blocco 1 → Blocco 2 → Blocco 3 → Blocco 4 → Blocco 5  
                                     ↑           ↑  
                                     │           │  
                              "Questi non      "Questi non  
                               vanno bene"      vanno bene"

CONSEGUENZA:  
• Tempo speso: 15 minuti per costruire 5 blocchi  
• Scoperta: 2 blocchi (4 e 5\) non vanno bene  
• Problema: I blocchi sbagliati influenzano la struttura complessiva  
• Rischio: Potrebbe essere necessario RICOSTRUIRE TUTTO  
• Tempo perso: 15 minuti \+ tempo di ricostruzione  
• Tempo totale potenziale: 1-5 ORE

#### **Scenario CON Plan Mode:**

text

PIANIFICAZIONE PRIMA DELL'ESECUZIONE:

Piano:  
□ Blocco 1: \[descrizione\]    → ✅ Ok  
□ Blocco 2: \[descrizione\]    → ✅ Ok  
□ Blocco 3: \[descrizione\]    → ✅ Ok  
□ Blocco 4: \[descrizione\]    → ❌ Non va bene → Modificato  
□ Blocco 5: \[descrizione\]    → ❌ Non va bene → Modificato

Piano Rivisto:  
□ Blocco 1: \[descrizione\]    → ✅ Ok  
□ Blocco 2: \[descrizione\]    → ✅ Ok  
□ Blocco 3: \[descrizione\]    → ✅ Ok  
□ Blocco 4: \[nuova descrizione\] → ✅ Ok  
□ Blocco 5: \[nuova descrizione\] → ✅ Ok

CONSEGUENZA:  
• Tempo di pianificazione: 10-15 minuti  
• Tutti i blocchi sono validati PRIMA della costruzione  
• Nessun rischio di dover ricostruire  
• Esecuzione: veloce e one-shot  
• Tempo totale: 20-30 minuti MAX

La differenza è lampante:

* Senza piano: 15 minuti di costruzione \+ 1-5 ore di ricostruzione \= 1-5+ ore  
* Con piano: 10-15 minuti di pianificazione \+ 10-15 minuti di esecuzione \= 20-30 minuti

L'autore riassume: *"Plan mode significa semplicemente: continuiamo ad insistere fino alla morte sulla nostra checklist fino a che non siamo soddisfatti."*

### **18.4 — Interpretazione Pratica: Domande Intelligenti del Piano**

Durante il Plan Mode, Claude Code non si limita a creare un piano. Pone anche domande strategiche che aiutano a raffinare il progetto. L'autore mostra due esempi concreti dalla costruzione dell'app Trello:

Domanda 1 — Scelta tecnica:

Claude: "Quale metodo di autenticazione preferisci?  
         A) Magic Link — l'utente riceve un'email e si autentica da lì

         B) Login diretto — l'utente inserisce credenziali e entra subito"

Questa domanda è importante perché la scelta tecnica influenza l'architettura dell'intera applicazione. Prenderla nella fase di pianificazione evita di dover ristrutturare l'app in seguito.

Domanda 2 — Sicurezza:

Claude: "La chiave Stripe che hai condiviso è una chiave live di produzione.  
         Vuoi usare chiavi test per lo sviluppo?

         Le chiavi test iniziano con sk\_test\_"

Claude Code identifica un rischio di sicurezza nel prompt dell'utente e lo segnala proattivamente. Questo tipo di feedback è uno dei valori aggiunti del Plan Mode.

### **18.5 — Meccanismo Sottostante: La Checklist come Contratto**

Il piano prodotto dal Plan Mode funziona come un contratto tra l'utente e Claude Code. Una volta approvato:

1. Claude Code sa esattamente cosa deve fare  
2. L'utente sa esattamente cosa aspettarsi  
3. Ogni deviazione dal piano è un errore identificabile  
4. Il progresso è misurabile (quanti item della checklist sono completati)

ANALOGIA DEL CONTRATTO:

Piano \= Contratto firmato tra utente e Claude Code

Clausola 1: Fase tech stack setup ✓ (completata)  
Clausola 2: Database schema ✓ (completata)  
Clausola 3: Autenticazione ✓ (completata)  
Clausola 4: Componenti UI □ (in corso)  
Clausola 5: Integrazione Stripe □ (in attesa)

Se Claude devia dal piano → L'utente può dire "questo non era nel piano"

Se l'utente aggiunge richieste → "Questo non era nel piano — facciamo un nuovo piano"

### **18.6 — Caso Pratico: Il Social Media Manager**

L'autore fornisce il suo esempio più significativo di Plan Mode:

CASO: SOCIAL MEDIA MANAGER

Tempo di Planning: 2 ore e 30 minuti  
├── Definizione delle piattaforme (YouTube IT/EN, LinkedIn, Meta)  
├── Definizione dei workflow per ogni piattaforma  
├── Definizione delle skill necessarie  
├── Definizione delle integrazioni (API per ogni piattaforma)  
├── Definizione del database di riferimento  
├── Revisione del piano  
├── Seconda revisione  
├── Approvazione finale

Tempo di Esecuzione: 3 ore  
├── Claude Code in Bypass Permission  
├── ONE-SHOT (nessun ritorno necessario)  
├── Tutti i collegamenti funzionanti  
│   ├── YouTube  
│   ├── LinkedIn  
│   └── Meta  
└── Sistema completo e operativo

TEMPO TOTALE: 5 ore e 30 minuti  
ITERAZIONI POST-ESECUZIONE: ZERO

RISULTATO: Sistema completo e in produzione

La proporzione è significativa: 45% pianificazione, 55% esecuzione, e zero correzioni post-esecuzione. L'investimento nella pianificazione ha prodotto un'esecuzione one-shot perfetta.

### **18.7 — Errori Comuni**

Errore 1: Approvare il piano troppo velocemente  
La tentazione di premere "Approva" per passare subito all'esecuzione è forte. Ma ogni minuto speso a revisionare il piano risparmia potenzialmente ore di debugging e ricostruzione. L'autore è chiaro: *"Questa è la parte su cui ci focalizziamo di più."*

Errore 2: Non dare feedback specifico durante la revisione  
Dire "non mi piace" non è feedback utile. Dire "il punto 4 non mi piace perché dovremmo usare PostgreSQL anziché SQLite, e il punto 5 manca di error handling" è feedback che Claude Code può utilizzare per migliorare il piano.

Errore 3: Saltare il Plan Mode per task "semplici"  
Molte task che sembrano semplici si rivelano complesse durante l'esecuzione. L'autore raccomanda il Plan Mode per qualsiasi task che coinvolga più di un file o più di una funzionalità.

Errore 4: Non fare Plan Mode prima di Bypass Permission  
Fare Bypass Permission senza un piano approvato è la ricetta per il disastro. L'autore lo raccomanda esplicitamente come workflow sequenziale: prima Plan Mode per creare e approvare il piano, poi Bypass Permission per eseguirlo.

Errore 5: Confondere Plan Mode con una modalità di esecuzione lenta  
Plan Mode non è "fare le cose lentamente". È investire tempo nella direzione prima di investire tempo nell'esecuzione. Il tempo totale è quasi sempre inferiore rispetto all'esecuzione diretta senza piano.

### **18.8 — Insight Avanzato**

La transizione Plan Mode → Bypass Permission:

L'autore mostra la transizione pratica nel suo workflow:

TRANSIZIONE PRATICA:

1\. Attivare Plan Mode  
2\. Scrivere il prompt completo  
3\. Revisionare il piano generato  
4\. Iterare fino a soddisfazione  
5\. Premere 'S' (per Save/Submit il piano approvato)  
6\. Attivare "Auto Accept" (accettazione automatica)  
7\. Passare a Bypass Permission  
8\. Claude Code esegue il piano in autonomia

L'autore descrive il punto 5-7: "Premiamo S e auto accept,

e poi andiamo in bypass permission."

Questo passaggio è il momento in cui l'utente "passa il controllo" a Claude Code. È il momento in cui la fiducia nel piano si traduce in azione autonoma.

Il piano come protezione economica:

Per chi usa il piano API, il Plan Mode è anche una protezione economica. Pianificare costa relativamente poco in token (la conversazione di pianificazione è breve e focalizzata). L'esecuzione costa molto di più. Un piano sbagliato che porta a un'esecuzione da rifare significa pagare due volte per lo stesso lavoro.

Per chi usa il piano subscription con Agent Teams, la logica è simile: gli Agent Teams consumano velocemente il budget mensile. Un piano accurato prima di lanciare un Agent Team può risparmiare centinaia di euro di consumo inutile.

## **CAPITOLO 19: BYPASS PERMISSION — AUTONOMIA MASSIMA**

### **19.1 — Definizione del Concetto**

Bypass Permission (ufficialmente "Dangerously Skip Permissions") è la modalità in cui Claude Code opera in completa autonomia, senza richiedere alcuna approvazione per qualsiasi operazione — incluse la creazione e la cancellazione di file. È la modalità più potente e più rischiosa, che richiede un piano ben definito come prerequisito e una comprensione chiara delle implicazioni.

### **19.2 — Spiegazione Espansa**

Il nome stesso della modalità contiene un avvertimento: "Dangerously" (pericolosamente). Anthropic ha intenzionalmente inserito la parola "pericolosamente" nel nome per segnalare che questa modalità richiede consapevolezza dei rischi.

#### **Cosa può fare Claude Code in Bypass Permission:**

CAPACITÀ COMPLETE:

✅ Leggere qualsiasi file nel progetto  
✅ Modificare qualsiasi file nel progetto  
✅ Creare nuovi file  
✅ CANCELLARE file esistenti        ← La differenza critica  
✅ Eseguire comandi bash  
✅ Installare pacchetti/dipendenze  
✅ Modificare configurazioni di sistema  
✅ Navigare nel web (se MCP attivo)  
✅ Chiamare sotto-agenti con gli stessi permessi  
✅ Tutto quanto SENZA CHIEDERE MAI conferma

La differenza critica rispetto ad "Accept Edits" è nella capacità di creare e cancellare file autonomamente. In Accept Edits, Claude Code chiede sempre conferma prima di creare o cancellare un file. In Bypass Permission, può farlo senza alcuna richiesta.

### **19.3 — Perché Questo Concetto È Importante**

L'importanza di Bypass Permission è duplice:

Lato positivo — Produttività massima:  
Quando il piano è buono e le istruzioni sono chiare, Bypass Permission permette a Claude Code di lavorare alla massima velocità possibile. Non ci sono interruzioni per chiedere permessi, non ci sono attese per la conferma dell'utente. Claude Code procede dall'inizio alla fine del piano senza fermarsi.

L'autore dimostra questo con il caso del social media manager: dopo 2.5 ore di pianificazione, Claude Code ha costruito l'intero sistema in 3 ore senza mai fermarsi — un one-shot completo.

Lato negativo — Rischio massimo:  
L'autore racconta un caso reale che serve da avvertimento:

*"È successo che una persona, mi sembra un paio di mesi fa, abbia cancellato completamente qualsiasi cosa all'interno del suo computer. Aveva dato un piano povero, aveva fatto bypass permission, e quello che è successo è che il computer ha continuato a fare ricerca per qualche ora, finché poi non ha deciso che la soluzione migliore per risolvere il problema era cancellare tutto quanto."*

Analisi del caso:

CASO DI DISASTRO:

Causa 1: Piano povero (insufficiente per guidare Claude Code)  
Causa 2: Bypass Permission attivato (nessun controllo)  
Causa 3: Claude Code ha operato per ore senza supervisione  
Causa 4: Claude Code ha determinato che la "soluzione" era cancellare tutto

Risultato: TUTTO il contenuto del computer cancellato

Prevenzione: Piano dettagliato \+ Checkpoint attivi \+ Supervisione periodica

### **19.4 — Interpretazione Pratica: Quando Usare Bypass Permission**

L'autore fornisce una guida chiara basata sulla sua esperienza e su quella del creatore di Claude Code:

USARE BYPASS PERMISSION QUANDO:

✅ Avete completato un piano dettagliato in Plan Mode  
✅ Il piano è stato revisionato e approvato  
✅ I checkpoint/rewind sono attivi (/config → Rewind: ON)  
✅ Avete un backup del progetto (o è su GitHub)  
✅ Le istruzioni nel CLAUDE.md sono chiare e specifiche  
✅ I vincoli negativi sono definiti ("NON fare X, NON cancellare Y")  
✅ Siete nelle vicinanze del computer per monitorare periodicamente

NON USARE BYPASS PERMISSION QUANDO:

❌ Non avete un piano chiaro  
❌ Il prompt è vago o aspirazionale  
❌ Lavorate su file di produzione senza backup  
❌ I checkpoint non sono attivi  
❌ Non avete definito vincoli negativi  
❌ State usando il piano API (i costi possono esplodere)

❌ È la prima volta che fate un task simile

### **19.5 — Meccanismo Sottostante: La Relazione Piano-Esecuzione**

La chiave per usare Bypass Permission in modo sicuro è la qualità del piano. L'autore stabilisce una relazione diretta:

RELAZIONE PIANO ↔ BYPASS PERMISSION:

Piano eccellente \+ Bypass Permission \= ONE-SHOT (risultato perfetto)  
Piano buono \+ Bypass Permission \= Buon risultato con poche correzioni  
Piano mediocre \+ Bypass Permission \= Risultato mediocre, molte correzioni  
Piano povero \+ Bypass Permission \= DISASTRO POTENZIALE

La qualità del piano è la PRECONDIZIONE per Bypass Permission sicuro.

L'autore riassume con le parole di Boris: *"Spende gran parte del suo tempo in Plan Mode, e una volta che il piano ha senso ed è fatto in maniera corretta, allora Claude Code può fare il cosiddetto one-shot."*

### **19.6 — Come Attivare Bypass Permission**

Il processo è diverso per ogni interfaccia:

#### **Nel Terminal (metodo più diretto):**

\# Avvio con flag  
$ claude \--dangerously-skip-permissions

\# L'autore usa un alias personalizzato:  
$ yolo  
\# Che corrisponde a:  
\# alias yolo="claude \--dangerously-skip-permissions"

L'autore spiega: *"YOLO, You Only Live Once — per me vuol dire avvia Claude Code con bypass permission."*

#### **In VS Code:**

1\. Icona ingranaggio (⚙️) → Settings  
2\. Cercare "Claude"  
3\. Checkbox: "Allow Dangerously Skip Permission" → ✅  
4\. Nel pannello Claude Code, selezionare la modalità Bypass Permission

#### **In Antigravity:**

1\. Icona ingranaggio IN ALTO A DESTRA → Settings  
2\. Cercare "Claude Code"  
3\. Checkbox: "Dangerously Skip Permission" → ✅  
4\. Nel pannello Claude Code, selezionare la modalità Bypass Permission

Nota importante: La posizione dell'icona ingranaggio è diversa nei due IDE. L'autore lo specifica: *"La rotellina adesso è qua in cima, in alto a destra"* (per Antigravity), mentre in VS Code è nella barra laterale.

### **19.7 — Errori Comuni**

Errore 1: Bypass Permission come modalità predefinita  
Alcuni utenti, dopo aver visto la velocità del Bypass Permission, lo usano per tutto. Questo è pericoloso perché non tutte le task meritano autonomia totale. Per task esplorative, debugging o modifiche a file critici, Ask Before Edits o Accept Edits sono più appropriate.

Errore 2: Lasciare il computer incustodito per ore durante Bypass Permission  
Anche con un buon piano, Claude Code può incontrare situazioni impreviste e prendere decisioni autonome che non sono ottimali. Monitorare periodicamente (anche solo guardando lo schermo ogni 10-15 minuti) previene situazioni problematiche.

Errore 3: Non avere checkpoint attivi  
Senza checkpoint, un'operazione distruttiva non è reversibile (almeno non facilmente). Verificare sempre che /config → Rewind/Checkpoint: ON prima di usare Bypass Permission.

Errore 4: Non definire vincoli negativi nel CLAUDE.md  
Senza vincoli espliciti su cosa NON fare, Claude Code in Bypass Permission potrebbe:

* Cancellare file che considera obsoleti  
* Ristrutturare completamente l'architettura del progetto  
* Modificare configurazioni di sistema  
* Eliminare codice che considera ridondante

Vincoli come "NON cancellare MAI i file nella cartella /config" o "NON modificare i file .env" sono essenziali.

Errore 5: Avere paura irrazionale di Bypass Permission  
L'autore nota che *"un po' di persone hanno diciamo paura"* di questa modalità. Con le precauzioni appropriate (piano, checkpoint, vincoli), Bypass Permission è lo strumento più produttivo disponibile. La paura irrazionale porta a non usarlo mai, il che significa perdere il beneficio della produttività massima.

### **19.8 — Insight Avanzato**

Il workflow ideale completo:

Combinando tutti i concetti discussi in questa sezione, il workflow ideale dell'autore è:

WORKFLOW COMPLETO IDEALE:

FASE 0 — PREPARAZIONE (una tantum per progetto)  
├── Creare la struttura .claude con rules, skills, agents  
├── Configurare il CLAUDE.md con contesto e vincoli  
├── Attivare Autocompact, Thinking Mode, Checkpoint  
└── Installare MCP necessari (es. Chrome Dev Tool)

FASE 1 — PLAN MODE (60-80% del tempo totale)  
├── Scrivere il prompt completo con tutti i requisiti  
├── Includere riferimenti visivi (screenshot, immagini)  
├── Includere dati tecnici (API key, stili CSS)  
├── Revisionare il piano generato  
├── Iterare il piano fino a soddisfazione totale  
├── Porre domande su punti ambigui  
└── Approvare il piano finale

FASE 2 — BYPASS PERMISSION (20-40% del tempo totale)  
├── Attivare bypass permission  
├── Attivare auto-accept  
├── Claude Code esegue il piano in autonomia  
├── Monitorare periodicamente  
├── Hook sonoro per notifica di completamento  
└── Risultato finale (idealmente one-shot)

FASE 3 — VALIDAZIONE  
├── Chiamare il sub-agente Reviewer (zero-context code review)  
├── Chiamare il sub-agente QA (test automatici)  
├── Verificare manualmente le funzionalità critiche

└── Fare deployment se tutto è ok

Questo workflow è il distillato dell'intera esperienza dell'autore e rappresenta il modo più efficiente di utilizzare Claude Code per progetti di qualsiasi complessità.

