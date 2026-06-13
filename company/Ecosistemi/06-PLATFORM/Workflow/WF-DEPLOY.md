# WF-DEPLOY — Deploy + Logs + Rollback + Smoke

> **Procedura ufficiale di deploy PLATFORM.** Eseguito da plt-deploy-op come gate G-DEPLOY. Comprende: pre-flight check, deploy Vercel, smoke test, log watch, rollback se necessario, evento costo.

## Trigger
- G-SEC e G-QA verdi nel shared_state di build (trigger automatico da plt-cc-master)
- Re-deploy post-fix di bug in produzione (trigger manuale da plt-director)
- Rollback richiesto da OPERATIONS o Board (trigger emergenza)

## Input
```json
{
  "repo_path": "path repo da deployare",
  "progetto_vercel": "nome progetto su Vercel",
  "environment": "production | preview | staging",
  "shared_state": {"g_sec": "verde", "g_qa": "verde"},
  "smoke_test_pages": ["/, /about, /contact, /prodotto, /checkout"],
  "commessa_id": "ID commessa per evento costo OPERATIONS",
  "rollback_version": "deployment_id versione precedente (per rollback emergenza)"
}
```

## Pipeline (Passi)

### Step 1 — PRE-FLIGHT CHECK (2 min)
```
plt-deploy-op:
  → verifica shared_state: g_sec == "verde" AND g_qa == "verde"
  → SE no → BLOCCO IMMEDIATO → notifica plt-cc-master → non procede
  → verifica env vars Vercel configurate (NEXT_PUBLIC_*, DATABASE_URL, etc.)
  → verifica branch: è il branch corretto (main o production)?
  → output: pre-flight VERDE / ROSSO con motivo blocco
```

### Step 2 — DEPLOY VERCEL (3-5 min)
```
plt-deploy-op: esegue vercel:deploy
  → monitora build log in real-time
  → se errore build:
    → analizza log → identifica tipo errore (TypeScript, import mancante, env var)
    → notifica plt-site-builder con path:error
    → attende fix → retry (max 3 tentativi)
    → se 3° tentativo fallisce → escalation plt-director
  → se build OK → ottiene URL deployment preview
```

### Step 3 — SMOKE TEST (3 min)
```
plt-deploy-op: GET su ogni URL in smoke_test_pages
  → verifica HTTP status: 200 (atteso) / 3xx (redirect ok se previsto) / 4xx-5xx (FAIL)
  → verifica: no error boundary React visibile (testo "Something went wrong")
  → verifica: CTA principale presente e cliccabile
  → verifica: form (se presente) → test submit con dati fake → no 500

SE ≥1 pagina critica fallisce:
  → ROLLBACK immediato (Step 4A)
SE solo pagine secondarie falliscono:
  → valutazione plt-cc-master: rollback o fix-forward?
```

### Step 4A — ROLLBACK (se necessario, 2 min)
```
plt-deploy-op:
  → identifica deployment_id versione precedente (da vercel:logs)
  → esegue rollback Vercel al deployment_id precedente
  → verifica che il rollback sia live con smoke test rapido (homepage + 1 pagina chiave)
  → notifica plt-cc-master: URL rollback, motivo, deployment_id fallito
  → plt-cc-master → escalation plt-site-builder per fix
  → workflow ricomincia da Step 2 dopo il fix
```

### Step 4B — LOG WATCH (10 min)
```
plt-deploy-op: vercel:logs per 10 minuti post-deploy
  → conta errori 5xx: soglia = 0 nei primi 10 min
  → se >0 errori 5xx in 10 min → ROLLBACK (Step 4A)
  → se 0 errori → G-DEPLOY VERDE

SE progetto SaaS con traffico: monitoring esteso a 30 min
```

### Step 5 — CHIUSURA (2 min)
```
plt-deploy-op:
  → emette evento costo per OPERATIONS:
    { "commessa_id": "...", "tipo": "deploy", "durata_min": N, "esito": "success",
      "url_produzione": "https://..." }
  → notifica plt-cc-master: G-DEPLOY VERDE, URL produzione
  → plt-custodian: aggiornamento registry (deployment_id, data, url, stato)
```

## Gate G-DEPLOY — Checklist
```
✓ Pre-flight: G-SEC verde + G-QA verde
✓ Build Vercel: nessun errore di compilazione
✓ Smoke test: HTTP 200 su tutte le pagine chiave
✓ Log watch: 0 errori 5xx in 10+ minuti
✓ Evento costo emesso per OPERATIONS
✓ Registry aggiornato da plt-custodian
→ G-DEPLOY VERDE: URL produzione consegnato a plt-cc-master
```

## Output
- URL sito in produzione (Vercel)
- Report deploy `{durata, deployment_id, smoke_test_result, log_watch_result}`
- Evento costo per OPERATIONS
- Registry aggiornato

## Owner Agente
`plt-deploy-op`

## Skill Usate
`vercel:deploy` · `vercel:logs` · `vercel:setup` (solo se primo deploy su progetto nuovo)
