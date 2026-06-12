> Fonte: PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md sez. 5 (registry engine — tts)

# T-TTS — Engine TTS (Text-to-Speech, Voiceover)

> Layer engine condiviso · Livello: L4 · Usato da: CF-R2 (CF-R2-A07-voiceover)
> Fonte: dossier 03 §5.
> Ecosistema: `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md`

---

## Identità engine

| Campo | Valore |
|---|---|
| Engine ID | tts |
| Capability servite | voiceover, audio-caption |
| Stato | PARZIALE (edge-tts gratuito attivo; ElevenLabs opzionale a pagamento) |
| Launcher | `engines/tts.sh` (da creare) — wrapper su edge-tts e/o ElevenLabs API |
| Fallback | edge-tts gratuito se ElevenLabs non abilitato |
| Tier modello owner | haiku (CF-R2-A07-voiceover) |

---

## Contratto engine (non negoziabile)

| Operazione | Implementazione | Descrizione |
|---|---|---|
| `generate(job)` | edge-tts o ElevenLabs API: testo + voice_id + lingua → .mp3 | Genera voiceover |
| `check()` | edge-tts: sempre disponibile (locale). ElevenLabs: ping API + crediti rimanenti | Health probe per engine attivo |
| `status()` | sincrono per edge-tts; polling per ElevenLabs se asincrono | |
| `estimate(job)` | edge-tts: `{crediti: 0}`. ElevenLabs: `{crediti_elevenlabs: caratteri × costo}` | ElevenLabs usa i propri crediti — richiede ok esplicito |

---

## Routing engine interno

```
engine_tts_of(job):
  se job.brief.budget.tier_max = "haiku" E job.brief.note NON contiene "voce-premium":
    → edge-tts (costo zero, qualità sufficiente)
  se job.brief.note contiene "voce-premium" E budget.crediti_elevenlabs > stima:
    → ElevenLabs (qualità alta)
  altrimenti:
    → edge-tts (default sicuro)
```

ElevenLabs viene usato SOLO se: (a) il brief lo richiede esplicitamente, e
(b) il budget lo copre (stima < budget.crediti_elevenlabs), e
(c) CF-SENT-cost approva.

---

## Edge-TTS (motore primario gratuito)

- Libreria: `edge-tts` Python (Microsoft TTS via rete, gratuito).
- Voci italiane disponibili: `it-IT-DiegoNeural` (maschile), `it-IT-ElsaNeural` (femminile),
  `it-IT-IsabellaNeural` (femminile, caldo).
- Voice per brand: la voce coerente con il tono del brand_kit viene salvata in
  `brand-kit.json.tts_voice_id` (es. `it-IT-DiegoNeural` per Mentalità Brutale).
- Parametri: `--rate +20%` (ritmo più veloce per contenuti energy), `--pitch +0Hz` (default).
- Output: `.mp3` → poi in input a T-FFMPEG per audio-mix.

---

## ElevenLabs (motore premium opzionale)

- API key nel vault (non nel repo).
- Cloni vocali: se il brand owner fornisce sample audio → clone vocale personale
  (approvazione esplicita del brand owner richiesta — voce è dato biometrico).
- Usato per: VSL ad alta conversione, video corsi premium, contenuti dove la qualità
  vocale impatta significativamente il tasso di completamento.

---

## Standard output

| Parametro | Valore standard |
|---|---|
| Formato | `.mp3`, 44.1kHz, stereo |
| Normalizzazione | poi gestita da T-FFMPEG (loudnorm -14 LUFS) |
| Naming | `orders/<id>/04-render/voiceover_<parte>.mp3` |
| Brand voice logging | voce usata loggata in `trace.jsonl` |

---

## Connessioni

- `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md` — registry engine §5
- `company/Ecosistemi/03-CONTENT-FACTORY/Funzioni/T-FFMPEG.md` — audio-mix post-voiceover
- `company/Ecosistemi/03-CONTENT-FACTORY/Agenti/CF-R2-A07-voiceover.md`
- `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` §5

*Fonte: dossier 03 §5 · Aggiornato: 2026-06-11*
