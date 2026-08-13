# ADR-011 — Censimento della quinta implementazione APEX-7 e chiusura del perimetro

- **Data:** 2026-08-13
- **Stato:** ATTIVO
- **Decisori:** Max (owner) · Claude (esecutore/controllore tecnico)
- **Estende:** [ADR-010](ADR-010-fusione-ruflo-apex7.md) (non lo sostituisce)

## Contesto

ADR-010 (2026-07-28) censiva **4** implementazioni APEX-7-shaped divergenti e promuoveva
`11-APEX-7-CORE` a motore ufficiale della Coordination Fabric.

L'audit del 2026-08-13 (innesto dell'orchestration layer dallo zip `apex7_orchestrator`,
CP-20260813-001/002) ne ha trovate **due in piu'**, entrambe fuori dal censimento:

5. **`empire/intelligence/apex7/`** (~650 righe: `agents.py`, `backends.py`, `memory.py`,
   `orchestrator.py`, `quality.py`, `ruflo_adapter.py`, `__main__.py`). Non e' un
   abbozzo: e' **la piu' onesta di tutte le linee esistenti**. `backends.py` separa
   esplicitamente un `LocalMockBackend` deterministico da un `LLMBackend` reale
   OpenAI-compatibile; `ruflo_adapter.py` alza `NotImplementedError` scrivendo nero su
   bianco che il binding Rust verso `ruvnet/ruflo` non c'e' e cosa servirebbe per farlo
   (pyo3/maturin). Nessuna delle altre linee dichiara i propri limiti cosi'.
6. **Lo zip `apex7_orchestrator` stesso** — una sesta linea, mai entrata nel repo.
   Dichiarava una certificazione `100% PASS L1-L7` che non reggeva all'esecuzione
   (Gate L6 mai eseguito, stringa hardcoded, swarm simulato). Respinta come
   implementazione; ne sono state innestate solo le idee valide.

Il punto: ADR-010 nasce per curare la frammentazione, ma il censimento su cui poggia
era incompleto. Una linea non censita non e' governata da nessuno.

## Decisione

**Il perimetro APEX-7 si chiude a un solo motore (`11-APEX-7-CORE`) e a un solo elenco
censito.** Nello specifico:

1. `empire/intelligence/apex7/` entra nel censimento come **quinta linea, deprecata-non-
   cancellata** (ADR-003), esattamente come le altre tre non canoniche.
2. I suoi due pezzi che il motore canonico **non ha** vengono promossi, non buttati:
   - `backends.py` — il motore canonico oggi non ha un seam per il backend LLM: i suoi
     agenti sono logica Python fissa. Il seam `Backend` Protocol + `LocalMockBackend` /
     `LLMBackend` e' il pezzo mancante per far girare agenti veri.
   - `ruflo_adapter.py` — l'unico punto del repo che dichiara onestamente cosa manca per
     collegare RuFLO davvero. Va conservato come contratto, non riscritto.
   La promozione avviene in un ciclo dedicato (ADR-006), non in questo.
3. **Nessuna nuova implementazione APEX-7 puo' nascere fuori da `11-APEX-7-CORE`.**
   Chi ha bisogno di comportamento diverso usa il multi-tenant (`domain=...`) o innesta
   un sottopacchetto additivo, come ha fatto `orchestration/`.
4. Ogni linea APEX-7 va registrata in `company/REGISTRO-IMPRESA.md` (ADR-008). Una linea
   non registrata e' un artefatto orfano, e per ADR-008 non dovrebbe esistere.

## Alternative scartate

- **Cancellare `empire/intelligence/apex7/` subito** — scartata: viola ADR-003 (wrap, mai
  riscrittura senza sostituto validato) e butterebbe via i due pezzi migliori del repo su
  quel fronte, che il motore canonico non ha.
- **Promuovere `empire/intelligence/apex7/` a motore al posto di `11-APEX-7-CORE`** —
  scartata: e' piu' onesta ma molto piu' piccola, e non ha ne' il multi-tenant, ne' la
  memoria SQLite, ne' i consumatori gia' agganciati (YouTube, i 3 stream Arena).
  Ribaltare il canone ora rifarebbe da capo la Fase 1 di ADR-010, gia' pilotata.
- **Lasciarla non censita** — scartata: e' la condizione che ha prodotto il problema che
  ADR-010 cerca di curare.

## Conseguenze

- `company/Memory/BACKLOG.md` B-015 resta aperto e punta qui: la promozione di
  `backends.py`/`ruflo_adapter.py` e' il lavoro concreto che ne discende.
- `company/REGISTRO-IMPRESA.md` — riga aggiunta per `empire/intelligence/apex7/` con
  stato "deprecata-non-cancellata, 2 pezzi da promuovere".
- ADR-010 Fase 2 (estensione ai 13 ecosistemi) **non parte** finche' il censimento non e'
  chiuso e il seam backend non e' promosso: scalare una linea canonica che non sa ancora
  parlare a un LLM reale propagherebbe il limite su 13 ecosistemi invece che su uno.
- Lo zip `apex7_orchestrator` non entra nel repo: ne resta l'innesto in
  `11-APEX-7-CORE/orchestration/` e l'audit in CP-20260813-001.

## Contradiction-check

Verificato contro ADR-003 (wrap non riscrittura — rispettato: nessuna cancellazione, solo
deprecazione e promozione selettiva), ADR-005 (B-015 resta in backlog, non blocca),
ADR-006 (la promozione dei due pezzi e' rimandata a un ciclo dedicato), ADR-008 (colma una
lacuna dell'anagrafe: due linee erano orfane), ADR-009 e ADR-010 (estesi, non contraddetti:
`11-APEX-7-CORE` resta il motore canonico; cambia solo il numero di linee censite e il
prerequisito per la Fase 2). Nessun conflitto irrisolto.
