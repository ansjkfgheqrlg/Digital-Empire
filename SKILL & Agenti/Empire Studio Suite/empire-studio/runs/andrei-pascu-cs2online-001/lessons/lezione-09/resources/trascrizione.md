# Diversi modi per dare contesto alle intelligenze artificiali

> *Questa trascrizione è stata corretta e sanificata con l'intelligenza artificiale e potrebbe contenere errori. Non è stata verificata da un essere umano.*

---

Garbage in, garbage out. Ne abbiamo già parlato. Ora vediamo concretamente come dare contesto a Claude.

Immagina di avere una serie di documenti Markdown per un cliente o un progetto: uno per il contesto generale, uno per i problemi che stai affrontando, uno per le tue skill, uno per le preferenze del cliente, la scheda prodotto, e così via. Ci sono principalmente tre modi per usarli.

---

## Modo 1 — Allegare tutti i file rilevanti

Prendi i file, li alleghi dentro una chat con Claude insieme al tuo prompt. Semplice, funziona.

## Modo 2 — Allegare solo i file rilevanti per quel task

Più intelligente. Non alleghi tutto: selezioni solo i file che servono per quella specifica richiesta. Se stai facendo il copy per un VSL, non ha senso allegare le preferenze del cliente per le email o le tue skill generali. Tieni solo quello che è direttamente utile, e allegalo insieme al prompt.

## Modo 3 — CoWork (condivisione cartella)

Dai a Claude accesso a una cartella sul tuo computer. La struttura consigliata è una cartella principale (es. "Claude") con sottocartelle organizzate per cliente o progetto.

La mia struttura personale, ad esempio:
- **Assets** — immagini e brand guidelines
- **B2B Client Work** — una sottocartella per ogni cliente
- **Business Planning** — piano di business
- **Claude Speedrun** — tutto il progetto del corso
- **Productivity** — task e pianificazione settimanale

Quando usi CoWork, condividi solo la cartella del cliente rilevante — non l'intera cartella Claude. Se gli dai accesso a tutto, Claude spreca token e context window a cercare la roba che gli serve. Fagli la vita facile: seleziona la cartella specifica.

CoWork è multi-step, quindi il context window è praticamente illimitato. Tieni però presente che più context window usi, più consumi la tua disponibilità giornaliera di Claude.

---

## Modo da evitare — Link esterni

Puoi allegare link invece di file, ma è uno dei modi peggiori per dare contesto. Preferisco un PDF a un link esterno. L'unico AI con cui mi sono trovato bene a condividere link direttamente è Perplexity.

---

## Modo migliore — Projects

Per progetti che durano giorni o settimane, usa i **Projects** di Claude. Ogni project ha:
- Tutte le chat relative a quel cliente/progetto in un posto solo
- Una **memory** aggiornata automaticamente da Claude
- **Instructions** — istruzioni fisse (es. "sono un'agenzia di marketing, sto aiutando questo cliente a migliorare le conversioni della landing page")
- **Files** — i documenti Markdown di contesto

Le instructions non devono essere lunghissime: il grosso del lavoro lo fanno i file e la memory. Ogni project ha la sua memory separata, il che cambia radicalmente la qualità degli output nel tempo.

---

## Quando usare cosa

- **Copy e lavoro testuale per un cliente** → Projects
- **Presentazioni, file multipli, task pesanti** → CoWork
- **Task one-time o veloce** → singola chat con i file rilevanti allegati

Mai allegare solo link per contesto. Mai allegare file a caso per sentirti smart — se non sono rilevanti per quel task specifico, stai lavorando a vuoto.
