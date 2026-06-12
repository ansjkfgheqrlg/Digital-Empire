> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 4.2

# WF-YT-CHANNEL-LAUNCH — Setup canale + brand_kit

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** YT-Strategia · **Fase:** 1 — Ricerca/Strategia
**Owner gate:** `mb-conductor` (ok umano obbligatorio) · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Scopo

Costruire il brand_kit completo di un canale YouTube e creare il canale su YouTube.
Questo workflow si attiva SOLO dopo WF-YT-NICHE con scheda niche approvata (gate upstream).
Il brand_kit è il contratto di identità del canale: ogni video, clip e thumbnail prodotto da
Content-Factory deve rispettarlo.

## Input

| Campo | Fonte |
|---|---|
| Scheda niche approvata (output WF-YT-NICHE) | mb-yt-strategy-coord |
| Pattern stile visual/TTS `[da F-MB1]` | Intelligence / wiki `sources/` |
| Account YouTube DE | Credenziali in custodia PLATFORM (NON in git) |

## Processo (step interni)

1. `mb-yt-brandkit-builder`: definisce nome canale, persona (narratore AI), voce TTS (provider, voice ID, velocità, tono)
2. `mb-yt-brandkit-builder`: definisce palette colori, font canale, stile visual (animazioni, B-roll, avatar se presente)
3. `mb-yt-brandkit-builder`: crea template thumbnail (dimensioni, posizione testo, sfondo, stile immagine)
4. `mb-yt-strategy-coord`: compila il brand_kit YAML finale
5. `mb-yt-strategy-coord`: presenta brand_kit a mb-conductor → **ok umano obbligatorio**
6. Post-approvazione: creazione canale YouTube (nome, descrizione, art di canale → ordinati a CF)
7. Salvataggio brand_kit in `mb/yt/<canale-slug>/brand_kit.yaml`

## brand_kit canale (schema)

```yaml
canale_slug: ""
nome_canale: ""
lingua: "it | en"
persona:
  nome_narratore: ""
  tts_provider: ""       # es. ElevenLabs, Google TTS
  tts_voice_id: ""
  velocita: 1.0
  tono: "neutro | caldo | autorevole"
palette:
  primario: "#XXXXXX"
  secondario: "#XXXXXX"
  sfondo: "#XXXXXX"
visual:
  stile: "animazione_2d | b_roll | avatar_ai | mixed"
  template_thumbnail: ""  # path reference in CF
  font_titolo: ""
niche: ""
keyword_primaria: ""
angolo_differenziante: ""
approvazione_umana: true
data_creazione: "YYYY-MM-DD"
```

## Acceptance criteria

- brand_kit compilato in ogni campo obbligatorio (nessun placeholder)
- Ok umano esplicito da mb-conductor prima di creare il canale
- Canale creato con art di canale, descrizione ottimizzata, link social (se previsti)
- brand_kit salvato in `mb/yt/<canale-slug>/brand_kit.yaml` + log wiki

## Multi-canale

Per ogni nuovo canale si esegue WF-YT-CHANNEL-LAUNCH da zero con brand_kit distinto.
Regola: mai due canali con stessa niche/persona/palette (rischio spam network YouTube, dossier §4.5).
Un canale nuovo si apre SOLO quando il precedente ha gate stabili (≥10 video, ≥80% gate verdi — F-MB5).
