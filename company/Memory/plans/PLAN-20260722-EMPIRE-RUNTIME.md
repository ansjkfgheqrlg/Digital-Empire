---
Owner: Max · Controllore: Claude (gate 5-bis) · Origine: FORGE · Governo: MANDATO + ADR-006 (ciclo 9 passi)
Created: 2026-07-22 · Orizzonte: 2026-07-22 → 2026-07-26 · Stato: ATTIVO
Riferimenti: CP-20260722-005 (audit) · CP-20260722-006 (seed) · company/Antigravity-Briefs/
---

# PLAN — EMPIRE RUNTIME: dal livello descritto al livello che gira

## 0. Chiarimento di Max (2026-07-22) — due cose diverse, mai più confuse

| | Cos'è | Dove vive | Durata |
|---|---|---|---|
| **Digital Empire** | **l'azienda intera**: 10 ecosistemi, Board C-Suite, Guilds, Ispettorato, Mandato, Memoria | `company/` + `empire/` (runtime) | permanente |
| **Workflow Estate** | **solo un piano di lavoro per l'estate 2026**. Un workflow tra i tanti | `WORKFLOW-ESTATE/` | 21→26 luglio 2026, poi archiviato |

**Il problema di nome**: la cartella `DIGITAL-EMPIRE/` (6702 file, importata il 21/07) **non è
l'azienda** — è il workflow estate costruito da Chief-Forge. Il nome mente. È da lì che nasceva
la domanda sbagliata "quale delle due è canonica": non sono due aziende, sono **l'azienda e un
suo workflow**.

### DEC-EMP-001 — unificazione del workflow estate (proposta, finestra di veto 2026-07-23 20:00)
- `WORKFLOW-ESTATE/` = **unica cartella del workflow estate** (rispetta i 6 pilastri Art.8)
- `DIGITAL-EMPIRE/` = contenuto da **assorbire** dentro `WORKFLOW-ESTATE/` secondo la mappa dei
  pilastri, poi la cartella sparisce. Il nome `DIGITAL-EMPIRE` resta **solo** per l'azienda.
- Esecuzione: **M-C** (Claude), usando `empire.paths` per non rompere i riferimenti.
- Veto di Max entro il 2026-07-23 20:00, altrimenti la decisione passa ad ATTIVA e si procede.

---

## 1. Obiettivo del piano

> Portare Digital Empire da **azienda descritta** (1.267 `.md`, 0 `.py`) a **azienda che gira**:
> interrogabile da codice, che si misura da sola, che rifiuta gli artefatti orfani e che fa
> avanzare i workflow solo attraverso gate verdi.

**Misura di successo** (non opinione — comando):
```
python -m empire doctor        → exit 0        (oggi: exit 1, 6 block)
python -m empire agents        → > 200 agenti  (oggi: comando inesistente)
python -m empire inspect report --daily → un report reale (oggi: cartelle vuote)
python -m empire flow gates    → i 6 gate estate con stato vero
python -m empire dash build    → cruscotto aperto offline
```

---

## 2. Stato di partenza — misurato, non stimato

| Livello | % | Prova |
|---|---|---|
| Documentale | ~80% | 1.267 `.md`, 10 ecosistemi, 8 ADR, Mandato in 8 articoli |
| Eseguibile | **~8%** | era 3%; `empire/` seed (23 test verdi) l'ha portato qui |
| Osservabilità | **0%** | `Ispettorato/{telemetry,report,state}/` vuote |
| Integrazione azienda↔workflow | ~10% | `empire.conform` ora vede WORKFLOW-ESTATE |
| Memoria operativa | ~40% | file vivi, scrittura manuale, ID che collidono (B-009) |

**Azienda reale: ~33%.** Obiettivo del piano: **65-70%**.

---

## 3. Le 3 corsie — parallele, perimetri disgiunti, zero collisioni

```
                    ✅ F0 — SEED  empire/ (Claude, fatto, 23 test verdi)
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        ▼                          ▼                          ▼
   🟣 CORSIA GAEL            🔵 CORSIA CLAUDE           🟡 CORSIA GEMINI
   G-A loader+index          M-A empire/memory/         GEM-04 registry
   G-B fix memory_manager    M-B empire/inspect/        GEM-05 dash
   G-C empire/flow/          M-C unificazione estate
        │                          │                          │
        └──────────────────────────┼──────────────────────────┘
                                   ▼
                            F2 — INTEGRAZIONE
                     doctor exit 0 · dashboard viva · gate reali
```

### 🟣 Corsia GAEL — l'azienda diventa interrogabile ed eseguibile
| Lotto | Cosa | Gate di uscita | Dipende da |
|---|---|---|---|
| **G-A** | `empire/loader.py` + `index.py` — i 300+ agenti dai `.md` → oggetti, indice, ricerca | `empire agents` > 200, load < 10 s, `find`/`show` OK, idempotente | seed ✅ |
| **G-B** | fix `memory_manager.py` (Unicode + path via `empire.paths`, CLI invariata — ADR-003) | gira da 3 CWD diversi, exit 0 | seed ✅ |
| **G-C** | `empire/flow/` — motore dei workflow, gate 🟢/🔴, coda swarm, `flow today` | `flow validate` OK, i 6 gate estate valutati sui dati reali | G-A |

File esclusivi: `empire/loader*.py`, `empire/index*.py`, `empire/flow/**`, `memory_manager.py`.
Task: [`company/Memory/tasks/TASK-GAEL-20260722-EMPIRE-RUNTIME.md`](../tasks/TASK-GAEL-20260722-EMPIRE-RUNTIME.md)

### 🔵 Corsia CLAUDE — l'azienda ricorda e si critica
| Lotto | Cosa | Gate di uscita | Dipende da |
|---|---|---|---|
| **M-A** | `empire/memory/` — memoria unica a 2 livelli, **lock anti-collisione ID** (chiude B-009), `mem recall` | 20 scritture concorrenti → 20 ID distinti; `mem search` < 1 s | seed ✅ |
| **M-B** | `empire/inspect/` — accende l'Ispettorato: WF-PERF-LOOP T0→T5, scorecard 5D deterministica, backfill sui ~30 checkpoint reali | `telemetry/` e `report/daily/` **non più vuote**, ≥3 pattern reali trovati | M-A |
| **M-C** | Unificazione estate (DEC-EMP-001) + risanamento Art.8: riempire i 2 pilastri vuoti, chiudere i 4 link morti | `empire conform WORKFLOW-ESTATE` → **zero block** | seed ✅ |

File esclusivi: `empire/memory/**`, `empire/inspect/**`, `company/Memory/**`,
`company/Ispettorato/**`, `WORKFLOW-ESTATE/` (struttura).

### 🟡 Corsia GEMINI (Antigravity) — l'azienda si censisce e si vede
| Lotto | Cosa | Gate di uscita | Dipende da |
|---|---|---|---|
| **GEM-04** | `empire/registry/` — censimento ADR-008, orfani, link, duplicati, **gate bloccante** | censimento < 60 s, gate blocca un file senza intestazione (exit 1) e passa con (exit 0) | seed ✅ |
| **GEM-05** | `empire/dash/` — cruscotto HTML offline + `DASHBOARD.md`, i 6 gate visibili | HTML con **0 richieste esterne**, `EmpireDesk --selftest` ≥ 16/16 | GEM-04 (consigliato) |

File esclusivi: `empire/registry/**`, `empire/dash/**`, `WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/`.
Prompt pronti: [`company/Antigravity-Briefs/PROMPT-DA-INCOLLARE.md`](../../Antigravity-Briefs/PROMPT-DA-INCOLLARE.md)

---

## 4. Calendario e gate

| Data | Gate | 🟢 se | 🔴 → azione |
|---|---|---|---|
| **2026-07-22** | **G-START** | 3 corsie avviate: Gael ha pullato e sta su G-A · Gemini su GEM-04 · Claude su M-A | corsia ferma → Max la sblocca a mano |
| 2026-07-23 12:00 | **G-A** | `empire agents` > 200 agenti reali | Gael passa a G-B, G-A slitta a fine giornata |
| 2026-07-23 20:00 | **DEC-EMP-001** | veto di Max ricevuto, o finestra scaduta → ATTIVA | impossibile (auto-default) |
| 2026-07-23 20:00 | **M-A** | 20 ID concorrenti distinti, `mem recall` funzionante | B-009 resta aperto, si continua a `git pull` prima di ogni checkpoint |
| 2026-07-24 20:00 | **GEM-04** | consegna con censimento + gate funzionante | Max riassegna a Claude o rilancia il prompt |
| 2026-07-24 20:00 | **M-C** | `conform WORKFLOW-ESTATE` → zero block | il workflow estate resta "abusivo" per Art.8, si dichiara |
| 2026-07-25 20:00 | **M-B** | primo report daily reale con ≥3 pattern | Ispettorato resta spento, si dichiara |
| 2026-07-25 20:00 | **G-C** | `flow gates` valuta i 6 gate estate sui dati reali | i gate estate restano manuali |
| **2026-07-26 18:00** | **G-FINALE** | `python -m empire doctor` **exit 0** + dashboard apribile + report daily esistente | RETRO su causa radice, non su sintomi |

**Nessun gate "quasi verde".** 🟢 o 🔴. Un gate scaduto senza esito registrato è 🔴.

---

## 5. Pre-mortem — cosa può andare storto (e la contromossa già decisa)

| Rischio | Probabilità | Contromossa **già scritta nel piano** |
|---|---|---|
| **Collisione di ID checkpoint** — è già successa 3 volte oggi (B-009) | alta | fino a M-A chiuso: `git pull` PRIMA di scrivere un checkpoint. Dopo M-A: lock su file |
| **Collisione su file** tra le 3 corsie | media | perimetri esclusivi dichiarati in `STATO-EMPIRE.md`; `cli.py` non si tocca mai (loop di plugin) |
| **I `.md` degli agenti hanno formati troppo diversi** → il loader non regge | alta | G-A TASK 1 impone di campionare 10 schede **prima** di scrivere il parser, e progettare per la varianza trovata |
| **Gemini consegna dichiarando fatto ciò che non ha testato** | media | il prompt impone comando+output reale; il gate 5-bis di Claude riesegue i comandi dichiarati |
| **Il seed viene modificato da qualcuno e rompe le altre corsie** | media | file congelati: estendere sì, cambiare firme solo con nota ⚠️ COORDINAMENTO + push |
| **Max diventa il collo di bottiglia** (troppi passi `executor: human`) | alta | G-C lo rende **visibile e misurabile**: il numero di passi human su Max è un KPI della dashboard |
| **Il push si blocca per bloat** (già successo, B-008) | media | `WORKFLOW-ESTATE/` non è ancora tracciato: si committa solo dopo pulizia (`.next/`, `.git` annidati) in M-C |
| **Si costruisce troppo e non si fattura** | **la più seria** | budget-guard: questo piano non tocca la corsia revenue. I 7 concessionari e il gate REV del 26/07 restano priorità di Max, indipendenti |

---

## 6. Cosa NON è in questo piano (dichiarato, per non illudersi)

- **Gli agenti non eseguono ancora il lavoro.** Alla fine del piano l'azienda sa *chi* sono i suoi
  300+ agenti, *se* sono completi, *cosa* hanno prodotto e *quanto bene* — ma farli **operare**
  davvero è il lavoro successivo, e va fatto **un ecosistema alla volta**, non in blocco.
- **Nessuna automazione viene attivata senza approvazione di Max**: hook git, task schedulati e
  hook post-task vengono *documentati*, non installati.
- **La revenue non dipende da questo piano.** Il gate REV del 26/07 (≥1 anticipo incassato) si
  gioca sulle chiamate ai 7 concessionari, non sul runtime.

---

## 7. Partenza immediata — i 3 comandi di adesso

**Max:**
1. apri Antigravity → incolla il **PROMPT 1 (GEM-04)** da
   `company/Antigravity-Briefs/PROMPT-DA-INCOLLARE.md`
2. avvisa Gael: *"git pull, poi leggi `company/Memory/tasks/TASK-GAEL-20260722-EMPIRE-RUNTIME.md`"*
3. veto o conferma su **DEC-EMP-001** entro il 2026-07-23 20:00

**Claude:** parte da **M-A** (`empire/memory/`), che chiude anche B-009.

**Gael:** `git pull` → `python -m empire status` + 23 test verdi → **G-A**.

---

## 8. Aggiornamento del piano

Questo file si aggiorna **solo** ai gate. Lo stato quotidiano vive in
`company/Memory/STATO-EMPIRE.md`; le prove nei checkpoint. Un piano riscritto ogni ora non è un
piano — è un diario.
</content>
