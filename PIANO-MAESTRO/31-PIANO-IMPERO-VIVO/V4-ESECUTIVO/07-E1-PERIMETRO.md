# 07 — E1: IL PERIMETRO PULITO

> Chi: **EMPERATOR** (solo, un commit per coppia) · Ore V3: 13-20 · Tetto: 30 · Dipende da: **E0.7
> solo per H7 e H11** (`06-E0.7-HOOK.md` §0: se H11 — lo scanner di chiavi in commit — è fermo, E1
> non parte: 32 commit manuali su un repo pubblico senza scanner sarebbero la recidiva numero
> quattro) e dalla **decisione 2** (albero canonico, default `DIGITAL-EMPIRE/`, V2 §26) ·
> Percorsi in scrittura: `company/Ecosistemi/04-MARKETING/**` (19 coppie), `company/Ecosistemi/07-FORGE/Agenti/`
> + `company/Genesi-Core/FORGE/Agenti/` (10 coppie), `.claude/agents/{cc-master,cf-conductor,chief-forge}.md`
> + `company/Board-CSuite/Chief-Forge/agenti/cf-conductor.md` + `DIGITAL-EMPIRE/04-AGENTS/chief-forge/chief-forge.md`
> + `~/.claude/agents/cc-master.md` (3 coppie), `company/**/archivio-origine/` (da creare, una per
> ecosistema toccato), `company/Backbone/Identity-HR/registro-agenti.yaml` (6 voci), `empire/registry/census.py`
> (una definizione + un `set`), `scripts/empire-sync.ps1` (3 righe), `company/Memory/.SYNC-SOSPESO`
> (sentinella, da creare e poi cancellare), `WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/preventivo-template.md:10`
> (un link), `company/Memory/decisions/ADR-0NN-albero-canonico.md` (da creare) · Politica di guasto:
> **fail-closed per fusione** (mai committare lo stato misto: una coppia = un commit atomico o
> niente), rientro con `git reflog` + `git checkout`
> STATO: COMPLETO (EMPERATOR, 2026-09-11 — scritto a mano, un documento per volta)

**Cosa fa questo scaglione, in una riga:** fa sì che ogni agente dell'Impero esista **in una copia
sola** dentro il perimetro che i contatori guardano — così che E2 (la rinomina che vale quaranta
punti) lavori su 407 nomi veri e non su 439 file con 32 doppioni divergenti, e che `forge scan` e
`registry census` contino **gli stessi id**. Senza E1, E2 riscriverebbe da zero contratti che in
casa esistono già, perfetti, in un'altra cartella (censimento 03a, Bomba 2).

**Il disco ha smentito il piano su quattro punti, e V4 li corregge qui (tutti misurati l'11/09):**

1. **Le coppie sono 32, non 36.** `dati/censimento-03a-popolazione.md:585-595`: 36 nomi doppi,
   ma 4 sono corredo generico (`memory`, `playbook`, `system-prompt`, `tools`), non agenti. **32
   duplicati divergenti veri**: 19 in 04-MARKETING (radice ↔ reparto), 10 in FORGE
   (`Ecosistemi/07-FORGE` ↔ `Genesi-Core/FORGE`, la copia buona è quella **invisibile a forge**),
   3 a cavallo fra scheda e agente eseguibile (`cc-master`, `cf-conductor`, `chief-forge`).
2. **`registry dupes` conta lo stesso file due volte.** `python -m empire registry dupes` (11/09):
   1.669 «gruppi identici», ma in `empire/.data/duplicates.json` **71 gruppi dentro `company/`
   hanno lo stesso percorso ripetuto due volte** (es. `company/01-agency/site-audit/PIANO-RESTYLING-2026-09-02.md`
   × 2). La causa è a monte: `dupes.py:25` itera gli `artifacts` del census, e il census produce
   lo stesso artefatto due volte. **Il numero 1.669 non è una misura**: il passo 2.6 ripara il
   census (dedup per percorso) e solo dopo `dupes` torna leggibile. Inoltre: **0 gruppi hanno una
   copia in `DIGITAL-EMPIRE/` E una in `WORKFLOW-ESTATE/`** — la decisione 2 non serve a fondere
   file identici fra i due alberi (non ce ne sono), serve alle 3 coppie a cavallo e a E5b.
3. **I numeri di partenza sono cambiati da V2:** `verify-agents.py` → **6 FAIL** (V2: 7), tutti
   dello stesso tipo: `conoscenza-empire` + i 5 `tesoreria-*` «non censiti in
   `registro-agenti.yaml`»; `verify-skills.py` → **0 FAIL** (V2: 3, già chiusi); `empire doctor` →
   **block 2, warn 3, info 43** (V2: warn 2). I due block: `LINK-DEAD` in
   `WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/preventivo-template.md:10` (riferimento a
   `Clienti/Prof Autocad/preventivo-forge/templates/preventivo.html`, inesistente) e `ADR-001`
   «numero di ecosistema duplicato 08» — **quest'ultimo è il passo 2.10 di E0.5**, non di E1.
4. **`registry census` non è rotto: conta 70 agenti** (`census.json`: `agent: 70` su 22.047
   artefatti) perché `_determine_kind` (`census.py:163-164`) marca «agent» **per percorso**
   (`/04-agents/`, `/agenti/`, prefissi `AGENTE-`/`agent-`) ed esclude `.claude/`; `forge scan`
   conta 439 file per un altro criterio. Il gate di V1 («stesso numero») non può passare
   **finché la definizione di "agente" non è una sola** — è il passo 2.6, prima del gate.

**Il «daemon di sync» ha un nome e un interruttore:** non è un processo separato, è l'hook
`Stop` di Claude Code (`.claude/settings.json:152`) che lancia `scripts/empire-sync.ps1 -Mode push`
a ogni fine turno **di ogni sessione**, sul PC di Max e su quello di Gael. Sospenderlo = una
sentinella su disco che lo script legge (passo 2.1), **non** un edit di `settings.json` (che le
altre sessioni non vedrebbero fino al riavvio).

---

## 0. Cosa NON è bloccato da questo scaglione (ADR-028)

Se E1 si ferma (H11 non pronto, decisione 2 in sospeso, una fusione a metà), **procede comunque
tutto questo**:
- **E0a, E0.5, E0b, E0.9, E0.6, E0.7 (gli altri 11 hook), F3, E3.0, E3**: nessuno legge le 32
  coppie né i contatori del census. Verificato: `01`-`06`, `09`-`11` non citano `04-MARKETING/Agenti`
  né `Genesi-Core`.
- **La fetta verticale (E3) e Preventa**: usano agenti di `Outreach/`, fuori dalle coppie.
- **Il lavoro quotidiano di chiunque nel repo, tranne dentro le cartelle delle coppie**: la
  sospensione del sync (2.1) ferma solo i **push automatici**; commit locali e pull continuano, e
  la sospensione dura **una sessione di E1 per volta** (si accende all'inizio, si spegne alla fine
  della giornata di lavoro, mai lasciata accesa di notte — passo 2.9).
- **LANCI v4** (esecutore Gael — **non dipende da Gael**: E1 non gli chiede niente; il solo effetto
  su di lui è che, nelle ore di E1, il suo hook `Stop` non pusha: lo vede nel log dello script,
  riga «sync sospeso», e pusha a mano se ha fretta — `git push`, nessun rebase pendente).

**Cosa aspetta E1:** **E2** (lavora sui nomi puliti) e, a valle, **E5a/E5-bis/E7**. Nient'altro.

**Cosa NON fa E1**, dichiarato: non scrive contratti (E2), non tocca gli 81 gruppi di file
identici che coinvolgono `company/` (sono `.txt`/`.json`/`.py` di archivi interni, non agenti: si
misurano in 2.6 e passano a E2/E5b con la lista), non sana il doppio `08` (E0.5 2.10), non decide
il perimetro `fonte=scheda`/`fonte=esecutore` (E5-bis), non cancella **niente** (L1: la perdente
va in `archivio-origine/`, stato ARCHIVIO, L8).

---

## 1. Prerequisiti — verificati con un comando, non dichiarati

| # | Prerequisito | Comando | Output atteso | Exit |
|---|---|---|---|---|
| P1 | H11 (scanner chiavi) è attivo nel pre-commit | `echo "OPENROUTER_API_KEY=sk-or-v1-0000000000" > /tmp/finta.env && git add -N /tmp/finta.env 2>/dev/null; python .githooks/check_secrets.py --file /tmp/finta.env; echo $?` (forma esatta in `06-E0.7-HOOK.md` 2.6) | `RESPINTO` e exit **1** | 1 |
| P2 | H7 (checkpoint solo coniati) è attivo | `python .githooks/check_memory.py` con un file `company/Memory/checkpoints/CP-20260911-999.md` finto → | `problemi`, non `avvisi`; exit 1 (poi si cancella il finto) | 1 |
| P3 | La radice è pulita (V2 §21-E1 «radice pulita prima di iniziare») | `git status --porcelain \| wc -l; ls SYNC-CONFLICT.txt 2>/dev/null; git rebase --show-current-patch 2>&1 \| head -1` | `0` · nessun `SYNC-CONFLICT.txt` · `fatal: No rebase in progress` (o equivalente) | 0 |
| P4 | Le 32 coppie sono ancora 32 (il censimento è del 06/09: si rimisura) | `python - <<'PY'` … lo script di 03a: per ogni file in `company/Ecosistemi/04-MARKETING/Agenti/*.md`, `…/Reparti/*/Agenti/*.md`, `company/Ecosistemi/07-FORGE/Agenti/*.md`, `company/Genesi-Core/FORGE/Agenti/*.md`, `.claude/agents/*.md`, `company/Board-CSuite/*/agenti/*.md`, `DIGITAL-EMPIRE/04-AGENTS/*/*.md`, `~/.claude/agents/*.md`: nome minuscolo senza estensione → lista; stampare i nomi con >1 file e i loro sha256 | **32** nomi (19 + 10 + 3), tutti con sha256 **diversi** fra le copie | 0 |
| P5 | I 6 FAIL di verify-agents sono solo «non censito» | `python scripts/verify-agents.py \| grep "FAIL  \["` | 6 righe, tutte `non censito in registro-agenti.yaml` (11/09) | 1 |
| P6 | verify-skills è già verde | `python scripts/verify-skills.py; echo $?` | `0 FAIL`, exit 0 | 0 |
| P7 | I due block di doctor sono quelli noti | `python -m empire doctor \| grep "^\[BLOCK\]"` | esattamente 2 righe: `LINK-DEAD …preventivo-template.md:10` e `ADR-001 …company/Ecosistemi` | 1 |
| P8 | Il census gira e conta 70 «agent» per percorso | `python -m empire registry census \| grep -E "agent|ecosystem"` · `python -c "import json,collections;a=json.load(open('empire/.data/census.json'))['artifacts'];print(len(a),len({x['path'] for x in a}))"` | `agent : 70` · **due numeri diversi** (22.047 artefatti, meno percorsi distinti: è il doppio conteggio del punto 2) | 0 |
| P9 | Il perimetro di `forge scan` è 439 (o il numero del giorno) | `python -m empire forge scan \| tail -3` | `61/439` OPERATIVO (05/09, `30-PIANO-COMPLETAMENTO-IMPERO.md:39`) — si scrive il numero del giorno | 0 |
| P10 | Il regolo di fusione ha uno strumento: `forge` misura un file singolo | `python -m empire forge --help` | esiste un modo di misurare **un file** (o una cartella): se c'è solo `scan` globale, il passo 2.3 aggiunge `--file` (specifica) | 0 |
| P11 | La decisione 2 è presa o è a default | `ls company/Memory/decisions/ADR-0*-albero-canonico.md` | il file esiste (passo 2.2) | 0 |

---

## 2. I passi — numerati, ognuno con il comando esatto

### 2.1 — L'interruttore del sync (EMPERATOR, 15 min) — file vivo: contratto d'innesto

**Edit in `scripts/empire-sync.ps1`, subito dopo `$ErrorActionPreference = "SilentlyContinue"`
(riga 25), tre righe nuove:**
```
$sospeso = Join-Path $PSScriptRoot "..\company\Memory\.SYNC-SOSPESO"
if ((Test-Path $sospeso) -and ($Mode -ne "pull")) { Write-Host "[empire-sync] push SOSPESO da $(Get-Content $sospeso -TotalCount 1) - vedi company/Memory/.SYNC-SOSPESO"; exit 0 }
```
- Il `pull` resta sempre attivo (nessuno lavora su un repo stantio); solo `push`/`full` si fermano.
- **Contratto d'innesto (V3 §4):** ospite = `scripts/empire-sync.ps1`, vivo (lo lanciano i due hook
  di `settings.json:121,152` su ogni PC). Politica **fail-open**: se il file sentinella non c'è o
  non è leggibile, lo script fa ciò che fa oggi. Gate di regressione dell'ospite: senza sentinella
  `powershell -File scripts/empire-sync.ps1 -Mode pull` → stesso output di prima (exit 0); con
  sentinella `-Mode push` → la riga `push SOSPESO`, exit 0, **nessun commit creato** (`git log -1`
  invariato). Rientro: `git checkout -- scripts/empire-sync.ps1`. Migrazione chiamanti: nessuna
  (gli hook chiamano lo stesso file con gli stessi argomenti).
- **Accensione** (inizio di ogni sessione di E1): `echo "E1 in corso, EMPERATOR, $(date -Iminutes) - spegnere a fine giornata" > company/Memory/.SYNC-SOSPESO`
  e **commit + push a mano subito** (così Gael lo vede): `git add company/Memory/.SYNC-SOSPESO && git commit -m "chore(E1): sync sospeso per la durata delle fusioni" && git push`.
- **Spegnimento** (passo 2.9): `git rm company/Memory/.SYNC-SOSPESO && git commit -m "chore(E1): sync riattivato" && git push`.
- Riga in cima a `STATO-EMPIRE.md` (blocco ⚠️ COORDINAMENTO): «sync automatico SOSPESO dalle
  <ora> alle <ora>: pushate a mano se serve».

### 2.2 — ADR `albero-canonico` (EMPERATOR 15 min, Max 1 riga o silenzio) — decisione 2

**Default (V2 §26.2):** vince `DIGITAL-EMPIRE/`. **Fatto misurato che cambia il peso della
decisione:** 0 gruppi identici a cavallo dei due alberi (punto 2 dell'intestazione), quindi la
decisione **non fonde niente oggi**: fissa (a) quale copia vince nelle 3 coppie a cavallo
(`chief-forge`: `.claude/agents/` è l'agente **eseguibile**, `DIGITAL-EMPIRE/04-AGENTS/` la scheda:
regola di 2.3, caso 3), (b) che `WORKFLOW-ESTATE/` è **stato ARCHIVIO** (L8) come albero — resta,
si legge, non si scrive più, un file `WORKFLOW-ESTATE/ARCHIVIO.md` di 5 righe lo dichiara con il
puntatore all'ADR — e (c) il perimetro di E5b. File: `company/Memory/decisions/ADR-0NN-albero-canonico.md`
sul template, con Contradiction-check che cita `registry dupes` (la NOTA in coda al suo report),
ADR-003 (wrap-first) e `dati/censimento-01b-organi.md:850-851` (26 path rotti + 2 cartelle vuote
in `WORKFLOW-ESTATE/`: il motivo per cui non può essere lui il canonico).

### 2.3 — La regola di fusione, scritta prima di aprire la prima coppia (EMPERATOR, 20 min)

Va in testa a `company/Memory/decisions/ADR-0NN-albero-canonico.md` §Decisione, punto (d), **e** in
un file di lavoro `PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/V4-ESECUTIVO/_E1-REGISTRO-FUSIONI.md` (da
creare: una riga per coppia, compilata man mano — è il registro che chi riprende legge).

**Regola (V2 §21-E1, resa eseguibile):**
1. Si misurano **entrambe** le copie: `python -m empire forge scan --file <A>` e `--file <B>`
   (se `--file` non esiste — P10 — **specifica da costruire in questo passo**: `forge scan --file
   <path>` stampa la riga `OPERATIVO|PARZIALE|DOCUMENTALE  <punteggio>  manca: <criteri>` per quel
   solo file, exit 0; 20 righe in `empire/forge.py` riusando la funzione che già valuta un file
   dentro `scan`).
2. **Vince chi ha più criteri C1-C6.** A parità: la più recente (`git log -1 --format=%ad -- <path>`).
3. **Caso 3 (scheda ↔ eseguibile):** vince **sempre l'eseguibile** (`.claude/agents/`, o
   `~/.claude/agents/` se è l'unica), qualunque sia il punteggio: un agente che Claude Code carica
   batte una scheda che nessuno carica (L3: vivo = usato). La scheda perdente **non va in
   archivio**: diventa un **puntatore** di 3 righe all'eseguibile (frontmatter + `> Canonico:
   <path>` + una riga sul perché), perché E5-bis avrà bisogno della coppia scheda↔esecutore con
   `fonte_di_verita` dichiarata (V3 §6): qui si dichiara `fonte_di_verita: esecutore`.
4. **La perdente non si cancella (L1):** `git mv <perdente> <ecosistema>/archivio-origine/<nome>.md`
   (cartella **da creare** al primo uso, con un `README.md` di 3 righe: «stato ARCHIVIO (L8) — le
   schede qui hanno perso una fusione di E1; il canonico è indicato in testa a ciascuna»), e in
   testa alla perdente 2 righe: `> ARCHIVIO — fusa in E1 il <data>; canonico: <path vincente>;
   motivo: <criteri A vs B>`.
5. **Il vincente eredita ciò che alla perdente veniva meglio** — ma **solo** se è un criterio
   misurato mancante nel vincente (es. la radice ha C4-uscita e il reparto no → si copia la sezione
   `## Output` nel reparto). Mai fondere prosa a gusto: se un pezzo non è un criterio C1-C6, resta
   dov'è (in archivio) e lo si cita in `_E1-REGISTRO-FUSIONI.md`.
6. **Puntatori nello stesso commit** (REGOLA PUNTATORI): `grep -rl "<nome file perdente>" company/ .claude/ PIANO-MAESTRO/ --include=*.md --include=*.yaml`
   → ogni risultato si corregge al percorso vincente **prima** del commit.

### 2.4 — Le 32 fusioni, una per commit (EMPERATOR, 9-15 h: 15-25 min l'una)

**Ordine:** prima le 10 di FORGE (la copia buona è quella invisibile: è dove il piano perdeva di
più), poi le 19 di 04-MARKETING, poi le 3 a cavallo. Per **ogni** coppia, nell'ordine, senza
saltare un punto:

```
# 0. radice pulita, sync sospeso
git status --porcelain | wc -l                      # deve dare 0
test -f company/Memory/.SYNC-SOSPESO || echo "ACCENDI 2.1 PRIMA"

# 1. misura
python -m empire forge scan --file "<A>"
python -m empire forge scan --file "<B>"
git log -1 --format="%ad %h" -- "<A>"; git log -1 --format="%ad %h" -- "<B>"

# 2. decisione (regola 2.3) -> riga nel registro, PRIMA di toccare i file
echo "| <nome> | <A> (<punteggio>) | <B> (<punteggio>) | vince: <A|B> | motivo: <...> | commit: (in corso) |" >> "PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/V4-ESECUTIVO/_E1-REGISTRO-FUSIONI.md"

# 3. archivio + eredita' + puntatori (regola 2.3 punti 4-6)
mkdir -p "<ecosistema>/archivio-origine"            # solo la prima volta per ecosistema, con README
git mv "<perdente>" "<ecosistema>/archivio-origine/<nome>.md"
# edit: 2 righe in testa alla perdente; sezioni ereditate nel vincente; puntatori (grep -rl)

# 4. gate della coppia (L9): il nome esiste in UNA copia sola nel perimetro forge
python -m empire forge scan --file "<vincente>"     # punteggio >= max(A,B)
python - <<'PY'
import glob,os,sys; nome="<nome>"
hits=[p for p in glob.glob("company/**/*.md",recursive=True) if os.path.basename(p).lower()==nome+".md" and "/archivio-origine/" not in p.replace("\\","/")]
print(hits); sys.exit(0 if len(hits)==1 else 1)
PY

# 5. un commit, atomico, con H11 e H7 che girano nel pre-commit
git add -A "<ecosistema>/" .claude/agents/ PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/V4-ESECUTIVO/_E1-REGISTRO-FUSIONI.md
git commit -m "fuse(E1): <nome> — vince <A|B> (<punteggio>), perdente in archivio-origine, puntatori aggiornati"
# 6. aggiornare la colonna "commit:" del registro con lo hash (e' nel commit successivo, va bene)
```

Se il punto 4 fallisce (due copie ancora nel perimetro, o punteggio calato): **non si committa**;
`git checkout -- . && git clean -fd "<ecosistema>/archivio-origine"` e si riapre la coppia. È la
politica fail-closed dell'intestazione.

**Tempo:** 32 × 15-25 min = 8-13 h. Il tetto di V3 (30) copre anche i passi 2.5-2.8.

### 2.5 — I 6 non censiti in `registro-agenti.yaml` (EMPERATOR, 30 min)

`conoscenza-empire`, `tesoreria-conductor`, `tesoreria-entrate`, `tesoreria-previsione`,
`tesoreria-report`, `tesoreria-spese` (P5). Per ciascuno una voce nella sezione giusta di
`company/Backbone/Identity-HR/registro-agenti.yaml` (schema: `company/Gerarchia/README.md`; forma
delle voci esistenti, es. riga 12-19), campi `id, name, role, tier, level, file, reports_to`:
- i 5 `tesoreria-*` sotto la sezione dell'ecosistema **14-TESORERIA** (`file: .claude/agents/tesoreria-<x>.md`,
  `reports_to: tesoreria-conductor` per i 4, `reports_to: EMPERATOR` per il conductor);
- `conoscenza-empire` sotto **10-MEMORY** (`reports_to: EMPERATOR`, tier T3-Opus).
Gate: `python scripts/verify-agents.py` → `0 FAIL`, exit 0. Contratto d'innesto: il registro è un
YAML letto da `verify-agents.py:35` e da nessun motore a runtime (`grep -rl "registro-agenti" --include=*.py .` → solo lo script); fail-open; rientro `git checkout -- company/Backbone/Identity-HR/registro-agenti.yaml`.

### 2.6 — Una definizione sola di «agente», poi il census che la usa (EMPERATOR, 1-2 h) — file vivo

**Prima la definizione, in `company/Backbone/Identity-HR/DEFINIZIONE-AGENTE.md`** (da creare, 15
righe): *«È un agente un file `.md` che (a) ha un frontmatter con `name:` **oppure** un titolo
`# <ID> — <Nome>` **e** (b) sta in `.claude/agents/`, `~/.claude/agents/`, o in una cartella chiamata
`Agenti/`, `agenti/`, `04-agents/`, `04-AGENTS/` dentro `company/` o `DIGITAL-EMPIRE/`, **e** (c) non
sta in `archivio-origine/`, non è corredo (`memory.md`, `playbook.md`, `system-prompt.md`,
`tools.md`, `README.md`), non è un report scritto da una macchina (`STATO-AGENTI.md`). Il suo id
è il nome del file minuscolo senza estensione.»* — è la stessa lista che `forge` usa
(`empire/forge.py:146-147`, `_CORREDO`) più le esclusioni che il censimento 03a §3.5 ha trovato.

**Poi i due edit in `empire/registry/census.py`:**
1. `_determine_kind` (`census.py:163-164`): il ramo `agent` legge la definizione — stessa lista di
   cartelle, stesse esclusioni — e **include `.claude/agents/`** (oggi escluso: è il motivo del 70).
2. `run_census` (`census.py:170+`): prima di restituire, **dedup per percorso** —
   `visti=set(); artifacts=[a for a in artifacts if not (a.path in visti or visti.add(a.path))]` —
   e una riga di log `dedup: N artefatti doppi rimossi`. È il bug del punto 2 dell'intestazione.
- **Contratto d'innesto:** ospite `empire/registry/census.py`, vivo (lo usano `registry dupes`,
  `registry orphans`, `registry gate` = H4 di E0.7). Politica **fail-closed** (un census che non
  gira lascia il vecchio `census.json`: `run_census` scrive solo a fine scansione, riga da
  verificare). Gate di regressione: `python -m pytest empire/tests -q` → **236 passed** come il
  05/09 (`30-PIANO-COMPLETAMENTO-IMPERO.md:49`) + i test nuovi di 2.7; `python -m empire registry
  gate` → stesso esito di prima sui file già committati. Rientro: `git checkout -- empire/registry/census.py`.
  Migrazione chiamanti: nessuna (firma invariata).
- Poi: `python -m empire registry census` → `agent : N` con N = numero di id della definizione.

### 2.7 — Il gate «stessi id» fra `forge scan` e `registry census` (EMPERATOR, 1 h) — specifica di comando

**`python -m empire registry census --json`** esiste? (`python -m empire registry census --help`,
11/09: **no** `--json`). **Specifica da costruire in questo passo:** `--json` stampa
`{"agenti": [<id>...], "totale": N}` e nient'altro. E in `empire/forge.py`: `forge scan --json`
stampa `{"agenti": [<id>...], "operativi": n, "totale": N}` (se già esiste, si verifica che porti
gli **id**, non solo i totali). Gate (§3, G4): differenza simmetrica fra le due liste = **0**, e
la lista delle differenze stampata quando non è 0 (V2 §21-E1: «gli id, non i totali»).
Test nuovo in `empire/tests/test_census_ids.py` (da creare): 3 file finti in una cartella
temporanea (`Agenti/x.md`, `Agenti/README.md`, `archivio-origine/y.md`) → census e forge devono
restituire entrambi `["x"]`.

### 2.8 — Il block `LINK-DEAD` e i puntatori di ecosistema (EMPERATOR, 1 h)

1. `WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/preventivo-template.md:10`: il riferimento
   `Clienti/Prof Autocad/preventivo-forge/templates/preventivo.html` non esiste. `find . -name
   "preventivo.html" -path "*preventivo-forge*" -not -path "*/node_modules/*"` → se esiste altrove,
   si corregge il percorso; se non esiste, la riga diventa `> (template HTML non più presente:
   il preventivo si genera con \`/preventivo-auto\`, vedi skill omonima)` — mai un link a un file
   che non c'è (`doctor` lo tiene BLOCK finché c'è).
2. Puntatori di ecosistema: dopo le 32 fusioni, `python -m empire links` (riferimenti rotti nei
   `.md`) → **0 rotti sotto `company/`**; ogni rotto residuo si corregge al percorso vincente o ad
   `archivio-origine/`. Poi `python -m empire registry links` (controlla **e corregge**): si lancia
   **prima in sola lettura** (`--help` per il flag di dry-run; se non c'è, si guarda `git diff`
   dopo e si scarta ciò che non è una fusione di E1).
3. I 43 `info(riparabili)` di `doctor` **non sono di E1** (sono `LINK-FIXABLE` risolvibili via
   `empire.paths.resolve_legacy`): si lascia il numero nel checkpoint e passano a E2.

### 2.9 — Spegnere l'interruttore e riconsegnare il repo (EMPERATOR, 5 min, a fine di OGNI giornata di E1)

```
python -m empire doctor | grep "block:"        # block 1 (ADR-001 resta finche' E0.5 2.10 non chiude) o 0
git rm company/Memory/.SYNC-SOSPESO && git commit -m "chore(E1): sync riattivato, <n>/32 coppie fuse" && git push
```
E la riga del blocco ⚠️ COORDINAMENTO in `STATO-EMPIRE.md` aggiornata con `<n>/32`.

---

## 3. Il gate — comando, condizione di fallimento, exit code (L9)

```
# G1 - una copia sola per nome nel perimetro forge (le 32 coppie)
python - <<'PY'
import glob,os,collections,sys
nomi=collections.Counter()
for p in glob.glob("company/**/*.md",recursive=True)+glob.glob(".claude/agents/*.md"):
    q=p.replace("\\","/")
    if "/archivio-origine/" in q: continue
    if not any(s in q for s in ("/Agenti/","/agenti/","/04-agents/","/04-AGENTS/",".claude/agents/")): continue
    b=os.path.basename(q).lower()[:-3]
    if b in ("memory","playbook","system-prompt","tools","readme"): continue
    nomi[b]+=1
doppi={n:c for n,c in nomi.items() if c>1}
print("nomi doppi:",len(doppi),doppi); sys.exit(0 if not doppi else 1)
PY
#   exit 0 = zero nomi doppi · exit 1 = ne resta almeno uno (stampati)

# G2 - verify-agents e verify-skills verdi
python scripts/verify-agents.py ; echo "G2a exit $?"
python scripts/verify-skills.py ; echo "G2b exit $?"
#   exit 0 entrambi

# G3 - doctor senza block (o con il solo ADR-001 se E0.5 2.10 non e' ancora chiusa: si dichiara)
python -m empire doctor ; echo "G3 exit $?"
#   exit 0 = block 0 · exit 1 = leggere le righe [BLOCK]: se e' SOLO "ADR-001 numero duplicato 08", E1 passa e lo scrive

# G4 - forge e census contano GLI STESSI ID
python -m empire registry census --json > /tmp/census.json
python -m empire forge scan --json > /tmp/forge.json
python -c "import json;a=set(json.load(open('/tmp/census.json'))['agenti']);b=set(json.load(open('/tmp/forge.json'))['agenti']);d=a^b;print('differenze:',len(d),sorted(d)[:20]);import sys;sys.exit(0 if not d else 1)"
#   exit 0 = differenza simmetrica vuota · exit 1 = stampa gli id che uno vede e l'altro no

# G5 - il census non conta piu' due volte lo stesso percorso
python -c "import json,sys;a=json.load(open('empire/.data/census.json'))['artifacts'];p=[x['path'] for x in a];sys.exit(0 if len(p)==len(set(p)) else 1)"; echo "G5 exit $?"
#   exit 0 = percorsi tutti distinti

# G6 - registro delle fusioni completo: 32 righe con hash di commit
grep -c "| commit: [0-9a-f]\{7,\}" "PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/V4-ESECUTIVO/_E1-REGISTRO-FUSIONI.md"
#   PASSA se stampa 32

# G7 - il sync e' riattivato (mai lasciare E1 con l'interruttore acceso)
test ! -f company/Memory/.SYNC-SOSPESO ; echo "G7 exit $?"
#   exit 0 = sentinella assente

# G8 - la suite del runtime non e' regredita
python -m pytest empire/tests -q | tail -1
#   PASSA se "passed" >= 236 e 0 failed (il test test_adr001_canonical_ecosystems_are_ten resta fallito
#   finche' E0.5 2.10 non chiude: si dichiara, non si conta come regressione di E1)
```

**Condizione di chiusura di E1:** G1, G2a, G2b, G4, G5, G6, G7 a exit 0; G3 a exit 0 **oppure** con
il solo block ADR-001 dichiarato; G8 senza regressioni. Nessun NON VALUTATO.

---

## 4. Politica di guasto e piano di rientro

| Guasto | Politica | Cosa si fa | Cosa si dichiara |
|---|---|---|---|
| La sessione cade a metà di una fusione (file spostato, commit non fatto) | fail-closed | alla ripresa: `git status`; se c'è lavoro non committato nelle cartelle della coppia → `git checkout -- . && git clean -fd <ecosistema>/archivio-origine`; la riga del registro resta `commit: (in corso)` e si riapre la coppia da 1 | nel registro delle fusioni: «coppia <nome> riaperta il <data>» |
| Il sync ha pushato lo stato misto (interruttore non acceso, o acceso dopo) | fail-closed sul repo | **non** `reset --hard`: `git revert <hash del sync>` per i soli file della coppia, poi la fusione si rifà per intero e si committa atomica | in cima a STATO-EMPIRE + nel registro |
| `forge scan --file` dà lo stesso punteggio a entrambe e le date coincidono | regola 2.3 punto 2 non decide | vince la copia nel percorso **canonico** (decisione 2: `DIGITAL-EMPIRE/`; per 04-MARKETING: il **reparto**, perché è dove E2 scriverà i contratti — `Reparti/L2-*/Agenti/`) | nel registro: «parità, canonico» |
| Un puntatore alla perdente sfugge al `grep` (link relativo, nome con maiuscole) | fail-open | `python -m empire links` a fine giornata lo trova; si corregge nel commit successivo | nel checkpoint: quanti |
| `census.py` dopo 2.6 rompe `registry gate` (H4) | fail-closed | `git checkout -- empire/registry/census.py`, si rifà l'edit con il test 2.7 verde **prima** di toccare `_determine_kind` | nel checkpoint |
| Gael pusha durante E1 (il suo hook non è sospeso perché non ha ancora pullato la sentinella) — **non dipende da Gael**: è un rischio, non un prerequisito | fail-open | il suo push non tocca le cartelle delle coppie (perimetro suo: LANCI, EMPIRE DESK); `git pull --rebase` prima del commit successivo; se tocca una coppia, si applica la riga 2 | nel checkpoint |
| H11 di E0.7 non è pronto | E1 **non parte** (intestazione) | si fanno 2.2, 2.3, 2.5, 2.8 punto 1 (non sono commit sulle coppie); le fusioni aspettano | riga ADR-026: «E1 ferma su H11; 2.2/2.3/2.5/2.8 fatte» |

**Il danno peggiore possibile di E1:** una coppia mezza fusa pushata al pubblico e poi «riparata»
a mano in due sessioni diverse — è il caso che produce **tre** copie da due. Per questo: un commit
per coppia, l'interruttore, e il registro con l'hash.

---

## 5. Le forze — chi fa cosa, e il prompt d'ingaggio già scritto

**Nessuna forza sulle fusioni.** Trentadue decisioni editoriali su copie divergenti, ognuna con un
commit atomico su un repo che altri stanno usando: è il lavoro in cui un agente delegato ha già
prodotto le cadute censite (`dati/censimento-03b2-cadute.md`: 33 cadute reali), e V2 §18 impone
**un solo scrittore** in `company/**`. EMPERATOR le fa in prima persona, a sessioni corte (10-12
coppie per sessione, checkpoint dopo ognuna).

**Unica delega ammessa — i test di 2.7**, a uno **scagnozzo sonnet**, perimetro un file, prompt:

> Sei uno scagnozzo di EMPERATOR nel repository `c:\Users\Utente\Desktop\qui tutto\Digital Empire`.
> Scrivi **un solo file**: `empire/tests/test_census_ids.py`. Non tocchi nessun altro file. Prima
> crea il file con lo scheletro (import, una classe vuota) e salvalo; poi aggiungi **un test per
> volta**, salvando dopo ognuno. Cose da coprire (non un numero di righe): (1) in una cartella
> temporanea con `Agenti/x.md` (frontmatter `name: x`), `Agenti/README.md`, `archivio-origine/y.md`,
> `python -m empire registry census --json` e `python -m empire forge scan --json` restituiscono
> entrambi `agenti == ["x"]`; (2) lo stesso percorso presente due volte nell'input del census
> compare una volta sola in `census.json`; (3) `.claude/agents/z.md` è contato come agente. Leggi
> prima `empire/tests/test_seed.py` per la forma dei test esistenti e `company/Backbone/Identity-HR/DEFINIZIONE-AGENTE.md`
> per la definizione. Gate: `python -m pytest empire/tests/test_census_ids.py -q` verde. Ultimo
> messaggio: il nome del file, quanti test, e cosa non sei riuscito a coprire.

---

## 6. Cosa si scrive in Memory alla chiusura

- **Checkpoint:** `python scripts/checkpoint.py cp --titolo "E1 chiusa: 32 coppie fuse in 32 commit, forge e census contano gli stessi N id, verify-agents 0 FAIL, doctor block <0|1>"` — dentro: il registro delle fusioni (o il suo percorso), quante volte ha vinto la radice / il reparto / l'invisibile / l'eseguibile, il numero di agenti dopo la definizione unica (atteso: **407** nomi distinti, censimento 03a §3.5 — si scrive il numero misurato), i 43 info di doctor lasciati a E2, la data/ora di accensione e spegnimento dell'interruttore per ogni sessione.
- **Riga per `STATO-EMPIRE.md`** (in cima): `## ✅ <data> — E1: perimetro pulito — 32 coppie fuse, un solo id per agente, forge = census — CP-...`; **togliere** il blocco ⚠️ COORDINAMENTO di E1.
- **ADR:** `ADR-0NN-albero-canonico.md` (2.2, con la regola di fusione al punto d).
- **BACKLOG:** i 43 `LINK-FIXABLE` di doctor → una voce «da chiudere in E2 con `registry links`»; gli 81 gruppi identici che toccano `company/` (dopo il dedup di 2.6 il numero vero) → una voce per E5b.
- **I sei numeri del cruscotto (V2 §23), prima e dopo:**
  - `controllo x/6`: invariato (E1 non tocca i 6 gate di `controllo`)
  - `OPERATIVO %`: **61/439 = 13,9%** prima → **n/407** dopo (il denominatore **scende** di 32 file: si scrive il numero vero, e si dichiara che è cambiato il denominatore, non il numeratore — L10)
  - `tracce (origine=hook)`: 0 (invariato)
  - `byte entrate.jsonl`: invariato
  - `pezzi fermi (ultimo_metro)`: invariato
  - `vivo%`: se E0.5 è chiusa, il numero del giorno; il denominatore degli agenti cambia anche qui
