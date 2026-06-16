# WF-ECOSYSTEM-DESIGN
## Handoff in uscita: HC-ARCH-FORGE-ECO

> Organo: ARCHITETTURA (Genesi Core) · Reparto owner: L2.5 Progettazione Ecosistemi · Stato: DEFINED
> Il livello massimo del design: dato un **mandato Board**, ARCHITETTURA progetta un **organo/ecosistema
> intero** (org L1→L5 + BACKBONE + namespace + bozza dossier) e lo consegna alla FORGE per la costruzione.
> Così ARCHITETTURA progetta gli organi che poi popoleranno l'azienda. Fonte: 14-DOSSIER-ARCHITETTURA §4.
> Collega: [[ECOSISTEMA.md]] · [[BACKBONE.md]]

---

## Trigger
- La **Board (L0)** ratifica un mandato per un nuovo territorio di business ("serve l'ecosistema E-commerce").
- Instradamento da WF-ARCH-DESIGN passo 1 quando `tipo = ecosistema` (o reparto-grande / org intera).
- **Natura:** OBBLIGATORIO e SOLO su mandato Board ratificato. Non si progetta un ecosistema senza mandato (§9 dossier: nascono DA Genesi Core).

---

## Input (JSON)
```json
{
  "design_id": "ARCHECO-2026-0618-002",
  "mandato": {
    "missione": "ecosistema E-commerce per la holding",
    "revenue_model": "...",
    "done_when": "...",
    "budget": "...",
    "sponsor_csuite": "..."
  },
  "dossier_intelligence_ref": "intelligence/mercato/ecommerce",
  "namespace_proposto": "ecommerce",
  "committente": "Board"
}
```
- Prerequisito: dossier mercato INTELLIGENCE presente (senza dati di mercato non si disegna l'org).

---

## Pipeline (passi · agente owner)
```
1. MANDATO CHECK                       (arch-director)
   └── 5 campi del mandato completi? mancano → respinto a Board, non si disegna.

2. RECALL PATTERN ORG                  (arch-pattern-scout)
   └── carica lo SCHELETRO canonico degli ecosistemi esistenti (schema "ecosistema") +
        BACKBONE dei 9/10 ecosistemi → riusa la forma comune (zero divergenze dallo schema).

3. SPEC ECOSISTEMA                     (arch-spec-writer)
   └── mandato + dossier mercato → spec: confini, cosa fa / non fa, handoff inter-eco attesi.

4. ORG DESIGN L1→L5                    (arch-org-designer)   motore: org-design
   ├── L2 reparti, L3 workflow, L4 funzioni, L5 roster agenti
   └── BACKBONE: topologia swarm, namespace memoria, matrice handoff con gli altri ecosistemi
        (riceve / fornisce / NON-fa) — confini espliciti con tutti gli esistenti.

5. NAMESPACE + BOZZA DOSSIER           (arch-org-designer)
   └── definisce namespace memoria `<eco>/*` + bozza dossier PIANO-MAESTRO (0N-ECOSISTEMA-*).

6. STRUCT-GATE (org completa)          (arch-validator ‖ arch-contradiction)  → WF-STRUCT-VALIDATE
   └── l'org rispetta lo schema "ecosistema"? collide con un ecosistema esistente? INCOMPLETO → ritorna a 4.

7. SINTESI + CONSEGNA                  (arch-director)
   └── blueprint-ecosistema CLOSED → HANDOFF a FORGE (WF-ECOSYSTEM-NEW) per la costruzione reale.
```

---

## Gate
- **G-ECO1 (mandato):** nessun design senza mandato Board completo (5 campi).
- **G-ECO2 (schema unico):** l'org prodotta rispetta lo stesso scheletro canonico degli ecosistemi esistenti → **0 divergenze** (G-VAL post-design).
- **G-ECO3 (confini):** la matrice handoff inter-eco è esplicita (riceve/fornisce/non-fa) per ogni ecosistema esistente.
- **G-ECO4 (struttura, non build):** ARCHITETTURA consegna il **disegno** dell'org; la costruzione filesystem/agenti reali è FORGE (WF-ECOSYSTEM-NEW).

---

## Output (JSON)
```json
{
  "design_id": "ARCHECO-2026-0618-002",
  "blueprint_eco_ref": "architettura/blueprint/ARCHECO-2026-0618-002",
  "org_chart": "L1→L5 (reparti, workflow, funzioni, roster)",
  "backbone": { "namespace": "ecommerce", "handoff_matrix": "riceve/fornisce/non-fa vs 10 eco" },
  "dossier_bozza_ref": "PIANO-MAESTRO/0N-ECOSISTEMA-ECOMMERCE.md (bozza)",
  "validazione": "PASS",
  "handoff_to": "FORGE/WF-ECOSYSTEM-NEW"
}
```

---

## Handoff
- **HC-ARCH-FORGE-ECO → 07-FORGE / WF-ECOSYSTEM-NEW:** il disegno dell'org entra nella forgiatura reale
  (scaffold filesystem, namespace memoria init, agenti L5 via WF-AGENT-NEW, registrazione holding).
- Confine: qui si progetta l'org (org_chart + BACKBONE + bozza dossier); la FORGE la **scaffolda e popola**.
- A valle FORGE: dossier proposto alla Board per ratifica → ecosistema VIVO (L1).

---

## Dry-run
Mandato Board "ecosistema E-commerce". Scout carica lo scheletro dei 10 ecosistemi esistenti,
spec-writer fissa confini, org-designer disegna L2 (es. Catalogo, Acquisizione, Fulfillment…) →
L5 roster, BACKBONE con matrice handoff vs i 10 eco, namespace `ecommerce/*`, bozza dossier.
Struct-gate: 0 divergenze dallo schema "ecosistema", nessuna collisione → PASS. Handoff a
WF-ECOSYSTEM-NEW che costruisce. Il disegno è ricostruibile a freddo da `architettura/blueprint/`.

---

## Connessioni
- [[WF-ARCH-DESIGN]] — instrada qui quando `tipo=ecosistema` (passo 1)
- [[WF-STRUCT-VALIDATE]] — gate sull'org completa (passo 6)
- [[arch-org-designer]] — owner del design org L1→L5 · [[arch-director]] — conductor · [[arch-spec-writer]] · [[arch-pattern-scout]]
- [[14-DOSSIER-ARCHITETTURA]] §4 (WF-ECOSYSTEM-DESIGN) · §9 (gerarchia) — fonte di verità
- 07-FORGE: WF-ECOSYSTEM-NEW — destinatario handoff (costruzione reale)
