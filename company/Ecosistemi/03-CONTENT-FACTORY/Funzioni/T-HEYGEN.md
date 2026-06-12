> Fonte: PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md sez. 5 (registry engine — heygen)

# T-HEYGEN — Engine HeyGen (Avatar, Talking-Head, Spokesperson)

> Layer engine condiviso · Livello: L4 · Usato da: CF-R2 (WF-VIDEO-AVATAR)
> Fonte: dossier 03 §5, §4b.
> Ecosistema: `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md`

---

## Identità engine

| Campo | Valore |
|---|---|
| Engine ID | heygen |
| Capability servite | avatar, talking-head, spokesperson |
| Stato | PRONTO, da collegare (scaffold CF Exponium riusabile — port di `heygen-studio/`) |
| Launcher | port parametrizzato di `heygen-studio/` da repo CF Exponium |
| Fallback | nessuno (per avatar/talking-head — blocco esplicito se non disponibile) |
| Tier modello owner | haiku (CF-R2-A05-avatar-operator) |

---

## Contratto engine (non negoziabile — pattern §5 del dossier)

| Operazione | Implementazione | Descrizione |
|---|---|---|
| `generate(job)` | chiamata API HeyGen: avatar_id + script + lingua + voice_id | Render video talking-head |
| `check()` | ping API HeyGen con chiave dal vault + `{connected, crediti_rimanenti}` | Health probe obbligatorio pre-render |
| `status(video_id)` | polling HeyGen job status (asincrono) | Attesa completamento |
| `estimate(job)` | stima crediti per durata video (minuti × costo per minuto) | Obbligatorio per T-render-queue |

---

## Capability e workflow di utilizzo (WF-VIDEO-AVATAR)

### avatar / talking-head (CF-R2-A05-avatar-operator)

**Pipeline completa:**
```
script.md (da CF-R3/WF-SCRIPT) + brand_kit (voice, lingua, persona)
  → selezione avatar_id:
      - se brand ha avatar HeyGen registrato in brand-kit.json → usa quello
      - se primo video per brand → brand_owner approva avatar da lista HeyGen
        → avatar_id salvato in brand-kit.json.heygen_avatar_id
  → selezione voice_id:
      - voice coerente con brand_kit.voice.tono (es. "diretto, italiano")
      - salvata in brand-kit.json.heygen_voice_id
  → estimate(job) → CF-SENT-cost approva/blocca
  → render HeyGen: output .mp4 grezzo talking-head
  → CF-R2-A06 (ffmpeg): aggiunge intro/outro brand, subtitle burn-in, loudness -14 LUFS
  → gate GATE-FORMATO + GATE-BRAND
```

### spokesperson (uso agency)
- Stesso flusso ma con avatar approvato dal cliente (brand_kit del cliente).
- Il cliente fornisce: avatar_id HeyGen proprietario o sceglie da libreria approvata.

---

## Regole di routing

1. HeyGen è l'unico engine per `avatar` e `talking-head`.
2. Se `check()` fallisce: blocco esplicito al lead, alert al committente, stima costi
   per riattivazione — mai sostituzione silenziosa con altro engine.
3. `estimate()` obbligatorio: render HeyGen consuma crediti significativi per video lunghi.
4. Avatar e voice per brand sono **invarianti del brand-kit**: non cambiare senza brief
   esplicito e approvazione (coerenza speaking persona nel tempo).

---

## Note di port da CF Exponium

- CF Exponium ha `heygen-studio/` con l'avatar di Marco hard-coded.
- Il port CF-DE parametrizza: `avatar_id = brand_kit.heygen_avatar_id`,
  `voice_id = brand_kit.heygen_voice_id`, `lingua = brand_kit.voice.lingua`.
- L'avatar di Marco NON viene usato per i brand DE — ogni brand ha il suo.
- Consultare il repo originale per la struttura API, **mai modificarlo**.

---

## Connessioni

- `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md` — registry engine §5
- `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/Produzione-Video/README.md`
- `company/Ecosistemi/03-CONTENT-FACTORY/Agenti/CF-R2-A05-avatar-operator.md`
- `company/Ecosistemi/03-CONTENT-FACTORY/Agenti/CF-R2-A08-render-queue.md`
- `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` §5, §4b

*Fonte: dossier 03 §5 · Aggiornato: 2026-06-11*
