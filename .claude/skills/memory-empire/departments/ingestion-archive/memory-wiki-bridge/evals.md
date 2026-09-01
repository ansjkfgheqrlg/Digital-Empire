# Evals — memory-wiki-bridge

## PASS se:
- [ ] Ogni checkpoint/ADR nello scope della run e' stato classificato (sync gia' fatto / gap
      colmato / backlog dichiarato) — nessuno ignorato in silenzio.
- [ ] Ogni pagina nuova ha >=2 cross-link e frontmatter completo.
- [ ] index.md e log.md aggiornati.
- [ ] Report finale con conteggio MATCH/GAP esplicito.

## FAIL se:
- [ ] Un checkpoint con contenuto rilevante resta senza traccia in wiki e senza dichiarazione.
- [ ] Pagina wiki creata orfana (0 link).
- [ ] Overwrite di una pagina esistente invece di update.
