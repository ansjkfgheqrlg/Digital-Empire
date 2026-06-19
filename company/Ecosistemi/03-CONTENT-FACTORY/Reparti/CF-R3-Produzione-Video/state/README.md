---
Type: STATE
Status: Active
Tags: #state #CF-R3 #video #namespace #trace #dry-run #amnesia-test
Created: 2026-06-19
Last updated: 2026-06-19
---

# State — CF-R3 Produzione Video

> Ogni ordine video è ripartibile a freddo dal `state.json` + `trace.jsonl`.
> Regola amnesia test: se un agente muore durante il render, il successivo riparte
> dalla fase indicata in state.json senza perdere il lavoro precedente.

---

## Namespace AgentDB

| Namespace | Contenuto | Owner | Operazioni |
|---|---|---|---|
| `cf/video` | Stato render per ordine: `{order_id, engine, job_id, status, crediti_stimati, crediti_consumati}` | CF-R3-COORD | store dopo ogni fase; retrieve per ripresa a freddo |
| `cf/souls` | Soul-id Higgsfield per brand: `{brand_slug, soul_id, creato_il, n_video, ultimo_render}` | CF-R3-SOUL | store a creazione; update dopo ogni render |
| `cf/render-queue` | Coda render: `{order_id, job_id, tipo, priority, stima, stato, approvazione}` | CF-R3-QUEUE | store a dry-run; update a approvazione e completamento |

---

## Schema state.json (per ordine)

Ogni ordine video ha il suo `orders/<order_id>/state.json`. Struttura standard:

```json
{
  "order_id": "CF-2026-0055",
  "workflow": "WF-VIDEO-UGC | WF-VIDEO-AVATAR | WF-SHORTFORM | WF-BATCH-VIDEO",
  "brand": "mentalita-brutale",
  "tipo_video": "video-ugc",
  "avviato_il": "2026-06-19T10:00:00Z",
  "fasi": {
    "00-dry-run": {
      "stato": "completato | in_corso | non_avviato | bloccato",
      "ts": "2026-06-19T10:00:00Z",
      "risultato": "APPROVATO | BLOCCO",
      "intent_path": "cf/render-queue/CF-2026-0055/ugc-intent.json"
    },
    "01-soul": {
      "stato": "completato",
      "soul_id": "mb-001",
      "azione": "lookup | creato"
    },
    "02-img-4k": {
      "stato": "completato",
      "n_immagini": 4,
      "higgsfield_job_id": "hf-img-job-001",
      "crediti_consumati": 38
    },
    "03-motion": {
      "stato": "completato",
      "n_clip": 4,
      "higgsfield_job_id": "hf-motion-job-001",
      "crediti_consumati": 76
    },
    "04-voiceover": {
      "stato": "completato",
      "engine": "edge-tts",
      "voice_id": "it-IT-DiegoNeural",
      "durata_s": 44.8,
      "crediti_consumati": 0
    },
    "05-montaggio": {
      "stato": "completato",
      "video_path": "orders/CF-2026-0055/04-render/video/video-001.mp4",
      "durata_s": 47.3,
      "aspect_ratio": "9:16",
      "loudness_lufs": -14.1,
      "crediti_consumati": 0
    },
    "06-gate-interno": {
      "stato": "completato",
      "gate_formato": "PASS",
      "gate_brand": "PASS",
      "n_rework": 0
    },
    "07-handoff-cf-r6": {
      "stato": "completato | in_attesa",
      "ts": null,
      "pronto_per_cf_r6": true
    }
  },
  "crediti_totali_stimati": 120,
  "crediti_totali_consumati": 114,
  "stato_finale": "completato | in_rework | bloccato_budget | fallito"
}
```

---

## Schema trace.jsonl (append-only, ogni riga un evento)

Il file `orders/<order_id>/trace.jsonl` è append-only. Ogni engine call (e ogni evento
significativo) appende una riga:

```json
{"ts":"2026-06-19T10:00:00Z","agent":"cf-r3-queue","event":"dry_run_intent_prodotto","engine_id":null,"job_id":null,"crediti_stimati":120,"crediti_consumati":null,"nota":"ugc-intent.json depositato in cf/render-queue"}
{"ts":"2026-06-19T10:01:00Z","agent":"cf-r3-soul","event":"soul_lookup","engine_id":"higgsfield","job_id":null,"crediti_stimati":0,"crediti_consumati":0,"nota":"soul_id mb-001 trovato in cf/souls"}
{"ts":"2026-06-19T10:02:00Z","agent":"cf-r3-img","event":"render_started","engine_id":"higgsfield","job_id":"hf-img-job-001","crediti_stimati":40,"crediti_consumati":null,"nota":"4 immagini 4K scene avviate"}
{"ts":"2026-06-19T10:04:30Z","agent":"cf-r3-img","event":"render_done","engine_id":"higgsfield","job_id":"hf-img-job-001","crediti_stimati":40,"crediti_consumati":38,"nota":"4 immagini depositate in 03-design/scenes/"}
{"ts":"2026-06-19T10:10:00Z","agent":"cf-r3-edit","event":"montaggio_completato","engine_id":"ffmpeg","job_id":null,"crediti_stimati":0,"crediti_consumati":0,"nota":"video-001.mp4 47.3s -14.1LUFS 9:16"}
{"ts":"2026-06-19T10:11:00Z","agent":"cf-r3-qa","event":"gate_interno_pass","engine_id":null,"job_id":null,"crediti_stimati":0,"crediti_consumati":0,"nota":"GATE-FORMATO PASS GATE-BRAND PASS"}
```

---

## Regola dry-run obbligatorio

Ogni workflow che genera spesa engine deve avere almeno una riga in trace.jsonl
con `event: "dry_run_intent_prodotto"` PRIMA di qualsiasi riga con `event: "render_started"`.
Mancanza della riga dry-run in trace.jsonl = violazione Art.4.3 → escalation CF-R3-COORD.

---

## Ripresa a freddo (amnesia test)

Se un agente muore dopo il render ma prima di aggiornare state.json:
1. CF-R3-COORD rileva che la fase successiva non è avviata.
2. Controlla trace.jsonl: c'è un `render_done` per questo job?
3. Sì → il file esiste in `03-design/`; riprende dalla fase successiva.
4. No → il job potrebbe essere in pending su Higgsfield; chiama `status(job_id)` e aspetta.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — dettaglio schema trace e regola dry-run
- [[cf-r3-queue]] · `agenti/cf-r3-queue.md` — produce l'intent.json e aggiorna cf/render-queue
- [[cf-r3-coord]] · `agenti/cf-r3-coord.md` — aggiorna state.json a ogni fase
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · §9 namespace e hook operativi
