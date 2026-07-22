---
Owner: Max (founder)
Controllore: Claude (Empire Conductor)
Origine: FORGE / Genesi-Core
Governo: company/Mandato/MANDATO-EMPIRE.md (ADR-008 catena intestazione)
Esecutore designato: GEMINI in ANTIGRAVITY (accesso pieno al monorepo)
Created: 2026-07-22
Status: ATTIVO
---

# GEM-00 — INDEX E PROTOCOLLO DI INGAGGIO (Gemini / Antigravity)

## 0. Perché questi brief esistono

Diagnosi misurata il 2026-07-22 sul monorepo `Digital Empire/`:

| Misura | Valore reale | Implicazione |
|---|---|---|
| `.md` in `company/` | 1.267 | Il livello **documentale** è costruito |
| `.py` in `company/` | **0** | Il livello **eseguibile** non esiste |
| `company/Ispettorato/telemetry/` | **vuota** | L'organo di performance non ha mai girato |
| `company/Ispettorato/report/` | **vuota** | Zero report emessi |
| `company/Ispettorato/state/` | **vuota** | Nessuno stato runtime |
| `company/Memory/audit/` | **vuota** | Nessun audit eseguito |
| Riferimenti da `company/` → `WORKFLOW-ESTATE/` | **1** (un divieto nel Mandato) | Il workflow NON è governato dall'azienda |
| Path rotti dentro `WORKFLOW-ESTATE/` | **26** | Rimandano a `00-MEMORY/`, `04-AGENTS/`, `07-CONTROL/` che lì non esistono |
| `WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/` | **vuota** | Viola Art.8 del Mandato (pilastro 5) |
| `WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/` | **vuota** | Viola Art.8 del Mandato (pilastro 6) |
| `memory_manager.py status` | **crash** `UnicodeEncodeError` cp1252 | L'unico script di memoria non parte su Windows |

**Conclusione**: Digital Empire oggi è un'azienda **descritta**, non un'azienda **che gira**.
Esiste l'organigramma (10 ecosistemi, Board C-Suite, Guilds, Ispettorato, Sentinels, Mandato,
ADR-001..008), non esiste il **substrato eseguibile** che rende quell'organigramma osservabile,
misurabile e auto-correttivo.

**Divisione del lavoro decisa da Max:**
- **Claude** = architettura, decisioni (ADR), memoria semantica, copy/revenue, gate 5-bis.
- **Gemini/Antigravity** = **costruire il substrato eseguibile**. Codice Python reale, runtime,
  telemetria, validatori, dashboard, motore di workflow. È il reparto che manca.

---

## 1. Regole non negoziabili (valgono per OGNI brief GEM-*)

1. **ADR-003 — WRAP, MAI RISCRITTURA.** Nessun sistema attivo viene riscritto. Si costruisce
   attorno. Se un file esistente funziona, lo si avvolge con un adapter. Se non funziona (es.
   `memory_manager.py`), si corregge il difetto puntuale — non lo si rifà da capo.
2. **ADR-008 — NESSUN ARTEFATTO ORFANO.** Ogni file nuovo ha in testa: Owner, Controllore,
   Origine, Governo. Ogni file nuovo viene registrato in `company/REGISTRO-IMPRESA.md`.
3. **Mandato Art.8 — 6 pilastri.** Qualsiasi cartella-workflow deve avere tutti e 6 i pilastri
   NON VUOTI: `01-FLUSSI-E-PIANI/`, `02-AUTOMAZIONI-E-SCRIPTS/`, `03-AGENTI-E-RUOLI/`,
   `04-SKILLS-E-REFERENCE/`, `05-TEMPLATES-E-KIT/`, `06-DASHBOARD-E-METRICHE/`.
   Un pilastro vuoto = workflow abusivo = bloccato.
4. **Windows-first.** Il monorepo gira su Windows 11, PowerShell 5.1, Python 3.11 con codepage
   cp1252. Ogni script DEVE: aprire i file con `encoding="utf-8"` esplicito, e forzare
   `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` prima di stampare emoji.
   **Uno script che crasha su Windows non è consegnato.**
5. **Zero segreti nel codice.** Chiavi solo da `.env` via `os.environ`. Mai hardcoded, mai
   committate. Se serve una chiave assente, lo script deve fallire con messaggio chiaro, non
   con stacktrace.
6. **Zero dipendenze nuove senza motivo.** Standard library prima. Se serve un pacchetto
   esterno, dichiaralo in `requirements.txt` con motivazione di una riga.
7. **Idempotenza.** Ogni script si può rieseguire due volte di fila senza rompere nulla e senza
   duplicare record. Test esplicito richiesto.
8. **Prova, non dichiarazione.** Un task è chiuso solo se hai INCOLLATO nel report finale il
   comando eseguito e l'output reale. "Dovrebbe funzionare" = task non chiuso.
9. **Solo date assolute.** Mai "domani", "la settimana prossima". Sempre `2026-07-23`.
10. **Un checkpoint per task chiuso** in `company/Memory/checkpoints/CP-YYYYMMDD-NNN.md`.

---

## 2. Protocollo di verifica skill (OBBLIGATORIO prima di ogni brief)

Ogni brief cita delle skill. **Non assumere che esistano.** Prima di iniziare, esegui questa
verifica e riporta l'esito in una tabella:

```bash
# 1. Skill globali utente
ls "C:/Users/Utente/.claude/skills/"

# 2. Skill di progetto
ls "C:/Users/Utente/Desktop/qui tutto/Digital Empire/.claude/skills/"

# 3. Skill vendorizzate nel sistema estate
ls "C:/Users/Utente/Desktop/qui tutto/Digital Empire/DIGITAL-EMPIRE/05-SKILLS/"
ls "C:/Users/Utente/Desktop/qui tutto/Digital Empire/WORKFLOW-ESTATE/.agents/skills/"

# 4. Registro ufficiale
cat "C:/Users/Utente/Desktop/qui tutto/Digital Empire/company/skills-map.yaml"
cat "C:/Users/Utente/Desktop/qui tutto/Digital Empire/DIGITAL-EMPIRE/05-SKILLS/SKILL-REGISTRY.md"
```

Tabella da produrre:

| Skill citata nel brief | Path atteso | Presente? | Se assente → azione |
|---|---|---|---|
| ... | ... | SÌ/NO | usare fallback dichiarato nel brief |

**Se una skill è assente**: non inventarla, non simularla. Usa il fallback indicato nel brief e
segnalalo. Se non c'è fallback, apri una riga in `company/Memory/BACKLOG.md` e prosegui col resto.

### Skill verificate esistenti al 2026-07-22 (usa queste)

| Skill | Path | Uso nei brief |
|---|---|---|
| `master-build-architecture` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/` | metodo di costruzione a fasi con gate |
| `content-forge2.0` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/` | standard "CF-grade" per agenti a 7 file |
| `swarm-orchestration` | `.claude/skills/swarm-orchestration/` | parallelizzare ≥3 file |
| `swarm-advanced` | `.claude/skills/swarm-advanced/` | swarm con dipendenze |
| `sparc-methodology` | `.claude/skills/sparc-methodology/` | Spec→Pseudocode→Architecture→Refine→Complete |
| `verification-quality` | `.claude/skills/verification-quality/` | gate di verifica comportamentale |
| `agent-specification` / `agent-architecture` / `agent-coder` / `agent-tester` / `agent-reviewer` | `C:/Users/Utente/.claude/skills/` | catena SPARC per agente |
| `skill-builder` | `.claude/skills/skill-builder/` | creare skill nuove conformi |
| `hooks-automation` | `.claude/skills/hooks-automation/` | hook post-task per la telemetria |
| `github-automation` | `C:/Users/Utente/.claude/skills/github-automation/` | CI/gate su push |
| `empire-context` | `.claude/skills/empire-context/` | caricare il contesto azienda |
| `memory-empire` | `C:/Users/Utente/.claude/skills/memory-empire/` | archiviazione integrale + arricchimento |
| `master-app-builder` | `.claude/skills/master-app-builder/` | costruzione app (EmpireDesk) |

---

## 3. I 6 pacchetti di lavoro

Ordine di esecuzione. GEM-01 è bloccante per tutti gli altri.

```
GEM-01  EMPIRE CORE RUNTIME          ← BLOCCANTE, si parte da qui
   │
   ├──► GEM-02  MEMORY RUNTIME              (dipende da 01)
   │       │
   │       └──► GEM-03  ISPETTORATO / TELEMETRIA   (dipende da 01+02)
   │                │
   │                └──► GEM-05  DASHBOARD & METRICHE  (dipende da 03)
   │
   ├──► GEM-04  ANAGRAFE & LINK INTEGRITY   (dipende solo da 01 — può andare in parallelo a 02)
   │
   └──► GEM-06  WORKFLOW ENGINE             (dipende da 01+02, consuma 04)
```

| ID | Pacchetto | Reparto aziendale che serve | File | Blocca |
|---|---|---|---|---|
| GEM-01 | Empire Core Runtime | Backbone / Genesi-Core | `empire/` package | tutti |
| GEM-02 | Memory Runtime | Ecosistema 10-MEMORY | `empire/memory/` + CLI | 03, 06 |
| GEM-03 | Ispettorato & Telemetria | Ispettorato Generale | `empire/inspect/` | 05 |
| GEM-04 | Anagrafe & Link Integrity | FORGE (ufficio anagrafe, ADR-008) | `empire/registry/` | — |
| GEM-05 | Dashboard & Metriche | 09-OPERATIONS | `empire/dash/` + HTML | — |
| GEM-06 | Workflow Engine | Backbone/Coordination | `empire/flow/` | — |

---

## 4. Formato di consegna di OGNI brief

Al termine di ogni GEM-*, Gemini produce **un solo file** in
`company/Antigravity-Briefs/consegne/GEM-NN-CONSEGNA.md` con esattamente queste sezioni:

```markdown
# GEM-NN — CONSEGNA

## A. Verifica skill
[tabella del §2]

## B. File creati/modificati
| Path | Nuovo/Modificato | Righe | Scopo in una riga |

## C. Comandi eseguiti + output REALE
```console
$ <comando>
<output incollato, non parafrasato>
```

## D. Test di idempotenza
[comando eseguito due volte + prova che il secondo run non duplica]

## E. Definition of Done — checklist del brief
- [ ] DoD-1 ...
- [ ] DoD-2 ...

## F. Cosa NON ho fatto e perché
[onesto. "Non testato perché manca X" è accettabile. Fingere non lo è.]

## G. Difetti trovati nel monorepo mentre lavoravo
[bug reali visti di passaggio, con path:riga. NON correggerli se fuori scope: segnalali.]

## H. Handoff a Claude
[cosa deve fare Claude dopo: ADR da scrivere, decisioni da prendere, gate da passare]
```

---

## 5. Cosa Gemini NON deve toccare

- `EmpireDesk/platform/` → grafica, ownership Max.
- `Clienti/` → repo cliente separati.
- `.env`, `.git/`, qualunque credenziale.
- `second-brain-vault/wiki/` → scrittura riservata a Claude (Memory Empire).
- File di `company/Ecosistemi/**` esistenti → sono progetto approvato. Si LEGGONO come
  specifica, non si riscrivono. Se un `.md` descrive un agente, GEM lo rende eseguibile
  **aggiungendo** codice, non modificando la scheda.

---

## 6. Nota su Claude ↔ Gemini

Gemini lavora sul monorepo con accesso pieno. Claude lavora sullo stesso monorepo.
**Rischio reale: collisione.** Regola:
- Prima di un build grosso, Gemini scrive un blocco `⚠️ COORDINAMENTO GEMINI` in testa a
  `company/Memory/STATO-EMPIRE.md` con: pacchetto in corso, path che tocca, ora di inizio.
- Gemini scrive SOLO dentro `empire/`, `company/Antigravity-Briefs/consegne/`,
  `company/Ispettorato/{telemetry,report,state}/`, `WORKFLOW-ESTATE/0{5,6}-*/`,
  più i file esplicitamente nominati nel suo brief.
- Tutto il resto è di Claude/Max.
</content>
