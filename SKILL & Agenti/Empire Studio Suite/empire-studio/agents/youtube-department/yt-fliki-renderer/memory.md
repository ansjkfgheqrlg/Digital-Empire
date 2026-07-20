# yt-fliki-renderer - Memory (P10)

## Cosa registra
- Job ID Fliki
- Timestamp inizio/fine render
- Status finale
- Errori API
- Path del video generato

## Quando aggiorna
- Dopo invio richiesta
- Dopo ogni polling
- Dopo download completato
- Su errore

## Comando tipico
```bash
python scripts/memory_manager.py --checkpoint "Fliki render completato" --phase 6 --trace "<run-id>"
```