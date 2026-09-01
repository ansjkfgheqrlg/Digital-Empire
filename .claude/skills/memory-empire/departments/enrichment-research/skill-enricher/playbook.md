# Playbook — skill-enricher

## Step 1: Per ogni proposal approvata
Estrai: file, section, content_to_add, insert_mode, source_trace

## Step 2: Backup
```bash
cp <target-file> memory/backups/<skill>-<timestamp>.md
```

## Step 3: Dry-run
```bash
python scripts/enrich_skill.py --target <file> --content <content-temp.md> --source <trace> --dry-run
```

## Step 4: Esegui
```bash
python scripts/enrich_skill.py --target <file> --content <content-temp.md> --source <trace>
```

## Step 5: Verifica
Read del file modificato → controlla che la sezione sia presente e corretta

## Step 6: Log
Scrivi in `memory/enrichments/applied-<timestamp>.json`:
```json
{
  "proposal_id": "PROP-001",
  "target_skill": "copywriting",
  "file_modified": "<path>",
  "backup_at": "memory/backups/copywriting-<ts>.md",
  "chars_added": N,
  "timestamp": "..."
}
```

## Step 7: Notifica change-auditor
Passa l'applied log per verifica finale
