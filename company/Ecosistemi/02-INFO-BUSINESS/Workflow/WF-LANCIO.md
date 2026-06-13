# WF-LANCIO — Lancio Orchestrato T-30 → T+7

## Reparto: L2-LANCI
## Owner: IB-LAUNCH-coordinator (Opus durante lancio)

## Trigger
Gate B3 verde (corso live su piattaforma, smoke test OK) + budget approvato da OPERATIONS + catalogo con prezzo deciso (gate B1).

## Input (payload)
```json
{
  "prodotto": "nome-corso",
  "piattaforma_url": "url corso",
  "lista_email": "size lista + fonte",
  "budget_lancio": "EUR",
  "finestra_temporale": "data T0 proposta",
  "include_webinar": true,
  "offer_stack": "prodotto + bonus + garanzia + bump"
}
```

## Pipeline

### PRE-LANCIO (T-30 → T-1)

**T-30** — `IB-LAUNCH-coordinator` + `ib-launch-planner`: calendario completo con ogni task, owner, dipendenza, deadline

**T-28** — HANDOFF → INTELLIGENCE: customer research approfondita / angoli lancio
- Payload: ICP, obiezioni top 5, domande frequenti, concorrenti
- Frame: Thought Leader Funnel / Founder Authority Stack (ingest Beggiato)

**T-21** — HANDOFF → CONTENT-FACTORY: brief contenuti organici pre-lancio
- Calendario pezzi: almeno 3 caroselli/post/reel tematici prima del cart open
- Per ogni pezzo: angolo, hook, CTA, formato

**T-14** — HANDOFF → MARKETING (via `IB-COPY-liaison`): sales page + sequenza pre-lancio
- Payload JSON formato standard §1.2 dossier
- Acceptance: APSOC ≥80; CTA univoca; zero claim non provati
- Deadline rientro: T-7

**T-7** — `IB-COPY-liaison`: tutte le email cart open/close rientrate e validate APSOC ≥80
- Se <80: rework automatico, non si programma

**T-5** — `IB-WEBINAR-host` (se webinar incluso): script completo + setup tecnico pronti

**T-3** — T-CALENDARIO: checklist 100%:
- Sales page live + testata su mobile/desktop
- Checkout testato con transazione reale (importo simbolico)
- Tracking eventi attivo (UTM, pixel, analytics)
- Email programmate nella piattaforma (non inviate)
- Accessi piattaforma corso configurati per coorte lancio

**T-1** — DRY-RUN completo (pattern #3):
- `IB-LAUNCH-coordinator` simula l'intero flusso: email invio → click → sales page → checkout → accesso corso
- Stima costi token/infrastruttura → Cost-Sentinel valuta (budget +/-20%)
- Lista issue con priorità: P0 (blocca go), P1 (da risolvere prima T0), P2 (post-lancio)

**T-0-ε** — GO/NO-GO: hive-mind consensus
- Votanti: IB-0-conductor, Quality-Sentinel, Brand-Voice-Sentinel, Cost-Sentinel
- Regola: consensus UNANIME. Un NO blocca → escalation a Board con issue specifica

### CART OPEN (T0 → T+4/6)

**T0** — Apertura: email 1 "il carrello è aperto" + post social + webinar (se previsto)

**T+1..n** — Sequenza cart open:
- 1 email = 1 obiezione (lista obiezioni da customer research T-28)
- Social proof progressivo: case study, screenshot, testimonianze
- FAQ live se webinar attivo

**Ogni 24h** — `IB-SALES-funnel`: report conversioni per step (visitatori sales page, checkout, acquisti, tasso conversione email)
- Micro-aggiustamenti permessi: solo copy soggetto email, non offerta o prezzo
- Modifica struttura/offerta → escalation a IB-0-conductor + Board

### CART CLOSE (ultime 48h)

- Scarcity REALE: deadline è il limite reale del carrello o scadenza bonus (Mandato Empire: mai finta)
- Email close x3: urgenza → ultime 24h → ultime ore
- Chiusura checkout all'ora esatta annunciata

### POST-LANCIO (T+1 → T+7)

**T+1** — `IB-COMMUNITY-manager`: onboarding acquirenti ≤24h dall'acquisto

**T+3** — `IB-SALES-funnel`: report numeri reali lancio (conversione, revenue, AOV, costi)

**T+7** — `ib-debriefer`: post-mortem strutturato
- Piano vs reale per ogni KPI
- Root cause dei gap
- Pattern per ReasoningBank (namespace `infobusiness/reasoningbank`)

**T+7** — `IB-COMMUNITY-manager` `ib-crosssell-scout`: primi segnali cross-sell → AGENCY

## Gate (soglie)
| Gate | T | Criterio |
|---|---|---|
| Checklist asset | T-3 | 100% task checklist completati |
| Dry-run | T-1 | Flusso completo OK + budget approvato |
| GO/NO-GO | T-0-ε | Consensus unanime Sentinels |
| Debrief | T+7 | Entry ReasoningBank scritta |

## Output
Lancio chiuso + report numeri reali + debrief in ReasoningBank + coorte studenti in onboarding + lista lead cross-sell qualificati per AGENCY.

## Dry-run: come si esegue
Simulazione completa: `IB-LAUNCH-coordinator` percorre il flusso come uno studente — clicca link email → apre sales page → aggiunge al carrello → checkout → accesso corso. Ogni step viene registrato. Stima costi API + tool.

## Handoff in uscita
```json
{
  "from": "infobusiness/lanci",
  "to": "infobusiness/community",
  "payload": {
    "lancio": "nome-corso",
    "acquirenti": "lista email acquirenti",
    "data_acquisto": "timestamp",
    "accesso_piattaforma": "configurato"
  },
  "acceptance_criteria": ["accesso attivo entro 24h", "email benvenuto inviata"]
}
```
