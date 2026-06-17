---
Type: WORKFLOW
Status: Active
Tags: #workflow #cro #pricing #catalogo #lotto #B-003
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-PRICING — Gestione Pricing e Aggiornamento Catalogo

> **ID:** WF-CRO-003 · **Owner:** `cro-conductor` · **Blueprint:** `BP-CRO.md`
> **Trigger:** richiesta di variazione prezzo O blocco sconto da `cro-pricing-arbiter`
> **Importante:** le variazioni del catalogo richiedono approvazione lotto MAXIMILIAN/CEO.

---

## Scopo

Gestire in modo strutturato ogni richiesta di variazione del catalogo prezzi o di sconto
su singolo deal: dalla richiesta iniziale all'istruttoria B-003, dal passaggio al lotto
all'aggiornamento del catalogo e alla comunicazione ai nodi che usano i prezzi. Garantisce
che nessuno sconto improvvisato esca da Digital Empire e che ogni modifica del catalogo sia
tracciata, versionata e approvata.

---

## Attori

| Step | Agente |
|---|---|
| Trigger e blocco sconto | `cro-pricing-arbiter` |
| Orchestrazione | `cro-conductor` |
| Istruttoria B-003 | `cro-pricing-arbiter` |
| Approvazione lotto | MAXIMILIAN / CEO (umano o organo) |
| Aggiornamento catalogo | `cro-pricing-arbiter` + `cro-memoria` |
| Comunicazione aggiornamento | `cro-conductor` → tutti i nodi |

---

## Flusso passo-passo

```
[TRIGGER A] Richiesta sconto su deal specifico
  → da deal desk, da Max durante call, da prospect
         │
[TRIGGER B] Richiesta variazione catalogo strutturale
  → da CEO, da MAXIMILIAN, da analisi pattern loss (3+ deal stesso problema prezzo)
         │
         ▼
[STEP 1] cro-pricing-arbiter — verifica catalogo
  → prezzo proposto = uno dei 4 prodotti standard?
  → se SÌ: PASS_CATALOGO, workflow non si avvia (operazione non necessaria)
  → se NO: BLOCCA_SCONTO, avvia WF-PRICING
         │
         ▼
[STEP 2] cro-conductor — riceve il blocco e avvia istruttoria
  → classifica la richiesta: sconto puntuale (su deal) vs variazione strutturale (catalogo)
  → per sconto puntuale: valuta alternative prima dell'istruttoria (vedi Step 2a)
  → per variazione strutturale: avvia istruttoria B-003 direttamente (Step 3)

[STEP 2a — solo sconto puntuale] Alternative al ribasso
  → `cro-conductor` propone al richiedente alternative:
     - supporto esteso (30gg extra)
     - bundle upgrade (se budget ok)
     - pagamento dilazionato (se problema liquidità)
  → se il prospect accetta alternativa: deal prosegue a prezzo catalogo, workflow chiuso
  → se il prospect non accetta e il deal è strategico: procedi a Step 3
         │
         ▼
[STEP 3] cro-pricing-arbiter — istruttoria B-003
  → raccoglie: tipo richiesta, prodotto interessato, prezzo proposto, delta vs catalogo
  → raccoglie: razionale (motivo della variazione), tipo cliente, storia acquisti
  → stima impatto su margine: [DM] (non inventato — se non disponibile: "impatto non quantificabile")
  → propone alternativa al ribasso (se non già valutata in 2a)
  → produce dossier istruttoria strutturato
  → GATE: dossier completo (tutti i campi) → passa al lotto; incompleto → ritorna a raccolta dati
         │
         ▼
[STEP 4] Lotto MAXIMILIAN / CEO — approvazione
  → `cro-conductor` consegna il dossier al lotto (umano: Max o Gael)
  → il lotto decide: APPROVA variazione | APPROVA alternativa | RIGETTA
  → decisione registrata con data e motivazione
  → GATE: decisione esplicita del lotto → procedi; nessuna risposta entro scadenza deal → catalogo standard
         │
   ┌─────┴──────────────┐
  APPROVA             RIGETTA
   │                   │
   ▼                   ▼
[STEP 5a]          [STEP 5b]
Aggiornamento      Comunicazione
catalogo           al richiedente:
                   "prezzo catalogo
                   invariato + motivazione"
         │
         ▼ (solo se APPROVA)
[STEP 5a] cro-pricing-arbiter — aggiornamento catalogo
  → crea nuova versione catalogo: {versione, data, prezzi, approvato_da}
  → GATE: versione precedente archiviata prima di attivare la nuova (no sovrascrittura)
         │
         ▼
[STEP 6] cro-memoria — archiviazione versione
  → store nuova versione catalogo con tutti i metadati
  → catalogo precedente marcato "superseded" con data
         │
         ▼
[STEP 7] cro-conductor — comunicazione aggiornamento
  → notifica tutti i nodi che usano il catalogo:
     - `cro-deal-desk` (pricing check su nuovi deal)
     - A3-PRICE di Agency (preventivi)
     - `cro-infobusiness-launches` (se variazione riguarda IB)
  → log dell'aggiornamento in `board/cro/pricing/changelog.md`
```

---

## Gate bloccanti

| Gate | Condizione PASS | Blocca |
|---|---|---|
| G1 — Verifica catalogo | Prezzo proposto = catalogo | `cro-pricing-arbiter` → BLOCCA |
| G2 — Alternative valutate | Almeno 2 alternative proposte prima dell'istruttoria | Obbligatorio su sconto puntuale |
| G3 — Dossier B-003 completo | Tutti i campi popolati + impatto stimato O [DM] | `cro-pricing-arbiter` rigetta dossier incompleto |
| G4 — Approvazione lotto | Decisione esplicita con data | Senza ok lotto: catalogo standard immutato |
| G5 — Archiviazione versione | Versione precedente marcata "superseded" | Atomicità: mai 2 versioni "attive" |

---

## Input del workflow

```json
{
  "trigger": "sconto_puntuale | variazione_strutturale",
  "prodotto": "Outreach Factory | Content Factory | Second Brain | Engine Room",
  "prezzo_catalogo": 4000,
  "prezzo_richiesto": 3400,
  "delta": -600,
  "richiedente": "prospect | Max | CEO | MAXIMILIAN",
  "deal_id": "optional",
  "urgenza": "deal in scadenza | strategica | routine"
}
```

## Output del workflow

```json
{
  "esito": "PASS_CATALOGO | ALTERNATIVA_ACCETTATA | APPROVATO_LOTTO | RIGETTATO",
  "prezzo_finale_autorizzato": 4000,
  "catalogo_aggiornato": false,
  "nuova_versione_catalogo": "optional",
  "comunicazione_nodi": ["cro-deal-desk", "A3-PRICE"],
  "record_istruttoria": "board/cro/pricing/B003-YYYY-NNN.md",
  "decisione_lotto": {
    "approvato_da": "MAXIMILIAN",
    "data": "2026-06-17",
    "motivazione": "optional"
  }
}
```

---

## State

File: `board/cro/pricing/catalogo-corrente.json` — versione attiva del catalogo.
File: `board/cro/pricing/changelog.md` — storico di ogni variazione con data e approvatore.
File: `board/cro/pricing/istruttorie/` — archivio istruttorie B-003 (aperte + chiuse).

---

## Connessioni

- [[cro-conductor]] · `agenti/cro-conductor.md`
- [[cro-pricing-arbiter]] · `agenti/cro-pricing-arbiter.md`
- [[cro-deal-desk]] · `agenti/cro-deal-desk.md`
- [[cro-memoria]] · `agenti/cro-memoria.md`
- [[WF-DEAL]] · `workflow/WF-DEAL.md`
- [[CRO-v1]] · `company/Board-CSuite/CRO.md` §Offerta corrente
- [[13-DOSSIER-MANDATO]] · `PIANO-MAESTRO/13-DOSSIER-MANDATO-ECOSISTEMA.md` Art.3
