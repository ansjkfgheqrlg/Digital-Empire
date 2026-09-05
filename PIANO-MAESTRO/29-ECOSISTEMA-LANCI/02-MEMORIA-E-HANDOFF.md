---
Type: PROJECT
Status: Proposta
Tags: #lanci #ecosistema-15 #memoria #handoff
Created: 2026-09-05
---

# 02 — MEMORIA E PASSAGGI DI CONSEGNE

> I due sistemi nervosi dell'ecosistema: **cosa l'azienda ricorda** e **come i reparti si parlano**.
> Entrambi sono stati riscritti dopo la critica: il primo perché i suoi presidi erano tutti
> saltabili, il secondo perché la sua regola più rigorosa non aveva un posto dove manifestarsi.

---

# PARTE A — LA MEMORIA

## A.1 Il precedente, che va guardato in faccia

Nel reparto Lanci che esiste oggi, il modello di memoria era **progettato bene**: quattro spazi
definiti, i proprietari di scrittura dichiarati, gli schemi coerenti. E il comando che ne prova
l'esistenza restituisce **nessun risultato**: le cartelle non sono mai state create, e **nessun
lancio è mai stato tracciato**.

**Non è mancata la progettazione. È mancata una conseguenza.**

Perciò la domanda che governa questa parte non è *"come si progetta bene una memoria"* — quella
risposta l'azienda ce l'aveva già e non è servita a niente. È: **cosa succede a chi non la scrive?**

## A.2 La risposta, in una riga

> **Una fase non si chiude se non ha scritto il suo record.**
> Il gate della fase, oltre al proprio criterio, verifica che il record esista.
> Nessun record → fase aperta → il calendario non avanza.

Scrivere la memoria smette di essere un dovere e diventa **una condizione per andare avanti**. È
l'unica forma di obbligo che in questa azienda ha funzionato: quella che blocca il lavoro
successivo.

### A.2.1 Chi la scrive, concretamente

> ⚠️ **La critica ha trovato che la versione precedente non lo diceva mai.** Prescriveva che *"la
> scrivono gli script"* senza nominare **chi invoca** quegli script. Una responsabilità di nessuno.

| Momento | Chi scrive | Cosa |
|---|---|---|
| Alla chiusura di ogni fase | **il conductor del reparto**, come ultimo atto della fase | il record della fase |
| A ogni verdetto di gate | **il gate stesso**, sempre, anche quando lascia passare | il verbale |
| A ogni conflitto aperto e chiuso | chi lo apre, chi lo chiude | il record del conflitto |
| A ogni decisione umana | il conductor che l'ha raccolta | la decisione e la ragione |
| A fine lancio | il distillatore della Memoria | gli schemi riutilizzabili |

**E il gate della fase successiva lo verifica.** Non è affidato alla buona volontà di nessuno.

## A.3 I dodici spazi

Uno per reparto, più quello comune. **Un solo proprietario di scrittura per spazio**: quando due
processi scrivono nello stesso posto, prima o poi uno mente.

| Spazio | Scrive | Contiene | Legge | Scade |
|---|---|---|---|---|
| `memoria/strategia/` | LAN-STR | verdetti, **incluse le idee respinte con la ragione** | tutti | mai |
| `memoria/intelligence/` | LAN-INT | frasi con fonte, dolori, concorrenti, buchi | tutti | 3-12 mesi per tipo |
| `memoria/prodotto/` | LAN-PRD | certificati, bandiere rosse trovate, esiti dei test | PRD, CPY, QLT | mai |
| `memoria/offerta/` | LAN-OFF | prezzi decisi **e scartati, col perché** | OFF, STR, TSR | mai |
| `memoria/copy/` | LAN-CPY | testi finali, punteggi, versioni scartate | CPY, FNL, EDT | mai |
| `memoria/funnel/` | LAN-FNL | strutture, numeri per pagina, esiti dei test | FNL, TRF, REG | mai |
| `memoria/traffico/` | LAN-TRF | costo per canale, creatività | TRF, TSR, REG | mai |
| `memoria/editoriale/` | LAN-EDT | piani, resa per formato, riusabili | EDT, TRF | mai |
| `memoria/tesoro/` | LAN-TSR | budget, spese, scarti, consuntivi | TSR, REG, Board | mai |
| `memoria/regia/` | LAN-REG | calendari, verbali, tracciamenti | tutti | mai |
| `memoria/qualita/` | LAN-QLT | ogni verdetto, **inclusi tutti i blocchi** | tutti | mai |
| `memoria/pattern/` | LAN-MEM | gli schemi riutilizzabili | **tutti, sempre** | mai |

## A.4 Lo schema del record

```json
{
  "id": "MEM-<REPARTO>-<AAAAMMGG>-<n>",
  "reparto": "LAN-OFF",
  "lancio_id": "2026-10-manuale-claude-code",
  "fase": "O5",
  "tipo": "decisione | misura | scarto | esito | conflitto",
  "titolo": "una riga in italiano",
  "corpo": "il contenuto vero",
  "fonti": ["percorso o indirizzo verificabile"],
  "numeri": { "chiave": "valore osservato" },
  "misurato": true,
  "contraddice": ["MEM-..."],
  "scritto_da": "lan-off-conductor",
  "scritto_il": "2026-10-02T14:03:00",
  "scaduto_il": null,
  "letto_il": [],
  "letto_volte": 0
}
```

**Le quattro regole di integrità**, prese dallo schema già in uso nell'Impero e non inventate qui:

1. **Un identificativo non si riassegna mai**, nemmeno se il record viene scartato.
2. **Un record aggiornato mantiene il suo identificativo**: si versiona, non si duplica.
3. **La deduplicazione è un passo esplicito**, non un effetto collaterale.
4. **Il campo `contraddice` è obbligatorio quando applicabile.** Due fonti vere possono dire cose
   opposte, e nasconderlo è peggio che dichiararlo.

**E le due nostre:**

- **`misurato: false` ⇒ nessun gate può usare quel record come prova.** È la legge di verità
  dell'Impero tradotta in un campo.
- **`letto_volte` e `letto_il` si incrementano davvero**, ed è ciò che rende calcolabile la salute
  della memoria. *(La versione precedente prometteva di misurare i record mai letti e non aveva
  nessun campo per farlo: la soglia del 40% era incalcolabile.)*

## A.5 Gli schemi riutilizzabili

```json
{
  "id": "PAT-<AAAAMMGG>-<n>",
  "titolo": "Aprire la vendita di venerdì costa il 30% del fine settimana",
  "tipo": "regola | soglia | trappola | scorciatoia",
  "nato_da": ["2026-10-manuale-claude-code"],
  "confermato_da": [], "smentito_da": [],
  "forza": "osservazione | indizio | regola",
  "evidenza": { "descrizione": "...", "numeri": {} },
  "si_applica_quando": "prodotto sopra i 97 euro con vendita di 5 giorni",
  "azione": "cosa fare concretamente la prossima volta"
}
```

| Forza | Quando ci arriva | Cosa comporta |
|---|---|---|
| **osservazione** | un lancio | si annota, non vincola nessuno |
| **indizio** | confermato da un secondo | il capo reparto lo **deve leggere** prima di decidere |
| **regola** | confermato da tre | **diventa un gate o una regola di reparto**: non si discute più |

**E il verso opposto: smentito due volte, scende di grado.** Una memoria che sale soltanto è una
superstizione con la data.

**Il campo che fa la differenza è `si_applica_quando`.** Uno schema senza condizione di
applicabilità viene applicato sempre, anche dove non vale, e diventa una superstizione nel giro di
due lanci.

## A.6 La fase zero — obbligata, e verificata

Ogni flusso comincia consultando la memoria:

```bash
python "…/scripts/pattern.py" cerca --reparto LAN-OFF --contesto "info-prodotto sotto i 100 euro"
```

**Non è facoltativo:** il gate della prima fase verifica che la consultazione sia avvenuta, e la
prova è il campo `letto_il` dei record restituiti. *(Nella versione precedente la "fase zero
obbligatoria" era una frase che nessun gate controllava.)*

**Un lancio che non consulta la memoria ripete errori che l'azienda ha già pagato.**

## A.7 Il rapporto con la memoria dell'Impero

| Cosa | Quando | Dove sale |
|---|---|---|
| Fine di ogni fase importante | subito | i checkpoint dell'Impero, **con lo strumento ufficiale, mai a mano** |
| Decisione strutturale | quando accade | le decisioni registrate |
| Stato del lancio | a ogni cambio di stato | il file di stato generale |
| Schemi promossi a **regola** | alla promozione | la wiki, sezione concetti |
| Consuntivo economico | a lancio chiuso | la Tesoreria, che **è la fonte di verità sui soldi** |
| Debrief | a lancio chiuso | la wiki, sezione progetti |

**Il confine:** la memoria dell'ecosistema contiene **il come**; la memoria dell'Impero contiene
**cosa è stato deciso**. Duplicare il primo nel secondo lo rende illeggibile.

## A.8 Contro il marciume

| Come muore una memoria | Presidio |
|---|---|
| si riempie di roba mai riletta | `scaduto_il` + potatura a fine lancio: i record scaduti **e mai letti** vanno in archivio — **non si cancellano**, ma escono dalla ricerca |
| contiene cose false che nessuno corregge | `contraddice` + il declassamento degli schemi smentiti |
| nessuno la legge | **la scrittura è condizione di chiusura**, la lettura è condizione di apertura, e `letto_volte` misura |
| diventa illeggibile | l'indice è **generato**, mai scritto a mano: riporta record totali, scaduti e mai letti. **Sopra il 40% di mai-letti la sentinella lo segnala** |

**La soglia del 40% ha una ragione:** una memoria letta al 60% è viva e si autocorregge, perché chi
legge trova gli errori. Una letta al 10% è un cimitero ordinato.

---

# PARTE B — I PASSAGGI DI CONSEGNE

## B.1 Lo schema unico

```json
{
  "handoff_id": "HO-<AAAAMMGG>-<n>",
  "versione_schema": "1.0",
  "da": "LAN-INT",
  "a": "LAN-CPY",
  "lancio_id": "2026-10-manuale-claude-code",
  "artefatto": "ricerca.json",
  "percorso": "lanci/2026-10-.../ricerca.json",
  "criterio_accettazione": [
    "almeno 15 frasi, ognuna con fonte verificabile",
    "almeno 5 dolori distinti",
    "almeno 3 concorrenti analizzati",
    "almeno 3 buchi dichiarati"
  ],
  "gate_superato": "GATE-INT-1",
  "verbale_gate": "gate/GATE-INT-1-verbale.json",
  "emesso_da": "lan-int-conductor",
  "emesso_il": "2026-10-05T09:12:00",
  "scade_il": "2026-10-07T09:12:00",
  "accettato": null,
  "motivo_rifiuto": null
}
```

**Quattro campi che sembrano formali e non lo sono:**

| Campo | Perché |
|---|---|
| `versione_schema` | senza, il giorno che lo schema cambia i vecchi passaggi diventano illeggibili e nessuno sa perché |
| `gate_superato` + `verbale_gate` | **un passaggio senza verbale non si accetta.** "L'ho fatto" non basta: serve chi l'ha controllato |
| `accettato: null` | lo stato iniziale è *non accettato*. **Il silenzio non vale come accettazione** |
| **`scade_il`** | **nuovo dopo la critica** — vedi B.2 |

## B.2 Il difetto che la critica ha trovato

**La versione precedente imponeva che il silenzio non valesse come accettazione, e non dava a un
passaggio non accettato nessun posto dove esistere.** Nessuna scadenza, nessuno stato, nessuna
comparsa nel cruscotto: un passaggio mai accettato restava **invisibile finché il calendario non
saltava**.

La regola più rigorosa del capitolo non aveva un luogo dove manifestarsi.

**Adesso:**

| # | Correzione |
|---|---|
| 1 | Ogni passaggio ha `scade_il` — **48 ore** dall'emissione, salvo diversa indicazione del calendario |
| 2 | I passaggi pendenti sono **un campo dello stato del lancio** (`handoff_pendenti`), quindi si vedono guardando lo stato |
| 3 | Un passaggio **scaduto** diventa un blocco: compare in `bloccato_da` e la fase dipendente non parte |

## B.3 La matrice — dentro l'ecosistema

| Da | A | Cosa | Criterio di accettazione |
|---|---|---|---|
| STR | INT, PRD, OFF | `decisione.json` | verdetto positivo, con le cinque risposte scritte |
| INT | CPY, OFF, FNL, EDT | `ricerca.json` | 15 / 5 / 3 / 3, ogni frase con fonte |
| PRD | OFF, CPY, REG | `certificato-prodotto.json` | zero bandiere rosse; beta test se dovuto |
| OFF | CPY, FNL, TSR, REG | `offerta.json` | prezzo e data presenti e non evasivi, **con firma** |
| CPY | FNL, EDT, TRF | `copy/` | ogni pezzo ha superato il gate della sua classe |
| FNL | TRF, REG | `funnel.json` | ogni pagina risponde **e registra l'evento** |
| EDT | TRF, REG | `piano-editoriale.json` | nessuna riga incompleta |
| TSR | REG, Board | `budget.json` | pareggio calcolato |
| REG | MEM | tutto il lancio | vendita chiusa |
| MEM | STR *(del lancio successivo)* | `pattern/` | almeno tre schemi |
| QLT | chiunque | i verbali | — *(i verdetti non si accettano: si subiscono)* |

## B.4 La matrice — verso gli altri ecosistemi

| Direzione | Con chi | Cosa |
|---|---|---|
| ⬅ | `02-INFO-BUSINESS` | prodotto finito e confezionamento — **lo crea lui** |
| ⬅ | `04-MARKETING` | standard dei testi e voce del marchio — **lo standard è suo** |
| ⬅ | `08-INTELLIGENCE` | dossier sui concorrenti, con le fonti |
| ⬅ | `09-OPERATIONS` | capacità disponibile nel periodo |
| ➡ | `03-CONTENT-FACTORY` | brief degli asset — **lei produce, noi ordiniamo** |
| ➡ | `14-TESORERIA` | ricavi e costi reali — **lei è la fonte di verità** |
| ➡ | `02-INFO-BUSINESS` | acquirenti e accoglienza, alla chiusura |
| ➡ | `10-MEMORY` | checkpoint, decisioni, debrief |
| ➡ | `01-AGENCY` | contatti di alto valore emersi dal lancio |
| ↔ | `07-FORGE` | agenti e skill da forgiare e registrare |

## B.5 Quando un passaggio viene rifiutato

1. Il destinatario scrive `accettato: false` e **compila `motivo_rifiuto` citando il criterio
   preciso** che non è soddisfatto. Un rifiuto senza criterio citato **è nullo**: torna indietro
   al destinatario.
2. L'artefatto **torna al mittente**, che resta il proprietario. **Il destinatario non lo
   aggiusta**: se lo aggiustasse, i due mestieri si confonderebbero e la volta dopo nessuno
   saprebbe di chi è la responsabilità.
3. Il mittente ha una **finestra dichiarata** per correggere: la dice il calendario, non il
   buonsenso.
4. **Al secondo rifiuto dello stesso artefatto**, sale alla Direzione. Al terzo è un conflitto
   formale e sale al Board di materia.
5. Ogni rifiuto è un record in `memoria/qualita/`. **Tre rifiuti della stessa specie obbligano a
   rivedere il criterio o il reparto**: se sbagliamo sempre lo stesso passaggio, il difetto non è
   di chi lo esegue.

---

## C. GLI ESEGUIBILI

`scripts/memoria.py`

| Funzione | Firma | Ritorna |
|---|---|---|
| `scrivi` | `scrivi(reparto: str, lancio_id: str, tipo: str, dati: dict) -> str` | l'identificativo del record; **rifiuta** se il proprietario non corrisponde al reparto |
| `leggi` | `leggi(spazio: str, filtri: dict) -> list[dict]` | i record, **e incrementa `letto_volte`** |
| `indice` | `indice() -> dict` | totali, scaduti, mai letti per spazio |
| `potatura` | `potatura(alla_data: str) -> list[str]` | i record archiviati — **archiviati, mai cancellati** |
| `verifica_fase` | `verifica_fase(lancio_id: str, fase: str) -> bool` | **il record della fase esiste?** È ciò che il gate chiama |

`scripts/pattern.py`

| Funzione | Firma | Ritorna |
|---|---|---|
| `distilla` | `distilla(lancio_id: str) -> list[dict]` | gli schemi candidati dal debrief |
| `cerca` | `cerca(reparto: str, contesto: str) -> list[dict]` | gli schemi applicabili, ordinati per forza |
| `conferma` | `conferma(pattern_id: str, lancio_id: str) -> dict` | aggiorna la forza; **promuove a regola alla terza conferma** |
| `smentisci` | `smentisci(pattern_id: str, lancio_id: str) -> dict` | **declassa alla seconda smentita** |

`scripts/handoff.py`

| Funzione | Firma | Ritorna |
|---|---|---|
| `emetti` | `emetti(da: str, a: str, artefatto: str, lancio_id: str) -> dict` | **rifiuta se manca il verbale del gate** |
| `accetta` | `accetta(handoff_id: str, chi: str) -> dict` | verifica il criterio prima di accettare |
| `rifiuta` | `rifiuta(handoff_id: str, criterio_violato: str) -> dict` | **rifiuta il rifiuto** se non cita un criterio |
| `pendenti` | `pendenti(lancio_id: str, oggi: str) -> list[dict]` | i passaggi in attesa, **con quelli scaduti in evidenza** |

---

## D. COSA È CAMBIATO

| Cambiamento | Contro quale obiezione |
|---|---|
| La memoria è **condizione di chiusura di fase** | *"tre presidi morbidi, tutti saltabili, e uno identico ha già fallito in questa azienda"* |
| **È scritto chi invoca gli script**, momento per momento | *"il piano non dice mai chi chiama memoria.py: è una responsabilità di nessuno"* |
| Il record ha **`letto_il` e `letto_volte`** | *"la soglia del 40% di mai-letti è incalcolabile: lo schema non ha nessun campo di lettura"* |
| La fase zero **è verificata da un gate** | *"è una frase che nessun gate controlla"* |
| I passaggi hanno **scadenza e stato** | *"la regola più rigorosa del capitolo non ha un luogo dove manifestarsi"* |
| Gli spazi sono **dodici**, uno per reparto più il comune | *"il conto non torna: un reparto resta senza spazio"* |
