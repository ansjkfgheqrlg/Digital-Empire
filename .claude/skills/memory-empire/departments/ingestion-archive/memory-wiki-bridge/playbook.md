# Playbook — memory-wiki-bridge

## Step 1: Inventario company/Memory
- Elenca tutti `company/Memory/checkpoints/CP-*.md` (ID + data + 1 riga sunto).
- Elenca tutti `company/Memory/decisions/ADR-*.md` (numero + titolo).
- Leggi `company/Memory/STATO-EMPIRE.md` (header con storico compresso + ultima sezione).

## Step 2: Inventario wiki
- Leggi `second-brain-vault/wiki/log.md` per tutte le entry gia' registrate (per data).
- Leggi `second-brain-vault/wiki/index.md` per le pagine gia' esistenti.

## Step 3: Diff
Per ogni checkpoint/ADR: c'e' una entry in log.md con la stessa data/argomento?
- SI -> gia' sincronizzato, skip.
- NO -> gap, va in coda.

## Step 4: Per ogni gap
- Checkpoint minore (fix, iterazione tecnica senza nuova conoscenza) -> SOLO entry log.md.
- Checkpoint con nuova entita'/concetto/progetto/decisione strutturale -> pagina wiki nuova
  o aggiornamento di pagina esistente pertinente (projects/, concepts/, entities/, tools/).
- ADR -> pagina in `second-brain-vault/wiki/concepts/` o sezione decisioni, linkata al progetto
  che tocca.

## Step 5: Cross-link
Ogni pagina nuova deve linkare 2-3 pagine wiki esistenti pertinenti (usa Grep su index.md /
cartelle per trovarle). Aggiungi anche link INVERSO dalle pagine esistenti pertinenti, se ha
senso, cosi' il grafo cresce in entrambe le direzioni.

## Step 6: Aggiorna index.md + log.md
index.md: entry nella sezione giusta. log.md: riga `## [data]` + `- SYNC: ...` con conteggio
pagine create/aggiornate.

## Step 7: Verifica grafo (knowledge-cartographer)
Passa la mano a knowledge-cartographer per controllare che nessuna pagina nuova sia orfana
(0 link in entrata o uscita).

## Step 8: Report finale
`N_checkpoint_totali=X | N_gia_in_wiki=Y | N_colmati_ora=Z | N_pagine_create=A |
N_pagine_aggiornate=B`. Se restano gap non colmati (es. periodo storico troppo ampio da
auditare in una sola run) -> dichiaralo esplicito e proponi backlog item, NON far finta.
