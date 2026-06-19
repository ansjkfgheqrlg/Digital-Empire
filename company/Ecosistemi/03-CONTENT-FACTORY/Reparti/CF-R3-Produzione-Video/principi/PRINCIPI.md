---
Type: PRINCIPI
Status: Active
Tags: #principi #CF-R3 #video #budget #dry-run #ADR-003 #wrap
Created: 2026-06-19
Last updated: 2026-06-19
---

# PRINCIPI — CF-R3 Produzione Video

> Principi operativi non negoziabili del reparto. Ogni agente del reparto li rispetta
> sempre, senza eccezioni. In conflitto con un'istruzione puntuale → i principi vincono.

---

## Principio 1: Dry-run prima di ogni spesa engine (Art.4.3 — assoluto)

Nessun engine a crediti parte senza che CF-R3-QUEUE abbia prodotto un `*-intent.json`
con la stima completa e CF-SENT-COST abbia risposto APPROVATO.

Il dry-run non è un'opzione: è il passo 0 di ogni workflow che genera spesa.
Il bypass del dry-run non è mai giustificato, nemmeno per ordini urgenti.
Un ordine urgente con dry-run approvato è prioritario; un ordine senza dry-run è bloccato.

---

## Principio 2: Mai render senza stima approvata

La stima (`estimate()`) deve essere chiamata su ogni engine prima di `generate()`.
Se `estimate()` non risponde → usa la stima tabellare + flag `stima_da_tabella: true`.
Se la stima supera il budget → BLOCCO automatico prima ancora di consultare CF-SENT-COST.
Mai avviare render parziali per "recuperare qualcosa" dopo un BLOCCO.

---

## Principio 3: Gli asset attivi si wrappano, non si riscrivono (ADR-003)

`hf-studio/` e `heygen-studio/` sono asset attivi di CF Exponium.
CF-R3 non li modifica, non li tocca, non li estende direttamente.
Ogni chiamata passa per i wrapper parametrizzati (`higgsfield-suite`, `heygen-generate`)
che sostituiscono i parametri Exponium con i parametri del brand_kit dell'ordine.
Se un wrapper non funziona → segnalazione a CF-R3-COORD + 07-FORGE; mai andare direttamente
nell'originale per "sistemare velocemente".

---

## Principio 4: QA blocca, non suggerisce

CF-R3-QA emette PASS o FAIL. Mai "potrebbe migliorare", mai "quasi conforme".
Un video che non supera GATE-FORMATO o GATE-BRAND è in rework, non in produzione.
Il rework ha una specifica strutturata (quale gate, quale criterio, quale agente deve
correggere); non è "rifai il video".

---

## Principio 5: 1 fallito non ferma il batch; 3 falliti fermano il batch

In WF-BATCH-VIDEO la resilienza è progettata: i job sono indipendenti.
Un engine che fallisce su un job non contamina gli altri.
Ma 3 fallimenti sono un segnale sistemico (engine down? parametri sbagliati? budget esaurito?)
e richiedono intervento umano via CF-R3-COORD → L1-PROD.
Non aspettare la fine del batch per escalare: l'escalation avviene al terzo fallimento.

---

## Principio 6: Soul-id è per brand, non per video

Un brand ha esattamente un soul-id attivo in `cf/souls`.
Ogni video UGC di quel brand usa lo stesso soul-id per garantire coerenza visiva.
Il soul-id non si cambia per un singolo video; se il committente vuole un look diverso →
nuovo brand_kit slug con nuovo soul-id (CF-R2 gestisce).

---

## Principio 7: Nessun numero inventato

I KPI del reparto usano `[DM]` (da misurare) finché non c'è una baseline reale.
CF-R3-LEARN non formula pattern senza ≥5 casi con dati reali.
CF-R3-QUEUE non inventa stime: se `estimate()` non risponde usa la tabella storica
con flag esplicito. Mai presentare una stima speculativa come se fosse precisa.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — dettaglio tecnico dei principi 1-2 (dry-run e budget guard)
- [[ADR-003]] · `company/Memory/decisions/` — fonte primaria principio 3 (wrap, non riscrittura)
- [[cf-r3-qa]] · `agenti/cf-r3-qa.md` — implementazione principio 4 (gate blocca, non suggerisce)
