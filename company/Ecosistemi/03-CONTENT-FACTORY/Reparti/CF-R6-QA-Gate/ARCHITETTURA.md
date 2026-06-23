---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #content-factory #qa #gate #CF-R6 #indipendenza #post-produzione
Created: 2026-06-23
Last updated: 2026-06-23
---

# ARCHITETTURA — CF-R6 QA & Gate

> **Reparto:** CF-R6 · **Area:** Post-Produzione · **Orchestra:** CF-R6-COORD riporta a L1-POST
> **INVARIANT CARDINALE:** indipendente da tutti i reparti di produzione — mai a L1-PROD

---

## 1. Posizione nella gerarchia CF-DE

```
CF-DIRECTOR (L0)
  └── L1-POST (Capo Area Post-Produzione)
        ├── CF-R6 — QA & GATE  ← questo reparto
        ├── CF-R7 — Pubblicazione & Distribuzione
        └── CF-R8 — Apprendimento & Ottimizzazione
```

CF-R6-COORD riceve i deliverable dai reparti di produzione (CF-R3, CF-R4, CF-R5) tramite
la coda `cf/qa`, ma la sua linea di riporto è esclusivamente L1-POST. Nessun capo area
di produzione (L1-PROD) ha autorità su CF-R6. L'indipendenza è strutturale, non procedurale.

---

## 2. I 3 gate sequenziali + Mandato

I gate si eseguono in sequenza fissa. Un gate ROSSO ferma il pezzo: i gate successivi
non vengono eseguiti. Nessun gate è bypassabile, nemmeno su richiesta del committente.

```
DELIVERABLE IN INGRESSO
       │
       ▼
┌──────────────────┐
│  GATE-FORMATO    │  Owner: CF-R6-FORMAT (haiku)
│  (automatizzabile│  Criteri: dimensioni, peso, codec, loudness, struttura
│   al 100%)       │  Risultato: PASS → avanza | FAIL → rework immediato
└──────────────────┘
       │ PASS
       ▼
┌──────────────────┐
│  GATE-BRAND      │  Owner: CF-R6-BRAND (sonnet)
│  (parametrico su │  Criteri: palette HEX vs brand_kit, font, logo, tone voice
│   brand_kit)     │  Campiona vs brand_kit.voice.esempi_si/esempi_no
└──────────────────┘
       │ PASS
       ▼
┌──────────────────┐
│  GATE-COPY APSOC │  Owner: CF-R6-COPY (sonnet)
│  (strutturale)   │  Criteri: hook ≤3s/prima slide/prima riga, problema+promessa
│                  │  vs icp, social proof solo reale, CTA unica e misurabile
└──────────────────┘
       │ PASS
       ▼
┌──────────────────┐
│  MANDATO         │  Owner: CF-R6-MANDATO (sonnet)
│  COMPLIANCE      │  Criteri: invariant non-parametrici Mandato Empire
│  (trasversale)   │  "prove non promesse", zero claim non verificabili, zero genericità
└──────────────────┘
       │ PASS
       ▼
   VERDETTO PASS
   → orders/<id>/05-qa/verdict.json
   → CF-R7 può procedere con pubblicazione
```

---

## 3. Indipendenza assoluta dalla produzione

L'indipendenza di CF-R6 è la regola ferrosa del reparto. Gap critico del v1: il gatekeeper
era un singolo agente (CF-R3-QA) interno al reparto di produzione — chi produceva
si auto-valutava. In v2 questo gap è eliminato strutturalmente.

**Come è garantita:**
- CF-R6-COORD riporta a L1-POST (non a L1-PROD): nessun capo area produzione nella catena
  di comando di CF-R6.
- I deliverable arrivano via coda `cf/qa`: CF-R6 li preleva autonomamente; non riceve
  istruzioni da chi ha prodotto.
- Il gate interno dei reparti di produzione (es. CF-R3-QA) è aggiuntivo, non sostitutivo:
  CF-R6 esegue i propri gate in modo completamente indipendente.
- Escalation di CF-R6 va sempre a L1-POST: mai a L1-PROD, mai al reparto produttore.

---

## 4. Namespace memoria e schema state

**Namespace:**
- `cf/qa` — coda QA attiva e storico verdetti per ordine
- `cf/failures` — ReasoningBank: pattern strutturati dei gate falliti

**Schema `orders/<id>/05-qa/verdict.json`:**
```json
{
  "order_id": "CF-2026-0061",
  "deliverable_path": "orders/CF-2026-0061/04-render/PNG/carosello-001/",
  "brand_kit": "brands/mentalita-brutale/brand-kit.json",
  "gate_formato": {
    "esito": "PASS",
    "dimensioni": "1080x1350 CONFORME",
    "peso_mb": 6.2,
    "struttura": "8 slide + cover CONFORME"
  },
  "gate_brand": {
    "esito": "PASS",
    "palette": "#1a1a1a dominante, accent #ff4444 nei titoli — CONFORME",
    "font": "Anton display, Inter body — CONFORME",
    "tone_campionato": "diretto, zero fronzoli — CONFORME"
  },
  "gate_copy": {
    "esito": "PASS",
    "hook_presente": true,
    "hook_posizione": "prima slide",
    "social_proof_verificabile": true,
    "cta_unica": true
  },
  "mandato_compliance": {
    "esito": "PASS",
    "claim_non_verificabili": 0,
    "genericita_rilevata": false
  },
  "verdetto_finale": "PASS",
  "n_rework": 0,
  "ts_verdetto": "2026-06-23T14:45:00Z",
  "owner_qa": "CF-R6-COORD"
}
```

**Regole di integrità state:** ogni `verdict.json` deve avere tutti i campi popolati; un
campo mancante equivale a gate non eseguito → il verdetto è automaticamente FAIL con motivo
"gate non completato". Nessun verdetto PASS con gate non eseguiti.

---

## 5. Ciclo rework

```
FAIL da qualsiasi gate
       │
       ▼
CF-R6-REWORK
  → motivo strutturato: {gate, criterio_fallito, correzione_richiesta}
  → rinvio al reparto produttore corretto (CF-R3 / CF-R4 / CF-R5)
  → incremento n_rework in state.json
       │
       ▼
[rework eseguito dal reparto produttore]
       │
       ▼
CF-R6 riesegue WF-QA-SINGOLO dall'inizio (non dal gate fallito)
       │
   n_rework ≥ 2 ?
       │ SÌ
       ▼
CF-R6-COORD: escalation a L1-POST
  + entry strutturata in `cf/failures` (ReasoningBank)
  + notifica CF-Director
```

---

## 6. Topologia swarm

| Pipeline | Topologia | Razionale |
|---|---|---|
| WF-QA-SINGOLO (1 pezzo) | pipeline sequenziale (FORMAT→BRAND→COPY→MANDATO) | gate dipendenti: un ROSSO ferma, i successivi non vengono eseguiti |
| WF-QA-BATCH (≥5 pezzi) | star: CF-R6-BATCH fan-out N WF-QA-SINGOLO paralleli → merge report | job indipendenti tra loro; nessuna abbreviazione per batch |
| WF-QUALITY-AUDIT (mensile) | pipeline analitica: CF-R6-LEARN → CF-R6-COORD → CF-Director + 07-FORGE | aggregazione storica, non real-time |

---

## 7. Gate FORMATO: soglie per formato

| Formato | Dimensioni | Peso max | Codec / Struttura | Loudness |
|---|---|---|---|---|
| Carosello IG | 1080×1350 px | 8 MB/slide | PNG, ≤8 slide + cover, testo leggibile, safe-area rispettata | — |
| Video Reel/TikTok/Shorts | 720×1280 (9:16) | — | h264 o h265, ≤60s IG/Shorts, ≤3min TikTok | -14 LUFS ±2 dB |
| Video YouTube | 1280×720 o 1920×1080 (16:9) | — | h264 o h265, durata dichiarata nell'ordine | -14 LUFS ±2 dB |
| Thumbnail | 1280×720 px | 2 MB | PNG o JPG, testo leggibile al 10% larghezza, safe-area | — |
| Grafica statica | dimensioni esatte canale (da ordine) | soglia piattaforma | PNG o JPG | — |
| Testo/articolo | n/a | n/a | heading strutturata, hook in apertura, CTA presente | — |

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R6`
- [[CF-R6-QA-Gate/README]] · `README.md` — roster e handoff
- [[CF-R3-Produzione-Video]] · principale fornitore deliverable video
- [[principi/PRINCIPI]] · `principi/PRINCIPI.md` — invariant operativi del reparto
