---
name: sync-wiki-totale
description: Sincronizza TUTTO il lavoro nuovo (checkpoint, decisioni ADR, STATO-EMPIRE, contenuto ingerito da Memory Empire) dentro la wiki di Digital Empire, aggiorna il grafo (cross-link, index.md, log.md) e riporta un conteggio MATCH/GAP preciso. Usa quando l'utente scrive /sync-wiki-totale o dice "sincronizza la wiki", "metti tutto nella wiki", "il grafo non e' aggiornato", "manca roba nella wiki".
metadata:
  version: 1.0.0
---

# Sync Wiki Totale

Un comando, zero domande: prende TUTTO quello che e' nuovo (lavoro interno in
`company/Memory/` + contenuto ingerito da Memory Empire) e lo mette nella wiki, con grafo
aggiornato per benino. Chiude il gap descritto in `company/Memory/BACKLOG.md` (B-019) e in
`second-brain-vault/wiki/log.md` (entry 2026-08-23).

## Perche' esiste
Ci sono DUE sistemi di memoria in Digital Empire:
1. `company/Memory/` (REGOLA ZERO, CLAUDE.md) — checkpoint, ADR, STATO-EMPIRE. Sempre rispettato.
2. `second-brain-vault/wiki/` (REGOLA FONDAMENTALE) — solo output di Empire Studio (video/tiktok/
   web ingeriti). Il lavoro interno non ci finiva MAI da solo → grafo che non cresce.

Questo comando e' il ponte esplicito tra i due, on-demand.

## Esecuzione (nessuna domanda, esegui diretto)

1. **Attiva memory-empire** (`~/.claude/skills/memory-empire/`), reparto `ingestion-archive`,
   **Pipeline B** (vedi `departments/ingestion-archive/department-lead/department-lead.md`):
   - `memory-wiki-bridge` — diff `company/Memory/checkpoints/*.md` + `decisions/ADR-*.md` +
     `STATO-EMPIRE.md` contro `second-brain-vault/wiki/log.md` + `index.md`. Per ogni gap:
     crea/aggiorna pagina wiki (template standard, frontmatter completo) o solo entry log.md se
     e' un fix minore. Segui `memory-wiki-bridge/playbook.md` passo-passo.
   - `knowledge-cartographer` — verifica che ogni pagina nuova abbia almeno 2-3 cross-link
     (nessuna pagina orfana nel grafo). Se orfana, collega o dichiara perche' non serve.
2. **Attiva anche wiki-syncer** sul contenuto Memory Empire (`knowledge/*/`) non ancora
   verificato in wiki, stesso principio: gap → colma.
3. **Aggiorna** `second-brain-vault/wiki/index.md` e `log.md` con le entry mancanti.
4. **Report finale all'utente**, formato secco:
   ```
   Checkpoint totali: X | gia' in wiki: Y | colmati ora: Z
   ADR totali: X | gia' in wiki: Y | colmati ora: Z
   Knowledge Memory Empire: X | gia' in wiki: Y | colmati ora: Z
   Pagine create: N | Pagine aggiornate: M | Pagine orfane trovate/risolte: K
   GAP residuo (se c'e'): [scope preciso, es. "pre-luglio 2026, backlog B-019"] — richiede
   via libera esplicita per l'audit storico completo, NON eseguirlo di default.
   ```

## Regola non negoziabile
Buco storico grande (mesi) → NON improvvisare un mega-audit silenzioso. Dichiaralo, chiedi
conferma. Sync del periodo recente/corrente invece si esegue sempre diretto, senza chiedere.

## Dopo l'esecuzione (REGOLA ZERO)
Questo comando stesso e' un task: a fine run scrivi checkpoint in
`company/Memory/checkpoints/` e aggiorna `STATO-EMPIRE.md` con cosa e' stato sincronizzato.
