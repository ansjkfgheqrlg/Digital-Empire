> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 2.1 + 4.2

# Reparto L2 — YT-Produzione (interfaccia CF) (`MB-YT`)

**Ecosistema:** 05-MULTI-BUSINESS · **Codice:** MB-YT-PROD · **Priorità:** ALTA
**Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Missione

Questo reparto NON produce contenuti: è l'interfaccia tra Multi-Business e Content-Factory (03).
Compila il brief-ordine video, lo trasmette via contratto Bus, e valida la consegna rispettando
i gate #2 (Audio) e #3 (Visual). Il Gate #1 Script è proprietà di YT-Ottimizzazione (mb-yt-opt-coord).

## Workflow L3 di competenza

| Workflow | Fase pipeline | Output |
|---|---|---|
| `WF-YT-VIDEO-ORDER` | 2 — Produzione (handoff CF) | Contratto a CF: `{brand_kit, formato: video_long/short, quantità, spec: durata/TTS/stile_visual, deadline}` → consegna: script + audio + video + thumbnail; validazione contro acceptance criteria |

**Passi 5-9 della pipeline (eseguiti da CF, validati qui):**
- Step 5: research argomento video (CF)
- Step 6: script — Gate #1 Script (mb-yt-opt-coord + Brand-Voice Sentinel)
- Step 7: voiceover TTS — Gate #2 Audio (mb-yt-handoff-validator)
- Step 8: visual AI/B-roll/avatar — Gate #3 Visual (mb-yt-handoff-validator + Quality Sentinel)
- Step 9: thumbnail (con gate #3)

## Funzioni L4

| Team | Responsabilità |
|---|---|
| T-brief-compiler | Compila il brief-ordine video per CF: brand_kit + formato + spec tecniche + deadline |
| T-handoff-validator | Valida la consegna CF contro gli acceptance criteria del contratto Bus |
| T-asset-receiver | Riceve e archivia gli asset (script/audio/video/thumbnail) nei namespace `mb/yt/<canale>/` |

## Agenti L5 assegnati

- `mb-yt-brief-compiler` (worker, Sonnet) — compila il contratto ordine video
- `mb-yt-handoff-validator` (worker, Sonnet) — gate #2 Audio e #3 Visual

## Gate di competenza

| Gate | Criteri chiave | Chi blocca |
|---|---|---|
| **#2 Audio** | Zero artefatti/glitch; pronuncia corretta; loudness -14 LUFS; durata audio = script ±5% | mb-yt-handoff-validator |
| **#3 Visual** | ≥1080p; zero frame neri/watermark; coerenza brand_kit; sync audio-video; thumbnail leggibile 120px | mb-yt-handoff-validator + Quality Sentinel |

Gate rosso → pacchetto torna a CF con report di failure (ReasoningBank, pattern 5).

## Dry-run obbligatorio

Prima di ogni ordine a CF: stima costo → Cost-Sentinel verde. Zero ordini senza approvazione
budget (pattern #3 — dry-run default; OUT OF SCOPE del Piano Maestro: niente spese API senza ok).

## KPI di reparto

- % consegne CF che passano il gate al primo colpo: obiettivo ≥ 80% (baseline post F-MB4)
- Lead time ordine → consegna validata: ≤ deadline contrattuale
- Zero override manuali di gate senza decisione di mb-conductor
