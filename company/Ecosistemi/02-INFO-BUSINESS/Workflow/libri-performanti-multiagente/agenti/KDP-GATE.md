---
Type: ENTITY
Status: Active
Tags: #agente #infobusiness #kdp #gate #controllo #deterministico
Created: 2026-09-02
Last updated: 2026-09-02
---

# KDP-GATE — Il controllo che blocca

> **ID:** KDP-GATE · **Tier:** nessun modello — **deterministico** (codice puro, costo zero)
> **Ruolo:** verifica il piano PRIMA che qualcuno lo esegua · **Team:** Piano Editoriale Libri
> **Wrappa:** `engine/piano.py::verifica()` (ADR-003)
> **Comando:** gira dentro `python -m engine.kdp piano` — non si può saltare

---

## Identità

**Nome:** `KDP-GATE`
**Ruolo:** Dice PASS o BLOCK su un piano editoriale, e quando dice BLOCK **il piano non viene
scritto**. Non suggerisce, non ammorbidisce, non fa media: elenca i campi che mancano e i
numeri senza fonte, uno per uno, col giorno a cui appartengono.

**Perché esiste separato da chi scrive il piano.** Nel flusso KDP il gate che blocca
(`kdp blocco`) ha bocciato **2 volte su 7** durante la scrittura di *The Winter Term*, e
**aveva ragione entrambe le volte**: capitoli scritti corti, scoperti al capitolo 8 invece che
al 24. È il pezzo che funziona meglio di tutto il workflow, e funziona perché chi scrive non è
chi approva. Il piano editoriale merita lo stesso trattamento: un piano sbagliato costa una
settimana di produzione, non un capitolo.

**Non usa nessun modello.** È codice deterministico: stesso piano, stesso verdetto, sempre,
gratis. Un controllo che costa e che può variare è un controllo che prima o poi si salta.

**Cosa NON fa:**
- **Non dice mai PASS con un campo mancante o un dato senza fonte.** Non esistono eccezioni
  "per questa volta".
- Non corregge il piano: segnala e basta. Correggere sarebbe diventare KDP-EDITOR, e allora
  il controllo sparirebbe.
- Non giudica se una premessa è *bella*: quello è mestiere umano. Giudica se è **completa**.
- Non scrive niente su disco.

---

## Responsabilità

1. **Campi obbligatori** — verifica tutti e 11 su ogni riga: `giorno`, `data_produzione`,
   `nicchia`, `punteggio_nicchia`, `dati_amazon`, `titolo_lavoro`, `autore`, `premessa`,
   `struttura_prevista`, `angolo_differenziante`, `comando_cli`. Uno vuoto = BLOCK.
2. **Numeri con fonte** — ogni `dati_amazon` deve avere un `punteggio` **e** un `misurato_il`.
   Senza data, un numero non è verificabile: il 2026-09-01 una decisione di catalogo è stata
   presa su punteggi di 19 giorni prima, e una nicchia nel frattempo era passata da **83,1 a
   72,9**. È il difetto che questo controllo esiste per impedire.
3. **Coerenza interna** — `punteggio_nicchia` deve coincidere con `dati_amazon.punteggio`. Due
   numeri che dovrebbero essere lo stesso numero e non lo sono significano che qualcuno ne ha
   scritto uno a mano.
4. **Comando compilato** — `comando_cli` deve contenere `kdp nuovo` **e** il titolo della riga.
   Un comando generico costringe chi esegue a decidere, ed è ciò che il piano deve evitare.
5. **Titoli distinti** — due righe con lo stesso titolo sono un errore di generazione.
6. **Premessa che sia una storia** — sotto 20 parole non è una premessa, è un'etichetta.
7. **Dichiarare la scarsità** — se le righe sono meno dei giorni chiesti, non blocca ma lo
   scrive come avviso: meno righe vere è accettabile, righe finte no (Art.2).

---

## Input / Output

**Input**
| Cosa | Da dove |
|---|---|
| le righe del piano | in memoria, da KDP-EDITOR, **prima** della scrittura su disco |
| numero di giorni atteso | parametro del comando |

**Output**
| Cosa | Forma |
|---|---|
| verdetto | `PASS` / `BLOCK` |
| bloccanti | elenco puntuale, ognuno con il giorno e il campo |
| avvisi | non bloccano, ma restano scritti |
| effetto | se BLOCK: **nessun file scritto**, exit ≠ 0 |

Stessa regola di `kdp copy`, che valida prima di salvare e se sbaglia non scrive: un artefatto
scritto a metà è peggio di nessun artefatto, perché sembra valido.

---

## Come ragiona (passo-passo)

1. Piano vuoto → BLOCK immediato.
2. Meno righe dei giorni chiesti → avviso, non blocco.
3. Per ogni riga, nell'ordine: campi obbligatori → numeri con fonte → coerenza dei punteggi →
   comando compilato → titolo non duplicato → premessa di lunghezza plausibile → angolo presente.
4. Raccoglie **tutti** i problemi prima di rispondere: un gate che si ferma al primo errore
   costringe a tre giri per scoprire tre difetti.
5. PASS solo se la lista dei bloccanti è vuota.

---

## KPI

| Metrica | Bersaglio | Perché |
|---|---|---|
| falsi PASS (piano approvato e poi rotto in esecuzione) | **0** | è l'unico difetto che conta |
| costo per verifica | **0,00 $** | deterministico, nessun modello |
| tempo | < 1 secondo | un gate lento viene saltato |
| bloccanti con giorno e campo indicati | 100% | un errore senza indirizzo non è azionabile |

---

## Memoria

Nessuna: è una funzione pura sulle righe che riceve. Non ha stato, quindi non può derivare.
Il verdetto viene stampato dal comando e finisce nel checkpoint della sessione.

---

## Escalation

- **BLOCK** → il comando esce ≠ 0 con la lista. Si corregge la causa e si rigenera; **non** si
  aggira. Se un bloccante sembra sbagliato, si discute la *regola* (e si cambia il codice con
  un test), non la singola esecuzione.
- **Ripetuti BLOCK sullo stesso campo** → è un difetto di KDP-EDITOR, non del piano: va
  corretto lì.

---

## Connessioni

- **A monte:** [[KDP-EDITOR]] — che non può approvare se stesso.
- **Fratello maggiore:** `kdp blocco` (`engine/gate_blocco.py`) — stesso principio applicato ai
  capitoli, 2 bocciature su 7 e ragione entrambe le volte.
- **Motore:** `engine/piano.py::verifica()`
- **Principio:** [[Concept_Guardrail_Che_Si_Fanno_Rispettare]] — un controllo che dà falsi
  allarmi viene disattivato; un controllo che non blocca non è un controllo.
