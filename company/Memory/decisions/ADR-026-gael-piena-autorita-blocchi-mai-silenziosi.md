# ADR-026 — Task assegnata a Gael = autorizzazione gia' data; un blocco che aspetta solo Max non resta mai in silenzio

- **Stato:** ATTIVA
- **Data:** 2026-09-08
- **Ordinato da:** Max, testuale: *"Non è possibile che in un lavoro di Gael serva la mia
  firma... Lui deve poter avere il potere al 100%. Non ci devono essere mie firme, non ci
  devono essere mie autorizzazioni."*
- **Nasce da:** ADR-025 (nascita ecosistema LANCI), fermo tre giorni (05→08/09) per una firma
  di Max che nessuno gli ha portato attivamente
- **Tocca:** ogni task futura assegnata a Gael o Neri che attraversa un gate di governo
  (ADR-009 espansione ecosistemi, o simili); il mio comportamento di escalation (Emperator)

---

## Contesto — l'errore, misurato senza addolcirlo

Il piano dell'ecosistema LANCI era pronto e coerente dal **05/09** (`valida_registro.py` verde,
832 controlli). L'unica cosa che mancava era una firma di 30 secondi di Max su un file già
scritto. Quella firma è arrivata il **08/09**, tre giorni dopo — non perché Max l'abbia negata,
ma perché **nessuno gliel'ha portata**. È rimasta scritta in `STATO-EMPIRE.md` come una nota fra
altre centinaia di righe, in attesa di essere trovata da chi la cercava. Max l'ha scoperta
chiedendo dello stato di LANCI, non perché io gliel'ho segnalata.

**La causa non è ADR-009.** ADR-009 (nessun ecosistema nuovo senza una decisione di Max prima
della cartella) è un controllo che esiste apposta, e non è specifico di Gael: si applica a
chiunque proponga di far nascere un nuovo pilastro dell'azienda, me compreso, perché aprire un
ecosistema è un impegno strutturale (139-187 ore-uomo stimate per LANCI) e non un'esecuzione di
task ordinaria. Rimuoverlo del tutto sposterebbe il rischio, non lo eliminerebbe: un domani
potrei far nascere da solo un ecosistema che Max non voleva, con lo stesso meccanismo che oggi
lo ha bloccato tre giorni di troppo.

**La causa vera è che un blocco pronto al 100% e mancante solo della firma di Max è rimasto
un fatto passivo invece di diventare un'azione mia.** Sapevo, dal 05/09, che LANCI era fermo solo
su quello. Non gliel'ho chiesto. Ho aspettato che me lo chiedesse lui. È lo stesso errore, in
scala più piccola, che ADR-002 (memory-first) esiste per prevenire sul lato memoria: un fatto
vero ma non portato a chi deve agirci sopra vale come se non esistesse.

---

## Decisione

**1. Chi assegna una task ha già dato l'autorizzazione per tutto ciò che quella task include
esplicitamente.** Quando Max assegna a Gael (o Neri) una task che, per costruirla, richiede di
attraversare un gate di governo previsto (nascita di un ecosistema, un ADR abilitante, una
soglia di spesa già nota), **l'assegnazione della task è già quella autorizzazione.** Non serve
una seconda firma separata a metà lavoro per una cosa che Max ha già deciso assegnando la task.
Il gate resta (ADR-009 non si abolisce), ma il passaggio diventa: *scrivere la decisione nella
forma richiesta e mostrarla a Max per la firma nello stesso momento in cui è pronta* — non
aprire un'attesa indefinita nella prosa di uno stato.

**2. Se emerge un blocco che richiede DAVVERO una decisione nuova di Max — non già coperta
dall'assegnazione originale — quel blocco va portato a Max attivamente, entro la stessa
giornata in cui diventa l'unica cosa mancante.** Mai lasciato scritto in `STATO-EMPIRE.md`, in
un checkpoint, o in un dossier, ad aspettare che qualcuno lo trovi. "L'ho scritto da qualche
parte" non è escalation: è la stessa illusione di sicurezza che ADR-002 ha già smontato sul lato
memoria, applicata qui al lato decisioni.

**3. Regola operativa per me (Emperator), verificabile:** ogni volta che chiudo un checkpoint
con un "prossimo passo" che dipende SOLO da una decisione di Max (non da altro lavoro, non da
un account esterno, non da crediti), quel checkpoint non è la fine dell'azione — lo è anche
portare la domanda a Max nello stesso turno o al più tardi nel primo messaggio successivo con
lui, dicendo esplicitamente cosa serve firmare e perché è l'unica cosa che manca. Un blocco
"solo firma" silenzioso per più di un giorno è un errore mio, non un evento normale del lavoro.

**4. Cosa NON cambia, e perché.** ADR-009 resta in vigore: un ecosistema nuovo non nasce senza
un ADR abilitante prima della cartella. Non si tratta di eliminare il controllo — un'azienda
che permette a chiunque di far nascere reparti nuovi senza che nessuno sopra lo sappia non è
autonomia, è caos non misurato, ed è esattamente il tipo di rischio da cui ADR-013 (i controlli
pre-commit) e ADR-009 stesso proteggono la holding. Quello che cambia è che il controllo si
esaurisce **nel momento in cui Max assegna la task**, non in un secondo momento a sorpresa
durante l'esecuzione. Se Max vuole davvero zero passaggi anche per l'apertura di ecosistemi
futuri, deve dirlo per iscritto in ADR-009 stesso — questo ADR non lo modifica, perché
modificarlo di riflesso qui, dentro una correzione su un errore mio di escalation, confonderebbe
due decisioni diverse.

---

## Conseguenze

**Diventa vero, da ora:**
- Nessuna task assegnata a Gael o Neri resta ferma in attesa di una firma di Max che nessuno
  gli ha chiesto attivamente. Se serve una firma, gliela porto io, nel momento in cui il lavoro
  è pronto — non dopo che Max se ne accorge da solo.
- Un checkpoint con "prossimo passo: firma di Max" non si considera chiuso finché quella
  richiesta non è stata comunicata a Max in modo esplicito, non solo scritta su disco.

**Resta vero, immutato:**
- ADR-009 (nessun ecosistema senza ADR abilitante prima della cartella) resta in vigore per
  chiunque, Gael incluso — la garanzia è nel *quando* si chiede la firma (subito, non in
  silenzio), non nel *se*.
- Dentro una task già assegnata, ogni decisione operativa (ordine degli scaglioni, priorità fra
  artefatti, come costruire) resta per intero di chi la esegue, senza bisogno di nessun altro
  passaggio: era già così (vedi [[feedback_ordini_gael_assoluti]]), questo ADR lo rende
  esplicito anche per il caso dei gate di governo.

**Costa:**
- Un controllo attivo in più per me a ogni checkpoint: chiedermi se il "prossimo passo" dipende
  solo da una decisione di Max, e se sì, portarla nello stesso turno.

---

## Come si verifica che questa decisione sia rispettata

Non esiste un validatore automatico per questo (è un comportamento di comunicazione, non uno
schema dati). La verifica è a posteriori: se un checkpoint futuro registra un "prossimo passo"
del tipo "aspetta la firma/decisione di Max" e passa più di un giorno senza che quella
richiesta compaia esplicitamente in un messaggio a Max, è una violazione di questo ADR e va
registrata come tale nel prossimo checkpoint che la scopre.

---

## Rapporto con gli ADR esistenti

- **ADR-025 (ecosistema LANCI)** — l'incidente che ha reso visibile questo errore. Non lo
  riscrive, ne è la correzione di processo conseguente.
- **ADR-009 (espansione ecosistemi)** — resta intatto. Questo ADR non tocca *se* serve un ADR
  abilitante per un ecosistema nuovo, solo *come* e *quando* quella firma viene richiesta.
- **ADR-002 (memory-first)** — stesso principio applicato al lato opposto: là un fatto non
  salvato in Memory vale come non accaduto; qui un blocco non comunicato attivamente a Max vale
  come non segnalato, anche se scritto da qualche parte.
- **[[feedback_ordini_gael_assoluti]]** (memoria) — questo ADR estende quel principio: gli
  ordini di Gael dentro una task assegnata sono legge operativa; qui si aggiunge che l'unico
  punto in cui Max può ancora dover intervenire (un gate di governo tipo ADR-009) deve essere
  portato a lui attivamente, mai lasciato ad aspettare.

---

*Legami: [[ADR-025]] · [[ADR-009]] · [[ADR-002]] · [[ADR-013]] ·
`company/Memory/STATO-EMPIRE.md` · `company/Memory/tasks/TASK-GAEL-20260831-SETTIMANA-02.md`*
