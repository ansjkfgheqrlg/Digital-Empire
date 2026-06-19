---
Type: STATE
Status: Active
Tags: #state #content-factory #CF-R1 #namespace #schema #integrità
Created: 2026-06-19
Last updated: 2026-06-19
---

# State — CF-R1 Strategia & Brief

> **Reparto:** CF-R1 Strategia & Brief · **Ecosistema:** 03-CONTENT-FACTORY
> Questo file documenta i namespace di memoria, gli schemi dei file di stato,
> e le regole di integrità per il reparto CF-R1.

---

## Namespace memoria

| Namespace | Percorso filesystem | Contenuto | Owner scrittura |
|---|---|---|---|
| `cf/briefs` | `orders/<id>/01-brief/brief.json` | Brief eseguibile per ogni ordine | CF-R1-QA (solo su PASS) |
| `cf/calendars` | `cf/calendars/<brand_slug>/settimana-YYYY-WW.json` | Piani editoriali per brand | CF-R1-CAL |
| `cf/patterns` | `cf/patterns/<brand_slug>/` | Pattern angle/hook validati e trend-attivi | CF-R1-LEARN (pattern), CF-R1-TREND (trend) |

---

## Schema `brief.json`

File: `orders/<id>/01-brief/brief.json`

```json
{
  "order_id": "CF-2026-0042",
  "brief_version": "1.0",
  "generato_il": "2026-06-19T10:52:00Z",
  "owner": "cf-r1-coord",
  "gate_r1_qa": "PASS",
  "n_rework": 0,
  "dry_run": false,
  "brand_slug": "mentalita-brutale",
  "formato": "carosello-ig",
  "quantita": 3,
  "angle": {
    "id": "angle_A",
    "formula": "errore-costoso",
    "nome": "I 3 errori che bloccano la crescita",
    "rationale": "ICP problem-aware, first_pass_rate storico 0.87 su questo brand"
  },
  "hook_type": "affermazione-diretta",
  "hook_draft": "Stai perdendo clienti ogni giorno. Non per mancanza di impegno — per questi 3 errori che non vedi.",
  "struttura_formato": "slide-deck",
  "canali": ["instagram"],
  "vincoli_brand": {
    "parole_vietate": ["forse", "quasi"],
    "palette": "dark",
    "cta_richiesta": "segui per altri errori",
    "soul_id": null
  },
  "slide_count": "8-10",
  "word_count": null,
  "durata_stimata": null,
  "icp_ref": "brands/mentalita-brutale/icp.json",
  "note_produzione": "",
  "priorita": "standard | trend | lancio"
}
```

---

## Schema `state.json` (campo 01-brief)

File: `orders/<id>/state.json`

```json
{
  "order_id": "CF-2026-0042",
  "fasi": {
    "00-intake": {
      "stato": "completata",
      "timestamp": "2026-06-19T10:30:00Z",
      "owner": "CF-D-DISPATCH"
    },
    "01-brief": {
      "stato": "completata | in_corso | in_rework | fallita",
      "timestamp": "2026-06-19T10:52:00Z",
      "owner": "cf-r1-coord",
      "gate_r1_qa": "PASS | FAIL",
      "n_rework": 0,
      "brief_path": "orders/CF-2026-0042/01-brief/brief.json",
      "lead_time_min": 22
    }
  }
}
```

---

## Schema `cf/patterns/<brand_slug>/pattern-*.json`

```json
{
  "pattern_id": "PAT-CF-R1-001",
  "brand_slug": "mentalita-brutale",
  "formato": "carosello-ig",
  "angle_formula": "errore-costoso",
  "hook_type": "affermazione-diretta",
  "first_pass_rate": 0.87,
  "n_casi": 7,
  "tipo": "pattern | antipattern",
  "aggiornato_il": "2026-06-19",
  "owner": "cf-r1-learn",
  "nota": ""
}
```

---

## Schema `cf/patterns/<brand_slug>/trend-attivi.json`

```json
[
  {
    "trend_id": "TREND-2026-0089",
    "topic": "Creator economy in declino: dati Q2 2026",
    "data_trend": "2026-06-18T14:00:00Z",
    "scadenza": "2026-06-21T14:00:00Z",
    "urgenza": "alta",
    "source": "08-INTELLIGENCE/wiki/trends/creator-economy-Q2-2026.md",
    "processato": false
  }
]
```

---

## Regole di integrità

1. **Solo CF-R1-QA scrive `brief.json`** — nessun altro agente può creare o modificare
   il brief.json definitivo. CF-R1-ANALYST e CF-R1-ANGLE producono bozze in memoria
   degli agenti, non su disco.
2. **`brief-draft.json` ≠ `brief.json`** — il draft esiste solo in modalità dry-run e
   non autorizza la produzione. Solo `brief.json` con `gate_r1_qa: PASS` nel state.json
   autorizza il passaggio a produzione.
3. **CF-R1-LEARN non modifica pattern con n < 3** — la regola anti-rumore è un
   invariante di integrità: nessun pattern viene scritto in `cf/patterns` con meno di
   3 casi verificati.
4. **CF-R1-TREND non deposita trend scartati in `trend-attivi.json`** — i trend scartati
   vanno solo in `cf/briefs/trend/scartati/`; mai in trend-attivi.json.
5. **`state.json` aggiornato a ogni passo** — ogni agente che completa il suo step
   aggiorna il campo corrispondente in state.json prima di passare il controllo all'agente
   successivo. Un workflow non è ricuperabile a freddo se state.json è obsoleto.

---

## Connessioni

- [[WF-BRIEF]] · `workflow/WF-BRIEF.md`
- [[WF-CALENDAR]] · `workflow/WF-CALENDAR.md`
- [[WF-TREND-BRIEF]] · `workflow/WF-TREND-BRIEF.md`
- [[cf-r1-qa]] · `agenti/cf-r1-qa.md` — unico owner scrittura brief.json
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R1`
