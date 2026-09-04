# Video Analysis — `RnoC5IlOUhs`

> **Run**: `max18-v01-second-brain-obsidian`
> **Titolo reale** (da `ingest.json`): *CORSO COMPLETO SECOND BRAIN 2h: Claude + Obsidian*
> **Canale**: Giovanni Beggiato · **Durata**: 8330 s = **2h 18m 50s**
> **Formato**: tutorial screen-share quasi integrale (Obsidian + Claude Code/Cowork + Notion + Excalidraw + GitHub), con talking-head solo nel primo minuto e brevi rientri.
> **Frame densi**: 1389 (1 ogni 6.0 s) · **Scene uniche** (`scenes.md`, soglia 3.0): **352**
> **Risoluzione frame**: 640x360 — il testo grande e le slide Excalidraw sono leggibili; il testo piccolo di UI (proprietà YAML, output di terminale, sidebar Notion) è spesso al limite. Dove non è leggibile con certezza **non viene trascritto**.

## Convenzioni
- Ogni blocco = una scena di `scenes.md`, con timestamp nominale e file frame.
- `➕` marca **ogni inferenza** non letta direttamente su schermo né detta a voce.
- Le citazioni fra virgolette dalla voce vengono da `transcript.md` (letto al 100%).
- Regola NO-FINTO: se un frame non è stato aperto in questa sessione, non se ne descrive il contenuto.

---

## Nota di continuità (perché questa analisi esiste)

Una sentinella gemella aveva già iniziato la visione ed era arrivata a **175 scene su 352**; è stata terminata da un **limite di sessione dell'account**, non da un errore di merito. Il suo lavoro viveva solo nel contesto e **non era su disco** — su disco esisteva solo `_daved.txt`, una lista di 176 righe nel formato `NNNN@mm:ss` (indici frame + timestamp) **senza alcuna descrizione di contenuto**: un registro di *quali* frame aveva aperto, non di *cosa* contenevano. La visione è quindi stata rifatta da zero in questa sessione, scrivendo su disco a blocchi.

---

# PARTE 1 — Apertura e promessa (0:00 → 4:12)

### Scena 1 · `frame-0001.png` · 0:00
Talking head. Uomo giovane, capelli castani mossi, maglietta blu scuro, microfono a condensatore nero in primo piano, poltrona da ufficio grigia, mensola bianca con libri colorati, pianta rampicante a sinistra, lampada calda a destra. Nessun testo a schermo.
Voce: *"benvenuti al tutorial più completo sulla company Brain"* — la tesi d'apertura è che la company brain *"separerà chi usa l'AI per moltiplicare il proprio business da chi la usa per giocarci"*.

### Scena 2 · `frame-0002.png` · 0:06
Stessa inquadratura talking head, nessun testo.

### Scena 3 · `frame-0003.png` · 0:12
Talking head con **overlay di testo grande in basso a sinistra, parzialmente fuori campo: "cos'è?"** (le altre parole sono tagliate dal bordo del frame). ➕ È un'animazione di sottotitolo/kinetic text sincronizzata con la frase *"quasi nessuno sa davvero che cosa sia"*.

### Scena 4 · `frame-0004.png` · 0:18 — **primo sguardo alla company brain reale**
Screen-share di **Obsidian in graph view a tutto schermo, tema scuro**: una **sfera densissima** di migliaia di nodi colorati (verde, azzurro, viola, arancio, giallo, rosso), con un anello esterno di puntini bianchi isolati.
In alto a sinistra la **legenda dei gruppi di colore**, leggibile come elenco di cartelle: `areas`, `code`, `concepts`, `data`, `docs`, `entities`, `outputs`, `projects`, `self`, `sources`, `workspace`, più tre voci sotto di taglia minore: `CONVENTIONS`, `README`, `tutorial-completo` / `tutorial-grafico`.
In basso a sinistra la webcam del relatore in PiP.
Questa è la **brain da 22.870 documenti** citata a voce.

### Scena 5 · `frame-0005.png` · 0:24 — **anatomia di una nota atomica reale**
Screen-share Obsidian, nota aperta: **`kpi-2025-edifici`**.
- Pannello **Properties** con i campi: `title` = "KPI 2025 — Edifici gestiti"; `summary` = una frase che descrive il contenuto ("A fine 2025 Aurora gestisce 751 edifici sulla piattaforma…"); `tags` (4 pill colorate, tra cui si leggono `data` e `kpi`); `status`; `created` e `updated` con date **10-06-2026**; `related` con tre wikilink.
- Corpo della nota: titolo `KPI 2025 — Edifici gestiti`, poi bullet:
  - *"Edifici gestiti sulla piattaforma a fine 2025: **751**."*
  - *"Dove vivono: tutti registrati nell'anagrafica di [[prodotto-aurora-core]]."*
  - *"Quadratura: la somma degli immobili dei 9 clienti attivi (120+250+140+99+45+60+28+15) fa esattamente 751."*
- **Sidebar sinistra con le 11 cartelle già visibili**: `areas`, `code`, `concepts`, `data`, `docs`, `entities`, `outputs`, `projects`, `self`, `sources`, `workspace`.
⚠️ La lista di addendi nella riga "Quadratura" ha **8 numeri visibili per 9 clienti dichiarati** e la somma degli 8 letti (120+250+140+99+45+60+28+15 = 757) **non fa 751**: a 640x360 una o più cifre non sono leggibili con certezza, quindi i singoli addendi **non vanno usati come dato**. Il dato solido è: *751 edifici, 9 clienti attivi, quadratura dichiarata*.

### Scena 6 · `frame-0006.png` · 0:30
Talking head, nessun testo.

### Scena 7 · `frame-0007.png` · 0:36 — **identità dell'autore (correzione di trascrizione)**
Screen-share di un sito in una finestra browser: URL **`gentes.ai`**. Pulsante nero in alto **"Let's talk →"**. Barra **"POWERED BY"** con loghi/nomi: *Value Group, Higgsfield, **Anthropic**, **Notion**, Amazon, P&G, Google*. Titolo hero: **"Ten years building growth systems inside Amazon and P&G"**, con badge "① Introducing Gentes".
🔎 La trascrizione automatica scrive *"la mia agenzia di intelligenza artificiale **Gente Sei**"*: il frame mostra che il nome reale è **Gentes / gentes.ai**. Da qui in avanti si usa il nome letto a schermo.

### Scena 8 · `frame-0008.png` · 0:42
Talking head, nessun testo.

### Scena 9 · `frame-0009.png` · 0:48 — **la community**
Screen-share browser su **`skool.com/avanguardia-plus`**, feed della community **"Avanguardia Plus"**. Post visibili:
- *Marco Del Moro* — **"Come evitare che i clienti consumino le mie API in produzione (SaaS AI)?"** (categoria "Supporto Tecnico"), testo: *"Ciao a tutti, sto sviluppando un agente AI/SaaS da offrire in abbonamento ai clienti. Durante la fase di sviluppo utilizzo il mio account e pago le API del provider AI. Il mio dubbio riguarda la produzione: se…"*
- *Paola Gelmini* — **"Automazione #1 - Lead Generation"** (Discussioni Generali).
- **Giovanni Beggiato** — **"Benvenuti! Comincia con questo 👋"**, testo: *"Un grosso benvenuto in community! Come accennato, Avanguardia Plus è un programma pensato per portarti al primo ritorno economico con l'AI entro 90 giorni. Ci…"*
🔎 Conferma incrociata: l'uploader `Giovanni Beggiato` (da `ingest.json`) è la stessa persona che nel video si presenta come **"Joe"** e che qui posta come owner della community.

### Scena 10 · `frame-0010.png` · 0:54 — **agenda del corso (Excalidraw), versione estesa**
Screen-share **excalidraw.com**, lavagna bianca, titolo grande **"COSA VEDERMO"** (refuso dell'autore per *COSA VEDREMO*). Elenco puntato con rombi arancioni:
1. **ROI delle Company Brain e perchè ORA**
2. **Production Ready Brain 22.870 documenti**
3. **Come Obsidian, Notion, Github, Qdrant e Claude interagiscono**
4. **Come installare Obsidian**
5. **Come funziona Obsidian (wikilinks, backlinks, frontmatter, tags)**
6. **Le 11 cartelle: la struttura del cervello, con la regola che dice dove va ogni cosa senza più pensarci**
7. **prendiamo il materiale grezzo dell'azienda e lo trasformiamo in note atomiche e collegate**
8. **L'indice per le AI (llms.txt)**
9. **Grafo a sfera**
🔎 Nota: il numero **22.870** letto sulla lavagna diverge dal *"22.500 note"* detto a voce più avanti (25:04) e dai *"22.870"* della voce a 1:10. Il video usa entrambe le cifre; il dato scritto è 22.870.

### Scena 11 · `frame-0014.png` · 1:18
Di nuovo la graph view a sfera della brain grande, stessa legenda di cartelle, relatore in PiP che gesticola. Nessun testo nuovo.

### Scena 12 · `frame-0017.png` · 1:36 — agenda, scroll 1
Stessa lavagna Excalidraw. Rispetto alla scena 10, la voce 6 è nella forma corta **"Le 11 cartelle: la struttura del cervello."** e in fondo compaiono righe nuove ancora senza rombo:
- **L'indice per le AI (llms.txt)**
- **Grafo a sfera**
- **Github o Google Drive per version control** (parzialmente tagliata in basso)
➕ Le righe senza rombo sono quelle che l'autore sta ancora aggiungendo/formattando dal vivo.

### Scena 13 · `frame-0022.png` · 2:06 — agenda, scroll 2
Stessa lavagna. Ora sono sottolineati a mano in blu: *ROI delle Company Brain*, *22.870*, *Obsidian, Notion, Github, Qdrant*. Ultima riga visibile: **"Self-Improvement guidati dalla company brain"** (tagliata).

### Scena 14 · `frame-0029.png` · 2:48 — **agenda completa**
Lavagna scrollata: si legge l'elenco fino in fondo. Voci finali:
- **Github o Google Drive per version control**
- **Self-Improvement guidati dalla company brain**
- **Layer Visivi (Notion, HTML)**
- **Memoria Viva: aggiornamento automatico ad ogni sessione**
Questa è la **spina dorsale completa del corso**: 13 voci.

### Scena 15 · `frame-0033.png` · 3:12 — **il Notion companion con TUTTI i prompt**
Screen-share Notion, pagina **"Company Brain — Tutti i prompt del tutorial"** (privata, con pulsante "Translate to English" e "Share").
**Indice dei prompt leggibile nella parte alta:**
- Prompt 3 — *Trasforma il canon in note atomiche (prima gli hub)*
- Prompt 4 — *Completa il cervello (fino a circa 28 note)*
- **Passo 3** — *Gate di qualità, indice per le AI, showcase, grafo, GitHub*
- Prompt 5 — *Il gate di qualità (solo referto)*
- Prompt 6 — *Correggi e ripeti finché esce "0 errori"*
- Prompt 7 — *Genera l'indice per le AI (llms.txt)*
- Prompt 8 — *Lo showcase (la fotografia per le demo)*
- Prompt 9 — *Metti il vault sotto git*
- **Passo 4** — *Interrogare il cervello, mostrarlo, tenerlo vivo*
- Prompt 10 — *Interroga il cervello (a 28 note, senza RAG)*
- Prompt 11 — *La domanda di incrocio (dove le cartelle si arrendono)*
- Prompt 12 — *Il cruscotto HTML locale*
- Prompt 13 — *Apri e chiudi la sessione*
- *"Se vuoi unirti alla community di imprenditori, raggiungici QUI"*

**Corpo della pagina, sezione aperta:**
> **Passo 1 — Obsidian, la prima nota, i collegamenti (a mano)**
> *"Nessun prompt all'AI qui: si fa una volta sola, dentro Obsidian."*
> **1. Installa Obsidian e crea il contenitore vuoto**
> • Vai su `obsidian.md`, scarica la versione per il tuo sistema (Mac o Windows) e installala
> • Sul tuo computer crea una cartella nuova e vuota: `aurora-cervello`
> • Apri Obsidian → "Apri cartella come vault" ("Open folder as vault") → seleziona `aurora-cervello`
> **2. Prima nota** — crea la nota (Cmd+N / Ctrl+N), chiamala `self-identita-aurora`, e scrivi nel corpo:
> `Aurora Sistemi S.p.A. è un'azienda da 340 persone che vende sistemi …`

**Sidebar Notion** (leggibile): sezione *Meetings* ("Connect your calendar", "New AI meeting note"), sezione *Recents* con le pagine **Company Brain — Tutti i promp…**, **Clienti**, **Cervello Pino**, **Cruscotto Aurora**, **New page**, **Reparti**, **Prodotti**, **Default view**, **KPI mensili**, **Sedi**, **Competitor**; sezione *Agents* con "New agent".
🔎 Le pagine `Cervello Pino` e `Cruscotto Aurora` che si vedono qui sono **le stesse che verranno costruite dal vivo a 2:07-2:09** — cioè l'autore ha il risultato finale già presente nel workspace prima della demo.

### Scena 16 · `frame-0037.png` · 3:36
Lavagna Excalidraw di nuovo, elenco completo, con sottolineature blu aggiunte su *L'indice per le AI (llms.txt)*.

### Scena 17 · `frame-0039.png` · 3:48
Stessa lavagna, sottolineature su *Grafo a sfera* e *Github o Google Drive per version control*.

### Scena 18 · `frame-0043.png` · 4:12
Stessa lavagna, sottolineature su *Self-Improvement guidati dalla company brain*, *Layer Visivi (Notion, HTML)*, *Memoria Viva: aggiornamento automatico ad ogni sessione*. Fine della presentazione dell'agenda.

---

# PARTE 2 — Il caso business: conoscenza sparsa, ROI, arbitraggio (4:30 → 20:06)

### Scena 19 · `frame-0046.png` · 4:30 — **il patto col pubblico**
Lavagna Excalidraw, nuova slide. Titolo in maiuscoletto: **"QUESTO È UN CORSO PRATICO"**. Tre bullet con rombo arancione:
1. **Costruiremo un company brain assieme**
2. **Capirete il vantaggio competitivo di averne uno**
3. **Saprete cosa serve per scalarlo**

### Scena 20 · `frame-0055.png` · 5:24 — **le 3 zone della conoscenza sparsa** (diagramma centrale della tesi)
Lavagna Excalidraw. Nodo viola in cima: **"CONOSCENZA SPARSA"**. Tre figli collegati:
| Box | Colore | Etichetta | Sottotitolo |
|---|---|---|---|
| 1 | verde | **Nelle chat** (icona bolle) | *"decisioni prese al volo"* |
| 2 | arancio | **Nella testa delle persone** (icona testa con ingranaggio) | *"il commerciale, il tecnico"* |
| 3 | giallo | **In dieci strumenti diversi** (icone CRM / foglio di calcolo / mail / documento) | *"che nessuno ritrova"* |
🔎 Il frame corregge la voce: il relatore a 9:53 dice *"20.000 tool diversi"*, la slide scritta dice **"dieci strumenti diversi"**.

### Scena 21 · `frame-0066.png` · 6:30
Stesso diagramma, l'autore ha numerato a mano in blu i box **① Nelle chat** e **② Nella testa delle persone**.

### Scena 22 · `frame-0071.png` · 7:00
Sotto il box ② compaiono due frecce a mano che si biforcano verso due etichette scritte a mano: **"TOP PERFORMER"** e **"ONBOARDING"** — le due facce del rischio "conoscenza nella testa delle persone".

### Scena 23 · `frame-0076.png` · 7:30
Stessa scena, vista leggermente scrollata; le due etichette sono complete.

### Scena 24 · `frame-0082.png` · 8:06
A destra del box ③ inizia un nuovo disegno a mano in blu: due linee sinuose orizzontali che si incrociano (➕ è l'inizio dello schema "tubi che non si incontrano" / colli di bottiglia; l'oggetto viene completato nelle scene seguenti).

### Scena 25 · `frame-0087.png` · 8:36
Appare, collegata a "TOP PERFORMER" con una **freccia rossa**, il simbolo **"$"** barrato/cerchiato in rosso — la perdita economica. In basso comincia a comparire il testo della slide successiva (tagliato).

### Scena 26 · `frame-0088.png` · 8:42
Stessa scena; la freccia rossa da "TOP PERFORMER" al "$" è ora tracciata due volte (doppia freccia).
Voce, sui tre danni del top performer: **(1)** perdita economica immediata, **(2)** impossibilità di fare training perché la conoscenza non è documentata, **(3)** costo di tempo per riassumere e riformare qualcuno allo stesso livello.

### Scena 27 · `frame-0100.png` · 9:54
Il box ③ è ora numerato in blu. A destra il disegno delle due linee sinuose è completato con una **ellisse rossa sull'incrocio** e una **freccia rossa** che la indica. ➕ Marca il punto in cui i canali informativi si sovrappongono senza che nessuno lo governi.

### Scena 28 · `frame-0101.png` · 10:00
Vista completa del diagramma "CONOSCENZA SPARSA" con tutte e tre le numerazioni ①②③, le due etichette a mano e il disegno rosso a destra.

### Scena 29 · `frame-0107.png` · 10:36
Transizione: in alto restano tracce del disegno precedente (si leggono a mano **"TRAINING"** e, sopra, "$"), mentre entra in campo la slide dei numeri (parzialmente).

### Scena 30 · `frame-0108.png` · 10:42 — **i tre dati di mercato con fonte** ⭐
Slide Excalidraw, tre bullet con rombo arancione e fonte scritta in blu sotto ciascuno:
1. **"Il settore impiegatizio passa circa il 19% della settimana a cercare informazioni (1 giorno su 5)"** — **FONTE: McKinsey Global Report**
2. **"Un nuovo assunto ci mette in media 8-12 mesi per diventare davvero produttivo. (gran parte leggere report, domande, etc)"** — **FONTE: HBR**
3. **"Quando una persona se ne va, si porta via la sua conoscenza. Esce dalla porta e quel pezzo di azienda esce con lei."** (senza fonte)
🔎 La trascrizione automatica rende il secondo dato come *"8-1 mesi"*: il frame mostra **8-12**. Questi tre sono gli unici numeri di terze parti citati con fonte in tutto il video.

### Scena 31 · `frame-0129.png` · 12:48
Stessa slide, scrollata a destra; sottolineature blu su *"cercare informazioni"* e *"davvero produttivo"*. Lo spazio a sinistra è vuoto: l'autore sta per disegnarci sopra.

### Scena 32 · `frame-0140.png` · 13:54 — **la curva di apprendimento disegnata a mano** ⭐
A sinistra della slide dei dati, disegno a mano in blu: assi **"Apprend."** (verticale) e **"Tempo"** (orizzontale). La curva sale, poi **scende in una conca**, poi risale ripida fino a un **plateau**. Sul fondo della conca c'è un cerchietto rosso, e sotto, in rosso, tre righe raggruppate da una graffa:
- **3-6**
- **8-12**
- **14-18**
Voce: sono i **mesi** che servono per superare la conca — 3-6 per un *top performer*, 8-12 per un *mid performer*, 14-18 per un *low performer*.

### Scena 33 · `frame-0153.png` · 15:12 — **chi guadagna in quale metà della curva** ⭐
Stesso grafico, ora annotato:
- Tratto **arancione** sulla prima parte della curva con etichetta **"VOI GUADAGNATE"**;
- Tratto **verde** sulla seconda parte (dopo la risalita) con etichetta **"AZIENDA GUADAGNA"**;
- Vicino all'asse Tempo, riquadro rosso: **"≤ 2 anni"**;
- In alto a destra, in rosso: **"TRAINING"**.
Tesi: l'azienda tiene il dipendente ≥2 anni perché solo dopo la conca inizia a guadagnarci; ridurre la conca = massimizzare il guadagno aziendale.

### Scena 34 · `frame-0165.png` · 16:24 — **le tre implicazioni economiche** ⭐
In alto a sinistra compare una lista scritta a mano in rosso:
- **AZIENDA ↑↑**
- **JOB ROTATION ↑↑**
- **CHURN (%) ↓↓ ⟹ $** (con il simbolo del dollaro cerchiato)
Cioè: la company brain accorcia la curva → l'azienda guadagna di più, può fare job rotation, e abbassa il tasso di abbandono del personale, che a sua volta è denaro.

### Scena 35 · `frame-0166.png` · 16:30
Torna la slide dei dati, ora con **"19%" cerchiato in rosso** e **"8-12 mesi" cerchiato in rosso**: l'autore evidenzia i due numeri chiave.

### Scena 36 · `frame-0167.png` · 16:36
Stessa slide, entrambi i numeri cerchiati; la terza riga (la conoscenza che esce dalla porta) è sottolineata.

### Scena 37 · `frame-0171.png` · 17:00 — **lo "shadow AI" del dipendente** ⭐
Nuova slide Excalidraw, diagramma:
- Box viola a sinistra: **"Dipendente"** (icona persona al computer);
- Tre oggetti che escono da lui: **"Contratto"** (verde), **"Cartellino del prezzo"** (rosa), **"Dati interni"** (giallo);
- Un triangolo di **warning ⚠️** con etichetta **"Nessun controllo"**;
- Una freccia verso una nuvola azzurra: **"ChatGPT / AI esterna"**.
- Didascalia sotto: **"Dati aziendali incollati fuori, senza protezione"**.
- Frase grande sotto, in corsivo: **"…stra AI e' intelligente quanto cio' che puo' leggere della … a azienda."** (bordi tagliati dal frame; il testo completo è *"La nostra AI è intelligente quanto ciò che può leggere della vostra azienda"*, ricostruito ➕ dal parlato a 18:24).

### Scena 38 · `frame-0186.png` · 18:30
Stessa slide con annotazioni a mano blu: il dipendente è etichettato **"GIO"** (il nome del dipendente-esempio; a voce lo chiama *"Joe"*), frecce blu che puntano "Contratto" e "Dati interni", e un **riquadro tratteggiato blu** attorno alla nuvola ChatGPT. In basso compare il titolo della slide successiva: **"L'arbitraggio del cervello aziendale"**.

### Scena 39 · `frame-0188.png` · 18:42
Zoom sulla stessa slide, riquadro tratteggiato attorno alla nuvola ben visibile: i dati aziendali finiscono dentro un perimetro che l'azienda non controlla.

### Scena 40 · `frame-0197.png` · 19:36
Sopra la nuvola compare scritto a mano in blu **"STESSA RISPOSTA"** con una freccia che punta la nuvola, e a destra due grandi parentesi graffe a mano.
Tesi: se tu e il tuo competitor usate lo stesso modello senza contesto proprietario, ricevete **la stessa identica risposta** → l'uso dell'AI, da solo, ha **zero vantaggio competitivo**.

### Scena 41 · `frame-0199.png` · 19:48 — **slide "L'arbitraggio del cervello aziendale"** ⭐
Slide pulita, due colonne:
- Titolo: **"L'arbitraggio del cervello aziendale"** · sottotitolo: **"Chi si muove prima prende ciò che chi arriva dopo non recupera"**
- **Colonna 1 — "1. Si accumula"**: ciclo chiuso a tre nodi → **"Lo usi ogni giorno"** (azzurro) → **"La memoria cresce"** (verde) → **"Risposte migliori"** (rosa) → e ritorno. Didascalia: **"Il tempo non si compra"**.
- **Colonna 2 — "2. Quasi nessuno lo sa fare"**: una linea del tempo con icona pellicola, etichetta **"finestra aperta"**, e due punti: **"Oggi: 💎 vantaggio raro"** → **"Domani: 📄 normalità"**. Didascalia: **"Come il sito web nel 1999"**.

### Scena 42 · `frame-0202.png` · 20:06
Stessa slide, zoom sulla colonna 1: il ciclo è leggibile per intero.
