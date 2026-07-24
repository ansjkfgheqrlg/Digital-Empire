# CS04 — I 4 Bug Reali di Phase 9 (Cosa Insegna l'End-to-End Test)

> **Setting**: Phase 9, sub-phase 9.8 (regression test su sorgenti reali dell'utente)
> **Personaggi**: io che testo, lo schema validator che fallisce in modi sorprendenti, pytest che cattura regression
> **Esito**: 4 bug scoperti in sequenza, fixati in mezza giornata, ognuno con test pytest dedicato
> **Lezione cardine**: i bug più costosi sono quelli che NON emergono in unit test ma in end-to-end test reali. Investi nel test reale prima di ogni release.

---

## 1. Il contesto

Phase 9 stava per concludersi. Avevo:
- 5 nuovi agenti optimizer (O1-O5)
- Schema tightened a v0.3
- 5 builder updated con "Depth Awareness"
- C3 potenziato con nuovi check Phase 9
- 13 nuovi test pytest (totale 69 verdi)

Sub-phase 9.8 era il regression test: ri-eseguire il pipeline sui 2 sorgenti reali dell'utente e misurare miglioramento v1.0 → v1.1.

Mi sentivo confident. Tutti i test pytest passavano. Schema validi. CLI funzionanti. Dovevo solo confermare con run reali.

Mi sbagliavo. In sequenza ho scoperto 4 bug. Ognuno mi ha insegnato qualcosa di diverso. Li racconto in ordine cronologico.

---

## 2. Bug-9.1 — Schema validator non rilevava agenti con nomi custom

### Come l'ho scoperto

Dopo aver costruito Test #1 v1.1 (`beast-preventivi` con 4 agenti aggiunti: discovery, pricing, qa, humanizer), ho fatto:

```bash
python3 scripts/schema_validator.py --target skill --output-dir test1-skill-v1.1/beast-preventivi
```

Output atteso: PASS (gli agenti c'erano, tutti con 7/7 file canonici).
Output reale: `phase9_issues_found: 0` — ma anche `agents_analyzed: 0`. Cioè: lo schema validator **non aveva trovato gli agenti per nulla**.

### Indagine

Sono andato a leggere `run_phase9_checks()` in `schema_validator.py`:

```python
def run_phase9_checks(target: str, output_dir: Path) -> list[dict]:
    all_issues = []

    # Trova tutte le skill
    skill_mds = list(output_dir.rglob("SKILL.md"))
    for skill_md in skill_mds:
        all_issues.extend(check_skill_min_references(skill_md.parent))

    # Trova tutti gli agenti
    agent_mds = list(output_dir.rglob("agent.md"))  # ← BUG QUI
    for agent_md in agent_mds:
        all_issues.extend(check_agent_canonical_files(agent_md.parent))

    return all_issues
```

Cercava `agent.md` come **filename letterale**. Ma i miei agenti reali si chiamavano:
- `discovery-agent.md`
- `pricing-agent.md`
- `copy-reviewer.md`
- `humanizer-agent.md`

Nessuno era `agent.md` puro. **Zero match → zero issue → falso PASS**.

### Cosa avevo assunto (erroneamente)

Quando avevo scritto lo schema, pensavo che il "main file" di un agente fosse sempre `agent.md`. Era così nei miei template di esempio. Nella realtà, i builder spesso producono agenti con nomi descrittivi.

### Il fix

Heuristics multiple per discovery agenti:

```python
# Heuristic 1: file 'agent.md' puro
for f in output_dir.rglob("agent.md"):
    found_agent_dirs.add(f.parent)

# Heuristic 2: file *-agent.md (Phase 9 convention)
for f in output_dir.rglob("*-agent.md"):
    found_agent_dirs.add((f.parent, f.stem))

# Heuristic 3: file con frontmatter agent_id dentro 'agents/' folder
for f in output_dir.rglob("*.md"):
    # ... check frontmatter ...
```

### Lezione

**Le tue assunzioni sui filename sono spesso sbagliate.** Quando i tuoi test usano sempre `agent.md` puro, sembra che lo schema funzioni. Real-world usage usa nomi descrittivi.

Pattern: **per ogni assunzione strutturale, fa esempio reale che la valida**. Se tutti i tuoi esempi seguono la stessa convention, non hai testato la convention — hai testato il copy-paste.

---

## 3. Bug-9.2 — Single-file convention con companions non riconosciuta

### Come l'ho scoperto

Dopo fix di Bug-9.1, lo schema validator trovava `discovery-agent.md`. Ma poi diceva: **2/7 file canonici presenti**.

Strano. Avevo creato tutti i 7 file. Ho fatto `ls`:

```
agents/operativi/
├── discovery-agent.md
├── discovery-agent.system_prompt.md
├── discovery-agent.tools.md
├── discovery-agent.playbook.md
├── discovery-agent.failure_modes.md
├── discovery-agent.eval_cases.json
└── discovery-agent.README.md
```

Tutti e 7 presenti. Convention: `<slug>.<canonical-file>`. Lo schema cercava... qualcos'altro.

### Indagine

`check_agent_canonical_files()` cercava:

```python
canonical = ["agent.md", "system_prompt.md", "tools.md", "playbook.md",
             "failure_modes.md", "eval_cases.json", "README.md"]
present = [f for f in canonical if (agent_dir / f).exists()]
```

Cercava esattamente i file chiamati `system_prompt.md`, `tools.md`, ecc. — non `discovery-agent.system_prompt.md`.

**Convention diversa** dal mio template:
- Template prevedeva: cartella `<agent-name>/` con dentro file generici (agent.md, system_prompt.md, tools.md, ...)
- Convention reale: file `<agent-name>.<canonical>` come single-file con companions

Entrambe valide. Lo schema gestiva solo la prima.

### Il fix

Nuova funzione `check_agent_canonical_files_single_file()`:

```python
def check_agent_canonical_files_single_file(agent_dir, slug, min_files=5):
    canonical_suffixes = [".md", ".system_prompt.md", ".tools.md",
                          ".playbook.md", ".failure_modes.md",
                          ".eval_cases.json", ".README.md"]
    present = [s for s in canonical_suffixes if (agent_dir / f"{slug}{s}").exists()]
    # ... check counts e content minimums
```

Discovery agents ora restituiva tuple `(agent_dir, slug)` invece che solo `agent_dir`, così la function sapeva quale slug usare per le suffix.

### Lezione

**Una convention nei tuoi template non è una convention nel codice.** Avevo scritto la convention "cartella + file generici" nei miei template di esempio. Poi avevo costruito agenti reali in convention diversa (single-file + companions). Lo schema validator non era stato adattato.

Pattern: quando esistono 2+ convention valide per la stessa cosa, il validator deve gestirle entrambe. Non puoi obbligare 1 convention senza documentazione + enforcement esplicito.

---

## 4. Bug-9.3 — Filtro path "phase" troppo permissivo

### Come l'ho scoperto

Avevo aggiunto 13 nuovi test pytest in `test_phase9_checks.py`. Tutti passavano tranne uno:

```
tests/test_phase9_checks.py::test_run_phase9_checks_finds_thin_agent FAILED
```

Stranissimo. Il test era:

```python
def test_run_phase9_checks_finds_thin_agent(tmp_path):
    agent_dir = tmp_path / "my-agent"
    _create_agent(agent_dir, ["agent.md", "system_prompt.md"])  # solo 2/7 file
    issues = run_phase9_checks("agent", tmp_path)
    assert len(issues) >= 1  # → AssertionError: 0 >= 1
```

Doveva trovare l'agente thin (solo 2/7 file) e generare almeno 1 issue. Invece restituiva zero issue.

### Indagine

Ho aggiunto print statement:

```python
print(f"Test path: {tmp_path}")
print(f"Issues found: {len(issues)}")
```

Output:
```
Test path: /tmp/pytest-of-user/pytest-1/test_run_phase9_checks_finds_t0
Issues found: 0
```

Path conteneva "pytest". E nel mio schema validator avevo:

```python
# Skip se è dentro phase7-run o packaged-final
if "phase" in str(agent_md) or "packaged" in str(agent_md):
    continue
```

`"phase" in str("test_run_phase9_checks_finds_t0")` → **True**! Perché il nome del test stesso contiene "phase9".

Lo schema validator scartava il path durante test, pensando fosse un artefatto di test/build da escludere.

### La trappola cognitiva

Il filtro era ben intenzionato: volevo escludere cartelle tipo `phase7-run/` o `phase9-regression/` o `packaged-final/` (dove le skill di test/regression non dovevano essere validate).

Ma `"phase" in str(path)` era troppo permissivo. Matchava anche:
- `pytest-of-user/pytest-1/test_run_phase9_checks_finds_t0` (test paths)
- `/Users/me/myphone/projects/...` (improbabile ma esiste)
- Qualsiasi path che casualmente contenesse "phase"

### Il fix

Regex stringente:

```python
import re
if re.search(r"/(phase\d+-(run|regression)|packaged-final)/", str(agent_md)):
    continue
```

Match solo:
- `/phase{N}-run/`
- `/phase{N}-regression/`
- `/packaged-final/`

E nessun altro path con "phase" o "packaged" come substring casuale.

### Lezione

**`"x" in str(path)` è quasi sempre la soluzione sbagliata per filtri path.** Usa regex o `pathlib.Path.parts` invece. Substring match è troppo permissivo nei test (dove i nomi dei test stessi possono catturare la substring).

Pattern: quando filtri path, **rendi esplicita la struttura attesa** (con regex o parts), non solo la substring.

Bonus lezione: questo bug ha richiesto che il test stesso potesse fail. Senza il test, sarebbe stato silent in produzione e gli agenti thin sarebbero passati silently.

---

## 5. Bug-9.4 — Mancava check "complex-skill-no-agents"

### Come l'ho scoperto

Tutti i bug precedenti fixati. Ho rifatto il run di validazione su Test #1 baseline v1.0 (`beast-preventivi`, la skill scaffold-y senza agenti).

Output: **PASS** (Verdict, Errors: 0, Warnings: 0, Phase 9 issues: 0).

Ma aspetta. L'utente aveva esplicitamente segnalato come bug: "questa skill non ha agenti interni!". E lo schema validator stava dicendo: tutto a posto?

### Indagine

Lo schema v0.3 controllava:
- ✅ `references_min_files: 3` → la skill aveva 8 reference, OK
- ✅ `evals_min_count: 4` → aveva evals.json con 6 cases, OK
- ✅ frontmatter required keys → presenti
- ✅ skill_md ≤500 lines → OK
- ✅ description pushy markers ≥3 → OK

Niente di sbagliato strutturalmente. Era una skill **strutturalmente valida ma operativamente magra** (mancavano agenti che facessero il lavoro).

Il check "deve avere agenti" semplicemente **non esisteva**. Ovviamente non esisteva — non l'avevo scritto.

### La domanda meta

"OK ma quando una skill deve avere agenti?". Non sempre. Una skill semplice (es. format converter) può non averne. Quando è "complex enough" da meritarli?

### Il fix (con heuristic)

Ho aggiunto `check_complex_skill_has_agents()`:

```python
def check_complex_skill_has_agents(skill_dir):
    refs_dir = skill_dir / "references"
    stages_dir = refs_dir / "stages"
    processes_dir = refs_dir / "processes"

    is_complex = False
    reason = ""
    if stages_dir.exists() and len(list(stages_dir.glob("*.md"))) >= 3:
        is_complex = True
        reason = f"{len(...)} stages → multi-stage pipeline"
    elif processes_dir.exists() and len(list(processes_dir.glob("*.md"))) >= 2:
        is_complex = True
        reason = f"{len(...)} processes → multi-process workflow"

    if not is_complex:
        return []  # skill semplice, no agenti necessari

    agents_dir = skill_dir / "agents"
    if not agents_dir.exists() or len(list(agents_dir.rglob("*.md"))) == 0:
        return [{
            "id": f"complex-skill-no-agents-{skill_dir.name}",
            "severity": "warning",
            "evidence": f"{skill_dir.name}: complex skill ({reason}) ma senza agenti interni.",
            "fix_hint": "Considera di aggiungere agents/ con: 1 agente operativo per stage..."
        }]
    return []
```

**Heuristic**: una skill è "complex" se:
- Ha ≥3 file in `stages/` (multi-stage pipeline), oppure
- Ha ≥2 file in `processes/` (multi-process workflow)

Per skill complex senza agenti: warning (non error). Era judgment soft, non bloccante.

### Re-test

Run di Test #1 baseline v1.0:
- Verdict: **WARN** (non più PASS)
- Phase 9 issues: 1
- Issue: `complex-skill-no-agents-beast-preventivi`
- Evidence: "beast-preventivi: complex skill (4 stages → multi-stage pipeline) ma senza agenti interni."

Bug catchato. Esattamente quello che l'utente aveva segnalato manualmente.

### Lezione

**Le tue "regole obvious" non sono nello schema finché non le scrivi.** L'utente aveva detto "una skill complessa deve avere agenti". Era ovvio. Non era nello schema. Quindi il validator non lo controllava.

Pattern: per ogni feedback qualitativo che ti dà l'utente ("ho notato che X non ha Y"), chiediti: posso codificarlo come check meccanico? Se sì, fallo subito. Diventa permanent.

---

## 6. La cronologia dei 4 bug (in mezza giornata)

| Tempo | Bug | Tempo per fix | Test aggiunto |
|---|---|---|---|
| T+0 | Inizio regression test Phase 9.8 | — | — |
| T+30min | Bug-9.1 scoperto (agent.md non trovato) | 15 min | test_agent_with_custom_name |
| T+1h | Bug-9.2 scoperto (single-file convention) | 20 min | test_agent_single_file_convention |
| T+2h | Bug-9.3 scoperto (pytest path filter) | 10 min | (test esistente già falliva) |
| T+3h | Bug-9.4 scoperto (complex-skill-no-agents check) | 25 min | test_complex_skill_warns |
| T+4h | Regression test completo PASS | — | — |

4 bug + 4 test in 4 ore. Senza, sarebbero emersi in produzione (presso utenti reali, mesi dopo).

---

## 7. Le 5 lezioni macro estratte dai 4 bug

### Lezione 1 — End-to-end test reali catturano bug che unit test mancano

I 56 test pytest pre-Phase 9 passavano. I 4 bug sopra **non erano coperti da nessun test**. Erano latenti.

Solo l'end-to-end test (Phase 9.8) li ha esposti. Pattern: **investi in test reali con dati reali prima di ogni release maggiore**. Sono 1 ora di setup, salvano settimane di bug-hunting post-release.

### Lezione 2 — Ogni bug fixato → test aggiunto è disciplina, non opzionale

Per i 4 bug, ho aggiunto 3 nuovi test pytest immediatamente (Bug-9.3 già aveva un test failing). Tutti i futuri run del validator catturano regression su questi casi.

Senza test: 6 mesi dopo qualcuno modifica `schema_validator.py`, reintroduce uno dei bug, nessuno se ne accorge fino a quando non emerge in produzione.

Pattern: **"bug found + bug fixed + test added"** è il triplet. Saltare il "test added" è debt mascherato.

### Lezione 3 — Le assumptions cognitive sono il primo nemico

Tutti e 4 i bug venivano da assunzioni:
- Bug-9.1: "il main file di un agente è `agent.md` letterale"
- Bug-9.2: "agents sono cartelle con file generici dentro"
- Bug-9.3: "i miei path di skip sono solo path skip reali"
- Bug-9.4: "se una skill è complex, il builder aggiungerà agenti"

Tutte sembravano ovvie. Tutte erano sbagliate in contesti reali.

Pattern: per ogni assumption del tuo codice, **chiediti se hai dato per scontato qualcosa**. Spesso sì. Esplicita.

### Lezione 4 — Schema permissivo è il primo posto dove guardare bug

Quando un bug emerge ("output sembra incompleto ma validator passa"), il primo sospetto è: lo schema permette troppo. Quasi sempre è vero.

Pattern v0.1 (`additionalProperties: true`, niente `required`, niente content minimums) è scaffold-permissive per definizione. Tightening è work continuo.

### Lezione 5 — Bug heuristic vs Bug strutturali

I 4 bug erano misti:
- Bug-9.1, 9.2: **strutturali** (logica sbagliata)
- Bug-9.3: **heuristic** (filtro troppo permissivo)
- Bug-9.4: **mancante** (check non implementato)

Tipi diversi di bug richiedono fix diversi:
- Strutturali → riscrivi logica
- Heuristic → tighten regex/conditions
- Mancanti → aggiungi nuovo check

Pattern: quando hai bug, **categorizzalo** prima di fixare. Il fix sbagliato per il tipo sbagliato peggiora il problema.

---

## 8. I numeri di chiusura Phase 9

Dopo i 4 fix:
- Pytest: 56 → **69 verdi** (+13 nuovi)
- Schema validator: cattura ora 4 categorie nuove di bug
- Test #1 baseline v1.0: era PASS falsa, ora WARN (corretto)
- Test #2 baseline v1.0: era passing su 6 sub-skill thin, ora FAIL con 31 issues (corretto)
- Test #1 v1.1: PASS reale (4 agenti aggiunti, 7/7 file canonici)
- Test #2 v1.1: PASS reale (101 file totali, sub-skill ricche, agenti completi)

Phase 9 chiusa. v1.1 packaged. 4 bug **non sono** arrivati in produzione perché trovati in test.

---

## 9. Connessioni con altri principi/pattern

- **Esemplifica**: P09 (Failure Modes First-Class) — i 4 bug sono failure modes catturati durante development
- **Esemplifica**: PT06 (Schema Tightening Loop) — Bug-9.4 è esattamente un caso di "tighten dopo evidence"
- **Esemplifica**: P10 (Self-Improvement Loops) — questi bug sarebbero stati ricoperti da SI1/SI2/SI3 se fossero emersi in produzione
- **Si ricollega a**: CS02 (Optimizer Team) — quel case study mostra Phase 9 dal lato "feature design"; questo case study mostra Phase 9 dal lato "bug discovery"
- **Lezione comune**: con CS01/CS02/CS03 — feedback esterno (utente, test reale, validator) > self-assessment

---

## Appendice — i 4 bug come tabella riassuntiva

| Bug | Tipo | Causa | Fix | Test aggiunto |
|---|---|---|---|---|
| **9.1** | Strutturale | `rglob("agent.md")` cercava filename letterale | Multi-heuristic discovery (*-agent.md, agents/ folder, frontmatter agent_id) | test_finds_custom_named_agents |
| **9.2** | Strutturale | Single-file convention non gestita | Nuova funzione `check_agent_canonical_files_single_file()` con suffix matching | test_single_file_convention_validates |
| **9.3** | Heuristic | `"phase" in str(path)` troppo permissivo (catch pytest paths) | Regex stringente: `r"/(phase\d+-(run|regression)|packaged-final)/"` | (test esistente già falliva) |
| **9.4** | Mancante | Nessun check per "skill complessa senza agenti" | Nuova funzione `check_complex_skill_has_agents()` con heuristic stages≥3 OR processes≥2 | test_complex_skill_warns |
