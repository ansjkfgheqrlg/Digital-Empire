---
Type: ENTITY
Status: ✅ PUBBLICABILE — copertina, PDF, copy, scheda ispirazione pronti
Tags: #kdp #libro #publishing #terzo-prodotto
Created: 2026-08-24
Last updated: 2026-08-24
---

# "The Second-Hand Spellbook" — Terzo Libro KDP

## Overview
Terzo libro completato con [[Tool_Pipeline_Libri_KDP]] — 24/24 capitoli, **38.110 parole,
115 pagine reali**, prova cronometrata (CP-7) del piano "un libro in mezz'ora"
(2026-08-19/20). Il piano prometteva 30 minuti; il risultato reale è stato **48 minuti** —
non perché il flusso non funzioni, ma perché il gate di blocco ha bocciato **3 volte di
fila** lo stesso difetto (capitoli scritti troppo corti quando si scrive in fretta:
1.357 → 1.099 → 1.436 parole/capitolo contro un bersaglio di 1.600), ognuna costata
~6 minuti di riallungamento.

## Dettagli
- **Il piano "un libro in mezz'ora" (CP-1..CP-7)**: bersaglio spostato al centro della
  finestra pagine (1.600 parole/capitolo = 120 pagine, non più 1.500 = 112, sotto il
  minimo); nuovo `gate_blocco.py` (0,06 secondi, nessun PDF/OCR) da lanciare dopo ogni
  gruppo di capitoli, che sui dati storici reali del 13 agosto boccia correttamente tutti
  e tre i difetti che negli altri due libri erano emersi solo a fine libro; riassunti a
  formato fisso (3 righe/capitolo + lista "fili aperti"); copertina consegnata subito in
  Fase 3 invece che il giorno dopo; codice sceso da 41 a 27,6 secondi.
- **CP-3 falsificato dal libro stesso**: l'assunzione "320 parole/pagina è accurata entro
  1 pagina" (misurata sui primi due libri) è saltata su questo terzo libro — scarto di 4,3
  pagine (117,3 stimate vs 113 reali, sotto il minimo). Il criterio di rinuncia scritto in
  anticipo nel piano ("se un libro sfora, torno a misurare") si è attivato per davvero:
  corretto generando il PDF una volta prima della consegna finale, non solo a fine libro.
  Il rapporto parole/pagina **dipende dallo stile** (dialoghi brevi impaginano diverso
  dalla prosa continua).
- **Due bug del gate trovati usandolo per davvero**: un `NameError` sulla costante
  dell'esito negativo (mai preso dagli 85 test perché chiamano la funzione interna, non la
  CLI); un consiglio numerico che contraddiceva il nuovo bersaglio CP-1 (rimandava al
  minimo invece che al centro).
- **Magazzino argomenti**: scraper Amazon funziona senza login manuale, verifica automatica
  su 5 candidate (3 passate, 2 scartate con motivo esplicito — una con mediana 3.343
  recensioni, muro competitivo). Restano 2 argomenti liberi in coda: dark academia mystery,
  cozy mystery bakery.

## Come Impatta DE
Terza prova end-to-end della pipeline, e la prima con un piano di velocità sotto misura
reale invece che ipotizzata — il difetto "scrivo corto quando scrivo in fretta" è ora
documentato come costo fisso del flusso veloce, non un incidente, con una correzione
concreta per il prossimo libro (dichiarare 1.750 parole/capitolo per atterrare a 1.600 reali).

## Connessioni
- [[Tool_Pipeline_Libri_KDP]] — il motore/metodo, con il piano "un libro in mezz'ora"
- [[Entity_The_Ninth_Winter_Libro_KDP]] — secondo libro, stessa calibrazione 320 parole/pagina
- [[Entity_The_Quiet_Hours_Libro_KDP]] — primo libro della pipeline

## Status
- First added: 2026-08-24 (backfill wiki storico 06→08/2026, permesso esplicito Max)
- Confidence: Alta — pagine/parole verificate su PDF reale, checkpoint CP-20260819-002,
  CP-20260819-003, CP-20260820-001
