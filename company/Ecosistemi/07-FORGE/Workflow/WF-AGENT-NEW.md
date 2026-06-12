> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 07 L2 AGENT-WORKS · L3 WF-AGENT-NEW

# WF-AGENT-NEW — Workflow L3: Creazione Agente Singolo

**Ecosistema:** 07-FORGE · **Reparto:** AGENT-WORKS (L2.2) · **Stato:** DEFINED

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Produrre un **agente L5 testato, registrato e operativo** a partire da un gap di capacità
identificato. Struttura di output: 7 file canonici (identità, prompt, I/O, reasoning,
tools, handoff, memoria). Nessun agente nasce senza smoke test e senza voce in Identity-HR.

---

## Trigger di attivazione

- Ecosistema ha un workflow L3/L4 scoperto (manca il worker o il coordinator)
- Il dossier prevede un roster non ancora reale (piano di build FORGE F1-F5)
- Observability segnala collo di bottiglia che richiede un worker aggiuntivo
- WF-TEAM-NEW richiede i singoli agenti per il team canonico

---

## Fasi del workflow

| Fase | Attore | Output | Gate |
|---|---|---|---|
| **Memoria check** | `frg-spec-writer` | ricerca in `forge/registry` (AgentDB): agente affine esistente? | se esiste con pass_rate alto → estendi, non duplicare |
| **Spec agente** | `frg-spec-writer` (agent-specification) | spec.md: ruolo, responsabilità, I/O, acceptance, tier modello, costo stimato | G-SPEC approvato da `frg-chief` |
| **Architettura 7-file** | `frg-org-designer` (architect-agent) | struttura 7-file: identity.md, prompt.md, io.md, reasoning.md, tools.md, handoff.md, memory.md | schema canonico CF rispettato |
| **Smoke test** | agente stesso + `frg-eval-runner` | 1 task reale piccolo eseguito con successo | task completato senza errori; output conforme all'acceptance |
| **Registrazione HR** | `frg-hr-registrar` | record in registro-agenti.yaml (tier, costo, KPI, stato: active) | G-REGISTRY: agente non esistente senza registro |
| **Budget pre-approval** | `frg-hr-registrar` → OPERATIONS | costo stimato/run dichiarato a OPERATIONS | OPERATIONS conferma budget tier disponibile |
| **Deploy** | `frg-skill-smith` | agente disponibile nell'ecosistema richiedente | handoff al coordinator del workflow destinatario |

---

## Struttura 7-file dell'agente (schema canonico CF)

```
<agente-id>/
├── identity.md     — ID, ruolo, tier, ecosistema, reparto, team
├── prompt.md       — system prompt (kernel ≤ 500 righe)
├── io.md           — input attesi, output prodotti, formato handoff
├── reasoning.md    — processo decisionale (come ragiona, sequenza passi)
├── tools.md        — skill/tool che usa, con condizioni d'uso
├── handoff.md      — escalation protocol, chi chiama se stuck
└── memory.md       — cosa store/search nel Brain (namespace, chiavi)
```

---

## Regole operative

- **Tier al ribasso**: si parte dal modello più economico che regge il task (target: ≥70% Haiku)
- **Smoke test obbligatorio**: un agente mai testato non va nel registro
- **Nascita = registro + budget**: entrambi obbligatori in sequenza
- **Un agente, un ruolo**: nessun agente multiruolo (rischio drift); se serve più capacità → team

---

## KPI

| Metrica | Target |
|---|---|
| Agenti con smoke test verde al primo tentativo | ≥ 80% |
| Tempo spec → registro (agente standard) | ≤ 3 giorni |
| Agenti running non anagrafati | 0 |
| Quota task su tier Haiku o inferiore | ≥ 70% del roster |
