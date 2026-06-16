# WF-STRUCT-VALIDATE
## Gate riusabile: struct-gate

> Organo: ARCHITETTURA (Genesi Core) · Reparto owner: L2.4 Validazione Strutturale · Stato: DEFINED
> Il gate strutturale della holding: prende un artefatto e dice **COMPLETO / INCOMPLETO** con la
> lista esatta dei buchi rispetto allo schema canonico. Deterministico, bloccante.
> Usato due volte: **pre-FORGE** (il blueprint è completo?) e **post-FORGE** (il costruito rispetta il blueprint?).
> Fonte: 14-DOSSIER-ARCHITETTURA §4 (WF-STRUCT-VALIDATE) + §5 (skill `struct-gate`). Collega: [[ECOSISTEMA.md]] · [[BACKBONE.md]]

---

## Trigger
- **Pre-FORGE:** chiamato da WF-ARCH-DESIGN passo 5 — il blueprint è strutturalmente completo prima di consegnarlo?
- **Post-FORGE:** chiamato dalla FORGE (WF-FORGE-PIPELINE, fase Consegna) — l'artefatto costruito rispetta il blueprint?
- Chiamata diretta da MAXIMILIAN/Mandato che vogliono un check strutturale prima del proprio gate.
- **Natura:** OBBLIGATORIO. Nessun artefatto passa a valle senza esito di questo gate (parte del passo 4 GATE del ciclo a 9 passi).

---

## Input (JSON)
```json
{
  "validate_id": "VAL-2026-0617-031",
  "fase": "pre-forge | post-forge",
  "tipo": "skill | agente | team | principio | stile | workflow | documento | reparto | ecosistema",
  "schema_ref": "architettura/schemi/skill@v3",
  "artefatto_ref": "architettura/blueprint/ARCH-2026-0617-014",
  "blueprint_ref": "architettura/blueprint/ARCH-2026-0617-014"
}
```
- `fase=pre-forge` → `artefatto_ref` è il blueprint, si confronta con lo `schema_ref`.
- `fase=post-forge` → `artefatto_ref` è l'artefatto costruito, si confronta con lo `schema_ref` **e** col `blueprint_ref`.

---

## Pipeline (passi · agente owner)
```
1. CARICA SCHEMA + ARTEFATTO          (arch-validator)
   ├── arch-schema-keeper risolve schema_ref → lista campi/sezioni OBBLIGATORI + REGOLE del tipo
   └── carica artefatto_ref (e blueprint_ref se post-forge)

2. CHECK CAMPI OBBLIGATORI            (arch-validator)
   └── per ogni campo/sezione dello schema: presente? non vuoto? rispetta vincoli (es. kernel<=500)?
        ogni mancanza → buchi[] con { campo, atteso, trovato, gravita }

3. CHECK CONFORMITÀ BLUEPRINT (solo post-forge)   (arch-validator)
   └── il costruito ha le sezioni/file promessi dal blueprint? deriva → buchi[] gravita=BLOCK

4. CHECK NON-CONTRADDIZIONE           (arch-contradiction)
   └── skill-contradiction-analyzer: l'artefatto duplica/contraddice l'esistente? → collisioni[]

5. VERDETTO                            (arch-validator)
   └── buchi BLOCK presenti o collisione non risolta → INCOMPLETO; altrimenti → COMPLETO
   └── scrive esito in architettura/validazioni/<validate_id>
```

---

## Gate
- **G-VAL1 (determinismo):** stesso artefatto + stesso schema ⇒ stesso verdetto. Niente giudizio "soggettivo" (quello è MAXIMILIAN).
- **G-VAL2 (bloccante):** verdetto `INCOMPLETO` blocca il passaggio a valle; i `buchi` sono la lista esatta da chiudere.
- **G-VAL3 (gravità):** `BLOCK` (campo obbligatorio assente / deriva dal blueprint) blocca; `WARN` (raccomandato) passa con nota.
- **G-VAL4 (solo struttura):** il gate giudica la FORMA, mai la qualità del contenuto (confine §6 dossier).

---

## Output (JSON)
```json
{
  "validate_id": "VAL-2026-0617-031",
  "verdetto": "COMPLETO | INCOMPLETO",
  "buchi": [
    { "campo": "escalation", "atteso": "tabella failure→contromisura", "trovato": "assente", "gravita": "BLOCK" },
    { "campo": "evals", "atteso": ">=3 eval", "trovato": "1 eval", "gravita": "WARN" }
  ],
  "collisioni": [],
  "schema_usato": "skill@v3",
  "fase": "pre-forge"
}
```

---

## Handoff
- **Pre-FORGE, COMPLETO →** restituisce a WF-ARCH-DESIGN che esegue HANDOFF a FORGE.
- **Pre-FORGE, INCOMPLETO →** ritorna a `arch-blueprint` con `buchi[]` (loop max 2, poi escala).
- **Post-FORGE, COMPLETO →** sblocca la consegna FORGE → MAXIMILIAN.
- **Post-FORGE, INCOMPLETO →** rimanda alla FORGE: "il costruito non rispetta il blueprint, ecco i buchi".
- Buchi ricorrenti su uno schema → segnala a WF-SCHEMA-EVOLVE (ReasoningBank: rafforza la "costituzione").

---

## Dry-run
Blueprint di una skill senza sezione `evals`. Pre-FORGE: schema `skill@v3` esige `>=3 eval` →
buco `{evals, BLOCK}` → verdetto INCOMPLETO → ritorna a blueprint. Aggiunta la sezione → re-run →
COMPLETO → consegna a FORGE. Post-FORGE: la skill costruita ha solo 2 eval vs blueprint=3 →
deriva → INCOMPLETO → rimanda alla FORGE. Esito sempre tracciato in `architettura/validazioni/`.

---

## Connessioni
- [[WF-ARCH-DESIGN]] — chiama questo gate al passo 5 (pre-FORGE)
- [[WF-SCHEMA-EVOLVE]] — destinatario dei buchi ricorrenti
- [[arch-validator]] — owner del gate · [[arch-contradiction]] — check collisione · [[arch-schema-keeper]] — risolve lo schema
- [[14-DOSSIER-ARCHITETTURA]] §4–§5 — fonte di verità (gate + skill `struct-gate`)
- 07-FORGE: WF-FORGE-PIPELINE — chiama il gate in fase post-forge
