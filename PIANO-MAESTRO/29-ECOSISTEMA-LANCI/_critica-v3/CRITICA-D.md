# CRITICA-D — dossier 07, 08, 10

## 1. I 50 AGENTI REGGONO?

**Il totale torna, i sottototali no.** Il censimento di 08 (righe 118-134) somma correttamente a 50 (1+3+4+5+3+6+4+3+4+3+4+4+2+4=50). Ma la tabella "sei livelli" di 01 (righe 17-27) dichiara L3=11 capi reparto, L4=30 operativi, L5="13 gate + 4 sentinelle". Ricostruendo gli stessi livelli dal censimento di 08: i reparti con un `conductor` nominato sono **10**, non 11 (Qualità e Memoria non ne hanno — 01 righe 131-132 e 146-160 lo dichiarano esplicitamente per Memoria); gli agenti operativi puri sono **29**, non 30. Il totale combinato (1+10+29+10=50) torna comunque, ma le due cifre intermedie di 01 §1.1 sono sbagliate di un'unità ciascuna rispetto al proprio censimento in 08 — due documenti dello stesso giro di revisione, stessa data (2026-09-05), non riconciliati fra loro.

**Il numero dei gate è sbagliato, e nasconde un buco vero.** 01 riga 26 e 10 riga 51 dichiarano "13 gate bloccanti". Contando i gate nominati esplicitamente in 07+01 (GATE-STR-1, GATE-INT-1, GATE-PRD-1/2/3, GATE-OFF-1, GATE-CPY-1, GATE-FNL-1, GATE-EDT-1, GATE-TSR-1/2/3, GATE-REG-1, GATE-MEM-1) si arriva a **14**. Peggio: GATE-TSR-3 (07 riga 103, criterio "il consuntivo esiste e i totali coincidono con la Tesoreria... il lancio non passa ad appreso") e GATE-MEM-1 (01 riga 303, "CHIUSO → APPRESO ... GATE-MEM-1") rivendicano **la stessa transizione** con due criteri diversi. La macchina a stati di 01 §4 (righe 256-307) — l'unico meccanismo che "esegue" davvero i gate, per dichiarazione dello stesso piano (01 riga 33: "i gate... sono dentro lancio avanza") — non menziona mai GATE-TSR-3. O il gate è scritto in 07 e mai cablato (quindi non blocca mai nulla), o la transizione CHIUSO→APPRESO ha due controllori senza un ordine fra loro. Va risolto prima di scrivere `scripts/gate.py`.

**Il file 08 non sa nemmeno il proprio numero.** Il file si chiama `08-AGENTI-SKILL-COMANDI.md` ma il suo H1 (riga 8) recita "# 11 — AGENTI, SKILL E COMANDI". È esattamente il difetto ("tre numeri diversi in tre pagine") che il documento vanta di aver risolto altrove per le skill (righe 255-256: "Undici skill, undici comandi... adesso è un numero solo").

**Candidati alla fusione/soppressione — funzioni Python travestite da agente:**
- `lan-tsr-conductor` (07 righe 87-95; formule A.5, righe 120-131): le fasi T1/T2/T3/T6 sono somma di voci, confronto con un tetto, arrotondamento, divisione — aritmetica pura, specificata da formule esatte nello stesso documento. Non serve un modello linguistico per sommare un budget. Unica eccezione plausibile: la narrazione di T6 ("dove la previsione ha sbagliato") può giustificare un passaggio LLM leggero DOPO che uno script ha fatto i calcoli.
- `lan-tsr-sentinella` (07 riga 92, T5: "ricalcola scarto e costo di acquisizione... automatico"): la tabella stessa dice "automatico". Se è automatico, è un cron/script, non un agente da invocare.
- `lan-reg-calendarista` (07 riga 273: "il calendario si genera, non si scrive"): aritmetica sulle date con margini dichiarati. Zero giudizio richiesto.
- `lan-reg-tracciatore`, per la parte di soglia (07 §C.5, righe 334-342): ogni riga è "se X < soglia allora azione Y" — una tabella di lookup, non un ragionamento. Solo la formulazione in linguaggio naturale dell'azione potrebbe giustificare un LLM, non la decisione.
- L'intera famiglia `lan-qlt-gate` (generico, fonti, copy, costi — 08 riga 131): ammissione dello stesso documento, 08 riga 296: "Contano, confrontano, aprono indirizzi: non ragionano." Anche la "verifica a campione" (07 righe 194-196) — aprire una pagina e cercarci dentro una frase citata — è un fetch + substring match, non un compito per un modello.
- Le 6 entità "sentinella" (Editoriale, 01 riga 128; Tesoro, 01 riga 130; le 4 trasversali, 01 riga 26) sono per definizione di ruolo (08 riga 106: "sola lettura... non agisce: segnala") guardiani di soglia. Il piano ha già il modello giusto per farle collassare in una sola cosa: `lan-qlt-gate` è descritto (08 righe 149-154) come UN motore generico che "esegue un criterio scritto in un file" per 13 (o 14) gate diversi. La stessa architettura — un motore + N file di soglia — elimina la necessità di 6 "agenti" sentinella distinti. Il piano applica il principio in un punto e lo dimentica nell'altro.

Stima: applicando queste fusioni, almeno **8-10 dei 50** sono candidati sicuri a diventare funzioni Python dentro `scripts/`, non agenti invocabili — quasi un reparto intero di lavoro "agentizzato" senza bisogno di un modello.

**Il contratto d'uscita non è verificato da nessuno.** Il principio 2 (08 riga 88: "Ingresso e uscita tipizzati, o non esiste") e lo scheletro del corpo (08 riga 184: "Contratto d'uscita: cosa restituisci, con quale schema") lo impongono in prosa. Ma i quattro controlli di `registro.py` (08 righe 227-232: coppia specifica/agente, frontmatter valido, strumenti coerenti col ruolo, reparto abilitato) **non aprono mai il corpo dell'agente** per controllare che la sezione 3 sia compilata con uno schema vero. Un agente con frontmatter perfetto e sezione 3 vuota passa la verifica ufficiale lo stesso — il buco che il principio 2 dice di voler chiudere.

**Il campo `tools` è coerente per Gate/Sentinella, falso per l'Archivista.** La tabella dei ruoli (08 righe 99-109) assegna all'Archivista "lettura e scrittura **limitata alla propria cartella di memoria**" (riga 105), presentandolo come vincolo "imposto dagli strumenti" (riga 47). Verificato: il campo `tools` di Claude Code limita le CLASSI di strumento concesse (Read/Write/Edit/Grep/...), non i PERCORSI — "Write" concede scrittura ovunque il processo possa scrivere, non solo dentro `memoria/<reparto>/`. Confermato nel repository: 18 agenti reali usano già `tools:` (verificato via `grep -rl "^tools:" .claude/agents/` → 18 file, lo stesso numero dichiarato a riga 41), ma nessuno di essi dimostra uno scoping di percorso, perché il campo non lo supporta. Per Gate/Sentinella (dove basta togliere la scrittura del tutto) il vincolo è davvero meccanico; per l'Archivista, "limitata alla propria cartella" resta prosa, a meno di aggiungere un hook `PreToolUse` che verifichi il percorso di scrittura — mai menzionato nel piano.

## 2. IL COSTO NON C'È?

**No, manca del tutto, e il documento lo dichiara onestamente.** 08 §10 (righe 283-303) dice esplicitamente: "Non è una misura. Nessun lancio è mai stato eseguito" (riga 285). Dà solo classi qualitative (dominante/medio/trascurabile, righe 288-292) e la regola generale del modello per ruolo (08 riga 162: haiku per i controlli, sonnet per le missioni, opus per chi progetta) — ma **nessun conteggio di chiamate**, nemmeno una stima per il solo lancio pilota. È coerente col principio 5 di 08 ("quando non sa, si ferma e lo dichiara"), ma resta un buco reale per chi deve decidere se 139-187 ore-uomo di costruzione (09 riga 192) si ripagano.

**Stima d'ordine di grandezza, dichiarata tale.** Con ~0,08-0,11 $ di sola tassa fissa per invocazione (esclusi i token), un lancio reale attiva almeno:
- **gate**: 14-15 controlli nominali, alcuni rieseguiti dopo un rigetto — il piano stesso dichiara 12 giorni di margine su 38 come "somma dei rifacimenti che i gate del piano stesso prevedono come normali" (07 righe 269-271), quindi 2-4 ri-esecuzioni sono già previste → 15-20 invocazioni;
- **sentinelle**: T5 "automatico" per ~38 giorni (07 riga 92) più il tracciatore giornaliero da T-0 a T+5 e oltre (07 riga 264) → 40-50 invocazioni;
- **copy**: "11 pezzi × 1-2 giri su modello pesante" (08 riga 290, la voce dichiarata "dominante") → 11-22 invocazioni, ma su Sonnet/Opus con prompt lunghi: qui il costo reale è dominato dai token, non dalla tassa fissa — ogni giro può costare 1-3 $, non 0,10 $;
- **ricerca, funnel, editoriale, offerta, strategia**: altre 20-40 invocazioni cumulate stimabili dalle fasi elencate in 07 §B.2 e nel censimento di 08.

Totale plausibile per il **primo lancio** (in modalità pilota, che salta buona parte di ricerca/certificazione): dell'ordine di **150-250 invocazioni-agente**. Anche al solo tasso fisso (0,08-0,11 $) sono già 12-27 $, ma la voce dichiarata "dominante" (i testi, su modello pesante) porta il conto realistico verso **50-150 $ per lancio**, prima di contare i lanci successivi dove S2/S3/S4 aggiungono altri 30+ agenti attivi. Per un'azienda di tre persone che valuta ogni spesa a preventivo, questo numero — anche solo come stima dichiarata, non come misura — mancava e andava scritto prima di costruire, non lasciato come "si misura al primo lancio" (08 riga 302).

## 3. IL DOSSIER 07 — difetti strutturali

**D-D-01 — Le formule di `previsto_a_oggi` non hanno un tetto per le voci scadute.**
Riga: 74 (`lineare`) e 78 (`posticipato`), confrontate con riga 76 (`unico`, correttamente capato) e riga 77 (`anticipato`, correttamente capato con `min(1, ...)`).
Perché si rompe: `lineare → importo × (giorni trascorsi / giorni totali della voce)` non ha `min(1, ...)`. Se `giorni_trascorsi > giorni_totali` (voce scaduta ma non chiusa), il rapporto supera 1 e `previsto_a_oggi` supera l'importo budgetato per quella voce. Lo stesso per `posticipato`: quando `giorni_trascorsi > giorni_totali`, il numeratore supera il denominatore.
Caso concreto: una voce "pubblicita" da 400€, profilo `lineare` (il default dichiarato a riga 81, quindi il caso più comune quando nessuno specifica il profilo), con fine prevista il 19/10. Se al 25/10 nessuno ha ancora chiuso la spesa finale, `previsto_a_oggi` di quella voce sale oltre i 400€, gonfiando il denominatore di `scarto_pct` (riga 130, formula di GATE-TSR-2). Uno sforamento reale del 20% appare più piccolo di quanto sia — esattamente il tipo di gate "che non può bloccare mai" che questa terza versione dichiara di aver eliminato (riga 69).
Riparazione: aggiungere `min(1, ...)` a `lineare` e a `posticipato`, come già fatto per `anticipato`.

**D-D-02 — La regola delle "tre deroghe" non ha un esecutore.**
Riga: 115-116 ("tre deroghe sullo stesso lancio obbligano a rifare il budget da capo").
Perché si rompe: è scritta in prosa, senza contatore né gate. Non compare nella macchina a stati di 01 §4 (righe 256-307: nessuna transizione conta le deroghe), né come campo nello schema di `deroghe.json` (mai definito, solo nominato a riga 102). È lo stesso principio che 08 enuncia contro sé stesso (righe 61-62: "una regola scritta in prosa viene disobbedita").
Caso concreto: alla terza voce scritta in `deroghe.json` per lo stesso `lancio_id`, nessun componente del sistema se ne accorge: il lancio prosegue, il tetto derogato tre volte resta in vigore.
Riparazione: un contatore in `gate.py` che legge `deroghe.json` per `lancio_id` e alla terza voce forza la transizione "IN_PRODUZIONE → DATATO" già esistente in 01 (riga 298), rendendo il vincolo meccanico.

**D-D-03 — `costo_acquisizione(canale)` non ha una fonte dati definita.**
Riga: 124, con la nota alle righe 133-136 sulla non-mescolanza di traffico gratuito e comprato.
Perché si rompe: la formula presume un numero — clienti attribuiti per canale — che nessun documento dice chi produce, in che schema, e con quale handoff verso `LAN-TSR`. La tabella "chi produce/valida" di 01 §1.6 (righe 100-111) non ha una riga per questo dato fra FNL/TRF e TSR.
Caso concreto: `lan-tsr-sentinella` (T5, riga 92) deve "ricalcolare... il costo di acquisizione" ma non ha da dove leggerlo in modo strutturato: o lo chiede a mano (rompendo l'automazione dichiarata alla stessa riga), o lo stima (violando il principio 5 di 08, riga 91).
Riparazione: aggiungere in 01 §1.6 una riga esplicita per un `attribuzioni-per-canale.json` prodotto da FNL/TRF e letto da TSR, con lo schema, prima di costruire `lan-tsr-sentinella`.

**D-D-04 — Il campione di verifica delle fonti può scendere sotto 15 senza che la regola lo dica.**
Riga: 178 ("Numero di frasi ≥15") vs riga 192 ("le fonti irraggiungibili... le loro frasi non contano nel conteggio delle quindici").
Perché si rompe: non è chiaro se I2 (riga 165) deve raccogliere esattamente 15 frasi o un margine in più per assorbire il decadimento dei link nel tempo che passa fra raccolta (I2) e gate (dopo I7).
Caso concreto: I2 raccoglie 15 frasi con fonte il giorno 1. Il gate gira dopo I3-I7, giorno 10: 2 fonti sono morte nel frattempo (comune su forum/recensioni). Restano 13 frasi valide, sotto la soglia "≥15" — ma il calendario dedica a tutto INT solo 2 giorni di margine (07 riga 247), non pensati per un secondo giro di raccolta.
Riparazione: dichiarare esplicitamente in B.2/B.3 un margine di raccolta (es. 18-20 frasi), oppure spostare la verifica di raggiungibilità subito dopo I2.

**D-D-05 — Il calendario di WF-INT lascia margine zero nel caso peggiore che il documento stesso dichiara.**
Riga: 158 ("16-30 ore-uomo") vs riga 247 (finestra T-30→T-26, 4 giorni di calendario, "2 g" dichiarati come margine).
Perché si rompe: 30 ore-uomo a ritmo pieno sono quasi 4 giorni pieni. Se la ricerca richiede il massimo dichiarato, consuma l'intera finestra, lasciando zero margine reale per un rigetto di GATE-INT-1 — che è esattamente il tipo di rifacimento per cui la sezione C.1 dice che il margine esiste (righe 269-271).
Caso concreto: la ricerca richiede 28 ore-uomo (dentro il range dichiarato), finisce al giorno 4; il gate anti-invenzione la respinge (è previsto, righe 194-196): non resta margine nella finestra INT, e il ritardo si scarica sulle fasi successive, che hanno solo 1 giorno di margine ciascuna.
Riparazione: restringere la stima INT a un range compatibile con 4 giorni (es. 16-24 ore), oppure allargare la finestra T-30→T-26 a 5 giorni, dichiarando quale delle due scelte si è fatta.

**D-D-06 — "Si parte ridotto" non definisce quali delle dieci voci sono "non essenziali".**
Riga: 302-315 (le dieci voci) e riga 325 ("mancano voci non essenziali (es. gli annunci)").
Perché si rompe: l'unico esempio dato è "gli annunci", che non compare nemmeno come voce esplicita fra le dieci. Le altre nove non sono classificate: è essenziale la voce 7 (piano editoriale coi primi contenuti usciti)? La voce 6 (sequenze email caricate)? Senza una classificazione, la scelta fra "si parte ridotto" e "si rinvia" (righe 320-330) resta arbitraria nel momento peggiore per deciderla arbitrariamente: un giorno prima dell'apertura.
Riparazione: aggiungere una colonna "essenziale: sì/no" alla tabella di C.3.

## 4. L'ADR PROPOSTO DECIDE QUALCOSA?

**In parte sì, in parte è un riassunto travestito da decisione.** Degli 8 punti della sezione "Decisione" (righe 44-59):

- **Punti 1, 4, 6, 8 decidono davvero, e sono verificabili:** (1) crea la cartella e riserva il numero 15 "nello stesso commit" (riga 44-45) — testabile su un diff; (4) "IB-L2-LANC si sposta... non si copia e non si riscrive" (riga 50) — vieta esplicitamente un comportamento, rilevabile con un confronto file; (6) lo scaglione minimo come gate tecnico di costruzione, con criterio di chiusura nominato (l'uscita reale del Manuale) e reso non aggirabile perché "il registro rifiuta gli agenti dei reparti non abilitati" (riga 56); (8) tre condizioni di abbandono con soglie numeriche precise (rimando a 09 §10: 64 ore, 60 giorni, due lanci).
- **Punti 2, 3, 5, 7 non decidono nulla di nuovo:** ripetono ciò che 01 (dodici reparti), 07 (sette flussi) hanno già specificato. E il punto 5 ("tredici gate bloccanti", riga 51) riporta un numero verificato sbagliato in Sezione 1 (sono 14 i gate nominati, con una sovrapposizione irrisolta fra GATE-TSR-3 e GATE-MEM-1). Un ADR che sbaglia il conto di ciò che descrive pesa come sintesi frettolosa, non come atto decisionale.

**Cosa diventa vietato dopo la firma:** copiare/riscrivere IB-L2-LANC invece di spostarlo; costruire oltre lo scaglione minimo prima che il Manuale sia uscito (bloccato a livello tecnico, non solo dichiarato); creare la cartella prima che l'ADR sia registrato (riga 3, riga 20). Questi tre vincoli sono reali, specifici, e sono la parte migliore del documento.

**Reversibilità: mai dichiarata esplicitamente.** L'ADR rimanda le condizioni di uscita a "dossier 00 §6" (riga 59, non fornito in questa revisione) e le tre condizioni di abbandono a 09 §10 — che sono condizioni per **fermare la costruzione**, non per **sciogliere la decisione architetturale** già presa (l'esistenza dell'ecosistema, lo spostamento di IB-L2-LANC). Se S0 supera 64 ore "si torna al piano e si taglia" (09 riga 213) — ma taglia cosa? Il piano non dice se IB-L2-LANC torna al suo ecosistema originale, se il numero 15 si libera di nuovo, o se la cartella (anche vuota) resta. Un ADR dovrebbe dire come si disfa, non solo quando si smette di costruire.

**Le tre decisioni umane esplicitamente non prese** (righe 88-93: prezzo/regalo del Manuale, standard testi, sistema visivo) sono corrette da lasciare aperte — onesto dichiararle piuttosto che deciderle per default.

**Verdetto:** non è "solo un riassunto" — vale come decisione vera per i punti 1/4/6/8 — ma non è nemmeno un ADR pulito: per i punti 2/3/5/7 descrive invece di decidere (con un errore numerico dentro), e manca del tutto una sezione di reversibilità per la decisione architetturale in sé, a differenza delle condizioni di stop della costruzione, che invece sono ben fatte.

## 5. I TRE GIRI — le correzioni dichiarate sono davvero nel corpo?

Verificate 8 delle 10 correzioni elencate in 10 §C.3 (righe 182-195), aprendo 07, 01, 08 e il repository vero (codice sorgente e file di stato reali, non solo testo dei dossier). Risultato: 6 confermate, 1 con un numero sbagliato dentro il changelog stesso, 2 già superate dallo stato reale del repository, 3 non verificabili con i soli file assegnati.

**CONFERMATE:**
- **#3** (budget non poteva fallire) → 07 righe 56-59 (date e profilo di spesa) e riga 101 (`budget_approvato_da` diverso da chi ha scritto le voci): presenti esattamente come dichiarato. Confermata, ma con un difetto residuo non colto dai tre giri: D-D-01 (Sezione 3).
- **#5** (nessun comando verifica l'ufficialità) → verificato **nel codice vero**: `empire/registry/census.py` riga 142 esclude esplicitamente `.claude/` dal censimento (`".claude/" in p_lower`), e `empire/forge.py` riga 157 limita la scansione a `(repo_root() / "company").rglob("*.md")`. La descrizione di 08 (righe 20-28) è accurata, verificata leggendo il sorgente, non per fiducia sul testo.
- **#6** (campo tools vietato per errore) → verificato: `grep -rl "^tools:" .claude/agents/` restituisce esattamente **18** file, lo stesso numero dichiarato a riga 41 di 08 ("diciotto agenti... funzionano perfettamente"). Numero esatto, non arrotondato.
- **#7** (SOSPESO senza uscita) → 01 righe 309-337 mostrano lo schema con `stato_di_partenza`, `revisione_il`, `come_si_esce`, tutti dichiarati obbligatori (righe 330-334). Confermata.
- **#8** (calendario incompatibile) → 07 righe 243-267: sommando la colonna "Margine" si ottiene 1+2+1+1+1+2+2+1+1 = **12**, esattamente il numero dichiarato a riga 269. Il conto torna aritmeticamente, ma vedi D-D-05: il margine di INT si azzera nel caso peggiore già previsto dallo stesso documento.
- **#9** (duplicazione dell'esistente) → 01 righe 122-133 mostrano l'etichetta 🔵 "avvolge" col percorso dichiarato per STR, INT, PRD, CPY, FNL, TRF, REG. Confermata.

**SBAGLIATA NEL NUMERO — dentro il changelog stesso:**
- **#1** (squadra minima) → 10 riga 186 dichiara la correzione "undici agenti su **sei** reparti". Contando i reparti toccati dagli undici agenti elencati in 01 §5.1 (righe 393-409): Direzione, Strategia, Intelligence, Prodotto, Offerta, Funnel, Regia, Qualità = **otto** reparti distinti, non sei. Il changelog che descrive la propria correzione sbaglia il conto di quello che sta descrivendo.

**GIÀ SUPERATE DALLO STATO REALE DEL REPOSITORY** (verificate da riga di comando, non dal testo dei dossier):
- Sia 08 (righe 65-70: "il registro dei numeri dice che il 15 è libero, ma alla voce riservati non c'è nessuno") sia implicitamente 10 (riga 44) descrivono un fatto **già falso al momento di questa revisione**: `company/Ecosistemi/REGISTRO-NUMERI.md` riga 36 mostra 15 = LANCI **già riservato**, con riferimento "ADR-022 proposto". Non è necessariamente un errore dei tre giri (il file può essere stato aggiornato in parallelo, stessa data), ma dimostra che le affermazioni di fatto sullo stato del repository, dentro un piano, invecchiano nell'arco delle stesse ore in cui il piano viene scritto. Chi esegue 08 §1.3 deve ricontrollare il registro dal vivo, non fidarsi della prosa del dossier.
- Allo stesso modo, `python -m empire conform` (eseguito ora) restituisce **`block: 1`**, non i "due bloccanti" dichiarati sia da 08 (riga 77) sia da 10 (righe 85-86: "Il controllo di conformità dell'Impero oggi esce in errore per due bloccanti estranei ai lanci"). Il blocco reale riguarda `WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/preventivo-template.md` (riferimento morto, estraneo ai lanci come dichiarato) — ma è **uno**, non due. Il numero "due" va riverificato subito prima di costruire, non preso per buono dal testo.

**NON VERIFICABILI CON I DOSSIER ASSEGNATI** (riguardano reparti/dossier fuori dal perimetro di questa critica — 07 non tratta Copy né Funnel):
- **#4** (griglia dei testi, 60→11 punti automatici, poi 42 su tre griglie): riguarda il reparto Copy.
- **#2** (flusso funnel senza fasi/agenti, poi nove fasi): riguarda WF-FNL.
- **#10** (citazione falsa sui componenti parametrizzabili): riguarda un dossier di prodotto/funnel non fornito.

**Conclusione:** la maggioranza delle correzioni dichiarate **regge** alla prova diretta — inclusa una verifica nel codice sorgente vero, non solo nel testo del piano, un livello di rigore raro. Ma due controlli campione hanno trovato un problema reale: un numero sbagliato dentro il changelog stesso (#1), e due affermazioni di fatto sullo stato del repository già superate dagli eventi nell'arco delle stesse ore (registro numeri, controllo di conformità). Un changelog che sbaglia anche solo occasionalmente il proprio conto disarma il prossimo revisore tanto quanto uno che dichiara il falso: non si sa più quali righe fidarsi a occhio e quali ricontrollare tutte.

## 6. BUCHI — cose che il piano NON dice e servono per costruire

1. **Attribuzione clienti-per-canale** (v. D-D-03): nessuno schema/handoff fra LAN-FNL/LAN-TRF e LAN-TSR per il dato che alimenta `costo_acquisizione(canale)`.
2. **"Cassa provata con una transazione reale"** (07 riga 310, voce 5 della sincronizzazione): non è specificato lo script/strumento che esegue o verifica la transazione di prova, chi la esegue, o come si distingue da un incasso vero. Le altre nove voci della stessa tabella hanno tutte un "come si verifica" concreto; questa è l'unica rimasta vaga.
3. **Contatore delle deroghe** (v. D-D-02): nessun componente tecnico applica "tre deroghe = rifare il budget da capo".
4. **Concorrenza sui file di stato**: nessuna menzione di cosa succede se `stato_lancio.json`/`budget.json` vengono toccati nello stesso momento da due processi (Max e Gael lavorano in parallelo su questo stesso repository, con commit di sincronizzazione automatici — visibile nella cronologia git) su un lancio che dura settimane.
5. **Privacy/GDPR** sulle "frasi vere del pubblico, ognuna con l'indirizzo" (07 righe 165-166, ritenzione 12 mesi, riga 208): si archiviano citazioni verbatim di persone reali con la fonte, per un anno, senza menzione di base giuridica, anonimizzazione o diritto alla cancellazione.
6. **Il costo in chiamate-modello** (v. Sezione 2): nessuna stima numerica esiste nei tre dossier, nemmeno d'ordine di grandezza per il solo pilota.

## 7. CIÒ CHE È SOLIDO — non toccarlo

- **08 §1.1 (righe 18-34) è verificato nel codice sorgente vero**, non solo asserito: `census.py` riga 142 e `forge.py` riga 157 confermano esattamente quanto descritto. Il piano non si è fidato della propria memoria, è andato a leggere il codice — raro.
- **La correzione del campo `tools`** (08 §1.2) è concettualmente corretta e verificata nel repository (18 agenti reali già lo usano) per i ruoli Gate/Sentinella/Ricercatore/Operatore, dove la restrizione richiesta è di classe di strumento, non di percorso.
- **Il ridisegno del budget** (07 Parte A: date+profilo di spesa, approvazione da terzi) è concettualmente il fix giusto per il problema giusto, anche col bug residuo D-D-01.
- **SOSPESO con uscita obbligata** (01 §4.3) è un presidio reale contro un fallimento già documentato in questa azienda (un modello di memoria morto in silenzio).
- **Il criterio del pilota** "un sistema di gate che non ha mai bloccato non è provato" (10 righe 139-144) è controintuitivo e corretto — raro trovarlo scritto in un piano.
- **Le tre condizioni di abbandono** con soglie numeriche (09 §10) sono un vincolo di uscita reale — la maggior parte dei piani non ne ha nessuna.
- **Il gate anti-invenzione con verifica a campione** (07 B.3) è onesto sui propri limiti ("resta un controllo statistico, non una prova", riga 200) invece di vendersi come definitivo.

## 8. LE 5 COSE PIÙ IMPORTANTI DA CAMBIARE

1. **Correggere il bug delle formule di budget** (D-D-01, 07 righe 74 e 78): aggiungere `min(1, ...)` a `lineare` e `posticipato`. Senza, GATE-TSR-2 — il gate che questa versione dichiara di aver reso "capace di fallire" — può tornare a non bloccare mai, proprio sulle voci scadute non chiuse, il caso più comune a fine lancio.
2. **Riconciliare i conti** fra 01 §1.1 (11 capi reparto, 30 operativi, 13 gate) e il censimento reale di 08 §4 (10, 29, 14) — e risolvere la sovrapposizione fra GATE-TSR-3 e GATE-MEM-1 sulla stessa transizione CHIUSO→APPRESO, che oggi non è cablata in nessuna macchina a stati.
3. **Trasformare in script gli agenti puramente aritmetici**: almeno `lan-tsr-conductor`/`sentinella`, `lan-reg-calendarista`, e applicare alle 6 entità "sentinella" lo stesso modello "un motore + N file di criterio" già usato per i gate. Riduce sia il numero di agenti da costruire sia il costo per lancio.
4. **Scrivere una stima numerica del costo per lancio** (anche solo un conteggio di invocazioni attese per il pilota), invece delle sole classi qualitative: è l'unico dato mancante per decidere se l'ecosistema si ripaga, e la Tesoreria dell'Impero (a cui questo piano dice di dover "salire") non può contabilizzare una spesa che nessuno ha stimato nemmeno in ordine di grandezza.
5. **Ri-verificare dal vivo, non dal testo dei dossier**, lo stato di `REGISTRO-NUMERI.md` e di `python -m empire conform` prima di costruire: entrambi risultano già diversi da quanto scritto in 08/10 (15 già riservato; un solo blocco, non due). I dossier descrivono uno stato del repository già cambiato nell'arco delle stesse ore in cui sono stati scritti — ogni affermazione di fatto in un piano ha una data di scadenza breve.

---

**Altro notato, non approfondito (fuori perimetro di questa critica):**
- Verifica delle correzioni #2, #4, #10 di dossier 10: richiede i dossier di Copy e Funnel, non assegnati qui.
- Il registro ADR (`company/Memory/decisions/`) ha già due numeri duplicati (ADR-012 e ADR-016, due file ciascuno) — non riguarda i lanci, notato solo verificando che ADR-021 sia davvero l'ultimo prima di ADR-022.
- Progettare l'hook `PreToolUse` che renderebbe vero lo scoping di percorso per il ruolo Archivista (individuato in Sezione 1, non progettato qui).
- Il "reparto Vendite & Funnel" citato nell'ADR (riga 46) meriterebbe lo stesso controllo di sovrapposizione già fatto per TRF/EDT in 01 §2.1.
