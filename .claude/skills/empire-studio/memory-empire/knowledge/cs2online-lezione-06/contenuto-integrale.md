# Lezione 6 — Cucinando il tuo contesto (Claude Speedrun 2)

**Fonte:** trascrizione ufficiale scaricata dalla piattaforma + 43 frame video visionati nativamente.

---

## Trascrizione integrale

In questa lezione cuciniamo il tuo contesto.

Hai mai sentito parlare di garbage in, garbage out — merda dentro, merda fuori? È un concetto del mondo tech che spiega che se dai un input di merda, avrai un output di merda. Molti si chiedono perché Claude risponde male. Il motivo è semplice: gli stanno dando un prompt di merda. Devi creare un buon input.

Il problema è che se ogni volta che scrivi a Claude devi ridargli tutto il contesto — chi sei, cosa fa la tua azienda, come vuoi le risposte, quanto deve scrivere, come organizzare la risposta — non lo farai mai. Ed è per questo che i prompt di molti fanno schifo.

### La soluzione: una base informativa

La mia tecnica è creare una serie di documenti di contesto da allegare ogni volta che faccio un prompt. Dico a Claude: questi documenti valgono per sempre. Ogni volta che mi rispondi, rispondimi con questo formato, con questa metodologia. E sopra questo contesto fisso, metto la mia richiesta specifica. Lui combina le due cose e l'output è di qualità molto più alta.

### Formati: quale usare

Mandare PDF all'AI è generalmente una pessima idea — è il peggior formato per leggere le cose. Io preferisco Markdown (estensione .md). Puoi usare anche TXT o altri formati, ma Markdown è quello che consiglio. Per crearlo, ti consiglio l'app Mark Edit, che trovi nel link sotto questa lezione.

Più informazioni dai, meglio è — finché sono concise e ben organizzate. Non un muro di testo infinito, ma informazioni dense e strutturate.

### Esempi di documenti di contesto

Ho una cartella sul mio computer che si chiama AI Contexting. Dentro ci sono diversi documenti:

- Brand guidelines — in formato JSON, così Claude le può rileggere ogni volta che fa design o copy per il mio brand
- Business plan — quando chiedo a Claude di aiutarmi con i task della settimana, gli allego questo. Così sa quali sono i miei obiettivi e può suggerirmi cosa fare per avvicinarmi a quelli
- Strumenti aziendali — una lista di tutti gli strumenti che uso: Google Meet, WhatsApp, ClickUp, Loom, Claude, Lovable, Vimeo, ecc. Così quando mi pianifica la settimana sa cosa posso usare e me li consiglia
- Skill, pregi e difetti — Claude sa in cosa sono bravo e in cosa no. Questo cambia tantissimo la qualità degli output

Per Claude Speedrun ho creato una cartella apposita con dentro target e avatar del corso, brand guidelines in JSON, e altri documenti specifici. Ogni volta che chiedo un copy, un consiglio o una lezione, Claude ha accesso a tutto questo.

### Come creare un documento JSON dal tuo PDF

Se hai un PDF di brand guidelines e vuoi convertirlo in un JSON usabile come contesto, ecco come fare:

Apri Claude, nuova chat, e scrivi qualcosa tipo: "Questa è una brand guidelines di un corso che sto lanciando. Voglio che tu crei un JSON prompt di circa 300-400 righe, dettagliato, per indicare a un LLM come fare il design." Allega il PDF.

Per questo tipo di task — un documento che verrà riutilizzato indefinitamente nel futuro — usa il modello migliore disponibile. Se lo fai male, lo paghi ogni volta che lo usi. Usa Opus con extended thinking: è più potente e vale la pena per qualcosa che è la base di tutte le risposte future.

Il file JSON risultante lo salvi nella tua cartella di contesto. Per salvarlo puoi usare VS Code o Cursor: apri l'app, crea un nuovo file con estensione .json, incolla il contenuto generato da Claude, salva con Command S / Ctrl S.

### I quattro livelli di contesto

Quando fai un prompt, ci sono quattro livelli di informazione, definiti dalla frequenza con cui cambiano:

Livello 1 — cambia ogni volta: la richiesta stessa. Ogni prompt è diverso.

Livello 2 — cambia ogni settimana: cosa devi ottenere quella settimana, cosa cambia rispetto alla settimana precedente.

Livello 3 — cambia ogni trimestre: informazioni di business, pianificazione strategica, risultati del trimestre.

Livello 4 — non cambia quasi mai: chi sei, la tua professione, il tuo business, i nomi dei clienti, come sei come persona.

Per il livello 1 non crei nessun documento — cambia ogni volta, non ha senso. Per i livelli 2, 3 e 4 crei documenti di contesto, e li aggiorni con la frequenza corrispondente: settimanale, trimestrale, praticamente mai.

Sotto questa lezione trovi la lista dei documenti da creare con template che ti guidano su come farli.

Tutto il resto è lì sotto — usalo.

---

## Timeline demo schermo (osservata con visione diretta, 43 frame)

Vedi `runs/andrei-pascu-cs2online-001/lessons/lezione-06/lesson-analysis.md` per la mappa completa timestamp-per-timestamp con riferimento ai frame salvati in `frames/`. Sintesi:

- **0:25–1:15** — Excalidraw: diagramma "input → Claude → out" (garbage in garbage out)
- **1:45–2:15** — Excalidraw: icona cartella
- **3:45–5:30** — Demo reale: MarkEdit (esempio doc personale) + Finder, cartella contesto con sottocartella "Business planning" (8 file reali mostrati)
- **6:00–6:15** — Demo reale: cartella "Claude Speedrun" (contesto dedicato al corso)
- **7:00–7:15** — Demo reale: Gemini (chat history) + Claude.ai con saluto memory "andrei returns!"
- **9:00–11:00** — Demo reale: workflow completo PDF→JSON (Claude, Opus 4.6 Extended Thinking, prompt esatto, output JSON con palette colori) → VS Code → salvataggio in "Cartella contesto"
- **11:00–12:25** — Excalidraw: diagramma "4 livelli di informazioni nei prompt" costruito progressivamente

## Risorse allegate

- Esempio reale (parzialmente redatto) di documento "skills, strengths, weaknesses": `resources/esempio-context-doc-skills-weaknesses-TEMPLATE.md`
- Esempio brand guidelines: PDF + JSON risultante (`resources/esempio-brand-guidelines.pdf`, `.json`)
- PDF: lista esempi context documents, prompt onboarding call summary, lista strumenti APS, pro/contro organizzare giornata con AI
- 5 Workflow ufficiali citati (vedi ingest.json)
