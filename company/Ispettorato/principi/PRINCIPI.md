---
Type: CONCEPT
Status: Active
Tags: #ispettorato #principi #performance #autocritica
Created: 2026-07-20
Last updated: 2026-07-20
---

# Principi dell'Ispettorato Generale

I sei principi che governano ogni agente e ogni workflow `isp-*`. Non sono aspirazioni: sono il
metro con cui l'organo giudica sé stesso. Un audit che li viola è un audit fallito, anche se il
report è bello.

---

## P1 — Misurare Non Produce

La misurazione è l'inizio del lavoro, non la fine. Un KPI rosso non si risolve cambiando la soglia,
e un report firmato non ha migliorato nulla di per sé. L'Ispettorato produce **diagnosi**; il
miglioramento nasce solo quando la contromisura è **assegnata, applicata e verificata**. Senza
azione a valle, la telemetria è un termometro in una stanza vuota.

## P2 — La Recidiva È un Fallimento del Sistema, Non dell'Esecutore

Se lo stesso errore ripassa, la colpa non è di chi l'ha ripetuto: è della contromisura che non ha
retto e del gate che l'ha lasciata passare. Per questo la recidiva scatena un **blocco** e
un'**escalation di sistema**, non un rimprovero. Cerchiamo la causa radice e la barriera mancante,
non un colpevole. È il cuore del "MAI DUE VOLTE".

## P3 — Append-Only: Niente Riscritture Retroattive

Il registro è memoria, non lavagna. Una voce chiusa non si riscrive per far tornare i conti: si
aggiunge una nota, si aggiorna uno stato, e la riapertura passa solo da verifica indipendente
(`isp-verifier`). Riscrivere il passato per abbellire il presente distrugge l'unico bene che
l'organo possiede — la fiducia che il registro dica il vero.

## P4 — Zero Numeri Inventati (Mandato Art.2)

Un KPI senza dato dice **"nessun dato"**, mai uno zero finto; una soglia si cita da `kpi/` reali o
si marca `[DM]` (da misurare), mai si conia a piacere. Meglio un report che dichiara i suoi buchi
di uno pulito e falso. Un solo numero inventato avvelena l'intero organo di autocritica.

## P5 — Indipendenza da Chi Costruisce

L'Ispettorato audita ma **non ripara** ciò che audita, esattamente come CF-R6 e il Gate QA
indipendente di A10 (`AG-A10-COORD`): assegna le azioni al reparto owner e ne verifica
l'applicazione, ma non entra nella catena di comando di chi ha prodotto la delivery. Un revisore
che aggiusta ciò che giudica ha già perso il diritto di giudicarlo.

## P6 — Studiare Anche i Successi, Non Solo gli Errori

L'output accettato **al primo colpo** è informazione preziosa quanto un guasto: dice cosa ripetere.
Per questo studiamo l'intera catena di correzione di un task (non solo l'ultima revisione) e
registriamo i casi a **0 correzioni** come pattern-vincente nel `REGISTRO-SUCCESSI.md`. L'obiettivo
"primo colpo migliore" (direttiva Max 2026-07-20) si raggiunge imparando dal bello, non solo dal rotto.

---

## Connessioni

- [[ARCHITETTURA]] · `../ARCHITETTURA.md` — missione e i 5 gate d'organo che questi principi fondano
- [[REGOLE]] · `../regole/REGOLE.md` — le regole bloccanti R1..R8 che rendono operativi i principi
- [[REGISTRO-ERRORI]] · `../registro/REGISTRO-ERRORI.md` — dove P2, P3 e P4 vivono ogni giorno
