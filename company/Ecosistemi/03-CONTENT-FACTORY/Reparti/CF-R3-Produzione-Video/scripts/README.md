---
Type: SCRIPTS
Status: Active
Tags: #scripts #CF-R3 #video #wrapper #ffmpeg #higgsfield #heygen #stima
Created: 2026-06-19
Last updated: 2026-06-19
---

# Scripts — CF-R3 Produzione Video

> **ADR-003 critico:** i wrapper di hf-studio e heygen-studio non modificano i file originali.
> I wrapper aggiungono il layer di parametrizzazione brand_kit; l'originale resta intatto.

---

## Wrapper asset attivi (ADR-003 — non modificare gli originali)

### `higgsfield-suite` (wrapper hf-studio)

**Scopo:** Port parametrizzato di `hf-studio` CF Exponium. Espone le capability
`image-4k`, `motion`, `soul-id` con parametri brand_kit invece di parametri Exponium
hard-coded.

**Contrato esposto:**
```
generate(job)   → avvia render Higgsfield con parametri brand_kit tradotti in formato nativo
check()         → verifica connessione Higgsfield API (OK / ERRORE con motivo)
status(job_id)  → polling stato render (pending / running / done / failed)
estimate(job)   → stima crediti prima di generate(); obbligatorio prima di ogni chiamata
```

**Parametri aggiuntivi rispetto all'originale:**
- `brand_kit_path` → sostituisce i parametri Exponium con quelli del brand corrente
- `brand_slug` → usato per routing soul-id in `cf/souls`
- `output_dir` → `orders/<id>/03-design/` invece di path Exponium fisso

**[WRAPPA] port parametrizzato di hf-studio — originale non modificato**

---

### `heygen-generate` (wrapper heygen-studio)

**Scopo:** Port parametrizzato di `heygen-studio` CF Exponium. Espone la capability
`avatar` con mapping `brand_kit.voice.tono → avatar_id` invece di avatar Exponium fisso.

**Contratto esposto:**
```
generate(job)   → avvia render HeyGen con avatar e voice_id selezionati da brand_kit
check()         → verifica connessione HeyGen API (OK / ERRORE con motivo)
status(video_id)→ polling stato render HeyGen (pending / processing / completed / failed)
estimate(job)   → stima crediti prima di generate(); obbligatorio
```

**Parametri aggiuntivi:**
- `voice_tono` → mappa a `avatar_id` e `voice_id` HeyGen via tabella routing brand
- `brand_kit_path` → per verifica conformità voice al brand (parole_vietate, tono)
- `output_dir` → `orders/<id>/03-design/` invece di path Exponium fisso

**[WRAPPA] port parametrizzato di heygen-studio — originale non modificato**

---

## Script target CF-R3 (da costruire in CF-F6 quando Higgsfield/HeyGen collegati)

### `render-estimator`

**Scopo:** Calcola la stima crediti per un intero ordine video prima del dry-run formale.
Utile per CF-R3-COORD per pre-valutare la fattibilità prima di avviare CF-R3-QUEUE.

**Input:** `order.json` + `tipo_workflow`
**Output:** stima per engine, totale, margine vs budget

**Logica:** per ogni engine call del workflow → chiama `<engine>.estimate(job)`;
aggrega; se stima non disponibile → usa tabella crediti storici medi (aggiornata da CF-R3-LEARN).

---

### `format-gate-check`

**Scopo:** Esegue GATE-FORMATO su un file video in modo autonomo, senza attivare
l'intero flusso di CF-R3-QA. Utile per verifiche rapide post-montaggio.

**Input:** path file video + canale_target
**Output:** JSON con esito per ogni criterio (aspect, durata, codec, loudness, sottotitoli)

**Dipendenza:** `ffprobe` (incluso nella distribuzione ffmpeg locale)

**Esempio di output:**
```json
{
  "file": "orders/CF-2026-0055/04-render/video/video-001.mp4",
  "canale": "instagram-reel",
  "aspect_ratio": { "atteso": "9:16", "rilevato": "1080x1920", "esito": "PASS" },
  "durata_s": { "limite": 60, "rilevata": 44.8, "esito": "PASS" },
  "codec": { "atteso": "h264|h265", "rilevato": "h264", "esito": "PASS" },
  "loudness_lufs": { "target": -14, "rilevato": -14.1, "tolleranza": 2, "esito": "PASS" },
  "verdetto_finale": "PASS"
}
```

---

### `batch-dispatcher`

**Scopo:** Distribuisce i job di un batch sugli engine disponibili rispettando il cap
paralleli dichiarato nel budget e la sequenza di priorità (deadline → revenue → interno).

**Input:** `batch-intent.json` approvato da CF-SENT-COST
**Output:** N istanze job avviate in parallelo; registro aggiornato in `cf/render-queue`

**Logica:**
- Legge `cap_paralleli` dal budget tier
- Avvia i primi N job
- Quando un job completa → avvia il successivo dalla coda
- Tiene contatore `{avviati, completati, falliti}`; a 3 falliti → escalation

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — contratto engine e regola di estensione
- [[WF-VIDEO-UGC]] · `workflow/WF-VIDEO-UGC.md` — usa higgsfield-suite
- [[WF-VIDEO-AVATAR]] · `workflow/WF-VIDEO-AVATAR.md` — usa heygen-generate
- [[cf-r3-queue]] · `agenti/cf-r3-queue.md` — usa render-estimator per stima pre-dry-run
