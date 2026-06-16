# WF-AGENT-NEW
## Blueprint agente (da ARCHITETTURA) → agente 7-file testato e registrato in HR

> Organo: FORGE (Genesi Core) · Reparto owner: L2.2 AGENT-WORKS · Stato: DEFINED
> Riceve un **blueprint agente validato** da ARCHITETTURA (HC-ARCH-FORGE, schema `agente@v1`) e ci
> scrive il CONTENUTO: i 7 file canonici dell'agente. Mai inventa il ruolo né l'I/O — arrivano già
> architettati e PASS. Motori reali: `architect-agent` / `agent-factory`.
> Collega: [[WF-ARCH-DESIGN]] · [[WF-FORGE-PIPELINE]] · [[WF-TEAM-NEW]]

---

## Trigger
- Arriva da ARCHITETTURA un blueprint con `forma_scelta = "agente"` (HC-ARCH-FORGE).
- `WF-TEAM-NEW` richiede i singoli membri di un team canonico (uno spawn per worker/coordinator).
- Roster di un ecosistema previsto ma non ancora reale (build FORGE F1-F5).
- **Natura:** specializzazione "agente" di WF-FORGE-PIPELINE; ogni agente nasce con smoke test e voce HR.

---

## Input (JSON)
```json
{
  "request_id": "ARCH-2026-0617-021",
  "blueprint_ref": "architettura/blueprint/ARCH-2026-0617-021",
  "schema_usato": "agente@v1",
  "forma_scelta": "agente",
  "spec_ref": "architettura/blueprint/ARCH-2026-0617-021#spec",
  "validazione": "PASS",
  "ruolo": "battle-card writer per AGENCY",
  "tier_proposto": "haiku",
  "costo_stimato_run_usd": 0.00,
  "team_padre": "T-battle-card | null"
}
```
- `validazione != PASS` → rigetto ad ARCHITETTURA. Nessun agente costruito al buio.

---

## Pipeline (passi · agente owner)
```
1. APERTURA + MEMORIA CHECK           (frg-chief → frg-spec-writer)
   └── verifica PASS; cerca in forge/registry (AgentDB): agente affine con pass_rate alto? → estendi, non duplicare

2. BUILD 7-FILE                       (frg-org-designer · architect-agent/agent-factory)
   └── riempie i 7 file canonici DENTRO la struttura del blueprint (ruolo/I/O/tier già definiti da ARCH):
        identity · prompt (kernel ≤500 righe) · io · reasoning · tools · handoff · memory

3. SMOKE TEST                         (agente stesso + frg-eval-runner)   →  G-SMOKE
   └── 1 task reale piccolo eseguito: output conforme all'acceptance del blueprint, zero errori

4. TIER + BUDGET PRE-APPROVAL         (frg-hr-registrar → OPERATIONS)
   └── tier al ribasso (target ≥70% Haiku); costo/run dichiarato a OPERATIONS budget-guard

5. CONTRADICTION (ruolo)              (frg-contradiction-gate)
   └── il ruolo non collide/duplica un agente esistente → VERDE

6. CONSEGNA + REGISTRO HR             (frg-hr-registrar + frg-chief)
   └── record in registro-agenti.yaml (tier, costo, KPI, stato=active) · handoff a MAXIMILIAN → Mandato → HR
```

---

## 7-file canonici (schema `agente@v1` di ARCHITETTURA)
```
<agente-id>/
├── identity.md   — ID, ruolo, tier, organo, reparto, team
├── prompt.md     — system prompt (kernel ≤500 righe)
├── io.md         — input attesi, output prodotti, formato handoff
├── reasoning.md  — decision tree (come ragiona, sequenza passi)
├── tools.md      — skill/tool usati, con condizioni d'uso
├── handoff.md    — escalation protocol, chi chiama se stuck
└── memory.md     — namespace/chiavi store-search nel Brain
```

---

## Gate
- **G-FORGE0:** `validazione != PASS` → rigetto ad ARCHITETTURA.
- **G-SMOKE:** un agente mai testato non entra in registro (smoke test verde obbligatorio).
- **G-TIER:** parte dal modello più economico che regge il task (≥70% roster su Haiku o inferiore).
- **G-BUDGET:** costo/run dichiarato e tier confermato disponibile da OPERATIONS prima dell'attivazione.
- **G-REGISTRY:** nascita = registro + budget; agente running non anagrafato = 0. Un agente, un ruolo (no drift).

---

## Output (JSON)
```json
{
  "request_id": "ARCH-2026-0617-021",
  "agente_id": "agy-battle-card-writer",
  "artefatto_path": "company/Ecosistemi/01-AGENCY/Agenti/agy-battle-card-writer/",
  "build_ref": "forge/builds/ARCH-2026-0617-021",
  "tier": "haiku",
  "smoke_test": "PASS",
  "contraddizioni": "VERDE",
  "handoff_to": "MAXIMILIAN",
  "status": "delivered"
}
```

---

## Handoff
- **In ingresso:** HC-ARCH-FORGE da `WF-ARCH-DESIGN` (blueprint agente validato, schema `agente@v1`).
- **In uscita:** consegna a **MAXIMILIAN** (all'altezza?) → **Mandato** (lecito?) → **Identity-HR** (registro-agenti.yaml) → VIVO. Se figlio di un team → ritorno a `WF-TEAM-NEW` per integration test.
- **Confine:** ARCHITETTURA fissa ruolo/I/O/tier; AGENT-WORKS riempie i 7 file. Cambio di ruolo = nuovo giro ARCH.

---

## Dry-run
Blueprint validato di `agy-battle-card-writer` (schema `agente@v1`, tier haiku). frg-org-designer riempie
i 7 file dentro la forma data, l'agente esegue 1 smoke task reale (genera una battle-card da URL) con
output conforme, OPERATIONS conferma costo/run ~$0, contradiction VERDE, frg-hr-registrar lo iscrive in
registro-agenti.yaml → consegna a MAXIMILIAN. Test-amnesia: `build_ref` ricostruibile a freddo.

---

## Connessioni
- [[WF-ARCH-DESIGN]] — produce il blueprint agente in ingresso
- [[WF-TEAM-NEW]] — chiama questo workflow per ogni membro del team
- [[WF-FORGE-PIPELINE]] — motore generale · [[WF-SPARC-ENFORCE]] — governance R→C della build
- [[frg-org-designer]] · [[frg-spec-writer]] · [[frg-eval-runner]] · [[frg-hr-registrar]] — agenti owner
- [[06-ECOSISTEMI-CORE]] §07 L2.2 AGENT-WORKS — fonte di verità
