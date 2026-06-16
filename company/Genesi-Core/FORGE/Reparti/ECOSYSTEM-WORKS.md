# ECOSYSTEM-WORKS — FORGE (Genesi Core)

## Missione (confine: FORGE costruisce CONTENUTO, ARCHITETTURA dà la STRUTTURA)
Forgia il **contenuto** di interi ecosistemi L1 quando la holding entra in un nuovo
territorio (es. F9+: E-commerce). ARCHITETTURA, via **WF-ECOSYSTEM-DESIGN** (L2.5), consegna
l'**org chart L1→L5 disegnata al millimetro** — reparti vuoti, workflow vuoti, roster previsti,
BACKBONE/namespace progettati, matrice di confine con gli altri 9 ecosistemi. ECOSYSTEM-WORKS
ci scrive dentro: missioni reali, contenuto dei reparti, system prompt dei roster, dossier.
È il livello massimo della forgiatura e nasce **solo su mandato Board**. Regola: tutto o niente.

## Team agenti (quali frg-* lavorano qui)
| id | ruolo | tier |
|---|---|---|
| `frg-org-designer` | incarna reparti/team dell'eco nuovo dentro l'org disegnata da ARCHITETTURA | opus |
| `frg-mkd-forger` | scrive il dossier dell'ecosistema (PRD tipo A / MKD) | sonnet |
| `frg-skill-smith` | forgia o mappa le skill proprie dell'ecosistema | sonnet |
| `frg-hr-registrar` | registra il roster L5 in Identity-HR + cost model OPERATIONS | haiku |
| `frg-chief` | Chief-Forge: riceve il mandato Board, orchestra, consegna o rollback | opus |

## Workflow di competenza
- **WF-ECOSYSTEM-NEW** — org disegnata da ARCHITETTURA (L2.5) → contenuto completo dell'ecosistema: ECOSISTEMA.md + BACKBONE.md popolati, reparti L2 reali, workflow L3, roster L5, dossier PIANO-MAESTRO, namespace memoria inizializzato, registrazioni. Tutto-o-niente: o tutti i deliverable, o rollback.

## Funzioni L4 (riusa quelle di AGENT-WORKS, a scala maggiore)
1. **T-org-incarnate** — riempie l'org chart disegnata con missioni e contenuto reale dei reparti.
2. **T-backbone-fill** — popola BACKBONE.md (topologia swarm, namespace memoria, handoff inter-eco).
3. **T-roster-cast** — incarna i roster L5 (delega a AGENT-WORKS WF-AGENT-NEW/WF-TEAM-NEW).
4. **T-dossier-write** — scrive il dossier PIANO-MAESTRO come MKD/PRD tipo A (delega a WORKFLOW-WORKS).
5. **T-namespace-init** — inizializza il namespace memoria dedicato (`ruflo memory init --namespace <eco>`).

## Handoff Contract
- **Riceve** da ARCHITETTURA (**HC-ARCH-FORGE** ramo ecosistemi, da WF-ECOSYSTEM-DESIGN): `{request_id, org_blueprint_ref, schema_usato:"ecosistema@vN", backbone_design, matrice_confine, validazione:"PASS"}`. Committente a monte: **Board (L0)**.
- **Costruisce**: il contenuto completo dell'ecosistema dentro la forma. Buco strutturale → ritorno ad ARCHITETTURA (mai improvvisare struttura).
- **Consegna** a MAXIMILIAN → Mandato → registro (roster + skills-map + dossier + ADR in 10 MEMORY). Output: ecosistema VIVO o rollback.

## Flusso interno (passi reali)
```
mandato Board (L0) ratificato → ARCHITETTURA WF-ECOSYSTEM-DESIGN → org_blueprint (PASS)
  → frg-chief: mandato completo? (missione, revenue, DONE WHEN, budget, sponsor) — no → respinge
  → frg-org-designer: incarna reparti/workflow dentro l'org disegnata
  → frg-skill-smith + AGENT-WORKS: forgia skill + roster L5 (delega ai workflow specifici)
  → frg-mkd-forger + WORKFLOW-WORKS: scrive dossier (PRD A) + BACKBONE
  → T-namespace-init: namespace memoria dedicato
  → dry-run: struttura navigabile, handoff coerenti, verify verde PRIMA del primo agente reale
  → frg-hr-registrar: registro roster + cost model + ADR in company/Memory/decisions/
  → consegna a MAXIMILIAN → Mandato → VIVO  (oppure rollback: tutto-o-niente)
Output: company/Ecosistemi/<NN-ECO>/ completo + registrazioni
```

## Gate
- **G-SPEC** — mandato Board completo e org_blueprint validato (no mandato → no scaffold).
- **G-MKD/PRD** — dossier come PRD tipo A con quality score ≥ 75; matrice di confine completa.
- **G-EVAL** — dry-run dello scaffold PASS (navigabile, handoff coerenti) prima di spawnare il primo agente.
- **G-CONTRADICTION** — nessun overlap con gli altri 9 ecosistemi (matrice anti-overlap esplicita).
- **G-REGISTRY** — roster in Identity-HR + skills-map + dossier + ADR (decisione di creazione = ADR in 10 MEMORY).

## shared_state / memoria (namespace forge/...)
- `forge/queue/ecosystem/<request_id>` — mandato Board + org_blueprint in coda.
- `forge/builds/ecosystem/<request_id>` — deliverable in costruzione (tutto-o-niente, rollback tracciato).
- `forge/registry/ecosystems` — ecosistemi creati, stato, namespace, dossier_ref.
- `<eco>/...` — namespace memoria dedicato del nuovo ecosistema, inizializzato da T-namespace-init.

## KPI
| KPI | Target |
|---|---|
| Ecosistemi consegnati completi (tutto-o-niente, no mezzi scaffold) | 100% |
| Dry-run scaffold PASS prima del primo agente reale | 100% |
| Matrice di confine con gli altri 9 ecosistemi presente | 100% |
| Divergenze dal template d'ecosistema (drift) | 0 |
| Decisione di creazione tracciata come ADR (10 MEMORY) | 100% |

## Connessioni
- [[../../ARCHITETTURA/Workflow/WF-ECOSYSTEM-DESIGN]] — disegna l'org L1→L5 che questo reparto incarna
- [[../../ARCHITETTURA/Schemi-Canonici/Schema-Ecosistema]] — la forma pesante che questo reparto riempie
- [[AGENT-WORKS]] — fornisce roster L5 e team canonici dell'eco nuovo
- [[WORKFLOW-WORKS]] — il dossier nasce come MKD/PRD tipo A
- [[../../../Ecosistemi/07-FORGE/Reparti/ECOSYSTEM-WORKS/README]] — stub v1 di questo reparto

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §07 L2 ECOSYSTEM-WORKS + 14-DOSSIER-ARCHITETTURA · Standard CF-grade · 2026-06-16*
