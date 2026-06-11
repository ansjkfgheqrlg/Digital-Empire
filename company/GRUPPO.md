# 🏛️ DIGITAL EMPIRE GROUP — Organigramma Holding

> **Documento vivente.** Rispecchia `PIANO-MAESTRO/00-PIANO-MAESTRO.md` §2.
> Gerarchia: Mandato Empire (LX) → Board/C-Suite (L0) → 10 Ecosistemi (L1) →
> Reparti (L2) → Workflow (L3) → Funzioni (L4) → Agenti (L5).
> Aggiornare ogni volta che un ecosistema cambia struttura o un agente viene assunto/ritirato.

---

## LX — DIPARTIMENTO EMPIRE (Autorità Suprema)

> Nessun agente, nessun codice. È il **Mandato**: le leggi costituzionali della holding.
> Tutto ciò che esce da Digital Empire deve rispettarlo. I Sentinel lo vigilano.

- **Mandato Empire** → `Mandato/MANDATO-EMPIRE.md`
- **5 Sentinel** → `Sentinels/` (Cost · Quality · Drift · Security · Brand-Voice)

---

## L0 — BOARD / C-SUITE

> Decisioni cross-ecosistema via hive-mind consensus (raft). Si attiva quando un task
> tocca 2+ ecosistemi o supera il budget autorizzato.

| Ruolo | Agente | File |
|---|---|---|
| CEO / Empire-Conductor | empire-conductor | `Board-CSuite/CEO-Empire-Conductor.md` |
| COO (Operations) | empire-coo | `Board-CSuite/COO.md` |
| CTO (Platform + Forge) | empire-cto | `Board-CSuite/CTO.md` |
| CMO (Marketing + Content) | empire-cmo | `Board-CSuite/CMO.md` |
| CRO (Revenue — Agency + InfoBiz) | empire-cro | `Board-CSuite/CRO.md` |
| CFO (Budget + Cost guard) | empire-cfo | `Board-CSuite/CFO.md` |
| Chief Forge (Org R&D — crea team/skill/ecosistemi) | empire-chief-forge | `Board-CSuite/Chief-Forge.md` |

---

## L1 — 10 ECOSISTEMI (Business Unit)

> Indipendenti ma connesse via Corporate Backbone (Bus). Ognuna ha la propria
> org interna L2→L5 in `Ecosistemi/<NN-NOME>/`.

| # | Ecosistema | Missione sintetica | Priorità | Path |
|---|---|---|---|---|
| 01 | **AGENCY** | Acquisisci e servi clienti (3 impl. AI: Outreach €4k, Content €3.5k, Second Brain €2.5k, Engine Room €8k) | ALTA | `Ecosistemi/01-AGENCY/` |
| 02 | **INFO-BUSINESS** | Lanci corsi, ebook, community (Manuale Claude Code, Skill Beast) | ALTA | `Ecosistemi/02-INFO-BUSINESS/` |
| 03 | **CONTENT-FACTORY** | Produzione contenuti multi-formato multi-brand per tutti gli ecosistemi | ALTA | `Ecosistemi/03-CONTENT-FACTORY/` |
| 04 | **MARKETING** | Motore persuasione trasversale: copywriting (priorità assoluta), ads, email, analytics | ALTA | `Ecosistemi/04-MARKETING/` |
| 05 | **MULTI-BUSINESS** | Business paralleli scalabili: YouTube Automation, E-commerce, Publishing/KDP | MEDIA-ALTA | `Ecosistemi/05-MULTI-BUSINESS/` |
| 06 | **PLATFORM** | Engineering, siti (Crea Siti, empire-style), tooling, sicurezza, CI/CD, deploy | TRASVERSALE | `Ecosistemi/06-PLATFORM/` |
| 07 | **FORGE** | Fabbrica organizzativa: crea skill, agenti, team, interi ecosistemi (skill-creator, content-forge, System OMEGA) | TRASVERSALE | `Ecosistemi/07-FORGE/` |
| 08 | **INTELLIGENCE** | Second brain, wiki, Empire Studio (ingestione video), ricerca e trend, Memory Empire | TRASVERSALE | `Ecosistemi/08-INTELLIGENCE/` |
| 09 | **OPERATIONS** | Runtime: swarm mass-production, budget guard, cost-attribution, storage, scheduling | TRASVERSALE | `Ecosistemi/09-OPERATIONS/` |
| 10 | **MEMORY** | Memoria operativa: checkpoint, decisioni (ADR), piani, stato. **Interrogata PRIMA, scritta DOPO ogni task** | **MASSIMA** | `Ecosistemi/10-MEMORY/` |

---

## ⊕ GUILDS (Trasversali — attraversano tutti gli ecosistemi)

> Una Guild è un gruppo di agenti con expertise comune che serve tutti i team.
> Non ha gerarchia verticale — è un collegium orizzontale.

| Guild | Expertise | Path |
|---|---|---|
| Prompt Guild | prompt engineering, prompt review | `Guilds/Prompt-Guild/` |
| Copy/APSOC Guild | framework APSOC, brand voice, headline | `Guilds/Copy-APSOC-Guild/` |
| Quality Guild | QA, testing, contradiction-analyzer, gate | `Guilds/Quality-Guild/` |
| Cost Guild | cost-attribution, budget guard, routing tier | `Guilds/Cost-Guild/` |
| Design Guild | visual identity, empire-style, template | `Guilds/Design-Guild/` |

---

## ⊕ SENTINELS (Always-on — vigilano su OGNI livello)

> Un Sentinel blocca attivamente l'output non conforme al Mandato Empire.
> Non è un reviewer opzionale: è un gate hard.

| Sentinel | Cosa vigila | Blocca se... |
|---|---|---|
| Cost Sentinel | spese API, crediti, budget per task | sfora budget autorizzato senza ok |
| Quality Sentinel | gate APSOC ≥80, zero claim senza prova | score < soglia o claim non verificato |
| Drift Sentinel | coerenza architetturale tra ecosistemi | output contraddice un ADR attivo |
| Security Sentinel | segreti, PII, injection, sicurezza | leak di credenziali o injection rilevata |
| Brand-Voice Sentinel | tono DE: diretto, provocatorio, trasparente | output generico, vago, AI-slop |

---

## Corporate Backbone (Servizi condivisi L0)

> Il sistema nervoso della holding. Tutti gli ecosistemi lo usano, nessuno lo possiede.

| Componente | Funzione | Path |
|---|---|---|
| **BUS** | Message bus inter-ecosistema, handoff contract JSON | `Backbone/Bus/` |
| **BRAIN** | AgentDB/HNSW + wiki bridge + ReasoningBank | `Backbone/Brain/` |
| **GOVERNANCE** | verify-empire.sh, gate qualità, contradiction-analyzer | `Backbone/Governance/` |
| **IDENTITY-HR** | registro-agenti.yaml unico, assume/ritira via Forge | `Backbone/Identity-HR/` |
| **OBSERVABILITY** | metrics, dashboard, neural_train, autopilot, cost-attr | `Backbone/Observability/` |
| **COORDINATION** | Ruflo swarm topologies, hive-mind consensus (raft) | `Backbone/Coordination/` |

---

## Gerarchia completa (livelli)

```
LX   Mandato Empire + Sentinels (autorità suprema — regole, non agenti)
L0   Board / C-Suite (7 agenti) — decisioni cross-ecosistema
L1   10 Ecosistemi — Business Unit indipendenti
L2   Reparti (dentro ogni ecosistema — es. AGENCY: Acquisizione, Delivery, Copy)
L3   Workflow (un team per flusso end-to-end — es. WF-OUTREACH-EMAIL)
L4   Funzioni (un team per singola funzionalità — es. T-Thumbnail)
L5   Agenti reali (coordinator + worker, running via Ruflo / Agent tool)
⊕    Guilds (trasversali tra ecosistemi)
⊕    Sentinels (always-on su tutti i livelli)
```

Schede complete per livello: `Gerarchia/`

---

## Navigazione rapida

| Voglio... | Vai a |
|---|---|
| Capire identità e regole | `Mandato/MANDATO-EMPIRE.md` |
| Vedere chi decide cosa | `Board-CSuite/` |
| Entrare in un ecosistema | `Ecosistemi/NN-NOME/ECOSISTEMA.md` |
| Capire il sistema nervoso | `Backbone/` |
| Trovare un agente specifico | `Backbone/Identity-HR/registro-agenti.yaml` |
| Verificare la struttura | `scripts/verify-empire.sh` |
| Stato corrente / task in corso | `Memory/STATO-EMPIRE.md` |
| Decisioni architetturali | `Memory/decisions/ADR-*.md` |

---

*Generato: 2026-06-11 · Fonte: `PIANO-MAESTRO/00-PIANO-MAESTRO.md` §1-4*
*Rigenerabile con: `python scripts/gen-empire.py --target gruppo`*
