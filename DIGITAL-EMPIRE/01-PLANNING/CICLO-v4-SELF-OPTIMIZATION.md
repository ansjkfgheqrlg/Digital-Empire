# ⚡ CICLO v4 — SELF-OPTIMIZATION (dimagrire per andare più forte)
> Ciclo 3 di 3 · Metodo: strumentare la performance agente-per-agente e ottimizzare la topologia v3. Vincolo finale: **la v4 deve pesare MENO della v1** (ruoli, messaggi, passaggi). Performance > accumulo.

## 1. SISTEMA KPI PER-AGENTE (3 soli numeri, derivati da board+memoria, nessun tooling nuovo)

| KPI | Formula (dati già nei messaggi board) | Soglia rossa | Azione automatica |
|---|---|---|---|
| **TTD** (time-to-done) | mediana(`closed_at − acked_at` dei suoi task) | >2× mediana di team | task decomposition o rimpasto ruolo |
| **FPR** (first-pass-rate) | % HANDOFF che il verificatore approva al 1° colpo | <50% su 5 task | **pairing repair**: il backup diventa co-pilota + mutation proposal auto-generata dal suo failure-modes.md |
| **ESC** (escalation load) | escalation generate/consumate per settimana | >3 generate/settimana | dirigente rivede il suo mandato al COUNCIL |

Misurazione: il router calcola i 3 KPI dal metadata dei messaggi (già presente: timestamps, status). Output: `metric` in memoria per agente, letti al COUNCIL. Zero dashboard extra.

## 2. AZIONI DI OTTIMIZZAZIONE (ognuna: guarisce E dimagrisce)

| # | Azione | Effetto performance | Peso |
|---|--------|--------------------|------|
| O1 | **Fusione indexer + checkpoint-manager → `memory-keeper`** (si sovrappongono: entrambi tengono l'indice della memoria) | 1 owner chiaro della L0, niente doppia scrittura INDEX | −1 ruolo |
| O2 | **Digest aggregation nel router:** i 7 REPORT EOD dei dirigenti → 1 EMPIRE-DIGEST per i comandanti | i comandanti leggono 1 msg invece di 7 | −6 msg/giorno |
| O3 | **Naming convention applicata** (v2-R7): operativi rinominati per ruolo (`casestudy-ops`, `site-ops`, `preventa-factory-ops`) | mapping skill↔agente univoco, backup giusti | pulizia |
| O4 | **Promotion ladder codificata**: operativo→backup-dirigente→dirigente→comandante. Criteri: ≥10 task chiusi, FPR≥90%, 0 violazioni regole. Demotion simmetrica (2 settimane rosse → ritorno a operativo con pairing) | incentivo interno; il sistema cresce per promozione, non per assunzione | struttura |
| O5 | **Anti-accumulo**: ruolo senza traffico (0 msg instradati) per 2 settimane → assorbito dal ruolo più vicino. Verificato al self-audit settimanale | la mappa resta viva, mai un museo | continuo |
| O6 | **Prima promozione prevista**: se Gate-FUNNEL passa al primo colpo (22/07), `funnel-engineer` diventa candidato lead per il futuro Forge Team-2 (scaling S6) | riconosce subito merito misurato | — |

## 3. BILANCIO v1 → v4 (la prova del dimagrimento)

| Misura | v1 | v4 | Δ |
|---|---|---|---|
| Ruoli verificatori | 6 | 5 | −1 |
| Ruoli memory | 3 | 2 (memory-keeper, +TRUTH-CMD) | −1 |
| Canali comunicazione | board + OBS-FEED | board (OBS=vista) | −1 |
| Passaggi per REQUEST cross-team | 2 (via dirigente) | 1 (p2p+cc) | −50% latenza |
| Msg/giorno comandanti | ~17 stimati | ~10 (digest) | −40% |
| Messaggi per Max | N diffusi | 1 digest + P0 | protetto |
| Successioni dichiarate | 0 | 1 chain comando + catene 3-deep critiche | anti-fragile |
| Appello vs blocchi | assente | OVERRIDE-REQ con timer | anti-gridlock |

**Topologia finale v4:** 4 comandanti · 7 dirigenti · 17 operativi (7 team) · 5 verificatori · 6 regolatori · 4 osservatori = **43 ruoli** (v1: 47), ognuno con backup o catena, ognuno misurato su 3 KPI.

## 4. REGOLE EREDITATE NEI CICLI (non si rinegoziano a v4)
6 regolatori v1 confermati **senza aggiunte** (secret, anti-stub, swarm-quota, scope, cadence, constitution) — v3 ha solo dato loro quorum/circuit-breaker. 4 osservatori confermati.

## 5. VALIDAZIONE (onestà Art.2)
Queste ottimizzazioni sono **strutturali-simulate**: i numeri Δ saranno confermati dal primo audit live con dati veri di board (F6 + primo COUNCIL). Ciò che non migliora davvero viene **revertito** (ogni azione O1..O6 ha rollback atomico = riga nel diff).

---
⛓️ Trace P12: `CICLO-v4#ecosystem` · input: CICLO-v3 (H1..H5) · output: topologia finale 43 ruoli · prossimo: PIANO-ECOSISTEMA-v4-MASTER (plan of record)
