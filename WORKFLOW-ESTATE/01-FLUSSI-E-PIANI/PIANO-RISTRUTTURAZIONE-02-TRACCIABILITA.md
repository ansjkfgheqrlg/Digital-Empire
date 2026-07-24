# PIANO 2 — CICLI CHE LASCIO TRACCIA
> Livello 2 di 7 · **Stato: Proposta** · Owner: Max · Controllore: Claude · Origine: RISTRUTTURAZIONE-01-FONDAMENTA.md

---

## 0. Autocritica di RISTRUTTURAZIONE-01-FONDAMENTA
Il Piano 01 elenca correttamente i percorsi fisici dei sensori spenti, ma pecca di:
1. **Mancanza di operatività:** Non definisce il tracciato logico (schema JSON o TXT) con cui gli agenti devono riempire tali cartelle.
2. **Nessun meccanismo di aggancio:** Non spiega in quale momento dell'esecuzione lo script debba scrivere il record.
3. **Telemetria statica:** Si limita a constatare che `empire inspect` restituisce 0, senza indicare la logica software necessaria per calcolare i parametri reali.

---

## 1. Dimensione Migliorata
**Tracciabilità delle Esecuzioni e Telemetria.**
L'obiettivo è far sì che ogni ciclo di lavoro della Content Factory e dell'outreach generi automaticamente tracciati macchina (log, metriche, performance) ad ogni avvio e chiusura.

---

## 2. Il Contenuto

### A. I Nervi del Sistema: Struttura dei Record Macchina
Ogni script di automazione (es. `carousel-factory`, `yt-fliki-renderer`, `outreach-runtime`) deve implementare le seguenti funzioni di log nativo durante il proprio ciclo di vita:

1. **Inizio Sessione (`/sessions/`):**
   - File: `sessions/run_<timestamp>_<uuid>.json`
   - Contenuto: `{"timestamp": "2026-07-24T14:15:00", "workflow": "WF-S5", "status": "STARTED", "parameters": {}}`
2. **Decisione Presa (`/decisions/`):**
   - File: `decisions/dec_<uuid>.json`
   - Contenuto: `{"timestamp": "...", "title": "DEC-EST-004", "type": "AUTO_BYPASS", "rationale": "competitor Dose Mentale selected as primary source"}`
3. **Misura Tempo e Risorse (`/performances/`):**
   - File: `performances/perf_<uuid>.json`
   - Contenuto: `{"execution_time_seconds": 128.5, "api_calls": {"fliki": 1}, "token_used": 4200}`
4. **Log Errori (`/errors/`):**
   - File: `errors/err_<uuid>.json`
   - Contenuto: `{"timestamp": "...", "severity": "CRITICAL", "message": "Fliki API response empty", "escalation": "STANDBY_TRIGGERED"}`

### B. Funzionamento di `empire inspect`
Il modulo `empire/inspect.py` (attualmente spento) viene attivato con logica di parsing a posteriori:
- Scansiona la cartella `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/performances/`.
- Calcola:
  - `total_runs`: numero totale di file JSON in `sessions/`.
  - `error_rate`: `count(errors/) / count(sessions/) * 100`.
  - `avg_duration`: media dei valori `execution_time_seconds` trovati.
- Aggiorna automaticamente la Dashboard in `06-DASHBOARD-E-METRICHE/KPI-SISTEMA.md`.

---

## 3. Gate di Passaggio 2→3

Il passaggio al Livello 3 è consentito solo se si soddisfano i seguenti criteri oggettivi:
1. **Esecuzione pulita di `empire inspect`:** Il comando non deve restituire "n/d", ma deve mostrare numeri reali (es: `Total Runs: 12, Error Rate: 0.0%`).
2. **Validazione dei tracciati:** Presenza di almeno 1 file JSON valido all'interno di ciascuna delle 4 cartelle chiave (`sessions/`, `performances/`, `decisions/`, `errors/` - quest'ultimo generato da un test di errore indotto).

*Cosa fare in caso di fallimento:* Se un'automazione non riesce a scrivere il proprio tracciato in `/performances/` entro 5 secondi dal termine del processo, l'intero ciclo viene considerato KO. Il runner invia una notifica ad `EmpireDesk` nella barra di Windows con un toast nativo di allerta ed entra in stato di attesa.

---

## 4. Autocritica del Piano 2
- **Cosa ho migliorato:** Ho definito lo schema dati esatto per i record macchina ed ho descritto come riattivare la telemetria di `empire inspect` leggendo tali record.
- **Cosa manca ancora:** Ho risolto la tracciabilità astratta, ma non ho calato questo sistema dentro i singoli 6 stream del piano estate (compiti del Livello 3).
- **SCORE:** **9.2 / 10** (Logico, pulito e additivo).

---
⛓️ Trace P12: `RISTR-PIANO-02#tracciabilita` · fonte: RISTRUTTURAZIONE-01-FONDAMENTA.md · migliorato da: [RISTRUTTURAZIONE-03-WORKFLOWS.md](RISTRUTTURAZIONE-03-WORKFLOWS.md)
