# concessionari-closer - Memory (P10)

## Cosa registra
- Stato di ogni concessionario
- Deal chiusi / persi
- Revenue generata
- Note di negoziazione
- Timestamp

## Comando tipico
```bash
python scripts/memory_manager.py --checkpoint "Deal chiuso con [nome]" --phase 4 --trace "S1-<concessionario-id>"
```