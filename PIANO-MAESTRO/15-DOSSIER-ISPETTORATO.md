# DOSSIER 15 — ISPETTORATO GENERALE (Performance & Autocritica)

**Data:** 2026-07-04 · **Direttiva:** Max (verbatim: "report completi sulle performance, dopo ogni
utilizzo analizzate al millimetro da un nuovo reparto apposta, che va in contatto con gli alti
ranghi; così ogni utilizzo / ogni volta / ogni giorno l'Impero si autocritica e auto-migliora
senza mai fare gli stessi errori, MAI").
**Owner build:** **MAX** (non Gael). · **Standard:** v2 (Direttiva di Scala, dossier 11).
**Stato:** DA COSTRUIRE — piano approvato, build in fasi M1→M5 (vedi §10).

---

## 1. MISSIONE (l'idea chiara e specifica)

L'ISPETTORATO GENERALE è l'organo di **misurazione, autocritica e miglioramento continuo**
dell'Impero. Tre garanzie, non negoziabili:

1. **REPORT COMPLETO dopo OGNI utilizzo.** Ogni run di ogni workflow (PreventivoForge, outreach,
   content, build interni…) produce automaticamente un run-report: cosa è successo, quanto è
   durato, quali gate, quali errori, quali numeri. Nessuna run "muta".
2. **ANALISI AL MILLIMETRO.** Ogni report viene auditato: scostamenti dai KPI, errori nuovi vs
   errori noti, pattern ricorrenti, cause radice. Non "è andata bene" — numeri e verdetti.
3. **MAI LO STESSO ERRORE DUE VOLTE (Regola Zero Recidiva).** Ogni errore diventa una voce
   permanente del REGISTRO-ERRORI con contromisura. Prima di ogni build/run futura, il registro
   viene consultato: ripetere un errore registrato = gate ROSSO bloccante + escalation.

**Contatto con gli alti ranghi:** l'Ispettorato riporta DIRETTAMENTE a Board C-Suite e a
MAXIMILIAN (5-bis). Non è un reparto di produzione: è l'occhio dell'Imperatore sui reparti.

## 2. POSIZIONE GERARCHICA E AUTORITÀ

- **Collocazione:** organo trasversale di governo, allo stesso livello di MAXIMILIAN e del
  Mandato-ecosistema (dossier 13). Cartella: `company/Ispettorato/`.
- **Riporta a:** Board C-Suite (CEO/COO/CFO per i KPI; CTO per i guasti tecnici) + MAXIMILIAN
  (che usa i report come input del 5-bis). Report giornaliero indirizzato a Max.
- **Autorità:** diritto di audit su OGNI ecosistema/workflow/cliente. Può dichiarare un gate
  ROSSO per recidiva (blocca il commit della fase). NON produce, NON corregge da solo: rileva,
  registra, assegna la correzione al reparto owner e VERIFICA che sia fatta.
- **Indipendenza:** come CF-R6 (QA indipendente dalla produzione) — chi misura non è mai chi
  ha costruito la cosa misurata.

## 3. FORMA GIUSTA (regola Max 2026-06-16)

Cosa grande e trasversale → **reparto + backbone dati** (telemetria). NON serve un intero
"ecosistema": l'Ispettorato è UN reparto forte con un'infrastruttura dati che attraversa tutto.
- Reparto: `company/Ispettorato/` (roster §5, workflow §7).
- Backbone dati: `company/Ispettorato/telemetry/` + convenzione trace per-workflow (§6).

## 4. COSA NON È (confini, anti-duplicazione — ADR-003)

| Esistente | Differenza |
|---|---|
| **CF-R8 Apprendimento** | locale alla Content Factory (pattern sui contenuti). L'Ispettorato è EMPIRE-WIDE e wrappa CF-R8 come fonte, non lo rifà. |
| **MAXIMILIAN 5-bis** | giudica "Max approverebbe?" sulla QUALITÀ degli artefatti. L'Ispettorato misura le PERFORMANCE delle run e fornisce a MAXIMILIAN i dati. |
| **Sentinelle (dossier 13)** | vigilanza su coerenza/contraddizioni delle regole. L'Ispettorato vigila su metriche/errori di esecuzione. Si parlano (handoff), non si sovrappongono. |
| **RETRO (passo 9 metodo)** | resta: la retro di fase ORA scrive nel formato Ispettorato e viene auditata (il passo 9 si aggancia, non si duplica). |
| **KNOWN ERRORS di Empire Studio (RULES.md)** | primo seme del REGISTRO-ERRORI: viene MIGRATO dentro, non lasciato duplicato. |

## 5. ROSTER (11 agenti CF-grade, 7 file ciascuno)

| # | Agente | Tier | Compito |
|---|---|---|---|
| 1 | `isp-conductor` | opus | Dirige l'Ispettorato: riceve trigger (fine run / fine giorno / fine fase), orchestra gli altri, firma i report. |
| 2 | `isp-telemetry-collector` | sonnet | Raccoglie i dati grezzi: trace.jsonl, exit code, durate, gate, storico (es. `storico-preventivi/` sidecar JSON). |
| 3 | `isp-run-auditor` | sonnet | Analisi al millimetro della singola run: timeline, gate, scostamenti KPI, anomalie. |
| 4 | `isp-error-registrar` | sonnet | Ogni errore → voce `ERR-YYYYMMDD-NNN` nel REGISTRO-ERRORI: sintomo, causa radice, contromisura, owner, stato. |
| 5 | `isp-recidiva-sentinel` | sonnet | Il "MAI DUE VOLTE": confronta ogni errore nuovo col registro. Match → RECIDIVA → gate ROSSO + escalation immediata. |
| 6 | `isp-kpi-analyst` | sonnet | KPI per workflow (definiti in `kpi/`): successo run, durata, gate verdi al 1° colpo, € API, difetti sfuggiti. Trend giornaliero/settimanale. |
| 7 | `isp-report-forger` | sonnet | Genera i report (template §8): run-report, daily, escalation. Formato fisso, sempre completo. |
| 8 | `isp-liaison-altiranghi` | sonnet | Il contatto con gli alti ranghi: instrada i report a Board/MAXIMILIAN/Max, traccia le decisioni di ritorno e le porta a terra. |
| 9 | `isp-improvement-dispatcher` | sonnet | Da ogni audit → azioni di miglioramento assegnate al reparto owner (in BACKLOG o fase), con scadenza e verifica. |
| 10 | `isp-verifier` | sonnet | Verifica indipendente: le contromisure promesse sono state applicate DAVVERO? Chiude o riapre le voci del registro. |
| 11 | `isp-revision-analyst` | sonnet | **"Primo colpo migliore" (direttiva Max 2026-07-20):** quando un output umano-Claude richiede N correzioni prima di essere accettato, studia OGNI correzione della catena (non solo l'ultima), ne estrae il pattern ("cosa mancava/andava capito subito") e lo scrive come voce `REV-YYYYMMDD-NNN` in `registro/REGISTRO-REVISIONI.md`. Obiettivo: il ciclo di correzione N si accorcia nel tempo — misura `revisioni_medie_per_task` come KPI trend. Studia anche i casi a **0 correzioni** (output accettato al primo colpo): li registra come pattern-vincente da ripetere, non solo gli errori. |

## 6. BACKBONE DATI (deterministico, €0 API — Mandato Art.4.3)

```
company/Ispettorato/
├── README.md · ARCHITETTURA.md
├── agenti/            (11 × 7 file)
├── workflow/          (4 WF, §7)
├── telemetry/
│   ├── runs/<workflow>/<run-id>.jsonl      ← trace eventi per run
│   └── daily/<YYYY-MM-DD>.md               ← snapshot giornaliero
├── registro/
│   ├── REGISTRO-ERRORI.md                  ← ERR-*: la memoria anti-recidiva (append-only)
│   ├── REGISTRO-REVISIONI.md               ← REV-*: cicli di correzione studiati, "primo colpo migliore" (append-only)
│   ├── REGISTRO-SUCCESSI.md                ← SUC-*: cosa è uscito bene al primo colpo, pattern da ripetere
│   └── REGISTRO-DECISIONI-ALTIRANGHI.md    ← decisioni di ritorno da Board/Max
├── report/
│   ├── run/<run-id>.md · daily/<data>.md · escalation/<id>.md
├── kpi/               (definizione KPI per workflow + soglie)
├── principi/ · regole/ · skills/ · scripts/ · state/
```

**Convenzione trace (da cablare in ogni workflow):** ogni run scrive eventi JSONL
(`run_id, ts, step, gate, exit, dur_ms, err`) — pattern già provato in 01-AGENCY
(`trace.jsonl`, ciclo CY-20260611-001). Script collettori in `scripts/` (Python, no LLM):
i report si COMPILANO dai dati; gli agenti li interpretano solo dove serve giudizio.

## 7. I 4 CICLI + 5 WORKFLOW

| Trigger (direttiva Max) | Workflow | Output |
|---|---|---|
| **DOPO OGNI UTILIZZO** | `WF-RUN-AUDIT` | run-report completo + errori registrati + eventuale RECIDIVA |
| **OGNI GIORNO** | `WF-DAILY-AUTOCRITICA` | daily report: KPI trend, autocritica ("cosa rifaremmo meglio"), top-3 azioni |
| **OGNI ERRORE** | `WF-RECIDIVA-GATE` | check registro → nuovo: registra+contromisura · noto: ROSSO+escalation |
| **VERSO GLI ALTI RANGHI** | `WF-REPORT-ALTIRANGHI` | pacchetto a Board/MAXIMILIAN/Max + tracking decisioni di ritorno |
| **DOPO OGNI CICLO DI CORREZIONE** (direttiva Max 2026-07-20) | `WF-REVISION-STUDY` | studia TUTTE le N correzioni di un task (non solo l'ultima) → `REGISTRO-REVISIONI.md` + pattern estratto → se 0 correzioni: voce in `REGISTRO-SUCCESSI.md` |

**Aggancio al metodo 9 passi:** passo 1 RECALL ora include "consulta REGISTRO-ERRORI";
passo 9 RETRO ora produce output in formato Ispettorato. (Aggiornare dossier 10 in M4.)

## 8. TEMPLATE RUN-REPORT (formato fisso, "al millimetro")

```markdown
# RUN-REPORT <run-id> — <workflow> — <data ora>
1. ESITO: VERDE/ROSSO · exit · durata totale
2. TIMELINE: step → durata → esito (tutti)
3. GATE: n/n verdi, dettaglio per gate (al 1° colpo? retry?)
4. NUMERI: KPI della run vs soglie (es. PF: foto, prezzo esposto→finale, KB PDF, € API)
5. ERRORI: nuovi (ERR-* creati) · noti ripetuti (RECIDIVA! escalation) · near-miss
6. SCOSTAMENTI: cosa è diverso dalla run precedente / dalla media
7. AZIONI: migliorie assegnate (owner, scadenza)
8. VERDETTO ISPETTORATO: 1 riga secca
```

## 9. PILOTA = PREVENTIVOFORGE (colma il buco rilevato il 2026-07-03)

PreventivoForge oggi ha checkpoint scritti a mano ma ZERO telemetria automatica. È il pilota
perfetto: run frequenti, gate già esistenti (6), storico già cablato (sidecar JSON).
Cablaggio minimo (Half A, quindi Max): `run.py` scrive `telemetry/runs/preventivo-forge/
<run-id>.jsonl` (step, gate, exit, durate) + a fine run genera il run-report dal template §8.
KPI PF: successo run, 6/6 gate al 1° colpo, durata, foto ≥ soglia, € API=0, RECIDIVE=0.

## 10. PIANO DI BUILD — FASI DI MAX (M1→M5, metodo 9 passi ognuna)

| Fase | Contenuto | Gate di uscita |
|---|---|---|
| **M1 — Fondamenta dati** | struttura `company/Ispettorato/` + REGISTRO-ERRORI (migrando KNOWN ERRORS di Empire Studio + lezioni già in Memory: collisione naming CP-20260616-001, collisioni PDF 2026-07-02, swarm morto per session-limit…) + definizione KPI PF | struttura completa 0 vuote · registro con ≥5 ERR reali migrati |
| **M2 — Pilota PreventivoForge** | trace JSONL in `run.py` + generatore run-report (script) + prova su run reale | 1 run reale → report completo §8 auto-generato |
| **M3 — Reparto CF-grade** | 11 agenti (§5) + 5 workflow (§7) via FORGE, swarm idempotente Title-Case | struct-gate: 11 agenti/4 WF/0 magri/0 stub + 5-bis MAXIMILIAN |
| **M4 — Aggancio Impero** | RECALL/RETRO aggiornati (dossier 10) + handoff con MAXIMILIAN, Board, Sentinelle, CF-R8 + daily attivo | 1 WF-DAILY-AUTOCRITICA prodotto su dati veri · dossier 10 aggiornato |
| **M5 — Estensione** | telemetria su outreach + prossimi workflow · report settimanale a Max · (opz.) hook Claude Code post-run | 2° workflow cablato · 1 RECIDIVA-GATE provato (test negativo simulato) |

**Regole di build:** ogni fase = ciclo 9 passi + CP + STATO + push. Budget-guard 20%.
Gael NON coinvolto (resta su Impero V2-2/V2-3); l'Ispettorato però AUDITERÀ anche il suo lavoro
una volta attivo. Coordinamento: blocco ⚠️ in STATO-EMPIRE prima di M3 (swarm).

## 11. CRITERIO DI SUCCESSO FINALE (quando l'Ispettorato "esiste")

1. Nessuna run senza run-report (automatico, non a mano).
2. Daily autocritica prodotta ogni giorno di attività, indirizzata a Max.
3. REGISTRO-ERRORI unico, vivo, consultato nel RECALL di ogni fase.
4. Un errore ripetuto viene BLOCCATO dal gate recidiva (provato con test negativo).
5. Board/MAXIMILIAN ricevono i report e le loro decisioni tornano a terra tracciate.

---
*Dossier 15 · standard v2 · owner MAX · collegati: 10-METODO, 11-DIRETTIVA-SCALA, 12-MAXIMILIAN, 13-MANDATO.*
