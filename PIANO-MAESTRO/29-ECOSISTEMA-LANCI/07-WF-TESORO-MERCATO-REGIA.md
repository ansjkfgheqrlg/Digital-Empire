# V1 — WORKFLOW SPESE, MERCATO ED ESECUZIONE
*(stesura di Emperator, non delegata — il servizio subagenti era giù)*

---
---

# WF-4 — SPESE E CONTROLLO BUDGET

## 1. Identità

| Campo | Valore |
|---|---|
| **Sigla** | `WF-TSR` |
| **Nome** | Workflow Tesoro del Lancio |
| **Missione** | Sa **quanto costa questo lancio ogni giorno** e **quante vendite servono per rientrare**, e blocca la spesa quando esce dal seminato |
| **Proprietario** | Reparto **LAN-TSR** — avvolge `14-TESORERIA`, non la sostituisce |
| **Durata** | vive per tutta la durata del lancio: nasce a T-30 e chiude 7 giorni dopo la chiusura del carrello |

**Il confine con la Tesoreria dell'Impero, ed è la cosa più importante di questo workflow:**

> **La Tesoreria è la fonte di verità sui soldi dell'azienda. LAN-TSR è la fonte di verità sui
> soldi di *questo lancio*.** Ogni euro nasce nel lancio e **sale** in Tesoreria. Non scende mai.
> Se un euro compare in tutti e due i posti con due valori diversi, **ha ragione la Tesoreria** —
> e la divergenza è un difetto da registrare, non un arrotondamento.

Senza questa regola nascono due contabilità, ed è la fine di entrambe.

## 2. Trigger

| Tipo | Dettaglio |
|---|---|
| **Comando** | `/lancio-budget <lancio_id>` per costruire il budget · `/lancio-spesa <lancio_id> --registra` per un movimento · `/lancio-costi <lancio_id>` per lo stato |
| **Handoff in ingresso** | `offerta.json` accettato: senza prezzo non si calcola il punto di pareggio |
| **Automatico** | la sentinella dei costi gira ogni giorno durante il lancio, senza che nessuno la chiami |

## 3. Input tipizzato

`lanci/<id>/input-budget.json`

```json
{
  "lancio_id": "string",
  "offerta_path": "string",
  "canali_previsti": ["organico | ads-meta | ads-google | ads-youtube | email | partner"],
  "budget_massimo": "number — l'importo oltre il quale non si va, deciso da una persona",
  "valuta": "EUR",
  "voci": [
    {
      "voce": "pubblicita | strumenti | produzione-contenuti | crediti-ia | servizi-esterni | commissioni | rimborsi | altro",
      "descrizione": "string",
      "importo_previsto": "number",
      "ricorrente": "boolean",
      "canale": "string | null",
      "gia_pagato": "boolean"
    }
  ],
  "commissione_pagamento_pct": "number — default 3.5 se non dichiarata, e il default va scritto",
  "rimborso_atteso_pct": "number — default 5, dalla soglia dell'Impero"
}
```

| Campo | Obbligatorio | Se manca |
|---|---|---|
| `lancio_id` | ✅ | esce con codice 2, nessun file scritto |
| `offerta_path` | ✅ | esce con codice 2 — senza prezzo il pareggio non esiste |
| `budget_massimo` | ✅ | **esce con codice 2**: un lancio senza tetto di spesa non è un lancio, è una speranza |
| `voci` | ✅ almeno una | codice 2 |
| `commissione_pagamento_pct` | ⬜ | usa 3,5 **e lo scrive** nel campo `assunzioni` del budget |
| `rimborso_atteso_pct` | ⬜ | usa 5 **e lo scrive** |

**La regola del default dichiarato:** ogni valore non fornito viene sostituito da un default
**che finisce scritto nell'output**. Un numero assunto e non dichiarato è un numero che nessuno
ricontrollerà mai.

## 4. Precondizioni

| # | Precondizione | Verifica |
|---|---|---|
| P1 | `offerta.json` esiste con `prezzo` numerico > 0 | `costi.py --check-offerta` esce 0 |
| P2 | Il lancio è almeno in stato `DATATO` | `stato_lancio.py leggi` |
| P3 | Nessun `budget.json` già presente (serve `--rifai` per sovrascrivere) | esistenza file |
| P4 | La Tesoreria dell'Impero è raggiungibile in lettura | apertura del suo registro |

## 5. Le fasi

| # | Fase | Cosa fa | Agente | Output | Durata | Umano |
|---|---|---|---|---|---|---|
| **T1** | Costruzione del budget | Somma le voci, applica i default dichiarati, confronta il totale col tetto massimo | `lan-tsr-pianificatore` | `budget.json` | 1 h | **Sì**: il tetto lo fissa una persona |
| **T2** | Punto di pareggio | Calcola quante vendite servono per rientrare, in tre scenari (prudente, atteso, buono) | `lan-tsr-pianificatore` | dentro `budget.json`, sezione `pareggio` | 0,5 h | no |
| **T3** | Prova a secco | Simula la spesa completa **senza spendere**: proietta il costo per canale sui volumi attesi e dice se il tetto regge | `lan-tsr-simulatore` | `dry-run-costi.md` | 1 h | no |
| **GATE G8-a** | Approvazione del budget | totale ≤ tetto **e** pareggio calcolato **e** ogni assunzione dichiarata | `lan-qlt-gate-costi` | `gate/G8a-verbale.json` | — | **Sì**: firma di chi mette i soldi |
| **T4** | Registrazione dei movimenti | Ogni spesa reale entra con data, voce, canale, importo, prova (ricevuta o schermata) | `lan-tsr-registratore` | `spesa.json` (righe che si appendono) | continuo | **Sì**: molti importi si inseriscono a mano |
| **T5** | Vigilanza quotidiana | Ogni giorno ricalcola lo scarto fra speso e previsto, e il costo di acquisizione per canale | `lan-tsr-sentinella` | `tracking/costi-<data>.json` | automatico | no |
| **GATE G8-b** | Lo scarto | scarto fra reale e previsto **> 10% → BLOCCO** della spesa ulteriore | `lan-qlt-gate-costi` | `gate/G8b-verbale.json` | — | sblocco **solo umano** |
| **T6** | Consuntivo | A lancio chiuso: quanto è costato, quanto ha reso, il margine, e **dove la previsione ha sbagliato** | `lan-tsr-consuntivo` | `consuntivo.md` | 2 h | no |
| **T7** | Salita in Tesoreria | Passa costi e ricavi definitivi alla Tesoreria dell'Impero | `lan-tsr-consuntivo` | handoff | 0,5 h | no |

## 6. I gate

| Sigla | Criterio | Chi lo esegue | Se blocca | Come si sblocca |
|---|---|---|---|---|
| **G8-a** | `totale_previsto ≤ budget_massimo` ∧ `pareggio` calcolato ∧ 100% delle assunzioni dichiarate | `lan-qlt-gate-costi` (non il pianificatore) | il lancio non passa a `IN_PRODUZIONE` | si taglia una voce, o **una persona alza il tetto lasciandolo scritto** |
| **G8-b** | `(speso − previsto_a_oggi) / previsto_a_oggi ≤ 0,10` | `lan-tsr-sentinella` propone, `lan-qlt-gate-costi` verbalizza | **si ferma ogni spesa nuova**, il resto del lancio continua | **solo una firma umana** in `deroghe.json`, con importo, motivo e nuovo tetto. Nessuna deroga di macchina, mai |
| **G8-c** | il consuntivo esiste e i suoi totali coincidono con la Tesoreria entro l'1% | `lan-tsr-consuntivo` | il lancio non passa a `APPRESO` | si sana la divergenza; se resta, si registra come difetto |

**Perché G8-b blocca solo la spesa e non il lancio:** fermare un lancio a metà per uno sforamento
costa più dello sforamento. Ma continuare a spendere alla cieca è come si perdono i soldi due
volte. Il compromesso è chirurgico: **il lancio va avanti con ciò che è già pagato**, e ogni euro
nuovo richiede una firma.

## 7. Output tipizzato

```json
{
  "lancio_id": "string",
  "valuta": "EUR",
  "budget_massimo": 800.00,
  "totale_previsto": 735.00,
  "voci": [ { "voce": "pubblicita", "canale": "ads-meta", "previsto": 400.00, "speso": 0.00 } ],
  "assunzioni": [
    "commissione di pagamento 3,5% — default, non verificata sul fornitore reale",
    "rimborsi attesi 5% — soglia dell'Impero, non misurata su questo prodotto"
  ],
  "pareggio": {
    "prezzo": 47.00,
    "ricavo_netto_unitario": 43.13,
    "vendite_per_pareggio": 18,
    "scenari": { "prudente": 12, "atteso": 30, "buono": 60 },
    "formula": "ceil(totale_previsto / (prezzo * (1 - commissione) * (1 - rimborsi)))"
  },
  "stato": "APPROVATO | BLOCCATO | IN_DEROGA"
}
```

## 8. Le formule, scritte per intero

```
ricavo_netto_unitario = prezzo × (1 − commissione_pct/100) × (1 − rimborso_pct/100)

vendite_per_pareggio  = arrotonda_per_eccesso( totale_previsto / ricavo_netto_unitario )

costo_acquisizione(canale) = spesa(canale) / clienti_paganti_attribuiti(canale)
   ⚠️ se i clienti attribuiti sono 0, il costo NON è infinito: è **non calcolabile**,
      e si scrive "non calcolabile", non un numero enorme

ritorno_sulla_spesa(canale) = ricavo_attribuito(canale) / spesa(canale)

margine_lancio = ricavo_totale_netto − costo_totale_reale

scarto_pct = (speso − previsto_a_oggi) / previsto_a_oggi × 100
```

**La nota sull'attribuzione, che è il punto debole di tutti i calcoli di questo tipo:**
l'attribuzione per canale è **un'assunzione**, non una misura, a meno che ogni canale non abbia
la sua pagina d'ingresso separata. Per questo la regola ereditata — *mai mischiare traffico
organico e a pagamento sulla stessa pagina* — non è pignoleria: **è la sola cosa che rende il
costo di acquisizione un numero vero invece che una divisione fra due numeri scollegati.**

## 9. Fallimenti

| Sintomo | Causa | Cosa fa il sistema |
|---|---|---|
| Nessuno registra le spese per tre giorni | inserimento manuale saltato | la sentinella segnala l'assenza di movimenti come **anomalia**, non come "zero spese" |
| Il costo di acquisizione è enorme | pochi clienti attribuiti | si scrive "non significativo sotto i 10 clienti", non un numero fuorviante |
| Il consuntivo non torna con la Tesoreria | doppio conteggio o movimento mancante | G8-c blocca il passaggio a `APPRESO` e la divergenza va nel registro dei difetti |
| Il tetto viene alzato ogni volta che si tocca | la deroga è diventata routine | **tre deroghe sullo stesso lancio obbligano a rifare il budget da capo**: un tetto derogato tre volte non è un tetto |
| Una spesa non ha prova | ricevuta mancante | il movimento si registra con `prova: null` **e resta segnalato**: non si rifiuta il fatto, si rifiuta di fingere che sia documentato |

## 10. Gli eseguibili

`scripts/costi.py`

| Funzione | Firma | Ritorna |
|---|---|---|
| `costruisci_budget` | `costruisci_budget(input_path: str) -> dict` | il budget con default dichiarati in `assunzioni` |
| `calcola_pareggio` | `calcola_pareggio(prezzo: float, totale: float, commissione: float, rimborsi: float) -> dict` | vendite per il pareggio + i tre scenari |
| `registra_spesa` | `registra_spesa(lancio_id: str, voce: str, importo: float, prova: str \| None) -> dict` | la riga appesa a `spesa.json` |
| `scarto` | `scarto(lancio_id: str, alla_data: str) -> float` | la percentuale di scarto sul previsto a quella data |
| `costo_acquisizione` | `costo_acquisizione(lancio_id: str, canale: str) -> float \| None` | `None` quando non è calcolabile — **mai un numero finto** |
| `consuntivo` | `consuntivo(lancio_id: str) -> dict` | costi, ricavi, margine, scarti fra previsione e realtà |

`scripts/dry_run_costi.py`

| Funzione | Firma | Ritorna |
|---|---|---|
| `simula` | `simula(budget: dict, volumi_attesi: dict) -> dict` | la proiezione della spesa, **senza spendere niente** |
| `verdetto` | `verdetto(simulazione: dict, tetto: float) -> tuple[bool, list[str]]` | (regge sì/no, elenco delle voci che sfondano) |

Codici di uscita comuni a tutto l'ecosistema: **0** superato · **1** bloccato con verbale ·
**2** input non valido, nessun file scritto · **3** problema d'ambiente, si può riprovare.

## 11. Skill e comando

`.claude/skills/lancio-budget/SKILL.md` → `/lancio-budget <id>`.
**Se manca `offerta.json`**: stampa *"manca il prezzo: il blocco è del reparto Offerta, gate G4"*
ed esce 2. Non inventa un prezzo di lavoro nemmeno per simulare — un numero di comodo dentro un
budget diventa il numero vero al terzo file che lo copia.

## 12. Come si misura che ha funzionato

| Metrica | Bersaglio |
|---|---|
| Lanci con punto di pareggio calcolato prima di spendere | **100%** |
| Scarto finale fra budget e spesa reale | **≤10%** |
| Movimenti senza prova | ≤10% del totale |
| Divergenze con la Tesoreria a fine lancio | **0** |
| Costo di acquisizione disponibile per canale | 100% dei canali con pagina d'ingresso separata |

---
---

# WF-6 — MERCATO E CONCORRENTI

## 1. Identità

| Campo | Valore |
|---|---|
| **Sigla** | `WF-INT` |
| **Nome** | Workflow Intelligence di Mercato |
| **Missione** | Porta al lancio **le parole vere del pubblico** e **i buchi veri dei concorrenti**, con la fonte accanto a ogni affermazione |
| **Proprietario** | Reparto **LAN-INT** — avvolge `08-INTELLIGENCE` |
| **Durata** | 2-4 giorni la prima volta su un mercato; 0,5 giorni per un aggiornamento |

## 2. Trigger

`/lancio-ricerca <lancio_id>` · si attiva dopo il verdetto positivo della Strategia · si
riattiva automaticamente quando la ricerca scade (§7).

## 3. Input tipizzato

```json
{
  "lancio_id": "string",
  "prodotto": "string",
  "pubblico_ipotizzato": "string — mai 'chiunque voglia imparare X'",
  "mercato": "string",
  "concorrenti_noti": ["string"],
  "fonti_da_battere": ["amazon | udemy | reddit | youtube-commenti | gruppi-facebook | forum | recensioni-google"],
  "ricerca_precedente": "string | null — percorso a una ricerca da aggiornare invece che rifare"
}
```

## 4. Precondizioni

| # | Precondizione |
|---|---|
| P1 | Il pubblico ipotizzato è specifico: se contiene "chiunque", "tutti quelli che", "persone interessate a" → si rifiuta con codice 2 |
| P2 | Almeno due fonti da battere dichiarate |
| P3 | Se esiste una ricerca precedente sullo stesso mercato di meno di 12 mesi, **si aggiorna, non si rifà** |

## 5. Le fasi

| # | Fase | Cosa fa | Agente | Output | Durata | Umano |
|---|---|---|---|---|---|---|
| **I1** | Consultazione della memoria | Cerca cosa l'Impero sa già su questo mercato — è la fase zero obbligatoria | `lan-int-bibliotecario` | `ricerca/00-gia-noto.json` | 0,5 h | no |
| **I2** | Raccolta delle voci | Raccoglie le frasi vere del pubblico dalle fonti, **ognuna con l'indirizzo esatto** | `lan-int-ascoltatore` | `ricerca/01-voci.json` | 1 g | no |
| **I3** | Dolori | Raggruppa le voci in punti di dolore distinti, ordinati per frequenza | `lan-int-analista` | `ricerca/02-dolori.json` | 0,5 g | no |
| **I4** | Concorrenti | Per ogni concorrente: offerta, prezzo, promessa, funnel, canali, **e soprattutto le recensioni a una e due stelle** | `lan-int-osservatore` | `ricerca/03-concorrenti.json` | 1 g | no |
| **I5** | Spazi vuoti | Ciò che nessun concorrente copre, ricavato dalle lamentele ricorrenti | `lan-int-analista` | `ricerca/04-spazi.json` | 0,5 g | no |
| **I6** | Obiezioni | La mappa delle obiezioni ordinata per **frequenza × intensità** | `lan-int-analista` | `ricerca/05-obiezioni.json` | 0,5 g | no |
| **I7** | Tono di voce | 20-30 frasi vere che mostrano come parla questo pubblico | `lan-int-ascoltatore` | `ricerca/06-tono.json` | 0,5 g | no |
| **GATE G2** | **Anti-invenzione** | il controllo che decide se questa ricerca esiste davvero | `lan-qlt-gate-fonti` | `gate/G2-verbale.json` | 1 h | no |
| **I8** | Archiviazione | Ogni pezzo diventa un record del registro, deduplicato | `lan-int-archivista` | `memoria/intelligence/` | 0,5 h | no |

## 6. Il gate anti-invenzione — il cuore di questo workflow

**Criterio, tutto insieme e tutto obbligatorio:**

| Controllo | Soglia | Come si verifica |
|---|---|---|
| Numero di frasi | **≥15** | conteggio |
| Frasi con fonte | **100%** | ogni frase ha un indirizzo, e nessun campo vuoto passa |
| Fonti raggiungibili | **≥90%** risponde | si prova ad aprirle davvero |
| **Verifica a campione** | **3 frasi estratte a caso devono comparire nella pagina che le cita** | si apre la pagina e si cerca il testo |
| Dolori distinti | ≥5 | conteggio, con controllo che non siano lo stesso dolore riscritto |
| Concorrenti analizzati | ≥3 | ognuno con almeno prezzo e promessa compilati |
| Spazi vuoti | ≥3 | ognuno collegato ad almeno una lamentela vera |
| Frasi di tono | ≥20 | conteggio |

**La verifica a campione è ciò che separa questo gate dalla buona intenzione.** Contare quindici
frasi è facile e si può fare inventandole. Aprire tre pagine a caso e cercarci dentro la frase
citata non si può falsificare senza costruire pagine finte — e a quel punto il problema non è più
il gate.

**Se fallisce:** la ricerca torna al mittente col conteggio esatto (*"frasi: 12 su 15; fonti
irraggiungibili: 2; verifica a campione: 1 su 3 fallita"*). Al secondo fallimento sullo stesso
lancio, sale al direttore.

## 7. Cosa scade, e quando

| Cosa | Scadenza | Cosa si fa alla scadenza |
|---|---|---|
| Prezzi dei concorrenti | **3 mesi** | si ricontrollano solo quelli, non tutta la ricerca |
| Offerta e promessa dei concorrenti | 6 mesi | idem |
| Frasi del pubblico e dolori | 12 mesi | si aggiungono le nuove, le vecchie restano marcate come datate |
| Spazi vuoti | 6 mesi | vanno riconfermati: uno spazio vuoto che resta vuoto per anni di solito è vuoto per una ragione |
| Tono di voce | 12 mesi | |

**Il monitoraggio continuo** è un aggiornamento incrementale, non una ricerca nuova: costa mezza
giornata invece di quattro, e questo è precisamente il motivo per cui il registro deve avere
identificativi stabili.

## 8. Lo schema del registro

```json
{
  "id": "INT-<AREA>-<PROGRESSIVO>-<AAMMGG>",
  "tipo": "voce | dolore | concorrente | spazio | obiezione | tono",
  "mercato": "string",
  "contenuto": "string",
  "fonte": "string — indirizzo o percorso; MAI vuoto",
  "raccolto_il": "ISO",
  "scade_il": "ISO",
  "frequenza": "number — quante volte è comparso",
  "intensita": "1-5 — quanto è forte, solo per dolori e obiezioni",
  "contraddice": ["INT-..."],
  "sostituisce": "INT-... | null",
  "verificato": "boolean — ha passato la verifica a campione?"
}
```

**Le quattro regole di integrità** (le stesse già in uso nell'Impero, non inventate qui):
un identificativo non si riassegna mai · un record aggiornato mantiene il suo identificativo e
riempie `sostituisce` · la deduplicazione è un passo esplicito · il campo `contraddice` esiste
perché due fonti vere possono dire cose opposte, e nasconderlo è peggio che dichiararlo.

## 9. Il confine con la biblioteca dell'Impero

| Chi | Possiede |
|---|---|
| `conoscenza-empire` (agente esistente) | **tutta la formazione dell'Impero**: metodi, framework, corsi studiati. È il fornitore unico |
| `08-INTELLIGENCE` | l'intelligence generale sui mercati e i concorrenti dell'azienda |
| **LAN-INT** | **solo la ricerca legata a un lancio specifico** |

**La regola che evita la seconda biblioteca:** LAN-INT **non archivia metodi** — archivia
*osservazioni di mercato datate*. Quando da un'osservazione nasce un metodo, quel metodo **sale a
`conoscenza-empire`** e LAN-INT ne conserva solo il riferimento. Se LAN-INT comincia a contenere
framework, sta diventando una biblioteca parallela e va potato.

## 10. Gli eseguibili

`scripts/ricerca.py`

| Funzione | Firma | Ritorna |
|---|---|---|
| `conta_requisiti` | `conta_requisiti(ricerca: dict) -> dict` | i conteggi di voci, dolori, concorrenti, spazi |
| `verifica_fonti` | `verifica_fonti(voci: list[dict], timeout_s: int = 10) -> list[dict]` | per fonte: raggiungibile sì/no |
| `verifica_a_campione` | `verifica_a_campione(voci: list[dict], quante: int = 3, seme: int \| None = None) -> list[dict]` | per frase estratta: compare davvero nella pagina? |
| `deduplica` | `deduplica(record: list[dict], soglia: float = 0.85) -> list[dict]` | i record unici, con i doppi collegati all'originale |
| `scaduti` | `scaduti(mercato: str, alla_data: str) -> list[dict]` | i record da riverificare |

## 11. Skill e comando

`/lancio-ricerca <id>` · `/lancio-ricerca <id> --aggiorna` per l'incrementale.
Se il pubblico dichiarato è generico, **si ferma e lo dice**: una ricerca su "chiunque voglia
imparare X" produce frasi che valgono per nessuno.

## 12. Come si misura

| Metrica | Bersaglio |
|---|---|
| Frasi con fonte | **100%** |
| Verifica a campione superata | 3 su 3 |
| Ricerche rifatte da zero quando bastava aggiornare | 0 |
| Obiezioni della mappa poi usate nel copy | ≥80% delle prime cinque |
| Spazi vuoti che diventano argomenti di vendita | ≥2 per lancio |

---
---

# WF-7 — ESECUZIONE DEL LANCIO *(l'orchestratore)*

## 1. Identità

| Campo | Valore |
|---|---|
| **Sigla** | `WF-REG` |
| **Nome** | Workflow Regia del Lancio |
| **Missione** | Tiene il calendario, sincronizza i reparti, apre e chiude la vendita, misura ogni giorno, e chiude col debrief |
| **Proprietario** | Reparto **LAN-REG** — avvolge `IB-L2-LANC`, che si sposta qui |
| **Durata** | 37 giorni: da T-30 a T+7 |

**Cosa si tiene alla lettera del workflow esistente:** la sua anatomia, che è già quella giusta —
*ingresso in JSON → sequenza con un proprietario per passo → gate → uscita in JSON → passaggio di
consegne → prova a secco obbligatoria*. È la stessa forma del workflow libri, che funziona.
**Cosa gli manca, ed è tutto:** il comando che lo esegue.

## 2. Trigger

`/lancio-avvia <lancio_id>` — richiede che il lancio sia in stato `DATATO`, cioè che prezzo e
data esistano. Prima di quello, questo workflow **non può partire**, e il messaggio lo dice.

## 3. Il calendario T-30 → T+7

| Giorno | Cosa deve essere pronto | Chi | Dipende da |
|---|---|---|---|
| **T-30** | Il lancio esiste, la data è fissata, il calendario è generato | REG | offerta accettata |
| **T-30** | Budget approvato e punto di pareggio calcolato | TSR | offerta |
| **T-29** | Ricerca chiusa e verificata | INT | — |
| **T-28** | Certificato del prodotto emesso | PRD | ricerca |
| **T-27** | Fondamento del messaggio: la grande promessa, approvata da una persona | CPY | ricerca + certificato |
| **T-25** | **Pagina di vendita** — il documento madre | CPY | grande promessa |
| **T-23** | Punteggio della pagina di vendita ≥80 | QLT | pagina di vendita |
| **T-22 → T-14** | **SPRINT IN PARALLELO** — i tre reparti lavorano insieme | CPY · FNL · EDT | pagina di vendita approvata |
| ↳ | tutti gli altri testi: pagine, video, webinar, quattro sequenze email, annunci | CPY | |
| ↳ | le nove pagine del funnel costruite e messe online | FNL | testi man mano |
| ↳ | il piano editoriale dei 37 giorni, completo riga per riga | EDT | grande promessa |
| **T-14** | I contenuti pre-lancio cominciano a uscire | EDT | piano approvato |
| **T-12** | Tutte le pagine rispondono e **tracciano davvero** | FNL | pagine online |
| **T-10** | Le campagne a pagamento sono pronte ma spente | TRF | annunci + pagine |
| **T-7** | La lista viene scaldata: la sequenza pre-lancio parte | REG | sequenza pronta |
| **T-5** | **Prova a secco completa**: si simula tutto senza spedire niente | REG | tutto |
| **T-3** | Il webinar, se previsto, ha le iscrizioni aperte | FNL + EDT | |
| **T-1** | **Punto di sincronizzazione** + via libera | QLT + **una persona** | tutta la lista |
| **T-0** | **Si apre la vendita** | **una persona** | via libera |
| **T-0 → T+5** | Ogni giorno: numeri, diagnosi, azione | REG | — |
| **T+5** | Ultima chiamata | CPY + REG | |
| **T+5** | **Si chiude la vendita** | **una persona** | |
| **T+6** | Consuntivo economico | TSR | vendite reali |
| **T+7** | Debrief con almeno tre schemi | MEM | consuntivo |

**Le date sono relative, non assolute.** Il calendario si **genera** dalla data di apertura: se
la data slitta, si rigenera. È il motivo per cui deve essere un file generato e non scritto a
mano — un calendario scritto a mano, quando la data cambia, resta indietro e mente.

## 4. Il grafo delle dipendenze

```
offerta (prezzo + data)
   │
   ├──► budget ──► [G8-a] ──┐
   │                        │
ricerca ──► certificato ────┼──► grande promessa ──► PAGINA DI VENDITA ──► [G5]
                            │                                                │
                            │            ┌───────────────────────────────────┘
                            │            │
                            │      ╔═════╧══════════ SPRINT PARALLELO ═══════════╗
                            │      ║  testi rimanenti  │  funnel  │  editoriale  ║
                            │      ╚═════╤══════════════════╤═══════════╤════════╝
                            │            │                  │           │
                            └────────────┴────────► [G9 sincronizzazione] ◄──────┘
                                                          │
                                                    via libera umano
                                                          │
                                                    APERTURA VENDITA
```

**Il vincolo che vale più di tutti:** lo sprint parallelo **non parte** finché la pagina di
vendita non ha superato il suo gate. Tre reparti che lavorano su una promessa non ancora
approvata producono tre versioni diverse della stessa cosa, e il rifacimento costa più del
tempo che si credeva di guadagnare.

## 5. Il punto di sincronizzazione — la lista di T-1

Tutte vere **insieme**, o non si apre:

| # | Voce | Come si verifica |
|---|---|---|
| 1 | Prodotto certificato, zero bandiere rosse | il certificato esiste con esito positivo |
| 2 | Prezzo e data confermati e non cambiati dall'ultima approvazione | confronto con la versione approvata |
| 3 | Tutte le pagine del funnel rispondono | controllo automatico su ognuna |
| 4 | Tutte le pagine registrano l'evento di conversione | l'evento è scattato almeno una volta in prova |
| 5 | Cassa e pagamento provati con una **transazione di prova reale** | prova registrata |
| 6 | Le quattro sequenze email caricate e programmate | verifica sullo strumento |
| 7 | Piano editoriale approvato e primi contenuti già usciti | conteggio |
| 8 | Budget approvato, scarto entro il 10% | il gate dei costi |
| 9 | Prova a secco eseguita e superata | il verbale esiste |
| 10 | Chi risponde ai clienti durante la vendita è designato e disponibile | **è una persona, e va nominata** |

La decima voce è quella che tutti dimenticano e che rovina i lanci: si apre la vendita e nessuno
sa chi risponde a chi scrive *"il pagamento non funziona"*.

## 6. Il via libera — la procedura

1. Il sistema produce il **verbale**: le dieci voci con esito, i numeri del budget, cosa non è
   pronto.
2. **Una persona decide.** Tre esiti possibili, e vanno tutti scritti:

| Esito | Quando | Cosa comporta |
|---|---|---|
| **Si parte** | tutte e dieci vere | si apre alla data |
| **Si parte ridotto** | mancano voci non essenziali (es. gli annunci) | si apre **senza quel pezzo**, dichiarandolo: il lancio parte organico e il pezzo si aggiunge dopo |
| **Si rinvia** | manca una voce essenziale (prodotto, pagamento, pagine) | **nuova data**, calendario rigenerato, e la ragione scritta |

3. Un rinvio **non è un fallimento**: è la cosa che questo sistema esiste per rendere possibile.
   Oggi l'alternativa al rinvio non è aprire lo stesso — è restare fermi per sei mesi senza che
   nessuno lo dichiari.

## 7. Il tracciamento giornaliero — diagnosi e azione

Ogni giorno di vendita aperta, alle 9 del mattino:

| Numero | Sotto soglia | Diagnosi | **L'azione, non l'allarme** |
|---|---|---|---|
| Iscrizioni alla lista | **<20%** | la pagina d'ingresso non convince, o il traffico è sbagliato | si cambia il titolo della pagina, non tutta la pagina; se il traffico è a pagamento si guarda quale annuncio porta gente sbagliata |
| Apertura delle email | **<20%** | il titolo dell'email | si riscrive il titolo della prossima e si rimanda a chi non ha aperto, con titolo diverso |
| Click nelle email | **<1%** | il contenuto | si accorcia e si porta l'invito all'azione più in alto |
| Presenza al webinar | **<30%** | i promemoria | si aggiunge un promemoria a un'ora prima e uno a dieci minuti |
| Conversione della pagina | **<2%** | prezzo, prova o obiezioni | si aggiungono prove e si affronta l'obiezione più frequente fra chi ha scritto |
| Costo di acquisizione | oltre il pareggio | si sta pagando più di quanto si incassa | **si spegne quel canale**, non si aspetta |
| Vendite a metà periodo | <30% dell'atteso | il problema è a monte del carrello | si controlla nell'ordine: la pagina traccia? il pagamento funziona? il prezzo è visibile? |

**La regola:** ogni riga di questa tabella ha un'azione, e l'azione **si esegue entro lo stesso
giorno**. Un cruscotto che segnala e non fa agire è un cruscotto che si smette di guardare al
terzo giorno.

## 8. Il debrief

| Sezione | Cosa contiene |
|---|---|
| Previsto contro reale | ogni numero del piano accanto al numero vero |
| **Gli scarti oltre il 10%** | **ognuno con una causa scritta.** Uno scarto senza causa è un debrief non finito |
| Cosa ha funzionato | con l'evidenza, non con l'impressione |
| Cosa no | idem |
| I gate | quali hanno bloccato, quanto è costato il blocco, **se avevano ragione** |
| **Almeno tre schemi riutilizzabili** | ognuno nel formato del banco della memoria |
| Cosa cambia nel prossimo lancio | azioni concrete, non buoni propositi |

**La sezione sui gate è quella che nessuno pensa di mettere e che vale di più**: dice se il
sistema che abbiamo costruito ha funzionato, non solo se il lancio ha venduto.

## 9. Fallimenti

| Sintomo | Causa | Cosa fa il sistema |
|---|---|---|
| Il calendario slitta di continuo | dipendenze sottovalutate | ogni slittamento si registra; **tre slittamenti sullo stesso lancio impongono di rigenerare il calendario dalla data vera**, non di continuare a rincorrerla |
| Il via libera viene dato con voci false | fretta | il verbale resta agli atti con le voci false marcate; se il lancio va male, il debrief parte da lì |
| Nessuno guarda i numeri giornalieri | il cruscotto non è nel flusso di lavoro | il tracciamento **si genera da solo** ogni mattina e finisce nel file del giorno: se nessuno lo apre, la sentinella lo segnala al terzo giorno |
| Il debrief non viene scritto | il lancio è finito e l'attenzione è già altrove | **il lancio non passa a `APPRESO`**: resta aperto in `CHIUSO`, e resta visibile nell'elenco dei lanci come non finito |
| Si apre la vendita senza la persona di riferimento | la voce dieci saltata | il gate non passa: è una voce come le altre |

## 10. Gli eseguibili

`scripts/calendario.py`

| Funzione | Firma | Ritorna |
|---|---|---|
| `genera` | `genera(data_apertura: str, durata_carrello_gg: int, tipo_funnel: str) -> dict` | le 37 righe del calendario, deterministiche |
| `rigenera` | `rigenera(lancio_id: str, nuova_data: str) -> dict` | il calendario spostato, **conservando ciò che è già fatto** |
| `in_ritardo` | `in_ritardo(lancio_id: str, oggi: str) -> list[dict]` | le voci scadute e non chiuse |

`scripts/tracking.py`

| Funzione | Firma | Ritorna |
|---|---|---|
| `raccogli` | `raccogli(lancio_id: str, data: str) -> dict` | i numeri del giorno (in parte inseriti a mano: i campi non compilati restano `null`, mai zero) |
| `diagnosi` | `diagnosi(numeri: dict) -> list[dict]` | per ogni soglia superata: diagnosi **e azione** |
| `report_giornaliero` | `report_giornaliero(lancio_id: str, data: str) -> str` | il file del giorno |

`scripts/debrief.py`

| Funzione | Firma | Ritorna |
|---|---|---|
| `confronta` | `confronta(lancio_id: str) -> dict` | previsto contro reale, voce per voce |
| `scarti_rilevanti` | `scarti_rilevanti(confronto: dict, soglia: float = 0.10) -> list[dict]` | gli scarti che richiedono una causa scritta |
| `verifica_completezza` | `verifica_completezza(debrief_path: str) -> tuple[bool, list[str]]` | (completo sì/no, cosa manca) — **esce 1 se mancano le cause o gli schemi** |

## 11. Skill e comandi

| Comando | Cosa fa |
|---|---|
| `/lancio-avvia <id>` | genera il calendario e apre il conto alla rovescia |
| `/lancio-stato <id>` | dove siamo, cosa blocca, **il comando esatto da eseguire adesso** |
| `/lancio-sincronizza <id>` | esegue la lista di T-1 e produce il verbale |
| `/lancio-oggi <id>` | i numeri del giorno con diagnosi e azioni |
| `/lancio-chiudi <id>` | avvia consuntivo e debrief |

## 12. Come si misura

| Metrica | Bersaglio |
|---|---|
| Lanci che aprono alla data prevista | ≥70% (un rinvio dichiarato **non conta come fallimento**) |
| Voci della lista di sincronizzazione false al via libera | **0** |
| Giorni di vendita senza tracciamento | 0 |
| Scarti oltre il 10% senza causa scritta | **0** |
| Schemi riutilizzabili per lancio | **≥3** |
| Debrief scritti entro T+7 | 100% |

---

## OBIEZIONI

**Contro WF-4 — «Nessuno inserirà le spese a mano ogni giorno, e senza quei dati tutto il resto è finto.»**
Vera, ed è il punto più debole. La risposta parziale: la sentinella tratta *l'assenza di
movimenti* come anomalia invece che come zero, quindi il buco si vede invece di passare per un
lancio economico. E il consuntivo si riconcilia con la Tesoreria, che i movimenti li ha comunque
perché passano dal conto. **Quello che resta vero:** il costo di acquisizione giornaliero sarà
approssimativo. Meglio dichiararlo che fingere una precisione che non c'è.

**Contro WF-4 — «Bloccare la spesa al 10% di scarto ferma il lancio nel momento peggiore.»**
Per questo blocca **solo la spesa nuova** e non il lancio. E la soglia è ereditata, non
inventata. Se si dimostrasse troppo stretta, si alza — ma si alza **una volta, per iscritto**,
non ogni volta che dà fastidio.

**Contro WF-6 — «La verifica a campione su tre frasi è troppo debole: si possono inventare le altre dodici.»**
Vero. Tre su quindici è un campione del 20%: chi inventa dodici frasi e ne mette tre vere ha una
probabilità concreta di passare. **La correzione che accetto:** il campione sale a 5 su 15 (33%)
e le frasi si estraggono con un seme casuale non prevedibile da chi ha prodotto la ricerca.
Resta comunque un controllo statistico, non una prova: va detto.

**Contro WF-6 — «Scadenze e riverifiche sono lavoro che nessuno farà.»**
Per questo l'aggiornamento è incrementale e costa mezza giornata contro quattro. Ma l'obiezione
tiene: se nessuno lancia l'aggiornamento, la ricerca invecchia in silenzio. Presidio: la ricerca
scaduta **marca il lancio successivo** che la usa, e il gate lo dichiara nel verbale.

**Contro WF-7 — «Trentasette giorni sono troppi. I lanci veri si fanno in due settimane.»**
Il calendario è **relativo e comprimibile**: `genera` accetta la durata. T-30 è il caso completo
con webinar; un lancio diretto senza webinar comprime a T-14 togliendo lo sprint del webinar e
metà del piano editoriale. Ciò che **non** si comprime sono le dipendenze: la pagina di vendita
prima dello sprint, il gate delle pagine prima del via libera.

**Contro WF-7 — «Dieci voci di sincronizzazione sono un cancello che nessuno riuscirà mai ad aprire tutto.»**
Per questo esiste il *si parte ridotto*: un esito previsto, scritto, non un'eccezione strappata.
La differenza fra un sistema che ammette il lancio ridotto e uno che pretende la perfezione è
che il primo viene usato.

---

## SEGNALAZIONI

1. La commissione di pagamento al 3,5% è un default, **non una misura sul fornitore reale**: va
   verificata prima del primo lancio vero.
2. L'attribuzione dei clienti per canale richiede pagine d'ingresso separate. Se il primo lancio
   non le ha, il costo di acquisizione per canale **non sarà calcolabile** e va dichiarato tale.
3. Il tracciamento di iscrizioni, aperture e click dipende dallo strumento di invio email in uso,
   che questo piano non ha verificato. Va accertato prima di S1.
