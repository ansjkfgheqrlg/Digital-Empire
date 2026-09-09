# PIANO CHIRURGICO — INNESTO DELLO STUDIO ANDREI PASCU DENTRO L'ECOSISTEMA LANCI

**Stato:** DRAFT V1 — destinato a tre giri di critica (P1 → P2 → P3)
**Data:** 2026-09-09
**Autore:** Doom Bot (assetto massimo), su ordine di Emperator
**Governo applicabile:** ADR-024 (canone v2, otto controlli) · ADR-025 (nascita LANCI) · ADR-026 (piena autorità di Gael, blocchi mai silenziosi) · ADR-027 (S0 non blocca la costruzione) · ADR-028 (niente blocca tutto) · ADR-003 (wrap, mai riscrittura) · ADR-005 (backlog non blocca)
**Bersaglio:** `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/` + `company/Ecosistemi/15-LANCI/` (in costruzione) + il primo lancio reale (Manuale Claude Code)

---

## 0. COME SI LEGGE QUESTO DOCUMENTO

### 0.1 Cosa contiene

**27 azioni**, ognuna con: cosa cambia esattamente (testo vero o struttura vera, non "aggiungere una nota"), dove (path esatto), chi (Gael / Max / sessione qualunque), quando (S0→S5 di `TASK-LANCI-BUILD-W3`), perché (principio misurato di Andrei Pascu con citazione), effort, e **cosa blocca esattamente** (ADR-028 punto 4).

Le azioni si dividono in due famiglie:

| Famiglia | Cosa | Numerazione |
|---|---|---|
| **A** | I quattro candidati già scritti e assegnati a questo piano | AP-004, AP-005, AP-008, AP-033 |
| **B** | Ciò che lo studio ha misurato e che i 33 candidati **non hanno catturato** | AP-034 → AP-060 (23 nuovi) |

### 0.2 Correzione di fatto al briefing

Il briefing dice «12 candidati già applicati». La tabella 🟢 di `MIGLIORAMENTI-DIGITAL-EMPIRE.md` (righe 25-39) ne contiene **13**: AP-001, 002, 003, 006, 007, 009, 010, 011, 012, 013, 014, 015, **016**. Più quattro marcati 🟢 «consegnato» nell'ultima tabella (AP-029..032). **Totale verde reale: 17.** Nessuno di questi è ri-proposto qui.

### 0.3 La spina dorsale del piano: due corsie per rischio di collisione, non per argomento

Gael sta costruendo **adesso** dentro `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/` e `company/Ecosistemi/15-LANCI/`. `04-COSTRUZIONE.md` §8 impone il blocco ⚠️ COORDINAMENTO in `STATO-EMPIRE.md` prima dei lavori grossi. Quindi il piano si divide **prima** per chi può toccare cosa, e **solo dopo** per scaglione:

| Corsia | Perimetro file | Chi può eseguire | Collisione con Gael |
|---|---|---|---|
| **C1 — LIBERA** | `.claude/skills/fabbrica-siti/**`, `competitor/Andrei Pascu/**`, `company/Memory/BACKLOG.md`, ADR nuovi | **qualunque sessione**, subito, senza coordinamento | **zero** |
| **C2 — RISERVATA** | `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/registro.yaml`, `dati/schemi/*.json`, `company/Ecosistemi/15-LANCI/**` | **solo Gael**, dentro la propria micro-task | **alta** — `valida_registro.py` deve restare a exit 0 |

> **Regola operativa che nasce da qui:** nessuna azione di corsia C1 aspetta Gael, e nessuna azione di corsia C2 viene eseguita da una sessione diversa da quella che sta girando la micro-task corrispondente. Il 62% del piano (17 azioni su 27) è in C1 e **può partire oggi senza toccare niente di ciò che Gael ha in mano**.

### 0.4 Scala di effort

| Sigla | Significato | Ore-uomo |
|---|---|---|
| **T1** | righe di testo dentro un file che esiste già | 0,25 - 0,75 h |
| **T2** | sezione nuova, pattern nuovo, blocco di schema | 1 - 3 h |
| **T3** | script nuovo, o modifica al registro con test rosso e ri-validazione | 3 - 8 h |
| **T4** | decisione umana / firma / ADR | non è ore-uomo: è attesa, e ha la sua scadenza |

---

## 1. IL RITROVAMENTO CHE VIENE PRIMA DI TUTTI GLI ALTRI

**Gli otto controlli di ADR-024 non esistono come codice. Nessuno di loro.**

Verificato sul disco il 2026-09-09:

```
$ find . -name "gate_siti*"
(nessun risultato)
$ ls .claude/skills/fabbrica-siti/scripts/
canone_sync.py   galleria.py
```

Lo dice ADR-024 stesso, §6: *«Il gate non esiste ancora (Fase 4): i quattro controlli sono **debito dichiarato**, non attivi.»*

E il controllo 8 è, testualmente, ADR-024 §4: *«Il controllo 8 non è solo per la Fabbrica Siti: **è il primo gate obbligatorio dell'ecosistema LANCI** (ADR-025) — nessun lancio parte senza che la catena dall'annuncio alla cassa sia stata percorsa a macchina.»*

**Quindi oggi il primo gate obbligatorio di LANCI è una frase.** E il difetto che quel gate esiste per prevenire — `/vendita → /acquista-v101` a 404, la cassa vera di un prodotto da 400 € non linkata da nessuna parte (`ANATOMIA-DEI-LANCI.md` Parte VIII, difetto #1) — è, per citazione diretta, *«il più costoso trovato addosso a un concorrente»* e *«vale da solo tutto lo studio»*.

Questo è **AP-034**, ed è l'azione con la priorità più alta del piano intero.

> **Nota ADR-028, obbligatoria:** questo ritrovamento **non ferma niente**. Non ferma S0, non ferma S1, non ferma S2. Blocca esattamente una cosa: la possibilità di dichiarare onestamente `GATE-FNL-1` passato con il controllo 8 incluso, cioè **una riga del criterio di uscita di `VE-1`**. Tutto il resto della settimana procede identico.

---

## 2. IL VINCOLO DI GOVERNO — cosa posso proporre senza amendment, e cosa no

Prima delle azioni, la mappa di ciò che il governo permette. Serve a rendere ogni riga sotto verificabile invece che opinabile.

| Tipo di modifica | Serve un amendment? | Perché |
|---|---|---|
| Aggiungere un **campo** a uno schema in `dati/schemi/*.json` | **No** | ADR-025 decisione 3 vincola le **sigle** (artefatti, gate, stati, agenti), non i campi. Ma `additionalProperties: false` è ovunque: la modifica è reale e `valida_registro.py` va rifatto |
| Estendere il `criterio_eseguibile` di un **gate esistente** | **No**, ma serve il test rosso | INV-04: *«un controllo senza un caso che lo faccia fallire è decorativo per costruzione»*. Nessun criterio nuovo senza il suo rosso |
| Aggiungere un **artefatto** (14°) | **Sì — amendment ADR-025 decisione 2** | La decisione fissa tredici artefatti per nome |
| Aggiungere un **agente** (16°) | **Sì — amendment ADR-025 decisione 4** | La decisione fissa quindici agenti per nome, e la motivazione è economica (tassa di harness 0,08-0,11 $ per invocazione, ADR-014) |
| Aggiungere un **gate** nuovo | **Zona grigia — dichiararlo** | ADR-025 non fissa il numero dei gate; `TASK-GAEL-20260908-SETTIMANA-03.md` §1️⃣ dice «14 gate». Preferire sempre l'estensione di un gate esistente |
| Aggiungere un **articolo a `CLAUDE-SITI.md`** (§13, §14) | **Sì — serve un ADR nuovo** | `CLAUDE-SITI.md`, sezione «Come si cambia questa legge»: *«Non si cambia in una conversazione. Si cambia con un ADR»* |
| Cambiare il `const` di `previsione.schema.json.formula` | **Sì — dichiarazione di variante nel documento 02** | La formula è scritta come costante apposta: *«una previsione di cui non si può rifare il conto a mano non è una previsione»*. **Questo piano evita questa strada** — vedi AP-004 |
| Scrivere codice nuovo in `.claude/skills/fabbrica-siti/scripts/` | **No** | ADR-024 §4 lo prevede già come Fase 4. Non è una decisione nuova: è debito dichiarato che si paga |

**Le tre azioni di questo piano che richiedono un amendment esplicito sono dichiarate nel §6.** Nessuna regola scritta in un ADR viene riscritta qui di mia iniziativa.

---

## 3. FAMIGLIA A — I QUATTRO CANDIDATI ASSEGNATI

---

### AP-004 — Il blueprint Tripwire, applicato al Manuale Claude Code

**Fonte:** outFunnel Lezione 20, KA-02, verbatim dal `lesson-analysis.md` (riga 25):

> *«Blueprint completo a 6 step: Traffico (ads + organico) → Lead Magnet multi-opt-in (PDF/libro/software gratis) → Email di consegna con redirect immediato → Sequenza email per vendere il Tripwire (es. 50€) → Se acquista, upsell al prodotto principale (es. 500€) → Se non acquista, follow-up a lungo termine (es. ogni 7 giorni).»*

E il problema che risolve, KA-01 (riga 24):

> *«prodotti costosi (es. 500€) sono difficili da vendere direttamente via ads — soluzione: introdurre un primo acquisto economico (Tripwire) per abbassare la resistenza; esempio Apple (iPhone come porta d'ingresso verso Mac/iPad più costosi).»*

Rinforzato da Lezione 6, KA-05 (riga 25): *«prima offerta a bassissimo prezzo (es. 5€) […] chi ha già pagato una volta spende più facilmente la volta dopo»*.

#### 3.1 Il fatto che rende questo candidato diverso da tutti gli altri

Digital Empire possiede **già entrambi i pezzi del blueprint**, finiti, e non ne ha lanciato nessuno:

| Pezzo | Cosa | Stato misurato | Fonte |
|---|---|---|---|
| **Tripwire** | Manuale Claude Code, 203 pagine | pronto dal **07/03/2026**, prezzo «€ NON LO SO» | `ADR-025`, tabella Contesto |
| **Prodotto principale** | «Claude Code Mastery», **397 €** | funnel già scritto: 18.770 px, 25 sezioni, 506 blocchi, **fermo su staging** | `ANATOMIA-DEI-LANCI.md` Parte X punto 5 |

E la Parte IX del modello a 12 passi, passo 1, dice testualmente: **«Scegli i pezzi che esistono già — mai costruire prodotto nuovo per un lancio.»** Non è un'analogia: è letteralmente la configurazione che il modello prescrive, già sul disco.

#### 3.2 La decisione strutturale — e perché NON tocco `previsione.schema.json`

Il registro modella **un lancio = un prezzo**: `offerta.schema.json` ha `prezzo` singolo, e `previsione.schema.json` ha `formula` come `const`:

```
"ricavo_lordo = pubblico_raggiungibile * tasso_visita * tasso_acquisto * prezzo"
```

Una catena tripwire→principale ha due prezzi e due ricavi. La strada sbagliata è cambiare quella costante. **La strada giusta, a costo zero di amendment, è: due lanci incatenati.**

| | Lancio 1 | Lancio 2 |
|---|---|---|
| `lancio_id` | `manuale-cc-2026` | `mastery-cc-2026` |
| Prodotto | Manuale Claude Code | Claude Code Mastery |
| `ruolo_prodotto` | **`vendita`** (enum già ammesso) | `vendita` |
| Fascia prezzo proposta | 27-47 € | 397 € (già dato in azienda) |
| Il suo `previsione.json` | proprio, formula invariata | proprio, formula invariata |
| Il legame | `alternative_scartate[].perche_no` + `struttura.ancoraggio` | `prezzi_precedenti_trovati[]` cita il lancio 1 |

**Zero modifiche di schema. Zero amendment. Il legame vive nei campi che esistono già.**

#### 3.3 Cosa cambia esattamente, dove, chi, quando

| Campo | Contenuto |
|---|---|
| **COSA** | (1) In `company/Ecosistemi/15-LANCI/lanci/manuale-cc-2026/offerta.json`, campo `struttura.ancoraggio`, il testo: *«Il Manuale è il primo gradino di una scala: chi lo compra riceve, dentro il prodotto, il percorso completo verso Claude Code Mastery (397 €). Il prezzo del Manuale non copre il suo valore: copre la soglia oltre la quale un lettore diventa un cliente.»* (2) In `previsione.json` del lancio 1, dentro `assunzioni[]`, una riga nuova: `{"nome": "tasso_conversione_tripwire_verso_mastery", "valore": <numero>, "stato": "assunto", "da_dove_viene_se_assunto": "benchmark di settore — outFunnel Lezione 20 non dà una cifra, la nostra è un numero di comodo dichiarato"}`. (3) In `alternative_scartate[]` dell'offerta, il prezzo alto scartato con `perche_no: "un prezzo da prodotto principale su un prodotto che il registro tratta come porta d'ingresso — vedi lancio mastery-cc-2026"` |
| **DOVE** | `company/Ecosistemi/15-LANCI/lanci/manuale-cc-2026/{offerta,previsione}.json` — path da confermare contro la struttura che Gael sta creando |
| **CHI** | **Gael**, dentro `MT-9ADD` (S1, i quattro artefatti a mano). Il **valore numerico del prezzo** resta di **Max** (`PU-PREZZO`) |
| **QUANDO** | **S1**, dentro `MT-9ADD`. È il momento esatto in cui `offerta.json` viene compilato a mano |
| **PERCHÉ** | outFunnel L20 KA-01: *«prodotti costosi (es. 500€) sono difficili da vendere direttamente via ads»*. Il Mastery a 397 € è fermo su staging **con il funnel già scritto** — la diagnosi del corso spiega perché non è mai partito |
| **EFFORT** | **T1** (3 campi di testo) + **T4** (la firma sul prezzo, che sarebbe servita comunque) |
| **CORSIA** | **C2 — riservata a Gael** |

#### 3.4 Cosa blocca esattamente (ADR-028)

> Questa azione **non blocca niente**. Il valore di `prezzo` è già un punto umano con le sue regole (`PU-PREZZO`, 14 giorni, nessun default — `03-FLUSSO-OFFERTA.md` §O5). Il testo dell'ancoraggio si scrive **prima** e indipendentemente dal numero, e resta valido qualunque numero Max firmi. **Se questa azione non si fa affatto, `MT-9ADD` si chiude lo stesso** e AP-004 va in `BACKLOG.md` (ADR-005).

#### 3.5 L'input che va portato a Max attivamente (ADR-026)

`00-LEGGIMI.md` §4 decisione 1: *«Il Manuale si vende o è un regalo?»*, scadenza **12/09**, default reversibile `vendita`.

**Questo piano aggiunge una terza formulazione della domanda, che nessuno ha ancora posto a Max:**

> *«Il Manuale non è "si vende o si regala". È "si vende a prezzo pieno o a prezzo di porta d'ingresso verso Mastery, che è già scritto e fermo su staging da mesi". Le due strade hanno lo stesso `ruolo_prodotto` nel registro (`vendita`) — cambia solo la fascia, e la fascia è reversibile al rialzo mai al ribasso.»*

Va portato a Max **lo stesso giorno**, in cima a `STATO-EMPIRE.md`, come impone ADR-026. **E non blocca:** il default `vendita` è già dichiarato e reversibile, e vale per entrambe le formulazioni.

---

### AP-005 — Le ads dinamiche a countdown e le tre versioni della pagina di vendita

**Fonte:** outFunnel Lezione 16, `lesson-analysis.md` righe 22-24, verbatim:

- **KA-02** (riga 22): *«Funnel per Promozioni: ha scadenza precisa, l'urgenza è centrale e DEVE crescere man mano che ci si avvicina alla fine — esempio a 3 fasi (pre-ordine → centrale con scarsità rinforzata → ultimi giorni con urgenza massima).»*
- **KA-03** (riga 23): *«Tecnica "Ads dinamiche": durante una promo di 30 giorni si creano fino a 30 varianti dello stesso annuncio, cambiando SOLO la cifra dei giorni rimanenti nel copy ("Mancano 30 giorni" → … → "Ultimo giorno") — copy e video restano identici, cambia solo la data.»*
- **KA-04** (riga 24): *«Sales Page adattabile in 3 versioni sequenziali: v1 focus sul valore (inizio promo), v2 rinforzo con social proof (metà promo), v3 timer/countdown con CTA forte (ultimi giorni).»*

#### 3.6 Dove va, e perché non serve toccare `copy.schema.json`

Trenta varianti di annuncio **non sono trenta pezzi di copy**: sono trenta **righe di calendario** che puntano allo stesso pezzo. Il registro lo modella già:

- `editoriale.schema.json` → `contenuti[]` con `data_uscita`, `canale`, `a_pagamento`, `formato`, `destinazione`, `stato`
- `GATE-EDT-1` criterio (registro riga 372-374): *«ogni contenuto ha destinazione risolvibile in ART-FNL AND ogni giorno del carrello ha almeno un contenuto»*

Trenta righe di countdown **soddisfano il criterio di GATE-EDT-1 per costruzione**. Il candidato non aggiunge un vincolo: riempie uno che c'è già ed è vuoto.

| Campo | Contenuto |
|---|---|
| **COSA** | (1) In `ART-CPY`, **un solo** `pezzo` di `tipo: "annuncio"` con `id: "ann-countdown-template"` e nel file di testo la variabile letterale `[GIORNI_RIMANENTI]`. (2) In `ART-EDT`, **una riga per ogni giorno del carrello**, con `formato: "annuncio-countdown"`, `a_pagamento: true`, `destinazione` = ruolo della pagina di vendita, e `id` nella forma `ann-countdown-g<N>` — la convenzione di nome è il legame verso il pezzo di copy. (3) **Tre righe aggiuntive** in `ART-EDT` con `formato: "cambio-versione-pagina"` alle date di stacco v1→v2→v3 |
| **DOVE** | `company/Ecosistemi/15-LANCI/lanci/manuale-cc-2026/copy/manifest.json` e `editoriale.json` |
| **CHI** | **Gael**, dentro `MT-GEKH` (S3) |
| **QUANDO** | **S3**, dopo `ART-CPY` e prima del gate `GATE-EDT-1` |
| **PERCHÉ** | KA-03: *«copy e video restano identici, cambia solo la data»* — è il costo marginale zero applicato alla scarsità. E si allaccia alla costante 7 di `ANATOMIA-DEI-LANCI.md` Parte V: *«La scarsità è di tempo, mai di posti. Un limite di posti su un prodotto digitale è una bugia che il cliente può smontare; una finestra temporale no»* |
| **EFFORT** | **T2** (le righe si generano da uno script di venti righe, non a mano) |
| **CORSIA** | **C2** |

#### 3.7 Il difetto strutturale che questo candidato apre, e che va chiuso nello stesso turno

**Tre versioni sequenziali della stessa pagina di vendita rompono `GATE-FNL-1`.** Il criterio (registro riga 362) verifica che *«ogni pagina risponde 200»* — a un istante. Una pagina il cui contenuto cambia al giorno 10 e al giorno 25 **non viene mai ri-verificata**, e la v3 (quella con il countdown e la CTA forte, cioè quella che incassa) è **l'unica che nessun gate ha mai guardato**.

È lo stesso difetto di Andrei Pascu ribaltato: lui ha la pagina viva e la cassa morta; noi rischiamo la pagina verificata e la sua versione finale mai verificata.

**Riparazione, dentro la stessa azione:** ogni riga `cambio-versione-pagina` di `ART-EDT` deve, nel giorno in cui scatta, ri-eseguire il controllo 8 sulla pagina cambiata. Concretamente: `catena.py` (AP-034) prende un argomento `--solo <url>` e la riga di calendario lo invoca.

**Cosa blocca:** *nulla oggi*. Se `catena.py` non esiste al momento di S3, la riga di calendario si scrive lo stesso con `stato: "da-fare"` e la verifica è manuale — **il piano non introduce un blocco che oggi non c'è**.

#### 3.8 Il vincolo di onestà che va scritto accanto

`SINTESI-SISTEMA-COPY.md` §8 regola 3: *«Il rifiuto esplicito di una tecnica manipolativa è esso stesso un argomento di vendita»*, con la citazione misurata *«Nessun impegno. Niente countdown finti.»* [y=11200].

Quindi il countdown della v3 **deve contare verso `offerta.data_chiusura` reale, e verso nient'altro**. Vedi AP-052.

---

### AP-008 — La checklist a 7 fattori diagnostici fra gli step

**Fonte:** outFunnel Lezione 12, `lesson-analysis.md` riga 22, KA-01, verbatim:

> *«Checklist di 7 fattori "fra gli step": (1) tempo trascorso fra step, (2) transizione emotiva, (3) contenuti esterni visti nel frattempo (es. ads di competitor), (4) coerenza del tono di voce, (5) aspettative create negli step precedenti, (6) eventi esterni/stagionalità, (7) cambiamenti nella percezione generale del mercato.»*

Il candidato dice, correttamente: *«nessuno dei 7 è oggi nei controlli di gate della Fabbrica Siti (che coprono correttezza tecnica, non coerenza temporale/emotiva)»*.

#### 3.9 Il problema di progettazione, e la sua soluzione già presente in casa

Sei dei sette fattori **non sono verificabili da un programma**. «Transizione emotiva» e «coerenza del tono di voce» non hanno un valore di ritorno. Un gate che pretende di giudicarli è un gate che finge.

**Ma la casa ha già il pattern giusto**, in `ricerca.schema.json`, campo `campione_verificato`:

> *«Il gate riapre almeno tre fonti a caso e registra l'esito. È il solo modo di distinguere una ricerca da un'invenzione ben scritta.»*

Il gate **non giudica la ricerca: verifica che la verifica sia stata fatta.** Si applica identico ai 7 fattori.

| Campo | Contenuto |
|---|---|
| **COSA** | Aggiungere a `funnel.schema.json` un array `transizioni[]`, **obbligatorio**, una riga per ogni coppia di pagine consecutive. Struttura esatta: `{"da": "<ruolo>", "a": "<ruolo>", "fattori": {"tempo_fra_step": {...}, "transizione_emotiva": {...}, "contenuti_esterni_nel_frattempo": {...}, "coerenza_tono": {...}, "aspettative_create_prima": {...}, "eventi_esterni_stagionalita": {...}, "percezione_mercato": {...}}, "compilata_da": "<agente>", "compilata_il": "<date-time>"}`. Ogni fattore è `{"esito": "coerente" | "da-correggere" | "non-applicabile", "nota": "<string, minLength 10>"}`. **`"non-applicabile"` è ammesso; il campo vuoto no** |
| **DOVE** | `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/schemi/funnel.schema.json` |
| **PIÙ** | Estendere `GATE-FNL-1.criterio_eseguibile` nel registro (riga 361-364) aggiungendo in coda: `AND ogni coppia di pagine consecutive ha una riga in transizioni[] con tutti e sette i fattori compilati e nota non vuota` |
| **PIÙ** | Il **test rosso**, obbligatorio per INV-04, da scrivere nel campo `test_rosso` di `GATE-FNL-1`: *«un funnel con tutte le pagine a 200, transazione di prova presente, e una transizione con il fattore coerenza_tono a nota vuota deve BLOCCARE»* |
| **CHI** | **Gael**, dentro `MT-4GNU` (il test rosso, che viene **prima**) e `MT-GEKH` (lo schema e il criterio) |
| **QUANDO** | Il test rosso in **S2** (`MT-4GNU` — nota: quella micro-task copre i sei rossi di S2; questo è un settimo, di S3, e va detto esplicitamente per non far fallire il conteggio «sei casi su sei»). Lo schema e il criterio in **S3** (`MT-GEKH`) |
| **PERCHÉ** | outFunnel L12 KA-01. E la controprova più dura dello studio: `ANDREI-PASCU-DOSSIER-COMPLETO.md` §6 — *«Il difetto più costoso mai misurato in tutto lo studio è l'errore esatto che il suo stesso corso insegna a non fare»*. Andrei vende la diagnosi fra gli step e non la applica al proprio funnel |
| **EFFORT** | **T3** (schema + criterio + rosso + ri-validazione a 832 controlli) |
| **CORSIA** | **C2** |

#### 3.10 Cosa blocca esattamente

> Blocca **solo `GATE-FNL-1`**, e solo dopo che lo schema è modificato. Prima di quel momento non esiste. Se non si fa, il funnel del primo lancio passa esattamente come passerebbe oggi. **Non è una precondizione di nessuna micro-task di `TASK-LANCI-BUILD-W3`.**

#### 3.11 Attenzione al conteggio dei test rossi

`MT-4GNU` ha come gate di chiusura: *«`python -m pytest tests/rossi/ -v` gira e **fallisce** come deve, **sei casi su sei**»*. Aggiungere un settimo rosso in quella cartella fa uscire «sette su sette» e **il gate di chiusura letterale non torna**. Riparazione: il rosso di `transizioni` va in `tests/rossi/s3/`, non in `tests/rossi/`, e la micro-task di S2 resta a sei. **Segnalato perché è esattamente il tipo di dettaglio che rompe una dichiarazione di chiusura, e vale un minuto adesso contro mezz'ora dopo.**

---

### AP-033 — Il regalo che non deve esistere ancora (nona costante)

**Fonte:** `ANATOMIA-DEI-LANCI.md` Parte XI, cattura 59, verbatim:

> *«Una leva nuova, distinta dal voucher: "Accesso istantaneo a 4 corsi di Andrei Pascu. Sconto di €199 su Funnel Operator alla sua uscita." — uno sconto **bloccato su un prodotto che non è ancora uscito**. Costo marginale zero per lui oggi, motivo concreto per restare nella sua lista fino al prossimo lancio. Va aggiunto come nona costante accanto alle otto di Parte V: **il regalo non deve per forza esistere già — può essere un'opzione su un lancio futuro.**»*

#### 3.12 La trappola da non cadere dentro, e il motivo per cui va detta prima

`03-FLUSSO-OFFERTA.md` §9 difetto 4 registra la riparazione più importante della versione 4:

> *«Il rapporto valore/prezzo era auto-soddisfacibile con bonus inventati […] Il modo più rapido per arrivare a 3 era aggiungere una riga: "Bonus: lista di controllo, valore 99 €". Il controllo diventava verde. **Il controllo istruiva a gonfiare.**»*

Un'opzione su un lancio futuro **non ha un prezzo di listino, perché il prodotto non è a listino**. Metterla in `bonus[]` con `fonte_valore: "prezzo-listino-proprio"` è **esattamente la riapertura del difetto 4**, con un vestito nuovo.

**Quindi:** AP-033 si implementa in un campo che **non entra nel calcolo di `valore_dichiarato`**. Se non si può fare così, non si fa.

| Campo | Contenuto |
|---|---|
| **COSA** | Aggiungere a `offerta.schema.json`, dentro `struttura`, un campo **opzionale**: `"opzione_futura": {"type": ["object","null"], "additionalProperties": false, "required": ["prodotto", "valore_promesso", "condizione", "scadenza_impegno"], "description": "Un'opzione su un prodotto NON ancora a listino. NON entra in valore_dichiarato né in rapporto_valore_prezzo: un prodotto che non esiste non ha un prezzo verificabile, e contarlo riaprirebbe il difetto 4 della versione 3 (bonus inventati che rendono verde il controllo). Vale come motivo per restare nella lista, non come valore d'offerta.", "properties": {"prodotto": {"type":"string"}, "valore_promesso": {"type":"number"}, "condizione": {"type":"string"}, "scadenza_impegno": {"type":"string","format":"date"}}}` |
| **DOVE** | `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/schemi/offerta.schema.json`, dentro `properties.struttura.properties` |
| **PIÙ** | Estendere `GATE-OFF-1.criterio_eseguibile` con: `AND struttura.opzione_futura NON contribuisce a valore_dichiarato` — e il test rosso: *«un'offerta il cui valore_dichiarato include il valore_promesso di opzione_futura deve BLOCCARE»* |
| **PIÙ** | **L'impegno va onorato.** Riga in `ART-DBR.schemi[]` alla chiusura del lancio: `{"testo": "Il lancio manuale-cc-2026 ha promesso <valore_promesso> € di sconto su <prodotto> alla sua uscita. L'impegno vale fino a <scadenza_impegno>.", "forza": "regola", "si_applica_quando": "si apre il lancio di <prodotto>"}`. **Zero modifiche allo schema debrief** — `schemi[]` esiste già con `si_applica_quando` |
| **PIÙ** | Riga gemella in `company/Memory/BACKLOG.md`, perché il debrief lo legge solo chi apre il lancio successivo, e potrebbero passare mesi |
| **CHI** | **Gael** (schema + gate + rosso). La **scelta se usarla** su questo lancio è di **Max**, dentro `PU-PREZZO` |
| **QUANDO** | **S2** (`MT-GHZ6`, dove vive `GATE-OFF-1`) per lo schema e il criterio. **S1** (`MT-9ADD`) per la compilazione, se Max la vuole. **S4** (`MT-69CE`) per la riga di debrief |
| **PERCHÉ** | `ANATOMIA-DEI-LANCI.md` Parte XI, sopra. Nel caso concreto del Manuale l'opzione futura ha un candidato ovvio: `{"prodotto": "Claude Code Mastery", "valore_promesso": 100, "condizione": "chi ha comprato il Manuale, all'apertura del lancio Mastery", "scadenza_impegno": "..."}` — e si incastra esattamente con AP-004 |
| **EFFORT** | **T2** (schema) + **T1** (le righe) |
| **CORSIA** | **C2** |

#### 3.13 Cosa blocca

> Il campo è **opzionale**. Un'offerta senza `opzione_futura` passa `GATE-OFF-1` esattamente come oggi. **Blocca zero.** Il nuovo criterio blocca solo l'uso disonesto del campo, cioè un caso che oggi non può nemmeno esistere.

---

## 4. FAMIGLIA B — CIÒ CHE I 33 CANDIDATI NON HANNO CATTURATO

23 azioni nuove, numerate in continuità: **AP-034 → AP-060**.

---

### 4.1 Blocco 1 — IL GATE CHE NON C'È (priorità massima)

---

#### AP-034 — `catena.py`: gli otto controlli di ADR-024 diventano un programma

| Campo | Contenuto |
|---|---|
| **COSA** | Uno script nuovo, `catena.py`, che prende un file di manifesto (elenco di URL con ruolo) e implementa gli **otto controlli di ADR-024 §4**, in quest'ordine di valore: **(8)** ogni CTA verso pagina interna risponde 200, e ogni pagina di cassa ha almeno un link entrante — **più l'estensione AP-032**: i link del footer si verificano **una volta alla fonte**, non pagina per pagina. **(7)** il corpo del prezzo effettivo ≥ corpo del testo di servizio (FAQ, note, legale). **(6)** nessun prezzo/scadenza/garanzia dentro un'immagine con `alt` vuoto. **(3)** `og:image` uguale su più pagine con `meta.description` diversa. **(5)** anni scritti a mano nel copy → WARN con numero di riga. **(1)** prodotto one-shot il cui bottone porta dritto al pagamento senza pre-cassa → FAIL salvo deroga dichiarata. **(2)** accento oltre soglia → WARN col conteggio. **(4)** campo editabile che non entra nel calcolo mostrato → FAIL |
| **DOVE** | `.claude/skills/fabbrica-siti/scripts/catena.py` — **lì e non dentro LANCI**, perché ADR-024 §4 dichiara quel gate come parte della Fabbrica (Fase 4) e ADR-003 vieta di riscrivere ciò che ha già una casa. LANCI lo **invoca**, non lo duplica |
| **INTERFACCIA** | `python catena.py --manifesto <file.json> [--solo <url>] [--json]`. Exit 0 = tutti PASS. Exit 1 = almeno un FAIL. Exit 2 = errore d'esecuzione. Le WARN non cambiano il codice d'uscita, si scrivono |
| **CHI** | **Qualunque sessione.** Non tocca un solo file di Gael |
| **QUANDO** | **Subito, in parallelo a S0.** Non ha nessuna dipendenza da S0, S1 o S2. È l'azione a più alto rendimento del piano intero |
| **PERCHÉ** | ADR-024 §4 controllo 8, e la sua giustificazione misurata: *«Un lancio con una pagina di vendita viva e una cassa irraggiungibile perde ogni euro che il copy ha guadagnato, e nessuno se ne accorge perché la pagina di vendita funziona benissimo.»* E `ANATOMIA-DEI-LANCI.md` Parte IX passo 12: *«Il passo 12 non è l'ultimo per caso: è il solo che, se salta, annulla gli altri undici.»* |
| **EFFORT** | **T3** — 4-8 h. I controlli 8, 3, 5 sono banali (HTTP + parsing). I controlli 7 e 2 richiedono di leggere gli stili calcolati: si fanno con Playwright, che è già in casa |
| **CORSIA** | **C1 — LIBERA** |
| **BLOCCA** | **Niente.** Oggi il controllo 8 non esiste; domani esiste. Non toglie nessuna strada, ne apre una. La sua assenza blocca esattamente una riga: la possibilità di dichiarare `VE-1` completo *con il controllo 8 incluso* |

> **Nota di scoping ADR-028 punto 4:** questo script **non deve** diventare un prerequisito di `GATE-FNL-1` prima di esistere e di essere stato eseguito almeno una volta senza falsi positivi. `04-COSTRUZIONE.md` §9 lo dice per un caso analogo: un controllo che sbaglia spesso *«viene derogato al primo lancio»*, e a quel punto è peggio di non averlo.

---

#### AP-035 — La pre-cassa diventa un generatore a sei variabili, non una pagina

| Campo | Contenuto |
|---|---|
| **COSA** | Uno script `pre_cassa.py` che prende **le sei variabili misurate** e sputa la pagina: `nome_prodotto`, `prezzo`, `colore_accento`, `porzione_colorata_del_nome`, `codice_sconto` (opzionale, **con finestra di validità obbligatoria**), `testo_bottone`. Deve emettere `<meta name="robots" content="noindex, nofollow">` **sempre**, e rifiutarsi di generare se `codice_sconto` è presente senza `finestra_validita` |
| **DOVE** | `.claude/skills/fabbrica-siti/pattern/pre-cassa/genera.py`, accanto a `pattern.html` e `scheda.md` che **esistono già** |
| **CHI** | **Qualunque sessione** |
| **QUANDO** | Prima di **S3** (`MT-GEKH`), perché è lì che il funnel si costruisce. Ma è indipendente: si può fare oggi |
| **PERCHÉ** | `SINTESI-METODO.md` §4: *«Sei variabili in tutto […] È un generatore, non una pagina.»* E «LE CINQUE COSE DA RUBARE SUBITO» #1: *«Lo stampo di pre-cassa a sei variabili — generabile a comando, già pattern nella Fabbrica.»* **Il pattern c'è; il comando no** |
| **EFFORT** | **T2** — il `pattern.html` esiste già, si tratta di parametrizzarlo |
| **CORSIA** | **C1** |
| **BLOCCA** | Niente. Senza generatore la pre-cassa si scrive a mano dal pattern, come oggi |

---

#### AP-036 — Il secondo stampo di cassa che manca: `cassa-corso-a-livelli`

| Campo | Contenuto |
|---|---|
| **COSA** | Un pattern nuovo, `cassa-corso-a-livelli`: **due card affiancate**, ciascuna con una checklist a spunta quasi identica e **una sola riga che cambia** fra le due, nessuno sconto e nessun codice — la leva è la scelta fra due piani, non il prezzo |
| **DOVE** | `.claude/skills/fabbrica-siti/pattern/cassa-corso-a-livelli/{pattern.html,scheda.md}`. Poi `python .claude/skills/fabbrica-siti/scripts/galleria.py` (ADR-024 §6: *«i pattern nuovi portano la galleria da 8 a 10: `galleria.py` va rilanciato […] o la galleria diventa un puntatore stale»*) |
| **CHI** | Qualunque sessione |
| **QUANDO** | **Non serve al primo lancio** se il Manuale ha un prezzo unico. Serve al lancio **Mastery** (AP-004) se avrà due piani. **Priorità bassa, effort basso** |
| **PERCHÉ** | `SINTESI-SISTEMA-COPY.md` §3: *«`cassa-corso-a-livelli` (2 usi: Copywriting Mentorship BASE/COMPLETO): niente sconto, niente codice — la leva è la scelta fra due piani mostrati come due card affiancate, ciascuna con una checklist a spunta (✓) quasi identica e una sola riga che cambia fra le due.»* Due usi = pattern, per §10 di `CLAUDE-SITI.md`. **Il DELTA ALLA FABBRICA lo chiede esplicitamente e non è mai stato fatto** |
| **EFFORT** | **T2** |
| **CORSIA** | **C1** |
| **BLOCCA** | Niente |

---

### 4.2 Blocco 2 — LA LIBRERIA DI COPY CHE NON ESISTE

---

#### AP-037 — La libreria di frasi riusabili di LANCI

| Campo | Contenuto |
|---|---|
| **COSA** | Una cartella `copy/libreria/` **condivisa fra i lanci**, non dentro un lancio. Ogni voce è un file: originale (se viene da fuori, con la fonte), versione a placeholder, quando si usa, quando **non** si usa |
| **DOVE** | `company/Ecosistemi/15-LANCI/copy/libreria/` — **fuori da `lanci/<id>/`**, perché il punto è che sopravviva al lancio |
| **CHI** | **Gael** per la cartella (è dentro il suo perimetro C2); **qualunque sessione** per popolarla, perché sono file nuovi che non collidono |
| **QUANDO** | La cartella in **S3** (`MT-GEKH`, quando nasce `copy/`). Il popolamento: in qualunque momento |
| **PERCHÉ** | `SINTESI-METODO.md` §4: *«lui non riscrive mai da zero ciò che ha già funzionato una volta. Ha una libreria — di pagine, di blocchi e di frasi — anche se non la chiama così.»* Con la prova misurata: *«"Lavori da solo? Vale lo stesso. Al posto del team, il vincolo sei tu." compare identico, carattere per carattere, su `/servizi` e `/consulenza`»* |
| **EFFORT** | **T2** per la struttura |
| **CORSIA** | **C2** (cartella) + **C1** (contenuto) |
| **BLOCCA** | Niente. `ART-CPY` non la richiede |

---

#### AP-038 — Le 22 formule retoriche entrano nella libreria pattern

| Campo | Contenuto |
|---|---|
| **COSA** | Le **22 costruzioni verificate testualmente** di `SINTESI-SISTEMA-COPY.md` §2, ognuna già nel formato «originale con coordinata + versione a placeholder», diventano 22 file della libreria. **Sono già scritte: si spostano, non si riscrivono.** Tre vanno marcate con un avvertimento operativo: la **#22** (*«No, non sei tu che sei sfortunato. Sei disinformato.»*) è dichiarata dalla fonte stessa come *«Barnum puro»*; la **#9** e la **#18** sostituiscono la garanzia con una frase-manifesto — e `SINTESI-SISTEMA-COPY.md` «COSA DOBBIAMO FARE MEGLIO DI LUI» impone: *«Sempre una politica di rimborso reale, non solo una frase-manifesto come sostituto»* |
| **DOVE** | `company/Ecosistemi/15-LANCI/copy/libreria/formule/01..22.md` |
| **CHI** | Qualunque sessione |
| **QUANDO** | Indipendente. Utile **prima di S3**, perché `PA-3` («scrittura dei pezzi») è dove servono |
| **PERCHÉ** | `SINTESI-SISTEMA-COPY.md` DELTA ALLA FABBRICA / PATTERN: *«le 22 formule del §2 diventano 22 voci della libreria pattern di copy riusabile, ciascuna già nel formato originale+placeholder pronto per essere ripreso da `pattern-builder`»*. **Chiesto esplicitamente, mai fatto, e nessuno dei 33 candidati lo copre** |
| **EFFORT** | **T2** — è travaso, non scrittura |
| **CORSIA** | **C1** |
| **BLOCCA** | Niente |

---

#### AP-039 — La formula a 11 tappe diventa la griglia di punteggio di `GATE-CPY-1`

| Campo | Contenuto |
|---|---|
| **COSA** | Per ogni `pezzo` di `tipo: "pagina-vendita"`, i `punteggio.blocchi[]` sono **le undici tappe misurate**, in quest'ordine: `hero`, `agitazione`, `prova-con-fonte`, `rivelazione-del-metodo`, `benefici`, `curriculum`, `qualificazione-negativa`, `obiezioni`, `autorevolezza`, `prezzo`, `faq` — più la dodicesima non persuasiva, `chiusura-legale`, che è **presenza/assenza** e vale zero punti ma la cui assenza è un FAIL. Ogni blocco dichiara `assegnato_da` (`calcolo` per presenza/lunghezza, `giudice` per qualità) e **`ancora`**, che lo schema ha già e nessuno riempie: *«senza ancore, due giudici danno voti diversi allo stesso testo»* |
| **DOVE** | Nessuna modifica a `copy.schema.json` — `blocchi[]` è già libero. La griglia va **dichiarata**, e il posto giusto è il registro, `WF-PAROLA` fase `PA-4` («punteggio»), campo nuovo `griglia_dichiarata` |
| **CHI** | **Gael**, dentro `MT-GEKH` |
| **QUANDO** | **S3** |
| **PERCHÉ** | `SINTESI-SISTEMA-COPY.md` §1: *«una formula fissa a 11 tappe […] Chi la fa tutta: la famiglia "out*" […] e Vendita101 attraversano tutte e 11 le tappe in ordine»*. E §8 regola 10 sulla dodicesima: *«Il footer legale è l'unica tappa che non devia mai, nemmeno sulle pagine che rompono tutto il resto»* — con la nota che la sua **unica assenza misurata** è su una pagina di Digital Empire, non sua (`40-43-44-pagine-anomale.md`). **È la nostra pagina che ha il difetto, non la sua.** Oggi `GATE-CPY-1` pretende `punteggio_totale >= 80` e *«nessun blocco sotto il 50% dei propri punti»* senza dire quali siano i blocchi: **il gate è tarato su una griglia che non esiste** |
| **EFFORT** | **T2** |
| **CORSIA** | **C2** |
| **BLOCCA** | Nulla di nuovo. `GATE-CPY-1` blocca già. Questa azione gli dà finalmente qualcosa contro cui misurare |

---

#### AP-040 — Il tipo di prova si sceglie dalla concretezza del prodotto

| Campo | Contenuto |
|---|---|
| **COSA** | Campo nuovo, obbligatorio, in `copy.schema.json` a livello di `pezzo`: `"concretezza": {"enum": ["strumento-tecnico", "percorso", "mindset"]}`. Regola conseguente, in `GATE-CPY-1`: `strumento-tecnico` → almeno una `affermazione` di categoria `prova` con `riferimento` risolvibile; `mindset` → **almeno una fonte esterna verificabile comunque**, che è precisamente dove noi facciamo meglio di lui |
| **DOVE** | `dati/schemi/copy.schema.json` + `criterio_eseguibile` di `GATE-CPY-1` |
| **CHI** | **Gael** |
| **QUANDO** | **S3** (`MT-GEKH`) |
| **PERCHÉ** | `SINTESI-SISTEMA-COPY.md` §1, la legge misurata: *«quando il prodotto è verificabile (uno strumento, un metodo con passi), le prove sono esterne e puntuali; quando il prodotto è un mindset, le prove esterne spariscono e il loro posto è preso da diagnosi universali che sembrano su misura per chiunque le legga — l'effetto Barnum sostituisce la fonte.»* E il DELTA: *«il criterio del §1 diventa un campo obbligatorio nel brief di ogni nuova pagina prodotto»*. Il Manuale Claude Code è `strumento-tecnico`: **le prove devono essere esterne e puntuali, e questo è verificabile** |
| **EFFORT** | **T2** |
| **CORSIA** | **C2** |
| **BLOCCA** | `GATE-CPY-1` soltanto, e solo dopo la modifica |

---

#### AP-041 — La scala prova/prezzo: più sale il prezzo, più servono fonti (non più obiezioni)

| Campo | Contenuto |
|---|---|
| **COSA** | Soglia dichiarata in `GATE-CPY-1`, parametrizzata come `soglia_rapporto_minima` di `offerta.schema.json` (stessa disciplina: parametro, non costante sparsa): **prezzo < 150 €** → almeno 0 fonti esterne; **150-400 €** → almeno 2; **> 400 €** → almeno 5, **e almeno una prova sociale con faccia e nome** |
| **DOVE** | `dati/registro.yaml`, `GATE-CPY-1.criterio_eseguibile`, più un blocco `parametri:` nuovo per tenere i numeri fuori dai criteri |
| **CHI** | **Gael** |
| **QUANDO** | **S3** |
| **PERCHÉ** | `ANATOMIA-DEI-LANCI.md` Parte IV, misurato: outHeadline 98 € → 0 fonti · Vendita101 400 € → 2 · Copy Mentorship 999 € → 5. E la citazione diretta del teardown: *«Più sale il prezzo, meno regge l'argomento "non ho testimonianze ma ho i dati". A 98 € puoi permetterti di posare; a 999 € ti servono facce.»* Con la nota che *«la prova sociale vera compare solo sopra i 349 €»*. **Questo decide direttamente se il Manuale a 27-47 € ha bisogno di testimonianze — che non abbiamo — o no.** Alla fascia tripwire di AP-004: **no**. È un argomento economico a favore del prezzo basso che nessuno aveva messo sul tavolo |
| **EFFORT** | **T2** |
| **CORSIA** | **C2** |
| **BLOCCA** | Niente sul primo lancio, per costruzione: alla fascia tripwire la soglia è zero |

---

### 4.3 Blocco 3 — DUE ARTICOLI NUOVI DELLA LEGGE DELLA FABBRICA

> **Entrambi richiedono un ADR nuovo.** `CLAUDE-SITI.md` è esplicito: *«Non si cambia in una conversazione. Si cambia con un ADR.»* Proposta: **ADR-029 — Canone v2, secondo strato: cosa entra dall'onda G**. E il precedente c'è già: ADR-024 ha fatto la stessa cosa per le onde A e B.

---

#### AP-042 — §13: la piattaforma si sceglie dalla vita del pezzo

| Campo | Contenuto |
|---|---|
| **COSA** | Articolo **§13** di `CLAUDE-SITI.md`, testo proposto per intero: *«**§13 — La piattaforma si sceglie dalla vita del pezzo.** Prima della corsia (§5) si decide la **durata**. Permanente e mutevole (un negozio, un catalogo che cambia spesso) → piattaforma, zero manutenzione propria. **Finestra breve con una cassa sola** (un lancio) → artigianale, controllo totale. **Cliente che è un'azienda** → artigianale con kit condiviso: nessuna sezione scrive stili propri. La disciplina cresce col valore del cliente, non col prezzo del prodotto. Origine: 44 pagine su piattaforma contro 7 artigianali, misurate il 2026-09-07/09; il `custom.css` del negozio pesa 1.183 byte su 3,6-8,2 MB scaricati — lo 0,02% — e di sei regole solo due sono vive. La personalizzazione visiva su una piattaforma è il lavoro a più basso rendimento che esista.»* |
| **DOVE** | `.claude/skills/fabbrica-siti/CLAUDE-SITI.md`, dopo §12 |
| **CHI** | Qualunque sessione scrive l'ADR e l'articolo. **Max firma l'ADR** |
| **QUANDO** | Indipendente da S0-S5. Utile prima di **S3**, dove si sceglie come costruire il funnel |
| **PERCHÉ** | `SINTESI-METODO.md` DELTA ALLA FABBRICA / CANONE, verbatim: *«Un articolo nuovo, che nasce da §1 di questo documento: la piattaforma si sceglie dalla vita del pezzo […] **È già metà di ADR-023 (due corsie): questo lo completa con il criterio della durata, che ci mancava.**»* |
| **EFFORT** | **T1** (l'articolo) + **T2** (l'ADR) + **T4** (la firma) |
| **CORSIA** | **C1** |
| **BLOCCA** | **Niente**, e c'è il precedente esatto: ADR-024 §6 dichiara che finché il gate non esiste, *«§11 e §12 valgono come legge letta dagli agenti, non come blocco automatico»*. §13 e §14 nascono nello stesso regime. **La firma di Max non ferma nessuno: si applica intanto, si firma quando si firma** |
| **AMENDMENT** | **Estende ADR-023, non lo contraddice.** Va scritto in ADR-029 nella forma «Sostituisce: niente. **Estende** ADR-023» — identica a come ADR-024 estende ADR-023 |

---

#### AP-043 — §14: la forma della pagina si decide dalla temperatura del traffico, non dal prezzo

| Campo | Contenuto |
|---|---|
| **COSA** | Articolo **§14**: *«**§14 — La temperatura del traffico governa la forma.** Non il prezzo. Pagina **fredda** (il lettore non ha ancora deciso): sotto i 2.000 px, una sezione, **una decisione sola**. Pagina **calda** (il lettore sta valutando): lunga quanto serve, con **una CTA ogni ~1.100 px**. Origine misurata su 42 pagine: gradini ≤2.200 px → 1.593 px medi, 36 blocchi, 4,9 CTA; pagine di vendita ≥9.000 px → 17.531 px medi, 252 blocchi, 16,2 CTA. Undici volte l'altezza, sette volte i blocchi, tre volte le CTA. Correzione a una nostra affermazione precedente: il prodotto da 98 € e quello da 999 € hanno praticamente la stessa altezza (26.993 contro 26.952 px). **Quello che sale col prezzo non è la lunghezza: è la densità di prova.** E il carattere si dichiara sempre: un `sans-serif` implicito è un'identità regalata al browser, e il canone ha già Onest.»* |
| **DOVE** | `.claude/skills/fabbrica-siti/CLAUDE-SITI.md`, dopo §13 |
| **CHI/QUANDO/CORSIA** | come AP-042 |
| **PERCHÉ** | `SINTESI-SISTEMA-VISIVO.md` §5 e DELTA / CANONE: *«Un articolo nuovo da §5 […] E da §2: il carattere si dichiara sempre»*. Con la misura di correzione al §4: *«Con dieci pagine a prezzo noto, la relazione non regge»* |
| **EFFORT** | **T1** dentro lo stesso ADR-029 |
| **BLOCCA** | Niente, stesso regime di §11/§12 |

---

#### AP-044 — I cinque controlli di gate che ADR-024 non ha (controlli 9-13)

Cinque controlli nuovi per `catena.py` (AP-034), tutti nati da difetti **misurati**, non da teoria — la stessa regola dei quattro strati che ha prodotto i controlli 3-8.

| # | Controllo | Esito | Fonte |
|---|---|---|---|
| **9** | **Densità di immagini per 1.000 px > 5,0** | WARN | `SINTESI-SISTEMA-VISIVO.md` DELTA/GATE: *«Sopra 5,0 la pagina si sta riempiendo di figure invece che di argomenti. Le sue pagine peggiori per verificabilità (`51-recensioni-mentorship`, 8,1 — 42 screenshot muti) sono anche le più dense»* |
| **10** | **Un bundle esce senza la scomposizione del prezzo visibile** | FAIL | `SINTESI-SISTEMA-COPY.md` DELTA/GATE (1) e §8 regola 7: *«784€ Armageddon non è mai spiegato come 139+98+98+250+199: il totale compare come blocco unico»*. E: *«Mostrare 139+98+98+250+199=784 costa una riga e vale fiducia»* |
| **11** | **Una «recensione verificata» senza link a fonte esterna, o un'immagine-prova con `alt` vuoto** | FAIL | DELTA/GATE (2) + «COSA DOBBIAMO FARE MEGLIO DI LUI»: *«42 screenshot su 42 con `alt=""` […] sono un difetto misurato di accessibilità e di verificabilità insieme»* |
| **12** | **Un codice sconto scritto a mano nel testo invece che letto da un file di configurazione** | FAIL | DELTA/GATE (3): *«ogni codice sconto vive in un solo file di configurazione, mai ripetuto a mano nel testo di ogni pagina»*. Difetto misurato: *«CWSHOP e 20% ricorrono identici, carattere per carattere, su cinque prodotti diversi — segno di un file di configurazione unico copiato, non riscritto»* |
| **13** | **Discrepanza di naming interno non riconciliata** | WARN | «COSA DOBBIAMO FARE MEGLIO DI LUI»: *«"outViral" contro "outViral 2" nella stessa pagina Armageddon non viene mai notata né spiegata — un controllo di coerenza terminologica va nel gate di pubblicazione, non lasciato al caso»*. E il difetto gemello: `<title>` «Armageggon» contro URL «armadeggon» |

| Campo | Contenuto |
|---|---|
| **DOVE** | `.claude/skills/fabbrica-siti/scripts/catena.py` + registrati in **ADR-029** |
| **CHI** | Qualunque sessione |
| **QUANDO** | Insieme ad AP-034, o subito dopo |
| **EFFORT** | **T2** aggiuntivo su AP-034 (9, 12, 13 sono banali; 10 e 11 richiedono parsing) |
| **CORSIA** | **C1** |
| **BLOCCA** | Niente — non esistono oggi |

---

### 4.4 Blocco 4 — IL LANCIO VERO: ciò che va deciso e scritto per il Manuale

---

#### AP-054 — L'obiezione che il concorrente non nomina mai, e che noi dobbiamo nominare

| Campo | Contenuto |
|---|---|
| **COSA** | Una riga in `ricerca.json` → `frasi[]` con `categoria: "obiezione"`, e **una tappa obbligatoria** nella griglia AP-039 (`obiezioni`) dedicata a: *«perché dovrei pagare per imparare Claude Code se la documentazione è gratis»* |
| **DOVE** | `company/Ecosistemi/15-LANCI/lanci/manuale-cc-2026/ricerca.json` e `copy/` |
| **CHI** | **Gael** (`MT-9ADD` per la ricerca, `MT-GEKH` per il copy) |
| **QUANDO** | **S1** per la ricerca, **S3** per il testo |
| **PERCHÉ** | `ANATOMIA-DEI-LANCI.md` Parte VII, ultima riga, verbatim: *«**Non nomina mai l'obiezione più ovvia del suo corso su Claude** ("lo imparo gratis dalla documentazione"): non compare né nel copy né nelle FAQ.»* Il suo `claude-speedrun.com` è **33.756 px, 34 sezioni, 473 blocchi, 40 CTA — la pagina più grande di tutto il suo ecosistema** (`SINTESI-SISTEMA-VISIVO.md` §4) — e in tutto quello spazio l'obiezione centrale non c'è. **È il buco più grande e più economico da colpire dell'intero studio, ed è un buco su un prodotto in competizione diretta col nostro.** Non era in nessuno dei 33 candidati |
| **EFFORT** | **T1** |
| **CORSIA** | **C2** |
| **BLOCCA** | Niente |

---

#### AP-055 — Il concorrente diretto entra nel registro della ricerca

| Campo | Contenuto |
|---|---|
| **COSA** | In `ricerca.json` → `concorrenti[]` (campo che **esiste già**, con `nome`, `prezzo`, `fonte_prezzo`, `cosa_non_copre`): la riga `{"nome": "Claude Speedrun 2 — Andrei Pascu", "prezzo": 249, "fonte_prezzo": "https://claude-speedrun.com", "cosa_non_copre": "l'obiezione 'lo imparo gratis dalla documentazione', mai nominata né nel copy né nelle FAQ su 33.756 px e 473 blocchi — misurato 2026-09-07/09"}` |
| **DOVE** | `.../manuale-cc-2026/ricerca.json` |
| **CHI** | **Gael**, `MT-9ADD` |
| **QUANDO** | **S1** |
| **PERCHÉ** | `03-FLUSSO-OFFERTA.md` §O2, regola: *«un prezzo proposto senza guardare i prezzi che l'azienda si è già data non è istruito»* — e lo stesso vale per il prezzo del concorrente diretto. Il Manuale ha quattro prezzi interni mai riconciliati **e nessuno ha mai messo sul tavolo il prezzo del prodotto concorrente**, che è 249 € |
| **EFFORT** | **T1** — quattro righe di JSON |
| **CORSIA** | **C2** |
| **BLOCCA** | Niente. `concorrenti[]` non è in `required` |

---

#### AP-056 — Il funnel di casa già scritto e mai lanciato si recupera, non si riscrive

| Campo | Contenuto |
|---|---|
| **COSA** | Prima di costruire `ART-FNL`, **aprire e censire** `chiamata-formazione.netlify.app` — 18.770 px, 25 sezioni, 506 blocchi — e decidere per iscritto quali sezioni si riusano. Le sezioni riusate entrano in `copy/libreria/` (AP-037), non copiate dentro un lancio |
| **DOVE** | Censimento in `.../manuale-cc-2026/`; il riuso in `copy/libreria/` |
| **CHI** | **Gael**, `MT-GEKH`. Precondizione: la pagina deve essere ancora raggiungibile — **da verificare, e se non lo è, si prende dalla cattura dello studio** |
| **QUANDO** | **S3**, prima di `VE-1` |
| **PERCHÉ** | `ANATOMIA-DEI-LANCI.md` Parte X punto 5, verbatim: *«**Un funnel nostro già scritto e mai lanciato**: `chiamata-formazione.netlify.app` — call 1:1 gratuita verso "Claude Code Mastery" a 397 €, 18.770 px, 25 sezioni, 506 blocchi, ferma su uno staging. **Era censita per errore fra le pagine del concorrente.**»* Più ADR-003 (wrap, mai riscrittura) e ADR-016 (25 pezzi finiti mai usciti). E il passo 1 del modello a 12 passi: *«mai costruire prodotto nuovo per un lancio»* |
| **EFFORT** | **T2** (censimento) |
| **CORSIA** | **C2** |
| **BLOCCA** | Niente. Se la pagina non è raggiungibile, si costruisce da zero e la riga va in `BACKLOG.md` |

---

#### AP-057 — La pagina di consegna è un artefatto del lancio, non un dopo-lancio

| Campo | Contenuto |
|---|---|
| **COSA** | Rendere obbligatoria, in `GATE-FNL-1`, la presenza di **almeno una pagina con `ruolo: "consegna"`** in `funnel.json.pagine[]` (il valore è **già nell'enum**, non serve toccare lo schema), con il proprio `evento_conversione`. Più, dentro AP-034/`catena.py`, la regola AP-031: **il colore di brand sta sulla CTA che converte, mai sul messaggio di sistema — anche nella pagina di consegna** |
| **DOVE** | `dati/registro.yaml`, `GATE-FNL-1.criterio_eseguibile` + `catena.py` controllo 2 esteso |
| **CHI** | **Gael** (il criterio) + qualunque sessione (il controllo) |
| **QUANDO** | **S3** |
| **PERCHÉ** | `ANATOMIA-DEI-LANCI.md` Parte XI: la consegna di Armageddon vive **su un dominio diverso** da quello del lancio, e *«l'unico uso del blu di brand (`#0062ff`) in tutta la pagina di consegna è sul bottone che chiude l'avviso "Stiamo aggiornando il brand" — non sul bottone "Iscriviti", grigio su nero, zero accento. **Il colore che dovrebbe guidare all'accesso guida invece a scusarsi.**»* E il dead-end del footer che **si propaga ovunque il footer sia incluso**. La consegna è dove vive AP-033 (l'opzione futura): se la pagina non è nel funnel, l'opzione futura non ha un posto dove essere letta |
| **EFFORT** | **T1** (criterio) + **T1** (controllo) |
| **CORSIA** | **C2** + **C1** |
| **BLOCCA** | `GATE-FNL-1` soltanto, e solo dopo la modifica. **Attenzione:** il gate esistente richiede `evento_conversione` con `prova.origine` su **ogni** pagina — su una pagina di consegna dietro login questo può essere impossibile. **Se lo è, si dichiara `non_misurato` (campo che lo schema ha già) invece di rendere il gate insoddisfacibile.** È esattamente il difetto che `04-COSTRUZIONE.md` §9 chiama «un controllo che sbaglia spesso viene derogato al primo lancio» |

---

#### AP-058 — Il percorso freddo costa 86 parole: è un parametro, non un aneddoto

| Campo | Contenuto |
|---|---|
| **COSA** | In `WF-PAROLA` fase `PA-1` («inventario dei pezzi»), criterio d'uscita esteso: i pezzi di `tipo: "pagina-cattura"` sul percorso freddo hanno un **tetto di parole dichiarato**, e la somma del percorso freddo si scrive nel manifesto |
| **DOVE** | `dati/registro.yaml`, `WF-PAROLA.fasi[PA-1].criterio_uscita` |
| **CHI** | **Gael** |
| **QUANDO** | **S3** |
| **PERCHÉ** | `ANATOMIA-DEI-LANCI.md` Parte III: *«**86 parole** di contenuto vero portano dall'apertura di `/define` al clic d'acquisto. Una singola pagina di vendita ne usa **1.140-1.560**. Il funnel è **tredici-diciotto volte più economico** in parole della pagina che convince.»* E la riga che vale il viaggio, un `h3` da 38,4 px: *«Ti consiglio di vedere e finire il video prima di cliccare il pulsante per capirne i contenuti.»* — *«Non è cortesia: è controllo del consumo. Chi arriva al bottone ha già visto il video, quindi clicca sapendo cosa compra. Meno rimborsi, meno assistenza, click di qualità più alta»* |
| **EFFORT** | **T1** |
| **CORSIA** | **C2** |
| **BLOCCA** | Niente |

---

#### AP-051 — L'ancora prima del prezzo, e la domanda di auto-stima

| Campo | Contenuto |
|---|---|
| **COSA** | In `offerta.json` → `struttura.ancoraggio` (campo che **esiste già** ed è opzionale), rendere il contenuto un **blocco di libreria**, non testo libero: la domanda di auto-stima del valore prima del reveal. Formula #5 della libreria AP-038 come alternativa per prodotti a basso ticket: *«Avere [PRODOTTO] è come avere [RISORSA UMANA EQUIVALENTE]… ma costa solo [CIFRA] al mese»* |
| **DOVE** | `copy/libreria/ancore/` + `struttura.ancoraggio` |
| **CHI** | **Gael** (`MT-9ADD`) |
| **QUANDO** | **S1** |
| **PERCHÉ** | `SINTESI-SISTEMA-COPY.md` §8 regola 1: *«Il prezzo si ancora prima di rivelarsi, mai il contrario»*, con la misura: *«Sulla Mentorship, il lettore stima da solo il valore ("quanto pagheresti?") prima che compaiano le cifre BASE €349 / COMPLETO €999»* [y=198]. E DELTA/CANONE: *«adottare la domanda di auto-stima del valore ("quanto pagheresti?") come blocco fisso immediatamente prima di ogni reveal di prezzo su prodotti ad alto ticket»* |
| **EFFORT** | **T1** |
| **CORSIA** | **C2** |
| **BLOCCA** | Niente — il campo è opzionale |

---

#### AP-052 — Il rifiuto esplicito della tecnica manipolativa è un argomento di vendita — e diventa un vincolo del gate

| Campo | Contenuto |
|---|---|
| **COSA** | Estendere `GATE-OFF-1.criterio_eseguibile` con: `AND struttura.motivo_per_agire_adesso cita esplicitamente data_chiusura`. Il campo esiste già e ha la descrizione giusta (*«una scadenza vera, mai "affrettati"»*) ma **nessun controllo la applica**. Test rosso: *«un'offerta con `motivo_per_agire_adesso: "affrettati, i posti sono limitati"` deve BLOCCARE»* — e blocca due volte, perché viola anche la costante 7 |
| **DOVE** | `dati/registro.yaml`, `GATE-OFF-1` |
| **CHI** | **Gael**, `MT-GHZ6` (S2) e `MT-4GNU` per il rosso |
| **QUANDO** | **S2** |
| **PERCHÉ** | `SINTESI-SISTEMA-COPY.md` §8 regola 3: *«Il rifiuto esplicito di una tecnica manipolativa è esso stesso un argomento di vendita»*, misurato: *«"Nessun impegno. Niente countdown finti." [y=11200] e l'elenco dei "Timer finti" fra le tecniche Black Hat da evitare [y=11183] trasformano un'assenza in una dichiarazione di fiducia»*. E `ANATOMIA-DEI-LANCI.md` Parte V costante 7. **Il concorrente è coerente su questo punto** (`ANDREI-PASCU-DOSSIER-COMPLETO.md` §6): non è un difetto da superare, è una cosa da eguagliare |
| **EFFORT** | **T1** + **T1** (rosso) |
| **CORSIA** | **C2** |
| **BLOCCA** | `GATE-OFF-1`. **Ma solo su un'offerta che dichiari una scarsità falsa** — un caso che, se si verifica, *deve* bloccare |

---

#### AP-053 — La qualificazione negativa, e a quali prodotti si applica

| Campo | Contenuto |
|---|---|
| **COSA** | Nella griglia AP-039, la tappa `qualificazione-negativa` è **obbligatoria** quando `concretezza == "strumento-tecnico"` e il prodotto è dichiarato avanzato; **assente** quando è un prodotto di massa. La formulazione di libreria, dall'originale misurato: *«Non è per tutti. Sono serio.»* [y=13269] → *«[PRODOTTO] non è per [LIVELLO BASSO]. È [POSIZIONAMENTO ESPLICITO].»* |
| **DOVE** | `copy/libreria/formule/` + griglia in `WF-PAROLA.PA-4` |
| **CHI** | **Gael** |
| **QUANDO** | **S3** |
| **PERCHÉ** | `SINTESI-SISTEMA-COPY.md` §5, con le tre ragioni misurate: pre-qualifica il compratore, *«funziona come leva di esclusività anche su un prodotto digitale a scorta infinita — non essendoci scarsità reale, la qualificazione negativa simula selettività senza ricorrere a scarsità artificiale»*, ed è *«riservata ai soli due prodotti "tecnici avanzati" della famiglia»*. **Decisione concreta per il Manuale:** in configurazione tripwire (AP-004) **non si usa** — un tripwire deve abbassare la resistenza, non alzarla. Si userà sul lancio Mastery |
| **EFFORT** | **T1** |
| **CORSIA** | **C2** |
| **BLOCCA** | Niente |

---

#### AP-060 — Il vincolo sull'upsell entra nel gate dell'offerta

| Campo | Contenuto |
|---|---|
| **COSA** | Promuovere AP-017 (oggi 🟡 «da valutare», target *«check qualitativo per un futuro gate offerte/upsell»*) a criterio di `GATE-OFF-1` sul **secondo** lancio della catena: `AND se il lancio dichiara un lancio precedente nella catena, esiste un campo che afferma che il prodotto precedente resta completo senza questo` |
| **DOVE** | `dati/registro.yaml`, `GATE-OFF-1` |
| **CHI** | **Gael** |
| **QUANDO** | **S2**, ma si attiva solo sul lancio Mastery |
| **PERCHÉ** | outFunnel Lezione 11, KA-05 verbatim: *«l'upsell non deve mai far sembrare il primo acquisto incompleto/mancante — se il cliente percepisce che gli è stata "tolta" una parte del prodotto originale per rivendergliela, si sente ingannato»*. E KA-07(2): *«svalutare il primo acquisto con un secondo prodotto che conteneva informazioni "dovute" già nel primo»*. Il `lesson-analysis.md` stesso annota: *«KA-05 e KA-07(2) sono la stessa regola vista da due angoli […] ripetuto 2 volte con esempi diversi — segnale che l'autore lo considera l'errore più costoso da evitare in un upsell»*. **Con AP-004 questo smette di essere teorico: il Manuale a 27-47 € deve restare un prodotto compiuto anche per chi non compra mai Mastery, e le sue 203 pagine devono bastare da sole** |
| **EFFORT** | **T1** |
| **CORSIA** | **C2** |
| **BLOCCA** | Niente sul primo lancio |

---

### 4.5 Blocco 5 — LA MANUTENZIONE, IL VOCABOLARIO, IL GOVERNO

---

#### AP-050 — Il mirror di lancio è un artefatto vivo e va riconciliato col negozio

| Campo | Contenuto |
|---|---|
| **COSA** | Due righe: (1) in `funnel.json`, un campo `mirror` per ogni pagina specchiata — `{"origine_url": "...", "allineato_il": "<date-time>"}` (**richiede un campo nuovo nello schema**); (2) alla chiusura del lancio, **una riga obbligatoria in `ART-DBR.schemi[]`**: *«Le modifiche fatte alla copia di lancio vanno riportate all'originale entro N giorni dalla chiusura, o è l'originale a invecchiare»*, `forza: "regola"`, `si_applica_quando: "il lancio ha usato il pattern mirror-di-lancio"` |
| **DOVE** | `dati/schemi/funnel.schema.json` + il debrief del lancio |
| **CHI** | **Gael** |
| **QUANDO** | Schema in **S3** (`MT-GEKH`), riga di debrief in **S4** (`MT-69CE`) |
| **PERCHÉ** | `ANATOMIA-DEI-LANCI.md` Mossa 5, con la prova: *«l'originale sul negozio dice "E adesso, nel **2025**…"; la copia di lancio, catturata **lo stesso giorno**, dice "nel **2026**". Qualcuno ha aperto l'editor e ha aggiornato **solo la copia**.»* E la conseguenza dichiarata e mai assegnata a nessuno: *«**Conseguenza per noi:** un mirror di lancio è un artefatto vivo, e va messo in manutenzione come tale. Se non lo si fa, invecchia **il negozio**, che è quello che vende tutto l'anno.»* AP-029 ha consegnato il **pattern**; nessuno ha consegnato la **manutenzione** |
| **EFFORT** | **T2** |
| **CORSIA** | **C2** |
| **BLOCCA** | Niente — il campo è opzionale, e la riga di debrief è una delle tre già richieste da `GATE-MEM-1` |

---

#### AP-059 — Il vocabolario delle leve d'offerta di LANCI

| Campo | Contenuto |
|---|---|
| **COSA** | Un file `VOCABOLARIO-LEVE.md` che tiene **separate** le leve che si confondono. Nove voci, una per ogni costante di `ANATOMIA-DEI-LANCI.md` Parte V più la nona di Parte XI, ognuna con: cos'è, misura d'origine, quando si usa, **con cosa non va confusa**. Le tre distinzioni che il candidato AP-026 chiedeva e che non hanno mai avuto un posto dove vivere: **tripwire ≠ voucher che pareggia il prezzo ≠ opzione su lancio futuro** |
| **DOVE** | `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/09-VOCABOLARIO-LEVE.md` — numerato in coda ai documenti esistenti (00→08) |
| **CHI** | **Qualunque sessione** — è un documento nuovo, non collide |
| **QUANDO** | Indipendente. Utile prima di **S1** |
| **PERCHÉ** | AP-026 (🔵 conferma), verbatim: *«Il pattern Tripwire (primo acquisto sotto-prezzato) e il pattern "voucher pareggia il prezzo" (Armageddon) sono due leve distinte, non la stessa cosa — da tenere separate nel vocabolario delle leve d'offerta»*, con target dichiarato *«vocabolario LANCI»*. **Quel vocabolario non esiste.** AP-033 (nona costante) è la terza voce e ha lo stesso problema. Un candidato che punta a un documento inesistente è un puntatore stale, e la REGOLA PUNTATORI dice che è peggio di nessun puntatore |
| **EFFORT** | **T2** |
| **CORSIA** | **C1** |
| **BLOCCA** | Niente |

---

#### AP-046b / AP-047b / AP-048b — Le tre riparazioni che valgono anche per noi

Tre regole di prodotto, non di gate, che `SINTESI-SISTEMA-COPY.md` «COSA DOBBIAMO FARE MEGLIO DI LUI» impone e che i controlli 10-12 di AP-044 verificano dal lato macchina:

| # | Regola | Dove vive nel lancio |
|---|---|---|
| **46b** | **Il prezzo di un bundle si scompone sempre** | Se il lancio del Manuale è un bundle (Manuale + bonus), `struttura.valore_dichiarato` — che il gate **già ricalcola invece di leggere** — va **mostrato scomposto in pagina**. Il gate lo calcola; la pagina deve dirlo |
| **47b** | **Ogni prova sociale linka una fonte esterna o è etichettata come interna** | `ART-CPY.affermazioni[].riferimento`, che è **già obbligatorio quando `categoria == "prova"`**. Estensione: se il riferimento è interno, il testo deve dirlo |
| **48b** | **Ogni codice sconto vive in un solo file di configurazione** | Il generatore AP-035 legge il codice da un file, mai da una stringa in pagina |

| **CHI/QUANDO** | 46b e 47b: **Gael**, S3. 48b: qualunque sessione, dentro AP-035 |
| **EFFORT** | **T1** ciascuna |
| **BLOCCA** | Niente |

---

## 5. LA SEQUENZA — dove ogni azione si innesta in S0→S5

### 5.1 Tabella maestra

| Scaglione | Micro-task | Azioni di questo piano | Corsia | Effort aggiunto |
|---|---|---|---|---|
| **Parallelo a S0** (nessuna dipendenza) | — | **AP-034** (`catena.py`) · **AP-044** (controlli 9-13) · **AP-035** (generatore pre-cassa) · **AP-042/043** (§13/§14 + ADR-029) · **AP-038** (22 formule) · **AP-059** (vocabolario leve) · **AP-036** (`cassa-corso-a-livelli`) | **C1** | 12-22 h, **su una sessione diversa da quella di Gael** |
| **S0** | MT-FJF6, MT-32RU, MT-CV7N, MT-F37C | **nessuna azione** — il piano non tocca S0 | — | 0 |
| **S1** | MT-9ADD | **AP-004** (ancoraggio tripwire) · **AP-055** (concorrente in ricerca) · **AP-054** (obiezione mai nominata) · **AP-051** (ancora prima del prezzo) · **AP-033** (opzione futura, se Max la vuole) | **C2** | 1-2 h |
| **S2** | MT-XV6Y, MT-3XWC, MT-4GNU, MT-GHZ6 | **AP-033** (schema + criterio `GATE-OFF-1`) · **AP-052** (scadenza vera) · **AP-060** (vincolo upsell) · i **rossi** corrispondenti in `MT-4GNU` | **C2** | 3-5 h |
| **S3** | MT-GEKH | **AP-005** (ads countdown + 3 versioni) · **AP-008** (7 fattori, `transizioni[]`) · **AP-039** (griglia 11 tappe) · **AP-040** (concretezza) · **AP-041** (scala prova/prezzo) · **AP-037** (libreria) · **AP-050** (mirror) · **AP-056** (funnel di casa) · **AP-057** (pagina di consegna) · **AP-058** (86 parole) · **AP-053** (qualificazione negativa) · **46b/47b** | **C2** | 10-16 h |
| **S4** | MT-69CE | **AP-033** (riga di debrief sull'impegno futuro) · **AP-050** (riga di riconciliazione mirror) | **C2** | 0,5 h |
| **S5** | MT-RGZ6 | `lancio blocchi` mostra anche: le **copertine in attesa** (`PU-COPERTINA`), gli **impegni futuri scaduti** (AP-033), i **mirror non riconciliati** (AP-050) | **C2** | 1-2 h |

**Totale effort aggiunto:** **28-46 ore-uomo**, di cui **12-22 in corsia libera** (eseguibili da una sessione qualunque in parallelo, senza toccare il lavoro di Gael) e **16-24 dentro le micro-task di Gael**.

### 5.2 Rapporto con la stima di ADR-025

`04-COSTRUZIONE.md` §4.2 stima 118-174 ore per l'infrastruttura, con l'ordine *«si pianifichi su 174 ore»*. Questo piano aggiunge **16-24 ore dentro il perimetro di Gael** — cioè **il 9-14% della stima alta**. È sotto la soglia del 40% che `04-COSTRUZIONE.md` condizione di abbandono 5 fissa come punto di ri-stima.

> **Ma va detto con onestà:** `TASK-GAEL-20260908-SETTIMANA-03.md` avverte già che *«il totale della settimana supera aritmeticamente le ore disponibili in 7 giorni per una sola persona»*. **Quindi la corsia C2 di questo piano NON è "da fare questa settimana": è "da fare quando la micro-task corrispondente viene aperta", che può essere la settimana prossima.** Il piano non aggiunge una scadenza.

---

## 6. COSA RICHIEDE UN AMENDMENT — dichiarato, non nascosto

Tre soli casi in tutto il piano. Nessuno di essi viene riscritto di mia iniziativa.

| # | Azione | ADR toccato | Cosa serve | Chi lo porta |
|---|---|---|---|---|
| **1** | **AP-042, AP-043** — §13 e §14 di `CLAUDE-SITI.md` | **ADR-023** (due corsie) | **Nuovo ADR-029**, nella forma *«Sostituisce: niente. **Estende** ADR-023»* — identica al precedente ADR-024. Non è un amendment: è un'estensione con precedente | Qualunque sessione scrive, **Max firma**. **Non blocca** (regime ADR-024 §6) |
| **2** | **AP-044** — controlli 9-13 | **ADR-024** (otto controlli) | **Amendment ad ADR-024 §4**, o inclusione in ADR-029. ADR-024 ha già il precedente: *«Controlli 5 e 6 aggiunti il 2026-09-07 pomeriggio, stesso giorno dell'ADR, appena misurati: un ADR si allarga il giorno in cui il fatto arriva, non alla revisione successiva»*. **Questo piano usa quella stessa porta** | Qualunque sessione |
| **3** | **Se e solo se** si volesse un unico lancio a due prezzi invece di due lanci incatenati (AP-004) | **`previsione.schema.json.formula` (`const`)** + documento `02-PREVISIONE-E-DENARO.md` | **Richiede una dichiarazione di variante esplicita.** **Questo piano NON la propone**: la strada dei due lanci incatenati ottiene lo stesso risultato a zero amendment | — |

**Non richiedono amendment** (verificato contro ADR-025 decisione 3): tutte le aggiunte di campo agli schemi, tutte le estensioni di `criterio_eseguibile` su gate esistenti, tutti i test rossi nuovi, tutti i file nuovi. Nessuna azione di questo piano aggiunge un **artefatto** (resterebbero 13), un **agente** (resterebbero 15), o uno **stato**.

### 6.1 Un rischio di governo che va nominato

**`valida_registro.py` esegue 832 controlli e deve stare a exit 0 *prima* di ogni build** (`TASK-GAEL-20260908-SETTIMANA-03.md` §1️⃣, e `04-COSTRUZIONE.md` §9: *«L'ultima riga vale per ogni giorno di lavoro»*). Ogni azione C2 di questo piano modifica il registro o uno schema. **Quindi ogni azione C2 va eseguita e ri-validata nello stesso turno, mai lasciata a metà** — un registro incoerente ferma Gael su qualcosa che non è suo, e sarebbe una violazione di ADR-028 causata da questo piano.

**Regola operativa: una azione C2 alla volta, `valida_registro.py` a exit 0 prima di passare alla successiva.**

---

## 7. LA MAPPA ADR-028 — cosa NON è bloccato da cosa

ADR-028 punto 4 impone: *«Chi scrive un nuovo gate, ADR o regola con parole tipo "non negoziabile", "blocca tutto", "non si procede finché" deve scrivere ESATTAMENTE cosa blocca — mai lasciarlo implicito.»*

### 7.1 I gesti umani in gioco, e il loro perimetro esatto

| Gesto umano | Blocca ESATTAMENTE | NON blocca (lista più lunga, come dice ADR-028 punto 1) |
|---|---|---|
| **Brevo** (`MT-FJF6`) | il gate «S0 chiuso con prova vera», e il collegamento di un form d'opt-in a un servizio email vero | `catena.py`, il generatore pre-cassa, §13/§14, la libreria, il vocabolario, S1, S2, S3, S4, S5, tutte le 27 azioni di questo piano |
| **Cassa vera** (`MT-32RU`) | `funnel.json.prova_cassa.stato` e quindi `GATE-FNL-1` | tutto il resto di `ART-FNL` (pagine online, misura, transizioni), tutto S1/S2/S3 tranne quel campo, tutte le azioni C1 |
| **Consegna + rimborso** (`MT-CV7N`) | lo stesso campo di sopra | idem |
| **`PU-RUOLO`** — vendita/regalo, scadenza 12/09 | la parola scritta in `offerta.ruolo_prodotto` | il testo dell'ancoraggio (AP-004), la ricerca, il pubblico, il certificato, la previsione, tutti gli schemi, tutti i gate. **E ha già un default reversibile dichiarato** |
| **`PU-PREZZO`** — la firma, 14 giorni, nessun default | l'exit 0 di `GATE-OFF-1` **sul lancio reale** | **S2, per costruzione**: la condizione di sblocco di S2 è che `lancio avanza prova-vuota` **esca con codice 1 bloccando al controllo dell'offerta**. Una firma mancante non solo non blocca S2 — S2 non può chiudersi senza quel blocco |
| **`PU-COPERTINA`** | il singolo `pezzo` che aspetta la copertina | ogni altro pezzo di copy, ogni pagina, ogni gate |
| **Firma di Max su ADR-029** | l'entrata in vigore formale di §13/§14 | l'applicazione pratica: ADR-024 §6 ha già il precedente — *«§11 e §12 valgono come legge letta dagli agenti»* prima del gate |

### 7.2 La clausola anti-blocco di questo piano

> **Nessuna azione di questo piano è precondizione di una micro-task di `TASK-LANCI-BUILD-W3`.**
> Se una qualunque delle 27 azioni non si fa, la micro-task corrispondente **si chiude lo stesso**, e l'azione va in `company/Memory/BACKLOG.md` per ADR-005.
> **L'unica cosa che questo piano rende impossibile è dichiarare una cosa fatta quando non lo è** — e quella è la Legge Suprema (§3 emperator.md, prova non dichiarazione), che ADR-028 punto 5 lascia esplicitamente intatta.

---

## 8. PRIORITÀ — l'ordine in cui vale la pena farle

Ordinamento per **rendimento**: quanto euro/rischio si guadagna per ora-uomo spesa.

| Rango | Azione | Perché in questa posizione |
|---|---|---|
| **1** | **AP-034** — `catena.py`, controllo 8 | Il gate dichiarato «primo gate obbligatorio di LANCI» oggi è una frase. Il difetto che previene *«vale da solo tutto lo studio»* e **azzera ogni euro che il copy ha guadagnato**. Corsia libera, nessuna dipendenza, si può fare oggi |
| **2** | **AP-004** — la configurazione tripwire | Cambia la domanda che va a Max il 12/09. Costa tre campi di testo. È l'unica azione che può cambiare **quanto** incassa il primo lancio, non solo se incassa |
| **3** | **AP-054** — l'obiezione mai nominata | Il buco più grande e più economico da colpire, su un prodotto in competizione diretta. Una riga di ricerca e un paragrafo di copy |
| **4** | **AP-044** — controlli 9-13 | Cinque difetti misurati che diventano cinque controlli, tutti dentro lo script del rango 1 |
| **5** | **AP-008** — i 7 fattori | Il gate più profondo del piano, e l'unico che guarda la **coerenza fra gli step** invece della correttezza dei singoli. È T3 ed è dentro il perimetro di Gael: paziente |
| **6** | **AP-039 + AP-040 + AP-041** — la griglia di copy | `GATE-CPY-1` oggi è tarato su una griglia che non esiste. Tre azioni che vanno insieme o non vanno |
| **7** | **AP-035, AP-037, AP-038** — generatore e libreria | Fanno risparmiare tempo sul **secondo** lancio, non sul primo. Corsia libera, si fanno quando c'è spazio |
| **8** | **AP-042/043 + ADR-029** — §13 e §14 | Legge, non gate. Vale per tutti i cantieri futuri, non per questo lancio |
| **9** | **AP-005** — ads countdown | Alto valore, ma dipende da `data_apertura` firmata: prima della firma è aria |
| **10** | Tutto il resto | Nell'ordine della tabella maestra §5.1 |

---

## 9. COSA HO DELIBERATAMENTE ESCLUSO, E PERCHÉ

Un piano che non dichiara i suoi scarti nasconde le sue decisioni.

| Cosa | Perché fuori |
|---|---|
| **Il rapporto tipografico 81,6 : 14,88** («Risparmi €585» contro il prezzo pagato) | Non è da adottare: `ANATOMIA-DEI-LANCI.md` Parte IV lo dice esplicitamente — *«Funziona, ed è esattamente ciò che **noi non faremo**: è diventato il controllo 7 del nostro gate»*. Il controllo 7 è già in AP-034 |
| **Il codice sconto pubblico e permanente** | Difetto 7 di Parte VIII, già corretto nel pattern `pre-cassa` esistente (`scheda.md` «Il difetto da non copiare») e in §11 di `CLAUDE-SITI.md` |
| **L'effetto Barnum come sostituto della prova** (formula #22) | Entra nella libreria **con l'avvertimento**, non come tecnica raccomandata. `SINTESI-SISTEMA-COPY.md` la marca *«uso con consapevolezza: è Barnum puro»*, e il DELTA impone *«mindset/percorso = niente Barnum, proof reale sostitutiva»* |
| **Lo stack React + TanStack Start di `apsales.eu`** | ADR-024 §5 l'ha già escluso: *«ADR-023 ha già deciso le due corsie e non si riapre per una pagina di servizio. Registrato, non adottato»* |
| **Un motore di orchestrazione per la catena di lanci** | ADR-025 decisione 5 lo vieta, ADR-019 spiega perché (sette motori, zero consumatori). AP-004 usa **due lanci incatenati con i campi che esistono**, non un orchestratore |
| **AP-018 (framework a 10 livelli di maturità AI), AP-019 (PDF→JSON con Opus), AP-020 (prompt difensivo anti-hallucination)** | Sono nella tabella 🟡 «da valutare» con target **fuori da LANCI** (content-forge, skill-forge, decisione di Max). Non sono mio perimetro |
| **Un artefatto o un agente nuovo** | ADR-025 decisioni 2 e 4 fissano 13 e 15. Ogni cosa in questo piano è stata progettata per **entrare in ciò che esiste**. Se una critica dei tre giri trova un caso in cui non ci sta, quel caso va dichiarato come amendment, non forzato dentro |

---

## 10. I PUNTI DEBOLI DI QUESTO DRAFT — dove attaccarlo nei tre giri

Li scrivo io, perché un piano che non nomina i propri fianchi li fa trovare a qualcun altro più tardi e più caro.

| # | Debolezza | Come si verifica se è reale |
|---|---|---|
| **1** | **I path di `company/Ecosistemi/15-LANCI/lanci/<id>/` sono ipotizzati**, non letti: Gael li sta creando adesso e potrebbe usare una struttura diversa | `ls company/Ecosistemi/15-LANCI/` dopo che Gael ha chiuso S1. Se differiscono, tutte le righe DOVE di corsia C2 vanno riscritte — **T1, non un problema di sostanza** |
| **2** | **AP-008 aggiunge un campo obbligatorio a un artefatto che il primo lancio deve produrre.** Anche con `"non-applicabile"` ammesso, è attrito reale in una settimana già oltre le ore disponibili | Misurare quanto tempo costa compilare `transizioni[]` per il funnel del Manuale. Se supera 30 minuti, va reso opzionale al primo lancio con un `debito_collaudo` dichiarato — lo stesso meccanismo di `ART-CRT` modalità retroattiva |
| **3** | **AP-004 poggia su un'assunzione mai misurata**: che esista un pubblico che compra il Manuale a 27-47 € e poi Mastery a 397 €. `04-COSTRUZIONE.md` pre-mortem causa 4 la chiama *«media-alta»* di probabilità: *«il canale previsto è spento dal 29/07/2026»* | `pubblico.json` di S1. Se `raggiungibili_verificati` è sotto le poche centinaia, **la condizione di abbandono 2 scatta prima di AP-004**, e AP-004 diventa irrilevante — non sbagliato, irrilevante |
| **4** | **`catena.py` può produrre falsi positivi** sui controlli 7 e 2 (leggono stili calcolati). Un gate che sbaglia spesso viene derogato, e allora è peggio di non averlo (`04-COSTRUZIONE.md` §9) | Farlo girare sulle 52 pagine già catturate dello studio **prima** di collegarlo a `GATE-FNL-1`. Se produce FAIL su pagine che sappiamo essere corrette, si taratura prima di attivarlo |
| **5** | **27 azioni sono tante.** Il rischio è quello che ADR-024 §1 ha già misurato una volta: *«un rischio previsto a parole e non presidiato da un gate non è presidiato»* — un piano lungo che diventa carta | La verifica del §11. Se dopo due settimane meno di 5 azioni sono state fatte, il piano ha lo stesso male che denuncia e va tagliato ai primi 4 ranghi del §8 |
| **6** | **Il rosso in più di AP-008 rompe il conteggio «sei su sei» di `MT-4GNU`** — già segnalato al §3.11, ma è il tipo di dettaglio che si perde in un travaso | `python -m pytest tests/rossi/ -v` deve dire sei, non sette |

---

## 11. COME SI VERIFICA CHE QUESTO PIANO SIA STATO APPLICATO

Comandi, non dichiarazioni — stessa disciplina di ADR-024 §7.

```bash
# 1. Il gate esiste ed è eseguibile
ls .claude/skills/fabbrica-siti/scripts/catena.py
python .claude/skills/fabbrica-siti/scripts/catena.py --help

# 2. La legge ha tredici e quattordici articoli
grep -c "^## §" .claude/skills/fabbrica-siti/CLAUDE-SITI.md    # atteso: 14

# 3. Il registro è coerente dopo ogni modifica di corsia C2
cd PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati && PYTHONIOENCODING=utf-8 python valida_registro.py
echo $?                                                          # atteso: 0

# 4. Il numero di artefatti e agenti NON è cambiato
grep -c '^  - id: "ART-' PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/registro.yaml   # atteso: 13
grep -c '^  - id: "lan-' PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/registro.yaml   # atteso: 15

# 5. I pattern nuovi sono in galleria (non puntatori stale)
ls .claude/skills/fabbrica-siti/pattern/cassa-corso-a-livelli
python .claude/skills/fabbrica-siti/scripts/galleria.py

# 6. La libreria di copy esiste e ha le 22 formule
ls company/Ecosistemi/15-LANCI/copy/libreria/formule/ | wc -l    # atteso: 22

# 7. Il vocabolario delle leve esiste (AP-026 smette di puntare al vuoto)
ls PIANO-MAESTRO/29-ECOSISTEMA-LANCI/09-VOCABOLARIO-LEVE.md

# 8. I test rossi di S2 sono ancora sei, non sette
python -m pytest tests/rossi/ -v 2>&1 | grep -c FAILED           # atteso: 6
```

E la verifica che vale più di tutte le altre, da eseguire **prima** di aprire il carrello del primo lancio:

```bash
python .claude/skills/fabbrica-siti/scripts/catena.py --manifesto lanci/manuale-cc-2026/funnel.json
echo $?    # se non è 0, il lancio non apre
```

> Perché è la sola cosa che, se salta, annulla tutte le altre. `ANATOMIA-DEI-LANCI.md` Parte IX, passo 12.

---

## 12. AGGIORNAMENTO DA FARE A `MIGLIORAMENTI-DIGITAL-EMPIRE.md`

Quel documento è dichiarato **vivo** (*«cresce, non si chiude»*). Le 23 voci nuove (AP-034..AP-060) vanno aggiunte alla tabella 🟡, con questo piano come fonte, **nello stesso turno in cui il piano viene approvato** — REGOLA PUNTATORI, mai stale.

E due voci esistenti cambiano stato:
- **AP-017** → da 🟡 «da valutare» a 🟡 «proposto, alta priorità», target `GATE-OFF-1` (diventa AP-060)
- **AP-026** → resta 🔵, ma il target *«vocabolario LANCI»* smette di essere un puntatore vuoto quando AP-059 esiste

---

## Connessioni

- `competitor/Andrei Pascu/ANATOMIA-DEI-LANCI.md` — Parti IV, V, VII, VIII, IX, X, XI
- `competitor/Andrei Pascu/site-study/SINTESI-METODO.md` · `SINTESI-SISTEMA-COPY.md` · `SINTESI-SISTEMA-VISIVO.md` — i tre DELTA ALLA FABBRICA da cui nasce la Famiglia B
- `competitor/Andrei Pascu/MIGLIORAMENTI-DIGITAL-EMPIRE.md` — i 33 candidati, da estendere a 60
- `SKILL & Agenti/Empire Studio Suite/empire-studio/runs/andrei-pascu-armageddon-outfunnel-001/lessons/lezione-{06,11,12,16,19,20}/lesson-analysis.md` — le citazioni verbatim di AP-004, AP-005, AP-008, AP-060
- `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/` — 00-LEGGIMI, 03-FLUSSO-OFFERTA, 04-COSTRUZIONE, `dati/registro.yaml`, `dati/schemi/*.json`
- `company/Memory/tasks/TASK-GAEL-20260908-SETTIMANA-03.md` + `micro/TASK-LANCI-BUILD-W3/` — le dodici micro-task in cui il piano si innesta
- `company/Memory/decisions/` — ADR-003, ADR-005, ADR-016, ADR-019, ADR-023, ADR-024, ADR-025, ADR-026, ADR-027, ADR-028
- `.claude/skills/fabbrica-siti/CLAUDE-SITI.md` + `pattern/pre-cassa/scheda.md` + `pattern/pagina-ponte/`

---

**Fine DRAFT V1.**
