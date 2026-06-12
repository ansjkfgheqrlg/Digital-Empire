> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 4.2 + 4.1 (step 1)

# WF-YT-NICHE — Scelta e validazione niche YouTube

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** YT-Strategia · **Fase:** 1 — Ricerca/Strategia
**Owner gate:** `mb-yt-strategy-coord` · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Scopo

Scegliere una niche YouTube valida per un canale automatizzato (voiceover TTS + visual AI +
script), validarla con una scorecard misurabile, e consegnare la scheda niche approvata come
pre-requisito per WF-YT-CHANNEL-LAUNCH. Non si lancia un canale senza niche validata.

## Dipendenza critica — F-MB1

Questo workflow è **informato dai dossier F-MB1** (ingestione Empire Studio di
`@Legamidiamore` e `@dosementale`). I parametri segnati `[da F-MB1]` si fissano SOLO
dopo quella ingestione. Eseguire WF-YT-NICHE prima di F-MB1 è possibile solo per ricerca
esplorativa — la scheda finale non si approva senza i pattern dei canali riferimento.

## Input

| Campo | Fonte | Note |
|---|---|---|
| Dossier ingestione F-MB1 | Intelligence / Empire Studio | Niche/angolo, RPM stimato `[da F-MB1]`, producibilità AI dei canali riferimento |
| Criteri di selezione | mb-conductor | RPM minimo, competizione massima accettabile, lingua target |
| Catalogo canali esistenti | `mb/yt/patterns` | Anti-duplicazione: niche/angolo mai usati prima |

## Processo (step interni)

1. `mb-yt-niche-scout`: scansiona categorie YouTube con potenziale TTS/AI → lista preliminare 10 niche
2. `mb-yt-keyword-miner`: keyword research per ogni niche (volume, competition, CPM, RPM stimato)
3. `mb-yt-competitor-mapper`: per ogni niche top-3 → analisi competitor (post F-MB1: frame reali)
4. `mb-yt-strategy-coord`: compila scorecard per ogni niche candidata
5. `mb-yt-strategy-coord`: presenta le top-3 a mb-conductor + ok umano per la niche scelta

## Scorecard di validazione niche (tutti i criteri misurabili)

| Criterio | Soglia | Fonte dato |
|---|---|---|
| Volume ricerca keyword primaria | > soglia minima `[da F-MB1: volume canali riferimento]` | YouTube suggest/tool |
| Competizione canali (n. canali >10k sub nella niche) | < soglia `[da F-MB1]` | Ricerca manuale |
| RPM stimato nella niche | > €1 (mercati IT/EN) | AdSense benchmarks + `[da F-MB1]` |
| Producibilità AI (solo TTS + visual AI — zero riprese live) | Sì / No | Analisi format canali competitor |
| Rischio policy YouTube | Basso / Medio / Alto | Checklist: reused content, disclosure, spam |
| Unicità rispetto ai canali DE esistenti | No sovrapposizione | `mb/yt/patterns` |

## Output

```json
{
  "niche": "<nome niche>",
  "lingua": "it | en",
  "keyword_primaria": "",
  "scorecard": {
    "volume": "...",
    "competizione": "...",
    "rpm_stimato": "€...",
    "producibilita_ai": true,
    "rischio_policy": "basso",
    "unicita": true
  },
  "angolo_differenziante": "",
  "note_competitor": "",
  "stato": "APPROVATA | RIFIUTATA",
  "approvazione_umana": true
}
```

## Acceptance criteria

- Scorecard compilata con dati verificabili (no stime inventate)
- Approvazione esplicita di mb-conductor + ok umano
- Scheda salvata in `mb/yt/strategy/niche-<slug>.json` + log wiki
