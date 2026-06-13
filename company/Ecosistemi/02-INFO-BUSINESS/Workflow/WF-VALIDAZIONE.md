# WF-VALIDAZIONE — Idea → Brief Validato

## Reparto: L2-PRODOTTO
## Owner: IB-VALIDATION-analyst + IB-PM-product-manager

## Trigger
Nuova idea di prodotto informativo (corso, ebook, webinar, guida) proposta da Board, BACKLOG, o segnale da community studenti / ecosystem AGENCY.

## Input (payload)
```json
{
  "idea": "titolo provvisorio + descrizione 3 righe",
  "fonte": "Board | BACKLOG | community | agency-segnale",
  "icp_ipotetico": "chi è il target",
  "materiale_raw_disponibile": "path cartella | nessuno",
  "urgenza": "alta | normale | bassa"
}
```

## Pipeline

1. **IB-VALIDATION-analyst** — ricerca evidenze per i 5 criteri (max 48h):
   - Criterio 1 — Domanda esistente: keyword research, community, prodotti concorrenti con social proof
   - Criterio 2 — Autorità DE: DE ha risultati/credibilità dimostrabili su questo topic?
   - Criterio 3 — Materiale raw: esiste già in `Formazzione/` o negli asset DE? (zero partenza da zero)
   - Criterio 4 — Velocità to market: MVP in <30gg? Dipendenze esterne?
   - Criterio 5 — Allineamento ecosistema: cross-sell AGENCY? Funnel evergreen?

2. **Scoring /100** (20 punti per criterio):
   - Per ogni criterio: 0 (no evidenza), 10 (evidenza debole), 15 (buona), 20 (forte)
   - Regola: nessun punteggio senza evidenza specifica citata

3. **Decisione routing** (IB-VALIDATION-analyst propone, IB-PM decide):
   - Score ≥60 → GO: entra in produzione con brief validato
   - Score 50-59 → MVP TEST 7 giorni: test minimo prima di produzione
   - Score <50 → BACKLOG con motivazione + riesamina tra [X settimane/mesi]

4. **MVP Test 7 giorni** (solo per 50-59):
   - Test a basso costo: landing con waitlist (>50 iscrizioni = segnale positivo), post di validazione, sondaggio lista esistente (≥5 "sì, lo comprerei" = segnale positivo)
   - Se test positivo → GO con brief validato
   - Se test negativo → BACKLOG con motivazione

5. **Brief validato** (solo per GO):
   - ICP confermato dalle evidenze (non ipotetico)
   - Outcome primario verificabile
   - Formato raccomandato (video/testo/ibrido) con motivazione
   - Materiale raw identificato (cartella path)
   - Prezzo di mercato stimato (input per IB-PM + gate B1)
   - Stima lead time produzione

## Gate (soglie)
| Gate | Criterio |
|---|---|
| Gate scoring | Score calcolato con evidenze reali, non opinioni |
| Gate brief | ICP, outcome, formato, raw e stima prezzo tutti compilati |
| Gate B1 (successivo) | Prezzo deciso e scritto nel catalogo prima di avviare produzione |

## Output
- Score /100 con breakdown per criterio
- Raccomandazione GO / MVP TEST / BACKLOG con motivazione
- Brief validato (per GO) → input per WF-CORSO o WF-EBOOK
- Entry in BACKLOG (per non-GO) con data riesame

## Dry-run: come si esegue
Esegui su un'idea già validata storicamente (es. Manuale Claude Code o Vendi la Skill n.1) e verifica che lo score rifletta la realtà di quel prodotto. Se lo score è <60 su un prodotto che ha funzionato → ricalibra i pesi.

## Handoff in uscita
```json
{
  "from": "infobusiness/prodotto/validazione",
  "to": "infobusiness/prodotto/produzione",
  "payload": {
    "prodotto": "titolo",
    "score": 72,
    "breakdown": {"domanda": 18, "autorita": 15, "raw": 20, "velocita": 10, "allineamento": 9},
    "icp": "descrizione validata",
    "outcome_primario": "...",
    "formato": "corso-video",
    "raw_path": "Formazzione/[folder]/",
    "prezzo_stimato": "197-297 EUR"
  },
  "acceptance_criteria": ["score ≥60 con evidenze", "brief completo"]
}
```
