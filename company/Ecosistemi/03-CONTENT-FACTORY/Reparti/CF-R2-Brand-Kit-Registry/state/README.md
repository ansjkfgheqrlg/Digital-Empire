---
Type: STATE
Status: Active
Tags: #state #content-factory #CF-R2 #namespace #brand-kit #versioning #integrità
Created: 2026-06-19
Last updated: 2026-06-19
---

# State — CF-R2 Brand-Kit & Tenant Registry

> Documenta il namespace memoria operativa del reparto, la struttura `brands/<slug>/`,
> lo schema brand_kit completo, e le regole di integrità e versioning.

---

## 1. Namespace `cf/brand-kits` — Registry globale

Il namespace `cf/brand-kits` è la fonte di verità sull'esistenza e lo stato di ogni tenant.
È interrogato da CF-D-QA prima di validare ogni ordine di produzione.

**Struttura index:**
```json
{
  "versione_registry": "1",
  "tenant": [
    {
      "slug": "mentalita-brutale",
      "nome": "Mentalità Brutale",
      "stato": "approvato",
      "brand_kit_path": "brands/mentalita-brutale/brand-kit.json",
      "icp_path": "brands/mentalita-brutale/icp.json",
      "brand_kit_version": "1.0",
      "icp_version": "1.0",
      "seed_source": "carousel-factory/brands/mentalita-brutale/config.json",
      "ultima_validazione": "YYYY-MM-DD",
      "ultima_sync_canva": "YYYY-MM-DD",
      "approvato_da": "cf-r2-coord",
      "timestamp_approvazione": "YYYY-MM-DDTHH:MM:SS"
    }
  ]
}
```

**Stati possibili per ogni tenant:**
- `in_onboarding` — WF-BRAND-ONBOARDING in corso; ordini bloccati
- `pending_icp_info` — attesa risposta committente per dati ICP; onboarding sospeso
- `pending_assets` — attesa logo/font da committente; onboarding avanzabile ma sync Canva incompleta
- `approvato` — brand_kit + icp validati, tenant disponibile per ordini
- `in_maintenance` — WF-BRAND-MAINTENANCE attivo; brand_kit in aggiornamento; ordini NON bloccati (usa versione precedente)
- `sospeso` — tenant disattivato dal committente o per violazione Mandato; ordini bloccati

---

## 2. Struttura `brands/<slug>/` per tenant

```
brands/<slug>/
├── brand-kit.json           — brand_kit CF-grade (schema completo — vedi §3)
├── icp.json                 — profilo ICP v<N> (dolori, desideri, obiezioni, awareness, linguaggio)
├── state.json               — fase corrente, versioni, changelog, timestamp
├── assets/
│   ├── logo.png             — logo brand (opzionale; null se non fornito)
│   └── fonts/               — font custom (opzionale; vuota se solo web fonts)
├── canva/
│   └── template_ids.json    — ID Canva brand kit + logo asset + template iniziali
├── history/
│   └── brand-kit-v<N>.json  — versioni precedenti del brand_kit (archivio)
├── icp-history/
│   └── icp-v<N>.json        — versioni precedenti dell'ICP (archivio)
└── drift-reports/
    └── drift-<date>.json    — report campionamento CF-R2-DRIFT per data
```

**state.json per tenant:**
```json
{
  "slug": "mentalita-brutale",
  "fase": "approvato",
  "brand_kit_version": "1.0",
  "icp_version": "1.0",
  "gate_qa": "PASS",
  "seed_source": "carousel-factory/brands/mentalita-brutale/config.json",
  "committente": "DE-interno",
  "timestamp_creazione": "YYYY-MM-DDTHH:MM:SS",
  "timestamp_approvazione": "YYYY-MM-DDTHH:MM:SS",
  "ultima_sync_canva": "YYYY-MM-DD",
  "ultima_validazione": "YYYY-MM-DD",
  "asset_pendenti": [],
  "changelog": [
    {
      "versione": "1.0",
      "data": "YYYY-MM-DD",
      "autore": "cf-r2-creator",
      "note": "brand_kit creato da seed carousel-factory v1"
    }
  ]
}
```

---

## 3. Schema brand_kit CF-grade (immutabile — da §0 dossier)

```json
{
  "slug": "string — identificatore univoco, kebab-case, max 32 char",
  "nome": "string — nome display del brand",
  "handle": {
    "ig": "string | null — @handle Instagram",
    "tiktok": "string | null",
    "yt": "string | null"
  },
  "visual": {
    "palette": {
      "primary": "string — HEX #RRGGBB obbligatorio",
      "accent": "string — HEX #RRGGBB obbligatorio",
      "bg": "string — HEX #RRGGBB obbligatorio"
    },
    "font": {
      "display": "string — nome font display/hero obbligatorio",
      "body": "string — nome font body obbligatorio"
    },
    "logo": "string | null — path relativo a brands/<slug>/assets/logo.png",
    "stile": "string — descrizione stile visivo (es. dark, minimalista, illustrativo)",
    "canva_brand_template_ids": "array[string] — ID template Canva; array vuoto se sync non ancora eseguita"
  },
  "voice": {
    "tono": "string — descrizione tono (es. diretto, accademico, ironico); obbligatorio non vuoto",
    "esempi_si": "array[string] — ≥2 esempi di frasi coerenti con il brand; non pari al segnaposto template",
    "esempi_no": "array[string] — ≥2 esempi di frasi vietate per il brand; non pari al segnaposto template",
    "parole_vietate": "array[string] — parole specifiche bandite; array vuoto ammesso"
  },
  "soul_id": "string | null — ID soul Higgsfield per video UGC; null se brand non ha video UGC",
  "canali": "array[{tipo: string, publisher: string, review_umana: boolean}] — ≥1 canale"
}
```

**Regole di integrità:**
- `slug` deve essere univoco nel registry; usare kebab-case; nessun carattere speciale eccetto `-`.
- Ogni HEX in `palette` deve passare regex `/^#[0-9A-Fa-f]{6}$/` — 6 cifre esatte, no shorthand 3 cifre.
- `voice.tono` non può essere stringa vuota o contenere il valore del segnaposto del template.
- `voice.esempi_si` e `voice.esempi_no` devono avere ≥2 elementi ciascuno e non contenere
  stringhe identiche ai segnaposto del template.
- `canali` deve avere ≥1 elemento con `tipo`, `publisher` e `review_umana` espliciti.
- `soul_id: null` è valido per brand senza produzione video.

---

## 4. Versioning brand_kit

| Tipo modifica | Versione | Azione archiviazione |
|---|---|---|
| Creazione iniziale | 1.0 | Nessuna (primo file) |
| Aggiunta/rimozione voice | 1.0 → 1.1 | Archivia 1.0 in history/ |
| Cambio palette o font | 1.0 → 1.1 | Archivia 1.0 in history/ + nota impatto produzione |
| Aggiornamento soul_id | 1.0 → 1.1 | Archivia 1.0 in history/ |
| Cambio slug | Non permesso | Richiede nuovo onboarding con slug nuovo |

Il campo `brand_kit_version` in `state.json` e in `cf/brand-kits` viene aggiornato
da CF-R2-CREATOR a ogni patch. Le versioni archiviate in `history/` sono mantenute
senza limite di numero (audit trail permanente).

---

## 5. Regole di integrità del registry

1. **Unicità slug** — CF-R2-COORD verifica unicità prima di creare ogni entry. Slug
   duplicato = rifiuto con indicazione dello slug conflittuale.
2. **Coerenza path** — `brand_kit_path` e `icp_path` in `cf/brand-kits` devono
   puntare a file esistenti nel filesystem. Broken link = tenant in stato "sospeso"
   automatico fino a ripristino.
3. **Gate obbligatorio** — nessun tenant transita a stato "approvato" senza
   `gate_qa: "PASS"` nel suo `state.json`.
4. **Changelog obbligatorio** — ogni modifica al `brand_kit.json` (anche patch minore)
   genera una entry nel `changelog` di `state.json`. Modifiche senza changelog sono
   anomalia da segnalare.
5. **ADR-003 invariante** — i file in `carousel-factory/brands/` non compaiono mai
   come destinazione di scrittura negli script CF-R2.

---

## Connessioni

- [[CF-R2-Brand-Kit-Registry]] · `README.md` — questo state documenta il cuore operativo del reparto
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — struttura completa e mapping seed v1
- [[cf-r2-coord]] · `agenti/cf-r2-coord.md` — owner del namespace cf/brand-kits
- [[WF-BRAND-ONBOARDING]] · `workflow/WF-BRAND-ONBOARDING.md` — popola la struttura state
