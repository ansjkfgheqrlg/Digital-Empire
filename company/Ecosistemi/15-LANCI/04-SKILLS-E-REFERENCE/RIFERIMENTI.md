# 04 — SKILL E RIFERIMENTI di LANCI

> Cosa l'ecosistema usa e non possiede. Ogni riga è un puntatore verificato il 2026-09-15
> (REGOLA PUNTATORI: se un file si sposta, questa riga si aggiorna nello stesso turno).

## 1. L'anatomia dei lanci di Andrei Pascu — RICEVUTA il 2026-09-15

Consegna di `TASK-LANCI-20260908-ANATOMIA-ANDREI-PASCU.md` (ADR-016, l'Ultimo Metro: una
consegna è fatta quando chi riceve la usa). Tre forme, tutte presenti sul disco:

| Forma | Percorso | Come LANCI la usa |
|---|---|---|
| Markdown | `competitor/Andrei Pascu/ANATOMIA-DEI-LANCI.md` (11 parti) | la fonte leggibile per `lan-off-conductor`, `lan-fnl-costruttore`, `lan-cpy-conductor` |
| Python | `competitor/Andrei Pascu/anatomia_lanci.py` — `python anatomia_lanci.py --check` esce 0; costanti `MODELLO_12_PASSI`, `SCALA_PREZZI`, `LEVE_OFFERTA`, `DIFETTI`, `STAMPO_PRECASSA`, `CONSEGNA_A_LANCI` | gli agenti la importano invece di rileggere la prosa |
| PDF | `documentazione Empire/Lanci/ANATOMIA-DEI-LANCI.pdf` (10 pagine) | la forma da mostrare |

**Dove entra nel registro — passo per passo:**

| Passo del modello (PARTE IX) | Dove vive in LANCI |
|---|---|
| 2 · somma i listini **pubblici** (ancora verificabile) | `ART-OFF.struttura.ancoraggio` + `bonus[].fonte_valore` — GATE-OFF-1 usa solo i bonus con fonte |
| 3 · un regalo che vale quanto il prezzo | `ART-OFF.struttura.bonus` e `rapporto_valore_prezzo` (soglia 3) |
| 4 · finestra di **tempo**, mai posti | `ART-OFF.durata_carrello_gg` + `motivo_per_agire_adesso` |
| 7 · **una** cassa sola | `ART-FNL.pagine[ruolo=checkout]` unica; `prova_cassa` su quella |
| 9 · gradino di pre-cassa | pattern `.claude/skills/fabbrica-siti/pattern/pre-cassa/` — `lan-fnl-costruttore` |
| 10 · codice sconto a scadenza, `noindex` | `ART-FNL` pagina `pre-cassa` (non indicizzata) |
| 11 · prezzo pagabile ≥ corpo del testo, mai in immagine | controllo 6-7 dell'anatomia → `lan-cpy-conductor`, `GATE-CPY-1` (affermazione con prova) |
| **12 · percorri la catena a macchina prima di aprire** | **`GATE-FNL-1`: ogni pagina risponde 200, riaperta dal gate; `GATE-REG-1`: lista di sincronizzazione tutta vera** |

**I difetti suoi che sono diventati nostri controlli:** «la cassa non risolve» (#1, il più costoso)
→ GATE-FNL-1 riapre ogni url con `Rete`, mai dal campo salvato.

**Cosa NON si copia:** limiti di posti su prodotti digitali; prezzo dentro un'immagine; codice sconto
pubblico e permanente (PARTE VII).

## 2. Skill e pattern che LANCI chiama

| Cosa | Percorso | Chi la usa |
|---|---|---|
| Fabbrica Siti (legge + canone + gate) | `.claude/skills/fabbrica-siti/` — `CLAUDE-SITI.md` | `lan-fnl-costruttore` per ogni pagina del funnel |
| stampo pre-cassa | `.claude/skills/fabbrica-siti/pattern/pre-cassa/` | `lan-fnl-costruttore` |
| pagina ponte | `.claude/skills/fabbrica-siti/pattern/pagina-ponte/` | `lan-fnl-costruttore` |
| copy APSOC | `.claude/skills/cro-copy-architect/`, `copywriting/`, `copy-editing/` (formazione Pascu innestata il 2026-09-10, CP-20260910-HYDJ) | `lan-cpy-conductor` |
| la cassa già costruita | `empire/tools/checkout.py` (`--accendi-stripe`, `--scadenza`, `--check`) | S0, `lan-fnl-costruttore` |
| la consegna già costruita | `KDP - prodottti digitali/Leanding Page/email-agent/` (webhook per prodotto, 25 test) | S0, `prova_cassa.consegna_verificata` |
| Tesoreria | `scripts/tesoreria.py` (ADR-020) — i soldi SALGONO lì, mai scendono | `scripts/ponte_tesoreria.py` |
| Ultimo Metro | ADR-016 — la coda in ingresso di questo ecosistema | `lan-str-filtro` |

## 3. Le leggi che valgono qui

ADR-025 (nasce LANCI; dec. 5: nessun motore nuovo) · ADR-026/027/028 (niente blocca tutto) ·
ADR-014 (il ponte verso i modelli) · ADR-016 (Ultimo Metro) · ADR-020 (Tesoreria) · ADR-003 (wrap).
