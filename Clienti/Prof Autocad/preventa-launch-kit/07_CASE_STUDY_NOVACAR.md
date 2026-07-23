# Case Study — Novacar srl

### Come una concessionaria multimarca ha automatizzato i preventivi per le auto importate dalla Germania

**Prodotto:** Preventa (ex PreventivoForge) · **Cliente:** Novacar srl, concessionaria multimarca (Milano) · **Periodo osservato:** 30 giugno – 23 luglio 2026

> Nota di metodo: ogni cifra in questo documento è verificabile su disco o citata da un checkpoint di progetto. Dove un dato utile non esiste ancora, è segnalato esplicitamente come da confermare. Nessuna citazione del cliente è stata inventata: non ce ne sono, perché non esistono ancora (vedi §6).

---

## 1. Il cliente

Novacar srl è una concessionaria multimarca che acquista veicoli usati su portali esteri (in particolare **mobile.de**, il principale portale auto tedesco) e li rivende in Italia. Per ogni auto comprata all'estero, il salone deve produrre un preventivo per il cliente finale in italiano, con il prezzo "chiavi in mano" corretto e la stessa impaginazione che la concessionaria usa da sempre.

*(Fonte: `concessionarie/novacar/config.json` — ragione sociale, sede; CP-20260702-003 — cliente reale identificato come Novacar srl)*

## 2. Il problema concreto

Un annuncio auto su mobile.de è **in tedesco** e non è pensato per essere consegnato a un cliente italiano. Prima di questo lavoro, per ogni veicolo importato la concessionaria doveva:

- **Tradurre a mano** scheda tecnica, dotazioni e descrizione dal tedesco all'italiano, voce per voce;
- **Ricalcolare il prezzo finale** applicando maggiorazione, costi di immatricolazione, pratiche e trasporto sopra il prezzo esposto sull'annuncio tedesco;
- **Scaricare e reimpaginare le foto** dell'annuncio senza tagliarle o perdere qualità;
- **Ricreare da zero il PDF** nel formato che Novacar usa storicamente (il modello di riferimento è un vero preventivo del cliente: *"Preventivo BMW Z4 2003 FR 3.0i.pdf"*), con logo, dati aziendali, scheda tecnica, equipaggiamento, garanzia e prezzo finale — sempre uguale a se stesso, indipendentemente da chi lo compila.

*(Fonte: `regole/REGOLE-SACRE.md` — modello di riferimento dichiarato; CP-20260702-003 — "rifare il PDF sul modello Novacar"; CP-20260723-003, sezione "Prima" — elenco dei passaggi manuali sostituiti)*

## 3. Cosa è stato costruito

Un motore che va **dal link dell'annuncio al PDF finito**, consegnato come applicazione desktop per Windows:

| Fase | Cosa fa | Come | Fonte |
|---|---|---|---|
| **S1 — Scraping** | Legge l'annuncio mobile.de | Chrome **reale** pilotato via Chrome DevTools Protocol (non un browser automatizzato "finto"): necessario perché mobile.de è protetto da **Akamai Bot Manager**, che blocca Playwright headless con l'errore "Zugriff verweigert" | CP-20260701-003 |
| **S2 — Parsing** | Estrae marca, modello, prezzo esposto, km, potenza, dotazioni, foto | Legge i dati reali dalla variabile interna della pagina (`window.__INITIAL_STATE__`), non solo i tag SEO che spesso sono vuoti | CP-20260701-003 |
| **S3 — Traduzione** | Traduce scheda tecnica e dotazioni in italiano | Glossario automotive tedesco→italiano dedicato (~150 termini), con verifica che non resti nessuna parola tedesca | CP-20260701-001, CP-20260701-003 |
| **S4 — Prezzo** | Calcola il prezzo finale al cliente | Formula per-concessionaria: `finale = esposto × (1 + maggiorazione%) + costi fissi (immatricolazione/pratiche/trasporto) + margine`. Per Novacar: maggiorazione 3%, due voci fisse da 1.500 € (`concessionarie/novacar/config.json`) | `rules/R4-pricing.md`, `concessionarie/novacar/config.json` |
| **S5 — PDF** | Genera il documento finale | Motore Chrome/CDP (`Page.printToPDF`), impaginato sul modello storico Novacar: 14 regole fisse (logo in copertina, dati azienda, scheda tecnica, equipaggiamento, garanzia, prezzo "Totale in strada", foto intere mai tagliate, chiusura solo logo) | CP-20260702-003, `regole/REGOLE-SACRE.md` |
| **Controllo qualità** | Blocca il PDF se qualcosa non torna | 6 controlli automatici bloccanti prima della consegna: estrazione dati, traduzione, prezzo ricalcolato in modo indipendente, render PDF, immagini complete, rispetto delle 14 regole d'impaginazione | CP-20260701-001, CP-20260702-003 |
| **App** | Rende tutto usabile da un venditore | App desktop con interfaccia grafica premium (fallback automatico a un'interfaccia semplice se il PC non supporta la grafica avanzata), pacchettizzata come eseguibile Windows autonomo — **non richiede Python né competenze tecniche** | CP-20260702-002, CP-20260702-003, CP-20260703-001 |

## 4. Come funziona in pratica

1. Il venditore **incolla il link dell'annuncio mobile.de** nell'app e preme "Genera".
2. L'app apre una finestra Chrome reale per leggere l'annuncio, superando le protezioni anti-bot del portale tedesco.
3. Scheda tecnica, equipaggiamento e descrizione vengono **tradotti in italiano** automaticamente.
4. Il prezzo finale viene calcolato con le regole già impostate per il salone (maggiorazione + costi fissi) e **ricalcolato in modo indipendente** da un secondo controllo, per intercettare eventuali errori prima che arrivino al cliente.
5. Il PDF viene generato rispettando esattamente il formato storico usato da Novacar: stessa struttura, stesso ordine delle sezioni, stesse regole — cambiano solo i dati dell'auto.
6. L'intero ciclo richiede **circa 1-2 minuti di lavorazione della macchina**, poi il PDF si apre da solo ed è archiviato nello storico del salone.

*(Fonte: `CONSEGNA-NOVACAR.md` §3 — istruzioni d'uso consegnate al cliente; CP-20260702-002/003 — funzionamento dell'app)*

## 5. Risultato misurabile

Numeri contati direttamente sui file di progetto (non stimati), relativi all'attività di sviluppo, collaudo e primo utilizzo tra il **3 e il 13 luglio 2026**:

- **65 run registrati** nello storico dei preventivi (`Memory/storico-preventivi/`, un record per esecuzione — conteggio diretto: `grep -c run_id` = 65, dealer `novacar`).
- **52 PDF generati** e conservati nelle cartelle `preventivi_<data>` accanto all'applicazione (conteggio diretto dei file `.pdf`).
- **11 marche distinte** trattate senza intervento manuale sul codice: Audi, BMW, Hyundai, Land Rover, Mercedes-Benz, Opel, Renault, Škoda, Tesla, Toyota, Volvo (elenco ricavato direttamente dai nomi dei file generati).
- **Circa 1-2 minuti** di lavorazione della macchina dal link al PDF pronto (fonte: `CONSEGNA-NOVACAR.md` §3, istruzioni consegnate al cliente).
- **6 controlli automatici bloccanti** prima che un PDF venga consegnato: se anche uno solo fallisce, il preventivo non esce (fonte: CP-20260701-001, CP-20260702-003).

**Un preventivo vero, preso dallo storico** (file `AF-20260713-150552-459563767_novacar_Opel-Insignia.json`, letto direttamente):
> Opel Insignia Dynamic — annuncio a 15.950 €, prezzo finale sul preventivo **19.428 €**. Titolo del documento generato automaticamente: *"Opel Insignia Dynamic 19.428 €"*.

**Prova di scraping live contro le protezioni anti-bot del sito sorgente** (non su un dato finto, su un annuncio mobile.de reale): Mercedes-Benz GLA 220 d 4MATIC AMG, annuncio 456259857 — **26/26 foto** scaricate, prezzo esposto **47.490 €** → prezzo finale **51.915 €**, PDF da 810 KB, 4 controlli su 4 verdi, 0 residui in tedesco. Il test è stato ripetuto due volte in modalità regressione sulla stessa pagina salvata, con esito identico.
*(Fonte: CP-20260701-003; file `Memory/storico-preventivi/2026-07-01_mercedes-gla-220_456259857.md` e i due record JSON di rigenerazione del 4 luglio)*

**Prova di distribuzione come eseguibile standalone**: `PreventivoForge.exe` (senza Python installato sulla macchina) testato con dealer Novacar preconfigurato — 4 controlli su 4 verdi, PDF da 156 KB generato correttamente.
*(Fonte: CP-20260702-003)*

## 6. Cosa questa prova NON dice (onestà, non marketing)

- **Non affermiamo che Novacar venda di più.** Il motore produce il documento di preventivo, non chiude la trattativa: nessun collegamento è stato misurato tra questo strumento e le vendite del salone.
- **I 65 run includono i collaudi del team di sviluppo** su annunci reali, fatti durante la costruzione e la verifica del motore (30 giugno – 13 luglio 2026). Sono la prova che il motore funziona su dati veri, **non il registro vendite del cliente**: non sappiamo dire quanti di questi 65 siano stati generati per un cliente finale reale del salone rispetto ai test tecnici.
- **Non esiste ancora una testimonianza firmata di Novacar.** Nessuna frase in questo documento è attribuita al cliente: se e quando arriverà una dichiarazione diretta, verrà aggiunta qui con nome e cognome, non prima.

> ⚠️ DATO DA CONFERMARE CON IL CLIENTE: tempo effettivamente risparmiato rispetto al metodo manuale precedente. Nei checkpoint è documentato solo il tempo di esecuzione della macchina (~1-2 min), non un confronto cronometrato con il processo manuale che Novacar usava prima.
> ⚠️ DATO DA CONFERMARE CON IL CLIENTE: quanti dei 52-65 preventivi sono stati effettivamente inviati a un cliente finale del salone (uso operativo) rispetto a quelli generati per collaudo interno del team di sviluppo.
> ⚠️ DATO DA CONFERMARE CON IL CLIENTE: se Novacar sta usando l'app in autonomia, ad oggi, senza supporto del team che l'ha costruita.

## 7. Cosa significa per un altro concessionario

- Il motore è **configurabile per concessionaria** (`concessionarie/<id>/config.json`): logo, dati aziendali, regole di prezzo cambiano senza toccare una riga di codice — lo stesso motore può servire più saloni con documenti diversi.
- Funziona anche su portali sorgente con **protezioni anti-bot avanzate** (dimostrato contro Akamai Bot Manager su mobile.de): non è un semplice script che si rompe al primo aggiornamento del sito.
- Si consegna come **applicazione desktop pronta all'uso**: nessun server da gestire, nessuna competenza tecnica richiesta al concessionario, nessuna migrazione di dati dal gestionale esistente.
- Il formato del PDF finale **rispetta quello che il concessionario già usa** — non impone un nuovo stile, riproduce quello con cui i clienti del salone hanno già familiarità.

---

## Fonti

| # | Affermazione | Fonte |
|---|---|---|
| 1 | Cliente reale = Novacar srl, modello PDF di riferimento = "Preventivo BMW Z4 2003 FR 3.0i.pdf" | `Clienti/Prof Autocad/preventivo-forge/regole/REGOLE-SACRE.md`; CP-20260702-003 |
| 2 | Dati anagrafici concessionaria (ragione sociale, sede) | `Clienti/Prof Autocad/preventivo-forge/concessionarie/novacar/config.json` |
| 3 | mobile.de protetto da Akamai Bot Manager; bypass via Chrome reale + CDP | CP-20260701-003 |
| 4 | Parsing dati reali via `window.__INITIAL_STATE__` | CP-20260701-003 |
| 5 | Glossario DE→IT ~150 termini, 0 residui tedeschi | CP-20260701-001; CP-20260701-003 |
| 6 | Formula prezzo (maggiorazione 3% + 1.500 + 1.500) | `Clienti/Prof Autocad/preventivo-forge/rules/R4-pricing.md`; `concessionarie/novacar/config.json` |
| 7 | 14 regole d'impaginazione (R-01…R-14) e 6 controlli automatici (Gate A/B/C/D + IMG + R) | `Clienti/Prof Autocad/preventivo-forge/regole/REGOLE-SACRE.md`; CP-20260701-001; CP-20260702-003 |
| 8 | App desktop, GUI premium, eseguibile standalone | CP-20260702-002; CP-20260702-003; CP-20260703-001 |
| 9 | Tempo di lavorazione ~1-2 minuti | `Clienti/Prof Autocad/preventivo-forge/CONSEGNA-NOVACAR.md` §3 |
| 10 | 65 run registrati (3-13 luglio 2026) | Conteggio diretto: `Memory/storico-preventivi/` (`grep -c run_id` = 65); confermato in CP-20260723-003 |
| 11 | 52 PDF nelle cartelle `preventivi_<data>` | Conteggio diretto dei file `.pdf` nelle cartelle `preventivo-forge/preventivi_*`; confermato in CP-20260723-003 |
| 12 | 11 marche distinte | Ricavato direttamente dai nomi dei file in `Memory/storico-preventivi/` |
| 13 | Esempio reale Opel Insignia 15.950 → 19.428 € | File letto direttamente: `Memory/storico-preventivi/AF-20260713-150552-459563767_novacar_Opel-Insignia.json` |
| 14 | Prova live GLA 220: 26/26 foto, 47.490 → 51.915 €, PDF 810 KB | CP-20260701-003; `Memory/storico-preventivi/2026-07-01_mercedes-gla-220_456259857.md` |
| 15 | Test `.exe` standalone: 4/4 gate verdi, PDF 156 KB | CP-20260702-003 |
| 16 | Onestà sui limiti della prova (nessun claim di vendita, run include collaudi, nessuna testimonianza ancora) | Impostazione dichiarata esplicitamente in CP-20260723-003 (sezione "carte scoperte" della prova pubblicata su `agency-empire/`), qui applicata allo stesso standard |

---

### Nota tecnica su una discrepanza trovata nei checkpoint

Il checkpoint **CP-20260703-001** cita un'ulteriore "prova reale precedente (2026-07-02)" sullo stesso annuncio GLA 220 con numeri diversi (44.490 € → 48.825 €, 26 foto). Questo documento **non riprende quel numero**: i due record effettivamente presenti su disco per quell'annuncio (`Memory/storico-preventivi/2026-07-01_mercedes-gla-220_456259857.md` e le due rigenerazioni del 4 luglio) riportano tutti **47.490 € → 51.915 €**. In assenza di un file corrispondente ai 44.490/48.825 € citati in CP-20260703-001, questo case study usa solo il valore verificabile su disco e segnala la difformità come incongruenza di checkpoint da chiarire, non come dato utilizzabile.

---

*Documento preparato per uso commerciale (outreach concessionari, allegato dopo richiesta di dettagli). Formati disponibili: Markdown (questo file), HTML stampabile (`07_CASE_STUDY_NOVACAR.html`), PDF (`07_CASE_STUDY_NOVACAR.pdf`, se generato — vedi nota di generazione in fondo al file HTML).*
