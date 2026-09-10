# BACKBONE — 15-LANCI

> L'architettura portante dell'ecosistema, come la fissa
> [ADR-025](../../Memory/decisions/ADR-025-ecosistema-lanci.md).
> Questo documento **spiega**; il registro **decide**. Se i due si contraddicono, ha torto
> questo documento.

---

## 1. Che macchina è

**Una macchina a stati con dei controlli. Non un motore di orchestrazione.**

È la decisione 5 di ADR-025, ed è motivata da una verifica sul codice fatta il 2026-09-05:
il motore canonico `orchestration-layer` ha un tetto rigido di sei attività per piano, un
vocabolario di ruoli chiuso a cinque nomi, e **non sa chiamare nessun modello**. Non
rappresenta un flusso a tredici artefatti senza essere prima riscritto.

Quello che serve qui è più piccolo e più noioso:

> leggere un file → validarlo contro il suo schema → decidere se si passa → scrivere un
> verbale

Circa **400 righe**, non 133 file. LANCI non scrive un ottavo motore in silenzio: registra
che il primo lavoro reale non richiedeva quello canonico, e lascia ad
[ADR-019](../../Memory/decisions/) la scelta se restare così o adattare il motore.

---

## 2. Il pezzo centrale: `avanza`

Un lancio è una cartella sotto `lanci/` con dentro gli artefatti e un `stato.json`.
Il comando che lo muove è uno solo.

```
lancio avanza <slug>
```

Cosa deve fare, e sono requisiti, non desideri:

| | |
|---|---|
| **Lock esclusivo** | due sessioni sullo stesso lancio non si sovrascrivono |
| **Idempotenza** | due esecuzioni di fila: la seconda non cambia niente |
| **Codici d'uscita** | `0` avanzato · `1` bloccato da un gate · `2` parametri sbagliati · `3` errore di sistema |
| **Verbale sempre** | a ogni transizione, anche quando il gate blocca |
| **Ricalcolo** | un artefatto è valido solo contro il proprio schema, **ricalcolato**: mai fidarsi di un campo salvato |

**Il criterio di chiusura dello scaglione S2 è che `avanza` su un lancio vuoto esca con
codice 1**, si fermi al controllo dell'offerta e scriva il verbale. Se esce zero, S2 non è
chiuso per quanto codice sia stato scritto: *un sistema che lascia passare un lancio senza
prezzo è il sistema che c'è già oggi, con più file dentro.*

---

## 3. I tredici artefatti, e la regola che li lega

Ogni artefatto ha, senza eccezioni:

1. uno **schema** che lo valida (`dati/schemi/*.schema.json`)
2. un **produttore unico**
3. un **giudice diverso dal produttore** — **INV-01**
4. un **gate** che lo blocca
5. gli artefatti da cui **dipende**
6. un **ramo di fallimento mai vuoto**

Il punto 3 è quello che regge tutto il resto. Un sistema in cui chi produce approva è un
sistema senza controlli, con più passaggi.

**`ART-CRT` ha una modalità retroattiva** (`modalita_ammesse: ["integrale", "retroattiva"]`)
pensata apposta per i prodotti già finiti: il Manuale esiste da mesi e non deve attraversare
un flusso di produzione che non ha mai percorso. Si dichiarano le sei bandiere rosse, si
testano i link, e si scrive il `debito_collaudo` invece di fingere che non ci sia.

---

## 4. Il giudice non scrive

**INV-09.** L'agente `lan-gate` ha `tools: ["Read", "Bash", "Glob", "Grep"]`. Niente `Write`,
niente `Edit`.

I verbali dei gate li scrive **lo script che lo invoca**, mai l'agente. Un giudice che può
riscrivere il fascicolo non è un giudice.

`valida_registro.py` verifica INV-01 e INV-09 **prima di ogni build**.

---

## 5. I punti umani, e perché hanno una scadenza

Sei punti in cui la macchina si ferma e aspetta una persona: `PU-RUOLO`, `PU-PREZZO`,
`PU-APERTURA`, `PU-INVIO`, `PU-SPESA`, `PU-COPERTINA`.

Ognuno dichiara una `scadenza_giorni` **oppure la motivazione esplicita per non averla**, e
un comportamento `allo_scadere` — **INV-06**. Le firme accettano solo un canale fra
`comando-utente`, `chat-firmata`, `file-fuori-agenti`, e **nessun agente ha permesso di
scrittura sul campo firma**. Il campo `proposta_hash` lega la firma al testo esatto firmato:
una proposta rigenerata dopo la firma **invalida la firma** — **INV-10**.

`PU-APERTURA` non ha un valore predefinito e non ce l'avrà mai: un lancio arriva a `PRONTO`
e lì si ferma finché una persona non dice di aprire.

---

## 6. Il ponte verso gli agenti

Regolato da [ADR-014](../../Memory/decisions/):

- prompt da **standard input**, mai in riga di comando
- **identificativo esplicito del modello**, mai quello predefinito
- `total_cost_usd` **letto**, e budget verificato **prima** della chiamata, non dopo
- ogni chiamata scritta in `registro-chiamate.jsonl`

**Tetto: 15,00 $ per lancio.** Al raggiungimento il lancio si ferma dov'è, salvato, e
riprende. Non ricomincia.

`lancio costi` legge dal registro delle chiamate. **Non stima mai.**

---

## 7. Il comando che giustifica l'ecosistema

```
lancio blocchi
```

Mostra in una schermata tutti i punti umani aperti dell'azienda, ordinati per giorni di
attesa.

> **Se quel comando fosse esistito, il Manuale non sarebbe stato fermo sei mesi in
> silenzio.**

È l'unica riga di questo documento che vale la pena ricordare a memoria.

---

## 8. L'ordine di costruzione

Sei scaglioni, in `04-COSTRUZIONE.md` del piano. Dentro ogni scaglione **il test rosso viene
prima del controllo**: un controllo senza un caso che lo faccia fallire è decorativo per
costruzione (**INV-04**).

| | | |
|---|---|---|
| **S0** | la catena dell'incasso | 6-10 h, **nessun codice** |
| **S1** | il primo lancio a mano fino alla firma | 5-9 h, **nessun codice** |
| **S2** | la macchina minima | 45-65 h |
| **S3** | dal prezzo all'apertura | 35-50 h |
| **S4** | la chiusura e la memoria | 15-22 h |
| **S5** | il governo | 12-18 h |

**S0 e S1 non contengono una riga di codice**, ed è voluto: prima si incassa un euro vero e
lo si rimborsa, poi si porta un lancio a mano fino alla firma di un prezzo. Il software nasce
dopo, dai difetti misurati, non prima dai problemi immaginati.

**S1 è il collaudo vero del piano**: se compilare quattro file a mano seguendo gli schemi
risulta assurdo, il difetto è negli schemi, e si scopre lì dove costa ore invece che dentro
il codice dove costa giorni. E se un lancio non supera S1, **non serve nessun software**:
significa che il problema dell'azienda non era l'automazione.

---

## Connessioni

- [[ECOSISTEMA]] — cosa fa questo ecosistema e perché esiste
- [`04-COSTRUZIONE.md`](../../../PIANO-MAESTRO/29-ECOSISTEMA-LANCI/04-COSTRUZIONE.md) — gli scaglioni, gesto per gesto
- [`07-REPARTI-E-GERARCHIA.md`](../../../PIANO-MAESTRO/29-ECOSISTEMA-LANCI/07-REPARTI-E-GERARCHIA.md) — chi fa cosa
- [`08-WORKFLOW.md`](../../../PIANO-MAESTRO/29-ECOSISTEMA-LANCI/08-WORKFLOW.md) — i dieci flussi, 42 fasi
- [`dati/registro.yaml`](../../../PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/registro.yaml) — **la fonte di verità**
