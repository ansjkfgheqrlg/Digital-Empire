# WF-FORGE-PIPELINE
## Il motore generale: blueprint validato → MKD → artefatto target

> Organo: FORGE (Genesi Core) · Reparto owner: L2.3 WORKFLOW-WORKS · Stato: DEFINED
> Il cuore della FORGE: un **blueprint validato** che arriva da ARCHITETTURA (HC-ARCH-FORGE)
> viene riempito di CONTENUTO, passando — quando c'è materia prima — per l'MKD obbligatorio.
> Motore reale: `content-forge` (`SKILL & Agenti/Content-forge/skill - FINALE/`, 433 file).
> Confine ferreo: **ARCHITETTURA = STRUTTURA, FORGE = CONTENUTO**. Mai inventare la forma.
> Collega: [[WF-ARCH-DESIGN]] · [[ECOSISTEMA.md]] · [[BACKBONE.md]]

---

## Trigger
- Arriva un blueprint validato da ARCHITETTURA (handoff **HC-ARCH-FORGE**) con `forma_scelta` qualsiasi.
- `frg-chief` instrada qui le forme generiche (documento/workflow/orchestration/wiki/injection) o
  delega ai workflow di tipo (`WF-SKILL-NEW`, `WF-AGENT-NEW`, `WF-TEAM-NEW`, `WF-ECOSYSTEM-NEW`).
- Esiste materia prima ingerita (Empire Studio / INTELLIGENCE) sul tema → si parte da MKD.
- **Natura:** è la spina dorsale di forgiatura; ogni altro WF-FORGE è una sua specializzazione.

---

## Input (JSON)
```json
{
  "request_id": "ARCH-2026-0617-014",
  "blueprint_ref": "architettura/blueprint/ARCH-2026-0617-014",
  "schema_usato": "skill@v3 | agente@v1 | team@v1 | documento@v1 | ecosistema@v1",
  "forma_scelta": "documento | workflow | orchestration | wiki | injection | <tipo>",
  "spec_ref": "architettura/blueprint/ARCH-2026-0617-014#spec",
  "validazione": "PASS",
  "materia_prima": "intelligence/empire-studio/<run> | null",
  "committente": "<ecosistema richiedente>"
}
```
- `validazione != PASS` → **rigetto immediato**, ritorno ad ARCHITETTURA (G-FORGE0). Niente build al buio.

---

## Pipeline (passi · agente owner)
```
1. APERTURA BUILD                     (frg-chief)
   └── verifica validazione=PASS; apre forge/builds/<request_id> stato=OPEN
   └── forma di tipo (skill/agente/team/ecosistema)? → delega al WF specifico, qui finisce.

2. MATERIA-PRIMA CHECK                (frg-mkd-forger ‖ INTELLIGENCE)
   └── int-context-packer: c'è materiale ingerito? SÌ → namespace intelligence/. NO → build da schema.
        fonte = riassunto di seconda mano → chiedi originale (G-INTEGRAL ereditato).

3. MKD (Master Knowledge Document)    (frg-mkd-forger · content-forge)
   └── espansione INTEGRALE della fonte dentro la forma del blueprint — mai riassumere, sempre espandere
        (esempio nudo→esempio DE concreto · concetto→concetto+cross-ref · lista→lista con rationale)

4. TARGET BUILD                       (frg-mkd-forger + reparto specializzato)
   └── un target alla volta: MKD → artefatto nel formato richiesto, DENTRO la struttura del blueprint

5. GATE in serie                      (frg-eval-runner → frg-contradiction-gate)   →  vedi Gate
   └── eval ≥ soglia → anti-drift VERDE → altrimenti ritorno al builder (max 2 cicli, poi escala)

6. ARCHIVIO + CONSEGNA                 (frg-mkd-forger + frg-chief)
   └── MKD archiviato in forge/mkd/ (asset permanente) · build_ref CLOSED · handoff a MAXIMILIAN
```

---

## Gate
- **G-FORGE0 (no-build-al-buio):** `validazione != PASS` in input → rigetto, ritorno ad ARCHITETTURA.
- **G-INTEGRAL:** fonte accettata solo se integrale (mai riassunto di seconda mano); MKD > fonte in ricchezza (MKD più corto della fonte = bug, si itera).
- **G-EVAL:** `frg-eval-runner` pass_rate ≥ soglia del tipo; borderline 70-84% → decide `frg-chief`.
- **G-CONTRADICTION:** `frg-contradiction-gate` VERDE vs artefatti esistenti, altrimenti stop.
- **G-LOOP:** >2 cicli build↔gate senza PASS → escala (spec sbagliata → ritorno ad ARCH-spec) + debito in `forge/decisions`.

---

## Output (JSON)
```json
{
  "request_id": "ARCH-2026-0617-014",
  "artefatto_path": "<path artefatto target>",
  "forma": "documento | workflow | ...",
  "mkd_ref": "forge/mkd/ARCH-2026-0617-014",
  "build_ref": "forge/builds/ARCH-2026-0617-014",
  "eval": "PASS",
  "pass_rate": 0.00,
  "contraddizioni": "VERDE",
  "handoff_to": "MAXIMILIAN",
  "status": "delivered"
}
```

---

## Handoff
- **In ingresso:** HC-ARCH-FORGE da `WF-ARCH-DESIGN` (blueprint validato — l'unica fonte di struttura).
- **In uscita (catena canonica):** consegna a **MAXIMILIAN** (è all'altezza di Max?) → **Mandato** (è lecito?) → **Identity-HR** (registra) → VIVO. `frg-chief` firma l'OK di consegna.
- **Confine:** la FORGE riempie la forma vuota, non la cambia. Modifica di struttura = nuovo giro ARCHITETTURA, mai dentro la FORGE.

---

## Dry-run
Blueprint validato di un "documento operativo X" + materia prima Empire Studio. frg-mkd-forger produce
MKD (espansione integrale, più ricco della fonte), build documento dentro la struttura del blueprint,
eval PASS, contradiction VERDE, MKD archiviato in `forge/mkd/`. Output: artefatto + `mkd_ref` riusabile
per un secondo target. Test-amnesia: `build_ref` ricostruibile a freddo dalla memoria.

---

## Connessioni
- [[WF-ARCH-DESIGN]] — produce HC-ARCH-FORGE, l'input di questo workflow
- [[WF-SKILL-NEW]] · [[WF-AGENT-NEW]] · [[WF-TEAM-NEW]] · [[WF-ECOSYSTEM-NEW]] — specializzazioni per forma
- [[frg-chief]] · [[frg-mkd-forger]] · [[frg-eval-runner]] · [[frg-contradiction-gate]] — agenti owner
- [[06-ECOSISTEMI-CORE]] §07 L2.3 WORKFLOW-WORKS — fonte di verità
- A valle: MAXIMILIAN · Mandato · Identity-HR (catena di liceità/registro)
