> Fonte: PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md sez. 4d (WF-THUMB)

# WF-THUMB — Workflow Thumbnail & Grafiche

> Livello: L3 · Reparto: CF-R4 VISUAL & DESIGN · Coordinatore: `CF-R4-A01-visual-lead`
> Fonte: dossier 03 §4d.
> Ecosistema: `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md`

---

## Identità

| Campo | Valore |
|---|---|
| ID workflow | WF-THUMB |
| Ecosistema | 03-CONTENT-FACTORY |
| Reparto L2 | CF-R4 VISUAL & DESIGN |
| Stato | SCAFFOLD (Canva MCP attivo; Higgsfield image-4k da collegare) |
| Committenti tipici | 05-MB (YouTube), 02-INFO (copertine corsi), CF-R2 (grafiche video) |
| Output | thumbnail 1280x720 + varianti A/B resize multi-formato |

---

## Cosa produce

Thumbnail YouTube, copertine corso/libro, grafiche social statiche — con 2 varianti A/B
per concept scelto, declinate in tutti i formati richiesti dal canale.

---

## Pipeline end-to-end

```
ordine → brief (titolo video/uso, canale, brand_kit, emozione target, safe-area)
  → DRY-RUN: CF-R4-A03 genera 3 concept testuali:
      concept = {composizione: "primo piano + testo overlay / split / minimal",
                 testo: "max 5 parole leggibili a 10%",
                 emozione: "sorpresa | urgenza | curiosità | autorevolezza"}
      → output: concepts.json in orders/<id>/03-design/

  → committente sceglie concept (o default: concept con score emozione più alto per icp)

  → generazione per il concept scelto, 3 engine alternativi:
      ramo A: Canva MCP → `search-brand-templates` per canale → `generate-design` →
               `perform-editing-operations` (testo, overlay) → `export-design` 1280x720
      ramo B: Higgsfield image-4k prompt ultra-specifico (CF-R4-A03) → immagine base →
               overlay testo ffmpeg/Canva
      ramo C: Canva MCP `generate-design-structured` senza template (layout libero)

  → T-resize: declinazioni automatiche:
      1280x720 (YouTube), 1080x1080 (IG post), 1080x1920 (story/reel), 1200x628 (OG)

  → varianti A/B (2 per concept: diverso colore testo / diversa composizione)

  → GATE-FORMATO: leggibilità a 10%, peso <2MB, safe-area rispettata, dimensioni esatte
  → GATE-BRAND: palette/font del brand_kit, logo posizionato correttamente
  → delivery: A e B inviate al committente per scelta

  → scelta committente → winner in orders/<id>/06-delivery/ → cf/patterns
     (brand, canale, concept, emozione, metriche CTR a 48h se disponibili)
```

---

## Handoff contract (ingresso)

```json
{
  "from": "05-MB | 02-INFO | CF-R2",
  "to": "CF-R4/WF-THUMB",
  "order_id": "CF-2026-XXXX",
  "payload": {
    "titolo": "testo del video / uso grafica",
    "canale": "youtube | instagram | course-cover | book-cover",
    "brand_kit": "brands/<slug>/brand-kit.json",
    "formati_output": ["1280x720", "1080x1080"],
    "emozione_target": "curiosità | urgenza | autorevolezza",
    "safe_area": true,
    "varianti_AB": 2
  },
  "acceptance_criteria": [
    "brand_kit presente con palette e font",
    "titolo/uso dichiarato",
    "formati output specificati"
  ]
}
```

---

## Failure handling

| Evento | Azione |
|---|---|
| template Canva non trovato per brand | → ramo C (generate-design-structured) oppure ramo B (Higgsfield); MAI silenzioso — loggato in trace.jsonl |
| engine image non collegato (Higgsfield) | → solo rami A+C disponibili; lo stato è dichiarato nel brief output |
| GATE-FORMATO fallisce (testo illeggibile a 10%) | → CF-R4-A05 riduce testo overlay o aumenta contrasto e re-esporta (1 retry automatico) |
| committente non sceglie la variante entro deadline | → Conductor allerta committente; il winner di default è variante A |

---

## Connessioni

- `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md` — organigramma completo
- `company/Ecosistemi/03-CONTENT-FACTORY/BACKBONE.md` — namespace memoria, topologia
- `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/Visual-Design/README.md`
- `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` §4d, §5

*Fonte: dossier 03 §4d · Aggiornato: 2026-06-11*
