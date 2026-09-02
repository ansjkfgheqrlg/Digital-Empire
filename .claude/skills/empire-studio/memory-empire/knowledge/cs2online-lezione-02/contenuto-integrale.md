# Lezione 2 — Termini che devi sapere (Claude Speedrun 2)

**Fonte:** blocco ufficiale "Cosa hai imparato" (26 bullet) + Glossario ufficiale CSV (52 termini, scaricato dalla piattaforma). Nessuna trascrizione .md disponibile per questa lezione.

---

## "Cosa hai imparato" (ufficiale, integrale)

- Cos'è un system prompt: un'istruzione nascosta data all'AI dal provider che tu non puoi modificare, ma sopra cui puoi costruire i tuoi prompt personalizzati
- Esistono modi per runnare LLM in locale sul tuo computer (es. Ollama), anche se serve hardware potente e va oltre il corso
- È tecnicamente possibile trainare modelli AI propri o su banche dati specifiche (anche se costa tantissimo)
- Cos'è un artifact (Claude) / canvas (ChatGPT, Gemini): un documento condiviso su cui lavori insieme all'AI, tipo un Google Docs collaborativo
- Come creare un artifact su Claude: basta chiedere esplicitamente nel prompt di "lavorare dentro un artifact"
- Differenza tra i modelli Claude (Opus, Sonnet, Haiku) e quando usare Haiku per risposte veloci e cheap
- Claude ha una memory e contesto delle chat passate, quindi personalizza le risposte in base a conversazioni precedenti (ma non ricorda tutto, perché il context ha un limite)
- Cos'è un Project su Claude (equivalente di Custom GPTs su ChatGPT o Gems su Gemini): una cartella che raggruppa chat relative a uno stesso progetto/cliente
- Come creare un Project su Claude per un cliente specifico: dai un nome, scrivi istruzioni fisse e carica file (ricerche di mercato, trascrizioni chiamate, richieste del cliente)
- Vantaggio dei Projects: ogni nuova chat dentro quel progetto parte già con il contesto che hai impostato, senza doverlo riscrivere ogni volta
- Cos'è la memory dell'AI: ciò che si ricorda tra una conversazione e l'altra
- Cos'è il web search nell'AI: la capacità di cercare online per accedere a informazioni più recenti rispetto ai dati di training (es. il vecchio problema della knowledge cutoff di ChatGPT ferma al 2021)
- Cos'è il chain of thought / reasoning: il processo in cui l'AI pensa ad alta voce e ti mostra il suo ragionamento prima di darti la risposta
- Come attivare l'extended thinking su Claude (Opus 4.6): selezionare "extended thinking" per farlo ragionare più a lungo e ottenere risposte migliori
- Le risposte con reasoning attivo sono significativamente migliori rispetto a quelle senza
- Cos'è la temperatura: uno slider che controlla quanto l'AI è creativo/fantasioso nelle risposte
- Cos'è un'API spiegata semplice: un modo per collegare due servizi diversi tra loro (es. Google Sheets → Yahoo Mail)
- Cos'è un'API key: una chiave segreta che dai al tuo codice per accedere a un altro servizio — non va mai condivisa per motivi di sicurezza e finanziari
- Dove trovare le API key: non dentro la chat (es. chatgpt.com) ma sulle piattaforme developer (es. Platform di OpenAI, Anthropic for Developers)
- Come usare un'API in pratica: esempio di automazione che ogni giorno a mezzanotte fa creare un messaggio a ChatGPT e lo invia via email
- Cos'è il vibe coding: scrivere codice usando il linguaggio naturale, dicendo all'AI cosa vuoi e lasciando che scriva il codice per te
- Esempio pratico di vibe coding: far creare a Claude un calendario HTML collegato a Google Sheets tramite API, tutto con un singolo prompt
- Puoi dare all'AI le brand guidelines e fargli generare pagine intere (es. la sales page del corso è sviluppata con AI, copy scritto a mano ma development fatto dall'AI)
- Cos'è un agent: un "robottino" AI che non solo parla con te ma esegue azioni automatiche in autonomia
- Cos'è un'automazione e come funziona: un workflow che esegue step da solo (es. ogni giorno alle 21:00 inviare un'email di reminder al team)
- Usare Zapier per creare automazioni semplici: esempio pratico di invio email automatica giornaliera tramite Gmail collegato a Zapier

---

## Glossario completo (52 termini, integrale da resources/glossario.csv)

| Termine | Definizione |
|---|---|
| AI (Artificial Intelligence) | Intelligenza artificiale. Tecnologia che permette ai computer di fare cose "intelligenti" come scrivere testi, creare immagini o ragionare. Quando diciamo AI, IA o AI technology, parliamo sempre di questo. |
| LLM (Large Language Model) | Un tipo specifico di AI addestrato su enormi quantità di testo. Sa "parlare" e scrivere. Claude, ChatGPT e Gemini sono tutti LLM. |
| Modello | Il motore di un'AI. Come le auto hanno modelli diversi (utilitaria, Ferrari, ambulanza), anche l'AI ha modelli diversi, ognuno pensato per un uso specifico: testo, immagini, video, audio. |
| Token | L'unità di misura dell'AI. Ogni parola o pezzo di parola che l'AI legge o scrive è un token. Più token usi, più costa. È il motivo per cui a volte Claude o ChatGPT ti dice "hai raggiunto il limite". |
| Context Window | Quante informazioni l'AI riesce a considerare contemporaneamente quando ti risponde. Immaginalo come uno zaino: più è grande, più cose ci stanno. Se gli dai troppe info, alcune vengono ignorate. Si misura in token. |
| Context Engineering | L'arte di organizzare e dare le informazioni giuste all'AI nel modo giusto, così che le consideri tutte quando ti risponde. Non basta mandare PDF a raffica: serve struttura. |
| Prompt | Il messaggio o la richiesta che tu mandi all'AI. Quello che scrivi nella chat. |
| Output | Il risultato che l'AI ti restituisce: testo, immagine, video, codice, quello che ti dà indietro dopo il tuo prompt. |
| Hallucination (Allucinazione) | Quando l'AI ti spara un'informazione completamente inventata ma te la presenta come vera, con sicurezza. Pericoloso perché a volte non è ovvio che sta mentendo. |
| Chat / Conversazione | La conversazione che hai con l'AI. Lo scambio di messaggi avanti e indietro. |
| System Prompt | Istruzioni segrete date all'AI dietro le quinte dal suo creatore (es. Anthropic per Claude). Tu non le puoi cambiare. Sono il motivo per cui l'AI si rifiuta di fare certe cose, tipo spiegarti roba illegale. |
| Artifacts / Canvas | Documenti condivisi su cui lavori insieme all'AI. Come un Google Docs in cui Claude scrive e tu puoi modificare. Su Claude si chiamano Artifacts, su ChatGPT e Gemini si chiamano Canvas. |
| Projects (Custom GPTs / Gems) | Su Claude: cartelle di chat raggruppate per progetto, con contesto e istruzioni che rimangono fissi per ogni nuova chat. Tipo una cartella "Cliente Antonio" dove Claude sa già chi è Antonio senza che glielo rispieghi ogni volta. |
| Memory (Memoria) | Quello che l'AI si ricorda di te tra una conversazione e l'altra. Claude ha memoria dedicata sia globale che per singolo Project. |
| Web Search | La capacità dell'AI di cercare informazioni online in tempo reale. Senza questa, l'AI sa solo quello su cui è stato addestrato e non conosce eventi recenti. |
| Knowledge Cutoff | La data oltre la quale l'AI non sa più nulla perché il suo addestramento si è fermato lì. Senza web search, tutto ciò che è successo dopo quella data non esiste per l'AI. |
| Prompt Engineering | La skill di scrivere prompt efficaci. Più sei bravo a chiedere, migliore è la risposta. È quasi un mestiere: saper formulare le richieste nel modo giusto. |
| Chain of Thought (Catena di Pensiero) | Quando l'AI ti mostra il suo ragionamento passo dopo passo, non solo il risultato finale. Puoi vedere come ha pensato prima di rispondere. |
| Reasoning | Il processo con cui l'AI "pensa" prima di darti la risposta. I modelli che fanno reasoning danno risposte molto migliori rispetto a quelli che rispondono d'impulso. |
| Extended Thinking | Modalità avanzata di reasoning dove l'AI pensa ancora più a lungo e in profondità prima di rispondere. Su Claude si attiva manualmente e migliora parecchio la qualità dell'output. |
| Temperatura | Un parametro che controlla quanto l'AI è creativo vs prevedibile. Temperatura alta = risposte più fantasiose e rischiose. Temperatura bassa = risposte più sicure e prevedibili. |
| API (Application Programming Interface) | Un sistema che permette di collegare due servizi diversi tra loro. Es: collegare Google Sheets a Gmail per inviare email automatiche. È il ponte che fa parlare software diversi. |
| API Key | La chiave segreta e personale che ti serve per collegare un servizio via API. Non va MAI condivisa con nessuno per motivi di sicurezza e finanziari. |
| Automazione / Workflow | Una serie di azioni che succedono automaticamente senza che tu faccia nulla. Es: ogni giorno alle 21:00 viene inviata un'email automatica al team. |
| Vibe Coding | Scrivere codice usando il linguaggio naturale, cioè le parole. Dici all'AI cosa vuoi e lui scrive il codice per te. Zero competenze di programmazione richieste. |
| Agent | Un'AI che non si limita a parlarti ma può eseguire azioni concrete nel mondo reale: inviare email, modificare file, fare ricerche, completare task in autonomia. |
| Anthropic | L'azienda che ha creato Claude. Fondata da ex ricercatori di OpenAI. Sono i "genitori" di Claude, come OpenAI lo è di ChatGPT. |
| Claude | L'AI di Anthropic e il protagonista di questo corso. Un LLM disponibile via app, sito web (claude.ai) e API. |
| Opus / Sonnet / Haiku | I tre modelli di Claude, dal più potente al più leggero. Opus = massima qualità, Sonnet = bilanciato, Haiku = veloce e cheap. Scegli in base al task. |
| Fine-tuning | Prendere un modello AI già esistente e riaddestrarlo su dati specifici per renderlo esperto in un campo. Tipo addestrare un tuttofare a fare il chirurgo. |
| Few-shot Prompting | Dare all'AI degli esempi concreti dentro il prompt per fargli capire esattamente cosa vuoi e come lo vuoi. Tipo: "Ecco 3 esempi, ora fai uguale". |
| Zero-shot Prompting | Chiedere all'AI di fare qualcosa senza dargli nessun esempio. Solo l'istruzione. Funziona per task semplici, meno per roba complessa. |
| Markdown | Un linguaggio semplicissimo per formattare testo (grassetto, titoli, elenchi) usato tantissimo nell'AI. Claude lo capisce e lo produce nativamente. Utile per dare contesto strutturato. |
| RAG (Retrieval-Augmented Generation) | Tecnica in cui l'AI prima cerca info in un database/documento e poi risponde usando quelle info. Combina ricerca + generazione per risposte più accurate. |
| Embedding | Un modo per trasformare testo in numeri che il computer capisce. Serve per far cercare e confrontare testi all'AI in modo intelligente. |
| Iterazione | Fare più giri di revisione con l'AI sullo stesso output. Mandi il prompt, vedi il risultato, correggi, rimandi. Ogni giro migliora il risultato. |
| Tone of Voice | Lo stile comunicativo di un brand o persona. Dare all'AI il tuo tone of voice significa fargli scrivere come parleresti tu, non come un robot generico. |
| Contesto / Context | Tutte le informazioni di background che dai all'AI per fargli capire la situazione. Più contesto rilevante = output migliore. Ma dev'essere organizzato, non buttato a caso. |
| Persona (nel prompting) | Dire all'AI di comportarsi come un certo tipo di professionista. Es: "Sei un copywriter senior con 10 anni di esperienza". Cambia radicalmente la qualità della risposta. |
| Copy / Copywriting | Testo scritto per persuadere, vendere o portare a un'azione. Ads, email, landing page, post social. Il pane quotidiano di chi lavora in marketing. |
| CTA (Call to Action) | L'invito all'azione che metti alla fine di un copy. "Compra ora", "Prenota la call", "Scarica il PDF". Il punto in cui chiedi al lettore di fare qualcosa. |
| Landing Page / Sales Page | Pagina web creata con un unico obiettivo: convertire il visitatore in cliente (o lead). Tutta la pagina è costruita per portarti a un'azione. |
| Lead | Una persona potenzialmente interessata al tuo prodotto/servizio che ti ha lasciato un contatto (email, telefono). Non è ancora cliente, è un "contatto caldo". |
| Funnel | Il percorso che una persona fa da sconosciuto a cliente. Tipo: vede un ad → clicca → arriva sulla landing page → compra. Ogni step è un pezzo del funnel. |
| A/B Test | Testare due versioni diverse della stessa cosa (ad, email, landing page) per vedere quale funziona meglio. Cambi una variabile e confronti i risultati. |
| Zapier | Piattaforma no-code per creare automazioni collegando app diverse. Es: "Quando ricevo un'email con allegato, salvalo su Google Drive e avvisami su Slack". Si usa spesso con le API di Claude. |
| No-Code / Low-Code | Creare software, siti o automazioni senza scrivere codice (o scrivendone pochissimo). Strumenti come Zapier, Lovable, Bubble rientrano in questa categoria. |
| Scraping | Estrarre dati automaticamente da siti web. Es: raccogliere tutti i prezzi dei competitor da un sito. Si può fare con l'AI o con tool dedicati. |
| Brand Guidelines | Le regole visive e comunicative di un brand: colori, font, tono, logo. Darle all'AI significa fargli produrre output coerenti con la tua identità. |
| Scalabilità | La capacità di un processo o business di crescere senza che il carico di lavoro cresca proporzionalmente. L'AI ti aiuta a scalare perché automatizza ciò che prima facevi a mano. |
| ROI (Return on Investment) | Quanto guadagni rispetto a quanto hai speso. Se spendi 100€ e ne guadagni 300€, il ROI è del 200%. La metrica fondamentale per capire se qualcosa funziona. |

## Workflow citati (titoli, non ancora verificato se hanno documento scaricabile proprio)

- Workflow 1 - Creare un Artifact su Claude
- Workflow 2 - Creare un Project su Claude per un cliente
- Workflow 3 - Usare Extended Thinking (Chain of Thought) su Claude
