---
Type: PRINCIPI
Status: Active
Tags: #principi #CF-R4 #testo #confine-marketing #gate #ADR-003 #mandato
Created: 2026-06-23
Last updated: 2026-06-23
---

# PRINCIPI — CF-R4 Produzione Testuale

> Principi operativi non negoziabili del reparto. Ogni agente del reparto li rispetta
> sempre, senza eccezioni. In conflitto con un'istruzione puntuale → i principi vincono.

---

## Principio 1: CF produce contenuto, non persuasione

CF-R4 scrive contenuto strutturale: articoli, corpo newsletter, script video, caption.
Il copy di conversione (APSOC: Attenzione → Problema → Soluzione → Obiezioni → CTA con
urgency) è dominio esclusivo di 04-MARKETING Copy Guild.

Il confine è assoluto e non si negozia in base all'urgenza, alla semplicità del pezzo
o alla richiesta esplicita del committente. Se un committente chiede a CF-R4 di scrivere
APSOC, CF-R4-COORD blocca e indirizza la richiesta a 04-MARKETING con il contratto
handoff HC-MK-CF-01.

Sui pezzi ibridi (newsletter con CTA, VSL base):
- CF scrive il corpo; MARKETING scrive il blocco CTA/APSOC.
- La newsletter non viene consegnata con il solo corpo CF: il merge avviene solo dopo che
  il blocco APSOC è stato consegnato da MARKETING con `gate_copy_guild: PASS`.
- Il VSL base da CF-R4 produce la struttura narrativa (hook + problema + soluzione
  descrittiva); l'APSOC per convertire è fuori scope CF.

---

## Principio 2: Il copy di conversione passa da 04-MARKETING — nessuna eccezione (Art.2)

Nessun agente di CF-R4 produce:
- CTA con urgency o scarsità ("ultimi 3 posti", "offerta valida fino a mezzanotte")
- Promesse di risultato garantito ("otterrai X in 30 giorni")
- Struttura APSOC completa

Ogni violazione di questo principio è una violazione del Mandato Empire Art.2 ("prove
non promesse") e della separazione di dominio CF/MARKETING definita in ADR-007.
CF-R4-QA blocca qualsiasi testo che contenga elementi APSOC autonomamente prodotti da CF.

---

## Principio 3: Zero claim non verificabili (Mandato Art.2 — assoluto)

Nessun testo prodotto da CF-R4 contiene:
- Percentuali, cifre o statistiche senza fonte esplicita nel brief o fornita dal committente
- Promesse di risultato garantito o formulazioni del tipo "sempre", "mai", "garantito"
- Testimonial, case study o numeri non verificati dal committente

Se il brief richiede dati che non sono stati forniti, CF-R4-WRITE marca il punto con
`[DM]` (da misurare) e notifica CF-R4-COORD per richiedere i dati al committente.
Non inventa mai i dati per "completare" il testo.

---

## Principio 4: QA blocca, non suggerisce (identico a CF-R3 P4)

CF-R4-QA emette PASS o FAIL. Mai "potrebbe migliorare", mai "quasi conforme".
Un testo che non supera GATE-COPY o GATE-BRAND è in rework, non in produzione.
Il rework ha una specifica strutturata (quale campo, quale criterio, quale riga);
non è "riscrivi il testo".

Il gate interno di CF-R4-QA è un gate preliminare di reparto. Superare GATE-COPY
di CF-R4 non esclude il gate globale di CF-R6: i due gate sono complementari,
non sostitutivi.

---

## Principio 5: Ogni derivato ha il suo gate — nessuna abbreviazione per batch

In WF-REPURPOSING ogni derivato viene trattato come un ordine indipendente.
Non si può "promuovere" un derivato al gate con la logica "il pezzo madre è già
stato approvato, quindi il derivato è implicitamente conforme".

Il tono, la struttura e i claim cambiano nel passaggio da un formato all'altro:
un articolo PASS non garantisce che la caption derivata sia PASS.
CF-R4-QA esegue il gate completo su ogni derivato, anche in batch di 10+.

1 derivato con FAIL non ferma il batch. 3 derivati con FAIL fermano il batch:
segnale sistemico che richiede diagnosi prima di proseguire.

---

## Principio 6: Nessun numero inventato (identico a CF-R3 P7)

I KPI del reparto usano `[DM]` (da misurare) finché non c'è una baseline reale di 4
settimane di produzione con pipeline completa.
CF-R4-LEARN non formula pattern senza ≥5 casi con dati reali.
CF-R4-QA non inventa soglie di qualità: le soglie sono quelle dichiarate nel brand_kit
e nel GATE-COPY del dossier — nessuna soglia locale improvvisata.

---

## Principio 7: Brief mancante o corrotto = blocco immediato

CF-R4-WRITE non avvia mai la redazione senza `brief.json` completo (angle, hook_type,
word_count, struttura_formato, vincoli_brand) e `brand_kit.voice`.
Se un campo obbligatorio del brief è mancante, CF-R4-WRITE blocca e scalona
a CF-R4-COORD, che richiede il dato a CF-R1 o al committente.
Tentare di "completare" un brief incompleto con assunzioni proprie è vietato:
le assunzioni producono contenuto non conforme al brand e al mandato del committente.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — dettaglio tecnico del confine CF/MARKETING e dei gate
- [[ADR-003]] · `company/Memory/decisions/` — principio wrap, non riscrittura (rilevante per skill content-forge)
- [[cf-r4-qa]] · `agenti/cf-r4-qa.md` — implementazione principio 4 (gate blocca, non suggerisce)
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · §3 CF-R4 — definizione confine CF/MARKETING e handoff HC-MK-CF-01
