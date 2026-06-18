---
Type: CONCEPT
Status: Active
Tags: #state #advertising #namespace #memoria #L2-2
Created: 2026-06-18
Last updated: 2026-06-18
---

# STATE — L2.2 Advertising

> Definizione del namespace memoria, schema state.json, regole di integrità e dry-run obbligatorio.
> Standard: CF-grade V2, test amnesia §6 Piano V2, namespace `marketing/ads/experiments`.

---

## 1. Namespace memoria (AgentDB/HNSW)

| Namespace | Contenuto | Owner scrittura | Owner lettura |
|---|---|---|---|
| `marketing/ads/experiments` | Matrici test, varianti, verdetti winner/perdente, pattern | AN3 (L2.4) / AD6 scrivono | AD2 legge prima di costruire nuove varianti |
| `marketing/ads/campaigns` | Setup campagne: struttura, budget, pacing, stato, state.json | AD3 scrive, ADS-LEAD aggiorna | ADS-LEAD / AD3 leggono |
| `marketing/ads/patterns` | Pattern creativi vincenti per ICP + piattaforma | AD6 scrive, AN4 (L2.4) consolida | AD2 legge come brief pre-costruzione |
| `marketing/ads/compliance-log` | Log G3 compliance: campaign_id, creative_id, esito, timestamp | AD4 scrive | ADS-LEAD, audit trail |
| `marketing/ads/qa-log` | Log AD-QA: campaign_id, creative_id, esito, dimensioni, timestamp | AD-QA scrive | ADS-LEAD, audit trail |

---

## 2. Schema state.json (per campagna)

Ogni esecuzione di WF-ADS-CAMPAIGN produce e aggiorna `marketing/ads/campaigns/{campaign_id}/state.json`.

```json
{
  "campaign_id": "campo popolato a runtime dal primo agente che crea la campagna",
  "committente": "01-AGENCY | 02-INFO | 04-MKT",
  "piattaforme": ["Meta", "Google", "LinkedIn", "TikTok"],
  "budget_approvato_EUR": "campo popolato a runtime",
  "envelope_cost_sentinel_EUR": "campo popolato a runtime",
  "budget_ok_max": true,
  "dry_run": true,
  "production": false,
  "approval_timestamp": "campo popolato a runtime solo dopo ok Max",
  "approver": "campo popolato a runtime solo dopo ok Max",
  "workflow_corrente": "WF-ADS-CAMPAIGN | WF-CREATIVE-TEST | WF-ADS-PERFORMANCE",
  "passo_corrente": "campo popolato a runtime (nome passo)",
  "g1_copy_pass": "pending | PASS | FAIL",
  "g3_compliance": {
    "Meta": "pending | PASS | FAIL",
    "Google": "pending | PASS | FAIL",
    "LinkedIn": "pending | PASS | FAIL",
    "TikTok": "pending | PASS | FAIL"
  },
  "ad_qa_gate": "pending | PASS | FAIL",
  "creative_matrix_id": "campo popolato a runtime",
  "n_varianti_pronte": 0,
  "winner_corrente": "campo popolato a runtime dopo primo test chiuso",
  "cicli_ottimizzazione": 0,
  "pattern_salvati": 0,
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

---

## 3. Regole di integrità

**R1 — dry_run = true per default:**
Ogni state.json creato da AD3 ha `dry_run: true` e `production: false`. Questi valori non
possono essere modificati da AD3 o AD2 — solo ADS-LEAD può impostare `production: true` e
SOLO dopo aver ricevuto e registrato l'approvazione esplicita di Max.

**R2 — approval_timestamp obbligatorio per production:**
Il campo `production: true` è invalido senza `approval_timestamp` e `approver` popolati.
Un state.json con `production: true` e `approval_timestamp: null` è uno stato corrotto
da segnalare immediatamente ad ADS-LEAD e loggare come incidente.

**R3 — gate in ordine sequenziale:**
I campi gate nel state.json devono avanzare nell'ordine: g1_copy → g3_compliance → ad_qa_gate.
Un gate successivo non può essere PASS se il gate precedente non è PASS. Qualsiasi inversione
è uno stato invalido.

**R4 — experiments con verdetto:**
Ogni record in `marketing/ads/experiments` deve avere campo `verdetto` con uno tra:
`winner_id` (creative vincitrice), `inconclusivo` (campione non sufficiente), `in_corso`.
Un record senza campo `verdetto` non è un esperimento chiuso.

**R5 — ripartibilità a freddo:**
Ogni agente che riprende un workflow interrotto DEVE leggere lo state.json prima di procedere.
Non si rispara la campagna da zero; si riprende dal `passo_corrente` indicato nello state.
Questo è il test amnesia §6 V2: un agente che non legge lo state è un agente che non rispetta
la ripartibilità.

---

## 4. Dry-run obbligatorio — come funziona

Il dry-run non è un'opzione di UI: è un campo obbligatorio nel state.json che protegge da
lanci accidentali. Il flusso per passare da dry-run a produzione:

```
1. AD3 produce campaign_plan.json con dry_run: true
2. Tutti i gate passano (G1, G3, AD-QA)
3. ADS-LEAD produce pacchetto approvazione per Max
4. Max approva esplicitamente (risposta registrabile: messaggio, email, Notion task)
5. ADS-LEAD aggiorna state.json:
   - dry_run: false
   - production: true
   - approval_timestamp: "YYYY-MM-DDTHH:MM:SSZ"
   - approver: "Max"
6. Solo ora AD3 può procedere al lancio reale
```

Qualsiasi salto di questo flusso = incidente da loggare + escalation CMO/CFO.

---

## 5. Pattern schema (per `marketing/ads/patterns/{icp_piattaforma}`)

```json
{
  "pattern_id": "campo popolato a runtime",
  "tipo": "copy-hook | copy-cta | visual-formato | audience-segment",
  "pattern_descritto": "descrizione del pattern vincente",
  "evidenza": "CTR X% vs Y%; CPA -Z%; campione N impressioni",
  "icp": "id ICP di riferimento",
  "piattaforma": "Meta | Google | LinkedIn | TikTok",
  "contesto_campagna": "categoria prodotto + obiettivo",
  "data_primo_osservato": "YYYY-MM-DD",
  "n_conferme": 1,
  "stato": "osservato | confermato (n_conferme >= 3)"
}
```

**Regola di consolidamento:** un pattern diventa "confermato" solo dopo 3+ osservazioni
indipendenti. Un singolo test non crea un pattern confermato. AD6 scrive il pattern come
"osservato"; AN4 (L2.4) lo promuove a "confermato" dopo la terza evidenza.

---

## Connessioni

- [[KPI]] · `kpi/KPI.md`
- [[REGOLE]] · `regole/REGOLE.md` — vincoli su dry-run e approvazione
- [[ad3-media-buyer]] · `agenti/ad3-media-buyer.md`
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §9 namespace`
