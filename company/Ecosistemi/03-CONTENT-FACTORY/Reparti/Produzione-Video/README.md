# CF-R2 — PRODUZIONE VIDEO

> Reparto L2 di 03-CONTENT-FACTORY · Coordinatore: `CF-R2-A01-video-lead`
> Fonte: dossier 03 §2 (CF-R2), §4b, §5.

---

## Cosa fa

Produce **video pronti alla pubblicazione**: UGC (Higgsfield), avatar/talking-head
(HeyGen), short-form montati (ffmpeg + TTS). Eredita la pipeline creativa di CF Exponium —
Soul ID → Image 4K → Motion → Montaggio — ma **parametrizzata per brand**: il soul/avatar
ricorrente è quello del `brand_kit` dell'ordine, non un personaggio fisso.

È il reparto più costoso della fabbrica (motori a crediti): per questo OGNI render passa
da T-render-queue (`estimate()` aggregato) e dal CF-SENT-cost PRIMA di consumare crediti.

### Org interna

| Livello | Team | Contenuto |
|---|---|---|
| L3 | **WF-VIDEO-UGC** | pipeline Higgsfield completa: soul-id ricorrente per brand → immagini 4K → motion → montaggio |
| L3 | **WF-VIDEO-AVATAR** | pipeline HeyGen: script → avatar → render, talking-head/spokesperson per brand |
| L3 | **WF-SHORTFORM** | montaggio reel/TikTok/Shorts da asset esistenti: cut, sottotitoli, audio |
| L4 | T-voiceover | TTS (edge-tts gratuito; ElevenLabs solo se brief+budget lo richiedono) |
| L4 | T-subtitle | caption burn-in sincronizzate |
| L4 | T-montaggio | ffmpeg: concat, crop 9:16/1:1/16:9, loudness -14 LUFS |
| L4 | T-render-queue | coda render + cost guard locale (eredita D3 di CF Exponium) |

### Agenti L5 (schede in `../../Agenti/`)

| ID | Ruolo | Tier |
|---|---|---|
| CF-R2-A01-video-lead | coordina le 3 pipeline, sceglie engine via capability | sonnet |
| CF-R2-A02-soul-curator | Soul ID / personaggi ricorrenti per brand (Higgsfield) | haiku |
| CF-R2-A03-image-operator | generazione immagini 4K (Higgsfield) | haiku |
| CF-R2-A04-motion-operator | image→video motion (Higgsfield) | haiku |
| CF-R2-A05-avatar-operator | render HeyGen avatar/talking-head | haiku |
| CF-R2-A06-editor-ffmpeg | montaggio: cut, crop, subtitle, audio | haiku |
| CF-R2-A07-voiceover | TTS voiceover per brand voice | haiku |
| CF-R2-A08-render-queue | coda render, stima costi, cost guard locale | wasm/haiku |

---

## Come si collega

**Inbound:**
- CF-R1 → `brief.json` approvato; CF-R3/WF-SCRIPT → script video di base.
- 04-MARKETING → blocco APSOC validato quando il video è di conversione (VSL, ad video).
- Layer engine (`../../Funzioni/`): T-HIGGSFIELD, T-HEYGEN, T-FFMPEG, T-TTS — contratto
  `generate/check/status/estimate`.

**Outbound:**
- Video montato + sottotitoli → CF-QA-A01 (GATE-FORMATO → GATE-BRAND → GATE-COPY) →
  CF-R5 (delivery/publish) via handoff contract con acceptance criteria.
- Stime costi e consumi → CF-SENT-cost + `trace.jsonl`.

**Routing engine (funzione pura, dal registry §5 del dossier):**
`ugc/motion/image-4k/soul-id → higgsfield` · `avatar/talking-head → heygen` ·
`voiceover → tts` · `montaggio/cut/crop/subtitle → ffmpeg`. MAI silenziosamente un
engine diverso da quello loggato in trace.jsonl.

---

## 🧠 Come si ATTIVA e RAGIONA

**Attivazione:** SOLO su brief + script approvati (mai senza GATE precedente). I worker
L5 vengono spawnati on-demand per la durata dell'ordine.

**Logica di ragionamento:**
1. CF-R2-A01 risolve la capability richiesta dal brief → engine dal registry.
2. **Dry-run default**: la pipeline gira producendo `*.intent.json` per ogni chiamata
   engine (prompt, parametri, costo stimato) senza consumare crediti — identico al
   "dry mode" di CF Exponium.
3. T-render-queue aggrega gli `estimate()` → confronto con `budget.crediti_engine`
   dell'ordine → CF-SENT-cost approva o **blocca con exit esplicito** (mai sforamento parziale).
4. Solo dopo l'ok: render reale. Pipeline UGC: soul-id(brand) → image-4k → motion →
   ffmpeg. Pipeline avatar: script → heygen render → ffmpeg (intro/outro, subtitle).
5. Gate di uscita verso QA: GATE-FORMATO (durata, aspect, codec, loudness),
   poi GATE-BRAND (soul coerente col brand, palette), poi GATE-COPY (hook nei primi 3s, CTA).

**Failure handling:** engine `check()` fallito → fallback dal registry se esiste,
altrimenti errore esplicito al lead (mai sostituzioni silenziose); render fallito 2 volte →
escalation CF-R2-A01 + `cf/failures`; budget insufficiente → l'ordine torna al committente
via CF-A00 con stima reale.

## KPI del reparto

| KPI | Direzione |
|---|---|
| Costo crediti per video consegnato (per formato e brand) | ↓ |
| First-pass rate sui 3 gate | ↑ |
| Scarto stima vs consumo reale di T-render-queue | ↓ |
| Lead time script→video consegnato | ↓ |

*Fonte: dossier 03 §2, §4b, §5 · Aggiornato: 2026-06-11*
