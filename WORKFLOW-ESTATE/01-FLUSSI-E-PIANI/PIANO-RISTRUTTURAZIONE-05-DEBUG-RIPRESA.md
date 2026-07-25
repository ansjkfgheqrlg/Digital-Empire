# PIANO 5 — SESSIONI, DEBUG E RIPRESA
> Livello 5 di 7 · **Stato: Proposta** · Owner: Max · Controllore: Claude · Origine: RISTRUTTURAZIONE-04-GERARCHIA.md

---

## 0. Autocritica di RISTRUTTURAZIONE-04-GERARCHIA
Il Piano 04 definisce la gerarchia ed il flusso di escalation degli errori, ma:
1. **Perdita di stato al crash:** Non prevede un meccanismo per salvare lo stato di esecuzione corrente in caso di riavvio improvviso (es. spegnimento del server).
2. **Nessun meccanismo di ripresa:** Obbliga a ripartire dall'inizio (Stage 0) ad ogni nuova esecuzione, sprecando API Token e tempo.
3. **Debug manuale:** Manca di una cartella di checkpoint strutturata che permetta a un agente di leggere lo storico recente della sessione.

---

## 1. Dimensione Migliorata
**Resilienza di Stato e Ripristino Sessuale (State Persistence).**
L'obiettivo è garantire che ogni workflow possa essere interrotto e riavviato dallo stesso esatto punto di esecuzione in modo sicuro e trasparente.

---

## 2. Il Contenuto

### A. I Checkpoint di Sessione
Ogni workflow scrive lo stato dei suoi Stage all'interno della cartella `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/checkpoints/`.
- File: `checkpoints/state_<workflow_id>_session.json`
- Struttura:
```json
{
  "session_uuid": "...",
  "workflow_id": "WF-S5",
  "timestamp": "2026-07-24T14:20:00",
  "last_successful_stage": 4,
  "stages_completed": {
    "0": "SUCCESS",
    "1": "SUCCESS",
    "2": "SUCCESS",
    "3": "SUCCESS",
    "4": "SUCCESS",
    "5": "NOT_STARTED"
  },
  "context_data": {
    "competitor_video_id": "youtube_abc123",
    "extracted_script_raw": "...",
    "refined_script_it": "..."
  }
}
```

### B. Ciclo di Ripresa Automatizzata (Resume)
All'avvio di ogni workflow, il `CEO Agent` esegue i seguenti passi:
1. **Ricerca Stato:** Cerca nella cartella `checkpoints/` se esiste un file attivo per il `<workflow_id>`.
2. **Scadenza (TTL):** Se il checkpoint è più vecchio di 24 ore, lo ignora e riparte da zero.
3. **Caricamento Contesto:** Se valido, ripristina la memoria di sessione (`context_data`) e avvia l'esecuzione a partire dallo stage contrassegnato come `NOT_STARTED` o `FAILED`.
4. **Verifica Integrità:** Controlla che gli input dello stage da riavviare siano fisicamente presenti su disco (es. lo script IT generato al punto precedente).

---

## 3. Gate di Passaggio 5→6

Il passaggio al Livello 6 è consentito solo se si soddisfano i seguenti criteri oggettivi:
1. **Test di Resume Eseguito:** Interrompendo manualmente un'automazione (uccidendo il processo a metà) e rilanciandola, lo script deve saltare gli stage già completati (evidenza di "Stage già completato, ripristino contesto" nel log di sessione).
2. **Presenza dei Checkpoint:** Generazione corretta del file `state_<workflow_id>_session.json` ad ogni completamento di stage.

*Cosa fare in caso di fallimento:* Se al restart il file di checkpoint risulta corrotto, il sistema lo sposta in `errors/` nominando il file `corrupted_checkpoint_<uuid>.json` e riparte da zero per sicurezza.

---

## 4. Autocritica del Piano 5
- **Cosa ho migliorato:** Ho introdotto la persistenza di stato a caldo, salvando tempo e costi in caso di crash ambientali del sistema.
- **Cosa manca ancora:** Abbiamo reso il sistema resiliente, ma manca la definizione formale di dove si fermi l'automazione e dove debba intervenire Max (compito del Livello 6).
- **SCORE:** **9.4 / 10** (Alta resilienza operativa).

---
⛓️ Trace P12: `RISTR-PIANO-05#debug-ripresa` · fonte: RISTRUTTURAZIONE-04-GERARCHIA.md · migliorato da: [RISTRUTTURAZIONE-06-AUTONOMIA.md](RISTRUTTURAZIONE-06-AUTONOMIA.md)
