---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #content-factory #CF-R2 #brand-kit #multi-tenant #namespace
Created: 2026-06-19
Last updated: 2026-06-19
---

# ARCHITETTURA — CF-R2 Brand-Kit & Tenant Registry

> **Reparto:** CF-R2 · **Area:** Pre-Produzione (L1-PRE) · **Standard:** CF-grade v2 (ADR-007)

---

## 1. Posizione nella gerarchia CF-DE

```
CF-DIRECTOR (L0)
    └── L1-PRE — CAPO AREA PRE-PRODUZIONE
            ├── CF-R1 — Strategia & Brief          (ordini → brief.json)
            └── CF-R2 — Brand-Kit & Tenant Registry  ← QUESTO REPARTO
                    (brand_kit + icp.json → approvazione tenant)
```

CF-R2 **coordina** col L1-PRE (capo area Pre-Produzione), non con CF-Director direttamente.
Le escalation di CF-R2 salgono a L1-PRE → CF-Director se il problema supera il livello reparto.

---

## 2. Struttura cartella reparto

```
CF-R2-Brand-Kit-Registry/
├── README.md                  — missione, roster, workflow, handoff
├── ARCHITETTURA.md            — questo file
├── agenti/
│   ├── cf-r2-coord.md         — sonnet, coordinatore registry
│   ├── cf-r2-qa.md            — sonnet, verificatore gate brand_kit
│   ├── cf-r2-creator.md       — sonnet, builder struttura brands/<slug>/
│   ├── cf-r2-canva.md         — haiku, sync Canva via MCP
│   ├── cf-r2-drift.md         — haiku, monitor brand-drift ciclico
│   └── cf-r2-icp.md           — sonnet, profiler ICP per brand
├── workflow/
│   ├── WF-BRAND-ONBOARDING.md — onboarding nuovo tenant end-to-end
│   └── WF-BRAND-MAINTENANCE.md — drift monitoring + patch brand_kit
├── principi/
│   └── PRINCIPI.md            — 3 principi non negoziabili del reparto
├── scripts/
│   └── README.md              — wrapper carousel-factory + 3 script deterministici
├── kpi/
│   └── KPI.md                 — metriche reparto con regole di misura
└── state/
    └── README.md              — namespace cf/brand-kits, struttura brands/<slug>/
```

---

## 3. Namespace memoria operativa

### 3.1 `cf/brand-kits` — Registry globale tenant

Il namespace `cf/brand-kits` contiene l'**index dei tenant attivi**:
```json
{
  "tenants": [
    {
      "slug": "mentalita-brutale",
      "stato": "approvato",
      "brand_kit_path": "brands/mentalita-brutale/brand-kit.json",
      "icp_path": "brands/mentalita-brutale/icp.json",
      "ultima_sync_canva": "YYYY-MM-DD",
      "ultima_validazione": "YYYY-MM-DD",
      "seed_source": "carousel-factory/brands/mentalita-brutale/config.json"
    }
  ]
}
```

Un tenant con `stato != "approvato"` non può ricevere ordini CF-DE.

### 3.2 `brands/<slug>/` — Struttura per tenant

```
brands/<slug>/
├── brand-kit.json     — brand_kit CF-grade (schema completo §0 dossier)
├── icp.json           — profilo ICP (dolori, desideri, obiezioni, awareness, linguaggio)
├── state.json         — fase onboarding, approvazione, ultima sync Canva, changelog
├── assets/
│   ├── logo.png       — logo brand (fornito o generato)
│   └── fonts/         — font brand se custom
└── canva/
    └── template_ids.json  — ID template Canva per brand
```

---

## 4. Schema brand_kit CF-grade (da §0 dossier — immutabile)

```json
{
  "slug": "mentalita-brutale",
  "nome": "Mentalità Brutale",
  "handle": {
    "ig": "@mentalita.brutale",
    "tiktok": null,
    "yt": null
  },
  "visual": {
    "palette": {
      "primary": "#8B0000",
      "accent": "#C0C0C0",
      "bg": "#0A0A0A"
    },
    "font": {
      "display": "Anton",
      "body": "Inter"
    },
    "logo": "brands/mentalita-brutale/assets/logo.png",
    "stile": "dark, gradiente rosso/argento, grain texture",
    "canva_brand_template_ids": []
  },
  "voice": {
    "tono": "diretto, brutale, zero fronzoli",
    "esempi_si": [
      "Il 90% delle persone non vuole sentirsi dire la verità. Eccola.",
      "Non esistono scorciatoie. Esistono persone disposte a fare quello che gli altri evitano."
    ],
    "esempi_no": [
      "Siamo entusiasti di annunciare...",
      "In questo articolo esploreremo insieme..."
    ],
    "parole_vietate": ["emozionante", "incredibile", "fantastico", "viaggio"]
  },
  "soul_id": null,
  "canali": [
    {
      "tipo": "ig",
      "publisher": "mentalita_orchestrator.py",
      "review_umana": true
    }
  ]
}
```

Tutti i campi sono obbligatori. CF-R2-QA blocca qualsiasi brand_kit con campo mancante
o con valori pari al segnaposto non sostituito del template.

---

## 5. Wrapper carousel-factory (ADR-003 — mai riscrivere)

I 4 brand in `carousel-factory/brands/` sono asset attivi del motore caroselli. CF-R2
li usa come **seed** esclusivamente in lettura:

```
Flusso seed:
carousel-factory/brands/<slug>/config.json
        │ (lettura read-only)
        ▼
scripts/brandkit-from-seed.py
        │ (trasformazione formato v1 → CF-grade)
        ▼
brands/<slug>/brand-kit.json (NUOVO FILE, non modifica l'originale)
```

Il file `config.json` originale rimane invariato. Ogni aggiornamento futuro al brand_kit
CF-grade non tocca mai `carousel-factory/`.

---

## 6. Brand-drift monitor — logica di campionamento

CF-R2-DRIFT campiona ≥5 output per brand per ciclo produzione. Il confronto è su:
- Palette: i colori HEX usati nell'output vs `visual.palette`
- Voice: presenza di parole vietate nell'output vs `voice.parole_vietate`
- Font: font usati nell'output vs `visual.font`
- Tono: verifica esempi_no non replicati nell'output

Se deviazione rilevata su ≥1 dimensione → alert a CF-R2-COORD con specifica.

---

## Connessioni

- [[CF-R0-Director]] · `Reparti/CF-R0-Director/ARCHITETTURA.md` — L0 che governa l'intake ordini
- [[CF-R1-Strategia-Brief]] · `Reparti/CF-R1-Strategia-Brief/ARCHITETTURA.md` — gemello area Pre-Produzione
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R2`
