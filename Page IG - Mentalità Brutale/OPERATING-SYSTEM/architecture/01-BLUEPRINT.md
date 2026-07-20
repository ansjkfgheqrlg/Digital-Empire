# BLUEPRINT — Mentalità Brutale Social Operating System (MB-OS)

## 1. Forma scelta da ARCHITETTURA

Non nasce un nuovo ecosistema: MB-OS è un **tenant operativo** che orchestra capability già vive.

- **P&L / direzione:** 05-MULTI-BUSINESS.
- **produzione:** 03-CONTENT-FACTORY CF-R1→R5.
- **gate indipendente:** CF-R6.
- **authorization/publish:** CF-R7.
- **learning:** CF-R8 + 04-MARKETING Analytics.
- **ingestione:** 08-INTELLIGENCE / Empire Studio.
- **nuove capability:** Chief-Forge → ARCHITETTURA → FORGE.
- **memoria:** Ecosistema 10 + memoria locale MB-OS.

Questa forma evita duplicazione e rispetta ADR-003: `carousel-factory` e il publisher precedente sono asset wrappati, non riscritti.

## 2. WF-0 — workflow business prima della tecnologia

```text
OBIETTIVO BUSINESS
attenzione qualificata → follower/lead posseduto → prodotto/affiliate coerente → ricavo attribuibile
        │
        ▼
INTELLIGENCE → STRATEGIA → CALENDARIO → PRODUZIONE → QA INDIPENDENTE
        │                                             │
        └──────────── evidence + fonti ───────────────┘
                                                      ▼
AUTH/TOKEN → STAGING HTTPS → SCHEDULER → META PUBLISH → POST-CHECK
                                                      ▼
                         INSIGHTS +48h/+7g → ANALYTICS → PATTERN n≥3
                                                      ▼
                                      CF-R8 → prossimo brief migliore
```

**North star business:** lead/ricavo attribuibile al canale, non vanity metrics. Prima della monetizzazione, proxy: reach qualificata → salvataggi/condivisioni → visite profilo → click bio.

## 3. Contratto unico del contenuto

Ogni contenuto viaggia come `content-manifest.json`:

```json
{
  "content_id": "MB-20260720-001",
  "brand": "mentalita-brutale",
  "format": "REEL | IMAGE | CAROUSEL",
  "caption": "...",
  "scheduled_at": "2026-07-21T18:30:00Z",
  "media": [{"path": "...", "public_url": null, "alt_text": "..."}],
  "experiment": {"pillar": "P1", "hook": "contrasto-brutale", "slot": "20:30", "cta": "salva"},
  "quality_evidence": {
    "format": "PASS", "brand": "PASS", "copy": "PASS", "rights": "PASS", "safety": "PASS"
  },
  "rights": {"confirmed": true, "source_or_license": "owned | licensed | generated:<tool>", "music_rights": "owned | licensed | none"}
}
```

Il manifest è il confine tra reparti: nessun passaggio a voce, nessun dato nascosto in prompt.

## 4. State machine

```text
DRAFT
  → RESEARCHED
  → PRODUCED
  → QA_PASS | REWORK
  → STAGED
  → SCHEDULED
  → PUBLISHING
  → PUBLISHED
  → MEASURED_48H
  → MEASURED_7D
  → LEARNED

Da qualunque stato: → PAUSED | FAILED_RETRYABLE | FAILED_TERMINAL
```

Transizioni live sono append-only in SQLite + trace; `content_hash` impedisce doppio publish.

## 5. Topologia operativa

- **Hierarchical** per governo: Social Director → capi reparto → worker.
- **Pipeline** per il singolo contenuto: ogni stage ha I/O e gate.
- **Mesh controllata** solo per Intelligence: più fonti possono lavorare in parallelo, ma il Research Lead firma un evidence pack unico.
- **QA isolato:** chi scrive/renderizza non assegna il proprio PASS finale.

## 6. I/O dei blocchi

| Blocco | Input | Output | Gate |
|---|---|---|---|
| Intelligence | fonti integrali, frame, transcript | evidence pack con timestamp | fonte osservata |
| Strategy | baseline + evidence | brief con ipotesi e variabile test | una variabile primaria |
| Production | brief + brand-kit | asset + caption + manifest | completezza |
| CF-R6 | asset/manifest | 5 verdict | tutti PASS |
| CF-R7 | manifest PASS + token | container/media id/permalink | token+quota+idempotenza |
| Analytics | media id + snapshot time | metriche normalizzate | niente dato vuoto trasformato in zero |
| CF-R8 | ≥3 casi comparabili | pattern candidato/validato | n≥3 + fonte + unicità |
| FORGE | gap KPI ripetuto | skill/workflow migliorato | eval + contradiction gate |

## 7. Guardrail di autonomia

L'architettura supporta piena automazione, ma non confonde **capacità** con **certificazione**:

1. `SHADOW`: tutta la pipeline salvo side effect.
2. `SUPERVISED`: 1 publish reale con conferma.
3. `CERTIFIED_AUTO`: scheduler autonomo con gate, cap e kill switch.
4. `PAUSED`: nessun side effect.

Target dichiarato: `CERTIFIED_AUTO`. Stato iniziale onesto: `SHADOW` finché token e test live non esistono.

## 8. DONE tecnico

- `runtime/scripts/mbctl.py doctor` verde statico.
- `validate` e `plan` ripetibili.
- `run` dry per default.
- `run --live` bloccato fuori certificazione.
- `run-due --live` idempotente.
- metriche a +48h/+168h senza inventare zeri.
- secret scan e unit test verdi.
