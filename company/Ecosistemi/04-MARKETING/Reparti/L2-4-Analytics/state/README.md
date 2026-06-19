---
Type: STATE
Status: Active
Tags: #state #namespace #memoria #analytics #pattern #ReasoningBank #L2.4
Created: 2026-06-18
Last updated: 2026-06-18
---

# State e Namespace Memoria — L2.4 Analytics & Ottimizzazione

> **Reparto:** L2.4 · **Ecosistema:** 04-MARKETING · **Versione:** v2

---

## 1. Namespace AgentDB del reparto

| Namespace | Contenuto | Owner scrittura | Owner lettura | Agente writer |
|---|---|---|---|---|
| `marketing/copy/patterns/{icp}` | Pattern copy vincenti per ICP — cuore del vantaggio cumulativo | AN4 | COPY-MASTER (L2.1), A3-A7 | AN4 via script `pattern-writer` |
| `marketing/copy/antipatterns/{icp}` | Cosa non funziona per quell'ICP (da ReasoningBank) | AN4 | COPY-MASTER, A8 | AN4 via script `pattern-writer` |
| `marketing/copy/scores` | Storico score APSOC per copy_id (trend qualità) | A8 / COPY-QA-LEAD (L2.1) | AN2 | A8 (L2.1) |
| `marketing/ads/experiments` | Matrici test, varianti, campioni, verdetti | AN3 / AD6 (L2.2) | AN-LEAD, AD-LEAD | AN3 via WF-AB-TEST |
| `marketing/analytics/tracking/{campagna_id}` | Tracking plan + verifica pre-lancio | AN1 | AN2, AN-OBSERVER | AN1 via WF-TRACKING-SETUP |
| `marketing/analytics/optimization-loops/{ciclo_id}` | State dei cicli WF-OPTIMIZATION-LOOP | AN-LEAD | AN-OBSERVER | AN-LEAD via WF-OPTIMIZATION-LOOP |

---

## 2. Schema pattern (namespace `marketing/copy/patterns/{icp}`)

```json
{
  "icp": "freelance-digitale-ita",
  "formato": "ad | email | sales-page | social",
  "sezione_apsoc": "A | P | S | O | CTA",
  "pattern": "testo del pattern operativo (specifico, non generico)",
  "evidenza": {
    "n_run": 2,
    "copy_ids": ["CP-001", "CP-004"],
    "metrica": "CTR medio 2.7% su 2 campagne Meta"
  },
  "data_consolidamento": "YYYY-MM-DD",
  "stato": "consolidato | in_osservazione"
}
```

## 3. Schema antipattern (namespace `marketing/copy/antipatterns/{icp}`)

```json
{
  "icp": "freelance-digitale-ita",
  "formato": "ad | email | sales-page | social",
  "sezione_apsoc": "A | P | S | O | CTA",
  "antipattern": "testo dell'antipattern (cosa non fare — specifico)",
  "evidenza": {
    "n_run": 2,
    "copy_ids": ["CP-002", "CP-005"],
    "metrica": "CTR medio 0.95% (benchmark: 2.7% del pattern vincente)"
  },
  "motivo_fallimento": "spiegazione diagnostica del perché non funziona per quell'ICP",
  "data_consolidamento": "YYYY-MM-DD"
}
```

## 4. Schema tracking plan (namespace `marketing/analytics/tracking/{campagna_id}`)

```json
{
  "tracking_plan_id": "TP-001",
  "campagna_id": "CAMP-001",
  "data_creazione": "YYYY-MM-DD",
  "eventi": [
    {
      "nome": "snake_case_event_name",
      "trigger": "descrizione trigger precisa",
      "valore": "cosa misura: valore, categoria, evento GA4",
      "piattaforma": "GA4 | Meta Pixel | conversion API"
    }
  ],
  "utm_schema": {
    "utm_campaign": "CAMP-001",
    "utm_content": "copy_id placeholder — popolato a runtime per variante"
  },
  "conversion_api": {
    "eventi_server_side": ["event_name_1", "event_name_2"],
    "pii_minimizzato": true
  },
  "eventi_fantasma": 0,
  "stato": "bozza | consegnato_06-PLATFORM | verificato_pre-lancio | PASS"
}
```

## 5. Schema ciclo ottimizzazione (namespace `marketing/analytics/optimization-loops/{ciclo_id}`)

```json
{
  "ciclo_id": "LOOP-001",
  "campagna_id": "CAMP-001",
  "data_apertura": "YYYY-MM-DD",
  "icp": "freelance-digitale-ita",
  "passi": {
    "p1_raccolta": {"stato": "completato", "timestamp": "YYYY-MM-DDTHH:MM:SS"},
    "p2_diagnosi": {"stato": "completato", "sezione_debole": "A"},
    "p3_distillazione": {"stato": "completato", "pattern_scritti": 1, "antipattern_scritti": 1},
    "p4_revisione": {"stato": "completato", "copy_id_revisionato": "CP-001-revised"},
    "p5_test": {"stato": "completato", "test_id": "EXP-001", "verdetto": "PASS"},
    "p6_consolida": {"stato": "completato", "winner": "CP-001-revised"}
  },
  "stato_ciclo": "raccolta_aperta | diagnosi_completata | distillazione_completata | variante_prodotta | test_completato | consolidato | inconclusivo",
  "data_chiusura": "YYYY-MM-DD"
}
```

---

## 6. Regole di integrità del namespace (anti-rumore)

1. **Un pattern non si scrive con `n_run < 2`** — lo script `pattern-writer` rifiuta
   la scrittura e restituisce exit code 1. Il record va in state come "segnale da monitorare".
2. **Un antipattern senza `motivo_fallimento`** non è un antipattern utile: è solo un
   dato negativo. Lo script `pattern-writer` richiede il campo.
3. **Un pattern contradittorio con uno esistente** (stessa ICP, formato, sezione, ma
   conclusione opposta) non si sovrascrive automaticamente: AN4 porta la contraddizione
   ad AN-LEAD per diagnosi prima della scrittura.
4. **Stato `in_osservazione`** significa: il pattern ha n_run = 1, non è ancora affidabile.
   COPY-MASTER può usarlo come "segnale" ma non come "best practice".
5. **Wiki-first per pattern con n_run ≥ 3:** questi vengono anche scritti in wiki
   `concepts/` o `synthesis/` e logati in `wiki/log.md` (regola §9 dossier v2).

---

## Connessioni

- [[an4-insight-distiller]] · `agenti/an4-insight-distiller.md` — owner scrittura patterns
- [[an1-tracking-engineer]] · `agenti/an1-tracking-engineer.md` — owner tracking plans
- [[WF-OPTIMIZATION-LOOP]] · `workflow/WF-OPTIMIZATION-LOOP.md`
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §9`
