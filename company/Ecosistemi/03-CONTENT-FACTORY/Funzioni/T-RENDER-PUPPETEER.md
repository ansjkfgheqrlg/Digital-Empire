> Fonte: PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md sez. 5 (registry engine — puppeteer-render)

# T-RENDER-PUPPETEER — Engine Render Puppeteer (HTML→PNG)

> Layer engine condiviso · Livello: L4 · Usato da: CF-R4 (WF-CAROSELLO ramo C)
> Fonte: dossier 03 §5, §6 (carousel-factory/render.mjs).
> Ecosistema: `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md`

---

## Identità engine

| Campo | Valore |
|---|---|
| Engine ID | puppeteer-render |
| Capability servite | html-to-png, carousel-render |
| Stato | ATTIVO (`carousel-factory/render.mjs` esistente e funzionante) |
| Launcher | wrapper intorno a `Workfolw crea caroselli à/carousel-factory/render.mjs` (NON riscrivere — ADR-003) |
| Fallback | canva export (se layout non è HTML-based) |
| Tier modello owner | wasm/haiku (CF-R4-A05-render-operator) |

---

## Contratto engine (non negoziabile)

| Operazione | Implementazione | Descrizione |
|---|---|---|
| `generate(job)` | `node render.mjs --input slides.html --output out/ --format png` | Render HTML slides → PNG |
| `check()` | `node --version && node render.mjs --check` | Verifica Node.js e dipendenze Puppeteer |
| `status()` | sincrono (processo Node.js in-line) | Exit 0 = ok, non-0 = errore |
| `estimate(job)` | `{crediti: 0, tempo_stimato_sec: n_slide × 2}` | Costo zero — sempre approvato |

---

## Asset core: render.mjs

- Path: `Workfolw crea caroselli à/carousel-factory/render.mjs` (path con typo/accenti — legacy).
- Durante CF-F2 questo file verrà copiato (NON spostato) in
  `company/Ecosistemi/03-CONTENT-FACTORY/Workflow/WF-CAROSELLO/render.mjs` con path puliti.
- L'originale resta intoccato finché il sostituto non è validato (regola Piano Maestro).
- Dipendenze: Node.js + `puppeteer` (installato nella directory carousel-factory).

---

## Come funziona il render

```
input: slides.html (generato da CF-R4-A02 con placeholders sostituiti da CF-R4-A04)
  → Puppeteer apre il file in browser headless (viewport 1080x1350 per carosello)
  → screenshot per ogni slide (basato su elemento `.slide` o paginazione dichiarata)
  → output: `slide_01.png`, `slide_02.png`, ... in cartella output/
  → ottimizzazione peso: se slide > 8MB → compressione via sharp o ffmpeg (CF-R4-A05)
```

---

## Template HTML compatibili (ramo C del WF-CAROSELLO)

Formato atteso di `slides.html`:
- Ogni slide = `<div class="slide">` con dimensioni fisse 1080x1350px.
- CSS inline per font (Google Fonts o font locali) e palette dal brand_kit.
- Il testo slide viene iniettato da CF-R4-A02 (slide copywriter) nel template.
- Esempi esistenti: `Digital Empire/caroselli/3-sistemi-ai/slides.html` (archiviato come riferimento).

---

## Regole di routing

1. Puppeteer viene scelto per WF-CAROSELLO quando:
   - Il brief specifica `note: "ramo-C"` o `nota: "layout-custom"`.
   - Non esiste template Canva per il brand (brand_kit.visual.canva_brand_template_ids vuoto).
2. Fallback a Canva export quando il layout è standard e il template Canva è disponibile.
3. Costo zero — CF-SENT-cost approva automaticamente senza intervento.
4. Path con caratteri speciali (typo `Workfolw`) gestiti con path assoluti nel wrapper.

---

## Connessioni

- `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md` — registry engine §5
- `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/Visual-Design/README.md`
- `company/Ecosistemi/03-CONTENT-FACTORY/Agenti/CF-R4-A05-render-operator.md`
- `Workfolw crea caroselli à/carousel-factory/render.mjs` — asset core (NON modificare, ADR-003)
- `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` §5, §6

*Fonte: dossier 03 §5, §6 · Aggiornato: 2026-06-11*
