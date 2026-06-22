---
Type: PRINCIPI
Status: Active
Tags: #principi #ricerca #lead #intelligence #agency #A1
Created: 2026-06-22
Last updated: 2026-06-22
---

# Principi — A1 Ricerca & Market Intelligence

> Principi operativi del reparto. Guidano le decisioni quando le regole non bastano.

---

## P1 — Non si scrappa senza ICP esplicito

Lo scraping cieco produce volume, non valore. Prima di avviare AG-A1-SCRAPE su una nicchia
nuova, deve esistere un profilo ICP dichiarato (da AG-A1-ICP, skill `icp-radar`). L'ICP
definisce cosa cercare, dove, e qual è la soglia di qualifica. Senza ICP, AG-A1-QUAL non ha
un metro contro cui scorare e la run si trasforma in raccolta di rumore.

La prova pratica: ogni run di WF-LEAD-SOURCING su nicchia nuova ha un riferimento a un profilo
ICP in `agency/a1/icp`. Nicchia già coperta → si riusa l'ICP esistente.

---

## P2 — Wrappa l'esistente, non riscrivere (ADR-003)

Lo scraper runtime di Digital Empire è vivo e funziona: `Outreach/Outreach Workflow/`
(scraper multi-fonte, `extractor.py`, `qualifier.py`), `competitor.py`, `cro_audit.py`.
A1 li orchestra, ne legge/scrive lo stato, ne documenta l'uso — non li riscrive.

Quando un agente di A1 sente la tentazione di "rifare lo scraper meglio", la risposta corretta
è: wrappare, parametrizzare, documentare il confine. Una riscrittura del runtime live è una
violazione di ADR-003 e si propone solo via ADR esplicito, mai in silenzio.

---

## P3 — Nessuna metrica inventata; ogni claim cita la fonte

Mandato Art.2: prove non promesse. Un report di nicchia che dice "il mercato cresce del 30%"
senza fonte è peggio di un report che dice "[DM] — dato non disponibile". I claim su ICP,
competitor, trend di mercato citano sempre la fonte (URL, dataset, skill che l'ha prodotto).

AG-A1-QA verifica il campo `fonti[]` su ogni report. Vuoto = FAIL. [DM] è la risposta corretta
quando il dato non esiste ancora — non un numero plausibile inventato per riempire il vuoto.

---

## P4 — Lead scartato = motivo registrato

Un lead sotto soglia non si butta in silenzio. AG-A1-QUAL registra il motivo dello scarto
(fuori ICP, dati incompleti, settore escluso, duplicato) in `agency/reasoning`. Il motivo
alimenta la calibrazione dell'ICP: se il 60% degli scarti è "settore X", forse l'ICP o la
fonte di scraping vanno aggiustati.

La conoscenza si accumula negli scarti tanto quanto nei lead qualificati. Buttare lo scarto
senza motivo butta anche il learning.

---

## P5 — Freschezza è qualità

Un lead con dati di 6 mesi fa è un lead diverso da uno scrappato ieri: l'email può essere
morta, il sito ridisegnato, l'azienda chiusa. La freschezza dei dati è un KPI di primo livello,
non un dettaglio. AG-A1-QA blocca lead con dati oltre soglia di freschezza concordata con A2.

Quando A2 segnala bounce rate alto in outreach → spesso la causa è freschezza, non copy.
A1 risponde con re-run di sourcing prioritario sulla nicchia interessata.

---

## P6 — Il dossier pre-call non ha campi vuoti

Un dossier consegnato ad A8 con "competitor: da compilare" non è un dossier: è un compito
scaricato sul closer prima della call. AG-A1-BRIEF consegna solo dossier completi: profilo lead
quantificato + audit problema + 3 competitor + ICP match + contesto nicchia. Se un campo non
è disponibile, lo dichiara esplicitamente con [DM] e il motivo — non lo lascia vuoto.

Il dossier arriva ≥2h prima della call. Un dossier perfetto consegnato 10 minuti prima è un
dossier mancato: il closer non ha tempo di studiarlo.

---

## Connessioni

- [[REGOLE]] · `regole/REGOLE.md` — le regole non negoziabili (più stringenti dei principi)
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A1`
- [[README]] · `README.md` — missione del reparto
