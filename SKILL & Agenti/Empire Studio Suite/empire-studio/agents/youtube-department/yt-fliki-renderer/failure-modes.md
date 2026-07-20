# yt-fliki-renderer - Failure Modes

## Errori comuni e recovery

1. **Rate limit API Fliki**
   - Azione: Attendere 10 minuti + exponential backoff
   - Registra in memory/errors

2. **Job stuck in "processing"**
   - Azione: Timeout dopo 5 minuti → cancella job e riprova

3. **Errore di autenticazione**
   - Azione: Verificare chiave in .env

4. **Video generato corrotto**
   - Azione: Rigenera con parametri diversi

**Regola:** Mai superare i limiti API. Sempre salvare job_id nel Memory.