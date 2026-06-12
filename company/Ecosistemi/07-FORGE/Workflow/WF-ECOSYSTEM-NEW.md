> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 07 L2 ECOSYSTEM-WORKS · L3 WF-ECOSYSTEM-NEW

# WF-ECOSYSTEM-NEW — Workflow L3: Forgiatura Ecosistema Completo

**Ecosistema:** 07-FORGE · **Reparto:** ECOSYSTEM-WORKS (L2.4) · **Stato:** DEFINED (F9+)

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Forgiare un **intero ecosistema L1** (business unit completa) quando la holding entra in
un nuovo territorio di business. È il livello massimo della FORGE: output è un ecosistema
funzionante con org L2-L5, BACKBONE.md, namespace memoria, dossier PIANO-MAESTRO e
registrazione completa. Attivazione: **SOLO mandato Board (L0) ratificato via hive-mind consensus (raft)**.

Il primo uso previsto: ecosistema E-commerce (F9+ della roadmap, build FORGE F5).

---

## Prerequisiti (gate d'ingresso — tutti obbligatori)

1. **Mandato Board completo**: missione, revenue model, DONE WHEN, budget, sponsor C-Suite dichiarati
2. **Dossier INTELLIGENCE**: ricerca mercato, dossier competitor, trend (da WF-COMPETITOR + WF-TREND)
3. **Business case OPERATIONS**: costo di run stimato dell'ecosistema (prima di scaffoldare)
4. **ADR in Memory**: decisione di creare l'ecosistema registrata in `company/Memory/decisions/`

---

## Fasi del workflow

| Fase | Attore | Output | Gate |
|---|---|---|---|
| **Mandato check** | `frg-chief` | verifica completezza mandato Board (5 campi) | mandato completo o respinto a Board |
| **Dossier mercato** | `frg-org-designer` + INTELLIGENCE | ricerca competitor, trend, posizionamento | dossier presente; senza dati di mercato non si propone |
| **PRD Enterprise (tipo A)** | `frg-prd-architect` | PRD ecosistema (10-30 pagine, tipo A) | quality score ≥ 75 |
| **Org design L2-L5** | `frg-org-designer` | org chart completa: reparti L2, workflow L3, funzioni L4, roster L5 | schema canonico rispettato (stesso scheletro degli altri 9 ecosistemi) |
| **BACKBONE.md** | `frg-org-designer` | topologia swarm, namespace memoria, handoff con gli altri 9 ecosistemi | confini espliciti con tutti gli ecosistemi esistenti (matrice riceve/fornisce/non-fa) |
| **Scaffold filesystem** | `frg-skill-smith` (skill ecosystem-scaffold) | struttura cartelle: Reparti/, Workflow/, Funzioni/, Agenti/, ECOSISTEMA.md | navigabile e conforme; verify.sh verde |
| **Namespace memoria** | `frg-hr-registrar` | `ruflo memory init --namespace <eco>` | namespace risponde a memory_search |
| **Agenti L5** | WF-AGENT-NEW per ogni agente del roster | agenti creati, testati, registrati | smoke test verde per ogni membro |
| **Dossier PIANO-MAESTRO** | `frg-prd-architect` + `frg-org-designer` | nuovo file `0N-ECOSISTEMA-*.md` | proposto alla Board per ratifica |
| **Registrazione holding** | `frg-hr-registrar` | skills-map.yaml + registro-agenti.yaml + GRUPPO.md aggiornati | G-REGISTRY holding completo |

---

## Regola "tutto o niente"

Un ecosistema mezzo-scaffoldato **non si consegna**. Deliverable richiesti in sequenza:
1. Org completa L2-L5
2. ECOSISTEMA.md + BACKBONE.md
3. Dossier PIANO-MAESTRO proposto
4. Namespace memoria inizializzato
5. Registrazione completa (Identity-HR + skills-map + GRUPPO.md)

Se uno manca → rollback (eliminazione dello scaffold parziale, ADR di rollback in Memory).

---

## Dry-run (gate prima del go-live)

Lo scaffold completo si valida a vuoto:
- Struttura navigabile (verify.sh categoria 1 verde)
- Handoff coerenti con gli altri 9 ecosistemi (test invio/ricezione handoff fittizio)
- Namespace memoria risponde
- Almeno 1 agente real-world operativo (smoke test)

Solo dopo dry-run verde → il primo agente reale può essere spawnato in produzione.

---

## KPI

| Metrica | Target |
|---|---|
| Ecosistemi scaffoldati senza mandato Board | 0 |
| Tempo mandato → scaffold completo | ≤ 10 giorni |
| Ecosistemi con verify.sh verde al primo dry-run | ≥ 90% |
| Divergenze dallo schema canonico dei 9 esistenti | 0 |
