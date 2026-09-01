# REF_11 — PRD Real Examples Annotated
## Casi Studio di Aziende Reali con Annotazioni Critiche

> **Come usare questo file**: Non copiare la struttura. Non usare questi PRD come template da riempire.
> Usali per capire la **mentalità** con cui i product manager di aziende di successo pensano ai problemi.
> La struttura è conseguenza del pensiero. Se capisci il pensiero, la struttura viene da sola.
>
> Ogni caso studio è marcato **[RICOSTRUITO]** — si tratta di ricostruzioni educative plausibili
> basate su documentazione pubblica, interviste, changelog e post-mortems disponibili online.
> Non sono PRD interni reali. Lo scopo è operativo: imparare dai principi, non dai formati.

---

## Come leggere le annotazioni

Le annotazioni seguono questo schema, applicato ai punti chiave del testo:

```
🔍 ANNOTAZIONE: Cosa funziona bene — perché questo elemento è efficace
⚠️ ANNOTAZIONE: Cosa manca o potrebbe essere più forte
💡 LEZIONE: Principio universale da portare nei tuoi PRD
```

Leggi ogni caso studio due volte:
1. Prima lettura: leggi il PRD come se fossi un engineer che deve costruirlo
2. Seconda lettura: leggi le annotazioni e cerca i pattern

---

---

# CASO STUDIO 1: Intercom — Feature "Inbox Views"
## [RICOSTRUITO] — PRD plausibile basato su documentazione pubblica

**Contesto**: Intercom è un SaaS B2B di customer support. Nel 2019 ha introdotto "Views" — un sistema di filtri e viste personalizzate per organizzare le conversazioni nella shared inbox. Prima di questa feature, tutti gli agenti vedevano tutte le conversazioni nello stesso stream non filtrato.

---

```markdown
---
# PRD: Inbox Views — Sistema di Viste Personalizzate
**Versione**: 2.1 | **Status**: APPROVED ✅
**Autore**: Product Manager, Messenger Team
**Data creazione**: Marzo 2019 (ricostruzione)
**Revisori**: Engineering Lead, Head of Design, Customer Success
**Epic**: Inbox Efficiency Q2 2019
---

## CHANGE LOG
| Versione | Data  | Modifica                                     | Motivo                             |
|----------|-------|----------------------------------------------|------------------------------------|
| 1.0      | +0d   | Draft iniziale con tutte le viste            | —                                  |
| 2.0      | +8d   | Rimossa condivisione view tra team           | Troppo complessa per v1, v2 scope  |
| 2.1      | +12d  | Aggiunti "smart views" automatici           | Feedback CS: onboarding più rapido |

---

## TL;DR

**Cosa è**: Un sistema per creare, salvare e condividere viste filtrate della Inbox, organizzate per tipo di conversazione, tag, assegnatario, e stato.

**Il problema**: I support manager di team con 5+ agenti perdono visibilità su cosa sta succedendo nella inbox. Gli agenti perdono tempo a cercare le conversazioni giuste tra centinaia di messaggi. Il risultato: SLA violati, lavoro duplicato, contesti persi.

**La soluzione**: Views personalizzate che filtrano le conversazioni per criteri multipli. Ogni agente vede il suo sottoinsieme rilevante. I manager hanno una view di overview.

**North Star Metric**: Riduzione del tempo medio "dalla conversazione non assegnata a primo tocco" del 30% entro 60 giorni dal rollout.

**Time-box**: 8 settimane — 2 engineer + 1 designer.

---

## PROBLEM STATEMENT

### Il Problema
Le aziende B2B con team di support di 5+ persone non riescono a gestire il volume di conversazioni Intercom senza un sistema di organizzazione. Con 100-500 conversazioni/giorno in una inbox condivisa, il lavoro diventa caotico.

**Evidenze concrete**:
- 78% dei clienti con team >5 agenti hanno creato workaround manuali (segmentazione via tag, inbox secondarie, canali Slack di coordinamento) — dato da survey interna Q4 2018
- 42% dei churn nel segmento "Growing Business" (20-200 seats) cita "inbox management difficulties" come fattore — dato da exit interviews
- Supporto Intercom riceve 300+ richieste/mese di feature filtri avanzati — dato help desk

### Perché ora
Q1 2019: crescita del segmento team enterprise +34% YoY. I clienti più grandi (e più paganti) sono quelli più frustrati. Perdere questo segmento è un rischio business diretto.

### Root cause
Il design originale della inbox Intercom era pensato per founder/solopreneur. Non scala a team distribuiti. Non è un bug — è un'assunzione di design che è diventata obsoleta con la crescita del mercato target.

---

## TARGET UTENTE

### Persona Primaria: Alex, Support Manager
- **Ruolo**: Customer Support Manager, B2B SaaS, team di 8 agenti
- **Contesto**: Lavora con Intercom ogni giorno. Gestisce lo stato della inbox come responsabilità principale. Viene valutato su: CSAT, first response time, ticket resolution rate.
- **Obiettivo primario**: Vedere a colpo d'occhio se il team sta rispettando gli SLA
- **Frustrazione attuale**: Deve fare query manuali ogni mattina per capire cosa c'è in coda. Perde 20-30 minuti/giorno in questo lavoro.
- **Definizione di successo**: "Apro Intercom e so subito dove concentrare il team"

### Persona Secondaria: Laura, Support Agent
- **Ruolo**: Support Agent mid-level, 2 anni in azienda
- **Contesto**: Gestisce 40-60 conversazioni/giorno. Specializzata in onboarding e billing.
- **Obiettivo primario**: Lavorare solo sulle conversazioni di sua competenza senza dover filtrare manualmente
- **Frustrazione attuale**: Vede tutte le conversazioni, anche quelle non sue. Rischio di duplicazione lavoro con i colleghi.
- **Definizione di successo**: "La mia coda mostra solo le conversazioni che devo gestire io"

---

## USER STORIES

### Epic US-01: Creazione View
```
US-001 [P0]
Come Support Manager,
voglio creare una view che mostri solo le conversazioni non assegnate con priorità alta,
in modo da poter identificare immediatamente cosa ha bisogno di attenzione urgente.

Acceptance Criteria:
□ AC-1: Posso creare una view con 1+ filtri attivi (assegnatario, tag, stato, priorità, canale)
□ AC-2: La view si salva automaticamente con un nome custom che scelgo
□ AC-3: La view appare nella sidebar sinistra sotto "Views" con il nome che ho scelto
□ AC-4: La view mostra in real-time le conversazioni che corrispondono ai criteri
□ AC-5: Se 0 conversazioni corrispondono, mostra stato empty con messaggio chiaro
```

```
US-002 [P0]
Come Support Agent,
voglio avere una view predefinita "Le mie conversazioni" che mostri solo quelle assegnate a me,
in modo da non dover filtrare manualmente ogni volta che apro Intercom.

Acceptance Criteria:
□ AC-1: La view "Le mie conversazioni" esiste per default per ogni nuovo utente
□ AC-2: La view si aggiorna in real-time quando mi viene assegnata una nuova conversazione
□ AC-3: Il badge numerico in sidebar mostra il conteggio aggiornato (polling max 30 secondi)
□ AC-4: La view NON mostra conversazioni chiuse da >7 giorni (a meno che non sia filtrata esplicitamente)
```

```
US-003 [P1]
Come Support Manager,
voglio poter riordinare le views nella sidebar tramite drag-and-drop,
in modo da avere le più importanti in cima.

Acceptance Criteria:
□ AC-1: Drag-and-drop funziona su desktop (non richiesto su mobile in v1)
□ AC-2: L'ordine persiste tra sessioni (salvato server-side)
□ AC-3: Le "Smart Views" automatiche non sono riordinabili (sono fisse in cima)
```

```
US-004 [P1]
Come Support Manager,
voglio vedere quante conversazioni ci sono in ogni view senza doverla aprire,
in modo da avere una panoramica rapida dello stato della inbox.

Acceptance Criteria:
□ AC-1: Badge numerico accanto al nome di ogni view in sidebar
□ AC-2: Badge sparisce quando il conteggio è 0
□ AC-3: Badge si aggiorna entro 60 secondi da cambio di stato di una conversazione
□ AC-4: Badge mostra max "99+" per conteggi superiori a 99
```

### Epic US-02: Smart Views Automatiche
```
US-005 [P0]
Come nuovo utente Intercom (onboarding primo giorno),
voglio trovare views già create utili al mio ruolo,
in modo da non dover capire i filtri da zero prima di poter lavorare.

Acceptance Criteria:
□ AC-1: Smart View "Non assegnate" creata automaticamente per tutti gli account con >1 agente
□ AC-2: Smart View "Le mie conversazioni" creata per ogni singolo utente al primo login
□ AC-3: Smart View "Snoozed" mostra conversazioni in stato snoozed assegnate all'utente
□ AC-4: Smart Views hanno icona diversa dalle custom views per distinguerle visivamente
□ AC-5: Smart Views non possono essere eliminate (solo nascoste)
```

### Epic US-03: Gestione Views
```
US-006 [P2]
Come Support Manager,
voglio poter eliminare le views che non uso più,
in modo da mantenere la sidebar ordinata.

Acceptance Criteria:
□ AC-1: Tasto elimina accessibile da menu contestuale (right-click o kebab menu)
□ AC-2: Confirmation dialog prima dell'eliminazione (non undoable)
□ AC-3: Le Smart Views non hanno l'opzione elimina — hanno solo "Nascondi"
□ AC-4: Eliminazione non impatta le conversazioni nella view (solo la view viene rimossa)
```

---

## WHAT WE'RE NOT BUILDING (V1 SCOPE)

- **Condivisione view tra agenti**: troppo complessa per v1 (permissioni, sync, conflitti). Spostata a v2.
- **Views per tipo di canale specifico** (solo email, solo chat): non abbastanza richiesta. Backlog.
- **Export di conversazioni da una view**: richiede lavoro lato export pipeline. Backlog.
- **View con logica OR tra filtri**: complessità UI elevata. v1 supporta solo logica AND.
- **Notifiche push per nuove conversazioni in una view**: v2.

---

## SUCCESS METRICS

### North Star
- Riduzione "tempo medio da conversazione non assegnata a primo tocco": -30% entro 60 giorni dal rollout completo

### Primary Metrics
- Adoption: ≥50% degli account con >3 agenti crea almeno 1 custom view entro 30 giorni
- Engagement: ≥70% degli utenti attivi usa una view (smart o custom) come entry point principale entro 60 giorni
- Support tickets su "inbox management": -20% entro 90 giorni (proxy per problema risolto)

### Counter Metrics (da monitorare per regressioni)
- Tempo di caricamento inbox: nessuna regressione >200ms (P95)
- Error rate su creazione view: <0.5%
- CSAT sulle conversazioni gestite tramite views: non peggiore del baseline

### Come sappiamo che ha funzionato
Survey 30 giorni post-lancio: "Riesci a trovare le conversazioni giuste più velocemente di prima?" — target ≥70% risponde "Sì, decisamente".

---

## RISCHI E DIPENDENZE

| Rischio | Probabilità | Impatto | Mitigazione |
|---------|-------------|---------|-------------|
| Performance con grandi volumi (>10k conversazioni) | Media | Alto | Load test con dataset sintetico prima del rollout |
| Confusion tra Smart Views e Custom Views | Alta | Medio | Differenziazione visiva chiara, tooltip in onboarding |
| Sidebar troppo affollata con molte views | Media | Basso | Limite soft: max 20 custom views per utente (v1) |

---
```

---

### Annotazioni — Caso Studio Intercom

---

**Problem Statement:**

🔍 ANNOTAZIONE: Il Problem Statement cita tre fonti diverse (survey, exit interviews, help desk tickets). Non basta dire "i clienti hanno problemi" — bisogna mostrare da dove viene questa conoscenza. Tre fonti diverse che convergono sullo stesso problema rendono il problem statement quasi inattaccabile in un review meeting.

⚠️ ANNOTAZIONE: Il problema "Root cause" è eccellente — riconosce che il problema non è un bug ma un'assunzione di design diventata obsoleta. Questo tipo di onestà è rara nei PRD. Manca però una stima del costo del non fare nulla: quanto churn/mese se non risolviamo questo?

💡 LEZIONE: Ogni evidenza nel Problem Statement deve avere una fonte. "Il 78% dei clienti..." senza fonte non vale nulla. Con fonte vale moltissimo. Se non hai dati, dici esplicitamente "dato qualitativo da X interviste" — è molto meglio che nessuna evidenza.

---

**Persona:**

🔍 ANNOTAZIONE: Notare che Alex e Laura hanno obiettivi diversi ma complementari. Il PRD non ha scelto una sola persona — ha scelto la gerarchia: Alex è primario (più impatto sul business), Laura è secondaria. La feature deve prima soddisfare Alex, poi Laura. Questo ordine di priorità guida tutte le decisioni di trade-off successive.

⚠️ ANNOTAZIONE: Le personas mancano di contesto sull'azienda in cui lavorano. Alex è in un'azienda B2B SaaS — ma che dimensione? Che settore? Questa informazione cambia il tipo di conversazioni che gestisce. Una versione più ricca specificherebbe "azienda SaaS HR, 50 dipendenti, gestisce mainly onboarding queries".

💡 LEZIONE: La "Definizione di successo" nella persona è uno degli elementi più trascurati. Costringe il PM a rispondere a: "Come saprebbe questa persona che il problema è stato risolto?" È la domanda giusta prima di iniziare a scrivere acceptance criteria.

---

**User Stories:**

🔍 ANNOTAZIONE: US-002 inizia con una Smart View di default. Questa è una scelta di onboarding intelligente: invece di aspettare che l'utente capisca i filtri, il sistema crea valore immediato. La user story cattura questo come requisito esplicito. Se non fosse scritta, probabilmente l'engineering avrebbe saltato il default.

⚠️ ANNOTAZIONE: US-003 specifica "drag-and-drop funziona su desktop (non richiesto su mobile in v1)". Questa esclusione è ottima ma manca la motivazione esplicita. In una review, qualcuno chiederà "perché non mobile?" — la risposta dovrebbe essere nel PRD (probabile risposta: il 92% degli agenti usa desktop, investimento mobile non giustificato in v1).

💡 LEZIONE: Gli acceptance criteria migliori sono quelli che un QA engineer può testare senza fare domande. "La view si salva automaticamente" è testabile. "La view funziona bene" non lo è. Se scrivi un AC e non riesci a immaginare il test case, riscrivi l'AC.

---

**What We're NOT Building:**

🔍 ANNOTAZIONE: Questa sezione è oro puro. Specificare cosa non si costruisce ha tre effetti: 1) protegge il team dallo scope creep durante lo sviluppo, 2) comunica agli stakeholder che queste esigenze sono state considerate (non ignorate), 3) crea il backlog naturale per v2. Ogni PRD dovrebbe avere questa sezione.

💡 LEZIONE: Per ogni feature inclusa in scope, chiediti se c'è una versione più grande che stai deliberatamente escludendo. Se sì, nomina quell'esclusione esplicitamente.

---

**Success Metrics:**

🔍 ANNOTAZIONE: La North Star è una metrica operativa misurabile con timestamp: "entro 60 giorni dal rollout". Non è "migliorare l'esperienza" — è una riduzione del 30% di un tempo specifico. Questo significa che il PM sa già come raccogliere il dato (event tracking sulla conversazione assignment flow).

⚠️ ANNOTAZIONE: Le Counter Metrics sono spesso assenti nei PRD junior. Qui sono presenti e includono una performance metric (tempo di caricamento inbox). Manca però una metrica di adoption per le Smart Views separata dalle Custom Views — le due potrebbero avere adoption molto diversa e il PRD non lo anticipa.

💡 LEZIONE: "Come sappiamo che ha funzionato" non è opzionale. Se non lo scrivi nel PRD, lo scrivi 6 mesi dopo nella post-mortem. Meglio anticiparlo.

---

---

# CASO STUDIO 2: Figma — Feature "Auto Layout"
## [RICOSTRUITO] — PRD plausibile basato su documentazione pubblica e changelog

**Contesto**: Figma ha introdotto Auto Layout nel settembre 2019. La feature risolve un problema fondamentale del design di interfacce: quando il contenuto cambia (un pulsante con testo diverso, una lista con più elementi), i frame non si ridimensionano automaticamente. Il designer doveva ridimensionare manualmente ogni elemento. Auto Layout introduce il concetto di "frame intelligenti" che si ridimensionano automaticamente al cambio del contenuto.

---

```markdown
---
# PRD: Auto Layout — Frame Intelligenti
**Versione**: 3.0 | **Status**: SHIPPED ✅
**Autore**: Product Manager, Core Editor Team
**Data creazione**: Q2 2019 (ricostruzione)
**Revisori**: Engineering Lead, Head of Design, Figma Design Team
**Epic**: Designer Productivity 2019
---

## CHANGE LOG
| Versione | Data  | Modifica                                           | Motivo                                        |
|----------|-------|----------------------------------------------------|-----------------------------------------------|
| 1.0      | +0d   | Draft con auto-resize su tutti gli assi            | —                                             |
| 2.0      | +14d  | Ridotto a resize unidirezionale (v1)               | Complessità tecnica, focus su caso d'uso core |
| 2.1      | +18d  | Aggiunta modalità "hug contents"                  | Feedback designer interni                     |
| 3.0      | +25d  | Definita strategia backward compatibility          | Risk review con engineering                   |

---

## TL;DR

**Cosa è**: Un sistema di layout automatico per i frame Figma che ridimensiona e riposiziona gli elementi figli quando il contenuto cambia.

**Il problema**: Ogni volta che il contenuto cambia (testo più lungo, lista con più elementi, pulsante con icona aggiunta), il designer deve ridimensionare manualmente decine di frame e componenti. Su una schermata complessa questo può richiedere 20-40 minuti di lavoro manuale ripetitivo.

**La soluzione**: Frame che si comportano come layout CSS flexbox — ridimensionamento automatico, spaziatura controllata, direzione configurabile (orizzontale/verticale).

**North Star**: Riduzione del 50% del tempo che i designer passano in "pixel pushing" su resize manuali.

**Time-box**: 16 settimane (Q3 2019) — 4 engineer + 2 designer.

**Filosofia di design**: Auto Layout deve sentirsi come un superpotere, non come una complicazione. Il caso d'uso più semplice (pulsante che cresce col testo) deve funzionare in 2 click.

---

## PROBLEM STATEMENT

### Il Problema
Il design responsive nel mondo reale produce componenti con contenuto variabile: pulsanti con label di lunghezza diversa, card con descrizioni più o meno lunghe, liste con numero di elementi variabile. In Figma, ogni variazione del contenuto richiede ridimensionamento manuale di ogni frame interessato.

**Evidenze concrete**:
- "Pixel pushing" (resize manuale dei frame) è la lamentela #1 negli user interview 2019 con designer professionisti — dato da 45 interviste condotte Q1 2019
- Il task "aggiorna il copy del pulsante in tutti i 40 stati del componente" richiede 35-45 minuti su file complessi — benchmark interno con team di design Figma
- Feature request "auto-resize" ha 3.200+ voti sulla community board di Figma — dato pubblico
- Sketch ha introdotto Smart Layout nel 2019 come risposta alla stessa esigenza — rischio competitivo diretto

### Perché ora
Figma sta crescendo come strumento per design system complessi. I clienti enterprise usano componenti con centinaia di stati. La mancanza di Auto Layout diventa un blocco per adoption nel segmento enterprise.

### Scope decision chiave: v1 vs v2
Il problema completo è "layout automatico 2D" (come CSS Grid). La soluzione v1 è "layout automatico 1D" (come CSS Flexbox). Questa è una scelta deliberata: il caso d'uso più comune (pulsante, lista, navbar) è 1D. Iniziare con 1D permette di risolvere il 70% del problema con il 30% della complessità tecnica.

---

## TARGET UTENTE

### Persona Primaria: Marco, Product Designer Mid-Level
- **Ruolo**: Product Designer in SaaS azienda, lavora su design system condiviso con 3 altri designer
- **Contesto**: Usa Figma 6-8 ore/giorno. Mantiene una libreria di componenti usata da tutto il team. Quando cambia un componente base, deve propagare le modifiche a tutti gli usi.
- **Obiettivo primario**: Fare modifiche ai componenti senza dover sistemare manualmente ogni istanza
- **Frustrazione attuale**: "Cambio il copy del pulsante, poi passo 20 minuti ad aggiustare padding e allineamenti in tutte le varianti"
- **Definizione di successo**: "Aggiorno il testo, il frame si ridimensiona da solo, niente da sistemare"

### Persona Secondaria: Sofia, Junior Designer
- **Ruolo**: Junior designer, 1 anno di esperienza con Figma
- **Contesto**: Usa componenti della libreria aziendale ma non li crea. Customizza componenti per specifici schermi.
- **Obiettivo primario**: Usare i componenti esistenti senza dover capire come sono costruiti internamente
- **Definizione di successo**: "Posso usare il componente senza rompere niente"

### Persona Esclusa (v1): Luca, Motion Designer
- Usa Figma per prototipazione avanzata con animazioni complesse
- Le sue esigenze di layout sono troppo specifiche per essere indirizzate in v1 (nested auto layout con comportamenti custom)
- Non è il target di questa feature — non deve condizionare le decisioni di design

---

## USER STORIES

### Epic US-01: Auto Layout Base
```
US-001 [P0]
Come Product Designer,
voglio applicare Auto Layout a un frame esistente con un shortcut,
in modo da poterlo fare senza interrompere il mio workflow.

Acceptance Criteria:
□ AC-1: Shortcut Shift+A applica Auto Layout al frame selezionato
□ AC-2: Auto Layout disponibile anche dal pannello Design (sezione Frame)
□ AC-3: Frame senza figli: Auto Layout si applica ma non cambia nulla visivamente
□ AC-4: Frame con figli: i figli vengono disposti nella direzione default (orizzontale) con spacing attuale
□ AC-5: L'operazione è undoable con Cmd+Z
```

```
US-002 [P0]
Come Product Designer,
voglio configurare direzione (orizzontale/verticale) e spaziatura tra elementi,
in modo da controllare come il frame organizza i suoi figli.

Acceptance Criteria:
□ AC-1: Panel Auto Layout mostra: Direction toggle (H/V), Gap between items (px), Padding (top/right/bottom/left)
□ AC-2: Cambio di direzione riorganizza i figli immediatamente (no refresh richiesto)
□ AC-3: Gap "Auto" distribuisce lo spazio rimanente ugualmente tra gli elementi (space-between)
□ AC-4: Padding supporta valore singolo (tutti e 4 i lati uguali) e valore custom per ogni lato
□ AC-5: Valori si aggiornano in real-time durante il drag nel canvas
```

```
US-003 [P0]
Come Product Designer,
voglio che il frame si ridimensioni automaticamente quando il testo al suo interno cambia,
in modo da non dover ridimensionare manualmente dopo ogni modifica al copy.

Acceptance Criteria:
□ AC-1: Modalità "Hug contents" (W e H): il frame si ridimensiona per abbracciare il contenuto
□ AC-2: Modalità "Fixed" (W o H): il frame rimane a dimensione fissa, il contenuto si wrappa o tronca
□ AC-3: Resize avviene entro 1 frame di rendering (nessun flickering visibile)
□ AC-4: Se il resize porta il frame fuori dallo schermo (width >viewport), nessun crash — il frame continua a ridimensionarsi
□ AC-5: Il resize è visibile in real-time mentre si digita nel text node
```

```
US-004 [P1]
Come Product Designer,
voglio poter rimuovere Auto Layout da un frame,
in modo da tornare al comportamento standard se ne ho bisogno.

Acceptance Criteria:
□ AC-1: Bottone "Remove Auto Layout" visibile nel panel quando Auto Layout è attivo
□ AC-2: Rimozione mantiene il layout visuale attuale (gli elementi non si spostano)
□ AC-3: La rimozione è undoable
□ AC-4: Rimozione NON cancella il contenuto del frame
```

### Epic US-02: Backward Compatibility
```
US-005 [P0 — CRITICO]
Come utente esistente con file Figma creati prima di Auto Layout,
voglio che i miei file esistenti non cambino comportamento dopo il rilascio,
in modo da non dover correggere lavoro già fatto.

Acceptance Criteria:
□ AC-1: Tutti i frame esistenti senza Auto Layout mantengono il comportamento precedente invariato
□ AC-2: Auto Layout è opt-in: non viene applicato automaticamente a nessun frame esistente
□ AC-3: Le shared libraries esistenti continuano a funzionare senza modifiche
□ AC-4: Figma beta testa la release con 100 file reali di clienti enterprise prima del rollout generale
□ AC-5: Rollout graduale: 10% utenti → 50% → 100% con monitoring tra ogni step
```

---

## DECISIONI DI DESIGN — TRADE-OFF DOCUMENTATI

### Decisione 1: Flexbox 1D in v1, non CSS Grid
**Alternativa considerata**: Implementare subito un sistema 2D (righe + colonne)
**Decisione**: Solo 1D in v1
**Ragionamento**: L'analisi dei file Figma reali mostra che il 73% dei casi d'uso è 1D (liste, navbar, pulsanti). Il 2D richiederebbe 3x il tempo di sviluppo. Rischio: la v1 risolve il 73% del problema, non il 100%.
**Chi decide**: PM + Engineering Lead, approvato da CEO

### Decisione 2: Nessuna migrazione automatica dei frame esistenti
**Alternativa considerata**: Offrire migrazione assistita con "Convert to Auto Layout" automatico
**Decisione**: Solo opt-in manuale
**Ragionamento**: La migrazione automatica ha troppi edge case (frame con posizionamento assoluto complesso, componenti con override). Il rischio di rompere file esistenti supera il beneficio. La frustrazione del "non posso migrare automaticamente" è accettabile; la frustrazione del "Auto Layout ha rotto il mio file esistente" non lo è.

### Decisione 3: Shortcut Shift+A
**Alternativa considerata**: Solo dal menu contestuale
**Decisione**: Shortcut dedicato come prima opzione
**Ragionamento**: Auto Layout è una delle feature più usate dai power user. Il shortcut comunica "questa è una feature di prima classe". Costo: occupa uno shortcut del namespace globale.

---

## SUCCESS METRICS

### North Star
- Riduzione stimata del tempo in "resize manuali": -50% per i designer che adottano Auto Layout (misurato tramite survey, non tracking diretto)

### Primary Metrics
- Adoption 30 giorni: ≥40% degli utenti attivi ha applicato Auto Layout almeno una volta
- Retention della feature: ≥70% degli utenti che la usano una volta la riusa nella settimana successiva (sticky feature)
- Community feedback: Net Sentiment sulla feature ≥ +60 (analisi manuale dei commenti Twitter/community)

### Counter Metrics
- Crash rate post-release: nessun aumento rispetto alla baseline (Auto Layout è un'operazione sul canvas — potenziale crash point)
- Support tickets su "Auto Layout ha rotto il mio file": <0.5% degli utenti attivi nel primo mese
- Regressione su performance del canvas: nessun aumento del tempo di rendering P95 >15%

---
```

---

### Annotazioni — Caso Studio Figma

---

**Scope Decision (v1 vs v2):**

🔍 ANNOTAZIONE: La sezione "Scope decision chiave: v1 vs v2" all'interno del Problem Statement è insolita ma preziosa. Figma ha preso una decisione tecnica enorme (1D invece di 2D) e l'ha documentata nel PRD con un numero: "70% del problema con 30% della complessità". Questo numero rende la decisione difendibile. Senza questo numero, la decisione sembra arbitraria.

💡 LEZIONE: Ogni decisione di scope ha un costo e un beneficio. Il PRD deve quantificare entrambi. "Risolviamo X% del caso d'uso con Y% della complessità" è il formato corretto. Non lo sai esattamente? Stima. Una stima documentata è meglio del nulla.

---

**Persona Esclusa:**

🔍 ANNOTAZIONE: La "Persona Esclusa" è un pattern poco usato ma molto potente. Nomina esplicitamente chi NON è il target, e perché. Questo impedisce che durante il design review qualcuno dica "ma e per i motion designer?". La risposta è già nel PRD: non è il loro target per questa feature.

💡 LEZIONE: Per ogni persona target, c'è almeno una persona non-target. Nominarla esplicitamente chiude un ciclo di discussioni infinite.

---

**Backward Compatibility (US-005):**

🔍 ANNOTAZIONE: US-005 è marcato [P0 — CRITICO] e include un acceptance criteria di processo (beta test con 100 file reali) e uno di rollout (graduale 10% → 50% → 100%). Questo è raro nei PRD: include requisiti sul processo di lancio, non solo sulla feature. Ma ha senso — Figma ha milioni di file esistenti. Una regressione sarebbe catastrofica.

⚠️ ANNOTAZIONE: Manca un piano di rollback. Se il monitoring tra 10% e 50% mostra problemi, chi decide se fermare il rollout? Con quale soglia? Un PRD maturo avrebbe una sezione "Rollback Plan".

💡 LEZIONE: Per feature che toccano comportamenti esistenti (backward compatibility risk), il PRD deve includere la strategia di rollout. "Si lancia e si vede" non è una strategia — è una speranza.

---

**Decisioni di Design documentate:**

🔍 ANNOTAZIONE: La sezione "Decisioni di Design — Trade-off documentati" è uno degli elementi più maturi di questo PRD. Ogni decisione ha: alternativa considerata, decisione presa, ragionamento con dati, chi ha approvato. Questo documento ha valore doppio: guida il presente e documenta il passato (tra 6 mesi qualcuno chiederà "perché non facciamo Grid?" — la risposta è già qui).

💡 LEZIONE: I trade-off documentati trasformano un PRD da specifica a knowledge base. Nel lungo periodo questo è uno degli investimenti più preziosi che un PM può fare.

---

---

# CASO STUDIO 3: Notion — Feature "Databases"
## [RICOSTRUITO] — PRD plausibile basato su documentazione pubblica e release notes 2019

**Contesto**: Notion ha introdotto i database nella versione 2.0 (2019). Era una delle aggiunte più ambiziose nella storia del prodotto: non solo aggiungeva una nuova feature, ma cambiava il posizionamento di Notion da "note-taking tool" a "all-in-one workspace". Il database di Notion non è solo una tabella — è un contenitore di pagine con proprietà tipizzate, views multiple e filtri.

---

```markdown
---
# PRD: Notion Databases — v1 Foundation
**Versione**: 4.0 | **Status**: SHIPPED ✅
**Autore**: Product Team, Notion
**Data creazione**: Q3-Q4 2018 (ricostruzione — sviluppo lungo 9 mesi)
**Epic**: Notion 2.0 — "The All-In-One Workspace"
---

## TL;DR

**Cosa è**: Un sistema di database relazionale integrato nell'editor Notion, che permette di organizzare pagine come righe di una tabella con proprietà tipizzate (testo, numero, data, select, multi-select, checkbox, URL, persona).

**Il problema**: Gli utenti power user di Notion hanno bisogno di organizzare informazioni strutturate. Le note e le pagine esistenti sono troppo poco strutturate per casi d'uso come CRM, project tracker, content calendar. Questi utenti usano Notion + Airtable + Trello in parallelo.

**La soluzione**: Un database direttamente dentro Notion, con multiple views (tabella, kanban, calendario, lista, galleria) e la possibilità di linkare database tra loro.

**North Star**: Notion diventa lo strumento principale per almeno un use case "strutturato" per ≥30% degli utenti attivi mensili.

**Ambizione di lungo termine**: Notion databases deve poter sostituire Airtable per il 90% dei casi d'uso mainstream.

**Time-box**: 9 mesi — team di 8-10 persone.

---

## PROBLEM STATEMENT

### Il Problema
Gli utenti più attivi di Notion sono knowledge workers che combinano note (documenti liberi) con tracking strutturato (task, progetti, CRM). In Notion v1, il tracking strutturato è impossibile: non ci sono tabelle con proprietà tipizzate, non c'è kanban, non c'è filtering.

**Evidenze**:
- Top 5 richieste di feature in ordine: 1) Database/spreadsheet, 2) Kanban board, 3) Calendar view, 4) Relazioni tra pagine, 5) Filtri avanzati — tutti e 5 sono risolvibili con una sola feature: i database
- 68% degli utenti pro usa Airtable o Trello in parallelo a Notion per gestire "cose strutturate" — dato survey interna
- NPS dei power user (top 20% per engagement) è 20 punti sotto il NPS degli utenti normali — il motivo principale citato nelle interviste: "Mancano i database"
- Il segmento "team" (più pagante) abbandona Notion per Airtable nel 34% dei casi di churn — dato sales

### Definizione del problema in una frase
**"Notion è straordinario per il pensiero libero. È inutilizzabile per il pensiero strutturato."**

### Perché questo è risolvibile ora
Il team ha 2 anni di esperienza con l'architettura dell'editor Notion (blocchi). I database possono essere implementati come tipo di blocco speciale — si integrano naturalmente nel sistema esistente senza refactoring dell'architettura.

---

## SCOPE: V1 vs "TUTTO"

Questa feature è un universo. Il PRD v1 copre deliberatamente il 40% del potenziale.

### V1 include (SHIPPED):
- Tipi di proprietà: Testo, Numero, Data, Select, Multi-Select, Checkbox, URL, Email, Persona
- Views: Tabella, Kanban (su property Select), Calendario (su property Data), Lista, Galleria
- Filtering e sorting base per ogni view
- Relazioni semplici tra database nella stessa workspace
- Rollup (calcoli aggregati su relazioni): CONTEGGIO, SOMMA, MEDIA, MIN, MAX

### V2 (roadmap approvata, non in scope v1):
- Formula columns (calcoli custom)
- Views linkate (stesso database, view diversa, in pagine diverse)
- Database templates
- Permessi granulari per singola colonna
- API per database

### MAI in scope (decisione strategica, non temporanea):
- Multi-workspace relations: i database restano isolati per workspace. Cross-workspace sarebbe un problema di sicurezza impossibile da risolvere in modo user-friendly.
- Real-time collaborative editing su celle: troppo complesso per v1 (conflict resolution su struttura tabellare è diverso da conflict resolution su testo).

---

## FILOSOFIA DI DESIGN — 3 PRINCIPI GUIDA

### Principio 1: Il database è prima di tutto una raccolta di pagine
Ogni riga di un database Notion è una pagina completa con contenuto libero. Non è solo una riga di dati. Questo distingue Notion da Airtable: in Airtable una riga è solo dati strutturati; in Notion una riga è un documento con dati strutturati come metadati.

**Implicazione sul design**: Il click su una riga apre la pagina, non una modale di editing. Il database è la vista strutturata di un insieme di pagine.

### Principio 2: Stesso database, views diverse
I dati esistono una volta. Le views sono solo modi di visualizzarli. Aggiungendo una proprietà in tabella, quella proprietà appare anche in kanban e calendario. Non esistono "dati della view tabella" e "dati della view kanban" — esiste solo il database.

**Implicazione sul design**: Tutta l'UI deve comunicare che si sta guardando la stessa cosa da angolazioni diverse.

### Principio 3: Complessità nascosta, non complessità rimossa
Il database di Notion deve sembrare semplice al primo uso, ma supportare casi d'uso sofisticati per i power user. Non si tratta di semplificare le feature — si tratta di rendere le feature complesse accessibili solo a chi ne ha bisogno.

**Implicazione sul design**: La creazione di un database mostra prima i tipi di proprietà più semplici (Testo, Numero, Checkbox). I tipi avanzati (Formula, Rollup) sono accessibili ma non in first view.

---

## SUCCESS METRICS

### Funnel di adoption
```
Step 1: Crea almeno 1 database → target ≥25% degli utenti pro entro 30 giorni
Step 2: Aggiunge almeno 5 righe → target ≥60% di chi ha fatto Step 1
Step 3: Crea almeno 2 views diverse → target ≥40% di chi ha fatto Step 2
Step 4: Usa il database ogni settimana per 4+ settimane → target ≥50% di chi ha fatto Step 3
```

### Business metrics
- Churn nel segmento "team" che va verso Airtable: -25% entro 6 mesi post-lancio
- Conversione free → pro: +15% entro 3 mesi (hypothesis: database è killer feature per conversione)
- NPS power user: +15 punti entro 6 mesi

### Segnale negativo da monitorare
- "Database confusion": % di utenti che crea un database e poi lo elimina entro 7 giorni → target <15%. Sopra questa soglia significa che il onboarding non funziona.

---
```

---

### Annotazioni — Caso Studio Notion

---

**"Definizione del problema in una frase":**

🔍 ANNOTAZIONE: "Notion è straordinario per il pensiero libero. È inutilizzabile per il pensiero strutturato." Questa frase vale l'intero Problem Statement. È il tipo di sintesi che un CEO capisce in 3 secondi, che un engineer può tenere a mente mentre sviluppa, e che un marketer può trasformare in copy. Non ogni PRD ha bisogno di questa frase, ma ogni PM dovrebbe cercarla.

💡 LEZIONE: Il Problem Statement deve avere una frase sintetica che cattura l'essenza. Tutto il resto è supporto a quella frase. Se non riesci a sintetizzare il problema in una frase, non lo hai capito abbastanza bene.

---

**Scope V1 vs "TUTTO":**

🔍 ANNOTAZIONE: La sezione di scope è articolata in tre livelli: "V1 include", "V2 roadmap", "MAI in scope". Il terzo livello è eccezionale: dice esplicitamente cosa non verrà MAI costruito e perché. "Multi-workspace relations: i database restano isolati per workspace. Cross-workspace sarebbe un problema di sicurezza impossibile da risolvere in modo user-friendly." Questo chiude una discussione per sempre — non per questa release, ma come decisione strategica.

⚠️ ANNOTAZIONE: Il V1 include cose molto ambiziose (5 tipi di views, relazioni, rollup). In retrospettiva, forse V1 era già troppo grande. Un PRD più rigoroso avrebbe separato "views" e "relazioni" in epic separati con ship date diverse. Ma Notion aveva la luxury di un lungo ciclo di sviluppo (9 mesi) che permetteva questo scope.

💡 LEZIONE: La categoria "MAI in scope" è diversa dalla categoria "non in V1". Usala quando hai una ragione strategica o tecnica definitiva. Non come scusa per non fare qualcosa — come comunicazione di una scelta deliberata.

---

**Filosofia di Design (3 principi guida):**

🔍 ANNOTAZIONE: I tre principi di design non sono requisiti funzionali — sono linee guida filosofiche. Cosa distingue questa sezione da contenuto generico: ogni principio ha una "Implicazione sul design" concreta. Non dice "sii semplice" — dice "il click su una riga apre la pagina, non una modale". L'implicazione pratica rende il principio utile.

💡 LEZIONE: I principi di design senza implicazioni pratiche sono decorazioni. Per ogni principio, scrivi "implicazione sul design: X". Se non riesci a scrivere l'implicazione, il principio non è abbastanza specifico.

---

**Funnel di Adoption:**

🔍 ANNOTAZIONE: Il funnel di adoption in 4 step è un modo sofisticato di misurare il successo. Non è solo "quanti utenti usano i database" — è un funnel che misura la profondità dell'adozione. Step 4 (usa ogni settimana per 4+ settimane) è la vera metrica di "feature sticky". Arrivare a Step 1 senza arrivare a Step 4 significa che la feature non ha risolto il problema abbastanza bene.

💡 LEZIONE: Per feature complesse (alto time-to-value), le metriche di adoption devono essere a funnel, non binarie. "X% degli utenti ha usato la feature" non ti dice se la feature ha creato valore — ti dice se qualcuno l'ha toccata una volta.

---

---

# CASO STUDIO 4: Linear — Feature "Cycles"
## [RICOSTRUITO] — PRD plausibile basato su documentazione pubblica e blog posts

**Contesto**: Linear è un issue tracker per team di engineering. I Cycles sono la versione Linear degli "sprint" agile — ma con alcune differenze filosofiche deliberate rispetto agli sprint classici di Jira/Scrum. Linear ha lanciato Cycles nel 2021, dopo aver analizzato perché gli sprint in Jira vengono spesso abusati o ignorati dai team.

---

```markdown
---
# PRD: Cycles — Sprint Semplificati per Team di Engineering
**Versione**: 2.0 | **Status**: SHIPPED ✅
**Autore**: Product Team, Linear
**Data creazione**: Q2 2021 (ricostruzione)
**Filosofia guida**: Opinionated by design.
---

## TL;DR

**Cosa è**: Un sistema di cicli di lavoro a tempo fisso integrato in Linear, che raggruppa issues per periodi definiti (default: 2 settimane) e mostra progress, velocity, e burndown.

**Il problema**: I team di engineering non riescono a pianificare il lavoro su orizzonti brevi (2-4 settimane) senza strumenti dedicati. Le soluzioni esistenti (Jira Sprint, Scrum classico) sono o troppo complesse o mal integrate con il workflow quotidiano.

**La soluzione**: Cycles leggeri, direttamente integrati nel workflow Linear esistente. Non è Scrum — è la versione Linear del ritmo di lavoro.

**Filosofia**: Linear non costruisce feature generiche. Costruisce feature opinionated. Cycles non cerca di supportare ogni variante di agile — supporta il modo in cui i team moderni (non enterprise legacy) vogliono lavorare.

**North Star**: ≥50% dei team Linear attivi usa Cycles ogni settimana entro 6 mesi dal lancio.

---

## PROBLEM STATEMENT

### Il Problema
I team di engineering tra 3-20 persone hanno bisogno di ritmo. Non di processo pesante — di ritmo. Un ciclo di 2 settimane in cui si decide cosa si fa, si lavora, si mostra il risultato. Questo ritmo esiste informalmente in molti team, ma senza strumento dedicato viene dimenticato, saltato, o diventa burocratico quando si cerca di implementarlo con Jira.

**Evidenze**:
- 72% dei team Linear intervistati ha un concetto di "sprint" anche se non lo chiama così — dato da 60 customer interviews Q1 2021
- "Come fate a sapere cosa fare questa settimana?" — risposta comune: "abbiamo un doc Google, o uno Slack canvas, o non lo sappiamo bene" — qualitative pattern da interviews
- Feature request "sprints/cycles" è la #2 assoluta in Linear dopo "roadmap" — dato community

### Cosa non vogliamo costruire
Questa sezione viene prima delle user stories deliberatamente.

Linear non costruirà:
- Sprint planning ceremonies integrate nello strumento
- Story point obbligatori
- Sprint review workflow
- Velocity come metrica di performance (solo come informazione)
- Impedance log (troppo Scrum)
- Sprint retrospective structure

**Perché queste esclusioni sono filosofiche, non temporanee**: Il rituale Scrum ha reso gli sprint una fonte di overhead burocratico per molti team. Linear non vuole replicare questo problema. Cycles è agile nella sostanza (ritmo + focus), non nella forma (cerimonie + metriche di performance).

---

## TARGET UTENTE

### Persona Primaria: Luca, Engineering Manager di team 8 persone
- **Ruolo**: EM in startup Serie A, team di 8 engineer + 1 designer
- **Contesto**: Usa Linear quotidianamente per issue tracking. Non usa Jira perché "troppo pesante". Cerca un modo per dare ritmo al team senza introdurre overhead di processo.
- **Obiettivo primario**: Il team sa cosa sta lavorando questa settimana e la prossima senza dover fare planning meeting di 2 ore
- **Frustrazione attuale**: "Abbiamo un notion doc con 'sprint 23' ma nessuno lo aggiorna davvero. I cicli finiscono e non sappiamo mai cosa è rimasto indietro."
- **Definizione di successo**: "Apro Linear, vedo il ciclo corrente, vedo cosa è rimasto dell'estimate, capisco se siamo in ritardo"

### Persona Secondaria: Anna, Senior Engineer
- **Ruolo**: Senior engineer che contribuisce attivamente alla pianificazione
- **Contesto**: Vuole sapere cosa è in scope per questa settimana senza dover chiedere al manager
- **Obiettivo primario**: Focus — lavorare sulle cose giuste senza distrazione da issues non prioritari del ciclo
- **Definizione di successo**: "Apro Linear, vedo i miei issue nel ciclo corrente, lavoro su quelli"

---

## USER STORIES

### Epic US-01: Creazione e Gestione Cycles
```
US-001 [P0]
Come Engineering Manager,
voglio creare un Cycle con data start e data end,
in modo da definire un periodo di lavoro con confini chiari.

Acceptance Criteria:
□ AC-1: Creazione Cycle dal sidebar con nome auto-generato (es: "Cycle 1") modificabile
□ AC-2: Data start e data end obbligatorie — la durata default è 2 settimane
□ AC-3: Un solo "Active Cycle" per team alla volta (Cycles passati e futuri possono coesistere)
□ AC-4: Il Cycle corrente è evidenziato in sidebar con indicatore visivo "ACTIVE"
□ AC-5: La durata default è configurabile nelle impostazioni team (1-6 settimane) — non per singolo Cycle
```

```
US-002 [P0]
Come Engineering Manager,
voglio aggiungere issues esistenti al Cycle corrente,
in modo da definire lo scope di lavoro del periodo.

Acceptance Criteria:
□ AC-1: Issues aggiungibili al Cycle tramite drag-and-drop dalla issue list
□ AC-2: Issues aggiungibili al Cycle tramite il pannello laterale dell'issue (campo "Cycle")
□ AC-3: Issues aggiungibili in bulk dalla issue list (multi-select + bulk action "Add to cycle")
□ AC-4: Un issue può essere in un solo Cycle attivo alla volta (non in due Cycles sovrapposti)
□ AC-5: Issues completate PRIMA dell'inizio del Cycle possono essere aggiunte come "completed"
```

```
US-003 [P1]
Come Engineering Manager,
voglio vedere il progress del Cycle in tempo reale (% completato, issue rimanenti),
in modo da capire se il team è in track per completare lo scope entro la fine del Cycle.

Acceptance Criteria:
□ AC-1: Progress bar nella view Cycle: X/Y issues completate
□ AC-2: Scope indicator: issues aggiunte DOPO l'inizio del Cycle sono marcate "added mid-cycle" (scope creep indicator)
□ AC-3: Burndown chart semplice: issues rimanenti per giorno del Cycle
□ AC-4: Burndown NON usa story points come unità — usa conteggio issues (Linear è opinionated: no points)
□ AC-5: "At risk" indicator automatico: se entro metà Cycle è completato <30% delle issues → warning visivo
```

### Epic US-02: Chiusura e Carryover
```
US-004 [P0 — OPINIONATED]
Come Engineering Manager,
voglio che le issues incomplete alla fine del Cycle vengano gestite con un workflow esplicito,
in modo da non perdere il lavoro non completato ma anche non spostarlo automaticamente.

Acceptance Criteria:
□ AC-1: Alla scadenza del Cycle, Linear mostra un modal "Cycle ended — X issues incomplete"
□ AC-2: Il modal offre 3 opzioni per ogni issue incompleta: "Move to next Cycle", "Move to Backlog", "Keep in current Cycle" (per Cycles estesi manualmente)
□ AC-3: NON esistono "auto-rollover" — ogni issue incompleta richiede una decisione esplicita
□ AC-4: La decisione può essere presa in bulk ("Move all to next Cycle")
□ AC-5: Le issues "moved to next cycle" mantengono la loro history — si vede che erano nel Cycle precedente

[NOTA DI DESIGN]: Il no-auto-rollover è una scelta filosofica deliberata. In Jira, le issues si rollano automaticamente al prossimo sprint e nessuno le nota mai. Linear forza una decisione consapevole. Questo introduce un piccolo overhead ma crea consapevolezza sul lavoro che non viene completato.
```

---

## SCELTE FILOSOFICHE — PERCHÉ LINEAR NON FA X

Questa sezione esiste perché Linear riceverà feedback del tipo "perché non avete fatto Y come Jira?". Le risposte sono documentate qui.

| Feature richiesta | Perché Linear non la fa | Decisione |
|-------------------|------------------------|-----------|
| Story Points | Richiede stima upfront che spesso non vale il tempo investito. Linear usa "issue count" come proxy. | Permanente |
| Sprint Planning ceremony | Linear non gestisce meeting — gestisce issues. Lo strumento supporta la pianificazione, non la sostituisce. | Permanente |
| Sprint Velocity come KPI manager | La velocity come metrica di performance crea gaming (gli engineer inflano le stime per sembrare più veloci). | Permanente |
| Sprint capacity planning | Utile ma complessità alta. I team che ne hanno bisogno sono enterprise — non è il target core di Linear v1 Cycles. | V2 possibile |
| Nested sprints (sprint di team + sprint di singola persona) | Complessità di modeling eccessiva per il value. | Permanente |

---

## SUCCESS METRICS

### Adoption
- ≥50% dei team Linear attivi crea almeno 1 Cycle entro 30 giorni dal lancio
- ≥60% dei team che creano un Cycle ne crea un secondo (ripetibilità = ritmo)
- ≥40% dei team usa Cycles ogni settimana per 8+ settimane consecutive (sticky rhythm)

### Quality
- NPS sulla feature: ≥60 (survey in-app 30 giorni post-lancio)
- Support tickets su "come funzionano i Cycles": <2% degli utenti attivi nel primo mese

### Segnale di rischio
- Team che creano Cycles ma non aggiungono issues (Cycle vuoto): se >30% → onboarding non funziona
- Team che abbandonano Cycles dopo il secondo (completano 2 cicli e smettono): se >40% → la feature non crea ritmo reale

---
```

---

### Annotazioni — Caso Studio Linear

---

**"Cosa non vogliamo costruire" prima delle user stories:**

🔍 ANNOTAZIONE: Linear mette "Cosa non costruiremo" PRIMA delle user stories. Questo è un pattern insolito e potente. Di solito le esclusioni di scope vengono alla fine come "out of scope". Linear le mette davanti perché le esclusioni sono filosofiche — definiscono cosa è Linear. Mettendole prima, chiunque legga il PRD capisce subito il punto di vista prima di leggere le specifiche.

💡 LEZIONE: Quando le esclusioni di scope sono filosofiche (non solo temporanee), mettile vicino al Problem Statement, non alla fine. Comunicano l'identità del prodotto, non solo i confini di una release.

---

**Nota di Design inline nelle User Stories:**

🔍 ANNOTAZIONE: US-004 include una [NOTA DI DESIGN] direttamente all'interno dell'acceptance criteria: "Il no-auto-rollover è una scelta filosofica deliberata. In Jira, le issues si rollano automaticamente al prossimo sprint e nessuno le nota mai." Questa nota spiega il PERCHÉ di un acceptance criteria specifico. È insolito vederlo nel formato user story, ma è prezioso — chi implementa capisce che non è un caso, è una scelta.

💡 LEZIONE: Gli acceptance criteria descrivono il COSA. Le note di design spiegano il PERCHÉ. Quando un AC è controintuitivo o va contro la convenzione di mercato, aggiungi una nota di design. Risparmia settimane di discussioni future.

---

**Tabella "Perché Linear non fa X":**

🔍 ANNOTAZIONE: La tabella delle scelte filosofiche è un documento politico oltre che tecnico. Quando arriveranno le richieste (e arriveranno: "ma Jira ha i story points!"), questa tabella è la risposta. La colonna "Decisione" distingue tra "Permanente" e "V2 possibile" — questo è importante: non tutte le esclusioni hanno lo stesso peso.

⚠️ ANNOTAZIONE: La colonna manca del "dato o evidence" che supporta la scelta. "Story Points: richiede stima upfront che spesso non vale il tempo investito" — questo è un'opinione, non un dato. Un PRD più rigoroso citerebbe evidence (ricerca, interviste, letteratura agile).

💡 LEZIONE: I prodotti opinionated hanno più engagement e più detractor. Documentare le scelte filosofiche protegge il team dai detractor e ispira i fan. Un PM opinionated che documenta il ragionamento è più credibile di un PM che accontenta tutti senza coerenza.

---

---

# LEZIONI TRASVERSALI
## 10 Principi che Emergono dall'Analisi dei 4 Casi

---

### Principio 1: Il Problem Statement è l'investimento più ad alto ROI di tutto il PRD

Ogni PRD analizzato dedica una quantità sproporzionata di spazio al problema rispetto alla soluzione. Non è un caso. Un problem statement forte rende le decisioni di scope automatiche: se una feature non risolve il problema definito, non va inclusa.

**Pattern comune**: Ogni PRD usa almeno 2-3 fonti diverse per supportare il problem statement (survey, interviste, dati di prodotto, metriche di churn). La convergenza di fonti diverse rende il problema inattaccabile.

**Applicazione pratica**: Prima di scrivere qualsiasi user story, chiediti: "Se domani il problem statement cambiasse, quali user stories eliminerei?" Se la risposta è "nessuna", le user stories non sono abbastanza derivate dal problema.

---

### Principio 2: Le esclusioni di scope valgono quanto le inclusioni

La sezione "What we're NOT building" appare in tutti e 4 i casi. Non è burocratica — è strategica. Serve a tre scopi simultaneamente:
1. Protegge il team durante lo sviluppo
2. Comunica che le esigenze escluse sono state considerate (non ignorate)
3. Costruisce il backlog naturale per v2

**Differenza importante**: alcune esclusioni sono temporanee (v2), altre sono filosofiche (permanenti). La distinzione deve essere esplicita.

---

### Principio 3: Le personas hanno sempre una "Definizione di successo"

Non "cosa fa questa persona" o "che lavoro ha questa persona" — ma "come saprebbe questa persona che il suo problema è risolto?" Questa domanda sposta la prospettiva dal descrittivo al predittivo.

Il criterio di successo della persona diventa il test di accettazione informale della feature: "Se Laura può aprire Linear e sapere cosa fare questa settimana senza chiedere al manager, la feature ha funzionato."

---

### Principio 4: I trade-off documentati hanno valore che cresce nel tempo

I PRD di Figma e Linear documentano esplicitamente le decisioni prese e le alternative considerate. Non è overhead — è un investimento in conoscenza istituzionale. Tra 12 mesi, quando un nuovo engineer chiede "perché non abbiamo fatto Grid?", la risposta è nel PRD. Senza documentazione, quella conoscenza vive solo nella testa di chi era in sala.

---

### Principio 5: Le Counter Metrics sono la prova di maturità del PM

Tutti e 4 i PRD includono metriche da monitorare per rilevare regressioni. Non solo "cosa deve migliorare" ma "cosa non deve peggiorare". I PM junior tracciano solo i successi. I PM senior tracciano anche i rischi.

Esempio pratico: Linear traccia "team che creano Cycles vuoti" come segnale di rischio di onboarding fallito. Questa metrica non si trova guardando i numeri di adoption — si trova solo se il PM ha pensato al failure mode prima del lancio.

---

### Principio 6: La North Star Metric è misurabile con timestamp

"Migliorare l'esperienza" non è una North Star. "Riduzione del 30% del tempo da conversazione non assegnata a primo tocco entro 60 giorni dal rollout" è una North Star. La differenza: ha un numero, ha un termine di paragone, ha un deadline.

Se non riesci a scrivere la North Star Metric in questa forma, non hai ancora definito il successo abbastanza precisamente.

---

### Principio 7: Il rollout è parte del PRD, non un problema da risolvere dopo

Figma include acceptance criteria di processo (beta test con 100 file reali) e di rollout (10% → 50% → 100% con monitoring). Questo è raro ma importante per feature con backward compatibility risk.

Regola pratica: per ogni feature che tocca comportamenti esistenti, il PRD deve avere una sezione "Rollout Strategy" con almeno: piano graduale, soglie di monitoring, criteri per procedere allo step successivo.

---

### Principio 8: La filosofia di design si traduce sempre in implicazioni pratiche

Notion documenta 3 principi filosofici. Ma ogni principio ha una "Implicazione sul design" concreta. Linear documenta una posizione filosofica su Scrum, e la traduce in acceptance criteria specifici (no auto-rollover, no story points, no velocity come KPI).

La filosofia senza implicazioni pratiche è decorazione. Le implicazioni senza filosofia sono liste di feature senza coerenza. Il PRD maturo ha entrambe, collegate.

---

### Principio 9: L'adoption funnel è più informativo dell'adoption rate

L'adoption rate (% di utenti che usa la feature) è utile ma superficiale. L'adoption funnel (quanti arrivano a step 1, quanti a step 2, quanti a step 4) rivela dove il valore si rompe. Notion misura 4 step di profondità nell'uso dei database. Questo permette di identificare il punto di drop-off e di intervenire specificamente lì.

---

### Principio 10: Il PRD è un documento vivo — il change log lo dimostra

Tutti e 4 i PRD hanno un change log con versioni. Non è formalismo — è evidenza che il PRD è stato aggiornato man mano che la conoscenza cresceva. Un PRD senza change log è un PRD che è stato scritto e dimenticato.

La versione 1.0 di un PRD contiene sempre delle assunzioni sbagliate. La domanda non è se ci saranno cambiamenti — è se saranno documentati.

---

---

# BENCHMARK QUALITATIVO
## Cosa distingue un PRD di Tier 1 da un PRD mediocre

| Aspetto | PRD mediocre | PRD di successo | Differenza chiave |
|---------|-------------|-----------------|-------------------|
| Problem Statement | "Gli utenti hanno difficoltà con X" | "Il 72% degli utenti [fonte] perde Y tempo su Z, causando churn nel segmento [dato]" | La fonte e il numero trasformano un'opinione in evidenza |
| Persona | "Designer, 25-40 anni, usa Figma" | Persona con ruolo specifico, contesto, obiettivo primario, frustrazione attuale, definizione di successo | La definizione di successo trasforma la persona da descrittiva a predittiva |
| User Stories | "L'utente può filtrare le conversazioni" | User story As a/I want/So that con acceptance criteria binari e testabili | Gli AC devono poter essere testati senza fare domande |
| Scope | Lista di feature da fare | Include/exclude/never con ragioni esplicite per ogni categoria | Il "never" filosofico è diverso dal "non in v1" temporaneo |
| Metriche | "Aumentare l'engagement" | North Star con numero, baseline, deadline + counter metrics per regressioni | Le counter metrics sono la firma dei PM senior |
| Trade-off | Decisioni implicite non documentate | Ogni decisione non ovvia ha: alternativa considerata, scelta, ragionamento, chi ha approvato | Il valore cresce nel tempo — chi arriverà dopo capirà il perché |
| Backward compatibility | Trattata come problema da risolvere in sviluppo | US dedicata con rollout graduale e monitoring in acceptance criteria | La BC è un requisito funzionale, non un'attività di deployment |
| Filosofia di design | Assente o generica ("sii semplice") | Principi con implicazioni pratiche concrete | Un principio senza implicazione è decorazione |
| Versionamento | Documento statico, nessun change log | Change log con ogni versione: cosa è cambiato e perché | Dimostra che il PRD è vivo e che le assunzioni vengono aggiornate |
| Tono | Neutro, tecnico, impersonale | Opinionated, con voice del prodotto, con position chiara su cosa è in e fuori | I PRD con voice forte generano team più allineati |
