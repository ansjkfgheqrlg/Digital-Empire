---
Type: REPARTO
Status: Active
Tags: #reparto #content-factory #video #produzione #CF-R3 #higgsfield #heygen #ffmpeg
Created: 2026-06-19
Last updated: 2026-06-19
---

# CF-R3 — Produzione Video

> **Ecosistema:** 03-CONTENT-FACTORY · **Area:** Produzione · **Livello:** L2 Reparto
> **Dossier:** `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R3`
> **Standard:** CF-grade (ADR-007) · **Wrappa asset ATTIVI: hf-studio + heygen-studio (ADR-003)**

---

## Missione

Produrre video pronti alla pubblicazione: UGC via Higgsfield (soul-id ricorrente → immagini
4K → motion), avatar/talking-head via HeyGen, short-form montati con ffmpeg+TTS.

Il reparto eredita la pipeline CF Exponium (`hf-studio`, `heygen-studio`) e la parametrizza
per multi-tenant: `brand_kit` e `icp` sono gli unici input fissi; tutto il resto è configurato
per il brand dell'ordine. Nessun video prodotto senza `brief.json` da CF-R1 e `brand_kit`
validato da CF-R2.

---

## Cosa fa il reparto

1. **Gestisce i soul-id** per brand — ogni brand ha il suo personaggio Higgsfield ricorrente
   (CF-R3-SOUL), garantendo coerenza visiva tra video diversi dello stesso brand.
2. **Genera immagini 4K** via Higgsfield, parametrizzate per la palette e lo stile del brand_kit.
3. **Converte immagini in video motion** via Higgsfield (image→video).
4. **Rende avatar HeyGen** a partire da script CF-R4, scegliendo l'avatar coerente con brand_kit.voice.
5. **Produce voiceover TTS** (edge-tts/ElevenLabs) calibrato sul tono del brand_kit.
6. **Monta il video finale** con ffmpeg: cut, crop multi-formato (9:16/1:1/16:9), subtitle-burn,
   audio-mix, loudness normalizzazione LUFS.
7. **Gestisce la coda render** — stima crediti via `estimate()` PRIMA di ogni render; BLOCCA
   se sfora `budget.crediti_engine`; CF-SENT-COST approva il totale.
8. **Apprende dai risultati** — correla tipo video/soul/durata con engagement reale.

## Cosa NON fa

- Non scrive script: quello è CF-R4 (WF-SCRIPT); riceve script pronti.
- Non esegue gate QA finale: quello è CF-R6 (indipendente dalla produzione).
- Non pubblica: quello è CF-R7 (Pubblicazione & Distribuzione).
- Non modifica `hf-studio` né `heygen-studio`: li wrappa con parametrizzazione brand_kit (ADR-003).
- Non produce contenuto senza budget pre-approvato: CF-SENT-COST blocca ogni render non approvato.
- Non esegue render reale senza dry-run previamente completato (Art.4.3).

---

## Roster del reparto (10 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `CF-R3-COORD` | Coordinatore Produzione Video | `agenti/cf-r3-coord.md` | coordinator | sonnet | Orchestra le 4 pipeline; sceglie engine via capability; riporta a L1-PROD |
| `CF-R3-QA` | Verificatore Gate Video | `agenti/cf-r3-qa.md` | verifier | sonnet | GATE-FORMATO + GATE-BRAND video; BLOCCA e non suggerisce |
| `CF-R3-SOUL` | Soul-ID Curator | `agenti/cf-r3-soul.md` | worker | haiku | Gestisce soul-id Higgsfield per brand; ricorrenza personaggio cross-video |
| `CF-R3-IMG` | Image Operator (4K) | `agenti/cf-r3-img.md` | worker | haiku | Generazione immagini 4K via Higgsfield [WRAPPA hf-studio] |
| `CF-R3-MOTION` | Motion Operator | `agenti/cf-r3-motion.md` | worker | haiku | Image→video motion via Higgsfield; durata e intensità per tipo contenuto |
| `CF-R3-AVATAR` | Avatar Operator | `agenti/cf-r3-avatar.md` | worker | haiku | Render HeyGen avatar [WRAPPA heygen-studio]; coerenza con brand_kit.voice |
| `CF-R3-VO` | Voiceover Operator | `agenti/cf-r3-vo.md` | worker | haiku | TTS voiceover edge-tts/ElevenLabs calibrato su brand_kit.voice |
| `CF-R3-EDIT` | Editor ffmpeg | `agenti/cf-r3-edit.md` | worker | haiku | Montaggio ffmpeg: cut/crop/subtitle-burn/audio-mix/loudness |
| `CF-R3-QUEUE` | Render Queue Manager | `agenti/cf-r3-queue.md` | worker | wasm/haiku | Coda render; stima crediti; BLOCCO pre-render se sfora budget |
| `CF-R3-LEARN` | Video Performance Analyst | `agenti/cf-r3-learn.md` | worker | sonnet | Correla tipo video/soul/durata con engagement; pattern in `cf/patterns` |

---

## Workflow del reparto (4 workflow CF-grade)

| ID | File | Scopo | Dry-run | Gate |
|---|---|---|---|---|
| **WF-VIDEO-UGC** | `workflow/WF-VIDEO-UGC.md` | Pipeline UGC completa: soul→img 4K→motion→VO→EDIT | Produce `ugc-intent.json` a costo zero | CF-SENT-COST pre-render; CF-R3-QA GATE-FORMATO+BRAND |
| **WF-VIDEO-AVATAR** | `workflow/WF-VIDEO-AVATAR.md` | Pipeline avatar HeyGen: script→AVATAR→EDIT | Produce `avatar-intent.json` a costo zero | CF-SENT-COST pre-render; CF-R3-QA GATE-FORMATO+BRAND |
| **WF-SHORTFORM** | `workflow/WF-SHORTFORM.md` | Montaggio reel/TikTok/Shorts da asset esistenti, ffmpeg locale | Costo zero (ffmpeg locale) | GATE-FORMATO ≤60s/9:16/loudness |
| **WF-BATCH-VIDEO** | `workflow/WF-BATCH-VIDEO.md` | Batch ≥5 video swarm mesh; approvazione totale pre-render | Stima totale batch → CF-SENT-COST approva PRIMA | CF-SENT-COST TOTALE; 3 fail → escalation |

---

## Namespace memoria

| Namespace | Contenuto |
|---|---|
| `cf/video` | Stato render video per ordine, engine_id, crediti consumati |
| `cf/souls` | Soul-id Higgsfield per brand (coerenza cross-ordine) |
| `cf/render-queue` | Coda render attiva, stime, approvazioni CF-SENT-COST |

---

## KPI del reparto

| KPI | Owner | Definizione |
|---|---|---|
| Video prodotti / ciclo | CF-R3-COORD | N. video con gate verde consegnati nel periodo; [DM] baseline |
| Costo per video per engine | CF-R3-QUEUE | Crediti consumati / video per Higgsfield / HeyGen / ffmpeg; [DM] baseline |
| GATE-FORMATO first-pass rate | CF-R3-QA | % video che superano GATE-FORMATO al primo giro; [DM] baseline |
| GATE-BRAND pass rate | CF-R3-QA | % video con soul/palette corretti al primo giro; [DM] baseline |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | CF-R1 (CF-D-DISPATCH) | `brief.json` con angle, hook type, durata stimata, canali |
| ← riceve da | CF-R4 (WF-SCRIPT) | `script.md` con hook nei 3s e CTA per WF-VIDEO-AVATAR |
| ← riceve da | CF-R2 | `brand_kit` validato con soul_id, palette, voice tone |
| ← riceve da | CF-SENT-COST | Approvazione budget pre-render (o BLOCCO) |
| → consegna a | CF-R6 (QA & Gate) | Video montato in `orders/<id>/04-render/video/` per GATE-FORMATO+BRAND |
| → consegna a | CF-R7 (Pubblicazione) | Video con gate verdi in state.json per publicazione |
| → alimenta | `cf/patterns` | Pattern tipo-video/soul/durata vs engagement (CF-R3-LEARN) |

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Dry-run obbligatorio Art.4.3 → ogni workflow produce `*-intent.json` a costo zero prima del render reale
- ADR-003: hf-studio e heygen-studio si wrappano, non si modificano

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R3`
- [[CF-R1-Strategia-Brief]] · fornitore brief.json e brief video
- [[CF-R6-QA-Gate]] · gate indipendente su ogni video prodotto
- [[WF-VIDEO-UGC]] · `workflow/WF-VIDEO-UGC.md`
- [[WF-VIDEO-AVATAR]] · `workflow/WF-VIDEO-AVATAR.md`
