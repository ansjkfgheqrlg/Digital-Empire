---
Type: TOOL
Status: Active
Tags: #tesoreria #finance #adr-020 #cfo-empire #jsonl #cassa
Created: 2026-09-03
Last updated: 2026-09-03
---

# Tesoreria — il reparto che conta i soldi di Digital Empire

## Overview
Quattordicesimo ecosistema di Digital Empire (ADR-020, 2026-09-03), nato dal fatto misurato lo stesso giorno: l'azienda non contava un solo euro — né incassi, né costi effettivi, né una metrica del percorso di vendita. Motore: `scripts/tesoreria.py`, due file JSONL ad accodamento (`company/Memory/tesoreria/entrate.jsonl`, `spese.jsonl`), cinque agenti (`tesoreria-conductor` capo, `-entrate`, `-spese`, `-report`, `-previsione`), skill `tesoreria`. Sotto supervisione di `cfo-empire`.

## Dettagli
**Tre leggi fisse**: (1) previsto non è incassato, mai — i due numeri restano sempre separati; (2) un numero che non esiste si dichiara, non si stima; (3) la storia dei soldi non si riscrive, si annota — correzioni per rettifica accodata, mai per cancellazione (già collaudato con 5 movimenti di prova prima del rilascio).

**Stati di un'entrata**: previsto → fatturato → incassato (o perso). **Motori di business** tracciati per ogni movimento: agency, kdp, corsi, youtube, instagram, saas, formazione-az, altro. **Categorie di spesa**: strumenti, pubblicita, collaboratori, tasse, servizi, hardware, formazione, altro, con flag ricorrente/una-tantum.

Report (`python scripts/tesoreria.py report`) restituisce: cassa (entrato − uscito), in arrivo (fatturato da incassare + previsto non fatturato, separati), margine per motore, spesa per categoria, autonomia in mesi (cassa / spese ricorrenti).

**Regola del passato vuoto** (ADR-020 §4): i mesi prima del 2026-09-03 restano vuoti per scelta esplicita — ricostruirli a memoria produrrebbe numeri non verificabili, peggiori di un vuoto dichiarato. Al 2026-09-03 il registro è ancora a zero movimenti (verificato eseguendo `report` lo stesso giorno).

**Buchi dichiarati apertamente**: nessun tetto di spesa in euro codificato (B-048), nessun connettore verso gestionali/banche reali (inserimento 100% manuale via CLI), nessuna soglia di allerta calcolata in codice (le regole equivalenti — fatture ferme >30gg, previsti fermi >60gg — vivono solo come prosa negli agenti, non come codice in `tesoreria.py`), nessun campo data-scadenza sulle entrate (niente scadenzario crediti/DSO reale).

## Come Impatta DE
È il primo strumento dell'Impero che rende falsificabile qualunque affermazione su incassi/spese/margine per motore — prima di ADR-020 il CFO sorvegliava spese di un'azienda che non aveva mai contato un ricavo, e il magazzino di 25 pezzi finiti mai pubblicati (ADR-016, Ultimo Metro) era passato inosservato proprio per questo.

## Connessioni
- [[Source_Giovanni_Beggiato_CFO_AI_Claude]] — confronto punto per punto in `confronto-tesoreria.md` (run `max17-v15`): stesso principio "il codice calcola, l'AI interpreta" applicato con strumenti più maturi (soglie in codice, scadenzario, cancello anti-invenzione, test di determinismo) che la Tesoreria non ha ancora, con 5 consigli concreti presi dal video.
- [[Tool_Conoscenza_Empire_Agente]] — gerarchia C-suite sotto cui vive `cfo-empire` e quindi la Tesoreria.
- [[Tool_Memory_Wiki_Bridge]] — stesso pattern di ecosistema nato da un ADR con motore-prima-della-documentazione, verificato prima di essere dichiarato "fatto".
