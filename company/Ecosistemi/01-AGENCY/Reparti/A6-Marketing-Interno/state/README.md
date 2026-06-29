---
Type: STATE
Status: Active
Tags: #state #namespace #memoria #marketing-interno #proof #A6
Created: 2026-06-23
Last updated: 2026-06-23
---

# State — A6 Marketing Interno & Proof

> Definizione dei namespace memoria, struttura dei file di stato, regole di integrità,
> e lifecycle degli artefatti del reparto. Namespace radice: `agency/a6/`.

---

## Namespace memoria del reparto

| Namespace | Path AgentDB | Contenuto | Owner scrittura | Chi legge |
|---|---|---|---|---|
| Case studies | `agency/a6/case-studies/` | Case study per cliente: APSOC, metriche verificate, stato gate, pubblicazione | AG-A6-CASE | AG-A6-COORD, AG-A6-QA, A2 |
| Proof | `agency/a6/proof/` | Testimonianze + metriche raccolte: fonte, consenso, valore | AG-A6-PROOF | AG-A6-CASE, AG-A6-QA |
| Vetrina | `agency/a6/vetrina/` | Stato landing/presentazione: gap, ticket 06-PLATFORM, deploy | AG-A6-COORD | AG-A6-QA, AG-A6-INBOUND |
| Upsell | `agency/a6/upsell/` | Proposte upsell/referral: prodotto attuale, next, segnale NPS, esito | AG-A6-UPSELL | AG-A6-COORD, A3 |
| Inbound | `agency/a6/inbound/` | Lead inbound: fonte, conversione, ottimizzazioni suggerite | AG-A6-INBOUND | AG-A6-COORD, A2 |

---

## Struttura file di stato

### Case study state (`agency/a6/case-studies/{case_id}/state.json`)

```json
{
  "case_id": "CASE-001",
  "cliente": "CLIENTE-X",
  "servizio_erogato": "CRO sprint | outreach | Engine Room",
  "data_avvio": "YYYY-MM-DD",
  "proof_status": "metriche_verificate | qualitativo | cliente_silente",
  "metriche": [
    {"nome": "conversione checkout", "valore": "+38%", "fonte": "report A4 + dashboard cliente"}
  ],
  "consenso_pubblicazione": "confermato | anonimizzato | assente",
  "brand_gate": "pending | PASS | FAIL",
  "brand_gate_motivo": "optional — dettaglio se FAIL",
  "asset_status": "richiesto_CF | consegnato | non_richiesto",
  "stato_finale": "in_progress | pubblicato | chiuso_senza_pubblicazione",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Upsell state (`agency/a6/upsell/{cliente}.json`)

```json
{
  "cliente": "CLIENTE-X",
  "segnale": "90gg_finiti + nps>=8",
  "nps": 9,
  "prodotto_attuale": "CRO sprint singolo",
  "next_mappato": "Engine Room €8.000 | referral_ask | nessuno",
  "tipo": "upsell | referral",
  "razionale": "basato sul risultato reale ottenuto",
  "handoff_a3": true,
  "esito": "proposto | contratto | declinato | in_attesa",
  "data_chiusura": "YYYY-MM-DD"
}
```

### Inbound state (`agency/a6/inbound/{periodo}.json`)

```json
{
  "periodo": "YYYY-MM",
  "lead_inbound": "[DM]",
  "call_prenotate_inbound": "[DM]",
  "tasso_conversione": "[DM]",
  "drop_identificati": ["nessun case study settore X"],
  "ottimizzazioni_suggerite": [
    {"gap": "...", "azione": "ticket WF-ASSET-VETRINA"}
  ],
  "stato": "misurato | tracking_assente"
}
```

---

## Regole di integrità dei namespace

1. **Claim senza `fonte`** — nessuna metrica in `agency/a6/case-studies` o `agency/a6/proof`
   può esistere senza campo `fonte` popolato e verificabile. AG-A6-QA è responsabile.
   Numero senza fonte = violazione R1 = blocco pubblicazione.

2. **Case study pubblicato senza `brand_gate: PASS`** — un case study in stato `pubblicato`
   deve avere `brand_gate: "PASS"`. Se `FAIL` o `pending`, non può essere `pubblicato`.

3. **Pubblicazione senza `consenso_pubblicazione`** — un case study con nome cliente non può
   essere `pubblicato` senza `consenso_pubblicazione: "confermato"`. Senza consenso →
   `anonimizzato` o blocco (R2).

4. **Upsell senza segnale valido** — nessun record in `agency/a6/upsell` con `tipo: upsell`
   senza `segnale` che includa `nps>=8` e `90gg_finiti` (R3).

5. **Ripartibilità a freddo** — tutti i file di stato hanno `last_updated`. Un agente che
   riprende un workflow interrotto legge lo state per sapere a quale step riprendere. Lo state
   deve rispecchiare esattamente il punto attuale del workflow.

---

## Lifecycle degli artefatti

| Artefatto | Creazione | Aggiornamento | Archiviazione |
|---|---|---|---|
| Proof | Step raccolta WF-CASE-STUDY | Alla verifica metriche | Conservato; linkato al case study |
| Case study state | Step scrittura WF-CASE-STUDY | Ad ogni step (gate, asset, pubblicazione) | Dopo `pubblicato`; non eliminato |
| Vetrina state | Step gap WF-ASSET-VETRINA | Ad ogni ticket/deploy | Aggiornato in continuo; non archiviato |
| Upsell state | Step segnale WF-UPSELL-REFERRAL | All'esito (contratto/declinato) | Dopo chiusura; non eliminato |
| Inbound state | Periodicamente (mensile) | Non aggiornato dopo il periodo | Storico conservato per trend |

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §4` — namespace e integrazione con altri sistemi
- [[WF-CASE-STUDY]] · `workflow/WF-CASE-STUDY.md` — produce proof + case study state
- [[WF-UPSELL-REFERRAL]] · `workflow/WF-UPSELL-REFERRAL.md` — produce upsell state
- [[kpi/KPI]] · `kpi/KPI.md` — i KPI si misurano a partire da questi namespace
