# ADR-029 — Doppio binario A/B: come una cosa imparata entra in una fabbrica che produce

- **Stato:** ATTIVO
- **Data:** 2026-09-10
- **Decide:** Emperator, su mandato permanente di Max
- **Sostituisce:** nessun ADR. **Sana un debito**: questa legge era in vigore e applicata da
  giorni, ma **non era mai stata scritta come decisione** — vedi §4.

---

## 1. Il problema

Uno studio che impara qualcosa di utile deve poterlo applicare. Ma la
`YOUTUBE-AUTOMATION-FACTORY` **produce video veri, adesso**: una modifica sbagliata al motore
non rompe un esperimento, rompe la produzione. Servono due velocità diverse, non una sola
scelta fra «non tocchiamo niente» e «cambiamo tutto subito».

## 2. La decisione

Ogni cosa imparata entra su **uno di due binari**, dichiarato al momento in cui viene scritta.

**Binario A — si applica subito, dopo ogni lezione o fonte.**
Comprende agenti, regolatori, gate a prompt, reference, skill, comandi, documenti.
Non tocca `02-AUTOMAZIONI-E-SCRIPTS/`. Sbagliare qui costa una correzione, non una produzione.

**Binario B — si applica solo a gate di categoria superato.**
Comprende ogni modifica al motore in `02-AUTOMAZIONI-E-SCRIPTS/`: script, funzioni, payload,
soglie eseguite dal codice, flussi della catena di produzione. Pretende **test verdi** e un
**video di prova**, non la sola convinzione di chi ha scritto la patch.

**Il contratto lo fa rispettare da solo.** `company/Memory/studi/aitubepro/regole/schema.py`
respinge come non a norma qualunque regola che tocchi `02-AUTOMAZIONI-E-SCRIPTS` e si dichiari
binario A. Non è una raccomandazione: è un controllo che gira.

## 3. Cosa NON dice questa decisione

Non dice che il binario B aspetta indefinitamente. Un gate di categoria è una data che arriva,
non un rinvio: chi scrive una regola B la scrive **completa e pronta**, con la sua misura, così
che al gate si applichi e basta. Un binario B usato come discarica di cose che non si vogliono
fare è un abuso di questo ADR, non un suo uso.

Non dice che si può rimandare il lavoro intorno. Vale [ADR-028](ADR-028-niente-blocca-tutto.md):
un pezzo che aspetta il gate ferma **solo se stesso**. Tutto ciò che gli sta accanto e non
dipende letteralmente da lui continua.

## 4. Il debito che questo ADR sana — e la lezione che porta

`PIANO-STUDIO-AITUBEPRO.md:315` dichiarava questa legge citando **«ADR-024»**. Ma ADR-024
esiste, ed è [Canone v2, primo strato](ADR-024-canone-v2-primo-strato.md): riguarda la Fabbrica
Siti, e non contiene una riga su gate di categoria o motore di produzione. Il piano aveva
**promesso un ADR mai scritto**, e nel frattempo quel numero è stato legittimamente occupato da
un'altra decisione. Da lì la citazione sbagliata si è propagata: `schema.py`, i report di
categoria, le verifiche di gate, gli appunti di lezione — nove punti, tutti concordi e tutti
sbagliati.

Trovato il 2026-09-10 da una sentinella che, invece di fidarsi della citazione ripetuta ovunque,
**ha aperto l'ADR-024 vero e lo ha letto.**

**La lezione, che vale oltre questo caso:** un numero di decisione si prende quando la decisione
viene scritta, mai quando viene promessa. È lo stesso errore già registrato per i numeri di
backlog nella trappola di `EMP-QQ2R` («si leggono, non si indovinano»), ripetuto su un altro
registro. Una citazione ripetuta in nove punti non è più vera di una citazione singola: è solo
più costosa da correggere.

## 5. Conseguenze operative

- Le citazioni «ADR-024» che si riferiscono al doppio binario vanno corrette in **ADR-029**.
- Chi scrive un piano che prevede una decisione nuova **conia l'ADR nello stesso turno**, o cita
  il piano stesso come fonte — mai un numero non ancora esistente.

## 6. Collegamenti

- [ADR-003](ADR-003-migrazione-wrap-non-riscrittura.md) — anch'esso citato a sproposito per la
  stessa legge; riguarda la migrazione asset, non i gate.
- [ADR-028](ADR-028-niente-blocca-tutto.md) — un impedimento ferma solo il suo perimetro esatto.
- `company/Memory/plans/PIANO-STUDIO-AITUBEPRO.md` §8 — dove la legge era stata descritta.
- `company/Memory/studi/aitubepro/regole/schema.py` — dove è fatta rispettare in codice.
