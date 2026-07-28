# ADR-010 — Fusione Ruflo Backbone + motore APEX-7-CORE (sistema nervoso empire-wide)

- **Data:** 2026-07-28
- **Stato:** ATTIVO
- **Decisori:** Max (owner) · Claude (esecutore/controllore tecnico)

## Contesto

Max ha chiesto se APEX-7 sia già un layer sempre-attivo su tutto Digital Empire. Verifica: no —
`YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py` è scoped solo a
YouTube, gira on-demand, nessun cron/daemon.

L'indagine (2 agenti Explore paralleli) ha trovato una frammentazione preesistente non
documentata prima d'ora:

1. **4 implementazioni APEX-7-shaped divergenti**: YouTube (critic fisso — `execute_critic`
   ritorna sempre lo stesso punteggio, agenti hardcoded in `agents.py`), skill generica
   `.agents/skills/apex-7/`, ecosistema canonico `11-APEX-7-CORE` (promosso da ADR-009 —
   SQLite, `BaseAgent` astratto, EventBus, già usato per skill-forge/carosello/outreach), e una
   reimplementazione indipendente in `12-STREAM-S7-BOT` (bot Solana).
2. **Il backbone Ruflo** (`PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md`) — Bus/Brain/Governance/
   Identity-HR/Coordination Fabric — era già pensato come il vero sistema nervoso trasversale
   ("Ruflo coordina, Claude Code esegue"), ma non aveva una riga di codice.

Le due linee (APEX-7 e Ruflo) sono nate indipendenti, senza reciproca consapevolezza.

## Decisione

Si fondono le due linee invece di costruire Ruflo da zero o lasciare APEX-7 come sistema
rivale: **`11-APEX-7-CORE` è promosso da ecosistema stand-alone a motore ufficiale della
Coordination Fabric di Ruflo.**

Rollout in due fasi:
- **Fase 1 (pilota, in corso)** — YouTube + Stream-S7-Bot migrano sullo stesso motore
  condiviso (`company/Ecosistemi/11-APEX-7-CORE/`), con isolamento multi-tenant per dominio.
- **Fase 2 (roadmap, non ancora costruita)** — estensione ordinata a tutti i 13 ecosistemi,
  un ecosistema alla volta, seguendo ADR-006 (ciclo 9 passi), dopo GATE+RETRO della Fase 1.
  Richiesto esplicitamente da Max: "va assolutamente ampliato per tutto l'intero Digital
  Empire" — non è opzionale, va scritta come roadmap fin da subito (vedi Piano allegato,
  `C:\Users\Utente\.claude\plans\tender-tumbling-flute.md`).

Le altre 3 implementazioni (YouTube standalone, skill generica, Stream-S7-Bot standalone)
restano deprecate-non-cancellate finché la migrazione non è verificata (ADR-003
wrap-non-riscrittura — nessuna riscrittura distruttiva senza prova che il sostituto funzioni).

## Alternative scartate

- **APEX-7-CORE canonico, Ruflo rimandato** — scartata: avrebbe lasciato il piano Ruflo
  (dossier 07, già scritto) morto sulla carta mentre si costruiva un sistema che lo duplica
  concettualmente.
- **Ruflo puro da zero** — scartata: avrebbe buttato via codice funzionante e testato
  (SQLite memory, EventBus, BaseAgent) già esistente in `11-APEX-7-CORE`, per riscriverlo
  identico sotto altro nome.
- **Rollout diretto su tutti i 13 ecosistemi subito** — scartata da Max stesso: pilota su 2
  prima di scalare, rispetta budget-guard e swarm-obbligatorio (ADR-006).

## Conseguenze

- `company/Ecosistemi/11-APEX-7-CORE/memory/memory_system.py` — `APEX7Memory` ora accetta
  `domain: str = "default"`, namespacing dati sotto `data/<domain>/` per isolamento
  multi-tenant. `domain="default"` mantiene il path storico invariato (carousel-machine,
  skill-forge, cold-outreach non impattati).
- `company/Ecosistemi/11-APEX-7-CORE/orchestrator/ruflo_core.py` — `RuFLOOrchestrator` accetta
  `domain: str = "default"` per coerenza di logging/metriche future.
- Nuovo test `company/Ecosistemi/11-APEX-7-CORE/test_multi_tenant.py` (4/4 verde) — verifica
  isolamento dati tra domini concorrenti.
- Fix bug bloccante: `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/memory.py` aveva un
  path assoluto hardcoded di un'altra macchina (`c:\Users\olhad\...`) come default — sostituito
  con path relativo allo script. `test_youtube_apex7.py` 11/11 ancora verde dopo il fix.
- Resta da fare (Fase 1, non ancora chiuso): retrofit di `apex7_orchestrator.py` (sostituire
  critic fisso e agenti hardcoded con chiamate al motore condiviso) e ritiro della
  reimplementazione indipendente in `12-STREAM-S7-BOT`.
- Ogni file toccato va registrato in `company/REGISTRO-IMPRESA.md` (ADR-008).
- `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md` va aggiornato per riflettere questa fusione (non
  ancora fatto in questo ciclo — prossimo passo).

## Contradiction-check

Verificato contro ADR-001 (10 ecosistemi, superato da ADR-009), ADR-003 (wrap non riscrittura —
rispettato: nessuna cancellazione, solo deprecazione), ADR-006 (ciclo 9 passi — rispettato:
Fase 2 rimandata a dopo GATE+RETRO Fase 1), ADR-008 (catena intestazione — registro da
aggiornare, vedi Conseguenze), ADR-009 (promuove `11-APEX-7-CORE` da ecosistema stand-alone a
motore condiviso — non lo abolisce, lo estende). Nessun conflitto irrisolto.
