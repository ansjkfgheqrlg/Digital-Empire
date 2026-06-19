---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #content-factory #video #CF-R3 #pipeline #engine
Created: 2026-06-19
Last updated: 2026-06-19
---

# ARCHITETTURA — CF-R3 Produzione Video

> **Reparto:** CF-R3 · **Area:** Produzione · **Orchestra:** CF-R3-COORD riporta a L1-PROD
> **Asset wrappati (ADR-003):** `hf-studio` (Higgsfield) + `heygen-studio` (HeyGen) — originali intatti

---

## 1. Posizione nella gerarchia CF-DE

```
CF-DIRECTOR (L0)
  └── L1-PROD (Capo Area Produzione)
        ├── CF-R3 — PRODUZIONE VIDEO  ← questo reparto
        ├── CF-R4 — Produzione Testuale
        └── CF-R5 — Visual & Design
```

CF-R3-COORD riceve dal CF-D-DISPATCH (via L1-PROD) gli ordini con `formato: video-ugc |
video-avatar | shortform | batch-video`. Ogni output finale transita obbligatoriamente
per CF-R6 (QA & Gate, indipendente) prima di raggiungere CF-R7 (Pubblicazione).

---

## 2. Engine disponibili e regola di scelta (ADR-003)

CF-R3-COORD sceglie l'engine via capability — mai hard-coded al brand:

| Capability | Engine | Stato | Port da |
|---|---|---|---|
| `image-4k`, `soul-id`, `motion`, `video-ugc` | Higgsfield | DA COLLEGARE | `hf-studio` CF Exponium [WRAPPA] |
| `avatar`, `talking-head`, `spokesperson` | HeyGen | DA COLLEGARE | `heygen-studio` CF Exponium [WRAPPA] |
| `montaggio`, `cut`, `crop`, `subtitle-burn`, `loudness` | ffmpeg | ATTIVO (locale) | nativo |
| `tts`, `voiceover` | edge-tts / ElevenLabs | PARZIALE | nativo + chiave API |

**Regola di wrap (ADR-003):** ogni chiamata a Higgsfield o HeyGen passa per il wrapper
parametrizzato che sostituisce i parametri Exponium hard-coded con `brand_kit.slug`,
`brand_kit.visual.palette`, `brand_kit.voice`. L'originale `hf-studio/` e `heygen-studio/`
non vengono mai modificati.

**Contratto engine (non negoziabile):**
```
generate(job)   → avvia render; produce asset in outputs/<job_id>/
check()         → verifica connessione engine (OK / ERRORE)
status(job_id)  → stato render (pending / running / done / failed)
estimate(job)   → stima crediti PRIMA di generate(); mai skippare
```

---

## 3. Topologia swarm

| Pipeline | Topologia | Razionale |
|---|---|---|
| WF-VIDEO-UGC (job singolo) | pipeline sequenziale (SOUL→IMG→MOTION→QUEUE→VO→EDIT→QA) | dipendenze hard: ogni fase usa output della precedente |
| WF-VIDEO-AVATAR (job singolo) | pipeline sequenziale (AVATAR→QUEUE→EDIT→QA) | sequenza obbligatoria script→render→montaggio |
| WF-SHORTFORM | pipeline leggera (EDIT→QA), ffmpeg locale | nessun engine esterno; costo zero |
| WF-BATCH-VIDEO (batch ≥5) | star + mesh: COORD fan-out N job → N worker paralleli (IMG+MOTION per job) → QA su ogni output | parallelismo per job; cap dalla `budget.tier_max` dell'ordine |

---

## 4. Ciclo di vita di un ordine video (state machine)

```
[ordine_ricevuto]
      │
      ▼
[01-brief]       ← CF-R1 produce brief.json (incluso script se video-avatar)
      │
      ▼
[02-dry-run]     ← CF-R3-QUEUE: estimate() su tutti gli engine → ugc-intent.json / avatar-intent.json
      │            ← CF-SENT-COST: approva o BLOCCA (exit-2)
      │
      ▼
[03-asset]       ← render engine (Higgsfield UGC o HeyGen Avatar)
      │
      ▼
[04-post]        ← CF-R3-VO (voiceover) + CF-R3-EDIT (montaggio ffmpeg)
      │
      ▼
[05-qa]          ← CF-R3-QA GATE-FORMATO + GATE-BRAND (pre-gate interno)
      │
      ▼
[06-qa-r6]       ← CF-R6 gate indipendente (3 gate: FORMATO+BRAND+COPY+MANDATO)
      │
      ▼ (PASS)
[orders/<id>/04-render/video/]  → CF-R7 per pubblicazione
```

Ogni transizione aggiorna `orders/<id>/state.json` e appende una riga a `trace.jsonl`
con `{ts, agent, event, engine_id, crediti_stimati, crediti_consumati}`.

---

## 5. Dry-run obbligatorio (Art.4.3)

Prima di ogni render reale ogni workflow produce un `*-intent.json` a costo zero.
Il dry-run è il punto di controllo ufficiale: CF-SENT-COST legge l'intent e approva o blocca.

```json
// Esempio ugc-intent.json (WF-VIDEO-UGC dry-run)
{
  "order_id": "CF-2026-0055",
  "brand": "mentalita-brutale",
  "soul_id": "soul-mb-001",
  "engine_calls": [
    { "engine": "higgsfield", "type": "image-4k", "n_scene": 4, "crediti_stimati": 40 },
    { "engine": "higgsfield", "type": "motion",   "n_clip": 4, "crediti_stimati": 80 },
    { "engine": "tts",        "type": "voiceover", "durata_s": 45, "crediti_stimati": 0 },
    { "engine": "ffmpeg",     "type": "montaggio", "crediti_stimati": 0 }
  ],
  "totale_crediti_stimati": 120,
  "budget_disponibile": 150,
  "decisione": "PENDING_APPROVAZIONE_CF-SENT-COST"
}
```

---

## 6. Budget guard e namespace memoria

**CF-R3-QUEUE** blocca ogni render prima che inizi se `totale_crediti_stimati > budget.crediti_engine`.
Non suggerisce: BLOCCA con motivo strutturato e escalation a CF-R3-COORD.

**Namespace AgentDB:**
- `cf/video` — stato render per ordine: `{order_id, engine, job_id, status, crediti}`
- `cf/souls` — soul-id per brand: `{brand_slug, soul_id, ultimo_render, n_video}`
- `cf/render-queue` — coda render attiva: `{order_id, job_id, priority, stima, approvato}`

**Schema trace.jsonl (ogni riga):**
```json
{"ts":"2026-06-19T14:30:00Z","agent":"cf-r3-img","event":"render_started","engine_id":"higgsfield","job_id":"hf-job-001","crediti_stimati":40,"crediti_consumati":null}
{"ts":"2026-06-19T14:32:15Z","agent":"cf-r3-img","event":"render_done","engine_id":"higgsfield","job_id":"hf-job-001","crediti_stimati":40,"crediti_consumati":38}
```

---

## 7. Gate pre-consegna a CF-R6

CF-R3-QA esegue un gate interno prima di passare il video a CF-R6 (che è il gate ufficiale
indipendente). Il gate interno non sostituisce CF-R6: serve a evitare che video palesemente
fuori specifica arrivino al gate indipendente sprecando tempo.

| Gate | Owner | Criteri |
|---|---|---|
| GATE-FORMATO interno | CF-R3-QA | aspect ratio corretto (9:16/1:1/16:9), codec h264/h265, loudness -14 LUFS ±2, durata nei limiti piattaforma |
| GATE-BRAND interno | CF-R3-QA | soul_id corrispondente al brand_kit.soul_id, palette primaria riconoscibile nei frame campionati |

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · §CF-R3 + §5(b) pipeline video + §6 engine layer
- [[CF-R3-Produzione-Video/README]] · `README.md` — roster e handoff
- [[CF-R6-QA-Gate]] · gate indipendente obbligatorio su ogni output video
- [[principi/PRINCIPI]] · `principi/PRINCIPI.md` — regole non negoziabili del reparto
