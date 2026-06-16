# WF-SKILL-AUDIT
## skill-contradiction-analyzer su set di skill (gate anti-drift)

> Organo: FORGE (Genesi Core) · Reparto owner: L2.1 SKILL-WORKS · Stato: DEFINED
> Rileva contraddizioni, duplicazioni e drift tra le skill della holding — prima del rilascio
> (gate G-CONTRADICTION dentro WF-SKILL-NEW e WF-SKILL-IMPROVE) o periodicamente sull'intero set.
> Non riceve un blueprint: è un **gate trasversale** invocato dagli altri workflow e da OPERATIONS.
> Strumento: `skill-contradiction-analyzer`. Collega: [[WF-SKILL-NEW]] · [[WF-SKILL-IMPROVE]]

---

## Trigger
- Chiamato come gate da `WF-SKILL-NEW` (passo 6) e `WF-SKILL-IMPROVE` (passo 5) prima della consegna.
- Audit periodico trimestrale sull'intero set di skill (pianificato da OPERATIONS/WF-CRON).
- Due skill dello stesso dominio aggiornate in cicli ravvicinati (rischio divergenza).
- Richiesta del Drift-Sentinel (Backbone) su anomalie nell'output di skill correlate.
- **Natura:** non produce artefatti — produce un verdetto che condiziona i rilasci.

---

## Input (JSON)
```json
{
  "audit_id": "AUDIT-2026-Q3",
  "scope": "singola | coppia | set-tematico | full",
  "skill_target": ["skill-a", "skill-b"],
  "trigger": "gate-WF-SKILL-NEW | gate-WF-SKILL-IMPROVE | cron-trimestrale | drift-sentinel",
  "committente": "frg-chief | OPERATIONS/WF-CRON | Drift-Sentinel"
}
```
- Niente `blueprint_ref`: questo workflow è un gate, non una build di forma nuova.

---

## Pipeline (passi · agente owner)
```
1. SELEZIONE SCOPE                     (frg-contradiction-gate ← frg-chief)
   └── definisce il set da auditare (singola / coppia / set tematico / full skills-map.yaml)

2. SCAN ANALYZER                        (frg-contradiction-gate · skill-contradiction-analyzer)
   └── analyzer su ogni coppia/set → report JSON con contraddizioni classificate per severità

3. TRIAGE                               (frg-contradiction-gate + frg-chief)
   └── classifica: BLOCCANTE / WARNING / INFORMATIVA (vedi tabella)

4. RISOLUZIONE BLOCCANTI                (frg-skill-smith → WF-SKILL-NEW / WF-SKILL-IMPROVE)
   └── ogni bloccante torna al workflow di fix; rilascio fermo finché non risolto

5. SEGNALAZIONE WARNINGS                (frg-hr-registrar)
   └── issue in forge/evals/; Drift-Sentinel notificato se impatta lo schema canonico

6. REPORT + CONSEGNA                     (frg-contradiction-gate)
   └── audit-report.md in forge/evals/ + entry wiki/log.md · esito a MAXIMILIAN/Board se trimestrale
```

---

## Classificazione contraddizioni
| Severità | Definizione | Azione |
|---|---|---|
| **BLOCCANTE** | Due skill affermano comportamenti opposti per lo stesso input; una nega un invariante dell'altra | Blocca il rilascio; risoluzione PRIMA di ship |
| **WARNING** | Overlap di funzione (rischio duplicazione) o linguaggio inconsistente | Log + segnalazione; risolto nel ciclo successivo |
| **INFORMATIVA** | Differenze stilistiche/naming, semantica coerente | Registrata per il ciclo di standardizzazione |

---

## Gate
- **G-CONTRADICTION (il gate che questo workflow È):** verdetto VERDE = nessun bloccante → via libera al rilascio chiamante.
- **G-BLOCK:** ≥1 contraddizione BLOCCANTE → rilascio fermo; ritorno a WF-SKILL-NEW/IMPROVE per fix.
- **G-COVERAGE (trimestrale):** audit full copre il 100% dello skills-map.yaml.
- **G-ARCHIVE:** ogni audit lascia audit-report.md in `forge/evals/` (archivio per trend analysis).

---

## Output (JSON)
```json
{
  "audit_id": "AUDIT-2026-Q3",
  "scope": "full",
  "skill_auditate": 124,
  "bloccanti": 0,
  "warnings": 3,
  "informative": 11,
  "verdetto": "VERDE",
  "report_ref": "forge/evals/contradiction-report-2026Q3.md",
  "handoff_to": "frg-chief → MAXIMILIAN/Board (se trimestrale)"
}
```

---

## Handoff
- **In ingresso:** chiamata di gate da WF-SKILL-NEW / WF-SKILL-IMPROVE, o trigger cron da OPERATIONS/WF-CRON, o Drift-Sentinel.
- **In uscita:** verdetto al workflow chiamante (via libera o stop); report trimestrale a **frg-chief → MAXIMILIAN → Board** (C-Suite) con notifica Drift-Sentinel; bloccanti → WF-SKILL-NEW/IMPROVE per fix.
- **Confine:** non costruisce né modifica skill — i fix passano sempre dai workflow di build, mai qui.

---

## Dry-run
Gate invocato da WF-SKILL-NEW su `battle-card-forge` vs le 6 skill competitor-* esistenti. Analyzer →
0 bloccanti, 1 warning (overlap parziale con `competitors`) → verdetto VERDE, warning loggato in
forge/evals/, via libera al rilascio. Caso trimestrale: scan full su 124 skill → 0 bloccanti, report
`contraddizioni-2026Q3.md` archiviato → esito a frg-chief → Board.

---

## Connessioni
- [[WF-SKILL-NEW]] · [[WF-SKILL-IMPROVE]] — chiamano questo workflow come gate prima di consegnare
- [[WF-ARCH-DESIGN]] — il gemello a monte ha `arch-contradiction` (anti-collisione strutturale); qui è anti-drift di contenuto
- [[frg-contradiction-gate]] · [[frg-skill-smith]] · [[frg-hr-registrar]] — agenti owner
- [[06-ECOSISTEMI-CORE]] §07 L2.1 SKILL-WORKS — fonte di verità
- OPERATIONS/WF-CRON — pianifica l'audit trimestrale
