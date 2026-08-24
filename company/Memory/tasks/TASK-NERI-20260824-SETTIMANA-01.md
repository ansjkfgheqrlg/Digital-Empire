---
Owner: Max (committente) · Esecutore: NERI · Controllore/Mentore: Emperator Agent (supporto diretto e costante, non solo review)
Origine: richiesta esplicita Max 2026-08-23 — Neri passa da ruolo organizzativo a operativo su tutto Outreach
Governo: REGOLA ZERO memory-first · vedi anche company/Memory/tasks/TASK-GAEL-20260824-SETTIMANA-01.md (stessa settimana, stessa struttura, Gael)
Emesso: 2026-08-23 · Settimana: W1 (lun 24 ago -> dom 30 ago 2026)
---

# 📋 Task Settimana 1 per NERI (24-30 agosto 2026)

Neri, questo è il primo blocco di task che ti scrivo dopo il passaggio deciso da Max: da qui
in avanti ti occupi tu di tutto l'**Outreach** di Digital Empire, non solo di organizzazione.
È un salto vero, e Max lo sa — per questo mi ha chiesto esplicitamente di starti molto più
vicino di quanto faccio con Gael. Quindi prima di ogni pezzo tecnico ti spiego cosa stiamo
facendo e perché, non solo il comando da lanciare. Se qualcosa non è chiaro, **chiedimelo
prima di procedere alla cieca** — è molto meglio una domanda in più che un giorno perso a
girare intorno a un problema.

Sono l'**Emperator Agent** — il mio ruolo operativo dentro Digital Empire (che è l'azienda
nel suo insieme) quando lavoro con te e con Gael. Mi trovi qui ogni volta che ti serve.

---

## 0. Come funzionano le task settimanali (stesso sistema di Gael, primo giro per te)

Niente task giornaliere: ogni **domenica** arrivano qui le task della settimana intera. Tu
gestisci i tuoi giorni — alcuni pieni, altri leggeri, conta il risultato a fine settimana, non
il ritmo giornaliero. Quando chiudi (o comunque a fine sessione) scrivi un checkpoint in
`company/Memory/checkpoints/CP-20260824-NNN.md` (prendi il primo numero libero — guarda cosa
c'è già nella cartella prima di scegliere il numero, altrimenti rischi una collisione con
Gael/Claude che scrivono nello stesso posto) e aggiorna lo `stato` in
`EmpireDesk/state/taskboard.json` per l'ID della task.

Questa settimana **2 task**, non di più — di proposito, per non sommergerti al primo giro.
Meglio farne una bene e capirla davvero che farne quattro a metà.

---

## Perché l'Outreach conta così tanto per Digital Empire

Prima del "come", il "perché": l'Outreach è come Digital Empire trova clienti veri, senza
aspettare che arrivino da soli. Non è un dettaglio tecnico — è il motore che porta soldi
dentro. Due prodotti diversi lo usano, con logiche diverse:

- **Preventa** — venduto a concessionari auto (import). Prezzo attuale: €2.000 una tantum
  (deciso da Max, sostituisce una vecchia proposta a abbonamento). Lead = concessionari
  specifici, trovabili con criteri geografici/di settore precisi.
- **Outreach Factory** (cartella `Outreach/Outreach Workflow/`) — il prodotto con il
  potenziale più alto di tutto Digital Empire quest'estate: build da **€5.000-15.000** a
  cliente. Una sola vendita chiusa vale più di gran parte del resto del piano estate messo
  insieme. Qui i lead sono clienti generici (qualsiasi business che vuole outreach
  automatizzato per sé), non concessionari — serve quindi un ventaglio di canali più ampio.

Questo spiega perché Max vuole più canali su entrambi: più fonti di lead + più canali di
invio = più probabilità di trovare chi risponde, su prodotti diversi con pubblici diversi.

---

## 🟢 TASK-PREVENTA-CANALI-W1 — Preventa: nuove fonti lead + nuovo canale di invio

**Dove**: `Outreach/preventa-maps-scraper/` (motore attuale: `scraper.py` per Google Maps,
`contact_leads.py`, `outreach_giornaliero.py` per l'invio automatico giornaliero). Invio
WhatsApp reale in `Outreach/WhatsApp Automation/` (sessione tramite profilo Chromium
persistente, **non toccare** la logica di sessione — usa `launch_persistent_context`, motivo
tecnico preciso, chiedimi prima se pensi serva cambiarla). Lead salvati in
`EmpireDesk/state/preventa_leads.json` (CRM Areus, non più Google Sheets).

**Cosa c'è oggi**: una sola fonte di lead (Google Maps) e un solo canale di invio (WhatsApp).
Funziona, ma è un imbuto stretto — se Google Maps non ha abbastanza concessionari in una
zona, o un lead non risponde su WhatsApp, oggi non c'è un piano B.

**Cosa aggiungere questa settimana**:
1. **Instagram come nuova fonte lead** — cercare concessionari auto import anche via
   Instagram (profili business locali), non solo Google Maps. In `Outreach/Instagram
   Automation/` c'è già un motore IG generico (usato per altri prodotti) — guarda come
   funziona prima di scriverne uno nuovo da zero, magari basta adattarlo.
2. **Libreria delle Inserzioni Meta (Facebook Ad Library)** come nuova fonte lead — i
   concessionari che fanno pubblicità su Meta sono lead più caldi (hanno budget, sono attivi
   online). È pubblica, consultabile senza login: `facebook.com/ads/library`.
3. **Gmail come nuovo canale di invio**, accanto a WhatsApp — non tutti i lead hanno un
   numero WhatsApp verificabile, ma quasi tutti hanno un'email pubblica sul sito o su Google
   Maps. Non serve inventare da zero: l'altro ramo di Outreach (`Outreach/Outreach Workflow/`)
   ha già un sender Gmail SMTP funzionante — guardalo prima come riferimento.

**Importante — non tutto insieme**: se questa settimana riesci a chiudere bene **una sola**
delle 3 aggiunte (es. solo Instagram, o solo Gmail), va benissimo. È molto meglio di
farne tre a metà e nessuna che funziona davvero. Scegli tu da dove partire, o chiedimi e
decidiamo insieme guardando cosa è più facile da agganciare al sistema esistente.

**Gate**: per ogni canale/fonte che aggiungi, dimostra che produce **lead reali** (non
finti/di prova) che finiscono nello stesso posto degli altri (`preventa_leads.json`), e che
un messaggio reale (anche uno solo, in dry-run se non hai ancora l'ok di Max per il live)
parte da quel canale. Nel checkpoint: comando + cosa è successo, con numeri veri.

---

## 🟡 TASK-OUTREACHFACTORY-CANALI-W1 — Outreach Factory: un canale in più (o uno più solido)

**Dove**: `Outreach/Outreach Workflow/` (email, il motore più maturo) + `Outreach/Instagram
Automation/` + `Outreach/LinkedIn Automation/` (già costruiti, verifica se girano ancora
davvero prima di aggiungerne altri — a volte le sessioni scadono, es. il token Facebook è
scaduto in passato).

**Perché proprio questo prodotto**: è quello con il ticket più alto (€5-15k), quindi è quello
dove vale di più investire tempo — ma è anche il più complesso, perché il cliente non è
verticale come Preventa (non sono tutti concessionari, sono business qualsiasi). Per questo
oggi ha già 3 canali (Email, Instagram, LinkedIn) invece di uno solo.

**Cosa fare questa settimana** (scegli tu, o decidiamo insieme — non fartelo dire e basta,
prova a ragionarci e dimmi cosa penseresti tu prima che ti risponda):
- **Opzione A**: aggiungere **Pagine Gialle** (paginegialle.it) come nuova fonte di lead
  generici — copre business italiani di ogni settore, buona fonte generalista per un prodotto
  che non è verticale su una nicchia sola.
- **Opzione B**: invece di aggiungere un canale nuovo, **verificare e sistemare** uno dei 3
  esistenti se non gira più bene (es. il token Facebook per Instagram scade periodicamente —
  controlla `.env` prima di dare per scontato che IG funzioni).

Non è un test con una risposta giusta — è una vera decisione di prodotto, e voglio che tu
inizi a farle. Se non sai da che parte guardare per decidere, dimmelo: ti faccio vedere come
ragionarci (dati che servono, cosa guardare prima di scegliere), non ti do solo la risposta.

**Gate**: stesso principio della task sopra — un lead reale generato dal canale nuovo/
sistemato, un invio reale (o dry-run verificato) che parte. Nel checkpoint spiega anche
**perché** hai scelto quella strada, non solo cosa hai fatto — è la parte che mi interessa
di più per capire come stai ragionando.

---

## Se ti blocchi (leggi PRIMA di arrenderti)

Bloccarsi è normale, capita a tutti — quello che conta è cosa fai dopo. Prova in ordine:

1. **Rileggi l'errore per intero**, non solo l'ultima riga — spesso la causa vera è più su.
2. **Chiediti: è la prima volta che questo tipo di errore appare nel repo?** Cerca nel codice
   (`grep`/ricerca testo) se qualcun altro ha già risolto qualcosa di simile — spesso sì.
3. **Scrivi in una riga cosa ti aspettavi e cosa è successo invece** — il solo fatto di
   scriverlo spesso fa vedere il problema da un'altra angolazione.
4. **Se dopo questo sei ancora fermo, chiamami** — scrivimi cosa hai provato (non solo "non
   funziona"), è molto più veloce per me aiutarti se vedo i tentativi già fatti.

Non è debolezza chiedere aiuto a metà — è debolezza restare fermi un giorno intero senza
dirlo a nessuno. Se blocchi più di una sessione sullo stesso punto, scrivilo anche in
`STATO-EMPIRE.md` (blocco ⚠️ COORDINAMENTO) così Max lo vede.

---

## Regole operative

1. **Prova, non dichiarazione** — comando + risultato reale incollato nel checkpoint.
2. Task chiusa (anche parziale) → checkpoint + `EmpireDesk/state/taskboard.json` aggiornato
   per `TASK-PREVENTA-CANALI-W1` / `TASK-OUTREACHFACTORY-CANALI-W1`.
3. Item minori scoperti strada facendo → `company/Memory/BACKLOG.md`, non fermano la
   settimana.
4. Prima di lanciare invii reali (non dry-run) su un canale nuovo, chiedi conferma esplicita
   a Max o a me — stessa regola di sempre per azioni verso l'esterno.

---

## Definition of Done — Settimana 1 (Neri)

- [ ] TASK-PREVENTA-CANALI-W1: almeno 1 fonte/canale nuovo per Preventa, funzionante con lead reali
- [ ] TASK-OUTREACHFACTORY-CANALI-W1: 1 canale nuovo o sistemato per Outreach Factory, con motivazione della scelta
- [ ] checkpoint di fine settimana con stato reale (fatto/parziale+dove sei/bloccato+perché — va benissimo anche "bloccato", basta che sia scritto)
