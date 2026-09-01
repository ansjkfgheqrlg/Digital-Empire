# Failure Modes — memory-wiki-bridge

## FM-01: Pagina wiki gia' esiste per l'argomento
Fix: AGGIORNA (Edit), mai sovrascrivere (Write) — stessa regola di wiki-syncer.

## FM-02: Checkpoint troppo vecchio / volume enorme (backfill storico)
Fix: NON improvvisare un audit gigante senza permesso. Dichiara lo scope coperto in questa run
e lascia il resto come backlog item esplicito (vedi B-019), come gia' fatto il 2026-08-23.

## FM-03: Pagina nuova senza cross-link (orfana nel grafo)
Fix: prima di chiudere, verifica con knowledge-cartographer. Se orfana, trova almeno 1 pagina
pertinente e collega in entrambe le direzioni, o sposta il contenuto dentro una pagina esistente.

## FM-04: Checkpoint minore trattato come pagina wiki nuova (rumore nel grafo)
Fix: fix/iterazioni tecniche senza nuova conoscenza restano SOLO in log.md, mai pagina propria.
