---
Type: CONCEPT
Status: Active
Tags: #principi #account-management #customer-success #retention #A7
Created: 2026-07-11
Last updated: 2026-07-11
---

# PRINCIPI — A7 Account Management & Customer Success

> I principi orientano il **giudizio** quando la regola non copre il caso. Le regole
> (`regole/REGOLE.md`) sono bloccanti; i principi spiegano **perché** lo sono.

---

## P1 — Un cliente, un proprietario

Ogni cliente ha **un** Key Account Manager (AG-A7-COORD), assegnato alla firma, proprietario della
relazione per tutto il ciclo. Non un team generico, non "chi risponde per primo": una persona.

**Razionale operativo:** il gap del v1 era esattamente questo — il cliente veniva consegnato da
A4-Delivery e poi non aveva più un interlocutore strutturato. Un cliente che non sa a chi scrivere
smette di scrivere, e un cliente che smette di scrivere è un cliente che sta già andandosene. La
proprietà unica rende il silenzio un **segnale rilevabile** invece che una zona grigia.
Operativamente: `kam` è un campo obbligatorio (R1); un cliente senza KAM è un'anomalia bloccante,
non un'imperfezione tollerabile.

---

## P2 — La relazione non è l'esecuzione

A4-Delivery consegna il lavoro. A7 presidia la **relazione attorno al lavoro**. A7 non lavora i
ticket tecnici: ne supervisiona l'SLA e agisce sul rischio.

**Razionale operativo:** se A7 comincia a lavorare i ticket, due cose si rompono. Primo, duplica
A4 e crea due verità sullo stesso lavoro. Secondo — più grave — smette di guardare il cliente e
comincia a guardare il task. Il valore di A7 è avere un agente che osserva il **rapporto** mentre
qualcun altro esegue. Il dato SLA ticket è il documento di confine: A4 lo **produce**, A7 lo
**legge** e agisce. Nessuna scrittura di A7 su dati di A4.

---

## P3 — Il rischio si intercetta prima, non si gestisce dopo

Il churn non è un evento: è la fine di una traiettoria che era visibile settimane prima. AG-A7-HEALTH
esiste per rendere quella traiettoria **misurabile in tempo reale**.

**Razionale operativo:** un cliente che va perso al G+80 aveva 3 ticket aperti al G+40 e non
rispondeva da una settimana al G+50. Quei segnali esistevano — nessuno li stava guardando. Da qui
la finestra delle **24h** (R2): non perché 24h siano magiche, ma perché un alert che resta fermo
diventa rumore, e il rumore è indistinguibile dal silenzio. Un segnale osservato ma non registrato
in `agency/a7/alerts` **non conta come intercettato**.

---

## P4 — La trasparenza costa meno del recupero

Un ritardo comunicato è un problema. Un ritardo nascosto e poi scoperto è una crisi di fiducia.
AG-A7-COMM comunica i fatti verificati, con fonte, anche quando sono scomodi.

**Razionale operativo:** un cliente perdona un ritardo su cui è stato avvisato; non perdona di
essere stato rassicurato mentre le cose andavano male. Per questo ogni fatto comunicato deve avere
una **fonte nello state** (`agency/a7/*` o `agency/a4/sla/*`) e nessun draft può contenere claim
scoperti (R4). "Addolcire" un fatto verificato è un FAIL di gate, non una scelta di stile — e
AG-A7-COMM ha il mandato esplicito di **rifiutare** la richiesta e segnalarla ad AG-A7-QA.

---

## P5 — Un numero non misurato non esiste

L'NPS si raccoglie, non si stima. La salute account si calcola dai segnali, non dall'impressione.
Se il dato manca, il valore è `[DM]` — mai uno zero, mai una media di comodo, mai un "direi 8".

**Razionale operativo:** il momento in cui A7 comincia a stimare l'NPS "dal clima positivo" è il
momento in cui tutti i KPI del reparto diventano finzione, e i handoff a valle (upsell ad A3,
referral ad A6) partono su una base falsa. Da qui il gate più duro del reparto (R5): **senza NPS
la closure non si chiude**. Un ciclo `chiuso_con_riserva` con `nps: [DM]` è onesto; un ciclo chiuso
con un NPS inventato è un danno che si propaga a due reparti a valle.

---

## P6 — Il cliente soddisfatto è l'inizio, non la fine

A G+90 un cliente contento non è un ciclo concluso: è la materia prima più economica che l'agenzia
possieda. Upsell (→ A3), referral e case study (→ A6), cross-sell (→ 02-INFO).

**Razionale operativo:** il costo di acquisizione di un cliente nuovo è ordini di grandezza sopra
quello di un'espansione su un cliente che ha già firmato, ha già visto il lavoro e si fida. Il v1
lasciava questo valore sul tavolo per pura assenza di un agente che lo raccogliesse. **Ma:** il
referral si chiede **solo** a chi è realmente soddisfatto (NPS ≥8) e **solo** con consenso esplicito
(R8). Chiedere un referral a un detrattore non è ottimismo commerciale — è un errore di lettura che
brucia il rapporto residuo e conferma al cliente di non essere mai stato ascoltato.

---

## Connessioni

- [[REGOLE]] · `regole/REGOLE.md` — la forma bloccante di questi principi
- [[ag-a7-qa]] · `agenti/ag-a7-qa.md` — l'agente che rende P4 e P5 non aggirabili
- [[ag-a7-coord]] · `agenti/ag-a7-coord.md` — il KAM unico di P1
- [[A4-Delivery]] · `../A4-Delivery/` — il confine di P2
