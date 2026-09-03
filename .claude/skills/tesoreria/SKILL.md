---
name: tesoreria
description: "Il reparto che conta i soldi di Digital Empire. Registra ogni euro che entra e ogni euro che esce, e produce il quadro completo in qualunque momento, cassa, quale motore di business guadagna davvero, dove se ne vanno i soldi, quanto durano. Usala quando arriva un pagamento, quando si paga qualcosa, quando si manda un preventivo, quando Max chiede come vanno i conti o quanto reggiamo, prima di una decisione che costa, e ogni volta che qualcuno cita un numero sui soldi e va verificato se quel numero esiste davvero."
---

# TESORERIA

> **Il fatto che l'ha resa necessaria.** Misurato il 2026-09-03: **Digital Empire non
> misurava un solo euro.** Né incassi, né costi effettivi, né una metrica del percorso di
> vendita. Il direttore finanziario sorvegliava le spese di un'azienda che non aveva mai
> contato un ricavo. **È per questo che nessuno si era accorto che il magazzino era pieno
> di lavoro finito e le vendite erano zero** (ADR-016, voce B-043).

---

## 1. I COMANDI — sono cinque, e bastano

```bash
# UN EURO CHE ENTRA
python scripts/tesoreria.py entrata --importo 1500 --da "Nome cliente" \
    --per agency --stato incassato --nota "sprint CRO settembre"

# UN EURO CHE ESCE
python scripts/tesoreria.py spesa --importo 20 --a "Anthropic" \
    --categoria strumenti --ricorrente --nota "abbonamento"

# UN PREVISTO CHE E' ARRIVATO DAVVERO
python scripts/tesoreria.py incassa --id E-20260903-002

# IL QUADRO
python scripts/tesoreria.py report
python scripts/tesoreria.py report --mese 2026-09
python scripts/tesoreria.py report --scrivi     # scrive company/Memory/TESORERIA.md
```

**Motori di business:** `agency` · `kdp` · `corsi` · `youtube` · `instagram` · `saas` ·
`formazione-az` · `altro`
**Stati di un'entrata:** `previsto` · `fatturato` · `incassato` · `perso`
**Categorie di spesa:** `strumenti` · `pubblicita` · `collaboratori` · `tasse` ·
`servizi` · `hardware` · `formazione` · `altro`

---

## 2. LE TRE LEGGI DEL REPARTO

### Previsto non è incassato. Mai.
Un preventivo mandato e un bonifico arrivato sono due cose diverse. **Sommarli è il modo
classico di credersi ricchi mentre il conto è vuoto.** Il rapporto li tiene separati
sempre, anche quando la somma farebbe più bella figura.

### Un numero che non esiste si dichiara, non si stima.
Se a luglio non è stato registrato nulla, la risposta è *"a luglio non è stato registrato
nessun movimento"* — non una stima. **Una stima presentata come misura è esattamente il
male che questo reparto esiste per curare:** l'azienda ci è arrivata credendo di sapere
cose che non aveva mai contato.

### La storia dei soldi non si riscrive, si annota.
Un movimento sbagliato non si cancella: si aggiunge quello di rettifica con la nota che
spiega perché. I file sono ad accodamento apposta. **Chi cancella una riga di tesoreria
sta cancellando una prova.**

---

## 3. DOVE VIVONO I DATI

```
company/Memory/tesoreria/
├── entrate.jsonl     una riga per movimento
├── spese.jsonl       una riga per movimento
└── README.md
company/Memory/TESORERIA.md    il rapporto, rigenerato a ogni esecuzione
```

Testo semplice, una riga per movimento. **Scelta voluta:** si leggono a occhio, si
correggono a mano, e due soci che lavorano in parallelo non si sovrascrivono quando le
loro modifiche si fondono. Niente database: un database che nessuno sa aprire è un altro
posto dove i numeri vanno a nascondersi.

---

## 4. GLI AGENTI DEL REPARTO

| Agente | Quando serve |
|---|---|
| `tesoreria-conductor` | il capo: qualunque domanda sui soldi, e il quadro completo |
| `tesoreria-entrate` | arriva un pagamento, parte un preventivo, si insegue un incasso |
| `tesoreria-spese` | si paga qualcosa, si caccia uno spreco ricorrente |
| `tesoreria-report` | serve il quadro, adesso |
| `tesoreria-previsione` | quanto reggiamo, questo motore si ripaga, questa spesa quanto costa |

---

## 5. LA REGOLA DEL PASSATO VUOTO

**La tesoreria è partita il 2026-09-03.** Tutto ciò che è successo prima non è
registrato: non perché non sia successo, ma perché l'azienda non lo scriveva da nessuna
parte.

**Quei mesi restano vuoti.** Ricostruirli a memoria riempirebbe la tesoreria di numeri
che nessuno può verificare — e un numero non verificabile è peggio di un vuoto
dichiarato, perché ha l'aria di una misura.

Serviranno **almeno tre mesi** di movimenti registrati prima che qualunque previsione di
crescita smetta di essere un'invenzione con l'aria di un calcolo.

---

## 6. ⚠️ VUOTI DICHIARATI — decisioni che l'azienda non ha ancora preso

- **Non esiste un tetto di spesa in euro.** Tutte le soglie del CFO sono percentuali di
  un denominatore mai fissato. Una percentuale del nulla non ferma nessuno (B-048).
- **La soglia di 0,50 EUR per chiamata non ha nessuna fonte in casa**: esisteva solo
  dentro il file che la applicava.
- **Tre valori diversi per lo stesso allarme di budget** (70% / 80% / 60-80-95-100) in
  tre documenti dell'Impero.
- **Nessuna metrica del percorso di vendita** è ancora misurata: contatti, chiamate,
  preventivi, chiusure. La tesoreria copre i soldi, non ciò che li precede.

---

## 7. QUANDO USARLA

- **appena un soldo si muove** — l'unica regola che rende viva una tesoreria è
  registrare *subito*: un movimento annotato tre giorni dopo è un movimento perso
- **prima di ogni decisione che costa** — quanto accorcia l'autonomia
- **nel rapporto settimanale** — cassa e autonomia stanno accanto al lavoro fatto
- **quando qualcuno cita un numero sui soldi** — per verificare se quel numero esiste

---

*Creata il 2026-09-03 su ordine di Max: «iniziamo a misurare tutto». Chiude la voce
B-043, il buco di misurazione più grave dell'azienda.
Legami: [[ADR-016]] · `cfo-empire` · `sentinel-cost` · `company/Ecosistemi/14-TESORERIA/`*
