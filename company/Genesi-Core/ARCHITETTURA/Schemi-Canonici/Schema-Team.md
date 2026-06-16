# SCHEMA CANONICO — Team

> Forma MEDIO-PESANTE. Insieme di agenti che si coordinano per un obiettivo, con contratto di
> handoff e stato condiviso. Motore reale: shape `team` (P06), `T-org-design`, `T-handoff-contracts`,
> `swarm-orchestration`. Più piccolo di un Reparto (nessuna missione organizzativa permanente).

## Quando si usa questa forma (e quando NO → quale altra forma)
- **USA** quando un obiettivo richiede ≥2 ruoli disgiunti che si passano lavoro (coordinator +
  workers, o pipeline). È la "regola madre" CF: coordinator, I/O espliciti, acceptance, escalation.
- **NO se** un solo ruolo basta → **Agente**. NO se è un'unità organizzativa permanente con KPI di
  reparto e più team dentro → **Reparto**. NO se è solo una sequenza di passi senza "chi" stabile
  → **Workflow**.

## Struttura obbligatoria (sezioni/campi al millimetro)
1. **Topologia**: supervisor | pipeline | peer-to-peer | hub-spoke | hybrid (dichiarata).
2. **Coordinator**: se topologia ∈ {supervisor, hub-spoke} — chi instrada e sintetizza.
3. **Workers** (`agents/`): ≥2 agenti, ognuno con ≥5/7 campi dello Schema-Agente (I/O JSON incluso).
4. **Handoff contract**: per ogni passaggio → `{mittente, destinatario, payload schema, precondizioni}`.
   RACI strict: 1 solo Responsible per responsabilità.
5. **`shared_state` schema**: i campi che il team legge/scrive, con tipo e owner di scrittura.
6. **Acceptance**: condizioni binarie che dichiarano "il team ha finito bene".
7. **Failure handling**: ≥5 failure mode con rilevazione + recupero (retry/escalation/abort).
8. **Connessioni**.

## Template vuoto (copiabile)
```
<team-slug>/
├── topology.md            # supervisor|pipeline|peer|hub-spoke|hybrid
├── coordinator.md         # se supervisor/hub-spoke
├── agents/                # ≥2 agenti (Schema-Agente, ≥5/7 campi)
├── handoff_rules.md       # RACI strict, payload schema per handoff
├── shared_state.md        # campi {nome, tipo, owner_scrittura}
├── acceptance.md          # condizioni binarie di "done"
├── failure_handling.md    # ≥5 failure mode
└── README.md
```
```json
// handoff contract (un passaggio)
{ "from": "agent-A", "to": "agent-B", "payload": {"spec": "...", "vincoli": []}, "precondizioni": ["spec validata"] }
```

## Checklist di completezza (per struct-gate)
- [ ] **Topologia** dichiarata esplicitamente.
- [ ] Se supervisor/hub-spoke → esiste il **coordinator** definito.
- [ ] ≥2 **workers**, ognuno con I/O JSON (≥5/7 campi Schema-Agente).
- [ ] **Handoff contract** con payload schema + precondizioni per ogni passaggio.
- [ ] RACI strict: 1 solo Responsible per ogni responsabilità (nessuna ambiguità).
- [ ] **shared_state** definito con tipo e owner di scrittura per ogni campo.
- [ ] **Acceptance** con condizioni binarie.
- [ ] **Failure handling** con ≥5 failure mode (rilevazione + recupero).
- [ ] **Connessioni** ≥3 cross-link.

## Esempio minimo compilato
Team `blueprint-pipeline` (pipeline). Workers: arch-spec-writer → arch-blueprint → arch-validator.
Handoff 1: spec-writer→blueprint `{spec, out_of_scope}` precond. "spec completa". shared_state:
`{richiesta:str (owner director), blueprint:obj (owner blueprint), validazione:enum (owner validator)}`.
Acceptance: validazione==PASS ∧ blueprint non vuoto. Failure: spec incompleta→torna a spec-writer;
blueprint collide→arch-contradiction; 2 retry falliti→escalation director. → COMPLETO.

## Anti-pattern (cosa rende lo schema NON valido)
- Handoff descritti a parole senza payload schema → i worker non sanno cosa ricevono.
- Più Responsible per la stessa responsabilità → conflitti, lavoro doppio/perso.
- Manca `shared_state` → gli agenti si parlano "a voce", nessuna fonte di verità.
- Nessuna acceptance → il team non sa quando ha finito.
- Trattare come Team ciò che è un Reparto (manca la cornice organizzativa permanente) o viceversa.

## Connessioni
- [[Schema-Agente]] — ogni worker segue questo schema
- [[Schema-Reparto]] — quando il team è parte di un'unità organizzativa permanente
- [[Schema-Workflow]] — il "come" eseguibile che un team può incarnare
- [[README]] — principio della FORMA GIUSTA · 14-DOSSIER-ARCHITETTURA §2 (reparti L2)
