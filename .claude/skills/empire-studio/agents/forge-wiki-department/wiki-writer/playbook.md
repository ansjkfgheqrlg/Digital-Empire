# wiki-writer - Playbook

## Flusso operativo
1. Determinare la sottocartella wiki corretta (sources/concepts/tools/synthesis).
2. Scrivere le note con front-matter (fonte, data, topic) via wiki_writer.py.
3. Aggiornare second-brain-vault/wiki/log.md con la riga INGEST.
4. Evitare sovrascritture: versionare o fondere note esistenti.

## Esempi
- Happy: input valido -> wiki-writer produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
