> Fonte: PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md sez. 5 (registry engine — canva)

# T-CANVA — Engine Canva (Design, Template, Export)

> Layer engine condiviso · Livello: L4 · Usato da: CF-R4 primariamente, CF-R5
> Fonte: dossier 03 §5, §6 (SKILL & Agenti/Workflow Canva/).
> Ecosistema: `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md`

---

## Identità engine

| Campo | Valore |
|---|---|
| Engine ID | canva |
| Capability servite | design, carousel-design, brand-template, export, resize, asset-upload |
| Stato | ATTIVO (MCP `mcp__claude_ai_Canva__*` disponibile) |
| Launcher | chiamate MCP dirette (no script intermedio) |
| Fallback | puppeteer-render (`render.mjs`) per layout custom |
| Tier modello owner | haiku (operazioni MCP standard) |

---

## Contratto engine (non negoziabile — pattern §5 del dossier)

| Operazione | Implementazione | Descrizione |
|---|---|---|
| `generate(job)` | `mcp__claude_ai_Canva__generate-design` o `create-design-from-brand-template` | Crea design da template o da zero |
| `check()` | verifica connessione MCP Canva (list-brand-kits come health probe) | Ritorna `{connected: true/false}` |
| `status()` | `mcp__claude_ai_Canva__get-design` su design_id | Stato export/render |
| `estimate(job)` | costo zero (Canva MCP incluso nel piano) — ritorna `{crediti: 0, tempo_stimato_sec: 30}` | Compatibile con T-render-queue |

---

## Capability → Tool MCP

| Capability | Tool MCP | Note |
|---|---|---|
| `carousel-design` (da template) | `create-design-from-brand-template` + `perform-editing-operations` | Usa `get-brand-template-dataset` per i campi editabili |
| `design` (generico) | `generate-design` o `generate-design-structured` | Per layout senza template brand |
| `brand-template` (crea/pubblica) | `create-brand-template-draft` + `publish-brand-template` | WF-BRANDKIT, non WF-CAROSELLO |
| `export` | `export-design` | Formati: PNG, JPG, PDF, MP4 (per motion Canva) |
| `resize` | `resize-design` | Declinazioni multi-formato da un design esistente |
| `asset-upload` | `upload-asset-from-url` + `create-folder` | Organizzazione library per brand slug |
| `search-design` | `search-designs` | Verifica se esiste già un design per l'ordine |

---

## Regole di routing

1. **Canva viene scelto** quando: esiste un brand template per lo slug del brand_kit
   (`canva_brand_template_ids` non vuoto in `brand-kit.json`).
2. **Fallback a puppeteer-render** quando: layout custom non coperto da template Canva,
   o `check()` ritorna false.
3. **Vietato** usare Canva per generazione di immagini realistiche/foto: per quelle →
   higgsfield image-4k o gemini-img.
4. MAI engine diverso da quello loggato in `trace.jsonl` (il routing è una funzione pura).

---

## Output atteso

- File esportato: PNG 1080x1350 (carosello), 1280x720 (thumbnail), o altro formato da brief.
- `design_id` Canva salvato in `orders/<id>/03-design/canva_design_id.txt` per audit.
- Entry in `trace.jsonl`: `{ts, agent: CF-R4-A04-canva-operator, engine: canva, tool: export-design, cost_crediti: 0}`.

---

## Connessioni

- `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md` — registry engine §5
- `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/Visual-Design/README.md` — reparto owner
- `company/Ecosistemi/03-CONTENT-FACTORY/Agenti/CF-R4-A04-canva-operator.md` — agente operator
- `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` §5, §6

*Fonte: dossier 03 §5, §6 · Aggiornato: 2026-06-11*
