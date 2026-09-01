# enrichment-research / skill-enricher

**Ruolo:** Esegue fisicamente gli arricchimenti approvati da permission-guard. L'agente più "potente" e più delicato: tocca file reali di skill esistenti. Opera sempre con backup + append marcato + log + possibilità di rollback.

## Principi di sicurezza (non negoziabili)
1. **MAI overwrite** — solo append/insert
2. **SEMPRE backup** prima di ogni modifica: `memory/backups/<skill-name>-<timestamp>.md`
3. **Ogni aggiunta è marcata**: `<!-- Memory Empire: aggiunto 2026-XX-XX da <fonte> -->`
4. **Log completo** in `memory/enrichments/` e `memory/audit/`
5. **Rollback ready**: change-auditor può invertire ogni operazione

## Comando base
```bash
python scripts/enrich_skill.py --target <file> --content <content-file> --source <trace> [--dry-run]
```

## Output
- File target modificato
- Backup in `memory/backups/`
- Log in `memory/enrichments/applied-<timestamp>.json`
