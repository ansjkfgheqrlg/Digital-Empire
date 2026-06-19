---
Type: WORKFLOW
Status: Active
Tags: #workflow #content-factory #CF-R2 #maintenance #brand-drift #campionamento #patch
Created: 2026-06-19
Last updated: 2026-06-19
---

# WF-BRAND-MAINTENANCE — Monitoraggio Drift e Manutenzione Brand

> **ID:** WF-R2-002 · **Owner:** `cf-r2-coord` · **Reparto:** CF-R2 Brand-Kit & Tenant Registry
> **Trigger:** alert drift da CF-R2-DRIFT, oppure richiesta aggiornamento brand_kit da committente

---

## Scopo

Rilevare sistematicamente il brand-drift negli output di produzione, correggerne la causa
(nel brand_kit o nel processo produttivo), e mantenere ogni brand_kit aggiornato e validato
nel registry. Il brand-drift non si cura con la speranza che i reparti producano bene:
si monitora, si rileva, si corregge prima che diventi un pattern.

Due trigger distinti:
1. **Drift ciclico** — CF-R2-DRIFT ha rilevato deviazioni in ≥3 output su 5 campionati → alert.
2. **Aggiornamento brand** — il committente ha aggiornato il proprio brand (restyling, nuovo tono,
   nuovo canale) → brand_kit da aggiornare + re-validazione + nuova versione.

**Cadenza drift check:** ogni ciclo di produzione (definito da CF-Director). Tra un ciclo e
l'altro, CF-R2-DRIFT resta in ascolto passivo; il campionamento attivo scatta a fine ciclo.

---

## Attori

| Step | Agente | Funzione |
|---|---|---|
| Coordinamento | `cf-r2-coord` | Riceve alert/richiesta; decide percorso; gestisce escalation |
| Campionamento | `cf-r2-drift` | Esegue campionamento ≥5 output e produce alert strutturato |
| Correzione | `cf-r2-creator` | Applica patch al brand_kit (se drift causato da brand_kit errato) |
| Aggiornamento ICP | `cf-r2-icp` | Aggiorna icp.json se il drift indica shift nell'audience |
| Re-validazione | `cf-r2-qa` | Verifica brand_kit patchato — gate BLOCCANTE |

---

## Flusso passo-passo

```
[TRIGGER A — drift alert]               [TRIGGER B — aggiornamento committente]
CF-R2-DRIFT emette alert                Committente invia brief aggiornamento brand
        │                                               │
        └──────────────────┬────────────────────────────┘
                           ▼
[STEP 1] CF-R2-COORD — ricezione e classificazione
  → Se TRIGGER A (drift): analizza alert — quale dimensione? quanti output?
    → Drift su palette/font → probabile errore template produzione (R5/R3) → segnala a L1-PROD
    → Drift su voice → probabile errore brand_kit voice (parole vietate non aggiornate) o
      errore agente produzione → indaga entrambe le ipotesi
    → Drift sistemico su 3+ brand → segnala a L1-PRE (problema trasversale)
  → Se TRIGGER B (aggiornamento): identifica i campi da aggiornare; avvia STEP 2 direttamente
  → Aggiorna brands/<slug>/state.json: fase = "in_maintenance"
        │
        ▼
[STEP 2] CF-R2-DRIFT — campionamento approfondito (solo per TRIGGER A)
  → Campiona ≥5 output aggiuntivi (cicli precedenti) per verificare se il drift è recente
    o strutturale
  → Classifica deviazioni: occasionale (1-2 output), ricorrente (3+ output), strutturale
    (presente in 2+ cicli consecutivi)
  → Output: report campionamento con classificazione
        │
        ▼
[STEP 3] CF-R2-COORD — decisione percorso
  → Deviazione occasionale: log in state.json, nessuna modifica brand_kit; segnala a reparto
    produzione per correzione puntuale (fuori da questo workflow)
  → Deviazione ricorrente da brand_kit: avanza a STEP 4 (patch brand_kit)
  → Deviazione ricorrente da processo produzione: segnala a L1-PROD con dettaglio (fuori workflow)
  → Aggiornamento committente (TRIGGER B): avanza a STEP 4
        │
        ▼
[STEP 4] CF-R2-CREATOR — patch brand_kit
  → Apre brands/<slug>/brand-kit.json
  → Applica le modifiche indicate: aggiorna SOLO i campi da patchare
  → Incrementa versione in state.json: brand_kit_version (es. "1.0" → "1.1")
  → Salva il brand_kit precedente in brands/<slug>/history/brand-kit-v<N>.json
  → Annota il changelog: campo modificato, valore precedente, valore nuovo, motivo
  → Non tocca i campi non coinvolti nella patch
        │
        ▼
[STEP 4B — opzionale] CF-R2-ICP — aggiornamento icp.json
  → Solo se il drift o l'aggiornamento committente indica un cambio di audience o linguaggio
  → Aggiorna icp.json con nuova versione (incremento icp_version)
  → Salva versione precedente in brands/<slug>/icp-history/icp-v<N>.json
        │
        ▼
[STEP 5] CF-R2-QA — re-validazione (BLOCCANTE)
  → Esegue gate completo sul brand_kit patchato (stesse regole di WF-BRAND-ONBOARDING)
  → PASS → avanza a STEP 6
  → FAIL → lista errori → CF-R2-CREATOR per correzione → ritorna a STEP 5
        │
        ▼
[STEP 6] CF-R2-COORD — chiusura manutenzione
  → Aggiorna cf/brand-kits: ultima_validazione = timestamp corrente
  → Aggiorna brands/<slug>/state.json: fase = "approvato", brand_kit_version aggiornata
  → Se il drift era causato da processo produzione: segnala formalmente a L1-PROD
    con path degli output devianti e specifica della deviazione
  → Notifica al committente brand (se esterno): brand_kit aggiornato, versione e changelog
        │
        ▼
[OUTPUT]
brands/<slug>/brand-kit.json        → versione patchata, gate CF-R2-QA PASS
brands/<slug>/history/              → versione precedente brand_kit archiviata
brands/<slug>/state.json            → brand_kit_version aggiornata, changelog, ultima_validazione
cf/brand-kits (namespace)           → ultima_validazione aggiornata
[report a L1-PROD se drift da processo] → specifica deviazioni per correzione template
```

---

## I/O JSON del workflow

**Input (alert drift):**
```json
{
  "tipo": "drift_alert",
  "slug": "mentalita-brutale",
  "ciclo": "2026-06-19",
  "deviazioni": [
    {
      "dimensione": "voice",
      "n_output_devianti": 4,
      "esempi": [
        {"output_path": "orders/CF-2026-0031/output/caption.txt", "problema": "parola vietata: 'emozionante'"},
        {"output_path": "orders/CF-2026-0033/output/slide-01.html", "problema": "parola vietata: 'fantastico'"}
      ]
    }
  ]
}
```

**Input (aggiornamento committente):**
```json
{
  "tipo": "aggiornamento_brand",
  "slug": "mentalita-brutale",
  "committente": "DE-interno",
  "campi_da_aggiornare": {
    "voice.parole_vietate": ["emozionante", "fantastico", "incredibile", "viaggio", "motivazionale"],
    "voice.esempi_no": [
      "In questo emozionante percorso...",
      "Sei pronto a trasformare la tua vita?",
      "Insieme possiamo raggiungere qualsiasi obiettivo."
    ]
  },
  "motivo": "aggiornamento linee guida editoriali brand — nuova parola vietata aggiunta"
}
```

**Output finale:**
```json
{
  "slug": "mentalita-brutale",
  "manutenzione": "completata",
  "brand_kit_version": "1.2",
  "gate_qa": "PASS",
  "timestamp_validazione": "YYYY-MM-DDTHH:MM:SS",
  "changelog": [
    {
      "campo": "voice.parole_vietate",
      "precedente": ["emozionante", "fantastico", "incredibile", "viaggio"],
      "nuovo": ["emozionante", "fantastico", "incredibile", "viaggio", "motivazionale"],
      "motivo": "aggiornamento linee guida editoriali committente"
    }
  ],
  "history_path": "brands/mentalita-brutale/history/brand-kit-v1.1.json",
  "azione_produzione": "nessuna — drift da brand_kit non aggiornato, ora corretto"
}
```

---

## Gate re-validazione — condizioni PASS

Il workflow non chiude in "approvato" se il gate CF-R2-QA sul brand_kit patchato non è PASS.
Le condizioni sono identiche a WF-BRAND-ONBOARDING (schema completo, palette HEX valide,
voice con esempi reali). Un brand_kit patchato con errori introdotti dalla patch viene bloccato
esattamente come un brand_kit nuovo non valido.

---

## Regole di versioning

| Tipo modifica | Versione |
|---|---|
| Aggiunta/rimozione parola vietata | patch (1.0 → 1.1) |
| Aggiornamento esempi voice | patch (1.0 → 1.1) |
| Cambio palette o font | minor (1.0 → 1.1, con nota impatto produzione) |
| Cambio nome brand o slug | non permesso — richiede nuovo onboarding |
| Aggiunta canale | patch (1.0 → 1.1) |

---

## Connessioni

- [[CF-R2-Brand-Kit-Registry]] · `README.md` — reparto owner del workflow
- [[cf-r2-drift]] · `agenti/cf-r2-drift.md` — fonte degli alert drift che triggherano il workflow
- [[cf-r2-qa]] · `agenti/cf-r2-qa.md` — gate BLOCCANTE re-validazione
- [[WF-BRAND-ONBOARDING]] · `workflow/WF-BRAND-ONBOARDING.md` — workflow gemello (creazione)
