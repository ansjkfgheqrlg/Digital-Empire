# V1 — WORKFLOW FUNNEL E PIANO EDITORIALE
*(stesura di Emperator)*

---
---

# WF-3 — STRUTTURA E OTTIMIZZAZIONE DEL FUNNEL

## 1. Identità

| Campo | Valore |
|---|---|
| **Sigla** | `WF-FNL` |
| **Nome** | Workflow Funnel e Pagine |
| **Missione** | Mette online le pagine del lancio e **prova che misurano**. Una pagina che non produce un numero non è online: è pubblicata |
| **Proprietario** | Reparto **LAN-FNL** — avvolge le skill di costruzione siti già installate |
| **Durata** | 5-8 giorni per un funnel completo; 2-3 se le pagine esistono già e vanno solo verificate e collegate |

## 2. Trigger

| Tipo | Dettaglio |
|---|---|
| **Comando** | `/lancio-funnel <lancio_id>` |
| **Handoff in ingresso** | i testi delle pagine da LAN-CPY (almeno la pagina di vendita approvata) + `offerta.json` |
| **Precondizione dura** | la pagina di vendita deve aver superato il suo gate: costruire pagine su testi non approvati significa rifarle |

## 3. Input tipizzato

```json
{
  "lancio_id": "string",
  "tipo_funnel": "webinar | video-diretto | solo-pagina-vendita",
  "copy_manifest": "string — percorso al manifest dei testi",
  "offerta_path": "string",
  "dominio": "string — dove vivono le pagine",
  "strumento_pagamento": "string",
  "strumento_email": "string",
  "pagine_esistenti": [
    { "tipo": "string", "url": "string", "va_riusata": "boolean" }
  ],
  "sistema_visivo": "empire-premium-style | design-system-esistente",
  "canali_traffico": ["organico", "a-pagamento"]
}
```

**Il campo `canali_traffico` non è decorativo:** se contiene entrambi i valori, il workflow
**genera due pagine d'ingresso separate**. È la regola ereditata più importante e la più
disattesa: se il traffico gratuito e quello a pagamento atterrano sulla stessa pagina, il
confronto fra i due non è più misurabile e ogni numero successivo — costo di acquisizione
compreso — diventa una divisione fra grandezze scollegate.

## 4. Precondizioni

| # | Precondizione | Verifica |
|---|---|---|
| P1 | La pagina di vendita ha superato il gate del copy | il verbale esiste con esito positivo |
| P2 | `offerta.json` con prezzo e data | il gate del prezzo |
| P3 | Lo strumento di pagamento è configurato e prova una transazione | **transazione di prova reale, non simulata** |
| P4 | Il dominio risponde | controllo diretto |
| P5 | Il sistema visivo è deciso | vedi §9 |

## 5. Le nove pagine — la lista chiusa

| # | Pagina | Scopo | Cosa contiene | Da chi riceve i testi |
|---|---|---|---|---|
| 1 | **Ingresso (organica)** | raccogliere nome ed email dal traffico gratuito | promessa compressa, modulo, una sola azione | CPY |
| 1b | **Ingresso (a pagamento)** | idem dal traffico comprato | stessa promessa, **pagina separata** | CPY |
| 2 | **Regalo** | consegnare ciò che è stato promesso | il file, e il primo passo successivo | CPY |
| 3 | **Vendita aggiuntiva a 15 euro** | finanziare il funnel | video breve, offerta secca, una sola azione | CPY |
| 4 | **Registrazione al webinar** | far iscrivere all'evento | video da 8-12 minuti, data, modulo | CPY |
| 5 | **Webinar dal vivo e replica** | fare la presentazione | il player, la chat, l'invito all'azione che compare al momento giusto | CPY |
| 6 | **Pagina di vendita** | vendere | il documento madre per intero | CPY |
| 7 | **Cassa** | incassare | riepilogo, garanzia, pagamento, meno campi possibile | CPY |
| 8 | **Ringraziamento** | confermare e orientare | conferma, cosa succede adesso, il primo passo | CPY |
| 9 | **Aggiunte dopo l'acquisto** | aumentare il valore dell'ordine | offerta complementare, e l'alternativa più economica se rifiuta | CPY |

**Le pagine non necessarie si dichiarano, non si omettono.** Un funnel senza webinar salta la 4 e
la 5, e il manifest scrive *"non previste: tipo funnel video-diretto"*. Una pagina assente senza
dichiarazione è indistinguibile da una dimenticata.

## 6. Il percorso del visitatore

```
   contenuto gratuito ──► INGRESSO organica ──┐
                                              ├──► REGALO ──► VENDITA 15€ ──┐
   annuncio a pagamento ──► INGRESSO paid ────┘         │                   │
                                                        │ (rifiuta)         │
                                                        ▼                   ▼
                                              ┌──── sequenza email 3 giorni ────┐
                                              │                                 │
                                              ▼                                 │
                                    REGISTRAZIONE WEBINAR                       │
                                              │                                 │
                                              ▼                                 │
                                     WEBINAR (o replica)                        │
                                              │                                 │
                                              ▼                                 │
                                      PAGINA DI VENDITA ◄──────────────────────┘
                                              │
                                              ▼
                                            CASSA ──► RINGRAZIAMENTO ──► AGGIUNTE
                                              │
                                     (abbandona il carrello)
                                              │
                                              ▼
                                    recupero + ritorno alla lista
```

**I punti di uscita che vanno presidiati**, perché sono dove si perde la maggior parte delle
persone: chi non apre il regalo · chi rifiuta la vendita aggiuntiva · chi si iscrive al webinar e
non si presenta · chi arriva alla cassa e non paga.

**Per ognuno esiste un rientro**, e il rientro non è mai un'uscita definitiva: chi non compra
torna nella lista con frequenza ridotta. La regola ereditata è netta — *il nutrimento non si
interrompe mai: cambia la frequenza, non la lista*. Un contatto a sei mesi compra al lancio
successivo, e cancellarlo perché non ha comprato oggi è buttare il lavoro già pagato.

## 7. Il tracciamento — cosa si registra e chi lo verifica

| Pagina | Eventi da registrare |
|---|---|
| Ingresso | `pagina_vista` · `modulo_inviato` |
| Regalo | `regalo_scaricato` |
| Vendita 15€ | `offerta_vista` · `offerta_accettata` · `offerta_rifiutata` |
| Registrazione webinar | `iscrizione_completata` |
| Webinar | `presenza_iniziale` · `presenza_al_pitch` · `click_invito` |
| Vendita | `pagina_vista` · `prezzo_visto` (scorrimento fino al prezzo) · `click_acquista` |
| Cassa | `cassa_aperta` · `pagamento_avviato` · `pagamento_completato` · `pagamento_fallito` |
| Ringraziamento | `acquisto_confermato` |
| Aggiunte | `aggiunta_vista` · `aggiunta_accettata` |

**`prezzo_visto` è l'evento che nessuno registra e che spiega più di tutti gli altri.** Se molti
vedono la pagina e pochi arrivano al prezzo, il problema è la pagina; se molti arrivano al prezzo
e pochi comprano, il problema è il prezzo o l'offerta. Senza quell'evento le due diagnosi sono
indistinguibili, e si finisce per riscrivere una pagina che andava bene.

## 8. Il gate "online e funzionante" — il controllo, non l'opinione

Per **ogni** pagina, tutte le condizioni insieme:

| # | Controllo | Soglia | Automatico |
|---|---|---|---|
| 1 | La pagina risponde | codice 200 | sì |
| 2 | Tempo di risposta | **≤3 secondi** | sì |
| 3 | Le etichette di tracciamento sono nel codice | presenti | sì |
| 4 | **L'evento di conversione è scattato almeno una volta in prova** | ≥1 | sì, con una visita di prova |
| 5 | Resa su telefono | nessuno scorrimento orizzontale, testo ≥16px, pulsante ≥44px | sì |
| 6 | I collegamenti interni funzionano | 100% | sì |
| 7 | La pagina successiva del percorso esiste ed è raggiungibile | sì | sì |
| 8 | Cassa: **una transazione di prova reale è andata a buon fine** | 1 | **no: la fa una persona** |

**Il controllo 4 è quello che separa questo gate da un controllo di facciata.** Verificare che
l'etichetta sia nel codice non prova niente: si verifica che l'evento **sia arrivato**. Il modo è
brutale ed efficace — si visita la pagina, si compila il modulo con un indirizzo di prova, si
guarda se l'evento compare. Se non compare, la pagina non è online.

**Il controllo 8 non si automatizza mai**: implica un pagamento reale. Si fa con l'importo minimo
e si rimborsa, ma **si fa**. Un funnel dove nessuno ha mai provato a pagare è un funnel che
scopre il problema dal primo cliente vero.

**Lo script:** `scripts/gate_pagina.py`

| Funzione | Firma | Ritorna |
|---|---|---|
| `controlla_pagina` | `controlla_pagina(url: str, attesi: list[str]) -> dict` | i sette controlli automatici con esito e misura |
| `prova_evento` | `prova_evento(url: str, evento: str, timeout_s: int = 60) -> bool` | vero solo se l'evento è **arrivato** |
| `verifica_percorso` | `verifica_percorso(funnel: dict) -> list[str]` | i passaggi interrotti del percorso |
| `verbale` | `verbale(lancio_id: str) -> int` | scrive `funnel.json`, esce 1 se una pagina non passa |

## 9. Il conflitto sul sistema visivo — proposta di risoluzione

**Il conflitto:** esiste un design system scritto per la landing dell'ebook (54 righe di regole
molto specifiche: palette, tipografia, effetti, e le sette sezioni obbligatorie della pagina) e
una skill di stile premium installata nell'Impero. Descrivono lo stesso tipo di pagina con due
sistemi diversi.

**Proposta motivata:** **lo standard è la skill installata**, per tre ragioni — è una skill viva
e manutenuta, vale per tutto l'Impero e non per una pagina sola, ed è già stata applicata altrove.

**Ma non si butta niente** (vale la direttiva): le 54 righe dell'altro documento contengono due
cose che la skill non ha e che vanno **assorbite come profilo "lancio info-prodotto"**: la
struttura a sette sezioni della pagina di vendita, e la regola sull'uso del colore d'accento solo
per micro-dettagli e mai come fondo pieno.

**Chi decide davvero:** la guild Design. Questa è una proposta operativa, reversibile, e il
workflow non resta fermo ad aspettare la ratifica.

## 10. Il ciclo di ottimizzazione — perché non è un allarme

I benchmark sono ereditati e non si inventano:

| Punto | Verde | Giallo | Rosso |
|---|---|---|---|
| Iscrizione alla pagina d'ingresso | >35% | 20-35% | <20% |
| Vendita aggiuntiva 15€ | >15% | 8-15% | <8% |
| Iscrizione al webinar dal video | >20% | 10-20% | <10% |
| Presenza al webinar | >30% | 20-30% | <20% |
| Conversione del webinar | >5% | 2-5% | <2% |
| Recupero dopo il webinar | >15% | 8-15% | <8% |

**Il ciclo, quando un numero è giallo o rosso:**

```
1. IPOTESI      una frase sola, che dica la causa: "il titolo non nomina il problema"
2. VARIANTE     UNA modifica. Una sola. Due modifiche insieme non dicono quale ha funzionato
3. VOLUME       quante persone servono prima di poter decidere (sotto, non si decide)
4. DECISIONE    si tiene la variante, si torna indietro, o non si sa ancora
5. MEMORIA      l'esito va nello spazio del reparto, che vinca o che perda
```

**Il volume minimo, e questa è la parte che quasi tutti sbagliano:**

| Differenza che si vuole vedere | Visitatori per versione |
|---|---:|
| grande (dal 20% al 30%) | ~300 |
| media (dal 20% al 25%) | ~1.200 |
| piccola (dal 20% al 22%) | ~7.000 |

**La conseguenza pratica che va detta a chiare lettere:** con il traffico di un lancio piccolo
si possono vedere solo le differenze **grandi**. Un test su una modifica minuscola con 200
visitatori non dà una risposta: dà rumore che sembra una risposta. **Quindi si testano solo cose
grosse** — un titolo completamente diverso, un'offerta diversa, una struttura diversa — e le
rifiniture si decidono per mestiere, non per test.

**Chi decide:** il capo del reparto Funnel se la modifica è dentro una pagina; il direttore
dell'ecosistema se la modifica tocca l'offerta o il prezzo.

## 11. Cosa si avvolge, invece di riscrivere

| Cosa esiste | Dove | Come si usa |
|---|---|---|
| Skill di costruzione e pubblicazione siti | installate | le chiama il reparto Funnel |
| Skill di stile premium | installata | è il sistema visivo standard |
| Skill per moduli e iscrizioni | installata | pagine d'ingresso |
| **~30 componenti già scritti**, fra cui **4 di gestione obiezioni** | progetto della landing esistente | **si indicizzano e si riusano.** I quattro componenti di gestione obiezioni sono la cosa più preziosa: sono lavoro già fatto su un problema difficile |
| La landing già costruita | progetto dell'ebook | si **verifica e si collega**, non si rifà |

**Come si riusano i componenti senza confondere i mestieri:** il reparto Copy **non scrive
codice**. Consegna il contenuto di ogni obiezione in un file strutturato, campo per campo, sui
parametri che i componenti si aspettano. Il reparto Funnel li monta. Se un'obiezione importante
non ha un componente corrispondente, il manifest lo dichiara e il reparto Funnel decide se
estendere la libreria — è area sua.

## 12. Come si misura

| Metrica | Bersaglio |
|---|---|
| Pagine che superano tutti i controlli prima dell'apertura | **100%** |
| Eventi di conversione verificati almeno una volta | **100%** |
| Transazione di prova eseguita | **1, sempre** |
| Pagine d'ingresso separate quando ci sono due tipi di traffico | 100% |
| Test decisi sotto il volume minimo | **0** |

---
---

# WF-5 — CONTENUTI E PIANO EDITORIALE DEL LANCIO

## 1. Identità

| Campo | Valore |
|---|---|
| **Sigla** | `WF-EDT` |
| **Nome** | Workflow Editoriale del Lancio |
| **Missione** | Riempie i 37 giorni del lancio di contenuti che **portano dentro il funnel**, e garantisce che escano davvero |
| **Proprietario** | Reparto **LAN-EDT** — ordina alle fabbriche di contenuto, non produce da sé |
| **Durata** | 2 giorni per il piano; poi la produzione segue il calendario |

## 2. Il difetto che questo workflow esiste per impedire

Nell'Impero è documentato un problema preciso: **contenuti finiti che non escono mai.**
Venticinque pezzi completati e mai pubblicati, il più vecchio fermo da 135 giorni.

**Non è un problema di produzione: è un problema di consegna.** E in un lancio è letale, perché
un contenuto che esce tre giorni dopo la chiusura del carrello non vale zero — vale meno di zero,
perché ha consumato la produzione che serviva altrove.

**Il presidio, e ha tre parti:**

1. **Nessuna riga del piano è "pronta" finché non ha una data di pubblicazione e un responsabile
   con un nome.**
2. **Un contenuto prodotto e non pubblicato entro 48 ore dalla sua data diventa un blocco
   visibile** nello stato del lancio, non una nota.
3. **Alla chiusura del lancio, il debrief conta i pezzi prodotti contro i pezzi usciti.** Se la
   differenza è maggiore di zero, va spiegata.

## 3. Input tipizzato

```json
{
  "lancio_id": "string",
  "data_apertura": "string ISO",
  "durata_carrello_gg": "number",
  "grande_promessa": "string — dal fondamento del copy",
  "canali": [
    { "canale": "youtube | instagram | email | tiktok | linkedin",
      "cadenza_settimanale": "number",
      "formati": ["video-lungo", "video-breve", "carosello", "post", "storia"] }
  ],
  "fabbriche_disponibili": ["youtube", "caroselli", "pubblicazione-automatica"],
  "contenuti_riusabili": ["percorso a pezzi già pronti e mai usciti"]
}
```

**Il campo `contenuti_riusabili` è deliberato:** il primo posto dove cercare contenuti per un
lancio è il magazzino di ciò che è già stato prodotto e mai pubblicato. Ventisei pezzi fermi sono
ventisei giorni di calendario già coperti.

## 4. La struttura dei tre tipi di contenuto

| Tipo | Quota | Cosa fa | Quando esce |
|---|---:|---|---|
| **Richiamo** | ~70% | porta gente nuova: risolve un problema in sé, senza vendere niente | tutto il periodo, più denso da T-30 a T-10 |
| **Spostamento** | ~20% | cambia il modo in cui il pubblico vede il problema, così che la soluzione diventi ovvia | concentrato da T-14 a T-3 |
| **Conversione** | ~10% | chiede l'azione: iscriviti, guarda, compra | da T-3 in poi, e durante la vendita |

**Perché le quote in quest'ordine.** Un calendario fatto solo di richiamo porta pubblico che non
compra; uno fatto solo di conversione brucia il pubblico che ha. Lo spostamento è la parte che
quasi tutti saltano ed è quella che fa la differenza fra un lancio a cui la gente assiste e uno a
cui partecipa: è il contenuto che **riformula il problema**, e senza di lui l'offerta arriva a
un pubblico che non ha ancora capito perché gli serve.

## 5. Lo schema di una riga di piano — il livello richiesto

Chi esegue una riga **non deve decidere niente**. Il modello è il piano editoriale già
funzionante dell'Impero, dove ogni riga contiene perfino il comando pronto da eseguire.

```json
{
  "giorno": 12,
  "data": "2026-10-14",
  "fase": "T-16",
  "tipo": "richiamo | spostamento | conversione",
  "canale": "youtube",
  "formato": "video-lungo",
  "titolo": "string — il titolo vero, non un tema",
  "gancio_3_secondi": "string — le parole esatte dei primi tre secondi",
  "struttura": ["apertura", "problema", "dimostrazione", "conclusione"],
  "testo_accompagnamento": "string — la descrizione o didascalia, scritta",
  "invito_azione": "string — cosa si chiede",
  "porta_a": "ingresso-organica | registrazione-webinar | pagina-vendita | nessuna",
  "fonte_materiale": "string | null — se riusa un pezzo già prodotto",
  "prodotto_da": "fabbrica-youtube | fabbrica-caroselli | a-mano",
  "comando": "string — il comando già compilato da eseguire",
  "responsabile": "string — un nome di persona, mai un ruolo generico",
  "stato": "da-produrre | prodotto | pubblicato",
  "pubblicato_il": "string | null",
  "url_pubblicato": "string | null"
}
```

**I tre campi che quasi nessun piano editoriale ha e che qui sono obbligatori:**
`porta_a` (un contenuto che non porta da nessuna parte nel funnel non serve al lancio) ·
`responsabile` con un nome vero · `url_pubblicato`, che è **la sola prova che un contenuto è
uscito davvero**.

## 6. Le fasi

| # | Fase | Cosa fa | Agente | Output | Durata |
|---|---|---|---|---|---|
| **E1** | Inventario del magazzino | Cerca i contenuti già prodotti e mai usciti che si possono usare | `lan-edt-magazziniere` | `editoriale/00-riusabili.json` | 2 h |
| **E2** | Struttura del calendario | Distribuisce i tre tipi sui 37 giorni secondo le quote e le fasi | `lan-edt-pianificatore` | `editoriale/01-struttura.json` | 3 h |
| **E3** | Riempimento delle righe | Compila ogni riga con tutti i campi, incluso il comando | `lan-edt-redattore` | `piano-editoriale.json` | 1 g |
| **GATE G7** | Completezza | nessuna riga incompleta, ogni giorno chiave coperto | `lan-qlt-gate-piano` | `gate/G7-verbale.json` | 1 h |
| **E4** | Ordine alle fabbriche | Passa i brief alle fabbriche di contenuto esistenti | `lan-edt-committente` | ordini | continuo |
| **E5** | Vigilanza sulla pubblicazione | Ogni giorno controlla che ciò che doveva uscire sia uscito | `lan-edt-sentinella` | `editoriale/pubblicazioni.json` | automatico |
| **E6** | Marcatura per il riuso | A lancio chiuso, marca i pezzi che valgono anche dopo | `lan-edt-magazziniere` | `editoriale/evergreen.json` | 2 h |

## 7. Il gate del piano editoriale

| Controllo | Soglia |
|---|---|
| Righe con tutti i campi obbligatori | **100%** |
| Righe con `porta_a` valorizzato | **100%** (`nessuna` è un valore lecito ma va scelto, non lasciato vuoto) |
| Righe con un responsabile che è **un nome** | 100% |
| Giorni chiave coperti (T-14 inizio, T-3 conversione, T-0, ultimo giorno) | 100% |
| Quote dei tre tipi entro ±10 punti percentuali dal bersaglio | sì |
| Righe con comando compilato, dove la produzione è automatizzabile | 100% |

**Chi lo esegue:** il gate della Qualità, mai chi ha scritto il piano.

## 8. Il rapporto con le fabbriche esistenti

| Fabbrica | Cosa produce | Come la si chiama |
|---|---|---|
| Fabbrica video YouTube | video lunghi e brevi | si passa il brief; lei produce con i suoi gate |
| Fabbrica caroselli | caroselli per social | idem |
| Pubblicazione automatica | mette online su Instagram e TikTok | riceve il pezzo finito e la data |

**Il reparto Editoriale ordina e verifica. Non produce.** Se cominciasse a produrre, nascerebbe
una seconda fabbrica di contenuti dentro un ecosistema di lanci, e sarebbe il modo esatto in cui
questo piano fallirebbe.

**Il vincolo che va rispettato e che riguarda le copertine:** in questa azienda esiste una regola
netta per cui le copertine dei video **le fa una persona**, non la macchina. Il piano editoriale
prepara titolo e indicazioni, apre la cartella, e si ferma lì.

## 9. Il punto di sincronizzazione con lo sprint parallelo

I tre reparti — testi, funnel, editoriale — lavorano insieme fra T-22 e T-14. Prima
dell'apertura, tutti e tre devono essere veri **insieme**:

| Reparto | Cosa deve essere vero |
|---|---|
| Testi | tutti i pezzi superano il gate |
| Funnel | tutte le pagine rispondono e tracciano |
| **Editoriale** | il piano è approvato **e i contenuti pre-lancio sono già usciti** |

**L'ultima voce è quella che si dimentica.** Un piano editoriale approvato con zero contenuti
pubblicati significa che il lancio si apre davanti a un pubblico che non è stato scaldato. Il
gate lo verifica contando gli `url_pubblicato` prima di T-1.

## 10. Gli eseguibili

`scripts/piano_editoriale.py`

| Funzione | Firma | Ritorna |
|---|---|---|
| `struttura` | `struttura(data_apertura: str, durata_gg: int, canali: list[dict]) -> dict` | lo scheletro dei 37 giorni con le quote rispettate |
| `verifica_completezza` | `verifica_completezza(piano: dict) -> list[dict]` | le righe incomplete, campo per campo |
| `copertura_funnel` | `copertura_funnel(piano: dict) -> dict` | quanti contenuti portano a ciascuna destinazione |
| `non_pubblicati` | `non_pubblicati(piano: dict, oggi: str) -> list[dict]` | **i pezzi prodotti e non usciti oltre le 48 ore** |
| `evergreen` | `evergreen(piano: dict) -> list[dict]` | i pezzi che valgono anche dopo il lancio |

## 11. Skill e comando

`/lancio-editoriale <id>` genera il piano · `--verifica` esegue il gate ·
`--oggi` stampa cosa deve uscire oggi e con quale comando.

**Se manca la grande promessa:** si ferma. Un piano editoriale costruito prima che il messaggio
sia deciso produce trenta contenuti che parlano di trenta cose diverse.

## 12. Come si misura

| Metrica | Bersaglio |
|---|---|
| Righe complete al primo giro | ≥90% |
| **Contenuti prodotti che vengono pubblicati** | **100%** |
| Ritardo medio fra data prevista e pubblicazione | ≤1 giorno |
| Contenuti riusati dal magazzino | ≥20% del piano |
| Contenuti marcati per il riuso a lancio chiuso | ≥30% |

**La seconda riga è la ragione d'esistere di questo workflow.** Tutte le altre metriche possono
essere buone e il lancio fallire lo stesso, se i contenuti restano in una cartella.

---

## OBIEZIONI

**Contro WF-3 — «Trentasette giorni di funnel a nove pagine per vendere un ebook: chi le costruisce tutte?»**
Nessuno, ed è previsto. Il tipo di funnel determina quali pagine servono: un lancio diretto ne usa
quattro. Le nove sono la lista **completa**, non l'obbligo. Quello che non è negoziabile è il
gate: le pagine che esistono devono misurare.

**Contro WF-3 — «Il volume minimo per i test rende l'ottimizzazione inutile a questi numeri.»**
È vero e va detto invece che nascosto: con poche centinaia di visitatori si vedono solo le
differenze grandi. Per questo il workflow **vieta** i test sotto il volume minimo invece di
consentirli e far credere ai loro risultati. Una decisione presa su rumore è peggio di una
decisione presa per mestiere.

**Contro WF-5 — «Il piano a questo livello di dettaglio richiede più lavoro dei contenuti stessi.»**
Parzialmente vero al primo giro, falso dal secondo: la struttura si genera, le righe riusano
schemi già scritti, e il magazzino copre una parte del calendario. Il confronto giusto non è
"piano contro nessun piano", è "piano contro trenta decisioni prese di corsa la mattina stessa" —
ed è lì che nascono i pezzi che non escono.

**Contro WF-5 — «La vigilanza sulla pubblicazione è l'ennesimo controllo che nessuno guarderà.»**
Per questo non è un rapporto ma **un blocco nello stato del lancio**: un contenuto in ritardo di
48 ore compare dove si guarda lo stato, non in un file separato. È l'unica forma di allarme che
in questa azienda ha funzionato.

---

## SEGNALAZIONI

1. Le etichette di tracciamento dipendono dagli strumenti realmente in uso, che questo piano non
   ha verificato. Vanno accertati prima dello scaglione S1.
2. La transazione di prova richiede uno strumento di pagamento configurato: se non c'è, è un
   prerequisito del primo lancio e non un dettaglio del funnel.
3. Il magazzino dei contenuti mai pubblicati va inventariato prima del primo lancio: qui se ne
   assume l'esistenza sulla base di un dato documentato, non di una verifica fatta ora.
