# Reference — Linee Guida Monetizzazione YouTube & Reused Content

> Conoscenza on-demand per `video-producer`, `script-writer`, `niche-scout`. 
> Obiettivo: Prevenire il rifiuto della monetizzazione da parte del Programma Partner di YouTube (YPP).

---

## 1. Il Rischio: "Contenuti Ripetitivi" e "Contenuti Riutilizzati"
I canali facenti uso di YouTube Automation corrono spesso il rischio di essere demonetizzati o non ammessi al programma YPP con due causali principali:
1. **Reused Content (Contenuti Riutilizzati):** Pubblicare video che riutilizzano materiale altrui senza aggiungervi commento originale, valore educativo significativo o un editing trasformativo profondo.
2. **Repetitive Content (Contenuti Ripetitivi):** Contenuti che sono così simili tra loro che gli spettatori faticano a distinguerli (es. stessi modelli video AI, stock video usati nello stesso ordine, voci sintetiche identiche prive di espressività).

---

## 2. Invarianti di Conformità (Come essere ammessi alla monetizzazione)

Per certificare la conformità del video, applica rigorosamente le seguenti regole in fase di sceneggiatura e produzione:

### A. Sceneggiatura Trasformativa (Per lo `script-writer`)
* **Commento Critico Originale:** Lo script non deve essere una traduzione letterale o un riassunto pigro. Deve includere tesi, analisi, commenti originali e riorganizzare le informazioni con un proprio "punto di vista" (segnalato con il marcatore `➕` per tracciare le espansioni originali).
* **Struttura Narrativa Fluida:** Evitare pattern di testo prefabbricati o introduzioni ripetitive uguali su tutti i video del canale.

### B. Produzione Premium (Per il `video-producer` e `qa-audio-video`)
* **Uso Moderato di Stock Footage:** Non affidarsi esclusivamente a clip di archivio predefinite inserite in modo sequenziale. Sovrapponi elementi grafici, grafici animati, screenshot, estratti di notizie e zoom/pan continui per rendere il montaggio dinamico.
* **Voce Narrante di Alta Qualità:** Scegli le voci più umane ed espressive disponibili su Fliki. Evita voci piatte e metalliche (inserisci pause e modulazioni, vedi [fliki-avanzato.md](fliki-avanzato.md)).
* **Cura Estetica dei Sottotitoli:** Non usare sottotitoli standard noiosi. Devono essere dinamici, colorati ed evidenziare le parole chiave principali.
* **Editing Audio Stratificato:** Usa effetti sonori (SFX) per sottolineare i passaggi chiave e le transizioni. La musica non deve essere una singola traccia ripetuta all'infinito senza pause.

---

## 3. Checklist di Conformità per la Fabbrica
- [ ] Il video aggiunge commento critico o valore educativo rispetto alla fonte originale?
- [ ] Il montaggio include zoom, transizioni curate, SFX e overlay grafici (non solo stock video passivi)?
- [ ] La voce narrante selezionata è tra quelle certificate ad alta espressività e non presente nella blacklist di `learned_rules.json`?
- [ ] Il video si distingue nettamente dagli altri video pubblicati sul canale per stile visivo o focus argomentativo?
- [ ] **Nessun fotogramma proviene dal video sorgente** (§4)?

---

## 4. Il «metodo copia e incolla»: perché è una porta chiusa (A4-L06-02 · 2026-09-05)

Esiste un metodo diffuso — insegnato per intero nel corso AI TUBE PRO (A4/L06) — che consiste nel
**scaricare il video altrui e ripubblicarlo modificato**: si rimuove la traccia audio, si traduce
lo script, si rifà il voiceover, si cambia la musica, **si toglie il logo e si rifanno i testi a
schermo**, si riordinano le clip e se ne sostituiscono alcune con materiale da Envato o Pexels.
La difesa dichiarata è: «così **non incorriamo in strike**».

**La nostra fabbrica non lo fa, e non è una questione di gusto.** Tre ragioni, in ordine di peso:

1. **Quella difesa è contro la macchina, non contro il diritto.** Cambiare audio, ordine e grafica
   serve a non farsi riconoscere dal **Content ID**, che è un sistema di identificazione
   automatica: identifica, non stabilisce chi ha ragione. Un titolare può agire anche su un'opera
   modificata. **Non essere riconosciuti** ed **essere in regola** sono due cose diverse, e il
   metodo le confonde per tutta la lezione.
2. **Il «fair use» viene citato come se fosse una regola di YouTube.** Non lo è: è una dottrina
   del diritto **statunitense**, valutata da un giudice su quattro fattori, caso per caso.
   L'ordinamento italiano non ha un equivalente altrettanto largo. Costruire un modello di
   business su un istituto straniero frainteso è il rischio più grosso dell'intero metodo.
3. **È lavoro manuale, e cancella l'automazione.** Togliere un logo, rifare ogni testo a schermo,
   riordinare le clip e sostituirne alcune sono operazioni da editor video, **una per una, su ogni
   video**. La nostra catena genera via API senza aprire un browser: quel passaggio non solo non
   conviene, **non è eseguibile**.

**Cosa si prende invece, e non è poco:** l'**idea validata**. Che un format abbia funzionato — in
italiano o in un'altra lingua — è il segnale più economico che esista, e va usato (vedi
`video-analyst.md` §8, col caso misurato Lama Facha / Famiglia Sfortunata). **Si replica l'idea e
la struttura; il materiale visivo si genera o si prende alla fonte.**

**Un limite nostro, dichiarato:** i regolatori vigilano sulla copiatura **solo del testo**
(`regolatori.py`, `N_GRAM = 8`). Sul lato visivo non esiste alcun controllo — semplicemente perché
non riusiamo mai materiale altrui. **È una proprietà del flusso, non un presidio:** se qualcuno
introducesse clip scaricate, nessun regolatore se ne accorgerebbe. Annotato in `BACKLOG.md`.

Arbitrato completo: `company/Memory/studi/aitubepro/CONFLITTI.md` **C-004**.
