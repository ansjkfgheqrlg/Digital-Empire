# 🧠 Ecosistema 10 — MEMORY (Memoria Operativa della Holding)

> **Priorità: MASSIMA. Si costruisce PER PRIMO (dentro F1), prima di ogni altro ecosistema.**
> MEMORY è l'organo che ricorda tutto ciò che Digital Empire Group **fa e decide**:
> ogni checkpoint, ogni decisione, ogni piano, ogni stato, ogni esito di task.
> Regola cardinale (pattern #13 del Piano Maestro): **PRIMA di qualsiasi task si interroga
> MEMORY; DOPO ogni task si scrive in MEMORY. Nessun task è "fatto" finché non è salvato.**
>
> Modello di riferimento: `orchestration/memory/` di AION GROUP (CP-001→024, ADR-001→007,
> sessions/, MEMORY-INDEX) — elevato da cartella di supporto a **ecosistema completo** con
> reparti, agenti e gate di enforcement.

---

## 0. Missione + DONE WHEN

**Missione:** garantire che la holding non perda mai contesto, non ripeta errori, non
contraddica decisioni prese, e possa riprendere QUALSIASI lavoro da QUALSIASI punto —
in qualsiasi sessione, da qualsiasi agente.

**DONE WHEN (misurabili):**
1. `company/Memory/` esiste, navigabile, con INDEX.md e STATO-EMPIRE.md sempre aggiornati.
2. **100% dei task chiusi ha un checkpoint** (CP) — verificato dalla Memory-Sentinel.
3. **0 decisioni senza ADR**: ogni scelta architetturale/strategica ha il suo ADR-NNN.
4. Ogni sessione di lavoro inizia con il caricamento di INDEX + STATO (pre-task gate attivo
   via hook) e chiude con session log.
5. Sync a 3 strati funzionante: file Memory ↔ wiki ↔ AgentDB (namespace `memory/`).
6. Ripresa a freddo testata: una sessione nuova ricostruisce lo stato completo di un
   lavoro in corso SOLO leggendo MEMORY (test "amnesia").

**OUT OF SCOPE:** conoscenza esterna ingerita (video, articoli, formazione) → è
INTELLIGENCE (Empire Studio + Memory Empire knowledge/). MEMORY archivia ciò che
l'azienda FA; INTELLIGENCE ciò che l'azienda IMPARA da fuori.

---

## 1. Posizione nella holding

MEMORY serve TUTTI gli ecosistemi ed è servito da tutti: è l'unico ecosistema con cui
**ogni** team ha un handoff obbligatorio bidirezionale.

| Handoff | Direzione | Payload | Acceptance criteria |
|---|---|---|---|
| HC-ME-PRE (pre-task gate) | qualsiasi team → MEMORY | `{task_id, ecosistema, descrizione, keywords}` | context-pack restituito: stato + CP/ADR/piani rilevanti + pattern AgentDB |
| HC-ME-POST (post-task commit) | qualsiasi team → MEMORY | `{task_id, esito, output_paths, lezioni, costi}` | CP scritto + INDEX aggiornato + STATO aggiornato |
| HC-ME-ADR | Board/qualsiasi team → MEMORY | `{decisione, contesto, alternative, conseguenze}` | ADR-NNN registrato + contradiction-check passato |
| HC-ME-PLAN | Board/FORGE → MEMORY | nuovo piano o revisione | versionato in plans/ + STATO aggiornato |
| MEMORY → ReasoningBank (Backbone BRAIN) | continuo | fallimenti distillati in pattern | pattern in AgentDB namespace `patterns` |
| MEMORY → wiki (INTELLIGENCE) | continuo | eventi rilevanti per gli umani | entry in `wiki/log.md` |

**Confini netti:**
- **Backbone BRAIN** = infrastruttura (AgentDB/HNSW, bus): MEMORY la USA, non la duplica.
- **INTELLIGENCE** = conoscenza esterna (Empire Studio, Memory Empire knowledge/).
- **wiki** = vista leggibile dall'uomo; MEMORY = registro operativo macchina+uomo.

---

## 2. Struttura filesystem (la "cassaforte")

```
Digital Empire/company/Memory/
├── INDEX.md                    # indice maestro — SEMPRE caricato a inizio sessione
├── STATO-EMPIRE.md             # stato corrente holding: fase roadmap, lavori in corso,
│                               #   blocchi, prossime azioni (l'equivalente del "RIPRESA DA:")
├── checkpoints/                # CP-YYYYMMDD-NNN.md — uno per ogni task chiuso
├── decisions/                  # ADR-NNN.md — ogni decisione architetturale/strategica
├── plans/                      # tutti i piani (PIANO-MAESTRO è qui linkato + piani di fase)
├── sessions/                   # session-YYYYMMDD[-n].md — log di ogni sessione di lavoro
├── tasks/                      # log task per ecosistema
│   ├── 01-agency/ … 10-memory/
├── state/                      # state.json per ogni progetto/ordine in corso
│   └── <progetto-id>/state.json + trace.jsonl
└── audit/                      # audit trail: chi ha scritto cosa, quando, backup refs
```

**Template CP (obbligatorio):**
```markdown
# CP-YYYYMMDD-NNN — <titolo task>
- Ecosistema/Reparto: …
- Task: … (rif. piano/fase)
- Esito: ✅ completato | ⚠️ parziale | ❌ fallito
- Output: <path reali prodotti>
- Decisioni prese: <link ADR se create>
- Lezioni/errori: <per ReasoningBank>
- Costi: <token/crediti/€ se applicabile>
- Prossimo passo: …
```

**Template ADR:** contesto → decisione → alternative scartate → conseguenze → stato
(proposto/attivo/superato da ADR-X).

---

## 3. Reparti L2

### M1 — Recall & Pre-Task Gate (il reparto più critico)
Missione: nessun task parte "al buio".
- **T-M1.1 Context Loader (L3):** su HC-ME-PRE carica INDEX + STATO + CP/ADR pertinenti
  (match per ecosistema + keywords) + `memory_search` su AgentDB → produce **context-pack**.
- **T-M1.2 Relevance Scorer (L4):** ordina per rilevanza, taglia il rumore (max N item),
  segnala contraddizioni potenziali col task richiesto.

### M2 — Checkpoint & Sessioni
Missione: ogni task chiuso lascia traccia; ogni sessione ha apertura/chiusura.
- **T-M2.1 Checkpoint Writer (L3):** su HC-ME-POST scrive CP, aggiorna INDEX e STATO.
- **T-M2.2 Session Logger (L4):** apre/chiude session-log; a chiusura compila "RIPRESA DA:".

### M3 — Decisioni (ADR)
Missione: zero decisioni implicite.
- **T-M3.1 ADR Registrar (L3):** registra ADR su HC-ME-ADR.
- **T-M3.2 Contradiction Checker (L4):** confronta ogni nuovo ADR/piano con gli ADR attivi
  (motore: skill-contradiction-analyzer); conflitto → escalation al Board, non si registra.

### M4 — Piani & Stato
Missione: i piani sono versionati, lo stato è VERO (letto dal filesystem, mai dichiarato —
pattern catalog_status di Empire Studio).
- **T-M4.1 Plan Keeper (L3):** custodisce/versiona piani; ogni revisione = nuova versione + diff.
- **T-M4.2 State Tracker (L4):** mantiene state.json + trace.jsonl per progetto; aggiorna
  STATO-EMPIRE.md a ogni cambio fase.

### M5 — Sync & Integrità
Missione: i 3 strati (file ↔ wiki ↔ AgentDB) non divergono mai; tutto è recuperabile.
- **T-M5.1 Sync Agent (L3):** propaga eventi → `wiki/log.md` (vista umana) e → AgentDB
  namespace `memory/` (recall semantico agenti).
- **T-M5.2 Integrity Auditor (L4):** audit trail, verifica CP mancanti, backup/rollback
  (pattern backup→append→log→rollback di Memory Empire — mai overwrite).

---

## 4. Roster agenti L5

| ID | Ruolo | Tipo | Tier |
|---|---|---|---|
| ME-A00 ME-Conductor | orchestra l'ecosistema, riceve tutti gli HC-ME-* | coordinator | sonnet |
| ME-A01 context-loader | carica INDEX/STATO/CP/ADR + memory_search | worker | haiku |
| ME-A02 relevance-scorer | scoring e taglio context-pack | worker | haiku |
| ME-A03 checkpoint-writer | scrive CP + aggiorna INDEX/STATO | worker | haiku |
| ME-A04 session-logger | apertura/chiusura sessioni | worker | haiku |
| ME-A05 adr-registrar | registra ADR strutturati | worker | sonnet |
| ME-A06 contradiction-checker | conflitti tra decisioni/piani | worker | sonnet |
| ME-A07 plan-keeper | versioning piani + diff | worker | haiku |
| ME-A08 state-tracker | state.json/trace.jsonl per progetto | worker | haiku |
| ME-A09 sync-agent | propaga a wiki + AgentDB | worker | haiku |
| ME-A10 integrity-auditor | audit, backup, rollback, CP mancanti | worker | sonnet |
| ⊕ Memory-Sentinel | always-on: rileva task chiusi SENZA CP e sessioni senza log → escalation | sentinel | haiku |

---

## 5. Workflow chiave end-to-end

```
WF-PRETASK (gate bloccante — pattern #13)
  task richiesto → ME-A01 carica INDEX+STATO+CP/ADR → ME-A02 scoring →
  context-pack → SOLO ORA il task può partire
  (se MEMORY segnala contraddizione con ADR attivo → STOP + escalation Board)

WF-POSTTASK (commit obbligatorio)
  task chiuso → HC-ME-POST → ME-A03 scrive CP → ME-A08 aggiorna stato →
  ME-A09 sync (wiki/log + AgentDB) → lezioni → ReasoningBank →
  acceptance: il team committente riceve conferma CP-id (senza CP-id il task NON è chiuso)

WF-DECISION
  decisione emersa → ME-A05 draft ADR → ME-A06 contradiction-check vs ADR attivi →
  ok: registrato + INDEX | conflitto: escalation hive-mind Board

WF-SESSION
  apertura: ME-A01 serve STATO-EMPIRE + "RIPRESA DA:" della sessione precedente
  chiusura: ME-A04 session-log + CP di sessione + STATO aggiornato
```

---

## 6. Enforcement (come si rende OBBLIGATORIO)

Il memory-first non può essere solo una regola scritta — va cablato:

1. **Hook Claude Code** (fase di build M2): SessionStart → inietta INDEX + STATO-EMPIRE;
   UserPromptSubmit → reminder pre-task gate; a fine lavoro → reminder CP
   (stesso meccanismo già usato per WIKI-FIRST/Empire Studio in `.claude/settings`).
2. **CLAUDE.md di Digital Empire**: aggiunta REGOLA MEMORY-FIRST accanto a WIKI-FIRST.
3. **Schema team canonico**: l'acceptance criteria di OGNI team L3/L4 della holding include
   "CP scritto in Memory" — un handoff senza CP-id è invalido per contratto.
4. **Memory-Sentinel**: scansione periodica → task/sessioni senza CP → escalation.
5. **verify-empire.sh**: categoria di check dedicata (INDEX aggiornato, 0 CP orfani,
   STATO coerente col filesystem, ADR senza conflitti).

---

## 7. Asset esistenti → integrazione

| Asset | Azione |
|---|---|
| `orchestration/memory/` di CF (CP/ADR/sessions/MEMORY-INDEX) | MODELLO: copiare formato e disciplina, non i contenuti |
| Memory Empire skill (`~/.claude/skills/memory-empire/`) | PARTNER: resta motore di INTELLIGENCE per conoscenza esterna; MEMORY ne riusa i pattern (handoff JSON, backup→append→log→rollback) |
| `second-brain-vault/wiki/log.md` | VISTA UMANA: ME-A09 vi propaga gli eventi (non si duplica, si sincronizza) |
| Memoria auto di Claude (`~/.claude/projects/...Digital-Empire/memory/`) | PERSONALE di Claude: resta; i fatti aziendali durevoli vanno in company/Memory |
| AgentDB (ruflo) namespace `memory/` | INDICE SEMANTICO: ogni CP/ADR → memory_store per recall |
| Empire Studio `catalog_status.py` (stato letto dal filesystem) | PATTERN per State Tracker: stato mai dichiarato, sempre verificato |

---

## 8. Skill nuove da creare (ordina alla FORGE)

| Skill | Scopo | Priorità |
|---|---|---|
| `empire-memory-gate` | implementa WF-PRETASK: carica context-pack; invocabile da ogni agente | P0 |
| `empire-checkpoint` | implementa WF-POSTTASK: scrive CP da template + sync | P0 |
| `empire-adr` | registra ADR + contradiction-check | P1 |
| `empire-stato` | legge/aggiorna STATO-EMPIRE dal filesystem reale | P1 |

---

## 9. Integrazione Ruflo

- **Topologia:** hierarchical (ME-Conductor root); ME-A09 in mesh col Backbone.
- **Namespace AgentDB:** `memory/checkpoints`, `memory/decisions`, `memory/state`,
  `memory/sessions` — ogni CP/ADR indicizzato a doppio binario (file = verità, vettore = recall).
- **Hooks ruflo:** `hooks post-task --store-results true` mappato su WF-POSTTASK.

---

## 10. KPI + Quality Gates

| KPI | Target |
|---|---|
| Task chiusi con CP | 100% (gate, non KPI) |
| Decisioni con ADR | 100% |
| Tempo recall pre-task | ≤ 30s per context-pack |
| Test "amnesia" (ripresa a freddo) | superato a ogni fase roadmap |
| Divergenza file↔wiki↔AgentDB | 0 rilevate da audit |

**Gates:** G-ME1 pre-task gate attivo (hook) · G-ME2 CP-id obbligatorio negli handoff ·
G-ME3 contradiction-check su ogni ADR · G-ME4 audit integrità settimanale verde.

---

## 11. Fasi di build (dentro F1 — PRIMA di tutto il resto)

| Fase | Cosa | Gate |
|---|---|---|
| **ME-0** | Creare `company/Memory/` completa: INDEX, STATO-EMPIRE, cartelle, template CP/ADR/session | struttura esiste; primo CP scritto è QUESTO piano |
| **ME-1** | Migrare la storia: questo PIANO-MAESTRO in plans/, decisioni già prese (EMPIRE OS, 10 ecosistemi, memory-first) come ADR-001..N | INDEX popolato |
| **ME-2** | Enforcement: regola in CLAUDE.md + hook SessionStart/UserPromptSubmit | sessione nuova carica STATO automaticamente |
| **ME-3** | AgentDB: namespace memory/ + store dei CP/ADR esistenti | memory_search restituisce CP reali |
| **ME-4** | Memory-Sentinel + check in verify-empire.sh | 0 CP orfani |
| **ME-5** | Test "amnesia": sessione pulita ricostruisce lo stato solo da MEMORY | superato |

---

## 12. Rischi

| Rischio | Mitigazione |
|---|---|
| Burocrazia: CP percepiti come overhead → saltati | template 30 secondi, checkpoint-writer li compila lui; Memory-Sentinel rileva i buchi |
| INDEX cresce e diventa illeggibile | INDEX = solo puntatori 1-riga (stile MEMORY.md); rotazione per trimestre |
| Doppioni con wiki/log | confini netti §1: Memory=registro operativo, wiki=vista umana; sync unidirezionale ME-A09 |
| Stato dichiarato ≠ stato reale | State Tracker legge SEMPRE dal filesystem (pattern catalog_status) |
| Contradiction-checker troppo zelante (blocca tutto) | blocca solo conflitti con ADR ATTIVI; il resto è warning |

---

## Connessioni
- [[00-PIANO-MAESTRO]] — pattern #13 memory-first
- [[07-BACKBONE-RUFLO-SKILLS]] — BRAIN/AgentDB (infrastruttura usata da MEMORY)
- [[Memory_Empire]] — partner per la conoscenza esterna (INTELLIGENCE)
- [[projects/Exponium/Exponium_Content_Factory_Studio]] — modello memory/ CP+ADR
