# Projects/Repos Deep-Study Strategy (v1.0)

**Reparto:** Projects/Repos/Workloads · **Tipo:** workflow/repo/progetto · **Wiki:** Reference + Update-Proposal Integrated

## Regola sacra
**SOLA LETTURA. Mai modifica l'originale.** Solo `cat/grep/find/scan_repo.py` + analisi dell'agente.

## Cosa estrarre (nei minimi dettagli)
1. **Architettura**: struttura, moduli, entrypoint, dipendenze.
2. **Decisioni & perche'**: perche' e' stato fatto cosi' (non solo cosa fa).
3. **Come funziona**: il flusso operativo reale.
4. **Quanto bene funziona**: punti di forza, debolezze, anti-pattern.
5. **Pattern/principi**: confronto con master-build (P/PT/AP) e content-forge.

## Regole
- Ogni osservazione/atomo -> trace a `file:riga` (o sezione del report).
- Inferenze/giudizi non scritti nella fonte -> marcati `➕`.
- Repo grandi -> prioritizza entrypoint/README/config; dichiara lo scope.

## Output
`deep-analysis.md` / `repo-analysis.md` (architettura+decisioni+valutazione) + `atoms.json` (tracciati) -> Forge -> wiki.
`cross-update-proposals.md`: pattern del progetto applicabili ai workflow dell'utente (inclusi i reparti di Empire Studio).

## Decision tree
- E' un report/descrizione -> workflow-deep-analyzer.
- E' una repo/cartella -> repo-deep-study (scan_repo.py read-only) -> analisi.
- Sempre: project-knowledge-extractor (atomi) -> workload-comparator (update).
