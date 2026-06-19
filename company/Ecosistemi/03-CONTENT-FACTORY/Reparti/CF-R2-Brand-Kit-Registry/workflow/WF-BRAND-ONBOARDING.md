---
Type: WORKFLOW
Status: Active
Tags: #workflow #content-factory #CF-R2 #onboarding #tenant #brand-kit #gate-bloccante
Created: 2026-06-19
Last updated: 2026-06-19
---

# WF-BRAND-ONBOARDING — Onboarding Nuovo Tenant

> **ID:** WF-R2-001 · **Owner:** `cf-r2-coord` · **Reparto:** CF-R2 Brand-Kit & Tenant Registry
> **Trigger:** richiesta onboarding nuovo tenant (da CF-D-DISPATCH o committente diretto)

---

## Scopo

Portare un nuovo tenant da "brief brand" a "approvato nel registry CF-R2" con brand_kit.json
validato, icp.json completo, sync Canva eseguita, e struttura `brands/<slug>/` integra.

**Gate BLOCCANTE:** un brand senza approvazione CF-R2-COORD non può ricevere ordini CF-DE.
CF-D-QA blocca qualsiasi ordine con `brand_kit` puntante a un brand non approvato nel registry.

I 4 brand seed del carousel-factory v1 (`mentalita-brutale`, `brand-agency`, `brand-education`,
`brand-personal`) sono anch'essi onboardati attraverso questo workflow nella modalità "seed v1":
CF-R2-CREATOR legge il `config.json` v1 in sola lettura e costruisce i file CF-grade nella
cartella `brands/<slug>/` (ADR-003 — nessuna modifica ai file in `carousel-factory/brands/`).

**Dry-run:** eseguito con `dry_run: true`, il workflow produce un `brand-kit-draft.json` in
`brands/<slug>/` senza aggiornare il registry `cf/brand-kits` e senza avviare la sync Canva.
Usato per verificare che il brief onboarding sia sufficiente prima di impegnare risorse.

---

## Attori

| Step | Agente | Funzione |
|---|---|---|
| Coordinamento | `cf-r2-coord` | Riceve richiesta, assegna agenti, approva il tenant a fine flusso |
| Build brand_kit | `cf-r2-creator` | Crea struttura `brands/<slug>/` e compila brand-kit.json |
| Build ICP | `cf-r2-icp` | Compila `icp.json` con dolori, desideri, obiezioni, linguaggio |
| Sync Canva | `cf-r2-canva` | Crea/aggiorna brand kit Canva e carica logo |
| Gate schema | `cf-r2-qa` | Valida brand_kit e icp.json (gate BLOCCANTE) |

---

## Flusso passo-passo

```
[TRIGGER]
Richiesta onboarding tenant ricevuta da CF-D-DISPATCH o committente
        │
        ▼
[STEP 1] CF-R2-COORD — verifica pre-workflow
  → slug univoco nel registry cf/brand-kits?
  → brief onboarding contiene: nome, palette, font, tono, canali?
  → Se slug già esistente con stato "approvato": blocca (brand già onboardato)
  → Se slug esistente con stato "in_onboarding": riprendi da dove si è fermato (idempotente)
  → Crea entry in cf/brand-kits: stato = "in_onboarding"
  → Se dry_run: true → flag passato a tutti gli agenti
        │
        ▼
[STEP 2] CF-R2-CREATOR — build struttura brands/<slug>/
  → Crea cartella brands/<slug>/ con sottocartelle
  → Modalità "seed v1": legge carousel-factory/brands/<slug>/config.json in sola lettura
    → mappa campi v1 → formato CF-grade → brand-kit.json
  → Modalità "brief onboarding": compila brand-kit.json dai dati del brief
  → Campo mancante nel brief → valore null + nota in state.json (non inventa)
  → Output: brand-kit.json, state.json, canva/template_ids.json (vuoto)
  → Se asset pendenti (logo, font): segnala a CF-R2-COORD e prosegue
        │
        ▼
[STEP 3 — PARALLELO] CF-R2-ICP e CF-R2-CANVA avviati in parallelo da CF-R2-COORD
  │                                               │
  ▼                                               ▼
[3A] CF-R2-ICP — compila icp.json            [3B] CF-R2-CANVA — sync Canva
  → Da brief ICP committente                    → Prerequisito: gate_qa non ancora PASS
  → Se dati insufficienti: domande               → Se dry_run: skip sync Canva reale
    di chiarimento → CF-R2-COORD                 → Chiama list-brand-kits via MCP
    → committente (max 48h attesa)               → Crea/aggiorna brand kit Canva
  → Output: icp.json v1.0                        → Carica logo se presente
  → Salva in brands/<slug>/icp.json              → Aggiorna canva/template_ids.json
        │                                               │
        └──────────────────┬────────────────────────────┘
                           ▼
[STEP 4] CF-R2-QA — gate schema (BLOCCANTE)
  → Apre brand-kit.json: schema completo? palette HEX valide? voice con esempi reali?
  → Apre icp.json: dolori ≥1, desideri ≥1, obiezioni ≥1, awareness_level, linguaggio?
  → PASS → avanza a STEP 5
  → FAIL → lista errori per campo → CF-R2-CREATOR per correzione → ritorna a STEP 4
    (max 2 rework; se 3° FAIL: escalation CF-R2-COORD → L1-PRE)
        │
        ▼
[STEP 5] CF-R2-COORD — approvazione tenant
  → Verifica che state.json riporti gate_qa: PASS
  → Verifica che icp.json sia presente e valido (ha ricevuto PASS da CF-R2-QA)
  → Verifica che canva/template_ids.json esista (anche se vuoto, dichiara sync status)
  → Aggiorna cf/brand-kits: stato = "approvato", timestamp_approvazione
  → Aggiorna brands/<slug>/state.json: fase = "approvato"
  → Notifica a CF-D-DISPATCH: brand disponibile per ordini
        │
        ▼
[OUTPUT]
brands/<slug>/brand-kit.json     → validato CF-R2-QA, approvato CF-R2-COORD
brands/<slug>/icp.json           → v1.0 compilato CF-R2-ICP
brands/<slug>/state.json         → fase = approvato, changelog, timestamp
brands/<slug>/canva/template_ids.json → ID Canva (o vuoto con nota se logo pendente)
cf/brand-kits (namespace)        → entry tenant con stato = approvato
```

---

## I/O JSON del workflow

**Input (richiesta onboarding):**
```json
{
  "tipo": "onboarding",
  "slug": "vendi-la-skill",
  "nome": "Vendi la Skill",
  "committente": "02-INFO",
  "seed_source": null,
  "brief_brand": {
    "palette": {"primary": "#1C1C1C", "accent": "#F59E0B", "bg": "#FFFFFF"},
    "font": {"display": "Sora", "body": "Inter"},
    "tono": "diretto, orientato ai risultati, senza promesse facili",
    "esempi_si": [
      "Non vendi la skill. Vendi il risultato che la skill produce.",
      "Il cliente non compra la tua expertise. Compra la certezza che il suo problema sparisca."
    ],
    "esempi_no": [
      "In questo percorso fantastico insieme scopriremo...",
      "Sono super entusiasta di condividere con voi..."
    ],
    "parole_vietate": ["percorso", "insieme", "fantastico", "emozionante"],
    "canali": [{"tipo": "ig", "publisher": "ig_orchestrator.py", "review_umana": true}],
    "handle": {"ig": "@vendilaskill", "tiktok": null, "yt": null}
  },
  "brief_icp": {
    "chi_e_il_cliente": "freelance e consulenti 25-40, già con competenze, non sanno venderle",
    "dolori_segnalati": ["lavorano tanto ma guadagnano poco", "non chiudono i deal in chiamata"],
    "desideri_segnalati": ["raddoppiare il tasso di conversione sulle call di vendita"],
    "obiezioni_sentite": ["non sono un venditore", "abbassare il prezzo è l'unica soluzione"],
    "linguaggio_reale": ["deal", "call", "posizionamento", "proposta", "obiezione"]
  },
  "dry_run": false
}
```

**Output finale (approvazione):**
```json
{
  "slug": "vendi-la-skill",
  "stato": "approvato",
  "brand_kit_path": "brands/vendi-la-skill/brand-kit.json",
  "icp_path": "brands/vendi-la-skill/icp.json",
  "canva_brand_kit_id": "BKT-vls-0001",
  "approvato_da": "cf-r2-coord",
  "timestamp_approvazione": "YYYY-MM-DDTHH:MM:SS",
  "disponibile_per_ordini": true
}
```

---

## Gate BLOCCANTE — condizioni PASS

Il workflow non avanza al STEP 5 (approvazione) se almeno una delle seguenti condizioni
non è soddisfatta:

| Condizione | Verificatore | Descrizione |
|---|---|---|
| Schema brand_kit completo | CF-R2-QA | Tutti i campi §0 dossier presenti e non null-per-segnaposto |
| Palette HEX valide | CF-R2-QA | Ogni colore in formato `#RRGGBB` |
| Voice con esempi reali | CF-R2-QA | ≥2 esempi_si e ≥2 esempi_no non pari al segnaposto template |
| ICP compilato | CF-R2-QA | dolori, desideri, obiezioni, awareness_level, linguaggio presenti |
| Canva sync avviata | CF-R2-CANVA | template_ids.json presente (anche se vuoto) |

Un brand con gate non PASS rimane in stato "in_onboarding" nel registry e blocca tutti
gli ordini che lo referenziano.

---

## Idempotenza

Il workflow è idempotente: se rilancia su un brand già "in_onboarding", riprende dal passo
successivo all'ultimo completato (letto da `brands/<slug>/state.json`). Non ricrea file già
creati e conformi. Non re-esegue passi già PASS.

I file seed originali in `carousel-factory/brands/` non vengono mai modificati (ADR-003).

---

## Connessioni

- [[CF-R2-Brand-Kit-Registry]] · `README.md` — reparto owner del workflow
- [[cf-r2-coord]] · `agenti/cf-r2-coord.md` — orchestratore principale
- [[cf-r2-qa]] · `agenti/cf-r2-qa.md` — gate BLOCCANTE del workflow
- [[WF-BRAND-MAINTENANCE]] · `workflow/WF-BRAND-MAINTENANCE.md` — workflow successivo post-approvazione
