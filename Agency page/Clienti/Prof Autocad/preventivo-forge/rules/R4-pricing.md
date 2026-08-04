# R4 — Pricing (S4)

**OBIETTIVO:** calcolare il prezzo finale al cliente e il titolo del preventivo, in modo
deterministico e per-concessionaria. Scrive la sezione `price` di `listing_it.json`.

**TRIGGER:** `run.py` step 4 (dopo S3 se presente; funziona anche senza S3). Script: `implementation/pricer.py`.

**FORMULA (confermata Max 2026-06-30):**
`finale = round(esposto × (1 + surcharge_pct/100) + fixed_1 + fixed_2)`
Parametri per dealer in `concessionarie/<id>/config.json → pricing` (default `.env`: 3%, 1500, 1500).

**INPUT**
| Campo | Obbligatorio | Fonte |
|---|---|---|
| `listing.json.price_listed_eur` | sì | S2 |
| `dealer.pricing_resolved` | sì | `dealers.load_dealer()` |
| `listing_it.json.content` | no | S3 (se presente, per titolo IT) |

**OUTPUT:** `listing_it.json.price` = `{listed_eur, final_eur, final_title, breakdown{listed,surcharge_pct,surcharge_eur,fixed_1,fixed_2,final}}`. **MERGE**: preserva `content` di Half B.

**STEP-BY-STEP**
1. Carica `listing.json`; se manca `price_listed_eur` → errore (stop).
2. `compute_price(listed, pct, f1, f2)` → breakdown.
3. `build_title(make, model, variant, final_eur)` → `"{nome} {prezzo IT} €"` (es. `... 21.540 €`).
4. Merge in `listing_it.json` (crea se assente; non tocca `content`).

**TEMPLATE titolo:** `{marca} {modello} {variant} {formato_IT(finale)} €` — es. `Mercedes-Benz GLA 220 d 4MATIC AMG Line 21.540 €`. Formato IT: `21540 → 21.540`.

**ESEMPIO VERIFICATO:** esposto 18.000 → 18.540 (+3%) + 3.000 = **21.540 €**.

**GESTIONE ERRORI**
| Errore | Causa | Azione |
|---|---|---|
| `price_listed_eur` mancante | estrazione fallita | ValueError → stop (Gate A avrebbe dovuto bloccare) |
| parametri dealer assenti | config incompleta | fallback ai default `.env` |

**CASI LIMITE:** prezzo con IVA (`price_is_gross`) → il calcolo usa comunque l'esposto (regola cliente); annotare se serve distinzione IVA in futuro (BACKLOG).

**LOG:** `logs/<run>.log` + `trace.jsonl` (`step S4` + `final_title`). Ricalcolo indipendente = Gate C (Half B).
