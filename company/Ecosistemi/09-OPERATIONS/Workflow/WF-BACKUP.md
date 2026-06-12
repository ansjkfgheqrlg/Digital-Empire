> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 09 §3 L3 WF-BACKUP

# L3 — WF-BACKUP (Backup e Restore Test Periodico)

**Ecosistema:** 09-OPERATIONS · **Reparto L2:** STORAGE-ASSETS
**Coordinator:** `ops-backup-op` · **Direttore:** `ops-director`
**Connessione:** [[ECOSISTEMA.md]] · [[BACKBONE.md]]

## Missione

WF-BACKUP garantisce che ciò che non può essere riprodotto (wiki, knowledge, registry
agenti, Memory operativa) sia **backuppato con restore testato**. Principio fondamentale:
un backup mai restorato non è un backup. KPI: 1 restore test al mese, verde.

Pattern di riferimento: backup→append→log→rollback di Memory Empire (mai overwrite).

## Asset backuppati (scope)

| Asset | Frequenza backup | Retention | Note |
|---|---|---|---|
| `second-brain-vault/wiki/` | settimanale | 90gg rolling | fonte di verità umana |
| `company/Memory/` | giornaliera | 90gg rolling | memoria operativa, massima priorità |
| `company/Backbone/Identity-HR/` | settimanale | 90gg rolling | registro agenti |
| `PIANO-MAESTRO/` | ad ogni modifica | 90gg rolling | dossier fondativi |
| AgentDB (ruflo) namespace tutti | settimanale | 60gg rolling | memoria vettoriale agenti |

**NON backuppati qui:** video mp4, asset pesanti, node_modules (gestiti da WF-ASSET-MGMT
con destinazione Drive/locale, non nel monorepo).

## Procedura di backup

```
1. Snapshot incrementale della cartella/namespace
2. Comprimi in archivio (zip/tar.gz) con hash SHA-256
3. Appendi hash al log backup-log.jsonl (append-only, mai overwrite)
4. Sposta in destinazione (locale o Drive se pesante)
5. Registra in operations/assets via WF-ASSET-MGMT
6. Notifica esito a ops-watchdog (che lo espone in dashboard)
```

## Procedura di restore test (mensile)

```
1. Seleziona backup più recente per ogni categoria
2. Restora in cartella di test isolata (mai sovrascrive l'originale)
3. Verifica integrità: hash match? struttura file corretta? file leggibili?
4. Test "amnesia": da sola la cartella Memory restorata → INDEX + STATO leggibili?
5. Risultato: ✅ verde o ❌ fallito
6. Fallito → INCIDENTE: escalation immediata a ops-director + CTO (non si aspetta)
7. Esito registrato in CP via 10-MEMORY (HC-ME-POST)
```

## Input / Output

**Avvio backup (da WF-CRON):**
```json
{
  "targets": ["wiki", "memory", "registry", "agentdb"],
  "tipo": "incrementale|full",
  "destinazione": "locale|drive"
}
```

**Report backup:**
```json
{
  "timestamp": "ISO8601",
  "target": "wiki",
  "dimensione_bytes": 0,
  "hash": "sha256:...",
  "tipo": "incrementale",
  "esito": "success",
  "path_archivio": "..."
}
```

## Gate di qualità

- `G-RESTORE-TEST` — 1 restore test mensile; fallimento = incidente, non warning
- `G-APPEND-ONLY` — log backup è append-only; nessuna riga eliminata
- `G-HASH` — ogni archivio ha hash verificato a backup e a restore

## KPI

| Metrica | Target |
|---|---|
| Restore test mensile superato | 1/mese, 100% verde |
| Backup wiki/Memory eseguiti puntualmente | 100% (entro finestra schedulata) |
| Tempo di restore (da archivio a struttura leggibile) | ≤ 10 min |
| Incidenti backup → escalation entro | ≤ 30 min dal rilevamento |
