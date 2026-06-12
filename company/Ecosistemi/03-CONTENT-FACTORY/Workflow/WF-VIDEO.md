> Fonte: PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md sez. 4b (WF-VIDEO)

# WF-VIDEO — Workflow Video Multi-Engine

> Livello: L3 · Reparto: CF-R2 PRODUZIONE VIDEO · Coordinatore: `CF-R2-A01-video-lead`
> Fonte: dossier 03 §4b, §5.
> Ecosistema: `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md`

---

## Identità

| Campo | Valore |
|---|---|
| ID workflow | WF-VIDEO |
| Ecosistema | 03-CONTENT-FACTORY |
| Reparto L2 | CF-R2 PRODUZIONE VIDEO |
| Sub-workflow | WF-VIDEO-UGC · WF-VIDEO-AVATAR · WF-SHORTFORM |
| Stato | SCAFFOLD (engine da collegare: Higgsfield, HeyGen) |
| Dipende da | WF-BRIEF (brief.json), WF-SCRIPT (script.md) |

---

## Cosa produce

Video pronti alla pubblicazione in 3 pipeline:
- **WF-VIDEO-UGC** — video UGC via Higgsfield: soul-id ricorrente per brand → immagini 4K → motion → montaggio.
- **WF-VIDEO-AVATAR** — talking-head/spokesperson via HeyGen: script → avatar parametrizzato per brand → render.
- **WF-SHORTFORM** — reel/TikTok/Shorts da asset esistenti: cut, sottotitoli, audio via ffmpeg.

---

## Handoff contract (ingresso)

```json
{
  "from": "CF-R1/WF-BRIEF + CF-R3/WF-SCRIPT",
  "to": "CF-R2/WF-VIDEO",
  "order_id": "CF-2026-XXXX",
  "payload": {
    "brief_path": "orders/<id>/01-brief/brief.json",
    "script_path": "orders/<id>/02-copy/script.md",
    "brand_kit": "brands/<slug>/brand-kit.json",
    "engine_preference": "ugc | avatar | shortform | auto",
    "formato_output": "9:16 | 1:1 | 16:9",
    "durata_target_sec": 60,
    "budget_crediti_engine": 120
  },
  "acceptance_criteria": [
    "brief.json presente e approvato",
    "script.md presente con hook nei primi 3s e CTA",
    "budget crediti approvato da CF-SENT-cost"
  ]
}
```

---

## Pipeline end-to-end

```
ordine → brief.json + script.md
  → CF-R2-A01 risolve capability → engine dal registry §5:
      ugc/motion/image-4k/soul-id → higgsfield
      avatar/talking-head         → heygen
      voiceover                   → tts
      montaggio/cut/crop/subtitle → ffmpeg

  PIPELINE UGC (Higgsfield):
    soul-id(brand) → CF-R2-A02 → image-4k → CF-R2-A03 → motion → CF-R2-A04
    → CF-R2-A07 voiceover TTS → CF-R2-A06 ffmpeg (concat+subtitle+loudness)

  PIPELINE AVATAR (HeyGen):
    script → CF-R2-A05 (avatar brand parametrizzato) → render HeyGen
    → CF-R2-A06 ffmpeg (intro/outro brand, subtitle burn-in)

  PIPELINE SHORTFORM:
    asset esistenti → CF-R2-A06 cut/crop 9:16 → subtitle → loudness -14 LUFS

  CONTROLLO BUDGET (ogni pipeline):
    T-render-queue.estimate() Σ engine → vs budget.crediti_engine
    CF-SENT-cost: approva (continua) | blocca exit-2 (torna al committente con stima)

  → GATE-FORMATO (aspect, durata, codec h264, loudness -14 LUFS, subtitle sync)
  → GATE-BRAND (soul/avatar coerente col brand, palette intro/outro)
  → GATE-COPY (hook nei primi 3s, CTA presente, script rispetta icp)
  → 06-delivery/ → CF-R5/WF-PUBLISH
```

---

## Dry-run (obbligatorio alla prima esecuzione)

Ogni chiamata engine produce `*.intent.json` (prompt, parametri, costo stimato) senza
consumare crediti. Output dry-run: `orders/<id>/04-render/*.intent.json` per ogni step.
Nessun video reale senza ok esplicito sui crediti (vincolo globale Piano Maestro §4, pattern #3).

---

## Failure handling

| Evento | Azione |
|---|---|
| engine `check()` fallisce | → fallback dal registry (se esiste) oppure errore esplicito al lead — MAI sostituzione silenziosa |
| stima crediti > budget | → blocco exit-2, ordine torna al committente via CF-A00 con stima reale |
| render fallito 2 volte | → escalation CF-R2-A01 + entry `cf/failures` (ReasoningBank) |
| codec/aspect non conforme | → CF-R2-A06 riconverte automaticamente se ffmpeg disponibile |

---

## Connessioni

- `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md` — organigramma completo
- `company/Ecosistemi/03-CONTENT-FACTORY/BACKBONE.md` — namespace memoria, topologia
- `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/Produzione-Video/README.md` — reparto CF-R2
- `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` §4b, §5

*Fonte: dossier 03 §4b, §5 · Aggiornato: 2026-06-11*
