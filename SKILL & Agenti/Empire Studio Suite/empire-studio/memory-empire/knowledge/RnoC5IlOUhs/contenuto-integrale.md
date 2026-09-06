# Contenuto integrale - RnoC5IlOUhs

**"CORSO COMPLETO SECOND BRAIN 2h: Claude + Obsidian"**
Giovanni Beggiato - 2h18m50s - italiano - 20 capitoli ufficiali
Run: `empire-studio/runs/max18-v01-second-brain-obsidian` - Ingest 2026-09-04, studio chiuso 2026-09-06

> Archivio **integrale, non riassunto**. Parte 1 = tutto cio' che e' stato VISTO a schermo,
> 352 scene uniche su 352, copertura totale contata sul disco; Parte 2 = la trascrizione
> completa del parlato.
> Il video e' un tutorial screen-share: la maggior parte del valore (strutture di cartelle,
> prompt, codice, file generati) sta sullo schermo e **non viene mai detta a voce**. Senza la
> Parte 1 il corso e' dimezzato.
> I frame sono stati ri-estratti a **1280x720** dal video 1080p gia' sul disco: l'estrazione
> originale era a 640x360 e rendeva illeggibile il testo piccolo della UI.
> Le parti non leggibili sono marcate come tali e non sono state inventate.

---

# PARTE 1 - Tutto cio' che e' stato letto a schermo (352 scene)
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

### Scena 43 · `frame-0199.png` · 19:48 — [= vecchia Scena 41, già in `video-analysis.md`]
Verificato su HD: slide Excalidraw pulita "**L'arbitraggio del cervello aziendale**" / "Chi si muove prima prende ciò che chi arriva dopo non recupera", due colonne — "1. Si accumula" (ciclo Lo usi ogni giorno → La memoria cresce → Risposte migliori, cerchio chiuso, didascalia "Il tempo non si compra") e "2. Quasi nessuno lo sa fare" (icona finestra, "Oggi: 💎 vantaggio raro" → "Domani: 📄 normalità", didascalia "Come il sito web nel 1999"). Webcam PiP in basso a sinistra. Contenuto identico a quanto già scritto; l'HD non aggiunge dati nuovi rispetto alla versione già a wiki.
Voce: *"il fulcro di tutto è, e vorrei fermarmi sulla prima parte, che queste company Brain"*.

### Scena 44 · `frame-0202.png` · 20:06 — [= vecchia Scena 42, già in `video-analysis.md`]
Verificato su HD: stessa slide, inquadratura zoomata sulla colonna 1 (il pannello proprietà Excalidraw a sinistra è visibile — stroke/background/opacity/layers — segno che un elemento è selezionato). Nessun dato nuovo rispetto alla descrizione esistente.
Voce: *"sono che vedremo ora, sono dei giganteschi cervelli che cominciano a contenere mano tutta la conoscenza aziendale e cominciano a conoscervi nel corso del tempo."*

---

# PARTE 3 — L'arbitraggio si chiude: chi guadagna cosa (20:24 → 24:54)

### Scena 45 · `frame-0205.png` · 20:24
Stessa slide "L'arbitraggio del cervello aziendale", inquadratura ulteriormente stretta sulla colonna 1 (titolo e colonna 2 tagliati dal bordo destro del frame). Pannello proprietà Excalidraw ancora aperto a sinistra.
Voce: *"cominciamo ad utilizzarla la nostra memoria comincia a crescere, la conoscenza dell'AI diventa migliore per quanto riguarda la nostra azienda, quindi ci comincia a conoscere meglio. Riceveremo poi risposte migliori. Con risposte migliori noi potremmo continuare a riutilizzarla sempre in maniera più efficiente. Questo ciclo continua."*

### Scena 46 · `frame-0209.png` · 20:48
Stessa slide: il ciclo "1. Si accumula" viene ripercorso dal vivo con tratti **blu** ridisegnati sopra le frecce nere esistenti (Lo usi ogni giorno → La memoria cresce → Risposte migliori), evidenziandolo mentre l'autore parla.
Voce: *"fare una rappresentazione grafica super semplice, se questo"* — introduce il grafico ROI che disegnerà nella scena successiva.

### Scena 47 · `frame-0210.png` · 21:54 — **inizio del grafico ROI/Tempo a mano** ⭐
Vista scrollata a sinistra: canvas bianco vuoto con due tratti verticali neri separati (inizio disegno degli assi), la slide precedente spinta a destra e in parte tagliata (resta visibile "1. Si accumula" col ciclo blu e, appena leggibile al bordo, l'inizio della colonna 2).
Voce (frase lunga, 21:54→22:06): *"se questo è il vostro tempo e questo è il vostro ritorno sull'investimento che avete nell'utilizzare questo tipo di sistema, se voi non lo utilizzate, avrete una curva nell'utilizzo dell'AI più o meno fatta così […] perché i modelli di AI diventano migliori […] ma così anche tutti i vostri competitor, quindi non dimenticatevi che la curva dei competitor cresce esattamente come la vostra, quindi ha zero vantaggio competitivo. […] Mentre se utilizzate una company Brain come quella che avremo oggi, avremo una curva di questo tipo […] perché l'AI comincia a conoscervi sempre meglio e questo è esattamente il vostro vantaggio competitivo. […] chi vincerà nell'AI o"* — tesi centrale: senza company brain il vantaggio dell'AI è zero (tutti salgono alla stessa curva); con la company brain la curva è ripida e personale.
⚠️ Nota: il timestamp nominale in `_scene_index.json` per questa scena è 20:54, ma il frame mostra chiaramente l'inizio del disegno degli assi ROI/Tempo che nel transcript inizia solo verso 21:54-22:00 (subito prima del completamento visto in scena 48 a 22:06) — la citazione sopra è presa dalla finestra di trascrizione realmente coerente col contenuto visivo, non dal minuto nominale.

### Scena 48 · `frame-0222.png` · 22:06 — **il grafico ROI completo: con vs senza company brain** ⭐
Grafico a mano completato: assi **"ROI"** (verticale) e **"Tempo"** (orizzontale). Due curve: una **blu** ripida che sale quasi verticale a fine percorso, e una linea tratteggiata **verde/arancione alternata** molto più piatta. Tra le due, in corrispondenza dell'estremità destra, una **freccia rossa a doppia punta verticale** misura lo scarto, chiuso da una **parentesi graffa verde**. Slide precedente ("L'arbitraggio del cervello aziendale", ciclo "1. Si accumula") ancora visibile sulla destra del frame.
➕ La curva blu ripida rappresenta il ROI con company brain, la linea piatta tratteggiata il ROI senza (i "competitor" citati a voce); la freccia rossa è il vantaggio competitivo misurato.
Voce: *"chi avrà il miglior ritorno nell'investimento sono le aziende grosse perché loro hanno già dei processi, hanno già un sacco di conoscenza. Quindi l'AI può essere allenata su un sacco di dati. Noi ci stiamo muovendo in un mondo che è sempre più […] governato dai dati"*.

### Scena 49 · `frame-0225.png` · 22:24
Stesso grafico ROI/Tempo, inquadratura scrollata leggermente; in alto a sinistra compare la scritta a mano in rosso **"DAT[…]"** (inizio di "DATA", tagliata dal bordo — coerente con "data first" detto a voce).
Voce: *"data first. E con l'AI i dati sono il nuovo oro, come lo erano per i social media, ma ora ancora di più, ma in questo caso sono i vostri dati per la vostra azienda."*

### Scena 50 · `frame-0233.png` · 23:12 — **il "LAG" del competitor in ritardo** ⭐
Vista scrollata ulteriormente a sinistra: in alto **"[DA]TA FIRST"** (parzialmente leggibile, tagliato a sinistra) e sotto, in rosso, **"LAG"** con una linea tratteggiata rossa a onde sotto la scritta. Una linea verticale nera scende dall'asse fino a un **pallino rosso pieno** sull'asse Tempo, a metà percorso circa. Sulla destra restano visibili il grafico ROI (curva blu, linea tratteggiata verde/arancione, freccia rossa, parentesi verde) e la slide del ciclo "1. Si accumula" con "Lo usi ogni giorno / La memoria cresce / Risposte migliori" leggibili per intero.
➕ Il pallino rosso segna il punto temporale in cui un competitor/startup entra nel mercato "in ritardo"; "LAG" etichetta lo scarto da colmare.
Voce: *"che il vostro vantaggio competitivo è anche rispetto alla startup che vuole fregarvi […] che la startup avrà un lag, quindi un ritardo di tutta questa parte qui, ipotizzando che la startup […] entri qui. Avrà un ritardo di tutto questo periodo qui che voi avrete modo con la vostra AI di colmare."*

### Scena 51 · `frame-0234.png` · 23:18
Vista scrollata verso il basso/destra sulla slide "L'arbitraggio del cervello aziendale": titolo e sottotitolo tagliati dal bordo superiore ("…o del cervello aziendale" / "…ende ciò che chi arriva dopo non recupera"), colonna "2. Quasi nessuno lo sa fare" pienamente leggibile (finestra aperta, Oggi: 💎 vantaggio raro → Domani: 📄 normalità, "Come il sito web nel 1999"). Sul bordo sinistro, tagliati, riaffiorano frammenti della colonna 1 ("La memoria cresce" verde, un box rosa sopra) con una freccia blu.
Voce: *"definiamo arbitraggio. Ok? Quindi, come si misura l'arbitraggio? L'arbitraggio è la differenza tra […] quello che fate voi oggi e quello che fa il mercato domani. Voi avete un arbitraggio, sia che vendiate"*

### Scena 52 · `frame-0237.png` · 23:36 — **titolo "ARBITRAGGIO" scritto a mano** ⭐
Stessa inquadratura; in alto a destra, su spazio bianco vuoto, compare la scritta a mano in **blu, grande: "ARBITRAGGIO"** — nuova sezione che l'autore sta per costruire.
Voce: *"questo servizio che lo applichiate e poi andremo alla demo perché se voi oggi fate questo e oggi il vostro competitor sta facendo questo, questo qui è il vostro arbitraggio […] questo si articola in due parti, è il vantaggio competitivo dell'azienda che lo sta applicando alla propria ed è anche il fattore novità […] che voi potete portare in quanto freelancer per questa tipologia di servizio. Ovviamente questa finestra lentamente si chiuderà perché"*

### Scena 53 · `frame-0243.png` · 24:12 — **le due componenti dell'arbitraggio: VC e novità/ROI** ⭐
Sotto "ARBITRAGGIO" (blu), nuovo disegno in rosso e blu: due barre/parentesi verticali blu affiancate, e a destra in rosso una freccia verso l'alto con etichetta **"VC"**, e sotto un'altra freccia con etichetta **"NOVITÀ (ROI↗)"**; in basso a destra un piccolo rettangolo vuoto appena abbozzato (terzo elemento non completato in questo frame).
➕ "VC" = vantaggio competitivo dell'azienda che applica la company brain; "NOVITÀ (ROI↗)" = il fattore novità/ROI che il freelancer porta rivendendo il servizio — le due parti dell'arbitraggio appena enunciate a voce.
Voce: *"uno perché canali YouTube come il mio servono a aumentare la consapevolezza di quello che si può fare. Due, perché ci sono, per esempio, community come la mia, nella quale io insegno ad imprenditori e freelancer come applicare queste cose nella loro azienda o come rivenderle. Quindi, ovviamente, chi prima comincia meglio si trova."*

### Scena 54 · `frame-0247.png` · 24:36
Talking head puro, nessun testo a schermo; mani aperte a mezz'aria mentre gesticola.
Voce: *"convincervi che guardare questo corso avrà un elevato ROI per voi. E ora"*

### Scena 55 · `frame-0248.png` · 24:42
Talking head, stessa inquadratura, bocca aperta a metà frase.
Voce: *"direi procediamo alla demo di modo tale che voi possiate capire anche a livello pratico qual è effettivamente il vantaggio e vederlo proprio e toccarlo con mano. Ed ecco con cosa stiamo"*

---

# PARTE 4 — Demo della Company Brain con 22.000 note (24:54 → 30:48)

### Scena 56 · `frame-0250.png` · 24:54 — **prima vista della graph view + pannello Filters di Obsidian** ⭐
Screen-share Obsidian, tema scuro, **graph view**. Sidebar sinistra con la cartella `data` evidenziata (verde lime) espansa in un lungo elenco di note, tutte con prefisso `data-benchmark-…`: si leggono tra gli altri `data-benchmark-burn-multiple-d…`, `data-benchmark-cac-vs-benchma…`, `data-benchmark-churn-vs-benchm…`, `data-benchmark-costo-di-servi…`, `data-benchmark-crescita-ar-vs-…`, `data-benchmark-densita-dispo…`, `data-benchmark-emissioni-esafat…`, `data-benchmark-energia-gestita…`, `data-benchmark-fte-su-cas-vs…`, `data-benchmark-indice-di-fund…`, `data-benchmark-lead-time-sodd…`, `data-benchmark-margine-per-…`, `data-benchmark-nrr-vs-benchma…`, `data-benchmark-penetrazione-doc…`, `data-benchmark-pipeline-coverage`, `data-benchmark-quota-ricorrent…`, `data-benchmark-riparazioni-energ…`, `data-benchmark-rule-of-40-su-…`, `data-benchmark-tasso-di-adoz…`, `data-benchmark-tempo-medio-di…`, `data-benchmark-uptime-sla-di…` (nomi troncati a destra dalla sidebar, non tutti leggibili per intero — non trascrivere oltre il visibile). In alto un contatore file/filtri non leggibile con certezza. A destra, pannello **Filters** nativo di Obsidian con: campo "Search files...", toggle **Tags / Attachments / Existing files only / Orphans**, sezione **Groups**, sezione **Display** (Arrows, Text fade threshold, Node size, Link thickness, bottone arancione **Animate**), sezione **Forces** (Center force, Repel force, Link force, Link distance). La sfera del grafo è ancora compatta.
Voce: *"giocando. Questa sarà la company Brain che noi con calma andremo ora a"*

### Scena 57 · `frame-0251.png` · 25:00 — **legenda completa delle cartelle colorate** ⭐
Stessa graph view; la sidebar ora mostra la **legenda completa** con tutte le cartelle e il relativo colore-gruppo: `_showcase`, **areas** (arancione), `code`, **concepts** (verde/teal), **data** (verde lime), **docs** (azzurro), `entities`, **outputs** (viola), **projects** (giallo), `scripts`, **self** (rosso/rosa), `sources`, **workspace** (blu); sotto, senza colore: `CONVENTIONS`, `README`, `tutorial-completo`, `tutorial-pratico`. Pannello Filters identico alla scena precedente. Sfera del grafo compatta, nei toni verde/blu/viola/giallo.
Voce: *"ricostruire in questo video. Ovviamente non useremo tutti i file che sono qua dentro, sono 22.500 note. Questa è una company Brain Production Ready, totalmente"*

### Scena 58 · `frame-0253.png` · 25:12 — **la sfera con l'anello di file orfani** ⭐
Vista ingrandita/riposizionata della stessa graph view: il pannello Filters è ora ridotto a due sole icone in alto a destra. La sfera occupa gran parte del frame e mostra con chiarezza un **anello esterno tratteggiato di punti bianchi** che circonda l'intera sfera densa colorata — i file orfani, isolati dal grafo principale. Legenda cartelle a sinistra identica e pienamente leggibile.
➕ L'anello di punti bianchi isolati è lo stesso fenomeno che il capitolo (da `ingest.json`) chiamerà poi "Problematica dei file orfani in Obsidian".
Voce: *"funzionante, vedete? è abbastanza massiva eh per essere una company brain."*

### Scena 59 · `frame-0254.png` · 25:18
Stessa graph view, legenda cartelle piena e leggibile (identica alla scena 57), cursore in alto a sinistra vicino alla voce `_showcase`. Sfera invariata.
Voce: *"Vi replicheremo esattamente la struttura e vi farò vedere poi come dividere le"*

### Scena 60 · `frame-0255.png` · 25:24
Stessa graph view, cursore ora sopra la riga `code` della legenda (seconda voce).
Voce: *"cose. Vi darò i prompti per poter inserire le vostre cose all'interno di questa cosa qui. Questa è production ready, quindi che cosa vuol dire? che in questo tutorial andremo a vedere come costruire queste cartelle, andremo a vedere come collegarla con il nostro notion di modo tale da avere un layer"*

### Scena 61 · `frame-0258.png` · 25:42 — **il layer Notion: tabella "Clienti"** ⭐
Screen-share Notion. Breadcrumb in alto: "New page › Cruscotto Aurora › **Clienti**", a destra "Edited 22h ago", pulsante "Share", stella. Sidebar sinistra: "Home", sezione **Meetings** ("Connect your calendar", "New AI meeting note"), sezione **Recents**: **Clienti** (selezionata), "Cruscotto Aurora", "Company Brain — Tutti i prom…" (troncato), "New page", "Reparti", "Prodotti", "Default view", "KPI mensili", "Sedi", "Competitor"; sezione **Agents**: "New agent"; sezione **Shared**. Corpo pagina: titolo "📁 Clienti", vista "Default view", tabella con colonne **Cliente** (Aa) · **ARR** (#) · **Città'** · **Del** (#) · **MQ** (#) · altra colonna troncata "Pro…"; le celle sono barre grigie segnaposto (dato non renderizzato/nascosto in questo frame, non i valori reali).
➕ Questo è il "layer visivo per noi" di cui parla la voce nella scena successiva: Notion sopra gli stessi dati che vivono in Obsidian.
Voce: *"per le AI per capire come trovare i dati"*

### Scena 62 · `frame-0259.png` · 25:48
Torna la graph view di Obsidian, ora vista più zoomata: legenda ridotta a sole barre colorate senza etichette leggibili (in alto a sinistra) e una colonna verticale di icone sul bordo destro dello schermo con etichette parziali **"Meet"**, **"Back"**, **"Agents"**, **"Shared"**, **"Assistant"** — verosimilmente il rail di un'altra applicazione/estensione visibile dietro la finestra Obsidian, non identificabile con certezza.
Voce: *"e anche un layer visivo per noi per poterci interfacciare con l'AI, no? E dopo e questa ha anche tutta la parte di"*

### Scena 63 · `frame-0260.png` · 25:54 — **il database vettoriale Qdrant dietro il RAG** ⭐
Screen-share browser, URL **`localhost:6333/dashboard#/collections`**. Interfaccia **Qdrant**: sidebar sinistra "Welcome, Console, **Collections** (selezionata), Tutorial, Datasets, Access Tokens". Pannello principale, titolo "Collections", barra ricerca "Search Collection", pulsanti "+ Create Collection" e "Upload Snapshot". Tabella con intestazioni **NAME · STATUS · POINTS (APPROX) · SEGMENTS · SHARDS · VECTORS CONFIG · ACTIONS**; unica riga:
- NAME: **`company_brain`**
- STATUS: **GREEN**
- POINTS (APPROX): **22 205**
- SEGMENTS: **6**
- SHARDS: **1**
- VECTORS CONFIG: **`dense` 384 · Cosine** / **`bm25` Sparse**
Questo è lo stack RAG reale dietro la company brain: retrieval ibrido denso (embedding 384 dimensioni, similarità coseno) + sparso (BM25), 22.205 punti indicizzati.
Voce: *"Rag connesso. Ovviamente per un video YouTube questa parte è troppo difficile, quindi avrebbe poco senso che io vi faccia vedere come scalare un sistema a 22.500 note production ready. Se siete un imprenditore o un freelancer e volete"*

### Scena 64 · `frame-0263.png` · 26:12
Stessa graph view con legenda piena, cursore spostato leggermente in alto a sinistra. Nessun cambiamento sostanziale rispetto alla scena 59.
Voce: *"approfondire questi servizi e ricevere il prompt applicare questo one shot nella vostra azienda, vi lascio il link sotto in descrizione che è il link per la mia community. Bene, detto questo, cominciamo a testarla per farvi vedere cosa andremo a fare oggi. Allora, andiamo nella nostra company knowledge base, quindi in quella gigantesca e"*

### Scena 65 · `frame-0266.png` · 26:30 — **apertura della company brain reale in "Antigravity IDE"** ⭐
Finestra di sistema macOS "Apri file" sopra uno sfondo scuro con la scritta parziale **"Antigravity IDE"** e, in basso a destra, l'etichetta **"Antigravity - Settings"**. Titolo del dialogo: **"Company Knowledge Base"** con contatore "0" accanto. Colonna sinistra del dialogo: Recents, Shared, Favorites (Applications, **Desktop** selezionata in blu, Documents, Downloads), Locations (iCloud Drive, "giovannibe…", "Macintosh…"), Tags (Red). Colonna centrale, gruppo "Yesterday": "3. Business p…pandadoc.mov", **"Company Knowledge Base"** (evidenziata in blu), "Knowledge Base", "Second Brain"; gruppo "April": "Giovanni Beggiato", "headshot"; gruppo "March": "LinkedIn". Colonna destra: contenuto della cartella selezionata — file `tutorial-pratico.md` in alto, poi sotto "Previous 7 Days": cartelle **`_showcase`, `areas`, `code`, `concepts`**, file `CONVENTIONS.md`, cartelle **`data`, `docs`, `entities`**, un file di testo (nome non leggibile con certezza), cartella **`outputs`** (lista tagliata dal bordo inferiore del dialogo, prosegue oltre il visibile). Pulsanti in basso: "New Folder", "Cancel", **"Open"** (blu).
Voce: *"apriamola. E adesso cominciamo con il fare una qui un po' ehm diciamo"*

### Scena 66 · `frame-0267.png` · 26:36 — **le 11 cartelle come file reali su disco, dentro Antigravity + Claude Code** ⭐
La company brain è ora aperta dentro **Antigravity IDE** (interfaccia stile VS Code). Tab attiva in alto: **"Claude Code"** (icona rossa), sotto "Untitled". Sidebar **Explorer**, root **"Company Knowledge Base"** espansa, elenco per intero dall'alto: cartelle **`_showcase`, `.claude`, `.obsidian`, `.tmp`, `areas`, `code`, `concepts`, `data`, `docs`, `entities`, `outputs`, `projects`, `scripts`, `self`, `sources`, `workspace`**; file **`.env`, `.gitignore`, `CONVENTIONS.md`**, un file `.txt` (nome non leggibile con certezza), **`README.md`, `tutorial-completo.md`, `tutorial-pratico.md`** (questi ultimi due evidenziati/gialli, probabilmente aperti o modificati di recente).
Corpo editor: schermata vuota di benvenuto Claude Code — logo **"🔴 Claude Code"**, una piccola icona pixel-art arancione (alieno/robot), testo **"// TODO: Everything. Let's start."**. Barra prompt in basso: placeholder "Esc to focus or unfocus Claude", icone "+" e file, toggle rosso **"Bypass permissions"** con punto esclamativo.
Pannello destro: intestazione **"Company Knowledge Base"**, campo chat "Ask anything, @ to mention, / for act…", selettore modello **"Gemini 3.5 Flash (Medium)"** con freccia a tendina, icona microfono. Barra di stato in basso: "Screen Reader Optimized", "Antigravity - Settings".
➕ Conferma che l'ambiente di lavoro dell'autore combina **Antigravity** (IDE agentico) con **Claude Code** in un pannello e un secondo agente **Gemini 3.5 Flash** nel pannello laterale, entrambi puntati sulla stessa cartella `Company Knowledge Base` — cioè le 11 cartelle sono già la vera struttura su disco, non solo uno schema teorico.
Voce (frase lunga, la "query ingannevole" di test): *"ingannevole per l'AI, perché vogliamo testare quanto forte è l'AI. Ehi, sai dirmi qual è il cliente più grosso per questa azienda? […] Quello che noi vediamo ora è che il cliente più grosso è Residenze Aurora Verde, che è €620.000 di ARR."*

### Scena 67 · `frame-0276.png` · 27:30 — **tabella "Clienti" completa in Notion (verifica dei dati)** ⭐
Notion, pagina "Clienti", tabella con colonne **Cliente · ARR · Città' · Dal · MQ · Pro[dotti]** (troncata). Prime 20 righe leggibili per intero:
| Cliente | ARR | Città | Dal | MQ | tag prodotto |
|---|---|---|---|---|---|
| Residenze Aurora Verde (badge "OPEN" al passaggio del mouse) | €620.000,00 | Brescia | 2014 | 90000 | Care |
| Polo Universitario Sud | €597.000,00 | Catania | 2024 | 60000 | Edge |
| Torre Eurosky Uffici | €558.000,00 | Roma | 2016 | 90000 | Cloud |
| BioPharma Stabilimenti | €555.000,00 | Latina | 2022 | 40000 | Edge |
| Galleria Moderna | €552.000,00 | Firenze | 2018 | 40000 | Care |
| Iberia Centros | €528.000,00 | Madrid | 2013 | 18000 | Care |
| Università Politecnica Adriatica | €522.000,00 | Ancona | 2021 | 60000 | Care |
| Museo delle Arti Contemporanee | €511.000,00 | Torino | 2017 | 25000 | Care |
| MediCenter Salute | €508.000,00 | Padova | 2013 | 12000 | Cloud |
| Aurora DACH Buildings | €486.000,00 | Monaco di Baviera | 2014 | 8000 | Care |
| Distretto Tessile Pratese | €420.000,00 | Prato | 2020 | 25000 | Care |
| Retail Gamma | €402.000,00 | Verona | 2022 | 8000 | Edge |
| Nordic Retail Chain | €370.000,00 | Amburgo | 2024 | 12000 | Edge |
| Centro Direzionale Partenope | €369.000,00 | Napoli | 2013 | 25000 | Cloud |
| Industria Meccanica Veneta | €347.000,00 | Vicenza | 2018 | 12000 | Care |
| Stadio Arena Nuova | €343.000,00 | Udine | 2013 | 90000 | Care |
| Supermercati Risparmio | €314.000,00 | Bologna | 2022 | 8000 | Care |
| Helvetia Office Park | €309.000,00 | Zurigo | 2021 | 12000 | Care |
| Banca Civica | €278.000,00 | Torino | 2017 | 18000 | Care |
| Terranova Sviluppo | €277.000,00 | Bologna | 2016 | 90000 | Care |
Il badge "OPEN" compare solo sulla riga sotto il cursore (comportamento hover), non è un tag permanente — confermato confrontando con la scena 73 dove "OPEN" appare invece su un'altra riga.
Voce: *"corretto, no? Quindi vediamo che l'AI ha interpretato bene la nostra richiesta […] Ora questo è una semplice quemo […] Hey! Il polo universitario sud ha incrementato il suo ARR, quindi il suo ricavo annuo nei nostri confronti e ha ora un ARR di €750.000 l'anno. Puoi per favore aggiornare Obsidian e assicurarti che tutto sia aggiornato? Perfetto, premiamo invio e"*

### Scena 68 · `frame-0287.png` · 28:36 — **il thought-process di Claude Code letto riga per riga** ⭐
Antigravity IDE, tab "Identify largest client for company". Trascrizione integrale della conversazione visibile:
> "Hey, sai dirmi qual è il cliente più grosso per questa azienda?"
> ● Controllo nel vault i dati clienti.
> ● **Bash** — List entities and views folders
> &nbsp;&nbsp;`ls "/Users/giovannibeggiato/Desktop/Company Knowledge Base/entities/" "/Users/giovannibeggiato/Desktop/Company Knowledge Base/scripts/rag/views/" 2>/dev/null`
> &nbsp;&nbsp;output: `<persisted-output>` "Output too large (41.1KB). Full output saved to: /Users/giovannibeggiato/.claude/projects/-Users-giovannibeggiato-Desktop-Company-Knowledge-Base/8546614f-6fa7-4583-a…" (troncato dal bordo)
> ● Thought for 1s
> ● **Read** `view-clienti-arr.md`
> ● **Bash** — List overrides directory
> &nbsp;&nbsp;`ls -la "/Users/giovannibeggiato/Desktop/Company Knowledge Base/workspace/overrides/" 2>/dev/null` → output: `cliente-residenze-aurora-verde.md`
> ● Thought for 1s
> "C'è un override su Residenze Aurora Verde, lo controllo prima di risponderti."
> ● **Read** `cliente-residenze-aurora-verde.md`
> ● Thought for 4s
> "Il cliente più grosso è **Residenze Aurora Verde** (Brescia, segmento SMB) con **620.000 EUR di ARR**. Il dato viene dalla vista `view-clienti-arr.md` e include l'override manuale che hai applicato il 9 giugno (ARR portato da 590.000 a 620.000 EUR, già propagato alla vista). Al secondo posto c'è Polo Universitario Sud con 597.000 EUR, quindi anche senza l'override Residenze Aurora Verde resterebbe comunque in vetta con un margine minimo. In totale i 34 clienti nominati valgono 10.866.000 EUR di ARR."
Sidebar Explorer identica alla scena 66 (le 11 cartelle + `.claude`, `.obsidian`, `.tmp` + i file di root).
➕ Questo è l'esempio concreto di come l'AI usa `view-clienti-arr.md` (una vista/aggregazione) insieme a un file di **override** manuale prima di rispondere — il meccanismo "canon vs override" che il video approfondirà più avanti.
Voce: *"Vediamo che cosa sta facendo nel nostro thought process. Comincia a fare i vari comandi, comincia ad entrare dentro la nostra azienda, vedete? comincia a leggere i vari file markdown e dopo arriva alle informazioni"*

### Scena 69 · `frame-0288.png` · 28:42 — **script `edit_fact.py` e `propagate.py`, skill `canon-edit`/`brain-sync`** ⭐
Sidebar Explorer: cartella `entities` espansa con l'elenco clienti (`cliente-coop-abitare.md`, `cliente-datahall-nord.md`, `cliente-distretto-tessile-prat…`, `cliente-fiera-centrale.md`, `cliente-galleria-moderna.md`, `cliente-grand-hotel-lacuale…`, `cliente-helvetia-office-park…`, `cliente-hotel-belvedere-grou…`, `cliente-iberia-centros.md`, `cliente-immobiliare-lombard…`, `cliente-industria-meccanica…`, `cliente-logiport-italia.md`, `cliente-logistica-tirrenica.md`, `cliente-medicenter-salute.md`, `cliente-museo-delle-arti-con…`, `cliente-nordic-retail-chain.md`, `cliente-outlet-del-sole.md`, `cliente-polo-universitari…` [M], `cliente-porto-antico-spazi.md`, `cliente-residenze-auror…` [M], `cliente-retail-gamma.md`, `cliente-stadio-arena-nuova.md`, `cliente-supermercati-rispar…`, `cliente-terranova-sviluppo.md`, `cliente-torre-eurosky-uffici.md`, `cliente-universita-politecnica…`, `competitor-cubit-energy.md`).
Chat, trascrizione integrale:
> "Hey, il Polo Universitario Sud ha incrementato il suo ARR, quindi il suo ricavo nei nostri confronti è ora di 750.000 euro. Puoi per favore aggiornare Obsidian e assicurarti che tutto sia aggiornato?"
> ● Thought for 1s
> ● **canon-edit** *(skill)*
> ● Thought for 0s
> ● **Bash** — Write ARR override for Polo Universitario Sud
> &nbsp;&nbsp;`cd "/Users/giovannibeggiato/Desktop/Company Knowledge Base" && python3 scripts/edit_fact.py --nome "Polo Universitario Sud" --campo arr --valore 750000 --date 2026-0…` (comando troncato dal bordo destro)
> &nbsp;&nbsp;output: "Override scritto e VISIBILE in Obsidian (non sarà 'coperto' da generate_notes): nota override: `workspace/overrides/cliente-polo-universitario-sud.md` · scheda: `entities/cliente-polo-universitario-sud.md`"
> ● Thought for 6s / Thought for 0s
> ● **Bash** — Open override note and client card in Obsidian
> &nbsp;&nbsp;`open "/Users/giovannibeggiato/Desktop/Company Knowledge Base/workspace/overrides/cliente-polo-universitario-sud.md" && open "/Users/giovannibeggiato/Desktop/Company K…"` → (Bash completed with no output)
> ● **brain-sync** *(skill, barra di progresso teal in corso)*
> ● Thought for 1s
> ● **Bash** — Run full propagation (canon, views, Qdrant, Notion, audit)
> &nbsp;&nbsp;`cd "/Users/giovannibeggiato/Desktop/Company Knowledge Base" && python3 scripts/propagate.py`
> &nbsp;&nbsp;stato: "Correcting…" / "Connecting…" (parola non leggibile con piena certezza)
Campo input in basso: "Queue another message…" con allegato `cliente-polo-universitario-sud.md`.
➕ Riga di comando esatta per aggiornare un fatto: `python3 scripts/edit_fact.py --nome "<Nome>" --campo <campo> --valore <valore> --date <data>`; propagazione con `python3 scripts/propagate.py` (dichiarato: canon, views, Qdrant, Notion, audit).
Voce: *"vedete che ora quello che sta facendo è il brain sync. Che cosa vuol dire? […] sta adesso facendo una propagazione completa su tutti i sistemi che abbiamo collegato. Quindi ora quello che farà sarà prima scrivere su Obsidian […] e dopo una volta fatto utilizzerà questa skill per aggiornare tutte le nostre interfacce grafiche di modo tale che tutti abbiano live accesso a tutte le informazioni di cui abbiamo bisogno."*

### Scena 70 · `frame-0294.png` · 29:18 — **verifica in Notion: propagazione riuscita**
Notion "Clienti": la riga **Polo Universitario Sud** ora mostra **€750.000,00** (Catania, 2024, 60000, Edge), evidenziata/selezionata con sottolineatura blu, sopra **Residenze Aurora Verde** €620.000,00 (Brescia, 2014, 90000, Care). L'aggiornamento scritto da Claude Code è arrivato fino a Notion.
Voce: *"750.000"*

### Scena 71 · `frame-0295.png` · 29:24 — **cartella `workspace/overrides` e i file di eval/audit** ⭐
Antigravity IDE, sessione Claude Code vuota ("Tired of repeating yourself? Tell Claude to remember what you've told it using **CLAUDE.md**."). Sidebar Explorer: `code`, `concepts`, `data`, `docs`, `entities`, `outputs`, `projects`, `scripts`, `self`, `sources`, **`workspace`** espansa con dentro `journal` (cartella) e **`overrides`** espansa (`cliente-polo-universita…md` [M], `cliente-residenze-auro…md` [M]); poi, allo stesso livello, una serie di file sciolti dentro `workspace`: `_audit_sample.json`, `_eval_gold.json`, `_eval_questions.json`, `_eval_results_full.json`, `_eval_results_rag_baseline.j…`, `_eval_results_rag_prod…` [M], `_eval_results.json`, `_index.md`, `_redteam_ans.json` [M], `_redteam.json`, `canon.json` [M], `enrich.log`, `notes.json` [M].
➕ Questi nomi (`_eval_gold`, `_eval_questions`, `_redteam`, `canon.json`, `enrich.log`) anticipano il capitolo sui gate di qualità e gli script di controllo (da `ingest.json`): la company brain ha già in `workspace/` un proprio impianto di valutazione/red-teaming del RAG.
Voce: *"l'anno e se noi andiamo nella nostra conversazione e gli ridiamo il solito prompt che abbiamo visto prima, dovremmo, se tutto va bene, ricevere che il nostro cliente, diciamo, più grosso è questo Polo Sud."*

### Scena 72 · `frame-0301.png` · 30:00 — **anatomia completa di una scheda-cliente (`cliente-polo-universitario-sud.md`)** ⭐
Vista divisa: a sinistra la chat Claude Code ripete la query e risponde citando il file; a destra l'**editor con il file aperto per intero**, breadcrumb `entities > cliente-polo-universitario-sud.md`. Contenuto integrale letto riga per riga:
```
---
title: Polo Universitario Sud
summary: Scheda dei clienti di Aurora Sistemi.
tags: [entities, tipo/cliente, status/active]
status: active
created: 2026-06-08
updated: 2026-06-08
related: "[[soc-clienti]],[[sito-polo-universitario-sud-1]] [[segmento-smb]]"
---

# Polo Universitario Sud

**Polo Universitario Sud (Education, Catania)**

È considerato un cliente SMB, con una superficie complessiva di 60000 mq distribuiti su 9 edifici.

Il cliente genera un ARR (Annual Recurring Revenue) di 750000 EUR.

## Prodotti e Servizi in Uso

Polo Universitario Sud utilizza i seguenti prodotti e servizi di Aurora Sistemi:
- Edge
- Care
- Cloud

## Voci collegate
- [[soc-clienti]]
- [[sito-polo-universitario-sud-1]]
- [[segmento-smb]]
```
Risposta chat a sinistra: *"Il cliente più grosso è Polo Universitario Sud (Education, Catania): genera un ARR di 750.000 EUR, il più alto tra tutti i 34 clienti nominati di Aurora Sistemi. È un cliente SMB dal 2024, con 60.000 mq su 9 edifici, e usa Edge, Care e Cloud. Per contesto, i successivi in classifica sono Residenze Aurora Verde (620.000 EUR) e Torre Eurosky Uffici (558.000 EUR), su un ARR totale clienti di 11.019.000 EUR."*
➕ Questa è la seconda "nota atomica" mostrata per intero nel video (dopo `kpi-2025-edifici` in `video-analysis.md` scena 5): stesso schema properties (title/summary/tags/status/created/updated/related) + corpo con wikilink `[[…]]` in coda.
Voce: *"qui vediamo che il cliente ha un ARR di €750.000,00 e questo si è ripercosso ovunque anche poi nel nostro database. Quindi questo è esattamente quello che andremmo a creare oggi. Andremo anche a capire come il collegamento con Notion avviene e cioè letteralmente"*

### Scena 73 · `frame-0304.png` · 30:18
Notion "Clienti": stessa tabella, ora con **Polo Universitario Sud** in prima riga (€750.000,00, Catania, 2024, 60000, Edge) seguito da Residenze Aurora Verde (€620.000,00). Il badge "OPEN" compare questa volta sulla riga "Museo delle Arti Contemporanee", sotto il cursore — conferma che è un elemento hover, non un tag fisso.
Voce: *"ricostruiremo questa interfaccia e alla fine voi avrete modo di cominciare"*

### Scena 74 · `frame-0305.png` · 30:24
Torna la graph view di Obsidian con legenda cartelle piena e sfera colorata invariata.
Voce: *"a popolare la vostra company Brain di modo tale che possa diventare una sfera perfetta, insomma, come questa. Benissimo, detto questo, andiamo alla parte pratica e un piccolo disclaimer è che per fare questo video vi ho preparato, che trovate nel secondo link in descrizione, un company brain con"*

### Scena 75 · `frame-0308.png` · 30:42 — **il documento "Company Brain — Tutti i prompt del tutorial" (parte 1)** ⭐
Notion, pagina privata **"Company Brain — Tutti i prompt del tutorial (segui passo passo)"** (emoji 🧠 rosa, immagine di copertina pittorica). Contenuto integrale visibile:
> **TLDR**
> Se sei un imprenditore e vuoi applicare AI nella tua azienda (creando un secondo cervello con claude e molto altro) OPPURE se sei un freelancer e hai intenzione di rivendere questo servizio ad aziende, ti consiglio di controllare questo link:
>
> **AVANAGUARDIA-PLUS.**
> Un consulente AI fa formazioni su questi argomenti per €1.000+ / giorno, in Avanguardia-Plus li trovi (aggiornati) a $99… quindi €85!
>
> Cominciamo:
> 📁 *Il Passo 1 si fa a mano dentro Obsidian (nessun prompt all'AI): trovi i blocchi di testo da scrivere. I prompt numerati per l'AI partono dal Passo 2.*
>
> TLDR
> &nbsp;&nbsp;AVANAGUARDIA-PLUS.
> &nbsp;&nbsp;Passo 1 — Obsidian, la prima nota, i collegamenti (a mano)
> &nbsp;&nbsp;Passo 2 — Le 11 cartelle e le prime note con l'AI
Voce: *"tutti i prompt modo tale che voi possiate farli passo passo. È una bre"*

### Scena 76 · `frame-0309.png` · 30:48 — **indice completo dei 14 prompt + inizio Passo 1 ("aurora-cervello")** ⭐
Stessa pagina Notion, scrollata. Indice TLDR completo (trascrizione integrale):
> Prompt 2 — Estrai il canon (prima un piano, poi il tuo ok)
> Prompt 3 — Trasforma il canon in note atomiche (prima gli hub)
> Prompt 4 — Completa il cervello fino a circa 28 note
> **Passo 3 — Gate di qualità, indice per le AI, showcase, grafo, GitHub**
> &nbsp;&nbsp;Prompt 5 — Il gate di qualità (solo referto)
> &nbsp;&nbsp;Prompt 6 — Correggi e ripeti finché esce "0 errori"
> &nbsp;&nbsp;Prompt 7 — Genera l'indice per le AI (llms.txt)
> &nbsp;&nbsp;Prompt 8 — Lo showcase (la fotografia per la demo)
> &nbsp;&nbsp;Impostazioni grafo a sfera (a mano, in Obsidian)
> &nbsp;&nbsp;Prompt 9 — Metti il vault sotto git (senza push)
> **Passo 4 — Interrogare il cervello, mostrarlo, tenerlo vivo**
> &nbsp;&nbsp;Prompt 10 — Interroga il cervello (a 28 note, senza RAG)
> &nbsp;&nbsp;Prompt 11 — La domanda di incrocio (dove le cartelle si arrendono)
> &nbsp;&nbsp;Prompt 12 — Il cruscotto HTML locale
> &nbsp;&nbsp;Prompt 13 — Apri la sessione (il briefing)
> &nbsp;&nbsp;Prompt 14 — Chiudi la sessione (il diario)
>
> **Passo 1 — Obsidian, la prima nota, i collegamenti (a mano)**
> Nessun prompt all'AI qui: si fa una volta sola, dentro Obsidian.
> 1. Installa Obsidian e crea il contenitore vuoto
>    - Vai su `obsidian.md`, scarica la versione per il tuo sistema (Mac o Windows) e installala.
>    - Crea sul computer una cartella nuova e vuota: `aurora-cervello`.
>    - Apri Obsidian → "Apri cartella come vault" ("Open folder as vault") → seleziona `aurora-cervello`.
> 2. Prima nota — crea (Cmd+N / Ctrl+N), chiamala `self-identita-aurora`, e scrivi nel corpo:
➕ Numerazione dei prompt non contigua nel testo visibile (si passa da "Passo 1" a "Prompt 2"): il "Prompt 1" non compare in questo frame, probabilmente enunciato nella parte di pagina non scrollata fin qui.
Voce: *"breve descrizione, insomma. Quindi, andate lì e se volete fare, e ve lo consiglio, le cose passo passo con me […] per favore andate nel file, mettetevelo in un secondo schermo e poi riuscite a seguire facendo tutto. Cominciamo con il scaricare Obsidian e dopo vi spiego"*

---

# PARTE 5 — Installazione e basi di Obsidian (31:12 → 35:18)

### Scena 77 · `frame-0313.png` · 31:12
Chrome, nuova scheda, home Google generica. Barra preferiti con cartelle/bookmark: "Claude, LinkedIn, Canva, Outlook, Agency, Clienti, Sites, Video, Typeform - Works…, X, YouTube Video Do…, YT Team, Tweet | store di…" (alcuni nomi troncati dalla barra).
Voce: *"brevemente che cos'è perché c'è un po' di fraintendimento. Allora, andiamo qui, ovviamente premiamo Obsidian. Perfetto,"*

### Scena 78 · `frame-0314.png` · 31:18
Risultati Google per "**obsidian download**": primo risultato "Obsidian › https://obsidian.md › download" — "Download" — *"23 Mar 2026 — Obsidian is available on all major platforms. Download Obsidian for iOS, Android, macOS, Windows and Linux. 4.7★★★★★ (989) · Free · Utilities/Tools"*; poi "Obsidian - Sharpen your thinking"; poi "Download and install Obsidian - Obsidian Help".
Voce: *"possiamo andare qua, premere download e fate download per macOS o insomma"*

### Scena 79 · `frame-0315.png` · 31:24 — **pagina download, versione in scaricamento**
`obsidian.md/download`, sezione "App" con righe per piattaforma: **iOS → App Store**; **Android → Google Play / APK**; **Windows → Universal**; **Mac → Universal**; **Linux → AppImage / Snap / Deb / AppImage (AArch64, ARM64) / Flatpak** (Community maintained). In basso a sinistra una barra di download in corso, nome file parzialmente leggibile che termina in *"…sidian-1.12.7-arm64.AppIma…"* (bordo taglia il resto — non leggibile con certezza oltre questo frammento).
⚠️ Il frammento visibile suggerisce un pacchetto Linux AppImage, mentre la voce poco prima parla di "macOS" — non risolvibile con certezza da questo solo frame; la versione **1.12.7** è comunque confermata anche nella scena 81.
Voce: *"qualsiasi cosa voi abbiate. Ed una volta che lo avete aperto dovreste avere questo questa schermata qui insomma"*

### Scena 80 · `frame-0316.png` · 31:30 — **la cartella "aurora cervello" creata sul Desktop**
Desktop macOS (sfondo lago/montagne). Icone in alto: "Giovanni Beggiato", **"aurora cervello"** (nuova cartella blu), "Company Knowledge Base", "Second Brain", "Knowledge Base", "Agentic Personal", "Archive"; colonna destra: video "3. Business part - pandadoc.mov", "OBS Recordings", "LinkedIn", "headshot", "Agentic Personal copy", "Company Brain", "Screenshot 2026-0…t 10.31.08". Dock in basso con, tra le altre, le icone di WhatsApp (verde), **Obsidian** (gemma viola) e Notion (N nera); una freccia blu disegnata a mano punta verso il basso, verso l'icona di Obsidian nel dock.
Voce: *"nel desktop, questa applicazione che viene fuori. La cosa che facciamo adesso è creare questa cartella. Io ho chiamato la nostra cartella di lavoro Aurora Cervello. Perché lo faremo? Perché Obsidian è un layer che va sopra la cartella e ci permette di avere una rappresentazione visiva di quello che c'è. Quindi ad Obsidian serve una cartella per mostrarci i dati. Allora, cominciamo ad aprirlo. Voi premerete, allora farete open folder"*

### Scena 81 · `frame-0321.png` · 32:00 — **schermata di scelta vault di Obsidian, versione 1.12.7** ⭐
Dialogo Obsidian sopra il desktop. Lista vault recenti a sinistra: "aurora cervello" (`/Users/giovannibeggiato/Desktop`), "Company Knowledge Base" (stesso percorso), "Company Brain" (stesso percorso), "Knowledge Base" (stesso percorso), "Second Brain" (stesso percorso). Pannello destro: logo Obsidian, **"Obsidian"**, **"Version 1.12.7"**; tre opzioni — **"Create new vault"** / "Create a new Obsidian vault under a folder." → pulsante "Create"; **"Open folder as vault"** / "Choose an existing folder of markdown files." → pulsante "Open"; **"Open vault from Obsidian Sync"** / "Set up a synced vault with existing remote vault." → pulsante "Sign in"; selettore lingua "English".
Voce: *"as vault e andremo in Aurora cervello. Quindi, semplicemente ora abbiamo la"*

### Scena 82 · `frame-0322.png` · 32:06 — **vault vuoto appena aperto**
Finestra Obsidian aperta sul vault "aurora cervello" (nome visibile in basso a sinistra nella status bar). Tab in alto: **"Graph view"**, completamente vuota (nessun nodo, perché il vault non contiene ancora file). Sidebar sinistra con soli i pulsanti icona (explorer file, ricerca, segnalibri, tag/calendario, canvas, altro) senza contenuto.
Voce: *"nostra rappresentazione di assolutamente niente perché la cartella è vuota e"*

### Scena 83 · `frame-0323.png` · 32:12
Graph view ancora vuota; tooltip **"Open quick switcher"** visibile su un'icona della barra laterale sinistra (passaggio del mouse).
Voce: *"come è giusto che sia non ci sono file. Allora, cominciamo subito con il vedere che cos'è Obsidian. E allora per farlo"*

### Scena 84 · `frame-0324.png` · 32:18
Torna il Desktop (uscita temporanea dal fullscreen), stessa disposizione di icone e dock della scena 80.
Voce: *"metterò anche questa a tutto schermo di modo tale che lo vediamo e cominciamo a"*

### Scena 85 · `frame-0325.png` · 32:24
Graph view vuota, stessa inquadratura della scena 83 con un'icona della sidebar evidenziata al passaggio del mouse.
Voce: *"creare la nostra prima nota e la chiamiamo una nota ciao e ci scrivo qualcosa. Ah, come vedete qui ora è comparso questo ciao, però se vado nel mio Aurora cervello vedo che ho che ciao è in un"*

### Scena 86 · `frame-0327.png` · 32:36 — **verifica: `ciao.md` è un file markdown reale sul disco**
Finder macOS, sidebar (Recents, Shared, Favorites: Applications/Desktop/Documents/Downloads, Locations: iCloud Drive/giovannibeggiato/Macintosh HD/AirDrop/Trash, Tags: Red/1/Final_Projects/prova 1/Grigio/Lavoro). Colonna file: **`ciao.md`** · Date Modified **"Today at 10:48"** · Size **"9 bytes"** · Kind **"Markdo…ument"** (Markdown Document, troncato).
Voce: *"formato markdown e se poi lo vado ad aprire dentro ad una IDE vedo letteralmente che c'è scritto qualcosa che è quello che ho scritto dentro."*

### Scena 87 · `frame-0329.png` · 32:48
Desktop, la cartella **"aurora cervello"** appare con la casella del nome in modalità selezione/rinomina (bordo attorno all'etichetta). Barra verticale di icone sul bordo destro dello schermo (stessa app non identificata delle scene precedenti).
Voce: *"Quindi da qui capiamo che cos'è Obsidian. Obsidian"*

### Scena 88 · `frame-0330.png` · 32:54
Stesso Finder della scena 86, ora con la riga **`ciao.md`** evidenziata/selezionata in blu; stessi metadati (10:48, 9 bytes, Markdown Document).
Voce: *"database e molte persone confondono queste due cose. Motivo per cui quando andate su 1000, 2000, 3000 note comincerà a fare fatica […] Obsidian è un layer che permette di collegare varie note markdown. Vedremo dopo perché l'AI preferisce questo layer e come fare questi formati markdown leggibili dall'AI"*

### Scena 89 · `frame-0335.png` · 33:24 — **il contenuto reale della nota "ciao"**
Obsidian, nota **"ciao"** aperta: titolo in grassetto "ciao", corpo: **"qualcosa"**. Barra di stato in basso: **"0 backlinks · 1 word · 9 characters"**. Tooltip **"Open graph view"** visibile sulla sidebar sinistra.
Voce (frase lunga, sintesi): *"[…] possiamo anche vedere che se noi le cancelliamo, ovviamente verranno cancellate in maniera totale sia dal grafico che dalla nostra cartella […] ora è il momento di cominciare a costruire la nostra company Brain. Quindi, per farlo faremo la nostra prima nota quasi completa […] andiamo quindi alla prima"*

### Scena 90 · `frame-0347.png` · 34:36 — **il testo esatto delle prime due note + wikilink, dal doc dei prompt** ⭐
Notion, stessa pagina "Company Brain — Tutti i prompt del tutorial", scrollata sul resto del **Passo 1** (contenuto integrale, riprende da dove si era interrotta la scena 76):
> **1. Installa Obsidian e crea il contenitore vuoto**
> - Vai su `obsidian.md`, scarica la versione per il tuo sistema (Mac o Windows) e installala.
> - Crea sul computer una cartella nuova e vuota: `aurora-cervello`.
> - Apri Obsidian → "Apri cartella come vault" ("Open folder as vault") → seleziona `aurora-cervello`.
>
> **2. Prima nota** — crea (Cmd+N / Ctrl+N), chiamala `self-identita-aurora`, e scrivi nel corpo:
> ```
> Aurora Sistemi S.p.A. e' un'azienda da 340 persone che vende sistemi per rendere efficienti gli edifici. Tre linee di prodotto: Aurora Edge, Aurora Cloud, Aurora Care.
> ```
>
> **3. Seconda nota + wikilink** — crea `persona-elena-ferraro` e scrivi:
> ```
> Elena Ferraro guida la divisione commerciale di [[self-identita-aurora]]. E' la persona che conosce il perche' dietro ogni cliente acquisito.
> ```
> Poi torna su `self-identita-aurora` e aggiungi in fondo:
> ```
> Il commerciale di riferimento e' [[persona-elena-ferraro]].
> ```
>
> **4. Backlink** — su `self-identita-aurora`, attiva il pannello "Backlinks" (tre puntini in alto a destra → "Mostra backlink"). Vedrai comparire da solo `persona-elena-ferraro`.
>
> **5. Grafo** — apri la vista grafo dall'icona nella barra laterale (o Cmd+P / Ctrl+P → "Apri vista grafo"). Due pallini, una linea […] *(prosegue oltre il bordo del frame)*
🔎 Questo blocco spiega e corregge la scena 92 di questo stesso file: il transcript automatico lì rende *"un'azienda di 340 persone che vada a vedere i sistemi"*, ma il testo sorgente esatto — letto qui — è *"un'azienda da 340 persone che vende sistemi per rendere efficienti gli edifici"*.
Voce: *"nota. Allora, la prima nota la chiameremo Selfdity di Aurora e vedrete poi perché ci tengo a chiamarla selfa,"*

### Scena 91 · `frame-0349.png` · 34:48
Obsidian, nuova nota vuota appena creata: titolo in grassetto **"self-identita-aurora"**, corpo vuoto, cursore lampeggiante subito sotto il titolo. Sidebar sinistra con un solo file elencato: "Untitled". Barra di stato in basso: **"0 backlinks · 0 words · 0 characters"**. Webcam di Giovanni in basso a sinistra.
Voce: *"tengo a chiamarla selfa, ok? E il motivo è perché questa parte self sarà uno dei [...] blocchi che noi utilizzeremo, una delle 11 cartelle che useremo"*

### Scena 92 · `frame-0353.png` · 35:12 — doc Notion "Passo 1" per intero ⭐
Notion, pagina **"Company Brain — Tutti i prompt del tutorial"**, sezione **"Passo 1 — Obsidian, la prima nota, i collegamenti (a mano)"**. Testo integrale visibile:
> Nessun prompt all'AI qui: si fa una volta sola, dentro Obsidian.
>
> **1. Installa Obsidian e crea il contenitore vuoto**
> - Vai su `obsidian.md`, scarica la versione per il tuo sistema (Mac o Windows) e installala.
> - Crea sul computer una cartella nuova e vuota: `aurora-cervello`.
> - Apri Obsidian → "Apri cartella come vault" ("Open folder as vault") → seleziona `aurora-cervello`.
>
> **2. Prima nota** — creala (Cmd+N / Ctrl+N), chiamala `self-identita-aurora`, e scrivi nel corpo:
> ```
> Aurora Sistemi S.p.A. e' un'azienda da 340 persone che vende sistemi per rendere efficienti gli edifici. Tre linee di prodotto: Aurora Edge, Aurora Cloud, Aurora Care.
> ```
>
> **3. Seconda nota + wikilink** — crea `persona-elena-ferraro` e scrivi:
> ```
> Elena Ferraro guida la divisione commerciale di [[self-identita-aurora]]. E' la persona che conosce il perche' dietro ogni cliente acquisito.
> ```
> Poi torna su `self-identita-aurora` e aggiungi in fondo:
> ```
> Il commerciale di riferimento e' [[persona-elena-ferraro]].
> ```
>
> **4. Backlink** — su `self-identita-aurora`, attiva il pannello "Backlinks" (tre puntini in alto a destra → "Mostra backlink"). Vedrai comparire da solo `persona-elena-ferraro`.
Sidebar sinistra Notion con voci: Cruscotto Aurora, Company Brain — Tutti i prom..., Reparti, Prodotti, Default view, KPI mensili, Sedi, Competitor.
Voce: *"nota. Allora, la prima nota la chiameremo Selfdity di Aurora e vedrete poi perché ci tengo a chiamarla selfa"* (audio a cavallo con la scena precedente; il contenuto scritto sopra è letto direttamente dal documento, non dal transcript automatico).

### Scena 93 · `frame-0354.png` · 35:18
Obsidian, nota **"self-identita-aurora"** ora compilata: titolo in grassetto, corpo con il testo esatto **"Aurora Sistemi S.p.A. e' un'azienda da 340 persone che vende sistemi per rendere efficienti gli edifici. Tre linee di prodotto: Aurora Edge, Aurora Cloud, Aurora Care."** Barra di stato: **"0 backlinks · 28 words · 187 characters"**.
🔎 Il transcript automatico rende questa frase come *"un'azienda di 340 persone che vada a vedere i sistemi"*, ma il testo scritto a schermo (letto qui) è quello riportato sopra, identico al doc Notion della scena 92.
Voce: *"e quindi metteremo Aurora sistemi Spa è un'azienda di eh 340 persone che vada a vedere i sistemi. Quindi noi ora salviamo e sappiamo che abbiamo fatto la nota."*

### Scena 94 · `frame-0356.png` · 35:30
Stesso doc Notion della scena 92, medesima porzione di "Passo 1" a schermo (titolo, punto 1, punto 2 con nota compilata, punto 3 "Seconda nota + wikilink" con `persona-elena-ferraro` evidenziato in rosa/selezionato).
Voce: *"Bene, andiamo ora a crearci un'altra nota, ok? E quindi cominciamo a inserire i nomi delle persone che lavorano dentro alla nostra azienda."*

### Scena 95 · `frame-0357.png` · 35:36
Obsidian, nuova nota vuota: titolo in grassetto **"persona-elena-ferraro"**, corpo vuoto, cursore dopo il titolo. Sidebar sinistra ora con due file: "self-identita-aurora" e "Untitled" (la nota appena creata, ancora senza rinomina visibile in lista).
Voce: *"Poi, premessa, eh vi darò eh dei prompt che vi permetteranno di fare questa cosa compilata da AI. Ok? Quindi per ora soffermiamoci solo a capire il funzionamento. E allora quello che diciamo è che Elena guida la divisione commerciale di ehm della nostra azienda che si chiama Aurora."*

### Scena 96 · `frame-0358.png` · 35:42
Stesso doc Notion (scroll leggermente diverso, ora si vede dal punto 1 al punto 4), con il testo `persona-elena-ferraro` selezionato/evidenziato al punto 3 e un menu contestuale a comparsa sopra: **"Normal Text"** con icone formattazione (grassetto, corsivo, sottolineato, barrato, link, commento, radice quadrata, altre opzioni), sezione **"Skills"** con voci **"Improve writing"**, **"Proofread"**, **"Explain"**, **"Edit with AI"**.
Voce: *"Vedete che in questo caso, ok? Anzi, meglio fare così in modo tale che possiate apprezzarlo. In questo caso siamo tornati nella situazione di prima, ok? Queste due note sono sconnesse, però noi vorremmo che questa nota ora e questa nota qui diventassero connesse"*

### Scena 97 · `frame-0359.png` · 35:48
Obsidian, nota **"persona-elena-ferraro"** ora compilata: corpo **"Elena Ferraro guida la divisione commerciale di [[self-identita-aurora]]. E' la persona che conosce il perche' dietro ogni cliente acquisito."** — il wikilink `self-identita-aurora` appare in blu/sottolineato (link cliccabile). Sidebar sinistra con due note: "persona-elena-ferraro" (attiva) e "self-identita-aurora". Barra di stato: **"0 backlinks · 19 words · 141 characters"**.
Voce: *"corrette. Perché? Perché questa è la nostra azienda, ok? E questa azienda, abbiamo detto che si chiama Aurora, mentre questa è, diciamo, il responsabile commerciale [...] noi o meglio Lei quello che farà è mettere queste parentesi quadre che permetteranno di riferirsi ad un'altra nota."*

### Scena 98 · `frame-0390.png` · 38:54 — doc Notion, punti 4-6 (frontmatter anticipato) ⭐
Stesso doc Notion, scrollato più in basso: punto 1 (troncato in alto), poi per intero:
> **2. Prima nota** — creala (Cmd+N / Ctrl+N), chiamala `self-identita-aurora`, e scrivi nel corpo: [blocco codice con testo Aurora Sistemi già visto]
> **3. Seconda nota + wikilink** — crea `persona-elena-ferraro` e scrivi: [blocco codice con testo Elena Ferraro già visto]
> Poi torna su `self-identita-aurora` e aggiungi in fondo: `Il commerciale di riferimento e' [[persona-elena-ferraro]].`
> **4. Backlink** — su `self-identita-aurora`, attiva il pannello "Backlinks" (tre puntini in alto a destra → "Mostra backlink"). Vedrai comparire da solo `persona-elena-ferraro`.
> **5. Grafo** — apri la vista grafo dall'icona nella barra laterale (o Cmd+P / Ctrl+P → "Apri vista grafo"). Due pallini, una linea: è già un grafo.
> **6. Frontmatter** — apri `self-identita-aurora` e incolla questo blocco in cima, prima del testo: *(il blocco stesso è oltre il bordo inferiore del frame, non leggibile qui)*
Voce: *"Il l'AI per leggere le varie skill comincia con il leggere questa parte qui che si chiama front e se e solo se il contesto è rilevante allora procede a leggere tutto il resto."*

### Scena 99 · `frame-0391.png` · 39:00 — nota rinominata "self-info-azienda" con backlink attivo
Obsidian, la nota già vista come "self-identita-aurora" è ora rinominata **"self-info-azienda"** (titolo e tab in alto aggiornati). Corpo: stesso testo Aurora Sistemi S.p.A. + riga aggiunta **"Il commerciale di riferimento e' [persona-elena-ferraro]"** (wikilink in blu/sottolineato). Sidebar sinistra: "persona-elena-ferraro" e "self-info-azienda". Barra di stato: **"1 backlink · 34 words · 228 characters"** — il backlink è comparso da solo dopo la creazione del wikilink incrociato.
Voce: *"tutto quanto verrà aggiornato in automatico, ma non solo, abbiamo anche la libertà di muovere dentro e fuori a questa configurazione le note senza che queste vengano [...] cambiate in termini di relazione."*

### Scena 100 · `frame-0409.png` · 40:48 — Desktop macOS, struttura cartelle reale
Desktop con sfondo Lake Tahoe (rocce e acqua turchese). Icone cartelle visibili in alto: **"Giovanni Beggiato"**, **"aurora cervello"**, **"Company Knowledge Base"**, **"Second Brain"**, **"Knowledge Base"**; in alto a destra: **"Agentic Personal"**, **"Archive"**, file **"3. Business part - pandadoc.mov"**, cartella **"OBS Recordings"**, **"LinkedIn"**, **"headshot"**, **"Agentic Personal copy"**, **"Company Brain"**, file **"Screenshot 2026-0...t 10.31.08"**. Dock in basso con tooltip **"Claude"** visibile su un'icona; altre icone dock riconoscibili: Safari, Chrome, un'app scura con logo circolare rosso/nero, un'icona nera con "X" stilizzata, un'icona arancione a stella/esplosione, un cubo 3D grigio, un grafico a barre viola, WhatsApp verde, un diamante viola, Notion, un blocco note, cestino.
Voce: *"apriamoci il nostro ehm cloud eh code. Utilizziamo anche cowork, così per semplicità, insomma, per di interfaccia possiamo fare quello che vogliamo, no? Quindi entriamo nel nostro cowork work in a project, apriremo la nostra Aurora cervello"*

### Scena 101 · `frame-0410.png` · 40:54 — app desktop Claude Code, schermata iniziale
App desktop **Claude Code**, tab **"Code"** attivo in alto, titolo **"Welcome back, Gio"**. Sezione **"Pull requests"**: riga **"Ready for review — Add /cheat-sheet skill (autonomous logo-vs-icon cheat sheets) #26"**, repo **"Giobebbe/social-media-mana…"**, "5d". Sidebar sinistra: New session, Routines, Customize, More; "Recents": Ultra Code/Plan/Agent T…, PDF folder summaries, n8n cheat sheet with br…, Weight loss research fo…, 2. Mia Repo Evolution, Uninstall n8n MCP, Email chatbot with PDF…, General coding session (×2), Email chatbot with PDF…, Tetris game implementat… (×3, elenco troncato in basso). Barra inferiore: tab "Local"/"CODE", campo **"…escribe a task or ask a question"**, toggle "…cept edits", indicatore modello **"Opus 4.6 · Fast"** e riquadro **"Medium"** (testo minuto, difficile da leggere con certezza oltre queste parole).
Voce: *(prosegue dalla scena precedente, nessuna nuova battuta isolata in questo intervallo di frame)*

### Scena 102 · `frame-0411.png` · 41:00 — dialogo permessi
Popup di conferma sopra l'interfaccia Cowork (sfondo sfumato): **"Allow Claude to change files in "aurora cervello"? This includes all files and subfolders. Claude will be able to read, edit, and permanently delete—and may share file contents with third-party tools it connects to. Be careful about exposing sensitive information."** Tre pulsanti: **"Cancel"**, **"Always allow"**, **"Allow"** (evidenziato in bianco, cursore sopra). Sullo sfondo si intravede la schermata Cowork "Let's knock something off your list" con l'elenco task recenti.
Voce: *"comincia a fare i vari comandi, comincia ad entrare dentro la nostra azienda, vedete? comincia a leggere i vari file markdown"*

### Scena 103 · `frame-0412.png` · 41:06 — schermata principale Cowork
Interfaccia **Cowork**: banner **"Claude Fable 5 works best with the latest desktop app. Update now."**, titolo **"Let's knock something off your list"**, badge **"2× more usage until July 5"** + link "Learn how to use Cowork safely". Campo di input **"How can I help you today?"** con selettore cartella **"aurora cervello"** e modalità **"Ask"**, modello **"Opus 4.6 · High"** in basso a destra. Sezione **"Active"** (link "Clear active") con elenco task: **"Commercial manager inquiry"** (17 hours ago), **"Create YouTube video on Claude Routines"** (56 days ago), **"Italian greeting and conversation start"** (60 days ago), **"Revise coaching progra[m]…ment Italian"** (parzialmente coperto dalla webcam). Sidebar Cowork: New task, Projects, Scheduled, Live artifacts, Dispatch (Beta), Customize; Pinned: Dashboard Live Drive; Recents: Commercial manager in…, Aurora Sistemi raw mat…, Ultra features access, Claude.md file access, Dashboard Live artifact…, PDF 20 folder summary, Desktop folder access.
Voce: *"apriremo la nostra Aurora cervello, benissimo, e gli chiederemo: "Hei, sapresti dirmi ehm chi è il responsabile commerciale dell'azienda?""*

### Scena 104 · `frame-0417.png` · 41:36 — risposta di Claude con fonti citate ⭐
Task Cowork aperto. Bolla utente: **"Ehi, sapresti dirmi chi è il responsabile commerciale dell'azienda?"** Risposta Claude, preceduta da **"Read 2 files, ran a command >"**:
> Il responsabile commerciale è **Elena Ferraro**.
> Guida la divisione commerciale di Aurora Sistemi S.p.A. (l'azienda da 340 persone con le tre linee Aurora Edge, Aurora Cloud e Aurora Care). È indicata come il commerciale di riferimento e, dalle note, è "la persona che conosce il perché dietro ogni cliente acquisito".
> Fonti: file `self-info-azienda.md` e `persona-elena-ferraro.md` nella cartella selezionata.
Icone azione sotto la risposta (copia, esegui, pollice su, commento). Pannello destro: indicatore avanzamento task (spunte), riquadro **"aurora cervello"** con elenco file: "Instructions · CLAUDE.md", "persona-elena-ferraro.md", "self-info-azienda.md"; sezione **"Context"** con placeholder icone e testo "Track tools and referenced files used in this task."
Voce: *"e dopo arriva alle informazioni di Elena, quindi guida la divisione eh sì di Elena. Guida la divisione commerciale di Aurora. L'azienda A è indicata come il commerciale di riferimento è la persona che conosce. Perfetto."*

### Scena 105 · `frame-0419.png` · 41:48 — follow-up e note aggiuntive (pizza, spazzolini)
Bolla utente: **"Hai anche altre informazioni di Elena a riguardo?"** Claude: **"Working on it..."** Pannello destro mostra un'anteprima della nota `persona-elena-ferraro` con parte di testo evidenziata in blu: **"Elena Ferraro guida la divisione commerciale di [[self-info-azienda]]."** poi elenco puntato: **"E' la persona che conosce il perche' dietro ogni cliente acquisito."** / **"È la persona che si occupa di vendere, non lo so, spazzolini"** / **"Le piace la pizza"**.
Voce: *"Ora le chiedo, hai anche qualche altra informazione di Elen a riguardo? Ora quello che farà sarà ovviamente andare dentro le nostre note e andare a capire che cosa c'è all'interno."*

### Scena 106 · `frame-0421.png` · 42:00 — risposta completa di Claude, split-screen con desktop ⭐
Schermo diviso: a sinistra il desktop macOS (sfondo Lake Tahoe, cartelle e dock parzialmente visibili), a destra il pannello Cowork con la risposta completa a **"Hai anche altre informazioni di Elena a rig[uardo]"**, preceduta da **"Thought process >"**:
> Le uniche informazioni che ho su Elena sono quelle nel file `persona-elena-ferraro.md`, e sono poche:
> - Guida la divisione commerciale di Aurora Sistemi S.p.A.
> - È la persona che conosce il "perché" dietro ogni cliente acquisito.
> - Si occupa di vendere (la nota dice scherzosamente "non lo so, spazzolini").
> - Le piace la pizza.
>
> Non ho altri dettagli (cognome a parte, contatti, ruolo preciso, ecc.). Se vuoi, posso cercare altre informazioni nelle tue email, nel calendario o negli altri strumenti collegati. Dimmi solo dove guardare.
Banner **"Claude Fable 5 works best with the latest desktop app. Update now."** Sidebar Cowork con Recents estesi: Commercial manager in… (evidenziato, attivo), Commercial manager in…, Aurora Sistemi raw mat…, Ultra features access, Claude.md file access, Dashboard Live artifact…, PDF 20 folder summary, Desktop folder access, Giovanni Beggiato folde…, Environment variables…, Demo automation and…, Relaunch t…
Voce: *"Vedete quanto potente sia questo tipo di utilizzo, perché qui cominciamo ad avere tutto collegato in maniera appropriata, no? Quindi qui vediamo. Le piace la pizza."*

### Scena 107 · `frame-0422.png` · 42:06
Obsidian, nota `persona-elena-ferraro` aggiornata: corpo con wikilink **"self-info-azienda"** poi elenco puntato: "E' la persona che conosce il perche' dietro ogni cliente acquisito." e, evidenziata in blu/selezionata, la riga **"E la persona che si occupa di vendere, non lo so, spazzolini"** seguita da **"Le piace la pizza"**. Barra di stato: **"1 backlink · 18 words · 83 characters"** (cifre piccole, lette con attenzione).
Voce: *"Bene, ora torniamo nella nostra nota e ora ovviamente cancelliamo perché vogliamo tenere il tutto nella maniera più corretta possibile."*

### Scena 108 · `frame-0432.png` · 43:06 — dimostrazione del problema di scala (frase ripetuta all'infinito) ⭐
Stessa nota `persona-elena-ferraro`, ora invasa da un'unica frase ripetuta decine di volte senza interruzione, a riempire l'intera pagina visibile: **"E' la persona che conosce il perche' dietro ogni cliente acquisito."** incollata in sequenza continua (nessuna interruzione di riga leggibile tra una ripetizione e l'altra). Barra verticale blu di selezione lungo il margine sinistro del testo. Barra di stato: **"1 backlink · 438 words · 2,688 characters"**.
Voce: *"al momento immaginiamo di avere ora 1000 note di questo tipo. Lei dovrebbe fare uno sforzo immane e immaginiamo ovviamente di avere ora magari questa frase e la ripetiamo ehm adesso all'infinito. Lei ogni volta che entra nella nota dovrebbe andare a leggersi tutto il contesto e ovviamente questo consumerebbe un sacco di token e avrebbe problemi di allucinazione."*

### Scena 109 · `frame-0434.png` · 43:18
Nota `persona-elena-ferraro` ripulita dalla ripetizione, tornata al testo breve: wikilink a "self-info-azienda" + riga singola "E' la persona che conosce il perche' dietro ogni cliente acquisito." Barra di stato: **"1 backlink · 30 words · 141 characters"**.
Voce: *"porterebbe lei a sbagliare. Quindi ora introduciamo il secondo, diciamo, blocco importante che è come facciamo a rendere le note visibili all'AI nella maniera più corretta possibile."*

### Scena 110 · `frame-0437.png` · 43:36 — editor di codice, esempio di frontmatter in un file SKILL.md ⭐
Cambio di contesto: editor tipo VS Code, progetto **"Social Media Manager"**. Sidebar Explorer: cartella `claude` → `skills` con sottocartelle **research, reverse-prompting, schedule-meeting, scroll-journey, shorts, sign, skill-creator** (espansa, con sottocartella `references` e file **`SKILL.md`** selezionato), poi skill-extraction-skool, skool-community-replies, skool-video-upload, step-back-prompting, video-extraction, write-skool-module, youtube-comments, youtube-description, `.gitkeep`; più sotto `workflows`, `scheduled_tasks.lock`, `settings.json`, `settings.local.json`, `pytest_cache`, `imp`, `venv`, `automations`. Contenuto del file `SKILL.md` aperto (frontmatter in cima, tra tre trattini):
> name: skill-creator
> description: Create new skills, improve existing ones, or capture a working session as a reusable skill. Use when the user wants to create/improve/fix a skill, add a workflow or automation, says make this a skill, or /skill-creator.
> allowed-tools: Bash, Read, Write, Edit, Glob, Grep, AskUserQuestion
> ---
> # Skill Creator
> ## Goal
> Turn any repeated multi-step workflow into a reusable slash command with proper error handling.
> Create new skills and iteratively improve existing ones for this project.
> Read `references/skill-writing-guide.md` for the full conventions reference — it contains the Golden Rules, skill types, script boilerplate, and writing style guide.
> ## When to Create a Skill
> A process deserves its own skill when:
> - It's repeated 3+ times across conversations
> - It involves multiple steps that benefit from structured orchestration
> - It needs specific tools (browser automation, file editing, API calls)
> - The user explicitly asks to automate something
> ## Step 1: Capture Intent
> Before writing anything, interview the user. [...] extract the steps, tools used, and corrections made first — then confirm.
> Questions to clarify: 1. **What problem does this solve?** — the WHY, not just the WHAT / 2. **What type of skill is it?** [...] / 3. **When should it trigger?** [...] / 4. **What tools does it need?** [...] / 5. **Does it overlap with existing skills?** [...]
> ## Step 2: Choose a Pattern
> Read 1-2 existing skills that match the type you're building. [...] tabella "If building... | Read these for reference" con righe Content generation → linkedin-post, youtube-description; Pipeline → shorts; Browser automation (riga finale troncata in basso).
Barra di stato editor: "Screen Reader Optimized", "Ln 1, Col 1", "Spaces: 4", "UTF-8", "LF", "Markdown", "Antigravity - Settings".
Voce: *"Il l'AI per leggere le varie skill comincia con il leggere questa parte qui che si chiama front e se e solo se il contesto è rilevante allora procede a leggere tutto il resto. E quindi questo cosa vuol dire? Che per far funzionare bene Obsidian dovremmo avere un funzionamento del genere, quindi un front."*

### Scena 111 · `frame-0443.png` · 44:12 — doc Notion, blocco frontmatter completo + inizio Passo 2 ⭐
Torna il doc Notion "Passo 1", scrollato oltre il punto 3 (visibile solo l'ultima riga "Il commerciale di riferimento e' [[persona-elena-ferraro]]." troncata in alto). Testo integrale:
> **4. Backlink** — su `self-identita-aurora`, attiva il pannello "Backlinks" (tre puntini in alto a destra → "Mostra backlink"). Vedrai comparire da solo `persona-elena-ferraro`.
> **5. Grafo** — apri la vista grafo dall'icona nella barra laterale (o Cmd+P / Ctrl+P → "Apri vista grafo"). Due pallini, una linea: è già un grafo.
> **6. Frontmatter** — apri `self-identita-aurora` e incolla questo blocco in cima, prima del testo:
> ```
> ---
> title: Identita' di Aurora Sistemi
> summary: Aurora Sistemi e' un'azienda da 340 persone che vende sistemi di efficie[nza...] (riga troncata oltre il bordo destro del frame, non leggibile per intero)
> tags: [self, type/identita]
> status: active
> created: 2026-06-09
> updated: 2026-06-09
> related: [[persona-elena-ferraro]]
> ---
> ```
> **Passo 2 — Le 11 cartelle e le prime note con l'AI**
> **Prompt 1 — Crea le 11 cartelle**
> Dà all'AI lo scheletro del cervello: 11 cartelle vuote, niente altro.
> ```
> Crea nel mio vault, alla radice, queste 11 cartelle vuote, una per ciascun lavoro del cervello:
> self, areas, projects, sources, concepts, docs, entities, data, code, outputs, ... (elenco troncato in basso dal bordo del frame, cartelle restanti non leggibili qui)
> ```
Menu contestuale a comparsa **"Code >"** con icone di formattazione, sopra il blocco frontmatter selezionato/evidenziato in blu.
Voce: *"Guarda caso, il front è esattamente quello di cui andremo a parlare ora. E prima che lo incolli, voglio farvi vedere che cosa succede quando premiamo questi tre tratt."*

### Scena 112 · `frame-0444.png` · 44:18 — pannello Properties di Obsidian aperto
Obsidian, nota **"self-info-azienda"**: sotto il titolo compare la sezione **"Properties"** con un campo vuoto (placeholder "Empty") e un menu a tendina di scelta tipo proprietà con tre opzioni: **"aliases"**, **"cssclasses"**, **"tags"** (quest'ultima in evidenza/hover). Corpo della nota sottostante invariato (testo Aurora Sistemi + link a persona-elena-ferraro). Barra di stato: **"1 backlink · 34 words · 230 characters"**.
Voce: *"Allora, vedete che cominciamo ad avere delle proprietà. Quindi, in questo caso, io potrei scrivere title e potrei mettermi eh identità di Aurora."*

### Scena 113 · `frame-0445.png` · 44:24
Stesso doc Notion della scena 111, medesima porzione di testo a schermo (punti 4-6 del Passo 1 + inizio Passo 2/Prompt 1), nessuna variazione visibile rispetto al frame precedente.
Voce: *"Poi ovviamente questo può essere eh cambiato in Ok, questa è una textbox, potrei aggiungere del dei tags, potrei cambiare delle m insomma delle proprietà. Potrei fare un sacco di cose."*

### Scena 114 · `frame-0446.png` · 44:30
Obsidian, nota **"self-info-azienda"**: nel pannello Properties è stata aggiunta la prima proprietà — riga **"title"** con valore digitato **"Identità di aurora"** — e sotto il link **"+ Add property"** per aggiungerne altre. Corpo della nota invariato. Barra di stato: **"1 backlink · 1 property · 34 words · 230 characters"**.
Voce: *"Ok? Quindi, detto che questo va a crearmi tutto questo mare di proprietà, ora quello che voglio fare è incollare quello che vi ho scritto."*

### Scena 115 · `frame-0481.png` · 48:00 — solo webcam, nessuna UI a schermo
Salto temporale: inquadratura a piena pagina di Giovanni in webcam (nessuna condivisione schermo visibile in questo frame). Sfondo: mensola con pianta pendente, lampada accesa a destra, parete chiara.
Voce: *"collegamenti, ma questi collegamenti sono super importanti per l'AI perché [...] immaginatevi come se l'EI potesse entrare in un file e poi diramarsi a seconda di qual è la il collegamento migliore."*

### Scena 116 · `frame-0482.png` · 48:06 — solo webcam, mani aperte a "ventaglio"
Giovanni in webcam a figura intera, stesso sfondo (mensola con libri colorati e pianta pendente a sinistra, lampada accesa a destra). Nessuna condivisione schermo. Gesto enfatico: entrambe le mani aperte davanti al petto, dita allargate a ventaglio, palmi rivolti verso l'interno come a "incorniciare" un concetto.
Voce: *"migliore. Ok? Quindi perché le company Brain funzionano? Ok, perché esistono"* — introduce la domanda retorica sul perché le company Brain funzionino.

### Scena 117 · `frame-0483.png` · 48:12 — solo webcam, sguardo basso
Stessa inquadratura webcam, nessuna UI. Giovanni guarda verso il basso/lato, espressione pensosa, mani non visibili (fuori campo sotto il microfono).
Voce: *"questi collegamenti. Parleremo dopo di come funzionano e qual è la logica"* — anticipa che spiegherà più avanti la logica dei collegamenti.

### Scena 118 · `frame-0484.png` · 48:18 — solo webcam, sguardo in camera
Stessa inquadratura webcam, nessuna UI. Giovanni fissa dritto in camera, espressione neutra/concentrata, bocca socchiusa a metà parola.
Voce: *"sottostante, ma questo è il motivo per"* — prosegue la spiegazione del motivo sottostante ai collegamenti.

### Scena 119 · `frame-0485.png` · 48:24 — solo webcam, leggero sorriso
Stessa inquadratura webcam, nessuna UI. Giovanni con accenno di sorriso, sguardo in camera leggermente di lato.
Voce: *"cui una normale nota di testo, ok? eh è"* — contrappone la nota di testo normale a Obsidian.

### Scena 120 · `frame-0486.png` · 48:30 — solo webcam, mani alzate in gesto esplicativo
Stessa inquadratura webcam, nessuna UI. Entrambe le mani sollevate all'altezza del petto, palmi verso l'alto, gesto da "spiegazione in corso".
Voce: *"perché Obsidian ha la possibilità di"* — inizia a spiegare perché Obsidian è superiore per l'AI.

### Scena 121 · `frame-0487.png` · 48:36 — solo webcam, gesto di "pizzico"
Stessa inquadratura webcam, nessuna UI. Mano destra sollevata accanto al volto con pollice e indice quasi uniti (gesto da "piccola cosa/precisione"), sguardo fisso in camera.
Voce: *"l'EI con questo front e proprietà può lavorare e può anche navigare"* — spiega che l'AI può lavorare e navigare grazie a frontmatter e proprietà.

### Scena 122 · `frame-0488.png` · 48:42 — Excalidraw, schema "Company Brain: 11 cartelle" ⭐
Excalidraw (excalidraw.com) a schermo intero, webcam di Giovanni in riquadro basso-sinistra (mano alzata a mezz'aria). Titolo su nastro: **"COMPANY BRAIN: 11 CARTELLE"**, sottotitolo **"Una sola decisione: quanto e' azionabile?"**. Griglia di 11 card colorate con icona + nome + descrizione, su tre righe:
- Riga 1 (viola/verde/arancio/giallo): **self** "chi e azienda" · **areas** "responsabilita' continue" · **projects** "lavoro a tempo, con traguardo" · **sources** "la inbox grezza"
- Riga 2 (giallo/blu/verde/blu): **concepts** "idee, una per nota" · **docs** "procedure intere" · **entities** "schede dei nomi propri" · **data** "i numeri"
- Riga 3 (azzurro/arancio/arancio): **code** "script e automazioni" · **outputs** "deliverable finiti" · **workspace** "bozze e diario"
Pannello strumenti Excalidraw a sinistra (colori stroke/background, opacity, layers) visibile ma inattivo.
Voce: *"momento in cui ora vogliamo cominciare a costruire la nostra company Brain."* — introduce lo schema delle 11 cartelle appena mostrato.

### Scena 123 · `frame-0570.png` · 56:54 — editor stile VS Code, menu File aperto su "New Window"
Salto temporale (da 48:42 a 56:54). Editor scuro (sidebar "Explorer" con cartella **"aurora cervello"** appena visibile in alto) con menu contestuale File aperto: voce **"New Window"** (⇧⌘N) evidenziata in blu, sotto in elenco "New Window with Profile", "Open...", "Open Folder...", "Open Workspace from File...", "Open Recent", "Add Folder to Workspace...", "Save Workspace As...", "Duplicate Workspace", "Save", "Save As...", "Share", "Auto Save", "Revert File", "Close Editor", "Close Folder", "Close Window". Pannello centrale sullo sfondo mostra il logo **"Claude Code"** con il messaggio placeholder **"Type /model to pick the right tool for the job."**. Webcam di Giovanni in basso a sinistra.
Voce: *"di modo tale che vi sia più chiaro, fatemi andare nella mia company Brain,"* — annuncia che aprirà la sua company Brain reale come esempio pratico.

### Scena 124 · `frame-0571.png` · 57:00 — finestra di sistema "Open" con le 11 cartelle reali
Finestra di dialogo Apri file di macOS, cartella corrente **"giovannibeggiato"** (percorso in breadcrumb in alto), colonna sinistra con Preferiti (Recents, Shared, Applications, Desktop, Documents, Downloads) e Posizioni (iCloud Drive, "giovannibegg...", Macintosh...) e Tag (Red). Elenco cartelle nella working directory, tutte con icona cartella blu: **areas, code, concepts, data, docs, entities, outputs, projects, self, sources, workspace** — esattamente le 11 cartelle dello schema Excalidraw appena mostrato. Pulsanti "New Folder", "Cancel", "Open" (blu) in basso. Webcam invariata in basso a sinistra.
Voce: *"perché ora ho fatto la migrazione di tutto il mio social media manager e dovrebbe essere Eccoci qui."* — spiega che sta per mostrare la sua company Brain reale, appena migrata.

### Scena 125 · `frame-0575.png` · 57:24 — Explorer completo "Company Brain" + nota di sessione aperta
Editor scuro, sidebar Explorer con radice **"Company Brain"** e sottocartelle: **.obsidian, .tmp, areas, code, concepts, data, docs, engine, entities, labs, outputs, projects, scripts, self, sources, studio, workspace** (workspace espanso). Nel pannello principale è aperto il file **"workspace/journal/sessions/2026-06-10-0221.md"** (breadcrumb in alto), con frontmatter e corpo (testo integrale leggibile):
> ```
> ---
> title: "Sessione 2026-06-10 — Eval audit autonomo vs skill /audit + fix regressioni Flatten"
> tags: [type/session]
> date: 2026-06-10
> related:
>   - "[[tooling-skill-e-audit]]"
>   - "[[modulo-youtube-desc]]"
>   - "[[modulo-linkedin]]"
>   - "[[metriche-mrr-churn]]"
> ---
> ```
> **# Sessione 2026-06-10 — Eval audit autonomo vs skill /audit + fix regressioni Flatten**
> **## Fatto**
> - Eval A/B audit autonomo (4 agenti progettati al volo) vs skill /audit, entrambi report-only, contraddizioni verificate a comando. Autonomo: 3 HIGH + 12 MEDIUM reali. Skill: 0 HIGH, 1 WARNING vero (metrica stale su data/index), 5 PASS smentiti, verdetto "ready for production" sbagliato. Cause gate ciechi sul flatten + agenti Explore/Haiku, corpo stile (REFERENCES_PATH), 13 SKILL.md e 19 script con path pre-flatten, deny segreti su path inesistenti, 2 hook rotti (validate_pipeline_output no-op, post_audit al load), agents/ senza frontmatter, riferimenti morti (youtube-script, shorts, data/ vs engine/data/). Demo /youtube-description post-fix con 8 references caricate. Report eval in .tmp/eval-audit, dashboard visiva, audit_log #37 aggiornato.
> **## Decisioni**
> - La skill /audit come orchestratore non serve: il modello da solo trova di più. Da salvare: gate meccanici, registro FP, sweep istituzionali (stale-metric), verifica adversariale. Ridisegno skill = decisione di Gio. FP nuovi registrati; wikilink legacy risolvono su sources/legacy; graph.json tracciato renta dismissed
> **## Da fare**
> - Decidere ridisegno skill /audit (sottotile: gate+FP+sweep). Valutare: allow Bash(*) in settings, sheets_client path credenziali (guardrail #7), 54 note senza fonte, PII git-tracked in sign/
> **## Voci collegate**
> - [[tooling-skill-e-audit]]
> - [[modulo-youtube-desc]]
> - [[modulo-linkedin]]
> - [[metriche-mrr-churn]]
Barra di stato in basso: "Ln 1, Col 1 · Spaces: 2 · UTF-8 · LF · Markdown". Webcam Giovanni in basso a sinistra.
Voce: *"qui ho fatto qu c sessioni e dopo invece ho la parte di daily in cui tutto questo"* — mostra il proprio journal di sessioni reale (nota: contenuto della nota riguarda ironicamente un audit sulla skill /audit stessa, tema Digital Empire/Claude Code, non Second Brain generico).

### Scena 126 · `frame-0578.png` · 57:42 — file giornaliero "2026-06-10.md", riepilogo giornata
Stesso editor, sidebar invariata. Aperto il file **"workspace/journal/daily/2026-06-10.md"** (breadcrumb: workspace › journal › daily › 2026-06-10.md › ## Riepilogo giornata). Corpo nota (testo leggibile, numerazione riga a margine da 7/18 poi 40-52 — porzione centrale della nota, non l'inizio):
> **# 2026-06-1➕** (cifra finale del giorno non leggibile con certezza nello screenshot, coerente col nome file "2026-06-10.md")
> **## Fatto**
> - Skill /hq-giornata estesa ai tre momenti: buongiorno, fine sessione (per conversazione), fine giornata (riconciliazione finale); intervista sostituita dalla sintesi automatica del contesto (PR #9, #10)
> - Risolto il falso ImportError google.genai: era il python di sistema senza venv, non un bug; regola venv nel CLAUDE.md root, guardrail engine #65, gate engine_venv (PR #11); Gemini e2e verificato OK
> - Audit #36: drift Shorts in 4 doc, leak PII in pdf_to_template, parsing video ID fragile — fixati (PR #12); gate verdi (61 test, 34 moduli, lint 0, doc_refs 0)
> - Mergiata PR #8, tree tornato a main, branch merged cancellati da GitHub (0 PR aperte); ripulita mappa company-brain corretta, brain-sync
>
> **## Riepilogo giornata** (paragrafo sottostante evidenziato/selezionato in blu dal cursore):
> "Sei chiusure di sessione registrate dall'hook, quattro narrative scritte (00:18 audit/numeri, 01:23 Shorts, 01:24 demo Gentes, 01:43 fine giornata): le chiusure extra sono compact e riaperture delle stesse conversazioni, tutto il lavoro e' riconciliato. Quattro PR mergiate (#8-#12 tranne una, la #8 che era di ieri sera tardi), repo pulito su main, vault e Qdrant allineati. Da domani valgono i tre momenti: buongiorno, fine sessione, fine giornata."
> "Coda di giornata (sessione 01:58): chiuso anche l'ultimo sospeso, il consolidamento del ~/.claude globale — 3 skill legacy ritirate, settings.json ripulito, nuovo-cliente non si ricrea. Resta un solo sospeso per domani: il gate check_journal_format.py citato in CLAUDE.md ma assente da scripts/."
> "Seconda coda (sessione 02:21, chiusura vera): eval A/B sull'audit — il modello in autonomia batte la skill /audit (3 HIGH reali vs 0, con 5 PASS falsi della skill); unico punto alla skill lo stale-metric sweep. Fix round mergiato (PR #13, 51 file): regressioni del flatten su generator, SKILL.md, script, deny segreti, hook. Il sospeso check_journal_format era una citazione ambigua, non un gate mancante: corretta (il gate vive in .claude/skills/audit/scripts/). La sessione parallela 02:22 ha migrato related: a lista YAML su 156 note (guardrail #8) e il suo commit recupera il sync di questa chiusura. Per domani ridisegno skill /audit e valutazione sicurezza."
Barra di stato: "Giovanni Beggiato · 10 hours ago · Screen Reader Optimized · Ln 46, Col 1 (1417 selected) · Spaces: 4 · UTF-8 · LF · Markdown".
Voce: *"Ok, questo perché è importante? Perché dobbiamo averne due, perché il daily è un suo. E quindi Lei andrà a vedere con i vari titoletti che cosa ho fatto qua dentro,"* — spiega la differenza tra journal di sessione e daily riepilogativo.

### Scena 127 · `frame-0580.png` · 57:54 — nuova finestra Antigravity IDE, sidebar con daily/sessions
Nuova finestra dell'editor (splash **"Antigravity IDE"** / sottotitolo **"Code with Agent"** al centro, pannello vuoto), sidebar Explorer a sinistra con radice "Company Brain" e le stesse sottocartelle di scena 125 (.showcase, .claude, .obsidian, .tmp, areas, code, concepts, data, docs, engine, entities, labs, outputs, projects, scripts, self, sources, studio, workspace), workspace espanso su **journal** → **daily** (evidenziata/selezionata in blu) e **sessions** (anch'essa con evidenziazione), più "change-log.md", "_index.md". Pannello destro "Agent" vuoto in alto. Webcam Giovanni in basso a sinistra.
Voce: *"mentre poi nello specifico ogni sessione andrà a dettagliare quello che è stato fatto e e come. E vedete che qui è tutto collegato da AI. Ok? Super super"* — sottolinea che daily e sessioni sono entrambi collegati e gestiti dall'AI.

### Scena 128 · `frame-0590.png` · 58:54 — chat "Continue coding session" con l'assistente, cartella sessions espansa
Editor con sidebar che mostra la cartella **sessions** espansa: elenco file datati **2026-05-20.md, 2026-05-21.md, 2026-05-22.md, 2026-05-25.md, 2026-05-27.md, 2026-05-29.md, 2026-05-30.md, 2026-06-01.md, 2026-06-02.md, 2026-06-03.md, 2026-06-04.md, 2026-06-05.md, 2026-06-09.md, 2026-06-10.md** (evidenziato, con tooltip a comparsa **"Desktop/Company Brain/workspace/journal/sessions"**), sotto un'altra sottocartella "sessions" con **2026-06-10-0018.md, 2026-06-10-0123.md, 2026-06-10-0124.md, 2026-06-10-0143.md, 2026-06-10-0158.md, 2026-06-10-0221.md, change-log.md**. Pannello principale: tab **"Continue coding session"**, conversazione con l'agente (testo integrale):
> "Hey Claude, ti ho già salutato stamattina. Siamo già in sessione"
> *Thought for 1s*
> "è una domanda"
> "Perfetto, niente doppio briefing allora. Dimmi pure su cosa lavoriamo."
> *Thought for 2s*
> "Ah, capito: vuoi sapere se abbiamo già aperto la giornata. Controllo il daily di oggi."
> **Read** `2026-06-10.md`
> *Thought for 3s*
> "Sì, confermo: la giornata è già aperta. Il daily di oggi (2026-06-10.md) esiste, ha il focus impostato e registra già sessioni chiuse stamattina alle 09:23 e alle 10:06. Quindi niente nuovo briefing: questa è semplicemente un'altra conversazione dentro la stessa giornata. Quando finisci qui basta un "fine sessione", e il daily si aggiorna da solo."
> [chip file allegato: **2026-06-10.md**] "Sto facendo ora una demo. Per favore non chiudere ancora la giornata, che ho del lavoro da fare."
> *Thought for 1s*
> "Certo, niente chiusura. Ecco la sintesi: "Fine sessione" chiude una singola conversazione: genero una sintesi automatica di quello che abbiamo fatto dal contesto, scrivo una nota di sessione nel journal, aggiorno il daily di oggi e lancio il sync del cervello (lint, indici, commit)."
> "Finaliz[z]ing..." (messaggio troncato in corso di generazione)
Barra messaggio in basso: campo "Queue another message...", chip file "2026-06-10.md", toggle rosso "Bypass permissions".
Voce: *"apro e chiudo, funziona super bene se avete un buon rag dietro, perché qui può andare proprio nei dettagli piccoli piccoli piccoli e può trovarvi qualsiasi cosa. Certo, niente chiusure. Ecco la"* ➕ — Giovanni descrive a voce lo stesso flusso che appare a schermo nella chat (apertura/chiusura sessione via RAG); le ultime parole coincidono testualmente con la risposta dell'agente visibile in chat.

### Scena 129 · `frame-0596.png` · 59:30 — macOS Mission Control, nessuna finestra selezionata
Salto a vista Mission Control di macOS: barra superiore con miniature di spazi/finestre — **"Desktop 1"**, **"Google Chrome"**, **"aurora cervello — Clau..."** (nome finestra troncato), una finestra scura tipo terminale (senza titolo leggibile), e in alto a destra un lembo di finestra **"Notion"**. Sfondo desktop: wallpaper del Lago Tahoe (acqua turchese, massi granitici, montagne innevate, pino a destra). Al centro tooltip **"No Available Windows"** vicino al cursore. Dock in basso con icone: Finder/Desktop, Chrome, un'app con pallino rosso (icona scura), un'icona a X, Slack, un'icona colorata a raggiera, Antigravity, un cubo 3D viola, un'icona a grafico, WhatsApp, un'icona viola, Notion, Note, un'altra icona, un'icona con badge rosso, Cestino. Webcam Giovanni in basso a sinistra, sguardo verso il basso durante la transizione tra finestre.
Voce: *"il funzionamento della company Brain. Ora torniamo a noi e prima di di mandare"* — chiude la parentesi dimostrativa e annuncia il ritorno all'esercizio pratico con lo spettatore.

### Scena 130 · `frame-0597.png` · 59:36 — Excalidraw, schema "Tassonomia vs Ontologia" ⭐
Excalidraw a schermo intero (stessa interfaccia di scena 122), webcam Giovanni in basso a sinistra. Due colonne separate da linea tratteggiata verticale:
- Sinistra, titolo **"TASSONOMIA"**: box viola **"Progetti"** collegato con linee a due box verdi **"Progetti Interni"** e **"Progetti Clienti"**; sotto due fumetti, arancio **"Che tipo di cosa è?"** e azzurro **"ti dice dove archiviarla"**.
- Destra, titolo **"ONTOLOGIA"**: due cerchi gialli **"Aurora Sistemi"** (etichetta sotto "azienda") e **"Marco"** (etichetta sotto "persona"), collegati da una freccia con testo **"lavora nel commerciale"**; sotto due fumetti, viola **"Cosa sono e come si collegano?"** e verde **"leggibile da una macchina"**.
Pannello strumenti Excalidraw a sinistra invariato.
Voce: *"brevemente che cosa succede e perché"* — introduce lo schema che contrappone tassonomia (gerarchia di cartelle) e ontologia (entità e relazioni), il cuore concettuale di come l'AI naviga il vault.

### Scena 131 · `frame-0599.png` · 59:48 — macOS Mission Control, ancora "No Available Windows"
Stessa vista Mission Control della scena 129 (stesso wallpaper Lago Tahoe con massi granitici, stessa fila di miniature in alto — "Desktop 1", "Google Chrome", una miniatura scura senza titolo leggibile, "aurora cervello — Clau...", "Obsidian" —, stessa dock in basso), tooltip **"No Available Windows"** ancora al centro schermo vicino al cursore. Frame catturato ~18 secondi dopo la scena 129: nessun cambiamento sostanziale di contenuto, solo transizione che si protrae mentre Giovanni parla. Webcam invariata in basso a sinistra.
Voce: *"questa, per esempio. Quindi, fatemi brevemente andare qui."* — annuncia che sta per aprire una schermata di esempio (la company Brain reale).

### Scena 132 · `frame-0600.png` · 59:54 — finestra browser non massimizzata, Excalidraw + sidebar Explorer
Fotogramma di transizione: la finestra Chrome su excalidraw.com non è a schermo intero, per cui si vede sia il canvas Excalidraw (a sinistra, con **"ONTOLOGIA"** pienamente visibile e "SONOMIA" tagliato — resto di "TASSONOMIA" fuori campo a sinistra) sia, alla destra della finestra browser, la sidebar Explorer di un editor scuro con radice **"Company Brain"** e sottocartelle elencate: **.showcase, .claude, .obsidian, .tmp, areas, code, concepts, data, docs, engine, entities, labs, outputs, projects, scripts, self, sources, studio, workspace** (workspace evidenziata/selezionata in blu). Toolbar del browser in alto con icone circolari colorate (blu, rosso, viola) e icone cloud/lente/stella. Webcam Giovanni in basso a sinistra.
Voce: *"una serie di cartelle. Le cartelle sono, ok, tutta una serie di cose, quindi"* — introduce il concetto di cartelle come base della tassonomia.

### Scena 133 · `frame-0601.png` · 60:00 — Excalidraw a schermo intero, Tassonomia/Ontologia
Finestra ora massimizzata: canvas Excalidraw (excalidraw.com nella barra indirizzo) a schermo intero, schema **TASSONOMIA / ONTOLOGIA** della scena 130 pienamente visibile e centrato — colonna sinistra "Progetti" → "Progetti Interni"/"Progetti Clienti", fumetti "Che tipo di cosa è?" / "ti dice dove archiviarla"; colonna destra "Aurora Sistemi" (azienda) ↔ "Marco" (persona) con freccia "lavora nel commerciale", fumetti "Cosa sono e come si collegano?" / "leggibile da una macchina". Pannello strumenti Excalidraw a sinistra invariato. Piccolo cursore a croce ("+") in alto a sinistra del canvas. Webcam in basso a sinistra.
Voce: *"immaginatevi di avere il vostro alberello, ok? Che faccia così, che"* — usa la metafora dell'albero di cartelle per spiegare la tassonomia.

### Scena 134 · `frame-0604.png` · 60:18 — stesso schema, cursore a freccia sul lato Tassonomia
Stesso schema TASSONOMIA/ONTOLOGIA, canvas leggermente ripannato rispetto alla scena precedente (schema spostato un poco a sinistra). Cursore ora a forma di freccia ripiegata ("↖"-simile) appena a sinistra del titolo "TASSONOMIA", nessun testo nuovo ancora scritto. Nessun'altra differenza di contenuto.
Voce: *"come deve essere archiviato qualcosa. Ok? Quindi questo mi dice come devo"* — spiega che la tassonomia dice come archiviare i contenuti.

### Scena 135 · `frame-0606.png` · 60:30 — Excalidraw, "COMPANY BRAIN: 11 CARTELLE" con annotazioni a mano ⭐
Ritorno allo schema della scena 122 ("COMPANY BRAIN: 11 CARTELLE", nastro con sottotitolo "Una sola decisione: quanto e' azionabile?"), ma ora arricchito da numerose annotazioni a pennarello blu aggiunte sopra/attorno alle 11 card colorate (il titolo e l'angolo superiore destro sono tagliati dal bordo del frame). Card visibili: **self** "chi e azienda" · **areas** "responsabilita' continue" · **projects** "lavoro a tempo, con traguardo" · **sources** "la inbox grezza" (riga 1, "sources" tagliato a destra); **concepts** "idee, una per nota" · **docs** "procedure intere" · **entities** "schede dei nomi propri" (riga 2, "data" fuori campo a destra); **code** "script e automazioni" · **outputs** "deliverable finiti" (riga 3, "workspace" tagliato a destra). Annotazioni a mano leggibili in questo fotogramma:
- sopra self/areas: icona cerchiata "1", elenco **"OBIETTIVI · MISSIONE · CLIENTI · OFFERTE"** con freccia che scende verso l'alto della card "areas"
- sopra areas/projects: **"REPARTI"** e, più a destra, **"AUTOMAZIONI"** con sotto una parola parzialmente leggibile, verosimilmente **"PROGETTABILE"** ➕ (non completamente certa)
- sopra concepts/docs: **"SOP"**
- sopra entities: due colonne di parole piccole, lette come **"PERSONE / RUOLI"** e **"FORN. / TOOL"** ➕ (grafia minuta, lettura non certa al 100%)
- a sinistra, accanto a concepts: **"ARR: FATTURATO"**, **"AVVIO"**, terza parola poco leggibile (~**"DEFINITORE"**) ➕, e sotto **"CHURN:"** con un tratto/sottolineatura incompiuta
- sotto code: freccia, **"SCRIPT"**, **"ONGOING AUTOMATION"**
- sotto outputs: freccia, **"PROPOSTE"**, **"CASE STUDY"**, **"CONTRATTI"**
- angolo destro, parzialmente tagliato dal bordo del frame: uno schizzo a griglia/tabella con una lettera iniziale simile a **"K"** — illeggibile con certezza, tagliato dal bordo.
Voce: *"se l'avete colta bene, senò ve la dico, è sulla azionabilità quella che io ho"* — rivela il criterio di archiviazione (azionabilità) sotteso alla tassonomia appena mostrata.

### Scena 136 · `frame-0607.png` · 60:36 — stesso schema annotato, inquadratura leggermente diversa
Stesso schema "COMPANY BRAIN: 11 CARTELLE" con le stesse annotazioni della scena precedente, canvas ripannato leggermente a destra: ora il titolo a nastro è pienamente visibile, così come il blocco sinistro **"ARR: FATTURATO / AVVIO / DEFINITORE"** ➕ e **"CHURN:"** per intero; la card **"workspace"** compare ora parzialmente ("workspac...", "bozze e diar..."), tagliata sul bordo destro insieme alla card **data** (visibile solo lo spigolo). Le altre annotazioni (OBIETTIVI/MISSIONE/CLIENTI/OFFERTE, ARTICOLI/APPUNTI/NOTE in alto a destra, SOP, SCRIPT/ONGOING AUTOMATION, PROPOSTE/CASE STUDY/CONTRATTI) sono identiche alla scena 135. Webcam Giovanni in basso a sinistra, mani sollevate a mezz'aria in gesto esplicativo.
Voce: *"scelto. Ok? Quindi, quindi questa è la mia logica di archiviazione."* — conclude che l'azionabilità è il criterio scelto per la sua company Brain.

### Scena 137 · `frame-0609.png` · 60:48 — schema completo "COMPANY BRAIN: 11 CARTELLE", tutte le annotazioni leggibili per intero ⭐
Stesso schema, ora completamente visibile senza tagli di bordo (webcam non sovrappone l'area rilevante). Trascrizione integrale, riga per riga:
- Titolo a nastro: **"COMPANY BRAIN: 11 CARTELLE"**; sottotitolo: **"Una sola decisione: quanto e' azionabile?"**
- Riga 1 delle card: **self** "chi e azienda" · **areas** "responsabilita' continue" · **projects** "lavoro a tempo, con traguardo" · **sources** "la inbox grezza"
- Riga 2: **concepts** "idee, una per nota" · **docs** "procedure intere" · **entities** "schede dei nomi propri" · **data** "i numeri"
- Riga 3: **code** "script e automazioni" · **outputs** "deliverable finiti" · **workspace** "bozze e diario"
- Annotazioni a penna blu sopra le card:
  - sopra self, icona cerchiata "1" e lista **"• OBIETTIVI · • MISSIONE · • CLIENTI · • OFFERTE"**, con freccia verso l'alto della card areas
  - sopra sources, in alto a destra: lista **"• ARTICOLI · • APPUNTI · • NOTE"**
  - tra areas e projects: **"• REPARTI"**, **"AUTOMAZIONI"**, parola sotto poco chiara (~"PROGETTABILE") ➕
  - sopra concepts/docs: **"• SOP"**
  - sopra entities: testo su due colonne piccole, letto come **"PERSONE / RUOLI"** e **"FORN. / TOOL"** ➕ (lettura incerta, grafia minuta)
  - a destra di data: un piccolo schizzo a griglia/tabella con lettere iniziali tipo **"K..."**, tagliato/poco leggibile ➕
- Annotazioni a sinistra del canvas (fuori dalle card, colonna concepts/code): **"ARR: FATTURATO"**, **"AVVIO"**, terza parola incerta (~"DEFINITORE") ➕, sotto **"CHURN:"** con un tratto orizzontale incompiuto
- Sotto code: freccia, **"• SCRIPT"**, **"• ONGOING AUTOMATION"**
- Sotto outputs: freccia, **"• PROPOSTE"**, **"• CASE STUDY"**, **"• CONTRATTI"**
- A destra di workspace: piccola freccia curva e testo **"DIARIO SESSIONI & GIORNALIERO"**
Voce: *"più è riorganizzato nello spazio. Infatti project oneof quando diventano ongoing vanno direttamente dentro code o quando hanno finito vanno dentro output"* ➕ (probabile refuso ASR di "one-off" trascritto "oneof") — la spiegazione a voce combacia con le annotazioni a schermo: i progetti diventano script/ongoing automation dentro code, oppure deliverable dentro outputs.

### Scena 138 · `frame-0612.png` · 61:06 — Excalidraw, schema Tassonomia/Ontologia con nuova annotazione "COME DEVO ARCHIVIARE"
Ritorno al canvas TASSONOMIA/ONTOLOGIA (schema della scena 130/133). A sinistra del riquadro "Progetti" compare una nuova annotazione a penna blu: **"COME / DEVO / ARCHIVIARE"** su tre righe, con una freccia ripiegata che punta verso l'albero di cartelle "Progetti → Progetti Interni / Progetti Clienti". Resto dello schema invariato (fumetti "Che tipo di cosa è?" / "ti dice dove archiviarla" a sinistra; "Aurora Sistemi"/"Marco" con freccia "lavora nel commerciale", fumetti "Cosa sono e come si collegano?" / "leggibile da una macchina" a destra). Webcam in basso a sinistra.
Voce: *"Quindi questa è la mia decisione a livello di brain perché perché io sono"* — introduce la propria scelta di archiviazione (di cui l'annotazione "come devo archiviare" è la sintesi visiva).

### Scena 139 · `frame-0613.png` · 61:12 — stesso schema, annotazione "COME DEVO ARCHIVIARE" confermata
Canvas leggermente ripannato rispetto alla scena precedente (schema spostato più a sinistra, "TASSONOMIA" e "ONTOLOGIA" entrambi pienamente centrati). Annotazione **"COME / DEVO / ARCHIVIARE"** identica, stessa posizione relativa rispetto all'albero "Progetti". Nessun altro cambiamento di contenuto.
Voce: *"molto ehm eh puntato alle azioni, quindi io voglio"* — prosegue spiegando la propria inclinazione all'azionabilità.

### Scena 140 · `frame-0616.png` · 61:30 — schema ripannato, comparsa di una sottolineatura sotto "ONTOLOGIA"
Canvas ripannato ulteriormente verso destra: l'annotazione "COME DEVO ARCHIVIARE" ora è tagliata sul bordo sinistro (si leggono solo frammenti "...ME", "...EVO", "...RCHIVIARE"). Sotto il titolo **"ONTOLOGIA"** compare una nuova sottolineatura/scarabocchio a penna blu (tratto ondulato), assente nelle scene precedenti — sembra un'enfasi appena tracciata. Resto dello schema (Aurora Sistemi/Marco, fumetti) invariato. Webcam in basso a sinistra.
Voce: *"cosa che Obsidian fa, di cui non si parla molto è la parte ontologica."* ➕ — la sottolineatura appena tracciata sotto "ONTOLOGIA" coincide plausibilmente con l'enfasi vocale sulla parola.

### Scena 141 · `frame-0617.png` · 61:36 — Ontologia in primo piano, sottolineatura completa
Canvas ripannato ancora più a destra: la colonna "TASSONOMIA" è quasi interamente fuori campo (si leggono solo frammenti dei box: "...ogetti", "...terni", "...lienti", "...cosa è?"), mentre "ONTOLOGIA" con la sua sottolineatura ondulata è pienamente visibile e centrata, insieme al diagramma "Aurora Sistemi" ↔ "Marco" ("lavora nel commerciale") e ai fumetti "Cosa sono e come si collegano?" / "leggibile da una macchina". Webcam invariata.
Voce: *"Ontologica vuol dire come collego le informazioni. È un'ontologia applicata"* — definisce esplicitamente il concetto di ontologia appena evidenziato a schermo.

### Scena 142 · `frame-0629.png` · 62:48 — solo webcam, penna in mano
Condivisione schermo interrotta: solo webcam a figura intera, stesso sfondo (mensola con libri colorati e pianta pendente a sinistra, lampada accesa a destra). Giovanni tiene in mano una penna argentata/bianca vicino al microfono, sguardo verso il basso, bocca aperta a metà parola.
Voce: *"perché perché ci permette di creare la tassonomia che vogliamo, quindi permette"* — riprende il riassunto sull'importanza della company Brain.

### Scena 143 · `frame-0630.png` · 62:54 — solo webcam, mano destra sollevata a "pizzico"
Stessa inquadratura webcam, nessuna UI. Mano destra sollevata accanto al volto con pollice e indice quasi uniti (gesto di precisione), sguardo fisso in camera.
Voce: *"di archiviare le cose come vogliamo farlo o come il nostro cliente vuole. E"* — sottolinea che la tassonomia si adatta alle proprie esigenze o a quelle del cliente.

### Scena 144 · `frame-0631.png` · 63:00 — solo webcam, mano sollevata più alta
Stessa inquadratura webcam. Mano destra ora sollevata più in alto accanto alla testa, dita leggermente flesse, espressione concentrata.
Voce: *"decidere perché vi darà il funzionamento di tutta l'azienda. Se volete tenere la"* — insiste sull'importanza della scelta della tassonomia per il funzionamento dell'azienda.

### Scena 145 · `frame-0632.png` · 63:06 — solo webcam, sguardo fisso in camera
Stessa inquadratura webcam, mani non visibili (fuori campo sotto il microfono), espressione neutra e fissa verso l'obiettivo.
Voce: *"tassonomia che ho fatto io, l'ho fatta apposta perché funzioni in qualsiasi business, no?"* — dichiara che la propria tassonomia è stata progettata per essere agnostica rispetto al tipo di business.
</content>

### Scena 146 · `frame-0633.png` · 63:12
Talking head, uomo con maglietta blu scura, mani alzate davanti al petto con dita curve mentre gesticola (mima le "microbacinelle" di cui parla). Stessa scenografia delle scene di apertura: mensola con libri colorati, pianta rampicante, lampada calda. Nessun testo a schermo.
Voce: *"non ha un funziona solo per, non lo so, la clinica o la l'officina, funziona pure per me che faccio contenuto, ho la mia agenzia e cose di questo tipo, no?"* — ribadisce che l'ontologia che sta per mostrare è agnostica rispetto al tipo di business.

### Scena 147 · `frame-0634.png` · 63:18
Talking head, leggero pan, una mano sollevata fuori fuoco a sinistra.
Voce: *"E poi avete l'ontologia. L'ontologia è la logica di collegamento ed è una cosa che voi ovviamente se non volete seguire la mia logica dovrete farvi, no?"*

### Scena 148 · `frame-0635.png` · 63:24
Talking head, mano destra portata verso il mento/guancia.
Voce: *"Quindi dovrete dare ad Obsidian il come colleghiamo queste cosine qui. Ok?"*

### Scena 149 · `frame-0636.png` · 63:30
Talking head, inquadratura frontale stabile, bocca aperta a metà frase.
Voce: *"Quindi, detto questo, adesso torniamo a bomba dentro la nostra AI"* — chiusura del blocco teorico sull'ontologia, transizione verso la parte pratica.

### Scena 150 · `frame-0638.png` · 63:42 — **slide "ONTOLOGIA" con l'esempio Aurora/Marco** ⭐
Excalidraw a schermo intero (talking-head ridotto a riquadro in basso a sinistra). Titolo **"ONTOLOGIA"** sottolineato con tratto ondulato. Due cerchi gialli collegati da doppia freccia: **"Aurora Sistemi"** (sottotitolo *azienda*) ↔ **"Marco"** (sottotitolo *persona*), etichetta sulla freccia **"lavora nel commerciale"**. Sotto, due fumetti: uno viola **"Cosa sono e come si collegano?"**, uno verde acqua **"leggibile da una macchina"**. A destra, schema disegnato a mano in blu: **"AURORA"** e **"MARCO"** in alto, parentesi graffe convergenti su un riquadro **"COMMERC[IALE]"**, da cui partono frecce verso **"DIPENDENTE"**, **"TENURE"**, **"FUNZ[IONE]"** e, più a destra, **"SALARIO"**. Nella colonna sinistra della UI Excalidraw sono visibili due caselle verdi **"Progetti Interni"** / **"Progetti Clienti"** e una casella parzialmente tagliata **"[...t]ipo di cosa è?"**.
Voce: (continuazione della battuta precedente sull'ontologia come "logica di collegamento" tra entità agnostiche rispetto al business).

### Scena 151 · `frame-0639.png` · 63:48
Editor **Antigravity IDE** (VS Code-like), sidebar Explorer con cartella **"aurora cervello"** vuota selezionata. Pannello centrale: tab "Claude Code", scheda "Untitled", intestazione **"🔶 Claude Code"**, mascotte arancione al centro, testo **"Type /model to pick the right tool for the job."** In basso, campo di input con placeholder **"⌘ Esc to focus or unfocus Claude"** e toggle **"Bypass permissions"** a destra.
Voce: *"e quindi adesso io posso chiudere la mia company Brain perché partiamo ora da Aurora Cervello."*

### Scena 152 · `frame-0640.png` · 63:54
Desktop macOS (sfondo Lake Tahoe). Icone cartelle visibili: "[Giovan]ni Beggiato", **"aurora cervello"**, **"Company Knowledge Base"** (selezionata, con tooltip), **"Second Brain"**, **"Knowledge Base"**, "Agentic Personal", "Archive", un video "3. Business part - pandadoc.mov", "OBS Recordings", "Linkedin", "headshot", **"Company Brain"**, uno screenshot datato "2026-0...t 10.31.08". Dock in basso con Finder, Chrome, ChatGPT, Slack, Antigravity e altre app.
Voce: *"Ho cancellato giusto per farvi vedere tutto quanto quello che c'era dentro al mio ehm Aurora cervello."*
➕ Le molte cartelle simili ("Second Brain", "Knowledge Base", "Company Brain", "Company Knowledge Base") sembrano essere tentativi/demo precedenti dello stesso autore, non spiegate a voce in questo punto.

### Scena 153 · `frame-0641.png` · 64:00 — **Mission Control conferma il nome "Antigravity IDE"** ⭐
Vista Mission Control di macOS con le finestre/spazi aperti in miniatura, etichettati: "Desktop 1", "Google Chrome", "Notion", **"Antigravity IDE"**, "Obsidian" (quest'ultimo con tooltip **"No Available Windows"**, cioè nessuna finestra ancora aperta).
Voce: *"Ed il motivo è perché ora voglio cominciare a costruirlo."*
🔎 Questo frame conferma testualmente il nome esatto dell'editor usato per Claude Code: **"Antigravity IDE"**.

# PARTE B2 — Creazione delle 11 cartelle in Obsidian + Claude (64:06 → 69:18)

### Scena 154 · `frame-0642.png` · 64:06
Stessa schermata Claude Code vuota in Antigravity IDE (mascotte arancione, placeholder "Type /model to pick the right tool for the job."), cartella "aurora cervello" ancora vuota nell'Explorer.
Voce: *"Per farlo, adesso vado nel mio bellissimo notion e quindi posso dirgli"*

### Scena 155 · `frame-0643.png` · 64:12 — **la pagina Notion "Company Brain — Tutti i prompt"** ⭐
Notion a schermo intero. Sidebar sinistra: Home, Meetings (Connect your calendar, New AI meeting note), Recenti (Clienti, Cruscotto Aurora, **"Company Brain — Tutti i prompt del..."** evidenziata, New page, Reparti, Prodotti, Default view, KPI mensili, Sedi, Competitor), sezione Agents (New agent), Shared. In alto: titolo pagina "Company Brain — Tutti i prompt del...", lucchetto "Private", "Translate to English", Share.
Contenuto visibile (fine punto 6 precedente + inizio Passo 2):
> 6. Frontmatter — apri `self-identita-aurora` e incolla questo blocco in cima, prima del testo:
> ```
> title: Identita' di Aurora Sistemi
> summary: Aurora Sistemi e un'azienda da 340 persone che vende sistemi di efficie[nza...]
> tags: [self, type/identita]
> status: active
> created: 2026-06-09
> updated: 2026-06-09
> related: [[persona-elena-ferraro]]
> ---
> ```
> **Passo 2 — Le 11 cartelle e le prime note con l'AI**
> **Prompt 1 — Crea le 11 cartelle**
> Da' all'AI lo scheletro del cervello: 11 cartelle vuote, niente altro.
> ```
> [C]rea nel mio vault, alla radice, queste 11 cartelle vuote, una per ciascun lavoro del cervello:
> self, areas, projects, sources, concepts, docs, entities, data, code, outputs, workspace.
> Non crearne altre e non metterci dentro nessun file. Solo le 11 cartelle.
> ```
> **Prompt 2 — Estrai il canon (prima un piano, poi il tuo ok)**
> Congela i fatti d[uri dell'azienda in un] canon coerente. (Prima metti il materiale grezzo dell'azienda dentro `sources/`.) *(riga finale tagliata dal frame)*

Un tooltip **"Copied code to clipboard"** conferma che l'autore ha appena copiato il blocco del Prompt 1.
Voce: *"dargli il primo script, il primo prompt, perdonatemi. Quindi quello che gli"*

### Scena 156 · `frame-0644.png` · 64:18 — **Prompt 1 incollato in Claude Code, pronto per l'invio** ⭐
Antigravity IDE, campo di input di Claude Code con il testo incollato ed evidenziato (selezione blu sulle prime parole):
> "Crea nel mio vau[l]t, alla radice, queste 11 cartelle vuote, una per ciascun lavoro del cervello: self, areas, projects, sources, concepts, docs, entities, data, code, outputs, workspace. Non crearne altre e non metterci dentro nessun file. Solo le 11 cartelle."

Testo identico, parola per parola, a quello appena letto sulla pagina Notion. Toggle "Bypass permissions" visibile in basso a destra del campo.
Voce: *"faccio è creami nel mio volt alla radice queste 11 cartelle vuote, una per ciascun lavoro del cervello, self, whatever, ehm, non crearne altre, non metterci nessun file dentro, solo le cartelle."*

### Scena 157 · `frame-0648.png` · 64:42
Desktop macOS; sopra la cartella "aurora cervello" è comparsa una nuova cartella etichettata **"source[s]"**, con sopra una piccola finestra di anteprima/Quick Look che mostra un elenco di righe simile a una tabella (contenuto non leggibile con certezza a questa risoluzione).
Voce: *"Adesso, perché è importante cominciare? Perché gli diamo una struttura e io poi ho anche creato, vediamo se riesco a farvelo vedere, sì, un documento molto casuale dove ho le sources, ok?"*

### Scena 158 · `frame-0649.png` · 64:48 — **Explorer con le 11 cartelle create + primo file sources aperto** ⭐
Antigravity IDE: la sidebar Explorer ora mostra la cartella "aurora cervello" **popolata con le 11 sottocartelle**: areas, code, concepts, data, docs, entities, outputs, projects, self, sources, workspace (elenco alfabetico, tutte vuote). Nel pannello di chat Claude Code, tab "Create 11 brain folders...": messaggio utente col Prompt 1, poi risposta:
- "Thought for 1s"
- "Creo le 11 cartelle vuote alla radice del vault."
- blocco **Bash** "Create 11 empty folders in vault root": `cd "/Users/giovannibeggiato/Desktop/aurora cervello" && mkdir -p self areas pro[jects...]` con output `total 24` e permessi cartella (`drwxr-xr-x@ 14 giovannibeggiato staff 448 Jun 10 12:14 .`)
- "Fatto. Le 11 cartelle vuote sono alla radice del vault: self, areas, projects, sources, concepts, docs, entities, data, code, outputs, workspace. Nessun file dentro, nessuna cartella extra."

A destra si è aperto un secondo file, **`01_chi-siamo-sito-web.md`** (percorso `Users > giovannibeggiato > Desktop > sources > 01_chi-siamo-sito-web.md`), parzialmente leggibile (testo completo nella scena successiva).
Voce: *"Queste sono le cose che alcune le trovate nei siti aziendali, no? se le vedete, quindi ve lo faccio vedere brevemente. Quindi un chi siamo, la nostra missione, cosa facciamo, sono tutte organizzate un po' in maniera casuale."*

### Scena 159 · `frame-0650.png` · 64:54 — **testo integrale di `01_chi-siamo-sito-web.md`** ⭐
Stessa schermata, editor allargato: il file **`01_chi-siamo-sito-web.md`** (dentro `sources/`) è ora leggibile per intero, riga per riga:
```
1  # Chi siamo — testo pagina "Azienda" del sito aurorasistemi.it
2  _(ultima revisione marketing: gennaio 2026)_
5  ## La nostra missione
6  Rendere ogni edificio più efficiente, sicuro e sostenibile, dando a chi gestisce
7  il patrimonio immobiliare un unico "cervello digitale" al posto di dieci sistemi
8  scollegati.
10 ## In breve
11 Aurora Sistemi S.p.A. nasce a Milano nel 2018 dall'idea di due ingegneri, Elena
12 Ferraro e Marco Bianchi, convinti che la gestione degli immobili in Italia fosse
13 ancora ferma a fogli Excel e centraline che non si parlano tra loro.
15 Oggi siamo un team di 47 persone. La sede principale è a Milano, in Via Tortona
16 27; dal 2022 abbiamo aperto un secondo ufficio a Bologna, dove si trova buona
17 parte del team di Customer Success.
19 ## Cosa facciamo
20 Aurora Sistemi è una piattaforma software (SaaS) in cloud per la gestione
21 intelligente degli edifici. In un'unica interfaccia il cliente vede tutti i suoi
22 immobili: consumi energetici, manutenzioni, accessi e sicurezza, documenti.
24 ## Come ci posizioniamo
25 Siamo "la piattaforma italiana per la gestione intelligente del patrimonio
26 immobiliare". A differenza dei vecchi sistemi BMS, frammentati e legati
27 all'hardware, Aurora è una soluzione unica, in cloud, conforme al GDPR e pensata
28 per chi gestisce decine o centinaia di edifici.
30 ## A chi ci rivolgiamo
31 Lavoriamo con organizzazioni che gestiscono patrimoni immobiliari medio-grandi in
32 Italia — di norma dai 20 edifici in su: società di property e facility
33 management, catene retail, pubblica amministrazione, sanità e banche.
```
Nota bene: questo è materiale-sorgente **finto** per la demo (l'azienda "Aurora Sistemi" è dichiarata fittizia dallo stesso autore più avanti, a 67:55).
Voce: *"Poi un organigramma di ruoli, persone, cose, poi ho un export di CRM con un po' di clienti e cose di questo tipo, no?"*

### Scena 160 · `frame-0652.png` · 65:06 — **elenco file di `sources/` + export CRM aperto in foglio di calcolo** ⭐
Due finestre sovrapposte sul Desktop. A sinistra, un foglio di calcolo (pannello proprietà "Sheet" con "Sheet Name: Sheet 1", pulsanti "Duplicate Sheet"/"Delete Sheet") con una tabella dati, colonne **ARR_eur | stato | moduli_attivi**:
```
720000  attivo            Core, Energy, Manutenzione, Insights
640000  attivo            Core, Energy, Access
410000  attivo            Core, Manutenzione
350000  attivo            Core, Energy, Insights
300000  attivo            Core, Manutenzione, Access
380000  attivo            Core, Energy, Manutenzione
260000  attivo            Core, Access
520000  attivo            Core, Access, Manutenzione
290000  attivo            Core, Energy
180000  churned 06/2025   Core, Manutenzione
```
A destra, una finestra Finder mostra il contenuto della cartella **`sources/`**, 9 file selezionabili:
`01_chi-siamo-sito-web.md`, `02_pitch-deck-vendita.md`, `03_prodotti-brochure.md`, `04_organigramma.md`, `05_verbale-board-Q4-2025.md`, **`06_export-CRM-clienti.csv`** (evidenziato, è il file aperto nel foglio a sinistra), `07_note-customer-success.md`, `08_intervista-CEO_podcast.md`, `09_email-interne.md`.
Voce: *"export di CRM con un po' di clienti e cose di questo tipo, no? Quindi qui vediamo cose puramente generate da AI e"*

### Scena 161 · `frame-0653.png` · 65:12
Torna il Desktop pulito (senza finestre aperte), sidebar Finder ancora visibile sul lato destro con Preferiti/Tag ma senza elenco file.
Voce: *"vediamo che ho, insomma, un sacco di dati incasinati. Adesso il motivo per cui non posso"*

### Scena 162 · `frame-0654.png` · 65:18 — **comando bash completo per creare le 11 cartelle** ⭐
Stessa conversazione Claude Code di prima, ora leggibile a piena larghezza. Il blocco Bash è completo:
```
$ cd "/Users/giovannibeggiato/Desktop/aurora cervello" && mkdir -p self areas projects sources concepts docs entities data code outputs workspace && ls -la
```
Output: `total 24`, `drwxr-xr-x@ 14 giovannibeggiato staff 448 Jun 10 12:14 .`, `drwx------@ 18 giovannibeggiato staff 576 Jun 10 11:52 ..` (righe successive con le 11 cartelle non visibili, tagliate dallo scroll). Nel campo di input in basso è agganciato come chip il file `01_chi-siamo_sito-web.md`.
Voce: *"dargli impasto i dati a cazzo così e devo dargli prima una struttura è che"*

### Scena 163 · `frame-0659.png` · 65:48 — **Notion: Prompt 1 completo + inizio Prompt 2 (Canon)** ⭐
Notion, pagina "Company Brain — Tutti i prompt", scrollata sul Prompt 1 e sull'inizio del Prompt 2:
> **Prompt 1 — Crea le 11 cartelle**
> Dà all'AI lo scheletro del cervello: 11 cartelle vuote, niente altro.
> ```
> Crea nel mio vault, alla radice, queste 11 cartelle vuote, una per ciascun lavoro del cervello:
> self, areas, projects, sources, concepts, docs, entities, data, code, outputs, workspace.
> Non crearne altre e non metterci dentro nessun file. Solo le 11 cartelle.
> ```
> **Prompt 2 — Estrai il canon (prima un piano, poi il tuo ok)**
> Congela i fatti duri dell'azienda in un unico canon coerente. (Prima metti il materiale grezzo dell'azienda dentro `sources/`.)
> ```
> Sei l'architetto del cervello aziendale di Aurora Sistemi S.p.A., un'azienda fittizia che useremo per la demo.
> Leggi tutto il materiale grezzo nella cartella sources/. Da lì, estrai i FATTI duri e scrivili in un UNICO canon coerente. Il canon deve coprire:
> - identità: missione, cliente ideale (ICP), offerta, posizionamento, sedi, anno di fondazione, numero di dipendenti;
> - prodotti, con cosa fa ciascuno;
> - reparti (le funzioni continue dell'azienda);
> - persone e ruoli;
> - clienti, ognuno con i suoi numeri (da quando sono clienti, quanti immobili, ARR);
> - KPI di fine 2025: ARR totale, clienti attivi, churn, NRR, edifici gestiti.
> Regole d'oro:
> - nessun fatto inventato: se non è nel materiale in sources/, NON scriverlo;
> - i numeri devono QUADRARE tra loro (la somma dell'ARR dei clienti deve essere coerente con l'ARR totale dei KPI);
> [continua, tagliato dal bordo inferiore del frame]
> ```
Voce: *"nel nostro notion di ehm che cos'è un canon. Allora, immaginatevi di avere,"*

### Scena 164 · `frame-0664.png` · 66:18 — **l'analogia del "bacinello d'acqua" disegnata sopra Notion** ⭐
Stessa pagina Notion, ora con un'annotazione a mano disegnata in blu sopra il testo (sovrapposizione tipo lavagna): a sinistra un bicchiere/bacinello grande parzialmente riempito di blu, collegato con linee a due-tre bicchieri più piccoli e vuoti in alto a destra — la rappresentazione visiva del "bacinello d'acqua che si spezza in 11 microbacinelle" descritto a voce. Sotto, il testo del Prompt 2 mostra ora con i marcatori Markdown grezzi (`**...**`) visibili: "Sei l'architetto del cervello aziendale di **Aurora Sistemi S.p.A.**, un'azienda [fittizia...]", "## Il canon deve coprire", "- **Identità**: missione, cliente ideale (ICP), offerta, posizionamento, sedi, an[no...]", "- **Prodotti**: con la descrizione di cosa fa ciascuno.", "- **Reparti**: le funzioni continue dell'azienda.", "- **Persone e ruoli**.", "- **Clienti**: ognuno con i suoi numeri (da quando sono clienti, quanti immobili, ARR).", "- **KPI di fine 2025**: [ARR totale, clienti attivi, churn, NRR, edifici gestiti — riga tagliata in basso]".
Voce: *"microbacinelle, ok? Ovviamente ogni singola di queste bacinelle avrà al suo"*

### Scena 165 · `frame-0679.png` · 67:48
Torna la stessa conversazione Claude Code (folder creation), campo di input vuoto, cursore del mouse fermo sopra il toggle "Bypass permissions" in basso a destra.
Voce: *"gli diremo adesso questo. Quindi,"*

### Scena 166 · `frame-0682.png` · 68:06
Transizione: Desktop macOS visibile sotto, con la sidebar di Notion che scompare/appare in sovraimpressione sul bordo destro (Home, Meetings, Recents: Clienti, Cruscotto Aur[ora], Company Brai[n], New page, Reparti, Prodotti, Default view, KPI mensili, Sedi, Competitor, Agents, Shared, Private).
Voce: *"dentro nel mio desktop, quindi dovrò eh"*

### Scena 167 · `frame-0683.png` · 68:12 — **Prompt 2 (Canon) incollato in Claude Code** ⭐
Antigravity IDE: il testo del Prompt 2 è ora incollato nel campo di input di Claude Code, leggibile:
> "Leggi tutto il materiale grezzo nella cartella `sources/`. Da lì, estrai i **fatti duri** e scrivili in un **unico canon coerente**.
> ## Il canon deve coprire
> - **Identità**: missione, cliente ideale (ICP), offerta, posizionamento, sedi, anno di fondazione, numero di dipendenti.
> - **Prodotti**: con la descrizione di cosa fa ciascuno.
> - **Reparti**: le funzioni continue dell'azienda.
> - **Persone e ruoli**."
(testo continua oltre il bordo inferiore del riquadro, non visibile in questo frame)
Voce: *"dirgli ora che è nel desktop. Ok, quindi"*

### Scena 168 · `frame-0694.png` · 69:18 — **piano in 5 punti di Claude prima di scrivere il Canon** ⭐
Claude Code, stessa chat: il prompt utente (collassato) mostra il chip allegato `01_chi-siamo_sito-web.md` e l'incipit "Sei l'architetto del cervello aziendale di **Aurora Sistemi S.p.A.**, un'azienda fittizia che useremo per la demo." (resto del prompt grigio/collassato). Sotto, la sequenza di azioni di Claude:
- Read `07_note-customer-success.md`
- Read `08_intervista-CEO_podcast.md`
- Read `09_email-interne.md`
- "Thought for 9s"
- **"Ho letto tutti e 9 i file in `sources/` e verificato i numeri. Ecco il piano:"**
1. **Trovato**: sito "chi siamo", pitch deck, brochure prodotti, organigramma HR, verbale board Q4 2025, export CRM clienti, note Customer Success, intervista CEO, email interne. Le fonti sono coerenti tra loro, nessuna contraddizione.
2. **I numeri quadrano già**: la somma ARR dei 9 clienti attivi nel CRM fa esattamente **€ 3.840.000** e gli immobili sommano esattamente **751**, identici ai KPI del verbale board e del deck. Churn **180k = Costruzioni Sud, -5,8% del 3,1M di inizio anno**.
3. **Struttura del canon**: un solo file con 6 sezioni nell'ordine richiesto: Identità → Prodotti (5 moduli) → Reparti (6 funzioni) → Persone e ruoli (11 nominate + distribuzione team) → Clienti (tabella: 9 attivi + Costruzioni Sud marcato churned, con anno, immobili, ARR, moduli) → KPI fine 2025 (con riga di verifica che mostra che le somme tornano).
4. **Dove lo scrivo**: `workspace/canon.md` nel vault (è un file di lavoro, non una nota finale).
5. **Cosa lascio fuori**: niente di inventato; includo l'obiettivo 2026 del board (**ARR >5M, NRR >110%, churn <10%, +6 assunzioni**) come fatto documentato, segnalato come obiettivo e non come KPI.

"Ok per scrivere?"

Explorer a sinistra: cartella "aurora cervello" con le 11 sottocartelle già elencate (areas, code, concepts, data, docs, entities, outputs, projects, self, sources, workspace), ancora senza badge di contenuto.
Voce: *"leggerlo in maniera adeguata. E mi dice"* — la battuta successiva del narratore, *"ho letto tutti e noi i file in sources e verificato i numeri. Ecco il piano"*, corrisponde quasi verbatim al testo a schermo.
🔎 La trascrizione automatica rende "tutti e 9 i file" come *"tutti e noi i file"*: il frame mostra chiaramente **"tutti e 9 i file"**.

# PARTE B3 — Canon aziendale e note atomiche (70:18 → 74:24)

### Scena 169 · `frame-0704.png` · 70:18 — **slide "LA NOTA ATOMICA" nomina Niklas Luhmann per iscritto** ⭐
Excalidraw a schermo intero. Titolo **"LA NOTA ATOMICA"**, sottotitolo **"Niklas Luhmann: una idea per scheda"**. Confronto in due colonne:
- **"NO"**: rettangolo arancione pallido **"PDF da 40 pagine, tutto insieme"**, con una X sotto e la scritta **"nessuno lo riusa"**.
- **"SI"**: cinque caselle colorate disposte a rete, ciascuna **"1 idea"** (viola, verde, arancione al centro, giallo, blu), collegate tra loro da linee curve; sotto, **"il valore è nei legami"** e **"riusabile in 20 contesti"**.
🔎 Il nome **Niklas Luhmann** compare qui esplicitamente per iscritto sulla slide, mentre a voce (69:37 ca.) l'autore dice *"non pronuncerò ora questa parola"* riferendosi al metodo (Zettelkasten, mai nominato a voce in questo tratto).
Voce: *"introduciamo il concetto di che cos'è"* — introduzione della nota atomica prima di tornare a Notion.

### Scena 170 · `frame-0706.png` · 70:30
Stessa slide "LA NOTA ATOMICA", inquadratura leggermente diversa: titolo e sottotitolo "Niklas Luhmann: una idea per scheda" pienamente visibili in alto a destra, colonna "NO" con il riquadro arancione "PDF da 40 pagine, tutto insieme" e la X con "nessuno lo riusa" ben leggibili; sul bordo destro si intravede l'inizio della colonna "SI" (due caselle "1 idea" tagliate).
Voce: *"tirato per i capelli, ma è il prefondatore di e delle teorie alla base"*

### Scena 171 · `frame-0717.png` · 71:36 — **"ZETTELKASTEN" scritto a mano + esempio Fiducia/Soldi + "90.000+"** ⭐
Sopra la stessa slide compare un'annotazione a mano in blu: la scritta **"ZETTELKASTEN"** in stampatello, con due frecce che scendono verso due riquadri numerati — **"FIDUCIA"** (cerchio "①") e **"SOLDI"** (cerchio "②") — gli esempi di "scheda 1" e "scheda 2" citati a voce. Più in basso a sinistra, scritto a mano: **"90.000+"** (il numero di schede del metodo). Sul bordo destro si intravede ancora il riquadro arancione "NO" della slide sottostante.
Voce: *"fatto è stato creare 90.000 schede autonome con cui scriveva i libri. Che"*
🔎 Il nome del metodo, **"Zettelkasten"**, che il narratore dichiara esplicitamente di non voler pronunciare a voce ("non pronuncerò ora questa parola", 70:44-70:51), compare qui scritto per esteso a mano sullo schermo.

### Scena 172 · `frame-0739.png` · 73:48
Slide "LA NOTA ATOMICA" di nuovo pulita, senza le annotazioni a mano della scena 171 (probabilmente rimosse o su un livello separato). Colonna "SI" con la rete completa delle 5 caselle "1 idea" colorate, "il valore è nei legami", "riusabile in 20 contesti".
Voce: (pausa nel parlato tra 73:45 e 73:54) *"questo, tornando alla nostra immagin[e]... è che non vogliamo avere questi malloppi di PDF da 40 pagine tutti insieme, ma"*

### Scena 173 · `frame-0745.png` · 74:24
Stessa slide, zoom leggermente diverso: sotto "PDF da 40 pagine, tutto insieme" compare ora una sottolineatura ondulata blu sulla parola "pagine", e sotto "riusabile in 20 contesti" una sottolineatura ondulata blu su "riusabile in 20 contesti" — l'autore sta enfatizzando questi due punti col tratto a mano.
Voce: *"di fondo aziendale, no? Un ultimo"*

# PARTE B4 — Costruzione degli Hub (Hub And Spoke) e degli indici (74:30 → 82:18)

### Scena 174 · `frame-0746.png` · 74:30 — **slide "HUB-AND-SPOKE: l'ordine di costruzione"** ⭐
Nuova slide Excalidraw. Titolo **"HUB-AND-SPOKE: l'ordine di costruzione"**, sottotitolo **"come una ruota di bicicletta"**. Al centro un cerchio grigio **"HUB"** con icona persona e didascalia **"identita azienda, reparti"** (così scritto, senza accento sullo schermo). Attorno, sei nodi colorati etichettati **"dettaglio"** con icone diverse (documento, informazione "i", posizione/pin, due liste, organigramma ad albero), collegati al centro da linee radiali grigie e tra loro da un cerchio tratteggiato. Etichette curve: **"1) prima gli hub"** e **"2) poi i dettagli"**. Sotto, un riquadro: **"Ogni link punta a qualcosa che esiste già, quindi i link rotti sono impossibili."**
Voce: *"concetto da introdurre prima di andare in notion è gli hub[,] che cosa vuol"*

### Scena 175 · `frame-0753.png` · 75:12
Vista intermedia/scroll tra la slide "LA NOTA ATOMICA" (parzialmente visibile a sinistra, con "riusabile in 20 contesti" sottolineato) e l'inizio della slide successiva ("...ordine di costruzione" appena visibile in basso).
Voce: *"che ora, se noi non facessimo il"*

### Scena 176 · `frame-0756.png` · 75:30
Ulteriore scroll: sopra rimane visibile la rete "SI" della nota atomica, sotto compare uno schizzo preparatorio a mano in blu — una serie di ovali/pallini collegati da linee che convergono verso un nodo centrale (a forma di stella/ragno), con un piccolo cerchio rosso isolato a destra — bozza preliminare del diagramma hub-and-spoke prima della versione pulita. In basso a sinistra si legge il titolo parziale **"SPOKE: l'ordine di costruzione"**.
Voce: *"pallino viene creato prima del tag o prima della nota corrispondente"*

### Scena 177 · `frame-0760.png` · 75:54 — **Hub-and-Spoke, versione completa e leggibile** ⭐
Slide "HUB-AND-SPOKE: l'ordine di costruzione" a schermo pieno, identica alla scena 174 ma più leggibile: si notano due collegamenti (verso il nodo in alto e verso quello a sinistra) evidenziati in blu più spesso rispetto agli altri quattro, come se l'autore stesse animando/ripercorrendo le connessioni una per una. In alto a destra, residuo dello schizzo a mano libera della scena 176 (alcuni cerchi blu collegati) rimasto su un'altra porzione della canvas infinita di Excalidraw.
Voce: *"ora che hai le tue cartelle, le 11, assicurati di avere gli hub, quindi"*

### Scena 178 · `frame-0763.png` · 76:12 — **Prompt 3 completo in Notion: "Trasforma il canon in note atomiche"** ⭐
Notion, pagina "Company Brain — Tutti i prompt del...". In alto, coda delle **Regole** del Prompt 2 (Canon):
> ## Regole
> - Nessun fatto inventato: se non è nel materiale in `sources/`, non scriverlo.
> - I numeri devono **quadrare** tra loro (la somma dell'ARR dei client[i] deve esse[re coerente...] [taglio a bordo destro]
> - Scrivi il canon in un solo file di lavoro, non ancora come note finali.
> - Se non riesci a fare qualcosa, comunicalo.
>
> ## Prima di scrivere
> Dammi un piano in 5 righe di cosa hai trovato in `sources/` e di come pensi di st[rutturare...] [taglio]

Sotto, titolo **"Prompt 3 — Trasforma il canon in note atomiche (prima gli hub)"**, sottotitolo *"Dal canon alle note vere, in ordine hub-and-spoke: prima le note-mappa, poi i dettagli."* Riquadro del prompt:
> Ottimo, il canon va bene. Ora trasformalo in note atomiche dentro le 11 cartelle.
>
> ## Regole per ogni nota compilata
> - Una sola idea per nota, massimo 300 righe.
> - In cima, il frontmatter con: `title`, `summary` (una frase), `tags` (il primo è... [taglio]
> - Il campo `related` deve stare su una sola riga fisica, con i wikilink separati [taglio]
> - Almeno 3 wikilink uscenti verso note reali (conta i target unici, non lo stes[so link ripetuto]) [taglio]
> - Nome del file unico in tutto il vault, con un prefisso di dominio: `self-identi[tà-aurora]`... [taglio]
>
> ## Ordine di costruzione (rispettalo)
> 1. Prima gli **hub** (le note-mappa): `self/self-identita-aurora` (l'hub central[e]... [taglio]
> 2. Poi le note di **dettaglio**: prodotti, clienti, KPI, concetti. Ognuna si col[lega...] [taglio]
>
> Un wikilink punta solo a una nota che esiste già: niente link verso note non anc[ora create]. [taglio]
>
> Parti dagli hub. Mostrami `self-identita-aurora` prima di proseguire.

Sotto ancora, titolo successivo appena visibile: **"Prompt 4 — Completa il cervello fino a circa 28 note"**.
Voce: *"andando nel nostro notion, questo è il nostro prompt e ora andremo di nuovo nel nostro AI e gli diremo questo. E cosa gli diciamo? Allora, ottimo, il Canon va bene. Ora trasformalo in note atomiche dentro le 11 cartelle."*
🔎 Diverse righe del prompt sono tagliate dal bordo destro/inferiore del frame (marcato `[taglio]` sopra); il contenuto oltre il taglio non è leggibile in questo frame.

### Scena 179 · `frame-0764.png` · 76:18
Antigravity IDE, tab "Create 11 brain folders in vault root". Sidebar Explorer a sinistra con la cartella "aurora cervello" e le sottocartelle: areas, code, concepts, data, docs, entities, outputs, projects, self, sources, workspace. Nella chat, prompt utente collassato con chip allegato `01_chi-siamo_sito-web.md` e incipit "Sei l'architetto del cervello aziendale di **Aurora Sistemi S.p.A.**, un'azienda fittizia che useremo per la demo." Sotto, la sequenza di azioni già note (Read `07_note-customer-success.md`, Read `08_intervista-CEO_podcast.md`, Read `09_email-interne.md`, "Thought for 9s") e il piano in 5 punti che si conclude con "Ok per scrivere?" — il cursore del mouse è fermo sul campo di input in basso, sopra il chip del file allegato, accanto al toggle "Bypass permissions".
Voce: *"nostro prompt e ora andremo di nuovo nel nostro AI e gli diremo questo. E cosa"*

### Scena 180 · `frame-0765.png` · 76:24 — **Prompt 3 incollato per intero nel campo di input di Claude Code** ⭐
Stessa vista, chat scrollata: il piano in 5 punti e "Ok per scrivere?" restano visibili sopra. Nel campo di input in basso, incorniciato in rosso (evidenziato), il testo del Prompt 3 è ora incollato integralmente e leggibile:
> "Ottimo, il canon va bene. Ora trasformalo in note atomiche dentro le 11 cartelle.
> ## Regole per ogni nota compilata
> - Una sola idea per nota, massimo 300 righe.
> - In cima, il frontmatter con: `title`, `summary` (una frase), `tags` (il primo è sempre il nome della cartella), `status`, `created`, `updated` e il campo `related`.
> - Il campo `related` deve stare su una sola riga fisica, con i wikilink separati da virgola e senza spazi dentro le doppie parentesi.
> - Almeno 3 wikilink uscenti verso note reali (conta i target unici, non lo stesso link ripetuto).
> - Nome del file unico in tutto il vault, con un prefisso di dominio: `self-identita-aurora`, `cliente-..." [continua, tagliato dal bordo destro]
Voce: *"gli diciamo? Allora, ottimo, il Canon va bene. Ora trasformalo in note atomiche dentro le 11 cartelle. Regola per ogni"*

### Scena 181 · `frame-0776.png` · 77:30
Stessa chat: il prompt precedente ora appare collassato in una card grigia ("Ottimo, il canon va bene. Ora trasformalo in note atomiche dentro le 11 cartelle." con link "Show more"), sotto la scritta di stato **"Schlepping..."** (Claude sta elaborando). Il campo di input in basso mostra "Queue another message..." con l'icona di stop (quadratino rosso) al posto della freccia di invio, segno che l'esecuzione è in corso.
Voce: *"bypass permission e vediamo che cosa ci produce. Perfetto. Allora, mi dice Canon scritto in"*

### Scena 182 · `frame-0777.png` · 77:36 — **hub `self-identita-aurora.md` scritto, frontmatter completo** ⭐
Nella chat compare l'azione **Write `self-identita-aurora.md`** (38 righe), con anteprima delle prime righe: "title: Identità — Aurora Sistemi S.p.A." / "summary: Aurora Sistemi è la piattaforma SaaS italiana per la gestione intelligente del patrimonio immobiliare, fondata a Milano nel 2018." Sotto, il messaggio di Claude:
> "Fatto. Canon scritto in `workspace/canon.md` e gli **7 hub** creati (1 self + 6 reparti), tutti interconnessi senza link morti. Ecco `self/self-identita-aurora.md`, l'hub centrale:"

Segue blocco di codice con il frontmatter completo:
```
---
title: Identità — Aurora Sistemi S.p.A.
summary: Aurora Sistemi è la piattaforma SaaS italiana per la gestione intelligente del patrimonio immobiliare, fondata a Milano nel 2018
tags: [self, identita, azienda, hub]
status: active
created: 2026-06-10
updated: 2026-06-10
related: [[area-prodotto-engineering]], [[area-vendite]], [[area-customer-success]], [[area-marketing]], [[area-finance-operations]], [[area-p... [taglio a bordo destro]
---
# Identità — Aurora Sistemi S.p.A.

Hub centrale del cervello aziendale. Da qui si raggiungono i reparti (e, salendo dalle note di dettaglio, prodotti, clienti e KPI).

## In una frase
[riga tagliata dal bordo inferiore del frame, non leggibile]
```
Voce: *"Allora, mi dice Canon scritto in workspace. Canon e quindi lo avremo qui. Perfetto. Quindi se volessimo leggerlo, questo è il riassunto dei nostri documenti. Sette hub creati, uno self più 6 reparti."*
🔎 Le date `created`/`updated` (2026-06-10) e la coda del campo `related` oltre il quinto wikilink sono tagliate dal bordo destro del frame.

### Scena 183 · `frame-0778.png` · 77:42 — **`canon.md` aperto per intero, sezione "1. Identità"** ⭐
Doppio riquadro: a sinistra la stessa chat di Claude Code (con l'anteprima di `self-identita-aurora.md` e il messaggio "Fatto. Canon scritto in..."), a destra si è aperto l'editor con `workspace/canon.md` (percorso in alto: "workspace > canon.md > # CANON — Aurora Sistemi S.p.A."). Testo integrale leggibile:
```
# CANON — Aurora Sistemi S.p.A.

_File di lavoro. Estratto e riconciliato dalle 9 fonti in `sources/`. Nessun fatto inventato._
_Compilato: 2026-06-10._

---

## 1. Identità

- **Ragione sociale**: Aurora Sistemi S.p.A.
- **Anno di fondazione**: 2018, a Milano.
- **Fondatori**: Elena Ferraro (CEO) e Marco Bianchi (CTO), entrambi dal mondo dell'ingegneria degli impianti.
- **Missione**: rendere ogni edificio più efficiente, sicuro e sostenibile, dando a chi gestisce il patrimonio immobiliare un unico "cervello digitale" al posto di dieci sistemi scollegati.
- **Offerta**: piattaforma software SaaS in cloud per la gestione intelligente degli edifici. Un'unica interfaccia per tutti gli immobili: consumi energetici, manutenzioni, accessi e sicurezza, documenti.
- **Posizionamento**: "la piattaforma italiana per la gestione intelligente del patrimonio immobiliare". A differenza dei vecchi BMS (frammentati e legati all'hardware), Aurora è soluzione unica, in cloud, conforme al GDPR, con time-to-value in settimane.
- **Cliente ideale (ICP)**: organizzazioni che gestiscono patrimoni immobiliari medio-grandi in Italia, di norma dai 20 edifici in su — società di property & facility management, catene retail, pubblica amministrazione, sanità, banche. Interlocutore tipo: Facility Manager / Direttore Operations / Energy Manager.
- **Sedi**:
  - Milano — sede principale (HQ), Via Tortona 27.
```
(riga 17 "Milano — sede principale..." tagliata dal bordo inferiore del frame, il resto dell'elenco sedi non è leggibile qui)
Voce: *"Perfetto. Quindi se volessimo leggerlo, questo è il riassunto dei nostri documenti. Sette hub creati, uno self più 6 reparti."*

### Scena 184 · `frame-0779.png` · 77:48
Stessa vista della chat (senza il pannello canon.md aperto), con la frase "e gli 7 hub creat[i]" evidenziata in blu (selezione del mouse) all'interno del messaggio "Fatto. Canon scritto in `workspace/canon.md` e gli 7 hub creati (1 self + 6 reparti), tutti interconnessi senza link morti." Nessun contenuto nuovo rispetto alla scena 182, solo l'evidenziazione.
Voce: *"Quindi i reparti sappiamo che sono in areas, quindi perfetto, sono questi i reparti e poi abbiamo self. Eccolo qui."*

### Scena 185 · `frame-0781.png` · 78:00 — **hub di reparto `area-customer-success.md` aperto per intero** ⭐
Pannello destro ora mostra `area-customer-success.md` (percorso: "areas > area-customer-success.md"). Contenuto integrale:
```
title: Reparto — Customer Success
summary: Reparto che cura onboarding, supporto e crescita dei clienti esistenti, guidato da Giulia Rinaldi a Bologna.
tags: [areas, reparto, customer-success, hub]
status: active
created: 2026-06-10
updated: 2026-06-10
related:
  - "[[self-identita-aurora]]"
  - "[[area-vendite]]"
  - "[[area-prodotto-engineering]]"
---

# Reparto — Customer Success

Funzione continua responsabile di onboarding, supporto e crescita dei clienti esistenti di [[self-identita-aurora|Aurora Sistemi]]. È il motore della retention e dell'espansione (NRR 115% nel 2025).

- **A capo**: Giulia Rinaldi (Head of Customer Success), basata a Bologna.
- **Customer Success Manager**: Chiara Fontana, segue i key account (Banca Adriatica, Immobiliare Lombarda SGR).
- **Dimensione**: ~9 persone, concentrate a Bologna.

## Come lavora
Prende in carico i clienti chiusi da [[area-vendite]] e li fa crescere con l'upsell di nuovi moduli costruiti da [[area-prodotto-engineering]]. Nel 2025 ha guidato gli upsell chiave: Banca Adriatica (Access su tutte le filiali), Gruppo Retail (Energy) e Immobiliare Lombarda (Insights).
```
🔎 L'ultima riga visibile in fondo al frame è tagliata e di lettura incerta (sembra l'inizio di una didascalia in corsivo sul tipo di nota, tipo "_[Hub/Nota] di reparto. Le note di dettaglio su clienti e..._"): la parola iniziale non è leggibile con certezza, dichiarato invece di indovinare.
Voce: *"Benissimo. E vedete che ha già creato i reparti aziendali."*

### Scena 186 · `frame-0783.png` · 78:12 — **campo `related` selezionato (7 righe) nell'hub self-identita-aurora** ⭐
Torna la vista su `self-identita-aurora.md` nell'editor destro, con la riga `related:` evidenziata in blu (selezione), che mostra i wikilink: `[[area-prodotto-engineering]]`, `[[area-vendite]]`, `[[area-customer-success]]`, `[[area-marketing]]`, `[[area-finance-oper[ations]]`, `[[area-p...` (coda tagliata dal bordo destro). Sotto, il corpo della nota: "# Identità — Aurora Sistemi S.p.A.", "Hub centrale del cervello aziendale. Da qui si raggiungono i reparti (e, salendo dalle note di dettaglio, prodotti, clienti e KPI).", "## In una frase", "La piattaforma italiana per la gestione intelligente del patrimonio immobiliare: un unico "cervello digitale" in cloud al posto di dieci..." (continua oltre il bordo). In basso a destra della barra di stato, indicatore "7 lines selected".
Voce: *"solo per headsup ogni tanto, ed è il motivo per cui lo facciamo in questa maniera, ogni tanto il front e quindi lo yaml, che è questa sintassi qui, si rompe e quindi lo vedrete rosso."*

### Scena 187 · `frame-0786.png` · 78:30 — **Obsidian, prima apparizione: Graph view con canon orfano** ⭐
Cambio di applicazione: da Antigravity/Claude Code si passa a Obsidian. Sidebar Explorer a sinistra con le stesse cartelle (areas, code, concepts, data, docs, entities, outputs, projects, self, sources, workspace). Pannello principale: "Graph view" con nodi visibili e relative etichette: **canon** (in alto, isolato, con un piccolo pallino arancione accanto — segnalato come nodo separato/orfano), **area-finance-operations**, **area-prodotto-engineering**, **area-vendite**, **area-people-cultura**, **self-identita-aurora** (al centro del grappolo), **area-marketing**, **area-customer-success**. Le linee di collegamento formano una rete fitta tra i nodi delle aree e il nodo centrale self-identita-aurora, mentre "canon" resta separato in alto, senza linee visibili verso gli altri nodi.
Voce: *"Se andiamo in Obsidian, ora vedremo se si è rotto o meno. Vedete innanzitutto file eh ehm orfano che dicevamo che è il Canon e ce lo aspettiamo perché è un documento."*

### Scena 188 · `frame-0806.png` · 80:30 — **Notion, Prompt 4 completo: "Completa il cervello fino a circa 28 note"** ⭐
Notion, coda del Prompt 3 in alto ("Almeno 3 wikilink uscenti verso note reali...", "Nome del file unico in tutto il vault, con un prefisso di dominio: `self-identi[tà]`...", "## Ordine di costruzione (rispettalo)", punti 1-2, "Un wikilink punta solo a una nota che esiste già...", "Parti dagli hub. Mostrami `self-identita-aurora` prima di proseguire."). Sotto, titolo **"Prompt 4 — Completa il cervello fino a circa 28 note"**, sottotitolo *"Riempi tutte le cartelle, categoria per categoria, fermandoti intorno a 28 note di contenuto."* Riquadro del prompt, integrale:
> "Perfetto. Ora completa il resto del cervello, sempre con le stesse regole (nota atomica, frontmatter, related su una riga, almeno 3 wikilink reali, nomi unici).
>
> Genera le note mancanti, categoria per categoria, collegandole a ciò che già esiste:
> - data/: i KPI di fine 2025 (ARR totale, clienti attivi, churn, NRR, edifici);
> - concepts/: ARR, churn, efficienza energetica;
> - entities/: gli altri clienti, le persone coi ruoli, i tre prodotti, gli strumenti usati;
> - docs/, projects/, outputs/, code/: le procedure, i progetti in corso, i deliverable, gli script dell'azienda.
>
> I canali commerciali (LinkedIn, eventi, partner) NON sono cartelle: sono TAG (channel/linkedin), perché una stessa attività può valere per due canali e in cartella la duplicheresti.
>
> Fermati intorno a 28 note di contenuto, quante bastano per una demo che riempie il grafo. Alla fine dammi il conteggio per cartella."
Voce: *"andiamo nel nostro notion, prendiamo il nostro prompt numero 4 e gli diciamo 'Perfetto, ora fai tu e completa il cervello.' Ok, niente di pazzesco, lo troverete il prompt."*

### Scena 189 · `frame-0807.png` · 80:36
Antigravity/Claude Code: nella chat compare per intero il testo di `self-identita-aurora.md` (hub letto in precedenza) — "# Identità — Aurora Sistemi S.p.A.", "Hub centrale del cervello aziendale...", "## In una frase", "## Fatti di identità" (ragione sociale, fondazione, fondatori, missione, offerta, posizionamento, ICP, sedi, dipendenti — righe parzialmente troncate a destra), "## I sei reparti" con la lista numerata 1-6 dei wikilink `[[area-prodotto...]]`, `[[area-vendite...]]`, `[[area-customer...]]`, `[[area-marketing...]]`, `[[area-finance...]]`, `[[area-people...]]` (nomi completi tagliati dal bordo destro). Sotto, incorniciato in rosso, il Prompt 4 appena incollato nel campo di input, stessa formulazione della scena 188 fino a "...gli strumenti usati;" (il testo prosegue oltre il bordo inferiore del riquadro). Indicatore di stato in basso: "7 lines selected".
Voce: *"Ah, una cosa che ho messo che è interessante è ehm per i canali, dato che questa è un'azienda eh commerciali come LinkedIn Eventi, Partner eccetera, li voglio eh se li crea come tag,"*

### Scena 190 · `frame-0808.png` · 80:42 — **Prompt 4 espanso per intero ("Show less") + stato "Thinking.../Stuttering..."** ⭐
Il prompt inviato è ora mostrato per intero (pulsante "Show less" in basso a destra del riquadro), con anche la parte finale prima tagliata:
> "I canali commerciali (LinkedIn, eventi, partner) NON sono cartelle: sono TAG (channel/linkedin), perché una stessa attività può valere per due canali e in cartella la duplicheresti.
>
> Fermati intorno a 28 note di contenuto, quante bastano per una demo che riempie il grafo. Alla fine dammi il conteggio per cartella."

Sotto il riquadro, due righe di stato in corsivo: "Thinking..." e "Stuttering...". Campo di input vuoto "Queue another message...", chip "7 lines selected" ancora presente in basso.
Voce: *"perché più canali ehm o un'attività può essere collegata a più canali, no? E quindi, eh, dato che abbiamo il concetto di nota atomica, ora vi è molto più chiaro perché stiamo facendo questa cosa"*

### Scena 191 · `frame-0816.png` · 81:30 — **Claude spiega la strategia dei prefissi e comincia a scrivere le note prodotto** ⭐
Chat: contesto allegato `self-identita-aurora.md#3...`, prompt collassato ("Perfetto. Ora completa il resto del cervello, sempre con le stesse regole (nota atomica, frontmatter, related su una riga, almeno 3 wikilink reali, nomi unici)."), poi "Thought for 216s" e il messaggio di Claude:
> "Procedo con le note di dettaglio. Riuso i prefissi di dominio dei tuoi esempi (`cliente-`, `concetto-`, `kpi-`, e per coerenza `persona-`, `prodotto-`, `strumento-`, `doc-`, `progetto-`, `output-`, `code-`), ordino la creazione in modo che ogni `related` punti solo a note già scritte (zero link morti). I canali commerciali restano tag (`channel/...`), non cartelle.
> Scrivo tutto in un'unica passata (prodotti → concetti → KPI → persona → clienti → strumenti → docs/projects/outputs/code)."

Azioni seguenti: **Write `prodotto-aurora-core.md`** (18 righe), anteprima: "title: Prodotto — Aurora Core" / "summary: Modulo base della piattaforma: anagrafica edifici, dashboard unica, spazi e archivio documentale, su cui si appoggiano tutti gli altri m[oduli]" (taglio). Poi **Write `prodotto-aurora-energy.md`** (8 righe), anteprima parzialmente coperta dal riquadro "Queue another message..." in basso: "title: Prodotto — A[urora Energy]" (taglio).
Voce: *"Nel mentre che continua, volevo solo farvi vedere, vedete che ora lentamente stiamo spezzando le varie cose, prodotto, prodotto, concetto ARR."*

### Scena 192 · `frame-0818.png` · 81:42 — **`concetto-churn.md` aperto per intero: churn logo e gross, numeri Costruzioni Sud** ⭐
Pannello destro: `concetto-churn.md` (percorso "concepts > concetto-churn.md"), contenuto integrale:
```
title: Concetto — Churn
summary: La perdita di clienti (logo churn) o di fatturato (gross churn) in un periodo; in Aurora il 2025 ha visto un solo logo perso.
tags: [concepts, concetto, churn, metrica]
status: active
created: 2026-06-10
updated: 2026-06-10
related: [[concetto-arr]], [[area-customer-success]], [[area-finance-operations]]
---

# Concetto — Churn

Il **churn** misura quanto si perde. Due tagli:

- **Logo churn**: numero di clienti persi. In Aurora nel 2025 = 1 cliente (Costruzioni Sud, uscito a giugno dopo un'acquisizione) su 9 a inizio anno, ~11%.
- **Gross revenue churn**: [[concetto-arr|ARR]] perso. In Aurora = € 180.000, ~5,8% dell'ARR di inizio anno.

È il contraltare dell'espansione: [[area-customer-success]] lavora per minimizzarlo, [[area-finance-operations]] lo certifica. Obiettivo Board 2026: logo churn sotto il 10%.
```
Pannello sinistro (chat): sopra, coda della nota `prodotto-aurora-arr` ("title: Prodotto — ARR (Annual Recurring Revenue)" / "summary: Il fatturato ricorrente annuo; la metrica nord di Aurora,..." — taglio) poi le azioni **Write `concetto-churn.md`** (19 righe, stessa anteprima di cui sopra), **Write `concetto-efficienza-energetica.md`** (18 righe, anteprima: "title: Concetto — Efficienza energetica" / "summary: Ridurre sprechi e consumi degli edifici monitorando luce, ..." taglio), **Write `kpi-2025-arr.md`** (9 righe).
Voce: *"quello che sta succedendo letteralmente è il concetto di nota atomica, no? Quindi questo stiamo è quello che stiamo facendo e stiamo cominciando a spezzettare. Vedete che qua si popola un po' tutto quanto per arrivare ad avere un sistema interconnesso."*

### Scena 193 · `frame-0819.png` · 81:48 — **tab "Create 11 brain folders...", scrittura in serie dei 5 file KPI 2025** ⭐
Antigravity/Claude Code: sidebar Explorer a sinistra con l'albero "aurora cervello" espanso (areas, code, `concepts` con dentro `concetto-arr.md`, `concetto-churn...` selezionato in evidenza, `concetto-effic...`, poi data, docs, entities, outputs, projects, self, sources, workspace con `canon.md`). Tab attiva in alto: "Create 11 brain folders ..." con sottotitolo ripetuto "Create 11 brain folders in vault root". Pannello chat: in cima il contesto allegato `self-identita-aurora.md#3...` e il prompt collassato "Perfetto. Ora completa il resto del cervello, sempre con le stesse regole (nota atomica, frontmatter, related su una riga, almeno 3 wikilink reali, nomi unici)." Sotto, quattro azioni **Write** in sequenza, ciascuna con pallino e anteprima delle prime righe:
- **Write `kpi-2025-clienti-attivi.md`** (18 lines): "title: KPI 2025 — Clienti attivi" / "summary: A fine 2025 Aurora ha 9 clienti attivi, dopo l'ingresso di HotelLine e l'uscita di Costruzioni Sud."
- **Write `kpi-2025-churn.md`** (18 lines): "title: KPI 2025 — Churn" / "summary: Nel 2025 Aurora ha perso 1 cliente (logo churn ~11%) per € 180.000 di ARR (gross churn ~5,8%)."
- **Write `kpi-2025-nrr.md`** (19 lines): "title: KPI 2025 — NRR" / "summary: La Net Revenue Retention 2025 di Aurora è 115%; l'espansione sui clienti esistenti ha più che compensato il churn."
- **Write `kpi-2025-edifici.md`** (parzialmente coperta dal campo di input in basso, non leggibile oltre il titolo).

Campo di input in basso, incorniciato in rosso: "Esc to focus or unfocus Claude", con chip allegato `concetto-churn.md` e pulsante "Bypass permissions". In basso a destra dello schermo: "Screen Reader Optimized" e "Antigravity · Settings".
Voce: *"Ok, quindi qui mi dice cervello completato. Abbiamo nella parte self che c'è l'identità."* — Claude conferma di aver completato la generazione delle note mancanti (KPI compresi) e Joe verifica che l'hub `self-identita-aurora` sia il fulcro da cui tutto si collega.

### Scena 194 · `frame-0824.png` · 82:18 — **prima Graph view "piena" in Obsidian, decine di nodi tag+nota** ⭐
Cambio applicazione: Obsidian a schermo intero. Sidebar sinistra ridotta a sole icone (nessun Explorer aperto) più, sotto, l'albero cartelle in miniatura: areas, code, concepts, data, docs, entities, outputs, projects, self, sources, workspace. Pannello principale: "Graph view" (titolo in alto) con una nuvola fitta di decine di nodi bianchi (note) e verdi (tag, riconoscibili dal prefisso `#`), collegati da una rete di linee sottili molto densa attorno a un nodo centrale più grande, **self-identita-aurora**, e a un secondo nodo grande poco sopra, **area-customer-success**. Etichette leggibili con certezza: `#property-management`, `#founder`, **canon** (in alto a destra, isolato, senza linee visibili verso gli altri nodi), `kpi-2025-edifici`, `#efficienza-energetica`, `#ceo`, `#pitch-deck`, `#sales`, `#marketing`, `#prodotto`, `cliente-immobiliare-lombarda`, `prodotto-aurora-energy`, `#entities`, `#cliente`, `area-vendite`, `area-marketing`, `#operations`, `#finance`, `area-finance-operations`, `#churn`, `kpi-2025-churn`, `concetto-arr`, `concetto-churn`, `#report`, `#metrica`, `area-prodotto-engineering`, `#engineering`, `#hub`, `#azienda`, `2026`. Molte altre etichette (decine) sono presenti ma a risoluzione 1280×720 risultano troppo piccole per una lettura affidabile: dichiarato invece di indovinare.
Voce: *"Allora, se noi andassimo in Obsidian, quindi tornassimo qui, voglio mostrarvi... vedete che abbiamo la sfera che comincia lentamente a crearsi, no?"* — Joe passa da Antigravity a Obsidian per mostrare come il grafo delle relazioni ("la sfera") si stia infittendo mano a mano che le note vengono scritte, prima di andare a controllare la sezione KPI.

### Scena 195 · `frame-0848.png` · 84:42
Solo webcam a schermo intero (nessuno screen-share): Joe parla in camera, mano destra sollevata a gesticolare, sinistra chiusa a pugno. Sfondo: mensola con libri (dorsi viola/verde/blu, titoli non leggibili), pianta pensile, lampada accesa a destra.
Voce: *"immaginatela come se viaggiasse solo tra quei collegamenti nella nostra company Brain."* — Joe spiega che l'AI "viaggia" solo lungo i wikilink del vault, da cui l'importanza di non lasciare note isolate dal grafo.

### Scena 196 · `frame-0849.png` · 84:48
Ancora solo webcam. Joe ora tiene fra le dita, con entrambe le mani, una penna bianca (Apple Pencil) orizzontale davanti al microfono, sguardo verso l'obiettivo, bocca aperta a metà frase.
Voce: *"Quindi noi vogliamo avere file orfani? La risposta è no."* — pone la domanda retorica sui file orfani per introdurre la distinzione che segue.

### Scena 197 · `frame-0850.png` · 84:54
Solo webcam, inquadratura ravvicinata: Joe tiene la penna bianca quasi verticale tra pollice e indice di entrambe le mani, appena sotto il mento, sguardo fisso in camera.
Voce: *"Vogliamo avere file orfani a livello concettuale, ma non orfani a livello grafo, ok?"* — introduce la distinzione chiave: orfano "concettuale" (nessuno lo cita a voce) va bene, orfano "di grafo" (zero wikilink in entrata) no.

### Scena 198 · `frame-0851.png` · 85:00
Solo webcam, Joe con lo sguardo abbassato verso il basso a sinistra (fuori camera), penna non più visibile in mano, mano sinistra sollevata all'altezza del petto.
Voce: *"Perché vogliamo comunque che lei vada dentro."* — riferendosi all'AI, che deve poter "entrare" anche nelle note più marginali.

### Scena 199 · `frame-0852.png` · 85:06
Solo webcam, inquadratura frontale classica, bocca aperta a metà parola, mani non visibili (sotto il bordo inferiore del frame).
Voce: *"Per esempio, le note che avete preso in un meeting, ok? che magari le avete buttate lì a calcioni"* — porta l'esempio delle note di riunione salvate senza cura, come caso tipico di nota "orfana concettuale" che però deve restare raggiungibile dal grafo.

### Scena 200 · `frame-0853.png` · 85:12
Solo webcam, medesima inquadratura, Joe con la bocca socchiusa, sguardo dritto in camera, mano sinistra alzata poco visibile in basso a sinistra.
Voce: *"per capirci. Eh, vogliamo che queste siano all'interno, no, del tutto,"* — ribadisce che anche queste note "buttate lì" devono restare collegate al vault nel suo complesso.

### Scena 201 · `frame-0854.png` · 85:18
Solo webcam, Joe guarda in basso, penna bianca di nuovo visibile nella mano sinistra (bordo sinistro del frame), mano destra chiusa a pugno sollevata sul lato destro.
Voce: *"perché se per caso diciamo le AI, 'Hei, vai a vedere che cosa avevamo detto in quel meeting...'"* — costruisce lo scenario in cui l'utente chiede all'AI di recuperare informazioni da una nota di meeting specifica.

### Scena 202 · `frame-0855.png` · 85:24
Solo webcam, Joe con gli occhi chiusi ed espressione concentrata/smorfia, entrambe le mani sollevate ai lati del microfono in un gesto di apertura.
Voce: *"...perché c'era una roba interessante e magari non sono collegate a nulla, ok?"* — conclude l'esempio: se quella nota di meeting non è collegata a nulla, l'AI non ha modo di raggiungerla.

### Scena 203 · `frame-0856.png` · 85:30 — **dissolvenza incrociata: webcam → Graph view Obsidian** ⭐
Frame di transizione a metà dissolvenza: sopra, in trasparenza, resta visibile il volto di Joe (webcam) e sotto/dietro emerge già la Graph view di Obsidian, sufficientemente nitida da leggere quasi tutte le etichette. Sidebar sinistra: cartelle areas, code, concepts, **data** (espansa: `kpi-2025-arr`, `kpi-2025-churn`, `kpi-2025-clienti-attivi`, `kpi-2025-edifici`, `kpi-2025-nrr`), docs, entities, outputs, projects, self, sources, workspace. Nodi del grafo (tutti bianchi, nessun tag verde in questa vista): `code-export-crm`, `area-vendite`, `concetto-arr`, `concetto-efficienza-energetica`, `cliente-hotelline-hospitality`, `persona-marco-bianchi`, **area-customer-success** (nodo grande), `persona-elena-ferraro`, `area-marketing`, `strumento-crm`, `kpi-2025-churn`, `doc-onboarding-cliente`, `persona-chiara-fontana`, `prodotto-aurora-energy`, `nota-collegata-2`, `area-prodotto-engineering`, `cliente-banca-adriatica`, `progetto-arr-6m-2026`, `area-finance-operations`, `concetto-churn`, `cliente-immobiliare-lombarda`, `output-pitch-deck-vendita`, `kpi-2025-edifici`, `kpi-2025-arr`, `kpi-2025-nrr`, `area-people-cultura`, **self-identita-aurora** (nodo centrale grande), `persona-giulia-rinaldi`, `prodotto-aurora-core`, `kpi-2025-clienti-attivi`, `nota-collegata-1`, `_template-nota`, `canon`, `prodotto-aurora-accesso`.
Voce: *"noi non avremo modo di accedervi, quindi dobbiamo instaurare ora una specie di..."* — mentre lo schermo passa dalla webcam al grafo, Joe introduce la soluzione al problema appena posto (l'accesso alle note isolate).

### Scena 204 · `frame-0857.png` · 85:36 — **Graph view Obsidian a piena leggibilità, tutti i 33 nodi identificati** ⭐
Dissolvenza completata: solo Obsidian a schermo, webcam ridotta al riquadro in basso a sinistra. Stessa Graph view della scena precedente ora completamente nitida, stessi 33 nodi elencati sopra confermati uno per uno (nessuna etichetta dubbia in questo frame). `canon` e `nota-collegata-1` risultano visivamente più periferici/in basso nel grafo rispetto al grosso grappolo centrale, ma non è possibile determinare con certezza dal solo frame se abbiano linee di collegamento entranti: dichiarato invece di indovinare. ➕ (inferenza, coerente col discorso in corso) a questo punto della registrazione `canon` dovrebbe essere ancora il nodo orfano già segnalato nella scena 187, poiché la soluzione (l'indice `_index`) non è ancora stata introdotta nel progetto.
Voce: *"...stratagemma per collegare tutti gli orfani. Questo si chiamerà SL/index e volevo farvelo vedere ora..."* — Joe annuncia il nome della tecnica che sta per introdurre: un file "SL/index" (slash-index, cioè `_index`) presente in ogni cartella per agganciare le note altrimenti isolate.

### Scena 205 · `frame-0865.png` · 86:24 — **`workspace/canon` aperto per intero: le sezioni "1. Identità" e "2. Prodotti"** ⭐
Obsidian, editor a piena vista: percorso "workspace / canon" in alto. Sidebar: cartella **workspace** espansa con `_template-nota` e **canon** (selezionato, evidenziato). Corpo della nota, sezione "1. Identità" con elenco puntato integrale:
- **Ragione sociale**: Aurora Sistemi S.p.A.
- **Anno di fondazione**: 2018, a Milano.
- **Fondatori**: Elena Ferraro (CEO) e Marco Bianchi (CTO), entrambi dal mondo dell'ingegneria degli impianti.
- **Missione**: rendere ogni edificio più efficiente, sicuro e sostenibile, dando a chi gestisce il patrimonio immobiliare un unico "cervello digitale" al posto di dieci sistemi scollegati.
- **Offerta**: piattaforma software SaaS in cloud per la gestione intelligente degli edifici. Un'unica interfaccia per tutti gli immobili: consumi energetici, manutenzioni, accessi e sicurezza, documenti.
- **Posizionamento**: "la piattaforma italiana per la gestione intelligente del patrimonio immobiliare". A differenza dei vecchi sistemi BMS (frammentati e legati all'hardware), Aurora è soluzione unica, in cloud, conforme al GDPR, con time-to-value in settimane.
- **Cliente ideale (ICP)**: organizzazioni che gestiscono patrimoni immobiliari medio-grandi in Italia, di norma dai 20 edifici in su — società di property & facility management, catene retail, pubblica amministrazione, sanità, banche. Interlocutore tipo: Facility Manager / Direttore Operations / Energy Manager.
- **Sedi**: Milano — sede principale (HQ), Via Tortona 27. Bologna — secondo ufficio dal 2022, dove si trova buona parte del team di Customer Success.
- **Dipendenti**: 47 persone (organico confermato dal Board a fine 2025).

Segue "2. Prodotti" con l'inizio di una tabella (Prodotto | Tipo | Cosa fa): riga "Aurora Core | Base | Cuore della piattaforma. Anagrafica di tutti gli edifici (metratura, destinazione d'uso, impianti, contratti), dashboard unica, gestione spazi e planimetrie, archivio documentale (certificazioni, contratti, collaudi). Tutti gli altri moduli si a..." (tagliata dal bordo inferiore). Barra di stato in basso a destra: "0 backlinks · 942 words · 7,192 characters".
Voce: *"...non c'è nessuno che va a parlare con il nostro Canon e il problema non è quante diramazioni abbiamo, ma è quanti file riferiscono alla nostra nota, vogliamo che il nostro index e la nostra nota siano collegati tra di loro,"* — Joe apre proprio `canon.md` per mostrare dal vivo il caso concreto: **0 backlinks** in basso conferma che, a questo punto, nessuna nota rimanda ancora al Canon.

### Scena 206 · `frame-0868.png` · 86:42 — **annotazione a penna verde sul sidebar: "index" con freccia verso `canon`** ⭐
Graph view di Obsidian (stessi nodi delle scene 203-204, disposizione leggermente diversa). Sopra il riquadro sidebar, tracciato a mano con la penna/Apple Pencil in verde acceso: la scritta corsiva **"index"** e una freccia curva che parte da sotto e punta verso l'alto/verso la scritta, posizionata esattamente accanto alla cartella **workspace** (espansa: `_template-nota`, `canon`) nella sidebar. Nodi del grafo leggibili: `kpi-2025-churn`, `concetto-churn`, `nota-collegata-2`, `output-pitch-deck-vendita`, `area-finance-operations`, `kpi-2025-nrr`, `prodotto-aurora-core`, `doc-onboarding-cliente`, `_template-nota`, `concetto-efficienza-energetica`, `prodotto-aurora-accesso`, **area-customer-success**, `persona-giulia-rinaldi`, `cliente-banca-adriatica`, `kpi-2025-edifici`, `area-prodotto-engineering`, **self-identita-aurora** (centrale), `cliente-immobiliare-lombarda`, `area-marketing`, `area-vendite`, `kpi-2025-clienti-attivi`, `prodotto-aurora-energy`, `concetto-arr`, `kpi-2025-arr`, `persona-chiara-fontana`, `strumento-crm`, `area-people-cultura`, `progetto-arr-6m-2026`, `persona-elena-ferraro`, `canon`, `persona-marco-bianchi`, `code-export-crm`, `cliente-hotelline-hospitality`, `nota-collegata-1`. Il nodo `canon` è visibile isolato in basso a destra del grappolo centrale.
Voce: *"perché questo fa sì che non ci siano orfani scollegati e che quindi lei possa entrare e cominciare a vedere anche queste note."* — mentre annota "index" sulla cartella workspace, Joe collega visivamente il concetto appena spiegato (il file `_index` per cartella) al nodo `canon` ancora isolato nel grafo.

### Scena 207 · `frame-0870.png` · 86:54
Solo webcam a schermo intero, nessuno screen-share. Joe con mano sinistra sollevata a mezz'aria, dita leggermente chiuse a pinza attorno alla penna bianca (Apple Pencil, appena visibile), sguardo verso il basso a sinistra, bocca aperta a metà parola.
Voce: *"Di nuovo, noi non useremo il grafico perché il grafo sarà per l'AI, ma noi dobbiamo sapere leggere cosa va male nel grafico..."* — Joe chiarisce che il Graph view non è uno strumento di lavoro quotidiano per l'utente umano (quello è per l'AI), ma resta utile per diagnosticare visivamente le note isolate o mal collegate.

### Scena 208 · `frame-0871.png` · 87:00
Solo webcam del presentatore (nessun contenuto a schermo condiviso): mano destra sollevata all'altezza del volto con in mano lo stilo/pennino bianco (Apple Pencil), sguardo basso verso il microfono, espressione pensierosa.
Voce: *"il grafico perché il grafo sarà per l'AI, ma noi dobbiamo sapere leggere"*

### Scena 209 · `frame-0872.png` · 87:06
Solo webcam: il presentatore abbassa lo stilo tenendolo con due dita, bocca aperta a metà frase, sguardo rivolto verso il basso/verso la telecamera in transizione.
Voce: *"cosa va male nel grafico e capire come possiamo migliorarlo di modo tale che"*

### Scena 210 · `frame-0873.png` · 87:12
Solo webcam: inquadratura frontale ferma, mani non visibili, espressione neutra/attenta mentre parla.
Voce: *"l'AI possa utilizzarlo nel migliore dei modi, no? Quindi oltre ai nostri prompt"*

### Scena 211 · `frame-0874.png` · 87:18
Solo webcam: pugno chiuso con lo stilo sollevato sopra la spalla sinistra, gesto enfatico ad accompagnare la spiegazione.
Voce: *"abbiamo anche una maniera visiva e il toggle, no, trova gli orfani per far sì che riusciamo a vederli."*

### Scena 212 · `frame-0875.png` · 87:24 — **Obsidian, Graph view completo con cartella `data` espansa (44 note)** ⭐
Cambio di schermata: da webcam a schermo condiviso Obsidian, con webcam del presentatore ridotta a riquadro in basso a sinistra (PIP). Sidebar Explorer a sinistra con le cartelle del vault, in ordine: `areas`, `code`, `concepts`, **`data`** (espansa, mostra 5 file: `kpi-2025-arr`, `kpi-2025-churn`, `kpi-2025-clienti-attivi`, `kpi-2025-edifici`, `kpi-2025-nrr`), `docs`, `entities`, `outputs`, `projects`, `self`, `sources`, **`workspace`** (espansa, mostra `_template-nota` e `canon`). Cursore del mouse posizionato sul nodo `prodotto-aurora-core` nel pannello grafo.
Pannello principale "Graph view" con una rete fitta di nodi etichettati, tra cui: `kpi-2025-churn`, `concetto-churn`, `nota-collegata-2`, `output-pitch-deck-vendite`, `area-finance-operations`, `kpi-2025-nrr`, `prodotto-aurora-core`, `concetto-efficienza-energetica`, `prodotto-aurora-access`, `doc-onboarding-cliente`, `_template-nota`, `area-customer-success` (nodo grande, molto connesso), `persona-giulia-rinaldi`, `cliente-banca-adriatica`, `kpi-2025-edifici`, `area-prodotto-engineering`, `self-identita-aurora` (nodo grande centrale), `cliente-immobiliare-lombarda`, `persona-chiara-fontana`, `kpi-2025-arr`, `area-marketing`, `area-vendite`, `kpi-2025-clienti-attivi`, `prodotto-aurora-energy`, `concetto-arr`, `nota-collegata-1`, `strumento-crm`, `area-people-cultura`, `progetto-arr-fin-2026`, `persona-elena-ferraro`, `canon`, `persona-marco-bianchi`, `code-export-crm`, `cliente-hoteline-hospitality`. `canon` appare qui integrato nel grafo (non piu' isolato come nella scena 187 di `_parte-178-204.md`).
Voce: *"cominceremo e lo faremo, però era solo una premessa che volevo farvi."*

### Scena 213 · `frame-0876.png` · 87:30 — **Antigravity/Claude Code: report "Regole rispettate" + "Tre cose da segnalarti" (44 note)** ⭐
Editor Antigravity, tab "Create 11 brain work fol..." con titolo pagina "Create 11 brain work folders in vault". Sidebar Explorer: root `aurora cervello`, cartelle `areas`, `code`, `concepts`, `data`, `docs`, `entities`, `outputs`, `projects`, `self`, `sources`, `workspace` (espansa: `_template-nota...`, `canon.md`). Webcam del presentatore in basso a sinistra (PIP).
Chat: contesto allegato `self-identita-aurora.md#3...`, messaggio utente "Perfetto. Ora completa il resto del cervello, sempre con le stesse regole (nota atomica, frontmatter, related su una riga, almeno 3 wikilink reali, nomi unici)." Sopra, riga tagliata dal bordo superiore: "sources/ 0 (vuota nel vault: il grezzo sta sul desktop)" poi "Totale contenuto 30" poi "Più `workspace/canon.md` (il file di lavoro, non una nota atomica)." Segue la risposta di Claude, trascritta integralmente:
```
Regole rispettate
- Ogni nota: una sola idea, frontmatter completo (title, summary, tags, status, created, updated, related), primo tag = nome cartella, ≥3 wikilink uscenti a note reali e uniche.
- Ordine di creazione studiato perché ogni related punti solo a note già esistenti: zero link morti, zero orfani.
- Canali commerciali come tag, non cartelle: channel/referral (Immobiliare Lombarda), channel/eventi (pitch deck, progetto ARR).
- Numeri coerenti col canon: somma ARR clienti = 3,84M, somma immobili = 751.

Tre cose da segnalarti
1. "Tre prodotti" vs cinque. Mi hai chiesto i tre prodotti, ma nel canon ce ne sono cinque (Core, Energy, Manutenzione, Access, Insights). Ho creato i 3 più centrali per la demo (Core, Energy, Access). Vuoi che aggiunga anche Manutenzione e Insights? Sono +2 note.
2. Selezione su persone e clienti. Per restare intorno a 28 ho messo 4 persone (su 11) e 3 clienti attivi (su 9). Se la demo ti serve più "popolata", dimmelo e completo gli altri.
3. Il linter di Obsidian riscrive related. Avevo scritto il campo su una riga sola come da regola, ma il tuo linter lo converte in lista YAML multi-riga (l'hai già visto sugli hub). In questo vault la regola "una riga fisica" non regge a causa di quel tool: se ti serve davvero il formato a riga singola, va disattivata la relativa regola del linter.
```
Campo di input in basso: placeholder "Esc to focus or unfocus Claude", allegato `self-identita-aurora.md`, pulsante rosso "Bypass permissions". Barra di stato: "Screen Reader Optimized", "Antigravity - Settings".
Voce: *"Quindi ora andremo nel nostro eh company Brain e gli diremo: "Hei, ora ho bisogno di un ulteriore aggiunta". Allora, analizza bene com'è strutturato il progetto, ok? analizza tutte le cartelle"*

### Scena 214 · `frame-0886.png` · 88:30 — **Prompt "aggiungi un `_index`" inviato, Claude in elaborazione ("Thinking...")** ⭐
Stessa chat, scorsa più in basso. Contesto allegato `self-identita-aurora.md`. Messaggio utente integrale (con `_index` evidenziato in blu, selezionato):
> "Hey, ora ho bisogno di un'ulteriore aggiunta. Analizza bene la struttura del progetto: analizza tutte le cartelle, anche quelle che hai in conversazione, e assicurati di avere tutto documentato. In particolare, assicurati di avere:
> - un front matter
> - un indice (un `_index`) che possa evitare note orfane all'interno del progetto
> Ti posso chiedere di introdurre questo indice in ogni cartella, o dove meglio ritieni opportuno?"

Sotto, righe di stato: "Thinking... · 64 tokens" e una seconda riga parzialmente tagliata dal riquadro di input ("...onking..."). Campo di input in basso: "Queue another message...", allegato `self-identita-aurora.md`, pulsante "Bypass permissions" ora con icona quadrata rossa (generazione in corso, stoppabile). Sidebar invariata rispetto alla scena 213.
Voce: *"perfetto, ha capito esattamente quello che volevo fare e ora eh metteremo questa piccola chicca, appunto, per quello che vi ho appena spiegato."*

### Scena 215 · `frame-0888.png` · 88:42 — **Risposta di Claude: "44 file .md, tutti con frontmatter — zero senza", 2 scoperte sul template** ⭐
Chat scorsa oltre il prompt della scena 214. Riquadro di output del comando eseguito, trascritto integralmente:
```
OUT File .md totali: 44
    Senza frontmatter: NESSUNO
    Link rotti (escluso template): NESSUNO
```
Poi la risposta di Claude (con la prima riga del "Risultato finale" evidenziata in blu, selezionata):
```
● Fatto. Grafo chiuso e verificato.

Risultato finale
- 44 file .md, tutti con frontmatter — zero senza.
- Zero link rotti, zero note orfane (escluso il template, che è uno scaffold per definizione fuori dal grafo).

Cosa ho aggiunto
- Un _index in ogni cartella (11) + un indice madre _index-aurora.md alla radice → unico punto d'ingresso, grafo navigabile dall'alto: madre → indice di cartella → nota. Ogni nota ora riceve almeno un link entrante dal suo indice.
- Nomi unici (_index-<cartella>) per non rompere la risoluzione wikilink di Obsidian.
- Frontmatter aggiunto a canon.md, che ne era privo.

Due scoperte importanti durante l'analisi (te le segnalo perché cambiano le regole che mi avevi dato prima):
1. Ho trovato il tuo _template-nota.md in workspace/: è la fonte vera delle regole di frontmatter del vault, e spiega perché il linter riscriveva le mie note. Le regole reali sono: related a blocco con wikilink fra virgolette (non più "una riga sola"), title/summary sempre fra virgolette doppie, anni come tag annidati anno/2025. Ho riallineato tutti i 12 indici a questo template (erano appena creati, non ancora linterati).
2. La regola "related su una riga" che mi avevi dato nei turni precedenti è di fatto superata dal template: erano in conflitto, e il linter (col template che si applica) vince. Da...
```
🔎 Il punto 2 prosegue oltre il bordo inferiore, coperto dal riquadro "Esc to focus or unfocus Claude": testo non leggibile da qui in avanti.
Sidebar Explorer: root troncato "aurora...", stesse 11 cartelle, `workspace` ora mostra solo `_index-aurora.md` (evidenziato/selezionato in blu). Campo di input: allegato `_index-workspace.md`, pulsante "Bypass permissions" ancora rosso.
Voce: *"Molto bene, abbiamo 44 file ora MD, zero link rotti, abbiamo un index in ogni cartella"*

### Scena 216 · `frame-0890.png` · 88:54 — **Split screen: chat a sinistra + `_index-outputs.md` aperto a destra (frontmatter e corpo integrali)** ⭐
Vista divisa in due pannelli. Sinistra: stessa chat della scena 215 (risposta di Claude "Fatto. Grafo chiuso e verificato." con lo stesso "Risultato finale" e le stesse "Due scoperte importanti"). Destra: nuovo pannello con il file `_index-outputs.md` aperto, breadcrumb in alto "outputs › _index-outputs.md › ...". Contenuto del file, trascritto integralmente:
```
---
title: "Indice — outputs"
summary: "Mappa dei deliverable prodotti da Aurora."
tags: [outputs, index, moc]
status: active
created: 2026-06-10
updated: 2026-06-10
related:
  - "[[output-pitch-deck-vendite]]"
  - "[[area-marketing]]"
  - "[[self-identita-aurora]]"
---

# Indice — outputs

La cartella `outputs/` contiene i deliverable concreti.

## Note
- [[output-pitch-deck-vendite]] — pitch deck commerciale, agg. dicembre 2025.

## Salendo
- Indice madre: [[_index-aurora]]
- Reparti proprietari: [[area-marketing]], [[area-vendite]]
```
Sidebar Explorer sinistra: root "aurora...", cartella `outputs` evidenziata/selezionata, stesse 11 cartelle sotto. Barra di stato in basso: "Screen Reader Optimized", "Antigravity - Settings".
Voce: *"e vediamo ora che abbiamo i vari index, no, che fanno riferimento adesso al nostro index workspace."*

### Scena 217 · `frame-0892.png` · 89:06 — **Obsidian, Graph view con gli `_index` di ogni cartella e `_index-aurora` come hub** ⭐
Torna la vista Obsidian a schermo intero (niente PIP webcam in questo frame). Sidebar Explorer: stesse 11 cartelle (`areas`, `code`, `concepts`, `data`, `docs`, `entities`, `outputs`, `projects`, `self`, `sources`, `workspace`), tutte collassate.
Pannello "Graph view": rispetto alla scena 212 compaiono ora i nuovi nodi indice, riconoscibili dal prefisso `_index-`: `_index-concepts`, `_index-data`, `_index-self`, `_index-docs`, `_index-outputs`, `_index-areas`, `_index-workspace`, `_index-sources`, `_index-code`, `_index-projects`, `_index-entities`, oltre al nodo centrale `_index-aurora` posizionato tra `area-vendite` e `self-identita-aurora`. Nodi già visti in scena 212 restano presenti: `concetto-churn`, `kpi-2025-churn`, `nota-collegata-2`, `prodotto-aurora-access`, `output-pitch-deck-vendite`, `area-finance-operations`, `kpi-2025-nrr`, `doc-onboarding-cliente`, `prodotto-aurora-core`, `_template-nota`, `area-customer-success` (nodo grande), `persona-giulia-rinaldi`, `concetto-efficienza-energetica`, `cliente-banca-adriatica`, `area-prodotto-engineering`, `cliente-immobiliare-lombarda`, `kpi-2025-arr`, `persona-chiara-fontana`, `area-vendite`, `prodotto-aurora-energy`, `concetto-arr`, `kpi-2025-edifici`, `area-marketing`, `nota-collegata-1`, `self-identita-aurora` (nodo grande centrale), `strumento-crm`, `area-people-cultura`, `persona-elena-ferraro`, `canon`, `persona-marco-bianchi`, `cliente-hoteline-hospitality`, `kpi-2025-clienti-attivi`. Il nodo `canon` risulta ora collegato alla rete (non più isolato).
Voce: *"E come vedete ora abbiamo il collegamento a Canon. Quindi questo vuol dire che se noi andiamo qui ora il nostro Canon non è più una nota orfana e quindi abbiamo fatto tutto come si deve"*

### Scena 218 · `frame-0897.png` · 89:36 — **Cambio app: Excalidraw, canvas quasi vuoto** ⭐
Browser su `excalidraw.com`. Barra strumenti in alto: icona lucchetto/mano, freccia di selezione, gomma, rettangolo, rombo, ellisse, freccia, linea, matita/disegno libero (evidenziata in blu, strumento attivo), testo "A", immagine, cornice, altri strumenti "...". In alto a destra: menu "Excalidraw" con dropdown, pulsante viola "Share", icona quadrata (menu principale). Barra indirizzo browser: lucchetto, `excalidraw.com`, icone estensioni (cerchi colorati blu/rosso/altro), stella (preferiti), icona profilo.
Pannello proprietà a sinistra: **Stroke** (nero selezionato, poi rosso, verde, blu, arancione, bianco), **Background** (trasparente selezionato, poi rosa, verde, blu, giallo, trasparente), **Stroke width** (spessore grosso/bold selezionato in blu), **Opacity** (slider al 100), **Layers** (4 icone: invia al fondo, invia indietro, porta avanti, porta in primo piano).
Canvas: quasi completamente vuoto, solo un piccolo scarabocchio nero (una curva/linea disegnata a mano libera) in alto a sinistra del centro. 🔎 Sopra lo scarabocchio, una scritta piccola e grigia in alto al centro del canvas non è leggibile con certezza (probabile hint di editor tipo "Click and drag..."), dichiarato invece di indovinare. In basso al centro, tooltip "Scroll back to content". Webcam del presentatore in basso a sinistra (PIP).
Voce: *"fatemi andare su Excalidro. Ora noi abbiamo la nostra AI, abbiamo cominciato a fare il nostro cervello, però abbiamo che cosa? Abbiamo per ora fatto una"*

### Scena 219 · `frame-0926.png` · 92:30 — **Notion, pagina "Company Brain — Tutti i prompt": coda Prompt 4 + intestazione "Passo 3"** ⭐
Notion. Sidebar sinistra: 🏠 Home, "Meetings" (Connect your calendar, New AI meeting note), "Recents" (Clienti, Cruscotto Aurora, **Company Brain — Tutti i prom...** evidenziata/attiva, New page, Reparti, Prodotti, Default view, KPI mensili, Sedi, Competitor), "Agents" (New agent), "Shared". Tab pagina: "Company Brain — Tutti i prompt del..." con tag "🔒 Privato", in alto a destra "Aa Translate to English", "Share".
Contenuto (coda del Prompt 4, già documentato per intero in `_parte-178-204.md` scena 188/190): "Riempi tutte le cartelle, categoria per categoria, fermandoti intorno a 28 note di contenuto." poi, in riquadro scuro, il testo integrale del Prompt 4:
> "Perfetto. Ora completa il resto del cervello, sempre con le stesse regole (nota atomica, frontmatter, related su una riga, almeno 3 wikilink reali, nomi unici).
> Genera le note mancanti, categoria per categoria, collegandole a ciò che già esiste:
> - data/: i KPI di fine 2025 (ARR totale, clienti attivi, churn, NRR, edifici);
> - concepts/: ARR, churn, efficienza energetica;
> - entities/: gli altri clienti, le persone coi ruoli, i tre prodotti, gli strumenti usati;
> - docs/, projects/, outputs/, code/: le procedure, i progetti in corso, i deliverable, gli script dell'azienda.
> I canali commerciali (LinkedIn, eventi, partner) NON sono cartelle: sono TAG (channel/linkedin), perché una stessa attività può valere per due canali e in cartella la duplicheresti.
> Fermati intorno a 28 note di contenuto, quante bastano per una demo che riempie il grafo. Alla fine dammi il conteggio per cartella."

Sotto, nuova intestazione: **"Passo 3 — Gate di qualità, indice per le AI, showcase, grafo, GitHub"**, sottotitolo **"Prompt 5 — Il gate di qualità (solo referto)"**, descrizione: *"Controlla ogni nota contro le sei regole e ti restituisce solo il referto."* Segue l'inizio di un nuovo riquadro scuro (prompt), parzialmente tagliato in basso: "Crea un link python che faccia 'a gate di qualita' sul cervello di Aurora. Passa 11 cartelle (salta solo sources/ e workspace/, che sono materiale grezzo e scratc[h]..." (taglio a fondo pagina).
Voce: *"Quindi, come già sappiamo Notion e ora abbiamo eccoci qua, il nostro ehm"*

### Scena 220 · `frame-0927.png` · 92:36 — **Prompt 5 completo (6 regole) + Prompt 6 "Correggi e ripeti finché esce 0 errori"** ⭐
Stessa pagina Notion, scorsa più in basso. Coda del Prompt 4 ("cartella la duplicheresti." / "Fermati intorno a 28 note di contenuto..."), poi intestazione "Passo 3 — Gate di qualità, indice per le AI, showcase, grafo, GitHub", "Prompt 5 — Il gate di qualità (solo referto)", descrizione "Controlla ogni nota contro le sei regole e ti restituisce solo il referto." Riquadro del prompt, ora leggibile per intero:
> "Crea un link python che faccia 'a gate di qualita' sul cervello di Aurora. Passa 11 cartelle (salta solo sources/ e workspace/, che sono materiale grezzo e scratch) e controllala contro queste sei regole:
> 1. Frontmatter completo: title, summary, tags, status, created, updated.
> 2. Massimo 300 righe di corpo per nota.
> 3. Almeno 3 wikilink [[...]] in uscita verso note che esistono davvero (conta i bersagli unici, non lo stesso link ripetuto; gli _index non valgono).
> 4. Zero link rotti: ogni [[bersaglio]] punta a una nota che esiste.
> 5. Zero orfani: ogni nota ha almeno 1 link in ENTRATA (gli _index sono esentati).
> 6. Una sola componente connessa: tutto il grafo è un unico grappolo, non due iso[le]..." (parola finale tagliata dal bordo destro, presumibilmente "isole")
>
> "Elenca gli errori nota per nota, raggruppati per regola. Se è tutto in regola, rispondi solo: "OK, 0 errori". Per ora non correggere niente, dammi solo il refer[to]." (coda tagliata dal bordo destro)

Sotto, nuova intestazione: **"Prompt 6 — Correggi e ripeti finché esce "0 errori""**, descrizione: *"Il ciclo correttivo: l'AI sistema ciò che ha segnalato, rifà il gate, e ripete fino a zero."* In basso, tooltip overlay "Copied code to clipboard" (il presentatore ha appena copiato il blocco del Prompt 5). Riquadro del Prompt 6 appena visibile al fondo, prima riga: "Correggi le note che hai segnalato, applicando le regole del gate:" (taglio).
Voce: *"il nostro prompt. Allora, ehm, ora gli diremo"*

### Scena 221 · `frame-0928.png` · 92:42 — **Torna Antigravity: campo di input evidenziato in rosso, pronto a ricevere il Prompt 5** ⭐
Editor Antigravity, stessa chat/tab "Create 11 brain work fol..." vista nelle scene 213-216, ora scorsa fino alla fine della risposta precedente di Claude: "Scope: ho indicizzato solo il vault Aurora. Le directory `.claude/` e `.claude/plans` viste in sessione sono config dello strumento, non parte del cervello: lasciate fuori." poi "Vuoi che fissi `_index-aurora` come nota home (impostazione di Obsidian) o lo lasci a te?" Sidebar Explorer: cartella `workspace` espansa con `_index-workspa...`, `_template-nota...`, `canon.md`, `_index-aurora.md`.
Il campo di input in basso ha ora il bordo evidenziato in rosso/arancione (focus attivo) con il cursore lampeggiante sul placeholder "Esc to focus or unfocus Claude"; allegato `_index-workspace.md`, pulsante "Bypass permissions" con icona quadrata rossa.
Voce: *"diremo"*

### Scena 222 · `frame-0929.png` · 92:48 — **Prompt 5 incollato nel campo di Antigravity, testo riformulato a voce ("Passa al setaccio OGNI nota")** ⭐
Stessa schermata, il campo di input rosso ora contiene il testo incollato/dettato, trascritto per intero fin dove visibile (taglio in fondo al riquadro):
```
Crea un link python che faccia "a gate di qualita' sul cervello di Aurora. Passa al setaccio OGNI nota delle
11 cartelle (salta solo sources/ e workspace/, che sono materiale grezzo e scratch)
e controllala contro queste sei regole:

1. Frontmatter completo: title, summary, tags, status, created, updated.
2. Massimo 300 righe di corpo per nota.
3. Almeno 3 wikilink [[...]] in uscita verso note che esistono davvero (conta i
   bersagli unici, non lo stesso link ripetuto; gli _index non valgono).
4. Zero link rotti: ogni [[bersaglio]] punta a una nota che esiste.
5. Zero orfani: ogni nota ha almeno 1 link in ENTRATA (gli _index sono esentati).
```
🔎 Il testo qui differisce lievemente dal Prompt 5 di Notion (scena 220): l'ordine "Passa 11 cartelle... e controllala" diventa "Passa al setaccio OGNI nota delle 11 cartelle... e controllala", coerente con la formulazione a voce del presentatore piuttosto che con la copia esatta da Notion. La regola 6 non è visibile in questo frame (tagliata sotto il bordo del riquadro). Sopra il riquadro resta visibile la stessa risposta di Claude della scena 221 ("Scope: ho indicizzato solo il vault Aurora...", "Vuoi che fissi `_index-aurora` come nota home...").
Voce: *"questo. Allora, crea un link Python. Ehm, un link, uno script. Cosa ho scritto?"*

### Scena 223 · `frame-0937.png` · 93:36 — **chat Antigravity: le due scoperte sul `_template-nota.md` e la domanda su `_index-aurora` come nota home** ⭐
Antigravity a schermo intero (IDE indicato in basso a destra come "Antigravity · Settings"), webcam ridotta al riquadro in basso a sinistra. Sidebar Explorer: root **aurora cervello** con le cartelle areas, code, concepts, data, docs, entities, outputs, projects, self, sources, **workspace** (espansa: `_index-workspa...`, `_template-nota...`, `canon.md`, e a livello radice `_index-aurora.md`). Tab in alto: "Create 11 brain work fol..." con sottotitolo "Create 11 brain work folders in vault". Due blocchi di chat visibili per intero:
- Blocco con chip **`self-identita-aurora.md`**: "Hey, ora ho bisogno di un'ulteriore aggiunta. Analizza bene la struttura del progetto: analizza tutte le cartelle, anche quelle che hai in conversazione, e assicurati di avere tutto documentato. In particolare, assicurati di avere: · Nomi unici (`_index-<cartella>`) per non rompere la risoluzione wikilink di Obsidian. · Frontmatter aggiunto a `canon.md`, che ne era privo. Due scoperte importanti durante l'analisi (te le segnalo perché cambiano le regole che mi avevi dato prima): 1. Ho trovato il tuo `_template-nota.md` in `workspace/`: è la fonte vera delle regole di frontmatter del vault, e spiega perché il linter riscriveva le mie note. Le regole reali sono: `related` a blocco con wikilink fra virgolette (non più "una riga sola"), `title`/`summary` sempre fra virgolette doppie, anni come tag annidati `anno/2025`. Ho riallineato tutti i 12 indici a questo template (erano appena creati, non ancora linterati). 2. La regola "`related` su una riga" che mi avevi dato nei turni precedenti è di fatto superata dal template: erano in conflitto, e il template (col linter che lo applica) vince. Da ora seguo quello. Scope: ho indicizzato solo il vault Aurora. Le directory `.claude/` e `.claude/plans/` viste in sessione sono config dello strumento, non parte del cervello: lasciate fuori. Vuoi che fissi `_index-aurora` come nota home (impostazione di Obsidian) o lo lasci a te?"
- Blocco con chip **`_index-workspace.md`**: "Crea uno script python che faccia da gate di qualità sul cervello di Aurora. Passa al setaccio OGNI nota delle 11 cartelle (salta solo `sources/` e `workspace/`, che sono materiale grezzo e scratch)" — poi il testo prosegue in grigio sbiadito verso il bordo inferiore del riquadro, ancora leggibile ma sul punto di uscire dalla vista.
Sotto, indicatore "Thinking..."; campo di input "Queue another message...", chip allegato `_index-workspace.md`, pulsante "Bypass permissions" a destra.
Voce: *"Allora, perché gli dico questo? Perché è normale che a volte non passiamo i controlli al primo colpo ed è una cosa normalissima nel mondo dell'AI"* — Joe commenta il turno appena mostrato, in cui l'AI segnala di aver dovuto correggere le proprie regole precedenti dopo aver trovato il vero template.

### Scena 224 · `frame-0942.png` · 94:06
Solo webcam a schermo intero, nessuno screen-share. Joe con sguardo abbassato, bocca socchiusa a metà parola, mani non visibili (sotto il bordo del frame). Sfondo invariato: mensola con libri dai dorsi viola/verde/blu, pianta pensile, lampada accesa a destra.
Voce: *"Un concetto molto importante che ehm ripeto abbastanza in community è"* — introduce il concetto che sta per spiegare, distinguendo ciò che l'AI può fare per noi da ciò che non può.

### Scena 225 · `frame-0943.png` · 94:12
Solo webcam, inquadratura ravvicinata. Joe tiene la penna bianca (Apple Pencil) fra pollice e indice della mano sinistra, sollevata all'altezza del microfono; mano destra alzata con le dita aperte in un gesto di spiegazione. Sguardo dritto in camera.
Voce: *"nel mondo delle AI noi possiamo fare outsourcing di competenza perché"* — comincia a distinguere ciò che si può delegare all'AI (la competenza tecnica) da ciò che non si può delegare.

### Scena 226 · `frame-0944.png` · 94:18
Solo webcam, capelli più arruffati rispetto alla scena precedente. Mano destra con pollice e indice piegati in un gesto di punto/elenco, penna appena visibile al bordo sinistro del frame nella mano opposta.
Voce: *"l'AI può scrivere codice al posto nostro, di pensiero perché molto spesso l'AI può pensare"* — prosegue l'elenco di ciò che si può "outsourceare" all'AI: scrittura del codice e, spesso, il pensiero.

### Scena 227 · `frame-0945.png` · 94:24
Solo webcam, entrambe le mani sollevate ai lati del volto in un gesto ampio, penna bianca ben visibile nella mano sinistra. Sguardo dritto in camera, bocca aperta a metà parola.
Voce: *"quale sia la migliore architettura, ok? al posto nostro, però non possiamo fare"* — conclude l'esempio dell'architettura pensata dall'AI e introduce il "però": il limite che sta per dichiarare.

### Scena 228 · `frame-0946.png` · 94:30
Solo webcam, stessa inquadratura ravvicinata. Joe tiene la penna verticale nella mano sinistra sollevata accanto al volto, mano destra aperta e sollevata anch'essa, entrambe le mani ai lati del microfono.
Voce: *"outsourcing della comprensione e questo"* — pronuncia il punto chiave del passaggio: ciò che non si può delegare all'AI è la comprensione.

### Scena 229 · `frame-0947.png` · 94:36
Solo webcam, Joe con lo sguardo abbassato, bocca aperta, entrambe le mani chiuse a pugno abbassate all'altezza del petto/microfono, penna appena visibile nella mano sinistra.
Voce: *"è la skill, il pensiero critico è comprensione di un problema. Ehm, e"* — definisce il pensiero critico come "comprensione di un problema", la competenza che resta insostituibile.

### Scena 230 · `frame-0949.png` · 94:48
Solo webcam, inquadratura frontale, Joe con la bocca aperta a metà parola, sguardo verso il basso, mani non visibili oltre il bordo inferiore.
Voce: *"questo è importante perché siamo arrivati al punto in cui possiamo raccontare un sacco di cose alle AI, ma"* — introduce il rischio: si può "raccontare" tanto all'AI senza però comprenderlo davvero.

### Scena 231 · `frame-0950.png` · 94:54
Solo webcam, Joe con gli occhi chiusi, espressione concentrata, sguardo verso il basso, mani fuori campo.
Voce: *"se non capiamo i cosa c'è sotto, sarà molto complesso che poi Lei riesca a farlo per noi capendolo da sola. Ok?"* — conclude il ragionamento: senza comprensione da parte dell'utente, l'AI non può capire da sola al posto suo.

### Scena 232 · `frame-0951.png` · 95:00
Solo webcam, ma con due mani estranee (probabilmente in un effetto di rientro/uscita rapido dal campo) visibili sfocate ai due bordi del frame, una a sinistra con un anello al dito, una a destra in movimento. Joe al centro, sguardo dritto in camera, bocca aperta a metà parola.
Voce: *"Perché ricordatevi sempre che a prescindere da quanto bravi diventino i modelli, sono sempre allenati sulla media dei dati disponibili. Ok? Bene."* — chiude il concetto con l'avvertenza sui limiti strutturali dei modelli, allenati sulla "media" dei dati.

### Scena 233 · `frame-0952.png` · 95:06 — **ritorno allo screen-share: "Thought for 88s" e nota di scope sull'`_index-aurora`** ⭐
Ritorno ad Antigravity, webcam ridotta al riquadro in basso a sinistra. Stessa tab "Create 11 brain work fol..." e stessa sidebar della scena 223, ora con la cartella `workspace` richiusa. Il primo blocco di chat (`self-identita-aurora.md`) è scorso quasi fuori vista, restano leggibili solo le ultime righe: "...annidati `anno/2025`. Ho riallineato tutti i 12 indici a questo template (erano appena creati, non ancora linterati)." e "2. La regola "`related` su una riga" che mi avevi dato nei turni precedenti è di fatto superata dal template: erano in conflitto, e il template (col linter che lo applica) vince. Da ora seguo quello. Scope: ho indicizzato solo il vault Aurora. Le directory `.claude/` e `.claude/plans/` viste in sessione sono config dello strumento, non parte del cervello: lasciate fuori. Vuoi che fissi `_index-aurora` come nota home (impostazione di Obsidian) o lo lasci a te?". Sotto, il blocco `_index-workspace.md` col prompt del gate di qualità (stesso testo della scena 223) e la nuova risposta dell'AI, in bullet:
- "Thought for 88s"
- "Creo il gate come script Python autonomo (nessuna dipendenza esterna) e lo eseguo per produrre il referto."
- "Una precisazione di scope che il tuo enunciato implica: l'indice madre `_index-aurora.md` sta nella radice del vault, non dentro una delle 11 cartelle, quindi per definizione ("ogni nota delle 11 cartelle") resta fuori dal setaccio. Le cartelle effettivamente scansionate sono 9 (11 − `sources/` − `workspace/`)."
In basso, indicatore di stato "Cerebrating..." (etichetta di "thinking" del tool, al posto del solito "Thinking...").
Voce: *"Allora, eh lui intanto sta creando il nostro script di Python autonomo. Benissimo."* — Joe segue in diretta la risposta dell'AI mentre genera lo script del gate di qualità.

### Scena 234 · `frame-0953.png` · 95:12 — **referto completo: "OK, 0 errori" e le 6 regole del gate** ⭐
Stessa tab, blocco `_index-workspace.md` in alto (prompt del gate, come sopra) e sotto il referto completo dell'AI:
- "Referto:"
- **"OK, 0 errori"**
- "Lo script è `gate_qualita.py` alla radice del vault. Ha setacciato le **28 note** delle 9 cartelle scansionate (le 11 meno `sources/` e `workspace/`) e tutte e 6 le regole passano:"
1. Frontmatter completo — ok
2. Corpo ≤ 300 righe — ok
3. ≥3 wikilink uscenti reali e unici, `_index` esclusi dal conteggio — ok
4. Zero link rotti — ok
5. Zero orfani, ≥1 link in entrata (`_index` esentati) — ok
6. Una sola componente connessa — ok
- "Lo lanci con `python3 gate_qualita.py` (exit code 0 se pulito, 1 se trova errori, così puoi usarlo anche in un hook pre-commit). Il referto raggruppato per regola compare solo quando c'è almeno un errore; se è tutto a posto stampa esattamente `OK, 0 errori`."
- "Due note su come ho risolto i punti ambigui dell'enunciato, così sai cosa controlla davvero:"
- **"Esistenza dei bersagli (regola 4)"** valutata sull'intero vault, non solo sulle 9 cartelle: così un eventuale link legittimo verso `canon` o un indice di `workspace/` non risulterebbe falsamente rotto.
- **"Connessione (regola 6)"** calcolata solo tra le note scansionate, grafo non orientato: il grappolo regge da solo, senza dover passare dall'indice madre che sta fuori scope.
Sidebar Explorer aggiornata: sotto la cartella `workspace` (richiusa) compaiono ora, allo stesso livello delle 11 cartelle, `_index-aurora.md` e il nuovo file `gate_qualita.py`. Campo di input in basso incorniciato in rosso: "Esc to focus or unfocus Claude".
Voce: *"E quindi ora è tutto bello che pulito, tutto è stato confermato, vedo regole precise e vediamo che il gate qualità è stato fatto qui."* — Joe legge il referto "0 errori" e nota che il gate qualità è stato creato correttamente.

### Scena 235 · `frame-0954.png` · 95:18 — **split view: chat a sinistra, `gate_qualita.py` aperto a destra** ⭐
Layout a due colonne in Antigravity: a sinistra lo stesso pannello chat con referto "OK, 0 errori" e le 6 regole (scena precedente, ora compresso); a destra, tab nuova **`gate_qualita.py`** aperta in editor. Sidebar sinistra: file `gate_qualita.py` selezionato/evidenziato in blu sotto la cartella `workspace` (richiusa). Codice sorgente leggibile (alcune righe tagliate dal bordo destro del frame, segnalato dove il testo esce dalla vista):
```
#!/usr/bin/env python3
"""
Gate di qualita' sul cervello di Aurora.
Setaccia ogni nota delle 11 cartelle, saltando sources[...taglio bordo destro]
e la controlla contro 6 regole. Stampa un referto ragg[...taglio]
Uso: python3 gate_qualita.py
"""

import os
import re
import sys

VAULT = os.path.dirname(os.path.abspath(__file__))
SKIP = {"sources", "workspace"}          # material[...taglio]
FOLDERS = ["self", "areas", "projects", "c[...taglio]",
           "entities", "data", "code", "outputs"]  # [...taglio]
REQUIRED_FM = ["title", "summary", "tags", "status", [...taglio]
MAX_BODY_LINES = 300
MIN_OUT = 3

LINK_RE = re.compile(r"\[\[([^\]]+?)\]\]")
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.S)

def is_index(stem):
    return stem.startswith("_index")

def split_fm(text):
    """Ritorna (dict_chiavi_presenti, corpo). Frontmat[...taglio]"""
    m = FM_RE.match(text)
    if not m:
        return None, text
    block = m.group(1)
    keys = set()
    for line in block.splitlines():
        km = re.match(r"^([A-Za-z0-9_-]+):\s*", line)
        if km:
            keys.add(km.group(1))
```
Barra di stato in basso: "Screen Reader Optimized", "Ln 1, Col 1", "Spaces: 4", "UTF-8", "LF", "{} Python", "3.12.12 64-bit", "Select Python Interpreter", "Pyrefly (Basic)", "Antigravity · Settings". Il file scorre oltre la riga 37 visibile (`keys.add(km.group(1))`), il resto della funzione non è leggibile in questo frame.
Voce: *"Ovviamente è stato fatto fuori perché lui è super partes, no? va a controllare tutte le cartelle, quindi va bene che sia nella cosiddetta root, quindi fuori da tutto da tutte quante queste cartelle, ma dentro a questa cartella principale."* — Joe apre il file per mostrare dal vivo il codice dello script, spiegando perché sta nella root e non dentro una delle 11 cartelle.

### Scena 236 · `frame-0955.png` · 95:24
Torna la vista a colonna singola (solo pannello chat, tab `gate_qualita.py` chiusa). Il mouse è fermo sopra il nome del file `gate_qualita.py` nella sidebar, che mostra un tooltip con il percorso completo: **"~/Desktop/aurora cervello/gate_qualita.py"**. Contenuto del pannello identico alla scena 234 (referto "OK, 0 errori" e le 6 regole). Campo di input in basso: "Esc to focus or unfocus Claude".
Voce: *"tutte quante queste cartelle, ma dentro a questa cartella principale. Ok? Quindi tutti questi 11 più questi due sono tutti allo stesso livello."* — Joe conferma col tooltip del percorso che `gate_qualita.py` (insieme a `_index-aurora.md`) sta alla radice del vault, allo stesso livello delle 11 cartelle.

### Scena 237 · `frame-0959.png` · 95:48 — **cambio applicazione: doc "Company Brain — Tutti i prompt del..." con i Prompt 6, 7, 8** ⭐
Cambio di applicazione: non più Antigravity ma un tool tipo Notion (sidebar sinistra con "Home", "Meetings" → "Connect your calendar" / "New AI meeting note", "Recents": Clienti, Cruscotto Aurora, **"Company Brain — Tutti i prom..."** evidenziato, New page, Reparti, Prodotti con sotto-voce "Default view", KPI mensili, Sedi, Competitor, sezione "Agents" con "+ New agent"). Tab in alto: **"Company Brain — Tutti i prompt del..."** (titolo troncato dall'interfaccia), etichetta "Private", link "Translate to English", pulsante "Share". Webcam ridotta in basso a sinistra. Corpo del documento, tre blocchi prompt leggibili per intero:
- **"Prompt 6 — Correggi e ripeti finché esce "0 errori""** — "Il ciclo correttivo: l'AI sistema ciò che ha segnalato, rifà il gate, e ripete fino a zero." Blocco codice: "Correggi le note che hai appena segnalato, applicando le regole del gate: frontmatter completo, massimo 300 righe, almeno 3 wikilink reali in uscita, zero link rotti, zero orfani, un solo grappolo connesso. Poi rifai il gate da capo e mostrami il nuovo referto. Ripeti finché non esce "0 errori"."
- **"Prompt 7 — Genera l'indice per la AI (llms.txt)"** — "La porta d'ingresso per la AI: un indice derivato, rigenerato dal frontmatter." Blocco codice: "Genera il file llms.txt nella radice del vault: e' l'indice-porta per la AI. Per ogni cartella di contenuto (self, areas, projects, docs, entities, data, code, outputs) elenca le note nel formato "- [[nome-file]] — summary", prendendo il summary dal frontmatter di ogni nota. In cima metti una riga di intestazione per ogni cartella. NON includere sources/ e workspace/. NON inventare niente: title e summary vengono SOLO dal frontmatter delle note. Ricordati che llms.txt e' DERIVATO: si rigenera da capo, non si modifica a mano."
- **"Prompt 8 — Lo showcase (la fotografia per la demo)"** — "Numeri da mostrare a un cliente: quante note, quanti link, quante componenti connesse." Blocco codice: "Fammi lo showcase del cervello di Aurora: una fotografia da mostrare in una demo. Conta tutte le note (le 11 cartelle, salta sources/ e workspace/), i wikilink totali che le tengono insieme, e quante componenti connesse ha il grafo (1 = tutto collegato). Poi dammi una tabella "note per cartella" e, sotto, l'elenco degli hub (i più linkati). Prendi il summary dell'_index di ogni cartella. Salva tutto in _showcase/showcase.md. E' una fotografia DERIVATA: si rigenera, non si scrive a mano."
Voce: *"Bene, ora abbiamo fatto il gate qualità, che cosa ci manca? Allora, a me piace molto inserire una seconda cosa che è un indice per l'LEM con tanti LM, perdonatemi, un indice per l'LM che è un lls.t txt."* — Joe passa dal codice al documento con l'elenco di tutti i prompt del corso, introducendo il Prompt 7 (llms.txt) mentre lo mostra già scritto per esteso nella pagina.

### Scena 238 · `frame-0961.png` · 96:00 — **Antigravity IDE: referto del gate di qualità, "OK, 0 errori"** ⭐
Editor Antigravity (non più Obsidian): sidebar sinistra "aurora cervello" con cartelle `areas`, `code`, `concepts`, `data`, `docs`, `entities`, `outputs`, `projects`, `self`, `sources`, `workspace` e i file `_index-aurora.md`, `gate_qualita.py`. Tab aperta "Create 11 brain work fol...". Nel pannello chat, prompt utente (con allegato `_index-workspace.md`): "Crea uno script python che faccia da gate di qualità sul cervello di Aurora. Passa al setaccio OGNI nota delle 11 cartelle (salta solo sources/ e workspace/, che sono materiale grezzo e scratch)" — segue una riga più chiara, in parte sbiadita/tagliata dal box, poco leggibile con certezza. Risposta dell'agente, in grassetto **Referto: OK, 0 errori**, poi: "Lo script è `gate_qualita.py` alla radice del vault. Ha setacciato le **28 note** delle 9 cartelle scansionate (le 11 meno `sources/` e `workspace/`) e tutte e 6 le regole passano:
1. Frontmatter completo — ok
2. Corpo ≤ 300 righe — ok
3. ≥3 wikilink uscenti reali e unici, `_index` esclusi dal conteggio — ok
4. Zero link rotti — ok
5. Zero orfani, ≥1 link in entrata (`_index` esentati) — ok
6. Una sola componente connessa — ok

Lo lanci con `python3 gate_qualita.py` (exit code 0 se pulito, 1 se trova errori, così puoi usarlo anche in un hook pre-commit). Il referto raggruppato per regola compare solo quando c'è almeno un errore; se è tutto a posto stampa esattamente `OK, 0 errori`.
Due note su come ho risolto i punti ambigui dell'enunciato, così sai cosa controlla davvero:
- **Esistenza dei bersagli (regola 4)** valutata sull'intero vault, non solo sulle 9 cartelle: così un eventuale link legittimo verso `canon` o un indice di `workspace/` non risulterebbe falsamente rotto.
- **Connessione (regola 6)** calcolata solo tra le note scansionate, grafo non orientato: il grappolo regge da solo, senza dover passare dall'indice madre che sta fuori scope."
In basso, campo chat con placeholder "⌘ Esc to focus or unfocus Claude", chip allegato `gate_qualita.py`, toggle "Bypass permissions". Barra di stato: "Screen Reader Optimized", "Antigravity · Settings".
Voce: *"Allora, lo incollo e ehm poi ve lo descrivo. Allora, questo non è una best practice, ma è una eh proposta per ora."* — Joe introduce il concetto successivo (l'indice `llms.txt` per l'AI) mentre lo schermo mostra ancora il referto del gate di qualità appena costruito.

### Scena 239 · `frame-0968.png` · 96:42 — **annotazione a penna verde "llms.txt" + nuovo prompt per generarlo** ⭐
Stessa vista Antigravity. In alto, tracciata a mano in verde acceso: la scritta corsiva **"llms.txt"** e accanto lo schizzo di un blocco note. Chat scrollata: in alto, riassunto ripiegato del prompt precedente sul gate di qualità e le due note su bersagli/connessione. Sotto, nuovo blocco con chip file `gate_qualita.py` e prompt utente: "Genera il file llms.txt nella radice del vault: e' l'indice-porta per la AI. Per ogni cartella di contenuto (self, areas, projects, concepts, docs, entities, [testo proseguono oltre il bordo del box, tagliato] data, code, outputs) elenca le sue note nel formato "- [[nome-file]] — summary"" — parte finale tagliata dal riquadro, dichiarato. Risposta agente: "Thought for 24s", poi: "**llms.txt** è derivato, quindi non lo scrivo a mano: creo un generatore che lo rigenera dal frontmatter delle note, e lo eseguo. Così title/summary vengono solo dalle note e il file si può ricostruire da capo quando il cervello cambia. Scelta che ti segnalo: **escludo i file `_index-` dall'elenco**. Sono scaffolding di navigazione (summary del tipo "Mappa della cartella X"), non contenuto; un door-index per AI è più utile se punta alle note vere. Se li vuoi dentro, lo dici e cambio un flag." Stato in corso: "Simmering...". Campo chat in basso: "Queue another message...", toggle "Bypass permissions" attivo, pulsante stop rosso (agente al lavoro).
Voce: *"Quindi, ehm, è un file derivato che riaggiorneremo ogni volta che magari aggiungeremo cose o magari faremo una modifica alla brain eccetera"* — Joe spiega perché `llms.txt` non va scritto a mano ma rigenerato, in perfetta sincronia con quanto appare a schermo.

### Scena 240 · `frame-0969.png` · 96:48 — **scrittura di `genera_llms.py` (70 righe)**
Stessa scena, chat scrollata oltre: dopo il blocco "llms.txt è derivato... cambio un flag", appare "**Write** `genera_llms.py`" con badge "70 lines" e anteprima del codice: `#!/usr/bin/env python3`, poi apertura docstring `"""` e prima riga "Generatore di llms.txt per il cervello di Aurora." Stato sotto: "Wrangling...". Nella sidebar sinistra compare ora il nuovo file `genera_llms.py` sotto `gate_qualita.py`. Annotazione verde "llms.txt" ancora visibile in alto.
Voce: *"aggiungeremo cose o magari faremo una modifica alla alla brain eccetera, nella quale diremo 'Ehi, guarda che tu hai esattamente queste cose qui dentro la brain e questo è il riassuntino.'"* — continua a motivare la natura "derivata" e sempre aggiornata del file, mentre l'agente scrive lo script.

### Scena 241 · `frame-0970.png` · 96:54 — **esecuzione bash: `genera_llms.py` genera e stampa `llms.txt`** ⭐
Chat scrollata ancora oltre: dopo l'anteprima di `genera_llms.py`, blocco "**Bash** Generate and display llms.txt" con riquadro terminale a due righe:
`IN   cd "/Users/giovannibeggiato/Desktop/aurora cervello" && python3 genera_llms.py && echo "=== llms.txt ===" && cat llms.txt`
`OUT  Scritto /Users/giovannibeggiato/Desktop/aurora cervello/llms.txt (30 note in 9 cartelle)`
`     === llms.txt ===`
`     # Aurora Sistemi — llms.txt`
Sotto, stato di avanzamento troncato "onking..." (verosimilmente "Thinking..." tagliato dal frame, dichiarato). Il comando rivela il percorso reale della cartella di lavoro sul Mac di Joe: `/Users/giovannibeggiato/Desktop/aurora cervello`. Sidebar: ora compare anche il file `llms.txt` in fondo alla lista, sotto `genera_llms.py`.
Voce: *"quale diremo 'Ehi, guarda che tu hai esattamente queste cose qui dentro la brain e questo è il riassuntino.' Ovviamente il workflow sarà che voi aprite la vostra sessione cloud..."* — Joe descrive il workflow a valle: l'agente AI legge questo riassunto prima di entrare nel vault vero e proprio.

### Scena 242 · `frame-0975.png` · 97:24 — **`llms.txt` aperto per intero: tutte le sezioni e le 30 note elencate** ⭐
Layout a tre colonne: sidebar file (`llms.txt` ora selezionato in fondo alla lista), pannello chat ristretto, editor principale con `llms.txt` aperto in una nuova tab (accanto a "Create 11 brain work..."). Chat (colonna stretta, testo tagliato a destra dal bordo del pannello): risposta agente in grassetto "**Fatto.** llms.txt generato alla radice del vault. Cosa contiene:" poi "Le 9 cartelle di contenuto nell'ordine che hai indicato (self → outputs), ognuna con la sua riga di intestazione `## <cartella>`." e "30 note elencate come `- [[nome-file]] — summary`, con il summary preso solo dal frontmatter (le virgolette del template vengono ripulite)." Ultima riga visibile "sources/ e" prosegue oltre il bordo, tagliata — dichiarato.
Editor `llms.txt`, contenuto integrale (righe tagliate a destra dal bordo del frame dove indicato, dichiarato):
```
# Aurora Sistemi — llms.txt
> Indice-porta per AI. File DERIVATO: rigenerato da genera_llms.py, non modificare a mano.

## self
- [[self-identita-aurora]] — Aurora Sistemi è la piattaforma SaaS italiana per la gestione [tagliato]

## areas
- [[area-customer-success]] — Reparto che cura onboarding, supporto e crescita dei clienti [tagliato]
- [[area-finance-operations]] — Reparto di amministrazione, controllo di gestione e legale [tagliato]
- [[area-marketing]] — Reparto che cura posizionamento, contenuti e generazione lead per A[tagliato]
- [[area-people-cultura]] — Reparto di HR, recruiting e cultura aziendale, guidato da Sara [tagliato, nome incerto]
- [[area-prodotto-engineering]] — Reparto che sviluppa la piattaforma Aurora e i suoi modu[tagliato]
- [[area-vendite]] — Reparto che acquisisce nuovi clienti per Aurora Sistemi, guidato dal [tagliato]

## projects
- [[progetto-arr-5m-2026]] — L'obiettivo approvato dal Board per il 2026: portare l'ARR ol[tagliato]

## concepts
- [[concetto-arr]] — Il fatturato ricorrente annuo: la metrica nord di Aurora, somma dei c[tagliato]
- [[concetto-churn]] — La perdita di clienti (logo churn) o di fatturato (gross churn) in[tagliato]
- [[concetto-efficienza-energetica]] — Ridurre sprechi e consumi degli edifici monitorando[tagliato]

## docs
- [[doc-onboarding-cliente]] — Il percorso con cui Customer Success porta un nuovo cliente[tagliato]

## entities
- [[cliente-banca-adriatica]] — Key account dal 2022 (520k ARR, 140 filiali); nel 2025 ha [tagliato]
- [[cliente-hotelline-hospitality]] — Unico nuovo logo del 2025 (260k ARR, 35 hotel); usa [tagliato]
- [[cliente-immobiliare-lombarda]] — Cliente storico dal 2019, il più grande per fatturato[tagliato]
- [[persona-chiara-fontana]] — CSM di Aurora che segue i key account Banca Adriatica e Imm[tagliato]
- [[persona-elena-ferraro]] — CEO e co-fondatrice di Aurora Sistemi, guida strategia e Ven[tagliato]
- [[persona-giulia-rinaldi]] — Guida il Customer Success di Aurora dall'ufficio di Bologna [tagliato]
- [[persona-marco-bianchi]] — CTO e co-fondatore di Aurora Sistemi, responsabile di Prodot[tagliato]
- [[prodotto-aurora-accessi]] — Modulo di controllo accessi (badge, fasce orarie, videosorv[tagliato]
- [[prodotto-aurora-core]] — Modulo base della piattaforma: anagrafica edifici, dashboard[tagliato]
- [[prodotto-aurora-energy]] — Modulo che monitora consumi di luce, gas e acqua, segnala s[tagliato]
- [[strumento-crm]] — Il CRM da cui Vendite e Finance esportano l'anagrafica clienti (sett[tagliato]
```
Barra di stato in basso: "Screen Reader Optimized", "Antigravity · Settings", "Ln 1, Col 1", "Spaces: 4", "UTF-8", "LF", "{} Plain Text".
Voce: *"quello che c'è qua dentro. Ok? Quindi mi dice, hai eh questo self con un piccolo riassuntino di quello che c'è, eh areas con i riassuntini di quello che sono, projects, eccetera eccetera eccetera."* — Joe descrive a voce esattamente la struttura che si vede a schermo, sezione per sezione.

### Scena 243 · `frame-0978.png` · 97:42 — **spiegazione completa: cosa contiene `llms.txt` e come si rigenera**
Chat Antigravity scrollata oltre lo screenshot precedente: si vede la fine del blocco "OUT" del comando bash (righe `Scritto /Users/giovannibeggiato/Desktop/aurora cervello/llms.txt (30 note in 9 cartelle)`, `=== llms.txt ===`, `# Aurora Sistemi — llms.txt`), poi il testo completo della risposta "**Fatto.** llms.txt generato alla radice del vault." con tutti i bullet leggibili per intero:
- "Le 9 cartelle di contenuto nell'ordine che hai indicato (self → outputs), ognuna con la sua riga di intestazione `## <cartella>`."
- "30 note elencate come `- [[nome-file]] — summary`, con il summary preso **solo** dal frontmatter (le virgolette del template vengono ripulite)."
- "`sources/` e `workspace/` esclusi; file `_index-` esclusi."

Segue "**Come si rigenera** (è derivato, non si tocca a mano):" con il comando in riquadro `python3 genera_llms.py`, poi: "Lo script `genera_llms.py` riscrive `llms.txt` da capo leggendo i frontmatter correnti. Quando aggiungi o modifichi note, rilancialo e l'indice si aggiorna da solo. Una nota di coerenza: il generatore e il gate condividono le stesse assunzioni (stesse 9 cartelle, stesso parsing di frontmatter, esclusione `_index`), così quello che passa il gate è esattamente ciò che finisce in `llms.txt`. Se vuoi, il prossimo passo naturale è incatenare i due: un unico comando che lancia `gate_qualita.py` e, solo se esce 0, rigenera `llms.txt` — utile come hook pre-commit. Se non sei in un repo git, posso lasciartelo come piccolo script `build.sh`." Campo chat in basso ora mostra "1 line selected" al posto del chip file (il cursore ha selezionato una riga di codice).
Voce: *"Vedete quindi che è letteralmente è un indice che io vi consiglio di mettere a livello token, a livello di efficienza mi ha aiutato un sacco. Non è una best practice, è una raccomandazione dello zio Jo, vedete voi cosa farne."* — Joe ribadisce la natura di consiglio personale (non standard) dell'indice `llms.txt` appena mostrato per intero.

### Scena 244 · `frame-0979.png` · 97:48 — **transizione: Antigravity → Notion, pagina "Company Brain — Tutti i prompt del..."** ⭐
Frame di passaggio tra due applicazioni: a sinistra, in trasparenza/sfumato, resta visibile il pannello dell'editor Antigravity di prima (si intravedono frammenti di testo tagliati come "...cartelle)" e "...aggiungi o modifichi note, rilancialo e l'indice si aggiorna da solo"). Al centro un riquadro popup di navigazione Notion (sidebar "Home"): sezione **Meetings** ("Connect your calendar", "New AI meeting note"), sezione **Recents** (Clienti, Cruscotto Aurora, **Company Brain — Tutti i prom...** evidenziata, New page, Reparti, Prodotti, Default view, KPI mensili, Sedi, Competitor), sezione **Agents** ("New agent"), sezione **Shared** ("Start collaborating"), poi di nuovo "Company Brain — Tutti i prom...", "New page", pulsante "New chat" in basso. A destra, la pagina Notion di destinazione, intestata "Company Brain — Tutti i prompt del..." (tag "Private"), con tre voci di un catalogo prompt numerato, tutte tagliate sul bordo destro del frame (dichiarato):
- "**Prompt 6 — Correggi e ripeti finché esce "**[tagliato]" / sottotitolo "Il ciclo correttivo: l'AI sistema ciò che hai segnalato, ril[tagliato]" / corpo: "Correggi le note che hai appena segnalato, ar[tagliato] frontmatter completo, massimo 300 righe, alm[tagliato] link rotti, zero orfani, un solo grappolo con[tagliato] mostrami il nuovo referto. Ripeti finché no[tagliato]"
- "**Prompt 7 — Genera l'indice per la AI (llms.t**[tagliato]" / sottotitolo "La porta d'ingresso per le AI: un indice derivato, rigen[tagliato]" / corpo: "Genera il file llms.txt nella radice del vaul[tagliato] Per ogni cartella di contenuto (self, areas, [tagliato] data, code, outputs) elenca le sue note nel f[tagliato] prendendo il summary dal frontmatter di ogni [tagliato] intestazione per ogni cartella. NON includere[tagliato] niente: title e summary vengono SOLO dal fror[tagliato, refuso per "frontmatter"] Ricordati che llms.txt e' DERIVATO: si rigene[tagliato]"
- "**Prompt 8 — Lo showcase (la fotografia per**[tagliato]" / sottotitolo "Numeri da mostrare a un cliente: quante note, quanti [tagliato]" / corpo: "Fammi lo showcase del cervello di Aurora: una[tagliato] Conta tutte le note (le 11 cartelle, salta so[tagliato] totali che le tengono insieme, e quante comp[tagliato] collegata). Poi dammi una tabella ["note per c[tagliato] il summary dell'_index di ogni cartella. Sal[tagliato] e' una fotografia DERIVATA: si rigenera, non[tagliato]"
Questa pagina Notion si rivela essere il canovaccio scritto da cui Joe ha copiato via via i prompt mostrati nelle scene precedenti (il Prompt 7 corrisponde parola per parola al prompt "Genera il file llms.txt..." delle scene 239/242).
Voce: *"per esempio, ai ehm ragazzi e gli imprenditori dentro alla community chiederò quando farò l'audit del loro eh cervello, è di introdurre anche una terza cosa che è invece una rappresentazione grafica di quello che c'è dentro la vostra ehm il vostro cervello."* — mentre passa a Notion, Joe introduce già a voce il tema successivo (la rappresentazione visiva/dashboard, cioè lo "showcase" del Prompt 8 appena intravisto a schermo).

### Scena 245 · `frame-0980.png` · 97:54 — **ritorno su Antigravity, stesso testo della spiegazione `llms.txt`**
Schermo di nuovo intero su Antigravity, contenuto pressoché identico alla scena 243 (stessi bullet su "30 note elencate...", "sources/ e workspace/ esclusi...", sezione "Come si rigenera" con `python3 genera_llms.py` e il paragrafo su `genera_llms.py`/coerenza col gate/proposta di `build.sh`). Il cursore del mouse è posizionato tra il testo e il campo di input in basso, dove si legge di nuovo "1 line selected".
Voce: *"cosa che mi piace fare molto è e è che, per esempio, ai ehm ragazzi e gli imprenditori dentro alla community chiederò quando farò l'audit del loro eh cervello, è di introdurre anche una terza cosa"* — continua a introdurre il terzo elemento (rappresentazione grafica/showcase) di cui parlerà nelle scene successive.

### Scena 246 · `frame-0985.png` · 98:24 — **doppio pannello: nuovo prompt "showcase" a sinistra, `llms.txt` completo a destra** ⭐
Layout a due colonne: a sinistra la chat Antigravity ristretta, a destra l'editor con `llms.txt` aperto (stesso contenuto integrale già trascritto alla scena 242 — intestazione, sezioni `## self`, `## areas`, `## projects`, `## concepts`, `## docs`, `## entities` con tutte le voci, testo tagliato sul bordo destro dell'editor). Nella chat a sinistra, sotto la spiegazione già vista, compare un nuovo blocco con chip **`llms.txt#50-50`** e prompt utente: "Fammi lo showcase del cervello di Aurora: una fotografia da mostrare in una demo." seguito da testo proseguito e sbiadito/tagliato: "Conta tutte le note (le 11 cartelle, salta so[tagliato] workspace/), i wiklink..." — corrisponde al "Prompt 8" appena visto nella pagina Notion della scena 244. Stato sotto: "Thinking... · 878 tokens" e "Imagining...". Campo chat in basso: "Queue another message...", chip `llms.txt`, toggle "Bypass permissions", pulsante stop rosso.
Voce: *"c'è dentro la vostra ehm il vostro cervello. Questo è molto utile. Allora, io sono una persona molto visiva, quindi mi piace vedere le cose prima di poter entrare nel nel tutto, no?"* — Joe motiva perché vuole anche una "fotografia" visiva del cervello, oltre al testo di `llms.txt` mostrato a destra.

### Scena 247 · `frame-0987.png` · 98:36 — **agente al lavoro sullo showcase, token in salita**
Vista a colonna singola (editor `llms.txt` richiuso), chat Antigravity con lo stesso blocco "Fatto. llms.txt generato..." scrollato più in alto (si vedono solo le ultime righe: bullet "30 note elencate...", "sources/ e workspace/ esclusi; file _index- esclusi.", sezione "Come si rigenera" con `python3 genera_llms.py` e il paragrafo completo su coerenza/`build.sh` come alla scena 243). Sotto, lo stesso blocco prompt con chip **`llms.txt#50-50`**: "Fammi lo showcase del cervello di Aurora: una fotografia da mostrare in una demo. Conta tutte le note (le 11 cartelle, salta sources/ e workspace/), i wikilink" — testo leggermente più esteso ma ancora sfumato/tagliato in fondo. Stato di avanzamento cambiato rispetto alla scena precedente: "Thinking... · 1.8k tokens" e "Vibing..." (l'agente sta ancora elaborando, il contatore token è salito da 878 a 1.8k e cambia l'etichetta di stato). Campo chat in basso invariato: chip `llms.txt`, "Bypass permissions", stop rosso.
Voce: *"vedere cosa c'hai messo dentro, in modo tale da poterla capire al volo senza diventare impazzito e mi piace vedere anche quanti file hai dentro, come sono disposti in una maniera molto impattante e molto immediata, no?"* — Joe continua a spiegare il valore dello showcase visivo mentre l'agente lo sta ancora generando in background.

### Scena 248 · `frame-0994.png` · 99:18 — **scrittura di `genera_showcase.py` (139 righe)**
Chat scrollata: si vede la coda del paragrafo precedente ("...pre-commit. Se non sei in un repo git, posso lasciartelo come piccolo script `build.sh`."), poi il blocco prompt con chip `llms.txt#50-50`: "Fammi lo showcase del cervello di Aurora: una fotografia da mostrare in una demo. Conta tutte le note (le 11 cartelle, salta sources/ e workspace/), i wikilink totali che le tengono insieme, e quante componenti connesse ha il grafo (1 e tutto..." (fine riga sbiadita/tagliata). Risposta agente: "Thought for 43s", poi: "Come `llms.txt`, anche questa è una fotografia **derivata**: creo un generatore e lo eseguo, così i numeri sono calcolati dal grafo reale e si rigenerano quando il cervello cambia." Segue "**Write** `genera_showcase.py`" con badge "139 lines" e anteprima codice: `#!/usr/bin/env python3`, poi `"""` e prima riga "Generatore dello showcase del cervello di Aurora." Stato sotto, parola parzialmente tagliata dal bordo sinistro del frame: "‑uttering..." (verosimilmente "Stuttering..." o simile, non leggibile con certezza — dichiarato). Sidebar: nuovo file `genera_showcase...` (nome troncato dalla larghezza del pannello) aggiunto sotto `genera_llms.py`, `llms.txt` evidenziato/selezionato.
Voce: *"Trovo che questo sia estremamente utile anche quando andate a vendere questa tipologia di servizio, eh, perché vi permette di riassumere in una maniera abbastanza visiva."* — Joe collega lo showcase appena generato al suo uso commerciale, mostrarlo ai clienti in fase di vendita.

### Scena 249 · `frame-0996.png` · 99:30 — **`_showcase/showcase.md` generato: markdown sorgente + anteprima renderizzata con le metriche reali** ⭐
Layout a tre colonne: chat ristretta a sinistra (sidebar con nuova cartella `_showcase` espansa contenente `showcase.md`), al centro il file `showcase.md` in editor sorgente, a destra "Preview showcase.md" con il rendering.
Chat: prompt `llms.txt#50-50` collassato in alto, poi risposta: "**Fatto.** Fotografia salvata in `_showcase/showcase.md`[tagliato]" seguita da "**La fotografia del cervello di Aurora**" con bullet:
- "**39 note totali** — 30 di contenuto + 9 hub (un `_index` per cartella)"
- "**262 wikilink** che le tengono insieme"
- "**1 componente connessa** → tutto collegato, nessuna isola"
poi: "La tabella note-per-cartella e l'elenco degli hub (il summary di ogni `_index`) sono nel file." e l'inizio di "**Come si rigenera** (è derivato, non si scrive a mano):" (tagliato in fondo al pannello).

Editor sorgente `showcase.md` (righe numerate, testo tagliato a destra dal bordo del frame dove indicato):
```
# Showcase — Cervello Aurora Sistemi
> Fotografia DERIVATA del grafo. Rigenerata da genera_showcase.py, non modificare a mano.

> Scope: le 11 cartelle meno sources/ e workspace/ (9 cartelle). L'indice madre alla radice resta fuori.

## La fotografia

| Metrica | Valore |
| --- | --- |
| Note totali | 39 |
| di cui note di contenuto | 30 |
| di cui hub (un _index per cartella) | 9 |
| Wikilink totali (la colla del grafo) | 262 |
| Componenti connesse | 1 |
```

Pannello "Preview showcase.md" (rendering finale), titolo "**Showcase -- Cervello Aurora Sistemi**", box di nota: "Fotografia DERIVATA del grafo. Rigenerata da genera_showcase.py, non modificare a mano. Scope: le 11 cartelle meno sources/ e workspace/ (9 cartelle). L'indice madre alla radice resta fuori." Sezione "**La fotografia**" con tabella:

| Metrica | Valore |
|---|---|
| Note totali | 39 |
| di cui note di contenuto | 30 |
| di cui hub (un _index per cartella) | 9 |
| Wikilink totali (la colla del grafo) | 262 |
| Componenti connesse | 1 (tutto collegato) |

Sezione "**Note per cartella**" con tabella (ultima riga "entities" tagliata/sfumata in fondo al frame):

| Cartella | Contenuto | Hub | Totale |
|---|---|---|---|
| self | 1 | 1 | 2 |
| areas | 6 | 1 | 7 |
| projects | 1 | 1 | 2 |
| concepts | 3 | 1 | 4 |
| docs | 1 | 1 | 2 |
| entities | 11 (?) | 1 (?) | 12 (?) — riga tagliata dal bordo inferiore, cifre poco nitide, dichiarato |

Voce: *"Poi potete farvi tutte le dashboard che volete, potete farvi Jarvis, gli fate battere le mani, come vedete su Instagram, potete fare tutto quello che volete. By the way, facilissimo fare quella roba là. Usate Deep Gram e utilizzate 11 Labs."* — Joe commenta le alternative "dashboard vocali" più scenografiche, mentre a schermo resta la sua versione testuale/tabellare dello showcase appena generato.

### Scena 250 · `frame-1005.png` · 100:24 — **transizione su Notion: "Prompt 8" per intero + nuovo "Prompt — Impostazioni grafo a sfera"** ⭐
Nuovo frame di passaggio Antigravity → Notion, stessa composizione della scena 244: a sinistra, in ombra/sfumato, si intravede ancora la chat Antigravity precedente, con un frammento di testo leggibile "...era un numero sbagliato buttato lì da me, il gate a strumenti (`gate_qualita.py`, `genera_llms.py`, ...ati," (frase tagliata, dichiarata). Al centro il popup di navigazione Notion "Home" (Meetings: "Connect your calendar", "New AI meeting note"; Recents: Clienti, Cruscotto Aurora, **Company Brain — Tutti i prom...**, New page, Reparti, Prodotti, Default view, KPI mensili, Sedi, Competitor; Agents: "New agent"; Shared: "Start collaborating"; Private: Company Brain — Tutti i prom..., New page, "Add item"; pulsante "New chat" in basso). A destra, la pagina "Company Brain — Tutti i prompt del..." (tag "Private"), che mostra ora per intero (bordo destro del frame taglia comunque la fine di ogni riga, dichiarato):
Coda del "Prompt 7": "...La porta d'ingresso per le AI: un indice derivato, rigenerato dal front[tagliato]" e corpo "Genera il file llms.txt nella radice del vault: e' l'indi[tagliato] Per ogni cartella di contenuto (self, areas, projects, co[tagliato] data, code, outputs) elenca le sue note nel formato "- [[[tagliato] prendendo il summary dal frontmatter di ogni nota. In cim[tagliato] intestazione per ogni cartella. NON includere sources/ e [tagliato] niente: title e summary vengono SOLO dal frontmatter dell[tagliato] Ricordati che llms.txt e' DERIVATO: si rigenera da capo, [tagliato]"

"**Prompt 8 — Lo showcase (la fotografia per la demo)**" (titolo per intero, con icona), sottotitolo "Numeri da mostrare a un cliente: quante note, quanti link, quante co[tagliato]", corpo: "Fammi lo showcase del cervello di Aurora: una fotografia c[tagliato] Conta tutte le note (le 11 cartelle, salta sources/ e wor[tagliato] totali che le tengono insieme, e quante componenti conne[tagliato] collegato). Poi dammi una tabella "note per cartella" e, a[tagliato] il summary dell'_index di ogni cartella. Salva tutto in _[tagliato] E' una fotografia DERIVATA: si rigenera, non si scrive a [tagliato]" — corrisponde esattamente al prompt e al file mostrati in azione nelle scene 246-249.

Nuova voce del canovaccio, non ancora eseguita a schermo nelle scene precedenti: "**Impostazioni grafo a sfera (a mano, in Obsidian)**", corpo: "Nella vista grafo → icona ingranaggio → forze:
- Distanza dei link (Link distance): **BASSA** → avvicina le note collegate, formano piccole sfere
- Forza di repulsione (Repel force): **MODERATA** → le note non si toccano ma non volano via
- Forza centrale (Center force): **DOLCE** → tira tutto verso il centro, niente disperde ai bor[tagliato, presumibilmente "bordi"]
- Orfani (Show orphans): **ACCESI** [tagliato] → formano un anello esterno attorno al grappolo[tagliato]"
Voce: *"Super semplice, ma quello che voglio dirvi è avete un modo o una dashboard. A me piace vederla così semplice in formato testo. Sono una persona noiosa, per dire qua dentro ci sono queste cose ed è esattamente così grossa la tua dashboard."* — Joe torna a ribadire la sua preferenza per il formato testuale/tabellare rispetto alle dashboard più elaborate, mentre il canovaccio Notion anticipa già il prossimo argomento (le impostazioni manuali del grafo a sfera in Obsidian).

### Scena 251 · `frame-1006.png` · 100:30 — Prompt 9 (versione breve) e Prompt 10 su Notion ⭐
Notion, tema scuro, pagina **"Company Brain — Tutti i prompt del..."** (titolo tab troncato). Sidebar a sinistra: Home, Meetings (Connect your calendar / New AI meeting note), Recents (Clienti, Cruscotto Aurora, **Company Brain — Tutti i prom...** evidenziata, New page, Reparti, Prodotti, Default view, KPI mensili, Sedi, Competitor), Agents (New agent), Shared.
Corpo pagina dall'alto: coda di un elenco puntato precedente — "- Orfani (Show orphans): ACCESI -> formano l'anello esterno attorno al grappolo" — poi "Poi aggiungi i gruppi di colore per cartella (le persone di un colore, i dati di un altro, ecc.)."
Intestazione **"Prompt 9 — Metti il vault sotto git (senza push)"**, sottotitolo "La macchina del tempo locale: repository + branch + commit, niente push." Riquadro codice (con evidenziazione colore su alcune parole):
"Metti il mio vault sotto git, così ho una macchina del tempo. Se non è ancora u[n] repository, crealo. Crea un branch di lavoro chiamato feature/wave-01, prendi tut[ti] i file e fai un commit con questo messaggio:
"Bootstrap del cervello a 11 cartelle: note + grafo Obsidian".
NON fare push da nessuna parte: il cervello resta solo sul mio computer."
Sotto: "Passo 4 — Interrogare il cervello, mostrarlo, tenerlo vivo", poi "Prompt 10 — Interroga il cervello (a 28 note, senza RAG)", sottotitolo "Carichi tutte le note e fai una domanda da imprenditore. Regola d'oro: rispondi solo con le note, cita il file, se non c'è dillo." Riquadro codice: "Ti do l'intero cervello di Aurora Sistemi: tutte le note markdown del vault, con il loro frontmatter. Rispondi alla mia domanda usando SOLO il contenuto di queste note. - Cita sempre il nome del file da cui prendi ogni informazione. - Se la risposta non è presente nelle note, scrivi esattamente: "Non presente nel cervello." Non inventare, non stimare, non dedurre. Domanda: qual è l'ARR di Aurora e come è cambiato l'organico negli ultimi tre anni?" (testo tagliato in fondo al frame).
Voce: *"un nuovo problema. Andiamo di nuovo qui e ve lo definisco"* — la voce non è ancora sincronizzata col Prompt 9: sta introducendo il tema data-compliance/version-control, mentre il documento con i prompt 9-10 è già visibile in anteprima sullo schermo.

### Scena 252 · `frame-1007.png` · 100:36 — richiamo al diagramma "controllo di qualità" ⭐
Excalidraw (excalidraw.com), disegno a mano già visto in una fase precedente del video: cerchio rosso con "1" e titolo **"INTRODURRE UN CONTROLLO DI QUALITÀ"**; al centro una nuvola con frecce convergenti da più direzioni; sotto, un omino stilizzato collegato alla nuvola da una freccia nera (in discesa) e una blu (in salita); a sinistra dell'omino un triangolo/cuneo rosso; a destra della nuvola un'icona documento (rettangolo con righe) con una "X" rossa vicino; una grande freccia rossa curva chiude il cerchio dal documento in basso a destra fino al cuneo rosso a sinistra. In alto a destra, un avviso toast del browser parzialmente tagliato dal bordo: *"...ni link punta a qualcosa che esiste [...] quindi i link rotti sono impossibili"* (➕ ricostruibile come "ogni link punta a qualcosa che esiste già, quindi i link rotti sono impossibili").
Voce: *"Ora abbiamo fatto i nostri 1000 controlli, no? E abbiamo questi script."* — richiamo esplicito al gate di qualità costruito in precedenza, prima di introdurre il "nuovo problema" (data compliance / version control).

### Scena 253 · `frame-1038.png` · 103:42 — Prompt 9, versione "istruzioni precise" ⭐ 🔎
Stessa pagina Notion di scena 251, scrollata più in alto: in cima la coda di un prompt precedente sulle forze del graph view — "Distanza dei link (Link distance): BASSA -> avvicina le note collegate, formano piccole sfere fitte / Forza di repulsione (Repel force): MODERATA -> le note non si toccano ma non volano via / Forza centrale (Center force): DOLCE -> tira tutto verso il centro, niente disperde ai bordi / Orfani (Show orphans): ACCESI -> formano l'anello esterno attorno al grappolo" poi "Poi aggiungi i gruppi di colore per cartella (le persone di un colore, i dati di un altro, ecc.)."
Intestazione, qui **senza** il suffisso visto in scena 251: **"Prompt 9 — Metti il vault sotto git"**, sottotitolo identico "La macchina del tempo locale: repository + branch + commit, niente push." Il riquadro codice sotto è però un'altra versione, un elenco numerato:
"Trasforma il mio vault Obsidian in [u]n repository Git. Obiettivo: avere una cronol[ogia completa delle modifiche...] (testo tagliato a destra)
Istruzioni precise:
1. Verifica se la cartella del vault è già un repository Git. Se non lo è, inizi[alizzalo con 'git init'].
2. Crea un file '.gitignore' adatto a Obsidian: escludi '.obsidian/workspace.jso[n'...] (tagliato)
3. Crea un branch di lavoro chiamato 'feature/wave-01' e spostati su quel branch.
4. Aggiungi tutti i file allo staging e fai commit e push con questo messaggio es[atto]: "Bootstrap del cervello a 11 cartelle: note + grafo Obsidian"
5. Alla fine mostrami: il branch attivo, l'output di 'git status' e l'output di '[...]" (tagliato, continua fuori frame)
Sotto: "Passo 4 — Interrogare il cervello, mostrarlo, tenerlo vivo" e "Prompt 10 — Interroga il cervello (a 28 note, senza RAG)", stesso sottotitolo di scena 251.
🔎 Le due letture dello stesso riquadro "Prompt 9" (rilette entrambe due volte, per certezza) non coincidono: in scena 251 (100:30) il codice è un paragrafo breve che dice esplicitamente **"NON fare push da nessuna parte: il cervello resta solo sul mio computer"**; qui (103:42) il codice è un elenco numerato il cui punto 4 dice **"fai commit e push"** — l'istruzione "non fare push" è sparita, sostituita dall'opposto. Non è un errore di lettura mio: il contenuto del box è realmente diverso tra i due momenti (probabilmente riscritto/espanso con l'AI tra una ripresa e l'altra). Nota operativa per l'Impero: un'espansione di prompt via AI può capovolgere in silenzio un vincolo di sicurezza scritto a mano — da controllare sempre dopo un "espandi questo prompt".
Voce: *"andiamo al nostro eh notion, prendiamo il prompt ed ora lo inseriremo qui e vediamo che cosa c'è scritto. Trasformo il mio [vault] Obsidian"* — sta letteralmente copiando questo prompt per incollarlo nell'IDE.

### Scena 254 · `frame-1039.png` · 103:48 — il Prompt 9 incollato nell'IDE "Antigravity" ⭐
Editor **Antigravity** (barra di stato in basso a destra: "Screen Reader Optimized" / "Antigravity - Settings"), tema scuro. Explorer a sinistra: cartella radice "aurora cervello" con sottocartelle _showcase (espansa, contiene showcase.md), areas, code, concepts, data, docs, entities, outputs, projects, self, sources, workspace; a livello radice i file _index-aurora.md, gate_qualita.py, genera_llms.py, genera_showcase..., llms.txt.
Tab aperta: "Create 11 brain work fol[ders in vault]"; sopra la chat un chip di riferimento "🔗 llms.txt#50-50"; testo utente (grigio, righe successive coperte) "Fammi lo showcase del cervello di Aurora: una fotografia da mostrare in una demo. Conta tutte le note (le 11 cartelle, salta sources/ e workspace/), i wikilink [...]".
Risposta dell'assistente sotto: "La tabella note-per-cartella e l'elenco degli hub (il summary di ogni _index) sono nel file. Come si rigenera (è derivata, non si scrive a mano): `python3 genera_showcase.py` — Lo script genera_showcase.py ricalcola tutto dal grafo reale e riscrive _showcase/showcase.md. Una correzione che ti devo, per onestà: in un turno precedente ti avevo detto "28 note scansionate" dal gate — era un numero sbagliato buttato lì da me, il gate non lo aveva stampato. Il conteggio vero, calcolato ora, è **39 note nelle 9 cartelle (30 contenuto + 9 hub)**. I tre strumenti (gate_qualita.py, genera_llms.py, genera_showcase.py) ora condividono lo stesso scope e lo stesso parsing, quindi i numeri sono coerenti tra loro. Nota di scope, identica a prima: l'indice madre _index-aurora.md sta nella radice e resta fuori dal conteggio; _showcase/ è una cartella di artefatti derivati, non viene scansionata dal gate né inclusa in llms.txt."
Sotto, riquadro bordato di rosso (input non ancora inviato) col **Prompt 9 completo** (identico al testo numerato di scena 253):
"Trasforma il mio vault Obsidian in un repository Git. Obiettivo: avere una cronologia completa delle modifiche, come una macchina del tempo per il mio company brain.
Istruzioni precise:
1. Verifica se la cartella del vault è già un repository Git. Se non lo è, inizializzalo con 'git init'.
2. Crea un file '.gitignore' adatto a Obsidian: escludi '.obsidian/workspace.json', '.obsidian/workspace-mobile.json', file di cache e file di sistema ('.DS_Store', 'Thumbs.db'). Tutto il resto della cartella '.obsidian' va versionato, perché contiene grafo e configurazioni.
3. Crea un branch di lavoro chiamato 'feature/wave-01' e spostati su quel branch.
4. Aggiungi tutti i file allo staging e fai commit e push con questo messaggio esatto:" (tagliato in fondo al frame)
In basso: icone allegato/pin, pulsante "Bypass permissions" (rosso), freccia di invio rossa.
Voce: *"in una repository git. Obiettivo avere una cronologia completa delle modifiche come una macchina del tempo nel mio brain e poi una serie di cose."* — legge/parafrasa a voce il prompt appena incollato.

### Scena 255 · `frame-1044.png` · 104:18 — apertura del file `.env` 🔎
Stessa schermata Antigravity, ora con un secondo pannello a destra: tab **".env"** aperta (file vuoto, una sola riga numerata "1"); nell'Explorer il file `.env` è evidenziato/selezionato in blu. Il riquadro del prompt (a sinistra) mostra la stessa lista numerata, scrollata più in basso: righe 2-4 visibili con testo tagliato a destra ("...ne della cartella '.obsidian' va versionato, perché contiene grafo e configurazioni." / "...rea un branch di lavoro chiamato 'feature/wave-01' e spostati su" / "...ggiungi tutti i file allo staging e fai commit e push con questo") e in basso a sinistra un banner giallo/toast parzialmente visibile: *"terminal environment injectio..."* (tagliato).
Voce: *"allora ora dovremmo dargli accesso a GitHub. Eh, potremmo farlo con MCP, potremmo farlo con token, diamoglielo con il token. Ovviamente dovremmo metterlo in un [.env] file."* — 🔎 la trascrizione automatica rende ".env" come *"un DNV file"*; il frame conferma che si tratta del file `.env` appena aperto vuoto (il sottotitolo automatico ha storpiato il nome del file).

### Scena 256 · `frame-1045.png` · 104:24 — dashboard GitHub, repo reali e Claude dentro Copilot ⭐
Browser, github.com, dashboard "Home". Colonna sinistra "Top repositories" (pulsante verde "New"): `Giobebbe/social-media-manager`, `Giobebbe/company-brain`, `Giobebbe/gentes-website`, `Giobebbe/avanguardia-plus-linkedin`, `Giobebbe/antigravity-corso-completo-italiano`, `Giobebbe/second-brain-os-template`, `Giobebbe/crea-kitchen` (ultimo nome poco leggibile con certezza), poi "Show more".
Centro: casella "Ask anything or type @ to add context" con pulsanti "Ask", "All repositories", selettore modello **"Claude Haiku 4.5"**, e pulsanti "Agent", "Create issue", "Write code", "Git", "Pull requests". Sotto, "Feed" → "Trending repositories": `addyosmani/agent-skills` — "Production-grade engineering skills for AI coding agents" (Shell, ⭐ 50.3k) e `phuryn/pm-skills` — "PM Skills Marketplace: 100+ agentic skills, commands, and plugins — from discovery to strategy, execution, launch, and growth." (⭐ 14k).
A destra, menu account aperto: **Giobebbe**, Set status, Profile, Repositories, Stars, Gists, Organizations, Enterprises, Sponsors, Settings, Copilot settings, Feature preview, Appearance, Accessibility, Try Enterprise (Free), Sign out; cursore fermo su "Profile". Dietro il menu, un pannello notifiche parzialmente coperto ("UN...", "Oct 2...", "Sav... Bird...", non leggibile con certezza).
➕ I nomi dei repository (`company-brain`, `antigravity-corso-completo-italiano`, `second-brain-os-template`) indicano che l'autore vende/condivide anche un corso su Antigravity e un template "second brain OS" a parte; non viene detto a voce in questo punto del video.
Voce: *"Qui poi avremo la nostra repository. Andremo qua sotto. Andremo in eh settings."* — sta per aprire le impostazioni dell'account per generare il token.

### Scena 257 · `frame-1046.png` · 104:30
Browser, github.com/settings/profile. Sidebar (porzione bassa visibile): sezione "Integrations" → Applications, Scheduled reminders; sezione "Archives" → Security log, Sponsorship log; voce isolata **"Developer settings"** (icona `</>`), cursore del mouse appena sotto, in procinto di cliccarla. Pannello centrale, pagina "Profile": campo "Location" (vuoto), checkbox "Display current local time", sezione "ORCID iD" con spiegazione e pulsante verde "Connect your ORCID iD", testo su opzionalità dei campi, pulsante verde "Update profile"; sotto "Contributions & activity" con due checkbox ("Make profile private and hide activity", "Include private contributions on my profile") e pulsante "Update preferences"; in fondo comincia "Profile settings" con checkbox spuntata "Show Achievements on my profile".
Voce: *"settings. Qua sotto ci saranno i developer [...] Avremo il personal access token."* — sta navigando verso Developer settings per creare il token.

### Scena 258 · `frame-1054.png` · 105:18 — prompt integrale + campo GITHUB TOKEN ⭐
Stessa vista Antigravity di scena 254/255, riquadro del prompt scrollato fino in fondo, tutte le 5 istruzioni leggibili per intero:
"1. Verifica se la cartella del vault è già un repository Git. Se non lo è, inizializzalo con 'git init'.
2. Crea un file '.gitignore' adatto a Obsidian: escludi '.obsidian/workspace.json', '.obsidian/workspace-mobile.json', file di cache e file di sistema ('.DS_Store', 'Thumbs.db'). Tutto il resto della cartella '.obsidian' va versionato, perché contiene grafo e configurazioni.
3. Crea un branch di lavoro chiamato 'feature/wave-01' e spostati su quel branch.
4. Aggiungi tutti i file allo staging e fai commit e push con questo messaggio esatto:
   "Bootstrap del cervello a 11 cartelle: note + grafo Obsidian"
5. Alla fine mostrami: il branch attivo, l'output di 'git status' e l'output di 'git log --oneline'.

GITHUB TOKEN: [cursore lampeggiante, campo vuoto]"
In basso a sinistra, toast giallo parzialmente visibile "...erminal environment injectio...". Nell'Explorer il file `.env` resta evidenziato.
Voce: *"Faremo la verifica della mail. Perfetto. Poi metteremo token a second brain [...] Tutorial completo su come creare una second[a] Br[ain] su YouTube."* — sta nominando il token "second brain" durante la creazione su GitHub, prima di incollarlo nel campo GITHUB TOKEN.

### Scena 259 · `frame-1055.png` · 105:24 — le 5 app aperte per il tutorial ⭐
Vista "app switcher" (stile macOS): in alto cinque riquadri con etichetta sotto: **"Desktop 1"** (miniatura sfondo lago di montagna), **"Obsidian"** (miniatura scura, graph view), **"Antigravity IDE"** (miniatura scura, editor di codice — bordo evidenziato in blu, finestra attiva), **"Notion"** (miniatura scura), **"Google Chrome"** (miniatura scura). Sotto, sfondo desktop: lago turchese con massi di granito e montagne innevate, con tooltip centrale **"No Available Windows"**. Dock in basso: Chrome, un'app con pallino rosso di notifica, un'icona nera "K"/Craft, Slack, un'icona a stella arancione, un'icona triangolare viola/scura (verosimilmente il logo di Antigravity), un'icona a grafico a barre, WhatsApp (verde), un diamante viola, Notion (N nero), un blocco note, un foglio di calcolo verde, cestino.
➕ L'etichetta "Antigravity IDE" nello switcher conferma il nome esatto del tool visto nelle scene precedenti (non "VS Code", non "Claude Code").
Voce: *"Vedete che questo è super importante perché immaginiamo ora di andare nel nostro esempio della company Brain."* — transizione; nessun collegamento diretto con lo switcher, che è solo un passaggio di scena.

### Scena 260 · `frame-1056.png` · 105:30
Excalidraw (excalidraw.com): tela quasi vuota. Pannello stile a sinistra (colori tratto, sfondo, spessore, opacità, livelli). In alto testo segnaposto grigio chiaro (istruzioni standard di Excalidraw per lo strumento testo, poco leggibile con certezza). Sul bordo destro, tagliata dal frame, l'inizio di una scritta a mano **"LOCAL"** in nero e, sotto, l'abbozzo di una forma trapezoidale.
Voce: *"al volo eh che cosa ci sarà scritto nel promptio che dovrebbe chiarire un sacco di cose"* — sta ancora parlando del prompt GitHub appena creato; la metafora branch/commit/timeline (visibile completa nella scena successiva) non è ancora stata disegnata per intero in questo frame.

### Scena 261 · `frame-1097.png` · 109:36 — diagramma disegnato a mano: BRANCH / COMMIT / MAIN ⭐
Excalidraw, stessa tela di scena 260 ora sviluppata: in alto a sinistra scritta **"BRANCH"**, con una linea nera che scende e termina su una piccola icona (rettangolo con un cerchio dentro e un pennacchio/bandierina sopra, stile "postazione/laptop"). Sotto, tre linee orizzontali parallele: una **blu**, etichettata **"MAIN"** a destra, con trattini verticali lungo il percorso e freccia finale a destra; una **arancione** che parte da un punto di intersezione e sale con una grossa freccia verso l'angolo in alto a destra, dove incontra un fitto scarabocchio rosso/bordeaux a zig-zag che coprebbe del testo arancione sottostante (🔎 non leggibile con certezza sotto lo scarabocchio, sembra qualcosa come "PROD..." / "CONFIGURE" / "FOR..."); una **verde**, etichettata **"COMMIT"** a sinistra, che parte da un pallino verde sulla linea principale e termina con una freccia corta a destra.
🔎 Lo scarabocchio rosso sopra il testo arancione sembra rappresentare visivamente un branch "fallito/da scartare", coerente con l'esempio verbale raccontato poco prima (cambiare la foto di sfondo del sito, se non funziona si cancella il ramo) — ma il testo esatto sotto lo scarabocchio non è leggibile con certezza, quindi non lo riporto come citazione.
Voce: *"l'importante il motore di queste cose. Se volete un corso dettagliato, fatto con calma, in community, faccio questo, faccio rag, facciamo tutto quello della company Brain."* — chiude la spiegazione tecnica di Git rimandando a un corso community dedicato.

### Scena 262 · `frame-1098.png` · 109:42
Talking head, stessa inquadratura consueta (mensola con libri colorati, pianta, lampada calda, sedia da ufficio grigia, microfono in primo piano). Nessun testo a schermo; gesticola con la mano destra.
Voce: *"faccio rag, facciamo tutto quello della company Brain. Qui è giusto per darvi"* — continua a rimandare gli approfondimenti tecnici (RAG) al corso community.

### Scena 263 · `frame-1099.png` · 109:48
Talking head, stessa inquadratura; entrambe le mani sollevate, gesticolando ampiamente, sguardo abbassato.
Voce: *"due concetti. Se avete passione, volete andarvelo anche a studiare in autonomia."* — invita chi è interessato ad approfondire Git per conto proprio.

### Scena 264 · `frame-1100.png` · 109:54
Talking head, stessa inquadratura; mano sinistra alzata col palmo aperto verso la camera, mano destra con dita raccolte, sguardo diretto in camera.
Voce: *"Quello che stiamo facendo adesso è abbiamo fatto la company Brain, abbiamo"* — comincia a riepilogare il percorso fatto finora.

### Scena 265 · `frame-1101.png` · 110:00
Talking head, stessa inquadratura; mano destra alzata a palmo aperto ben visibile in primo piano, sguardo diretto in camera.
Voce: *"dato all'AI la capacità di entrare nei vari file e di navigarli. Ora dobbiamo"* — prosegue il riepilogo, introduce il tema successivo (la memoria dei checkpoint).

### Scena 266 · `frame-1102.png` · 110:06
Talking head, stessa inquadratura consueta. Nessun testo a schermo.
Voce: *"noi perdiamo il computer, il computer si rompa e cose di questo tipo. Allo stesso"* — spiega perché serve un backup esterno del cervello.

### Scena 267 · `frame-1103.png` · 110:12
Talking head, stessa inquadratura; entrambe le mani sollevate a mezz'aria, gesticolando.
Voce: *"modo vogliamo che se qualcuno aggiorna del nostro team la company Brain,"* — introduce il caso d'uso team (più persone che aggiornano lo stesso cervello).

### Scena 268 · `frame-1104.png` · 110:18
Talking head, stessa inquadratura; mani vicine al petto, gesto di raccogliere/stringere.
Voce: *"questo folder è aggiornato e abbiamo un'unica verità, un'unica source of"* — il concetto di "source of truth" unica per il team.

### Scena 269 · `frame-1105.png` · 110:24
Talking head, stessa inquadratura; mano sinistra alzata con una penna/stilo bianco tra le dita.
Voce: *"truth. Ok? E quindi andiamo lì dentro, prendiamo quello e lo portiamo poi nel"* — completa il concetto di source of truth, introduce il gesto di "tirare giù" i dati aggiornati.

### Scena 270 · `frame-1106.png` · 110:30
Talking head, stessa inquadratura, sguardo abbassato verso il basso.
Voce: *"nostro computer e diciamo "Ok, ho il file aggiornato". Ok? Quindi tutti"* — chiude l'esempio del recupero dati aggiornati dal cloud.

### Scena 271 · `frame-1107.png` · 110:36
Talking head, stessa inquadratura; entrambe le mani sollevate ai lati del volto, gesticolando.
Voce: *"Github o che voi utilizziate Google Drive, la realtà è che vabbè, Gitub è più tecnico, scala meglio, però cambia"* — mette a confronto GitHub e Google Drive come alternative equivalenti.

### Scena 272 · `frame-1108.png` · 110:42
Talking head, inquadratura leggermente più stretta (zoom in, si vede la maglietta aperta sul collo), mano destra chiusa a pugno vicino al microfono.
Voce: *"relativamente poco e ehm avete comunque un posto in cui potete fare la"* — continua il confronto GitHub/Google Drive.

### Scena 273 · `frame-1110.png` · 110:54
Talking head, stessa inquadratura; una mano (sfocata) visibile al bordo sinistro del frame.
Voce: *"varie ehm versioni del vostro progetto e poi potrete tornare a quella precedente"* — spiega il concetto di version control (tornare a versioni precedenti).

### Scena 274 · `frame-1111.png` · 111:00 — profilo GitHub reale "Giobebbe" ⭐
Browser, **github.com/Giobebbe**. Header: menu hamburger, logo GitHub, username **"Giobebbe"**, tab "Overview", "Repositories 16", "Projects", "Packages", "Stars". Colonna sinistra: foto profilo (uomo sorridente, capelli castani), nome "Giobebbe", pulsante "Edit profile", "2 followers · 0 following". Colonna destra, "Popular repositories" (link "Customize your pins"), quattro riquadri repo:
- **second-brain-os-template** (Public template) — *"Second Brain OS template: a preconfigured Obsidian + Claude Code vault for solopreneurs and content creators"* — ⭐ 7
- **Story** (Public) — *"My first exercise with GitHub"*
- **horizon-ai-glasses** (Public) — TypeScript
- **claude-code-mastery** (Public) — HTML
- **roi-voice-ai-calculator** (Public) — CSS
- **website-stitch** (Public) — HTML
Sotto: "160 contributions in the last year", heatmap dei contributi (righe Mon/Wed/Fri, colonne Jun→May) quasi tutta scura/vuota fino a circa febbraio 2026, poi un blocco fitto di quadratini verdi da febbraio a maggio; tab anno "2026" selezionato (blu), poi "2025", "2024"; link "Learn how we count contributions".
➕ Il pattern della heatmap (attività concentrata solo negli ultimi mesi) suggerisce che l'autore ha ripreso/intensificato l'uso di questo account GitHub solo di recente; non è detto a voce.
Voce: *"quando volete. Una volta che è stato fatto, allora voi potrete vedere che nelle vostre repository avrete, eccoci qui, il nostro Aurora Cervello."* — arriva esattamente sulla repository che sta per aprire.

### Scena 275 · `frame-1113.png` · 111:12 — repo `aurora-cervello`, commit "Bootstrap" già fatto ⭐
Browser, **github.com/Giobebbe/aurora-cervello**, vista file scrollata: cartelle `outputs`, `projects`, `self`, `sources`, `workspace`, poi file `.gitignore`, `_index-aurora.md`, `gate_qualita.py`, `genera_llms.py`, `genera_showcase.py`, `llms.txt` — tutte le righe mostrano lo stesso messaggio di commit **"Bootstrap del cervello a 11 cartelle: note + grafo Obsidian"** e lo stesso orario relativo **"4 minutes ago"**, a conferma che il commit del Prompt 9 è stato eseguito esattamente col messaggio previsto. Sotto, sezione "README" non ancora presente: icona libro, testo "Add a README with an overview of your project.", pulsante verde "Add a README".
Sidebar destra: link troncato "Publish your first package" (in alto), "Contributors 1" con avatar "Giobebbe", "Languages" (barra blu piena, "Python 100.0%"), "Suggested workflows" — **SLSA Generic generator** ("Generate SLSA3 provenance for your existing release workflows", pulsante "Configure"), **Python package** ("Create and test a Python package on multiple Python versions", pulsante "Configure"), **Pylint** ("Lint a Python application with pylint.", pulsante "Configure"), link "More workflows" / "Dismiss suggestions".
Voce: *"nostro Aurora Cervello, se noi entriamo, ha esattamente tutto quello che abbiamo già ehm utilizzato e di cui abbiamo"* — entra nella repo e conferma che il contenuto corrisponde a quanto già costruito.

### Scena 276 · `frame-1114.png` · 111:18 — repo privata, branch `feature/wave-01`, 1 commit ⭐
Browser, github.com/Giobebbe/aurora-cervello. Nav orizzontale: Code, Issues, Pull requests, Agents, Actions, Projects, Security and quality, Insights, Settings. Intestazione repo: **"aurora-cervello"** con badge **"Private"** (lucchetto), pulsanti "Watch 0", "Fork 0", "Star 0". Selettore branch **"feature/wave-01"**, "1 Branch", "0 Tags", campo "Go to file", pulsante "Add file", pulsante verde "Code".
Riga di stato commit: "Giobebbe — Bootstrap del cervello a 11 cartelle: note + grafo Obsidian" · hash **"42c675e"** · "4 minutes ago" · badge **"1 Commit"** (cursore del mouse sopra).
Elenco cartelle, tutte con lo stesso commit e lo stesso orario: `_showcase`, `areas`, `code`, `concepts`, `data`, `docs`, `entities` (e altre sotto, non visibili nel frame).
Sidebar destra: "About" — "No description, website, or topics provided."; "Releases" — "No releases published" (link "Create a new release"); "Packages" — "No packages published" (link "Publish your first package"); "Contributors 1" con avatar Giobebbe.
Voce: *"già ehm utilizzato e di cui abbiamo parlato. C'è stato fatto un commit, quindi una fotografia poco fa ed eccoci"* — conferma a voce che il commit ("la fotografia") è stato appena fatto.

### Scena 277 · `frame-1116.png` · 111:30 — diff del commit, `.gitignore` generato per intero ⭐
Browser, github.com/Giobebbe/aurora-cervello/commit/42c675e7ed8fa83797aaf98defcd3f5224e8d011. Heading "Commit 42c675e", "Giobebbe committed 5 minutes ago". Riquadro messaggio: "Bootstrap del cervello a 11 cartelle: note + grafo Obsidian". Riga info: badge "feature/wave-01", "0 parents · commit 42c675e" (icona copia), **"50 files changed"**, "+1,638" (conteggio verde, nessuna cancellazione mostrata).
Banner di avviso arancione: **"⚠ Some content is hidden"** / "Large Commits have some content hidden by default. Use the searchbox below for content that may be hidden."
Pannello sinistro "Filter files" con albero: `.gitignore`, `_index-aurora.md`, `_showcase` (espansa, `showcase.md`), altri file sotto non visibili.
Diff mostrato per **`.gitignore`** (badge verde "+21"):
```
@@ -0,0 +1,21 @@
+ # === Segreti: MAI versionare ===
+ .env
+ .env.*
+ *.key
+
+ # === Obsidian: stato UI locale (non versionare) ===
+ .obsidian/workspace.json
+ .obsidian/workspace-mobile.json
```
(la riga 8 è tagliata in fondo al frame, il file continua oltre le 21 righe dichiarate).
Voce: *"esattamente quello che è stato cambiato. Vedete quindi che qui posso tornare a"* — sta mostrando esattamente questo diff.

### Scena 278 · `frame-1117.png` · 111:36 — cronologia commit, data "Jun 10, 2026" ⭐
Browser, github.com/Giobebbe/aurora-cervello/commits/feature/wave-01/. Heading "Commits", selettore branch "feature/wave-01", filtri "All users" / "All time". Elenco: sezione **"Commits on Jun 10, 2026"**, un solo commit — "Bootstrap del cervello a 11 cartelle: note + grafo Obsidian", "Giobebbe committed 5 minutes ago", hash "42c675e" (icone copia e "view code").
➕ La data "Jun 10, 2026" è la data reale (di sistema o di scena) in cui è stato girato/simulato questo passaggio del tutorial.
Voce: *"versioni precedenti e fare tutto quello che abbiamo che abbiamo detto di nuovo. Se volete un corso per capire meglio"* — chiude il blocco GitHub rimandando a un corso dedicato sul suo canale.

### Scena 279 · `frame-1121.png` · 112:00 — pannello "Claude Code" dentro Antigravity ⭐
Editor Antigravity, stesso Explorer di sempre (root "aurora cervello": _showcase espansa con showcase.md, areas, code, concepts, data, docs, entities, outputs, projects, self, sources, workspace, poi _index-aurora.md, `.env` evidenziato, `.gitignore`, gate_qualita.py, genera_llms.py, genera_showcase..., llms.txt). Tab aperta **"Claude Code"** (con "Untitled" sotto), corpo centrale: logo/heading **"💥 Claude Code"**, sotto una piccola icona pixel-art arancione (creatura/granchio stilizzato), testo: *"Use planning mode to talk through big changes before a commit. Press [Shift][Tab] to cycle between modes."* In basso, campo input *"⌘ Esc to focus or unfocus Claude"* con icona microfono, chip ".env", pulsante "Bypass permissions", freccia di invio rossa. Barra di stato: "Screen Reader Optimized" / "Antigravity - Settings".
➕ Conferma che dentro l'IDE "Antigravity" viene aperto un pannello dedicato letteralmente etichettato **"Claude Code"**: i due strumenti convivono nella stessa finestra.
Voce: *"quanto è accurato. Allora, [sbuffare] ovviamente abbiamo la nostra cosa,"* — sta per avviare la piccola demo di interrogazione del cervello.

## Prompting del cervello, e miglioramento continuo (112:15 → 117:59)

### Scena 280 · `frame-1126.png` · 112:30 — demo live: query ARR con fonti citate e rifiuto corretto ⭐
Stesso editor, nuova tab **"Query Aurora ARR and headcount changes"**. Messaggio utente (in alto, testo attenuato): "Rispondi alla mia domanda usando SOLO il contenuto di queste note." — "- Cita sempre il nome del file da cui prendi ogni informazione." (righe successive coperte).
Risposta dell'assistente, passo per passo:
"Thought for 1s"
🔧 **Bash: Search for multi-year headcount history**
IN: `cd '/Users/giovannibeggiato/Desktop/aurora cervello' && grep -rin -e "organico" -e "persone" -e "dipendent" -e "team" -e "cresci" -e "fonda[to]"` (comando tagliato a destra)
OUT: `areas/area-customer-success.md:16: Funzione continua responsabile di onboarding, supporto e crescita dei clienti esistenti di [[self-identit[à]]]...` / `projects/progetto-arr-5m-2026.md:20:- **Leve**: nuovi loghi da [[area-vendite]] + espansione sui clienti esistenti da [[area-customer-succe[ss]]]...` / `areas/area-finance-operations.md:21: il custode dei numeri: ARR, churn, NRR e la riconciliazione con la contabilità presentata al Board. A[...]` (righe tagliate a destra)
"Thought for 2s"
**"ARR di Aurora"** — "A fine 2025 l'ARR di Aurora è **€ 3.840.000**, in crescita del **+24% (+€ 740.000)** rispetto ai € 3.100.000 di inizio 2025. (file: `kpi-2025-arr.md`; confermato anche in `area-finance-operations.md`)"
**"Come è cambiato l'organico negli ultimi tre anni"** — **"Non presente nel cervello."** "Le note riportano solo l'organico attuale (**47 persone** su due sedi Milano e Bologna) e il piano di **+6 assunzioni** approvato per il 2026 (file: `area-people-cultura.md`, `canon.md`). Non c'è alcuno storico dell'organico sui tre anni precedenti."
➕ Il percorso di sistema `/Users/giovannibeggiato/Desktop/aurora cervello` conferma il nome completo dell'autore (Giovanni Beggiato) e che il vault vive su macOS.
Voce: *"Aurora è di 3.8 milioni in crescita di rispetto ai del eh di inizio 2025 e e mi"* — legge a voce lo stesso numero appena mostrato a schermo, confermando che la demo risponde correttamente rispettando la regola "solo dalle note, altrimenti dillo".

### Scena 281 · `frame-1129.png` · 112:48 — Prompt 13 e 14: apertura/chiusura sessione (diario) ⭐
Notion, stessa pagina "Company Brain — Tutti i prompt del...", scrollata più in basso. In cima, tagliata dal bordo superiore del frame, un'intestazione 🔎 parzialmente leggibile — dal sottotitolo sotto e dalla numerazione successiva è ricostruibile come **"Prompt 13 — Apri la sessione (il briefing)"** — sottotitolo pienamente leggibile: "A inizio giornata, fai riprendere il filo al cervello dal diario dell'ultima volta." Riquadro codice:
"Buongiorno. Apriamo la sessione di lavoro sul cervello di Aurora.
Leggi l'indice llms.txt e l'ultima nota dentro workspace/journal/sessions/ (il diario dell'ultima volta).
Poi dammi un briefing in 5 righe:
- dove eravamo rimasti, dal diario;
- cosa era rimasto aperto;
- cosa conviene affrontare oggi, in ordine di priorità.
Non scrivere ancora niente nel cervello. Solo il briefing."
Sotto, intestazione **"Prompt 14 — Chiudi la sessione (il diario)"**, sottotitolo "A fine giornata, fai scrivere al cervello la nota di sessione, agganciata alle entità vere toccate." Riquadro codice:
"Chiudiamo la sessione di oggi. Scrivi la nota di diario nel cervello.
- Cartella: workspace/journal/sessions/
- Nome file: sessione-<data di oggi> (esempio: sessione-2026-06-09)
- In cima il frontmatter: title, summary (UNA frase su cosa abbiamo fatto oggi), tags (il primo è workspace/session), status: done, created e updated con la data di oggi, e related su una riga coi wikilink alle note toccate.
- Corpo in tre sezioni brevi:
  ## Fatto — cosa abbiamo concluso oggi
  ## Deciso — le scelte prese e il perché
  ## Aperto — cosa resta in sospeso per domani
- Aggancia la nota alle entità vere toccate oggi coi [[wikilink]] (i clienti, i KPI, i progetti). Mai una nota di diario sciolta nel vuoto.
Prima dimmi in 3 righe cosa hai capito che abbiamo fatto oggi. Al mio ok, scrivi."
Voce: *"abbiamo in previsione. Ok. Il secondo prompt che voglio farvi vedere è questo."* — la voce si riferisce ancora alla demo del Prompt 10 in corso; questi Prompt 13/14 sono solo visibili di striscio mentre scorre la pagina.

### Scena 282 · `frame-1130.png` · 112:54 — Prompt 11 e Prompt 12 (cruscotto HTML) ⭐
Stessa pagina Notion, scrollata più in alto rispetto alla scena precedente (mostra i prompt in ordine crescente). In cima, coda del Prompt 10: "- Se la risposta non è presente nelle note, scrivi esattamente: "Non presente nel cervello." Non inventare, non stimare, non dedurre." poi "Domanda: qual è l'ARR di Aurora e come è cambiato l'organico negli ultimi tre anni?"
Intestazione **"Prompt 11 — La domanda di incrocio (dove le cartelle si arrendono)"**, sottotitolo "Due fatti in due note diverse: la risposta si costruisce camminando sui collegamenti." Riquadro codice:
"Rispondi usando SOLO le note del cervello di Aurora.
- Cita sempre il nome del file da cui prendi ogni informazione.
- Elenca SOLO i clienti che hanno DAVVERO tutti e due i prodotti. Se un cliente ne ha uno solo, lascialo fuori.
- Se la risposta non è nel cervello, scrivi: "Non presente nel cervello."
Domanda: quali clienti hanno attivato sia Aurora Cloud sia Aurora Care, e chi li segue nel customer success?"
Intestazione **"Prompt 12 — Il cruscotto HTML locale"**, sottotitolo "Un singolo file HTML offline da aprire con un doppio click: il biglietto da visita per una demo." Riquadro codice:
"Genera un cruscotto HTML statico dai dati del canon: gli indicatori dell'ultimo mese, i grafici di andamento (fatturato, organico, edifici), la classifica clienti e l'organico per reparto. Tutto in un solo file .html che apre con un doppio click, offline e senza account."
Sotto, intestazione dell'inizio di "Prompt 13 — [...]efing)" coperta da un tooltip nero **"Copied code to clipboard"** (conferma che un blocco di codice è stato appena copiato).
Voce: *"Eccoci qui, dove rispondiamo ad ehm una domanda, ok? In una maniera un po' più"* — introduce la domanda "di incrocio" (Prompt 11) che sta per lanciare.

### Scena 283 · `frame-1131.png` · 113:00
Stessa vista "Query Aurora ARR and headcount changes" della scena 280 (stessa risposta ARR + organico già descritta), ora con in più un riquadro di input vuoto bordato di rosso e attivo sotto la risposta, pronto per il prossimo prompt.
Voce: *"complessa. Quindi, sostanzialmente, quello che andiamo a fare è e ora fatemi pulire la conversazione, è andare dentro"* — annuncia che sta per ripulire la chat e iniziare una nuova conversazione per il prompt successivo.

### Scena 284 · `frame-1132.png` · 113:06 — Prompt 11 incollato, pronto per l'invio ⭐
Nuova tab **"Claude Code"** (schermata di reset, stessa icona pixel-art arancione di scena 279 ma testo placeholder diverso: **"// TODO: Everything. Let's start."**). Sotto, riquadro bordato di rosso col **Prompt 11 completo** già incollato, identico a quello letto in scena 282:
"Rispondi usando SOLO le note del cervello di Aurora.
- Cita sempre il nome del file da cui prendi ogni informazione.
- Elenca SOLO i clienti che hanno DAVVERO tutti e due i prodotti. Se un cliente ne ha uno solo, lasciolo fuori.
- Se la risposta non è nel cervello, scrivi: "Non presente nel cervello."
Domanda: quali clienti hanno attivato sia Aurora Cloud sia Aurora Care, e chi li segue nel customer success?"
Voce: *"a ehm i vari i vari nodi. Quindi, rispondi utilizzando solo le note del"* — sta dettando/leggendo lo stesso prompt appena incollato.

### Scena 285 · `frame-1135.png` · 113:24 — stato di elaborazione "Discombobulating..." ⭐
Nuova tab **"Query Aurora customer pr[oduct adoption]..."**. Messaggio utente: chip ".env", "Rispondi usando SOLO le note del cervello di Aurora." poi pulsante grigio **"Show more"** che nasconde il resto del prompt (si intravede appena, sotto il pulsante, l'inizio di "Cita sempre il nome del file da cui prendi ogni informazione"). Sotto, indicatore di stato con icona rossa: **"🔺 Discombobulating..."** (etichetta scherzosa usata dal tool per il proprio "sto pensando", al posto del classico "Thinking..."). In fondo, campo "Queue another message..." e un pulsante rosso quadrato (stop, generazione in corso).
➕ "Discombobulating..." è un dettaglio di branding/microcopy dello strumento (Antigravity/Claude Code), non spiegato a voce.
Voce: *"segue nel Customer Success? Vedete ora e poi parleremo di architettura. Eh già"* — ha appena lanciato la domanda e anticipa che dopo la demo parlerà di architettura RAG.

### Scena 286 · `frame-1144.png` · 114:18 — nota atomica reale: `prodotto-aurora-access.md` ⭐
Vista divisa in due pannelli. Sinistra: tab "Query Aurora customer pr...", Explorer con la cartella `entities` espansa: `_index-entities.md`, `cliente-banca-a[driatica].md`, `cliente-hoteline-[hospitality].md`, `cliente-immobil[iare-lombarda].md`, `persona-chiara-f[ontana].md`, `persona-elena-f[erraro].md`, `persona-giulia-ri[naldi].md`, `persona-marco-...[bianchi].md`, tre file `prodotto-aurora...` (uno evidenziato), `strumento-crm-...md`. Nella chat: "Rispondi usando SOLO le note del cervello di Aurora." poi riferimenti file "./_showcase/showcase.md" / "./areas/_index-areas.md", "Thought for 1s", 🔧 **Bash: Search notes for Aurora Cloud and Aurora Care** con OUT "(Bash completed with no output)", "Thought for 2s", risposta: "Ho cercato in tutte le note del cervello di Aurora i prodotti citati nella domanda. I prodotti registrati nel cervello sono solo tre: **Aurora Access, Aurora Core e Aurora Energy**. Né "Aurora Cloud" né "Aurora Care" compaiono in alcuna nota. **Non presente nel cervello.**" In basso, messaggio in digitazione: "[e se io t]i facessi la domanda invece sui prodotti di cui siamo proprietari, [quindi] Access, Core ed Energy?"
Destra: tab **`prodotto-aurora-access.md`** aperta, frontmatter e corpo per intero:
```
---
title: "Prodotto — Aurora Access"
summary: "Modulo di controllo accessi (badge, fasce orarie, videosorveglianza) per gestire la sicurezza di molte sedi da un unico punto."
tags: [entities, prodotto, aurora-access]
status: active
created: 2026-06-10
updated: 2026-06-10
related:
  - "[[prodotto-aurora-core]]"
  - "[[area-prodotto-engineering]]"
  - "[[area-customer-success]]"
---

# Prodotto — Aurora Access

Modulo che si appoggia a [[prodotto-aurora-core]] per il controllo degli accessi agli edifici: badge, permessi per fasce orarie, integrazione con la videosorveglianza. Pensato per chi deve gestire la sicurezza di molte sedi da un unico punto.

- **Costruito da**: [[area-prodotto-engineering]].
- **Upsell dell'anno 2025**: estensione a tutte le filiali di Banca Adriatica, seguita da [[area-customer-success]].
- **Usato da**: Gruppo Retail, Rete Sanità Nord, UniCampus, Banca Adriatica.
```
Voce: *"vedete che io riesco effettivamente a verificare che non abbiamo alcuna"* — commenta dal vivo il fatto che il cervello non trova "Aurora Cloud"/"Aurora Care" perché non esistono davvero.

### Scena 287 · `frame-1145.png` · 114:24 — comando bash reale usato per la ricerca ⭐
Stesso tab, ora a pannello singolo. Si vede il comando bash completo della ricerca appena eseguita:
`cd "/Users/giovannibeggiato/Desktop/aurora cervello" && grep -rln -i "aurora cloud\|aurora care" --include="*.md" .`
OUT: `(Bash completed with no output)` — poi la stessa risposta di scena 286 ("I prodotti registrati... Non presente nel cervello."), seguita dal nuovo messaggio utente già inviato: "e se io ti facessi la domanda invece sui prodotti di cui siamo proprietari, quindi Access, Core ed Energy?", "Thought for 2s", e l'inizio (tagliato in fondo al frame) di un nuovo blocco "🔧 Bash: Re[ad client, CS area, and persona notes]".
Voce: *"gli abbiamo dato. E guardate che senza"* — introduce l'idea che senza un'architettura corretta il sistema "si sponna" (si confonde).

### Scena 288 · `frame-1147.png` · 114:36 — grep sulle note clienti, tre profili a confronto ⭐
Stesso tab, scrollato: "🔧 Bash: Read client, CS area, and persona notes":
IN: `cd "/Users/giovannibeggiato/Desktop/aurora cervello" && for f in entities/cliente-banca-adriatica.md entities/cliente-hotelline-hosp[itality.md ...]` (comando tagliato a destra)
OUT: `===== entities/cliente-banca-adriatica.md ===== --- title: "Cliente — Banca Adriatica"` (tagliato)
"Thought for 16s", poi:
"Applicando la stessa regola stretta (un cliente conta solo se ha davvero tutti i prodotti citati), ecco cosa dicono le note.
Moduli attivi per cliente:
- cliente-banca-adriatica.md: Core, Access, Manutenzione → ha Core + Access, manca Energy.
- cliente-hotelline-hospitality.md: Core, Energy → ha Core + Energy, manca Access.
- cliente-immobiliare-lombarda.md: Core, Energy, Manutenzione, Insights → ha Core + Energy, manca Access.
Clienti con tutti e tre (Access + Core + Energy): nessuno."
Sotto, stato di elaborazione: **"🔺 Germinating..."**
Voce: *"Non ho idea da dove venga, non so neanche se sia offensivo."* — battuta fuori tema sul proprio accento, mentre il sistema sta ancora elaborando.

### Scena 289 · `frame-1152.png` · 115:06 — Chiara Fontana emerge come referente comune ⭐
Stesso tab, risposta precedente scrollata per intero, con una riga evidenziata/selezionata in blu: *"Se invece intendevi "almeno due dei tre", allora tutti e tre i clienti si qualificano, e nel customer success:"* — e sotto, tagliato in fondo, l'inizio dell'elenco clienti (visibile per intero nella scena successiva).
Voce: *"conta solo se hai davvero tutti i prodotti citati. Ecco cosa dicono le"* — legge a voce la regola appena applicata dal sistema.

### Scena 290 · `frame-1155.png` · 115:24 — risposta completa + nuova domanda su ARR per impiegato ⭐
Stesso tab, ora con l'elenco leggibile per intero:
"Se invece intendevi "almeno due dei tre", allora tutti e tre i clienti si qualificano, e nel customer success:
- **Banca Adriatica** (Core + Access) → seguita da **Chiara Fontana** (persona-chiara-fontana.md, area-customer-success.md).
- **Immobiliare Lombarda SGR** (Core + Energy) → seguita da **Chiara Fontana** (stesse fonti).
- **HotelLine Hospitality** (Core + Energy) → nessun referente di customer success indicato nelle note (acquisita da Vendite, onboarding chiuso a ottobre). Chi la segua nel CS: **Non presente nel cervello.**"
Nuovo messaggio utente (con chip file "prodotto-aurora-access.md"): **"Hey, c'è un modo di identificare quale degli impiegati porta il maggior ARR?"** Sotto: "Thinking... · 20 tokens", poi stato **"🔺 Ruminating..."**.
➕ Tre diciture di "sto pensando" diverse osservate finora in questo blocco (scene 285, 288, 290): **"Discombobulating..."**, **"Germinating..."**, **"Ruminating..."** — sembra che il tool ruoti etichette scherzose casuali invece di un semplice "Thinking...".
Voce: *"sostanzialmente chiamiamo e c'è un modo di identificare eh quale degli impiegati porta il maggior ARR."* — corrisponde esattamente alla domanda appena digitata a schermo.

### Scena 291 · `frame-1156.png` · 115:30 — nota atomica reale: `persona-marco-bianchi.md` ⭐
Vista divisa in due pannelli. Sinistra: tab "Query Aurora customer pr...", risposta precedente (clienti Access+Core+Energy, scena 290 di parte-C) ancora visibile sopra il campo "Queue another message...". Explorer con cartella `entities` espansa, file `persona-marco-bianchi.md` evidenziato. Destra: tab `persona-marco-bianchi.md` aperta, frontmatter e corpo per intero:
```
---
title: "Persona — Marco Bianchi (CTO)"
summary: "CTO e co-fondatore di Aurora Sistemi, responsabile di Prodotto & Engineering."
tags: [entities, persona, founder, cto]
status: active
created: 2026-06-10
updated: 2026-06-10
related:
  - "[[area-prodotto-engineering]]"
  - "[[prodotto-aurora-core]]"
  - "[[persona-elena-ferraro]]"
---

# Persona — Marco Bianchi (CTO)

Co-fondatore e direttore tecnico di Aurora Sistemi. Come [[persona-elena-ferraro|Elena Ferraro]], viene dall'ingegneria degli impianti, insieme dal 2018.

- **Ruolo**: responsabile di [[area-prodotto-engineering]] — sviluppo della piattaforma e di tutti i moduli, a partire da [[prodotto-aurora-core]].
- **Riporti tecnici**: Luca Esposito (Engineering Lead, Core) e Paolo Marchetti (PM, Energy).
```
La barra di stato mostra "Ln 18, Col 134 (9 selected)": il puntatore ha appena selezionato il link `aurora-core` nella riga del "Ruolo".
Voce: *"saranno collegate con altre, diciamo,"* — mentre mostra un'altra nota di persona, spiega che questi nodi persona si collegano ad altri nodi (prodotti, aree) dentro al grafo.

### Scena 292 · `frame-1157.png` · 115:36 — lettura KPI ARR e clienti attivi ⭐
Stesso tab "Query Aurora customer pr...", a pannello singolo, scrollato. Messaggio utente ripetuto per contesto: "e se io ti facessi la domanda invece sui prodotti di cui siamo proprietari, quindi Access, Core ed Energy?" seguito dalla risposta con l'elenco clienti (Banca Adriatica, Immobiliare Lombarda SGR, HotelLine Hospitality) già letta nelle scene precedenti. Nuovo messaggio utente con chip file "prodotto-aurora-access.md": **"Hey, c'è un modo di identificare quale degli impiegati porta il maggior ARR?"**
"Thought for 3s", poi 🔧 **Bash: Read ARR, active clients, and sales notes**
IN: `cd "/Users/giovannibeggiato/Desktop/aurora cervello" && for f in data/kpi-2025-arr.md data/kpi-2025-clienti-attivi.md area[...]` (comando tagliato a destra)
OUT: `===== data/kpi-2025-arr.md ===== title: "KPI 2025 — ARR totale"`
Sotto: "Thinking... · 30 tokens", poi stato **"🔺 Forming..."**.
Voce: *"eventualmente andranno a connettersi con KPI e quindi ora sappiamo Eccoci qui."* — corrisponde esattamente a quanto appena mostrato: i nodi persona che si connettono ai dati KPI.

### Scena 293 · `frame-1160.png` · 115:54 — risposta completa: Chiara Fontana porta il maggior ARR ⭐
Stesso tab, risposta scrollata per intero:
"Sì, ma solo in modo parziale, perché il cervello documenta l'ARR di **3 clienti su 9**. Per gli altri 6 i canoni non sono nelle note (kpi-2025-arr.md dice solo che la somma dei 9 quadra a € 3.840.000).
**Metodo**: l'unico impiegato legato esplicitamente a clienti con ARR noto è **Chiara Fontana (CSM)**, che "segue" due key account. Sommo l'ARR dei clienti assegnati a ciascuna persona nominata.
Attribuzione per persona (solo clienti documentati):
- **Chiara Fontana** (persona-chiara-fontana.md)
  - Banca Adriatica → € 520.000 (cliente-banca-adriatica.md)
  - Immobiliare Lombarda SGR → € 720.000 (cliente-immobiliare-lombarda.md)
  - Totale: € 1.240.000
- **HotelLine** (€ 260.000, cliente-hotelline-hospitality.md): acquisita da area-vendite.md, ma nelle note **non è assegnata a una persona specifica** del customer success.
Risposta: in base al cervello, l'impiegata che porta il maggior ARR è **Chiara Fontana**, con € 1.240.000 di key account in gestione.
Due avvertenze importanti:
1. "Portare ARR" qui significa gestione/retention del cliente (ruolo del CS), non acquisizione: la vendita iniziale è di area-vendite.md. Le note non attribuiscono a nessun venditore un ARR per nome.
2. Mancano i dati di 6 clienti su 9, quindi non si può escludere che un altro impiegato gestisca account più grandi. Per quei clienti: **Non presente nel cervello.**"
Voce: *"esplicitamente eh a clienti con AR noto"* — legge a voce lo stesso passaggio del "Metodo" appena apparso a schermo.

### Scena 294 · `frame-1164.png` · 116:18 — reset della chat, nuova conversazione ⭐
Tab **"Claude Code"** rinominata "Untitled", schermata di reset identica nello stile alle scene 279/284 (icona pixel-art arancione, ora con corpo pieno invece del contorno), messaggio placeholder: **"You've come to the absolutely right place!"** Campo di input vuoto bordato di rosso in basso.
Voce: *"Ehi, guardando al mio database in una"* — inizia a dettare la nuova domanda sulle informazioni mancanti, mentre la chat è ancora vuota.

### Scena 295 · `frame-1172.png` · 117:06 — esplorazione completa del vault: elenco di tutti i file ⭐
Nuova tab **"Identify missing databas..."**. Messaggio utente con chip file "persona-marco-bianchi.m...": **"Ehi, guardando al mio database in una tabella abbastanza schematica, riesci a dirmi quali sono le informazioni mancanti per riuscire a farli delle analisi complete?"**
Risposta: "Ti aiuto. Per dirti cosa manca, prima devo vedere cosa c'è. Esploro il database."
🔧 **Bash: List all vault files**
IN: `cd "/Users/giovannibeggiato/Desktop/aurora cervello"`
OUT (elenco completo, un file per riga): `./.DS_Store`, `./.env`, `./.gitignore`, `./_index-aurora.md`, `./_showcase/showcase.md`, `./areas/.DS_Store`, `./areas/_index-areas.md`, `./areas/area-customer-success.md`, `./areas/area-finance-operations.md`, `./areas/area-marketing.md`, `./areas/area-people-cultura.md`, `./areas/area-prodotto-engineering.md`, `./areas/area-vendite.md`, `./code/_index-code.md`, `./code/code-export-crm.md`, `./concepts/_index-concepts.md`, `./concepts/concetto-arr.md`, `./concepts/concetto-churn.md`, `./concepts/concetto-efficienza-energetica.md`, `./data/_index-data.md`, `./data/kpi-2025-arr.md`, `./data/kpi-2025-churn.md`, `./data/kpi-2025-clienti-attivi.md`, `./data/kpi-2025-edifici.md`, `./data/kpi-2025-nrr.md`, `./docs/_index-docs.md`, `./docs/doc-onboarding-cliente.md`, `./entities/_index-entities.md`, `./entities/cliente-banca-adriatica.md`, `./entities/cliente-hotelline-hospitality.md`, `./entities/cliente-immobiliare-lombarda.md`, `./entities/persona-chiara-fontana.md`, `./entities/persona-elena-ferraro.md`, `./entities/persona-giulia-rinaldi.md`, `./entities/persona-marco-bianchi.md`, `./entities/prodotto-aurora-access.md`, `./entities/prodotto-aurora-core.md`, `./entities/prodotto-aurora-energy.md`, `./entities/strumento-crm.md`.
"Thought for 1s" — "Aurora è il caso di studio. Leggo le entità chiave: persone (dipendenti), clienti, prodotti, KPI e aree."
🔧 **Bash: Read all entity files**
IN: `cd "/Users/giovannibeggiato/Desktop/aurora cervello"`
OUT (inizio): `===== entities/persona-chiara-fontana.md ===== --- title: "Persona — Chiara Fontana (Customer Success M[...]`
Voce: *"tabella abbastanza schematica, riesci a"* — corrisponde letteralmente al testo appena digitato a schermo, letto mentre appare.

### Scena 296 · `frame-1174.png` · 117:18 — seconda lettura: KPI, aree, export CRM, progetto ⭐
Stesso tab, scrollato. OUT precedente continua: `===== entities/persona-chiara-fontana.md ===== --- title: "Persona — Chiara Fontana (Customer Success Manager)"`.
"Thought for 1s" — "Ora leggo KPI, aree, l'export CRM e il progetto, così vedo la parte numerica e organizzativa."
🔧 **Bash: Read KPIs, areas, project, crm export, identity**
IN: `cd "/Users/giovannibeggiato/Desktop/aurora cervello" && for f in data/kpi-*.md areas/area-*.md projects/progetto-arr-5m-20[26...]` (comando tagliato a destra)
OUT: `===== data/kpi-2025-arr.md ===== --- title: "KPI 2025 — ARR totale"`
Sotto: "Thinking... · 16 tokens", poi stato **"🔺 Wandering..."**.
Voce: *"eventualmente andranno a connettersi con KPI"* (ripetizione/prosecuzione della frase di scena 292, il parlato scorre più lento del testo a schermo che nel frattempo è già avanzato).

### Scena 297 · `frame-1176.png` · 117:30 — output bash sull'area vendite e sul progetto ARR 5M ⭐
Vista divisa. Sinistra: stesso tab "Identify missing databas...", indicatore "Thinking... · 857 tokens" poi stato **"🔺 Computing..."**. Destra: pannello "Bash tool output" scrollato, si legge per intero:
`...funzione continua responsabile dell'acquisizione...`
`- **A capo**: Davide Conti (VP Sales), riporta`
`- **Account Executive**: Matteo Russo.`
`- **Dimensioni**: ~7 persone.`
`## Come lavora`
`Riceve i lead da [[area-marketing]] e porta sul[...]`
`_Hub di reparto. Le note di dettaglio su client[i...]`
`===== projects/progetto-arr-5m-2026.md =====`
```
title: "Progetto — ARR oltre 5 milioni nel 2026"
summary: "L'obiettivo approvato dal Board per i[l...]"
tags: [projects, obiettivo, anno/2026, channel/...]
status: in-progress
created: 2026-06-10
updated: 2026-06-10
related:
  - "[[kpi-2025-arr]]"
  - "[[area-vendite]]"
  - "[[area-customer-success]]"

# Progetto — ARR oltre 5 milioni nel 2026

Obiettivo annuale approvato dal CdA il 22/01/20[26...]

- **Target**: [[kpi-2025-arr|ARR]] oltre € 5.00[0.000...]
- **Vincoli di qualità**: NRR sopra il 110%, ch[urn...]
- **Leve**: nuovi loghi da [[area-vendite]] + e[spansione...]
- **Abilitatore organico**: +6 assunzioni 2026,

Stato: in corso (anno fiscale 2026).

===== code/code-export-crm.md =====
title: "Script — Export CRM clienti"
```
Voce: *"Non ho idea da dove venga, non so neanche se sia offensivo."* ⚠ nota: questa battuta (già citata in scena 288 di parte-C) non torna a questo timestamp nella trascrizione fornita in questo blocco — a 117:30 il transcript riporta invece la prosecuzione della spiegazione sui KPI; si segnala la voce effettivamente letta al minuto: *"connettersi con KPI e quindi ora sappiamo Eccoci qui. Perfetto."* (continuazione dello stesso passaggio delle scene 292/296).

### Scena 298 · `frame-1177.png` · 117:36 — stessa esplorazione, nuova etichetta di elaborazione ⭐
Stesso tab e stesso output della scena 297 (nessun avanzamento visibile nel testo), ma il contatore di pensiero è salito a "Thinking... · 1.3k tokens" e lo stato è ora **"🔺 Percolating..."**.
➕ Con questa scena si contano **cinque** etichette scherzose di "sto pensando" osservate in questo blocco di sistema RAG-demo: Discombobulating, Germinating, Ruminating (già in parte-C), più **Forming**, **Wandering**, **Computing**, **Percolating** (nuove, scene 292/296/297/298) — confermano che il tool ruota etichette casuali invece di un singolo "Thinking...".
Voce: *"perfetto. Ora un'altra cosa"* — introduce la richiesta di analisi sulle informazioni mancanti, chiudendo il tema precedente.

### Scena 299 · `frame-1179.png` · 117:48 — audit delle colonne mancanti nel database Aurora ⭐
Editor Antigravity (barra in basso: "Antigravity - Settings", non VS Code puro) con tab "Identify missing databas..." aperto sopra un file legato a `persona-marco-bianchi.m...`. Chat Claude in corso. Prompt utente in alto: *"Ehi, guardando al mio database in una tabella abbastanza schematica, riesci a dirmi quali sono le informazioni mancanti per riuscire a fargli delle analisi complete?"* Risposta con heading **"Il problema di fondo (è quello del "top employee")"**: "Il tuo cervello oggi è fotografico e descrittivo:" seguito da un passaggio evidenziato in blu (selezionato), poco leggibile per la compressione dello screenshot, che riporta in sostanza "dice benissimo com'è fatta Aurora oggi [...] quante ARR per cliente. Ma non risponde a cosa funziona meglio, cosa rende davvero, dove stai andando." ➕ testo esatto della selezione non del tutto verificabile. Poi testo pulito: "Per quelle analisi servono le cose che oggi mancano quasi ovunque: **una metrica per ogni unità** (persona, prodotto, cliente), **i costi** (non solo i ricavi), e **il tempo** (serie storiche, non una foto al 31/12)." Segue: "Il "top employee" è il sintomo perfetto: il database descrive ruoli e gerarchia, ma non attacca nessun numero alla singola persona. Solo Chiara ha un "colpo dell'anno" scritto, quindi sembra l'unica brava. Non è che sia la migliore: è l'unica misurata." Heading **"Cosa puoi GIÀ fare (così è chiaro il confine)"**: "Il database non è debole, è incompleto. Già oggi rispondi a: cliente più grande (Immobiliare Lombarda, 720k), cliente con più edifici (Gruppo Retail, 210), e la penetrazione dei moduli sui 9 clienti: Core 9/9, Energy 5/9, Manutenzione 5/9, Access 2/9. Quello che NON sai è quanto rende ciascun modulo, perché manca il prezzo." Heading **"Le colonne mancanti, tabella per tabella"**, sottosezione **"CLIENTI (oggi hai: settore, anno, immobil, ARR, moduli)"** con tabella a 2 colonne "Colonna da aggiungere" | "Cosa ti sblocca": riga 1 "ARR per ogni anno (storico)" → "espansione e NRR del singolo cliente: chi cresce, chi si sta spegnendo"; riga 2 tagliata in basso dalla finestra del chat input ("ARR diviso [...]" / "[...]200k tranquillo"). Barra inferiore del pannello chat: "⌘ Esc to focus or unfocus Claude", "2 lines selected", pulsante rosso invio, "Bypass permissions".
Voce: *"manca meglio dove sta andando. una metrica per ogni unità, i costi, il tempo, cosa puoi già fare, le colonne mancanti e quindi qui comincia a darvi anche degli insight su eh che cosa dovreste aggiungere perché lei possa cominciare questa AI a analizzare meglio i vostri dati"* — il narratore legge/parafrasa a voce l'output che scorre a schermo.

### Scena 300 · `frame-1182.png` · 118:06 — sezione "Dati che mancano del tutto" e migliorie strutturali
Stesso tab e stessa chat, scrollata più in basso. Heading **"Dati che mancano del tutto (tabelle nuove)"**: "Questi non sono colonne, sono interi pezzi di azienda assenti:" con lista numerata leggibile per intero:
1. "Conto economico / costi: vedi solo i ricavi (ARR). Zero costi, margine, EBITDA, cassa, runway. Oggi non puoi dire se Aurora guadagna."
2. "CAC, LTV, payback: quanto costa acquisire un cliente e in quanto tempo rientri. È il cuore di un SaaS e non c'è." (riga selezionata/evidenziata in blu)
3. "Pipeline e forecast 2026: l'obiettivo è 5M ma non esiste una pipeline che dica se raggiungibile o un sogno."
4. "Serie storica dei KPI 2018-2025: oggi hai due punti (inizio e fine 2025). Due punti non fanno una tendenza."
5. "Marketing a numeri: lead generati, costo per lead, conversione lead→cliente. Marketing è descritto ma senza una sola cifra."
6. "Concorrenti e win/loss: parli di "vecchi BMS" ma non c'è un concorrente nominato né perché vinci o perdi."
7. "People in numeri: turnover per reparto, tempo di assunzione, costo del lavoro per reparto."

Heading **"Migliorie strutturali (rendono le analisi automatiche)"**, punto 1: "Metti i numeri nel frontmatter come campi, non nella prosa. Oggi l'ARR è scritto "€ 720.000" dentro al testo: per sommarlo o filtrarlo serve farlo a mano. Se diventa un campo (`arr: 720000`, `settore: banca`), Obsidian con Dataview lo somma e filtra da solo. Esempio concreto: "tutti i clienti retail sopra 400k senza insights" diventa una query, non una rilettura a mano." Punto 2, in parte tagliato in fondo: "Schede che mancano: i 6 clienti senza nota (ci sono solo 3/9), i 2 prodotti senza nota (Manutenzione, Insights), e soprattutto Costruzioni Sud, il cliente perso: è la fonte più preziosa per capire perché si perde un cliente." Sotto, si intravede l'inizio del paragrafo successivo "Le mo[sse]" tagliato dalla finestra chat.
Voce: *"i vostri dati e a darvi anche degli insight per la vostra azienda maggiori, quindi per esempio KCK TV e tutte le le metriche e via dicendo. Quindi vedete quanto potente diventano questi strumenti nel momento in cui cominciamo ad utilizzarli nella maniera corretta con il contesto corretto."*

### Scena 301 · `frame-1184.png` · 118:18 — le 3 mosse che sbloccano l'80%
Stesso pannello, scroll ulteriore: in alto resta visibile la coda del blocco "Migliorie strutturali" (stessi due punti "Metti i numeri nel frontmatter..." e "Schede che mancano..." già letti in scena 300, ora interi). Nuovo heading **"Le 3 mosse che sbloccano l'80%"**: "Se fai solo tre cose, in ordine:"
1. "Prezzo per modulo sui clienti → sblocca ricavo per prodotto, attach rate a valore, e metà delle analisi commerciali."
2. "Una metrica di risultato per persona (almeno AE e CSM) → sblocca il "top employee" e la valutazione del team."
3. "I costi (conto economico base + RAL) → sblocca profittabilità, margine, ARR per dipendente: passi da "quanto fatturo" a "quanto guadagno"."

Chiude con la domanda del modello: "Vuoi che ti prepari lo schema dei campi nuovi (un template aggiornato per cliente/persona/prodotto) e le 8 schede mancanti come bozze da riempire?" Barra chat in basso: "⌘ Esc to attach selected text", "2 lines selected".
Voce: *"ora, prima di muoverci ulteriormente, ehm, volevo farvi una mini tabellina che voleva essere indicativa di, ehm, come dovrebbe funzionare."* — il narratore sta già introducendo l'argomento successivo (la tabellina) mentre a schermo è ancora visibile l'output precedente.

### Scena 302 · `frame-1186.png` · 118:30 — stacco netto su Excalidraw, schema a mano BRANCH/COMMIT ⭐
Cambio di finestra completo rispetto alle tre scene precedenti: tab browser `excalidraw.com`, con toolbar degli strumenti di disegno in alto e pannello proprietà a sinistra (colori tratto nero/rosso/verde/blu/arancione, sfondo trasparente/rosa/verde/azzurro/giallo, spessore tratto, opacità al 100, livelli). In basso a destra pulsanti "Excalidraw" e "Share". Sul canvas, disegno a mano libera: in alto a sinistra scritta **"BRANCH"** con una linea orizzontale che parte in alto a destra (terminando con una freccia) e scende verticalmente fino a un piccolo rettangolo con un cerchio dentro e un'iconcina a forma di mano/persona sopra di esso. Più in basso due linee quasi orizzontali che si incrociano (una arancione, una blu) con un punto verde su una di esse; sotto, scritta **"COMMIT"** con una linea verde che scende e piega a destra terminando in un punto verde con freccia.
➕ Il contenuto visivo (schema di branch/commit stile Git) non trova corrispondenza diretta nel parlato trascritto a questo timestamp esatto — possibile stacco di montaggio tra due momenti di schermo condiviso, o disegno preesistente su cui il presentatore torna per un'analogia (sessioni/checkpoint della second brain come commit). Si segnala la voce effettivamente letta al minuto, prosecuzione del discorso sulla tabellina: *"muoverci ulteriormente, ehm, volevo farvi una mini tabellina che voleva essere indicativa di, ehm, come dovrebbe funzionare. Sono numeri indicativi, eh, non prendeteli come solo questo o non c'è nient'altro, ma dovrebbe darvi un 80/20 per capire che tipologia di company"* (il "cervello" — company brain — a cui si riferisce, prosecuzione del discorso).

### Scena 303 · `frame-1222.png` · 122:06 — Excalidraw, tabella di scala "# NOTE" ⭐
Canvas Excalidraw (stesso file della scena 302, ripreso/proseguito). A sinistra due rettangoli rossi con etichette manoscritte **"daily logs"** e **"sessions"**, ciascuno con una parentesi graffa "⊢" disegnata sotto; al centro una freccia che parte nera in alto e diventa blu scendendo verso destra-basso. A destra, tagliata dal bordo della finestra, una tabella manoscritta in arancione a due colonne: intestazione **"# NOTE"** | (colonna di destra tagliata, si legge solo "A..."); righe: **"< 500"**, **"500 - 2500"**, **"2500 - 20'000"**, **"20'000 +"**. La colonna di destra (probabile "architettura consigliata") non è ancora leggibile in questo frame.
Voce: *"sono delle lezioni dedicate dove ho fatto semplicemente vedere come ci si comporta. Qui ho usato un eh embedding projector che è con tensor flow"* — introduce lo strumento che verrà mostrato nelle scene successive.

### Scena 304 · `frame-1223.png` · 122:12 — piattaforma Skool "Avanguardia Plus", lezione "Cosa sono i Vector Databases"
Stacco su un'altra finestra browser: piattaforma community Skool, URL `skool.com/avanguardia-plus/classroom/...`. Header con logo "Avanguardia Plus", tab "Community / Classroom / Calendar / Members / Map / Leaderboards / About" (Classroom attivo). Sidebar sinistra: corso **"Fondamenta AI / Business"** (barra di progresso a 0%) con elenco lezioni: "Premesse sul Modulo", "Scegli il nome azienda", "Compra un dominio", "Cloudflare Setup", "Google Workspace", "Setup & Warmup infrastruttura cold email"; sezione **"Fondamenta AI"** espansa con voci parzialmente coperte dal riquadro webcam: "Cosa Uso Per fare Le Presentazioni", "...enza Artificiale", "...agli LLM", "...utilizzare e quando", "...eering Basics", "...asterclass (1h+ LIVE)". Contenuto principale: titolo **"Cosa sono i Vector Databases"** con icone spunta/matita a destra; sotto, player video incorporato che mostra come miniatura la schermata dell'Embedding Projector di TensorFlow con frecce blu disegnate sopra; barra di reazione sotto il player con cuore/pollice/fuoco/applauso/occhi/faccina e pulsante "Comment". Testo della lezione: heading **"Cosa impari in questa lezione"**: "Un vector database è un tipo di database ottimizzato per salvare e cercare vector embeddings. Se RAG è il processo, il vector database è dove i dati vivono." Poi: "La differenza rispetto a un database tradizionale: un database SQL cerca corrispondenze esatte ("dammi tutte le righe dove città = Milano"). Un vector database cerca per similarità semantica ("dammi i chunk di testo più simili a questa domanda")." Segue heading **"Come si usa nella pratica"** tagliato in basso dal bordo del frame.
Voce: *"che è esattamente questo dove potete vedere che qui se io cerco, non lo so, king e quindi il re, vedete che io ho che dal centro, quindi ops, scusatemi, dal centro"* — riferimento diretto al contenuto del video mostrato in miniatura.

### Scena 305 · `frame-1224.png` · 122:18 — Embedding Projector di TensorFlow, vista dal vivo
Nuovo tab browser, URL `projector.tensorflow.org`, header magenta **"Embedding Projector"**. Pannello sinistro **"DATA"**: menu a tendina "Tensors from: Word2Vec 10K", "Label by: word", "Color by: No color map", "Edit by: word", campo "Tag selection as", pulsanti "Load / Publish / Download / Label", checkbox **"Spherize data"** spuntata, "Checkpoint: Demo datasets", "Metadata: oss_data/word2vec_10000_200d_labels.tsv". Barra superiore: icone strumenti di selezione e "Points: 10000 | Dimension: 200". Sul canvas centrale, ancora zoomato indietro: una nuvola blu compatta di punti (il cluster di embedding non ancora esplorato/etichettato).
Voce: *"e quindi da qui che ora segnerò, io avrò che Kings e King sono vettori simili nella stessa direzione nello spazio tridimensionale."*

### Scena 306 · `frame-1229.png` · 122:48 — video della lezione Skool, cluster di parole "-ing" nell'Embedding Projector ⭐
Torna la pagina Skool "Cosa sono i Vector Databases", ma ora il player video incorporato è ingrandito/in riproduzione (si vede, dentro al player stesso, un riquadro piccolo con il presentatore in basso a sinistra — è la registrazione precedente dell'Embedding Projector rivista da dentro la lezione). Sullo sfondo del player sono leggibili le etichette di parole disposte a grappolo: "networking", "buckingham", "cooking", "tracking", "viking", "checking", "smoking", "drinking", "striking", "looking", "attacking", "working", "thinking" — tutte terminanti in "-ing", con frecce blu disegnate a mano che convergono verso l'area di "drinking" da un angolo del grafico. Sotto il player, la stessa barra di reazioni (cuore/pollice/fuoco/applauso/occhi/faccina) e pulsante "Comment".
Voce: *"Quindi ora non voglio fare un corso tecnico perché non è lo scopo, neanche in community abbiamo corsi tecnici, ma ho messo le fondamenta perché voi possiate capire meglio queste infrastrutture"* — chiude il tema tecnico prima di tornare all'analogia pratica.

### Scena 307 · `frame-1230.png` · 122:54 — Excalidraw, tabella di scala con seconda colonna parzialmente rivelata
Ritorno al canvas Excalidraw di scena 303 (stesso disegno "daily logs" / "sessions" con parentesi e freccia nera-blu). La tabella arancione a destra ora mostra anche l'inizio della seconda colonna, in blu, intestata **"ARCH..."** (tagliata): riga "< 500" → "~"; riga "500 - 2500" → "~"; riga "2500 - 20'000" → "Emb..." (verosimilmente "Embeddings", tagliato); riga "20'000 +" → "Pipe..." (verosimilmente "Pipeline", tagliato). ➕ Le celle di destra restano parzialmente fuori dal bordo del frame: lettura completa non verificabile in questo screenshot.
Voce: *"e motivo per cui oggi non andremo nel dettaglio del Rug, ve lo spiegherò ad alto livello, ma perché c'è tutto uno spessore tecnico dietro che bisogna insomma apprezzare se volete applicarla in maniera massiva e quindi in maniera scalabile in un'azienda."*

### Scena 308 · `frame-1234.png` · 123:18 — Obsidian Graph view del vault Aurora, percorso tracciato a mano ⭐
Vista grafo di Obsidian, tema scuro. Sidebar sinistra con le cartelle del vault: `_showcase`, `areas`, `code`, `concepts`, `data`, `docs`, `entities`, `outputs`, `projects`, `self`, `sources`, `workspace`, più il file `_index-aurora`. Sul canvas centrale decine di nodi (pallini di dimensione variabile secondo i collegamenti) con etichette leggibili: `_index-areas`, `area-finance-operations`, `_showcase`, `concetto-churn`, `area-self`, `persona-giulia-rinaldi`, `kpi-2025-nrr`, `_index-aurora`, `kpi-2025-client-attivi`, `_index-outputs`, `persona-chiara-fontana`, `cliente-hotelline-hospitality`, `area-marketing`, `output-pitch-deck-vendite`, `persona-elena-ferraro`, `_index-workspace`, `code-export-crm`, `area-customer-success`, `persona-marco-bianchi`, `kpi-2025-churn`, `area-people-culture`, `cliente-banca-adriatica`, `concetto-efficienza-energetica`, `progetto-arr-5m-2026`, `_index-sources`, `area-prodotto-engineering`, `nota-collegata-1`, `_index-data`, `_index-projects`, `doc-onboarding-cliente`, `_index-code`, `prodotto-aurora-access`, `_index-concepts`, `cliente-immobiliare-lombarda`, `_template-nota`, `kpi-2025-edifici`, `nota-collegata-2`, `prodotto-aurora-core`, `self-identita-aurora`, `_index-entities`, `prodotto-aurora-energy`. Sopra il grafo, un tratto blu spesso disegnato a mano zigzaga da `output-pitch-deck-vendite` scendendo tra vari nodi centrali fino a fermarsi vicino a `self-identita-aurora` / `_index-entities`, evidenziando un percorso di collegamenti attraverso il grafo.
Voce: *"al posto che andare dentro e farsi tutti i 1000, diciamo, eh rami e sprecare token, l'AI andrà direttamente a vedere le cose che in un database vettoriale sono più o meno orientate nella stessa direzione."*

### Scena 309 · `frame-1242.png` · 124:06 — Excalidraw, tabella "# NOTE / ARCHITETTURA" completa
Stesso canvas Excalidraw della tabella già vista (scene 303/307), ora leggibile per intero. Intestazione: **"# NOTE"** (arancione) | **"ARCHITETTURA"** (blu). Righe: **"< 500"** → "~" con una freccetta che punta a testo blu corsivo, letto come *"MAPPE CONTENUTO + Plus. txt"* ➕ trascrizione incerta per la grafia manoscritta, possibile refuso per "più .txt"/file di testo semplice; **"500 - 2500"** → "~" (stessa freccetta, nessun testo aggiuntivo distinto in questo frame); **"2500 - 20'000"** → **"Embeddings / RAG"**; **"20'000 +"** → **"Pipeline RAG completo"**. In basso a destra, tagliata dal bordo, una freccia rossa verticale che punta verso il basso/destra (elemento del disegno non ulteriormente identificabile in questo frame).
Voce: *"e poi avremo un modulo dedicato, insomma. Per concludere,"*

### Scena 310 · `frame-1243.png` · 124:12 — ricerca Google "supabase"
Pagina risultati Google per la query **"supabase"** (visibile nella barra di ricerca). Primo risultato: "Supabase | The Postgres Development Platform" con URL `supabase.com` e descrizione "Supabase is the Postgres development platform. Start your project with a Postgres database, Authentication, instant APIs, Edge Functions, Realtime ...". Sotto, sitelink: "Pricing" (Explore Supabase fees and pricing information...), "Docs" (Supabase provides a full Postgres database for every project with...), "Database" (Every Supabase project is a dedicated Postgres database...), "Beginners" (Supabase is the Postgres development platform that...), e un secondo risultato parzialmente visibile in basso ("...build the best developer platform...", "...abase.com »").
Voce: *"database che consiglio sono, se volete fare integrazioni di tipo rag, potete"*

### Scena 311 · `frame-1244.png` · 124:18 — homepage Supabase.com
Homepage di `supabase.com`, tema scuro, contenuto superiore ancora in dissolvenza/caricamento (loghi e voci di menu sfumati). Header con nav "Product / Developers / Solutions / Pricing / Docs / Blog" e pulsante verde "Dashboard" in alto a destra. Claim centrale: **"Start your project with a Postgres database, Authentication, instant APIs, Edge Functions, Realtime subscriptions, Storage, and Vector embeddings."** Due pulsanti: **"Start your project"** (verde) e **"Request a demo"**. Sotto, loghi di aziende clienti (tra cui si legge "submagic", "mozilla", "GitHub") e testo "Trusted by fast-growing companies worldwide". In fondo, tre voci parzialmente visibili: "...atabase", "Authentication", "Edge Functions".
Voce: *"usare Superabase e quindi il classico che vedete all'interno, insomma, dei eh dei video, soprattutto quando c'erano le"*

### Scena 312 · `frame-1246.png` · 124:30 — ricerca Google "qdrant"
Pagina risultati Google per la query **"qdrant"**. Risultato sponsorizzato ("Sponsored result"): **"Qdrant"** — `https://www.qdrant.tech` — descrizione: "Vector Database for RAG — Enterprise-ready vector database for cloud, on-prem, and edge deployments. Build with the top...". Sitelink: "Pricing" (Explore different pricing options...), "Managed Cloud Platform" (Get a free 1GB cluster today...), "Open-Source Vector Database" (High-accuracy, low-latency vector search at billion-vector scale...), e una quarta voce tagliata "...ctor Database" con descrizione "...hed speed and reliability at billion-vector scale." In fondo il link "Hide sponsored result" e frammento URL "...nt.tech".
Voce: *"integrazioni, oppure potete usare un database come quadrant, hanno alcune differenze. Supase vi permette di fare"*

### Scena 313 · `frame-1252.png` · 125:06 — ricerca Google "weaviate", ultimo esempio di vector DB
Pagina risultati Google per la query **"weaviate"** (visibile nella barra di ricerca, con filtro "Reviews" comparso sotto la searchbar). Risultato principale: "Weaviate · https://weaviate.io" — **"Weaviate: The AI database developers love"** — descrizione: "With over 20M open source downloads and thousands of customers, Weaviate is a core piece of the stack for leading startups, scale-ups, and enterprises." Sitelink: "Vector Database" (Weaviate is an open-source vector database that simplifies the ...), "Careers" (Weaviate is a vector database, which uses AI and machine ...), "Weaviate Database" (Weaviate is an open-source vector database designed to store and ...), una quarta voce in parte coperta dalla webcam ("...g Center" — "...ub for builders of all levels. Get Started ..."), e una quinta tagliata ("...abase to explore Weaviate features ...", "...viate.io »"). Pannello di conoscenza a destra: foto di un edificio con mappa (zona "GRACHTENGORDEL" di Amsterdam, marker "The Pantry"), scheda **"Weaviate"** con "5,0 ★★★★★ 3 reviews", "Software company in Amsterdam, Netherlands", pulsanti "Website / Directions / +3", "Located in: Fosbury & Sons", "Address: Prinsengracht 769, 1017 JZ Amsterdam, Netherlands", "Hours: Open · Closes 5pm", "Province: North Holland", "Suggest an edit · Own this business?", "Add missing information". Il presentatore in webcam ha entrambe le mani alzate a palmo aperto, in un gesto enfatico di conclusione/elenco.
Voce: *"contesto corretto, però questo è come e diciamo aumentate la potenza della vostra company Brain, perché ricordiamoci,"*

### Scena 314 · `frame-1253.png` · 125:12 — stacco/transizione a schermo diviso verso Obsidian
Frame di transizione a schermo diviso in due metà verticali. Metà sinistra: coda della pagina Google/Maps di Weaviate vista nella scena 313 (foto di un edificio ad Amsterdam con marker "The Pantry", scheda "...viate" con "★★★★★ 3 reviews", pulsanti "...ebsite / Directions / +3"), ancora visibile ma già in dissolvenza. Metà destra: Obsidian a schermo intero, sidebar cartelle del vault (`_showcase`, `areas`, `code`, `concepts`, `data`, `docs`, `entities`, `outputs`, `projects`, `self`, `sources`, `workspace`, file `_index-aurora`) e, sul canvas, l'inizio della vista grafo con nodi già etichettati (`_index-areas`, `area-self`, `concetto-churn`, `kpi-2025-client-attivi`, `area-vendite`, `output-pitch-deck-vendite`, `area-customer-success`, `persona-marco-bianchi`, `code-export-crm`, `cliente-immobiliare-lombarda`, `kpi-2025-edifici`, tra gli altri). In basso a sinistra il riquadro webcam del presentatore.
Voce: *"contesto corretto, però questo è come e diciamo aumentate la potenza della vostra company Brain, perché ricordiamoci, Obsidian è il nostro layer 1, adattiamo"* — chiude il discorso sui vector database e riapre il riepilogo dell'architettura a livelli, con Obsidian come "layer 1".

### Scena 315 · `frame-1254.png` · 125:18 — Obsidian, vista grafo del vault a schermo intero ⭐
Vista "Graph view" (titolo in alto) a schermo intero, tema scuro. Sidebar sinistra con le stesse cartelle della scena precedente. Sul canvas centrale l'intero grafo del vault Aurora, decine di nodi di dimensione variabile con etichette leggibili: `_index-areas`, `strumento-crm`, `_showcase`, `area-finance-operations`, `concetto-churn`, `persona-giulia-rinaldi`, `kpi-2025-nrr`, `_index-aurora`, `kpi-2025-client-attivi`, `area-marketing`, `output-pitch-deck-vendite`, `area-vendite`, `persona-chiara-fontana`, `cliente-hotelline-hospitality`, `_index-docs`, `code-export-crm`, `area-customer-success`, `persona-elena-ferraro`, `_index-workspace`, `kpi-2025-churn`, `area-people-cultura`, `persona-marco-bianchi`, `concetto-efficienza-energetica`, `cliente-banca-adriatica`, `progetto-arr-5m-2026`, `_index-sources`, `area-prodotto-engineering`, `nota-collegata-1`, `_index-data`, `doc-onboarding-cliente`, `_index-code`, `prodotto-aurora-access`, `_index-concepts`, `cliente-immobiliare-lombarda`, `_template-nota`, `kpi-2025-edifici`, `nota-collegata-2`, `_index-projects`, `self-identita-aurora` (nodo grande), `_index-entities`, `prodotto-aurora-energy`, `canon`, `nota-collegata-2`, `prodotto-aurora-core`. In basso il riquadro webcam del presentatore.
Voce: *"le AI, abbiamo costruito la nostra Volt. Se l'avete fatta con questo, siete sicuri che avete un'architettura che funzioni e sapete che può essere scalabile fino a un certo punto."* — usa il grafo come prova visiva del vault ("Volt"/Vault) costruito.

### Scena 316 · `frame-1262.png` · 126:06 — Notion, pagina "Company Brain — Tutti i prompt", Prompt 12 e 13
Notion, pagina privata **"Company Brain — Tutti i prompt del..."** (tab in alto, con pulsante "Translate to English" e "Share"). Sidebar sinistra: "Home", "Meetings" (Connect your calendar, New AI meeting note), sezione "Recents" con "Clienti", "Cruscotto Aurora", "Company Brain — Tutti i prom..." (evidenziata), "New page", "Reparti", "Prodotti" con sotto-voce "Default View", "KPI mensili", "Sedi", "Competitor", sezione "Agents" (New agent), "Shared". Contenuto centrale, coda di un blocco precedente su regole di risposta ("Rispondi usando SOLO le note del cervello di Aurora." — "Cita sempre il nome del file..." — "Elenca SOLO i clienti che hanno DAVVERO tutti e due i prodotti..." — "Se la risposta non è nel cervello, scrivi: 'Non presente nel cervello.'" — "Domanda: quali clienti hanno attivato sia Aurora Cloud sia Aurora Care, e chi li segue nel customer success?"). Poi heading **"Prompt 12 — Il cruscotto HTML locale"**: "Un singolo file HTML offline da aprire con un doppio click: il biglietto da visita per una demo." Blocco codice: "Genera un cruscotto HTML statico dai dati del canon: gli indicatori dell'ultimo mese, i grafici di andamento (fatturato, organico, edifici), la classifica clienti e l'organico per reparto. Tutto in un solo file .html che apro con un doppio click, offline e senza account." Heading **"Prompt 13 — Apri la sessione (il briefing)"**: "A inizio giornata, fai riprendere il filo al cervello dal diario dell'ultima volta." Blocco codice, parzialmente tagliato dal bordo inferiore: "Buongiorno. Apriamo la sessione di lavoro sul cervello di Aurora. Leggi l'indice llms.txt e l'ultima nota dentro workspace/journal/sessions/ (il diario dell'ultima volta). Poi dammi un briefing in 5 righe: - dove eravamo rimasti, dal diario; - cosa era rimasto aperto; - cosa conv[iene fare oggi in] ordine di priorità." seguito da (non del tutto leggibile) "Non scrivere ancora niente nel cervello. Solo il briefing." Tooltip "Copied code to clipboard" visibile a metà pagina.
Voce: *"Possiamo fare o cruscotti locali, quindi con un HTML locale, lo vedete in un sacco di video YouTube, oppure possiamo utilizzare Notion. Adesso vi farò vedere entrambe le integrazioni, però sostanzialmente questo è il concetto."* — introduce le due opzioni di layer visivo che la pagina Notion documenta come prompt pronti.

### Scena 317 · `frame-1267.png` · 126:36 — Antigravity, prompt esatto per il cruscotto HTML statico ⭐
Editor Antigravity (barra in basso "Antigravity - Settings"), tab **"Identify missing databas..."** aperto. Sidebar file Explorer con cartella "aurora cervello" e sottocartella "entities" espansa (`_index-entities.md`, `cliente-banca-adriatica.md`, `cliente-hotelline-hospitality.md`, `cliente-immobiliare-lombarda.md`, `persona-chiara-fontana.md`, `persona-elena-ferraro.md`, `persona-giulia-rinaldi.md`, `persona-marco-bianchi.md` selezionato, `prodotto-aurora-access.md`, `prodotto-aurora-core.md`, `prodotto-aurora-energy.md`, `strumento-crm.md`). Nella chat, coda della risposta precedente sull'audit del database: punto 1 "Metti i numeri nel frontmatter come campi, non nella prosa..." con esempio in codice `arr: 720000`, `settore: banca`; punto 2 "Schede che mancano: i 6 clienti senza nota (ci sono solo 3/9), i 2 prodotti senza nota (Manutenzione, Insights), e soprattutto Costruzioni Sud, il cliente perso...". Poi heading **"Le 3 mosse che sbloccano l'80%"**: "Se fai solo tre cose, in ordine:" 1. "Prezzo per modulo sui clienti → sblocca ricavo per prodotto, attach rate a valore, e metà delle analisi commerciali." 2. "Una metrica di risultato per persona (almeno AE e CSM) → sblocca il 'top employee' e la valutazione del team." 3. "I costi (conto economico base + RAL) → sblocca profittabilità, margine, ARR per dipendente: passi da 'quanto fatturo' a 'quanto guadagno'." Chiusura: "Vuoi che ti prepari lo schema dei campi nuovi (un template aggiornato per cliente/persona/prodotto) e le 8 schede mancanti come bozze da riempire?" In basso, riquadro di input evidenziato con bordo rosso contenente il prompt digitato/incollato dal presentatore: **"Genera un cruscotto HTML statico dai dati del canon: gli indicatori dell'ultimo mese, i grafici di andamento (fatturato, organico, edifici), la classifica clienti e l'organico per reparto. Tutto in un solo file .html che apro con un doppio click, offline e senza account."** Barra sotto l'input: "2 lines selected", "Bypass permissions", pulsante invio rosso.
Voce: *"Quindi adesso facciamo un prompt super semplice e lo incolleremo qua dentro. gli diremo genere, un croscotl scarico statico dei dati del canon, gli indicatori dell'ultimo mese, grafici, l'andamento, la classifica, tutto in un solo file, HTML che apre con un doppio click online e senza account."* — corrisponde parola per parola (a parte piccoli inciampi del parlato) al prompt scritto a schermo.

### Scena 318 · `frame-1269.png` · 126:48 — stesso prompt in elaborazione, "Considering..."
Stessa finestra e stesso tab della scena precedente. Il prompt appena inviato riappare in un blocco "Bash tool output (o57wx9)..." con lo stesso testo ("Genera un cruscotto HTML statico dai dati del canon: gli indicatori dell'ultimo mese, i grafici di andamento (fatturato, organico, edific[i])... la classifica...") troncato e pulsante "Show more" per espanderlo. Sotto, indicatore di stato **"Considering..."** con pallino rosso. Il riquadro di input in basso è ora vuoto con placeholder "Queue another message...", resta selezionato il file "2 lines selected" e "Bypass permissions".
Voce: *"eh potete anche generare, se utilizzate Cowork, potete utilizzare un live artifact, avete veramente la possibilità di utilizzare qualsiasi layer visivo vogliate."* ➕ il parlato in questo istante anticipa un concetto (Cowork/live artifact) diverso da ciò che si vede a schermo (l'elaborazione del prompt appena inviato) — probabile sovrapposizione di montaggio tra l'azione ripresa e il commento vocale.

### Scena 319 · `frame-1273.png` · 127:12 — cruscotto HTML generato "Aurora Sistemi S.p.A.", vista in alto ⭐
Browser locale, barra indirizzo **"File | /Users/giovannibeggiato/Desktop/aurora%20cervello/outputs/cruscotto-aurora.html"**. Pagina con sfondo scuro: header con logo quadrato sfumato viola-azzurro, titolo **"Aurora Sistemi S.p.A."**, sottotitolo "Cruscotto direzionale"; a destra "Periodo di riferimento: fine 2025", "Fonte: canon.md · compilato 2026-06-10", "Dati riconciliati · nessun dato inventato". Sezione **"INDICATORI CHIAVE - FINE 2025"** con 6 card: "ARR TOTALE" **"€ 3,84 Mln"** ("€ 3.840.000", "+24% vs inizio 2025"); "CLIENTI ATTIVI" **"9"** ("+1 nuovo logo · -1 perso", "netto 0"); "EDIFICI GESTITI" **"751"** ("su Aurora Core", "9 clienti"); "NRR" **"115%"** ("nel revenue attention", "target >110%"); "CHURN LOGO" **"~11%"** ("1 cliente perso su 9", "Costruzioni Sud"); "CHURN FATTURATO" **"5,8%"** ("€ 180.000 gross", "perdita attesa"). Sezione **"ANDAMENTO"** con due grafici: a sinistra "Fatturato (ARR)" — linea che va da "€ 3,10 Mln" (2 periodi reali) a "€ 3,84 Mln" per poi proseguire tratteggiata fino a "€ 5,00 Mln" (obiettivo Board 2026); a destra "Clienti attivi" — linea a gradini dal 2019 al 2025 con valori 1, 4, 6, 8, 9, 9, 9. In basso, tagliate dal bordo, altre due card in arrivo: "Edifici gestiti" e un'altra non ancora leggibile.
Voce: *"vari pezzettini. Perfetto. Quindi il primo è questo output di cruscotto Aurora HTML che può rappresentare la nostra company Brain. Possiamo farlo interattivo, possiamo farlo con le nostre, non lo so, guidelines aziendali."* — presenta esattamente il cruscotto appena mostrato come primo layer visivo.

### Scena 320 · `frame-1276.png` · 127:30 — stesso cruscotto, scroll su classifica clienti e organico per reparto
Stessa pagina, scrollata più in basso (intestazione di sezione tagliata dal bordo superiore). Elenco classificato di clienti per fatturato, con barra multicolore (gradiente blu-rosa che rappresenta i moduli attivi) e quadratini legenda per ciascuno: 1 "Immobiliare Lombarda SGR" "€ 720.000" ("Property management", "120 edifici · dal 2018"); 2 "Gruppo Retail Centro" "€ 640.000" ("Catena retail", "210 edifici · dal 2020"); 3 "Banca Adriatica" "€ 520.000" ("Banca", "140 edifici · dal 2019"); 4 "Comune di Bologna" "€ 410.000" ("Pubblica amm.", "95 edifici · dal 2021"); 5 "LogiPark Logistica" "€ 380.000" ("Logistica", "65 edifici · dal 2021"); 6 "TorreVerde Property" "€ 350.000" ("Property management", "60 edifici · dal 2022"); 7 "Rete Sanità Nord" "€ 300.000" ("Sanità", "38 edifici · dal 2022"); 8 "UniCampus Student Housing" "€ 260.000" (parzialmente coperto dalla webcam); "HotelLine Hospitality" "€ 260.000". Legenda colori in basso: "Manutenzione", "Access", "Insights". A destra, grafico a ciambella **"47 persone"** al centro, con legenda: "Prodotto & Engineering 18 · 38%", "Customer Success 9 · 19%", "Vendite 7 · 15%", "Finance & Operations 5 · 11%", "Marketing 4 · 9%", "People & Cultura 2 · 4%", "Fondatori 2 · 4%".
Voce: *"credo che avere un un cruscotto figo ora da parte mia sia esattamente quello eh per cui avete cliccato sul video, quindi lo eviteremo."* — sdrammatizza l'estetica del cruscotto appena mostrato.

### Scena 321 · `frame-1277.png` · 127:36 — fondo pagina del cruscotto, riga di stato finale
Stesso elenco clienti scrollato leggermente più in basso (donut "47 persone" ora in alto a destra, legenda ridotta a "Customer Success 9", "Vendite 7", "Finance & Operations 5", "Marketing 4", "People & Cultura 2", "Fondatori 2"). In fondo alla pagina, riga di stato centrata: **"Cruscotto statico offline · generato dai dati del canon di Aurora Sistemi · 47 persone · 9 clienti attivi · 751 edifici"** ➕ separatori esatti tra i valori poco leggibili per la compressione, lettura sostanzialmente coerente col resto della pagina.
Voce: *"lo eviteremo. Eh però [sbuffare] insomma avete capito. Questo è un primo layer visivo. Il secondo layer visivo è utilizzarlo tramite Notion."* — chiude il primo esempio (HTML locale) e introduce il secondo (Notion).

### Scena 322 · `frame-1278.png` · 127:42 — ritorno in cima al cruscotto HTML
Stessa pagina "Aurora Sistemi S.p.A." di scena 319, di nuovo scrollata in cima (stesso contenuto identico: le 6 card indicatori e i due grafici "Fatturato (ARR)" / "Clienti attivi"). Il presentatore è tornato all'inizio della pagina prima di cambiare strumento.
Voce: *"utilizzarlo tramite Notion. Adesso connetterò al volo questo con eh cloud code. Andremo qua dentro, gli diremo ehm"* — mentre lo schermo mostra ancora il cruscotto HTML, il parlato sta già annunciando il passaggio a Claude Code + Notion.

### Scena 323 · `frame-1279.png` · 127:48 — documentazione Notion "Connecting to Notion MCP" ⭐
Browser su `developers.notion.com/guides/mcp/get-started-with-mcp`. Header "Developer Docs" con tab "Guides / API Reference / CLI Reference / Workers / Admin API / Changelog / Examples" e barra di ricerca, pulsante "Log in", "Developer portal", "Ask Assistant". Sidebar sinistra: sotto "Get started" — "Overview", "Quickstart", "Personal access tokens", "Internal connections", "Public connections", "Authorization", "Handling API keys", "Preparing for users", "List on the Marketplace"; sotto "Agent APIs" — "Notion MCP" (espanso: "Overview", **"Connecting to Notion MCP"** evidenziata, "Supported tools"). Contenuto centrale: titolo **"Connecting to Notion MCP"**, sottotitolo "Learn how to connect your AI tool to Notion using MCP.", paragrafo: "This guide walks you through connecting your AI tool to Notion using the Model Context Protocol (MCP). Once connected, your tool can read and write to your Notion workspace based on your access and permissions." Heading **"Claude Code"**: "Run this command in your terminal:" blocco codice **"claude mcp add --transport http notion https://mcp.notion.com/mcp"** con icone copia/spunta/link. Sotto: "Then authenticate by running `/mcp` in Claude Code and following the OAuth flow." Blocco espandibile "Using --scope flag for different installation scopes". Paragrafo tagliato in basso: "Use the `/mcp` command to list and manage the MCP servers you have installed, and use the `/context` command to understand the context token usage of your current session, including the number of tokens used by each MCP server that's enabled." Sidebar destra "On this page": "Claude Code" (attivo), "Cursor", "VS Code (GitHub Copilot)", "Claude Desktop", "Windsurf", "ChatGPT", "Codex", "Antigravity", "Other tools" (con sotto-voce "JSON configuration format"), "Connect through the Notion app", "Troubleshooting", "FAQ".
Voce: *"code. Andremo qua dentro, gli diremo ehm vediamo se riusciamo a partire da conversazione. Ok, facciamo MCP ad, vediamo se riusciamo a fare qualcosa e"* — il presentatore sta leggendo/seguendo esattamente questa pagina di documentazione per copiare il comando.

### Scena 324 · `frame-1280.png` · 127:54 — terminale Claude Code, autocomplete dei comandi slash
Editor con Explorer a sinistra (progetto "aurora cervello", cartella "entities" espansa con gli stessi file persona/cliente delle scene precedenti). Tab in alto "Claude Code" con etichetta "Untitled" e, sotto, banner ASCII "Claude Code" con la mascotte arancione. Riquadro chat "⌘ Esc to focus or unfocus Claude" con file allegato "cruscotto-aurora.html" e pulsante "Bypass permissions". Pannello "Terminal" sotto (tab "Problems / Output / Debug Console / Terminal / Ports", versione "2.1.170"): prompt "giovannibeggiato@192 aurora cervello % claude"; comando già eseguito "> /fast" con risposta "⚡ Fast mode ON · model set to Opus 4.6 · $10/$50 per Mtok"; comando in digitazione "> /cl▍" con menu di autocompletamento sotto: "/clear — Start a new session with empty context; previous session stays on disk (resumable with /resume)", "/claude-api — Reference for the Claude API / Anthropic SDK — model ids, pricing, params, streaming, tool use, MCP, agents, caching, token counting, model migration. TRIGGER — read BEFORE opening t...", "/exit", "/code-review-mcp-issue-prompts — Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to your .claude/settings.json to reduce permission prompts." ➕ ultime due righe del menu poco leggibili per la sovrapposizione del cursore.
Voce: *"vediamo se riusciamo a partire da conversazione. Ok, facciamo MCP ad,"* — corrisponde al momento in cui digita `/clear` per ripartire da una conversazione pulita prima di aggiungere il server MCP.

### Scena 325 · `frame-1281.png` · 128:00 — sessione Claude Code ripulita, comando MCP add eseguito
Stesso pannello, ora senza il riquadro chat superiore (Explorer identico). Terminale: prompt "giovannibeggiato@192 aurora cervello % claude", poi banner di benvenuto "Welcome back Gio!" con mascotte, testo "Opus 4.6 (1M context) with hi[gher limits]... · Claude Max", "giobeggiato@gmail.com's Organization", "~/Desktop/aurora cervello"; a destra riquadro "Tips for getting started": "Run /init to create a CLAUDE.md file with instructions for Claude", "Introducing Claude Fable 5: a Mythos-class model that we've made saf...", "Fixed sessions not saving transcripts (and not appearing in --resume...", "Added '--safe-mode' flag (and 'CLAUDE_CODE_SAFE_MODE') to start Clau... /release-notes for more". Sotto: "⚠ 1 setup issue: MCP · /doctor", "Meet Fable 5, our newest model for complex, long-running work. Try anytime with /model. Included in your plan limits until Jun 22, then switch to usage credits to continue." Cronologia comandi: "> /clear", "> mcp add --transport http notion https://mcp.notion.com/mcp" con stato "⚙ Perusing..." Riga vuota di prompt in basso "> ▍" e barra di stato "Opus 4.6 (1M context) · $0.16 | 0/1000000 tokens · 180m 41s". ➕ il nome del modello "Claude Fable 5" così come appare nel banner non è verificabile altrove nella sessione ed è riportato alla lettera da quanto leggibile a schermo.
Voce: *"vediamo se riusciamo a fare qualcosa e se è già connesso, soprattutto perché potremmo anche avere il comando/mcp."* — il presentatore osserva l'esito del comando appena lanciato.

### Scena 326 · `frame-1287.png` · 128:36 — Claude Code, verifica della connessione a Notion
Stesso Explorer. Tab in alto "sei connesso con Notion?". Chat: messaggio utente in blocco grigio (icona file "cruscotto-aurora.html") **"sei connesso con Notion?"**, ripetuto anche come testo semplice sotto. Sotto, indicatore di elaborazione con pallino rosso e parola parzialmente scritta **"Pontific_a"** (verosimilmente "Pontificating..." — le etichette di stato di Claude Code cambiano verbo casualmente durante l'elaborazione, coerente con "Considering..." e "Perusing..." viste nelle scene precedenti). In basso riquadro di input vuoto "Queue another message...", file allegato "cruscotto-aurora.html", "Bypass permissions".
Voce: *"Sei connesso con Notion? Nel caso in cui voi non lo siate, comunque, eh solo una cosa, una volta che avete fatto enter,"* — corrisponde esattamente al prompt appena digitato a schermo.

### Scena 327 · `frame-1294.png` · 129:18 — Notion, nuova pagina "Cervello Pino" creata dall'AI ⭐
Notion, nuova pagina privata intitolata **"Cervello Pino"** con emoji albero di pino 🌲 come icona pagina. Sidebar sinistra: "Home", "Meetings" (Connect your calendar, New AI meeting note, View all), sezione "Shared", sezione "Private" con "Cervello Pino" (in grassetto/selezionata), "Company Brain — Tutti i prom...", "New page", "Library", "My Tasks". Contenuto: titolo grande **"Cervello Pino"**; sotto, callout verde con icona documento: **"🌲 Cervello Pino — Cruscotto KPI di Aurora Sistemi S.p.A."** — "Piattaforma SaaS italiana per la gestione intelligente del patrimonio immobiliare (fondata a Milano nel 2018). Dati consolidati a fine 2025 (fonte: verbale CdA del 22/01/2026, riconciliato dalla contabilità)." Heading **"📊 KPI principali — chiusura 2025"** con tre card colorate affiancate: verde "📈 ARR" **"€ 3,84M"** ("+24% sui € 3,10M di inizio anno (+€ 740k)"); blu "🔄 NRR" **"115%"** ("Espansione che supera il churn. Obiettivo Board: >110%"); viola "🏢 Edifici gestiti" **"751"** ("Somma dei 9 clienti attivi, quadra con l'anagrafica Core"). Tagliate dal bordo inferiore, altre card in arrivo: "Clienti attivi", "Logo churn", "Gross revenue".
Voce: *"integrazione Notion fatta. App Notion, lo chiameremo cervello pino. Abbiamo il nostro ARR, abbiamo il nostro revenue,"* — descrive esattamente la pagina appena creata dall'AI su richiesta del presentatore ("costruiscimi su Notion un cruscotto di KPI... chiamalo cervello pino").

### Scena 328 · `frame-1295.png` · 129:24 — Notion "Cervello Pino", tabella "Revenue — dettaglio ARR" e key account
Stessa pagina "Cervello Pino", scrollata più in basso. In alto, coda tagliata di un blocco precedente ("...2025)"). Heading **"📊 Revenue — dettaglio ARR"** con tabella a 3 colonne "Voce | Valore | Note": "ARR inizio 2025" | "€ 3.100.000" | "Base di partenza"; "– Churn (gross)" | "– € 180.000" | "Costruzioni Sud, uscita giugno 2025 (acquisita da gruppo con sistema proprietario)"; "+ Espansione (upsell)" | "+ € 660.000" | "Motore NRR: Banca Adriatica (Access), Gruppo Retail (Energy), Immobiliare Lombarda (Insights)"; "+ Nuovo logo" | "+ € 260.000" | "HotelLine Hospitality (onboarding chiuso a ottobre)"; riga totale evidenziata in verde "ARR fine 2025" | "€ 3.840.000" | "+24% YoY". Sotto, callout blu con icona lampadina: "💡 La crescita 2025 è stata trainata soprattutto dall'espansione sui clienti esistenti (upsell di moduli), non dall'acquisizione: un solo nuovo logo nell'anno. È il modello che la CEO Elena Ferraro cita come 'il vero motore' di Aurora." Heading **"👥 Clienti — i 3 key account per fatturato"** con tre card affiancate, tagliate dal bordo inferiore: verde "🏢 Immobiliare Lombarda SGR" ("Property management · cliente dal..." troncato); blu "🏦 Banca Adriatica" ("Banca · cliente dal 2022" troncato); arancione "🏨 HotelLine Hospitality" ("Hospitality · cliente dal 2025" troncato). Sidebar sinistra invariata salvo "Recents" ora con "Cervello Pino" in cima, poi "Company Brain — Tutti i prom...", "Clienti", "Cruscotto Aurora", "New page", "Reparti", "Prodotti" (con "Default View"), "KPI mensili", "Sedi", "Competitor".
Voce: *"eh, perfetto, clienti e cose di questo tipo, no? Potremmo fare questo, potremmo fare una cosa di questo tipo, potremmo,"* — commenta la tabella di dettaglio ARR e la sezione clienti appena generate in Notion.

### Scena 329 · `frame-1296.png` · 129:30 — Notion "Cervello Pino", coda card key account + Obiettivo 2026 e Reparti ⭐
Stessa pagina Notion "Cervello Pino" (sidebar identica: Home, Meetings con "Connect your calendar"/"New AI meeting note", Recents con **Cervello Pino** in grassetto/selezionata, poi "Company Brain — Tutti i prom...", "Clienti", "Cruscotto Aurora", "New page", "Reparti", "Prodotti" con "Default view", "KPI mensili", "Sedi", "Competitor", sezione Agents con "New agent"), scrollata oltre le tre card key account di scena 328: in cima, tagliate dal bordo superiore, la coda testuale delle tre card — verde "Core, Energy, Manutenzione, Insights / 2025: ha aggiunto Insights. Referenzia volentieri.", blu "2025: Access esteso a tutte le filiali — upsell più esteso dell'anno.", arancione (quasi del tutto tagliata) "...logo 2025. Forte interesse su Energy." Sotto, callout grigio con icona documento: "Il database qui sotto elenca tutti i clienti. ARR ed edifici sono valorizzati solo dove certi nel vault aziendale: per i clienti non-key account le singole cifre non sono dettagliate nelle note di origine (so il totale: € 3,84M su 751 edifici, ma non la ripartizione cliente per cliente)." Poi heading **"🎯 Obiettivo 2026 (approvato dal CdA il 22/01/2026)"** con card viola: **"🚀 ARR oltre € 5.000.000 (da € 3,84M)"**, bullet "Vincoli di qualità: NRR > 110%, logo churn < 10%", "Leve: nuovi loghi (Vendite) + espansione clienti esistenti (Customer Success)", "Abilitatore: +6 assunzioni, soprattutto Engineering e Customer Success". Poi heading **"🧩 Reparti e contesto"** con tabella "Reparto | A capo | Ruolo sui numeri": "Vendite | Davide Conti (VP Sales) | Acquisizione nuovi loghi (~7 persone)", riga successiva tagliata dal bordo inferiore "Customer Success | Giulia Rinaldi (Bologna) | Retention ed espansione —[...]".
Voce: *"fare una cosa di questo tipo, potremmo,"* — continua a scorrere/commentare la pagina Notion appena generata dall'AI.

### Scena 330 · `frame-1297.png` · 129:36 — Notion, database "Clienti" (dentro Cruscotto Aurora, non Cervello Pino) ⭐
Notion, breadcrumb in alto **"New page / Cruscotto Aurora / Clienti"** — pagina distinta da "Cervello Pino", appartiene al ramo preesistente "Cruscotto Aurora". Titolo **"📁 Clienti"**, pulsante "Default view". Tabella con colonne "Aa Cliente | # ARR | città | # Dal | # MQ | ≡ Pr[...]" (ultima colonna tagliata a destra) e molte righe con valori leggibili: "Polo Universitario Sud" €750.000 Catania 2024 60000 Edge; "Residenze Aurora Verde" €820.000 Brescia 2014 90000 Care; "Torre Eurosky Uffici" €558.000 Roma 2016 90000 Cloud; "BioPharma Stabilimenti" €555.000 Latina 2022 40000 Edge; "Galleria Moderna" €552.000 Firenze 2018 40000 Care; "Iberia Centros" €528.000 Madrid 2013 18000 Care; "Università Politecnica Adriatica" €522.000 Ancona 2021 60000 Care; "Museo delle Arti Contemp[oranee]" €511.000 Torino (icona "OPEN" al passaggio del mouse) 2017 25000 Care; "MediCenter Salute" €508.000 Padova 2013 12000 Cloud; "Aurora DACH Buildings" €486.000 Monaco di Baviera 2014 8000 Care; "Distretto Tessile Pratese" €420.000 Prato 2020 25000 Care; "Retail Gamma" €402.000 Verona 2022 8000 Edge; "Nordic Retail Chain" €370.000 Amburgo 2024 12000 Edge; "Centro Direzionale Partenope" €369.000 Napoli 2013 25000 Cloud; "Industria Meccanica Veneta" €347.000 Vicenza 2018 12000 Care; "Stadio Arena Nuova" €343.000 Udine 2013 90000 Care; "Supermercati Risparmio" €314.000 Bologna 2022 8000 Care; "Helvetia Office Park" €309.000 Zurigo 2021 12000 Care; "Banca Civica" €278.000 Torino 2017 18000 Care (riga tagliata dal bordo inferiore). ➕ questo elenco di ~18 clienti con cifre e città diverse da quelli citati nel cruscotto/Cervello Pino (i 9 attivi + Costruzioni Sud) appartiene a una pagina Notion diversa e preesistente ("Cruscotto Aurora"), non contraddice quindi i dati della nuova pagina generata — è un dataset dimostrativo separato già presente nel workspace.
Voce: *"una volta che abbiamo fatto una"* — mostra al volo anche questo database Notion preesistente mentre introduce il concetto successivo.

### Scena 331 · `frame-1300.png` · 129:54 — Antigravity, risposta di Claude con link "Cervello Pino" e due note di trasparenza ⭐
Editor Antigravity, tab **"Check Notion connection"**. Sidebar Explorer identica alle scene precedenti (cartella "aurora cervello", "entities" espansa). Chat: blocco utente (grigio) col prompt "Per favore, costruiscimi su Notion un cruscotto di KPI per la mia azienda Aurora con tutto quello che hai. Se riesci, fammi anche un dettaglio sui clienti, sul revenue e cose di questo tipo. Chiamalo "Cervello Pino" in modo che non si confonda con quello che già c'era dentro". Risposta di Claude: **""Cervello Pino" è creato su Notion:** → https://app.notion.com/p/37b041ea6fb381a7a508f7108c499626" — "Cosa contiene:" — "Cruscotto KPI (chiusura 2025) — 6 card colorate:" con bullet "ARR € 3,84M (+24% YoY)", "NRR 115%", "Edifici gestiti 751", "Clienti attivi 9", "Logo churn ~11%", "Gross revenue churn ~5,8%" — "Revenue — tabella a ponte: € 3,10M iniziale → -180k churn → +660k espansione → +260k nuovo logo → € 3,84M finale." — "Clienti — i 3 key account in evidenza (Immobiliare Lombardia 720k, Banca Adriatica 520k, HotelLine 260k) + un database "Clienti Aurora" inline con tutti i 10 (9 attivi + Costruzioni Sud perso), filtrabile per stato/settore/moduli." — "Obiettivo 2026 (ARR >5M, NRR >110%, churn <10%, +6 assunzioni) e mappa reparti." Poi **"Due note di trasparenza:"** numerate: **"1."** "Ho usato i dati del vault locale "aurora cervello", non un workspace Notion preesistente: il tuo Notion non aveva nessun teamspace, quindi ho costruito da zero coi dati certi del vault." **"2."** "ARR ed edifici per cliente li ho valorizzati solo dove certi. Il vault dà il totale (€ 3,84M su 751 edifici) e il dettaglio dei 3 key account, ma non la ripartizione cliente-per-cliente degli altri 6. Inoltre il vault cita 9 clienti attivi ma ne nomina solo 8: ho messo un placeholder "Cliente settore PA" per far quadrare il conteggio, invece di inventare un nome." Chiusura: "Vuoi che ti provi a derivare l'ARR mancante per cliente o che colleghi questa pagina ad altre note?" In basso riquadro input rosso "⌘ Esc to focus or unfocus Claude", file allegato "cruscotto-aurora.html", "Bypass permissions".
Voce: *"diciamo, è la connessione al nostro"* — commenta il risultato appena mostrato (la pagina Notion creata dall'AI con le note di trasparenza sui dati mancanti).

### Scena 332 · `frame-1301.png` · 130:00 — Antigravity, nuova scheda "Claude Code" vuota accanto a "Check Notion connection"
Stesso editor, ora con due tab in alto: "Check Notion connection" e, appena aperta, **"Claude Code"** (etichetta "Untitled" sotto). Contenuto centrale: icona grande del robot arancione di Claude Code e testo **"Type /model to pick the right tool for the job."** Sidebar Explorer invariata: cartella "aurora cervello" con `_showcase`, `areas`, `code`, `concepts`, `data`, `docs`, `entities`, **`outputs`** (evidenziata/selezionata), `projects`, `self`, `sources`, `workspace`, e file `_index-aurora.md`, `.env`, `.gitignore`, `gate_qualita.py`, `genera_llms.py`, `genera_showcase.py`, `llms.txt`. In basso riquadro input rosso "⌘ Esc to focus or unfocus Claude", file allegato "cruscotto-aurora.html", "Bypass permissions".
Voce: *"cosa da affrontare e cioè in questo"* — apre una sessione pulita mentre introduce l'ultimo argomento del tutorial (la memoria viva).

### Scena 333 · `frame-1305.png` · 130:24 — webcam a schermo intero, introduzione al problema della "memoria statica"
Nessuno schermo software visibile: solo il riquadro webcam a piena inquadratura, il presentatore parla direttamente in camera (mensola con libri sullo sfondo, pianta a sinistra, lampada accesa a destra).
Voce: *"che non abbiamo ancora un modo di dire allei "Ehi, ascolta, ma a marzo avevamo parlato di questo argomento? Ti ricordi cos'era? Cosa avevamo deciso?""* — introduce il limite della memoria statica nei file: l'AI non si ricorda spontaneamente conversazioni passate senza un meccanismo dedicato.

### Scena 334 · `frame-1306.png` · 130:30 — webcam, mano con penna/stilo alzata
Ancora solo webcam a piena inquadratura, stesso sfondo (mensola libri, pianta, lampada). Il presentatore tiene in mano una penna/stilo bianco sollevato accanto al viso, espressione corrucciata mentre insiste sul concetto.
Voce: *"cos'era? Cosa avevamo deciso?" No, tutta"* — ribadisce la domanda retorica sul ricordo, poi introduce l'importanza dell'architettura che sta per mostrare.

### Scena 335 · `frame-1307.png` · 130:36 — webcam, prosegue la spiegazione
Ancora webcam a piena inquadratura, stessa inquadratura e sfondo, il presentatore continua a parlare guardando in camera.
Voce: *"che ci permette di avere enormi ritorni,"* — continua a motivare perché questa architettura di memoria viva è preziosa.

### Scena 336 · `frame-1308.png` · 130:42 — ritorno su Antigravity, tab "Claude Code" ancora vuoto
Stesso editor Antigravity di scena 332: tab "Claude Code" (etichetta "Untitled"), icona robot arancione al centro con testo "Type /model to pick the right tool for the job." Sidebar Explorer invariata (cartella "aurora cervello" con `_showcase`, `areas`, `code`, `concepts`, `data`, `docs`, `entities`, `outputs` evidenziata, `projects`, `self`, `sources`, `workspace`, file `_index-aurora.md`, `.env`, `.gitignore`, `gate_qualita.py`, `genera_llms.py`, `genera_showcase.py`, `llms.txt`). Riquadro di input in basso ancora vuoto "⌘ Esc to focus or unfocus Claude", file allegato "cruscotto-aurora.html", "Bypass permissions".
Voce: *"discutere informazioni interessanti"* — mentre lo schermo resta sulla sessione vuota, il parlato sta ancora elencando gli usi pratici della memoria viva (meeting, clienti, prezzi, contratti) prima di scrivere il prompt.

### Scena 337 · `frame-1314.png` · 131:18 — Excalidraw, canvas bianco vuoto con strumento disegno selezionato
Browser su `excalidraw.com`. Toolbar in alto con set di strumenti (selezione, mano, forme, freccia, testo, matita evidenziata in viola/attiva, timer, altro) e, a destra, pulsanti "Excalidraw" e "Share" (viola). Pannello proprietà a sinistra: "Stroke" (nero/rosso/verde/blu/arancione/bianco selezionato), "Background" (bianco/rosa/verde/blu/giallo/trasparente), "Stroke width" (tre spessori, il più spesso selezionato), "Opacity" (slider al massimo), "Layers" (quattro icone). Canvas centrale completamente bianco e vuoto, con testo minuscolo in alto al centro "Click and drag, mouse when you're finished" e in basso "Scroll back to content" con pulsante sotto. Nessun disegno ancora tracciato.
Voce: *"skill abbiamo? Abbiamo innanzitutto il"* — apre Excalidraw per abbozzare al volo lo schema delle tre skill (inizio sessione, fine sessione, fine giornata) di cui sta parlando; il disegno vero e proprio non è ancora tracciato in questo frame.

### Scena 338 · `frame-1342.png` · 134:06 — Antigravity, prompt "memoria viva" digitato per intero nel campo di input ⭐
Stesso editor Antigravity, tab "Claude Code" ancora con l'icona robot e "Type /model to pick the right tool for the job." visibili sopra, ma ora il riquadro di input in basso (bordo rosso attivo) contiene il prompt digitato per intero, trascritto qui riga per riga così come appare a schermo: "Costruiamo una skill per il cervello di Aurora che gestisca il journal: inizio sessione, fine sessione, fine giornata." — riga vuota — "CONTESTO -- memoria viva" — "Il cervello ha due strati di memoria:" — "- Memoria STATICA: le note delle entità vere (clienti, KPI, progetti)." — "  Vivono già nel cervello e cambiano di rado." — "- Memoria DINAMICA: il diario di lavoro. Ogni sessione e ogni giornata" — "  lasciano una nota che si AGGANCIA sempre alle entità statiche coi" — "  [[wikilink]]. Mai una nota di diario sciolta nel vuoto." — "Lo scopo della skill e' tenere viva la memoria dinamica e cucirla a" (riga finale tagliata dal bordo inferiore del riquadro, il testo continua oltre quanto visibile). Sidebar Explorer invariata. In basso a destra icona microfono, "Bypass permissions", freccia di invio rossa.
Voce: *"dentro e gli diciamo contesto memoria viva. Il cervello ha due strati, memoria"* — corrisponde quasi verbatim (con piccole variazioni di parlato) al testo scritto a schermo nel prompt appena mostrato.

### Scena 339 · `frame-1351.png` · 135:00 — prompt "Costruiamo una skill..." appena inviato, in elaborazione
Antigravity, tab **"Costruiamo una skill per..."**. Chat con blocco utente (file allegato "cruscotto-aurora.html"): "Costruiamo una skill per il cervello di Aurora che gestisca il journal:" "inizio sessione, fine sessione, fine giornata" (testo attenuato/in corso di invio). Nessuna risposta ancora visibile sotto. In basso riquadro "Queue another message...", file "cruscotto-aurora.html", "Bypass permissions" con pulsante di invio rosso evidenziato. Sidebar Explorer invariata rispetto alle scene precedenti.
Voce: *"per aiutare le Yi a trovare le cose."* — chiude la spiegazione del prompt appena prima di inviarlo.

### Scena 340 · `frame-1355.png` · 135:24 — risposta di Claude: skill "journal" costruita, istruzioni d'uso e percorsi file ⭐
Stesso editor, tab **"Build journal skill for..."**. In alto una riga collassata "Si esce in parallelo per andare più veloce" e un frammento YAML `name: journal` / `description: >`. Risposta di Claude: "Fatto. Ho costruito **una sola skill** (`journal`) con i tre comandi al suo interno, più i due template, e prima ho scritto i due template in parallelo per andare più veloce come hai chiesto." Heading **"Come invochi i tre comandi"**: "Scrivi semplicemente, in chat:" — "**buongiorno** → briefing di inizio sessione in 5 righe. Non scrive niente." — "**chiudi sessione** → prima ti dice in 3 righe cosa abbiamo fatto, al tuo ok scrive `sessione-<data>`." — "**fine giornata** → legge tutte le sessioni del giorno, ti dice in 3 righe cosa e' successo, al tuo ok scrive il daily." Poi: "La skill si attiva da sola su queste frasi (e varianti tipo "chiudiamo la sessione", "riassunto del giorno"). Se vuoi forzarla puoi anche scrivere `/journal`." Heading **"Dove sono finiti i file"**: "**Skill**: `.claude/skills/SKILL.md` — l'orchestratore coi tre comandi e le regole." — "**Template sessione**: `workspace/journal/_templates/_template-sessione.md`" — "**Template daily**: `workspace/journal/_templates/_template-daily.md`" — "**Cartelle del diario (create)**: `workspace/journal/sessions/` e `workspace/journal/daily/`" Poi: "Regole rispettate dentro la skill: date sempre `YYYY-MM-DD`, frontmatter conforme a `_template-nota.md`, ogni nota di diario con almeno un `[[wikilink]]` a un'entità reale (se manca, te lo chiede, nessuna entità inventata." Testo tagliato in fondo: "Vuoi che pr[...]". Sidebar Explorer: compare ora una nuova cartella **`.claude`** in cima all'albero (appena creata dalla skill), accanto alle cartelle preesistenti.
Voce: *"l'ha costruita. Come la invoco."* — introduce esattamente la sezione "Come invochi i tre comandi" appena mostrata a schermo.

### Scena 341 · `frame-1363.png` · 136:12 — "Buongiorno Claude": briefing generato dalla skill journal ⭐
Stesso editor, tab **"Italian greeting"**. Chat: file allegato "cruscotto-aurora.html", messaggio utente **"Buongiorno Claude"**. Sopra la risposta, blocco codice mostra il file letto: "# Aurora Sistemi — llms.txt" / "> Indice-porta per AI. File DERIVATO: rigenerato da genera_llms.py, non modificare a mano." Indicatore "Thought for 0s". Risposta di Claude: "Buongiorno Gio." — "Non c'è ancora nessuna nota di sessione nel diario, quindi il briefing è solo sull'indice del cervello (`llms.txt`)." Heading **"Dove siamo"**: "Il cervello di **Aurora Sistemi** è popolato e in piedi: 6 aree, 3 clienti attivi mappati (Banca Adriatica, HotelLine, Immobiliare Lombarda), KPI 2025 e l'unico progetto strategico aperto." — "Il diario di lavoro è vuoto: questa è di fatto la prima sessione tracciata." Heading **"Cosa è aperto / da affrontare oggi, in ordine"**, numerato: "1. [[progetto-arr-5m-2026]] — l'obiettivo Board 2026: ARR oltre 5M con NRR >110% e churn logo <10%. È l'unico progetto attivo, quindi il candidato naturale su cui lavorare." — "2. Churn — il 2025 ha chiuso con logo churn ~11% ([[kpi-2025-churn]]), sopra la soglia <10% che il progetto richiede. Punto di attenzione concreto." — "3. Vedo che hai aperto `outputs/cruscotto-aurora.html` nell'IDE — se il lavoro di oggi è lì, partiamo da quello." Chiusura: "Da cosa vuoi cominciare?" Sidebar Explorer ora espansa su `workspace > journal > _templates, daily, sessions`, con in fondo `_index-workspace.md`, `_template-nota.md`, `canon.md`, `_index-aurora.md`, `.env`, `.gitignore`.
Voce: *"quindi solo questa nel"* — mentre risponde a Claude di voler solo testare la skill con una conversazione semplice nel suo workspace, riferendosi al briefing appena mostrato a schermo.

### Scena 342 · `frame-1373.png` · 137:12 — doppio pannello: chat "si certamente" + file `sessione-2026-06-10.md` aperto con frontmatter evidenziato ⭐
Editor diviso in due. Pannello sinistro "Italian greeting": risposta a un precedente "si certamente" con blocco "Exit code 1" / "2026-06-10" poi "**Write** sessione-2026-06-10.md" "23 lines", quindi testo: "Fatto. La skill funziona: nota salvata in `workspace/journal/sessions/sessione-2026-06-10.md`." "Cosa contiene:" — "**Frontmatter** valido — `title`/`summary` tra virgolette, `tags` flow-list con `workspace` primo, `related` lista a blocco con wikilink tra virgolette, date in `YYYY-MM-DD`." — "**Aggancio** a `[[progetto-arr-5m-2026]]` (regola del wikilink obbligatorio rispettata)." — "**Corpo in tre sezioni**: `## Fatto`, `## Deciso`, `## Aperto`." — "Il test è riuscito: la sessione si chiude e si salva nel workspace come previsto." Sotto, messaggio utente "Hey Claude, grazie per oggi. Finisco la giornata qui" e stato "Generating...". Pannello destro, nuova tab **"sessione-2026-06-10.md"** (percorso "workspace > journal > sessions > sessione-2026-06-10.md"), contenuto del file trascritto per intero, riga per riga (frontmatter evidenziato in blu/selezionato):
```
---
title: "Sessione — 2026-06-10"
summary: "Test della skill journal: briefing di buongiorno e prima chiusura di sessione per verificare il salvataggio della nota."
tags: [workspace, type/session]
status: done
created: 2026-06-10
updated: 2026-06-10
related:
  - "[[progetto-arr-5m-2026]]"
---

# Sessione — 2026-06-10

## Fatto
- Briefing di buongiorno sul cervello di Aurora Sistemi (diario ancora vuoto, prima sessione tracciata).
- Test della skill journal: verificato che la chiusura di sessione salvi correttamente una nota nel workspace.

## Deciso
- Agganciare questa nota di test a [[progetto-arr-5m-2026]], unico progetto attivo, per rispettare la regola del wikilink obbligatorio.

## Aperto
- Lavoro reale sul progetto ARR 5M e sul churn logo 2025 (~11%, sopra la soglia <10%) ancora da affrontare.
```
Barra di stato in basso: "Ln 1, Col 1 (294 selected)", "Spaces: 2", "UTF-8", "LF", "{} Markdown", "Antigravity - Settings". Sidebar sinistra ora mostra il file `sessione-2026-06-10.md` selezionato dentro `workspace/journal/sessions/`.
Voce: *"guardate eh quello che vi dicevo con"* — introduce il commento sulla solidità tecnica del sistema, riferendosi esattamente al file appena scritto e mostrato a schermo.

### Scena 343 · `frame-1377.png` · 137:36 — "fine giornata": Claude riassume la sessione e legge il template daily
Pannello unico, tab "Italian greeting" scrollata più in basso. Coda tagliata di un blocco precedente ("...si certamente"), poi messaggio utente **"Hey Claude, grazie per oggi. Finisco la giornata qui"**, indicatore "Thought for 2s". Risposta di Claude: "Grazie a te, Gio. Attivo "fine giornata". Prima di scrivere il daily, in 3 righe cosa è successo oggi in totale:" numerato: "1. Briefing di buongiorno sul cervello di Aurora Sistemi (diario vuoto, prima giornata tracciata)." "2. Test della skill `journal`: chiusura di sessione che ha salvato correttamente la nota nel workspace." "3. Nessun lavoro reale sulle entità: giornata dedicata a verificare il meccanismo del diario." Poi: "C'è una sola sessione oggi ([[sessione-2026-06-10]]), che fonderò nel daily. Ti torna? Dammi l'ok e scrivo." Messaggio utente successivo (file allegato "sessione-2026-06-10.md"): **"fai pure"**. Blocco strumento: "Bash Read daily template, check existing" con comando: "IN cd "/Users/giovannibeggiato/Desktop/aurora cervello" && cat workspace/journal/_templates/_template-daily.md 2>/dev/null && ..." "OUT Exit code 1" "---" "title: "Daily — YYYY-MM-DD"" Stato in basso "Manifesting...". Sidebar sinistra ora con la cartella **`daily`** evidenziata/selezionata dentro `workspace/journal/`.
Voce: *"Quindi ora ci assicuriamo che appaia nel daily, quindi qui dovrebbe cominciare ad"* — descrive esattamente l'azione appena avviata a schermo (lettura del template daily per generare la nota di fine giornata).

### Scena 344 · `frame-1378.png` · 137:42 — doppio pannello: chat "fine giornata" + `_template-daily.md` aperto per intero ⭐
Editor diviso in due. Pannello sinistro "Italian greeting" (contenuto identico a scena 343, ora leggermente scrollato: coda "si certamente", "Hey Claude, grazie per oggi. Finisco la giornata qui", "Thought for 2s", i tre punti numerati del riassunto, "fai pure", tool call "Bash Read daily template, check existing" con "Exit code 1"). Pannello destro, nuova tab **"_template-daily.md"** (percorso "workspace > journal > _templates > _template-daily.md"), contenuto trascritto per intero, riga per riga:
```
---
title: "Daily — YYYY-MM-DD"
summary: "Una frase di sintesi sull'intera giornata."
tags: [workspace, type/daily]
status: done
created: YYYY-MM-DD
updated: YYYY-MM-DD
related:
  - "[[sessione-YYYY-MM-DD]]"
  - "[[entita-principale-toccata]]"
---

# Daily — YYYY-MM-DD

## Fatto
- Sintesi unica di cosa è stato concluso oggi, fondendo le sessioni senza ripeterle riga per riga.

## Deciso
- Le scelte chiave della giornata e il perché.

## Aperto
- Cosa resta in sospeso a fine giornata.

## Sessioni
- [[sessione-YYYY-MM-DD]]

<!--
REGOLE (vedi workspace/_template-nota.md):
- Date sempre YYYY-MM-DD, mai relative.
- related = lista a blocco con TUTTE le sessioni del giorno + le entità principali toccate.
- title e summary sempre fra virgolette doppie.
```
(commento HTML tagliato dal bordo inferiore, il template continua oltre quanto visibile). Barra di stato "Ln 1, Col 1", "Spaces: 2", "UTF-8", "LF", "{} Markdown". Sidebar sinistra: `_template-daily.md` selezionato/evidenziato dentro `_templates/`, sotto `_template-sessione.md`, poi cartella `daily`, cartella `sessions` con `sessione-2026-06-10.md`.
Voce: *"i template di sessione. Vedete, ormai"* — indica esattamente questo file di template appena aperto a schermo.

### Scena 345 · `frame-1379.png` · 137:48 — chat a schermo intero, comando bash completo e prima scrittura del daily
Pannello unico "Italian greeting" scrollato: in cima (tagliata) la coda di "sessione che ha salvato correttamente la nota nel workspace.", poi punto 3 "Nessun lavoro reale sulle entità: giornata dedicata a verificare il meccanismo del diario.", poi "C'è una sola sessione oggi ([[sessione-2026-06-10]]), che fonderò nel daily. Ti torna? Dammi l'ok e scrivo.", messaggio utente "fai pure", blocco strumento **"Bash Read daily template, check existing"** con comando completo: "IN cd "/Users/giovannibeggiato/Desktop/aurora cervello" && cat workspace/journal/_templates/_template-daily.md 2>/dev/null && ..." "OUT Exit code 1" "---" "title: "Daily — YYYY-MM-DD"". Subito sotto appare il nuovo passo **"Write 2026-06-10.md"** "27 lines" — il file daily appena scritto. Sidebar sinistra: cartella `_templates` selezionata/evidenziata, sotto cartella `daily` ora espansa con il nuovo file `2026-06-10.md` appena creato, poi cartella `sessions` con `sessione-2026-06-10.md`.
Voce: *"durerà, forse è durato troppo rispetto a"* — commento del presentatore sulla durata del tutorial, mentre a schermo il file daily viene scritto.

### Scena 346 · `frame-1381.png` · 138:00 — doppio pannello: chat completata + `2026-06-10.md` (daily) aperto per intero ⭐
Editor diviso in due. Pannello sinistro "Italian greeting", scrollato ulteriormente: tool call "Bash Read daily template, check existing" con "Exit code 1" / "---" / "title: "Daily — YYYY-MM-DD"", poi "Write 2026-06-10.md" "27 lines", poi testo parzialmente visibile "Daily salvato:" e riquadro input "Queue another message...". Pannello destro, nuova tab **"2026-06-10.md"** (percorso "workspace > journal > daily > 2026-06-10.md"), contenuto del file daily generato, trascritto per intero:
```
---
title: "Daily — 2026-06-10"
summary: "Prima giornata tracciata del diario: test della skill journal, dal briefing di buongiorno alla chiusura di sessione."
tags: [workspace, type/daily]
status: done
created: 2026-06-10
updated: 2026-06-10
related:
  - "[[sessione-2026-06-10]]"
  - "[[progetto-arr-5m-2026]]"
---

# Daily — 2026-06-10

## Fatto
- Briefing di buongiorno sul cervello di Aurora Sistemi: diario di lavoro ancora vuoto, questa è la prima giornata tracciata.
- Testata la skill journal end-to-end: chiusura di sessione che salva correttamente la nota nel workspace.

## Deciso
- Agganciare le note di test a [[progetto-arr-5m-2026]], unico progetto attivo, per rispettare la regola del wikilink obbligatorio.

## Aperto
- Lavoro reale sul progetto ARR 5M e sul churn logo 2025 (~11%, sopra la soglia <10%) ancora da affrontare.

## Sessioni
- [[sessione-2026-06-10]]
```
Sidebar sinistra: cartella `daily` con `2026-06-10.md` selezionato/evidenziato, sotto cartella `sessions` con `sessione-2026-06-10.md`. Questo è l'ultimo output tecnico mostrato nel tutorial: il sistema di memoria viva end-to-end (skill journal + template + note agganciate via wikilink) completo e funzionante.
Voce: *"fatto, deciso, aperto, sessioni e ci"* — elenca esattamente le sezioni del file daily appena aperto e mostrato per intero a schermo.

### Scena 347 · `frame-1382.png` · 138:06 — webcam a schermo intero, presentatore guarda in basso mentre commenta
Solo webcam a piena inquadratura, stesso sfondo (mensola libri, pianta, lampada accesa). Il presentatore guarda leggermente in basso mentre parla, nessuno schermo software visibile.
Voce: *"siamo. Bene, signori, quindi direi che" / "abbiamo fatto il nostro tutorial sulla"* — chiude il segmento tecnico e apre le conclusioni del tutorial.

### Scena 348 · `frame-1383.png` · 138:12 — webcam a schermo intero, ringraziamento iniziale ⭐
Solo webcam, stessa inquadratura, il presentatore sorride leggermente parlando direttamente in camera, mano destra che accenna un gesto (parzialmente visibile a bordo inquadratura).
Voce: *"mille per essere arrivati fino alla"* — apre il ringraziamento conclusivo del video ("Grazie mille per essere arrivati fino alla fine").

### Scena 349 · `frame-1384.png` · 138:18 — webcam, prosegue il ringraziamento
Solo webcam, stessa inquadratura, presentatore che parla con espressione rilassata.
Voce: *"di più su come farlo in maniera anche"* — prosegue l'invito a scoprire come applicare il sistema "in maniera anche più massiva" per la propria azienda.

### Scena 350 · `frame-1386.png` · 138:30 — webcam, gesticola verso la fotocamera (call to action)
Solo webcam, il presentatore alza leggermente la mano destra (parzialmente visibile a bordo inquadratura) in un gesto enfatico mentre parla.
Voce: *"vendere questa tipologia di servizi da"* — introduce il richiamo alla propria community per chi vuole anche vendere questo tipo di servizio alle aziende.

### Scena 351 · `frame-1387.png` · 138:36 — webcam, presentatore sorridente a bocca aperta
Solo webcam, stessa inquadratura, espressione sorridente, bocca aperta a metà frase.
Voce: *"interattive con una community di ormai"* — continua a descrivere la propria community ("moduli su moduli e live interattive con una community di ormai 90 imprenditori").

### Scena 352 · `frame-1389.png` · 138:48 — webcam, ultimo frame del video: occhi chiusi, saluto finale ⭐
Solo webcam, ultimo frame estratto del blocco: il presentatore ha gli occhi chiusi e un'espressione rilassata/sorridente mentre pronuncia le parole di chiusura, stesso sfondo invariato per tutta la coda del video (mensola con libri, pianta, lampada accesa).
Voce: *"ovviamente grazie ancora per aver"* — penultima battuta del video, subito prima della chiusura letterale "...seguito il tutorial." con cui termina l'intero tutorial sulla company Brain.

---

# PARTE 2 - Trascrizione integrale del parlato

[00:00:02] Hei e benvenuti al tutorial più completo sulla company Brain. La company Brain è,
[00:00:04] secondo me, una di quelle cose che
[00:00:05] separerà chi usa l'AI per moltiplicare
[00:00:08] il proprio business da chi la usa per
[00:00:10] giocarci, però quasi nessuno sa davvero
[00:00:12] che cosa sia e ancora meno persone sanno
[00:00:15] come costruirne una. E quindi in questo
[00:00:17] video è esattamente questo quello che
[00:00:18] andremo a fare. Vi insegnerò a
[00:00:20] costruirne una da zero e lo farò passo
[00:00:23] passo con voi sul vostro business. Su
[00:00:25] YouTube non esistono ancora tutorial
[00:00:27] completi sull'argomento, quindi questo è
[00:00:29] quello che potete considerare il video.
[00:00:32] Se siete nuovi al canale, sono Joe con
[00:00:34] la mia agenzia di intelligenza
[00:00:35] artificiale Gente Sei. Facciamo
[00:00:37] consulenza ad aziende che vanno dai
[00:00:38] €10.000 al mese fino ai 50 milioni di
[00:00:41] euro all'anno ed ho poi una community
[00:00:42] privata di imprenditori e freelancer che
[00:00:45] vogliono applicare AI al loro business o
[00:00:47] che vogliono rivenderlo ad altre
[00:00:48] aziende. Detto questo, senza perdere
[00:00:50] ulteriore tempo, fatemi spiegare quello
[00:00:52] che vedremo oggi. Questo, innanzitutto
[00:00:54] sarà un corso estremamente pratico,
[00:00:55] quindi cominceremo dal capire qual è
[00:00:57] l'arrow delle company Brain per
[00:00:59] un'azienda, quindi i nostri secondi
[00:01:01] cervelli fatti con Cloud e perché ora è
[00:01:04] il momento in cui ogni azienda dovrebbe
[00:01:06] implementarne una. Passerò poi a
[00:01:08] presentarvi la company Brain in
[00:01:10] produzione fatta con 22.870
[00:01:13] 70 documenti e quindi qualcosa di questo
[00:01:16] tipo e vi darò esattamente la struttura
[00:01:19] e la faremo assieme, passo passo di
[00:01:21] cartelle che ho utilizzato e come ho
[00:01:24] fatto a gestire un contesto così grande.
[00:01:26] Quindi a fine di questo tutorial voi
[00:01:28] avrete capito come funziona, saprete
[00:01:30] come crearle e le avremo create tutte
[00:01:32] assieme. Capiremo poi come Obsidian,
[00:01:36] Notion, Gitab e vi spiegherò anche come
[00:01:38] ho utilizzato Quadrant, come tutte
[00:01:41] queste cose interagiranno tra loro,
[00:01:43] perché la nostra brain non deve essere
[00:01:44] solo bella da vedere, ma deve essere
[00:01:46] anche estremamente pratica. Quindi
[00:01:47] dovremmo avere il nostro layer AI, che è
[00:01:50] Obsidian, il nostro layer visivo per un
[00:01:53] eventuale team o per voi per poterlo
[00:01:55] utilizzare, quindi Notion. avremo una
[00:01:58] parte di version control, quindi un
[00:02:00] Google Drive o GitHub e poi dovremmo
[00:02:02] avere eventualmente un Rug se vogliamo
[00:02:04] scalarla. E poi detto questo,
[00:02:07] cominceremo a costruire la vostra con la
[00:02:09] stessa struttura della mia. Partiremo
[00:02:11] proprio dall'inizio, quindi cominceremo
[00:02:12] ad installare Obsidian, capiremo poi
[00:02:15] come funziona Obsidian, quindi andremo a
[00:02:17] parlare di tutte quelle cose che su
[00:02:19] YouTube non sono discusse, quindi cosa
[00:02:21] sono i Wikilinks, cosa sono i backlinks,
[00:02:23] cosa sono i formatter, come funzionano i
[00:02:25] tags, ma non solo. Andremo a definire
[00:02:27] che cos'è la differenza tra tassonomia
[00:02:30] ed ontologia e perché Obsidian riesce a
[00:02:33] creare appunto questa ontologia e come
[00:02:36] questo permette all'AI di navigare tra i
[00:02:38] vari collegamenti. Andremo a definire le
[00:02:41] 11 cartelle di progetto, quindi vi darò
[00:02:43] la struttura, diciamo, del vostro
[00:02:45] cervello con clud. Poi prenderemo il
[00:02:48] materiale grezo di qualunque azienda, io
[00:02:50] ho preparato una demo, e la trasformiamo
[00:02:52] nelle cosiddette note atomiche e poi le
[00:02:56] porteremo dentro Obsidian. Questo
[00:02:58] permetterà a voi di utilizzare qualsiasi
[00:03:01] cosa abbiate come conoscenza aziendale o
[00:03:04] dei vostri clienti ed inserirla dentro
[00:03:06] Obsidian. Tutto questo sarà ovviamente
[00:03:09] guidato passo a passo da questo Notion
[00:03:11] che ho preparato per voi, secondo link
[00:03:13] sotto in descrizione, nel quale
[00:03:15] troverete anche tutti i prompt che ho
[00:03:17] intenzione di utilizzare e tutto
[00:03:19] spiegato nel dettaglio. Quindi,
[00:03:21] letteralmente, la cosa che dovrete fare
[00:03:23] è semplicemente seguire il tutorial e
[00:03:25] replicare i miei passi per avere una
[00:03:27] company Brain funzionante alla fine di
[00:03:30] questo tutorial. Parleremo poi di che
[00:03:31] cos'è l'indice per l'AI e perché io vi
[00:03:34] consiglio di inserire un LLMS.
[00:03:37] txt e come entra in gioco quando l'AI
[00:03:40] deve fare retrieval di dati. Parleremo
[00:03:43] di come creare il nostro grafa, quindi
[00:03:45] su Obsidian, parleremo di GitHub e
[00:03:48] Google Drive per la version control,
[00:03:50] parleremo di come una volta che questa
[00:03:52] AI è stata settata potremmo utilizzare
[00:03:54] la stessa company Brain per avere delle
[00:03:57] raccomandazioni su come migliorare i
[00:03:58] nostri dati aziendali. parleremo dei
[00:04:00] nostri layer visivi, in particolare
[00:04:02] parleremo di Notion ed HTML e poi
[00:04:05] concluderemo con il parlare della
[00:04:08] memoria viva, quindi creeremo un sistema
[00:04:10] tale per cui quando lo salutiamo e
[00:04:13] quando usciamo aggiornerà
[00:04:15] automaticamente le nostre conversazioni
[00:04:17] e la nostra company Brain e permetterà a
[00:04:20] noi di avere quindi una memoria viva
[00:04:22] giorno per giorno che verrà aggiunta in
[00:04:24] automatico alla nostra company Brain.
[00:04:26] Detto questo, cominciamo. Cominciamo
[00:04:28] quindi con il settare delle aspettative
[00:04:29] per questo corso. Questo sarà un corso
[00:04:31] pratico. Che cosa vuol dire? Vuol dire
[00:04:33] che noi costruiremo passo passo la
[00:04:36] struttura del nostro company Brain.
[00:04:38] Significa che voi alla fine di questo
[00:04:39] video potrete o andare a rivendere
[00:04:41] questo servizio ad aziende nel caso in
[00:04:43] cui voi siate interessati o potrete
[00:04:45] settarlo nella propria azienda nel caso
[00:04:47] in cui voi vogliate. Il secondo è
[00:04:49] capiremo qual è il vantaggio competitivo
[00:04:52] di avere questa tipologia di sistema e
[00:04:54] perché dovete implementarlo il prima
[00:04:56] possibile nella vostra azienda. E la
[00:04:59] terza è saprete cosa serve per scalarlo
[00:05:03] e come potrete farlo. [sbuffare] Il
[00:05:05] motivo per cui dico questo è perché per
[00:05:07] capire questo corso avremmo bisogno di
[00:05:10] entrambe teoria e pratica per far sì che
[00:05:13] voi abbiate una visione di insieme di
[00:05:15] quello che può essere raggiunto con un
[00:05:17] company brain. Quindi cominciamo con il
[00:05:20] definire che cos'è quella che noi
[00:05:23] intendiamo conoscenza sparsa e perché
[00:05:25] dovremmo averne uno. E per farlo andiamo
[00:05:27] a vedere cosa succede in una qualsiasi
[00:05:29] realtà aziendale. Spesso si pensa che la
[00:05:32] conoscenza sia semplicemente il nostro
[00:05:35] PDF, il nostro file Word le nostre SOP
[00:05:39] aziendali. La verità è che la conoscenza
[00:05:42] è in tre zone distinte all'interno della
[00:05:45] nostra azienda. La prima è nelle chat,
[00:05:48] quindi cose che abbiamo lasciato in una
[00:05:51] chat aziendale, Slack o in una mail o un
[00:05:55] documento che è lì. E questa conoscenza
[00:05:57] ha rischio di essere cancellata o venire
[00:06:00] persa nel tempo, poiché diventa
[00:06:02] difficile riprenderla o capire dove in
[00:06:06] primis questa conoscenza era nel momento
[00:06:08] in cui abbiamo bisogno di ricercarla,
[00:06:10] no? Quindi il nostro collega che non si
[00:06:12] ricorda dove ci ha mandato le cose o noi
[00:06:14] che abbiamo mandato un documento, ma non
[00:06:16] sappiamo se è su Slag, su Gmail o con
[00:06:18] che indirizzo l'abbiamo mandato. La
[00:06:20] seconda tipologia di conoscenza invece
[00:06:22] che noi abbiamo è quella nella testa
[00:06:25] delle persone. Allora, qui abbiamo un
[00:06:27] mondo che si apre perché perché noi
[00:06:30] possiamo vedere questa tipologia di
[00:06:31] conoscenza come la conoscenza nella
[00:06:36] testa delle persone nel caso in cui
[00:06:38] abbiamo un cosiddetto top performer,
[00:06:41] giusto? Quindi una persona che è
[00:06:44] estremamente
[00:06:45] competente e quindi per l'azienda questa
[00:06:48] persona vale oro. Oppure potremmo vedere
[00:06:51] questo come una tipologia di conoscenza
[00:06:54] che rende difficile l'onboarding delle
[00:06:56] persone. Quindi eh che cosa vuol dire?
[00:06:59] vuol dire che magari abbiamo un classico
[00:07:02] specialista di processo che ha gran
[00:07:05] parte della conoscenza nella sua testa,
[00:07:07] proprio perché magari ha lavorato per 10
[00:07:08] anni nella stessa posizione e quindi
[00:07:11] questo rende difficile avere una
[00:07:13] metodologia standard per portare qualcun
[00:07:16] altro a coprire il ruolo se dobbiamo
[00:07:17] muovere questa persona o nel caso in cui
[00:07:20] dovessimo scalare l'azienda perché
[00:07:23] diventa un bottle il neck aziendale, no?
[00:07:24] Perché in questo caso questa tipologia
[00:07:27] di conoscenza è abbastanza eh buona ma
[00:07:30] dannosa perché immaginate che voi
[00:07:33] vogliate scalare la vostra azienda, voi
[00:07:35] avete che il vostro bottlene neck è
[00:07:38] esattamente quindi il momento in cui il
[00:07:41] collo di bottiglia che voi avete è
[00:07:43] esattamente la conoscenza di questa
[00:07:45] persona. Quindi qui, se la conoscenza di
[00:07:47] questa persona non viene ehm messa come
[00:07:51] una SOP aziendale, quindi in qualche
[00:07:53] modo descritta, definita, beh, l'azienda
[00:07:56] fa fatica a scalare perché senza magari
[00:07:57] questo processo non riusciamo ad andare
[00:08:00] oltre. Un'altra cosa che c'è da dire e
[00:08:03] che è il lato negativo del top perform.
[00:08:14] Beh, allora capite che abbiamo un impatto su tutti i KPI aziendali perché?
[00:08:17] Beh, perché innanzitutto se un top
[00:08:20] perform, l'azienda comincia a rimetterci
[00:08:22] in termini economici ed il motivo è
[00:08:24] molto semplice. Il top performer fa un
[00:08:25] lavoro perfetto o fatto al meglio delle
[00:08:29] eh degli standard, insomma, che
[00:08:31] l'azienda si aspetta, motivo per cui c'è
[00:08:33] questo eh ritorno economico molto
[00:08:35] importante. La seconda problematica del
[00:08:38] top performer è solo lui. Cioè se noi
[00:08:41] non documentiamo questo tipo di
[00:08:43] conoscenza, non abbiamo modo di fare
[00:08:47] training dei nostri impiegati e di
[00:08:50] spiegare loro che cos'è che questo top
[00:08:52] performer sta facendo, che loro non
[00:08:53] stanno facendo, e di modo tale da
[00:08:56] migliorare il livello. Ma al terzo è
[00:08:59] anche un problema di tempo, giusto?
[00:09:02] Perché se il top performer se ne va, noi
[00:09:05] dobbiamo avere cosa? Dobbiamo spendere
[00:09:07] un sacco di tempo per assumere una
[00:09:11] persona che abbia lo stesso livello di
[00:09:13] conoscenza e per fare di nuovo training
[00:09:17] a questa persona, perché magari è
[00:09:19] l'imprenditore che è l'unico con quella
[00:09:22] tipologia di conoscenza lì, ehm, di
[00:09:25] personale nuovo che possa riarrivare a
[00:09:27] quel livello. Quindi vedete che queste
[00:09:29] tre cose sono estremamente collegate
[00:09:31] l'una all'altra, no? Quindi termini
[00:09:33] economici l'azienda perde immediatamente
[00:09:35] a livello di fatturato, magari top sales
[00:09:37] manager se ne va. Secondo, non abbiamo
[00:09:40] la possibilità di fare training. Terzo,
[00:09:42] perdiamo in tempo proprio perché non
[00:09:44] abbiamo le prime due e quindi dobbiamo
[00:09:46] sopperire alla mancanza.
[00:09:49] La terza tipologia invece di conoscenza
[00:09:51] che abbiamo
[00:09:53] è quella sparsa nei 20.000 tool diversi
[00:09:57] che nessuno utilizza. Che cosa vuol
[00:09:59] dire? Vuol dire che qui abbiamo magari
[00:10:02] che la nostra conoscenza aziendale per
[00:10:05] quanto riguarda le policy è su un PDF da
[00:10:09] qualche parte, no? Poi magari abbiamo
[00:10:11] che il nostro fatturato annuale è su un
[00:10:15] file Excel e quindi magari abbiamo lì
[00:10:19] oppure abbiamo che l'informazione del
[00:10:21] fornitore è messa dentro la nostra mail
[00:10:24] oppure abbiamo Zapier, oppure ovunque
[00:10:26] voi vogliate, abbiamo 1000 strumenti
[00:10:29] diversi. che impattano negativamente. E
[00:10:32] questo che impatto ha a livello
[00:10:34] economico? Benissimo, per farlo andiamo
[00:10:36] a vedere i dati di chi queste cose le fa
[00:10:40] per professione e quindi chi studia
[00:10:43] questi ehm impatti a livello economico e
[00:10:46] capiamoli da l'alto livello per capire
[00:10:50] dove noi possiamo appunto portare a ROI.
[00:10:52] Il primo dato che ci viene subito sotto
[00:10:55] occhio è questo e cioè il 19%
[00:10:59] della settimana lavorativa di un
[00:11:01] impiegato viene passato a cercare
[00:11:04] informazioni. Ok? Questo dato di McKinsy
[00:11:07] è un dato abbastanza, per quanto mi
[00:11:09] riguarda, tragico e se avete mai
[00:11:12] lavorato in big corporate o in aziende
[00:11:14] di grosse dimensioni, sapete che questo
[00:11:16] dato non è per niente, è una sovrastima,
[00:11:18] perché se qualcuno deve fare una cosa su
[00:11:21] un processo vengono perse le mezze
[00:11:23] giornate per capire come il processo
[00:11:25] funziona, chi è la persona giusta, quale
[00:11:28] team dovrebbe fare cosa e non c'è mai
[00:11:31] una ehm ownership diretta, no, di come
[00:11:34] funziona
[00:11:35] chi è, eccetera eccetera. E quindi
[00:11:37] queste mezze giornate vengono perse
[00:11:39] proprio per solo per capire dove
[00:11:42] prendere le informazioni. A me è
[00:11:44] successo eh nella mia carriera
[00:11:46] corporate, ho fatto due grosse aziende,
[00:11:48] di perdere anche 3-4 giorni per capire
[00:11:51] chi doveva essere il mio punto di
[00:11:53] riferimento per qualcosa. Immagino che
[00:11:55] nelle aziende piccole ci possa essere un
[00:11:56] piccolo offset, no, di questo numero,
[00:11:58] quindi magari è un po' più piccolo nella
[00:12:00] ricerca di informazioni, ma sicuramente
[00:12:03] ci saranno delle altre cose che vanno a
[00:12:05] impattare, no, su questo. Magari la
[00:12:07] documentazione è fatta male, per
[00:12:09] esempio, magari non avete delle degli
[00:12:11] standard aziendali sufficienti. Il
[00:12:13] secondo dato che invece vogliamo è che
[00:12:17] ehm un nuovo assunto ci mette in media
[00:12:20] 8-1 mesi per diventare davvero
[00:12:22] produttivo. Allora, questo dato è
[00:12:24] assolutamente una cosa che posso
[00:12:26] confermarvi. Io nella mia carriera ho
[00:12:28] fatto il manager di della parte
[00:12:32] produzione, avevo un team di 75 persone
[00:12:35] e la cosa che vi posso dire ehm se vi
[00:12:37] interessa, ho fatto Pampers Europa e e
[00:12:40] Midolast, però quello che vi voglio dire
[00:12:42] è la curva di apprendimento delle
[00:12:45] persone e nel caso voi non l'abbiate mai
[00:12:47] vista, ve la mostro ve la mostro al
[00:12:49] volo, ha una forma di questo tipo. Ok?
[00:12:53] Quindi se questo è il tempo,
[00:12:56] ok? E questo è la curva di
[00:12:59] apprendimento,
[00:13:01] la curva di apprendimento ha una forma
[00:13:02] del genere, cioè l'impiegato comincia ad
[00:13:04] imparare, poi si accorge di non sapere e
[00:13:07] dopo va e impara. Ok? Ovviamente qui poi
[00:13:11] avrà un plateau dato dalla dal fatto che
[00:13:14] diventa un esperto nel ruolo. Ok? Il
[00:13:17] problema di questo è che questo puntino
[00:13:19] qui, quando parliamo di top performer,
[00:13:22] abbiamo che avviene tra i tre e i 6
[00:13:25] mesi, ok? 3 mesi siete proprio stellari.
[00:13:29] Quando parliamo di un mid performer
[00:13:32] abbiamo che avviene tra gli 8 e i 12
[00:13:34] mesi. Quando parliamo di un low
[00:13:36] performer parliamo di una cosa che va
[00:13:38] dai 14 ai 18 mesi. Ok? Questo è il
[00:13:44] motivo per cui se siete nella carriera
[00:13:47] impiegatizia in genere non si fa ehm job
[00:13:53] rotation o cambiare ruolo in azienda,
[00:13:55] non so come si dica, prima dei 2 anni.
[00:13:58] Ok? Cioè questo è esattamente il motivo
[00:14:02] per cui il vostro employer vi tiene in
[00:14:05] una posizione per almeno 2 anni. Ed il
[00:14:08] motivo è molto semplice perché in questa
[00:14:11] parte qui, ok, che la la faremo
[00:14:14] arancione,
[00:14:16] voi state guadagnando, quindi voi
[00:14:21] guadagnate,
[00:14:23] mentre nella parte successiva
[00:14:28] è l'azienda
[00:14:31] che guadagna.
[00:14:33] Ok? Quindi capite bene che che per un
[00:14:37] imprenditore o per voi che vendete
[00:14:38] questo servizio o per voi che volete
[00:14:40] implementare questa knowledge aziendale,
[00:14:42] avete tutto l'interesse a ridurre questa
[00:14:46] parte qui, ok? Questa parte qui dove
[00:14:51] diciamo è semplicemente eh l'impiegato
[00:14:55] che deve capire bene come funziona il
[00:14:58] ruolo. Se riusciamo a ridurla riusciamo
[00:15:00] a massimizzare i guadagni aziendali.
[00:15:03] Questo vuol dire che abbiamo una marea
[00:15:04] di implicazioni importanti che ad oggi
[00:15:07] non sono chiare a molte persone, che
[00:15:09] sono che l'azienda
[00:15:13] guadagna di più,
[00:15:16] vuol dire che possiamo avere, nel caso
[00:15:20] volessimo, la cosiddetta job rotation,
[00:15:23] quindi aiutare gli impiegati a crescere
[00:15:26] in carriera ehm molto più velocemente
[00:15:29] perché non devono più stare in un ruolo
[00:15:31] troppo a lungo, perché sono AI ehm
[00:15:34] supportati da AI e questo ha una cosa
[00:15:37] che in azienda serve un sacco se avete
[00:15:39] una cultura forte, vi permette di
[00:15:42] ridurre quello che viene definito il
[00:15:45] chn, ok? che è una è una metrica che
[00:15:47] viene definita in percentuale, che è il
[00:15:49] tasso di abbandono degli impiegati
[00:15:51] dall'azienda per insoddisfazione.
[00:15:53] Ovviamente su questo incidono altri
[00:15:55] fattori eh come paga e soddisfazione nel
[00:16:00] lavoro, eccetera eccetera eccetera, ma
[00:16:02] un fattore importante è il tempo e che
[00:16:06] l'impiegato rimane dentro e quindi
[00:16:08] capite che se vi sta aiutando a ridurre
[00:16:11] il chn, ok? ovviamente avete un ritorno
[00:16:15] dal punto di vista economico, quindi
[00:16:17] spero di cominciare a trasmettervi
[00:16:18] quanto importante sia questa tipologia
[00:16:21] di servizio a livello business prima
[00:16:23] ancora di andare a premere i bottoncini
[00:16:25] per capire poi, no, che cosa e come la
[00:16:29] facciamo. Bene, la terza è quella che
[00:16:32] abbiamo detto prima, cioè quando una
[00:16:34] persona se ne va porta via la
[00:16:36] conoscenza, ok? e noi non vogliamo
[00:16:38] questa cosa. Quindi eh spero vi piaccia
[00:16:41] la metafora, ma eh quando questo
[00:16:44] impiegato esce dalla porta, esce dalla
[00:16:47] dall'azienda, no, un un pezzo di
[00:16:50] aziendina. Ora il pushback più grande è
[00:16:54] Oddio No, ma i dati aziendali. Allora,
[00:16:57] chiariamoci e parliamo velocemente.
[00:16:59] Quello che sta succedendo è questo e
[00:17:02] cioè e che vi piaccia o no, succede in
[00:17:05] tutte le aziende. Il dipendente, che è
[00:17:07] il nostro amico e lo chiamiamo Joe, Joe
[00:17:11] vuole fare il suo lavoro nel modo più
[00:17:13] efficiente possibile e Joe tende ad
[00:17:15] essere un impiegato pigro. Allora, che
[00:17:18] cosa succede? Joe, siccome non ha un AI
[00:17:22] dedicata, che cosa fa? prende il suo
[00:17:24] contratto, prende magari il listino
[00:17:26] prezzi, prende i dati interni
[00:17:28] all'azienda e cosa fa? Li sbatte dentro
[00:17:31] cvt.
[00:17:32] E questo è la prima cosa che succede. E
[00:17:35] che cosa vuol dire? Beh, vuol dire che
[00:17:37] molto probabilmente gran parte dei
[00:17:38] vostri dati, che vi piace o meno, a meno
[00:17:40] che non siate un solo preneur, ehm, sono
[00:17:43] già dove devono essere. Ok? Queste
[00:17:45] grandi aziende probabilmente li hanno
[00:17:47] già tutti. Ehm, succede anche nelle
[00:17:50] grosse aziende, quindi mi aspetto che
[00:17:52] nelle piccole succeda più o meno la
[00:17:53] stessa cosa e vuol dire che
[00:17:56] probabilmente i vostri dati sono già in
[00:17:57] Cina, in qualche bel server o in America
[00:18:00] altrettanto e quindi i vostri dati poi
[00:18:03] non sono così speciali. E questo è se vi
[00:18:06] è mai arrivata una chiamata da un numero
[00:18:08] un centralino, eh, sapete quelli
[00:18:11] automatici che o elettronici, come li
[00:18:13] volete chiamare, che dicono "Ehi, ciao,
[00:18:15] sono tizio di e questo servizio". E voi
[00:18:17] dite "Ma io non ho mai dato il consenso
[00:18:19] a essere chiamato o non vi conosco".
[00:18:21] Beh, vuol dire che i vostri dati sono
[00:18:22] già ovunque. Bene, la seconda invece che
[00:18:24] è quella che mi interessa un po' di più
[00:18:25] è che la vostra AI è intelligente quanto
[00:18:29] ciò che può leggere della vostra
[00:18:31] azienda. Ok? Che cosa vuol dire? Vuol
[00:18:34] dire che sia voi che il vostro
[00:18:36] competitor state utilizzando lo stesso
[00:18:40] sistema. Ok? Che cosa vuol dire? Che se
[00:18:43] entrambi state utilizzando chat CBT
[00:18:46] senza un contesto vostro alla fine il
[00:18:50] fatto che voi stiate usando AI non ha
[00:18:53] alcun vantaggio competitivo. State
[00:18:55] ottenendo tutti la stessa identica
[00:18:58] risposta. E questo è importante perché
[00:19:01] le persone fanno eh vedo eh ovunque ehm
[00:19:06] che c'è questa formazione su Chat CVT,
[00:19:09] Gemini, Clodno
[00:19:12] usando allo stesso modo, cioè mediamente
[00:19:15] male. E il fatto che voi abbiate un
[00:19:16] prompt un po' meglio non vi dà alcun
[00:19:18] vantaggio competitivo perché iterando in
[00:19:20] maniera sufficientemente lunga chiunque
[00:19:23] può arrivare alla vostra conclusione.
[00:19:24] Quindi questo è per dirvi attenzione che
[00:19:27] se la vostra AI non è allenata sui
[00:19:29] vostri dati aziendali state ottenendo le
[00:19:32] stesse risposte dei vostri competitor e
[00:19:34] quindi c'è un livello, chiamiamolo zero,
[00:19:38] e quindi non è un utilizzo che vi porta
[00:19:40] ad alcun vantaggio competitivo. E quindi
[00:19:43] per concludere, prima di mostrarvi la
[00:19:45] demo, voglio dirvi perché è importante
[00:19:48] che voi quindi abbiate una vostra AI e
[00:19:51] una vostra company Brain e come questa
[00:19:53] evolverà nel vostro nel corso del tempo
[00:19:55] e vi darà un vantaggio competitivo
[00:19:57] importante. Allora, il fulcro di tutto
[00:20:01] è, e vorrei fermarmi sulla prima parte,
[00:20:03] che queste company Brain
[00:20:07] sono che vedremo ora, sono dei
[00:20:11] giganteschi cervelli che cominciano a
[00:20:15] contenere mano tutta la conoscenza
[00:20:18] azianzale e cominciano a conoscervi nel
[00:20:20] corso del tempo. Che cosa vuol dire?
[00:20:22] Vuol dire che noi partiamo ogni giorno
[00:20:25] cominciamo ad utilizzarla
[00:20:27] la nostra memoria comincia a crescere,
[00:20:30] la conoscenza dell'AI diventa migliore
[00:20:32] per quanto riguarda la nostra azienda,
[00:20:34] quindi ci comincia a conoscere meglio.
[00:20:36] Riceveremo poi risposte migliori. Con
[00:20:39] risposte migliori noi potremmo
[00:20:41] continuare a riutilizzarla sempre in
[00:20:43] maniera più efficiente. Questo ciclo
[00:20:45] continua. Quindi questo, in poche parole
[00:20:47] che cosa vuole dire? Vuol dire che per
[00:20:49] fare una rappresentazione grafica super
[00:20:51] semplice, se questo
[00:20:55] e fatemi vedere se anche voi lo vedete.
[00:20:58] Perfetto. Sì, se questo è il vostro
[00:21:01] tempo e questo è il vostro ritorno
[00:21:04] sull'investimento che avete
[00:21:06] nell'utilizzare questo tipo di eh
[00:21:08] sistema, eh se voi non lo utilizzate,
[00:21:12] avrete una curva nell'utilizzo dell'AI
[00:21:15] più o meno fatta così.
[00:21:18] Ok? Perché? Perché i modelli di AI
[00:21:21] diventano migliori e quindi il fatto che
[00:21:23] voi utilizziate CH CPT diventa migliore
[00:21:26] di default e così però anche tutti i
[00:21:29] vostri competitor, quindi non
[00:21:31] dimenticatevi che la la curva dei
[00:21:33] competitor cresce esattamente come la
[00:21:35] vostra, quindi ha zero vantaggio
[00:21:37] competitivo. Avete solo un ritorno
[00:21:39] dell'investimento migliore perché vi
[00:21:40] aiuta meglio nei vostri processi
[00:21:41] interni, ma come voi a tutti gli altri.
[00:21:44] Mentre se utilizzate una company Brain
[00:21:45] come quella che avremo oggi, avremo una
[00:21:47] curva di questo tipo, no? perché l'AI
[00:21:49] comincia a conoscervi sempre meglio e
[00:21:51] questo è esattamente il vostro vantaggio
[00:21:54] competitivo. Non dimenticatevi che
[00:21:57] questo ha un impatto enorme anche in
[00:21:59] ambito startup e cioè se voi siete
[00:22:01] un'azienda strutturata, e questo ci
[00:22:03] tengo a specificarlo perché non molti
[00:22:04] l'hanno capito, chi vincerà nell'AI o
[00:22:08] chi avrà il miglior ritorno
[00:22:09] nell'investimento sono le aziende grosse
[00:22:12] perché perché loro hanno già dei
[00:22:14] processi, hanno già un sacco di
[00:22:15] conoscenza. Quindi l'EI può essere
[00:22:18] allenata su un sacco di dati. Noi ci
[00:22:20] stiamo muovendo in un mondo che è sempre
[00:22:22] più, come dicono eh gli inglesi,
[00:22:25] governato dai dati, no? Quindi data
[00:22:27] first. E con l'AI i dati sono il nuovo
[00:22:31] oro, come lo erano per i social media,
[00:22:33] ma ora ancora di più, ma in questo caso
[00:22:36] sono i vostri dati per la vostra
[00:22:38] azienda. E che cosa vuol dire? che il
[00:22:41] vostro vantaggio competitivo è anche
[00:22:43] rispetto alla startup che vuole fregarvi
[00:22:46] o domani eccetera, che la startup avrà
[00:22:50] un lag, quindi un ritardo di tutta
[00:22:53] questa parte qui, ipotizzando che la
[00:22:55] startup, non lo so, entri qui. Ok? Avrà
[00:22:59] un ritardo di tutte queste tutto questo
[00:23:02] periodo qui che voi avrete modo con la
[00:23:06] vostra AI di colmare. Ok? Benissimo,
[00:23:11] questo è il primo. Quindi, detto questo,
[00:23:13] perché dovreste farlo oggi? Eh beh,
[00:23:16] perché eh avrete quello che noi
[00:23:19] definiamo arbitraggio. Ok? Quindi, come
[00:23:24] si misura l'arbitraggio? L'arbitraggio è
[00:23:26] la differenza tra ehm in parole
[00:23:29] semplici, quello che fate voi oggi e
[00:23:33] quello che fa il mercato domani. Voi
[00:23:35] avete un arbitraggio, sia che vendiate
[00:23:37] questo servizio che che lo applichiate e
[00:23:39] poi andremo alla demo perché se voi oggi
[00:23:42] fate questo e oggi il vostro competitor
[00:23:45] sta facendo questo, questo qui è il
[00:23:48] vostro arbitraggio, no?
[00:23:50] E abbiamo che questo si articola in due
[00:23:53] parti, è il vantaggio competitivo
[00:23:57] dell'azienda che lo sta applicando alla
[00:23:59] propria ed è anche il fattore novità e
[00:24:03] Rai estremamente elevato che voi potete
[00:24:07] portare in quanto freelancer per questa
[00:24:09] tipologia di servizio. Ovviamente questa
[00:24:11] finestra lentamente si chiuderà perché
[00:24:14] uno perché canali YouTube come il mio
[00:24:17] servono a aumentare la consapevolezza di
[00:24:19] quello che la può fare. Due, perché ci
[00:24:21] sono, per esempio, community come la
[00:24:23] mia, nella quale io insegno ad
[00:24:25] imprenditori e freelancer come applicare
[00:24:27] queste cose nella loro azienda o come
[00:24:28] rivenderle. Quindi, ovviamente, chi
[00:24:30] prima comincia eh meglio si trova. Bene,
[00:24:33] detto questo, spero di avervi dato
[00:24:34] un'infarinatura sufficiente per
[00:24:37] convincervi che guardare questo corso
[00:24:39] avrà un elevato arroi per voi. E ora
[00:24:42] direi procediamo alla demo di modo tale
[00:24:44] che voi possiate capire anche a livello
[00:24:46] pratico eh qual è effettivamente il
[00:24:49] vantaggio e vederlo proprio e toccarlo
[00:24:51] con mano. Ed ecco con cosa stiamo
[00:24:54] giocando. Questa sarà la company Brain
[00:24:58] che noi con calma andremo ora a
[00:25:01] ricostruire in questo video. Ovviamente
[00:25:02] non useremo tutti i file che sono qua
[00:25:05] dentro, sono 22.500
[00:25:08] note. Questa è una company Brain
[00:25:11] Production Ready, totalmente
[00:25:13] funzionante, vedete? è abbastanza
[00:25:14] massiva eh per essere una company brain.
[00:25:18] Vi replicheremo esattamente la struttura
[00:25:20] e vi farò vedere poi come dividere le
[00:25:24] cose. Vi darò i prompti per poter
[00:25:26] inserire le vostre cose all'interno di
[00:25:27] questa cosa qui. Questa eh è production
[00:25:31] ready, quindi che cosa vuol dire? che in
[00:25:33] questo tutorial andremo a vedere come
[00:25:36] costruire queste cartelle, andremo a
[00:25:38] vedere come collegarla con il nostro
[00:25:41] notion di modo tale da avere un layer
[00:25:44] per le AI per capire come trovare i dati
[00:25:48] e anche un layer visivo per noi per
[00:25:50] poterci interfacciare con l'AI, no? E
[00:25:53] dopo e questa ha anche tutta la parte di
[00:25:57] Rag connesso. Ovviamente per un video
[00:26:00] YouTube questa parte è troppo difficile,
[00:26:03] quindi avrebbe poco senso che io vi
[00:26:05] faccia vedere come scalare un sistema a
[00:26:07] 22.500 note production ready. Se siete
[00:26:10] un imprenditore o un freelancer e volete
[00:26:12] approfondire questi servizi e ricevere
[00:26:14] il prompt applicare questo one shot
[00:26:16] nella vostra azienda, eh vi lascio il
[00:26:18] link sotto in descrizione che è il link
[00:26:20] per la mia community. Bene, detto
[00:26:21] questo, cominciamo a testarla per farvi
[00:26:23] vedere cosa andremo a fare oggi. Allora,
[00:26:25] andiamo nella nostra company knowledge
[00:26:28] base, quindi in quella gigantesca e
[00:26:31] apriamola. E adesso cominciamo con il
[00:26:35] fare una quiri un po' ehm diciamo
[00:26:39] ingannevole per l'AI, perché vogliamo
[00:26:41] testare quanto forte è l'AI. Ehi, ah sai
[00:26:44] dirmi ehm qual è il cliente più grosso
[00:26:47] per questa azienda? E questa perché è
[00:26:49] una qui ingannevole? Perché se ci
[00:26:51] soffermiamo su più grosso, più grosso
[00:26:54] vuol dire che il mio cliente è il più
[00:26:57] grosso in termini del suo fatturato,
[00:27:03] oppure è più grosso in termini di valore
[00:27:07] per la mia azienda, quindi il cliente
[00:27:10] che mi paga di più. Tutte queste cose
[00:27:12] non le abbiamo ancora definite. Quello
[00:27:14] che noi vediamo ora è che il cliente più
[00:27:16] grosso è Residenze Aurora Verde, che è
[00:27:20] €620.000
[00:27:22] di ARR. Allora, questo è vero o no? Per
[00:27:25] controllarlo basta andare nel nostro
[00:27:27] notion e vediamo che il cliente è
[00:27:30] corretto, no? Quindi vediamo che l'AI ha
[00:27:33] interpretato bene eh diciamo la nostra
[00:27:36] richiesta e vediamo anche che nella
[00:27:38] nostra cartella clienti noi non abbiamo
[00:27:40] altri riferimenti. Ok? Ora questo è una
[00:27:45] semplice quemo averne qualsiasi di quiri
[00:27:50] all'interno di questa nostra conoscenza,
[00:27:51] quindi chi è il nostro COO, dove ha
[00:27:54] messo il tizio quel file, come funziona,
[00:27:57] eccetera. Ma non solo, abbiamo la
[00:27:59] possibilità di avere anche
[00:28:00] un'interazione dinamica tra le nostre
[00:28:02] piattaforme, quindi Obsidian con Notion
[00:28:05] e poi Notion con
[00:28:08] Obsidian. Vediamo un esempio. Hey!
[00:28:12] Il
[00:28:14] polo universitario sud ha incrementato
[00:28:20] il suo ARR, quindi il suo ricavo annuo
[00:28:23] nei nostri confronti e ha ora un ARR di
[00:28:29] €750.000
[00:28:31] l'anno. Puoi per favore aggiornare
[00:28:33] Obsidian e assicurarti che tutto sia
[00:28:35] aggiornato? Perfetto, premiamo invio e
[00:28:38] vedete che ora quello che sta facendo è
[00:28:40] il brain sync. Che cosa vuol dire? che
[00:28:43] sta adesso facendo una propagazione
[00:28:45] completa su tutti i sistemi che abbiamo
[00:28:48] eh collegato. Quindi ora quello che farà
[00:28:51] sarà prima scrivere su Obsidian che noi
[00:28:55] abbiamo richiesto di fare insomma
[00:28:57] qualcosa quindi con queste due
[00:28:59] metodologie e dopo una volta fatto
[00:29:02] utilizzerà questa skill per aggiornare
[00:29:04] tutte le nostre interfacce grafiche di
[00:29:06] modo tale che tutti abbiano live accesso
[00:29:09] a tutte le informazioni di cui abbiamo
[00:29:12] bisogno. Perfetto. Allora, vediamo che
[00:29:15] il nostro polo universitario sud ora è a
[00:29:19] 750.000
[00:29:24] l'anno e se noi andiamo nella nostra conversazione e gli ridiamo il solito
[00:29:27] prompt che abbiamo eh visto prima,
[00:29:31] dovremmo, se tutto va bene, ricevere che
[00:29:34] il nostro cliente, diciamo, più grosso è
[00:29:38] questo Polo Sud. Poi potremmo anche
[00:29:41] chiedere di vedere il il file markdown e
[00:29:45] lì vedremo che effettivamente questi
[00:29:47] dati sono stati cambiati. Il cliente è
[00:29:49] il Polo Sud, il più alto tra nominante,
[00:29:51] è un cliente SNB, eccetera. Per contesto
[00:29:54] i sufficienti, i successivi in
[00:29:55] classifica sono eccetera eccetera
[00:29:57] eccetera. Ok? Polo punmarkdown e quindi
[00:30:01] qui vediamo che il cliente ha un ARR di
[00:30:05] €750.000 €00 e questo si è ripercosso
[00:30:07] ovunque anche poi nel nostro database.
[00:30:10] Quindi questo è esattamente quello che
[00:30:13] andremmo a creare oggi. Andremo anche a
[00:30:15] capire come il collegamento con Notion
[00:30:17] avviene e cioè letteralmente
[00:30:19] ricostruiremo questa interfaccia e eh
[00:30:21] alla fine voi avrete modo di cominciare
[00:30:24] a popolare la vostra company Brain di
[00:30:26] modo tale che possa diventare una sfera
[00:30:28] perfetta, insomma, come questa.
[00:30:30] Benissimo, detto questo, eh andiamo alla
[00:30:33] parte pratica e un piccolo disclaimer è
[00:30:36] che per fare questo ehm video vi ho
[00:30:39] preparato, che trovate nel secondo link
[00:30:41] in descrizione, un company brain con
[00:30:44] tutti i prompt modo tale che voi
[00:30:46] possiate farli passo passo. È una bvi
[00:30:48] breve descrizione, insomma. Quindi, ehm,
[00:30:52] andate lì e se volete fare, e ve lo
[00:30:55] consiglio, le cose passo passo con me,
[00:30:58] quindi faremo un po' di teorie e poi l'
[00:30:59] applicheremo subito, eh, per favore
[00:31:02] andate nel nel file, mettetevelo in un
[00:31:05] secondo schermo e poi riuscite a seguire
[00:31:07] facendo tutto. Cominciamo eh con il
[00:31:10] scaricare Obsidian e dopo vi spiego
[00:31:12] brevemente che cos'è perché c'è un po'
[00:31:14] di fraintendimento. Allora, andiamo qui,
[00:31:16] ovviamente premiamo Obsidian. Perfetto,
[00:31:18] possiamo andare qua, premere download e
[00:31:21] fate download per macOS o insomma
[00:31:24] qualsiasi cosa voi abbiate. Ed una volta
[00:31:26] che lo avete aperto dovreste avere
[00:31:28] questo ehm questa schermata qui insomma
[00:31:31] nel desktop, questa applicazione che
[00:31:32] viene fuori. Ehm la cosa che facciamo
[00:31:35] adesso è creare questa cartella. Io ho
[00:31:37] chiamato la nostra cartella di lavoro
[00:31:39] Aurora Cervello. Ok? E perché lo faremo?
[00:31:43] Perché Obsidian ovviamente è un layer
[00:31:46] che va sopra la cartella e ci permette
[00:31:48] di avere una rappresentazione visiva di
[00:31:50] quello che c'è. Quindi ad obsidian serve
[00:31:53] una cartella per mostrarci i dati.
[00:31:54] Allora, cominciamo ad aprirlo. Voi
[00:31:56] premerete, eh allora farete open folder
[00:32:00] as vault e andremo in Aurora cervello.
[00:32:04] Quindi, semplicemente ora abbiamo il la
[00:32:07] nostra rappresentazione di assolutamente
[00:32:10] niente perché la cartella è vuota e
[00:32:12] comeè giusto che sia non ci sono file.
[00:32:15] Allora, cominciamo subito con il vedere
[00:32:17] che cos'è Obsidian. E allora per farlo
[00:32:20] metterò anche questa a tutto schermo di
[00:32:21] modo tale che lo vediamo e cominciamo a
[00:32:24] creare la nostra prima nota e la
[00:32:26] chiamiamo una nota ciao e ci scrivo
[00:32:28] qualcosa.
[00:32:30] Ah, come vedete qui ora è comparso
[00:32:32] questo ciao, però se vado nel mio Aurora
[00:32:35] cervello vedo che ho che ciao è in un
[00:32:40] formato markdown e se poi lo vado ad
[00:32:42] aprire dentro ad una ID vedo
[00:32:44] letteralmente che c'è scritto qualcosa
[00:32:47] che è quello che ho scritto dentro.
[00:32:48] Quindi da qui capiamo che cos'è
[00:32:51] Obsidian. Obsidian
[00:32:54] database e molte persone confondono
[00:32:57] queste due cose. Motivo per cui quando
[00:33:00] andate su 1000, 2000, 3000 note
[00:33:03] comincerà a fare fatica, no? Ma Obsidian
[00:33:07] è un layer che permette di collegare
[00:33:11] varie note markdown. Ok? Vedremo dopo
[00:33:15] perché l'AI preferisce questo layer e
[00:33:18] come fare questi formati markdown
[00:33:20] leggibili dall'AI, ma questo è quello
[00:33:22] che stiamo andando a fare. Ora, se voi
[00:33:25] notate poi nella nostra graph view, che
[00:33:27] è quella che vi permette di avere la
[00:33:29] vostra visualizzazione a palla, abbiamo
[00:33:32] la nostra prima nota. Ovviamente,
[00:33:36] allora, se noi chiamiamo ora la seconda
[00:33:38] seconda nota, anche lei comincerà ad
[00:33:42] apparire, no, nel nostro nel nostro
[00:33:45] graph view. Una cosa importante da dire
[00:33:47] è che poi queste cose sono interattive,
[00:33:49] quindi se noi premiamo possiamo andare
[00:33:52] dentro alle varie note, ok? Quindi anche
[00:33:55] qui ciao eccetera. Vedete ovviamente che
[00:33:57] qui per il momento sono due note
[00:33:59] indipendenti. Da cosa lo vediamo? Che
[00:34:01] non sono collegate da niente e sono una
[00:34:04] accanto all'altra. Ora che abbiamo
[00:34:05] definito queste cose, possiamo anche
[00:34:07] vedere che se noi le cancelliamo,
[00:34:09] ovviamente verranno cancellate in
[00:34:10] maniera totale sia dal grafico che dalla
[00:34:13] nostra cartella. Vedete? una e due.
[00:34:16] Bene, ora è il momento di cominciare a
[00:34:19] costruire la nostra company Brain.
[00:34:20] Quindi, per farlo faremo la nostra prima
[00:34:23] nota eh quasi completa, ok? Di modo tale
[00:34:27] da cominciare a vedere questo grafico
[00:34:28] che comincerà a formarsi. Per farlo
[00:34:31] chiamiamo in causa il nostro amato
[00:34:33] Notion ed andiamo quindi alla prima
[00:34:36] nota. Allora, la prima nota la
[00:34:39] chiameremo Selfdity
[00:34:41] di Aurora e vedrete poi perché ehm ci
[00:34:45] tengo a chiamarla selfa,
[00:34:49] ok? E il motivo è perché questa parte
[00:34:52] self sarà uno dei ehm diciamo eh blocchi
[00:34:57] che noi utilizzeremo, una delle 11
[00:34:58] cartelle che useremo e vengono fatte per
[00:35:02] identificare un o per raggruppare delle
[00:35:05] identità. Poi ne parleremo, per il
[00:35:06] momento compilatela, ok?
[00:35:09] e quindi metteremo Aurora sistemi Spa è
[00:35:13] un'azienda di eh 340 persone che vada a
[00:35:17] vedere i sistemi. Quindi noi ora
[00:35:18] salviamo e sappiamo che abbiamo fatto la
[00:35:20] nota. Bene, andiamo ora a crearci
[00:35:24] un'altra nota, ok? E quindi cominciamo a
[00:35:26] inserire i nomi delle persone che
[00:35:30] lavorano dentro alla nostra azienda. Ok?
[00:35:33] Poi, premessa, eh vi darò eh dei prompt
[00:35:37] che vi permetteranno di fare questa cosa
[00:35:39] compilata da AI. Ok? Quindi per ora
[00:35:42] soffermiamoci solo a capire il
[00:35:43] funzionamento. E allora quello che
[00:35:45] diciamo è che Elena guida la divisione
[00:35:49] commerciale di ehm della nostra azienda
[00:35:52] che si chiama Aurora. Ora però voglio
[00:35:54] cancellare e voglio farvi, anzi voglio
[00:35:56] farvi vedere una cosa. Vedete che in
[00:35:58] questo caso, ok? Anzi, meglio fare così
[00:36:02] in modo tale che possiate apprezzarlo.
[00:36:04] In questo caso siamo tornati nella
[00:36:07] situazione di prima, ok? Queste due note
[00:36:10] sono sconnesse, però noi vorremmo che
[00:36:12] questa nota ora e questa nota qui
[00:36:15] diventassero connesse in modo tale che
[00:36:17] lei capisse che sono relazionate, ok?
[00:36:21] Perché? Perché questa è la nostra
[00:36:24] azienda, ok? E questa azienda, abbiamo
[00:36:27] detto che si chiama Aurora, mentre
[00:36:32] questa è, diciamo, il responsabile
[00:36:36] commerciale e ovviamente c'è una
[00:36:39] relazione perché il responsabile
[00:36:40] commerciale lavora nell'azienda,
[00:36:42] corretto? Quindi come facciamo a farlo?
[00:36:45] Al posto che scrivere che eh Elena
[00:36:48] Ferrero guida la dimensione commerciale
[00:36:51] di Aurora srl,
[00:36:53] noi o meglio Lei quello che farà è
[00:36:56] mettere queste parentesi quadre che
[00:36:59] permetteranno di riferirsi ad un'altra
[00:37:05] nota. Ok? Quindi in questo caso questo
[00:37:08] che è identità azienda si riferirà
[00:37:11] all'azienda.
[00:37:12] Quindi che cosa vuol dire? Vuol dire che
[00:37:14] abbiamo creato un comportamento
[00:37:17] ehm e abbiamo correlato, scusatemi, le
[00:37:21] due note e lo vediamo da questa lineetta
[00:37:23] qui. Che cosa vuol dire? Vuol dire che
[00:37:26] se io ora questo al posto che chiamarlo
[00:37:28] selfora, lo chiamo self
[00:37:33] info azienda, che magari è più chiaro,
[00:37:37] ok?
[00:37:38] tutto quanto verrà aggiornato in
[00:37:41] automatico,
[00:37:42] ma non solo, abbiamo anche la libertà di
[00:37:47] muovere dentro e fuori a questa
[00:37:50] configurazione
[00:37:52] le note senza che queste vengano diciamo
[00:37:57] in alcun modo ehm cambiate in termini di
[00:38:01] relazione. Quindi ora vediamo che cosa.
[00:38:04] Beh, vediamo che tutto questo è
[00:38:06] navigabile. Quindi se io premo ora self,
[00:38:09] anzi persona è Elena Ferraro e e premo
[00:38:13] self info azienda, posso cominciare a
[00:38:16] viaggiare,
[00:38:17] no, tra una e l'altra. E questo è iper
[00:38:22] importante. Che cosa abbiamo visto?
[00:38:24] Abbiamo visto che qui c abbiamo creato,
[00:38:27] e fatemi cancellare ora la cartella al
[00:38:29] volo, un primo link e questo link in
[00:38:33] questo caso si chiama wiki link. Ok?
[00:38:37] Quindi è un link che va da questa
[00:38:39] direzione a quella. Ora però ovviamente
[00:38:43] vorremmo avere anche un'altra cosa e
[00:38:46] cioè vorremmo avere che qua dentro o
[00:38:49] dentro questa ehm diciamo questa sezione
[00:38:53] venga scritto chi è il nostro
[00:38:55] responsabile commerciale, no? E quindi
[00:38:58] noi qui in questo caso potremmo dire il
[00:39:00] commerciale il il commerciale di
[00:39:01] riferimento è e dopo abbiamo di nuovo le
[00:39:04] nostre parentesi quadre, ok? E mettiamo
[00:39:07] il collegamento e di nuovo, giusto per
[00:39:10] farvelo vedere alla nostra persona.
[00:39:13] Quindi qui avremo la possibilità di
[00:39:15] collegarlo. Che cosa è cambiato in
[00:39:16] termini di grafo? Beh, in termini di
[00:39:18] grafo niente, ma ora per l'AI invece è
[00:39:21] cambiato un sacco perché non abbiamo
[00:39:23] solo un wikilink, abbiamo eh anche un
[00:39:27] back link, quindi una cosa che torna
[00:39:28] indietro e Obsidian se ne occuperà
[00:39:31] tramite le AI in maniera automatica, che
[00:39:34] permette di dire solo che questo è il
[00:39:38] commerciale e poi l'AI sarà in grado di
[00:39:41] entrare nel link e prendere tutto il
[00:39:44] contesto della persona. Quindi
[00:39:46] ipotizziamo che abbia tre mansioni, no?
[00:39:50] E diciamo è che conosce il perché dietro
[00:39:53] il cliente d'acquisto. Ehm è la persona
[00:39:56] che si occupa di vendere, non lo so,
[00:39:58] spazzolini e poi magari mettiamo
[00:40:03] ehm le piace la pizza. Queste sono tutte
[00:40:07] informazioni che un eventuale AI
[00:40:10] potrebbe eh in qualche modo ricavare,
[00:40:13] ora interrogando ehm appunto i questo
[00:40:18] link qui. Ok? E questo perché comincia a
[00:40:20] diventare potente? Beh, perché
[00:40:21] cominciate a capire che quest da qui il
[00:40:24] mondo, quindi il nostro team di
[00:40:26] commerciali e quindi per il team di
[00:40:28] commerciale vai al link team. Il link
[00:40:30] team è collegato a tutti i sotto team.
[00:40:32] ogni persona ha le proprie informazioni,
[00:40:35] cioè vedete quanto questa cosa può
[00:40:36] espandersi anche per processi e via
[00:40:39] dicendo. Come facciamo ora a vedere che
[00:40:41] queste cose siano vere, però allora,
[00:40:44] apriamoci il nostro ehm cloud eh code.
[00:40:49] Utilizziamo anche cowork, così per
[00:40:51] semplicità, insomma, per di interfaccia
[00:40:54] possiamo fare quello che vogliamo, no?
[00:40:55] Quindi entriamo nel nostro cowork work
[00:40:58] in a project, apriremo la nostra Aurora
[00:41:01] cervello, benissimo, e gli chiederemo:
[00:41:05] "Hei, sapresti dirmi ehm chi è il
[00:41:08] responsabile commerciale dell'azienda?"
[00:41:09] Vediamo che cosa sta facendo nel nel
[00:41:12] nostro thought process. Comincia a fare
[00:41:15] i vari comandi, comincia ad entrare
[00:41:17] dentro la nostra azienda, vedete?
[00:41:20] comincia a leggere i vari file markdown
[00:41:23] e dopo arriva alle informazioni di
[00:41:27] Elena, quindi guida la divisione eh sì
[00:41:30] di Elena. Guida la divisione commerciale
[00:41:32] di Aurora. L'azienda A è indicata come
[00:41:35] il commerciale di riferimento è la
[00:41:36] persona che conosce. Perfetto. Ora le
[00:41:38] chiedo, hai anche qualche altra
[00:41:40] informazione di Elen a riguardo? Ora
[00:41:42] quello che farà sarà ovviamente andare
[00:41:44] dentro le nostre note e andare a capire
[00:41:47] che cosa c'è all'interno. Vedete quanto
[00:41:50] potente sia questo tipo di utilizzo,
[00:41:53] perché qui cominciamo ad avere tutto
[00:41:55] collegato in maniera appropriata, no?
[00:41:57] Quindi qui vediamo. Le piace la pizza.
[00:42:00] Bene, ora torniamo nella nostra nota e
[00:42:05] ora ovviamente cancelliamo perché
[00:42:08] vogliamo tenere il tutto nella maniera
[00:42:10] più corretta possibile. Quindi, nel caso
[00:42:11] non ve ne siate accorti, per accedere al
[00:42:13] grafo, ora possiamo rifarci a questo
[00:42:15] tastino che è il nostro grafo, oppure
[00:42:17] premere command P. E se gli mettiamo
[00:42:20] graph view, open graph view, questo è
[00:42:23] quello che noi abbiamo eh ora
[00:42:25] visualizzato. Ora c'è un problema e cioè
[00:42:30] queste note sono leggibili per un umano
[00:42:33] perché sono formati di testo, ma l'AI se
[00:42:37] queste cose cominciano a scalare fa un
[00:42:40] sacco di fatica nell'interpretarle.
[00:42:43] E questo perché? Beh, perché al momento
[00:42:45] immaginiamo di avere ora 1000 note di
[00:42:48] questo tipo. Lei dovrebbe fare uno
[00:42:51] sforzo immane e immaginiamo ovviamente
[00:42:55] di avere ora magari questa frase e la
[00:42:59] ripetiamo ehm adesso all'infinito. Lei
[00:43:03] ogni volta che entra nella nota dovrebbe
[00:43:05] andare a leggersi tutto il contesto e
[00:43:08] ovviamente questo consumerebbe un sacco
[00:43:10] di token e avrebbe problemi di
[00:43:12] allucinazione. porterebbe lei a
[00:43:14] sbagliare. Quindi ora introduciamo il
[00:43:18] secondo, diciamo, blocco importante che
[00:43:21] è come facciamo a rendere le note
[00:43:25] visibili all'AI nella maniera più
[00:43:28] corretta possibile. Ovviamente per
[00:43:30] farlo, se vi ricordate, noi abbiamo
[00:43:33] detto che ehm o o se non lo sapete ho un
[00:43:37] corso di 4 ore di cloud code in
[00:43:39] community e se volete andare da
[00:43:42] principiante a esperto.
[00:43:44] Il l'AI per leggere le varie skill
[00:43:49] comincia con il leggere questa parte qui
[00:43:51] che si chiama front e se e solo se il
[00:43:55] contesto è rilevante allora procede a
[00:43:57] leggere tutto il resto. E quindi questo
[00:43:59] cosa vuol dire? Che per far funzionare
[00:44:01] bene Obsidian dovremmo avere un
[00:44:02] funzionamento del genere, quindi un
[00:44:04] front.
[00:44:05] Ok? Guarda caso, il front è esattamente
[00:44:10] quello di cui andremo a parlare ora. E
[00:44:12] prima che lo incolli, voglio farvi
[00:44:14] vedere che cosa succede quando premiamo
[00:44:15] questi tre tratt. Allora, vedete che
[00:44:17] cominciamo ad avere delle proprietà.
[00:44:19] Quindi, in questo caso, io potrei
[00:44:21] scrivere title e potrei mettermi
[00:44:25] eh identità di Aurora.
[00:44:30] Poi ovviamente questo può essere eh
[00:44:33] cambiato in Ok, questa è una textbox,
[00:44:36] potrei aggiungere
[00:44:38] del dei tags, potrei cambiare delle m
[00:44:44] insomma delle proprietà. Potrei fare un
[00:44:46] sacco di cose. Ok? Quindi, detto che
[00:44:49] questo va a crearmi tutto questo mare di
[00:44:52] proprietà, ora quello che voglio fare è
[00:44:55] incollare quello che vi ho scritto.
[00:44:56] Quindi incolliamo, apriamo e questo è
[00:44:59] esattamente quello che vediamo. Ok,
[00:45:01] quindi ora che cosa abbiamo? Abbiamo che
[00:45:05] questa nota ha un titolo
[00:45:08] che è Identità di Aurora Sistemi, un
[00:45:11] summary che è super importante
[00:45:14] nel momento in cui noi andremo a
[00:45:17] descrivere le nostre note perché sarà
[00:45:19] esattamente la cosa che Lei andrà a
[00:45:21] leggere per capire se questa nota dentro
[00:45:23] la vostra company Brain è rilevante, che
[00:45:25] tipo di informazioni ha, ok? [sbuffare]
[00:45:27] deve essere ovviamente un sunto eh di
[00:45:30] quello che c'è sotto, ma un sunto
[00:45:32] esplicativo. E dopo quello che succederà
[00:45:34] sarà che cominceremo ad avere dei tag.
[00:45:37] Allora, per i tag c'è una regola e cioè
[00:45:40] mettere il primo tag con è una
[00:45:43] convenzione più che una regola e il
[00:45:45] primo tag che rappresenta la cartella in
[00:45:48] cui la eh noi conterremo questa nota.
[00:45:51] Che cosa vuol dire? che io ho messo che
[00:45:53] il questa nota dovrà essere contenuta
[00:45:54] perché ho già deciso e ho già capito
[00:45:56] quale sarà la mia struttura perfetta e
[00:45:58] che è quella che avrete insomma voi e
[00:46:00] potete utilizzarla che tutto questo
[00:46:02] andrà dentro la ehm diciamo cartella
[00:46:06] self. Ok? La seconda è dargli un tag che
[00:46:10] voi capiate eh di modo tale che abbiate
[00:46:14] modo di ehm di vedere insomma queste
[00:46:17] cose, ok? e di e di taggarle come meglio
[00:46:20] preferite. Io ho messo questi type tipo
[00:46:23] identità perché self è un eh identifico
[00:46:26] l'azienda, identifico la persona, quindi
[00:46:28] anche è ehm persona Elena avrà un type
[00:46:33] identità.
[00:46:34] Status ho messo attivo, nel senso attivo
[00:46:37] o non attivo sono per i servizi, magari
[00:46:39] non lo offriamo più, lo offriamo,
[00:46:40] abbiamo smesso, eccetera. e a chi è
[00:46:44] connesso. Eh, questo è connesso alla
[00:46:46] persona. Ora, se vedete nel nostro
[00:46:49] grafo, nulla è cambiato, queste note
[00:46:52] alcun impatto sul nostro eh grafo,
[00:46:55] nemmeno se noi mettessimo persona dentro
[00:46:57] self non cambierebbe esattamente nulla.
[00:46:58] Ok? Però se noi andiamo qui ora noi
[00:47:03] avremmo volendo, la possibilità di
[00:47:05] visualizzare i nostri tag qua dentro,
[00:47:08] vedete?
[00:47:10] E quindi qui vediamo che adesso abbiamo
[00:47:12] che la nostra self info azienda è
[00:47:15] collegata a due tag, ma Elena in questo
[00:47:18] caso non è collegata ad assolutamente
[00:47:20] nulla e questo lo vediamo perché qui
[00:47:22] mancano appunto i nostri collegamenti.
[00:47:25] Allora, se noi invece andassimo a fare
[00:47:27] una roba simile, potremmo cambiare
[00:47:29] persona, Elena, eccetera, ma quello che
[00:47:32] voglio farvi vedere è che ora il
[00:47:34] collegamento tra persona Elena Ferraro
[00:47:37] ed identità e self è avvenuto, no?
[00:47:38] Perché se io vado in questo, ho questo
[00:47:40] collegamento. Ovviamente se io ne stacco
[00:47:42] uno, il grafo mi permette di capire che
[00:47:45] questo appunto non è collegato. Ok?
[00:47:47] Quindi manca questo collegamento.
[00:47:49] Importante dire noi non andremmo poi
[00:47:51] fisicamente a vedere questi
[00:47:52] collegamenti, ma questi collegamenti
[00:47:54] sono super importanti per l'AI perché
[00:47:58] perché immaginatevi come se l'EI potesse
[00:48:02] entrare in un file e poi diramarsi a
[00:48:04] seconda di qual è la il collegamento
[00:48:06] migliore. Ok? Quindi perché le company
[00:48:09] Brain funzionano? Ok, perché esistono
[00:48:13] questi collegamenti. Parleremo dopo di
[00:48:15] come funzionano e qual è la logica
[00:48:17] sottostante, ma questo è il motivo per
[00:48:21] cui una normale nota di testo, ok? eh è
[00:48:26] peggio per l'AI rispetto a un Obsidian,
[00:48:29] perché Obsidian ha la possibilità di
[00:48:31] avere questi collegamenti internota che
[00:48:34] l'EI con questo front e proprietà può
[00:48:37] lavorare e può anche navigare
[00:48:39] liberamente. Allora, è arrivato il
[00:48:41] momento in cui ora vogliamo cominciare a
[00:48:43] costruire la nostra company Brain.
[00:48:44] Abbiamo messo le fondamenta di come
[00:48:46] funziona Obsidian, come scrivere note,
[00:48:48] di modo tale che riusciremo a leggere
[00:48:50] anche cosa succede e capiremo, insomma,
[00:48:53] cosa Leiai farà senza andare alla ceca.
[00:48:56] Eh, quello che ci rimane da fare ora è
[00:48:58] mettere una struttura. Perché vogliamo
[00:49:00] farlo? Perché vogliamo avere prima uno
[00:49:02] scheletro e dopo vogliamo popolarlo. La
[00:49:05] struttura migliore che ho trovato è a 11
[00:49:08] cartelle e vi spiego perché 11 cartelle.
[00:49:11] E quindi prima di farle volevo
[00:49:12] cominciare uno a uno a raccontarvi che
[00:49:14] cosa c'è all'interno, in modo tale che
[00:49:16] voi possiate sapere esattamente dove lei
[00:49:18] metterà i vostri dati. La prima cartella
[00:49:21] è una cartella che io chiamo self, ok?
[00:49:25] Poi saranno tra l'altro autodescritte.
[00:49:28] Eh, qua dentro è vi faccio un paio di
[00:49:30] esempi dove io metto la missione, la
[00:49:35] visione aziendale, dopo possiamo mettere
[00:49:39] che clienti abbiamo,
[00:49:42] vogliamo mettere le nostre offerte, cioè
[00:49:46] la sostanza è ehm anche non lo so,
[00:49:50] obiettivi e tutte cose di questo tipo.
[00:49:53] La sostanza è vogliamo una cartella che
[00:49:56] ci permetta di identificare in maniera
[00:49:58] univoca e descrivere in maniera chiara
[00:50:01] chi siamo, dove vogliamo andare, che
[00:50:03] obiettivi abbiamo e che permette di dare
[00:50:06] alle AI una fotografia, ok? Di noi oggi.
[00:50:10] Poi areas sono le responsabilità che
[00:50:15] abbiamo all'interno della nostra azienda
[00:50:17] o di quello che stiamo facendo, no?
[00:50:18] Questa struttura, come vedrete, è
[00:50:20] generalista, cioè applicabile a ogni
[00:50:22] business. Allora, qui per esempio
[00:50:24] metteremo eh i vari reparti aziendali,
[00:50:29] quindi eh nel caso in cui voi abbiate
[00:50:31] un'azienda, customer service, eh sales,
[00:50:35] eh marketing o cose di questo tipo, nel
[00:50:38] caso in cui voi siate un freelancer vi
[00:50:41] mettete magari reparto, non lo so,
[00:50:43] social media, piattaforme social media,
[00:50:45] quindi YouTube, LinkedIn, cose di questo
[00:50:47] tipo, no? Ehm, poi parte project
[00:50:52] sono invece i lavori che hanno una fine,
[00:50:57] quindi è la definizione di progetto.
[00:51:00] Eh, in azienda questo è una cosa che ha
[00:51:02] un inizio e una fine, no? non è una cosa
[00:51:04] ongoing, quindi magari non so, progetto
[00:51:06] di rinnovamento della parte di marketing
[00:51:09] o rinnoviamo gli script, cose di questo
[00:51:12] tipo. Projects per un freelancer è, non
[00:51:15] lo so, progetti per l'azienda, quindi
[00:51:17] automazioni che stiamo sviluppando anche
[00:51:21] clienti, insomma la parte progettuale,
[00:51:24] ok, in generale e e qui è appunto tutto
[00:51:28] quello che ha un inizio e ha una fine.
[00:51:30] Io, per esempio, la company Brain che è
[00:51:34] appunto che ho creato prima con i 7.000
[00:51:36] documenti, per me questo è un project.
[00:51:40] Ok? Quando invece e perché? perché era
[00:51:44] una demo che ho fatto completamente
[00:51:46] funzionante, production ready, per
[00:51:49] creare un prompto,
[00:51:51] per esempio, in community, mentre la mia
[00:51:54] company Brain, quindi quella che io
[00:51:55] utilizzo, che è la stessa, è
[00:51:56] semplicemente la cartella diversa, è eh
[00:52:00] diciamo è una cosa che è un cappello più
[00:52:03] grande, no? Quello non è un progetto
[00:52:04] perché non è che ha un inizio una fine,
[00:52:06] quella è una cosa che va ongoing. Bene.
[00:52:09] Poi abbiamo inbox [schiarire la voce]
[00:52:11] che chiamo grezza, quindi sources.
[00:52:13] Questi sono qualsiasi appunti voi
[00:52:17] abbiate, le note che mettete all'interno
[00:52:21] o cose di questo tipo, no? Quindi, non
[00:52:23] lo so, avete, che ne so, articoli che
[00:52:26] avete spulciato tramite AI, eccetera.
[00:52:30] concepts sono ehm le informazioni che
[00:52:35] l'AI serve. Quindi se io parlo di per
[00:52:38] esempio ARR, quindi annual recurrent
[00:52:42] revenue, voglio che la che l'AI capisca
[00:52:44] che è il non lo so, per esempio, è
[00:52:48] fatturato annuo della mia azienda.
[00:52:51] Oppure se io parlo di chn, il Chern è
[00:52:55] definito in maniera diversa a seconda
[00:52:57] del business che avete. Potete avere
[00:53:00] chen di clienti, se avete una community
[00:53:03] come la mia oppure un'azienda, potete
[00:53:05] avere ch di persone, avete varie cose,
[00:53:09] no? Quindi qui andrete a definire,
[00:53:10] quindi a dare tutte le definizioni, ok?
[00:53:13] Per capirci, questa è la parte di
[00:53:15] concept, ok? Definizione.
[00:53:19] Perché? Perché così l'AI ogni volta avrà
[00:53:21] il contesto necessario
[00:53:24] per capire che se io gli dico "Ehi, il
[00:53:27] mio ch aziendale o il mio chin
[00:53:29] community, non lo so, su school eh sta
[00:53:33] peggiorando o sta migliorando, cosa
[00:53:35] abbiamo fatto di diverso, lei in
[00:53:38] automatico saprà che la community media
[00:53:41] di school ha un ch del x%, quindi se il
[00:53:46] mio chn peggiora, allora comincerà a
[00:53:48] trovare delle soluzioni. altrimenti
[00:53:50] qualcos'altro. Se io gli dico hoy ho un
[00:53:52] ch però del mio personale lei avrà tutta
[00:53:55] una serie di metriche diverse per fare
[00:53:57] delle valutazioni corrette. Ok? Quindi
[00:53:59] questo è l'importante delle cose di Ch.
[00:54:02] Poi abbiamo docs che sono le e vedetele
[00:54:07] come le nostre SOP aziendali, ok? Quindi
[00:54:11] le nostre procedure interne, come
[00:54:12] facciamo un boarding di personale, come
[00:54:14] facciamo un boarding di cliente, cose di
[00:54:16] questo tipo. Entities sono eh le persone
[00:54:22] che lavorano dentro la nostra azienda.
[00:54:26] Eh possiamo avere poi eh prodotti, i
[00:54:29] nomi, ok? Magari abbiamo fornitori,
[00:54:34] magari abbiamo tool che utilizziamo,
[00:54:38] abbiamo varie cose. Poi abbiamo la parte
[00:54:41] di dati, queste sono tutte formato
[00:54:45] tabella, ok? E questi sono, per esempio,
[00:54:50] KPI, valori, cose, eh, report, insomma,
[00:54:56] questo è il mondo in cui i data vivono.
[00:54:59] Abbiamo poi la parte, fatemi vedere se
[00:55:02] vedete. Ottimo. Allora, avete la parte
[00:55:05] di code. Quindi questi sono
[00:55:07] letteralmente
[00:55:09] le gli script,
[00:55:11] ok? script che noi facciamo e le ongoing
[00:55:18] automation.
[00:55:20] Quindi se facciamo automazioni per noi,
[00:55:24] ok, lei in automatico saprà che quando
[00:55:27] questa va in production da uno passiamo
[00:55:30] all'altro, ok?
[00:55:33] e sarà gestito da AI senza che voi
[00:55:35] abbiate problemi. Eh, la parte di
[00:55:38] outputs, questi sono i deliverable
[00:55:40] finiti, quindi per esempio eh proposte
[00:55:44] che avete fatto commerciali, di modo
[00:55:46] tale che possiate vedere come sono
[00:55:47] andati, come non sono andati e cose di
[00:55:49] questo tipo. Avete i case study, avete
[00:55:54] poi non lo so, eh, magari avete dei
[00:55:56] contratti che avete mandato e quindi
[00:56:00] volete tenerli. La parte di workspace
[00:56:02] invece
[00:56:04] sono le ehm il diario giornaliero, ok?
[00:56:08] Quindi diario di sessioni
[00:56:13] e giornaliero. Questo è quello che di
[00:56:19] nuovo io, per esempio, sto costruendo il
[00:56:21] mio piccolo Jarvis, quindi per me è un
[00:56:23] Hey Clud e lui ha tutta una skill che
[00:56:26] permette di inizializzare una sessione
[00:56:29] dopo un ciao Claud, sessione finita e
[00:56:33] lui chiude, salva e mi aggiorna le varie
[00:56:37] cose, anche le sessioni intermedie. E
[00:56:39] questo è quello che vi permette di dire
[00:56:41] "Ok, ehm a ti ricordi che tre settimane
[00:56:44] fa abbiamo parlato di". E allora lui
[00:56:46] andrà nelle varie sessioni, andrà a
[00:56:48] vedere che cosa è successo. Per farvi
[00:56:51] vedere un esempio pratico di questo, eh,
[00:56:54] di modo tale che vi sia più chiaro,
[00:56:56] fatemi andare nella mia company Brain,
[00:57:00] perché ora ho fatto la migrazione di
[00:57:01] tutto il mio social media manager
[00:57:04] e dovrebbe essere Eccoci qui. E quindi
[00:57:07] voi vedete che adesso è esattamente la
[00:57:10] stessa struttura che vi sto dando, ma
[00:57:12] nel mio workspace il giornale delle
[00:57:16] sessioni sono ieri notte, insomma, ho
[00:57:20] lavorato un pochino e quindi vedete che
[00:57:22] qui ho fatto qu c sessioni e dopo invece
[00:57:26] ho la parte di daily in cui tutto questo
[00:57:29] viene eh consolidato e mi dice che cosa
[00:57:33] ho fatto, quando l'ho fatto, vedete, una
[00:57:35] di mattina, eccetera. eccetera eccetera.
[00:57:38] Rieepigo giornata e quello che ho fatto.
[00:57:40] Ok, questo perché è importante? Perché
[00:57:41] dobbiamo averne due, perché il daily è
[00:57:43] un suo. E quindi Lei andrà a vedere con
[00:57:47] i vari titoletti che cosa ho fatto qua
[00:57:49] dentro, mentre poi nello specifico ogni
[00:57:53] sessione andrà a dettagliare quello che
[00:57:57] è stato fatto e e come. E vedete che qui
[00:57:59] è tutto collegato da AI. Ok? Super super
[00:58:03] importante. Ora voi dovreste riuscire a
[00:58:05] vedere tutto. Sì, perfetto, riuscite a
[00:58:07] vedere tutto. Ehm, ora se io gli dicessi
[00:58:11] e "Hei Claud, ti ho già salutato
[00:58:13] stamattina, siamo già in sessione" e
[00:58:16] allora è una domanda, controllo il daily
[00:58:18] di oggi. Oggi è il 10, quindi ora
[00:58:22] leggerà e dovrebbe rispondermi se tutto
[00:58:24] funziona bene. Sì, confermo, la giornata
[00:58:26] è aperta. Ok. Ehm,
[00:58:29] sto facendo ora una demo, per favore,
[00:58:32] non chiudere ancora la giornata che ho
[00:58:33] del lavoro da fare. Ehm, e puoi
[00:58:37] descrivere brevemente quello che succede
[00:58:39] quando io ti dico fine sessione o quando
[00:58:41] ti dico fine giornata. Ehm, queste
[00:58:44] saranno cose che sto mostrando nel mio
[00:58:46] video YouTube, quindi cerca di essere
[00:58:47] sintetico e non andare nei dettagli
[00:58:49] perché poi avranno il prompto. E questo
[00:58:53] apro e chiudo, funziona super bene se
[00:58:56] avete un buon rag dietro, perché qui può
[00:58:59] andare proprio nei dettagli piccoli
[00:59:01] piccoli piccoli e può trovarvi qualsiasi
[00:59:03] cosa. Certo, niente chiusure. Ecco la
[00:59:06] sintesi. Fine sessione chiude una
[00:59:07] singola conversazione. fine giornata si
[00:59:10] dice una volta sola dall'ultima
[00:59:11] conversazione la chiusura del negozio.
[00:59:13] Recupera le eventuali sessioni rimaste
[00:59:15] orfane. Verifica che il mio Github sia
[00:59:17] pulito, sigilla i daily e fa un sync
[00:59:20] finale. Sync finale vuol dire aggiorna
[00:59:22] tutto, quindi quando avrete il vostro
[00:59:24] notion aggiornerà il notion tutto
[00:59:26] quanto. Ok? Quindi questo è più o meno
[00:59:28] il funzionamento della company Brain.
[00:59:31] Ora torniamo a noi e prima di di mandare
[00:59:34] il prompt voglio descrivervi solo
[00:59:36] brevemente che cosa succede e perché
[00:59:38] Obsidian è importante. Per farlo ehm vi
[00:59:41] vorrei ora descrivere quello che noi
[00:59:43] vedremo. E quando dico vedremo intendo
[00:59:45] che vedremo in una schermata come
[00:59:48] questa, per esempio. Quindi, fatemi
[00:59:50] brevemente andare qui. Allora, avremo
[00:59:53] una serie di cartelle. Le cartelle sono,
[00:59:57] ok, tutta una serie di cose, quindi
[00:59:58] immaginatevi di avere il vostro
[01:00:00] alberello, ok? Che faccia così, che
[01:00:02] faccia così, poi abbiamo un'altra
[01:00:05] cartella e e tutto quest'albero
[01:00:06] continua. Le cartelle creano la
[01:00:09] cosiddetta tassonomia. Che cosa vuol
[01:00:12] dire? Che vuol dire che spiegano
[01:00:16] come deve essere archiviato qualcosa.
[01:00:20] Ok? Quindi questo mi dice come devo
[01:00:24] archiviare
[01:00:26] e vedete che la logica di archiviazione,
[01:00:29] se l'avete colta bene, senò ve la dico,
[01:00:31] è sulla azionabilità quella che io ho
[01:00:35] scelto. Ok? Quindi, quindi questa è la
[01:00:40] mia logica di archiviazione. Potete
[01:00:42] scegliere quella che volete, ma quindi
[01:00:45] quanto più un doc è azionabile, tanto
[01:00:47] più è riorganizzato nello spazio.
[01:00:49] Infatti project oneof quando diventano
[01:00:52] ongoing vanno direttamente dentro code o
[01:00:55] quando hanno finito vanno dentro output
[01:00:57] eccetera eccetera eccetera. Quindi
[01:00:58] output sono cose pronte da usare, code
[01:01:00] pure, ma sono parti di codice e quindi
[01:01:03] vedete che c'è una sua architettura.
[01:01:06] Quindi questa è la mia decisione a
[01:01:08] livello di brain perché perché io sono
[01:01:11] molto ehm eh
[01:01:14] puntato alle azioni, quindi io voglio
[01:01:16] che anche la mia brain abbia un po' la
[01:01:18] mia stessa logica. Map è cose che hanno
[01:01:20] alto arroai, non voglio fuffa. Quindi
[01:01:23] questo è come archiviare. Ora l'altra
[01:01:26] cosa che Obsidian fa, di cui non si
[01:01:29] parla molto è la parte ontologica.
[01:01:32] Ontologica vuol dire come collego le
[01:01:35] informazioni. È un'ontologia applicata
[01:01:37] all'I, ok? È sostanzialmente dare una
[01:01:40] struttura al ragionamento. Che cosa vuol
[01:01:42] dire? Vuol dire che se io ho, in questo
[01:01:44] caso, nella nostra demo, ho Aurora e ho
[01:01:47] Marco, quindi esattamente il eh la cosa
[01:01:51] che vedete voi qui, ok? Ho queste due,
[01:01:54] la parte ontologica mi dice come queste
[01:01:57] due informazioni si connettano, ok? E
[01:02:01] quindi qui è la parte che dirà lavora
[01:02:04] nel commerciale. Ok? Quindi questo è
[01:02:07] come sono collegate. Quindi commerciale
[01:02:10] avrà a sua volta un sacco di
[01:02:11] sfaccettature, no? Quindi avrà
[01:02:14] dipendente,
[01:02:16] avrà eh funzione
[01:02:20] aziendale, avrà eh tenier, quindi gli
[01:02:25] anni in azienda, avrà salario,
[01:02:29] avrà un sacco di sfaccettature questo
[01:02:31] collegamento, no? E se vi ricordate è
[01:02:33] esattamente questa parte qui. Quindi ora
[01:02:37] noi abbiamo tutto quello che ci serve
[01:02:39] per capire che la nostra company Brain
[01:02:42] per fare un riassunto è importante
[01:02:44] perché perché ci permette di creare la
[01:02:49] tassonomia che vogliamo, quindi permette
[01:02:51] di archiviare le cose come vogliamo
[01:02:54] farlo o come il nostro cliente vuole. E
[01:02:56] la tassonomia è molto importante da
[01:02:58] decidere perché vi darà il funzionamento
[01:03:01] di tutta l'azienda. Se volete tenere la
[01:03:04] tassonomia che ho fatto io, l'ho fatta
[01:03:05] apposta perché funzioni in qualsiasi
[01:03:08] business, no? Vedete che è agnostica,
[01:03:11] non ha un funziona solo per, non lo so,
[01:03:13] la clinica o la l'officina, funziona
[01:03:16] pure per me che faccio contenuto, ho la
[01:03:19] mia agenzia e cose di questo tipo, no? E
[01:03:21] poi avete l'ontologia. L'ontologia è la
[01:03:24] logica di collegamento ed è una cosa che
[01:03:27] voi ovviamente se non volete seguire la
[01:03:30] mia logica dovrete farvi, no? Quindi
[01:03:32] dovrete dare ad Obsidian il come
[01:03:34] colleghiamo queste cosine qui. Ok?
[01:03:37] Quindi, detto questo, adesso torniamo a
[01:03:40] bomba dentro la nostra AI e quindi
[01:03:44] adesso io posso chiudere la mia company
[01:03:47] Brain perché partiamo ora da Aurora
[01:03:49] Cervello. Ho cancellato giusto per farvi
[01:03:52] vedere tutto quanto quello che c'era
[01:03:55] dentro al mio ehm Aurora cervello. Ed il
[01:03:59] motivo è perché ora voglio cominciare a
[01:04:03] costruirlo.
[01:04:05] Per farlo, adesso vado nel mio
[01:04:07] bellissimo notion e quindi posso dirgli
[01:04:11] dargli il primo script, il primo prompt,
[01:04:13] perdonatemi. Quindi quello che gli
[01:04:15] faccio è creami nel mio volt alla radice
[01:04:20] queste 11 cartelle vuote, una per
[01:04:23] ciascun lavoro del cervello, self,
[01:04:25] whatever, ehm, non crearne altre, non
[01:04:27] metterci nessun file dentro, solo le
[01:04:30] cartelle.
[01:04:32] Adesso, perché è importante cominciare?
[01:04:35] Perché gli diamo una struttura e io poi
[01:04:38] ho anche creato, vediamo se riesco a
[01:04:40] farvelo vedere, sì, un documento molto
[01:04:42] casuale dove ho le sources, ok? Queste
[01:04:45] sono le cose che alcune le trovate nei
[01:04:47] siti aziendali, no? se le vedete, quindi
[01:04:49] ve lo faccio vedere brevemente. Quindi
[01:04:51] un chi siamo, la nostra missione, cosa
[01:04:54] facciamo, sono tutte organizzate un po'
[01:04:56] in maniera casuale. Poi un organigramma
[01:05:00] di ruoli, persone, cose, poi ho un
[01:05:04] export di CRM con un po' di clienti e
[01:05:08] cose di questo tipo, no? Quindi qui
[01:05:09] vediamo cose puramente generate da AI e
[01:05:12] vediamo che ho, insomma, un sacco di
[01:05:14] dati incasinati. Adesso il motivo per
[01:05:18] cui non posso
[01:05:20] dargli impasto i dati a cazzo così e
[01:05:24] devo dargli prima una struttura è che
[01:05:27] l'AI deve avere prima di digerire tutti
[01:05:31] i vostri dati aziendali deve avere un
[01:05:34] una specie di microguardiano o un
[01:05:37] cervelletto che permetta di farlo. Ed è
[01:05:40] proprio per questo che ora introduciamo
[01:05:42] il concetto e che lo vedrete anche poi
[01:05:45] nel nostro notion di ehm che cos'è un
[01:05:49] canon. Allora, immaginatevi di avere,
[01:05:53] non lo so, un un bacinello d'acqua, ok?
[01:05:59] e l'acqua arriva fino a qui [sbuffare] e
[01:06:01] quindi ehm questo è esattamente quello
[01:06:04] che vogliamo riprodurre, però eh che
[01:06:07] stiamo chiedendo adesso all'AI di
[01:06:08] prendere questa documentazione e di e di
[01:06:11] spezzarla, ok, in 11, per capirci,
[01:06:15] microbacinelle, ok? Ovviamente ogni
[01:06:19] singola di queste bacinelle avrà al suo
[01:06:22] interno dell'acqua, ok? Però è ovvio che
[01:06:26] la somma dell'acqua di tutte le 11
[01:06:28] bacinelle deve fare la bacinella di
[01:06:30] partenza. Che cosa vuol dire in parole
[01:06:33] povere e in termini aziendali? che noi
[01:06:35] adesso stiamo dando un documento e il
[01:06:38] canon non è altro che la nostra Bibbia
[01:06:42] aziendale, che significa che tutti i
[01:06:46] fatti contenuti in questo documento,
[01:06:49] tutti e solo i fatti in questo documento
[01:06:53] devono essere e quindi i fatti che noi
[01:06:57] andiamo a riportare in queste 11
[01:07:00] cartelle in un numero non definito
[01:07:03] ovviamente di documenti. Ok?
[01:07:06] E quello che gli stiamo chiedendo è di
[01:07:09] stare attento a non allucinare o a non
[01:07:11] inventare o a non creare della
[01:07:13] documentazione. Quindi quello che gli
[01:07:16] stiamo dicendo ora e il Canon si ferma
[01:07:19] qui è: "Hei, dimmi tutto quello che vedi
[01:07:22] dentro la documentazione. Mi raccomando,
[01:07:25] una volta che l'hai visto, creami un
[01:07:28] piano di come hai intenzione di dividere
[01:07:31] questa cosa solo dopo che lui avrà fatto
[01:07:34] questo piano." Allora, potremmo
[01:07:37] procedere e introdurremo il secondo
[01:07:39] concetto che è il concetto di note
[01:07:41] atomiche.
[01:07:42] Allora, andiamo qui sotto, copiamo il
[01:07:45] nostro prompt, andiamo nella nostra AI e
[01:07:48] gli diremo adesso questo. Quindi,
[01:07:51] andiamo a vedere che cosa ci dice. Sei
[01:07:53] l'architetto del cervello aziendale di
[01:07:55] Aurora Sistemi Spa, un'azienda fitizia
[01:07:57] che useremo per la demo. Leggi tutto il
[01:07:59] materiale grezo nella cartella sources.
[01:08:03] Eh, ovviamente la cartella sources è qua
[01:08:06] dentro nel mio desktop, quindi dovrò eh
[01:08:09] dirgli ora che è nel desktop. Ok, quindi
[01:08:12] questo manca nel desktop, per me, per
[01:08:16] voi, mettete dove volete. Da lì estrae i
[01:08:18] fatti duri, non so come si dica, quindi
[01:08:20] ho messo così, e scrivili in un unico
[01:08:22] Canon coerente. Il Canon deve coprire
[01:08:25] identità, prodotti, reparti, persone e
[01:08:28] ruoli, clienti KPI di fine 2025. In
[01:08:33] questo caso è per l'anno scorso, poi
[01:08:35] potete anche fare semplicemente KPI e
[01:08:38] basta. Ok, regole. Eh, nessun fatto
[01:08:41] inventato. Se non è nel materiale
[01:08:43] sources non scriverlo. I numeri devono
[01:08:45] quadrare. Scrivi il Canon in un solo
[01:08:48] file di lavoro. Non ancora come note
[01:08:51] finali. Se non riesci a fare qualcosa,
[01:08:53] comunicamelo. Prima di scrivere, dammi
[01:08:55] un piano in cinque righe di cosa hai
[01:08:57] trovato in sources e come pensi di
[01:08:59] strutturare il Canon. Poi aspetta il mio
[01:09:01] oke. Ovviamente potrei mettere in plan
[01:09:04] modi di semplicemente eh velocità. Lo
[01:09:08] utilizzo con bypass permission e dopo vi
[01:09:10] mostro il risultato. Allora, fatemi
[01:09:13] zoomare in modo tale che riusciamo a
[01:09:15] leggerlo in maniera adeguata. E mi dice
[01:09:18] ho letto tutti e noi i file in sources e
[01:09:20] verificato i numeri. Ecco il piano. Ho
[01:09:21] trovato sito. Chi siamo? Peach,
[01:09:25] HR, eccetera eccetera, eccetera. I
[01:09:27] numeri quadrano già. La somma RAR dei
[01:09:29] nove clienti attivi nel CRM è di questo.
[01:09:32] I mobili si sommano esattamente.
[01:09:35] Chern. Perfetto. Struttura del Canon, un
[01:09:38] solo file con sei sezioni nell'ordine
[01:09:41] richiesto. Identità, prodotti, moduli,
[01:09:44] reparti, eccetera eccetera. Dove lo
[01:09:46] scrivo? Workspace Canon nel volt è un
[01:09:50] file, quindi qua dentro è un file di
[01:09:53] lavoro, non una nota iniziale. Cosa
[01:09:55] lascio fuori? Niente di inventato,
[01:09:58] includo l'obiettivo 2026 del board, eh
[01:10:02] come fatto documentato, segnalato come
[01:10:04] obiettivo e KPI. Adesso, prima di
[01:10:07] cominciare a implementare il Canon,
[01:10:10] perché non gli diremo di sì, gli
[01:10:12] introduciamo il concetto di che cos'è
[01:10:14] una nota atomica. E qui cominciamo ad
[01:10:16] entrare nel vivo delle cose. Che cos'è
[01:10:19] una nota atomica? Allora, partiamo da
[01:10:21] chi è questo signore. Facciamo un
[01:10:23] piccolo escursus perché questo è
[01:10:26] sostanzialmente il [risate]
[01:10:29] tirato per i capelli, ma è il
[01:10:31] prefondatore di e delle teorie alla base
[01:10:34] di Obsidian, di Logse e qualche altra
[01:10:37] cosa. Allora, questo signore era un
[01:10:39] sociologo del XXo secolo, tra l'altro è
[01:10:42] diventato iper famoso e aveva questa
[01:10:44] teoria. Ehm, allora, io non pronuncerò
[01:10:49] ora ehm
[01:10:51] questa parola, però è la è il suo
[01:10:55] metodo, è è un approccio bottom up. Ok?
[01:10:58] Questo approccio si basa su il concetto
[01:11:01] di questa nota atomica. E perché è molto
[01:11:04] figo e che cosa ha fatto? Allora, questo
[01:11:08] concetto si basa sul fatto che in ogni
[01:11:11] scheda, ok? Ci deve essere un'idea, ok?
[01:11:16] scritta, parole proprie, deve essere
[01:11:17] autonoma, ma deve esserci un'idea.
[01:11:20] Quindi immaginate che nella scheda 1 ci
[01:11:22] sia la definizione di fiducia e magari
[01:11:25] nella scheda 2 ci sia la definizione di
[01:11:29] soldi. Ok? Quello che questo signore ha
[01:11:32] fatto è stato creare 90.000 schede
[01:11:37] autonome con cui scriveva i libri. Che
[01:11:40] cosa vuol dire? Vuol dire che ogni
[01:11:42] scheda era collegata a livello logico ad
[01:11:46] un'altra, ok? Ovviamente in molteplici
[01:11:49] modi. E [sbuffare] quindi quando lui
[01:11:52] doveva cominciare a scrivere i suoi
[01:11:54] libri non faceva altro che seguire il
[01:11:58] funzionamento o la cosa logica di queste
[01:12:01] schede e cominciava a scrivere il libro.
[01:12:04] Quindi, per esempio, fiducia poteva
[01:12:07] essere collegato, non lo so, a famiglia,
[01:12:11] ok? Oppure anche al denaro, eh, no,
[01:12:16] perché magari avete fiducia
[01:12:18] nell'investitore finanziario oppure può
[01:12:21] essere collegato con amicizia, no? E
[01:12:24] quindi quello che lui faceva era
[01:12:27] rimettere a posto queste schede di modo
[01:12:30] tale che poi il libro venisse già
[01:12:32] precompilato, no? Quindi perché questo
[01:12:35] per un'azienda è importante? Perché noi
[01:12:37] abbiamo questi PDF che sono dei
[01:12:39] mappazzoni infiniti che molte volte
[01:12:41] contengono sempre le stesse cose
[01:12:44] semplicemente riscritte con contesto
[01:12:46] diverso. Cioè per esempio il nostro gol
[01:12:48] del 2025 è andare o 26 o 27 o 28 o 29 è
[01:12:54] andare a 1 milione di MRR e poi il
[01:12:58] nostro ch è il 5% e primo documento è il
[01:13:02] marketing sales speech. Secondo
[01:13:04] documento è un un sales review. Terzo
[01:13:08] documento è la parte di operation che
[01:13:10] magari è incasinata e non riesce a
[01:13:12] tenere il target di inventario per
[01:13:14] arrivarvi al profitto che volete,
[01:13:17] eccetera eccetera. Quindi vedete che
[01:13:19] questo concetto del prendere tutti
[01:13:21] questi libri, spezzarli in note
[01:13:23] indipendenti e poi applicarli, ok? è una
[01:13:27] cosa che ehm per noi ha un valore
[01:13:30] estremo, perché se possiamo avere solo
[01:13:32] una nota con un riferimento di quali
[01:13:34] sono i nostri KPI e poi questa si
[01:13:36] collega a tutto quello che vogliamo,
[01:13:38] beh, capite bene che l'AI a quel punto
[01:13:40] va a nozze perché con i riferimenti
[01:13:41] corretti entriamo e ha sempre il
[01:13:43] contesto corretto. Quindi proprio per
[01:13:45] questo, tornando alla nostra immagin
[01:13:54] è che non vogliamo avere questi malloppi di PDF da 40 pagine tutti insieme, ma
[01:13:56] vogliamo riuscire ad ottenere queste
[01:13:59] strutture perché perché la parola
[01:14:03] corretta è che sono riutilizzabili in
[01:14:07] più contesti. di nuovo, che io faccia
[01:14:10] una review finanziaria nell'azienda o
[01:14:12] che faccia un un'analisi
[01:14:14] dell'inventario, che faccia un meeting
[01:14:18] col team di vendita eccetera, c'è sempre
[01:14:20] necessità di avere gli stessi KPI e goal
[01:14:23] di fondo aziendale, no? Un ultimo
[01:14:24] concetto da introdurre prima di andare
[01:14:27] in notion è gli hubio che cosa vuol
[01:14:31] dire? Abbiamo detto che dobbiamo avere
[01:14:33] delle note atomiche, ora andremo a
[01:14:35] crearle. LI lo farà per noi e lo farà
[01:14:37] per voi con il prompt che vi sto per
[01:14:38] dare. Ma che cosa dobbiamo fare prima?
[01:14:41] Beh, vedete che questi eh queste
[01:14:44] connessioni non sono fatte a caso,
[01:14:46] ricordano molto Obsidian, no? In questa
[01:14:48] piccola immagine. E il motivo è perché
[01:14:50] saranno esattamente le connessioni che
[01:14:52] andremo a vedere in Obsidian ora. Ma
[01:14:54] cosa dobbiamo fare prima? Dobbiamo fare
[01:14:56] gli hub. Ok? Che cosa sono gli H? Se vi
[01:14:59] ricordate, ora abbiamo 11 cartelle, ok?
[01:15:02] Ma non abbiamo ancora detto dentro
[01:15:04] queste 11 cartelle che tago, come
[01:15:06] funzionano e cose di questo tipo.
[01:15:09] Quindi, qual è il rischio? Il rischio è
[01:15:11] che ora, se noi non facessimo il
[01:15:13] passaggio per gli Hub, Obsidian cosa
[01:15:16] farebbe? Comincerebbe a creare un sacco
[01:15:18] di piccole note che abbiamo visto, no?
[01:15:21] Questi pallini e comincerebbe a
[01:15:24] collegarli una con l'altra, no? Il
[01:15:27] problema è che se per caso questo
[01:15:29] pallino viene creato prima del tag o
[01:15:32] prima della nota corrispondente
[01:15:35] eccetera, rimane tra virgolette orfano e
[01:15:39] noi vogliamo ridurre questo il più
[01:15:42] possibile perché questo è un link rotto
[01:15:44] tra virgolette, ok? Quindi, oltre al
[01:15:47] controllo di qualità che faremo dopo,
[01:15:49] ora dobbiamo dire alle AI, ok, prima,
[01:15:52] ora che hai le tue cartelle, le 11,
[01:15:56] assicurati di avere gli hub, quindi
[01:15:59] tutto dettagliato con tags, con links,
[01:16:02] eccetera eccetera eccetera. E solo una
[01:16:04] volta che l'hai fatto, allora procedi a
[01:16:07] spezzare tutte le mie informazioni in
[01:16:09] note atomiche ed inserirle. Quindi,
[01:16:11] andando nel nostro notion, questo è il
[01:16:14] nostro prompt e ora andremo di nuovo nel
[01:16:17] nostro AI e gli diremo questo. E cosa
[01:16:20] gli diciamo? Allora, ottimo, il Canon va
[01:16:23] bene. Ora trasformalo in note atomiche
[01:16:25] dentro le 11 cartelle. Regola per ogni
[01:16:29] nota. Una sola nota, massimo 300 righe,
[01:16:31] abbiamo detto deve essere un riassunto
[01:16:33] della del concetto. Ok? Poi in cima al
[01:16:37] front, title, summary, eccetera, quindi
[01:16:41] la formattazione che abbiamo visto
[01:16:42] all'inizio, perché cominciamo a creare
[01:16:44] l'ontologia e quindi la connessione che
[01:16:47] permetterà alle Yi di funzionare. Poi il
[01:16:49] campo related deve stare su una sola
[01:16:52] riga fisica, benissimo, almeno tre
[01:16:55] wikilink, nome unico, ordine di
[01:16:57] esecuzione, prima gli hub, le note,
[01:17:00] mappa, self self identità aurora, l'abb
[01:17:03] centrale che collega tutti i reparti.
[01:17:05] Qui sarà self eh per voi, self nome
[01:17:08] della vostra azienda e le note dei
[01:17:10] reparti in areas. Poi le note di
[01:17:12] dettaglio, prodotti, clienti Kpi, un un
[01:17:15] week. Parti dagli hub, mostrami self
[01:17:19] identità Aurora prima di proseguire.
[01:17:22] Vedete che io quindi qui ancora non ho
[01:17:25] grosse cose, no? E quindi diciamogli
[01:17:29] bypass permission
[01:17:31] e vediamo che cosa ci produce. Perfetto.
[01:17:35] Allora, mi dice Canon scritto in
[01:17:37] workspace. Canon e quindi lo avremo qui.
[01:17:41] Perfetto. Quindi se volessimo leggerlo,
[01:17:43] questo è il riassunto dei nostri
[01:17:45] documenti. Sette hub creati, uno self
[01:17:49] più 6 reparti. Quindi i reparti sappiamo
[01:17:53] che sono in areas,
[01:17:55] quindi perfetto, sono questi i reparti e
[01:17:58] poi abbiamo self. Eccolo qui.
[01:18:03] Benissimo. E vedete che ha già creato i
[01:18:07] reparti aziendali. Attenzione che ora eh
[01:18:10] solo per headsup ogni tanto, ed è il
[01:18:13] motivo per cui lo facciamo in questa
[01:18:14] maniera, ogni tanto il front e quindi lo
[01:18:18] yaml, che è questa sintassi qui, si
[01:18:20] rompe e quindi lo vedrete rosso. Dovrete
[01:18:22] assicurarvi che in Obsidian lo vediate
[01:18:24] con la tabellina corretta. Se andiamo in
[01:18:26] Obsidian, ora vedremo se si è rotto o
[01:18:29] meno. Vedete innanzitutto
[01:18:31] file eh ehm orfano che dicevamo che è il
[01:18:35] Canon e ce lo aspettiamo perché è un
[01:18:37] documento. Ok. Bene. Le sei aree sono
[01:18:41] tutte connesse e sono connesse a cosa?
[01:18:45] Alla nostra selfa,
[01:18:48] che è il centro, no, di tutto. E se noi
[01:18:51] adesso entriamo qua dentro vediamo che
[01:18:54] Perfetto, abbiamo lo YamL. Eh, fatto.
[01:18:56] Guardate che se ce lo avete rosso vuol
[01:18:59] dire che è rotto e basta che chiediate a
[01:19:02] Cloud "Ehi, sistema il front". Eh, c'è
[01:19:06] qualcosa che non va. Spesso viene perché
[01:19:09] questo viene messo come stringa di testo
[01:19:11] con le virgolette invece che con il
[01:19:14] puntato. Allora, se poi noi tornassimo
[01:19:17] qui cominciamo a vedere che abbiamo i
[01:19:19] nostri backlink. Tutto è navigabile, no?
[01:19:21] Possiamo, tutto è collegato con il self
[01:19:25] identity, possiamo continuare a muoverci
[01:19:28] in and out. E vedete che Obsidian ora
[01:19:30] comincia a fare le connessioni come
[01:19:32] deve, solo perché gli abbiamo dato
[01:19:34] tutto. Se volessimo vedere anche i tags,
[01:19:37] vedete che siamo riusciti a crearci le
[01:19:40] nostre piccole tag per averle tutte
[01:19:44] collegate nella maniera corretta, no?
[01:19:46] Quindi ora cominciamo a vedere che
[01:19:49] questo comincia a prendere un po' di
[01:19:51] forma. Ok? Per le chiccate qui potete
[01:19:54] mettere, non lo so, self. e vedete che
[01:19:57] poi tutto quello che è collegato a self
[01:19:58] si colora e cose di questo tipo. E
[01:20:01] giusto per farvi vedere anche ehm potete
[01:20:05] premere il tasto animate, questo
[01:20:06] comincerà a collegarsi
[01:20:09] e poi avrete il centro della forza, che
[01:20:12] è il il modo in cui, diciamo, gli darete
[01:20:15] la forma della sfera o la sfera che
[01:20:18] meglio vorrete, insomma. Allora,
[01:20:20] torniamo alle cose che contano e non
[01:20:22] fermiamoci alle sciocchezze. Quindi ora
[01:20:24] andiamo nel nostro notion, prendiamo il
[01:20:27] nostro prompt numero 4 e gli diciamo
[01:20:32] "Perfetto, ora fai tu e completa il
[01:20:35] cervello." Ok, niente di pazzesco, lo
[01:20:37] troverete il prompt. Ah, una cosa che ho
[01:20:39] messo che è interessante è ehm per i
[01:20:43] canali, dato che questa è un'azienda eh
[01:20:46] commerciali come LinkedIn Eventi,
[01:20:48] Partner eccetera, li voglio eh se li
[01:20:51] crea come tag, perché più canali ehm o
[01:20:56] un'attività può essere collegata a più
[01:20:58] canali, no? E quindi, eh, dato che
[01:21:01] abbiamo il concetto di nota atomica, ora
[01:21:03] vi è molto più chiaro perché stiamo
[01:21:04] facendo questa cosa, riusciamo a
[01:21:06] ricostruire diversi pezzi se al posto
[01:21:09] che avere che questi canali, diciamo,
[01:21:12] questi LinkedIn, YouTube, quello che
[01:21:14] sia, come cose indipendenti, siano dei
[01:21:17] tag e possiamo quindi aggregare la
[01:21:19] conoscenza nel migliore dei modi. Ora vi
[01:21:24] aspetto che questo si sistemi e dopo vi
[01:21:27] faccio vedere un altro paio di cose
[01:21:29] dentro Obsidian. Ok? Nel mentre che
[01:21:30] continua, volevo solo farvi vedere,
[01:21:32] vedete che ora lentamente stiamo
[01:21:35] spezzando le varie cose, prodotto,
[01:21:38] prodotto, concetto ARR. Quindi ora
[01:21:41] quello che sta succedendo letteralmente
[01:21:43] è il concetto di nota atomica, no?
[01:21:45] Quindi questo stiamo è quello che stiamo
[01:21:47] facendo e stiamo cominciando a
[01:21:48] spezzettare. Vedete che qua si popola un
[01:21:51] po' tutto quanto per arrivare ad avere
[01:21:53] un sistema interconnesso. Ok, quindi qui
[01:21:56] mi dice cervello completato. Abbiamo
[01:21:58] nella parte self che c'è l'identità.
[01:22:01] Ovviamente era solo questo quello che
[01:22:02] c'era dentro alle mie cose e vediamo che
[01:22:04] tutto è collegato a quello, le sei aree,
[01:22:07] i tre concetti e e vediamo ora come si
[01:22:11] correlano. Allora, se noi andiamo
[01:22:13] andassimo in Obsidian, quindi tornassimo
[01:22:15] qui, voglio mostrarvi oltre alla parte
[01:22:18] grafica che quindi vedete che abbiamo la
[01:22:21] sfera che comincia lentamente a a
[01:22:25] crearsi, no? e quindi potremmo andare a
[01:22:27] modificarla, ma la cosa che mi interessa
[01:22:30] fare in questo momento è andare a vedere
[01:22:33] che cosa succede sulla parte di KPI,
[01:22:36] perché voglio farvi vedere una cosa.
[01:22:38] Allora, per farlo andiamo ovviamente
[01:22:39] nella parte data e prenderemo un
[01:22:42] qualsiasi documento.
[01:22:44] Allora, cosa vedete? Che, come vi
[01:22:47] dicevo, ora qui abbiamo che cosa? un KPI
[01:22:52] di ARR totale e come vedete abbiamo
[01:22:56] collegato il concetto ARR, abbiamo
[01:22:59] collegato l'area finance operation,
[01:23:03] abbiamo collegato il tutto alla nostra
[01:23:06] identità e vedete quindi come un dato
[01:23:10] vada a collegarsi poi con un concetto.
[01:23:14] Ok? E proprio per questo vi ho fatto
[01:23:16] l'esempio prima del libro e dello
[01:23:20] spezzare e e del sociologo che ha fatto
[01:23:22] le 90.000 note, no? Perché vedete come
[01:23:25] tutto questo ora diventi un puzzle per
[01:23:27] l'AI e eh quindi se tutto è
[01:23:31] interconnesso, l'EI può lentamente su
[01:23:34] tutti i link andare dentro a tutto e
[01:23:35] vedere tutto. Ok? Quindi, se noi
[01:23:38] vedessimo adesso, vedi il concetto di
[01:23:41] ARR per avere più contesto. Ora
[01:23:43] arriviamo qui. L'ARR è la prima metrica
[01:23:46] eccetera con cui l'area finance
[01:23:48] operation eccetera eccetera. Vedete
[01:23:50] perché e anche in community ho
[01:23:52] raccomandato a tutti e gli sto aiutando
[01:23:54] di farsi una company brain o di
[01:23:55] venderla, quanto questo ehm servizio sia
[01:23:59] potente, no? e e ed è una cosa
[01:24:02] fenomenale per quanto mi riguarda. Ora,
[01:24:05] cosa super importante, eh andiamo a
[01:24:09] vederci una cosa.
[01:24:12] Allora,
[01:24:14] ok, file orfani, togliamo i tags e ve lo
[01:24:17] punto io. Allora, qual è il problema di
[01:24:21] avere un file orfano? Ok? Voi li vedete
[01:24:25] nei graffi di solito e nessuno vi
[01:24:27] racconta che succede. La verità è che
[01:24:29] qua, se non abbiamo almeno una
[01:24:33] connessione a questo file, l'orfano è un
[01:24:36] problema per quanto ci riguarda perché
[01:24:39] non viene letto dall'AI. L'AI
[01:24:41] immaginatela come se viaggiasse solo tra
[01:24:44] quei collegamenti nella nostra company
[01:24:46] Brain. Ok? Quindi noi vogliamo avere
[01:24:50] file orphany. La la risposta è no.
[01:24:53] Vogliamo avere file orfani di a livello
[01:24:57] concettuale, ma non orfani a livello
[01:24:59] grafo, ok? Perché vogliamo comunque che
[01:25:02] lei vada dentro. Per esempio, le note
[01:25:04] che avete preso in un meeting, ok? che
[01:25:07] magari le avete buttate lì a a calcioni
[01:25:11] per capirci. Eh, vogliamo che queste
[01:25:14] siano all'interno, no, del tutto, perché
[01:25:17] perché se per caso diciamo le AI, "Hei,
[01:25:19] vai a vedere che cosa avevamo detto in
[01:25:20] quel meeting perché c'era una roba
[01:25:22] interessante e magari non sono collegate
[01:25:25] a nulla, ok? noi non avremo modo di
[01:25:27] accedervi, quindi dobbiamo instaurare
[01:25:30] ora una specie di ehm diciamo eh
[01:25:35] stratagemma per collegare tutti gli
[01:25:37] orfani. Questo si chiamerà SINEx e
[01:25:42] volevo farvelo vedere ora perché poi lo
[01:25:44] introdurremo magari tra un pochino o gli
[01:25:46] chiederemo tra un pochino di farlo. E
[01:25:49] questo SL slash index non sarà altro che
[01:25:53] un file che sarà dentro tutte le
[01:25:55] cartelle. Quindi in questo caso avremmo,
[01:25:59] lo faccio qua che così lo vedete, la
[01:26:01] nostra cartella data, avremo poi uno
[01:26:04] slindex per il data e poi avremo il
[01:26:08] nostro KPI
[01:26:10] 2025 ARR e poi ripeteremo tutta la cosa.
[01:26:14] Questo perché? Perché nel caso, per
[01:26:16] esempio, del nostro workspace, ok, dove
[01:26:19] non c'è nessuno che va a parlare con il
[01:26:23] nostro Canon e il problema non è quante
[01:26:27] diramazioni, diciamo, abbiamo, ma è
[01:26:29] quanti file riferiscono alla nostra
[01:26:32] nota, vogliamo che il nostro index, ok,
[01:26:36] e la nostra nota siano collegati tra di
[01:26:40] loro, perché questo fa sì che non ci
[01:26:42] siano orfanis collegati e che quindi
[01:26:45] Quindi lei possa entrare e cominciare a
[01:26:47] vedere anche queste note. Ok? Questa è
[01:26:49] una cosa importante perché non tanti ne
[01:26:50] parlano e ed è fondamentale, insomma,
[01:26:53] perché voi riusciate a fare un grafo
[01:26:55] come si deve. Di nuovo, noi non useremo
[01:26:58] il grafico perché il grafo sarà per
[01:27:01] l'AI, ma noi dobbiamo sapere leggere
[01:27:04] cosa va male nel grafico e capire come
[01:27:08] possiamo migliorarlo di modo tale che
[01:27:10] l'AI possa utilizzarlo nel migliore dei
[01:27:12] modi, no? Quindi oltre ai nostri prompt
[01:27:14] abbiamo anche una maniera visiva e il
[01:27:16] toggle, no, trova gli orfani per far sì
[01:27:19] che riusciamo a vederli. Insomma, ora
[01:27:22] cominceremo e lo faremo, però era solo
[01:27:23] una una premessa che volevo farvi.
[01:27:25] Quindi ora andremo nel nostro eh company
[01:27:30] Brain e gli diremo: "Hei, ora ho bisogno
[01:27:35] di un
[01:27:37] ulteriore aggiunta". Allora, analizza
[01:27:40] bene com'è strutturato il progetto, ok?
[01:27:43] analizza tutte le cartelle e le hai
[01:27:46] anche in conversazione, ma guarda bene
[01:27:48] struttura, come hai front, i tags,
[01:27:52] assicurati di avere tutto documentato.
[01:27:55] Ah, una cosa che manca e che rende
[01:27:57] questo progetto ancora non production
[01:27:59] ready e prima ancora di introdurre
[01:28:01] qualsiasi check di qualità è il fatto
[01:28:04] che manca un indice, un undersore index
[01:28:08] che potrei utilizzare per evitare di
[01:28:11] avere note orfane. all'interno del
[01:28:13] progetto. Ti posso chiedere se puoi per
[01:28:15] favore introdurlo eh su ogni cartella o
[01:28:19] dove meglio ritieni opportuno.
[01:28:23] Benissimo,
[01:28:24] in questo caso noi andremo, fatemi
[01:28:27] vedere se l'ha capito bene. Ok,
[01:28:29] perfetto, ha capito esattamente quello
[01:28:30] che volevo fare e ora eh metteremo
[01:28:33] questa piccola chicca, appunto, per
[01:28:35] quello che vi ho appena spiegato. Appena
[01:28:37] finirà vi faccio vedere che cosa è
[01:28:38] cambiato anche a livello di grafo. Molto
[01:28:40] bene, abbiamo 44 file ora MD, zero link
[01:28:45] rotti, abbiamo un index in ogni cartella
[01:28:50] e vediamo ora che abbiamo i vari index,
[01:28:52] no, che fanno riferimento adesso al
[01:28:56] nostro index workspace.
[01:28:59] E come vedete ora abbiamo il
[01:29:00] collegamento a Canon. Quindi questo vuol
[01:29:03] dire che se noi andiamo qui ora il
[01:29:07] nostro Canon non è più una nota orfana e
[01:29:11] quindi abbiamo fatto tutto come si deve
[01:29:16] per assicurarci che ehm il nostro grafo
[01:29:19] sia navigabile dall'AI. Ok? Ok. Allora,
[01:29:24] ora però che cosa succede? e vi faccio
[01:29:27] dei eh parallelismi. Allora, eh anzi
[01:29:30] fatemi andare su Excalidro. Ora noi
[01:29:32] abbiamo la nostra AI, abbiamo cominciato
[01:29:35] a fare il nostro cervello, però abbiamo
[01:29:40] che cosa? Abbiamo per ora fatto una
[01:29:42] pulizia di tutto quello che già c'era
[01:29:45] nel cervello, quindi è una pulizia verso
[01:29:48] l'interno, quindi documenti verso
[01:29:50] l'interno. Non abbiamo mai fatto una
[01:29:53] pulizia verso l'esterno. Che cosa vuol
[01:29:56] dire? Che noi prima o poi avremo un
[01:29:59] nostro collaboratore che comincerà ad
[01:30:01] utilizzare questo sistema e quindi
[01:30:03] questo sistema manderà dentro delle cose
[01:30:05] alla nostra AI, no?
[01:30:07] e non avremmo un metodo per dire le cose
[01:30:10] che gli sta mandando dentro sono eh
[01:30:12] diciamo cose utili o scritte nel modo
[01:30:15] corretto oppure no, o le i si rompe.
[01:30:17] Immaginatevi per avere un paragone, a me
[01:30:20] piacciono molto questi paragoni molto
[01:30:21] semplici, di eh avere il vostro chef,
[01:30:26] ok? stellato e il vostro chef stellato,
[01:30:30] questo è il mio chef, ha un sacco di
[01:30:33] mini collaboratori e questi
[01:30:35] collaboratori saranno i dipendenti o
[01:30:37] chiunque utilizzerà, diciamo, il
[01:30:39] servizio. Ok? E qui c'è il nostro
[01:30:42] ristorante.
[01:30:45] Ok? E qui abbiamo la nostra cucina che è
[01:30:48] dove noi lavoriamo, no? Che cosa ci
[01:30:52] serve? Allora, ci serve uno step
[01:30:55] intermedio perché perché il nostro ehm
[01:30:58] eh piccolo aiutante cuoco produrrà un
[01:31:01] piatto. Lo chef stellato dice sì o no.
[01:31:05] Se sì, allora portalo al ristorante. Se
[01:31:09] no, rifallo e riportamelo fuori. E una
[01:31:13] volta che sarai arrivato al secondo
[01:31:15] giro, allora se quello va bene, ti farò
[01:31:18] metterlo eh piazzarlo ai miei clienti.
[01:31:22] Questo paragone cosa vuol dire? Vuol
[01:31:24] dire che noi avremmo nella nostra
[01:31:27] company Brain serie di piccoli file che
[01:31:30] ogni persona produrrà, ma che se non
[01:31:33] sono formattati nella maniera corretta,
[01:31:36] ok, non li vogliamo dentro la company
[01:31:39] Brain, o meglio, non è che non li
[01:31:42] vogliamo, ma vogliamo che Lei
[01:31:45] riguardi il file e una volta che ha
[01:31:47] guardato il file lo sistemi e solo
[01:31:50] allora me lo rimandi dentro. Ok? Quindi
[01:31:54] questo è il primo step che noi andremo a
[01:31:57] fare, ok? E ce ne sono un po' che
[01:32:00] andremo a fare ora, ma questo è
[01:32:03] sostanzialmente eh quello che faremo si
[01:32:05] chiama introdurre per parole in parole
[01:32:08] povere, ok?
[01:32:10] Un
[01:32:12] controllo
[01:32:14] di qualità.
[01:32:16] Ok?
[01:32:18] Quindi ora andiamo a sistemare questo e
[01:32:21] dopo cominceremo a guardare anche gli
[01:32:23] altri problemi che ci sono e che di cui
[01:32:25] ora appunto non siamo a conoscenza.
[01:32:27] Quindi, come già sappiamo Notion e ora
[01:32:32] abbiamo eccoci qua, il nostro ehm
[01:32:37] il nostro prompt. Allora, ehm, ora gli
[01:32:42] diremo
[01:32:50] questo. Allora, crea un link Python. Ehm, un link,
[01:32:53] uno script. Cosa ho scritto?
[01:32:56] [risate] Python che faccia e da gate di
[01:33:00] qualità sul cervello di Aurora. Passa
[01:33:03] setaccio. Ogni nota delle 11 cartelle.
[01:33:06] Salta solo Sources Workspace. che sono
[01:33:09] materiale grezzo e scratch e controllala
[01:33:13] contro queste sei regole. Formatter
[01:33:15] completo, massimo 300 righe, almeno tre
[01:33:18] Wikilink, sono una cosa che abbiamo
[01:33:19] detto all'inizio, no? Era per tenerla
[01:33:21] compliant, zero link rotti, zero orfani,
[01:33:24] una sola componente connessa. Elenca gli
[01:33:26] errori nota per nota, raggruppati per
[01:33:28] regola. Se è tutto in regola rispondi
[01:33:30] solo ok, zero errori. Per ora non
[01:33:32] correggere niente, dammi solo referto.
[01:33:34] Allora, perché gli dico questo? Perché è
[01:33:36] normale che a volte non passiamo i
[01:33:40] controlli al primo colpo ed è una cosa
[01:33:42] normalissima nel mondo dell'AI, cioè nel
[01:33:44] senso non abbiamo ancora questi,
[01:33:46] nonostante abbiamo appena avuto anche
[01:33:48] rilasci di ipermodelli ehm di ehm avere
[01:33:53] queste cose che facciano tutto one shot
[01:33:55] e ci sono un sacco di piccole accortezze
[01:33:58] che noi dobbiamo conoscere eh per far sì
[01:34:02] che il nostro sistema funzioni. Un
[01:34:03] concetto molto importante che ehm
[01:34:07] ripeto abbastanza in community è nel
[01:34:09] mondo delle AI noi possiamo fare
[01:34:12] outsourcing di competenza perché
[01:34:15] [sbuffare] l'EI può scrivere codice al posto
[01:34:17] nostro, di pensiero perché molto spesso
[01:34:20] l'AI può pensare a [suono gutturale]
[01:34:23] quale sia la migliore architettura, ok?
[01:34:25] al posto nostro, però non possiamo fare
[01:34:28] outsourcing della comprensione e questo
[01:34:31] è la skill, il pensiero critico è
[01:34:34] comprensione di un problema. Ehm, e
[01:34:38] questo è importante perché siamo
[01:34:40] arrivati al punto in cui possiamo
[01:34:43] raccontare un sacco di cose alle AI, ma
[01:34:45] se non capiamo i cosa c'è sotto, sarà
[01:34:49] molto complesso che poi Lei riesca a
[01:34:51] farlo per noi capendolo da sola. Ok?
[01:34:54] Perché ricordatevi sempre che a
[01:34:56] prescindere da quanto bravi diventino i
[01:34:57] modelli, sono sempre allenati sulla
[01:35:00] media dei dati disponibili. Ok? Bene.
[01:35:04] Allora, eh lui intanto sta creando il
[01:35:06] nostro script di Python autonomo.
[01:35:09] Benissimo. E quindi ora è tutto bello
[01:35:12] che pulito, tutto è stato confermato,
[01:35:14] vedo regole precise e vediamo che il
[01:35:17] gate qualità è stato fatto qui.
[01:35:19] Ovviamente è stato fatto fuori perché
[01:35:21] lui è super partes, no? va a controllare
[01:35:23] tutte le cartelle, quindi va bene che
[01:35:25] sia nella cosiddetta root, quindi fuori
[01:35:28] da tutto da tutte quante queste
[01:35:29] cartelle, ma dentro a questa cartella
[01:35:32] principale. Ok? Quindi tutti questi 11
[01:35:35] più questi due sono tutti allo stesso
[01:35:37] livello. Bene, ora abbiamo fatto il gate
[01:35:42] qualità, che cosa ci manca? Allora, a me
[01:35:45] piace molto inserire una seconda cosa
[01:35:47] che è un indice per l'LEM con tanti LM.
[01:35:53] perdonatemi
[01:35:54] un indice per l'LM che è un lls.t txt.
[01:35:59] Allora, lo incollo e ehm poi ve lo
[01:36:04] descrivo. Allora, questo non è una best
[01:36:05] practice, ma è una eh proposta per ora.
[01:36:11] E che cosa ehm e che cosa ehm dice,
[01:36:15] diciamo, questo filino di testo, al
[01:36:18] posto che lasciare a lei hai la l'onere
[01:36:22] di interpretare che cosa c'è dentro al
[01:36:24] suo cervello ogni volta che la
[01:36:25] riapriamo, no? Quindi riguardarsi la
[01:36:27] struttura, il grafo, eccetera. Facciamo
[01:36:30] un piccolo filino in cui, e qui è dove
[01:36:33] alleggeremo efficienteremo un po' il
[01:36:35] consumo token, in cui gli raccontiamo
[01:36:38] tutte le cose che ha al suo interno. Ok?
[01:36:41] Quindi, ehm, è un file derivato che
[01:36:46] riaggiorneremo ogni volta che magari
[01:36:48] aggiungeremo cose o magari faremo una
[01:36:50] modifica alla alla brain eccetera, nella
[01:36:53] quale diremo "Ehi, guarda che tu hai
[01:36:56] esattamente queste cose qui dentro la
[01:36:59] brain e questo è il riassuntino."
[01:37:01] Ovviamente il workflow sarà che voi
[01:37:04] aprite la vostra sessione cloud, spero
[01:37:07] vi piaccia il coso, Cloud andrà a
[01:37:10] leggere questo, capirà cosa c'è nella
[01:37:12] brain e dopo da qui comincerà a fare le
[01:37:14] varie branches e quindi ad entrare poi
[01:37:16] dentro al tutto. Come vedete è un filino
[01:37:20] di testo txt racconta esattamente tutto
[01:37:23] quello che c'è qua dentro. Ok? Quindi mi
[01:37:26] dice, hai eh questo self con un piccolo
[01:37:30] riassuntino di quello che c'è, eh areas
[01:37:33] con i riassuntini di quello che sono,
[01:37:35] projects, eccetera eccetera eccetera.
[01:37:38] Vedete quindi che è letteralmente è un
[01:37:41] indice che io vi consiglio di mettere a
[01:37:43] livello token, a livello di efficienza
[01:37:44] mi ha aiutato un sacco. Non è una best
[01:37:47] practice, è una raccomandazione dello
[01:37:48] zio Jo, vedete voi cosa farne. L'altra
[01:37:51] cosa che mi piace fare molto è e è che,
[01:37:54] per esempio, ai ehm ragazzi e gli
[01:37:57] imprenditori dentro alla community
[01:37:59] chiederò quando farò l'audit del loro eh
[01:38:01] cervello, è di introdurre anche una
[01:38:05] terza cosa che è invece una
[01:38:07] rappresentazione grafica di quello che
[01:38:09] c'è dentro la vostra ehm il vostro
[01:38:11] cervello. Questo è molto utile.
[01:38:14] Allora, io sono una persona molto
[01:38:16] visiva, quindi mi piace vedere le cose
[01:38:18] prima di poter entrare nel nel tutto,
[01:38:22] no? Quindi mi piace vedere cosa c'hai
[01:38:25] messo dentro, in modo tale da poterla
[01:38:27] capire al volo senza diventare impazzito
[01:38:30] e mi piace vedere anche quanti file hai
[01:38:34] dentro, come sono disposti in una
[01:38:36] maniera molto impattante e molto
[01:38:38] immediata, no? Mi piacciono queste cose.
[01:38:40] Trovo che questo sia estremamente utile
[01:38:42] anche quando andate a vendere questa
[01:38:43] tipologia di servizio, eh, perché vi
[01:38:45] permette di riassumere in una maniera
[01:38:48] abbastanza visiva. Poi potete farvi
[01:38:49] tutte le dashboard che volete, potete
[01:38:51] farvi Jarvis, gli fate battere le mani,
[01:38:53] come vedete su Instagram, potete fare
[01:38:55] tutto quello che volete. By the way,
[01:38:57] facilissimo fare quella roba là. Usate
[01:38:59] Deep Gram e utilizzate 11 Labs. Super
[01:39:03] semplice, ma quello che voglio dirvi è
[01:39:06] avete un modo o una dashboard. A me
[01:39:08] piace vederla così semplice in formato
[01:39:10] testo. Sono una persona noiosa, per dire
[01:39:13] qua dentro ci sono queste cose ed è
[01:39:16] esattamente così grossa la tua
[01:39:18] dashboard. Adesso, appena ce lo fa
[01:39:22] vedere, vi mostro il Ah, eccolo qui. Eh,
[01:39:25] showcase.md. vi mostro il risultato di
[01:39:28] questa cosa. Tra l'altro non credo
[01:39:29] neanche. Eccola qui. Perfetto. A me
[01:39:31] piacciono le cose semplici. Vado subito
[01:39:33] al sodo, quindi io va bene non
[01:39:35] dashboard, però è una skill che eh
[01:39:38] questa fatta più per fare conseguenza ai
[01:39:41] ragazzi dentro, però ehm ecco, ve la
[01:39:45] consiglio. Vedete note totali di cui
[01:39:50] note di contenuto di cui dentro
[01:39:52] hubilinks
[01:39:54] totali componente connesse, uno tutto
[01:39:56] collegato e poi qua mi permette di
[01:39:59] andare dentro. Quindi self, quante ne
[01:40:00] avete, cosa avete definito, eh quanti
[01:40:03] hub ci sono? Areas, insomma, mi permette
[01:40:07] di vederle e dopo questa cosa qui, no?
[01:40:10] Molto impattante, molto visiva e ti dice
[01:40:12] "Ok, ti sto gestendo tipo se la
[01:40:13] facessimo nell'altra". ehm mi direbbe
[01:40:17] sto gestendo 20.000 note, una roba
[01:40:20] disumana. Ok, quindi terzo step è
[01:40:24] questo.
[01:40:26] Adesso la parte grafica di Obsidian ve
[01:40:28] l'ho già raccontata e ora introduciamo
[01:40:31] un nuovo problema. Andiamo di nuovo qui
[01:40:33] e ve lo definisco. Ora abbiamo fatto i
[01:40:36] nostri 1000 controlli, no? E abbiamo
[01:40:38] questi script. Ma ora qual è il
[01:40:40] problema? E cominciamo a parlare anche
[01:40:42] un po' di data compliance. Obsidian è
[01:40:47] quello che viene chiamato local first,
[01:40:51] quindi significa che i dati sono dentro
[01:40:54] al vostro computer, ok? Non c'è niente
[01:41:00] eh per il momento eh di contenuto ehm
[01:41:05] come si dice in un cloud online e questo
[01:41:08] ha dei pro e dei contro. Allora,
[01:41:10] innanzitutto ha un pro enorme e cioè
[01:41:14] avete tutto dentro al vostro computer e
[01:41:18] ha un conto enorme che è non avete la
[01:41:21] possibilità se il vostro computer si
[01:41:24] rompe, dato che niente è salvato in
[01:41:25] Obsidian, ma Obsidian è solo un layer
[01:41:27] sopra e perdete la cartella, non avete
[01:41:30] una repository dove metterla, no?
[01:41:32] Allora, qui dobbiamo entrare in due eh
[01:41:36] mondi. Allora, uno è come facciamo a
[01:41:39] trattare i dati sul GDPR. La risposta è:
[01:41:44] dovete, per esempio, quando useremo
[01:41:46] Notion, quando useremo Quadrant, dopo
[01:41:49] andare a guardarvi i DPA e dovrete
[01:41:52] firmare i DPA. Questo è come voi potrete
[01:41:56] garantire la gestione dei dati in
[01:41:58] maniera eh corretta, ovviamente
[01:42:00] rispettando anche quello che poi il DPA
[01:42:02] prevede. Se lo leggete è tutto lì
[01:42:04] dentro, quello è tutto quello che dovete
[01:42:05] sapere. La seconda è come posso avere
[01:42:09] uno storico e quindi qual è il mio
[01:42:12] cervello dietro al mio eh obsidian.
[01:42:16] Allora, per parlare di questo dovremmo
[01:42:18] introdurre uno strumento che faccia
[01:42:21] version control, quindi appunto la
[01:42:24] versione storica. E voi qui avete due
[01:42:27] grosse possibilità. Avete Google Drive,
[01:42:31] ok, super utilizzato, tra l'altro, eh
[01:42:35] avete Gitub, ok? Gitab molto più solido.
[01:42:39] Ho visto aziende che utilizzano anche
[01:42:41] Google Drive senza alcun tipo di
[01:42:42] problema. L'importante è uno strumento
[01:42:44] in un cloud. nella quale più persone
[01:42:47] possano accedervi, che può permettervi
[01:42:51] di capire, ok, è andato male qualcosa,
[01:42:54] come recupero i dati? Oppure se aggiorno
[01:42:56] tutta quella cartella e dopo qualcun
[01:42:59] altro lavora dopo di me, come fa a
[01:43:01] sapere che ho tutti i dati aggiornati?
[01:43:03] Allora, avete quello che vi ho mostrato
[01:43:05] all'inizio, quindi il buongiorno cloud e
[01:43:07] i cloud, fine sessione e poi lì
[01:43:09] integrerete il comando, spingi le cose
[01:43:12] su GitHub o su Google Drive e quando ti
[01:43:14] chiedo buongiorno cloud, riscaricami
[01:43:17] tutto da Google Drive o da GitHub di
[01:43:19] modo tale che io possa ehm avere sempre
[01:43:22] tutto aggiornato, no? Questo lo fate
[01:43:24] semplicemente con una connessione e cose
[01:43:27] di questo tipo. Io ora introdurrò
[01:43:30] velocemente Gitab, ma voglio dirvi
[01:43:32] questo è il primo dei vostri cervelli,
[01:43:34] ok? Quindi quello dove terremo lo
[01:43:37] storico di che cosa c'è. Quindi, detto
[01:43:39] questo, ehm, andiamo al nostro eh
[01:43:43] notion, prendiamo il prompt ed ora lo
[01:43:46] inseriremo qui e vediamo che cosa c'è
[01:43:48] scritto. Trasformo il mio volto Obsidian
[01:43:50] in una repository git. Obiettivo avere
[01:43:53] una cronologia completa delle modifiche
[01:43:55] come una macchina del tempo nel mio
[01:43:56] brain e poi una serie di cose. Ok,
[01:44:00] allora ora dovremmo dargli accesso a
[01:44:03] GitHub. Eh, potremmo farlo con MCP,
[01:44:05] potremmo farlo con token, diamoglielo
[01:44:08] con il token. Ovviamente dovremmo
[01:44:10] metterlo in un DNV file. Adesso lo
[01:44:13] sappiamo tutto. Anzi lo creeremo. DV.
[01:44:18] Qui poi avremo la nostra repository.
[01:44:21] Andremo qua sotto. Andremo in eh
[01:44:26] settings.
[01:44:29] Qua sotto ci saranno i developer
[01:44:34] Avremo il personal access token. Faremo
[01:44:38] fine grind token e generate new token.
[01:44:43] Faremo la verifica della mail. Perfetto.
[01:44:46] Poi metteremo token a second brain
[01:44:59] Tutorial completo su come creare una secondra su YouTube.
[01:45:02] Perfetto,
[01:45:04] gli metteremo public. Ora gli metteremo
[01:45:10] disapply to all current and future.
[01:45:12] Perfetto. Add permission. Perfetto.
[01:45:16] Generate token e gli metteremo dentro al
[01:45:19] dot invv. Quindi che cosa abbiamo fatto
[01:45:22] e perché Gitab? Allora, fatemi spiegare
[01:45:25] al volo eh che cosa ci sarà scritto nel
[01:45:29] promptio che dovrebbe chiarire un sacco
[01:45:32] di cose. Allora, a parte ho fatto un
[01:45:34] corso completo per GitHub per
[01:45:36] principianti che vi spiegherà benissimo
[01:45:38] come utilizzarlo, è nel mio eh canale,
[01:45:40] andatelo pure a vedere, ma immaginiamo
[01:45:43] di avere una nostra linea del tempo, ok?
[01:45:46] e andiamo a vedere che cosa sono i
[01:45:47] comandi. Allora, quando diciamo fare un
[01:45:52] commit,
[01:45:54] ok, noi intendiamo
[01:45:57] vai nella linea del tempo, ok? E fammi
[01:46:00] una fotografia, ok? Quindi il commit,
[01:46:05] ogni volta che lo facciamo stiamo
[01:46:06] chiedendo a GitHub di fare una foto alla
[01:46:10] nostra situazione e metterla in questa
[01:46:14] linea del tempo. Quindi immaginiamo che
[01:46:16] facciamo che ci svegliamo la mattina,
[01:46:19] quindi siamo qui, immaginiamo che
[01:46:21] lavoriamo 2 ore, dopo aver lavorato
[01:46:23] sappiamo che stiamo andando ad una task
[01:46:26] abbastanza critica. Quindi arriviamo qui
[01:46:28] e qua diciamo "Hei GitHub, per favore
[01:46:32] fai un commit e poi io continuo a
[01:46:34] lavorare." Ok? Immaginiamo che tutto
[01:46:37] vada male. Qui posso dire "Ok, torna al
[01:46:41] commit precedente". Ok, quindi è come un
[01:46:45] checkpoint, è una una foto. Bene, ora
[01:46:50] detto questo, introduciamo invece il
[01:46:54] secondo concetto, quindi abbiamo visto
[01:46:57] che cos'è un commit e ehm adesso abbiamo
[01:47:01] un branch l'unica cosa che ci interessa.
[01:47:05] Ok, quindi questo è una branch significa
[01:47:10] faccio lavoro su un ramo separato.
[01:47:14] Quindi ipotizziamo ora sempre nella
[01:47:17] nostra linea del tempo, diciamo, "Ok,
[01:47:19] qui voglio ho il mio sito web, ok, lo
[01:47:22] sto sviluppando e cosa voglio fare?
[01:47:25] Voglio provare a cambiare e sono qui col
[01:47:27] mio sviluppo web, voglio provare a
[01:47:29] cambiare la foto di sfondo, l'animazione
[01:47:32] di sfondo del mio sito web. Allora,
[01:47:34] ovviamente io voglio che il mio sito web
[01:47:36] rimanga funzionante, quindi qui avrò il
[01:47:39] mio piccolo commit e poi comincerò a
[01:47:41] fare una branch. Quindi comincerò a
[01:47:43] lavorare in una cosa che è separata dal
[01:47:45] ramo principale che viene chiamato ramo
[01:47:49] main. Ok? [sbuffare] E qui che cosa
[01:47:52] faremo? Andremo a fare le prove
[01:47:57] per cambiare la nostra foto. Ok?
[01:48:00] Immaginiamo che non funzioni, quello che
[01:48:04] possiamo fare è dire a Gitab, "Hei,
[01:48:12] cancellami questo ramo, non importa, ho sbagliato tutto." E qui sentirete
[01:48:14] branch, sentirete worktree, avrete un
[01:48:17] sacco di di termini tecnici. Quello vuol
[01:48:19] dire semplicemente lavorare in una
[01:48:21] sessione parallela e se facciamo danni
[01:48:24] possiamo appunto rimuovere tutto quanto.
[01:48:27] Vedete che questo è super importante
[01:48:29] perché immaginiamo ora di andare nel
[01:48:31] nostro esempio della company Brain.
[01:48:33] Ipotizziamo di e e sono tutte cose che
[01:48:36] potete fare in automatico con AI,
[01:48:37] comunque eh non dovete diventare massimi
[01:48:38] esperti, ma saperla usare è importante.
[01:48:43] Quindi ipotizziamo di sapere che
[01:48:44] dobbiamo andare a fare una modifica
[01:48:46] importante alla company Brain
[01:48:48] o aggiungere cose che modificherebbero
[01:48:51] drasticamente la struttura perché non lo
[01:48:54] so, 1000 cambiamenti. potremmo dire,
[01:48:56] "Ehi, eh, fammi una foto dove siamo
[01:48:59] oggi, poi cominciami a lavorare in
[01:49:02] parallelo, poi se solo se vedo che la
[01:49:05] mia company brain quando ho fatto tutto
[01:49:07] risponde, allora diciamo fai il merge e
[01:49:12] quindi
[01:49:14] fai sì che questo ramo verde diventi
[01:49:17] tutt'uno col blu e quindi salva i
[01:49:18] cambiamenti. Se invece questo ramo non
[01:49:21] avviene e perché magari il la qualità è
[01:49:25] scarsa, evita di farlo e semplicemente
[01:49:27] cancellalo. Ok? Questo è solo per darvi
[01:49:30] un concetto iniziale perché ora,
[01:49:32] appunto, Gitub sta andando per dirvi eh
[01:49:35] l'importante il motore di queste cose.
[01:49:38] Se volete un corso dettagliato, fatto
[01:49:39] con calma, in community, faccio questo,
[01:49:42] faccio rag, facciamo tutto quello della
[01:49:44] company Brain. Qui è giusto per darvi
[01:49:46] due concetti. Se avete passione, volete
[01:49:47] andarvelo anche a studiare in autonomia.
[01:49:50] Quello che stiamo facendo adesso è
[01:49:52] abbiamo fatto la company Brain, abbiamo
[01:49:54] dato all'AI la capacità di entrare nei
[01:49:57] vari file e di navigarli. Ora dobbiamo
[01:50:00] dare all'AI la capacità di ricordarsi i
[01:50:03] checkpoint precedenti nel caso in cui
[01:50:06] noi perdiamo il computer, il computer si
[01:50:08] rompa e cose di questo tipo. Allo stesso
[01:50:11] modo vogliamo che se qualcuno aggiorna
[01:50:14] del nostro team la company Brain,
[01:50:15] vogliamo avere un unico posto in cui
[01:50:17] questo folder è aggiornato e abbiamo
[01:50:20] un'unica verità, un'unica source of
[01:50:22] truth. Ok? E quindi andiamo lì dentro,
[01:50:25] prendiamo quello e lo portiamo poi nel
[01:50:27] nostro computer e diciamo "Ok, ho il
[01:50:29] file aggiornato". Ok? Quindi tutti
[01:50:31] questi paroloni per dire che voi usiate
[01:50:33] Github o che voi utilizziate Google
[01:50:35] Drive, la realtà è che vabbè, Gitub è
[01:50:38] più tecnico, scala meglio, però cambia
[01:50:40] relativamente poco e ehm avete comunque
[01:50:44] un posto in cui potete fare la
[01:50:46] cosiddetta version control, quindi avere
[01:50:48] il vostro archivio con dentro tutte le
[01:50:51] varie ehm
[01:50:54] versioni del vostro progetto e poi
[01:50:57] potrete tornare a quella precedente
[01:50:58] quando volete. Una volta che è stato
[01:51:00] fatto, allora voi potrete vedere che
[01:51:03] nelle vostre repository avrete, eccoci
[01:51:05] qui, il nostro Aurora Cervello. E il
[01:51:08] nostro Aurora Cervello, se noi entriamo,
[01:51:10] ha esattamente tutto quello che abbiamo
[01:51:13] già ehm utilizzato e di cui abbiamo
[01:51:16] parlato. C'è stato fatto un commit,
[01:51:18] quindi una fotografia poco fa ed eccoci
[01:51:22] qua. Bootstrap del cervello a 11
[01:51:25] cartelle. potrei entrare e potrei vedere
[01:51:27] esattamente quello che è stato cambiato.
[01:51:30] Vedete quindi che qui posso tornare a
[01:51:31] versioni precedenti e fare tutto quello
[01:51:33] che abbiamo che abbiamo detto di nuovo.
[01:51:35] Se volete un corso per capire meglio
[01:51:38] GitHub è nel mio canale YouTube,
[01:51:39] andatevelo a vedere. Bene, quindi prima
[01:51:41] di parlare ora di layer visivo, eh
[01:51:44] quindi Notion, quindi HTML, volete farla
[01:51:48] vedere in azienda e o giocarci,
[01:51:50] introduciamo una piccola demo perché
[01:51:53] voglio farvi come vedere come funziona,
[01:51:55] insomma, il sistema già ora senza Rag e
[01:51:57] quanto è accurato. Allora, [sbuffare]
[01:52:00] ovviamente abbiamo la nostra cosa,
[01:52:02] andiamo qui, abbiamo il nostro piccolo
[01:52:04] prompt e e interroghiamo il cervello e
[01:52:07] gli diciamo "Rispondi alla mia domanda
[01:52:09] usando solo il contenuto di queste note.
[01:52:13] Cita sempre il nome de file da cui
[01:52:14] prendere informazione. Se la risposta
[01:52:15] non è presente nelle note, scrivi
[01:52:16] esattamente, non presente nel cervello."
[01:52:19] Qual è l'ayerar di Aurora e come è
[01:52:21] cambiato negli ultimi 3 anni? Vediamo
[01:52:23] che tipologia di informazioni ci
[01:52:25] restituisce. A fine 2025 leerard di
[01:52:27] Aurora è di 3.8 milioni in crescita di
[01:52:31] rispetto ai del eh di inizio 2025 e e mi
[01:52:36] va riferimento, come è cambiato negli
[01:52:38] ultimi anni, non è presente nel
[01:52:41] cervello. Poi ci dice che cosa le note
[01:52:43] riportano e il piano di assunzioni che
[01:52:45] abbiamo in previsione. Ok. Il secondo
[01:52:48] prompt che voglio farvi vedere è questo.
[01:52:52] Eccoci qui, dove rispondiamo ad ehm una
[01:52:56] domanda, ok? In una maniera un po' più
[01:52:59] complessa. Quindi, sostanzialmente,
[01:53:00] quello che andiamo a fare è e ora fatemi
[01:53:02] pulire la conversazione, è andare dentro
[01:53:06] a ehm i vari i vari nodi. Quindi,
[01:53:10] rispondi utilizzando solo le note del
[01:53:12] cervello di Aurora. Ovviamente, come
[01:53:14] sempre, domanda: quali clienti hanno
[01:53:17] attivato sia Aurora Cloud e eh chi li
[01:53:20] segue nel Customer Success? Vedete ora e
[01:53:24] poi parleremo di architettura. Eh già
[01:53:27] che tipo di domande abbastanza complesse
[01:53:29] possiamo fare con un tutorial che adesso
[01:53:32] non so quanto sia durato, ma eh con
[01:53:35] quello che sembra semplice, ora vedete
[01:53:37] qua, vedrete, anzi perché vi faccio un
[01:53:39] un numero indicativo, già questa
[01:53:41] architettura quanta roba può fare ed è
[01:53:43] un'architettura che può essere già
[01:53:44] scalata in ehm in una maniera abbastanza
[01:53:49] complessa, no? E quindi ora ci dice, "Ho
[01:53:51] cercato in tutte le note del cervello di
[01:53:53] Aurora i prodotti citati nella domanda.
[01:53:55] I prodotti registrati nel cervello sono
[01:53:56] tre: Access Score e Energy. Né Aurora
[01:53:59] Cloud né Aurora Care compaiono in alcuna
[01:54:01] nota non presente nel cervello. Ora io
[01:54:03] potrei dirgli e se io ti facessi la
[01:54:06] domanda invece sui prodotti di cui ehm
[01:54:09] siamo proprietari, quindi Access, Core
[01:54:11] ed Energy e e se io poi ora vado qui,
[01:54:15] vedete che io riesco effettivamente a
[01:54:16] verificare che non abbiamo alcuna
[01:54:20] tipologia di prodotto come quelli che
[01:54:22] gli abbiamo dato. E guardate che senza
[01:54:25] un'architettura corretta tutto questo si
[01:54:27] sponna proprio, diventa un umaciello.
[01:54:31] Tra l'altro è una roba che ho sempre
[01:54:33] fatto anche da piccolo questo accento.
[01:54:35] Non ho idea da dove venga, non so
[01:54:36] neanche se sia offensivo. Ahm Allora,
[01:54:40] nel caso lo sia, scusatemi. Allora,
[01:54:42] applicando [risate]
[01:54:43] la stessa regola stretta, un cliente
[01:54:47] conta solo se hai davvero tutti i
[01:54:48] prodotti citati. Ecco cosa dicono le
[01:54:51] note. Core Access Energy, eccetera,
[01:54:55] clienti con tutti e tre. Nessuno.
[01:54:57] L'unico l'unico modulo comune a tutti è
[01:54:59] Core Access, compare solo in Banca
[01:55:02] Adriatica, eccetera eccetera eccetera.
[01:55:05] Almeno due dei tre. Allora, tutti e tre
[01:55:07] i clienti si qualificano nel customer
[01:55:09] success. Da chiara, da Chiara e
[01:55:11] sostanzialmente chiamiamo
[01:55:14] e c'è un modo di identificare eh quale
[01:55:18] degli impiegati porta il maggior ARR.
[01:55:21] Quindi vedete quanto possiamo entrare
[01:55:23] dentro al grafo e perché perché avremmo
[01:55:25] sicuramente che queste persone saranno
[01:55:28] collegate con i prodotti prodotti
[01:55:31] saranno collegate con altre, diciamo,
[01:55:34] nodi all'interno della nostra brain che
[01:55:36] eventualmente andranno a connettersi con
[01:55:38] KPI e quindi ora sappiamo Eccoci qui.
[01:55:42] Perfetto. Sì, ma solo in modo parziale
[01:55:44] perché il cervello documenta le IRAR di
[01:55:46] tre clienti su nove. Per i sei i cannon
[01:55:49] non sono nelle note. Dice che la somma
[01:55:52] delle nove è metodo, l'unico impiegato
[01:55:54] esplicitamente eh a clienti con AR noto
[01:55:57] è Chiara Fontana e quindi ora sappiamo
[01:55:59] anche perché lei era l'unico impiegato
[01:56:01] che ci interessava. Molto bene.
[01:56:05] Ah, vedete? Perfetto. Ora un'altra cosa
[01:56:09] che vorrei farvi vedere è eh il livello
[01:56:13] di comprensione che può avere una brain.
[01:56:16] Ehi, guardando al mio database in una
[01:56:19] tabella abbastanza schematica, riesci a
[01:56:22] dirmi quali sono delle informazioni
[01:56:25] mancanti per riuscire a fargli delle
[01:56:28] analisi complete? Ti faccio un esempio.
[01:56:30] Ti ho chiesto in una conversazione
[01:56:31] precedente
[01:56:33] ehm chi era il top employee e tu
[01:56:36] giustamente mi hai giustificato che non
[01:56:38] era possibile trovarlo, o meglio che era
[01:56:39] solo Chiara perché solo i suoi dati
[01:56:41] erano all'interno. Riesci a trovarmi
[01:56:43] tutte le migliorie che io posso fare al
[01:56:47] mio database e o dati mancanti che ti
[01:56:50] potrebbero servire per riuscire a darmi
[01:56:53] una ehm immagine della mia azienda il
[01:56:56] più completo possibile. Perfetto. Per
[01:56:58] dirti cosa manca, devo capire cosa c'è.
[01:57:00] Vedete ora che questo signore va a
[01:57:02] aprirsi il database e quindi entra
[01:57:06] dentro, andrà a vedere tutto quello che
[01:57:08] c'è,
[01:57:11] leggerà tutte le entità. Quindi vedete
[01:57:14] quanto è importante e ora andrà dentro
[01:57:18] alle varie casistiche, vedete? Quindi ai
[01:57:19] KPI, ARR e comincerà a guardarli. Dopo
[01:57:24] abbiamo visto sempre qua dentro che
[01:57:26] cominciava a fare il reparto finance
[01:57:28] ands e insomma vedete voi poi quanta ehm
[01:57:32] quanto spessorio di pensiero può avere
[01:57:34] un sistema che apparentemente è molto
[01:57:36] semplice. E perfetto. E qui ora vi fa
[01:57:38] vedere che cosa serve per ovviamente
[01:57:42] demo che abbiamo fatto. Quindi dice
[01:57:45] benissimo che cosa fa Aurora oggi, ma
[01:57:47] manca meglio dove sta andando. una
[01:57:50] metrica per ogni unità, i costi, il
[01:57:54] tempo, cosa puoi già fare, le colonne
[01:57:57] mancanti e quindi qui comincia a darvi
[01:57:59] anche degli insight su eh che cosa
[01:58:03] dovreste aggiungere perché lei possa
[01:58:05] cominciare questa AI a analizzare meglio
[01:58:08] i vostri dati e a darvi anche degli
[01:58:11] insight per la vostra azienda maggiori,
[01:58:13] quindi per esempio KCK TV e tutte le le
[01:58:16] metriche e via dicendo. Quindi vedete
[01:58:19] quanto potente diventano questi
[01:58:21] strumenti nel momento in cui cominciamo
[01:58:23] ad utilizzarli nella maniera corretta
[01:58:26] con il contesto corretto. Ora, prima di
[01:58:30] muoverci ulteriormente, ehm, volevo
[01:58:33] farvi una mini tabellina che voleva
[01:58:36] essere indicativa di, ehm, come dovrebbe
[01:58:41] funzionare. Sono numeri indicativi, eh,
[01:58:43] non prendeteli come solo questo o non
[01:58:47] c'è nient'altro, ma dovrebbe darvi un
[01:58:49] 8020 per capire che tipologia di company
[01:58:52] brain dovete fare con che tipologia di
[01:58:53] architettura sulla base del numero di
[01:58:55] note che andremmo a stabilire. Quindi
[01:58:58] questo lo chiamiamo numero di note e
[01:59:01] questa la chiamiamo invece ehm non lo
[01:59:05] so, architettura
[01:59:08] e ehm e e strategia. Ok, fate vois,
[01:59:12] quello che volete. [sbuffare] Allora,
[01:59:16] la il numero di note
[01:59:19] e facciamo così. Allora, [sbuffare] il
[01:59:22] numero di note è meno di 500 tra le 5 e
[01:59:27] le eh 2500 note tra le 2500 e le m
[01:59:36] 20.000 note e 20.000
[01:59:39] note plus. Ok, queste due architetture
[01:59:43] sono abbastanza simili, ok? Quindi una e
[01:59:47] due. E quindi ve le riassumo con qui
[01:59:51] faremo le nostre mappe di contenuto.
[01:59:56] Eh, contenuto, quindi i nostri hubo
[02:00:00] quello che abbiamo discusso. Più quello
[02:00:02] che vi consiglierei io è di avere il ehm
[02:00:07] lls.txt.
[02:00:10] Ok? Qui quando parliamo tra i 2500 note
[02:00:13] e le 20.000 note. Cominciate ad avere
[02:00:16] gli eh beddings
[02:00:25] eh rag e invece qui ovviamente 20000 note plus avete una pipeline
[02:00:29] Rag
[02:00:31] completa. Ok? Questo perché? Perché ehm
[02:00:36] quando cominciate ad andare su
[02:00:39] dimensioni massive di eh company Brain,
[02:00:43] dovete fare quello che ho fatto io
[02:00:44] all'inizio. Motivo per cui vi dicevo è
[02:00:47] un corso a s stante, è estremamente
[02:00:49] difficile fare rag, vi richiede un sacco
[02:00:51] di conoscenze che non non ho spiegato
[02:00:54] qui, cos'è un embedding, come si fa il
[02:00:56] chunking e tutta quella cosa lì, ma ehm
[02:00:59] per fare questa tipologia qua cominciano
[02:01:01] a servirvi appunto i rag che, se vi
[02:01:03] ricordate, voglio solo farvi questo
[02:01:05] parallelismo, avevamo prima cartelle,
[02:01:08] avevamo la prima cartella che era il
[02:01:11] cosiddetto eh daily logs e qui avevamo
[02:01:15] invece le cosiddette sessions. Ok? E
[02:01:19] queste erano delle cose, diciamo, più
[02:01:23] Vediamo se riuscite a vederlo. Perfetto.
[02:01:25] Sì, erano delle cose un po' più,
[02:01:28] diciamo, granulari che poi venivano
[02:01:31] aggregate dal daily. Il motivo del rag è
[02:01:34] perché e giusto per dirvela in maniera
[02:01:36] semplificata, ora lei capisce bene
[02:01:38] andando dentro ai vari link, ok, di
[02:01:42] obsidian cosa succede leggendo il front
[02:01:44] eccetera. Ma ad un certo punto, per
[02:01:46] efficientare la ricerca, dobbiamo fare
[02:01:49] la cosiddetta ricerca semantica. Che
[02:01:51] cosa significa? Che eh ad un certo punto
[02:01:54] tutte le parole devono essere
[02:01:56] trasformate in vettori e quindi alla
[02:01:58] fine andiamo a vedere quando due vettori
[02:02:02] sono simili. E giusto per farvi vedere
[02:02:05] eh tutta questa parte del motivo per cui
[02:02:06] non la spiego, sono delle lezioni
[02:02:08] dedicate dove ho fatto semplicemente
[02:02:10] vedere come ci si comporta. Qui ho usato
[02:02:13] un eh embedding projector che è con
[02:02:16] tensor flow che è esattamente questo
[02:02:18] dove potete vedere che qui se io cerco,
[02:02:21] non lo so, king e quindi il re, vedete
[02:02:26] che io ho che dal centro, quindi ops,
[02:02:29] scusatemi, dal centro e quindi da qui
[02:02:32] che ora segnerò, io avrò che Kings e
[02:02:36] King sono vettori simili nella stessa
[02:02:39] direzione nello spazio tridimensionale.
[02:02:41] Quindi ora non voglio fare un corso
[02:02:42] tecnico perché non è lo scopo, neanche
[02:02:44] in community abbiamo corsi tecnici, ma
[02:02:46] ho messo le fondamenta perché voi
[02:02:48] possiate capire meglio queste
[02:02:50] infrastrutture e motivo per cui oggi non
[02:02:52] andremo nel dettaglio del Rug, ve lo
[02:02:54] spiegherò ad alto livello, ma perché c'è
[02:02:56] tutto uno spessore tecnico dietro che
[02:02:58] bisogna insomma apprezzare se volete
[02:03:00] applicarla in maniera massiva e quindi
[02:03:03] in maniera scalabile in un'azienda.
[02:03:05] Ecco, però, ecco, giusto per capirci il
[02:03:07] motivo per cui quando le note scalano
[02:03:10] ehm lei, diciamo, con un rag è meglio, è
[02:03:13] perché al posto che andare dentro e
[02:03:16] farsi tutti i 1000, diciamo, eh rami e
[02:03:20] sprecare token, l'AI andrà direttamente
[02:03:22] a vedere le cose che in un database
[02:03:25] vettoriale sono più o meno orientate
[02:03:27] nella stessa direzione. dopo avere
[02:03:29] spezzato la domanda, quindi magari dove
[02:03:32] è eh o quanto è l'ARR di Aurora nel
[02:03:37] 2026, magari ha una direzione così e
[02:03:39] quindi andremo a cercare tutti i vettori
[02:03:41] che sono più o meno nella stessa
[02:03:42] direzione perché saranno quelli che
[02:03:44] hanno più probabilità di avere la
[02:03:45] risposta corretta o meglio che avranno
[02:03:47] risposte correlate e quindi poi l'AI
[02:03:49] andrà a a trovare solo questi. capite
[02:03:51] bene che questo è molto meglio ed è
[02:03:54] estremamente difficile ed è dove poi,
[02:03:56] tra l'altro, le aziende pagano molto
[02:03:58] bene ehm quando riuscite a fargli questo
[02:04:00] setup, insomma, e se siete in community
[02:04:02] avete il prompt sotto e poi avremo un
[02:04:04] modulo dedicato, insomma. Per
[02:04:06] concludere,
[02:04:08] database che consiglio sono, se volete
[02:04:12] fare integrazioni di tipo rag, potete
[02:04:15] usare Superabase e quindi il classico
[02:04:18] che vedete all'interno, insomma, dei eh
[02:04:21] dei video, soprattutto quando c'erano le
[02:04:22] integrazioni, oppure potete usare un
[02:04:25] database come quadrant, hanno alcune
[02:04:28] differenze. Supase vi permette di fare
[02:04:30] version control e quindi di avere,
[02:04:33] scusate, un uno storico della modifica
[02:04:36] dei dati. Quadrant è un database rag
[02:04:39] specializzato, appunto, nella vector DB
[02:04:44] retrieval, quindi diciamo è un tool
[02:04:47] specializzato. Avete Pinecon,
[02:04:51] è un altro esempio, Wiviate, mi pare.
[02:04:55] Sì. Quindi, insomma, avete un sacco di
[02:04:58] soluzioni. Ognuna dovrà essere calata al
[02:05:01] contesto corretto, però questo è come e
[02:05:05] diciamo aumentate la potenza della
[02:05:08] vostra company Brain, perché
[02:05:10] ricordiamoci,
[02:05:12] Obsidian è il nostro layer 1, adattiamo
[02:05:16] le AI, abbiamo costruito la nostra Volt.
[02:05:19] Se l'avete fatta con questo, siete
[02:05:20] sicuri che avete un'architettura che
[02:05:21] funzioni e sapete che può essere
[02:05:24] scalabile fino a un certo punto. Poi
[02:05:26] dopo quello sappiamo che l'evoluzione
[02:05:28] successiva è un raggiamo andare in
[02:05:30] contesti più grandi e potenti. Abbiamo
[02:05:32] messo quindi poi il nostro brain che è
[02:05:35] il nostro cloud code che permette, no,
[02:05:37] di viaggiare e vedere tutto e abbiamo
[02:05:39] messo il nostro eh diciamo i nostri
[02:05:42] controlli qualità e abbiamo messo anche
[02:05:45] il nostro layer di version control che è
[02:05:48] il nostro gitable, il nostro Google
[02:05:50] Drive. Che cosa manca? Beh, manca un
[02:05:54] layer visivo di interazione perché, come
[02:05:56] abbiamo detto, questo è un layer che
[02:05:58] viene utilizzato prevalentemente da AI.
[02:06:00] Quindi per farlo che cosa facciamo?
[02:06:03] Possiamo fare o cruscotti locali, quindi
[02:06:05] con un HTML locale, lo vedete in un
[02:06:07] sacco di video YouTube, oppure possiamo
[02:06:10] utilizzare Notion. Adesso vi farò vedere
[02:06:12] entrambe le integrazioni, però
[02:06:13] sostanzialmente questo è il concetto. Ci
[02:06:16] serve semplicemente una schermata
[02:06:18] frontale con la quale premere i bottoni.
[02:06:20] Quindi questo è il le cose che vedete su
[02:06:22] Instagram di Jarvis, per esempio, e
[02:06:25] invece Notion è quella che utilizzano i
[02:06:27] team quando devono andare a collaborare.
[02:06:29] Quindi adesso facciamo un prompt super
[02:06:32] semplice e lo incolleremo qua dentro.
[02:06:34] gli diremo genere, un croscotl scarico
[02:06:37] statico dei dati del canon, gli
[02:06:39] indicatori dell'ultimo mese, grafici,
[02:06:41] l'andamento, la classifica, tutto in un
[02:06:43] solo file, HTML che apre con un doppio
[02:06:45] click online e senza account. Ovviamente
[02:06:48] eh potete anche generare, se utilizzate
[02:06:51] Cowork, potete utilizzare un live
[02:06:54] artifact, avete veramente la possibilità
[02:06:57] di utilizzare qualsiasi layer visivo
[02:06:59] vogliate. Voglio solo farvene vedere due
[02:07:02] perché, insomma, è abbastanza ehm
[02:07:05] conveniente vederli in modo tale che
[02:07:07] possiamo dire di avere fatto un sistema
[02:07:09] completo e abbiamo messo insieme tutti i
[02:07:11] vari pezzettini. Perfetto. Quindi il
[02:07:13] primo è questo output di cruscotto
[02:07:15] Aurora HTML che può rappresentare la
[02:07:18] nostra company Brain. Possiamo farlo
[02:07:20] interattivo, possiamo farlo con le
[02:07:23] nostre, non lo so, guidelines aziendali.
[02:07:26] Potete farlo con quello che volete. Non
[02:07:28] credo che avere un un cruscotto figo ora
[02:07:32] da parte mia sia esattamente quello eh
[02:07:34] per cui avete cliccato sul video, quindi
[02:07:36] lo eviteremo. Eh però [sbuffare] insomma
[02:07:38] avete capito. Questo è un primo layer
[02:07:40] visivo. Il secondo layer visivo è
[02:07:44] utilizzarlo tramite Notion. Adesso
[02:07:47] connetterò al volo questo con eh cloud
[02:07:49] code. Andremo qua dentro, gli diremo ehm
[02:07:54] vediamo se riusciamo a partire da
[02:07:55] conversazione. Ok, facciamo MCP ad,
[02:08:00] vediamo se riusciamo a fare qualcosa e
[02:08:03] se è già connesso, soprattutto perché
[02:08:05] potremmo anche avere il comando/mcp.
[02:08:09] Ok. File modified. Done. Added the
[02:08:11] notion htpcp server. Ok. E prossimo
[02:08:15] authenticate, quindi MCP.
[02:08:19] Qui avremo il nostro bellissimo MCP
[02:08:23] Notion. Sembra già connesso.
[02:08:26] Ok. E probabilmente l'avevo da una
[02:08:28] sessione precedente a questo punto. Eh,
[02:08:31] vediamo.
[02:08:32] Sei connesso con Notion? Nel caso in cui
[02:08:34] voi non lo siate, comunque, eh solo una
[02:08:37] cosa, una volta che avete fatto enter,
[02:08:39] dovete solo riavviare il workspace e poi
[02:08:42] potete ehm connettervi da qui. Eh sì,
[02:08:45] controllo subito. E adesso perfetto, la
[02:08:48] conduzione funziona. per favore,
[02:08:51] costruiscimi su Notion un cruscotto di
[02:08:54] KPI per la mia azienda Aurora con tutto
[02:08:56] quello che hai e se riesci fammi anche
[02:08:59] un dettaglio di clienti, revenue e cose
[02:09:03] di questo tipo. Chiamalo ehm cervello
[02:09:08] pino, di modo tale che non si confonda
[02:09:10] con quello che già c'era dentro. Adesso
[02:09:12] aspettiamo e vediamo esattamente che
[02:09:14] cosa succede. Perfetto. Quindi
[02:09:16] integrazione Notion fatta. App Notion,
[02:09:18] lo chiameremo cervello pino. Abbiamo il
[02:09:21] nostro ARR, abbiamo il nostro revenue,
[02:09:25] eh, perfetto, clienti e cose di questo
[02:09:28] tipo, no? Potremmo fare questo, potremmo
[02:09:30] fare una cosa di questo tipo, potremmo,
[02:09:34] una volta che abbiamo fatto una
[02:09:36] visualizzazione di questo tipo, dire
[02:09:38] alle Ai: "Hei, per favore, ora crea una
[02:09:41] connessione con Notion ed Obsidian, di
[02:09:44] modo tale che una volta che io modifichi
[02:09:46] questo campo si rifletta anche in
[02:09:48] Obsidian. Ovviamente l'AI se ne occuperà
[02:09:52] in maniera autonoma e quindi questo,
[02:09:54] diciamo, è la connessione al nostro
[02:09:57] layer visivo. Adesso abbiamo un'ultima
[02:10:00] cosa da affrontare e cioè in questo
[02:10:04] momento noi abbiamo quella che viene
[02:10:06] definita memoria statica, che significa
[02:10:09] memoria ehm statica nei file. Ok? Quindi
[02:10:14] è quasi sintetica, no? un qualcosa che
[02:10:16] creiamo, mettiamo dentro, però poi non
[02:10:19] si aggiorna. Quindi il nostro problema è
[02:10:21] che non abbiamo ancora un modo di dire
[02:10:23] allei "Ehi, ascolta, ma a marzo avevamo
[02:10:26] parlato di questo argomento? Ti ricordi
[02:10:30] cos'era? Cosa avevamo deciso?" No, tutta
[02:10:32] questa architettura, no, eh molto viva
[02:10:36] che ci permette di avere enormi ritorni,
[02:10:38] soprattutto quando si tratta di
[02:10:40] discutere informazioni interessanti
[02:10:41] all'interno di, non lo so, meeting,
[02:10:44] clienti,
[02:10:45] ricordarsi che cosa abbiamo detto, un
[02:10:47] prezzo a un fornitore o contratti,
[02:10:50] eccetera. Quindi dobbiamo creare ora
[02:10:52] l'ultima cosa che voglio farvi, di modo
[02:10:55] tale che questo sia il vostro sistema
[02:10:56] end to end che è questa memoria viva.
[02:10:59] Come facciamo?
[02:11:01] notion abbiamo il nostro piccolo prompt.
[02:11:05] Allora, e poi vi spiego come funziona.
[02:11:07] Allora, questo prompt funziona di modo
[02:11:10] tale che si costruiscano tre skill. Per
[02:11:13] mostrarvele vado al volo qui. E che
[02:11:16] skill abbiamo? Abbiamo innanzitutto il
[02:11:19] inizio
[02:11:21] eh giornata, ok?
[02:11:25] Eh, slash inizio sessione. La giornata
[02:11:29] inizia sempre con una sessione e
[02:11:31] viceversa. Che cosa possiamo fare? Beh,
[02:11:34] noi possiamo interagire più volte con
[02:11:36] più conversazioni con un AI, no? Quindi,
[02:11:38] che cosa vogliamo? Vogliamo una skill
[02:11:41] che alla fine della sessione, ok, si
[02:11:45] ricordi tutto. Ok, quindi per ricordarsi
[02:11:48] tutto vuol dire che faccia eh le note,
[02:11:51] che scriva i meeting, che magari
[02:11:54] riassuma il o che faccia un summary di
[02:11:58] quello che abbiamo discusso e cose di
[02:11:59] questo tipo. E ovviamente all'interno
[02:12:01] della stessa giornata, quindi oggi è il
[02:12:04] 10 del 6, abbiamo eh nota 1,
[02:12:07] conversazione 2, 3 4 5.
[02:12:11] Qui invece abbiamo una fine giornata. E
[02:12:15] allora che cosa vogliamo fare con il
[02:12:17] fine giornata?
[02:12:19] Vogliamo avere il riassunto di tutte le
[02:12:23] sessioni
[02:12:25] più
[02:12:27] quindi sessioni più eh pending topics,
[02:12:32] quindi i topics che dobbiamo fare
[02:12:34] domani,
[02:12:38] i next step che abbiamo discusso magari
[02:12:40] con il nostro team. Ok?
[02:12:43] Quindi abbiamo queste tre cosine
[02:12:47] e ehm ovviamente per farlo dobbiamo
[02:12:50] ingerire tutto questo. Tutto questo
[02:12:52] perché è utile? Torniamo a noi. Se io vi
[02:12:55] dico che la mia richiesta, tipo "Ehi,
[02:12:59] che cosa abbiamo discusso a marzo con il
[02:13:01] cliente tal dei tali? È un vettore così.
[02:13:04] Se io riesco a avere un vettore
[02:13:07] giornata, ok, che è marzo e quindi
[02:13:12] magari saranno tutti i vettori in questa
[02:13:14] direzione, ok?
[02:13:17] E poi ho che il tizio tal dei tali nel
[02:13:21] vettore giornata è questo. sono riuscito
[02:13:24] a farmi, eccolo qui, un vettore simile e
[02:13:28] quindi poi l'AI andrà direttamente
[02:13:30] dentro al vettore, vedrà che il vettore
[02:13:33] è simile, poi andrà a spezzettarlo e
[02:13:36] allora Lei andrà a colpo diretto e dirà
[02:13:38] "Ah, ok, qui avevamo quattro sessioni e
[02:13:42] quindi la sessione tua è esattamente
[02:13:44] questa e quello che hai detto al tizio è
[02:13:47] esattamente quello che c'è qua dentro,
[02:13:50] motivo per cui le sessioni sono super
[02:13:53] granul ulari e le vogliamo tenere tutte,
[02:13:55] mentre le giornate sono dei riassunti
[02:13:57] solo perché dobbiamo creare vettori
[02:13:59] simili. Quindi, come lo facciamo?
[02:14:02] nostro super prompt che abbiamo già
[02:14:04] probabilmente copiato, inserito qua
[02:14:06] dentro e gli diciamo contesto memoria
[02:14:07] viva. Il cervello ha due strati, memoria
[02:14:10] statica, memoria dinamica, memoria di
[02:14:12] lavoro. Ogni ogni sessione e giornata
[02:14:14] lasciano ehm una nota, si aggancia
[02:14:18] sempre alle entità statiche con i
[02:14:19] Wikilink, magari una nota diario sciolta
[02:14:23] nel vuoto, eccetera. Prima di scrivere
[02:14:25] leggi l'indice. Quindi vedete che vi ho
[02:14:27] fatto proprio tutta l'infrastruttura
[02:14:29] endto, avete qualcosa di completamente
[02:14:30] funzionante alla fine di questo. Ehm,
[02:14:33] com'è fatta? Dove andranno le entità,
[02:14:35] che API, progetti, se non ne esistono,
[02:14:38] che cosa costruire? una skill chiamata
[02:14:41] journal con tre comandi: buongiorno,
[02:14:44] inizio sessione, leggi, dammi un
[02:14:46] briefing di cinque righe, non scrivere
[02:14:47] niente al cervello, solo il briefing,
[02:14:50] chiudi sessione e poi fine giornata, il
[02:14:53] riassunto della giornata. template,
[02:14:56] regole che a me piacciono per trovare
[02:14:58] per aiutare le Yi a trovare le cose.
[02:15:00] Glielo mandiamo e ora vi faccio vedere
[02:15:04] appunto live questa cosa come come
[02:15:07] funziona, in modo tale che ehm voi
[02:15:11] possiate anche vedere il funzionamento
[02:15:13] della vostra company Brain che abbiamo
[02:15:15] oggi creato in questo in questo
[02:15:17] tutorial. Perfetto. Ora eh mi dirà che
[02:15:20] l'ha costruita. Come la invoco.
[02:15:23] Ovviamente non so se notate il piccolo
[02:15:25] passive aggressive, tipo muoviti, se
[02:15:28] riesci in parallelo, [risate] scrivi
[02:15:30] semplicemente "Buongiorno, la skill
[02:15:33] journal, dove sono finite? Come
[02:15:35] funzionano?" E quindi ora vedremo che
[02:15:38] nella parte workspace avremo il nostro
[02:15:40] journal daily e session. Buongiorno
[02:15:43] Clod, adesso vediamo che ha chiamato la
[02:15:45] skill journal. ha retto il nostro Brain
[02:15:48] index, ha trovato la latest session.
[02:15:50] Vedete quanto importanti sono tutte le
[02:15:52] cose che abbiamo fatto. Perfetto, quindi
[02:15:55] è solo l'ince del cervello. Dove siamo?
[02:15:57] Il cervello sistema è ancora popolato.
[02:15:58] Vedo che hai aperto output cruscotto. Da
[02:16:01] cosa vuoi cominciare?
[02:16:03] Ehm,
[02:16:05] voglio solo vedere se eh riesci a
[02:16:09] salvare una semplice conversazione,
[02:16:11] quindi solo questa nel
[02:16:14] mio workspace. Il motivo è che sto
[02:16:17] provando la mia skill buongiorno e Cloud
[02:16:20] e buonasera Cloud, insomma per chiudere
[02:16:22] la sessione. Funziona? Chiudo quindi
[02:16:24] sessione. Hai fatto il briefing di
[02:16:26] buongiorno sul cervello di orora ai
[02:16:27] sistemi. Volevo solo trestare la skill.
[02:16:30] Nessun lavoro reale sulle entità
[02:16:32] mancanti. Per agganciare la nota a
[02:16:33] un'entità reale, eh serve almeno un
[02:16:36] wikilink come riferimento, visto che è
[02:16:38] l'unico attivo nel briefing. Ti torna?
[02:16:41] Sì, certamente.
[02:16:43] Ehm.
[02:16:45] Perfetto. E ora diremo:
[02:16:49] "Hei Cloud, grazie per oggi, finisco la
[02:16:52] giornata qui e non appena lui avrà fatto
[02:16:56] tutti i suoi controlli, possiamo
[02:16:58] mandargli invio. Intanto qua vediamo che
[02:17:01] la nostra sessione è stata registrata,
[02:17:03] no? La nostra skill è stata salvata.
[02:17:05] Front Matter valido. Adesso vedremo che
[02:17:07] l'ha fatto. Quindi ha salvato tutto
[02:17:10] secondo le nostre best practices. Quindi
[02:17:12] guardate eh quello che vi dicevo con
[02:17:15] tutti i i la parte tecnica è un po'
[02:17:17] noiosa forse che abbiamo fatto, ma
[02:17:19] guardate che solido che è il sistema.
[02:17:21] Voi letteralmente non avete fatto una
[02:17:22] demo, avete fatto un sistema production
[02:17:24] ready da oggi e quindi ora mi dice
[02:17:28] "Grazie a te Jo, attivo a fine giornata,
[02:17:30] fai pure."
[02:17:37] Quindi ora ci assicuriamo che appaia nel daily, quindi qui dovrebbe cominciare ad
[02:17:39] apparire. Tra l'altro template, abbiamo
[02:17:41] i template di sessione. Vedete, ormai
[02:17:45] con questo piccolo, Adesso non so quanto
[02:17:47] durerà, forse è durato troppo rispetto a
[02:17:49] quello che volevo, ma abbiamo costruito
[02:17:51] un sistema fighissimo, avete una company
[02:17:53] Brain che funziona bene. Ehm, son
[02:17:56] contento. Benissimo, eccolo qua, daily
[02:17:59] fatto, deciso, aperto, sessioni e ci
[02:18:02] siamo. Bene, signori, quindi direi che
[02:18:07] abbiamo fatto il nostro tutorial sulla
[02:18:10] company Brain. Sono felicissimo. Grazie
[02:18:12] mille per essere arrivati fino alla
[02:18:14] fine. Spero il tutorial vi sia stato
[02:18:16] utile. Se vi fa piacere imparare molto
[02:18:19] di più su come farlo in maniera anche
[02:18:21] più massiva e come far scalare la vostra
[02:18:24] company Brain per la vostra azienda,
[02:18:26] sentitevi pure liberi di premere il
[02:18:27] primo link qua sotto. E anche se volete
[02:18:29] vendere questa tipologia di servizi da
[02:18:31] aziende è la mia community e dentro
[02:18:34] abbiamo moduli su moduli e live
[02:18:36] interattive con una community di ormai
[02:18:38] 90 imprenditori e che stanno applicando
[02:18:40] appunto AI nel loro business. Detto
[02:18:42] questo, se vi è piaciuto like per favore
[02:18:45] fatemi sapere se ne volete altri e
[02:18:48] ovviamente grazie ancora per aver
[02:18:49] seguito il tutorial.

