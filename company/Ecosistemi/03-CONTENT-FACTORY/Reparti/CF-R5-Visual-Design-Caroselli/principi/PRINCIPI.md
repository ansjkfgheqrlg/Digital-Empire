---
Type: PRINCIPI
Status: Active
Tags: #principi #CF-R5 #visual #carosello #ADR-003 #gate #brand #carousel-factory
Created: 2026-06-23
Last updated: 2026-06-23
---

# PRINCIPI — CF-R5 Visual & Design / Caroselli

> Principi operativi non negoziabili del reparto. Ogni agente del reparto li rispetta
> sempre, senza eccezioni. In conflitto con un'istruzione puntuale → i principi vincono.

---

## Principio 1: carousel-factory si wrappa, non si riscrive (ADR-003 — assoluto)

Il carousel-factory in `Workfolw crea caroselli à/carousel-factory/` è un asset attivo.
CF-R5 non lo modifica, non lo tocca, non lo estende direttamente.

Ogni chiamata a render.mjs passa per il wrapper `cf-carousel` parametrizzato con
`brand_kit` e `brief` dell'ordine. Il file `render.mjs` originale non viene mai aperto
in scrittura. I template HTML del carousel-factory vengono usati come-sono.

Se un wrapper non funziona → segnalazione a CF-R5-COORD + 07-FORGE; mai andare direttamente
nel file originale per "sistemare velocemente". Un fix diretto nel runtime originale è una
violazione di ADR-003 indipendentemente dall'urgenza.

Ogni workflow e ogni scheda agente che usa carousel-factory dichiara esplicitamente:
`[WRAPPA] carousel-factory — runtime originale non modificato`.

---

## Principio 2: GATE-FORMATO e GATE-BRAND sono sempre obbligatori (Art.4.1)

Nessun deliverable visivo lascia CF-R5 senza aver superato GATE-FORMATO e GATE-BRAND.

- GATE-FORMATO verifica criteri oggettivi e automatizzabili: dimensioni, peso, contrasto,
  safe-area. Non c'è margine discrezionale: 1080×1351 px è FAIL (fuori tolleranza ±2px).
- GATE-BRAND verifica criteri parametrici sul brand_kit dell'ordine: non su un mandato fisso.
  Un colore corretto per un brand può essere sbagliato per un altro.
- I due gate sono sequenziali: GATE-BRAND non parte se GATE-FORMATO è FAIL.
- Entrambi si applicano a ogni ramo (Canva / Puppeteer / AI-image): il fatto che un ramo
  sia "il più veloce" non esonera dal gate.

---

## Principio 3: QA indipendente blocca, non suggerisce

CF-R5-QA è indipendente da ogni ramo di produzione. Chi ha prodotto il PNG non esegue
il proprio gate: la separazione è strutturale.

CF-R5-QA emette PASS o FAIL. Mai "quasi conforme", mai "potrebbe migliorare".
Un deliverable che non supera il gate è in rework, non in delivery parziale.

Il rework ha una specifica strutturata:
- quale gate ha fallito (GATE-FORMATO o GATE-BRAND)
- quale campo specifico (es. `dimensioni`, `peso`, `palette.primary`, `font.display`)
- valore trovato vs valore atteso
- agente che deve correggere

Questo tipo di feedback è tecnico, non creativo. La parte creativa (es. "il carosello
non è abbastanza impattante") non è dominio di CF-R5-QA; se arriva dal committente →
richiesta a CF-R5-CONCEPT per un rework creativo via CF-R5-COORD.

---

## Principio 4: Dry-run prima della generazione a pagamento (Art.4.3)

Per WF-CAROSELLO Ramo A (AI image Gemini/Higgsfield) ogni ordine inizia con il dry-run:
CF-R5-SLIDECOPY + CF-R5-PROMPT producono copy e prompt completi a costo zero.

La generazione delle immagini parte solo dopo che CF-R5-COORD ha approvato il dry-run.
Il Ramo B (Canva) e il Ramo C (render.mjs) hanno costo zero per default: per loro il
dry-run è comunque eseguito per validare il copy prima della generazione.

---

## Principio 5: Il brand_kit è l'unica fonte di verità visiva

Nessun agente di CF-R5 applica colori, font o loghi diversi da quelli dichiarati nel
`brand_kit.visual` dell'ordine. Non ci sono shortcut "lo so a memoria", "è lo stesso
brand dell'ordine precedente", "il cliente ha detto che va bene così".

Se il brand_kit non ha un campo (es. `font.body` assente) → segnalazione a CF-R2-COORD;
mai assumere un default in autonomia. L'assenza di un campo è un errore di upstream da
correggere, non un'opzione da indovinare.

---

## Principio 6: Nessun numero inventato

I KPI del reparto usano `[DM]` (da misurare) finché non c'è una baseline reale di
almeno 4 settimane di produzione.

CF-R5-LEARN non formula pattern senza ≥5 casi reali con dati tracciabili in `trace.jsonl`.
Un pattern con n < 5 è segnalato come "osservazione preliminare", non come pattern.
Nessuna raccomandazione creativa (composizione, hook visivo) viene presentata come
"evidenza" senza la fonte dati.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — dettaglio tecnico ADR-003 e layer engine
- [[ADR-003]] · `company/Memory/decisions/` — fonte primaria principio 1 (wrap, mai riscrittura)
- [[cf-r5-qa]] · `agenti/cf-r5-qa.md` — implementazione principio 3 (gate blocca)
