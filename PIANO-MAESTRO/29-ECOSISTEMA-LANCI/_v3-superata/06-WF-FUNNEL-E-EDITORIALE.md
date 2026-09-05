---
Type: PROJECT
Status: Proposta
Tags: #lanci #ecosistema-15 #funnel #editoriale
Created: 2026-09-05
---

# 06 — WF-FNL (FUNNEL) e WF-EDT (EDITORIALE)

> Terza versione. La precedente aveva un difetto che la rendeva inservibile: **il flusso del
> funnel descriveva dodici sezioni e non nominava un solo agente né una sola fase.** Era
> letteralmente il fallimento numero uno del pre-mortem — bella carta, nessuno che la esegua.
> Corretto qui, insieme ad altri sei rilievi. Il paragrafo finale li elenca.

---
---

# PARTE A — WF-FNL · IL FUNNEL

## A.1 Identità

| Campo | Valore |
|---|---|
| **Sigla** | `WF-FNL` — *e il reparto si chiama `LAN-FNL`, mai `LAN-SITI`* |
| **Nome** | Flusso Funnel e Pagine |
| **Missione** | Mette online le pagine e **prova che misurano**. Una pagina che non produce un numero non è online: è pubblicata |
| **Proprietario** | `LAN-FNL` — **avvolge il reparto Vendite & Funnel esistente** (§A.9) |
| **Durata** | **30-45 ore-uomo** per un funnel completo; **10-15** se le pagine esistono e vanno verificate e collegate |

> ⚠️ **Nome:** la versione precedente lo chiamava `LAN-SITI` in alcuni passaggi e `LAN-FNL` in
> altri, e gli handoff erano indirizzati al nome sbagliato. Un reparto con due nomi riceve
> passaggi di consegne che nessuno raccoglie.

## A.2 Trigger, input, precondizioni

**Comando:** `/lancio-funnel <lancio_id>`

```json
{
  "lancio_id": "string",
  "tipo_funnel": "webinar | video-diretto | solo-pagina-vendita",
  "copy_manifest": "string",
  "offerta_path": "string",
  "dominio": "string",
  "strumento_pagamento": "string",
  "strumento_email": "string",
  "pagine_esistenti": [{ "tipo": "string", "url": "string", "va_riusata": "boolean" }],
  "canali_traffico": ["organico", "a-pagamento"]
}
```

**`canali_traffico` non è decorativo:** se contiene entrambi i valori, il flusso genera **due
pagine d'ingresso separate**. È la regola ereditata più importante e la più disattesa: con
traffico gratuito e comprato sulla stessa pagina, il confronto fra i due non è più misurabile e
ogni numero successivo — costo di acquisizione compreso — diventa una divisione fra grandezze
scollegate.

| Precondizione | Verifica |
|---|---|
| La pagina di vendita ha superato il suo gate | il verbale esiste |
| `offerta.json` con prezzo e data | il gate dell'offerta |
| Lo strumento di pagamento è configurato | **una transazione di prova reale**, non simulata |
| Il dominio risponde | controllo diretto |

## A.3 LE FASI — con l'agente che le esegue

> Questa tabella è ciò che mancava del tutto.

| # | Fase | Cosa fa | Agente | Output | Ore | Parallelo | Umano |
|---|---|---|---|---|---:|---|---|
| **F0** | Intake e inventario | valida l'input; censisce le pagine già esistenti e decide quali si riusano | `lan-fnl-conductor` | `funnel/00-intake.json` | 2 | no | no |
| **F1** | Topologia | disegna il percorso completo: pagine necessarie per questo tipo di funnel, bivi, uscite, rientri | `lan-fnl-conductor` | `funnel/01-topologia.json` | 3 | no | no |
| **F2** | Piano di tracciamento | per ogni pagina, quali eventi si registrano e con che nome | `lan-fnl-verificatore` | `funnel/02-tracciamento.json` | 2 | no | no |
| **F3** | Parametrizzazione dei componenti | rende riusabili i componenti di gestione obiezioni esistenti (§A.10) | `lan-fnl-costruttore` | componenti con parametri | 4 | no | no |
| **F4** | Costruzione delle pagine | costruisce ogni pagina chiamando le skill esistenti | `lan-fnl-costruttore` | le pagine | 12-20 | **sì**, una per pagina | no |
| **F5** | Pubblicazione | mette online | `lan-fnl-costruttore` | url pubblici | 2 | no | **Sì** — è irreversibile |
| **F6** | Installazione del tracciamento | mette le etichette e collega gli eventi | `lan-fnl-costruttore` | — | 3 | no | no |
| **GATE-FNL-1** | **La verifica** | gli otto controlli su ogni pagina (§A.5) | `lan-fnl-verificatore` | `funnel.json` | 3 | no | il controllo 8 sì |
| **F7** | Ottimizzazione | il ciclo, quando un numero è sotto soglia (§A.6) | `lan-fnl-ottimizzatore` | `funnel/07-test.json` | continuo | no | no |

**Quattro agenti**, come dichiarato nel censimento: conductor, costruttore, verificatore,
ottimizzatore. **E il verificatore non è il costruttore** — è la regola *chi produce non approva*
applicata qui, dove serve di più.

## A.4 Le nove pagine

| # | Pagina | Scopo | Riceve i testi da |
|---|---|---|---|
| 1 | **Ingresso (organica)** | nome ed email dal traffico gratuito | LAN-CPY |
| 1b | **Ingresso (a pagamento)** | idem dal traffico comprato — **pagina separata** | LAN-CPY |
| 2 | **Regalo** | consegna ciò che è stato promesso | LAN-CPY |
| 3 | **Vendita aggiuntiva 15 €** | finanzia il funnel | LAN-CPY |
| 4 | **Registrazione al webinar** | far iscrivere | LAN-CPY |
| 5 | **Webinar e replica** | la presentazione | LAN-CPY |
| 6 | **Pagina di vendita** | vendere | LAN-CPY |
| 7 | **Cassa** | incassare | LAN-CPY |
| 8 | **Ringraziamento** | confermare e orientare | LAN-CPY |
| 9 | **Aggiunte dopo l'acquisto** | aumentare il valore dell'ordine | LAN-CPY |

**Le pagine non necessarie si dichiarano, non si omettono.** Un funnel diretto salta la 4 e la 5, e
il manifest scrive *"non previste: tipo video-diretto"*. Una pagina assente senza dichiarazione è
indistinguibile da una dimenticata.

## A.5 Il gate — gli otto controlli

| # | Controllo | Soglia | Automatico |
|---|---|---|---|
| 1 | La pagina risponde | codice 200 | sì |
| 2 | Tempo di risposta | ≤3 secondi | sì |
| 3 | Le etichette di tracciamento sono nel codice | presenti | sì |
| 4 | **L'evento di conversione è arrivato** | ≥1 in prova | sì, con una visita di prova |
| 5 | Resa su telefono | nessuno scorrimento orizzontale · testo ≥16px · pulsante ≥44px | sì |
| 6 | I collegamenti interni funzionano | 100% | sì |
| 7 | La pagina successiva del percorso esiste | sì | sì |
| 8 | **Cassa: una transazione di prova reale è riuscita** | 1 | **no: la fa una persona** |

**Il controllo 4 è ciò che separa questo gate da una formalità.** Verificare che l'etichetta sia
nel codice non prova niente: si verifica che l'evento **sia arrivato**. Si visita la pagina, si
compila con un indirizzo di prova, si guarda se l'evento compare. Se non compare, la pagina non è
online.

**Il controllo 8 non si automatizza mai:** implica un pagamento vero. Si fa con l'importo minimo e
si rimborsa, ma **si fa**. Un funnel dove nessuno ha mai provato a pagare scopre il problema dal
primo cliente.

**Lo script:** `scripts/gate_pagina.py` — `controlla_pagina(url, attesi) -> dict` ·
`prova_evento(url, evento, timeout_s=60) -> bool` · `verifica_percorso(funnel) -> list[str]` ·
`verbale(lancio_id) -> int`.

## A.6 L'ottimizzazione — un ciclo, non un allarme

| Punto | Verde | Giallo | Rosso |
|---|---|---|---|
| Iscrizione alla pagina d'ingresso | >35% | 20-35% | <20% |
| Vendita aggiuntiva 15 € | >15% | 8-15% | <8% |
| Iscrizione al webinar dal video | >20% | 10-20% | <10% |
| Presenza al webinar | >30% | 20-30% | <20% |
| Conversione del webinar | >5% | 2-5% | <2% |
| Recupero dopo il webinar | >15% | 8-15% | <8% |

> ⚠️ **Questi numeri vengono da materiale formativo su infoprodotti generalisti, non da questa
> azienda.** Applicarli a un ebook tecnico in italiano su un pubblico piccolo è **un'assunzione**.
> Restano come soglie di partenza — meglio di niente — **marcate come provvisorie**, e il primo
> lancio ha il compito di produrre i numeri veri. Dal secondo si usano i propri.

**Il ciclo:**

```
1. IPOTESI     una frase che dica la causa: "il titolo non nomina il problema"
2. VARIANTE    UNA modifica. Due insieme non dicono quale ha funzionato
3. VOLUME      quanti visitatori servono prima di poter decidere
4. DECISIONE   si tiene, si torna indietro, o non si sa ancora
5. MEMORIA     l'esito si scrive, che vinca o che perda
```

| Differenza da vedere | Visitatori per versione |
|---|---:|
| grande (dal 20% al 30%) | ~300 |
| media (dal 20% al 25%) | ~1.200 |
| piccola (dal 20% al 22%) | ~7.000 |

**La conseguenza, detta chiaramente:** con il traffico di un lancio piccolo si vedono **solo le
differenze grandi**. Un test su una modifica minuscola con 200 visitatori non dà una risposta: dà
rumore che sembra una risposta. **Quindi si testano solo cose grosse** — un titolo completamente
diverso, un'offerta diversa — e le rifiniture si decidono per mestiere.

## A.7 Output e handoff

```json
{
  "lancio_id": "string",
  "pagine": [
    { "tipo": "ingresso-organica", "url": "https://...", "codice": 200,
      "tempo_ms": 1240, "eventi_attesi": ["pagina_vista", "modulo_inviato"],
      "eventi_verificati": ["pagina_vista", "modulo_inviato"],
      "mobile_ok": true, "verificata_il": "ISO" }
  ],
  "transazione_di_prova": { "eseguita": true, "importo": 1.00, "rimborsata": true },
  "pagine_non_previste": ["registrazione-webinar", "webinar"],
  "stato": "COMPLETO | INCOMPLETO"
}
```

**Handoff in uscita:** a `LAN-TRF` (le pagine su cui mandare traffico) e a `LAN-REG` (voce 3 e 4
della lista di sincronizzazione). **Criterio di accettazione:** ogni pagina con `eventi_verificati`
uguale a `eventi_attesi`.

## A.8 Fallimenti

| Sintomo | Causa | Cosa fa il sistema |
|---|---|---|
| L'evento non arriva mai | etichetta installata male, o consenso ai cookie che la blocca | il gate blocca; è **il caso più frequente** e va provato per primo |
| La pagina risponde ma è lenta | risorse pesanti | blocca oltre i 3 secondi: sotto quella soglia si perde più traffico di quanto ne porti un annuncio |
| La transazione di prova fallisce | pagamento non configurato | **blocca l'apertura della vendita**: è la voce che salva il lancio |
| Le pagine esistenti non tracciano | costruite prima che il tracciamento esistesse | è precisamente ciò che il gate deve scoprire: se succede al primo lancio, il gate ha già ripagato la costruzione |
| Un test viene deciso sotto il volume minimo | fretta | l'ottimizzatore **rifiuta** di dichiarare un vincitore e lo scrive |

## A.9 Cosa si avvolge — e la duplicazione evitata

> ⚠️ **La versione precedente ignorava un reparto che esiste.** `IB-L2-VEND-Vendite-Funnel`
> contiene tre workflow — fra cui uno sulla pagina di vendita e uno sull'ottimizzazione delle
> conversioni — e sei schede agente. **Zero occorrenze in tutto il piano precedente.** Era
> esattamente la duplicazione che il piano si vietava.

| Cosa esiste | Come si usa |
|---|---|
| **Il reparto Vendite & Funnel** (3 workflow, 6 schede agente) | `LAN-FNL` **lo avvolge**: i suoi workflow diventano il contenuto delle fasi F1 e F7, le sue schede agente diventano la specifica dei nostri quattro agenti |
| Le skill di costruzione, scrittura e pubblicazione siti | le chiama il costruttore |
| La skill di stile premium | è il sistema visivo standard |
| La skill per moduli e iscrizioni | pagine d'ingresso |
| **La skill di lancio già installata** | va letta prima di scrivere qualunque cosa in F1: **anch'essa aveva zero occorrenze nel piano precedente** |
| La landing già costruita | si **verifica e si collega**, non si rifà |

## A.10 I componenti riusabili — la verità

> ⚠️ **Il piano precedente dichiarava una cosa falsa, verificata nel codice.** Diceva che il copy
> consegna le obiezioni *"tipizzate sui parametri che i componenti si aspettano"*.
> **Quei componenti non accettano parametri:** il contenuto è scritto dentro il codice.

| Fatto | Conseguenza |
|---|---|
| I cinque componenti **non hanno parametri** | vanno parametrizzati: **è la fase F3**, quattro ore, sul percorso critico |
| Appartengono alla pagina di un'**agenzia di servizi web** | tre obiezioni su quattro sono di un altro pubblico (*"ho già un sito"*) |
| Il file vive in una cartella duplicata | **va deciso quale copia è la fonte** prima di toccarli |

**Il riuso è del guscio grafico, non del contenuto.** È comunque un guadagno — la parte difficile
è il comportamento visivo — ma va detto per quello che è.

## A.11 Il conflitto sul sistema visivo

Esiste un sistema di regole scritto per la landing dell'ebook (54 righe: palette, tipografia,
effetti, le sette sezioni obbligatorie) e una skill di stile installata nell'Impero.

**Proposta:** **lo standard è la skill**, perché è viva, manutenuta e vale per tutto l'Impero.
**Ma non si butta niente:** le due cose che la skill non ha — la struttura a sette sezioni della
pagina di vendita e la regola sul colore d'accento solo per micro-dettagli — si assorbono come
profilo *"lancio info-prodotto"*.

**Decide la guild Design.** Il flusso non resta fermo ad aspettare la ratifica.

---
---

# PARTE B — WF-EDT · L'EDITORIALE

## B.1 Il difetto che questo flusso esiste per impedire

Nell'Impero è documentato un problema preciso: **contenuti finiti che non escono mai.** Venticinque
pezzi completati e mai pubblicati, il più vecchio fermo da centotrentacinque giorni.

**Non è un problema di produzione: è un problema di consegna.** In un lancio è letale: un contenuto
che esce tre giorni dopo la chiusura della vendita non vale zero — vale **meno** di zero, perché ha
consumato la produzione che serviva altrove.

> ⚠️ **E c'è un fatto scomodo che la critica ha verificato:** uno degli strumenti di pubblicazione
> dell'Impero **stampa ancora "pubblicazione completata con successo (SIMULATA)" ed esce come se
> fosse riuscito.** Il presidio contro il "mai pubblicato" poggerebbe proprio lì.
> **Conseguenza per il piano:** la prova che un contenuto è uscito **non può essere il codice di
> uscita di quello strumento**. Deve essere **l'indirizzo pubblico**, letto e verificato.

## B.2 Il presidio, in tre parti

1. **Nessuna riga è "pronta" senza una data di pubblicazione e un responsabile con un nome.**
2. **Un contenuto prodotto e non pubblicato entro 48 ore dalla sua data diventa un blocco
   visibile** nello stato del lancio, non una nota in un rapporto.
3. **Alla chiusura, il debrief conta i pezzi prodotti contro quelli usciti.** Differenza maggiore
   di zero → va spiegata.

**E una riga è "uscita" solo se ha `url_pubblicato` e quell'indirizzo risponde.** Non se lo stato
dice "pubblicato".

## B.3 Le fasi

| # | Fase | Cosa fa | Agente | Output | Ore |
|---|---|---|---|---|---:|
| **E1** | Inventario del magazzino | trova i contenuti già prodotti e mai usciti che si possono usare | `lan-edt-magazziniere` | `editoriale/00-riusabili.json` | 2 |
| **E2** | Struttura | distribuisce i tre tipi sui giorni, secondo le quote e le fasi | `lan-edt-conductor` | `editoriale/01-struttura.json` | 3 |
| **E3** | Riempimento | compila ogni riga fino all'ultimo campo, comando incluso | `lan-edt-redattore` | `piano-editoriale.json` | 8-12 |
| **GATE-EDT-1** | Completezza | nessuna riga incompleta, ogni giorno chiave coperto | `lan-qlt-gate` | verbale | 1 |
| **E4** | Ordine alle fabbriche | passa i brief alle fabbriche di contenuto esistenti | `lan-edt-conductor` | ordini | continuo |
| **E5** | Vigilanza | **ogni giorno controlla che ciò che doveva uscire sia uscito** | `lan-edt-sentinella` | `editoriale/pubblicazioni.json` | automatico |
| **E6** | Marcatura per il riuso | a lancio chiuso, marca i pezzi che valgono anche dopo | `lan-edt-magazziniere` | `editoriale/evergreen.json` | 2 |

## B.4 I tre tipi di contenuto

| Tipo | Quota | Cosa fa | Quando |
|---|---:|---|---|
| **Richiamo** | ~70% | porta gente nuova: risolve un problema in sé, senza vendere | tutto il periodo, più denso all'inizio |
| **Spostamento** | ~20% | cambia il modo in cui il pubblico vede il problema | concentrato nelle due settimane prima |
| **Conversione** | ~10% | chiede l'azione | dagli ultimi giorni in poi |

**Lo spostamento è la parte che quasi tutti saltano** ed è quella che fa la differenza fra un
lancio a cui la gente assiste e uno a cui partecipa: è il contenuto che **riformula il problema**.
Senza, l'offerta arriva a un pubblico che non ha ancora capito perché gli serve.

## B.5 Lo schema di una riga

```json
{
  "giorno": 12, "data": "2026-10-14", "fase": "T-16",
  "tipo": "richiamo | spostamento | conversione",
  "canale": "youtube", "formato": "video-lungo",
  "titolo": "il titolo vero, non un tema",
  "gancio_3_secondi": "le parole esatte dei primi tre secondi",
  "testo_accompagnamento": "la descrizione, scritta",
  "invito_azione": "cosa si chiede",
  "porta_a": "ingresso-organica | registrazione-webinar | pagina-vendita | nessuna",
  "fonte_materiale": "string | null",
  "prodotto_da": "fabbrica-youtube | fabbrica-caroselli | a-mano",
  "comando": "il comando già compilato",
  "responsabile": "un nome di persona, mai un ruolo",
  "stato": "da-produrre | prodotto | pubblicato",
  "pubblicato_il": "string | null",
  "url_pubblicato": "string | null"
}
```

**I tre campi che quasi nessun piano editoriale ha:** `porta_a` (un contenuto che non porta da
nessuna parte non serve al lancio) · `responsabile` con un nome vero · **`url_pubblicato`, l'unica
prova che un contenuto è uscito**.

## B.6 Il gate

| Controllo | Soglia |
|---|---|
| Righe con tutti i campi obbligatori | **100%** |
| Righe con `porta_a` valorizzato | 100% (`nessuna` è lecito ma va **scelto**) |
| Righe con un responsabile che è un nome | 100% |
| Giorni chiave coperti | 100% |
| Quote dei tre tipi entro ±10 punti | sì |
| Comando compilato dove la produzione è automatizzabile | 100% |

## B.7 Il rapporto con le fabbriche

**Il reparto Editoriale ordina e verifica. Non produce.** Se cominciasse a produrre, nascerebbe una
seconda fabbrica di contenuti dentro un ecosistema di lanci — il modo esatto in cui questo piano
fallirebbe.

**E il vincolo sulle copertine:** in questa azienda le copertine dei video **le fa una persona**,
non la macchina. Il piano editoriale prepara titolo e indicazioni, apre la cartella, e si ferma.

## B.8 Come si misura

| Metrica | Bersaglio |
|---|---|
| Righe complete al primo giro | ≥90% |
| **Contenuti prodotti che vengono pubblicati** | **100%** |
| Ritardo medio | ≤1 giorno |
| Contenuti riusati dal magazzino | ≥20% |
| Contenuti marcati per il riuso a fine lancio | ≥30% |

**La seconda riga è la ragione d'esistere di questo flusso.** Tutte le altre possono essere buone e
il lancio fallire lo stesso, se i contenuti restano in una cartella.

---

## C. COSA È CAMBIATO

| Cambiamento | Contro quale obiezione |
|---|---|
| Il funnel ha **nove fasi con l'agente che le esegue**, output tipizzato, handoff e fallimenti | *"dodici sezioni, zero agenti nominati: è il pre-mortem numero uno"* |
| Il reparto si chiama **`LAN-FNL`, sempre** | *"riceve handoff indirizzati a un nome che non ha"* |
| **Si avvolge il reparto Vendite & Funnel esistente**, e la skill di lancio | *"tre workflow e sei schede agente già scritti: zero occorrenze nel piano"* |
| La parametrizzazione dei componenti è **una fase con le sue ore** | *"il contratto dichiarato non esiste: verificato nel codice"* |
| I benchmark sono **marcati come provvisori** | *"vengono da un altro mercato e non è dichiarato"* |
| La prova di pubblicazione è **l'indirizzo, non il codice di uscita** | *"lo strumento di pubblicazione stampa ancora successo simulato ed esce zero"* |
| Le ore sostituiscono i giorni | *"le durate non tengono conto di quanto tempo esiste davvero"* |
