---
Owner: Max · Controllore: Claude · Origine: FORGE · Governo: MANDATO-EMPIRE.md + ADR-002
Esecutore: GEMINI (Antigravity) · Priorità: P0 · Created: 2026-07-22
Dipendenze: GEM-01 chiuso · Blocca: GEM-03, GEM-06
---

# GEM-02 — MEMORY RUNTIME
## L'ecosistema di memoria che oggi è tre memorie scollegate

> **LEGGI PRIMA:** `GEM-00-INDEX-E-PROTOCOLLO.md` + `GEM-01` (consegna). Questo brief usa `empire.paths`.

---

## 1. IL PROBLEMA MISURATO

ADR-002 impone il pattern **memory-first**: leggi la memoria prima di ogni task, scrivi
checkpoint dopo ogni task. La regola è scritta in `CLAUDE.md` come REGOLA ZERO. Ma sul disco:

| Memoria | Path | Stato reale | Chi la scrive |
|---|---|---|---|
| Memoria aziendale | `company/Memory/` | 113 file, viva. `INDEX.md` + `STATO-EMPIRE.md` + 8 ADR + ~30 checkpoint | Claude e Max, **a mano** |
| Memoria estate (importata) | `DIGITAL-EMPIRE/00-MEMORY/` | 51 file, con `memory_manager.py` CLI | mai usata dopo l'import |
| Memoria estate (riorganizzata) | `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/memory_manager.py` | script presente, **crashava** (risolto in GEM-01 TASK 6) | nessuno |
| Memoria personale Claude | `~/.claude/projects/.../memory/` | 10 file + MEMORY.md | Claude |
| `company/Memory/audit/` | — | **VUOTA** | nessuno |
| `company/Memory/sessions/` | — | **1 file**, del 2026-06-10 | nessuno da 42 giorni |

**Tre conseguenze reali, non teoriche:**
1. Un checkpoint scritto da Gael in `company/Memory/checkpoints/` non è visibile al
   `memory_manager.py` dell'estate, e viceversa. Due storie parallele della stessa azienda.
2. La numerazione dei checkpoint ha già collisionato una volta
   (vedi `CP-20260719-006`: *"collisione numerazione checkpoint (002/003 rinumerati 004/005)"*).
   È un bug strutturale: due persone che scrivono file numerati a mano collidono sempre.
3. Non esiste **ricerca**. `STATO-EMPIRE.md` è un file lungo che si legge dall'alto e cresce
   in testa. Trovare "cosa avevamo deciso su X" significa leggere tutto.

**GEM-02 costruisce UN SOLO runtime di memoria** che scrive in entrambi i posti dove serve,
assegna ID senza collisioni, e rende la memoria interrogabile in un secondo.

---

## 2. SKILL DA USARE (verifica prima — GEM-00 §2)

| Skill | Path | Uso | Fallback |
|---|---|---|---|
| `memory-empire` | `~/.claude/skills/memory-empire/` | **leggila per intero**: definisce l'archiviazione integrale in `knowledge/`, i 5 reparti, il reparto `enrichment-research`. Il runtime deve essere compatibile con quel modello, non alternativo | usa solo lo schema §4 |
| `master-build-architecture` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/` | contiene `scripts/memory_manager.py` — **è il pattern originale wrappato** dall'estate. Leggilo per capire la genealogia | — |
| `sparc-methodology` | `.claude/skills/sparc-methodology/` | SPEC prima del codice | spec = §4-5 |
| `agent-tester` | `~/.claude/skills/agent-tester/` | test su ogni tipo di atomo | unittest |
| `verification-quality` | `.claude/skills/verification-quality/` | gate finale comportamentale | checklist §7 |
| `hooks-automation` | `.claude/skills/hooks-automation/` | il checkpoint automatico post-task (§6 TASK 6) | scrittura manuale documentata |

---

## 3. VINCOLO ARCHITETTURALE — memoria a due livelli, una sola scrittura

```
                      ┌──────────────────────────────┐
   codice/agente ────► │  empire.memory.write(atom)   │
                      └──────────────┬───────────────┘
                                     │  una sola chiamata
                    ┌────────────────┴────────────────┐
                    ▼                                 ▼
   LIVELLO OPERATIVO (append-only, JSONL)   LIVELLO NARRATIVO (Markdown umano)
   empire/.data/memory/atoms.jsonl          company/Memory/checkpoints/CP-*.md
   — machine-readable                       company/Memory/decisions/ADR-*.md
   — indicizzato, cercabile                 company/Memory/STATO-EMPIRE.md (blocco in testa)
   — mai riscritto, solo appeso             — leggibile da Max e Gael senza tool
```

**Regola d'oro:** il livello operativo è la **verità**; il livello narrativo è la **vista**.
Se divergono, si rigenera la vista dagli atomi (`empire mem render`), mai il contrario.

**ADR-003 in azione:** `company/Memory/` non viene ristrutturata. I file esistenti restano dove
sono, nel formato in cui sono. Il runtime li **legge come sorgente storica** (import una tantum)
e da lì in poi ci **scrive dentro nel formato esistente**.

---

## 4. SCHEMA — l'atomo di memoria

Un solo tipo di record, con un campo `kind` discriminante. Riga JSONL:

```json
{
  "id": "CP-20260722-014",
  "kind": "checkpoint",
  "ts": "2026-07-22T14:03:11+02:00",
  "actor": "Gemini",
  "task": "GEM-02-TASK-4",
  "workflow": "WORKFLOW-ESTATE",
  "ecosystem": "10-MEMORY",
  "title": "Memory runtime: CLI e indice",
  "body": "testo integrale, mai troncato",
  "refs": ["ADR-002", "CP-20260722-GEM01"],
  "artifacts": ["empire/memory/store.py"],
  "status": "done",
  "prov": {"owner": "Max", "controller": "Claude", "origin": "FORGE", "governance": "MANDATO Art.8"},
  "hash": "sha256 del body"
}
```

`kind` ammessi (dedotti dai sistemi esistenti, non inventare oltre):
`checkpoint` · `decision` (ADR) · `plan` · `brainstorm` · `error` · `metric` · `pattern`
(ReasoningBank) · `retro` · `perf` (usato da GEM-03) · `feedback` (usato da GEM-03) ·
`session` · `ingestion` (usato da memory-empire) · `audit`.

### Regola anti-collisione ID (risolve il bug reale già avvenuto)
`id = <PREFIX>-<YYYYMMDD>-<NNN>` dove `NNN` è assegnato con **lock su file**:
1. apri `empire/.data/memory/.idlock` in modalità esclusiva (`os.O_CREAT|os.O_EXCL`, con retry
   e timeout 5 s);
2. leggi il massimo `NNN` esistente **sia** in `atoms.jsonl` **sia** scandendo i nomi dei file
   in `company/Memory/checkpoints/`;
3. assegna `max+1`, scrivi, rilascia il lock.

Deve funzionare anche se due processi (Claude e Gemini) scrivono nello stesso secondo.
**Test obbligatorio**: 20 scritture concorrenti via `concurrent.futures` → 20 ID distinti, zero perdite.

---

## 5. ARCHITETTURA RICHIESTA

```
empire/memory/
├── __init__.py         # API pubblica: write, read, search, render, migrate
├── model.py            # dataclass Atom + validazione kind/campi obbligatori per kind
├── store.py            # JSONL append-only + lock ID + hash + rotazione a 50 MB
├── render.py           # Atom → Markdown nel formato ESISTENTE di company/Memory/
├── ingest.py           # import una tantum dei 3 sistemi legacy → atoms.jsonl
├── search.py           # ricerca full-text (indice invertito stdlib, no dipendenze)
├── state.py            # genera/aggiorna il blocco in testa a STATO-EMPIRE.md
├── cli.py              # sottocomandi di `python -m empire mem ...`
└── tests/
    ├── test_store.py       # incluso il test di concorrenza
    ├── test_render.py      # round-trip: atom → md → parse → atom identico
    ├── test_ingest.py
    └── test_search.py
```

### 5.1 `render.py` — il punto delicato
Deve produrre Markdown **indistinguibile** da quello che Claude scrive oggi a mano. Prima di
implementare: leggi 5 checkpoint reali in `company/Memory/checkpoints/` + i template in
`company/Memory/templates/` ed estrai il formato **osservato**, non quello che ti aspetti.
Test di round-trip obbligatorio: `parse(render(atom)) == atom` su tutti i `kind`.

### 5.2 `ingest.py` — migrazione storica, una sola volta
Sorgenti da importare in `atoms.jsonl`:
1. `company/Memory/checkpoints/*.md` → kind `checkpoint`
2. `company/Memory/decisions/ADR-*.md` → kind `decision`
3. `company/Memory/sessions/*.md` → kind `session`
4. `company/Memory/BACKLOG.md` (una riga = un atomo) → kind `plan`, status `open`
5. `DIGITAL-EMPIRE/00-MEMORY/**` → tutti i kind, marcando `source: estate`
6. `company/Memory/STATO-EMPIRE.md` → **ogni blocco `##` diventa un atomo** con la sua data.
   È il file più informativo del repo: contiene ordini di Max, decisioni, riprese. Va spezzato.

`--dry-run` obbligatorio: stampa quanti atomi per kind **senza scrivere**. Solo dopo che Max
guarda i numeri, si esegue davvero. Idempotente: rieseguire non duplica (dedup su `hash`).

### 5.3 `cli.py` — comandi
```
python -m empire mem write --kind checkpoint --task GEM-02 --title "..." --body "..." [--refs ADR-002]
python -m empire mem read <ID>
python -m empire mem list --kind decision --since 2026-07-01
python -m empire mem search "prezzo manuale"        # < 1 s su tutto il corpus
python -m empire mem status                          # conteggi per kind, ultimo atomo, salute
python -m empire mem render --id CP-20260722-014     # rigenera il .md dalla verità
python -m empire mem state                           # aggiorna il blocco in testa a STATO-EMPIRE.md
python -m empire mem ingest [--dry-run]
python -m empire mem recall --task "outreach"        # cosa devo sapere prima di lavorare su X
```

`mem recall` è il comando che implementa **ADR-002 memory-first** in modo eseguibile: dato un
argomento, restituisce in ordine di rilevanza: ADR attivi che lo toccano, ultimi 3 checkpoint
correlati, errori noti, pattern ReasoningBank confermati. Massimo 40 righe. È il comando che un
agente esegue **prima** di iniziare, invece di leggere 1267 file.

---

## 6. SEQUENZA — task dopo task

**TASK 1 — Ricognizione.** Verifica skill (§2). Leggi `memory-empire/SKILL.md` per intero,
`ADR-002`, `company/Memory/templates/`, 5 checkpoint reali, `STATO-EMPIRE.md` (tutto).
Output: `empire/memory/SPEC.md` con il formato **osservato** dei checkpoint, documentato campo
per campo. **Gate 1**: la SPEC contiene un esempio reale copiato dal repo, non inventato.

**TASK 2 — `model.py` + `store.py`.** Atomo, validazione, append JSONL, lock ID.
**Gate 2**: test di concorrenza 20 scritture parallele → 20 ID unici. Incolla l'output.

**TASK 3 — `render.py`.** Round-trip su tutti i kind.
**Gate 3**: `render()` di un atomo importato da un checkpoint reale produce un file
**byte-identico o diverso solo per whitespace** rispetto all'originale. Incolla il `diff`.

**TASK 4 — `ingest.py` + `search.py`.** Prima `--dry-run`, mostra i numeri, poi esegui.
**Gate 4**: `mem search "prezzo manuale"` trova gli atomi relativi a B-003/DEC-EST-001
(sappiamo che esistono: sono in BACKLOG e in STATO-EMPIRE) in **< 1 secondo**. Incolla tempo.

**TASK 5 — `state.py` + `cli.py`.**
**Gate 5**: `mem recall --task "empiredesk"` restituisce ≤40 righe che includono l'ordine di Max
del 2026-07-21 sera sulla divisione Max/Gael. Se non lo trova, l'indicizzazione è insufficiente.

**TASK 6 — Automazione (usa `hooks-automation`).**
Crea `empire/memory/hooks/post_task.py`: dato un task chiuso, scrive l'atomo `checkpoint` e
aggiorna `STATO-EMPIRE.md` **senza intervento umano**. Documenta in
`company/Antigravity-Briefs/consegne/GEM-02-HOOK-SETUP.md` come agganciarlo a Claude Code
(`.claude/settings.json`, evento post-task) — **documenta, non modificare `settings.json`**:
quella è una modifica che approva Max.
**Gate 6**: il hook eseguito a mano produce un atomo + aggiorna il file. Incolla il diff.

**TASK 7 — Chiusura.** `empire/memory/README.md`, registrazione in `REGISTRO-IMPRESA.md`,
checkpoint `CP-20260722-GEM02` (scritto **con il runtime stesso** — è la prova finale),
consegna nel formato GEM-00 §4.

---

## 7. DEFINITION OF DONE

- [ ] DoD-1 — `mem write` + `mem read` round-trip perfetto su tutti i 13 `kind`
- [ ] DoD-2 — 20 scritture concorrenti → 20 ID distinti, zero collisioni (output incollato)
- [ ] DoD-3 — `mem ingest` importa **tutti** i checkpoint esistenti; conteggio = numero file su disco
- [ ] DoD-4 — `mem ingest` eseguito 2 volte → zero duplicati (dedup su hash, dimostrato)
- [ ] DoD-5 — `mem search` su tutto il corpus in < 1 s
- [ ] DoD-6 — `mem recall --task X` produce ≤40 righe rilevanti su 3 argomenti diversi provati
- [ ] DoD-7 — nessun file esistente in `company/Memory/` cancellato o riformattato (`git status` incollato)
- [ ] DoD-8 — `render()` produce Markdown conforme al formato osservato (diff incollato)
- [ ] DoD-9 — il checkpoint di chiusura di GEM-02 è stato scritto **usando il runtime**
- [ ] DoD-10 — zero crash Unicode su Windows, da 3 CWD diversi
- [ ] DoD-11 — pytest ≥ 25 test verdi
- [ ] DoD-12 — compatibile con `memory-empire`: archiviazione integrale, **mai riassunti**

---

## 8. ANTI-PATTERN

| Anti-pattern | Perché rifiutato |
|---|---|
| Riassumere il body di un atomo | `memory-empire` impone archiviazione **integrale**. Un riassunto perde l'informazione per sempre. |
| Ristrutturare `company/Memory/` | ADR-003. Claude e Max ci lavorano ogni giorno. |
| Sostituire `STATO-EMPIRE.md` con un DB | È il file che Max legge. Resta Markdown, resta leggibile a occhio. |
| ID assegnati con `len(files)+1` | È esattamente il bug che ha già causato la collisione 002/003. Serve il lock. |
| Aggiungere SQLite/Chroma/embedding | Non ora. JSONL + indice invertito stdlib. Se un giorno servirà semantica, sarà un ADR. |
| Scrivere in `~/.claude/projects/.../memory/` | È la memoria personale di Claude. Non toccarla. |
| Modificare `.claude/settings.json` per il hook | Lo approva Max. Tu documenti il come. |

---

## 9. HANDOFF

Sblocca **GEM-03** (Ispettorato): i kind `perf` e `feedback` sono già nello schema, GEM-03 li
riempie. E **GEM-06** (Workflow Engine): userà `mem write` per ogni gate attraversato.

A Claude: l'esito del `--dry-run` di `ingest` — se emergono contraddizioni tra i tre sistemi di
memoria (es. due decisioni opposte sullo stesso tema), **non risolverle**: elencale. Le risolve
Max con un ADR.
</content>
