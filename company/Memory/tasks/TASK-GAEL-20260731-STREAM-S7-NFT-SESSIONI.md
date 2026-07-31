---
Owner: Max (committente) · Esecutore: GAEL · Controllore: Claude (gate APEX-7, su richiesta)
Origine: 12-STREAM-S7-BOT · Governo: ADR-006 (ciclo 9 passi) + REGOLA ZERO memory-first
Emesso: 2026-07-31 · Priorità: P1 (ordine diretto di Max)
Segue: TASK-GAEL-20260730-STREAM-S7-NFT-METODO.md (CHIUSO, CP-20260730-007) — non lo riapre,
       costruisce sopra. Quel verdetto (bocciato per live, Magic Eden/Solana) resta valido e
       non viene rifatto qui.
---

> **STATO: da avviare.** Nessuna sessione aperta.

# 🚨 ORDINE MAX — Flusso di tutte le sessioni, verso l'operativo reale

## 0. Cosa ha chiesto Max (riassunto, non verbatim questa volta — il verbatim è già nel task
precedente)

Un flusso con **tutte le sessioni da fare**, tutto quello che deve partire, per portare Stream
S7 dal punto in cui è ora (metodo NFT verificato ma bocciato per live) fino a "funziona nella
realtà". Ha corretto il sito di riferimento: non Magic Eden ma **mintify.xyz**, poi ha detto
esplicitamente **"usa quale sito vuoi"** — la scelta tecnica resta a chi esegue.

## 1. Cosa ho verificato su Mintify PRIMA di scrivere le sessioni (ricerca fatta ora, non
assunta)

`https://mintify.xyz/` non risponde (errore HTTP 530 — dominio irraggiungibile al momento della
verifica). Da ricerca: **Mintify è reale**, dominio ufficiale `mintify.com` — aggregatore
multichain + analytics + terminal di trading NFT, con API dati/analytics (`learn.mintify.xyz/api`
per la richiesta di accesso). Chain supportate dichiarate: **Ethereum, Blast, Base, Ordinals,
Flow, Apechain, Abstract, Berachain** — **Solana NON è nella lista**.

**Perché questo conta, non è un dettaglio**: tutto lo stack Stream S7 esistente è Solana-nativo
al 100% — `data_manager.py` ascolta il mempool Solana, `analysis_engine.py` legge
`getTransaction` su RPC Solana, `nft_magiceden_client.py` (appena chiuso) è scritto per Magic
Eden/Solana. **Passare a Mintify non è uno swap di endpoint, è un cambio di famiglia di
blockchain** (EVM/Ordinals invece di Solana) — nessun pezzo del parser dati esistente si riusa
direttamente.

**Nota di sicurezza, non richiesta ma dovuta**: nei risultati di ricerca compare anche
`mntfy.xyz` (senza la "i", http non https, sito diverso) spacciato per "Mintify App — Trade
Crypto & NFTs". **Non toccarlo.** Dominio simile a quello ufficiale, protocollo non sicuro,
pattern tipico di sito civetta. Usa solo `mintify.com` / la sua documentazione API ufficiale.

## 2. La scelta architetturale che questo apre (Gael decide, non io — ma va scritta prima di
partire)

| Opzione | Cosa significa | Riusa lo stack esistente? |
|---|---|---|
| **A — Resta su Magic Eden/Solana** | Il lavoro di ieri (CP-20260730-002→007) è già la risposta completa. Nessuna sessione nuova di analisi necessaria, solo eventuale esecuzione (vedi §4) | Sì, tutto |
| **B — Mintify come fonte dati aggiuntiva, esecuzione resta Solana** | Mintify usato solo per analytics/segnali cross-market, l'acquisto/vendita resta su Magic Eden/Solana | Parziale |
| **C — Nuovo layer EVM via Mintify** | Nuovo parser, nuovo wallet (EVM, non Solana), nuova execution — di fatto un secondo Stream S7 per un'altra blockchain | No, si ricostruisce |

**Raccomandazione di Claude (non vincolante, Gael/Max decidono)**: partire da **B**. È l'unica
opzione che non butta via il lavoro già chiuso e verificato (89/89 controlli) e testa se
Mintify aggiunge davvero edge (dati aggregati multi-marketplace, spesso migliori di uno
scraping singolo) prima di un investimento più grosso in un nuovo layer EVM (opzione C).

## 3. Il flusso — tutte le sessioni, in ordine

Ogni sessione è **un blocco chiuso**: apre solo dopo che la precedente ha un output verificato
(checkpoint con comando+risultato reale), non "in teoria dovrebbe". Stessa disciplina del task
precedente — niente scorciatoie.

### SESSIONE 1 — Ricognizione Mintify (informativa, zero rischio)
- Registrazione API (`learn.mintify.xyz/api` o quanto risulti dalla doc ufficiale al momento)
- Leggere: quali endpoint reali, rate limit, costo (free tier vs pagamento), formato dati
  (listing, floor, volume, rarity — stessi campi già usati per Magic Eden in
  `nft_magiceden_client.py`, per confronto diretto)
- Output: un documento `MINTIFY-RECON.md` in `12-STREAM-S7-BOT/`, stesso standard di
  `STUDIO-NFT-FASE0.md` — solo fatti verificati, non descrizioni da marketing del sito

### SESSIONE 2 — Decisione architetturale (documento, non codice)
- Sulla base della Sessione 1: confermare/cambiare l'Opzione A/B/C sopra
- Se B o C: quali chain EVM specifiche coprire prima (non "tutte", una alla volta)
- Output: nota di decisione in `STATO-EMPIRE.md` (blocco COORDINAMENTO), motivata

### SESSIONE 3 — Fase 0 bis: tecnica di studio riapplicata alla nuova fonte
- **Non riusare il verdetto di Magic Eden come se valesse anche qui.** Dati diversi, mercato
  diverso (EVM ha dinamiche di gas/MEV diverse da Solana) — richiede lo stesso rigore da capo:
  7 criteri della Fase 0 del task precedente (§2 di `TASK-GAEL-20260730-STREAM-S7-NFT-METODO.md`),
  applicati qui

### SESSIONI 4-7 — Ondata 1 equivalente (blocchi fondamentali) sulla nuova fonte
- Fonte dati Mintify (endpoint reali, non mock)
- Modello di fair value ricalcolato sui dati Mintify (il fit trovato debole su Magic Eden,
  bootstrap R² fino a 0.257, potrebbe essere diverso qui — o no, va misurato)
- Modello di costo reale per la chain scelta (gas fee EVM ≠ gas fee Solana, priority fee
  diversi — se resta B, il costo di *esecuzione* resta comunque quello Solana/Magic Eden)
- Position sizing: riusa `RiskManager` esistente, stesso principio del task precedente
- **Ogni sessione chiude con un numero reale**, non una stima

### SESSIONI 8-9 — Ondata 2 (miglioramenti) + Ondata 3 (perfezionamenti)
- Stessa struttura del task precedente (auto-calibrazione, filtro scam/wash-trading, backtest,
  intervallo di confidenza) applicata alla nuova fonte

### SESSIONE 10 — Ondata 4: controlli chirurgici, confronto A vs B/C
- Confronto numerico esplicito: il layer Mintify (se costruito) fa meglio o peggio del layer
  Magic Eden già chiuso, sugli stessi 3 problemi strutturali di `report-studio.md` (latenza,
  costo/rate-limit, rug/abbandono)? Non basta "sembra promettente" — serve lo stesso IC95% e lo
  stesso confronto onesto già fatto in CP-20260730-007

### SESSIONE 11 — Report consolidato + checklist gate L5
- Un solo documento che mette insieme memecoin (G-A/G-B/G-C) + NFT Magic Eden (chiuso ieri) +
  NFT/Mintify (se costruito qui): quale, se uno, si avvicina a un'expectancy realmente positiva
- Checklist esplicita di cosa manca per il gate L5 (100%, safety critical): RPC provider a
  pagamento, hot wallet dedicato, 30 giorni di paper trading con expectancy positiva misurata
  (non stimata) — vedi `LEGGIMI.md` §"Come passare alla modalità Soldi Veri"

### SESSIONE 12 — SOLO su ordine esplicito e scritto di Max, dopo la Sessione 11
- Nessuna sessione precedente autorizza capitale vero. Questo è un cancello a parte, non un
  passo automatico della sequenza.
- Se e quando Max dà l'ordine: hot wallet usa-e-getta (mai il vault), `TRADE_MODE=LIVE`,
  capitale iniziale minimo esplicitamente fissato da Max (non deciso da Gael), kill-switch
  verificato attivo prima del primo trade vero.

---

## 4. Cosa NON cambia rispetto al task precedente (regole già valide, ripetute perché contano)

1. File frozen invariati: `event_bus.py`, `memory_interface.py`, `quality_gates.py`,
   `gate_verifiers.py`, `gate_agent.py`, `meta_agent.py`, `orchestrator.py`, `ruflo_adapter.py`.
2. Motore memecoin (G-A/G-B/G-C) e layer NFT Magic Eden (appena chiuso) non si toccano — si
   affianca, non si riscrive.
3. Paper trading di default. Nessuna chiave privata vera fuori da `.env`, mai loggata.
4. Ogni sessione chiusa → checkpoint con comando + output reale incollato, mai "dovrebbe
   funzionare".
5. `python test_apex7.py` resta verde (13/13) prima e dopo ogni sessione.
6. Se qualcosa non torna (API Mintify ambigua, dato mancante, dominio irraggiungibile come
   successo a me con `mintify.xyz` stesso): **non indovinare**, scrivilo in `STATO-EMPIRE.md`
   con l'errore esatto e passa alla sessione successiva dove possibile.

## 5. Definition of Done

- [ ] Sessione 1: `MINTIFY-RECON.md` scritto, con endpoint/rate-limit/costo reali verificati
- [ ] Sessione 2: decisione A/B/C presa e motivata in `STATO-EMPIRE.md`
- [ ] Se B/C scelta: Sessioni 3-10 completate con lo stesso standard di rigore del task
      precedente (numeri reali, non descrizioni)
- [ ] Sessione 11: report consolidato + checklist gate L5 esplicita
- [ ] Sessione 12: **non iniziata** finché Max non dà ordine esplicito e scritto
- [ ] `python test_apex7.py` verde a fine di ogni sessione
- [ ] Checkpoint per ogni sessione chiusa

## 6. Ordine di marcia

1. `git pull`, verifica `python test_apex7.py` 13/13 verde
2. Leggi questo file + `TASK-GAEL-20260730-STREAM-S7-NFT-METODO.md` + `CP-20260730-007.md`
   (RETRO del lavoro appena chiuso — non ripartire senza sapere cosa è già stato scoperto)
3. Sessione 1 → checkpoint → commit
4. Sessione 2 (decisione) → checkpoint → commit
5. Se A: task sostanzialmente chiuso qui, scrivi il perché in un checkpoint e fermati
6. Se B/C: Sessioni 3→11 in ordine, un checkpoint a testa
7. Sessione 12: solo su ordine di Max, mai di iniziativa

**Se un dominio non risponde o un'API non esiste come descritta**: segnalalo con l'errore
esatto (esattamente come ho fatto io con `mintify.xyz` → HTTP 530) e prosegui, non fermarti in
attesa e non inventare un dato per continuare.
