---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #content-factory #apprendimento #ottimizzazione #CF-R8 #post-produzione #pattern #reasoningbank
Created: 2026-06-30
Last updated: 2026-06-30
---

# ARCHITETTURA — CF-R8 Apprendimento & Ottimizzazione

> **Reparto:** CF-R8 · **Area:** Post-Produzione · **Orchestra:** CF-R8-COORD riporta a L1-POST
> **INVARIANT CARDINALE:** nessun pattern senza ≥3 casi verificati — nessuna conclusione inventata (Mandato Art.2)
> **Ruolo trasversale:** CF-R8 opera su tutti i reparti CF-DE come osservatore; non modifica nulla direttamente.

---

## 1. Posizione nella gerarchia CF-DE

```
CF-DIRECTOR (L0)
  └── L1-POST (Capo Area Post-Produzione)
        ├── CF-R6 — QA & GATE  (fonte di cf/failures)
        ├── CF-R7 — Pubblicazione & Distribuzione  (fonte di metriche performance)
        └── CF-R8 — APPRENDIMENTO & OTTIMIZZAZIONE  ← questo reparto
```

CF-R8-COORD riceve dati in ingresso da tutti i reparti tramite i namespace `cf/failures`
(alimentato da CF-R6-LEARN) e `cf/patterns` (alimentato da CF-R7-FEEDBACK), ma la sua
linea di riporto è esclusivamente L1-POST. Nessun capo area di produzione (L1-PROD)
ha autorità su CF-R8 né su i pattern che produce.

CF-R8 opera in modalità **trasversale**: legge output da tutti i reparti, distilla
conoscenza, propone miglioramenti. Non agisce direttamente: propone a CF-Director
o a 07-FORGE, che decidono e implementano.

---

## 2. Due workflow in sequenza logica

```
SORGENTI DATI
  cf/failures  ← CF-R6-LEARN (gate falliti distillati)
  cf/patterns  ← CF-R7-FEEDBACK (metriche 48h e 7gg)
  cf/briefs    ← CF-R1 (libreria formule corrente, hook_type)
       │
       ▼
┌─────────────────────────────────────────────────────┐
│  WF-PATTERN-DISTILLATION  (cadenza: sett./mensile)  │
│                                                     │
│  CF-R8-HOOK  → analisi hook/angle per brand         │
│  CF-R8-REASONING → distilla cf/failures             │
│  CF-R8-ENGINE → qualità output per engine           │
│       │                                             │
│       ▼                                             │
│  CF-R8-QA: gate ≥3 casi + fonte tracciabile         │
│       │ PASS                                        │
│       ▼                                             │
│  memory_store("cf/patterns", pattern_validato)      │
│  + aggiornamento libreria formule CF-R1             │
│  + notifica CF-Director                             │
└─────────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────┐
│  WF-IMPROVEMENT-CYCLE  (cadenza: mensile)           │
│                                                     │
│  CF-R8-COORD: aggrega top-3 problemi del mese       │
│  CF-R8-REASONING: proposta fix / ADR-bozza          │
│       │                                             │
│       ▼                                             │
│  CF-Director approva → implementazione              │
│  4 settimane osservazione                           │
│  CF-R8-QA: valida miglioramento (delta first-pass)  │
│  CF-R8-NEURAL: alimenta neural_train (se dati ok)   │
└─────────────────────────────────────────────────────┘
```

---

## 3. Aggiornamento libreria hook/formule CF-R1

CF-R8-HOOK è l'unico agente autorizzato a proporre aggiornamenti alla libreria formule
di CF-R1 (`cf/briefs` e libreria `hook_type` per brand/nicchia).

**Flusso di aggiornamento:**

1. CF-R8-HOOK identifica un pattern hook confermato (≥3 casi in metriche 7gg).
2. CF-R8-QA valida il pattern: fonte tracciabile, n ≥ 3, correlazione non inventata.
3. CF-R8-COORD propone aggiornamento a CF-R1-LEARN (agente corrispondente in CF-R1).
4. CF-R1-LEARN integra il nuovo hook_type o aggiorna il peso nella libreria formule.
5. Versioning: ogni aggiornamento libreria porta timestamp e riferimento al pattern_id
   in `cf/patterns` che lo ha generato.

**Invariant:** CF-R8 non scrive direttamente nella libreria CF-R1; propone e CF-R1
accetta o rifiuta con motivazione. La libreria rimane di proprietà di CF-R1.

---

## 4. Namespace memoria e schema state

**Namespace operativi di CF-R8:**

| Namespace | Owner scrittura | Contenuto |
|---|---|---|
| `cf/patterns` | CF-R8-QA (dopo validazione) | Pattern hook/engine/failures validati (≥3 casi, fonte tracciabile) |
| `cf/failures` | CF-R6-LEARN (sorgente); CF-R8-REASONING (legge e distilla) | ReasoningBank: gate falliti classificati per tipo/brand/formato |
| `cf/improvements` | CF-R8-COORD | Improvement cycle: proposta, stato, data implementazione, effetto misurato |

**Schema pattern validato in `cf/patterns`:**
```json
{
  "pattern_id": "PAT-R8-HOOK-IG-CAROSELLO-001",
  "tipo": "hook | engine | failure-distillato",
  "contesto": {
    "brand": "mentalita-brutale",
    "formato": "carosello-ig",
    "nicchia": "mindset"
  },
  "pattern": "Hook interrogativo con dato numerico nella prima slide",
  "esempi": [
    {"order_id": "CF-2026-0041", "hook": "Perché il 90% dei tuoi post non porta follower?", "engagement": "[DM]"},
    {"order_id": "CF-2026-0055", "hook": "3 errori che uccidono il tuo reach ogni giorno", "engagement": "[DM]"},
    {"order_id": "CF-2026-0063", "hook": "Quanto vale davvero un follower nel 2026?", "engagement": "[DM]"}
  ],
  "n_casi": 3,
  "fonte": [
    {"namespace": "cf/patterns", "key": "CF-R7-FEEDBACK-2026-06-20", "ts": "2026-06-20T10:00:00Z"},
    {"namespace": "cf/patterns", "key": "CF-R7-FEEDBACK-2026-06-13", "ts": "2026-06-13T10:00:00Z"},
    {"namespace": "cf/patterns", "key": "CF-R7-FEEDBACK-2026-06-06", "ts": "2026-06-06T10:00:00Z"}
  ],
  "validato_da": "CF-R8-QA",
  "ts_validazione": "2026-06-30T09:00:00Z",
  "azione_proposta": "Aggiornare libreria CF-R1: hook_type 'interrogativo-numerico' con peso aumentato per formato carosello-ig + nicchia mindset",
  "stato": "VALIDATO | IN_IMPROVEMENT | IMPLEMENTATO"
}
```

---

## 5. Flusso proposta ADR e richiesta 07-FORGE

CF-R8 è l'unico reparto CF-DE autorizzato a proporre ADR-bozza al Board e richieste
formali a 07-FORGE. Questo avviene solo per pattern strutturali (non per fix puntuali).

**Quando si propone ADR:**
- Pattern che rivela un difetto architetturale ricorrente (≥3 casi confermati in ≥2 reparti).
- Proposta che cambierebbe il contratto di ordine, la gerarchia, o un invariant esistente.
- Improvement che richiede modifica a un ADR attivo.

**Quando si richiede a 07-FORGE:**
- Pattern richiede una skill nuova o la modifica di un agente esistente.
- Fix proposto non è implementabile con le risorse correnti dei reparti.
- Ottimizzazione engine richiede un nuovo wrapper o un nuovo formato.

**Flusso:**
```
CF-R8-REASONING: bozza proposta (ADR o richiesta FORGE)
  → CF-R8-COORD: review e approvazione del reparto
  → CF-Director: approvazione prima dell'invio
  → Board (se ADR) / 07-FORGE (se skill/agente)
  → tracking in cf/improvements con stato "in_attesa_approvazione"
```

---

## 6. Topologia swarm

| Pipeline | Topologia | Razionale |
|---|---|---|
| WF-PATTERN-DISTILLATION (settimanale hook) | star: CF-R8-HOOK + CF-R8-REASONING + CF-R8-ENGINE in parallelo → CF-R8-QA merge | 3 tipi di analisi indipendenti convergono in un unico gate QA |
| WF-PATTERN-DISTILLATION (mensile failures) | pipeline: CF-R8-REASONING → CF-R8-QA → memory_store | analisi sequenziale approfondita dei failures distillati |
| WF-IMPROVEMENT-CYCLE | pipeline: CF-R8-COORD → CF-R8-REASONING → CF-Director → osservazione → CF-R8-QA | ciclo con gate esplicito di approvazione umana prima dell'implementazione |
| Neural feeding (asincrono) | CF-R8-NEURAL standalone post-validazione | job asincrono attivato da CF-R8-COORD solo quando cf/patterns ha dati sufficienti |

---

## 7. Gate DISTILLATION: criteri di validazione pattern

Questi gate si applicano in WF-PATTERN-DISTILLATION prima di ogni `memory_store("cf/patterns")`.
Sono eseguiti da CF-R8-QA. Nessun gate è bypassabile.

| Gate | Criterio | FAIL se |
|---|---|---|
| Gate-N3 | n_casi ≥ 3 | n_casi < 3, anche in emergenza |
| Gate-FONTE | Ogni caso ha `{namespace, key, ts}` tracciabile | anche un solo caso senza fonte tracciabile |
| Gate-CORRELAZIONE | Il pattern descrive un'osservazione, non una causalità non dimostrata | il pattern afferma "X causa Y" senza studio controllato |
| Gate-UNICITA | Il pattern non duplica un pattern già in `cf/patterns` | stessa osservazione già presente (merge, non duplicato) |

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R8`
- [[CF-R8-Apprendimento/README]] · `README.md` — roster e handoff completi
- [[CF-R6-QA-Gate/state/README]] · `../CF-R6-QA-Gate/state/README.md` — schema cf/failures (sorgente primaria)
