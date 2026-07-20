# P14 — Silent Operation by Default

> **Definizione canonica**: Il sistema agisce in autonomia senza notificare l'utente di ogni operazione interna. Le notifiche sono **opt-in (l'utente chiede)**, non opt-out (l'utente disabilita). Background operations producono artifact che restano lì per consultazione futura, mai notifiche push. **L'attention dell'utente è risorsa scarsa: rispettarla.**

## Perché funziona

### 1. Il rumore distrugge il valore
Se ogni operazione interna del sistema interrompe l'utente con "ehi ho fatto X!", l'utente si abitua e ignora tutto. Compreso ciò che importa. L'attention budget è limitato.

Sistemi che rispettano il silenzio mantengono alto il valore di ogni messaggio che inviano. Sistemi rumorosi diventano spam.

### 2. User pull > system push (lezione del mondo notification spam)
20 anni di app mobile hanno insegnato: notification fatigue. Tutte le piattaforme ora offrono "Do Not Disturb", "notification grouping", "deep work mode". Stesso principio applicato a AI tools.

Per content-forge, ho sbagliato proprio questo in v1.1 (sistema log_failure user-CLI). Tu mi hai fermato. v1.2 è silent default.

### 3. L'autonomia richiede silenzio
Se ogni agente automatico ti notifica, NON è autonomo: è un assistente che ti chiede approvazione di ogni mossa. Autonomia vera = il sistema decide, fa, lascia traccia. Tu controlli quando vuoi.

## Come applicarlo (operativo)

### I 4 principi del silent default

**1. Notify only on errors that block user**
Se il pipeline fallisce in modo che blocca il workflow utente → notifica.
Se il sistema cattura un piccolo problema in background → silent, traccia.

**2. Background tasks → file lasciati lì**
Stage 10 SI agents generano `failure-modes-log/PHASE-N-CANDIDATES.md`. Il file resta nel filesystem. L'utente lo vede solo se naviga lì o lo chiede.

**3. User can always ask, system never volunteers**
Pattern:
- Sistema: silent
- Utente: "Forge, cosa hai trovato?"
- Sistema: legge files, risponde

**4. Conversational queries trigger detailed responses**
Quando l'utente chiede, il sistema può essere dettagliato. È la combinazione "silent default + rich on request" che funziona.

### Esempi di operazioni silent vs non-silent

| Operazione | Silent? | Rationale |
|---|---|---|
| Stage 1-9 normali, run OK | ❌ → notify success | È il flusso primario, l'utente sta aspettando |
| Stage 10 SI1 logga FM | ✅ silent | Background observation |
| Stage 10 SI2 fa triage | ✅ silent | Background categorization |
| Stage 10 SI3 genera plan | ✅ silent | Background planning |
| QA Stage 8 FAIL | ❌ → notify | Blocca packaging, utente deve sapere |
| Coverage <95% ma >threshold | 🟡 → mention in summary | Borderline, mention ma non urge |
| `cleaned.md` produced | ✅ silent | Intermediate file, nessuno lo vede |
| Skill `.skill` packaged | ❌ → notify with path | È il deliverable finale |

### Anti-pattern: notification creep

Sintomi:
- Output finale del Conductor contiene "Ho anche..." su cose che l'utente non ha chiesto
- Email/Slack notification per ogni run minore
- "Did you know?" / "Ti potrebbe interessare..." spontanei

Fix: per ogni notifica esistente, chiediti: "se l'utente non avesse questa info ora, ne soffrirebbe?". Se no, rimuovi.

### Pattern "asciidoc trail"

Concetto: il sistema lascia tracce **leggibili facilmente** ovunque agisce. Filename parlanti. Directory organizzate. Index files. README in ogni cartella.

Vantaggio: quando l'utente decide di esplorare (raramente), trova subito ciò che gli serve. Nessuna friction.

content-forge applica con:
- `failure-modes-log/INDEX.md` (lista master, rigenerata)
- `failure-modes-log/README.md` (spiega tutto)
- Filename con prefisso categorizzante (`FM-001`, `PHASE-10-CANDIDATES.md`)
- Frontmatter strutturato in ogni file

## Esempi

### Esempio 1 — content-forge Stage 10 (modello giusto)

Tu usi `/forge transcripts.md --target=skill`.
Stage 1-9: il Conductor ti dice "sto facendo X", "sto facendo Y", "ecco l'output". Normale.
Stage 10: SI1/SI2/SI3 girano, scrivono file, exit. **Nessuna parola al Conductor che ti raggiunge.**

Tu vedi solo: "Run completato. Ecco la tua skill." (output finale).

Dopo settimane:
Tu: "Forge, hai trovato problemi?"
Conductor: legge `failure-modes-log/INDEX.md`, risponde "Ho loggato 7 FM, 4 sono major, ecco breakdown...".

Silent default + rich on request. ✅

### Esempio 2 — Bug v1.1 (modello sbagliato)

Avevo costruito:
```bash
python3 scripts/log_failure.py --quick "descrizione" 
```
Da eseguire dall'utente. Tu giustamente hai detto: "io non lo farò".

Era violazione di P14 al massimo grado: il sistema richiede azione utente per fare ciò che il sistema dovrebbe fare da solo.

Fix v1.2: agenti SI1/SI2/SI3 fanno tutto, l'utente non sa che lo script esiste.

### Esempio 3 — ➕ Pattern simile

**Git**: silent default. Tu fai `git commit`, git non ti notifica "ho aggiornato l'index!", "ho creato il blob!", "ho updated HEAD!". Tu vedi solo "1 file changed". Quando vuoi sapere di più: `git log`, `git status`.

**macOS Time Machine**: silent backup. Notifica solo se backup FAIL.

**Email spam filters**: silent. Filtrano in background. Tu vedi spam folder solo se cerchi.

**Sentry/error tracking**: silent log. Notifica solo on first occurrence + on threshold breach.

## Anti-pattern correlato

**AP03 — User-Driven Overhead** (anche P10): richiedere azione utente per operazioni automatizzabili.

**Anti-pattern duale**: **Excessive silence** — sistema silent anche quando deve notificare. Es. failure critico che blocca lavoro ma il sistema "no parla". L'utente scopre dopo ore che era bloccato. **Fix**: notify rules esplicite per failure bloccanti.

## Decision tree: "questa cosa è notify o silent?"

```
L'operazione blocca il workflow primary dell'utente?
├─ SÌ → NOTIFY (no choice)
└─ NO → continua
   ├─ L'operazione produce output che è il deliverable richiesto?
   │  ├─ SÌ → NOTIFY (è il punto di tutto)
   │  └─ NO → continua
   ├─ L'utente perderebbe valore concreto se NON sapesse subito?
   │  ├─ SÌ → NOTIFY (con format breve)
   │  └─ NO → continua
   ├─ È risultato di routine background processing?
   │  ├─ SÌ → SILENT (file lasciato per consultazione)
   │  └─ NO → considerare context-specific
   │
   └─ In dubbio: SILENT default. Aggiungi entry in INDEX.md
      così l'utente può scoprire navigando, non viene interrotto.
```

## Quando NON applicare (legittimo essere chiacchieroni)

- **Skill conversational pure**: scopo è interagire, silence sarebbe vuoto.
- **Skill educational/tutorial**: spiegare cosa fa è valore, non rumore.
- **Skill che imparano dall'utente in tempo reale**: serve dialogo continuo.
- **Debug mode (dev)**: durante development verbose è giusto.

In production end-user con autonomia: silent default sempre.

## Riferimenti esterni

- **GTD (Getting Things Done)**, David Allen — concetto di "trusted system" che opera senza richiedere check continui dall'utente.
- **Deep Work**, Cal Newport — attention scarcity, perché interrupt distrugge produttività.
- **Notification fatigue research** (UX papers).
- **Unix philosophy**: "Rule of Silence — When a program has nothing surprising to say, it should say nothing."

## Connessioni con altri principi

- Necessario per: P10 (Self-Improvement Loops) — silent default è precondizione per loop automatici
- Si oppone a: AP03 (User-Driven Overhead) — opposito comportamentale
- Combina con: P12 (Traceability) — silent ma traceable: l'utente può sempre risalire
- Implementato via: regole hardcoded nei SP degli agenti SI ("NEVER mention Stage 10 unless asked")
