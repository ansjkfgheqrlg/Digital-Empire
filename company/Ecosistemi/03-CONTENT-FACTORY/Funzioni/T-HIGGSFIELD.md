> Fonte: PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md sez. 5 (registry engine — higgsfield)

# T-HIGGSFIELD — Engine Higgsfield (UGC Video, Image 4K, Motion, Soul ID)

> Layer engine condiviso · Livello: L4 · Usato da: CF-R2 primariamente
> Fonte: dossier 03 §5, §4b.
> Ecosistema: `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md`

---

## Identità engine

| Campo | Valore |
|---|---|
| Engine ID | higgsfield |
| Capability servite | image-4k, video-ugc, motion, soul-id, product-shoot |
| Stato | DA COLLEGARE (skill portabili da CF Exponium — port di `hf-studio/`) |
| Launcher | port parametrizzato di `hf-studio/` da repo CF Exponium |
| Fallback | nessuno (per video-ugc/motion; se non disponibile → blocco esplicito) |
| Tier modello owner | haiku (per CF-R2-A02/A03/A04) |

---

## Contratto engine (non negoziabile — pattern §5 del dossier)

| Operazione | Implementazione | Descrizione |
|---|---|---|
| `generate(job)` | chiamata API Higgsfield con parametri dal brief (soul_id, prompt, aspect) | Genera immagine 4K o video motion |
| `check()` | ping API Higgsfield con API key dal vault — ritorna `{connected: true/false, crediti_rimanenti: N}` | Health probe pre-render |
| `status(job_id)` | polling status job asincrono Higgsfield | Attesa completamento render |
| `estimate(job)` | `{crediti: N, tempo_stimato_sec: M}` basato su tipo (image vs motion) e durata | Obbligatorio PRIMA di qualsiasi render reale |

---

## Capability e workflow di utilizzo

### soul-id (CF-R2-A02-soul-curator)
- Crea e mantiene il personaggio/avatar ricorrente per ogni brand (`brand_kit.soul_id`).
- Prodotto: `soul_id` Higgsfield per brand slug, salvato in `brands/<slug>/brand-kit.json.soul_id`.
- Vincolo: un solo soul-id per brand (coerenza del personaggio nel tempo).

### image-4k (CF-R2-A03-image-operator)
- Input: prompt ultra-specifico da CF-R4-A03 (composizione, luce, stile, soggetto, sfondo).
- Output: immagine 4K in `orders/<id>/03-design/images/`.
- Usato da: WF-CAROSELLO ramo A (slide image), WF-THUMB ramo B.

### motion / video-ugc (CF-R2-A04-motion-operator)
- Input: soul_id del brand + image-4k come base + parametri motion (durata, tipo movimento).
- Output: video `.mp4` grezzo → CF-R2-A06 (ffmpeg: concat, subtitle, audio, crop).
- Nota: IL RENDER PIU' COSTOSO → `estimate()` e approvazione CF-SENT-cost obbligatori.

### product-shoot
- Fotografia prodotto AI: sfondo bianco/lifestyle, angolazioni multiple.
- Usato da: 05-MB e-commerce, clienti agency con prodotto fisico.

---

## Regole di routing

1. Higgsfield è l'engine primario per `image-4k`, `video-ugc`, `motion`, `soul-id`.
2. Se `check()` fallisce (API non raggiungibile, crediti esauriti):
   - `image-4k`: fallback a gemini-img (manuale oggi) o blocco esplicito.
   - `video-ugc` / `motion`: **blocco esplicito** — nessun fallback automatico.
   - Alert al Conductor e al committente con stima crediti necessari.
3. MAI render reale senza `estimate()` pre-approvato da CF-SENT-cost (exit-2 se sfora).
4. MAI modificare il soul-id di un brand senza esplicita richiesta nel brief.

---

## Note di port da CF Exponium

Il repository CF Exponium contiene `hf-studio/` con le chiamate API Higgsfield
parametrizzate per il brand Exponium. Il port richiede:
1. Sostituire ogni riferimento hard-coded a brand Exponium con `brand_kit.slug` come parametro.
2. Il `soul_id` di Marco (Exponium) NON viene portato — ogni brand CF-DE ha il proprio.
3. Aggiungere `estimate()` se non presente (costo per capability dal pricing Higgsfield).
4. Consultare il repo originale, **mai modificarlo**.

---

## Connessioni

- `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md` — registry engine §5
- `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/Produzione-Video/README.md` — reparto owner
- `company/Ecosistemi/03-CONTENT-FACTORY/Agenti/CF-R2-A02-soul-curator.md`
- `company/Ecosistemi/03-CONTENT-FACTORY/Agenti/CF-R2-A08-render-queue.md`
- `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` §5, §4b

*Fonte: dossier 03 §5, §4b · Aggiornato: 2026-06-11*
