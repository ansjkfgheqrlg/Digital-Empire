# Reparto L2.2 — AGENT-WORKS (forgia agenti e team)

> **Ecosistema:** 07-FORGE · **Livello:** L2 · **Owner:** Chief-Forge (`frg-chief`)
> Workflow L3: `../../Workflow/WF-AGENT-NEW/` · `../../Workflow/WF-TEAM-NEW/`

## Cosa fa

AGENT-WORKS produce le **persone digitali** della holding: agenti singoli (L5) e team
completi (L3/L4). È il reparto che dà corpo alla regola strutturale fondamentale di
EMPIRE OS: **un team di agenti per ogni singola funzionalità** (coordinator + workers,
I/O espliciti, acceptance criteria, escalation protocol, shared_state).

1. **WF-AGENT-NEW** — agente singolo: `architect-agent` progetta l'identità →
   struttura 7-file (identità, prompt, I/O, reasoning, tools, handoff, memoria) →
   smoke test → registrazione in Identity-HR.
2. **WF-TEAM-NEW** — team canonico L3/L4: org design (chi fa cosa), handoff contract
   tra i membri, schema shared_state, acceptance criteria del team, escalation.

Ogni agente nasce con: tier modello dichiarato (WASM/Haiku/Sonnet/Opus — il più
economico che regge il task), costo stimato/run, KPI misurabili, owner umano o C-Suite.

## Come si collega

| Con | Relazione |
|---|---|
| SKILL-WORKS | gli agenti USANO le skill (pattern #6): AGENT-WORKS non duplica conoscenza nelle istruzioni dell'agente, la referenzia |
| METHOD-GUARD | T-org-design applica lo schema canonico CF; SPARC su ogni team non banale |
| ECOSYSTEM-WORKS | quando l'ordine è un ecosistema intero, AGENT-WORKS fornisce i roster L5 |
| OPERATIONS | nessun agente nasce senza pre-approvazione budget (tier + costo stimato) |
| Identity-HR | ogni assunzione/ritiro passa da `frg-hr-registrar` → `registro-agenti.yaml` |
| `SKILL & Agenti/agent-factory/` | asset esistente da EVOLVERE (valutare merge con WF-AGENT-NEW) |

Funzioni L4 del reparto: `../../Funzioni/T-org-design/` ·
`../../Funzioni/T-handoff-contracts/` · `../../Funzioni/T-shared-state-schema/`.
Agenti: `frg-org-designer` (Opus — disegna), `frg-hr-registrar` (Haiku — registra),
con `frg-spec-writer` per il G-SPEC d'ingresso.

## 🧠 Come si ATTIVA e RAGIONA

**Attivazione.** Da ordine approvato di `frg-chief` con tipo `agente` o `team`.
Trigger tipici: un ecosistema ha un workflow L3 scoperto (es. F4 AGENCY chiede il wrap
del team outreach), il dossier prevede un roster non ancora reale, oppure Observability
segnala un collo di bottiglia che richiede un worker in più.

**Ragionamento:**
1. **Problema, non organigramma** — quale funzionalità concreta deve coprire l'agente/team?
   Se la risposta è "riempire uno schema" → blocco (regola di Chief-Forge).
2. **Riusa prima di assumere** — `memory_search` su `forge/registry`: esiste un agente
   con pass_rate alto e capacità affini? → estendi lui, non crearne un altro (KPI: 0 duplicati).
3. **Tier al ribasso** — si parte dal tier più economico che può reggere il task
   (OPERATIONS predica: ≥70% dei task su WASM/Haiku); Opus solo per design/arbitraggio.
4. **Schema canonico SEMPRE** — coordinator + workers; un agente solo è un team degenere
   ma ha comunque I/O, acceptance, escalation scritti.
5. **Smoke test prima del registro** — l'agente esegue un task reale piccolo; se fallisce,
   si itera: non si registra un agente mai testato.
6. **Nascita = registro + budget** — G-REGISTRY: un agente non censito in Identity-HR
   non esiste; un agente senza costo dichiarato non parte.

**Anti-pattern vietati:** agenti fotocopia (stesso ruolo, nome diverso); team senza
escalation protocol; istruzioni-agente che inglobano conoscenza che dovrebbe stare in
una skill; spawn diretto senza passare dal registro.

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §07 L2 AGENT-WORKS · Aggiornato: 2026-06-11*
