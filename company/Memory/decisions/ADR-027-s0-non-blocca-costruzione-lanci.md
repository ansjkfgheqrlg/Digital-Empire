# ADR-027 - S0 non blocca la costruzione di LANCI - solo la prova finale d'incasso vero

- **Stato:** ATTIVA
- **Data:** 2026-09-09
- **Ordinato da:** Max, testuale: *"chissene frega di questi problemi, sono importanti ma
  Gael può costruire tutta l'infrastruttura comunque senza problemi"*
- **Amende:** ADR-025, decisione 6 (*"se il giorno zero non si chiude, non si costruisce
  nient'altro dell'ecosistema"*)
- **Nasce da:** [[CP-20260909-DA2P]] — ho portato a Max i 3 gesti "mani umane" che fermano S0
  (MT-FJF6/MT-32RU/MT-CV7N) trattandoli, per applicazione letterale di ADR-025 decisione 6,
  come motivo per cui l'INTERA task 1️⃣ (`TASK-LANCI-BUILD-W3`) fosse "formalmente ferma". Max
  ha corretto sul posto: sbagliato.

## Contesto

ADR-025 decisione 6 dice: il primo giorno di costruzione è la catena dell'incasso, e se non
chiude "non si costruisce nient'altro dell'ecosistema". L'ho applicata alla lettera: le tre
micro-task "mani umane" (revocare la chiave Brevo, collegare una cassa vera, incassare e
rimborsare con carta vera) non toccabili da nessuna sessione, quindi ho scritto che tutta la
task 1️⃣ era ferma finché Max non avesse fatto quei tre gesti.

**Max ha corretto l'interpretazione, non il problema.** I tre gesti restano veri, urgenti, e
solo suoi (non ritrattati qui). Ma bloccare la SCRITTURA di 12 micro-task di codice/agenti/gate
in attesa che lui apra un conto pagamenti è uno scambio di due cose diverse: la **prova che la
catena dell'incasso funziona con denaro vero** (che dipende da lui) e la **costruzione del
codice che quella catena userà** (che non dipende da lui per niente — Gael può scrivere
`stato_lancio.py`, i sei agenti, `lan-gate`, i quattro artefatti a mano, il governo, ecc. senza
aver mai visto un pannello Brevo).

## Decisione

**1. La costruzione di `15-LANCI` (task 1️⃣, tutte le micro-task da `MT-F37C` in giù, cioè le 9
delle 12 che non sono "mani umane") procede SUBITO, in parallelo alle tre mani-umane — non le
aspetta.** Gael scrive codice, agenti, gate, artefatti a mano, governo: tutto quello che oggi
è già scritto nei corpi delle micro-task, senza bisogno di una cassa vera collegata.

**2. Quello che resta bloccato da `MT-FJF6`/`MT-32RU`/`MT-CV7N` è UN solo gate, non l'intero
ecosistema: la prova finale che S0 è chiuso davvero** — l'evento leggibile in un pannello con
un euro vero entrato, consegnato, rimborsato. Quel gate specifico (non la costruzione) resta
non negoziabile: nessuna dichiarazione di "S0 chiuso" senza quella prova reale, come sempre
(§3 emperator.md, prova non dichiarazione).

**3. `lan-gate` e i controlli automatici del registro possono essere scritti e testati con
un pagamento SIMULATO/di test lato codice** (dati finti nello schema, non finzione sulla
dichiarazione di chiusura): il divieto è dichiarare S0 chiuso senza il pagamento vero, non
scrivere il codice che lo gestirà.

**4. Correzione di ADR-025 decisione 6:** dove diceva *"se il giorno zero non si chiude, non
si costruisce nient'altro dell'ecosistema"*, si legge ora *"se il giorno zero non si chiude, il
gate finale di S0 non passa — il resto dell'ecosistema si costruisce comunque, e si integra col
pagamento vero appena Max chiude i tre gesti umani"*. ADR-025 non si riscrive nel file
originale (si conserva la storia): questo ADR la sovrascrive su questo punto specifico, tutto
il resto di ADR-025 resta intatto (ordine artefatti, tetto spesa, niente motore proprio,
`lan-gate` senza scrittura, punti umani con scadenza).

## Conseguenze

**Diventa vero, da ora:**
- Gael riprende `TASK-LANCI-BUILD-W3` da `MT-F37C` in giù, oggi stesso, senza aspettare Max.
- Le tre mani-umane restano aperte, in cima a `STATO-EMPIRE.md`, e restano SOLO di Max — ma non
  sono più lette come "blocco dell'intera settimana 1️⃣".
- Il gate `S0 chiuso` (evento vero in un pannello) resta l'unico punto dove "costruito" non
  basta e serve la prova reale.

**Resta vero, immutato:**
- Le altre 7 decisioni di ADR-025 (ordine artefatti, tetto 15$/lancio, niente motore proprio,
  `lan-gate` senza Write/Edit, punti umani con scadenza, firme con canale ammesso) non cambiano.
- ADR-026 (blocchi mai silenziosi) non cambia: il principio "un blocco reale si porta a Max
  attivamente" resta — cambia solo cosa quel blocco ferma davvero.

**Errore mio riconosciuto:** ho letto "non negoziabile" in ADR-025 e l'ho esteso a un perimetro
più largo di quanto la frase dicesse (tutto l'ecosistema, non solo il gate S0) — la stessa
famiglia di errore di [[feedback_max_spiega_concreto]] applicata al contrario: non vaghezza
nel dare l'ordine, ma un'estensione non verificata nel riceverlo. Da ricontrollare la prossima
volta che leggo "non negoziabile" in un ADR: negoziabile *cosa esattamente*, non l'intera task.

## Rapporto con gli ADR esistenti

- **ADR-025** — questo ADR ne corregge la sola decisione 6, punto sul perimetro del blocco.
  Le altre 7 decisioni restano invariate.
- **ADR-026** — resta la regola di escalation; qui si applica correggendo cosa viene escalato
  come "bloccante".
- **[[CP-20260909-DA2P]]** — il checkpoint che ha applicato l'interpretazione poi corretta qui.

---

*Legami: [[ADR-025]] · [[ADR-026]] · `company/Memory/tasks/TASK-GAEL-20260908-SETTIMANA-03.md`
· `company/Memory/tasks/micro/TASK-LANCI-BUILD-W3/`*
