# yt-seo-publisher - Memory (P10)

## Cosa registra
- Video ID YouTube
- URL pubblico
- Timestamp pubblicazione
- Titolo e descrizione usati
- Errori API

## Quando aggiorna
- Dopo upload riuscito
- Dopo impostazione metadata
- Su errore

## Comando tipico
```bash
python scripts/memory_manager.py --checkpoint "Video pubblicato" --phase 7 --trace "<run-id>"
```