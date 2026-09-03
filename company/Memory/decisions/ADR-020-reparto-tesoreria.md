# ADR-020 — Nasce la TESORERIA: Digital Empire comincia a contare i soldi

- **Stato:** ATTIVO
- **Data:** 2026-09-03
- **Ordinato da:** Max — *"iniziamo a misurare tutto. Fai un intero ecosistema di agenti e
  un vero e proprio reparto ufficiale che gestisce tutte le entrate e poi anche le spese,
  per avere un report sempre pronto, chirurgico"*
- **Chiude:** la voce B-043
- **Ecosistema:** `company/Ecosistemi/14-TESORERIA/`

---

## 1. Il fatto

Misurato il 2026-09-03, lavorando ai file del Board:

> **Digital Empire non misurava un solo euro.** Né incassi, né costi effettivi, né una
> sola metrica del percorso di vendita — contatti, chiamate, preventivi, chiusure.

Le conseguenze, tutte verificate sui file:

- il **CFO** sorvegliava le spese di un'azienda che non aveva mai contato un ricavo
- lo **stato della pipeline** del CRO era un'opinione, non una misura
- il **CMO** aveva un ciclo di analisi senza dati in ingresso
- e soprattutto: **nessuno si era accorto che il magazzino era pieno** — 25 pezzi di
  lavoro finito mai pubblicati, il più vecchio fermo da 135 giorni, zero vendite
  documentate (ADR-016)

**Non era distrazione. Non c'era niente da guardare.**

---

## 2. La decisione

**Nasce il reparto TESORERIA**, quattordicesimo ecosistema, sotto il `cfo-empire`.

### Il motore — costruito per primo, apposta
`scripts/tesoreria.py`. Registra entrate e spese, calcola cassa, margine per motore di
business, autonomia residua, e produce il rapporto in qualunque momento.

**Il motore prima della documentazione, e non è un dettaglio di metodo:** il direttore
tecnico ha dichiarato oggi che la piramide EMPIRE OS è *progetto al 100%, zero codice*.
Un reparto che nasce come cartella di documenti è un altro pezzo di quella piramide.
Questo nasce come strumento che gira, con la documentazione attorno.

**Collaudato prima di consegnare:** cinque movimenti di prova, verifica che una rettifica
non venga contata due volte (1.547 + 2.000 = 3.547, previsto sceso a zero), dati di prova
poi rimossi. I file dell'azienda partono vuoti.

### I cinque agenti
`tesoreria-conductor` (il capo) · `tesoreria-entrate` · `tesoreria-spese` ·
`tesoreria-report` · `tesoreria-previsione`

### La skill
`tesoreria` — i cinque comandi che bastano.

### I dati
`company/Memory/tesoreria/entrate.jsonl` e `spese.jsonl`. Testo, una riga per movimento.
**Scelta voluta:** si leggono a occhio, si correggono a mano, e due soci che lavorano in
parallelo non si sovrascrivono quando le loro modifiche si fondono. Niente database: *un
database che nessuno sa aprire è un altro posto dove i numeri vanno a nascondersi.*

---

## 3. Le tre leggi del reparto

### Previsto non è incassato. Mai.
Un preventivo mandato e un bonifico arrivato sono due cose diverse. Sommarli è il modo
classico di credersi ricchi mentre il conto è vuoto. I due numeri restano separati sempre,
anche quando la somma farebbe più bella figura.

### Un numero che non esiste si dichiara, non si stima.
Una stima presentata come misura è **esattamente il male che questo reparto esiste per
curare**: l'azienda ci è arrivata credendo di sapere cose che non aveva mai contato.

### La storia dei soldi non si riscrive, si annota.
Un movimento sbagliato non si cancella: se ne accoda uno di rettifica con la nota che
spiega perché. I file sono ad accodamento apposta. **Chi cancella una riga di tesoreria
sta cancellando una prova.**

---

## 4. La regola del passato vuoto

**La tesoreria parte oggi, 2026-09-03. Prima non c'è storia** — non perché non sia
successo niente, ma perché l'azienda non lo scriveva da nessuna parte.

**Quei mesi restano vuoti.** Ricostruirli a memoria riempirebbe la tesoreria di numeri
che nessuno può verificare, e un numero non verificabile è peggio di un vuoto dichiarato,
perché ha l'aria di una misura.

Serviranno **almeno tre mesi** di movimenti prima che qualunque previsione di crescita
smetta di essere un'invenzione con l'aria di un calcolo.

---

## 5. Cosa NON copre — dichiarato, non nascosto

- **Il percorso di vendita.** La tesoreria conta i soldi, non ciò che li precede:
  contatti, chiamate, preventivi mandati, tasso di chiusura. **Resta il buco più grande
  del CRO** e va chiuso dopo, con lo stesso metodo. → nuova voce **B-049**.
- **Le tasse e il commercialista.** La soglia SRL (85-100k, sotto cui il forfettario rende
  il 57-63% in più) è un numero che il reparto consegna al CFO, non una consulenza.
- **L'autorizzazione delle spese**, che resta del `cfo-empire`.
- **⚠️ Non esiste ancora un tetto di spesa in euro**: tutte le soglie del CFO sono
  percentuali di un denominatore mai fissato. Una percentuale del nulla non ferma nessuno
  (B-048).

---

## 6. La condizione di sopravvivenza

Una tesoreria vive o muore su una cosa sola: **che qualcuno registri i movimenti**.

Un movimento annotato tre giorni dopo è un movimento perso; un mese saltato rende
inservibile il confronto; e una tesoreria che mente diventa, in due settimane, un altro
file che nessuno apre — esattamente come i quindici puntatori a `ADR-012` che nessuno
guardava.

**Il primo movimento va registrato oggi.** Anche uno solo. Anche piccolo. Un registro
vuoto e un registro che non esiste si assomigliano troppo.

---

## 7. Il principio

> **Un'azienda sa di sé solo ciò che misura.** Tutto il resto — comprese le cose di cui è
> assolutamente certa — è memoria, e la memoria di un'impresa che cresce è la cosa meno
> affidabile che possiede.

---

*Legami: [[ADR-016]] (l'ultimo metro, che ha reso visibile il buco) · `cfo-empire` ·
`cro-empire` · `cmo-empire` · `sentinel-cost` · voci B-043 (chiusa), B-048, B-049 ·
`scripts/tesoreria.py` · skill `tesoreria`*
