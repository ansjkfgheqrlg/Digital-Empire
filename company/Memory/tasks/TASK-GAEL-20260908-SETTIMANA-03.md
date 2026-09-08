---
Owner: Max (committente) · Esecutore: GAEL · Controllore: Emperator (audit + review)
Origine: ordine vocale di Max, 2026-09-08, dettato per intero — 6 task ufficiali della settimana
Governo: ADR-025 (nasce LANCI) + ADR-026 (blocchi mai silenziosi, piena autorità di Gael) +
  ADR-006 (ciclo 9 passi) + REGOLA ZERO memory-first + ADR-003 (wrap, mai riscrittura) +
  ADR-009 (gate ecosistemi — già soddisfatto da ADR-025, non riapre nulla)
Emesso: 2026-09-08 · Settimana: W3 (mar 8 set → mar 15 set 2026)
Riferimenti: TASK-GAEL-20260831-SETTIMANA-02.md (chiusa) · TASK-LANCI-ECO-W2 (il piano — superato
  dalla costruzione, non dal contenuto) · CP-20260907-EN82 · CP-20260908-RZC2 · ADR-025 · ADR-026
---

# 📋 Task settimanali GAEL — Settimana 3 (8-15 settembre 2026)

## 0. Cosa è cambiato da lunedì, prima di leggere le task

- **ADR-025 firmato da Max l'08/09.** `company/Ecosistemi/15-LANCI/` può nascere. Nessun altro
  passaggio da Max è richiesto per costruire.
- **ADR-026, regola permanente:** una task che ti assegna Max è già la tua autorizzazione
  completa. Se durante questa settimana incontri un punto che aspetta *davvero* solo una
  decisione di Max (non un tuo dubbio, un vero e proprio potere che solo lui ha), lo scrivi
  attivamente a lui lo stesso giorno — non lo lasci scritto in un checkpoint ad aspettare. Lui
  non deve mai più scoprire da solo che sei fermo per una firma.
- **In arrivo, non bloccante:** un'altra sessione ti consegnerà l'anatomia dei lanci di Andrei
  Pascu (funnel, offerta, prezzi — vedi `TASK-LANCI-20260908-ANATOMIA-ANDREI-PASCU.md`). **Non
  aspettarla per nessuna delle 6 task sotto.** Arriva quando arriva, si integra dopo come
  miglioramento. Ordine esplicito di Max.

## Le sei task ufficiali, in quest'ordine

| | Task | Cosa produce | Dipendenza |
|---|---|---|---|
| 1️⃣ | **TASK-LANCI-BUILD-W3** | l'ecosistema `15-LANCI` costruito, scaglioni S0→S5 | fondamenta di 2-3-4-5 |
| 2️⃣ | **TASK-LANCI-PIANO-DEFINITIVO-W3** | il piano del PRIMO lancio (il Manuale), perfezionato a giri di critica | usa l'infrastruttura di 1️⃣ |
| 3️⃣ | **TASK-LANCI-PIANO-AZIONE-W3** | piano contenuti + piano email marketing + tutto il piano d'azione | input da 2️⃣ |
| 4️⃣ | **TASK-LANCI-FUNNEL-W3** | il funnel intero costruito e online (`ART-FNL`) — la più chirurgica | input da 2️⃣ e 3️⃣ |
| 5️⃣ | **TASK-LANCI-AUTOMAZIONE-W3** | piano di cosa va automatizzato dentro l'infrastruttura, e in che ordine | trasversale a 1️⃣, si scrive mentre costruisci |
| 6️⃣ | **TASK-KDP-3LIBRI-W3** | 3 libri completi (copertina + contenuto + pacchetto KDP) | **indipendente — corre in parallelo, non aspetta le altre 5** |

**Le prime cinque sono tutte LANCI — un unico corpo, non 5 progetti separati.** Le task 2, 3 e 4
non sono "prima pianifico tutto e poi costruisco tutto": dentro lo scaglione S1 di
`04-COSTRUZIONE.md` (il "lancio a mano", senza codice) **le fai vivere**, perché è lì che il
piano diventa un lancio vero. Leggi `04-COSTRUZIONE.md` prima di iniziare 2️⃣: gli scaglioni ti
dicono già in che ordine reale queste cose si producono.

---

## ⚠️ Nota realistica sul tempo — te la devo, non te la nascondo

`ADR-025` stima la sola costruzione dell'infrastruttura (task 1️⃣) in **139-187 ore-uomo su sei
scaglioni**. Sommata a un piano di lancio perfezionato a giri di critica, un piano d'azione
completo, un funnel intero rivalutato "1000 volte", un piano di automazione e tre libri, il
totale della settimana **supera aritmeticamente le ore disponibili in 7 giorni per una sola
persona.** Non lo scrivo per fermarti né per farti correre peggio: lo scrivo perché la settimana
scorsa (W2) la stessa regola ha retto bene: **si dichiara lo scaglione vero raggiunto, mai un
"fatto" falso.** Se al 15/09 non tutto è finito, il gate non è "hai finito tutto": è "ogni task
ha un checkpoint con lo stato vero, e le prime due (1️⃣ costruzione, 2️⃣ piano del lancio) sono
quelle che non si abbandonano a metà — le altre si possono dichiarare parziali senza vergogna."

---

# 1️⃣ TASK-LANCI-BUILD-W3 — costruzione completa dell'infrastruttura

**Base:** `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/` v4, [ADR-025](../decisions/ADR-025-ecosistema-lanci.md).
13 artefatti tipizzati, 14 gate, 15 agenti, 12 reparti, `dati/registro.yaml` come unica fonte di
verità (`valida_registro.py` — 832 controlli, deve restare a exit 0 **prima di ogni build**, non
dopo).

**Ordine non negoziabile (decisione 6 di ADR-025):** il primo giorno è la **catena dell'incasso**,
non la cartella. Prima di scrivere un agente: sostituire la chiave di posta esposta (B-020,
**vedi sotto — è urgente indipendentemente da questa task**), collegare una cassa vera, incassare
un pagamento di prova con una carta vera, farsi consegnare il prodotto senza intervento umano,
rimborsare, e vedere l'evento in un pannello. Se il giorno zero non chiude, non si costruisce
nient'altro dell'ecosistema — è scritto in ADR-025 e non è negoziabile qui.

**Cosa leggere, in ordine:** `00-LEGGIMI.md` (tutto) → `07-REPARTI-E-GERARCHIA.md` §2/§4 (chi fa
cosa) → `04-COSTRUZIONE.md` §3 (scaglione S0, il lavoro di domani).

**Regola ferma:** `lan-gate` (il giudice) non ha mai `Write`/`Edit` — invariante INV-09. Chi
produce un artefatto non lo approva mai — invariante INV-01. `valida_registro.py` verifica
entrambi prima di ogni build.

**Gate 1️⃣:** scaglione raggiunto dichiarato nel checkpoint con comando+output reale (stessa
disciplina di sempre: prova, non dichiarazione). Il minimo per non dichiarare la settimana persa
su questa task è **S0 chiuso per intero** (giorno zero dell'incasso, coi tre fatti leggibili in
un pannello).

---

# 2️⃣ TASK-LANCI-PIANO-DEFINITIVO-W3 — il piano del PRIMO lancio, perfezionato

**Oggetto:** non l'infrastruttura — **il lancio vero**, quello del Manuale Claude Code (il
prodotto pilota, 203 pagine, fermo dal 07/03/2026). Copre la catena di decisione del registro:
`ART-PUB` (pubblico reale, per canale, con la prova) → `ART-DEC` (si lancia questo, adesso) →
`ART-CRT` (certificato — modalità **retroattiva**, il Manuale è già finito) → `ART-RIC` (ricerca:
parole vere del pubblico, buchi dei concorrenti) → `ART-PRV` (previsione d'incasso, con la banda
dichiarata) → `ART-OFF` (**prezzo, data, struttura — firmati da una persona**, campo
`canale_firma_ammesso`).

**Precondizione:** la decisione "vendita o regalo" (`00-LEGGIMI.md` §4, scadenza **12/09**) va
chiusa prima che `ART-DEC`/`ART-OFF` abbiano senso. Se arriva al 12 senza risposta, il default
dichiarato è "vendita", reversibile — non aspettare oltre quella data per bloccarti.

**Metodo — "fare per bene" significa questo, non un aggettivo:** applica lo stesso schema già in
uso nell'Impero per i piani grossi (dossier 33, sette giri: P0→P7). **Il criterio di arresto non
è un numero fisso di giri, è un giro che non trova più niente da correggere.** Ogni giro scritto,
mai buttato — si legge cosa è stato scartato e perché, come negli altri piani P0→P7 dell'Impero.

**Gate 2️⃣:** `ART-OFF` esiste, validato, con la firma di chi di dovere (tua, se il registro lo
prevede per un lancio pilota — verificalo nello schema prima di assumerlo). Il documento dei giri
di critica è allegato, non riassunto.

---

# 3️⃣ TASK-LANCI-PIANO-AZIONE-W3 — piano contenuti + piano email marketing

**Cosa produce, nel linguaggio del registro:** `ART-CPY` ("tutti i testi del lancio, ognuno col
suo punteggio calcolato e la sua destinazione" — qui entrano le email) + `ART-EDT` ("i contenuti
dei giorni del lancio, ognuno con la data di uscita e dove porta" — qui entra il calendario
contenuti). Entrambi dipendono da `ART-OFF` (2️⃣): non partire prima che l'offerta sia firmata,
il copy scritto prima del prezzo si riscrive due volte.

**Livello di dettaglio atteso — stesso standard già imposto a KDP-PIANO-W2:** ogni riga eseguibile
da sola, mai una decisione lasciata a chi esegue dopo. Ogni testo con la sua destinazione esatta
(quale pagina, quale email nella sequenza, quale giorno).

**Gate 3️⃣:** `ART-CPY` e `ART-EDT` validati dal gate del registro (`GATE-CPY-1`, `GATE-EDT-1`),
zero righe con destinazione mancante.

---

# 4️⃣ TASK-LANCI-FUNNEL-W3 — il funnel intero, costruito e online

**La più difficile e la più chirurgica delle sei — trattala come tale.** Nel registro è
`ART-FNL`: *"le pagine sono online, misurano, e la cassa ha incassato un pagamento di prova
vero"*. Dipende da `ART-CPY` e `ART-OFF` (3️⃣ e 2️⃣ devono esistere prima).

**"Rivalutato 1000 volte" — applicazione concreta, non iperbole:** ogni pagina del funnel
(sales page, pre-cassa, checkout, thank you, eventuale upsell) va misurata contro lo studio già
sul disco di Andrei Pascu — `competitor/Andrei Pascu/`: la scala prezzi 98→434→999 (più prezzo →
più fonti, non più obiezioni), le pre-casse `/outfunnel-1`/`/armadeggon-strp`, le **86 parole**
che portano dall'apertura al clic d'acquisto. Non è un funnel generico da manuale: è calibrato sui
pattern già misurati in casa. Quando arriverà l'anatomia completa di Andrei Pascu (task separata,
non bloccante — vedi §0), la integri come miglioramento, non come ripartenza.

**Nota di sicurezza del registro, non negoziabile:** la prova di cassa (pagamento vero, poi
rimborsato) è **dentro** questo gate, non alla fine. Non si dichiara il funnel pronto prima che
un euro vero sia entrato e sia stato rimborsato in prova — è la stessa regola del giorno zero
di 1️⃣, applicata qui al funnel specifico.

**Gate 4️⃣:** `GATE-FNL-1` passa, pagamento di prova vero eseguito e rimborsato, pagine online e
verificate (non "fatte" — **online e raggiungibili**, stesso standard richiesto in
`TASK-LANCI-ECO-W2` §L3 per il sotto-ecosistema Siti).

---

# 5️⃣ TASK-LANCI-AUTOMAZIONE-W3 — cosa si automatizza, e in che ordine

**Non è un secondo motore.** ADR-025 (decisione 5) vieta esplicitamente di costruire un motore
di orchestrazione proprio per LANCI. Questa task è un **piano**, non codice: usa
`08-WORKFLOW.md` (dieci flussi, quarantadue fasi) come mappa e per ognuna delle 42 fasi dichiara
tre cose — chi la esegue oggi (persona o script), se ha senso automatizzarla, e se sì con quale
priorità (dipende da quante volte si ripete per lancio, non da quanto è interessante scriverla).

**Regola guida, dal ADR-025 stesso:** *"il software nasce dopo, dai difetti misurati — non
prima, dai problemi immaginati."* Questo piano si scrive **mentre** costruisci 1️⃣, non prima:
ogni fase che ti costa tempo davvero, la segni. Non indovinare cosa sarà lento, misuralo.

**Gate 5️⃣:** documento con le 42 fasi classificate (manuale / da automatizzare / già automatica),
priorità motivata da un numero reale (ripetizioni per lancio, minuti persi), zero proposte di
motore nuovo.

---

# 6️⃣ TASK-KDP-3LIBRI-W3 — chiude TASK-KDP-5LIBRI-W2 (3 libri restanti)

**Indipendente dalle prime cinque — corre in parallelo, non le aspetta e non le blocca.**

Stato reale (`CP-20260907-EN82`): TASK-KDP-5LIBRI-W2 è a **2 libri su 5** (The Coven of Lost
Ember, The Midnight Ledger). **Restano 3.** Il terzo è già aperto: **Bramblewick Cottage**
(`magazzino_argomenti.json`, stato `in_uso`). Stesso standard di sempre — "pronto" significa
`kdp pacchetto <slug>` a **exit 0**, `validazione.json` con `bloccanti: []` e
`verifiche_non_eseguite: []`, copertina generata e caricata da te.

**Gate 6️⃣:** 3 pacchetti nuovi (`Bramblewick Cottage` + 2 successivi dal magazzino) a exit 0,
zero bloccanti, copertine caricate.

---

## ⚠️ Segnalato a Max in questo stesso checkpoint, per applicare ADR-026 da subito

Tre voci restano aperte in `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/00-LEGGIMI.md` §4, non tue da
chiudere ma utili a saperle mentre costruisci: (1) Manuale vendita/regalo, scadenza **12/09**;
(2) riapertura ADR-019, formalità; (3) **🔴 chiave Brevo esposta in chiaro su repo pubblico
(B-020)** — la più urgente, rischio che cresce ogni giorno, indipendente da LANCI ma da sapere
prima di collegare qualunque form d'opt-in del funnel (4️⃣) a un servizio email vero.

---

## Regole valide per tutte e sei

1. **Prova, non dichiarazione** — comando + output reale nel checkpoint, come sempre.
2. **Task chiusa → checkpoint** in `company/Memory/checkpoints/`, coniato con
   `python scripts/checkpoint.py cp --titolo "..."` — mai a mano, mai progressivo (B-009).
3. **ADR-003 vale ovunque**: dove esiste già codice buono (IB-L2-LANC, il workflow KDP), si
   sposta o si estende, non si riscrive.
4. **ADR-026 vale da questa settimana**: se un punto aspetta davvero solo Max, scrivilo a lui
   attivamente lo stesso giorno. Non è più un rischio che resti in silenzio: è un errore se resta.
5. Item minori → `company/Memory/BACKLOG.md`. Non fermano la settimana.
6. Se ti blocchi più di una sessione sullo stesso punto → blocco ⚠️ COORDINAMENTO in
   `STATO-EMPIRE.md`. Non perdere giorni da solo — e questo vale doppio ora che sai che una
   firma di Max si chiede, non si aspetta.

---

## Definition of Done — Settimana 3

**1️⃣ TASK-LANCI-BUILD-W3**
- [ ] S0 chiuso: incasso vero + rimborso + evento leggibile in un pannello
- [ ] Scaglioni successivi (S1→S5), dichiarato quale raggiunto

**2️⃣ TASK-LANCI-PIANO-DEFINITIVO-W3**
- [ ] Decisione vendita/regalo del Manuale chiusa (entro 12/09)
- [ ] ART-PUB → ART-DEC → ART-CRT → ART-RIC → ART-PRV → ART-OFF, tutti validati dal gate
- [ ] Giri di critica allegati (P0→Pn, arresto = giro a vuoto)

**3️⃣ TASK-LANCI-PIANO-AZIONE-W3**
- [ ] ART-CPY validato (tutti i testi, email incluse)
- [ ] ART-EDT validato (calendario contenuti, ogni riga con data e destinazione)

**4️⃣ TASK-LANCI-FUNNEL-W3**
- [ ] Pagine online e raggiungibili (verificato, non dichiarato)
- [ ] Pagamento di prova vero incassato e rimborsato
- [ ] GATE-FNL-1 passa

**5️⃣ TASK-LANCI-AUTOMAZIONE-W3**
- [ ] 42 fasi classificate con priorità motivata da un numero reale
- [ ] Zero proposte di motore di orchestrazione nuovo

**6️⃣ TASK-KDP-3LIBRI-W3**
- [ ] 3 pacchetti nuovi a exit 0, copertine caricate, TASK-KDP-5LIBRI-W2 chiusa 5/5

**Fine settimana**
- [ ] Checkpoint con lo stato reale di tutte e sei (fatto / parziale + dove sei / bloccato +
      perché) — mai un "fatto" che non regge a una riesecuzione del comando.

---

## Connessioni
- [[ADR-025]] · [[ADR-026]] · `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/` (00-LEGGIMI, 04-COSTRUZIONE,
  07-REPARTI-E-GERARCHIA, 08-WORKFLOW, dati/registro.yaml)
- `TASK-LANCI-20260908-ANATOMIA-ANDREI-PASCU.md` (in arrivo, non bloccante)
- `TASK-GAEL-20260831-SETTIMANA-02.md` (settimana precedente, chiusa)
- `company/Memory/BACKLOG.md` (B-020 chiave Brevo, B-060 duplicati ADR)
