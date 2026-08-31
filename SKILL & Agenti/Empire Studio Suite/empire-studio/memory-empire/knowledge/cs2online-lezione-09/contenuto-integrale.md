# Lezione 9 — Come dare contesto alle AI (Claude Speedrun 2)

**Fonte:** trascrizione ufficiale integrale + "Cosa hai imparato" (18 bullet) + 10 frame video visionati nativamente. ULTIMA lezione sezione "AI - Le basi".

---

## Trascrizione integrale

Garbage in, garbage out. Ne abbiamo già parlato. Ora vediamo concretamente come dare contesto a Claude.

Immagina di avere una serie di documenti Markdown per un cliente o un progetto: uno per il contesto generale, uno per i problemi che stai affrontando, uno per le tue skill, uno per le preferenze del cliente, la scheda prodotto, e così via. Ci sono principalmente tre modi per usarli.

### Modo 1 — Allegare tutti i file rilevanti

Prendi i file, li alleghi dentro una chat con Claude insieme al tuo prompt. Semplice, funziona.

### Modo 2 — Allegare solo i file rilevanti per quel task

Più intelligente. Non alleghi tutto: selezioni solo i file che servono per quella specifica richiesta. Se stai facendo il copy per un VSL, non ha senso allegare le preferenze del cliente per le email o le tue skill generali. Tieni solo quello che è direttamente utile, e allegalo insieme al prompt.

### Modo 3 — CoWork (condivisione cartella)

Dai a Claude accesso a una cartella sul tuo computer. La struttura consigliata è una cartella principale (es. "Claude") con sottocartelle organizzate per cliente o progetto.

La mia struttura personale, ad esempio:
- Assets — immagini e brand guidelines
- B2B Client Work — una sottocartella per ogni cliente
- Business Planning — piano di business
- Claude Speedrun — tutto il progetto del corso
- Productivity — task e pianificazione settimanale

Quando usi CoWork, condividi solo la cartella del cliente rilevante — non l'intera cartella Claude. Se gli dai accesso a tutto, Claude spreca token e context window a cercare la roba che gli serve. Fagli la vita facile: seleziona la cartella specifica.

CoWork è multi-step, quindi il context window è praticamente illimitato. Tieni però presente che più context window usi, più consumi la tua disponibilità giornaliera di Claude.

### Modo da evitare — Link esterni

Puoi allegare link invece di file, ma è uno dei modi peggiori per dare contesto. Preferisco un PDF a un link esterno. L'unico AI con cui mi sono trovato bene a condividere link direttamente è Perplexity.

### Modo migliore — Projects

Per progetti che durano giorni o settimane, usa i Projects di Claude. Ogni project ha:
- Tutte le chat relative a quel cliente/progetto in un posto solo
- Una memory aggiornata automaticamente da Claude
- Instructions — istruzioni fisse (es. "sono un'agenzia di marketing, sto aiutando questo cliente a migliorare le conversioni della landing page")
- Files — i documenti Markdown di contesto

Le instructions non devono essere lunghissime: il grosso del lavoro lo fanno i file e la memory. Ogni project ha la sua memory separata, il che cambia radicalmente la qualità degli output nel tempo.

### Quando usare cosa

- Copy e lavoro testuale per un cliente → Projects
- Presentazioni, file multipli, task pesanti → CoWork
- Task one-time o veloce → singola chat con i file rilevanti allegati

Mai allegare solo link per contesto. Mai allegare file a caso per sentirti smart — se non sono rilevanti per quel task specifico, stai lavorando a vuoto.

---

## "Cosa hai imparato" (ufficiale, integrale)

- Applicare il principio "garbage in, garbage out" quando lavori con Claude: la qualità dell'output dipende dalla qualità del contesto che gli dai
- Creare file di contesto separati in Markdown per ogni aspetto del lavoro: contesto generale, problemi, skill, desideri del cliente, file già consegnati, scheda prodotto
- Primo metodo: allegare tutti i file di contesto + prompt direttamente in una chat con Claude
- Secondo metodo (più intelligente): allegare solo i file rilevanti per quel task specifico, lasciando fuori quelli che non c'entrano con la richiesta
- Scegliere quali file servono in base al prompt: se scrivi un VSL non alleghi le preferenze email del cliente, se fai copy non alleghi le tue skill
- Terzo metodo: usare Cowork dando a Claude accesso diretto alle cartelle del tuo computer
- Organizzare il computer con una cartella principale (es. "Claude") e sottocartelle per cliente/progetto, tenendola pulita e aggiornata ogni giorno
- Quando usi Cowork, condividere solo la sottocartella del cliente su cui stai lavorando, non l'intera cartella Claude — per risparmiare token e context window
- Sapere che Cowork è multi-step e ha context window praticamente illimitato, ma più contesto usi più consumi la tua disponibilità di Claude
- Evitare di dare contesto tramite link esterni: è uno dei modi peggiori, Claude non li gestisce bene (unica eccezione: Perplexity)
- Preferire file Markdown o anche PDF rispetto ai link esterni per passare informazioni a Claude
- Usare i Projects di Claude per clienti o progetti che durano giorni/settimane: ci metti dentro file di contesto, istruzioni e tieni tutte le chat raggruppate
- Nelle istruzioni del Project scrivere una descrizione generica del ruolo e dell'obiettivo, il resto va nei file o nel prompt
- Sfruttare la memory automatica dei Projects che si aggiorna da sola conversazione dopo conversazione
- Quando scegliere cosa: Projects per lavori di copy/linguaggio continuativi, Cowork per task pesanti con molti file o presentazioni, chat singola con file allegati per task veloci e one-time
- Non allegare file a caso solo per sentirti smart: ogni file deve essere rilevante, altrimenti lavori a vuoto

## Link utili

Claude, Claude Projects, Claude Cowork, Markdown Guide, Perplexity AI, Perplexity Spaces, Grok, Google Gemini Gems.
