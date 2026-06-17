---
Type: CONCEPT
Status: Active
Tags: #ceo #architettura #gerarchia #flusso-decisionale #mandato
Created: 2026-06-17
Last updated: 2026-06-17
---

# CEO / Empire-Conductor — Architettura Espansa

> Fonte primaria: `company/Board-CSuite/_BLUEPRINT/BP-CEO.md`
> Fonte v1: `company/Board-CSuite/CEO-Empire-Conductor.md`
> Connessioni: [[12-DOSSIER-MAXIMILIAN]] · [[13-DOSSIER-MANDATO-ECOSISTEMA]]

---

## 1. Posizione nella gerarchia

```
MAX (founder — umano)
  │
  ├─ MANDATO (LX) ─────────── Cosa è lecito (regole non negoziabili)
  ├─ MAXIMILIAN ───────────── Cosa è all'altezza (standard e visione)
  │
  └─ CEO / Empire-Conductor   ← questa figura (L0 Board C-Suite)
       │
       ├─ Board C-Suite (5 colleghi: COO, CFO, CRO, CMO, Chief-Forge)
       └─ 10 Ecosistemi (L1, in ingresso direttive; in uscita KPI)
```

Il CEO non si trova sopra il Mandato né sopra MAXIMILIAN. La sua autorità è operativa
e decisionale, non normativa (Mandato) né di standard (MAXIMILIAN).

---

## 2. Gerarchia interna del team CEO

```
ceo-conductor (Opus — decisore)
  │
  ├── [ANALISI PRE-DECISIONE]
  │     ├── ceo-analista-strategico (Opus)
  │     ├── ceo-advisor-rischi (Sonnet)
  │     └── ceo-advisor-opportunita (Sonnet)
  │
  ├── [ARBITRATO & RISORSE]
  │     ├── ceo-priorita-arbiter (Opus)
  │     └── ceo-budget-allocator (Sonnet)
  │
  ├── [TRACKING & COMUNICAZIONE]
  │     ├── ceo-okr-tracker (Haiku)
  │     └── ceo-comunicatore (Sonnet)
  │
  └── [VERIFICA & MEMORIA]
        ├── ceo-verificatore (Sonnet)
        └── ceo-memoria (Haiku)
```

Il `ceo-conductor` è l'unico agente che parla con il Mandato (LX) e con MAXIMILIAN.
Gli altri 9 agenti parlano solo all'interno del team CEO o verso le altre figure C-Suite
su delega esplicita del conductor.

---

## 3. Flusso decisionale standard

```
INPUT CROSS-ECOSISTEMA
        │
        ▼
[ceo-memoria] — carica STATO-EMPIRE + ADR attivi + checkpoint recenti
        │
        ▼
[ceo-conductor] — verifica: questione già decisa? Sì → applica ADR, stop
        │ No
        ▼
[ceo-analista-strategico] — mappa scenari possibili (3-5 opzioni)
[ceo-advisor-rischi]      ─┐ in parallelo
[ceo-advisor-opportunita] ─┘
        │
        ▼
[ceo-conductor] — istruttoria Mandato: la proposta contraddice un Articolo LX?
        │ Sì → respinta o proposta ADR a Max
        │ No
        ▼
[ceo-budget-allocator] — dry-run economico (se la decisione spende)
        │
        ▼
[ceo-conductor] — propone al Board; [ceo-priorita-arbiter] se conflitto risorse
        │
        ▼
VOTO RAFT (Board C-Suite) — quorum; stallo → voto decisivo conductor
        │
        ▼
GATE MANDATO (LX) — ogni decisione passa il gate prima del dispatch
        │
        ▼
[ceo-comunicatore] — traduce decisione in direttive eseguibili per ecosistemi
        │
        ▼
[ceo-memoria] — ADR (se architetturale) + checkpoint Memory
        │
        ▼
[ceo-verificatore] — monitora esecuzione; ritorna anomalie al conductor
```

---

## 4. Relazione con il Mandato (LX)

Il Mandato è il gate bloccante PRIMA del dispatch. Il CEO non può approvare nulla che
violi un Articolo LX. Se la proposta contradice LX:
- **Opzione A:** viene respinta (decisione non presa).
- **Opzione B:** viene convertita in proposta di deroga/ADR → sale a Max per approvazione.

Il CEO non può modificare il Mandato. Può solo proporre ADR a Max (Art.4.1 del Mandato).

---

## 5. Relazione con MAXIMILIAN

MAXIMILIAN interviene sul CEO come **passo 5-bis del ciclo a 9 passi** (ADR-006):
dopo la review indipendente (passo 5) e prima del commit (passo 7), per le decisioni
di scala o di standard architetturale. La domanda di MAXIMILIAN: *"Questa decisione è
abbastanza grande? È millimetrica? Max l'approverebbe?"*

Il CEO fornisce il dossier decisionale completo (rationale + opzioni + impatti). MAXIMILIAN
risponde APPROVA / RIFAI + motivo. Il CEO non bypassa mai questo gate.

---

## 6. Handoff contract con il Board C-Suite

| Contract ID | Da → A | Payload | Acceptance criteria |
|---|---|---|---|
| `HC-CEO-COO-01` | CEO → COO | direttiva operativa + acceptance criteria | COO conferma ricevuta e assegna owner operativo |
| `HC-CEO-CFO-01` | CEO → CFO | envelope di spesa + obiettivo | CFO valida disponibilità e risponde con go/no-go |
| `HC-CEO-CRO-01` | CEO → CRO | priorità revenue del trimestre | CRO aggiorna pipeline e conferma capacità |
| `HC-CEO-CMO-01` | CEO → CMO | priorità contenuti/marketing | CMO aggiorna piano contenuti e conferma |
| `HC-CEO-CF-01` | CEO → Chief-Forge | proposta nuovo ecosistema/team L1 | Chief-Forge porta a Council per voto |
| `HC-COO-CEO-01` | COO → CEO | report blocchi operativi + KPI giornalieri | CEO legge in apertura sessione Board |
| `HC-CFO-CEO-01` | CFO → CEO | alert Cost-Sentinel + budget status | CEO triggera WF-DECISIONE se soglia superata |
| `HC-CRO-CEO-01` | CRO → CEO | pipeline revenue + scalazione | CEO decide se portare a Council |

---

## 7. Namespace memoria (AgentDB `board/ceo`)

Il team CEO presidia le seguenti chiavi di stato:

| Chiave | Cosa contiene | Owner |
|---|---|---|
| `board/ceo/stato-holding` | snapshot STATO-EMPIRE corrente | ceo-memoria |
| `board/ceo/adr-attivi` | lista ADR attivi con contraddiction-check | ceo-memoria |
| `board/ceo/decisioni-pendenti` | decisioni aperte non ancora votate | ceo-conductor |
| `board/ceo/direttive-dispatch` | direttive inviate e loro stato (eseguita/in-corso/non-eseguita) | ceo-verificatore |
| `board/ceo/okr-trimestre` | OKR del trimestre corrente + progress | ceo-okr-tracker |
| `board/ceo/budget-envelope` | envelope di spesa autorizzate per ecosistema | ceo-budget-allocator |

---

## Connessioni

- [[README]] · `company/Board-CSuite/CEO-Empire-Conductor/README.md`
- [[BP-CEO]] · `company/Board-CSuite/_BLUEPRINT/BP-CEO.md`
- [[12-DOSSIER-MAXIMILIAN]] · `PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`
- [[ADR-006]] · `company/Memory/decisions/`
- [[10-ECOSISTEMA-MEMORY]] · `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md`
