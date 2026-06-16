# WF-TEAM-NEW
## Blueprint team (da ARCHITETTURA) → team canonico operativo (coordinator + workers)

> Organo: FORGE (Genesi Core) · Reparto owner: L2.2 AGENT-WORKS · Stato: DEFINED
> Riceve un **blueprint team validato** da ARCHITETTURA (HC-ARCH-FORGE, schema `team@v1`: org chart,
> handoff contract, shared_state) e ci costruisce il CONTENUTO: spawna i membri (via WF-AGENT-NEW),
> cabla gli handoff, integration-test. Mai inventa l'org chart — arriva già architettato e PASS.
> Collega: [[WF-ARCH-DESIGN]] · [[WF-AGENT-NEW]] · [[WF-FORGE-PIPELINE]]

---

## Trigger
- Arriva da ARCHITETTURA un blueprint con `forma_scelta = "team"` (HC-ARCH-FORGE).
- Un ecosistema dichiara un workflow L3/funzione L4 senza team assegnato.
- `WF-ECOSYSTEM-NEW` richiede i team L4 dell'ecosistema nuovo.
- **Natura:** il team è l'unità operativa fondamentale (pattern #1): nessuna funzionalità coperta da un agente solitario senza escalation.

---

## Input (JSON)
```json
{
  "request_id": "ARCH-2026-0617-033",
  "blueprint_ref": "architettura/blueprint/ARCH-2026-0617-033",
  "schema_usato": "team@v1",
  "forma_scelta": "team",
  "spec_ref": "architettura/blueprint/ARCH-2026-0617-033#spec",
  "validazione": "PASS",
  "org_chart": { "coordinator": "ruolo", "workers": ["ruolo-1", "ruolo-2"], "reviewer": "opzionale" },
  "shared_state_namespace": "intelligence/T-thumbnail",
  "ecosistema": "05-MULTI-BUSINESS"
}
```
- `validazione != PASS` → rigetto ad ARCHITETTURA. Nessun team costruito al buio.

---

## Pipeline (passi · agente owner)
```
1. APERTURA + LETTURA ORG-CHART       (frg-chief → frg-org-designer)
   └── verifica PASS; carica org chart dal blueprint (ruoli, confini, una sola responsabilità per worker)

2. SPAWN MEMBRI                        (frg-spec-writer + WF-AGENT-NEW, in parallelo)
   └── per ogni membro (coordinator + N workers + reviewer opz.) → WF-AGENT-NEW (7-file + smoke test)

3. CABLAGGIO HANDOFF + SHARED-STATE    (frg-org-designer)
   └── handoff contract coordinator↔workers e verso l'esterno (schema HC-v1) · shared_state namespace tipato

4. INTEGRATION TEST                    (frg-eval-runner)   →  G-INTEGRATION
   └── 1 task reale attraversa l'intero team end-to-end → output conforme all'acceptance del team

5. CONTRADICTION (team)                (frg-contradiction-gate)
   └── il team non duplica un team esistente nello stesso dominio → VERDE

6. CONSEGNA + REGISTRO                  (frg-hr-registrar + frg-chief)
   └── tutti i membri in registro-agenti.yaml · team in ECOSISTEMA.md · handoff a MAXIMILIAN → Mandato → HR
```

---

## Schema handoff contract del team (schema `team@v1` di ARCHITETTURA)
```json
{
  "team_id": "T-nome-team",
  "ecosistema": "XX-ECO",
  "coordinator": "agente-id-coordinator",
  "workers": ["agente-id-1", "agente-id-2"],
  "input_trigger": "cosa attiva il team",
  "acceptance_criteria": ["criterio 1 misurabile", "criterio 2 misurabile"],
  "escalation": "a chi va il task se fallisce dopo N tentativi",
  "shared_state_namespace": "namespace/team-id"
}
```

---

## Gate
- **G-FORGE0:** `validazione != PASS` → rigetto ad ARCHITETTURA.
- **G-ROLES:** ruoli non sovrapposti; ogni worker una sola responsabilità (no drift) — verificato da `frg-org-designer`.
- **G-MEMBERS:** ogni membro ha smoke test verde (eredita G-SMOKE di WF-AGENT-NEW) prima dell'integration test.
- **G-INTEGRATION:** task end-to-end conforme all'acceptance criteria del team, altrimenti iterazione.
- **G-ESCALATION:** team senza escalation protocol definito = 0; acceptance criteria sempre misurabili.

---

## Output (JSON)
```json
{
  "request_id": "ARCH-2026-0617-033",
  "team_id": "T-thumbnail",
  "ecosistema": "05-MULTI-BUSINESS",
  "membri": ["mb-thumb-coordinator", "mb-thumb-designer", "mb-thumb-qa"],
  "build_ref": "forge/builds/ARCH-2026-0617-033",
  "integration_test": "PASS",
  "contraddizioni": "VERDE",
  "handoff_to": "MAXIMILIAN",
  "status": "delivered"
}
```

---

## Handoff
- **In ingresso:** HC-ARCH-FORGE da `WF-ARCH-DESIGN` (blueprint team validato, schema `team@v1`).
- **In sub-flusso:** `WF-AGENT-NEW` per ogni membro (ritorna i 7-file testati).
- **In uscita:** consegna a **MAXIMILIAN** (all'altezza?) → **Mandato** (lecito?) → **Identity-HR** (registra membri + team) → VIVO.
- **Confine:** ARCHITETTURA disegna org chart/handoff/shared_state; AGENT-WORKS spawna e cabla. Cambio di org chart = nuovo giro ARCH.

---

## Dry-run
Blueprint validato di `T-thumbnail` (coordinator + designer + qa, schema `team@v1`, shared_state
`intelligence/T-thumbnail`). I 3 membri nascono via WF-AGENT-NEW con smoke verde, frg-org-designer cabla
gli handoff, frg-eval-runner fa passare 1 task reale (genera 3 thumbnail YT a partire da un brief)
end-to-end conforme, contradiction VERDE → consegna a MAXIMILIAN. Test-amnesia: ricostruibile a freddo.

---

## Connessioni
- [[WF-ARCH-DESIGN]] — produce il blueprint team in ingresso
- [[WF-AGENT-NEW]] — sub-flusso per ogni membro del team
- [[WF-ECOSYSTEM-NEW]] — chiama questo workflow per i team L4 dell'ecosistema nuovo
- [[frg-org-designer]] · [[frg-spec-writer]] · [[frg-eval-runner]] · [[frg-hr-registrar]] — agenti owner
- [[06-ECOSISTEMI-CORE]] §07 L2.2 AGENT-WORKS — fonte di verità
