# CONTRATTO — `stato.json`, verbali, registro chiamate (S2b→S5)

Scritto una volta il 2026-09-15 perché motore (`stato_lancio.py`), gate (`scripts/gates/`) e
governo (`scripts/governo.py`) sono costruiti da mani diverse in parallelo. **Chi scrive un campo
qui sotto lo scrive così; chi lo legge lo legge così.** Se un campo manca nel file (lancio creato
prima di questo contratto) il lettore lo tratta come vuoto/null, mai come errore.

## `lanci/<id>/stato.json` — lo scrive SOLO il motore

```json
{
  "schema_version": "1.0.0",
  "lancio_id": "manuale-claude-code",
  "prodotto": "Manuale Claude Code",
  "stato": "ISTRUITO",
  "creato_il": "2026-09-10T18:55:00+00:00",
  "cambiato_il": "2026-09-15T20:10:00+00:00",
  "stato_di_partenza": null,
  "storia": [{"da": null, "a": "IDEA", "il": "...", "perche": "creazione"}],

  "bloccato_da": null,
  "punti_umani_aperti": [],
  "sospensione": null,
  "impronte": {},
  "da_rivedere": [],
  "gate": {}
}
```

| Campo | Forma | Chi lo scrive | Chi lo legge |
|---|---|---|---|
| `bloccato_da` | `null` oppure `{"gate": "GATE-OFF-1", "dal": iso, "problemi": [str, ...]}` — l'ULTIMO gate che ha bloccato, con da quando | motore (`avanza`) | `lancio elenco` (causa del fermo), `lancio blocchi` |
| `punti_umani_aperti` | lista di `{"id": "PU-PREZZO", "aperto_il": iso, "scadenza_il": iso \| null, "domanda": str, "come_si_esce": "lancio firma <id> --prezzo N --data gg/mm/aaaa"}` — `id` ∈ `registro.punti_umani[].id`; `come_si_esce` è **un comando eseguibile**, non una descrizione | motore (apre quando un gate blocca per firma/via libera/spesa; chiude quando la causa sparisce) | `lancio blocchi` (ordina per giorni da `aperto_il`), promemoria |
| `sospensione` | `null` oppure `{"stato_di_partenza": "ISTRUITO", "dal": iso, "revisione_il": iso, "motivo": str, "come_si_esce": "lancio riprendi <id>", "orologi_congelati": {"<PU-id>": "<scadenza_il al momento della sospensione>"}}` | motore (`sospendi`, o scadenza di un punto umano senza default) | `riprendi`, `blocchi`, `elenco` |
| `impronte` | `{"pubblico.json": "<sha256>", ...}` — l'impronta di ogni artefatto **al momento in cui il suo gate è passato** | motore | motore (per `da_rivedere`) |
| `da_rivedere` | lista di nomi di artefatto (`"previsione.json"`) i cui ingressi a monte sono cambiati dopo il loro gate | motore | motore (rilancia quei gate al prossimo `avanza`), `stato` |
| `gate` | `{"GATE-PUB-1": {"passa": true, "il": iso, "tentativo": 2}}` — **comodità di lettura, MAI fonte**: ogni gate ricalcola dai file | motore | `stato`, `elenco` |

## `lanci/<id>/verbali/` — li scrive SOLO il motore

Un verbale per evento, anche quando NON succede niente di nuovo. Nome:
`YYYYMMDDTHHMMSS-<tipo>.json` per gli eventi (`creazione`, `transizione`, `sospensione`,
`ripresa`, `abbandono`, `firma`, `via-libera`, `ambiente`, `validazione-fallita`).

**Per i gate la chiave è `(controllo, tentativo)` — idempotenza**: il verbale di un gate si chiama
`gate-<GATE-ID>-t<tentativo>.json`; un secondo `avanza` **senza che nessun file sia cambiato**
(stesse impronte) non crea un verbale nuovo: aggiorna `ultimo_controllo_il` in quello esistente.
Il tentativo cresce solo quando un artefatto in ingresso è cambiato. Corpo:

```json
{"tipo": "gate", "gate": "GATE-OFF-1", "tentativo": 1, "passa": false,
 "problemi": ["..."], "dati": {...}, "ramo_fallimento": "ISTRUITO",
 "impronte_ingresso": {"offerta.json": "<sha256 o null>"},
 "il": iso, "ultimo_controllo_il": iso}
```

## `lanci/<id>/registro-chiamate.jsonl` — lo scrive SOLO `ponte.py`

Una riga JSON per ogni invocazione di agente, anche fallita:

```json
{"il": iso, "lancio_id": "...", "agente": "lan-pub-censore", "modello": "claude-sonnet-5",
 "durata_s": 12.4, "total_cost_usd": 0.093, "esito": "ok" | "errore" | "tetto",
 "prompt_sha256": "...", "nota": null}
```

`lancio costi <id>` = somma di `total_cost_usd` di quel file. Mai stimato. Tetto per lancio:
`registro.ponte.tetto_spesa_per_lancio_usd` (15 $): `ponte.invoca` rifiuta **prima** della
chiamata se la somma è già ≥ tetto (esito `tetto`, codice 3 per il motore).

## Gate — il contratto sta in `scripts/gates/_comune.py`

`esegui(dir_lancio, rete) -> Verdetto(gate, passa, problemi, dati, ramo_fallimento)`. Il gate non
scrive nulla. I moduli si chiamano `gate_<sigla>_<n>.py` (`GATE-PUB-1` → `gate_pub_1.py`).
Modulo assente → il motore esce **3** e scrive un verbale `ambiente` («controllo non costruito»),
non finge di averlo eseguito.

## Quale gate in quale transizione (dal registro, `transizioni[].condizione`)

| da → a | gate che devono passare | autorizza |
|---|---|---|
| IDEA → VALUTATO | GATE-PUB-1, GATE-STR-1 | sistema |
| IDEA → ARCHIVIATO | GATE-STR-1 boccia | sistema |
| VALUTATO → ISTRUITO | GATE-PRD-1, GATE-INT-1, GATE-PRV-1 | sistema |
| ISTRUITO → DATATO | GATE-OFF-1 (con firma umana dentro l'artefatto) | persona (`lancio firma`) |
| DATATO → IN_PRODUZIONE | GATE-TSR-1 | sistema |
| IN_PRODUZIONE → DATATO | GATE-TSR-2 boccia | sistema |
| IN_PRODUZIONE → PRONTO | GATE-CPY-1, GATE-FNL-1, GATE-EDT-1, GATE-REG-1 | sistema (REG-1 è l'ultimo) |
| PRONTO → APERTO | via libera firmato (`lancio via-libera`) | persona |
| APERTO → CHIUSO | data di chiusura raggiunta (`offerta.data_chiusura`) | persona |
| CHIUSO → APPRESO | GATE-CNS-1, GATE-MEM-1 | sistema |
| * → SOSPESO / SOSPESO → partenza / → ABORTITO | comandi `sospendi`, `riprendi`, `abbandona` | vedi registro |

Se una riga qui contraddice `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/registro.yaml`, ha torto questa riga.
