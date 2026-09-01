# SELF-EVOLUTION ENGINE

> APEX-7 migliora sé stesso ad ogni sessione. L'evoluzione è controllata, sicura e tracciata.

---

## Ciclo di Evoluzione

```
① OBSERVE (continuo)
   META AGENT raccoglie metriche da tutti gli agenti
   e da tutti gli eventi del bus.

   METRICHE RACCOLTE:
   → Quality scores per agente (media, min, max)
   → Gate pass rate per livello
   → Cicli medi per raggiungere PASS
   → Tempo medio per stage
   → Pattern di fallimento frequenti
   → Correlazioni tra agenti e risultati

② DETECT PATTERNS (ogni 10 osservazioni)
   META AGENT analizza le metriche:
   → Cosa fallisce sempre?
   → Cosa funziona sempre?
   → Cosa migliora nel tempo?
   → Cosa peggiora nel tempo?

③ HYPOTHESIZE (per ogni pattern)
   Per ogni pattern negativo:
   → Formula ipotesi causale
   → Confidence dell'ipotesi (0.0-1.0)
   → Progetta esperimento minimo
   → Valuta rischio (LOW/MEDIUM/HIGH)

④ EXPERIMENT (con controllo)
   → Modifica UNA sola variabile
   → Mantieni versione precedente
   → Esegui su 3 task campione
   → Misura delta vs baseline
   → Documenta tutto

⑤ EVALUATE
   SE delta quality > +5%: ADOPT
   SE delta quality -5% a +5%: DISCARD + log
   SE delta quality < -5%: ROLLBACK + alert

⑥ EVOLVE (se ADOPT)
   → Aggiorna la variabile nel sistema
   → Crea Architecture Snapshot
   → Salva in Strategy Store (se nuova strategia)
   → Emetti: system.evolved
   → Notifica ORCHESTRATOR
```

---

## Cosa Può Evolvere Autonomamente

| ✅ Variabile | Range Modifica | Note |
|---|---|---|
| Parametri prompt (temperatura, max tokens) | ±20% | Per agente |
| Gate threshold | ±10% | Da baseline |
| Priority scores eventi | ±1 livello | P2↔P3, mai P0/P1 |
| Strategy ranking | Ricalcolo automatico | Basato su success_rate |
| Timeout agenti | ±20% | Da default |
| Max iterations critique loop | 3-7 | Range ristretto |

---

## Cosa Richiede Approvazione Utente

| ⚠️ Modifica | Impatto |
|---|---|
| Aggiungere/rimuovere stage dal workflow | > 50% sistema |
| Modificare schema Memory | Strutturale |
| Cambiare agenti core (PLANNER, CRITIC, GATE) | Critico |
| Qualsiasi modifica che impatta > 50% del sistema | Soglia |
| Modificare i 7 principi fondamentali | Fondazionale |

---

## Rollback Automatico

Il sistema esegue rollback automatico se:

| 🔴 Condizione | Trigger | Azione |
|---|---|---|
| Quality score medio scende > 10% | Su 5 run consecutive | Rollback ultima evoluzione |
| Gate failure rate aumenta > 20% | Su 10 gate checks | Rollback threshold change |
| Un agente entra in stato DEGRADED | Immediato | Rollback + alert |
| Memory consistency check fallisce | Immediato | Restore da snapshot |
| Evento P0 non risolto in 60s | Timeout | Rollback + escalation human |

---

## Tracciamento Evoluzione

```
Ogni evoluzione è tracciata in:
1. Architecture Snapshot (Layer 4) — stato completo pre/post
2. Decision Log (Layer 2) — decisione con motivazione e alternative
3. Strategy Store (Layer 3) — se nuova strategia
4. Event Bus — evento system.evolved

Diff tra versioni sempre disponibile.
```

---

## Metriche di Performance

```
Baseline iniziale (first run):
  - avg_quality_score: 7.5
  - avg_cycles_to_pass: 2.3
  - gate_pass_rate: 0.78
  - avg_session_time_min: 25

Target dopo 10 evoluzioni:
  - avg_quality_score: 8.5+
  - avg_cycles_to_pass: 1.5-
  - gate_pass_rate: 0.90+
  - avg_session_time_min: 15-

APEX target (Level 7):
  - Performance ≥ 150% vs baseline su tutte le metriche
```
