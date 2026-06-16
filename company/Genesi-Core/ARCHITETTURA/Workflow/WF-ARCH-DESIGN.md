# WF-ARCH-DESIGN
## Handoff in uscita: HC-ARCH-FORGE

> Organo: ARCHITETTURA (Genesi Core) · Reparto owner: L2.2 Blueprint & Struttura · Stato: DEFINED
> Il cuore dell'organo: una richiesta di creazione esce come **blueprint strutturale validato**,
> pronto per la FORGE che ci costruirà dentro il CONTENUTO. Fonte: 14-DOSSIER-ARCHITETTURA §4.
> Collega: [[ECOSISTEMA.md]] · [[BACKBONE.md]]

---

## Trigger
- La FORGE (o un ecosistema, o la Board) chiede di creare un artefatto e serve la sua FORMA.
- Segnali: "creami una skill/agente/team/workflow X", "serve un documento su…", "progetta la struttura di…".
- Chiamata diretta da `WF-FORGE-PIPELINE` (07-FORGE) prima della fase MKD/Target build: la FORGE
  NON inventa strutture, le chiede qui.
- **Natura:** OBBLIGATORIO per ogni nuovo artefatto forgiato. Nessuna costruzione al buio (§4 dossier).

---

## Input (JSON)
```json
{
  "request_id": "ARCH-2026-0617-014",
  "tipo": "skill | agente | team | principio | stile | workflow | documento | reparto | ecosistema",
  "scopo": "skill per generare battle-card competitor da URL",
  "vincoli": ["kernel <= 500 righe", "no spese reali", "riusa pattern esistenti"],
  "committente": "FORGE-conductor | Board | <ecosistema>"
}
```
- `tipo` ecosistema/reparto-grande → instradato a WF-ECOSYSTEM-DESIGN (vedi Pipeline passo 1).

---

## Pipeline (passi · agente owner)
```
1. APERTURA RECORD                    (arch-director)
   └── registra in architettura/blueprint/<request_id> stato=OPEN
   └── è ecosistema/org intera? SÌ → instrada a WF-ECOSYSTEM-DESIGN, qui finisce. NO → passo 2.

2. PATTERN-SCOUT + SPEC (parallelo)   (arch-pattern-scout ‖ arch-spec-writer)
   ├── arch-pattern-scout: esiste già una struttura simile da riusare? → pattern_refs[]
   │     (anti-reinvenzione; legge architettura/pattern)
   └── arch-spec-writer: richiesta → SPEC precisa (acceptance, out-of-scope, dipendenze)
         motore: agent-specification / prd-architect-os

3. SCELTA FORMA + SCHEMA              (arch-director → arch-schema-keeper)
   ├── arch-director decide la FORMA MINIMA-MA-COMPLETA (§1 dossier): mai gonfiare, mai banalizzare
   └── arch-schema-keeper carica lo SCHEMA CANONICO del tipo (es. skill@v3)
         schema mancante? → trigger WF-SCHEMA-EVOLVE (bloccante) prima di procedere

4. BLUEPRINT MILLIMETRICO            (arch-blueprint)
   └── spec + schema + pattern_refs → STRUTTURA al millimetro
        (file, sezioni, I/O JSON, handoff, progressive disclosure, references)
        motore: architect-agent / agent-architecture / SPARC (Architecture phase)

5. GATE STRUTTURALE                  (arch-validator ‖ arch-contradiction)  →  vedi WF-STRUCT-VALIDATE
   ├── arch-validator: blueprint COMPLETO vs schema? buchi:[...]
   └── arch-contradiction: collide/duplica un artefatto esistente? (skill-contradiction-analyzer)
        INCOMPLETO o COLLIDE → ritorna a passo 4 con lista buchi (max 2 cicli, poi escala)

6. SINTESI + CONSEGNA                 (arch-director)
   └── marca record CLOSED, scrive validazione, esegue HANDOFF a FORGE
```

---

## Gate
- **G-ARCH1 (blocco cardine):** blueprint con `validazione != PASS` → **non** si passa alla FORGE. Niente costruzione al buio.
- **G-ARCH2 (no-collisione):** `arch-contradiction = COLLIDE` blocca la consegna finché non risolto o ratificato.
- **G-ARCH3 (forma giusta):** la FORMA scelta è minima-ma-completa per lo scopo (no over/under-engineering) — `arch-director` la motiva nel record.
- **G-ARCH4 (loop-guard):** >2 cicli blueprint↔gate senza PASS → escala (MAXIMILIAN, manuale fino a STEP 3) + debito registrato.

---

## Output (JSON)
```json
{
  "request_id": "ARCH-2026-0617-014",
  "blueprint_ref": "architettura/blueprint/ARCH-2026-0617-014",
  "schema_usato": "skill@v3",
  "forma_scelta": "skill",
  "spec_ref": "architettura/blueprint/ARCH-2026-0617-014#spec",
  "pattern_riusati": ["competitor-profiling/progressive-disclosure"],
  "validazione": "PASS",
  "contraddizioni": "NONE",
  "handoff_to": "FORGE",
  "note_conductor": "riusa progressive-disclosure di competitor-profiling; kernel target 380 righe"
}
```

---

## Handoff
- **HC-ARCH-FORGE → 07-FORGE:** il blueprint validato entra in `WF-FORGE-PIPELINE` (build del CONTENUTO)
  o nel workflow di tipo specifico: `WF-SKILL-NEW` (skill), `WF-AGENT-NEW` (agente), `WF-TEAM-NEW` (team).
- **Confine ferreo:** ARCHITETTURA consegna la STRUTTURA; la FORGE ci scrive dentro il CONTENUTO. Mai oltre.
- A valle della FORGE: MAXIMILIAN (è all'altezza?) → Mandato (lecito?) → Identity-HR (registra) → VIVO.

---

## Dry-run
Test "creami una skill X" (DONE WHEN §0.7): scout segnala riuso di `competitor-profiling`, spec-writer
fissa acceptance, schema-keeper carica `skill@v3`, blueprint disegna SKILL.md + references/ + evals +
progressive disclosure, validator+contradiction → PASS. Output: blueprint millimetrico di X **senza una
riga di contenuto** della skill. `blueprint_ref` ricostruibile a freddo (test-amnesia) da memoria.

---

## Connessioni
- [[WF-STRUCT-VALIDATE]] — il gate del passo 5 (riusabile pre/post FORGE)
- [[WF-ECOSYSTEM-DESIGN]] — ramo per ecosistemi/org intere (passo 1)
- [[WF-SCHEMA-EVOLVE]] — invocato se manca lo schema canonico (passo 3)
- [[arch-director]] · [[arch-spec-writer]] · [[arch-blueprint]] · [[arch-pattern-scout]] — agenti owner
- [[14-DOSSIER-ARCHITETTURA]] §4 — fonte di verità
- 07-FORGE: WF-FORGE-PIPELINE · WF-SKILL-NEW · WF-AGENT-NEW · WF-TEAM-NEW — destinatari handoff
