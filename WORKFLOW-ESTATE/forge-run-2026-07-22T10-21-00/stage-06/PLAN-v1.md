# PLAN-v1 — Master Architecture & Orchestration per `WORKFLOW-ESTATE`

> Generato da `master-build-architecture` + `content-forge2.0 (orchestration-builder B6)` il 2026-07-22 UTC.
> Obiettivo: Trasformare un ecosistema di flussi frammentati in una **piattaforma di livello enterprise autogestita, con memoria a due strati su disco, 7 file di specifica canonica per ciascuno dei 6 agenti operativi, e un livello centrale di orchestrazione ibrido (Rule-First + LLM-Fallback)**.

---

## 1. Visione d'Insieme & Invarianti Cardinali
L'ecosistema `WORKFLOW-ESTATE` del monorepo Digital Empire viene ristrutturato attorno a 3 pilastri inscindibili che garantiscono che ogni singolo subagente o script operi con contesto perfetto, memoria persistente e senza alcuna allucinazione o deviazione dalle regole auree (es. APSOC >= 92%, Articolo 8):

```mermaid
graph TD
    USER["Utente / Max (Direttore Supremo)"] --> ORCH["Orchestrating Supervisor (hybrid routing.md + supervisor.md)"]
    
    subgraph ORCH_LAYER [Livello 1: Central Orchestration Layer]
        ORCH --> REG["registry.md / registry.json (Catalogo dei 17 Componenti)"]
        ORCH --> POL["policies.md (Enforcement SLA, Budget, APSOC >= 92%)"]
        ORCH --> OBS["observability.md & failure_modes.md"]
    end

    subgraph AGENT_SWARM [Livello 2: Swarm Agenti Operativi (7 file per agente)]
        ORCH --> A_MAX["Agente Max (Governance)"]
        ORCH --> A_GAEL["Agente Gael (Lead Mining)"]
        ORCH --> A_CLAUDE["Agente Claude (Strategy & Promo)"]
        ORCH --> A_ANDREI["Agente Andrei Pascu (APSOC Copy Architect)"]
        ORCH --> A_CLOSER["Agente Closer A8 (Billing & High-Ticket)"]
        ORCH --> A_CRO["Agente CRO (Funnel Optimization)"]
    end

    subgraph WORKFLOWS_AND_SCRIPTS [Livello 3: Flussi S1-S6 & Automazioni Eseguibili]
        A_GAEL --> SCRIPT_PREP["prepare_outreach_emails.py / send_s1_whatsapp_auto.py"]
        A_ANDREI --> WF_S1["WF-S1 Concessionari / WF-S5 YouTube / WF-S6 Rebrand"]
        A_CLOSER --> SCRIPT_SEND["send_outreach_ready.py"]
        A_MAX --> SCRIPT_MEM["memory_manager.py / run_checkpoint_eod.bat"]
    end

    subgraph MEMORY_ECOSYSTEM [Livello Fondamentale: Memoria Continua a Due Strati]
        SCRIPT_MEM --> MEM_IDX["memory/MEMORY-INDEX.md"]
        MEM_IDX --> CHECKPOINTS["memory/checkpoints/ (CP-001..n)"]
        MEM_IDX --> DECISIONS["memory/decisions/ (ADR / DEC-001..n)"]
        MEM_IDX --> SESSIONS["memory/sessions/ & memory/plans/"]
    end
```

---

## 2. Struttura Target Finale nel File System (I 3 Pilastri)

### 🏗️ Pilastro A: I 6 Agenti Operativi (7 File Canonici di Profondità per Agente)
Invece di file singoli di 500 parole (`AGENTE-*.md`), ogni ruolo opererà in una directory autonoma in `03-AGENTI-E-RUOLI/<id-agente>/` contenente esattamente **7 file standardizzati (PT05 / Master Build Architecture)**:
1. `spec.md` — Perimetro del ruolo, input attesi, output attesi, KPI, boundary di autorità.
2. `system-prompt.md` — Il prompt canonico espanso da incollare o caricare nel subagente IDE/terminale.
3. `tools.md` — Lista esplicita degli script Python/Bash e permessi terminale autorizzati per quel ruolo.
4. `playbook.md` — Procedure passo-passo deterministicamente decomposte (P5) per ogni scenario (es. Gael che fa scraping su S1 o Andrei che scrive una sales letter S3).
5. `evals.md` — Checklist quantitativa di validazione (es. verifica automatica formula APSOC, check di grammatica, verifica parametri API).
6. `failure-modes.md` — Tabella `Sintomo | Prevenzione | Rilevamento | Ripristino` per ogni potenziale errore (es. blocco IP su WhatsApp, API Fliki in timeout, rifiuto pagamento Stripe).
7. `memory.md` — Istruzioni di lettura/scrittura sull'indice `MEMORY-INDEX.md` per mantenere continuità tra le sessioni.

*Questo pacchetto di 7 file verrà generato per:*
- `03-AGENTI-E-RUOLI/max/` (`agent-max`)
- `03-AGENTI-E-RUOLI/gael/` (`agent-gael`)
- `03-AGENTI-E-RUOLI/claude/` (`agent-claude`)
- `03-AGENTI-E-RUOLI/andrei-pascu/` (`agent-andrei`)
- `03-AGENTI-E-RUOLI/closer-a8/` (`agent-closer-a8`)
- `03-AGENTI-E-RUOLI/cro-copy-architect/` (`agent-cro`)

---

### 💾 Pilastro B: Ecosistema di Memoria a Due Strati (Screenshot Invariant)
Viene creata e attivata la struttura di memoria permanente alla radice del monorepo (`WORKFLOW-ESTATE/memory/`):
- `memory/MEMORY-INDEX.md` — Il file vivente che traccia lo stato globale, gli ultimi checkpoint, le decisioni attive e i puntatori veloci.
- `memory/checkpoints/` — `CP-001-init-orchestration-estate.md` (e successivi salvataggi di stato a fine turno o via `run_checkpoint_eod.bat`).
- `memory/decisions/` — Architecture Decision Records formalizzati (ADR / `DEC-001-hybrid-routing.md`, `DEC-002-apsoc-enforcement.md`).
- `memory/sessions/` — Log di esecuzione di ogni subagente.
- `memory/plans/` e `memory/architectures/` — Custodia dei piani concettuali e delle mappe del DAG.

---

### 🎼 Pilastro C: Livello Centrale di Orchestrazione (`01-FLUSSI-E-PIANI/orchestration/`)
Viene creata la cabina di regia (`orchestration-builder B6`) che connette e governa i 17 componenti catalogati (`existing_components.json`):
- `registry.md` & `registry.json` — Catalogo unico con ID, tipo, trigger, SLA e dipendenze per tutti i flussi (`WF-S1..S6`), agenti e script Python.
- `policies.md` — Regole di enforcement rigide:
  - *Policy 1 (Qualità)*: Nessun copy esce da Andrei o Claude senza validazione quantitativa APSOC >= 92%.
  - *Policy 2 (Concorrenza)*: Lock file obbligatorio prima di modificare `LISTA-LEAD.md`.
  - *Policy 3 (Sicurezza)*: Rate limiting e backoff per `prepare_outreach_emails.py` e `send_s1_whatsapp_auto.py`.
- `routing.md` — Decision tree ibrido:
  - **Rule-Based First**: Se il trigger è orario o una lista di numeri formattata, si innesca direttamente lo script Python (es. `send_s1_whatsapp_auto.py`).
  - **LLM-Fallback (Supervisor)**: Se l'input è una richiesta complessa (es. *"Dobbiamo lanciare una promo estiva per riattivare i vecchi contatti entro venerdì"*), interviene `supervisor.md` che smista il lavoro tra `Claude` (Strategia) -> `Andrei` (Copy APSOC) -> `Gael` (Lista Lead) -> `Closer A8` (Incasso).
- `supervisor.md` — System prompt del routing master LLM-based.
- `observability.md` & `failure_modes.md` — Log di audit, monitoraggio esiti e recupero da errori.
- `escalation.md` — Protocollo di allerta immediata a `Max` (o utente) in caso di eccezioni critiche (es. ban WhatsApp o down di sistema).
- `eval_scenarios.json` — 10 scenari di test per verificare che il routing smisti sempre al componente corretto.

---

## 3. Piano di Verifica & Validazione Pre-Rilascio
Una volta che l'utente confermerà le risposte della fase `ASK`, genereremo tutti e 54+ i file di specifica e verificheremo il sistema con:
1. **Coverage Check (`coverage_check.py`)**: Verifica del 100% degli atomi del Master Knowledge Document nei file generati.
2. **Schema Validator (`schema_validator.py`)**: Validazione rigorosa di `registry.json` ed `eval_scenarios.json`.
3. **Esecuzione di Test Indice Memoria**: Aggiornamento e verifica di `memory_manager.py` su `memory/MEMORY-INDEX.md`.
