---
Tipo: Piano Strategico (non operativo — nessun codice, nessuna esecuzione)
Owner: Max · Studia/analizza/migliora: NERI · Base tecnica: Gael + Claude
Data: 2026-08-03
---

# Piano Strategico — Stream S7 (trading NFT/token)

> Questo documento NON è il task operativo (quello esiste già, è di Gael:
> `company/Memory/tasks/TASK-GAEL-20260731-STREAM-S7-NFT-SESSIONI.md`, fermo a "da avviare" da
> 3 giorni). Questo è un livello sopra: **la domanda che nessuno ha ancora risposto è se
> continuare a costruire, non come costruire.** È il documento che Neri deve studiare,
> criticare, migliorare — non eseguire.

## 1. Riepilogo onesto — dove siamo davvero (fatti verificati, non impressioni)

| Data | Evento | Fonte |
|---|---|---|
| 2026-07-23 | S7 approvato come R&D speculativo, 0€ nel piano revenue estate, esecuzione isolata da S1/S2 | DEC-EST-007 |
| ~2026-07-28 | Motore memecoin (Pump.fun/Raydium) chiuso: parser dati reale, position manager, fix spam. `report-studio.md`: **expectancy negativa, >85% rischio perdita capitale nel primo mese** | CP-20260728-006, report-studio.md |
| 2026-07-30 | Metodo NFT su Magic Eden costruito e verificato: 89/89 controlli reali, dati reali (non simulati) | CP-20260730-002→007 |
| 2026-07-30 | **Verdetto: INVARIATO, bocciato per live.** Solo 1 problema strutturale su 3 migliora, e solo parzialmente. Edge non distinguibile da zero al 95% di confidenza | CP-20260730-007 |
| 2026-07-31 | Max corregge il riferimento a mintify.xyz, chiede il flusso di tutte le sessioni verso l'operativo. Scritto: 12 sessioni, gate architetturale A/B/C | CP-20260731-004, TASK-GAEL-...-SESSIONI.md |
| 2026-07-31 → 2026-08-03 | **Zero sessioni del task Mintify aperte.** Resta "da avviare" | `TASK-GAEL-...-SESSIONI.md` |
| 2026-08-03 (stesso giorno di questo piano) | Gael ha chiesto ricognizione dopo fine crediti: `requirements.txt` non installabile corretto (conflitto `solana==0.33.0` vs `websockets==12.0`, provato con dry-run, non dedotto), `STATO-RIPRESA.md` riallineato. **Conclusione indipendente, stessa diagnosi di questo piano**: *"non manca codice, manca una decisione"* | CP-20260803-001 |

**Il fatto che conta di più, non nascosto**: un task P1 esplicito è rimasto fermo 3 giorni. Non
per un blocco tecnico — per priorità reale. Questo è già un segnale, non solo un ritardo. **Non
è un'osservazione isolata di questo piano**: `STATO-RIPRESA.md` (riscritto lo stesso giorno, da
un'altra sessione, su richiesta di Gael) è arrivato in modo indipendente alla stessa identica
conclusione — due letture separate degli stessi fatti che convergono è un segnale più forte di
una sola.

`STATO-RIPRESA.md` elenca già, con numeri reali (non stimati), i 4 prerequisiti aperti se si
andasse verso LIVE — Neri parte da questi, non li riscopre da zero:
1. RPC Solana a pagamento (`BACKLOG.md` B-010) — l'endpoint pubblico risponde 429 dopo 2
   chiamate `getTransaction`
2. Latenza misurata 2456-3624ms contro il benchmark MEV 300-800ms — non si compra, serve Jito
   bundles/bare-metal/riscrittura Rust
3. Nessun feed prezzo live — `position_monitor.py` esce su valore stimato, TP/SL non sono veri
4. Modalità LIVE non scritta — `execution_engine.py` rifiuta esplicitamente il ramo `!=
   SIMULATION`

## 2. La domanda strategica vera

Non è "Magic Eden o Mintify". È:

> **Ha senso continuare a investire ore di ingegneria (di Gael, di Claude) in un ramo che ha
> già ricevuto due verdetti negativi consecutivi (memecoin + NFT), classificato 0€ revenue,
> mentre lo stesso ecosistema (S1/S2/Preventa/YouTube) ha lavoro reale che genera cassa e
> compete per lo stesso tempo di Gael?**

Il task Gael di 12 sessioni esiste ed è pronto — ma nessuno finora ha risposto a questa domanda
prima di scriverlo. Lo si è scritto per completezza operativa, non perché qualcuno abbia deciso
che vale la pena eseguirlo ora. È il gap che Neri deve colmare.

## 3. Opzioni reali (non un'unica strada obbligata)

| Opzione | Cosa significa concretamente | Costo | Quando ha senso |
|---|---|---|---|
| **CONTINUA** | Gael esegue le 12 sessioni come scritte | Giorni di lavoro Gael sottratti a revenue | Se Neri trova un motivo concreto per cui questa volta l'esito cambierebbe |
| **PAUSA ESPLICITA** | Il task resta scritto, non si tocca, richiamato solo quando S1/S2/Preventa sono stabili | Zero, se non il tempo già investito | Se il costo-opportunità (§ REP2 sotto) conferma che oggi non conviene |
| **RIDEFINISCI IL BERSAGLIO** | Non "vendere sniping retail" ma altro uso dei dati NFT/on-chain (es. analytics come prodotto, non trading) | Ripensare l'obiettivo, non il codice | Se la ricerca (§ R1 sotto) trova che il valore reale non è nel trading |
| **KILLA** | Si archivia, si documenta il perché, si libera la capacità mentale/organizzativa | Zero futuro, si accetta la perdita del lavoro fatto | Se nessuna delle precedenti regge dopo l'analisi |

**Nessuna di queste è già decisa.** È esattamente il lavoro che serve da Neri prima che Gael
riprenda in mano il task operativo.

## 4. Cosa serve per decidere bene (→ diventa l'incarico di Neri)

Oggi la decisione "continua/pausa/redefinisci/killa" verrebbe presa **a sensazione** — esattamente
l'errore che questo stesso ecosistema si vieta di fare sul codice (mai un numero senza fonte,
mai una percentuale senza intervallo). Serve lo stesso rigore applicato alla decisione
strategica, non solo al codice. Il dettaglio è nel task assegnato a Neri
(`company/Memory/tasks/TASK-NERI-20260803-STREAM-S7-STRATEGIA.md`).
