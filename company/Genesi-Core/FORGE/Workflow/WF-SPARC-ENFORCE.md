# WF-SPARC-ENFORCE
## sparc-methodology su ogni build non banale (governance R→C della FORGE)

> Organo: FORGE (Genesi Core) · Reparto owner: L2.5 METHOD-GUARD · Stato: DEFINED
> Garantisce che ogni build **non banale** della FORGE segua SPARC (S→P→A→R→C) e che i pattern
> non negoziabili restino vivi. NB di confine: la fase **A (Architecture) NON la esegue la FORGE** —
> è ARCHITETTURA che produce il blueprint validato (HC-ARCH-FORGE); SPARC-ENFORCE presidia che la
> build FORGE entri da R (Refinement) solo con A già chiusa e PASS. Gate: `frg-sparc-warden`.
> Collega: [[WF-ARCH-DESIGN]] · [[WF-FORGE-PIPELINE]]

---

## Trigger
- Ogni build FORGE non banale (skill/agente/team/workflow/ecosistema nuovi, feature, refactor di interfacce).
- `frg-sparc-warden` intercetta l'avvio di WF-SKILL-NEW / WF-AGENT-NEW / WF-TEAM-NEW / WF-ECOSYSTEM-NEW / WF-FORGE-PIPELINE.
- Variante Claude Browser: motore `omega-create` in fase R (le fasi SPARC restano identiche).
- **Natura:** non costruisce — è il guardiano che blocca i salti di fase, non li annota.

---

## Input (JSON)
```json
{
  "build_id": "ARCH-2026-0617-014",
  "blueprint_ref": "architettura/blueprint/ARCH-2026-0617-014",
  "validazione_arch": "PASS",
  "forma": "skill | agente | team | workflow | ecosistema",
  "classe": "banale | non-banale",
  "committente": "frg-chief"
}
```
- `validazione_arch != PASS` → la fase A non è chiusa → R bloccata (non si può raffinare senza architettura).

---

## Classificazione "banale vs non banale"
**Banale → fast-track (SPARC non richiesto):** fix 1-2 righe, update config/metadata, entry in lista esistente.
**Non banale → SPARC obbligatorio:** nuova skill/agente/team/workflow/ecosistema, feature nuova, refactor di interfacce, integrazione cross-ecosistema.
In caso di dubbio: `frg-sparc-warden` classifica consultando `frg-chief`.

---

## Pipeline (passi · fase SPARC · gate)
```
S — Specification   (agent-specification · frg-spec-writer)   → spec completa: requisiti, acceptance, out-of-scope
P — Pseudocode/Plan (agent-planner ‖ agent-researcher)        → piano + ricerca completata
A — Architecture    *** ARCHITETTURA, non FORGE ***           → blueprint validato = HC-ARCH-FORGE (PASS)
                    (frg-sparc-warden verifica solo che A sia chiusa e PASS prima di aprire R)
R — Refinement      (agent-coder + agent-tester · frg-eval-runner) → implementazione + test (≥1 ciclo)
C — Completion      (agent-reviewer + frg-sparc-warden)        → review schema canonico + pattern non negoziabili
```
**Salto di fase rilevato → build BLOCCATA (non annotata).** Si riparte dalla fase mancante.

---

## Gate
- **G-A-CHIUSA (confine):** R non si apre senza `validazione_arch=PASS`. La FORGE non architetta — riceve la A da ARCHITETTURA.
- **G-NO-SKIP:** ogni fase ha il suo gate; salto rilevato → blocco, non deroga silenziosa.
- **G-CANONICO (a Completion):** schema canonico rispettato (coordinator+workers+I/O+acceptance+escalation).
- **G-KERNEL:** progressive disclosure — kernel ≤500 righe (count righe).
- **G-INVARIANTI:** invarianti cardinali scritti esplicitamente nell'artefatto; memory-first (CP dopo task chiuso).
- **G-DEROGA-LOGGATA:** ogni deroga richiesta è loggata in `forge/decisions/` (mai deroghe silenziose).

---

## Pattern non negoziabili verificati a Completion
| # | Pattern | Verifica |
|---|---|---|
| 1 | Un team per funzionalità (coordinator+workers) | org chart presente |
| 6 | Skill = knowledge layer (agenti non inglobano conoscenza da skill) | nessun duplicato skill→agente |
| 7 | Progressive disclosure (kernel ≤500 righe) | count righe |
| 8 | Invarianti cardinali espliciti | sezione "invarianti" presente |
| 13 | Memory-first (checkpoint dopo ogni task chiuso) | CP creato |

---

## Output (JSON)
```json
{
  "build_id": "ARCH-2026-0617-014",
  "classe": "non-banale",
  "fasi_passate": ["S", "P", "A(arch)", "R", "C"],
  "salti_rilevati": 0,
  "pattern_check": "PASS",
  "deroghe_loggate": [],
  "esito": "CLEARED",
  "handoff_to": "frg-chief → consegna"
}
```

---

## Handoff
- **In ingresso:** segnalazione di avvio build da `frg-chief` + `blueprint_ref` con `validazione_arch`.
- **In uscita:** esito `CLEARED` a `frg-chief` (la build può consegnare a **MAXIMILIAN → Mandato → Identity-HR**); esito `BLOCKED` → ritorno alla fase mancante. Audit mensile dei rilasci → `forge/evals/sparc-audit-YYYYMMDD.md` + segnalazione Drift-Sentinel se deviazioni.
- **Confine:** SPARC-ENFORCE non scrive contenuto e non architetta — presidia il metodo lungo l'intera catena.

---

## Dry-run
Build non banale di una skill. frg-sparc-warden verifica: S chiusa (spec), P chiusa (piano+ricerca),
A = blueprint ARCHITETTURA con `validazione=PASS` (altrimenti R bloccata), R = draft+eval ≥1 ciclo,
C = review schema canonico + kernel ≤500 + invarianti presenti. Zero salti → esito CLEARED a frg-chief.
Caso blocco: build entra in R senza A PASS → BLOCKED, ritorno ad ARCHITETTURA.

---

## Connessioni
- [[WF-ARCH-DESIGN]] — produce la fase A (blueprint validato) che SPARC-ENFORCE pretende chiusa prima di R
- [[WF-FORGE-PIPELINE]] · [[WF-SKILL-NEW]] · [[WF-AGENT-NEW]] · [[WF-TEAM-NEW]] · [[WF-ECOSYSTEM-NEW]] — le build presidiate
- [[frg-sparc-warden]] · [[frg-spec-writer]] · [[frg-eval-runner]] — agenti owner (+ i 7 agenti SPARC)
- [[06-ECOSISTEMI-CORE]] §07 L2.5 METHOD-GUARD — fonte di verità
- OPERATIONS/WF-CRON — pianifica l'audit mensile SPARC
